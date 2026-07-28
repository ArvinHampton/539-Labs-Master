"""
Loaders for real public observatory products.

No synthetic generators. Fetch or fail with a clear message.
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import tarfile
import urllib.request
from pathlib import Path
from typing import Any, Callable
from urllib.error import HTTPError, URLError

import numpy as np

from .registry import (
    DATA_ROOT,
    REAL_ROOT,
    dismiss_synthetic,
    get_entry,
    list_observatories,
    load_registry,
    staging_dir,
)
from .series import ObservatorySeries

# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

_USER_AGENT = "R-FFT-539.9-observatory-loader/1.0 (scientific; +https://gwosc.org)"


def _urlopen(url: str, timeout: int = 120):
    req = urllib.request.Request(url, headers={"User-Agent": _USER_AGENT})
    return urllib.request.urlopen(req, timeout=timeout)


def _download(url: str, dest: Path, timeout: int = 600) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    tmp = dest.with_suffix(dest.suffix + ".part")
    try:
        with _urlopen(url, timeout=timeout) as resp, open(tmp, "wb") as out:
            shutil.copyfileobj(resp, out)
        tmp.replace(dest)
    except Exception:
        if tmp.exists():
            tmp.unlink(missing_ok=True)
        raise
    return dest


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _write_meta(stage: Path, meta: dict[str, Any]) -> None:
    (stage / "fetch_meta.json").write_text(
        json.dumps(meta, indent=2), encoding="utf-8"
    )


# ---------------------------------------------------------------------------
# GWOSC open strain (H1 / L1 / V1 / K1)
# ---------------------------------------------------------------------------

# Event → catalog JSON (public Event API v1-style, still served by gwosc.org)
_GWOSC_EVENT_JSON: dict[str, str] = {
    "GW150914": "https://gwosc.org/eventapi/json/GWTC-1-confident/GW150914/v3",
    "GW151226": "https://gwosc.org/eventapi/json/GWTC-1-confident/GW151226/v3",
    "GW170104": "https://gwosc.org/eventapi/json/GWTC-1-confident/GW170104/v3",
    "GW170608": "https://gwosc.org/eventapi/json/GWTC-1-confident/GW170608/v3",
    "GW170814": "https://gwosc.org/eventapi/json/GWTC-1-confident/GW170814/v3",
    "GW170817": "https://gwosc.org/eventapi/json/GWTC-1-confident/GW170817/v3",
    "GW190425": "https://gwosc.org/eventapi/json/GWTC-2.1-confident/GW190425/v3",
    "GW190521": "https://gwosc.org/eventapi/json/GWTC-2.1-confident/GW190521/v4",
    "GW200115_042309": "https://gwosc.org/eventapi/json/GWTC-3-confident/GW200115_042309/v2",
    "GW200129_065458": "https://gwosc.org/eventapi/json/GWTC-3-confident/GW200129_065458/v1",
}


def _resolve_gwosc_strain_url(
    *,
    event: str,
    detector: str,
    sample_rate: int = 4096,
    duration: float = 32.0,
) -> str:
    """
    Resolve a public HTTPS URL for open strain HDF5.

    Prefers the Event API strain list (stable for short event segments).
    Falls back to ``gwosc.locate.get_event_urls`` without a duration filter
    (duration filters currently 400 on some API v2 endpoints).
    """
    det = detector.upper()
    # 1) Known event JSON
    json_url = _GWOSC_EVENT_JSON.get(event)
    if json_url is None:
        # try eventapi search
        try:
            from gwosc.api import fetch_event_json

            meta = fetch_event_json(event)
            # meta may nest differently across versions
            if isinstance(meta, dict) and "events" in meta:
                ev = next(iter(meta["events"].values()))
            else:
                ev = meta
            if isinstance(ev, dict) and "jsonurl" in ev:
                json_url = ev["jsonurl"]
        except Exception:
            json_url = None

    candidates: list[dict[str, Any]] = []
    if json_url:
        with _urlopen(json_url, timeout=60) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
        ev = next(iter(payload.get("events", {"": payload}).values()))
        for s in ev.get("strain", []) or []:
            if s.get("detector") != det:
                continue
            fmt = str(s.get("format", "")).lower()
            if fmt not in {"hdf5", "hdf"}:
                continue
            candidates.append(s)

    def _score(s: dict[str, Any]) -> tuple:
        sr = int(s.get("sampling_rate") or 0)
        dur = float(s.get("duration") or 0)
        # prefer exact sample_rate and duration, then closest duration, then 4 kHz
        return (
            0 if sr == sample_rate else 1,
            abs(dur - float(duration)),
            0 if sr == 4096 else 1,
            dur,  # smaller preferred among ties
        )

    if candidates:
        candidates.sort(key=_score)
        url = candidates[0].get("url")
        if url:
            return str(url)

    # 2) gwosc.locate without duration (avoids API v2 400)
    try:
        from gwosc.locate import get_event_urls

        urls = get_event_urls(
            event, detector=det, sample_rate=sample_rate, format="hdf5"
        )
        if not urls:
            urls = get_event_urls(event, detector=det, format="hdf5")
        if urls:
            return str(urls[0])
    except ImportError as e:
        raise ImportError(
            "Package 'gwosc' is required for open strain fetch when the event "
            "is not in the built-in catalog map. Install: pip install gwosc"
        ) from e
    except Exception:
        pass

    raise FileNotFoundError(
        f"No GWOSC HDF5 strain URL for event={event} detector={det}. "
        "Check https://gwosc.org/eventapi/ and catalog coverage."
    )


def fetch_gwosc_strain(
    dataset_id: str,
    *,
    event: str | None = None,
    detector: str | None = None,
    sample_rate: int = 4096,
    duration: float = 32.0,
    force: bool = False,
) -> Path:
    """
    Download a short open-strain HDF5 segment centered on a catalog event.

    Uses the public GWOSC HTTPS file list (no synthetic data).
    """
    entry = get_entry(dataset_id)
    event = event or entry.get("default_event") or "GW150914"
    detector = detector or entry.get("default_detector") or "H1"
    stage = staging_dir(dataset_id)
    out = stage / f"{detector}_{event}_{int(duration)}s_{sample_rate}Hz.hdf5"
    if out.exists() and not force:
        return out

    url = _resolve_gwosc_strain_url(
        event=event,
        detector=detector,
        sample_rate=sample_rate,
        duration=duration,
    )
    _download(url, out)
    _write_meta(
        stage,
        {
            "dataset_id": dataset_id,
            "event": event,
            "detector": detector,
            "url": url,
            "path": str(out),
            "sha256": _sha256(out),
            "duration_s": duration,
            "sample_rate": sample_rate,
            "is_real": True,
            "synthetic": False,
        },
    )
    return out


def load_gwosc_strain(
    dataset_id: str,
    *,
    event: str | None = None,
    detector: str | None = None,
    sample_rate: int = 4096,
    duration: float = 32.0,
    decimate: int = 1,
    force_fetch: bool = False,
) -> ObservatorySeries:
    """Load GWOSC open strain as an ObservatorySeries (real data only)."""
    entry = get_entry(dataset_id)
    event = event or entry.get("default_event") or "GW150914"
    detector = detector or entry.get("default_detector") or "H1"
    path = fetch_gwosc_strain(
        dataset_id,
        event=event,
        detector=detector,
        sample_rate=sample_rate,
        duration=duration,
        force=force_fetch,
    )

    # Prefer h5py; fall back to gwpy if available
    strain, dt, extra = _read_gwosc_hdf5(path)
    if decimate > 1:
        strain = strain[::decimate]
        dt = dt * decimate
    times = np.arange(len(strain), dtype=np.float64) * dt
    return ObservatorySeries(
        dataset_id=dataset_id,
        facility=entry.get("facility", detector),
        values=strain,
        times=times,
        dt=float(dt),
        uniform=True,
        source_url=str(path),
        provenance={
            "event": event,
            "detector": detector,
            "sample_rate_native": sample_rate,
            "decimate": decimate,
            "file": str(path),
            "sha256": _sha256(path),
            **extra,
        },
        is_real=True,
        notes=[
            "GWOSC public open strain — not a synthetic series.",
            "For long-period (hundreds of seconds) free-first R-FFT, prefer "
            "multi-segment concatenation or O3 aux trends; short event windows "
            "are high-frequency content by construction.",
        ],
    )


def _read_gwosc_hdf5(path: Path) -> tuple[np.ndarray, float, dict[str, Any]]:
    try:
        import h5py
    except ImportError:
        h5py = None  # type: ignore

    if h5py is not None:
        with h5py.File(path, "r") as f:
            # GWOSC layout: strain/Strain + meta
            if "strain" in f and "Strain" in f["strain"]:
                strain = np.asarray(f["strain"]["Strain"][()], dtype=np.float64)
                meta = f["meta"] if "meta" in f else {}
                dt = float(meta["Duration"][()] / len(strain)) if "Duration" in meta else None
                if dt is None and "GPSstart" in meta:
                    # try sample rate
                    if "SampleRate" in f.get("strain", {}):
                        dt = 1.0 / float(f["strain"]["SampleRate"][()])
                    else:
                        dt = 1.0 / 4096.0
                if "SampleRate" in meta:
                    dt = 1.0 / float(meta["SampleRate"][()])
                # more reliable: x-attributes on dataset
                ds = f["strain"]["Strain"]
                if "Xspacing" in ds.attrs:
                    dt = float(ds.attrs["Xspacing"])
                elif dt is None:
                    dt = 1.0 / 4096.0
                extra = {
                    "gps_start": float(meta["GPSstart"][()]) if "GPSstart" in meta else None,
                    "duration": float(meta["Duration"][()]) if "Duration" in meta else None,
                }
                return strain, float(dt), extra

    # GWpy fallback
    try:
        from gwpy.timeseries import TimeSeries

        ts = TimeSeries.read(str(path))
        dt = float(ts.dt.value)
        return np.asarray(ts.value, dtype=np.float64), dt, {"gwpy": True}
    except Exception as e:
        raise RuntimeError(
            f"Could not read GWOSC HDF5 {path}. Install h5py or gwpy. ({e})"
        ) from e


# ---------------------------------------------------------------------------
# LIGO O3 auxiliary via NDS2 (optional gwpy)
# ---------------------------------------------------------------------------

def load_ligo_aux_nds2(
    dataset_id: str,
    *,
    channel: str | None = None,
    start: int | None = None,
    end: int | None = None,
    host: str = "nds.gwosc.org",
    port: int = 31200,
    channel_type: str | None = None,
) -> ObservatorySeries:
    """
    Fetch an O3 auxiliary channel window from public NDS2 (nds.gwosc.org).

    Uses the pure-Python client in ``nds2_pure.py`` — no gwpy / MSVC.
    Does not fabricate data if the server is offline.
    """
    entry = get_entry(dataset_id)
    channel = channel or entry.get("example_channel")
    gps = entry.get("example_gps") or [1266624018, 1266624618]
    start = int(start if start is not None else gps[0])
    end = int(end if end is not None else gps[1])
    if not channel:
        raise ValueError("channel name required for aux NDS2 fetch")

    stage = staging_dir(dataset_id)
    safe = channel.replace(":", "_").replace("/", "_")
    cache = stage / f"{safe}_{start}_{end}.npy"
    meta_path = cache.with_suffix(".json")

    if cache.exists() and meta_path.exists():
        values = np.load(cache)
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        dt = float(meta["dt"])
        times = np.arange(len(values), dtype=np.float64) * dt
        return ObservatorySeries(
            dataset_id=dataset_id,
            facility=entry.get("facility", "LIGO"),
            values=values,
            times=times,
            dt=dt,
            uniform=True,
            source_url=f"nds2://{host}:{port}/{channel}",
            provenance=meta,
            is_real=True,
            notes=["Cached NDS2 auxiliary channel (pure-Python client)."],
        )

    from .nds2_pure import NDS2Error, fetch_gwosc_aux

    try:
        series = fetch_gwosc_aux(
            channel,
            start,
            end,
            host=host,
            port=port,
            channel_type=channel_type,
        )
    except NDS2Error as e:
        raise RuntimeError(
            f"NDS2 fetch failed for {channel} @ {host}:{port} "
            f"GPS [{start}, {end}): {e}\n"
            f"Portal: {entry.get('portal')}"
        ) from e

    values = np.asarray(series.values, dtype=np.float64)
    dt = float(series.dt)
    times = np.arange(len(values), dtype=np.float64) * dt
    meta = {
        "channel": channel,
        "start": start,
        "end": end,
        "host": host,
        "port": port,
        "rate_hz": series.rate,
        "data_type": series.data_type,
        "dt": dt,
        "n": len(values),
        "client": "nds2_pure",
        "is_real": True,
        "synthetic": False,
    }
    np.save(cache, values)
    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    _write_meta(stage, meta)

    return ObservatorySeries(
        dataset_id=dataset_id,
        facility=entry.get("facility", "LIGO"),
        values=values,
        times=times,
        dt=dt,
        uniform=True,
        source_url=f"nds2://{host}:{port}/{channel}",
        provenance=meta,
        is_real=True,
        notes=[
            "Live NDS2 auxiliary channel via pure-Python client (no gwpy).",
            f"rate≈{series.rate:g} Hz, n={len(values)}, GPS[{start},{end}).",
        ],
    )


# ---------------------------------------------------------------------------
# NANOGrav residuals
# ---------------------------------------------------------------------------

_RESIDUAL_NAME_RE = re.compile(
    r"(residual|postfit|post_fit|\.res$|resid)", re.IGNORECASE
)


def fetch_nanograv_archive(dataset_id: str, *, force: bool = False) -> Path:
    entry = get_entry(dataset_id)
    url = entry.get("download_url")
    if not url:
        raise ValueError(f"{dataset_id} has no download_url in registry")
    stage = staging_dir(dataset_id)
    # filename from URL
    name = url.split("/")[-1].split("?")[0]
    dest = stage / name
    if dest.exists() and dest.stat().st_size > 0 and not force:
        return dest
    try:
        _download(url, dest)
    except (HTTPError, URLError, TimeoutError) as e:
        alt = entry.get("alt_download_url")
        if not alt:
            raise RuntimeError(
                f"Failed to download NANOGrav archive from {url}: {e}"
            ) from e
        _download(alt, dest)
    _write_meta(
        stage,
        {
            "dataset_id": dataset_id,
            "url": url,
            "path": str(dest),
            "sha256": _sha256(dest),
            "is_real": True,
            "synthetic": False,
        },
    )
    return dest


def _extract_tar(archive: Path, dest_dir: Path) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    marker = dest_dir / ".extracted"
    if marker.exists():
        return dest_dir
    with tarfile.open(archive, "r:*") as tar:
        tar.extractall(dest_dir)
    marker.write_text(archive.name, encoding="utf-8")
    return dest_dir


def _find_residual_tables(root: Path) -> list[Path]:
    """
    Prefer NANOGrav epoch-averaged post-fit residuals:
      12.5yr: .../resid/res_avg/*.avg.res
      15yr:   .../residuals/*_NG15yr_nb.avg.res
    Fallback: *.full.res / *.all.res, then other residual-like files.
    """
    avg = sorted(root.rglob("*.avg.res"))
    if avg:
        return avg
    full = sorted(root.rglob("*.full.res")) + sorted(root.rglob("*.all.res"))
    if full:
        return sorted(set(full))
    hits: list[Path] = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if p.suffix.lower() in {".res", ".dmx"}:
            hits.append(p)
        elif p.suffix.lower() in {".txt", ".dat"} and _RESIDUAL_NAME_RE.search(
            p.name
        ):
            hits.append(p)
    return sorted(set(hits))


def _load_ascii_residual_table(path: Path) -> tuple[np.ndarray, np.ndarray]:
    """
    Parse NANOGrav residual tables.

    Canonical res_avg / res_full header:
      # MJD frequency(MHz) residual(us) uncertainty(us) ...
    So time = col 0 (MJD), residual = col 2 (µs). Two-column tables use col 0/1.
    """
    rows: list[list[float]] = []
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            s = line.strip()
            if not s or s[0] in "#;!" or s.upper().startswith("C "):
                continue
            if s.startswith("//"):
                continue
            parts = re.split(r"[\s,;]+", s)
            nums: list[float] = []
            for tok in parts:
                try:
                    nums.append(float(tok))
                except ValueError:
                    # stop at first non-numeric trailing flag field
                    if nums:
                        break
            if len(nums) >= 3:
                # MJD, freq, residual_us
                rows.append([nums[0], nums[2]])
            elif len(nums) >= 2:
                rows.append([nums[0], nums[1]])
    if len(rows) < 4:
        raise ValueError(f"could not parse >=4 numeric rows from {path}")
    arr = np.asarray(rows, dtype=np.float64)
    return arr[:, 0], arr[:, 1]


def load_nanograv_12p5(
    dataset_id: str = "nanograv_12p5yr_residuals",
    *,
    pulsar: str | None = None,
    force_fetch: bool = False,
) -> ObservatorySeries:
    return _load_nanograv(dataset_id, pulsar=pulsar, force_fetch=force_fetch)


def load_nanograv_15yr(
    dataset_id: str = "nanograv_15yr_residuals",
    *,
    pulsar: str | None = None,
    force_fetch: bool = False,
) -> ObservatorySeries:
    return _load_nanograv(dataset_id, pulsar=pulsar, force_fetch=force_fetch)


def _load_nanograv(
    dataset_id: str,
    *,
    pulsar: str | None,
    force_fetch: bool,
) -> ObservatorySeries:
    entry = get_entry(dataset_id)
    archive = fetch_nanograv_archive(dataset_id, force=force_fetch)
    stage = staging_dir(dataset_id)
    root = _extract_tar(archive, stage / "extracted")

    tables = _find_residual_tables(root)
    if not tables:
        # Fallback: any multi-column ascii that looks like pulsar timing
        for p in root.rglob("*.txt"):
            if p.stat().st_size > 200:
                tables.append(p)
        tables = sorted(set(tables))

    if not tables:
        raise FileNotFoundError(
            f"Downloaded {archive.name} but found no residual-like tables under "
            f"{root}. Inspect the archive layout and extend the parser."
        )

    if pulsar:
        pulsar_u = pulsar.upper().replace(" ", "")
        matched = [t for t in tables if pulsar_u in t.name.upper().replace(" ", "")]
        if not matched:
            matched = [t for t in tables if pulsar_u in str(t).upper().replace(" ", "")]
        if not matched:
            names = ", ".join(t.name for t in tables[:12])
            raise FileNotFoundError(
                f"No residual table matching pulsar={pulsar}. Examples: {names}"
            )
        tables = matched

    # Default pulsar: well-timed J1713+0747 when present, else first table
    if pulsar is None:
        preferred = [t for t in tables if "J1713+0747" in t.name]
        path = preferred[0] if preferred else tables[0]
    else:
        path = tables[0]

    times_mjd, values_us = _load_ascii_residual_table(path)
    # Sort by MJD and convert to seconds from first epoch
    order = np.argsort(times_mjd)
    times_mjd = times_mjd[order]
    values_us = values_us[order]
    times = (times_mjd - times_mjd[0]) * 86400.0  # days → seconds
    time_unit = "MJD_to_seconds"
    residual_unit = "microseconds"

    return ObservatorySeries(
        dataset_id=dataset_id,
        facility=entry.get("facility", "NANOGrav"),
        values=values_us,
        times=times,
        dt=None,
        uniform=False,
        source_url=entry.get("download_url", str(archive)),
        provenance={
            "archive": str(archive),
            "table": str(path),
            "pulsar": path.name.split("_")[0],
            "pulsar_filter": pulsar,
            "time_unit": time_unit,
            "residual_unit": residual_unit,
            "mjd_start": float(times_mjd[0]),
            "mjd_end": float(times_mjd[-1]),
            "sha256_archive": _sha256(archive),
            "n_tables_found": len(tables),
            "is_real": True,
            "synthetic": False,
        },
        is_real=True,
        notes=[
            "NANOGrav public residual table — real PTA data.",
            "Uneven sampling: use ObservatorySeries.to_uniform(dt=86400) (1 day) "
            "before R-FFT unless a different cadence is pre-registered.",
            "Cadence is days–weeks; G₄=539.9 s is far below the PTA Nyquist — "
            "free-first R-FFT here exercises the pipeline on real residuals, not a "
            "claim that G₄ is a PTA discovery frequency.",
        ],
    )


# ---------------------------------------------------------------------------
# EHT — manifest only (no fabricated visibilities)
# ---------------------------------------------------------------------------

def load_eht_manifest(
    dataset_id: str = "eht_polarized_visibilities",
    **_: Any,
) -> ObservatorySeries:
    """
    Stage an EHT access manifest. Does **not** invent visibility time series.

    Raises with portal instructions unless a user-supplied staged CSV/NPY of
    real derived series is present under the staging directory.
    """
    entry = get_entry(dataset_id)
    stage = staging_dir(dataset_id)
    manifest = {
        "dataset_id": dataset_id,
        "facility": entry.get("facility"),
        "portal": entry.get("portal"),
        "cyverse_note": entry.get("cyverse_note"),
        "is_real_source": True,
        "staged_series_required": True,
        "instructions": [
            "1. Obtain multi-epoch polarised visibility products from the EHT data portal / CyVerse.",
            "2. Reduce to a real scalar time series of interest (e.g. closure-phase residual, "
            "polarized fraction vs time) using your reduction pipeline.",
            "3. Place a two-column CSV (time_seconds, value) at:",
            f"   {stage / 'user_series.csv'}",
            "4. Re-run load_series('eht_polarized_visibilities').",
        ],
    }
    man_path = stage / "ACCESS_MANIFEST.json"
    man_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    user_csv = stage / "user_series.csv"
    user_npy = stage / "user_series.npz"
    if user_csv.exists():
        arr = np.loadtxt(user_csv, delimiter=",", ndmin=2)
        if arr.shape[1] < 2:
            arr = np.loadtxt(user_csv, ndmin=2)
        times, values = arr[:, 0], arr[:, 1]
        return ObservatorySeries(
            dataset_id=dataset_id,
            facility=entry.get("facility", "EHT"),
            values=values,
            times=times - times[0],
            dt=None,
            uniform=False,
            source_url=str(user_csv),
            provenance={"manifest": str(man_path), "user_staged": True, "is_real": True},
            is_real=True,
            notes=["User-staged EHT-derived series; verify provenance externally."],
        )
    if user_npy.exists():
        z = np.load(user_npy)
        times = np.asarray(z["times"], dtype=np.float64)
        values = np.asarray(z["values"], dtype=np.float64)
        return ObservatorySeries(
            dataset_id=dataset_id,
            facility=entry.get("facility", "EHT"),
            values=values,
            times=times - times[0],
            dt=None,
            uniform=False,
            source_url=str(user_npy),
            provenance={"manifest": str(man_path), "user_staged": True, "is_real": True},
            is_real=True,
            notes=["User-staged EHT-derived series; verify provenance externally."],
        )

    raise FileNotFoundError(
        "EHT products are not auto-downloaded (multi-GB CyVerse packages). "
        f"Manifest written to {man_path}. Portal: {entry.get('portal')}. "
        f"Stage a real derived series as {user_csv} then reload."
    )


# ---------------------------------------------------------------------------
# INTEGRAL/SPI 511 keV (Validation V5)
# ---------------------------------------------------------------------------

def load_integral_spi_511(
    dataset_id: str = "integral_spi_511kev",
    **_: Any,
) -> ObservatorySeries:
    """
    Load INTEGRAL/SPI 511 keV **time-binned flux** if staged.

    Maps / rate revisions alone are Category A products; free-first R-FFT
    requires a 1-D light curve. Stages ACCESS_MANIFEST.json on every call.
    """
    entry = get_entry(dataset_id)
    stage = staging_dir(dataset_id)
    cat_a = entry.get("category_A") or {}
    cat_b = entry.get("category_B") or {}
    clocks = entry.get("three_clocks") or {}
    proto = entry.get("rfft_protocol") or {}

    manifest = {
        "dataset_id": dataset_id,
        "validation_id": entry.get("validation_id", "V5"),
        "facility": entry.get("facility"),
        "product": entry.get("product"),
        "portal": entry.get("portal"),
        "category_A": cat_a,
        "category_B": cat_b,
        "three_clocks": clocks,
        "rfft_protocol": proto,
        "is_real_source": True,
        "numerical_rfft": "pending_until_lightcurve_staged",
        "staging": {
            "user_series_csv": str(stage / "user_series.csv"),
            "lightcurve_npz": str(stage / "lightcurve.npz"),
            "format_csv": "time_seconds,flux  (header optional)",
            "format_npz": "arrays times, values (seconds, flux units)",
        },
        "instructions": [
            "1. Reduce or obtain a time-binned 511 keV flux light curve from INTEGRAL/SPI public products / papers.",
            "2. Do not invent a series from sky maps alone.",
            f"3. Write two-column CSV to {(stage / 'user_series.csv')}",
            "   or lightcurve.npz with times= and values=.",
            "4. Re-run: python scripts/run_rfft_observatory.py --analyze integral_spi_511kev --n-null 32",
            "5. Free peak + nulls are primary; G4 / ladder metrics are secondary only.",
        ],
    }
    man_path = stage / "ACCESS_MANIFEST.json"
    man_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    user_csv = stage / "user_series.csv"
    user_npz = stage / "lightcurve.npz"
    notes_base = [
        "INTEGRAL/SPI 511 keV — real observatory program (Yoneda et al. 2025; Siegert & Yoneda 2026).",
        "Category A: high-latitude hotspots, possible 2–3× rate revision (~10^44 s⁻¹).",
        "Category B model leakage/E_leak interpretations are not free spectral discovery.",
        "Clocks: I = t_geo; II = sigma=539 steps; III = G4=539.9 s secondary only.",
    ]

    if user_csv.exists():
        arr = np.loadtxt(user_csv, delimiter=",", ndmin=2)
        if arr.shape[1] < 2:
            arr = np.loadtxt(user_csv, ndmin=2)
        times = np.asarray(arr[:, 0], dtype=np.float64)
        values = np.asarray(arr[:, 1], dtype=np.float64)
        order = np.argsort(times)
        times, values = times[order], values[order]
        times = times - times[0]
        d = np.diff(times)
        d = d[d > 0]
        dt = float(np.median(d)) if len(d) else None
        uniform = dt is not None and np.allclose(np.diff(times), dt, rtol=0.05, atol=dt * 0.05 if dt else 0)
        return ObservatorySeries(
            dataset_id=dataset_id,
            facility=entry.get("facility", "INTEGRAL/SPI"),
            values=values,
            times=times,
            dt=dt if uniform else None,
            uniform=bool(uniform),
            source_url=str(user_csv),
            provenance={
                "manifest": str(man_path),
                "user_staged": True,
                "validation_id": "V5",
                "is_real": True,
                "synthetic": False,
            },
            is_real=True,
            notes=notes_base
            + [
                "User-staged 511 keV light curve; verify reduction against primary papers.",
                "Run free-first R-FFT: precondition=False, n_null>0; G4 secondary only.",
            ],
        )

    if user_npz.exists():
        z = np.load(user_npz)
        times = np.asarray(z["times"], dtype=np.float64)
        values = np.asarray(z["values"], dtype=np.float64)
        order = np.argsort(times)
        times, values = times[order], values[order]
        times = times - times[0]
        d = np.diff(times)
        d = d[d > 0]
        dt = float(np.median(d)) if len(d) else None
        return ObservatorySeries(
            dataset_id=dataset_id,
            facility=entry.get("facility", "INTEGRAL/SPI"),
            values=values,
            times=times,
            dt=dt,
            uniform=dt is not None,
            source_url=str(user_npz),
            provenance={
                "manifest": str(man_path),
                "user_staged": True,
                "validation_id": "V5",
                "is_real": True,
                "synthetic": False,
            },
            is_real=True,
            notes=notes_base
            + ["User-staged lightcurve.npz; free-first protocol required."],
        )

    raise FileNotFoundError(
        "INTEGRAL/SPI 511 keV is registry-active (Validation V5) but no time-binned "
        f"light curve is staged yet. Manifest written to {man_path}. "
        f"Stage {user_csv} (time_seconds, flux) then re-run --analyze integral_spi_511kev. "
        f"Portal: {entry.get('portal')}. "
        "Do not fabricate a light curve from sky maps alone."
    )


# ---------------------------------------------------------------------------
# PhysioNet EEG (EDF via MNE)
# ---------------------------------------------------------------------------

def fetch_physionet_chbmit(
    dataset_id: str = "physionet_chbmit_eeg",
    *,
    relative_path: str | None = None,
    force: bool = False,
) -> Path:
    """
    Download one CHB-MIT EDF from PhysioNet open files (HTTPS).

    Default: chb01/chb01_01.edf (~1 hour, 256 Hz).
    """
    entry = get_entry(dataset_id)
    base = entry.get("download_base", "https://physionet.org/files/chbmit/1.0.0/")
    rel = relative_path or entry.get("default_relative_path", "chb01/chb01_01.edf")
    url = base.rstrip("/") + "/" + rel.lstrip("/")
    stage = staging_dir(dataset_id)
    dest = stage / Path(rel).name
    if dest.exists() and dest.stat().st_size > 0 and not force:
        return dest
    _download(url, dest, timeout=600)
    _write_meta(
        stage,
        {
            "dataset_id": dataset_id,
            "url": url,
            "path": str(dest),
            "relative_path": rel,
            "sha256": _sha256(dest),
            "is_real": True,
            "synthetic": False,
        },
    )
    return dest


def load_physionet_eeg(
    dataset_id: str = "physionet_chbmit_eeg",
    *,
    relative_path: str | None = None,
    edf_path: str | Path | None = None,
    channel_name: str | None = None,
    duration_s: float | None = 3600.0,
    start_s: float = 0.0,
    force_fetch: bool = False,
) -> ObservatorySeries:
    """Load CHB-MIT (or configured) PhysioNet EDF as ObservatorySeries."""
    entry = get_entry(dataset_id)
    if edf_path is None:
        edf_path = fetch_physionet_chbmit(
            dataset_id, relative_path=relative_path, force=force_fetch
        )
    from .physionet_eeg import edf_to_observatory_payload

    payload = edf_to_observatory_payload(
        edf_path,
        channel_name=channel_name,
        duration_s=duration_s,
        start_s=start_s,
        dataset_id=dataset_id,
        facility=entry.get("facility", "PhysioNet EEG"),
    )
    return ObservatorySeries(
        dataset_id=payload["dataset_id"],
        facility=payload["facility"],
        values=payload["values"],
        times=payload["times"],
        dt=payload["dt"],
        uniform=True,
        source_url=payload["source_url"],
        provenance=payload["provenance"],
        is_real=True,
        notes=payload["notes"],
    )


def load_physionet_eeg_local(
    dataset_id: str = "physionet_eeg_local",
    *,
    edf_path: str | Path | None = None,
    channel_name: str | None = None,
    duration_s: float | None = None,
    start_s: float = 0.0,
) -> ObservatorySeries:
    """
    Load a user-staged local EDF.

    Looks for ``edf_path``, or any ``*.edf`` under the staging directory.
    """
    entry = get_entry(dataset_id)
    stage = staging_dir(dataset_id)
    path: Path | None = Path(edf_path) if edf_path else None
    if path is None:
        found = sorted(stage.rglob("*.edf"))
        if not found:
            raise FileNotFoundError(
                f"No EDF staged for {dataset_id}. Place a .edf under {stage} "
                "or pass edf_path=..."
            )
        path = found[0]
    from .physionet_eeg import edf_to_observatory_payload

    payload = edf_to_observatory_payload(
        path,
        channel_name=channel_name,
        duration_s=duration_s,
        start_s=start_s,
        dataset_id=dataset_id,
        facility=entry.get("facility", "PhysioNet EEG"),
    )
    return ObservatorySeries(
        dataset_id=payload["dataset_id"],
        facility=payload["facility"],
        values=payload["values"],
        times=payload["times"],
        dt=payload["dt"],
        uniform=True,
        source_url=payload["source_url"],
        provenance=payload["provenance"],
        is_real=True,
        notes=payload["notes"],
    )


# ---------------------------------------------------------------------------
# Dispatch
# ---------------------------------------------------------------------------

_LOADERS: dict[str, Callable[..., ObservatorySeries]] = {
    "load_gwosc_strain": load_gwosc_strain,
    "load_ligo_aux_nds2": load_ligo_aux_nds2,
    "load_nanograv_12p5": load_nanograv_12p5,
    "load_nanograv_15yr": load_nanograv_15yr,
    "load_eht_manifest": load_eht_manifest,
    "load_physionet_eeg": load_physionet_eeg,
    "load_physionet_eeg_local": load_physionet_eeg_local,
    "load_integral_spi_511": load_integral_spi_511,
}


def load_series(dataset_id: str, **kwargs: Any) -> ObservatorySeries:
    """Load a real observatory series by registry id. Synthetics are rejected."""
    dismiss_synthetic(dataset_id)
    entry = get_entry(dataset_id)
    loader_name = entry.get("loader")
    if loader_name not in _LOADERS:
        raise RuntimeError(f"No loader implementation for '{loader_name}'")
    return _LOADERS[loader_name](dataset_id, **kwargs)


def fetch_dataset(dataset_id: str, **kwargs: Any) -> Path | ObservatorySeries:
    """Fetch/stage data for a registry id (download side effects)."""
    dismiss_synthetic(dataset_id)
    entry = get_entry(dataset_id)
    loader = entry.get("loader")
    if loader == "load_gwosc_strain":
        return fetch_gwosc_strain(dataset_id, **kwargs)
    if loader in {"load_nanograv_12p5", "load_nanograv_15yr"}:
        return fetch_nanograv_archive(dataset_id, **kwargs)
    if loader == "load_eht_manifest":
        # write manifest via load attempt
        try:
            return load_eht_manifest(dataset_id)
        except FileNotFoundError:
            return staging_dir(dataset_id) / "ACCESS_MANIFEST.json"
    if loader == "load_ligo_aux_nds2":
        return load_ligo_aux_nds2(dataset_id, **kwargs)
    if loader == "load_physionet_eeg":
        return fetch_physionet_chbmit(dataset_id, **{
            k: kwargs[k]
            for k in ("relative_path", "force")
            if k in kwargs
        })
    if loader == "load_physionet_eeg_local":
        stage = staging_dir(dataset_id)
        return stage
    if loader == "load_integral_spi_511":
        try:
            return load_integral_spi_511(dataset_id)
        except FileNotFoundError:
            return staging_dir(dataset_id) / "ACCESS_MANIFEST.json"
    raise RuntimeError(f"fetch not defined for loader {loader}")


def stage_status() -> dict[str, Any]:
    """Report which observatory products are staged under data/RFFT_datasets/real."""
    reg = load_registry()
    out: dict[str, Any] = {
        "data_root": str(DATA_ROOT),
        "real_root": str(REAL_ROOT),
        "policy": reg.get("policy"),
        "datasets": {},
    }
    for ds_id in list_observatories(reg):
        entry = reg["observatories"][ds_id]
        stage = REAL_ROOT / entry.get("staging_subdir", ds_id)
        files = []
        if stage.exists():
            files = [
                str(p.relative_to(REAL_ROOT))
                for p in stage.rglob("*")
                if p.is_file() and p.name not in {".extracted"}
            ][:50]
        out["datasets"][ds_id] = {
            "facility": entry.get("facility"),
            "staged": bool(files),
            "n_files": len(files),
            "sample_files": files[:10],
            "portal": entry.get("portal"),
            "size_note": entry.get("size_note"),
        }
    return out
