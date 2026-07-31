#!/usr/bin/env python3
"""
L5 numerical diagnostic for RH pure Cat A track (upgraded).

- Continuous theta_x = arg P_x(sigma+it), U_x = log|P_x|, smoothed A_X
- Larger x_max; mpmath high precision for large t
- Off-line points = genuine local minima of |zeta| (grid scan), not fixed delta

DIAGNOSTIC ONLY — cannot prove RH.
No model constants (no G4, mu, E_leak, 539.9).

Status: RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF
See: RH_Target_Lemma_Sketch_Literature_L5.md Part III
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np

try:
    import mpmath as mp
except ImportError as e:
    raise SystemExit("mpmath required: pip install mpmath") from e

# First ordinates of nontrivial zeros on Re s = 1/2 (Odlyzko; public)
FIRST_ZERO_ORDINATES = [
    14.134725141734693,
    21.022039638771555,
    25.010857580145689,
    30.424876125859513,
    32.935061587739190,
    37.586178158825672,
    40.918719012147495,
    43.327073280914999,
    48.005150881167160,
    49.773832477672302,
    52.970321477714461,
    56.446247697063395,
    59.347044002602353,
    60.831778524609810,
    65.112544048081607,
    67.079810529494174,
    69.546401711173979,
    72.067157674481908,
    75.704690699083933,
    77.144840068874805,
]


def trap(y, x):
    fn = getattr(np, "trapezoid", None) or getattr(np, "trapz")
    return float(fn(y, x))


def sieve_primes(n: int) -> list[int]:
    if n < 2:
        return []
    n = int(n)
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0:2] = b"\x00\x00"
    r = int(n**0.5)
    for i in range(2, r + 1):
        if is_prime[i]:
            start = i * i
            step = i
            count = ((n - start) // step) + 1
            is_prime[start : n + 1 : step] = b"\x00" * count
    return [i for i in range(2, n + 1) if is_prime[i]]


def dps_for_t(t: float, base: int = 25) -> int:
    """Higher precision for larger |t| (phase of p^{-it} needs ~ log10(|t| log p) digits)."""
    # rough: need digits ~ 8 + log10(|t|) + a few for accumulation
    extra = max(0, int(math.log10(max(abs(t), 2.0)) + 5))
    return min(80, base + extra)


def factor_log_mp(p: int, sigma: float, t: float, dps: int) -> complex:
    """-log(1 - p^{-s}) with mpmath at given dps; return Python complex."""
    mp.mp.dps = dps
    s = mp.mpc(sigma, t)
    # log(1/(1-p^{-s})) = -log(1-p^{-s})
    w = 1 - mp.power(p, -s)
    lg = -mp.log(w)
    return complex(float(lg.real), float(lg.imag))


def cumulative_theta_U(
    primes: list[int], sigma: float, t: float, dps: int
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    theta[k], U[k] at x = p_k: continuous arg and log-modulus of P_x
    via sum of principal factor logs along prime order.
    """
    n = len(primes)
    theta = np.zeros(n, dtype=np.float64)
    U = np.zeros(n, dtype=np.float64)
    xs = np.zeros(n, dtype=np.float64)
    th = 0.0
    u = 0.0
    for k, p in enumerate(primes):
        dlog = factor_log_mp(p, sigma, t, dps)
        u += dlog.real
        th += dlog.imag
        theta[k] = th
        U[k] = u
        xs[k] = float(p)
    return xs, theta, U


def theta_at_x(
    xs: np.ndarray, theta: np.ndarray, U: np.ndarray, x: float
) -> tuple[float, float]:
    if x < xs[0]:
        return 0.0, 0.0
    i = int(np.searchsorted(xs, x, side="right") - 1)
    i = max(0, min(i, len(xs) - 1))
    return float(theta[i]), float(U[i])


def phi_bump(v: float) -> float:
    if v <= 1.0 or v >= 2.0:
        return 0.0
    w = (v - 1.0) * (2.0 - v)
    if w <= 0.0:
        return 0.0
    return math.exp(-1.0 / w)


def make_phi_normalized(n_quad: int = 64) -> tuple[np.ndarray, np.ndarray]:
    vs = np.linspace(1.0 + 1e-6, 2.0 - 1e-6, n_quad)
    raw = np.array([phi_bump(float(v)) for v in vs], dtype=np.float64)
    integ = trap(raw, vs)
    if integ <= 0:
        raise RuntimeError("phi normalization failed")
    return vs, raw / integ


