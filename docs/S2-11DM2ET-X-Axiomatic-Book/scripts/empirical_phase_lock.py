#!/usr/bin/env python3
"""
Empirical phase-locking investigation (protocol-compliant).

- Dynamics: T^sharp (min-defect charge completion) or unrestricted T3
- Period estimate: ordinary periodogram on natural DFT grid after linear detrend
- Horizon N pre-declared (power of two); NOT tuned to 539
- Bootstrap residual, B=2000 default; no reweighting by 539.9
- Compatibility with 539.9 ONLY after T_hat and bootstrap are recorded

Usage:
  python empirical_phase_lock.py
  python empirical_phase_lock.py --N 4096 --seeds 64 --B 500 --map sharp
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np

# Claimed value — used ONLY in post-estimation compatibility (never in estimator)
CLAIMED_PERIOD = 539.9


# ---------------------------------------------------------------------------
# Maps
# ---------------------------------------------------------------------------

def T3(n: int) -> int:
    """Unrestricted ternary Syracuse (floor form)."""
    if n <= 0:
        return 0
    r = n % 3
    if r == 0:
        return n // 3
    if r == 1:
        return (4 * n + 2) // 3
    return (2 * n + 1) // 3


def T_corr(n: int, k: int) -> int:
    return (n + 1) // 3 + 2 * (3**k)


def min_k_preserve(n: int) -> int | None:
    target = n % 9
    for k in range(0, 5):
        if T_corr(n, k) % 9 == target:
            return k
    return None


def charge_defect(n: int, k: int) -> int:
    d = abs(T_corr(n, k) % 9 - n % 9)
    return min(d, 9 - d)


def k_delta(n: int) -> int:
    defs = sorted((charge_defect(n, k), k) for k in range(3))
    return defs[0][1]


def T_sharp(n: int) -> int:
    """Min-defect completed map (protocol T^sharp)."""
    if n <= 0:
        return 0
    r = n % 3
    if r == 0:
        return n // 3
    if r == 1:
        return (4 * n + 2) // 3
    mk = min_k_preserve(n)
    if mk is not None:
        return T_corr(n, mk)
    return T_corr(n, k_delta(n))


def iterate(map_fn, seed: int, N: int) -> np.ndarray:
    n = int(seed)
    out = np.empty(N, dtype=np.float64)
    for t in range(N):
        out[t] = float(n)
        n = map_fn(n)
        if n < 0:
            n = 0
    return out


# ---------------------------------------------------------------------------
# Phase observable (pre-declared; no 539)
# ---------------------------------------------------------------------------

def phase_observable(traj: np.ndarray) -> np.ndarray:
    """
    Pre-declared feature: fractional part of log3(n+1) residual after
    removing the mean linear drift in log-space is handled later by detrend.
    Also mix modular coordinate mod 27 (period of k-law), independent of 539.
    """
    n = np.maximum(traj, 1.0)
    # log3 magnitude
    log3 = np.log(n) / math.log(3.0)
    # modular: n mod 27 in [-0.5, 0.5]
    mod = (n % 27.0) / 27.0 - 0.5
    # combine (fixed weights, pre-declared)
    return log3 + 0.35 * mod


def linear_detrend(y: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return (detrended, trend, residuals)."""
    t = np.arange(len(y), dtype=np.float64)
    # least squares: y = a + b t
    A = np.column_stack([np.ones_like(t), t])
    coef, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
    trend = A @ coef
    resid = y - trend
    return resid, trend, resid


# ---------------------------------------------------------------------------
# Periodogram on natural DFT grid (no privileged bin at 1/539.9)
# ---------------------------------------------------------------------------

def periodogram_peak(y: np.ndarray) -> tuple[float, float, np.ndarray, np.ndarray]:
    """
    Ordinary periodogram after input is already detrended.
    Returns (T_hat, f_hat, freqs, power).
    """
    N = len(y)
    # rfft: frequencies k/N for k=0..N//2
    spec = np.fft.rfft(y)
    power = (spec.real**2 + spec.imag**2) / N
    freqs = np.fft.rfftfreq(N, d=1.0)  # f_k = k/N
    # exclude DC (k=0)
    if len(freqs) < 2:
        return float("nan"), float("nan"), freqs, power
    k_star = 1 + int(np.argmax(power[1:]))
    f_hat = float(freqs[k_star])
    if f_hat <= 0:
        return float("nan"), f_hat, freqs, power
    T_hat = 1.0 / f_hat
    return T_hat, f_hat, freqs, power


def residual_bootstrap_periods(
    trend: np.ndarray,
    resid: np.ndarray,
    B: int,
    rng: np.random.Generator,
) -> np.ndarray:
    """Basic residual bootstrap; same N, natural DFT grid; no 539.9."""
    N = len(resid)
    boots = np.empty(B, dtype=np.float64)
    for b in range(B):
        r_star = rng.choice(resid, size=N, replace=True)
        y_b = trend + r_star
        # re-detrend lightly for stability (protocol allows residual bootstrap on fixed trend)
        y_b, _, _ = linear_detrend(y_b)
        T_b, _, _, _ = periodogram_peak(y_b)
        boots[b] = T_b
    return boots


