#!/usr/bin/env python3
"""
Sector↔band dictionary RFC: execute pre-registered S1–S3 on real EEG (D2).

Dictionary D2 (default): 9 equal-width log10-frequency bins in [f_min, f_max].
Sector label q = 0..8 low→high frequency.

Statistics (pre-registered in Sector_Band_Dictionary_RFC.md):
  S1: mean adjacent-sector coupling > label-shuffled null
  S2: high-frequency shell within-coupling > cross to deep shell
  S3: path-order surrogate (phase scramble per band) drops mixed diagnostic
      more than amplitude-matched Gaussian noise

PROVENANCE: band side empirical (Cat B). Residual form math not modified.
Does NOT claim 9=12, 18/521 peaks, Orch-OR, or security reduction.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np

# Pre-registration (do not retune after seeing p-values)
N_SECTORS = 9
F_MIN_HZ = 0.5
F_MAX_HZ = 40.0  # scalp EEG practical upper band for this probe
N_PERM = 200
RNG_SEED = 5399
SHELL_HIGH = 2  # top 2 log-bins = high-frequency "shell"
DEEP_LOW = 4  # bottom 4 bins = deep shell metaphor
ALPHA = 0.05
MAX_SECONDS = 120.0  # wall-clock segment for PLV
MAX_CHANNELS = 8


def log_bin_edges(f_min: float, f_max: float, n: int) -> np.ndarray:
    return np.logspace(np.log10(f_min), np.log10(f_max), n + 1)


def butter_bandpass(x: np.ndarray, fs: float, lo: float, hi: float, order: int = 3) -> np.ndarray:
    from scipy.signal import butter, filtfilt

    nyq = 0.5 * fs
    lo_n = max(lo / nyq, 1e-6)
    hi_n = min(hi / nyq, 0.999)
    if lo_n >= hi_n:
        return np.zeros_like(x)
    b, a = butter(order, [lo_n, hi_n], btype="band")
    # filtfilt needs adequate length
    if len(x) < 3 * max(len(a), len(b)):
        return np.zeros_like(x)
    return filtfilt(b, a, x)


def hilbert_phase(x: np.ndarray) -> np.ndarray:
    from scipy.signal import hilbert

    return np.angle(hilbert(x))


def plv(ph1: np.ndarray, ph2: np.ndarray) -> float:
    return float(np.abs(np.mean(np.exp(1j * (ph1 - ph2)))))


def band_signals(x: np.ndarray, fs: float, edges: np.ndarray) -> list[np.ndarray]:
    bands = []
    for q in range(len(edges) - 1):
        lo, hi = float(edges[q]), float(edges[q + 1])
        # keep at least ~3 cycles at lo if possible
        bands.append(butter_bandpass(x, fs, lo, hi))
    return bands


def coupling_matrix_from_phases(phases: list[np.ndarray]) -> np.ndarray:
    n = len(phases)
    C = np.zeros((n, n))
    for q in range(n):
        C[q, q] = 1.0
        for r in range(q + 1, n):
            v = plv(phases[q], phases[r])
            C[q, r] = C[r, q] = v
    return C


def mean_adjacent(C: np.ndarray) -> float:
    n = C.shape[0]
    return float(np.mean([C[q, q + 1] for q in range(n - 1)]))


def mean_shell_within(C: np.ndarray, shell_idx: list[int]) -> float:
    pairs = [(i, j) for a, i in enumerate(shell_idx) for j in shell_idx[a + 1 :]]
    if not pairs:
        return float("nan")
    return float(np.mean([C[i, j] for i, j in pairs]))


def mean_shell_to_deep(C: np.ndarray, shell_idx: list[int], deep_idx: list[int]) -> float:
    if not shell_idx or not deep_idx:
        return float("nan")
    return float(np.mean([C[i, j] for i in shell_idx for j in deep_idx]))


def mixed_diagnostic(C: np.ndarray) -> float:
    """
    Mixed residual-style diagnostic: mean |off-diagonal| coupling
    (all cross-sector mass), analogous to nonzero mixed pairing mass.
    """
    n = C.shape[0]
    vals = [C[q, r] for q in range(n) for r in range(q + 1, n)]
    return float(np.mean(vals))


def load_eeg_multichannel(edf_path: Path) -> tuple[np.ndarray, float, list[str]]:
    """Return data shape (n_ch, n_samples), fs, ch_names."""
    import mne

    raw = mne.io.read_raw_edf(str(edf_path), preload=True, verbose=False)
    # Prefer bipolar montage channels
    preferred = [
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
    ]
    names = list(raw.ch_names)
    pick = [ch for ch in preferred if ch in names]
    if len(pick) < 2:
        pick = names[: min(MAX_CHANNELS, len(names))]
    else:
        pick = pick[:MAX_CHANNELS]
    raw.pick(pick)
    fs = float(raw.info["sfreq"])
    n_max = int(MAX_SECONDS * fs)
    data = raw.get_data()
    if data.shape[1] > n_max:
        data = data[:, :n_max]
    return data, fs, pick


def phases_for_channel(x: np.ndarray, fs: float, edges: np.ndarray) -> list[np.ndarray]:
    bands = band_signals(x, fs, edges)
    return [hilbert_phase(b) for b in bands]


def average_C_over_channels(data: np.ndarray, fs: float, edges: np.ndarray) -> np.ndarray:
    n_ch = data.shape[0]
    acc = np.zeros((N_SECTORS, N_SECTORS))
    for c in range(n_ch):
        # z-score channel
        x = data[c].astype(float)
        x = x - np.mean(x)
        sd = np.std(x)
        if sd > 0:
            x = x / sd
        ph = phases_for_channel(x, fs, edges)
        acc += coupling_matrix_from_phases(ph)
    return acc / n_ch


def phase_scramble_bands(x: np.ndarray, fs: float, edges: np.ndarray, rng: np.random.Generator) -> list[np.ndarray]:
    """Path-order surrogate: scramble phase within each band independently."""
    bands = band_signals(x, fs, edges)
    out = []
    for b in bands:
        X = np.fft.rfft(b)
        mag = np.abs(X)
        # random phase; keep DC real
        rand_ph = rng.uniform(0, 2 * np.pi, size=mag.shape)
        rand_ph[0] = 0.0
        if len(mag) > 1:
            # nyquist bin if present: keep real
            if b.shape[0] % 2 == 0:
                rand_ph[-1] = 0.0
        Y = mag * np.exp(1j * rand_ph)
        y = np.fft.irfft(Y, n=len(b))
        out.append(hilbert_phase(y))
    return out


def amp_matched_noise_phases(x: np.ndarray, fs: float, edges: np.ndarray, rng: np.random.Generator) -> list[np.ndarray]:
    """Amplitude-matched Gaussian noise, then same band filters."""
    sd = float(np.std(x)) or 1.0
    noise = rng.normal(0.0, sd, size=x.shape)
    return phases_for_channel(noise, fs, edges)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    edf = root / "data" / "RFFT_datasets" / "real" / "physionet_chbmit" / "chb01_01.edf"
    if not edf.is_file():
        print("FAIL: EDF not found", edf)
        return 1

    try:
        import scipy  # noqa: F401
    except ImportError:
        print("FAIL: scipy required for S1–S3 probe")
        return 1

    rng = np.random.default_rng(RNG_SEED)
    data, fs, ch_names = load_eeg_multichannel(edf)
    edges = log_bin_edges(F_MIN_HZ, min(F_MAX_HZ, 0.45 * fs), N_SECTORS)

    C = average_C_over_channels(data, fs, edges)
    s1_obs = mean_adjacent(C)

    # S1 null: shuffle sector labels (permute rows/cols)
    s1_null = []
    for _ in range(N_PERM):
        perm = rng.permutation(N_SECTORS)
        Cp = C[np.ix_(perm, perm)]
        s1_null.append(mean_adjacent(Cp))
    s1_null = np.asarray(s1_null)
    # one-sided: larger adjacent coupling than null
    s1_p = float(np.mean(s1_null >= s1_obs))
    s1_pass = s1_p < ALPHA

    # S2: high-frequency shell = last SHELL_HIGH bins; deep = first DEEP_LOW
    shell_idx = list(range(N_SECTORS - SHELL_HIGH, N_SECTORS))
    deep_idx = list(range(DEEP_LOW))
    within = mean_shell_within(C, shell_idx)
    cross = mean_shell_to_deep(C, shell_idx, deep_idx)
    s2_pass = bool(within > cross) if (not math.isnan(within) and not math.isnan(cross)) else False
    s2_ratio = float(within / cross) if cross > 0 else float("inf")

    # S3: mixed diagnostic drop under path-order surrogate vs amp-matched noise
    # Use channel 0 as primary path for surrogates (pre-reg: first picked channel)
    x0 = data[0].astype(float)
    x0 = x0 - np.mean(x0)
    sd0 = np.std(x0)
    if sd0 > 0:
        x0 = x0 / sd0
    C0 = coupling_matrix_from_phases(phases_for_channel(x0, fs, edges))
    mixed_obs = mixed_diagnostic(C0)

    mixed_scramble = []
    mixed_noise = []
    n_s3 = min(N_PERM, 80)  # cost control
    for _ in range(n_s3):
        ph_s = phase_scramble_bands(x0, fs, edges, rng)
        ph_n = amp_matched_noise_phases(x0, fs, edges, rng)
        mixed_scramble.append(mixed_diagnostic(coupling_matrix_from_phases(ph_s)))
        mixed_noise.append(mixed_diagnostic(coupling_matrix_from_phases(ph_n)))
    mixed_scramble = np.asarray(mixed_scramble)
    mixed_noise = np.asarray(mixed_noise)
    drop_scramble = float(mixed_obs - np.mean(mixed_scramble))
    drop_noise = float(mixed_obs - np.mean(mixed_noise))
    # Prediction: path-order surrogate reduces mixed diagnostic more
    s3_pass = bool(drop_scramble > drop_noise)
    # also require scramble mean < obs
    s3_scramble_below = bool(np.mean(mixed_scramble) < mixed_obs)

    outcome = {
        "S1": "PASS" if s1_pass else "FAIL",
        "S2": "PASS" if s2_pass else "FAIL",
        "S3": "PASS" if (s3_pass and s3_scramble_below) else "FAIL",
    }
    n_pass = sum(1 for v in outcome.values() if v == "PASS")
    if n_pass == 3:
        decision = "PROMOTE_WORKING_CAT_B_DICTIONARY"
    elif n_pass == 0:
        decision = "RETIRE_BIO_SECTOR_METAPHOR_THIS_DATASET"
    else:
        decision = "MIXED_KEEP_RFC_OPEN_RESIDUAL_LOCKS_UNCHANGED"

    results = {
        "provenance": {
            "category": "B",
            "dictionary": "D2",
            "orientation": "q=0..8 low→high frequency",
            "dataset": "physionet_chbmit chb01_01.edf",
            "residual_math_unchanged": True,
            "not_claim_9_equals_12": True,
            "not_claim_18_521_peaks": True,
            "not_Orch_OR": True,
            "not_security_reduction": True,
            "pre_registered": {
                "n_sectors": N_SECTORS,
                "f_min_hz": F_MIN_HZ,
                "f_max_hz": F_MAX_HZ,
                "n_perm": N_PERM,
                "rng_seed": RNG_SEED,
                "shell_high_bins": SHELL_HIGH,
                "deep_low_bins": DEEP_LOW,
                "alpha": ALPHA,
                "max_seconds": MAX_SECONDS,
                "max_channels": MAX_CHANNELS,
            },
        },
        "data": {
            "fs": fs,
            "n_channels": int(data.shape[0]),
            "n_samples": int(data.shape[1]),
            "duration_s": float(data.shape[1] / fs),
            "channels": ch_names,
            "log_bin_edges_hz": edges.tolist(),
            "bin_centers_hz": (np.sqrt(edges[:-1] * edges[1:])).tolist(),
        },
        "coupling_matrix_C_mean_PLV": C.tolist(),
        "S1": {
            "description": "mean adjacent-sector PLV > label shuffle",
            "observed_mean_adjacent": s1_obs,
            "null_mean": float(np.mean(s1_null)),
            "null_std": float(np.std(s1_null)),
            "null_ci95": [
                float(np.percentile(s1_null, 2.5)),
                float(np.percentile(s1_null, 97.5)),
            ],
            "p_one_sided": s1_p,
            "alpha": ALPHA,
            "pass": s1_pass,
        },
        "S2": {
            "description": "high-frequency shell within PLV > shell-to-deep PLV",
            "shell_indices": shell_idx,
            "deep_indices": deep_idx,
            "within_shell": within,
            "shell_to_deep": cross,
            "ratio_within_over_cross": s2_ratio,
            "pass": s2_pass,
        },
        "S3": {
            "description": "path-order (phase scramble) drops mixed diagnostic more than amp-matched noise",
            "mixed_obs": mixed_obs,
            "mixed_scramble_mean": float(np.mean(mixed_scramble)),
            "mixed_noise_mean": float(np.mean(mixed_noise)),
            "drop_scramble": drop_scramble,
            "drop_noise": drop_noise,
            "n_surrogates": n_s3,
            "scramble_below_obs": s3_scramble_below,
            "pass": bool(s3_pass and s3_scramble_below),
        },
        "outcome": outcome,
        "n_pass": n_pass,
        "decision": decision,
        "action_per_RFC": {
            "PROMOTE_WORKING_CAT_B_DICTIONARY": "S1–S2 (and S3) pass → working Cat B; design relative SS tests",
            "RETIRE_BIO_SECTOR_METAPHOR_THIS_DATASET": "clear fail → keep residual math; retire bio-sector map here",
            "MIXED_KEEP_RFC_OPEN_RESIDUAL_LOCKS_UNCHANGED": "partial → RFC open; residual locks unchanged",
        }[decision],
    }

    out = root / "sector_band_S1S3_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print("OK: D2 dictionary on", edf.name, "chs=", ch_names)
    print("S1", outcome["S1"], "p=", round(s1_p, 4), "adj=", round(s1_obs, 4))
    print("S2", outcome["S2"], "within=", round(within, 4), "cross=", round(cross, 4))
    print("S3", outcome["S3"], "drop_scramble=", round(drop_scramble, 4), "drop_noise=", round(drop_noise, 4))
    print("DECISION:", decision)
    print("wrote", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
