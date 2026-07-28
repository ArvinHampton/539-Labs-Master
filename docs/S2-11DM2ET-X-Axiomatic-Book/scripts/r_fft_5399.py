#!/usr/bin/env python3
"""
Unified Resonant FFT Algorithm (R-FFT-539.9)

Corrected, documented, ready-to-use spectral pipeline for the S²-11DM²ET-X
model period G₄ = 539.9 s (Clock-III).

Modes
-----
* free (precondition=False) — primary discovery path; no G₄ in the estimator.
* model-tuned (precondition=True) — secondary compatibility / lock analysis only.
* scrambled-G4 control — phase-randomised null that preserves |spectrum| shape
  while destroying coherent phase (methodological analogue of "scrambled-G4").

Implementation fixes vs. earlier draft
--------------------------------------
1. Kaiser window imported from ``scipy.signal.windows`` (with pure-NumPy
   fallback if SciPy is unavailable).
2. Explicit ``G4`` assignment used for the target-bin index (no dangling name).

Interpretation rule (non-negotiable)
------------------------------------
A refined period near 539.9 s under precondition=True is **not** an independent
discovery statistic: G₄ has already entered the procedure. Primary claims must
use free spectra and nulls; see R_FFT_5399_Validation_Protocol.md.

Usage
-----
  python r_fft_5399.py
  python r_fft_5399.py --demo --N 8192 --dt 1.0
  from r_fft_5399 import full_r_fft_analysis, G4, BETA_PBH
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

import numpy as np

# ---------------------------------------------------------------------------
# Closed model constants (S²-11DM²ET-X / HQH-539 ledger)
# ---------------------------------------------------------------------------

G4: float = 539.9
"""Clock-III flux / gravitational breathing period (seconds)."""

KAPPA_DARK: float = 243.0 / 539.0
"""Dark-energy coupling κ_dark = 243/539 ≈ 0.45083."""

BETA_PBH: float = 11.0 / 61.0
"""PBH friction / Clock-III weight β_PBH = 11/61 ≈ 0.18033 (legacy slogan 0.18)."""

MU: float = 1.55
"""Cosmic / global stability parameter μ (stable target)."""

PHI_0: float = 0.0
"""Resonant attractor phase offset."""

A_COS: float = 0.90
"""Cosine amplitude of the resonant attractor Φ(t)."""

A_SIN: float = BETA_PBH
"""Sine amplitude of Φ(t); closed value is exactly β_PBH = 11/61."""

SUBHARMONIC_LADDER: tuple[float, ...] = (5.0, 10.0, 15.0, 30.0, 45.0)
"""Sub-harmonic / synchronization ladder (seconds)."""

KAISER_BETA: float = 8.6
"""Kaiser window shape parameter β for Step 1 of R-FFT-539.9."""

MODULATION_PERIOD_S: float = 5.0
"""Cosine modulation period applied on top of the Kaiser window (~5 s)."""

NFFT_FACTOR: int = 16
"""Default zero-pad factor: nfft = N × 16."""

REFINE_MAX_ITER: int = 70
REFINE_TOL: float = 1e-12


# ---------------------------------------------------------------------------
# Windows
# ---------------------------------------------------------------------------

def kaiser_window(n: int, beta: float = KAISER_BETA) -> np.ndarray:
    """
    Kaiser window of length n.

    Prefers ``scipy.signal.windows.kaiser``; falls back to a pure-NumPy
    implementation of the same formula (I₀-based).
    """
    if n <= 0:
        return np.array([], dtype=np.float64)
    if n == 1:
        return np.ones(1, dtype=np.float64)
    try:
        from scipy.signal.windows import kaiser as _kaiser

        return np.asarray(_kaiser(n, beta), dtype=np.float64)
    except ImportError:
        return _kaiser_numpy(n, beta)


def _i0(x: np.ndarray) -> np.ndarray:
    """Modified Bessel function I₀ (series), vectorized for Kaiser fallback."""
    # Sufficient accuracy for typical Kaiser β ≤ ~20
    t = np.asarray(x, dtype=np.float64)
    y = t * t / 4.0
    acc = np.ones_like(t)
    term = np.ones_like(t)
    for k in range(1, 40):
        term *= y / (k * k)
        acc += term
        if np.all(term < 1e-15 * acc):
            break
    return acc


def _kaiser_numpy(n: int, beta: float) -> np.ndarray:
    """NumPy Kaiser: w[i] = I₀(β √(1 − ((i−α)/α)²)) / I₀(β), α = (n−1)/2."""
    alpha = (n - 1) / 2.0
    i = np.arange(n, dtype=np.float64)
    t = (i - alpha) / alpha
    # numerical guard at endpoints
    inside = np.clip(1.0 - t * t, 0.0, 1.0)
    return _i0(beta * np.sqrt(inside)) / _i0(np.array(beta, dtype=np.float64))


def step1_window(
    n: int,
    dt: float,
    beta: float = KAISER_BETA,
    mod_period: float = MODULATION_PERIOD_S,
) -> np.ndarray:
    """
    R-FFT-539.9 Step 1 window: Kaiser(β) further modulated by a cosine
    at period ``mod_period`` (default ~5 s).
    """
    w = kaiser_window(n, beta)
    t = np.arange(n, dtype=np.float64) * float(dt)
    if mod_period > 0:
        w = w * np.cos(2.0 * np.pi * t / mod_period)
    return w


# ---------------------------------------------------------------------------
# Resonant structure (model-side; optional precondition only)
# ---------------------------------------------------------------------------

def phi_attractor(t: np.ndarray, g4: float = G4) -> np.ndarray:
    """
    Resonant attractor
        Φ(t) = Φ₀ + 0.90 cos(2π t / G₄) + (11/61) sin(2π t / G₄)
    """
    omega = 2.0 * np.pi / g4
    return PHI_0 + A_COS * np.cos(omega * t) + A_SIN * np.sin(omega * t)


def phi_velocity(t: np.ndarray, g4: float = G4) -> np.ndarray:
    """Phase-lock velocity Φ'(t) from the closed attractor."""
    omega = 2.0 * np.pi / g4
    return omega * (-A_COS * np.sin(omega * t) + A_SIN * np.cos(omega * t))


