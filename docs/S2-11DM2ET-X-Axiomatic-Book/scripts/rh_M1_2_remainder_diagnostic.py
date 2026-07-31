#!/usr/bin/env python3
"""
M1.2 remainder diagnostic (low height).

Computes Im R_x^EP(s) := Im( log ζ(s) - log P_x(s) ) on a short arc
about critical-line zeros and about off-line |ζ| local minima,
and compares to m * arg(s - ρ_proxy).

DIAGNOSTIC ONLY — does not prove M1.2 or RH.
No model constants.

Status: RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF
See: RH_M1_2_Remainder_Bound_Strategy.md
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
    raise SystemExit("mpmath required") from e

FIRST_ZERO_ORDINATES = [
    14.134725141734693,
    21.022039638771555,
    25.010857580145689,
    30.424876125859513,
    32.935061587739190,
    37.586178158825672,
    40.918719012147495,
    43.327073280914999,
]


def dps_for_t(t: float, base: int = 30) -> int:
    extra = max(0, int(math.log10(max(abs(t), 2.0)) + 8))
    return min(90, base + extra)


def sieve_primes(n: int) -> list[int]:
    if n < 2:
        return []
    n = int(n)
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            start = i * i
            is_prime[start : n + 1 : i] = b"\x00" * (((n - start) // i) + 1)
    return [i for i in range(2, n + 1) if is_prime[i]]


def log_P_x(primes: list[int], x: float, s: mp.mpc, dps: int) -> mp.mpc:
    """Continuous log P_x along primes p <= x (sum of principal factor logs)."""
    mp.mp.dps = dps
    total = mp.mpc(0)
    for p in primes:
        if p > x:
            break
        total += -mp.log(1 - mp.power(p, -s))
    return total


def log_zeta_path(s: mp.mpc, dps: int, n_steps: int = 24) -> mp.mpc:
    """
    Continuous log ζ(s) via path from s_star=2 to s (horizontal then vertical),
    integrating ζ'/ζ with mpmath.
    """
    mp.mp.dps = dps
    s_star = mp.mpc(2, 0)
    # horizontal: 2 -> sigma + 0i, then vertical to s (if imag != 0 start vertical from 2+it)
    # path: 2 -> 2+it -> sigma+it
    t = s.imag
    sig = s.real
    p1 = mp.mpc(2, t)
    # integrate ζ'/ζ
    def integ(a, b, steps):
        acc = mp.mpc(0)
        for k in range(steps):
            w0 = a + (b - a) * mp.mpf(k) / steps
            w1 = a + (b - a) * mp.mpf(k + 1) / steps
            mid = (w0 + w1) / 2
            # ζ'/ζ = digamma-like via derivative
            zpm = mp.zeta(mid, derivative=1) / mp.zeta(mid)
            acc += zpm * (w1 - w0)
        return acc

    log0 = mp.log(mp.zeta(s_star))  # principal at Re=2 > 1
    log0 = log0 + integ(s_star, p1, n_steps)
    log0 = log0 + integ(p1, s, n_steps)
    return log0


def arg_diff(z: complex) -> float:
    return math.atan2(z.imag, z.real)


def sample_arc(
    primes: list[int],
    rho_sigma: float,
    rho_t: float,
    eps: float,
    x: float,
    n_arc: int,
    m: int = 1,
) -> dict:
    """
    Sample s = rho + eps * e^{i alpha}, alpha in [0, pi].
    rho_proxy = rho_sigma + i rho_t (exact zero or |zeta| minimum).
    """
    dps = dps_for_t(rho_t)
    mp.mp.dps = dps
    rho = mp.mpc(rho_sigma, rho_t)
    alphas = np.linspace(0.0, math.pi, n_arc)
    rows = []
    imR_list = []
    marg_list = []
    theta_list = []

    for a in alphas:
        delta = eps * mp.exp(mp.j * mp.mpf(a))
        s = rho + delta
        # avoid landing exactly on zero
        if abs(s - rho) < eps * 1e-9:
            s = rho + eps * mp.mpc(1e-6, 1e-6)
        try:
            logP = log_P_x(primes, x, s, dps)
            logZ = log_zeta_path(s, dps)
            R = logZ - logP
            imR = float(R.imag)
            # continuous arg of (s-rho) on this arc: just alpha (principal from 0 to pi)
            marg = m * float(a)
            theta = float(logP.imag)
            rows.append(
                {
                    "alpha": float(a),
                    "sigma": float(s.real),
                    "t": float(s.imag),
                    "Im_R_EP": imR,
                    "m_arg": marg,
                    "theta_x": theta,
                    "abs_zeta": float(abs(mp.zeta(s))),
                    "U_x": float(logP.real),
                }
            )
            imR_list.append(abs(imR))
            marg_list.append(abs(marg))
            theta_list.append(theta)
        except Exception as ex:
            rows.append({"alpha": float(a), "error": str(ex)})

    sup_imR = max(imR_list) if imR_list else None
    sup_marg = max(marg_list) if marg_list else None
    # theta variation along arc
    if len(theta_list) >= 2:
        dtheta = max(theta_list) - min(theta_list)
    else:
        dtheta = None

    ratio = None
    if sup_imR is not None and sup_marg and sup_marg > 0:
        ratio = sup_imR / sup_marg

    return {
        "rho_sigma": rho_sigma,
        "rho_t": rho_t,
        "eps": eps,
        "x": x,
        "m": m,
        "dps": dps,
        "sup_abs_Im_R_EP": sup_imR,
        "sup_abs_m_arg": sup_marg,
        "ratio_sup_ImR_over_sup_marg": ratio,
        "delta_theta_on_arc": dtheta,
        "M1_2_numeric_pass_half": (
            sup_imR is not None and sup_marg is not None and sup_imR <= 0.5 * math.pi * m
        ),
        "arc": rows,
    }


def find_offline_minima(t_centers: list[float], n_keep: int = 6) -> list[dict]:
    """Light |zeta| minima scan with sigma >= 0.60."""
    sigmas = np.linspace(0.60, 0.90, 25)
    cands = []
    for t0 in t_centers:
        ts = np.linspace(t0 - 2.0, t0 + 2.0, 25)
        best = None
        for sig in sigmas:
            for tt in ts:
                mp.mp.dps = dps_for_t(float(tt), base=20)
                z = float(abs(mp.zeta(mp.mpc(sig, tt))))
                if best is None or z < best["zeta_abs"]:
                    best = {"sigma": float(sig), "t": float(tt), "zeta_abs": z}
        if best:
            # refine
            sig, tt, zb = best["sigma"], best["t"], best["zeta_abs"]
            for _ in range(6):
                improved = False
                for ds, dt in ((0.01, 0), (-0.01, 0), (0, 0.04), (0, -0.04)):
                    s2, t2 = sig + ds, tt + dt
                    if s2 < 0.60 or s2 > 0.95:
                        continue
                    mp.mp.dps = dps_for_t(t2, base=22)
                    z2 = float(abs(mp.zeta(mp.mpc(s2, t2))))
                    if z2 < zb:
                        zb, sig, tt = z2, s2, t2
                        improved = True
                if not improved:
                    break
            cands.append({"sigma": sig, "t": tt, "zeta_abs": zb, "kind": "offline_min"})
    cands.sort(key=lambda c: c["zeta_abs"])
    # unique
    kept = []
    for c in cands:
        if any(abs(c["t"] - k["t"]) < 0.4 and abs(c["sigma"] - k["sigma"]) < 0.03 for k in kept):
            continue
        kept.append(c)
        if len(kept) >= n_keep:
            break
    return kept


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="M1.2 remainder diagnostic (no proof claim)")
    ap.add_argument("--x-max", type=int, default=20000)
    ap.add_argument("--n-zeros", type=int, default=5)
    ap.add_argument("--n-arc", type=int, default=17)
    ap.add_argument("--eps-scale", type=float, default=0.08, help="arc radius ~ eps_scale")
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args(argv)

    x_max = 8000 if args.quick else args.x_max
    n_zeros = 3 if args.quick else args.n_zeros
    n_arc = 11 if args.quick else args.n_arc

    print(f"sieving primes to {x_max}...", flush=True)
    primes = sieve_primes(x_max)
    print(f"primes: {len(primes)}", flush=True)

    x_trunc = float(primes[min(len(primes) - 1, int(len(primes) * 0.95))])
    # also try a few truncations
    x_list = sorted(
        set(
            [
                float(primes[min(len(primes) - 1, len(primes) // 4)]),
                float(primes[min(len(primes) - 1, len(primes) // 2)]),
                x_trunc,
            ]
        )
    )

    online_results = []
    for t in FIRST_ZERO_ORDINATES[:n_zeros]:
        # arc about exact critical zero (sigma=1/2)
        eps = args.eps_scale
        # stay away from other zeros: small eps
        for x in x_list:
            rec = sample_arc(primes, 0.5, t, eps, x, n_arc, m=1)
            rec["label"] = f"online_zero_t={t:.4f}_x={x:.0f}"
            rec["kind"] = "critical_zero"
            online_results.append(rec)
            print(
                f"  {rec['label']}: sup|Im R|={rec['sup_abs_Im_R_EP']:.4g} "
                f"ratio={rec['ratio_sup_ImR_over_sup_marg']}",
                flush=True,
            )

    print("offline |zeta| minima...", flush=True)
    minima = find_offline_minima(FIRST_ZERO_ORDINATES[: max(3, n_zeros)], n_keep=5)
    offline_results = []
    for mpt in minima:
        # use minimum as rho_proxy (not a true zero)
        eps = args.eps_scale
        x = x_list[-1]
        rec = sample_arc(primes, mpt["sigma"], mpt["t"], eps, x, n_arc, m=1)
        rec["label"] = f"offline_min_s={mpt['sigma']:.3f}_t={mpt['t']:.3f}_x={x:.0f}"
        rec["kind"] = "offline_abs_zeta_min"
        rec["zeta_abs_at_center"] = mpt["zeta_abs"]
        offline_results.append(rec)
        print(
            f"  {rec['label']}: sup|Im R|={rec['sup_abs_Im_R_EP']:.4g} "
            f"z0={mpt['zeta_abs']:.3e}",
            flush=True,
        )

    def mean_ratio(rows):
        vals = [
            r["ratio_sup_ImR_over_sup_marg"]
            for r in rows
            if r.get("ratio_sup_ImR_over_sup_marg") is not None
        ]
        return float(np.mean(vals)) if vals else None

    def frac_pass(rows):
        if not rows:
            return None
        return sum(1 for r in rows if r.get("M1_2_numeric_pass_half")) / len(rows)

    summary = {
        "mean_ratio_online": mean_ratio(online_results),
        "mean_ratio_offline": mean_ratio(offline_results),
        "frac_pass_half_pi_online": frac_pass(online_results),
        "frac_pass_half_pi_offline": frac_pass(offline_results),
        "interpretation": (
            "ratio = sup|Im R_EP| / sup|m arg| on semicircle. "
            "M1.2 wants ratio < c0 < 1. Numeric pass_half means sup|Im R| <= pi/2. "
            "Low-height diagnostic only — does NOT prove M1.2 or RH."
        ),
    }

    out = {
        "provenance": {
            "status_label": "RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF",
            "proves_M1_2": False,
            "proves_RH": False,
            "model_constants": False,
            "note": "RH_M1_2_Remainder_Bound_Strategy.md",
        },
        "parameters": {
            "x_max": x_max,
            "n_primes": len(primes),
            "x_truncations": x_list,
            "n_zeros": n_zeros,
            "n_arc": n_arc,
            "eps": args.eps_scale,
        },
        "summary": summary,
        "online_arcs": online_results,
        "offline_arcs": offline_results,
        "offline_minima": minima,
        "status": "M1_2_DIAGNOSTIC_EXECUTED_NO_PROOF_CLAIM",
    }

    path = Path(__file__).resolve().parents[1] / "rh_M1_2_remainder_diagnostic_results.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("M1.2 diagnostic — NO PROOF / NO RH CLAIM")
    print("mean ratio online/offline:", summary["mean_ratio_online"], summary["mean_ratio_offline"])
    print("frac pass half-pi online/offline:", summary["frac_pass_half_pi_online"], summary["frac_pass_half_pi_offline"])
    print("wrote", path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
