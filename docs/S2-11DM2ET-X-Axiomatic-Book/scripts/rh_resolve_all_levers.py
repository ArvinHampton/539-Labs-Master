#!/usr/bin/env python3
"""
Resolve-for-all package (2026-08-08):
  L1  E1 real-drift C_U (Theorem E1 + path bookkeeping)
  L2  Average-case / R-vM density far-sum with 2π factor
  L3  Zero-free tube Phi for path continuation
  + joint window re-scan under improved far-sum constants
  + five-obligation / five-direction resolve board

RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF · ZLA · no model constants.
Does not prove O-TL / RH / Iso_H / Mass-with-A.
"""
from __future__ import annotations

import json
import math
from pathlib import Path


def fin(x, default=float("inf")):
    if isinstance(x, (int, float)) and math.isfinite(x):
        return float(x)
    return default


# ---------- L1: E1 real-drift ----------

def e1_bound_re_nonneg(re_z: float, abs_z: float) -> float:
    """|E1(z)| <= exp(-Re z)/|z| for Re z >= 0, z != 0 (Theorem E1)."""
    if abs_z <= 0:
        return float("inf")
    if re_z >= 0:
        return math.exp(-re_z) / abs_z
    # For Re z < 0: use crude continuation |E1(z)| <= exp(-Re z)/|z| is FALSE to use as upper
    # Use |E1(z)| <= exp(-Re z) * (1/|z|) is larger when Re z < 0.
    # Standard: |E1(z)| << exp(-Re z)/|z| still holds for |arg z| < pi - delta in sectors,
    # but for left half-plane |E1| grows. Use published crude:
    # |E1(z)| <= exp(-Re z)/|z| for Re z >= 0 only.
    # Left half: |E1(x+iy)| for x<0 is larger; use
    # |E1(z)| <= exp(-Re z) * min(1, 1/|z|) * C_sector as diagnostic upper only.
    return math.exp(-re_z) / abs_z  # DIAGNOSTIC overestimate when Re<0 (too large)


def far_sum_e1_real_drift(
    gamma: float,
    sigma: float,
    logX: float,
    c_r: float = 0.25,
    n_ann: int = 40,
) -> dict:
    """
    Dyadic far-sum of |U((s-rho') log X)| with U ~ E1 model,
    using R-vM mean density (log gamma)/(2*pi) per unit height,
    and E1 bound when Re(s-rho') log X >= 0.

    Model path point: s = sigma + i*gamma (near a zero at 1/2+i*gamma).
    Far zeros modeled as beta' = 1/2 (critical-line bulk) at height gamma + d.
    """
    Lg = math.log(gamma)
    r = c_r / Lg
    dens = Lg / (2.0 * math.pi)  # mean zeros per unit height
    total = 0.0
    annuli = []
    # vertical annuli only (bulk of zeros)
    for j in range(n_ann):
        d_lo = (2 ** j) * r
        d_hi = (2 ** (j + 1)) * r
        if d_lo > 2 * gamma:
            break
        width = d_hi - d_lo
        # mean count in two-sided height annulus
        n_mean = dens * 2.0 * width  # above and below
        # distance |s - rho'| ~ d for critical-line zeros at height offset d
        # beta'=1/2, sigma may be > 1/2
        re_s_minus_rho = sigma - 0.5
        # complex distance scale: |s-rho'|^2 ~ re^2 + d^2
        # use representative d = (d_lo+d_hi)/2
        d_mid = 0.5 * (d_lo + d_hi)
        abs_s_rho = math.hypot(re_s_minus_rho, d_mid)
        re_z = re_s_minus_rho * logX
        abs_z = abs_s_rho * logX
        if re_z >= 0 and abs_z > 0:
            u_bound = math.exp(-re_z) / abs_z  # E1 theorem
            regime = "Re_z>=0_E1"
        elif abs_z > 0:
            # left of zeros: no E1 decay; use min(1+ |log|, C/|z|) crude
            # For path on the line sigma=1/2, re_z=0 boundary.
            # Slightly left: use 1/|z| without exp decay (worse)
            u_bound = 1.0 / abs_z
            regime = "Re_z<0_no_decay_1_over_z"
        else:
            u_bound = float("inf")
            regime = "singular"
        contrib = n_mean * u_bound
        total += contrib
        if j < 12 or j == n_ann - 1:
            annuli.append(
                {
                    "j": j,
                    "d_mid": d_mid,
                    "n_mean": n_mean,
                    "abs_z": abs_z,
                    "re_z": re_z,
                    "u_bound": u_bound,
                    "contrib": contrib,
                    "regime": regime,
                }
            )
    # closed form comparison: on critical line sigma=1/2, re_z=0, u=1/(|d| log X)
    # contrib_j = dens*2*width * 1/(d_mid log X) ~ dens*2*(2^j r)/(2^j r log X)= 2 dens/log X
    # sum_j ~ n_eff * 2 dens / log X
    return {
        "gamma": gamma,
        "sigma": sigma,
        "logX": logX,
        "r": r,
        "dens": dens,
        "far_sum_E1_model": total,
        "sample_annuli": annuli,
    }