def percentile_ci(samples: np.ndarray, alpha: float = 0.05) -> tuple[float, float]:
    s = samples[np.isfinite(samples)]
    if len(s) == 0:
        return float("nan"), float("nan")
    lo = float(np.quantile(s, alpha / 2))
    hi = float(np.quantile(s, 1 - alpha / 2))
    return lo, hi


def phase_randomisation_pvalue(
    y: np.ndarray,
    observed_peak_power: float,
    B: int,
    rng: np.random.Generator,
) -> float:
    """Null: phase-randomised surrogates; p = fraction with peak power >= observed."""
    N = len(y)
    spec = np.fft.rfft(y)
    mag = np.abs(spec)
    count = 0
    for _ in range(B):
        phases = rng.uniform(0, 2 * np.pi, size=len(mag))
        # keep DC real
        phases[0] = 0.0
        if N % 2 == 0:
            phases[-1] = 0.0  # Nyquist real for even N
        surr = np.fft.irfft(mag * np.exp(1j * phases), n=N)
        surr, _, _ = linear_detrend(surr)
        _, _, _, power = periodogram_peak(surr)
        peak = float(np.max(power[1:])) if len(power) > 1 else 0.0
        if peak >= observed_peak_power:
            count += 1
    return (count + 1) / (B + 1)


# ---------------------------------------------------------------------------
# Compatibility (POST only)
# ---------------------------------------------------------------------------

def compatibility(
    T_hat: float,
    ci_lo: float,
    ci_hi: float,
    claimed: float = CLAIMED_PERIOD,
    delta: float | None = None,
) -> dict:
    """Optional hypothesis check — only after estimation."""
    in_ci = bool(ci_lo <= claimed <= ci_hi) if np.isfinite(ci_lo) else False
    abs_err = abs(T_hat - claimed) if np.isfinite(T_hat) else float("nan")
    out = {
        "claimed": claimed,
        "T_hat": T_hat,
        "abs_error": abs_err,
        "claimed_in_95pct_CI": in_ci,
        "ci": [ci_lo, ci_hi],
    }
    if delta is not None:
        out["within_delta"] = bool(abs_err <= delta)
        out["delta"] = delta
    return out


# ---------------------------------------------------------------------------
# Main experiment
# ---------------------------------------------------------------------------

@dataclass
class SeedResult:
    seed: int
    T_hat: float
    f_hat: float
    ci_lo: float
    ci_hi: float
    peak_pvalue: float
    peak_power: float


def run_seed(
    seed: int,
    map_fn,
    N: int,
    B: int,
    B_null: int,
    rng: np.random.Generator,
) -> SeedResult:
    traj = iterate(map_fn, seed, N)
    phi = phase_observable(traj)
    detrended, trend, resid = linear_detrend(phi)
    T_hat, f_hat, freqs, power = periodogram_peak(detrended)
    peak_power = float(np.max(power[1:])) if len(power) > 1 else 0.0

    boots = residual_bootstrap_periods(trend, resid, B, rng)
    ci_lo, ci_hi = percentile_ci(boots)

    pval = phase_randomisation_pvalue(detrended, peak_power, B_null, rng)

    return SeedResult(
        seed=seed,
        T_hat=T_hat,
        f_hat=f_hat,
        ci_lo=ci_lo,
        ci_hi=ci_hi,
        peak_pvalue=pval,
        peak_power=peak_power,
    )


