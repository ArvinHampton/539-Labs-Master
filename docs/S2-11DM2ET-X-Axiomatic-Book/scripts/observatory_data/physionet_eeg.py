"""
PhysioNet EEG → free-first R-FFT arrays.

Primary path: EDF/EDF+ via MNE (CHB-MIT and most PhysioNet EEG sets).
Produces the (t, signal, fs) triple expected by R-FFT-539.9 free-first analysis.

Notes
-----
* CHB-MIT files are ~1 hour at 256 Hz → only ~6–7 cycles of G₄=539.9 s.
  Free peaks near that period have limited resolution; interpret cautiously.
* Always free estimator + nulls first; power_5399 / snr_5399 are secondary.
* Pick one clean channel (or average a few bipolar pairs); do not dump all
  channels into one series without a pre-registered reason.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np

# Common bipolar montage names used in CHB-MIT-style files
_PREFERRED_CHANNELS = (
    "FP1-F7",
    "FP1-F3",
    "F7-T7",
    "T7-P7",
    "P7-O1",
    "FP2-F8",
    "FP2-F4",
    "F8-T8",
    "T8-P8",
    "P8-O2",
    "FZ-CZ",
    "CZ-PZ",
)


def physionet_eeg_to_arrays(
    edf_path: str | Path,
    channel_name: str | None = None,
    duration_s: float | None = None,
    start_s: float = 0.0,
) -> tuple[np.ndarray, np.ndarray, float]:
    """
    Convert a PhysioNet EEG EDF file into (t, signal, fs) for free-first R-FFT.

    Parameters
    ----------
    edf_path :
        Path to the ``.edf`` file (e.g. ``chb01_01.edf`` from CHB-MIT).
    channel_name :
        Channel to extract. If ``None``, uses a preferred scalp channel if
        present, otherwise the first channel containing ``EEG``, else first
        channel overall.
    duration_s :
        Maximum length in seconds to keep. ``None`` = entire recording.
    start_s :
        Start time in seconds from the beginning of the file.

    Returns
    -------
    t, signal, fs :
        Time (s from segment start), channel samples, sampling rate (Hz).
    """
    try:
        import mne
    except ImportError as e:
        raise ImportError(
            "mne is required for PhysioNet EDF conversion. "
            "Install with: pip install mne"
        ) from e

    edf_path = Path(edf_path)
    if not edf_path.is_file():
        raise FileNotFoundError(f"EDF not found: {edf_path}")

    raw = mne.io.read_raw_edf(str(edf_path), preload=True, verbose=False)

    if channel_name is None:
        preferred = [ch for ch in raw.ch_names if ch in _PREFERRED_CHANNELS]
        if preferred:
            channel_name = preferred[0]
        else:
            eeg_like = [
                ch
                for ch in raw.ch_names
                if "EEG" in ch.upper() or "-" in ch  # bipolar labels
            ]
            channel_name = eeg_like[0] if eeg_like else raw.ch_names[0]

    if channel_name not in raw.ch_names:
        raise ValueError(
            f"Channel '{channel_name}' not found. Available: {list(raw.ch_names)}"
        )

    raw.pick([channel_name])

    if duration_s is not None:
        tmax = start_s + float(duration_s)
        # MNE crop is inclusive of tmin, exclusive-ish of tmax; clamp to data
        tmax = min(tmax, float(raw.times[-1]))
        if tmax <= start_s:
            raise ValueError(
                f"empty crop: start_s={start_s}, duration_s={duration_s}, "
                f"file length={raw.times[-1]:.3f} s"
            )
        raw.crop(tmin=float(start_s), tmax=tmax)
    elif start_s > 0:
        raw.crop(tmin=float(start_s))

    data = np.asarray(raw.get_data()[0], dtype=np.float64)
    fs = float(raw.info["sfreq"])
    t = np.arange(len(data), dtype=np.float64) / fs
    return t, data, fs


def edf_to_observatory_payload(
    edf_path: str | Path,
    *,
    channel_name: str | None = None,
    duration_s: float | None = None,
    start_s: float = 0.0,
    dataset_id: str = "physionet_eeg_edf",
    facility: str = "PhysioNet EEG",
) -> dict[str, Any]:
    """
    Build a dict ready for ``ObservatorySeries`` construction + R-FFT.

    Returns values, times, dt=1/fs, provenance, notes.
    """
    t, signal, fs = physionet_eeg_to_arrays(
        edf_path,
        channel_name=channel_name,
        duration_s=duration_s,
        start_s=start_s,
    )
    dt = 1.0 / fs
    n_cycles_g4 = float(t[-1]) / 539.9 if len(t) else 0.0
    notes = [
        "PhysioNet / CHB-MIT-style EDF via MNE — real clinical EEG, not synthetic.",
        "Free-first R-FFT only; power_5399 / snr_5399 are secondary compatibility scores.",
    ]
    if n_cycles_g4 < 20:
        notes.append(
            f"Segment spans only ~{n_cycles_g4:.1f} cycles of G₄=539.9 s "
            f"(duration={t[-1]:.1f} s). Free peaks near G₄ have limited frequency "
            "resolution — interpret cautiously."
        )
    return {
        "dataset_id": dataset_id,
        "facility": facility,
        "values": signal,
        "times": t,
        "dt": dt,
        "fs": fs,
        "uniform": True,
        "source_url": str(Path(edf_path).resolve()),
        "provenance": {
            "edf_path": str(Path(edf_path).resolve()),
            "channel": channel_name,
            "start_s": start_s,
            "duration_s": duration_s,
            "fs": fs,
            "n": int(len(signal)),
            "n_cycles_g4_approx": n_cycles_g4,
            "is_real": True,
            "synthetic": False,
            "converter": "physionet_eeg_to_arrays",
        },
        "notes": notes,
    }