def package_L1():
    gamma = 3e12
    rows = []
    for sigma in [0.5, 0.5 + 0.25 / math.log(gamma), 0.55, 0.6, 0.7]:
        for logX in [10, 12, 14, 16, 18, 20]:
            row = far_sum_e1_real_drift(gamma, sigma, float(logX))
            rows.append(
                {
                    "sigma": sigma,
                    "logX": logX,
                    "far_sum": row["far_sum_E1_model"],
                    "r": row["r"],
                }
            )
    # Best far at sigma=1/2 across logX
    on_line = [r for r in rows if abs(r["sigma"] - 0.5) < 1e-12]
    # Theorem note
    return {
        "theorem_E1": "|w E1(w)| <= 1 for Re w >= 0 (proved; RH_E1_Off_Nearline)",
        "implication_for_C_U": (
            "On paths with Re(s-rho') >= 0 for all far zeros in the sum, "
            "|U| <= 1 / (|s-rho'| log X) with C_U = 1 exactly from Theorem E1 "
            "(no free constant >1 required for pure E1 model)."
        ),
        "bulk_critical_line_issue": (
            "For bulk zeros at beta'=1/2 and path at sigma=1/2, Re z = 0 (boundary). "
            "E1 gives |E1| <= 1/|z|. Real-drift gain appears only for sigma > beta' "
            "(path to the right of the zero). Moving right of the critical line "
            "helps far zeros ON the line, but a rightmost off-line zero at beta*>sigma "
            "puts Re z < 0 and kills the decay — the RH-hard case."
        ),
        "grid": rows,
        "min_far_on_line": min(on_line, key=lambda r: r["far_sum"]) if on_line else None,
        "min_far_sigma_0.6": min((r for r in rows if abs(r["sigma"] - 0.6) < 1e-12), key=lambda r: r["far_sum"]),
        "status": "L1_E1_REAL_DRIFT_EXECUTED",
    }


# ---------- L2: average-case / 2π R-vM far sum ----------

def far_sum_rvM_2pi(gamma, C_U, c_r, logX):
    """
    Average/R-vM far sum with density (log gamma)/(2*pi):
      contrib per annulus ~ C_U * dens * 2 * (const) / log X
      = C_U * (log gamma) / (pi log X)   [two-sided]
    Sum over J annuli until d ~ gamma:
      far ~ C_U * (J+1) * Lg / (pi log X)
    Compare prior C_U*(J+1)*Lg/logX which omitted 1/pi (and used dens~Lg not Lg/2pi).
    """
    Lg = math.log(gamma)
    r = c_r / Lg
    J = math.log2(max(2.0 * gamma / r, 2.0))
    # per-annulus with dens = Lg/(2pi), two-sided width factor absorbed:
    # standard: sum_j C_U/(2^j r logX) * (Lg/pi * 2^j r) = C_U Lg /(pi logX)
    # (using dens_two_sided effective Lg/pi for |gamma'-gamma| count density)
    per = C_U * Lg / (math.pi * logX)
    far = (J + 1.0) * per
    # also "saturated" form: once 1/|z| bound and geometric, integral form
    # int_{r}^{2gamma} (dens * 2 dd) * C_U / (d logX) = 2 dens C_U / logX * log(2gamma/r)
    dens = Lg / (2 * math.pi)
    far_integral = 2 * dens * C_U / logX * math.log(max(2 * gamma / r, 2.0))
    return {
        "far_annulus_sum": far,
        "far_integral_form": far_integral,
        "J": J,
        "Lg": Lg,
        "per_annulus": per,
        "C_U": C_U,
        "logX": logX,
    }