def resonant_precondition(
    series: np.ndarray,
    dt: float,
    g4: float = G4,
    beta_pbh: float = BETA_PBH,
    apply_phase_lock: bool = True,
    apply_amplitude: bool = True,
) -> np.ndarray:
    """
    Model-tuned preconditioning that **injects G₄ structure**.

    - Complex / quadrature phase lock via multiplication by e^{i 2π t / G₄}
      (implemented on the real series as a G₄-locked quadrature mix).
    - Optional β_PBH-scaled amplitude envelope from |Φ(t)| structure.

    WARNING: Using this before spectral estimation privileges frequency 1/G₄.
    Do **not** report refined periods from preconditioned runs as free discovery.
    """
    x = np.asarray(series, dtype=np.float64).copy()
    n = len(x)
    t = np.arange(n, dtype=np.float64) * float(dt)

    if apply_amplitude:
        # Mild amplitude structure proportional to attractor magnitude scale
        amp = 1.0 + beta_pbh * phi_attractor(t, g4=g4)
        x = x * amp

    if apply_phase_lock:
        # Quadrature mix locked to G₄ (real-valued output)
        phase = 2.0 * np.pi * t / g4
        x = x * np.cos(phase) + np.roll(x, 1) * np.sin(phase) * beta_pbh

    return x


# ---------------------------------------------------------------------------
# Core spectral primitives
# ---------------------------------------------------------------------------