def A_X_and_mean_U(
    xs: np.ndarray,
    theta: np.ndarray,
    U: np.ndarray,
    X: float,
    vs: np.ndarray,
    phi_density: np.ndarray,
) -> tuple[float, float]:
    if X <= math.e:
        raise ValueError("X must be > e")
    logX = math.log(X)
    theta_vals = np.empty(len(vs), dtype=np.float64)
    U_vals = np.empty(len(vs), dtype=np.float64)
    for j, v in enumerate(vs):
        x = math.exp(float(v) * logX)
        th, u = theta_at_x(xs, theta, U, x)
        theta_vals[j] = th
        U_vals[j] = u
    A = trap(theta_vals * phi_density, vs)
    Um = trap(U_vals * phi_density, vs)
    return A, Um


def zeta_abs(sigma: float, t: float, dps: int | None = None) -> float:
    dps = dps or dps_for_t(t)
    mp.mp.dps = dps
    z = mp.zeta(mp.mpc(sigma, t))
    return float(abs(z))


def scan_local_minima_abs_zeta(
    t_centers: list[float],
    sigma_lo: float = 0.60,
    sigma_hi: float = 0.92,
    n_sigma: int = 40,
    t_halfwidth: float = 2.5,
    n_t: int = 35,
    max_minima: int = 24,
    min_separation: float = 0.5,
    sigma_floor: float = 0.60,
) -> list[dict]:
    """
    Grid-scan |zeta| with sigma >= sigma_floor (strictly off the line).
    Keep 4-neighbor local minima + per-strip smallest cells; refine without
    crossing sigma_floor (prevents collapse onto nearby critical zeros).
    """
    sigmas = np.linspace(sigma_lo, sigma_hi, n_sigma)
    candidates: list[dict] = []

    for t0 in t_centers:
        ts = np.linspace(t0 - t_halfwidth, t0 + t_halfwidth, n_t)
        Z = np.full((len(sigmas), len(ts)), np.inf, dtype=np.float64)
        for i, sig in enumerate(sigmas):
            for j, tt in enumerate(ts):
                Z[i, j] = zeta_abs(float(sig), float(tt), dps=dps_for_t(float(tt), base=18))

        # (1) 4-neighbor local minima
        for i in range(1, len(sigmas) - 1):
            for j in range(1, len(ts) - 1):
                z0 = Z[i, j]
                if not math.isfinite(z0):
                    continue
                if (
                    z0 <= Z[i - 1, j]
                    and z0 <= Z[i + 1, j]
                    and z0 <= Z[i, j - 1]
                    and z0 <= Z[i, j + 1]
                ):
                    candidates.append(
                        {
                            "sigma": float(sigmas[i]),
                            "t": float(ts[j]),
                            "zeta_abs": float(z0),
                            "t_center": float(t0),
                            "kind": "local_min_4nbr",
                        }
                    )

        # (2) also: for each fixed sigma row, local min in t; for each t col, local min in sigma
        for i in range(len(sigmas)):
            for j in range(1, len(ts) - 1):
                z0 = Z[i, j]
                if math.isfinite(z0) and z0 <= Z[i, j - 1] and z0 <= Z[i, j + 1]:
                    candidates.append(
                        {
                            "sigma": float(sigmas[i]),
                            "t": float(ts[j]),
                            "zeta_abs": float(z0),
                            "t_center": float(t0),
                            "kind": "row_min_t",
                        }
                    )
        for j in range(len(ts)):
            for i in range(1, len(sigmas) - 1):
                z0 = Z[i, j]
                if math.isfinite(z0) and z0 <= Z[i - 1, j] and z0 <= Z[i + 1, j]:
                    candidates.append(
                        {
                            "sigma": float(sigmas[i]),
                            "t": float(ts[j]),
                            "zeta_abs": float(z0),
                            "t_center": float(t0),
                            "kind": "col_min_sigma",
                        }
                    )

        # (3) fallback top-4 smallest on strip
        flat = [
            (Z[i, j], i, j)
            for i in range(len(sigmas))
            for j in range(len(ts))
            if math.isfinite(Z[i, j])
        ]
        flat.sort(key=lambda x: x[0])
        for z0, i, j in flat[:4]:
            candidates.append(
                {
                    "sigma": float(sigmas[i]),
                    "t": float(ts[j]),
                    "zeta_abs": float(z0),
                    "t_center": float(t0),
                    "kind": "strip_smallest",
                }
            )

    # refine without crossing sigma_floor toward the critical line
    refined: list[dict] = []
    for c in candidates:
        sig, tt = c["sigma"], c["t"]
        if sig < sigma_floor:
            continue
        zbest = c["zeta_abs"]
        step_s, step_t = 0.012, 0.06
        for _ in range(10):
            improved = False
            for ds, dt in (
                (step_s, 0),
                (-step_s, 0),
                (0, step_t),
                (0, -step_t),
                (step_s, step_t),
                (-step_s, step_t),
                (step_s, -step_t),
                (-step_s, -step_t),
            ):
                s2 = sig + ds
                t2 = tt + dt
                if s2 < sigma_floor or s2 > 0.95:
                    continue
                z2 = zeta_abs(s2, t2, dps=dps_for_t(t2, base=20))
                if z2 < zbest * 0.999:  # require clear improvement
                    zbest, sig, tt = z2, s2, t2
                    improved = True
            if not improved:
                step_s *= 0.5
                step_t *= 0.5
                if step_s < 5e-4:
                    break
        refined.append(
            {
                "sigma": float(sig),
                "t": float(tt),
                "zeta_abs": float(zbest),
                "t_center": c["t_center"],
                "kind": c["kind"] + "+refine",
            }
        )

    refined.sort(key=lambda c: c["zeta_abs"])
    kept: list[dict] = []
    for c in refined:
        if c["sigma"] < sigma_floor - 1e-12 or not math.isfinite(c["zeta_abs"]):
            continue
        if any(
            abs(c["sigma"] - k["sigma"]) < 0.03 and abs(c["t"] - k["t"]) < min_separation
            for k in kept
        ):
            continue
        kept.append(c)
        if len(kept) >= max_minima:
            break
    return kept


