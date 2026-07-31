#!/usr/bin/env python3
"""
GHK hybrid diagnostic for RH phase programme.

At on-line zeros and off-line |zeta| minima, compare:
  arg ζ ≈ arg P_X + arg Z_X^{trunc}
where P_X = exp(sum_{n<=X} Λ(n)/(n^s log n))  [GHK P]
and Z_X^{trunc} uses nearby known zeros with U(z) ≈ -log(z)-γ (local approx).

DIAGNOSTIC ONLY — no RH / M1.2 proof claim.
No model constants.

Status: RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF
See: RH_Akatsuka_GHK_Survey.md
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

# Public zero ordinates (Odlyzko); on RH all rho = 1/2 + i gamma
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
    79.337375020249368,
    82.910380854086030,
    84.735492980517050,
    87.425274613125229,
    88.809111207634465,
    92.491899270558484,
    94.651344040519889,
    95.870634226365248,
    98.831194218193567,
    101.31785100573139,
]


def dps_for_t(t: float, base: int = 28) -> int:
    extra = max(0, int(math.log10(max(abs(t), 2.0)) + 6))
    return min(85, base + extra)


def sieve_primes(n: int) -> list[int]:
    if n < 2:
        return []
    n = int(n)
    isp = bytearray(b"\x01") * (n + 1)
    isp[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if isp[i]:
            isp[i * i : n + 1 : i] = b"\x00" * (((n - i * i) // i) + 1)
    return [i for i in range(2, n + 1) if isp[i]]


def von_mangoldt_up_to(x: float, primes: list[int]) -> list[tuple[int, float]]:
    """List (n, Λ(n)) for n <= x with Λ(n)>0."""
    out = []
    for p in primes:
        if p > x:
            break
        pk = p
        logp = math.log(p)
        while pk <= x:
            out.append((pk, logp))
            if pk > x / p:
                break
            pk *= p
    out.sort(key=lambda z: z[0])
    return out


def log_P_X_GHK(s: mp.mpc, X: float, primes: list[int], dps: int) -> mp.mpc:
    """log P_X = sum_{n<=X} Λ(n)/(n^s log n)  [GHK definition]."""
    mp.mp.dps = dps
    total = mp.mpc(0)
    for n, Lam in von_mangoldt_up_to(X, primes):
        total += Lam / (mp.power(n, s) * mp.log(n))
    return total


def U_local(z: mp.mpc) -> mp.mpc:
    """
    Local approximation U(z) ≈ E1(z) ≈ -log(z) - γ for small z
    (GHK: support of u near e ⇒ U(z) ~ E1(z)).
    Use principal log; branch cut negative real.
    """
    # -log(z) - γ  (leading singular part used in GHK discussion)
    return -mp.log(z) - mp.euler


def log_Z_X_trunc(
    s: mp.mpc,
    X: float,
    zero_gammas: list[float],
    dps: int,
    window_factor: float = 3.0,
) -> tuple[mp.mpc, int]:
    """
    log Z_X ≈ -sum_rho U((s-rho) log X) for nearby zeros on the critical line
    (rho = 1/2 + i gamma from tables). window: |t - gamma| * log X <= window_factor * pi
    """
    mp.mp.dps = dps
    logX = mp.log(X)
    t = float(s.imag)
    half = window_factor * math.pi / float(logX)
    total = mp.mpc(0)
    n_used = 0
    for g in zero_gammas:
        if abs(t - g) > half + 0.5:
            continue
        rho = mp.mpc(mp.mpf("0.5"), g)
        z = (s - rho) * logX
        # avoid exact zero
        if abs(z) < mp.mpf("1e-18"):
            z = mp.mpc(mp.mpf("1e-12"), mp.mpf("1e-12"))
        total -= U_local(z)
        n_used += 1
    return total, n_used


def continuous_arg_from_log(lg: mp.mpc) -> float:
    return float(lg.imag)


def evaluate_at_point(
    sigma: float,
    t: float,
    X: float,
    primes: list[int],
    zero_gammas: list[float],
    label: str,
    kind: str,
) -> dict:
    dps = dps_for_t(t)
    mp.mp.dps = dps
    s = mp.mpc(sigma, t)

    logP = log_P_X_GHK(s, X, primes, dps)
    logZ, n_zeros_used = log_Z_X_trunc(s, X, zero_gammas, dps)
    log_hybrid = logP + logZ

    # direct zeta
    try:
        log_zeta = mp.log(mp.zeta(s))
        zeta_abs = float(abs(mp.zeta(s)))
    except Exception as ex:
        return {"label": label, "error": str(ex)}

    # GHK says zeta ≈ P Z, so log zeta ≈ logP + logZ + err
    rem = log_zeta - log_hybrid
    # also classical EP remainder Im(log zeta - log P_Euler) with hard truncate primes
    # compare arg
    arg_zeta = continuous_arg_from_log(log_zeta)
    arg_P = continuous_arg_from_log(logP)
    arg_Z = continuous_arg_from_log(logZ)
    arg_sum = arg_P + arg_Z
    # unwrap arg_sum toward arg_zeta by 2pi
    while arg_sum - arg_zeta > math.pi:
        arg_sum -= 2 * math.pi
    while arg_sum - arg_zeta < -math.pi:
        arg_sum += 2 * math.pi

    # local zero contribution if on-line: nearest gamma
    nearest = min(zero_gammas, key=lambda g: abs(g - t))
    rho = complex(0.5, nearest)
    s_c = complex(sigma, t)
    m_arg = abs(math.atan2(s_c.imag - rho.imag, s_c.real - rho.real))

    err_bound_shape = {
        "X_over_s_logX": float(X / (max(abs(t), 2) * math.log(X))),
        "X_to_minus_sigma_logX": float((X ** (-sigma)) * math.log(X)),
    }

    return {
        "label": label,
        "kind": kind,
        "sigma": sigma,
        "t": t,
        "X": X,
        "dps": dps,
        "zeta_abs": zeta_abs,
        "arg_zeta": arg_zeta,
        "arg_P_X": arg_P,
        "arg_Z_X_trunc": arg_Z,
        "arg_P_plus_Z": arg_sum,
        "arg_error_zeta_minus_PZ": arg_zeta - arg_sum,
        "Im_log_zeta_minus_log_P": float((log_zeta - logP).imag),
        "Im_log_Z_trunc": float(logZ.imag),
        "Re_log_P": float(logP.real),
        "n_zeros_in_window": n_zeros_used,
        "nearest_gamma": nearest,
        "abs_m_arg_to_nearest_crit_zero": m_arg,
        "ratio_Im_R_over_marg": (
            abs(float((log_zeta - logP).imag)) / m_arg if m_arg > 1e-12 else None
        ),
        "err_bound_shape": err_bound_shape,
    }


def find_offline_minima(t_centers: list[float], n_keep: int = 8) -> list[dict]:
    sigmas = np.linspace(0.60, 0.90, 22)
    cands = []
    for t0 in t_centers:
        ts = np.linspace(t0 - 2.0, t0 + 2.0, 22)
        best = None
        for sig in sigmas:
            for tt in ts:
                mp.mp.dps = dps_for_t(float(tt), base=18)
                z = float(abs(mp.zeta(mp.mpc(sig, tt))))
                if best is None or z < best["zeta_abs"]:
                    best = {"sigma": float(sig), "t": float(tt), "zeta_abs": z}
        if best:
            sig, tt, zb = best["sigma"], best["t"], best["zeta_abs"]
            for _ in range(5):
                improved = False
                for ds, dt in ((0.012, 0), (-0.012, 0), (0, 0.05), (0, -0.05)):
                    s2, t2 = sig + ds, tt + dt
                    if s2 < 0.60 or s2 > 0.94:
                        continue
                    mp.mp.dps = dps_for_t(t2, base=20)
                    z2 = float(abs(mp.zeta(mp.mpc(s2, t2))))
                    if z2 < zb:
                        zb, sig, tt = z2, s2, t2
                        improved = True
                if not improved:
                    break
            cands.append({"sigma": sig, "t": tt, "zeta_abs": zb})
    cands.sort(key=lambda c: c["zeta_abs"])
    kept = []
    for c in cands:
        if any(abs(c["t"] - k["t"]) < 0.5 and abs(c["sigma"] - k["sigma"]) < 0.04 for k in kept):
            continue
        kept.append(c)
        if len(kept) >= n_keep:
            break
    return kept


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--x-max", type=int, default=15000)
    ap.add_argument("--X-hybrid", type=float, default=200.0, help="GHK mediator X")
    ap.add_argument("--n-zeros", type=int, default=6)
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args(argv)

    x_max = 6000 if args.quick else args.x_max
    n_zeros = 3 if args.quick else args.n_zeros
    X_hyb = 80.0 if args.quick else args.X_hybrid

    print(f"sieving to {x_max}...", flush=True)
    primes = sieve_primes(x_max)
    zeros = FIRST_ZERO_ORDINATES  # full list for Z trunc window
    t_centers = FIRST_ZERO_ORDINATES[:n_zeros]

    online = []
    print("on-line (near critical zeros)...", flush=True)
    for t in t_centers:
        # evaluate slightly off the zero so zeta and logs are defined
        for dsig, dt in ((0.0, 0.02), (0.0, -0.02), (0.02, 0.0)):
            sig = 0.5 + dsig
            tt = t + dt
            lab = f"near_zero_s={sig:.2f}_t={tt:.3f}"
            rec = evaluate_at_point(sig, tt, X_hyb, primes, zeros, lab, "near_critical_zero")
            online.append(rec)
            if "error" not in rec:
                print(
                    f"  {lab}: |arg err|={abs(rec['arg_error_zeta_minus_PZ']):.4g} "
                    f"Im(logZ)={rec['Im_log_Z_trunc']:.4g}",
                    flush=True,
                )
            break  # one offset per zero for speed

    print("offline minima...", flush=True)
    minima = find_offline_minima(t_centers[: max(3, n_zeros // 2)], n_keep=6 if not args.quick else 3)
    offline = []
    for m in minima:
        lab = f"offmin_s={m['sigma']:.3f}_t={m['t']:.3f}"
        rec = evaluate_at_point(
            m["sigma"], m["t"], X_hyb, primes, zeros, lab, "offline_abs_zeta_min"
        )
        rec["zeta_abs_center"] = m["zeta_abs"]
        offline.append(rec)
        if "error" not in rec:
            print(
                f"  {lab}: |arg err|={abs(rec['arg_error_zeta_minus_PZ']):.4g} "
                f"Im(R=logz-logP)={rec['Im_log_zeta_minus_log_P']:.4g} "
                f"Im(logZ)={rec['Im_log_Z_trunc']:.4g}",
                flush=True,
            )

    def mean_abs(rows, key):
        vals = [abs(r[key]) for r in rows if key in r and r[key] is not None]
        return float(np.mean(vals)) if vals else None

    summary = {
        "mean_abs_arg_error_online": mean_abs(online, "arg_error_zeta_minus_PZ"),
        "mean_abs_arg_error_offline": mean_abs(offline, "arg_error_zeta_minus_PZ"),
        "mean_abs_Im_R_online": mean_abs(online, "Im_log_zeta_minus_log_P"),
        "mean_abs_Im_R_offline": mean_abs(offline, "Im_log_zeta_minus_log_P"),
        "mean_abs_Im_logZ_online": mean_abs(online, "Im_log_Z_trunc"),
        "mean_abs_Im_logZ_offline": mean_abs(offline, "Im_log_Z_trunc"),
        "note": (
            "arg_error = arg ζ - (arg P_X + arg Z_trunc). Small error supports hybrid. "
            "Im(logZ) vs m arg tests local zero isolation. No RH claim."
        ),
    }

    out = {
        "provenance": {
            "status_label": "RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF",
            "proves_RH": False,
            "proves_M1_2": False,
            "model_constants": False,
            "GHK": "arXiv:math/0511182 Theorem 1",
            "survey": "RH_Akatsuka_GHK_Survey.md",
        },
        "parameters": {
            "x_max_primes": x_max,
            "X_hybrid": X_hyb,
            "n_zeros_online": n_zeros,
            "U_approx": "U(z)~-log(z)-euler (local GHK leading term)",
            "Z_trunc": "zeros with |t-gamma| <= 3*pi/log X (+0.5)",
        },
        "summary": summary,
        "online": online,
        "offline": offline,
        "offline_minima": minima,
        "status": "GHK_HYBRID_DIAGNOSTIC_EXECUTED_NO_PROOF_CLAIM",
    }

    path = Path(__file__).resolve().parents[1] / "rh_GHK_hybrid_diagnostic_results.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("GHK hybrid diagnostic — NO PROOF / NO RH CLAIM")
    print("mean |arg err| online/offline:", summary["mean_abs_arg_error_online"], summary["mean_abs_arg_error_offline"])
    print("mean |Im R| online/offline:", summary["mean_abs_Im_R_online"], summary["mean_abs_Im_R_offline"])
    print("wrote", path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