def linear_detrend(y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Least-squares linear detrend. Returns (detrended, trend)."""
    y = np.asarray(y, dtype=np.float64)
    n = len(y)
    if n < 2:
        return y.copy(), np.zeros_like(y)
    t = np.arange(n, dtype=np.float64)
    A = np.column_stack([np.ones(n), t])
    coef, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
    trend = A @ coef
    return y - trend, trend


def zero_padded_fft(
    y: np.ndarray,
    nfft: int | None = None,
    nfft_factor: int = NFFT_FACTOR,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    FFT with optional zero-padding. Returns (freqs_hz_units, X_complex, power).

    Frequency axis uses sample spacing ``d=1`` in index units; convert with
    ``freqs / dt`` for physical Hertz when ``dt`` is the sample period.
    """
    y = np.asarray(y, dtype=np.float64)
    n = len(y)
    if nfft is None:
        nfft = max(n * int(nfft_factor), n)
    nfft = int(nfft)
    X = np.fft.fft(y, n=nfft)
    # fftshift-style axis for full spectrum bookkeeping
    freqs = np.fft.fftfreq(nfft, d=1.0)
    power = np.abs(X) ** 2
    return freqs, X, power


def power_at_frequency(
    freqs: np.ndarray,
    power: np.ndarray,
    target_f: float,
) -> tuple[float, int, float]:
    """
    Squared-magnitude power at the bin nearest ``target_f`` (in the same
    units as ``freqs``). Returns (power_value, bin_index, bin_frequency).
    """
    # Prefer non-negative frequencies when target_f ≥ 0
    if target_f >= 0:
        mask = freqs >= 0
        if not np.any(mask):
            mask = np.ones_like(freqs, dtype=bool)
        idx_local = int(np.argmin(np.abs(freqs[mask] - target_f)))
        idx = int(np.flatnonzero(mask)[idx_local])
    else:
        idx = int(np.argmin(np.abs(freqs - target_f)))
    return float(power[idx]), idx, float(freqs[idx])


def snr_mean_spectrum(power_target: float, power: np.ndarray) -> float:
    """
    snr_5399-style score: target power / mean(|X|²) over the full spectrum.

    Note: this is **not** a median noise-floor estimator.
    """
    mean_p = float(np.mean(power))
    if mean_p <= 0.0:
        return float("nan")
    return float(power_target / mean_p)


def quadratic_peak_refine(
    freqs: np.ndarray,
    power: np.ndarray,
    target_f: float,
    max_iter: int = REFINE_MAX_ITER,
    tol: float = REFINE_TOL,
) -> tuple[float, float]:
    """
    Iterative three-bin quadratic interpolation on spectral power near
    ``target_f``. Returns (refined_f, refined_period = 1/refined_f).
    """
    # Work on non-negative frequencies, sorted
    mask = freqs >= 0
    f = freqs[mask]
    p = power[mask]
    order = np.argsort(f)
    f = f[order]
    p = p[order]
    if len(f) < 3:
        return float(target_f), (1.0 / target_f if target_f != 0 else float("nan"))

    # Start at nearest bin to target
    k = int(np.argmin(np.abs(f - target_f)))
    k = max(1, min(k, len(f) - 2))
    refined = float(f[k])

    for _ in range(max_iter):
        k = int(np.argmin(np.abs(f - refined)))
        k = max(1, min(k, len(f) - 2))
        f0, f1, f2 = float(f[k - 1]), float(f[k]), float(f[k + 1])
        y0, y1, y2 = float(p[k - 1]), float(p[k]), float(p[k + 1])
        # Standard 3-point parabola peak (uniform-bin form + uneven correction)
        denom = (y0 - 2.0 * y1 + y2)
        if abs(denom) < 1e-30:
            break
        # bin offset in index units
        delta = 0.5 * (y0 - y2) / denom
        delta = float(np.clip(delta, -1.0, 1.0))
        # interpolate frequency assuming local bin spacing
        df = 0.5 * ((f1 - f0) + (f2 - f1))
        new_f = f1 + delta * df
        if abs(new_f - refined) < tol:
            refined = new_f
            break
        refined = new_f

    if refined <= 0.0:
        return refined, float("nan")
    return refined, 1.0 / refined


def free_spectrum_peak(
    y: np.ndarray,
    dt: float,
    nfft: int | None = None,
    nfft_factor: int = NFFT_FACTOR,
    exclude_dc: bool = True,
) -> tuple[float, float, float, np.ndarray, np.ndarray, np.ndarray]:
    """
    Dominant peak on the natural (zero-padded) grid — **no G₄ reference**.

    Returns
    -------
    T_hat, f_hat, peak_power, freqs_phys, X, power
    """
    freqs_idx, X, power = zero_padded_fft(y, nfft=nfft, nfft_factor=nfft_factor)
    freqs_phys = freqs_idx / float(dt)  # Hz if dt in seconds

    mask = freqs_phys > 0 if exclude_dc else freqs_phys >= 0
    if not np.any(mask):
        return float("nan"), float("nan"), float("nan"), freqs_phys, X, power

    idx = int(np.flatnonzero(mask)[np.argmax(power[mask])])
    f_hat = float(freqs_phys[idx])
    peak_power = float(power[idx])
    T_hat = 1.0 / f_hat if f_hat > 0 else float("nan")
    return T_hat, f_hat, peak_power, freqs_phys, X, power


def phase_randomise(
    y: np.ndarray,
    rng: np.random.Generator,
) -> np.ndarray:
    """Phase-randomisation surrogate: keep |DFT|, scramble phases."""
    y = np.asarray(y, dtype=np.float64)
    n = len(y)
    spec = np.fft.rfft(y)
    mag = np.abs(spec)
    phases = rng.uniform(0.0, 2.0 * np.pi, size=len(mag))
    phases[0] = 0.0
    if n % 2 == 0:
        phases[-1] = 0.0
    return np.fft.irfft(mag * np.exp(1j * phases), n=n)


def subharmonic_powers(
    freqs: np.ndarray,
    power: np.ndarray,
    ladder: tuple[float, ...] = SUBHARMONIC_LADDER,
) -> dict[str, float]:
    """Power at bins nearest 1/T for each ladder period T (seconds)."""
    out: dict[str, float] = {}
    for T in ladder:
        if T <= 0:
            continue
        p, _, fbin = power_at_frequency(freqs, power, 1.0 / T)
        out[f"power_T{T:g}"] = p
        out[f"bin_f_T{T:g}"] = fbin
    return out


# ---------------------------------------------------------------------------
# Results container
# ---------------------------------------------------------------------------

@dataclass
class RFFTResult:
    """Structured return of full_r_fft_analysis."""

    # Modes
    precondition: bool
    scrambled_g4_control: bool
    g4: float
    dt: float
    n: int
    nfft: int

    # Target-bin metrics (model frequency 1/G₄)
    power_5399: float
    snr_5399: float
    target_f: float
    target_bin_f: float

    # Refined peak near model target (secondary when preconditioned)
    refined_f: float
    refined_period: float

    # Free (unpreconditioned path still reports free peak of the series fed in)
    free_T_hat: float
    free_f_hat: float
    free_peak_power: float

    # Model / report extras
    echo_amplitude: float  # A_SIN ≡ β_PBH closed form
    echo_beta: float  # BETA_PBH
    mu_stability: float  # MU ledger value (framework constant, not estimated)
    kappa_dark: float
    subharmonic_power: dict[str, float] = field(default_factory=dict)

    # Null diagnostics (optional)
    null_mean_power_5399: float | None = None
    null_mean_snr_5399: float | None = None
    null_fraction_exceeding: float | None = None
    n_null: int = 0

    # Provenance flags
    discovery_claim_allowed: bool = False
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


# ---------------------------------------------------------------------------
# Full analysis entry point
# ---------------------------------------------------------------------------

def full_r_fft_analysis(
    series: np.ndarray,
    dt: float = 1.0,
    *,
    precondition: bool = False,
    scrambled_g4_control: bool = False,
    g4: float = G4,
    kaiser_beta: float = KAISER_BETA,
    mod_period: float = MODULATION_PERIOD_S,
    nfft: int | None = None,
    nfft_factor: int = NFFT_FACTOR,
    detrend: bool = True,
    n_null: int = 0,
    rng: np.random.Generator | None = None,
    seed: int | None = 0,
) -> RFFTResult:
    """
    Full R-FFT-539.9 analysis pipeline.

    Parameters
    ----------
    series :
        Real-valued time series (evenly sampled with period ``dt``).
    dt :
        Sample period in seconds.
    precondition :
        If True, apply G₄-locked resonant preconditioning **before** the FFT.
        This is a **secondary / compatibility** mode only.
    scrambled_g4_control :
        If True, replace the (possibly preconditioned) series with a
        phase-randomised surrogate before windowing/FFT. Preserves spectral
        magnitude shape; destroys coherent G₄ phase.
    g4 :
        Model period (default 539.9). Explicit; never an unbound name.
    n_null :
        If > 0, run this many phase-scramble nulls and report mean power/SNR
        at 1/G₄ and the fraction exceeding the observed power_5399.
    seed :
        RNG seed when ``rng`` is not provided.

    Returns
    -------
    RFFTResult
        Includes power_5399, snr_5399, refined_period, free peak metrics,
        sub-harmonic powers, and ledger constants (echo_beta, mu_stability, …).

    Discovery policy
    ----------------
    ``discovery_claim_allowed`` is True **only** when
    ``precondition is False`` and ``scrambled_g4_control is False``.
    Even then, free_T_hat is the primary period estimate; power_5399 is
    a secondary compatibility score against the model frequency.
    """
    if rng is None:
        rng = np.random.default_rng(seed)

    x0 = np.asarray(series, dtype=np.float64).ravel()
    n = len(x0)
    if n < 4:
        raise ValueError("series must have length >= 4")

    notes: list[str] = []

    # Optional model precondition (injects G₄)
    x = x0
    if precondition:
        x = resonant_precondition(x, dt=dt, g4=g4)
        notes.append(
            "precondition=True: G₄ structure injected; refined_period is NOT "
            "an independent discovery statistic."
        )

    # Scrambled-G4 control (phase-randomise the series fed to the FFT)
    if scrambled_g4_control:
        if detrend:
            x, _ = linear_detrend(x)
            detrend = False  # already detrended
        x = phase_randomise(x, rng)
        notes.append(
            "scrambled_g4_control=True: phase-randomised surrogate; "
            "coherent G₄ phase destroyed, |spectrum| shape preserved."
        )

    if detrend:
        x, _ = linear_detrend(x)

    if nfft is None:
        nfft = max(n * int(nfft_factor), n)

    # Free discovery path: Kaiser only — NO 5 s cosine modulation and NO
    # privileged bin at 1/G₄. The ~5 s Step-1 modulation is model ladder
    # structure; applying it would pollute free_T_hat toward T≈5.
    w_free = kaiser_window(n, kaiser_beta)
    xw_free = x * w_free
    free_T, free_f, free_p, _, _, _ = free_spectrum_peak(
        xw_free, dt=dt, nfft=nfft, nfft_factor=nfft_factor,
    )

    # Documented R-FFT Step 1 for model-target metrics: Kaiser × cos(~5 s)
    w = step1_window(n, dt=dt, beta=kaiser_beta, mod_period=mod_period)
    xw = x * w

    freqs_idx, X, power = zero_padded_fft(xw, nfft=nfft, nfft_factor=nfft_factor)
    freqs_phys = freqs_idx / float(dt)

    target_f = 1.0 / float(g4)
    power_5399, _, target_bin_f = power_at_frequency(freqs_phys, power, target_f)
    snr = snr_mean_spectrum(power_5399, power)

    refined_f, refined_period = quadratic_peak_refine(
        freqs_phys, power, target_f,
        max_iter=REFINE_MAX_ITER, tol=REFINE_TOL,
    )

    sub_p = subharmonic_powers(freqs_phys, power)

    # Optional phase-scramble null ensemble on the *pre-null* windowed path
    null_mean_p: float | None = None
    null_mean_snr: float | None = None
    null_frac: float | None = None
    if n_null > 0:
        # Build nulls from the series after detrend/precondition but before
        # the scrambled_g4_control flag (i.e. re-scramble from a clean copy)
        base = np.asarray(series, dtype=np.float64).ravel()
        if precondition:
            base = resonant_precondition(base, dt=dt, g4=g4)
        base, _ = linear_detrend(base)
        null_powers = np.empty(n_null, dtype=np.float64)
        null_snrs = np.empty(n_null, dtype=np.float64)
        w_null = step1_window(n, dt=dt, beta=kaiser_beta, mod_period=mod_period)
        for i in range(n_null):
            surr = phase_randomise(base, rng)
            sw = surr * w_null
            _, _, p_s = zero_padded_fft(sw, nfft=nfft, nfft_factor=nfft_factor)
            f_s = np.fft.fftfreq(int(nfft), d=1.0) / float(dt)
            p539, _, _ = power_at_frequency(f_s, p_s, target_f)
            null_powers[i] = p539
            null_snrs[i] = snr_mean_spectrum(p539, p_s)
        null_mean_p = float(np.mean(null_powers))
        null_mean_snr = float(np.mean(null_snrs))
        null_frac = float(np.mean(null_powers >= power_5399))
        notes.append(
            f"phase-scramble nulls: n_null={n_null}, "
            f"fraction with power_5399 >= observed = {null_frac:.4f}"
        )

    discovery_ok = (not precondition) and (not scrambled_g4_control)
    if discovery_ok:
        notes.append(
            "discovery_claim_allowed=True only for free peak free_T_hat / "
            "free_f_hat; power_5399 remains a secondary model-compatibility score."
        )
    else:
        notes.append(
            "discovery_claim_allowed=False: precondition or scrambled control "
            "active — do not claim unsupervised discovery of G₄."
        )

    return RFFTResult(
        precondition=precondition,
        scrambled_g4_control=scrambled_g4_control,
        g4=float(g4),
        dt=float(dt),
        n=n,
        nfft=int(nfft),
        power_5399=float(power_5399),
        snr_5399=float(snr),
        target_f=float(target_f),
        target_bin_f=float(target_bin_f),
        refined_f=float(refined_f),
        refined_period=float(refined_period),
        free_T_hat=float(free_T),
        free_f_hat=float(free_f),
        free_peak_power=float(free_p),
        echo_amplitude=float(A_SIN),
        echo_beta=float(BETA_PBH),
        mu_stability=float(MU),
        kappa_dark=float(KAPPA_DARK),
        subharmonic_power=sub_p,
        null_mean_power_5399=null_mean_p,
        null_mean_snr_5399=null_mean_snr,
        null_fraction_exceeding=null_frac,
        n_null=int(n_null),
        discovery_claim_allowed=discovery_ok,
        notes=notes,
    )


def compare_precondition_modes(
    series: np.ndarray,
    dt: float = 1.0,
    *,
    n_null: int = 64,
    seed: int = 0,
    **kwargs: Any,
) -> dict[str, Any]:
    """
    Side-by-side free vs preconditioned vs scrambled-G4 control.

    Returns a dict with keys free / preconditioned / scrambled and a short
    summary emphasising that only free is eligible for discovery claims.
    """
    rng = np.random.default_rng(seed)
    free = full_r_fft_analysis(
        series, dt=dt, precondition=False, scrambled_g4_control=False,
        n_null=n_null, rng=rng, **kwargs,
    )
    pre = full_r_fft_analysis(
        series, dt=dt, precondition=True, scrambled_g4_control=False,
        n_null=0, rng=rng, **kwargs,
    )
    scr = full_r_fft_analysis(
        series, dt=dt, precondition=True, scrambled_g4_control=True,
        n_null=0, rng=rng, **kwargs,
    )
    return {
        "free": free.to_dict(),
        "preconditioned": pre.to_dict(),
        "scrambled_g4": scr.to_dict(),
        "summary": {
            "primary_period_estimate": free.free_T_hat,
            "primary_discovery_allowed": free.discovery_claim_allowed,
            "power_5399_free": free.power_5399,
            "power_5399_preconditioned": pre.power_5399,
            "power_5399_scrambled": scr.power_5399,
            "snr_5399_free": free.snr_5399,
            "snr_5399_preconditioned": pre.snr_5399,
            "snr_5399_scrambled": scr.snr_5399,
            "null_fraction_exceeding_free": free.null_fraction_exceeding,
            "warning": (
                "Do not treat preconditioned refined_period ≈ G₄ as unsupervised "
                "discovery. Compare free peak and phase-scramble nulls first."
            ),
        },
    }


# ---------------------------------------------------------------------------
# Demo signal + CLI
# ---------------------------------------------------------------------------

def demo_series(
    n: int = 8192,
    dt: float = 1.0,
    period: float = G4,
    snr: float = 2.0,
    seed: int = 0,
) -> np.ndarray:
    """Synthetic series with optional buried G₄ tone + noise (for smoke tests)."""
    rng = np.random.default_rng(seed)
    t = np.arange(n, dtype=np.float64) * dt
    signal = A_COS * np.cos(2.0 * np.pi * t / period) + A_SIN * np.sin(
        2.0 * np.pi * t / period
    )
    noise = rng.normal(0.0, 1.0, size=n)
    # scale signal so power ratio ≈ snr (rough)
    sig_std = float(np.std(signal)) or 1.0
    signal = signal / sig_std * snr
    return signal + noise


def _print_result(label: str, r: RFFTResult) -> None:
    print(f"\n=== {label} ===")
    print(f"  discovery_claim_allowed : {r.discovery_claim_allowed}")
    print(f"  free_T_hat              : {r.free_T_hat:.6g}")
    print(f"  free_f_hat              : {r.free_f_hat:.6g}")
    print(f"  power_5399              : {r.power_5399:.6g}")
    print(f"  snr_5399                : {r.snr_5399:.6g}")
    print(f"  refined_period          : {r.refined_period:.6g}")
    print(f"  echo_beta (β_PBH)       : {r.echo_beta:.6g}")
    print(f"  mu_stability            : {r.mu_stability}")
    if r.null_fraction_exceeding is not None:
        print(f"  null_fraction_exceeding : {r.null_fraction_exceeding:.4f}")
    for note in r.notes:
        print(f"  note: {note}")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="R-FFT-539.9 resonant FFT analysis")
    p.add_argument("--demo", action="store_true", help="Run synthetic demo")
    p.add_argument("--N", type=int, default=8192, help="Demo series length")
    p.add_argument("--dt", type=float, default=1.0, help="Sample period (s)")
    p.add_argument("--n-null", type=int, default=32, help="Phase-scramble nulls")
    p.add_argument("--seed", type=int, default=0)
    p.add_argument(
        "--json-out",
        type=Path,
        default=None,
        help="Write compare_precondition_modes JSON to this path",
    )
    args = p.parse_args(argv)

    if not args.demo and args.json_out is None:
        # default: demo
        args.demo = True

    series = demo_series(n=args.N, dt=args.dt, seed=args.seed)
    cmp = compare_precondition_modes(
        series, dt=args.dt, n_null=args.n_null, seed=args.seed,
    )

    _print_result("FREE (primary)", RFFTResult(**{
        k: v for k, v in cmp["free"].items()
    }))
    _print_result("PRECONDITIONED (secondary)", RFFTResult(**{
        k: v for k, v in cmp["preconditioned"].items()
    }))
    _print_result("SCRAMBLED-G4 CONTROL", RFFTResult(**{
        k: v for k, v in cmp["scrambled_g4"].items()
    }))

    print("\n=== SUMMARY ===")
    for k, v in cmp["summary"].items():
        print(f"  {k}: {v}")

    if args.json_out is not None:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(cmp, indent=2), encoding="utf-8")
        print(f"\nWrote {args.json_out}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