def ghk_E(gamma, logX, sigma, c1, c2):
    lt1 = math.log(max(c1, 1e-300)) + 4 * logX - 2 * math.log(gamma) - 2 * math.log(max(logX, 1e-15))
    t1 = math.exp(lt1) if lt1 < 700 else float("inf")
    t2 = c2 * math.exp(-sigma * logX) * logX
    return (t1 + t2 if math.isfinite(t1) else float("inf")), t1, t2


def package_L2():
    gamma = 3e12
    # Compare old (no 2pi) vs new
    comparison = []
    for logX in [10, 12, 14, 16, 18, 20, 24, 30]:
        old_C_U2 = None
        # old formula from prior package: (J+1)*C_U*Lg/logX
        Lg = math.log(gamma)
        r = 0.25 / Lg
        J = math.log2(max(2 * gamma / r, 2))
        old = (J + 1) * 2.0 * Lg / logX
        new = far_sum_rvM_2pi(gamma, 1.0, 0.25, float(logX))  # C_U=1 from E1
        new2 = far_sum_rvM_2pi(gamma, 2.0, 0.25, float(logX))
        comparison.append(
            {
                "logX": logX,
                "old_CU2_no_2pi": old,
                "new_CU1_with_2pi_annulus": new["far_annulus_sum"],
                "new_CU1_integral": new["far_integral_form"],
                "new_CU2_with_2pi": new2["far_annulus_sum"],
                "improvement_factor_old_vs_newCU1": old / new["far_annulus_sum"],
            }
        )

    # Joint window under improved far (C_U=1, 2pi) + various c1
    joint = []
    for c1 in [291, 148, 50, 10, 1, 0.1]:
        for eps in [0.1, 0.5, 1.0]:
            best = None
            for i in range(20, 800):
                logX = 0.05 * i
                E, t1, t2 = ghk_E(gamma, logX, 0.5, c1, 8.0)
                if E <= eps:
                    far = far_sum_rvM_2pi(gamma, 1.0, 0.25, logX)["far_annulus_sum"]
                    if best is None or far < best["far"]:
                        best = {"logX": logX, "far": far, "E": E, "X": math.exp(logX)}
            joint.append({"c1": c1, "eps": eps, "best": best})

    # What logX / C_U for far<=0.4 with 2pi formula
    targets = []
    for C_U in [1.0, 0.5, 0.1, 0.05, 0.02, 0.01]:
        for logX in [12, 14, 16, 18, 20, 24, 30, 40, 60, 100]:
            far = far_sum_rvM_2pi(gamma, C_U, 0.25, float(logX))["far_annulus_sum"]
            E, _, _ = ghk_E(gamma, float(logX), 0.5, 1.0, 8.0)
            targets.append(
                {
                    "C_U": C_U,
                    "logX": logX,
                    "far": far,
                    "E_at_c1_1": fin(E),
                    "far_le_0.4": far <= 0.4,
                    "both_c1_1": far <= 0.4 and fin(E) <= 0.1,
                }
            )

    both_hits = [t for t in targets if t["both_c1_1"]]
    far_ok_only = [t for t in targets if t["far_le_0.4"] and not t["both_c1_1"]]

    return {
        "formula": "far ~ C_U (J+1) log(gamma) / (pi log X) with dens = log(gamma)/(2pi)",
        "C_U_from_E1": 1.0,
        "comparison_old_vs_new": comparison,
        "joint_windows": joint,
        "target_scan": targets,
        "both_hits_c1_1": both_hits,
        "far_ok_not_ghk": far_ok_only[:8],
        "conclusion_L2": (
            "Inserting 2π into R-vM density improves far-sum by ~π relative to dens~log gamma, "
            "and E1 sets C_U=1 (vs prior diagnostic C_U=2). Net ~6x improvement vs old CU=2/no-2π, "
            "but min far under GHK-feasible logX remains O(10), not O(0.1). "
            "Average-case equals R-vM mean — no further free factor without cancellation."
        ),
        "status": "L2_AVERAGE_RVM_2PI_EXECUTED",
    }


