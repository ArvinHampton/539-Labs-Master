#!/usr/bin/env python3
"""
Holographic window investigation (model + empirical).

Model facts (HQH539_spec / KK tower notes):
  - COHERENT_WINDOW W = 18 (first 18 steps: holographic seeding phase)
  - 61 ω-punctures: holographic screen (ternary digits resolved before leak)
  - Threshold ~10^18 for full screen saturation
  - Spec: 18/521 split is theoretical; production applies T3 uniformly
  - Spec: natural termination ~374–506 steps (mean ~436); 539 is forced iteration

Empirical protocol: period estimate WITHOUT 539.9 in grid/horizon/bootstrap.
Optional compatibility with 18, 61, 539.9 only post-estimation.

Usage:
  python holographic_window_investigate.py
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

# Model integers that define the holographic construction (NOT 539.9 as estimator input)
W_COHERENT = 18  # trit coherent window
P_SCREEN = 61  # puncture / holographic screen digit count
# 539.9 only for post-hoc compatibility
CLAIMED_G4 = 539.9
CLAIMED_STEPS = 539


def T3(n: int) -> int:
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
    t = n % 9
    for k in range(5):
        if T_corr(n, k) % 9 == t:
            return k
    return None


def k_delta(n: int) -> int:
    def defect(k):
        d = abs(T_corr(n, k) % 9 - n % 9)
        return min(d, 9 - d)

    return min(range(3), key=lambda k: (defect(k), k))


def T_sharp(n: int) -> int:
    if n <= 0:
        return 0
    r = n % 3
    if r == 0:
        return n // 3
    if r == 1:
        return (4 * n + 2) // 3
    mk = min_k_preserve(n)
    return T_corr(n, mk if mk is not None else k_delta(n))


def iterate(map_fn, seed: int, N: int) -> np.ndarray:
    n = int(seed)
    out = np.empty(N, dtype=np.int64)
    for t in range(N):
        out[t] = n
        n = map_fn(max(n, 0))
    return out


def stopping_time(map_fn, seed: int, max_steps: int = 2000) -> int:
    """First t with n_t in {0,1}, or max_steps."""
    n = int(seed)
    for t in range(1, max_steps + 1):
        n = map_fn(max(n, 0))
        if n <= 1:
            return t
    return max_steps


def ternary_digits(n: int, width: int | None = None) -> list[int]:
    if n <= 0:
        digs = [0]
    else:
        digs = []
        x = int(n)
        while x:
            digs.append(x % 3)
            x //= 3
        digs.reverse()
    if width is not None:
        if len(digs) >= width:
            digs = digs[-width:]
        else:
            digs = [0] * (width - len(digs)) + digs
    return digs


def holographic_screen_value(n: int, width: int = P_SCREEN) -> float:
    """Project n onto last `width` ternary digits as base-3 fraction in [0,1)."""
    digs = ternary_digits(n, width=width)
    acc = 0.0
    for d in digs:
        acc = acc * 3.0 + d
    return acc / (3.0**width)


def phase_holographic_window(traj: np.ndarray, W: int = W_COHERENT) -> np.ndarray:
    """
    Rolling holographic window phase:
    for each t, use the W-step residue history (n_s mod 3) as a base-3 word,
    mapped to [0,1), then center to [-0.5,0.5].
    For t < W-1, pad with zeros (seeding phase incomplete).
    """
    N = len(traj)
    residues = traj % 3
    phi = np.empty(N, dtype=np.float64)
    for t in range(N):
        acc = 0
        for j in range(W):
            s = t - (W - 1 - j)
            r = int(residues[s]) if s >= 0 else 0
            acc = acc * 3 + r
        phi[t] = acc / (3.0**W) - 0.5
    return phi


def phase_screen_series(traj: np.ndarray, width: int = P_SCREEN) -> np.ndarray:
    """Per-step holographic screen coordinate (61-trit projection)."""
    return np.array([holographic_screen_value(int(n), width) - 0.5 for n in traj])


def phase_window_then_screen(traj: np.ndarray) -> np.ndarray:
    """Combine 18-window residue word with 61-screen (pre-declared weights)."""
    return 0.65 * phase_holographic_window(traj) + 0.35 * phase_screen_series(traj)


def linear_detrend(y: np.ndarray):
    t = np.arange(len(y), dtype=np.float64)
    A = np.column_stack([np.ones_like(t), t])
    coef, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
    trend = A @ coef
    return y - trend, trend, y - trend


def periodogram_peak(y: np.ndarray) -> tuple[float, float, float]:
    N = len(y)
    spec = np.fft.rfft(y)
    power = (spec.real**2 + spec.imag**2) / N
    freqs = np.fft.rfftfreq(N, d=1.0)
    if len(power) < 2:
        return float("nan"), float("nan"), 0.0
    k_star = 1 + int(np.argmax(power[1:]))
    f = float(freqs[k_star])
    T = 1.0 / f if f > 0 else float("nan")
    return T, f, float(power[k_star])


def residual_bootstrap_CI(trend, resid, B, rng) -> tuple[float, float, float]:
    N = len(resid)
    boots = []
    for _ in range(B):
        r_star = rng.choice(resid, size=N, replace=True)
        y_b, _, _ = linear_detrend(trend + r_star)
        Tb, _, _ = periodogram_peak(y_b)
        if np.isfinite(Tb):
            boots.append(Tb)
    if not boots:
        return float("nan"), float("nan"), float("nan")
    arr = np.array(boots)
    return (
        float(np.median(arr)),
        float(np.quantile(arr, 0.025)),
        float(np.quantile(arr, 0.975)),
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=4096)
    ap.add_argument("--seeds", type=int, default=40)
    ap.add_argument("--B", type=int, default=300)
    ap.add_argument("--map", choices=["sharp", "T3"], default="sharp")
    ap.add_argument("--seed0", type=int, default=5390018)  # not 539.9; arbitrary RNG seed
    args = ap.parse_args()

    map_fn = T_sharp if args.map == "sharp" else T3
    rng = np.random.default_rng(args.seed0)

    fixed = np.array(
        [
            20,
            21,
            243,
            4880,
            10**18,  # holographic threshold scale
            3**18 + 17,
            10**9 + 7,
        ],
        dtype=object,
    )
    # random big seeds
    rand = [int(rng.integers(10**10, 10**15)) for _ in range(args.seeds)]
    seeds = list(fixed) + rand

    # --- Analytic / model facts ---
    model = {
        "W_coherent": W_COHERENT,
        "P_screen": P_SCREEN,
        "3**18": 3**18,
        "log3(1e18)": math.log(1e18) / math.log(3),
        "HQCC_spec_note": (
            "Natural T3 stopping times ~374–506 (mean~436); "
            "539 is forced iteration / engineering choice; "
            "18-step holographic split is theoretical (no special op at step 17→18)"
        ),
        "composition_if_forced": "18 (window) + 1 (master) + 520 (towers) = 539 — inserts fixed counts",
    }

    # Natural stopping times (no forced 539)
    stops = [stopping_time(map_fn, int(s), max_steps=2000) for s in seeds]
    stop_stats = {
        "median": float(np.median(stops)),
        "mean": float(np.mean(stops)),
        "q05": float(np.quantile(stops, 0.05)),
        "q95": float(np.quantile(stops, 0.95)),
        "fraction_ge_539": float(np.mean([st >= CLAIMED_STEPS for st in stops])),
        "fraction_le_14": float(np.mean([st <= 14 for st in stops])),
    }

    # Spectral investigation for three phase constructions
    phase_builders = {
        "holo_window_W18": lambda tr: phase_holographic_window(tr, W_COHERENT),
        "holo_screen_P61": lambda tr: phase_screen_series(tr, P_SCREEN),
        "holo_window_plus_screen": phase_window_then_screen,
    }

    spectral = {}
    for name, builder in phase_builders.items():
        T_list = []
        cover_18 = cover_61 = cover_5399 = 0
        for s in seeds:
            traj = iterate(map_fn, int(s), args.N)
            # Continue past natural fixed point (forced-length style) by not stopping
            phi = builder(traj.astype(np.float64))
            det, trend, resid = linear_detrend(phi)
            T_hat, f_hat, peak_pow = periodogram_peak(det)
            med_b, lo, hi = residual_bootstrap_CI(trend, resid, args.B, rng)
            T_list.append(T_hat)
            if lo <= W_COHERENT <= hi:
                cover_18 += 1
            if lo <= P_SCREEN <= hi:
                cover_61 += 1
            if lo <= CLAIMED_G4 <= hi:
                cover_5399 += 1
        T_arr = np.array(T_list, dtype=np.float64)
        T_arr = T_arr[np.isfinite(T_arr)]
        T_med = float(np.median(T_arr))
        # ensemble median CI
        ens = [float(np.median(rng.choice(T_arr, size=len(T_arr), replace=True))) for _ in range(min(args.B, 500))]
        elo, ehi = float(np.quantile(ens, 0.025)), float(np.quantile(ens, 0.975))
        spectral[name] = {
            "T_hat_median": T_med,
            "T_hat_mean": float(np.mean(T_arr)),
            "ensemble_median_CI95": [elo, ehi],
            "quantiles": {
                "q05": float(np.quantile(T_arr, 0.05)),
                "q50": float(np.quantile(T_arr, 0.50)),
                "q95": float(np.quantile(T_arr, 0.95)),
            },
            "post_hoc_cover_fraction": {
                "18": cover_18 / len(seeds),
                "61": cover_61 / len(seeds),
                "539.9": cover_5399 / len(seeds),
            },
            "compat_median": {
                "abs_err_18": abs(T_med - W_COHERENT),
                "abs_err_61": abs(T_med - P_SCREEN),
                "abs_err_539.9": abs(T_med - CLAIMED_G4),
                "claimed_18_in_ens_CI": elo <= W_COHERENT <= ehi,
                "claimed_61_in_ens_CI": elo <= P_SCREEN <= ehi,
                "claimed_539.9_in_ens_CI": elo <= CLAIMED_G4 <= ehi,
            },
        }

    report = {
        "model_holographic_window": model,
        "map": args.map,
        "N": args.N,
        "n_seeds": len(seeds),
        "natural_stopping_time": stop_stats,
        "spectral_primary": spectral,
        "protocol": "539.9 not in estimator; 18 and 61 used only as pre-declared holographic constructions / post-hoc tests",
        "no_go_reminder": "Holographic window is an extra model constraint outside pure ACE contraction",
    }

    # Console
    print("=" * 68)
    print("HOLOGRAPHIC WINDOW INVESTIGATION")
    print("=" * 68)
    print(f"Model: W={W_COHERENT} coherent trits; P={P_SCREEN} screen digits")
    print(f"3^18 = {3**18}; log3(1e18) ≈ {model['log3(1e18)']:.3f}")
    print(f"Spec note: {model['HQCC_spec_note'][:100]}...")
    print()
    print("--- Natural stopping times (no forced 539) ---")
    print(f"  median={stop_stats['median']:.1f}  mean={stop_stats['mean']:.1f}")
    print(f"  q05–q95 = [{stop_stats['q05']:.0f}, {stop_stats['q95']:.0f}]")
    print(f"  fraction ≥ 539: {stop_stats['fraction_ge_539']:.3f}")
    print(f"  fraction ≤ 14 (ACE N_star): {stop_stats['fraction_le_14']:.3f}")
    print()
    print("--- Spectral (primary; no 539.9 in estimator) ---")
    for name, sp in spectral.items():
        print(f"  [{name}]")
        print(f"    T_hat median = {sp['T_hat_median']:.4f}")
        print(f"    ensemble CI  = {sp['ensemble_median_CI95']}")
        c = sp["compat_median"]
        print(
            f"    |err| vs 18,61,539.9 = "
            f"{c['abs_err_18']:.2f}, {c['abs_err_61']:.2f}, {c['abs_err_539.9']:.2f}"
        )
        print(
            f"    in CI? 18={c['claimed_18_in_ens_CI']}  "
            f"61={c['claimed_61_in_ens_CI']}  539.9={c['claimed_539.9_in_ens_CI']}"
        )
    print()
    print("--- Interpretation ---")
    print("  Holographic window (18) + screen (61) are model structures outside ACE.")
    print("  Forced 539 is engineering (spec); natural stopping is shorter.")
    print("  Long period 539.9 remains a hypothesis for spectral phase-lock tests.")
    print("=" * 68)

    out = Path(__file__).resolve().parent.parent / "holographic_window_results.json"
    # convert numpy types
    def conv(o):
        if isinstance(o, (np.floating, np.integer)):
            return o.item()
        raise TypeError

    out.write_text(json.dumps(report, indent=2, default=conv), encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
