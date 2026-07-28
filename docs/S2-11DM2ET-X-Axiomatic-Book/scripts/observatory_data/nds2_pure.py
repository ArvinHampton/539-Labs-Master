"""
Pure-Python NDS2 client for public GWOSC (nds.gwosc.org).

No gwpy, no nds2 C bindings, no MSVC. Wire format reverse-engineered from
the official nds2-client (daq_send / nds2_request_data / daq_recv_block).

Protocol notes
--------------
* Commands are ASCII lines ending in ``;\\n`` (except bare ``authorize\\n``).
* Each command reply is a 4-digit decimal status (``0000`` = OK,
  ``0019`` = DAQD_COMMAND_SYNTAX).
* ``get-data start end stride {channel};`` then streams:
  - 8 hex digits writer id
  - uint32 offline flag (network order)
  - data / reconfigure blocks (uint32 length + 16-byte header + payload)
"""
from __future__ import annotations

import socket
import struct
from dataclasses import dataclass
from typing import Iterable

import numpy as np

DAQD_OK = 0
DAQD_COMMAND_SYNTAX = 0x19
DAQD_SASL = 0x18
HEADER_LEN = 16
RECONFIG_SECONDS = 0xFFFFFFFF

# NDS1-compatible data_type codes used by public GWOSC aux (see daqc.h)
_DTYPE_MAP = {
    1: (">i2", 2),  # short
    2: (">i4", 4),  # int32 (also appears as enum INT32)
    4: (">f4", 4),  # float (GWOSC aux uses this)
    8: (">f4", 4),  # FLOAT32 enum
    16: (">f8", 8),  # FLOAT64 enum
}


@dataclass
class NDS2Series:
    channel: str
    start: int
    end: int
    rate: float
    data_type: int
    values: np.ndarray
    host: str
    port: int

    @property
    def dt(self) -> float:
        return 1.0 / self.rate if self.rate > 0 else float("nan")

    @property
    def times(self) -> np.ndarray:
        n = len(self.values)
        return np.arange(n, dtype=np.float64) * self.dt


class NDS2Error(RuntimeError):
    pass


