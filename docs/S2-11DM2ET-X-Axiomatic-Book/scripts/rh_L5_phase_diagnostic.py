#!/usr/bin/env python3
"""
L5 phase diagnostic for partial Euler products — NO RH CLAIM.

Computes continuous θ_x = arg P_x, U_x = log|P_x|, smoothed A_X,
and |ζ| at on-line zeros and off-line probes.

Status: L5_DIAGNOSTIC_EXECUTED_NO_RH_CLAIM
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import mpmath as mp

# First nontrivial zeta zero ordinates (Odlyzko / known values)
ODLYZKO_GAMMAS = [
    14.1347251417346937904572519835625,
    21.0220396387715549926284795938969,
    25.0108575801456887632137909925628,
    30.4248761258595132103118975305840,
    32.9350615877391896906623689640747,
    37.5861781588256712572177634807053,
    40.9187190121474951873981269146334,
    43.3270732809149995194961221654068,
    48.0051508811671597279424727494275,
    49.7738324776723021819167846785638,
    52.9703214777144606441472966088808,
    56.4462476970633948043677594767060,
    59.3470440026023530796536486749922,
    60.8317785246098098442599018245240,
    65.1125440480816066608750542531837,
]


def sieve_primes(n: int) -> list[int]:
    if n < 2:
        return []
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            is_prime[i * i :: i] = b"\x00" * (((n - i * i) // i) + 1)
    return [i for i in range(2, n + 1) if is_prime[i]]


def dps_for_t(t: float) -> int:
    return min(80, max(25, int(25 + math.log10(abs(t) + 1) + 5)))


def euler_factor_log(p: int, s: mp.mpc) -> mp.mpc:
    """Principal log of (1 - p^{-s})^{-1}."""
    z = mp.power(p, -s)
    # log(1/(1-z)) = -log(1-z)
    return -mp.log(1 - z)


def cumulative_theta_U(
    primes: list[int], sigma: float, t: float, x_max: float
) -> tuple[list[tuple[float, float, float]], int]:
    """
    Returns list of (x, theta, U) at each prime x=p <= x_max,
    and branch_warnings count (large principal-arg jumps).
    """
    dps = dps_for_t(t)
    with mp.workdps(dps):
        s = mp.mpc(sigma, t)
        theta = mp.mpf(0)
        U = mp.mpf(0)
        out: list[tuple[float, float, float]] = []
        branch_warnings = 0
        prev_arg = mp.mpf(0)
        for p in primes:
            if p > x_max:
                break
            clog = euler_factor_log(p, s)
            darg = mp.arg(mp.exp(clog))  # principal arg of factor = Im(clog) in (-pi,pi]
            # continuous: use Im(clog) which is already principal for each factor
            im = mp.im(clog)
            re = mp.re(clog)
            if abs(im - prev_arg) > 2:  # heuristic discontinuity flag between factors
                # factors are independent; large im alone is not a branch bug
                pass
            if abs(im) > 3:
                branch_warnings += 1
            theta += im
            U += re
            prev_arg = im
            out.append((float(p), float(theta), float(U)))
    return out, branch_warnings


def theta_at_x(
    primes: list[int], sigma: float, t: float, x: float
) -> tuple[float, float, int]:
    series, bw = cumulative_theta_U(primes, sigma, t, x)
    if not series:
        return 0.0, 0.0, bw
    return series[-1][1], series[-1][2], bw


def smooth_bump_phi(v: float) -> float:
    """C^infty-style bump on (1,2), zero outside; unnormalized."""
    if v <= 1.0 or v >= 2.0:
        return 0.0
    # standard flat bump: exp(-1/(v-1) - 1/(2-v))
    return math.exp(-1.0 / (v - 1.0) - 1.0 / (2.0 - v))


def smoothed_A(
    primes: list[int], sigma: float, t: float, X: float, n_quad: int = 24
) -> float:
    """A_X = ∫_1^2 θ_{X^v} φ(v) dv / ∫ φ, trapezoid on (1,2)."""
    # nodes interior to (1,2)
    vs = [1.0 + (i + 0.5) / n_quad for i in range(n_quad)]
    weights = [smooth_bump_phi(v) for v in vs]
    mass = sum(weights)
    if mass <= 0:
        return 0.0
    acc = 0.0
    bw_total = 0
    for v, w in zip(vs, weights):
        x = X**v
        th, _, bw = theta_at_x(primes, sigma, t, x)
        bw_total += bw
        acc += th * w
    return acc / mass


def zeta_abs(sigma: float, t: float) -> float:
    dps = dps_for_t(t)
    with mp.workdps(dps):
        return float(abs(mp.zeta(mp.mpc(sigma, t))))


def refine_minimum(
    t0: float,
    sigma_grid: list[float],
    t_span: float = 0.4,
    steps: int = 8,
    sigma_floor: float = 0.60,
) -> tuple[float, float, float]:
    """Coordinate-descent style search for local |ζ| minimum with σ >= sigma_floor."""
    best_s, best_t, best_z = 0.75, t0, float("inf")
    sigmas = [s for s in sigma_grid if s >= sigma_floor]
    ts = [t0 + t_span * (i / steps - 0.5) for i in range(steps + 1)]
    for s in sigmas:
        for t in ts:
            z = zeta_abs(s, t)
            if z < best_z:
                best_z, best_s, best_t = z, s, t
    # refine
    for _ in range(6):
        improved = False
        for ds, dt in [
            (0.01, 0.0),
            (-0.01, 0.0),
            (0.0, 0.02),
            (0.0, -0.02),
            (0.005, 0.01),
            (-0.005, -0.01),
        ]:
            s2 = best_s + ds
            t2 = best_t + dt
            if s2 < sigma_floor or s2 > 0.95:
                continue
            z = zeta_abs(s2, t2)
            if z < best_z:
                best_z, best_s, best_t = z, s2, t2
                improved = True
        if not improved:
            break
    return best_s, best_t, best_z


def peak_abs_A_along_X(
    primes: list[int],
    sigma: float,
    t: float,
    X_list: list[float],
) -> tuple[float, float, float]:
    """Return (max|A|, A_at_max, X_at_max)."""
    best = 0.0
    best_A = 0.0
    best_X = X_list[0]
    for X in X_list:
        A = smoothed_A(primes, sigma, t, X)
        if abs(A) > best:
            best = abs(A)
            best_A = A
            best_X = X
    return best, best_A, best_X


def main() -> int:
    ap = argparse.ArgumentParser(description="L5 partial Euler phase diagnostic (NO RH CLAIM)")
    ap.add_argument("--x-max", type=int, default=5000)
    ap.add_argument("--n-zeros", type=int, default=8)
    ap.add_argument("--max-minima", type=int, default=8)
    ap.add_argument("--delta", type=float, default=0.05)
    ap.add_argument(
        "--out",
        type=str,
        default="rh/rh_L5_phase_diagnostic_results.json",
    )
    args = ap.parse_args()

    primes = sieve_primes(args.x_max)
    gammas = ODLYZKO_GAMMAS[: args.n_zeros]
    # X scales for A_X peak scan
    X_list = []
    x = 20.0
    while x <= args.x_max ** 0.5:  # X^2 <= x_max roughly for v<=2
        X_list.append(x)
        x *= 1.5
    if not X_list:
        X_list = [10.0, 20.0]

    on_line = []
    off_line = []
    branch_on = 0

    print("L5 diagnostic — NO RH CLAIM", flush=True)
    print(f"primes <= {args.x_max}: {len(primes)}; zeros: {len(gammas)}", flush=True)

    for g in gammas:
        # on-line
        peak, A, Xa = peak_abs_A_along_X(primes, 0.5, g, X_list)
        zabs = zeta_abs(0.5, g)
        _, _, bw = theta_at_x(primes, 0.5, g, min(args.x_max, X_list[-1] ** 2))
        branch_on += bw
        on_line.append(
            {
                "sigma": 0.5,
                "t": g,
                "peak_abs_A": peak,
                "A_at_peak": A,
                "X_at_peak": Xa,
                "abs_zeta": zabs,
                "peak_abs_A_over_loglogX": peak / max(math.log(math.log(max(Xa, 3))), 1e-9),
            }
        )
        # fixed-δ off-line at same height
        for sign in (+1, -1):
            sig = 0.5 + sign * args.delta
            if sig <= 0.05 or sig >= 0.95:
                continue
            peak, A, Xa = peak_abs_A_along_X(primes, sig, g, X_list)
            off_line.append(
                {
                    "kind": "fixed_delta",
                    "sigma": sig,
                    "t": g,
                    "peak_abs_A": peak,
                    "A_at_peak": A,
                    "X_at_peak": Xa,
                    "abs_zeta": zeta_abs(sig, g),
                    "peak_abs_A_over_loglogX": peak
                    / max(math.log(math.log(max(Xa, 3))), 1e-9),
                }
            )

    # refined off-line minima near first zero heights
    sigma_grid = [0.60, 0.65, 0.70, 0.75, 0.80, 0.85]
    minima = []
    for g in gammas[: max(1, args.max_minima)]:
        s, t, z = refine_minimum(g, sigma_grid, sigma_floor=0.60)
        peak, A, Xa = peak_abs_A_along_X(primes, s, t, X_list)
        rec = {
            "kind": "refined_minimum",
            "sigma": s,
            "t": t,
            "peak_abs_A": peak,
            "A_at_peak": A,
            "X_at_peak": Xa,
            "abs_zeta": z,
            "peak_abs_A_over_loglogX": peak / max(math.log(math.log(max(Xa, 3))), 1e-9),
        }
        minima.append(rec)
        off_line.append(rec)

    def mean_peak(rows: list[dict]) -> float:
        if not rows:
            return float("nan")
        return sum(r["peak_abs_A"] for r in rows) / len(rows)

    def mean_norm(rows: list[dict]) -> float:
        if not rows:
            return float("nan")
        return sum(r["peak_abs_A_over_loglogX"] for r in rows) / len(rows)

    summary = {
        "status": "L5_DIAGNOSTIC_EXECUTED_NO_RH_CLAIM",
        "rh_claim": False,
        "x_max": args.x_max,
        "n_zeros": len(gammas),
        "n_primes": len(primes),
        "X_list": X_list,
        "on_line_points": len(on_line),
        "off_line_points": len(off_line),
        "mean_peak_abs_A_on": mean_peak(on_line),
        "mean_peak_abs_A_off": mean_peak(off_line),
        "mean_peak_abs_A_over_loglogX_on": mean_norm(on_line),
        "mean_peak_abs_A_over_loglogX_off": mean_norm(off_line),
        "branch_warnings_on_sample": branch_on,
        "note": (
            "Finite-range only. Slight on/off differences are inconclusive. "
            "Do not read as support for RH or Conjecture B."
        ),
    }

    payload = {
        "summary": summary,
        "on_line": on_line,
        "off_line": off_line,
        "refined_minima": minima,
    }

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print("─── summary ───")
    for k, v in summary.items():
        print(f"  {k}: {v}")
    print(f"wrote {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