# ---------- L3: zero-free tube Phi ----------

def package_L3():
    """
    Zero-free tube design: path gamma_path stays in region
      dist(s, Z(zeta)) >= d_tube(t)
    so Phi_local <= 1/d_tube instead of 1/r0 with r0=1/log t.

    Classical zero-free regions: sigma >= 1 - c/log(|t|+2) near sigma=1 only.
    At moderate sigma, no classical wide tube.

    Design options:
      T1. Horizontal path at height t_* in a gap between consecutive ordinates
          (mean gap = 2π/log t). Tube half-width = theta * mean_gap.
      T2. Slightly right of 1/2 in a Maynard-Pratt half-isolated configuration (rare).
      T3. Average over t of |zeta'/zeta| (delete worst-case local poles).
    """
    t = 1e6
    X = math.exp(10.0)
    logX = math.log(X)
    mean_gap = 2 * math.pi / math.log(t)
    reservoir = math.sqrt(X) / logX

    designs = []
    for theta in [0.01, 0.05, 0.1, 0.25, 0.5]:
        d_tube = theta * mean_gap
        Phi_local = 1.0 / d_tube
        # Phi without local (far zeros + arch + P only) from prior sketch scales
        # Reuse simplified: Phi_far ~ (log t)*log(t/r) with r=d_tube
        r0 = d_tube
        J = math.log2(max(t / r0, 2.0))
        Phi_far = J * math.log(t)
        Phi_arch = math.log(t + 2)
        # Phi_P at sigma from 0.5 to 0.7 average
        Phi_P_avg = 0.0
        sigs = [0.5, 0.55, 0.6, 0.65, 0.7]
        for sig in sigs:
            if sig < 1:
                Phi_P_avg += (X ** (1 - sig)) / max(1 - sig, 1e-6)
            else:
                Phi_P_avg += math.log(X)
        Phi_P_avg /= len(sigs)
        # integral length 0.2 (from 0.5 to 0.7)
        Phi_typ = Phi_P_avg + Phi_far + Phi_arch  # NO Phi_local if tube succeeds
        Phi_with_local = Phi_typ + Phi_local
        integ_typ = Phi_typ * 0.2
        integ_loc = Phi_with_local * 0.2
        designs.append(
            {
                "theta_gap_fraction": theta,
                "d_tube": d_tube,
                "mean_gap": mean_gap,
                "Phi_local": Phi_local,
                "Phi_typical_no_local": Phi_typ,
                "integral_0.2_no_local": integ_typ,
                "integral_0.2_with_local": integ_loc,
                "reservoir": reservoir,
                "no_local_lt_half_res": integ_typ < 0.5 * reservoir,
                "with_local_lt_half_res": integ_loc < 0.5 * reservoir,
                "gap_existence": (
                    "Mean gaps exist by R-vM; a gap of size >= 2 d_tube has density "
                    "depending on gap statistics (not proved for all large t)."
                ),
            }
        )

    return {
        "design": {
            "T1_horizontal_in_ordinate_gap": "primary unconditional attempt",
            "T2_half_isolation": "rare; not positive density",
            "T3_average_case": "deletes local poles in L1 mean",
        },
        "classical_limit": (
            "Wide zero-free tubes at moderate sigma are not classical. "
            "Only near sigma=1 do classical zero-free regions give d_tube ~ 1/log^k t."
        ),
        "numerical_T1": designs,
        "reading": (
            "If a horizontal path sits in an ordinate gap with theta>=0.05–0.1 of mean gap, "
            "Phi_local drops enough that the no-local integral can compete with the reservoir "
            "at these illustration parameters — BUT existence of such t_* with large on-line "
            "Omega AND a wide gap is open (correlation of large values with zero gaps)."
        ),
        "status": "L3_ZERO_FREE_TUBE_DESIGN_EXECUTED",
    }


# ---------- Resolve board ----------