class NDS2Client:
    def __init__(
        self,
        host: str = "nds.gwosc.org",
        port: int = 31200,
        timeout: float = 120.0,
    ) -> None:
        self.host = host
        self.port = port
        self.timeout = timeout
        self._sock: socket.socket | None = None
        self.protocol_version = 0
        self.protocol_revision = 0

    def connect(self) -> None:
        self.close()
        s = socket.create_connection((self.host, self.port), timeout=self.timeout)
        s.settimeout(self.timeout)
        self._sock = s
        # authorize: no semicolon
        code = self._cmd("authorize", semicolon=False)
        if code == DAQD_SASL:
            raise NDS2Error(
                f"Server {self.host} requires SASL/Kerberos auth (not public)."
            )
        if code != DAQD_OK:
            raise NDS2Error(f"authorize failed: status={code}")

        code = self._cmd("server-protocol-version")
        if code == DAQD_OK:
            self.protocol_version = self._read_u32()
        elif code != DAQD_COMMAND_SYNTAX:
            raise NDS2Error(f"server-protocol-version failed: {code}")

        code = self._cmd("server-protocol-revision 6")
        if code == DAQD_COMMAND_SYNTAX:
            code = self._cmd("server-protocol-revision")
        if code == DAQD_OK:
            self.protocol_revision = self._read_u32()

    def close(self) -> None:
        if self._sock is not None:
            try:
                try:
                    self._cmd("quit", semicolon=True)
                except Exception:
                    pass
                self._sock.close()
            except Exception:
                pass
            self._sock = None

    def __enter__(self) -> "NDS2Client":
        self.connect()
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    # -- low level --------------------------------------------------------

    def _sock_req(self) -> socket.socket:
        if self._sock is None:
            raise NDS2Error("not connected")
        return self._sock

    def _recv_exact(self, n: int) -> bytes:
        s = self._sock_req()
        buf = bytearray()
        while len(buf) < n:
            chunk = s.recv(n - len(buf))
            if not chunk:
                raise NDS2Error(f"connection closed while reading {len(buf)}/{n}")
            buf.extend(chunk)
        return bytes(buf)

    def _read_u32(self) -> int:
        return struct.unpack("!I", self._recv_exact(4))[0]

    def _read_f32(self) -> float:
        return struct.unpack("!f", self._recv_exact(4))[0]

    def _cmd(self, command: str, semicolon: bool = True) -> int:
        cmd = command.rstrip("\n")
        if semicolon and not cmd.endswith(";"):
            cmd += ";"
        cmd += "\n"
        self._sock_req().sendall(cmd.encode("ascii"))
        resp = self._recv_exact(4)
        try:
            return int(resp.decode("ascii"))
        except ValueError as e:
            raise NDS2Error(f"bad status bytes {resp!r}") from e

    # -- high level -------------------------------------------------------

    def fetch(
        self,
        channel: str,
        start: int,
        end: int,
        *,
        stride: int | None = None,
        channel_type: str | None = None,
    ) -> NDS2Series:
        """
        Fetch [start, end) GPS seconds for one channel.

        Parameters
        ----------
        channel_type :
            Optional NDS type suffix (``s-trend``, ``m-trend``, ``raw``, …).
            Omit for server default (works for GWOSC O3 AUX channels).
        """
        if end <= start:
            raise ValueError("end must be > start")
        stride = int(stride if stride is not None else (end - start))
        if stride <= 0:
            stride = end - start

        name = channel
        if channel_type:
            name = f"{channel},{channel_type}"

        cmd = f"get-data {int(start)} {int(end)} {int(stride)} {{{name}}}"
        code = self._cmd(cmd)
        if code != DAQD_OK:
            raise NDS2Error(
                f"get-data failed status={code} for {name} "
                f"GPS[{start},{end}) on {self.host}"
            )

        # writer id: 8 hex digits (ASCII)
        _wid = self._recv_exact(8)
        _offline = self._read_u32()

        rate = 0.0
        data_type = 4  # default float (GWOSC aux)
        chunks: list[np.ndarray] = []
        span = float(end - start)

        sock = self._sock_req()
        # After the first data block, use a short timeout to drain optional
        # trailing blocks without hanging.
        first_data = True
        while True:
            if not first_data:
                sock.settimeout(3.0)
            try:
                block_len = self._read_u32()
            except (NDS2Error, TimeoutError, socket.timeout, OSError):
                break
            if block_len == 0:
                break
            seconds = self._read_u32()
            if seconds == RECONFIG_SECONDS:
                self._recv_exact(12)
                payload_len = block_len - HEADER_LEN
                payload = self._recv_exact(max(payload_len, 0))
                if len(payload) >= 24:
                    _status, _offset, dtype_word = struct.unpack(
                        "!III", payload[:12]
                    )
                    rate = struct.unpack("!f", payload[12:16])[0]
                    data_type = dtype_word & 0xFFFF
                continue

            # header remainder: gps, gpsn, seq_num (seconds already read)
            _gps = self._read_u32()
            _gpsn = self._read_u32()
            _seq = self._read_u32()
            data_len = block_len - HEADER_LEN
            raw = self._recv_exact(max(data_len, 0))
            chunks.append(self._decode(raw, data_type))
            first_data = False
            # Offline full-span stride: usually one data block is enough
            if stride >= (end - start) and chunks:
                sock.settimeout(2.0)
                continue  # try drain; break on timeout

        sock.settimeout(self.timeout)

        if not chunks:
            raise NDS2Error(f"no data blocks for {channel} GPS[{start},{end})")

        values = np.concatenate(chunks).astype(np.float64, copy=False)
        if rate <= 0 and len(values) > 0 and span > 0:
            rate = float(len(values)) / span

        return NDS2Series(
            channel=channel,
            start=int(start),
            end=int(end),
            rate=float(rate),
            data_type=int(data_type),
            values=values,
            host=self.host,
            port=self.port,
        )

    @staticmethod
    def _decode(raw: bytes, data_type: int) -> np.ndarray:
        if data_type in _DTYPE_MAP:
            dtype, width = _DTYPE_MAP[data_type]
        else:
            # fallback: prefer float32 if divisible by 4
            if len(raw) % 4 == 0:
                dtype, width = ">f4", 4
            else:
                dtype, width = ">f8", 8
        n = len(raw) // width
        return np.frombuffer(raw[: n * width], dtype=dtype).astype(np.float64)


def fetch_gwosc_aux(
    channel: str,
    start: int,
    end: int,
    *,
    host: str = "nds.gwosc.org",
    port: int = 31200,
    channel_type: str | None = None,
    timeout: float = 180.0,
) -> NDS2Series:
    """One-shot fetch of a public GWOSC auxiliary channel."""
    with NDS2Client(host=host, port=port, timeout=timeout) as client:
        return client.fetch(
            channel, start, end, channel_type=channel_type
        )


def fetch_many(
    requests: Iterable[tuple[str, int, int]],
    **kwargs: object,
) -> list[NDS2Series]:
    out: list[NDS2Series] = []
    with NDS2Client(**kwargs) as client:  # type: ignore[arg-type]
        for ch, start, end in requests:
            out.append(client.fetch(ch, start, end))
    return out
