#!/usr/bin/env python3
"""
RH pure Cat A — batch execution of recommended research paths (diagnostics only).

Paths:
  R1  Regularised remainder on approach paths (GHK peel via local U=E1)
  R2  Multi-X approach: Delta arg P vs log log X
  R3  M1.4-style smoothed A_X at fixed height
  R4  L2 on-line vs L3 off-line |A|-style phase samples
  R5  A2 multi-method cross-check (tighter safety)

NO RH / M1.2 / target-lemma proof claim.
Status: RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF
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
]


def dps_for_t(t: float, base: int = 28) -> int:
    return min(85, base + max(0, int(math.log10(max(abs(t), 2)) + 6)))


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


def von_mangoldt(x: float, primes: list[int]) -> list[tuple[int, float]]:
    out = []
    for p in primes:
        if p > x:
            break
        pk, lp = p, math.log(p)
        while pk <= x:
            out.append((pk, lp))
            if pk > x / p:
                break
            pk *= p
    out.sort(key=lambda z: z[0])
    return out


def log_P_X(s: mp.mpc, X: float, primes: list[int], dps: int) -> mp.mpc:
    mp.mp.dps = dps
    tot = mp.mpc(0)
    for n, Lam in von_mangoldt(X, primes):
        tot += Lam / (mp.power(n, s) * mp.log(n))
    return tot


def U_E1(z: mp.mpc) -> mp.mpc:
    if abs(z) < mp.mpf("1e-18"):
        z = mp.mpc(mp.mpf("1e-12"), mp.mpf("1e-12"))
    return mp.expint(1, z)


def unwrap(prev: float, a: float) -> float:
    while a - prev > math.pi:
        a -= 2 * math.pi
    while a - prev < -math.pi:
        a += 2 * math.pi
    return a


def continuous_arg_P_path(
    points: list[tuple[float, float]], X: float, primes: list[int]
) -> tuple[list[float], float]:
    args = []
    prev = None
    for sig, t in points:
        dps = dps_for_t(t)
        a = float(log_P_X(mp.mpc(sig, t), X, primes, dps).imag)
        if prev is None:
            prev = a
        else:
            a = unwrap(prev, a)
            prev = a
        args.append(a)
    return args, (args[-1] - args[0] if args else 0.0)


# ---------------------------------------------------------------------------
# R1: Regularised remainder on approach path
# R_reg := log P + U((s-rho) log X) - log zeta   (= -log Z_far - E in GHK)
# M1.2-reg: |Im R_reg| vs m |arg(s-rho)| is the wrong comparison near on-line
# zeros (arg small on horizontal path). Instead report |Im R_reg| and |E|.
# ---------------------------------------------------------------------------
def path_R1_regularised(
    gamma: float,
    gammas: list[float],
    primes: list[int],
    X: float,
    n_pts: int = 24,
) -> dict:
    r = 0.35 / math.log(2 + abs(gamma))
    sigs = np.linspace(1.5, 0.5 + r, n_pts)
    rho = complex(0.5, gamma)
    window = max(5.0 * math.pi / math.log(X), 2.0)
    rows = []
    max_abs_Rreg = 0.0
    max_abs_E = 0.0
    max_abs_Im_far = 0.0
    arg_P_prev = None
    args_P = []

    for sig in sigs:
        dps = dps_for_t(gamma)
        mp.mp.dps = dps
        s = mp.mpc(float(sig), gamma)
        logP = log_P_X(s, X, primes, dps)
        logX = mp.log(X)
        z_loc = (s - mp.mpc(mp.mpf("0.5"), gamma)) * logX
        Uloc = U_E1(z_loc)

        # far zeros
        far = mp.mpc(0)
        n_far = 0
        for g in gammas:
            if abs(g - gamma) < 1e-12:
                continue
            if abs(g - gamma) > window and abs(float(s.imag) - g) > window:
                continue
            far -= U_E1((s - mp.mpc(mp.mpf("0.5"), g)) * logX)
            n_far += 1

        try:
            logz = mp.log(mp.zeta(s))
        except Exception as ex:
            rows.append({"sigma": float(sig), "error": str(ex)})
            continue

        # Regularised: log P + U_local  should ≈ log zeta + far + E_structure
        # R_reg = log P + U_local - log zeta   (= -far - E if hybrid exact with only local+far)
        R_reg = logP + Uloc - logz
        E_hyb = logz - logP + Uloc + far  # log zeta - log P - log Z_local - log Z_far
        # log Z_local = -U_local, so logP + logZ_local + logZ_far = logP - Uloc + far
        # E = logz - (logP - Uloc + far) = logz - logP + Uloc - far
        E = logz - logP + Uloc - far

        abs_R = float(abs(R_reg))
        abs_E = float(abs(E))
        max_abs_Rreg = max(max_abs_Rreg, abs_R)
        max_abs_E = max(max_abs_E, abs_E)
        max_abs_Im_far = max(max_abs_Im_far, abs(float(far.imag)))

        aP = float(logP.imag)
        if arg_P_prev is None:
            arg_P_prev = aP
        else:
            aP = unwrap(arg_P_prev, aP)
            arg_P_prev = aP
        args_P.append(aP)

        # distance to rho
        dist = abs(complex(float(sig), gamma) - rho)
        rows.append(
            {
                "sigma": float(sig),
                "dist_to_rho": dist,
                "arg_P": aP,
                "Im_R_reg": float(R_reg.imag),
                "Re_R_reg": float(R_reg.real),
                "abs_R_reg": abs_R,
                "abs_E_hybrid": abs_E,
                "Im_far": float(far.imag),
                "n_far": n_far,
            }
        )

    return {
        "gamma": gamma,
        "X": X,
        "r": r,
        "Delta_arg_P": args_P[-1] - args_P[0] if args_P else None,
        "max_abs_R_reg": max_abs_Rreg,
        "max_abs_E_hybrid": max_abs_E,
        "max_abs_Im_far": max_abs_Im_far,
        "mean_abs_R_reg": float(np.mean([r["abs_R_reg"] for r in rows if "abs_R_reg" in r]))
        if rows
        else None,
        "endpoint": rows[-1] if rows else None,
        "n_ok": len(rows),
    }


# ---------------------------------------------------------------------------
# R2: multi-X Delta arg P on fixed approach
# ---------------------------------------------------------------------------
def path_R2_multi_X(
    gamma: float, primes: list[int], X_list: list[float], n_pts: int = 20
) -> dict:
    r = 0.35 / math.log(2 + abs(gamma))
    pts = [(float(s), gamma) for s in np.linspace(1.5, 0.5 + r, n_pts)]
    series = []
    for X in X_list:
        if X > primes[-1]:
            continue
        _, delta = continuous_arg_P_path(pts, X, primes)
        series.append(
            {
                "X": X,
                "log_log_X": math.log(math.log(X)) if X > math.e else None,
                "Delta_arg_P": delta,
                "abs_Delta_arg_P": abs(delta),
            }
        )
    return {"gamma": gamma, "series": series}


# ---------------------------------------------------------------------------
# R3: M1.4 smoothed A_X — average arg P over log-uniform X in [X, X^2]
# ---------------------------------------------------------------------------
def path_R3_A_X(
    sigma: float,
    t: float,
    primes: list[int],
    X0: float,
    n_X: int = 12,
) -> dict:
    """A_X ≈ mean_{Y in [X0, X0^2]} arg P_Y(sigma+it) with continuous branch in Y."""
    if X0**2 > primes[-1]:
        X1 = float(primes[-1])
    else:
        X1 = X0**2
    Xs = np.exp(np.linspace(math.log(X0), math.log(max(X0 * 1.01, X1)), n_X))
    dps = dps_for_t(t)
    args = []
    prev = None
    for X in Xs:
        a = float(log_P_X(mp.mpc(sigma, t), float(X), primes, dps).imag)
        if prev is None:
            prev = a
        else:
            a = unwrap(prev, a)
            prev = a
        args.append(a)
    A = float(np.mean(args))
    return {
        "sigma": sigma,
        "t": t,
        "X0": X0,
        "X1": float(Xs[-1]),
        "n_X": n_X,
        "A_X_mean_arg": A,
        "arg_at_X0": args[0],
        "arg_at_X1": args[-1],
        "arg_range": max(args) - min(args),
        "args": args,
    }


# ---------------------------------------------------------------------------
# R4: L2 on-line (near zeros) vs L3 off-line minima phase samples
# ---------------------------------------------------------------------------
def find_offline_min(t0: float) -> dict:
    best = None
    for sig in np.linspace(0.60, 0.90, 16):
        for tt in np.linspace(t0 - 1.5, t0 + 1.5, 16):
            mp.mp.dps = dps_for_t(tt, base=16)
            z = float(abs(mp.zeta(mp.mpc(sig, tt))))
            if best is None or z < best["zeta_abs"]:
                best = {"sigma": float(sig), "t": float(tt), "zeta_abs": z}
    return best


def path_R4_L2_L3(primes: list[int], X: float, n_zeros: int = 4) -> dict:
    online = []
    offline = []
    for g in FIRST_ZERO_ORDINATES[:n_zeros]:
        # on-line: approach endpoint near zero
        r = 0.35 / math.log(2 + g)
        pts = [(float(s), g) for s in np.linspace(1.5, 0.5 + r, 16)]
        args, delta = continuous_arg_P_path(pts, X, primes)
        online.append(
            {
                "kind": "near_zero_approach",
                "gamma": g,
                "sigma_end": 0.5 + r,
                "Delta_arg_P": delta,
                "abs_Delta": abs(delta),
                "arg_end": args[-1] if args else None,
            }
        )
        # off-line minimum near this height
        m = find_offline_min(g)
        pts2 = [(float(s), m["t"]) for s in np.linspace(1.5, m["sigma"], 16)]
        args2, delta2 = continuous_arg_P_path(pts2, X, primes)
        offline.append(
            {
                "kind": "offline_min_approach",
                "center": m,
                "Delta_arg_P": delta2,
                "abs_Delta": abs(delta2),
                "arg_end": args2[-1] if args2 else None,
            }
        )
    return {
        "X": X,
        "online": online,
        "offline": offline,
        "mean_abs_Delta_online": float(np.mean([o["abs_Delta"] for o in online])),
        "mean_abs_Delta_offline": float(np.mean([o["abs_Delta"] for o in offline])),
    }


# ---------------------------------------------------------------------------
# R5: A2 multi-method — denser FD + complex-step style check
# ---------------------------------------------------------------------------
def raw_bump(t: float) -> float:
    if t <= 0 or t >= 1:
        return 0.0
    return math.exp(-1.0 / (t * (1.0 - t)))


def path_R5_A2(mass: float, M2: float, K: int = 2) -> dict:
    def u_at(X, x):
        tau = X * math.log(x / math.e) + 1.0
        return (X / x) * (raw_bump(tau) / mass)

    def fornberg_weights(z, nodes, m):
        n = len(nodes) - 1
        c = np.zeros((n + 1, m + 1))
        c[0, 0] = 1.0
        c1, c4 = 1.0, nodes[0] - z
        for i in range(1, n + 1):
            mn = min(i, m)
            c2, c5 = 1.0, c4
            c4 = nodes[i] - z
            for j in range(i):
                c3 = nodes[i] - nodes[j]
                c2 *= c3
                if j == i - 1:
                    for k in range(mn, 0, -1):
                        c[i, k] = c1 * (k * c[i - 1, k - 1] - c5 * c[i - 1, k]) / c2
                    c[i, 0] = -c1 * c5 * c[i - 1, 0] / c2
                for k in range(mn, 0, -1):
                    c[j, k] = (c4 * c[j, k] - k * c[j, k - 1]) / c3
                c[j, 0] = c4 * c[j, 0] / c3
            c1 = c2
        return c[:, m]

    best = 0.0
    best_at = None
    for X in [2.0, 5.0, 10.0, 50.0, 200.0]:
        for j in range(1, 800):
            tau = j / 801.0
            x = math.exp(1.0 - (1.0 - tau) / X)
            hs = max(1e-7 * x, 1e-12)
            nodes = [m * hs for m in range(-6, 7)]
            uvals = [u_at(X, x + xi) for xi in nodes]
            w = fornberg_weights(0.0, nodes, K)
            uk = abs(float(np.dot(w, uvals)))
            ratio = uk / (M2 * X ** (K + 1))
            if ratio > best:
                best = ratio
                best_at = {"X": X, "tau": tau, "ratio": ratio, "uK": uk}
    return {
        "A2_raw_max_dense": best,
        "A2_with_5pct": best * 1.05,
        "A2_with_10pct": best * 1.10,
        "at": best_at,
        "prior_A2_with_10pct": 0.16897,
        "M2_used": M2,
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--x-max", type=int, default=20000)
    args = ap.parse_args(argv)

    x_max = 8000 if args.quick else args.x_max
    n_zeros = 3 if args.quick else 6
    n_pts = 12 if args.quick else 24

    print(f"sieving to {x_max}...", flush=True)
    primes = sieve_primes(x_max)
    gammas = FIRST_ZERO_ORDINATES[: max(n_zeros + 8, 12)]
    targets = FIRST_ZERO_ORDINATES[:n_zeros]

    # R1
    print("R1 regularised remainder...", flush=True)
    r1 = []
    for g in targets:
        X = max(25.0, math.log(2 + g) ** 3)
        rec = path_R1_regularised(g, gammas, primes, X, n_pts=n_pts)
        r1.append(rec)
        print(
            f"  g={g:.3f} max|R_reg|={rec['max_abs_R_reg']:.4g} "
            f"max|E|={rec['max_abs_E_hybrid']:.4g} ΔargP={rec['Delta_arg_P']:.4g}",
            flush=True,
        )

    # R2
    print("R2 multi-X...", flush=True)
    X_list = [30, 50, 80, 120, 200, 400, 800, 1500]
    if args.quick:
        X_list = [30, 80, 200, 500]
    X_list = [X for X in X_list if X <= primes[-1]]
    r2 = []
    for g in targets[: max(2, n_zeros // 2)]:
        rec = path_R2_multi_X(g, primes, X_list, n_pts=max(10, n_pts // 2))
        r2.append(rec)
        print(
            f"  g={g:.3f} |ΔargP| vs X: "
            + ", ".join(f"{s['X']}:{s['abs_Delta_arg_P']:.4g}" for s in rec["series"]),
            flush=True,
        )

    # R3 M1.4 A_X
    print("R3 M1.4 A_X...", flush=True)
    r3 = []
    for g in targets[:3]:
        for sig in (0.5, 0.6, 1.0):
            # slight offset from exact zero
            tt = g + (0.02 if abs(sig - 0.5) < 1e-9 else 0.0)
            rec = path_R3_A_X(sig, tt, primes, X0=40.0 if args.quick else 80.0, n_X=8 if args.quick else 14)
            r3.append(rec)
            print(
                f"  A_X s={sig:.1f}+i{tt:.2f}: mean_arg={rec['A_X_mean_arg']:.4g} "
                f"range={rec['arg_range']:.4g}",
                flush=True,
            )

    # R4 L2/L3
    print("R4 L2 vs L3...", flush=True)
    X4 = 100.0 if args.quick else 200.0
    r4 = path_R4_L2_L3(primes, X4, n_zeros=min(n_zeros, 4))
    print(
        f"  mean |ΔargP| online/offline: "
        f"{r4['mean_abs_Delta_online']:.4g} / {r4['mean_abs_Delta_offline']:.4g}",
        flush=True,
    )

    # R5 A2
    print("R5 A2 dense...", flush=True)
    xs = np.linspace(1e-12, 1 - 1e-12, 50001)
    mass = float(np.trapezoid([raw_bump(float(x)) for x in xs], xs))
    # use known M2 from optimize run
    M2 = 85.71616032090529
    r5 = path_R5_A2(mass, M2)
    print(f"  A2 dense raw={r5['A2_raw_max_dense']:.6g} +5%={r5['A2_with_5pct']:.6g}", flush=True)

    # Optimized c1 with new A2 if tighter
    D2, C_mul, C_tail = 5.0222700105, 2.0, 2.0
    A2_use = r5["A2_with_10pct"]
    c1_new = 2 * C_mul * D2 * A2_use * M2
    c2 = 2 * C_mul * C_tail

    summary = {
        "R1_mean_max_abs_R_reg": float(np.mean([r["max_abs_R_reg"] for r in r1])),
        "R1_mean_max_abs_E": float(np.mean([r["max_abs_E_hybrid"] for r in r1])),
        "R1_mean_Delta_arg_P": float(np.mean([r["Delta_arg_P"] for r in r1 if r["Delta_arg_P"] is not None])),
        "R4_mean_abs_Delta_online": r4["mean_abs_Delta_online"],
        "R4_mean_abs_Delta_offline": r4["mean_abs_Delta_offline"],
        "R5_A2_with_10pct": A2_use,
        "c1_upper_with_R5_A2": c1_new,
        "c2_upper": c2,
        "note": (
            "All diagnostics only. Regularised R_reg = logP + U_local - log zeta. "
            "No RH/target lemma claim. A_X is mean continuous arg P over X-window."
        ),
    }

    out = {
        "provenance": {
            "status_label": "RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF",
            "proves_RH": False,
            "proves_M1_2": False,
            "proves_target_lemma": False,
            "model_constants": False,
            "paths": ["R1_reg_remainder", "R2_multi_X", "R3_A_X", "R4_L2_L3", "R5_A2"],
        },
        "parameters": {"x_max": x_max, "n_zeros": n_zeros, "quick": args.quick},
        "summary": summary,
        "R1_regularised": r1,
        "R2_multi_X": r2,
        "R3_A_X": r3,
        "R4_L2_L3": r4,
        "R5_A2": r5,
        "status": "RH_RESEARCH_BATCH_EXECUTED_NO_PROOF_CLAIM",
    }

    path = Path(__file__).resolve().parents[1] / "rh_research_batch_results.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("BATCH DONE — NO PROOF CLAIM")
    print(json.dumps(summary, indent=2))
    print("wrote", path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