def main() -> None:
    ap = argparse.ArgumentParser(description="Empirical phase-lock protocol (no 539.9 in estimator)")
    ap.add_argument("--N", type=int, default=4096, help="Horizon (power of two preferred); default 2^12")
    ap.add_argument("--seeds", type=int, default=48, help="Number of random seeds")
    ap.add_argument("--B", type=int, default=500, help="Bootstrap replicates (2000 for publication)")
    ap.add_argument("--B-null", type=int, default=200, help="Phase-randomisation surrogates for p-value")
    ap.add_argument("--map", choices=["sharp", "T3"], default="sharp")
    ap.add_argument("--seed0", type=int, default=20260726)
    ap.add_argument("--delta", type=float, default=None, help="Optional |T_hat-539.9|<=delta after estimation")
    ap.add_argument("--out", type=str, default="", help="JSON output path")
    args = ap.parse_args()

    map_fn = T_sharp if args.map == "sharp" else T3
    rng = np.random.default_rng(args.seed0)

    # Seeds: positive integers, not constructed from 539
    seeds = rng.integers(10**6, 10**12, size=args.seeds, dtype=np.int64)
    # Include a few fixed protocol seeds from tower types (20, 21 scale)
    fixed = np.array([20, 21, 243, 4880, 10**9 + 7, 2**31 - 1], dtype=np.int64)
    seeds = np.unique(np.concatenate([fixed, seeds]))

    results: list[SeedResult] = []
    for s in seeds:
        results.append(run_seed(int(s), map_fn, args.N, args.B, args.B_null, rng))

    T_hats = np.array([r.T_hat for r in results], dtype=np.float64)
    T_hats = T_hats[np.isfinite(T_hats)]

    # Aggregate primary estimate: median of per-seed T_hat
    T_med = float(np.median(T_hats)) if len(T_hats) else float("nan")
    T_mean = float(np.mean(T_hats)) if len(T_hats) else float("nan")
    # Ensemble bootstrap of the median (over seeds)
    ens_boot = []
    for _ in range(min(args.B, 1000)):
        sample = rng.choice(T_hats, size=len(T_hats), replace=True)
        ens_boot.append(float(np.median(sample)))
    ens_lo, ens_hi = percentile_ci(np.array(ens_boot))

    # PRIMARY report — still no claim about 539.9
    primary = {
        "map": args.map,
        "N": args.N,
        "n_seeds": len(results),
        "B_bootstrap": args.B,
        "B_null": args.B_null,
        "estimator": "ordinary periodogram after linear detrend; natural DFT grid",
        "phase_observable": "log3(n) + 0.35*((n mod 27)/27 - 0.5)",
        "T_hat_median": T_med,
        "T_hat_mean": T_mean,
        "ensemble_median_CI95": [ens_lo, ens_hi],
        "T_hat_per_seed_quantiles": {
            "q05": float(np.quantile(T_hats, 0.05)) if len(T_hats) else None,
            "q25": float(np.quantile(T_hats, 0.25)) if len(T_hats) else None,
            "q50": float(np.quantile(T_hats, 0.50)) if len(T_hats) else None,
            "q75": float(np.quantile(T_hats, 0.75)) if len(T_hats) else None,
            "q95": float(np.quantile(T_hats, 0.95)) if len(T_hats) else None,
        },
        "median_peak_pvalue": float(np.median([r.peak_pvalue for r in results])),
        "protocol_note": "539.9 not used in estimator, grid, horizon, or bootstrap",
    }

    # SECONDARY — compatibility only after primary is fixed
    compat = compatibility(T_med, ens_lo, ens_hi, CLAIMED_PERIOD, args.delta)
    # Also: fraction of seeds whose individual CI covers 539.9
    cover = sum(1 for r in results if r.ci_lo <= CLAIMED_PERIOD <= r.ci_hi)
    compat["fraction_seeds_CI_cover_claimed"] = cover / len(results)
    # Distance of median to claimed in units of ensemble CI half-width
    half = 0.5 * (ens_hi - ens_lo) if np.isfinite(ens_hi) else float("nan")
    compat["median_error_over_half_CI"] = (
        abs(T_med - CLAIMED_PERIOD) / half if half and half > 0 else float("nan")
    )

    report = {
        "primary": primary,
        "compatibility_post_estimation_only": compat,
        "per_seed": [asdict(r) for r in results[:20]],  # sample
        "n_per_seed_full": len(results),
        "ACE_reminder": "N_star=14 from contraction; 539 not forced by ACE/No-Go",
    }

    # Console summary
    print("=" * 64)
    print("EMPIRICAL PHASE-LOCK (protocol-compliant)")
    print("=" * 64)
    print(f"Map: {args.map}  N={args.N}  seeds={len(results)}  B={args.B}")
    print()
    print("--- PRIMARY (no use of 539.9) ---")
    print(f"  T_hat median = {T_med:.4f}")
    print(f"  T_hat mean   = {T_mean:.4f}")
    print(f"  Ensemble median 95% CI = [{ens_lo:.4f}, {ens_hi:.4f}]")
    print(f"  Per-seed T_hat quantiles: {primary['T_hat_per_seed_quantiles']}")
    print(f"  Median peak p-value (phase-rand) = {primary['median_peak_pvalue']:.4g}")
    print()
    print("--- COMPATIBILITY (post-estimation only) ---")
    print(f"  Claimed period = {CLAIMED_PERIOD}")
    print(f"  |T_hat - claimed| = {compat['abs_error']:.4f}")
    print(f"  Claimed in ensemble 95% CI? {compat['claimed_in_95pct_CI']}")
    print(f"  Fraction of seed CIs covering claimed: {compat['fraction_seeds_CI_cover_claimed']:.3f}")
    if args.delta is not None:
        print(f"  Within delta={args.delta}? {compat.get('within_delta')}")
    print()
    print("--- ACE / No-Go reminder ---")
    print("  Contraction N_star = 14; long resonant 539 not forced by residue/tower ACE.")
    print("  This run treats 539.9 only as a post-hoc hypothesis.")
    print("=" * 64)

    out = args.out
    if not out:
        out_dir = Path(__file__).resolve().parent.parent
        out = str(out_dir / "empirical_phase_lock_results.json")
    Path(out).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
