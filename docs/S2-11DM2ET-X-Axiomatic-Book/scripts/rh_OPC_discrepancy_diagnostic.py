#!/usr/bin/env python3
"""
OPC-Core diagnostic: measure spectral-arithmetic phase discrepancy.

  theta_X = arg P_X
  Delta_X = arg zeta - arg Z_trunc   (U=E1)
  E       = arg zeta - arg P - arg Z  (should be small)

Under RH_OPC_Partial_Resolution.md:
  |theta| large  <=>  |Delta| large when |E| small.

DIAGNOSTIC ONLY — does not prove OPC-Core / O-PC / RH.
Status: RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

try:
    import mpmath as mp
except ImportError as e:
    raise SystemExit("mpmath required") from e

ZEROS = [
    14.134725141734693,
    21.022039638771555,
    25.010857580145689,
    30.424876125859513,
    32.935061587739190,
    37.586178158825672,
    40.918719012147495,
    48.005150881167160,
    52.970321477714461,
    65.112544048081607,
]


def dps_for_t(t: float) -> int:
    return min(80, 28 + max(0, int(math.log10(max(abs(t), 2)) + 6)))


def sieve_primes(n: int) -> list[int]:
    n = int(n)
    isp = bytearray(b"\x01") * (n + 1)
    isp[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if isp[i]:
            isp[i * i : n + 1 : i] = b"\x00" * (((n - i * i) // i) + 1)
    return [i for i in range(2, n + 1) if isp[i]]


def log_P(s, X, primes, dps):
    mp.mp.dps = dps
    tot = mp.mpc(0)
    for p in primes:
        if p > X:
            break
        pk, lp = p, math.log(p)
        while pk <= X:
            tot += lp / (mp.power(pk, s) * mp.log(pk))
            if pk > X / p:
                break
            pk *= p
    return tot


def U_E1(z):
    if abs(z) < mp.mpf("1e-18"):
        z = mp.mpc(mp.mpf("1e-12"), mp.mpf("1e-12"))
    return mp.expint(1, z)


def log_Z(s, X, gammas, dps, window):
    mp.mp.dps = dps
    logX = mp.log(X)
    t = float(s.imag)
    tot = mp.mpc(0)
    n = 0
    for g in gammas:
        if abs(t - g) > window:
            continue
        tot -= U_E1((s - mp.mpc(mp.mpf("0.5"), g)) * logX)
        n += 1
    return tot, n


def unwrap(prev, a):
    while a - prev > math.pi:
        a -= 2 * math.pi
    while a - prev < -math.pi:
        a += 2 * math.pi
    return a


def eval_point(sigma, t, X, primes, gammas):
    dps = dps_for_t(t)
    mp.mp.dps = dps
    s = mp.mpc(sigma, t)
    window = max(5 * math.pi / math.log(X), 2.0)
    logP = log_P(s, X, primes, dps)
    logZ, nz = log_Z(s, X, gammas, dps, window)
    logz = mp.log(mp.zeta(s))
    th = float(logP.imag)
    az = float(logZ.imag)
    azeta = float(logz.imag)
    # principal-aligned discrepancy (single point; continuous path better for Delta)
    E = logz - logP - logZ
    # align azeta - az toward th by 2pi
    disc = azeta - az
    while disc - th > math.pi:
        disc -= 2 * math.pi
    while disc - th < -math.pi:
        disc += 2 * math.pi
    return {
        "sigma": sigma,
        "t": t,
        "X": X,
        "theta_X": th,
        "arg_Z": az,
        "arg_zeta": azeta,
        "Delta_X": disc,  # arg zeta - arg Z, unwrapped toward theta
        "abs_theta": abs(th),
        "abs_Delta": abs(disc),
        "abs_E": float(abs(E)),
        "n_zeros_window": nz,
        "log_log_X": math.log(math.log(X)) if X > math.e else None,
        "ratio_abs_theta_over_loglogX": abs(th) / math.log(math.log(X)) if X > math.e else None,
        "ratio_abs_Delta_over_loglogX": abs(disc) / math.log(math.log(X)) if X > math.e else None,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args()
    x_max = 8000 if args.quick else 20000
    n_z = 4 if args.quick else 8
    primes = sieve_primes(x_max)
    gammas = ZEROS
    targets = ZEROS[:n_z]
    X_list = [40, 80, 200, 500] if args.quick else [40, 80, 150, 300, 600, 1200]

    rows = []
    print("OPC discrepancy diagnostic...", flush=True)
    for g in targets:
        # evaluate slightly off the zero (on-line offset)
        for X in X_list:
            if X > primes[-1]:
                continue
            rec = eval_point(0.5, g + 0.03, float(X), primes, gammas)
            rec["kind"] = "near_zero_offset"
            rec["gamma"] = g
            rows.append(rec)
            # approach endpoint
            r = 0.35 / math.log(2 + g)
            rec2 = eval_point(0.5 + r, g, float(X), primes, gammas)
            rec2["kind"] = "approach_end"
            rec2["gamma"] = g
            rows.append(rec2)
            print(
                f"  g={g:.2f} X={X} near: |θ|={rec['abs_theta']:.4g} |Δ|={rec['abs_Delta']:.4g} "
                f"|E|={rec['abs_E']:.4g}  end: |θ|={rec2['abs_theta']:.4g} |Δ|={rec2['abs_Delta']:.4g}",
                flush=True,
            )

    def mean_abs(kind, key):
        vals = [r[key] for r in rows if r["kind"] == kind and r.get(key) is not None]
        return float(np.mean(vals)) if vals else None

    summary = {
        "mean_abs_theta_near": mean_abs("near_zero_offset", "abs_theta"),
        "mean_abs_Delta_near": mean_abs("near_zero_offset", "abs_Delta"),
        "mean_abs_E_near": mean_abs("near_zero_offset", "abs_E"),
        "mean_abs_theta_end": mean_abs("approach_end", "abs_theta"),
        "mean_abs_Delta_end": mean_abs("approach_end", "abs_Delta"),
        "mean_abs_E_end": mean_abs("approach_end", "abs_E"),
        "mean_ratio_theta_loglog_near": mean_abs("near_zero_offset", "ratio_abs_theta_over_loglogX"),
        "note": (
            "OPC-Core shadow: |theta| should track |Delta| when |E| small. "
            "Ratios << 1 mean loglog scale not seen. No proof claim."
        ),
    }

    out = {
        "provenance": {
            "status_label": "RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF",
            "proves_OPC_Core": False,
            "proves_RH": False,
            "doc": "RH_OPC_Partial_Resolution.md",
        },
        "summary": summary,
        "rows": rows,
        "status": "OPC_DISCREPANCY_DIAGNOSTIC_EXECUTED_NO_PROOF_CLAIM",
    }
    path = Path(__file__).resolve().parents[1] / "rh_OPC_discrepancy_diagnostic_results.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("summary:", json.dumps(summary, indent=2))
    print("wrote", path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
