#!/usr/bin/env python3
"""
M1.2 remainder sketch — R_bound with frozen pure constants.

Constants from rh/RH_M1_2_Constants_Isolation.md:
  C_u0 = 1.12  (Re z >= 0 medium)
  C_Sigma_log = 1.36  (4 * A0 with A0=0.34 literature placeholder)
  Classical Sigma_med majorant ~ C_Sigma_log * log(|t|+H)

Also reports incomplete medium sum from known zeros (diagnostic only).

Status: M1_2_SKETCH_NO_RH_CLAIM
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

# Frozen from pure-constants note (not invented optimized decimals)
C_U0 = 1.12
A0 = 0.34
C_SIGMA_LOG = 4.0 * A0  # 1.36
C_FAR = 1.0
C_ARITH = 2.0

ODLYZKO_GAMMAS = [
    14.134725141734693,
    21.022039638771555,
    25.010857580145689,
    30.424876125859513,
    32.935061587739190,
    37.586178158825671,
    40.918719012147495,
    43.327073280914999,
    48.005150881167160,
    49.773832477672302,
    52.970321477714461,
    56.446247697063395,
    59.347044002602353,
    60.831778524609810,
    65.112544048081607,
]


def sigma_med_classical(t: float, X: float, H: float) -> float:
    """Majorant (Sigma-cl-exp) dominant + secondary terms."""
    logX = math.log(max(X, 3.0))
    r_loc = 1.0 / logX
    # K_H ~ log2(H / r_loc)
    if H <= r_loc:
        k_h = 0
    else:
        k_h = max(0, int(math.ceil(math.log(H / r_loc) / math.log(2.0))))
    log_term = math.log(abs(t) + H + 2.0)
    dominant = C_SIGMA_LOG * log_term
    secondary = (4.0 / math.pi) * ((k_h + 1) * log_term / logX + 1.0)
    return dominant + secondary


def R_bound(
    sigma: float,
    t: float,
    X: float,
    K: int,
    H: float,
    zeros: list[complex],
    rho_star: complex | None,
) -> dict:
    logX = math.log(max(X, 2.0))
    r_loc = 1.0 / logX
    denom = (abs(t) * logX) ** K
    term_far = C_FAR * (X ** (K + 2)) / denom if denom > 0 else float("inf")
    term_arith = C_ARITH * (X ** (-sigma)) * logX

    # Classical majorant (complete — does not need zero list)
    sig_cl = sigma_med_classical(t, X, H)
    term_med_cl = C_U0 * sig_cl

    # Incomplete medium from known zeros (diagnostic)
    sigma_med_known = 0.0
    n_med = n_local = n_far = n_right = 0
    for rho in zeros:
        if rho_star is not None and abs(rho - rho_star) < 1e-12:
            continue
        dist = abs(complex(sigma, t) - rho)
        beta = rho.real
        if dist <= r_loc:
            n_local += 1
            continue
        if dist <= H:
            n_med += 1
            if beta > sigma:
                n_right += 1  # should use power/density, not C_u0
            sigma_med_known += min(1.0, 1.0 / (dist * logX))
        else:
            n_far += 1

    term_med_known = C_U0 * sigma_med_known
    total_cl = term_med_cl + term_far + term_arith
    ghk_useful = term_far < 1.0

    # P1 half-turn test: need m*pi > 2 R_bound
    half_turn_margin_cl = math.pi - 2.0 * total_cl

    return {
        "R_bound_classical": total_cl,
        "term_med_classical": term_med_cl,
        "Sigma_med_classical": sig_cl,
        "term_med_known_zeros_only": term_med_known,
        "Sigma_med_known_zeros_only": sigma_med_known,
        "term_far_power": term_far,
        "term_arith": term_arith,
        "n_local_excluded": n_local,
        "n_medium": n_med,
        "n_medium_beta_gt_sigma": n_right,
        "n_far": n_far,
        "r_loc": r_loc,
        "H": H,
        "ghk_power_error_useful": ghk_useful,
        "P1_half_turn_margin_classical": half_turn_margin_cl,
        "P1_fires_classical": half_turn_margin_cl > 0,
        "constants": {
            "C_u0": C_U0,
            "A0": A0,
            "C_Sigma_log": C_SIGMA_LOG,
        },
        "note": (
            "Classical Sigma_med uses N-window majorant; known-zero sum is incomplete. "
            "NO_RH_CLAIM."
        ),
    }


def choose_X(t: float, mode: str, x_flag: float | None) -> float:
    if x_flag is not None:
        return x_flag
    lt = math.log(abs(t) + 3.0)
    if mode == "log2":
        return max(3.0, lt ** 2)
    if mode == "log3":
        return max(3.0, lt ** 3)
    if mode == "log":
        return max(3.0, lt)
    return max(3.0, lt ** 2)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--x", type=float, default=None)
    ap.add_argument("--x-mode", default="log2", choices=["log", "log2", "log3"])
    ap.add_argument("--K", type=int, default=4)
    ap.add_argument("--sigma", type=float, default=0.6)
    ap.add_argument("--t", type=float, default=None, help="default: first zero height")
    args = ap.parse_args()

    zeros = [complex(0.5, g) for g in ODLYZKO_GAMMAS]
    t = args.t if args.t is not None else ODLYZKO_GAMMAS[0]
    X = choose_X(t, args.x_mode, args.x)
    H = math.log(X) ** 2
    rho_star = complex(0.5, ODLYZKO_GAMMAS[0])

    # Probe at off-line test point near first zero height
    res = R_bound(args.sigma, t, X, args.K, H, zeros, rho_star if abs(t - ODLYZKO_GAMMAS[0]) < 1e-9 else None)
    out = {
        "status": "M1_2_SKETCH_NO_RH_CLAIM",
        "sigma": args.sigma,
        "t": t,
        "X": X,
        "K": args.K,
        "H": H,
        **res,
    }
    path = Path("/workspace/rh/rh_M1_2_remainder_sketch_results.json")
    path.write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))
    print(f"\nWrote {path}")


if __name__ == "__main__":
    main()