def run_battery(
    primes: list[int],
    sigma: float,
    t: float,
    X_list: list[float],
    vs: np.ndarray,
    phi_density: np.ndarray,
    label: str,
    meta: dict | None = None,
) -> dict:
    dps = dps_for_t(t)
    xs, theta, U = cumulative_theta_U(primes, sigma, t, dps)
    zabs = zeta_abs(sigma, t, dps=dps)
    rows = []
    for X in X_list:
        if X > primes[-1]:
            continue
        A, Um = A_X_and_mean_U(xs, theta, U, X, vs, phi_density)
        th_X, U_X = theta_at_x(xs, theta, U, X)
        loglog = math.log(math.log(X)) if X > math.e else float("nan")
        rows.append(
            {
                "X": X,
                "theta_X": th_X,
                "U_X": U_X,
                "A_X": A,
                "U_mean_smooth": Um,
                "abs_A_over_loglog": abs(A) / loglog if loglog and loglog > 0 else None,
                "abs_theta_over_loglog": abs(th_X) / loglog if loglog and loglog > 0 else None,
            }
        )
    if rows:
        peak = max(rows, key=lambda r: abs(r["A_X"]))
        peak_abs_A = abs(peak["A_X"])
        peak_ratio = peak.get("abs_A_over_loglog")
        peak_X = peak["X"]
    else:
        peak_abs_A = peak_ratio = peak_X = None

    out = {
        "label": label,
        "sigma": sigma,
        "t": t,
        "dps": dps,
        "zeta_abs": zabs,
        "n_primes": len(primes),
        "x_max": float(primes[-1]),
        "theta_final": float(theta[-1]),
        "U_final": float(U[-1]),
        "peak_abs_A_X": peak_abs_A,
        "peak_abs_A_over_loglog": peak_ratio,
        "peak_X": peak_X,
        "X_grid": rows,
    }
    if meta:
        out["meta"] = meta
    return out


