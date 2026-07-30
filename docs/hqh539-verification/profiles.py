"""HQH-539 digest profiles: REF (canonical) and P32 (product/deploy)."""
from __future__ import annotations

import hashlib
from typing import Union

from hqh539 import DOMAIN_SEP, STEPS, iterate_n_steps, hqh_539_512

# REF is the canonical implementation in hqh539.py
hqh_539_512_ref = hqh_539_512


def _as_bytes(value: Union[str, bytes]) -> bytes:
    if isinstance(value, str):
        return value.encode("utf-8")
    return value


def hqh_539_512_p32(
    message: Union[str, bytes],
    salt: Union[str, bytes] = b"",
) -> str:
    """
    Product/deploy profile: fixed 32-byte big-endian fingerprint (low 256 bits).

    Matches the finalize shape used in 539-Labs-repo deploy/demo hash paths.
    Digests are NOT interchangeable with REF.
    """
    message_b = _as_bytes(message)
    salt_b = _as_bytes(salt)
    m = int.from_bytes(hashlib.sha3_512(message_b + salt_b).digest(), "big")
    m = iterate_n_steps(m, STEPS)
    state_bytes = (m & ((1 << 256) - 1)).to_bytes(32, "big")
    return hashlib.sha3_512(state_bytes + salt_b + DOMAIN_SEP).hexdigest()


def hqh_539_256_p32(message: Union[str, bytes], salt: Union[str, bytes] = b"") -> str:
    return hqh_539_512_p32(message, salt)[:64]


__all__ = [
    "hqh_539_512_ref",
    "hqh_539_512_p32",
    "hqh_539_256_p32",
]
