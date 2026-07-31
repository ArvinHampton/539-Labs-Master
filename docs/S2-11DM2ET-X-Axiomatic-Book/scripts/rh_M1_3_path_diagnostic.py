#!/usr/bin/env python3
"""
M1.3 path diagnostic under concrete HD-low.

For each of the first N Odlyzko zeros rho = 1/2 + i gamma:
  1. HD isolation: disk D(rho, 2r) contains only this zero among the table
  2. Semicircle path s(phi) = rho + r e^{i phi}, phi in [0, pi]
  3. Continuous Delta arg P_X along the path
  4. Hybrid residual E = log zeta - log P_X - log Z_trunc (U=E1)
  5. Distant-zero Im U sum as c3_far diagnostic

DIAGNOSTIC ONLY — no RH / M1.2 / M1.3 proof claim.
HD-low = finite Odlyzko table (non-circular at tabulated heights).
Status: RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF
See: RH_M1_3_Path_Design.md
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


def dps_for_t(t: float, base: int = 30) -> int:
    extra = max(0, int(math.log10(max(abs(t), 2.0)) + 6))
    return min(90, base + extra)


def sieve_primes(n: int) -> list[int]:
    n = int(n)
    if n < 2:
        return []
    isp = bytearray(b"\x01") * (n + 1)
    isp[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if isp[i]:
            isp[i * i : n + 1 : i] = b"\x00" * (((n - i * i) // i) + 1)
    return [i for i in range(2, n + 1) if isp[i]]


def von_mangoldt_up_to(x: float, primes: list[int]) -> list[tuple[int, float]]:
    out = []
    for p in primes:
        if p > x:
            break
        pk, logp = p, math.log(p)
        while pk <= x:
            out.append((pk, logp))
            if pk > x / p:
                break
            pk *= p
    out.sort(key=lambda z: z[0])
    return out


def log_P_X(s: mp.mpc, X: float, primes: list[int], dps: int) -> mp.mpc:
    mp.mp.dps = dps
    total = mp.mpc(0)
    for n, Lam in von_mangoldt_up_to(X, primes):
        total += Lam / (mp.power(n, s) * mp.log(n))
    return total


def U_E1(z: mp.mpc) -> mp.mpc:
    if abs(z) < mp.mpf("1e-18"):
        z = mp.mpc(mp.mpf("1e-12"), mp.mpf("1e-12"))
    return mp.expint(1, z)


def log_Z_split(
    s: mp.mpc,
    X: float,
    gammas: list[float],
    local_gamma: float,
    dps: int,
    window: float,
) -> tuple[mp.mpc, mp.mpc, int]:
    """
    Split log Z ≈ -sum U((s-rho) log X) into local (at local_gamma) + far (others in window).
    Window: |g - local_gamma| <= window OR |Im s - g| <= window.
    Returns (logZ_local, logZ_far, n_far).
    """
    mp.mp.dps = dps
    logX = mp.log(X)
    t = float(s.imag)
    local = mp.mpc(0)
    far = mp.mpc(0)
    n_far = 0
    for g in gammas:
        is_local = abs(g - local_gamma) < 1e-12
        if not is_local and abs(g - local_gamma) > window and abs(t - g) > window:
            continue
        rho = mp.mpc(mp.mpf("0.5"), g)
        z = (s - rho) * logX
        contrib = -U_E1(z)
        if is_local:
            local += contrib
        else:
            far += contrib
            n_far += 1
    return local, far, n_far


def continuous_arg_track(prev: float, new_prin: float) -> float:
    """Unwrap new principal arg to be continuous with prev."""
    a = new_prin
    while a - prev > math.pi:
        a -= 2 * math.pi
    while a - prev < -math.pi:
        a += 2 * math.pi
    return a


def isolation_HD(
    gamma: float, gammas: list[float], r: float
) -> dict:
    """HD-low: check no other tabulated zero within distance 2r of rho."""
    others = []
    for g in gammas:
        if abs(g - gamma) < 1e-12:
            continue
        # zeros on critical line: |rho - rho'| = |g - gamma|
        dist = abs(g - gamma)
        if dist < 2 * r:
            others.append({"gamma": g, "dist": dist})
    return {
        "isolated": len(others) == 0,
        "r": r,
        "check_radius": 2 * r,
        "intruders": others,
        "nearest_other_gap": min((abs(g - gamma) for g in gammas if abs(g - gamma) > 1e-12), default=None),
    }


def track_arg_P_along(points, X, primes, dps):
    """points: list of (sigma, t). Return continuous arg P list and delta."""
    args = []
    prev = None
    for sig, tt in points:
        s = mp.mpc(sig, tt)
        a = float(log_P_X(s, X, primes, dps).imag)
        if prev is None:
            prev = a
        else:
            a = continuous_arg_track(prev, a)
            prev = a
        args.append(a)
    delta = args[-1] - args[0] if args else 0.0
    return args, delta


def run_path_for_zero(
    gamma: float,
    gammas: list[float],
    primes: list[int],
    X: float,
    c_r: float,
    n_phi: int,
    m: int = 1,
) -> dict:
    r = c_r / math.log(2.0 + abs(gamma))
    hd = isolation_HD(gamma, gammas, r)
    dps = dps_for_t(gamma)
    mp.mp.dps = dps
    rho = mp.mpc(mp.mpf("0.5"), gamma)
    window = max(4.0 * math.pi / math.log(X), 3.0 * r + 0.5)

    # --- A. Semicircle (monodromy probe): expect Delta arg P ~ 0 (P is zero-free) ---
    phis = np.linspace(0.0, math.pi, n_phi)
    rows = []
    arg_P = arg_Z = arg_zeta = None
    max_abs_E = 0.0
    max_abs_Im_far = 0.0
    max_abs_Im_Rpeel = 0.0  # Im(log P - m log(s-rho))

    for phi in phis:
        s = rho + r * mp.exp(mp.j * phi)
        sig, tt = float(s.real), float(s.imag)
        logP = log_P_X(s, X, primes, dps)
        logZ_local, logZ_far, n_z = log_Z_split(s, X, gammas, gamma, dps, window)
        logZ_all = logZ_local + logZ_far
        try:
            log_zeta = mp.log(mp.zeta(s))
        except Exception as ex:
            rows.append({"phi": float(phi), "error": str(ex)})
            continue
        E = log_zeta - logP - logZ_all
        abs_E = float(abs(E))
        max_abs_E = max(max_abs_E, abs_E)
        max_abs_Im_far = max(max_abs_Im_far, abs(float(logZ_far.imag)))

        # peeled remainder: log P - m log(s-rho)  (principal log; imag tracked vs phi)
        log_smr = mp.log(s - rho)  # on path arg = phi
        Rpeel = logP - m * log_smr
        max_abs_Im_Rpeel = max(max_abs_Im_Rpeel, abs(float(Rpeel.imag)))

        aP, aZ, aZeta = float(logP.imag), float(logZ_all.imag), float(log_zeta.imag)
        if arg_P is None:
            arg_P, arg_Z, arg_zeta = aP, aZ, aZeta
        else:
            arg_P = continuous_arg_track(arg_P, aP)
            arg_Z = continuous_arg_track(arg_Z, aZ)
            arg_zeta = continuous_arg_track(arg_zeta, aZeta)

        rows.append(
            {
                "phi": float(phi),
                "sigma": sig,
                "t": tt,
                "arg_P": arg_P,
                "arg_Z": arg_Z,
                "arg_zeta": arg_zeta,
                "Im_Rpeel": float(Rpeel.imag),
                "abs_E": abs_E,
                "Im_logZ_far": float(logZ_far.imag),
                "Im_logZ_local": float(logZ_local.imag),
            }
        )

    if not rows or ("error" in rows[0] and len(rows) < 3):
        return {"gamma": gamma, "r": r, "X": X, "HD": hd, "error": "semicircle failed", "samples": rows}

    d_arg_P_semi = rows[-1]["arg_P"] - rows[0]["arg_P"]
    d_arg_Z = rows[-1]["arg_Z"] - rows[0]["arg_Z"]
    d_arg_zeta = rows[-1]["arg_zeta"] - rows[0]["arg_zeta"]

    # --- B. Approach path: sigma 1.5 → 0.5+r at t=gamma (correct geometry for phase growth) ---
    n_app = max(12, n_phi)
    sigs = np.linspace(1.5, 0.5 + r, n_app)
    app_pts = [(float(sg), gamma) for sg in sigs]
    app_args, d_arg_P_app = track_arg_P_along(app_pts, X, primes, dps)

    # hybrid |E| at approach endpoint
    s_end = mp.mpc(0.5 + r, gamma)
    logP_e = log_P_X(s_end, X, primes, dps)
    lz_l, lz_f, _ = log_Z_split(s_end, X, gammas, gamma, dps, window)
    try:
        E_end = float(abs(mp.log(mp.zeta(s_end)) - logP_e - lz_l - lz_f))
    except Exception:
        E_end = None

    return {
        "gamma": gamma,
        "r": r,
        "X": X,
        "c_r": c_r,
        "m": m,
        "n_phi": n_phi,
        "HD": hd,
        "semicircle": {
            "Delta_arg_P": d_arg_P_semi,
            "Delta_arg_Z": d_arg_Z,
            "Delta_arg_zeta": d_arg_zeta,
            "Delta_arg_s_minus_rho": math.pi,
            "max_abs_E": max_abs_E,
            "max_abs_Im_logZ_far": max_abs_Im_far,
            "max_abs_Im_Rpeel": max_abs_Im_Rpeel,
            "note": (
                "P_X is zero-free entire; monodromy of arg P about a zeta-zero is ~0. "
                "Local monodromy sits in Z / zeta, not in P."
            ),
        },
        "approach": {
            "sigma_start": 1.5,
            "sigma_end": 0.5 + r,
            "t": gamma,
            "Delta_arg_P": d_arg_P_app,
            "arg_P_start": app_args[0] if app_args else None,
            "arg_P_end": app_args[-1] if app_args else None,
            "abs_E_at_end": E_end,
            "note": "Horizontal approach at t=gamma; natural path for continuous phase of P.",
        },
        "m_pi": m * math.pi,
        "samples_endpoints": {"semi_start": rows[0], "semi_end": rows[-1]},
        "n_samples_ok": len(rows),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-zeros", type=int, default=6)
    ap.add_argument("--x-max", type=int, default=12000)
    ap.add_argument("--X-hybrid", type=float, default=0.0, help="0 => (log gamma)^3")
    ap.add_argument("--c-r", type=float, default=0.35)
    ap.add_argument("--n-phi", type=int, default=25)
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args(argv)

    n_zeros = 3 if args.quick else args.n_zeros
    x_max = 5000 if args.quick else args.x_max
    n_phi = 13 if args.quick else args.n_phi
    gammas = FIRST_ZERO_ORDINATES[: max(n_zeros + 5, 15)]  # extra for HD neighbours
    targets = FIRST_ZERO_ORDINATES[:n_zeros]

    print(f"sieving primes to {x_max}...", flush=True)
    primes = sieve_primes(x_max)

    results = []
    print("M1.3 paths under HD-low...", flush=True)
    for g in targets:
        if args.X_hybrid > 0:
            X = args.X_hybrid
        else:
            X = max(20.0, math.log(2 + g) ** 3)
        print(f"  gamma={g:.4f} X={X:.4g} ...", flush=True)
        rec = run_path_for_zero(g, gammas, primes, X, args.c_r, n_phi)
        results.append(rec)
        if "semicircle" in rec:
            sc, ap = rec["semicircle"], rec["approach"]
            print(
                f"    HD isolated={rec['HD']['isolated']} gap={rec['HD']['nearest_other_gap']:.4f} "
                f"r={rec['r']:.5f}  semiΔargP={sc['Delta_arg_P']:.4f} "
                f"appΔargP={ap['Delta_arg_P']:.4f}  max|E|_semi={sc['max_abs_E']:.4g} "
                f"max|Im Rpeel|={sc['max_abs_Im_Rpeel']:.4g}",
                flush=True,
            )

    def mean_nested(*keys):
        vals = []
        for r in results:
            cur = r
            ok = True
            for k in keys:
                if not isinstance(cur, dict) or k not in cur:
                    ok = False
                    break
                cur = cur[k]
            if ok and cur is not None:
                vals.append(cur)
        return float(np.mean(vals)) if vals else None

    summary = {
        "n_zeros": n_zeros,
        "n_isolated": sum(1 for r in results if r.get("HD", {}).get("isolated")),
        "mean_semi_Delta_arg_P": mean_nested("semicircle", "Delta_arg_P"),
        "mean_approach_Delta_arg_P": mean_nested("approach", "Delta_arg_P"),
        "mean_semi_max_abs_E": mean_nested("semicircle", "max_abs_E"),
        "mean_semi_max_abs_Im_Rpeel": mean_nested("semicircle", "max_abs_Im_Rpeel"),
        "mean_semi_max_abs_Im_Z_far": mean_nested("semicircle", "max_abs_Im_logZ_far"),
        "honesty": (
            "Semicircle monodromy of arg P is ~0 because P_X never vanishes. "
            "Approach path measures gradual phase of P. HD-low = Odlyzko isolation. No proof claim."
        ),
    }

    out = {
        "provenance": {
            "status_label": "RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF",
            "proves_RH": False,
            "proves_M1_2": False,
            "proves_M1_3": False,
            "model_constants": False,
            "HD": "HD-low: Odlyzko first zeros; isolation in D(rho,2r)",
            "path": "s = rho + r exp(i phi), phi in [0,pi], r = c_r / log(2+|gamma|)",
            "U": "E1",
            "doc": "RH_M1_3_Path_Design.md",
        },
        "parameters": {
            "n_zeros": n_zeros,
            "x_max_primes": x_max,
            "X_hybrid": args.X_hybrid if args.X_hybrid > 0 else "(log(2+gamma))^3",
            "c_r": args.c_r,
            "n_phi": n_phi,
        },
        "summary": summary,
        "zeros": results,
        "status": "M1_3_PATH_HD_LOW_DIAGNOSTIC_EXECUTED_NO_PROOF_CLAIM",
    }

    path = Path(__file__).resolve().parents[1] / "rh_M1_3_path_diagnostic_results.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("M1.3 HD-low diagnostic — NO PROOF CLAIM")
    print("summary:", json.dumps(summary, indent=2))
    print("wrote", path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
