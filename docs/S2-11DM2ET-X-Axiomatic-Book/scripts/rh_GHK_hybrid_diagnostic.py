#!/usr/bin/env python3
"""
GHK hybrid diagnostic for RH phase programme (strengthened).

At on-line zeros and off-line |zeta| minima, compare:
  arg ζ ≈ arg P_X + arg Z_X^{trunc}
where P_X = exp(sum_{n<=X} Λ(n)/(n^s log n))  [GHK P]
and Z_X^{trunc} uses nearby Odlyzko zeros with U in one of:

  local : U(z) = -log(z) - γ          (singular part of E1)
  e1    : U(z) = E1(z)                 (full exponential integral)
  full  : U(z) = ∫ u(x) E1(z log x) dx (GHK smoothed kernel, fixed f)

DIAGNOSTIC ONLY — no RH / M1.2 proof claim.
No model constants.

Status: RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF
See: RH_Akatsuka_GHK_Survey.md, RH_M1_2_Explicit_Hybrid_Constants.md
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


# ---------------------------------------------------------------------------
# Fixed bump f on (0,1): f(t) ∝ exp(-1/(t(1-t))), mass 1.
# Used for U-mode "full". Derivatives not needed for the probe.
# ---------------------------------------------------------------------------
_F_NORM: float | None = None


def _raw_bump(t: float) -> float:
    if t <= 0.0 or t >= 1.0:
        return 0.0
    return math.exp(-1.0 / (t * (1.0 - t)))


def bump_f_normalized(t: float) -> float:
    global _F_NORM
    if _F_NORM is None:
        # trapezoid mass of raw bump on (0,1)
        xs = np.linspace(1e-9, 1.0 - 1e-9, 2001)
        ys = np.array([_raw_bump(float(x)) for x in xs])
        _F_NORM = float(np.trapezoid(ys, xs))
        if _F_NORM <= 0:
            _F_NORM = 1.0
    return _raw_bump(t) / _F_NORM


def U_local(z: mp.mpc) -> mp.mpc:
    """Singular part: E1(z) ~ -log(z) - γ as z→0."""
    return -mp.log(z) - mp.euler


def U_E1(z: mp.mpc) -> mp.mpc:
    """Full exponential integral E1(z) = expint(1,z). Principal branch."""
    # mpmath: expint(1, z) = E_1(z) for complex z (branch cut on negative real)
    return mp.expint(1, z)


def U_full(z: mp.mpc, X: float, n_quad: int = 48) -> mp.mpc:
    """
    GHK U(z) = ∫_0^∞ u(x) E1(z log x) dx
    with u(x) = X/x * f(X log(x/e)+1), supp ⊂ [e^{1-1/X}, e].

    Change of variable: tau = X log(x/e)+1 ∈ [0,1],
      x = exp(1 - (1-tau)/X),  dx/x = d tau / X,
      u(x) dx = f(tau) d tau.
    And log x = 1 - (1-tau)/X, so
      U(z) = ∫_0^1 f(tau) E1( z * (1 - (1-tau)/X) ) d tau.
    """
    if n_quad < 8:
        n_quad = 8
    from numpy.polynomial.legendre import leggauss

    xi, wi = leggauss(n_quad)
    # map [-1,1] -> [0,1]
    taus = 0.5 * (xi + 1.0)
    weights = 0.5 * wi
    total = mp.mpc(0)
    Xmp = mp.mpf(X)
    for tau, w in zip(taus, weights):
        ft = bump_f_normalized(float(tau))
        if ft == 0.0:
            continue
        # log x = 1 - (1-tau)/X
        logx = 1 - (1 - mp.mpf(float(tau))) / Xmp
        if logx <= 0:
            continue
        arg = z * logx
        # avoid exact branch issues at 0
        if abs(arg) < mp.mpf("1e-30"):
            arg = mp.mpc(mp.mpf("1e-20"), mp.mpf("1e-20"))
        total += mp.mpf(ft) * mp.mpf(float(w)) * U_E1(arg)
    return total


def U_dispatch(z: mp.mpc, mode: str, X: float, n_quad: int) -> mp.mpc:
    if mode == "local":
        return U_local(z)
    if mode == "e1":
        return U_E1(z)
    if mode == "full":
        return U_full(z, X, n_quad=n_quad)
    raise ValueError(f"unknown U mode: {mode}")


def log_Z_X_trunc(
    s: mp.mpc,
    X: float,
    zero_gammas: list[float],
    dps: int,
    u_mode: str,
    n_quad: int,
    window_factor: float = 4.0,
) -> tuple[mp.mpc, int]:
    """
    log Z_X ≈ -sum_rho U((s-rho) log X) for nearby zeros on the critical line.
    window: |t - gamma| <= window_factor * pi / log X  (+0.5 absolute floor)
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
        if abs(z) < mp.mpf("1e-18"):
            z = mp.mpc(mp.mpf("1e-12"), mp.mpf("1e-12"))
        total -= U_dispatch(z, u_mode, X, n_quad)
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
    u_mode: str,
    n_quad: int,
    K_shape: int = 2,
) -> dict:
    dps = dps_for_t(t)
    mp.mp.dps = dps
    s = mp.mpc(sigma, t)

    logP = log_P_X_GHK(s, X, primes, dps)
    logZ, n_zeros_used = log_Z_X_trunc(s, X, zero_gammas, dps, u_mode, n_quad)
    log_hybrid = logP + logZ

    try:
        log_zeta = mp.log(mp.zeta(s))
        zeta_abs = float(abs(mp.zeta(s)))
    except Exception as ex:
        return {"label": label, "error": str(ex)}

    rem = log_zeta - log_hybrid
    arg_zeta = continuous_arg_from_log(log_zeta)
    arg_P = continuous_arg_from_log(logP)
    arg_Z = continuous_arg_from_log(logZ)
    arg_sum = arg_P + arg_Z
    while arg_sum - arg_zeta > math.pi:
        arg_sum -= 2 * math.pi
    while arg_sum - arg_zeta < -math.pi:
        arg_sum += 2 * math.pi

    nearest = min(zero_gammas, key=lambda g: abs(g - t))
    rho = complex(0.5, nearest)
    s_c = complex(sigma, t)
    m_arg = abs(math.atan2(s_c.imag - rho.imag, s_c.real - rho.real))

    # GHK shape terms (K=2 default): X^{K+2}/(|t| log X)^K  and  X^{-σ} log X
    logX = math.log(X)
    t_abs = max(abs(t), 2.0)
    shape1 = (X ** (K_shape + 2)) / ((t_abs * logX) ** K_shape)
    shape2 = (X ** (-sigma)) * logX
    abs_rem = float(abs(rem))
    abs_im_rem = abs(float(rem.imag))

    err_bound_shape = {
        "K": K_shape,
        "X_Kp2_over_t_logX_K": float(shape1),
        "X_to_minus_sigma_logX": float(shape2),
        "abs_E_GHK_proxy": abs_rem,
        "abs_Im_E_GHK_proxy": abs_im_rem,
        # diagnostic ratios (NOT rigorous c_i)
        "ratio_abs_rem_over_shape1": (abs_rem / shape1) if shape1 > 0 else None,
        "ratio_abs_rem_over_shape2": (abs_rem / shape2) if shape2 > 0 else None,
    }

    return {
        "label": label,
        "kind": kind,
        "sigma": sigma,
        "t": t,
        "X": X,
        "U_mode": u_mode,
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
        "Re_E_GHK_proxy": float(rem.real),
        "Im_E_GHK_proxy": float(rem.imag),
        "abs_E_GHK_proxy": abs_rem,
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


def mean_abs(rows, key):
    vals = [abs(r[key]) for r in rows if key in r and r[key] is not None]
    return float(np.mean(vals)) if vals else None


def run_regime(
    t_centers: list[float],
    zeros: list[float],
    primes: list[int],
    X_hyb: float,
    u_mode: str,
    n_quad: int,
    n_off: int,
    quick: bool,
) -> dict:
    online = []
    print(f"  on-line U={u_mode}...", flush=True)
    for t in t_centers:
        sig, tt = 0.5, t + 0.02
        lab = f"near_zero_s={sig:.2f}_t={tt:.3f}"
        rec = evaluate_at_point(
            sig, tt, X_hyb, primes, zeros, lab, "near_critical_zero", u_mode, n_quad
        )
        online.append(rec)
        if "error" not in rec:
            print(
                f"    {lab}: |arg err|={abs(rec['arg_error_zeta_minus_PZ']):.4g} "
                f"|E|={rec['abs_E_GHK_proxy']:.4g} Im(logZ)={rec['Im_log_Z_trunc']:.4g}",
                flush=True,
            )

    print(f"  offline minima U={u_mode}...", flush=True)
    minima = find_offline_minima(
        t_centers[: max(3, len(t_centers) // 2)], n_keep=n_off
    )
    offline = []
    for m in minima:
        lab = f"offmin_s={m['sigma']:.3f}_t={m['t']:.3f}"
        rec = evaluate_at_point(
            m["sigma"], m["t"], X_hyb, primes, zeros, lab, "offline_abs_zeta_min", u_mode, n_quad
        )
        rec["zeta_abs_center"] = m["zeta_abs"]
        offline.append(rec)
        if "error" not in rec:
            print(
                f"    {lab}: |arg err|={abs(rec['arg_error_zeta_minus_PZ']):.4g} "
                f"|E|={rec['abs_E_GHK_proxy']:.4g} "
                f"Im(R)={rec['Im_log_zeta_minus_log_P']:.4g} "
                f"Im(logZ)={rec['Im_log_Z_trunc']:.4g}",
                flush=True,
            )

    summary = {
        "U_mode": u_mode,
        "mean_abs_arg_error_online": mean_abs(online, "arg_error_zeta_minus_PZ"),
        "mean_abs_arg_error_offline": mean_abs(offline, "arg_error_zeta_minus_PZ"),
        "mean_abs_E_online": mean_abs(online, "abs_E_GHK_proxy"),
        "mean_abs_E_offline": mean_abs(offline, "abs_E_GHK_proxy"),
        "mean_abs_Im_R_online": mean_abs(online, "Im_log_zeta_minus_log_P"),
        "mean_abs_Im_R_offline": mean_abs(offline, "Im_log_zeta_minus_log_P"),
        "mean_abs_Im_logZ_online": mean_abs(online, "Im_log_Z_trunc"),
        "mean_abs_Im_logZ_offline": mean_abs(offline, "Im_log_Z_trunc"),
    }
    return {
        "summary": summary,
        "online": online,
        "offline": offline,
        "offline_minima": minima,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--x-max", type=int, default=15000)
    ap.add_argument("--X-hybrid", type=float, default=200.0, help="GHK mediator X")
    ap.add_argument("--n-zeros", type=int, default=6)
    ap.add_argument(
        "--U-mode",
        type=str,
        default="e1",
        choices=["local", "e1", "full", "all"],
        help="U kernel: local / e1 / full / all (compare)",
    )
    ap.add_argument("--n-quad", type=int, default=48, help="GL nodes for U=full")
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args(argv)

    x_max = 6000 if args.quick else args.x_max
    n_zeros = 3 if args.quick else args.n_zeros
    X_hyb = 80.0 if args.quick else args.X_hybrid
    n_quad = 24 if args.quick else args.n_quad
    n_off = 3 if args.quick else 6

    print(f"sieving to {x_max}...", flush=True)
    primes = sieve_primes(x_max)
    zeros = FIRST_ZERO_ORDINATES
    t_centers = FIRST_ZERO_ORDINATES[:n_zeros]

    modes = ["local", "e1", "full"] if args.U_mode == "all" else [args.U_mode]
    by_mode = {}
    for mode in modes:
        print(f"=== U-mode={mode} X={X_hyb} ===", flush=True)
        by_mode[mode] = run_regime(
            t_centers, zeros, primes, X_hyb, mode, n_quad, n_off, args.quick
        )

    # comparison table when multiple modes
    comparison = {}
    if len(modes) > 1:
        for mode in modes:
            sm = by_mode[mode]["summary"]
            comparison[mode] = {
                "mean_abs_arg_error_online": sm["mean_abs_arg_error_online"],
                "mean_abs_arg_error_offline": sm["mean_abs_arg_error_offline"],
                "mean_abs_E_online": sm["mean_abs_E_online"],
                "mean_abs_E_offline": sm["mean_abs_E_offline"],
            }

    primary = modes[0]
    primary_block = by_mode[primary]

    out = {
        "provenance": {
            "status_label": "RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF",
            "proves_RH": False,
            "proves_M1_2": False,
            "model_constants": False,
            "GHK": "arXiv:math/0511182 Theorem 1",
            "survey": "RH_Akatsuka_GHK_Survey.md",
            "constants_note": "RH_M1_2_Explicit_Hybrid_Constants.md",
        },
        "parameters": {
            "x_max_primes": x_max,
            "X_hybrid": X_hyb,
            "n_zeros_online": n_zeros,
            "U_modes_run": modes,
            "U_mode_primary": primary,
            "U_local": "U(z)=-log(z)-euler",
            "U_e1": "U(z)=E1(z)=expint(1,z)",
            "U_full": "U(z)=∫ f(tau) E1(z*(1-(1-tau)/X)) d tau, bump f on (0,1)",
            "n_quad_full": n_quad,
            "Z_trunc": "zeros with |t-gamma| <= 4*pi/log X (+0.5)",
            "note_c_i": (
                "err_bound_shape ratios are diagnostic only; "
                "not rigorous global c1,c2,c3 (see RH_M1_2_Explicit_Hybrid_Constants.md)"
            ),
        },
        "comparison": comparison,
        "summary": primary_block["summary"],
        "by_mode": {m: {"summary": by_mode[m]["summary"]} for m in modes},
        "online": primary_block["online"],
        "offline": primary_block["offline"],
        "offline_minima": primary_block["offline_minima"],
        # keep full rows for all modes when comparing (can be large)
        "online_by_mode": {m: by_mode[m]["online"] for m in modes},
        "offline_by_mode": {m: by_mode[m]["offline"] for m in modes},
        "status": "GHK_HYBRID_DIAGNOSTIC_E1_EXECUTED_NO_PROOF_CLAIM",
    }

    path = Path(__file__).resolve().parents[1] / "rh_GHK_hybrid_diagnostic_results.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("GHK hybrid diagnostic — NO PROOF / NO RH CLAIM")
    for mode in modes:
        sm = by_mode[mode]["summary"]
        print(
            f"  [{mode}] |arg err| on/off: {sm['mean_abs_arg_error_online']:.6g} / "
            f"{sm['mean_abs_arg_error_offline']:.6g}  "
            f"|E| on/off: {sm['mean_abs_E_online']:.6g} / {sm['mean_abs_E_offline']:.6g}"
        )
    print("wrote", path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