def mean_peak(rows: list[dict], key: str = "peak_abs_A_X") -> float | None:
    vals = [r[key] for r in rows if r.get(key) is not None]
    return float(np.mean(vals)) if vals else None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="L5 RH phase diagnostic (no RH claim)")
    ap.add_argument("--x-max", type=int, default=30000, help="sieve primes to this bound")
    ap.add_argument("--n-zeros", type=int, default=10, help="number of on-line zero ordinates")
    ap.add_argument("--max-minima", type=int, default=16, help="off-line |zeta| minima to keep")
    ap.add_argument(
        "--quick",
        action="store_true",
        help="smaller grid for faster smoke test (x_max=8000)",
    )
    args = ap.parse_args(argv)

    x_max = 8000 if args.quick else args.x_max
    n_zeros = min(args.n_zeros, len(FIRST_ZERO_ORDINATES))
    t_centers = FIRST_ZERO_ORDINATES[:n_zeros]

    # X grid up to x_max
    X_list = []
    lo = 3.0
    hi = math.log(x_max) - 0.08
    if hi <= lo:
        raise SystemExit("x_max too small")
    for v in np.linspace(lo, hi, 16):
        X_list.append(float(math.exp(v)))

    print(f"sieving primes to {x_max}...", flush=True)
    primes = sieve_primes(x_max)
    print(f"primes: {len(primes)}", flush=True)
    vs, phi_density = make_phi_normalized(56)

    # --- on-line battery ---
    print("on-line battery...", flush=True)
    results_online = []
    for t in t_centers:
        results_online.append(
            run_battery(
                primes,
                0.5,
                t,
                X_list,
                vs,
                phi_density,
                label=f"online_sigma=0.5_t={t:.6f}",
                meta={"kind": "critical_zero_ordinate"},
            )
        )
        print(f"  done t={t:.3f} dps={results_online[-1]['dps']}", flush=True)

    # --- off-line: genuine |zeta| local minima ---
    print("scanning |zeta| local minima off the line...", flush=True)
    minima = scan_local_minima_abs_zeta(
        t_centers=t_centers[: max(4, n_zeros // 2)],
        max_minima=args.max_minima if not args.quick else 8,
        n_sigma=18 if args.quick else 28,
        n_t=15 if args.quick else 21,
    )
    print(f"kept {len(minima)} minima", flush=True)

    results_offline = []
    for m in minima:
        lab = f"offline_min_sigma={m['sigma']:.4f}_t={m['t']:.4f}_z={m['zeta_abs']:.3e}"
        results_offline.append(
            run_battery(
                primes,
                m["sigma"],
                m["t"],
                X_list,
                vs,
                phi_density,
                label=lab,
                meta=m,
            )
        )
        print(f"  done {lab[:60]}...", flush=True)

    # branch warnings
    branch_warnings = []
    for r in results_online[:4] + results_offline[:4]:
        ths = [row["theta_X"] for row in r["X_grid"]]
        for a, b in zip(ths, ths[1:]):
            if abs(b - a) > math.pi:
                branch_warnings.append(
                    {"label": r["label"], "delta_theta": b - a, "note": "large theta jump"}
                )

    summary = {
        "n_online": len(results_online),
        "n_offline_minima": len(results_offline),
        "mean_peak_abs_A_online": mean_peak(results_online),
        "mean_peak_abs_A_offline_minima": mean_peak(results_offline),
        "mean_peak_abs_A_over_loglog_online": mean_peak(
            results_online, "peak_abs_A_over_loglog"
        ),
        "mean_peak_abs_A_over_loglog_offline_minima": mean_peak(
            results_offline, "peak_abs_A_over_loglog"
        ),
        "mean_zeta_abs_at_offline_minima": (
            float(np.mean([m["zeta_abs"] for m in minima])) if minima else None
        ),
        "interpretation": (
            "Finite-range diagnostic only. Offline points are grid-local minima of |zeta| "
            "off Re=1/2. Mild differences are inconclusive. NEVER claim RH from this output."
        ),
    }

    out = {
        "provenance": {
            "status_label": "RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF",
            "category": "A_diagnostic_only",
            "proves_RH": False,
            "model_constants": False,
            "L5_plan": "RH_Target_Lemma_Sketch_Literature_L5.md Part III",
            "upgrades": [
                "larger x_max",
                "mpmath high precision scaled with |t|",
                "offline = genuine |zeta| local minima (grid), not fixed delta",
            ],
        },
        "parameters": {
            "x_max": x_max,
            "n_primes": len(primes),
            "n_zeros_online": n_zeros,
            "X_list": X_list,
            "phi": "C^inf bump on (1,2), int_1^2 phi=1",
            "dps_rule": "base 25 + log10(|t|)+5, capped at 80",
            "minima_scan": {
                "sigma_range": [0.55, 0.92],
                "t_halfwidth": 1.25,
                "max_minima": args.max_minima,
            },
        },
        "summary": summary,
        "offline_minima_found": minima,
        "branch_warnings": branch_warnings,
        "online": results_online,
        "offline": results_offline,
        "diagnostic_checklist": {
            "branch_ok": len(branch_warnings) == 0,
            "never_claim_RH": True,
            "offline_are_local_minima": True,
        },
        "status": "L5_DIAGNOSTIC_EXECUTED_NO_RH_CLAIM",
    }

    out_path = Path(__file__).resolve().parents[1] / "rh_L5_phase_diagnostic_results.json"
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")

    print("L5 diagnostic — NO RH CLAIM")
    print("x_max", x_max, "primes", len(primes))
    print("online", len(results_online), "offline_minima", len(results_offline))
    print(
        "mean peak |A| online/offline:",
        summary["mean_peak_abs_A_online"],
        summary["mean_peak_abs_A_offline_minima"],
    )
    print(
        "mean |A|/loglog online/offline:",
        summary["mean_peak_abs_A_over_loglog_online"],
        summary["mean_peak_abs_A_over_loglog_offline_minima"],
    )
    print("mean |zeta| at offline minima:", summary["mean_zeta_abs_at_offline_minima"])
    print("branch_warnings", len(branch_warnings))
    print("status L5_DIAGNOSTIC_EXECUTED_NO_RH_CLAIM")
    print("wrote", out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