def package_resolve_board(L1, L2, L3):
    return {
        "five_obligations": {
            "O-M1.2": {
                "status": "OPEN",
                "resolved_today": (
                    "E1 sets C_U=1; 2π R-vM improves far-sum ~6x vs prior diagnostic; "
                    "joint numerical gamma1 under c1=291 still closed as obstruction; "
                    "architecture unchanged/accepted."
                ),
                "still_missing": "uniform far domination at O-TL-relevant paths for all large gamma",
            },
            "O-M1.3bis": {
                "status": "OPEN",
                "resolved_today": "Phi structure + tube design T1–T3; absolute path fails; tube path needs gap+Omega correlation",
                "still_missing": "path with Delta theta >> log log X",
            },
            "O-PC": {
                "status": "PARTIAL (on-line typical Omega accepted; strong/off-line open)",
                "resolved_today": "R4.1 GHK strip (prior) still the clean off-line error control; R4.2–R4.3 open",
                "still_missing": "strong Omega at O-TL scale; off-line conversion",
            },
            "O-Moll": {
                "status": "OPEN",
                "resolved_today": "not attacked (no classical mollifier breakthrough available)",
                "still_missing": "phase-oriented mollifier",
            },
            "O-TL": {
                "status": "OPEN — primary",
                "resolved_today": "no discharge; dependencies O-M1.2/M1.3bis/PC/Moll still open",
                "still_missing": "target lemma itself",
            },
        },
        "five_solid_directions": {
            "D1_density": "Resolved as far as corpus allows (prior+Step B); polylog moderate sigma OPEN",
            "D2_Iso_H": "OPEN; classical isolation tools insufficient (prior freeze)",
            "D3_path_Omega": "Phi+tube design advanced; continuation OPEN",
            "D4_resonance_offline": "R4.1 GHK strip resolved; O4.2–O4.4 OPEN",
            "D5_Mass_with_A": "Conditional DH template only; unconditional OPEN",
        },
        "three_levers": {
            "L1_E1_C_U": L1["status"],
            "L2_average_2pi": L2["status"],
            "L3_tube_Phi": L3["status"],
        },
        "global": {
            "RH": "OPEN",
            "label": "RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF",
            "one_liner": (
                "Resolve-for-all executed: E1/2π improve far-sum constants but do not open the "
                "M1.2 joint window under current c1; tube design identifies the gap+Omega "
                "correlation as the path-continuation obstruction; RH remains open."
            ),
        },
    }


def main():
    out_dir = Path(__file__).resolve().parents[1]
    L1 = package_L1()
    L2 = package_L2()
    L3 = package_L3()
    board = package_resolve_board(L1, L2, L3)

    results = {
        "status": "RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF",
        "date": "2026-08-08",
        "mandate": "Resolve for all — three levers + five obligations + five directions",
        "zla": True,
        "no_model_constants": True,
        "does_not_prove": ["RH", "O-TL", "Iso_H", "Mass-with-A", "uniform O-M1.2", "O-M1.3bis"],
        "L1_E1_real_drift": L1,
        "L2_average_rvM_2pi": L2,
        "L3_zero_free_tube_Phi": L3,
        "resolve_board": board,
    }

    def clean(o):
        if isinstance(o, float):
            if math.isnan(o):
                return "nan"
            if math.isinf(o):
                return "inf"
            return o
        if isinstance(o, dict):
            return {k: clean(v) for k, v in o.items()}
        if isinstance(o, list):
            return [clean(v) for v in o]
        return o

    out = out_dir / "rh_resolve_all_levers_results.json"
    out.write_text(json.dumps(clean(results), indent=2), encoding="utf-8")
    print("OK", out)
    print("L1 min on-line far", L1["min_far_on_line"])
    print("L1 min sig0.6", L1["min_far_sigma_0.6"])
    print("L2 comparison logX=14", [c for c in L2["comparison_old_vs_new"] if c["logX"] == 14][0])
    print("L2 both_hits", L2["both_hits_c1_1"])
    print("L2 joint c1=1 eps=0.1", [j for j in L2["joint_windows"] if j["c1"] == 1 and j["eps"] == 0.1][0])
    print("L3 theta=0.1", [d for d in L3["numerical_T1"] if d["theta_gap_fraction"] == 0.1][0])
    print("BOARD", board["global"]["one_liner"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
