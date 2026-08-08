#!/usr/bin/env python3
"""
Rational-4 tracks (2026-08-08 Pass3 priorities):
  T1 Form C at fixed rho*
  T2 kappa any p>1 on GHK/U
  T3 DH or Iso_H (alternate B_theta gates)
  T4 GO / SOC / AFE-Moll (O-TL arms)

AVOID: absolute far cosmetics, RW-only kappa, Soundararajan-as-Form-C,
       Levinson-as-O-Moll, residual=>RH.

RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF · ZLA · no model constants.
Does not prove Form C, kappa p>1, DH, Iso_H, GO, SOC, O-Moll, B_theta, O-TL, RH.
"""
from __future__ import annotations

import json
import math
from pathlib import Path


# ---------- T1 Form C ----------
def package_T1():
    """
    Form C: limsup |sum_{n<=X} Lambda(n)/(n^{rho*} log n)| = infinity
    at fixed rho* = beta* + i gamma*, beta* > 1/2.

    Explore classical large-value mechanisms that ARE allowed
    (not free-t Soundararajan misapplied as Form C proof).
    """
    # Analytic structure of Form C sum
    # S(X) = sum_{n<=X} Lambda(n) n^{-beta*} e^{-i gamma* log n} / log n
    # = sum_p sum_{k: p^k <=X} p^{-k beta*} e^{-i k gamma* log p} / k
    # Leading: sum_p p^{-beta*} e^{-i gamma* log p}  (k=1)

    # Partial summation / integral form already = residual Form B

    # What classical tools can touch Form C?
    tools = [
        {
            "tool": "Dirichlet series absolute convergence",
            "regime": "beta* > 1",
            "gives": "S(X) converges as X->inf; limsup finite",
            "helps_Form_C": False,
            "note": "off-line zeros have beta*<1, so absolute conv fails — the interesting regime",
        },
        {
            "tool": "Partial summation + psi-x Omega amplitude",
            "regime": "beta* maximal",
            "gives": "amplitude connection via Stieltjes; phases still free",
            "helps_Form_C": "partial",
            "note": "reopens epsilon_other / Iso_H-adjacent issues from P1",
        },
        {
            "tool": "Halasz / pretentious large values",
            "regime": "typically |sum_{n<=X} f(n)| for multiplicative f on unit circle or real",
            "gives": "large values when f pretends to be n^{it}",
            "helps_Form_C": False,
            "note": (
                "Form C has f(n) = Lambda(n) n^{-beta*}/log n * e^{-i gamma* log n}; "
                "the frequency is FIXED to gamma* of a zero — cannot choose pretentious t freely "
                "independent of the zero. Different problem."
            ),
        },
        {
            "tool": "Mean-square of S(X) along a family of gamma",
            "regime": "average over gamma",
            "gives": "possibly large mean square",
            "helps_Form_C": False,
            "note": "Form C needs ONE fixed gamma* (the zero's ordinate), not average over gamma",
        },
        {
            "tool": "Conditional: assume Omega of psi-x phase-aligned (old PAO)",
            "regime": "conditional",
            "gives": "Form C via Thm 4.1 equivalence",
            "helps_Form_C": "conditional",
            "note": "circular with original PAO; P1 showed star phase constant",
        },
        {
            "tool": "Vinogradov-Korobov zero-free => upper bounds on S(X)",
            "regime": "classical ZF",
            "gives": "upper envelope |S| << X^{1-beta*} e^{-c sqrt{log X}}/log X type",
            "helps_Form_C": False,
            "note": "upper bound only; limsup infinity not ruled out or proved by ZF upper bounds",
        },
    ]

    # Structural obstruction formalization
    obstruction = {
        "name": "Fixed-Frequency Multiplicative Large-Value Barrier (FFML)",
        "statement": (
            "Large-value theorems for Dirichlet polynomials typically optimize over the "
            "frequency t or use mean values in t. Form C freezes t = gamma* to the ordinate "
            "of a rightmost zero and requires limsup_X |S_X(rho*)| = infinity. "
            "No classical theorem supplies this off the critical line without assuming "
            "input of RH-comparable strength."
        ),
        "allowed_conditional": {
            "name": "FC(c)",
            "statement": "Along a sequence X_m, |sum_{n<=X_m} Lambda(n)/(n^{rho*} log n)| >= c > 0 (or -> infinity)",
            "status": "HYPOTHESIS — is Form C itself",
        },
    }

    # Numeric illustration: at beta=0.6, what |sum| upper from ZF looks like vs loglog
    rows = []
    for beta in [0.55, 0.7, 0.9]:
        for logX in [10, 20, 40]:
            X = math.exp(logX)
            c0 = 0.1
            upper = (X ** (1 - beta) / max(logX, 1)) * math.exp(-c0 * math.sqrt(logX))
            rows.append(
                {
                    "beta": beta,
                    "logX": logX,
                    "ZF_upper_schematic": upper if math.isfinite(upper) else "inf",
                    "loglog": math.log(logX) if logX > math.e else 1.0,
                    "upper_grows": upper > 1,
                }
            )

    return {
        "status": "T1_FORM_C_EXECUTED",
        "definition": "limsup |sum_{n<=X} Lambda(n)/(n^{rho*} log n)| = infinity",
        "equivalent_to": "Form B residual / B_theta off-line (signed-sum Thm 4.1)",
        "forbidden_attacks": [
            "Soundararajan free-t resonator claimed as Form C proof",
            "star-phased psi-x as the engine (P1)",
        ],
        "tools_survey": tools,
        "obstruction": obstruction,
        "zf_upper_vs_growth": rows[:6],
        "proved": [
            "Form B <-> Form C",
            "self loglog cancel",
            "ZF upper bounds (not lower)",
        ],
        "open": "Form C itself",
        "resolution_today": False,
        "conclusion": (
            "Form C remains the sharpest B_theta object. Fixed-frequency multiplicative "
            "large-value barrier (FFML) blocks classical free-t / pretentious transfer. "
            "No Form C theorem today."
        ),
    }


# ---------- T2 kappa p>1 ----------
def package_T2():
    """
    Pursuit of ANY rigorous kappa <= J^{-p} with p>1 on GHK/U far sums.
    Avoid: RW-only as 'theorem', absolute cosmetics.
    """
    gamma = 3e12
    Lg = math.log(gamma)
    C_U = 1.0

    # What CAN be proved without phase cancellation?
    # 1. Absolute: kappa=1, p=0
    # 2. Dyadic regrouping does not improve triangle inequality
    # 3. Optional: truncate annuli J_eff < J if path only sees local height window H
    #    If path length in t is L, zeros with |gamma'-t| >> L+1/logX contribute
    #    with more structure — but far sum definition already uses full height.

    # Path-local far sum: only zeros with |gamma' - t| <= H_path
    # J_local ~ log2(H_path / r) instead of log2(gamma/r)
    local_rows = []
    for H_path in [10, 100, 1e4, 1e6, 1e8]:
        for c_r in [0.25, 1.0]:
            for logX in [14.0, 16.0]:
                r = c_r / Lg
                J_loc = math.log2(max(H_path / r, 2.0))
                # density local
                dens = Lg / (2 * math.pi)
                # far local L1 ~ C_U (J_loc+1) * (log factor)
                # use same per-annulus: C_U * dens_eff * ...
                far_loc = C_U * (J_loc + 1) * Lg / (math.pi * logX)
                # but dens should use local — actually per annulus same order
                # If we only integrate height H_path, number of annuli decreases
                kn = 0.4 / far_loc if far_loc > 0 else 0
                p_need = math.log(1 / kn) / math.log(J_loc) if kn > 0 and J_loc > 1 else float("inf")
                local_rows.append(
                    {
                        "H_path": H_path,
                        "c_r": c_r,
                        "logX": logX,
                        "J_local": J_loc,
                        "far_L1_local_proxy": far_loc,
                        "kappa_need": kn,
                        "p_need": p_need,
                        "p_need_lt_1": p_need < 1 if math.isfinite(p_need) else False,
                    }
                )

    # Even with H_path=100, J still large if r small
    # Check if any cell has p_need <= 0 (i.e. absolute enough) — no
    abs_enough = [r for r in local_rows if r["far_L1_local_proxy"] <= 0.4]

    return {
        "status": "T2_KAPPA_P_GT_1_EXECUTED",
        "proved": {"kappa_abs": 1.0, "p_proved": 0.0},
        "avoided": ["claiming RW kappa as theorem", "c1 cosmetics as kappa substitute"],
        "path_local_scan": local_rows,
        "absolute_enough_local": abs_enough,
        "reading_local": (
            "Restricting to path-local height H reduces J but far_L1 still >> 0.4 "
            "for realistic H; absolute still fails. Does not produce p>1 theorem."
        ),
        "conditional": {
            "name": "Kappa(p0)",
            "statement": "far_signed <= J^{-p0} far_abs on M1.3 paths for some p0>1",
            "status": "HYPOTHESIS — open for all p0>0 beyond absolute",
        },
        "unconditional_p_gt_1": False,
        "resolution_today": False,
        "conclusion": (
            "No kappa bound with p>1 obtained. Path-local truncation does not rescue absolute majorants. "
            "Unconditional p_proved = 0 remains."
        ),
    }


# ---------- T3 DH or Iso_H ----------
def package_T3():
    """
    Alternate B_theta gates: restate ceilings; no new tech invented.
    """
    # Density exponents schematic
    dens = []
    for sig in [0.55, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99]:
        th = 3 * (1 - sig) / (2 - sig)  # Ingham shape
        dens.append({"sigma": sig, "T_exponent_Ingham_shape": th, "polylog": th <= 0})

    return {
        "status": "T3_DH_OR_ISOH_EXECUTED",
        "DH": {
            "definition": "N(beta*, T) = O((log T)^C) for some C, beta* in (1/2,1)",
            "classical_ceiling": dens,
            "near_1": "log-power bounds in thin edge only (KLN/Bellotti-type)",
            "moderate_sigma_polylog": False,
            "implication": "(RM)+DH => polylog A => Mass-with-A => B_theta (proved chain)",
            "resolution_today": False,
        },
        "Iso_H": {
            "definition": "only {rho*, bar rho*} on Re=beta* (up to EF truncation)",
            "tools_fail": [
                "point isolation (finite height only)",
                "FE (conjugate only)",
                "Ivic multiplicity (m not ordinate count)",
                "zero density (bulk not line)",
                "Maynard-Pratt half-isolation (local/rare)",
                "Hypothesis F (conditional, not Iso_H)",
            ],
            "implication": "(RM)+Iso_H => B_theta (proved)",
            "new_technology": False,
            "resolution_today": False,
        },
        "coupling_to_Form_C": {
            "epsilon_other": "Iso_H controls same-abscissa contamination for amplitude Omega path",
            "Form_C_prime_side": "does not require Iso_H formally (signed residual already reduced), but hard analytically",
            "density_not_isolation": "DEAD EDGE — confirmed",
        },
        "resolution_today": False,
        "conclusion": (
            "Neither DH at moderate sigma nor Iso_H is available. Alternate B_theta gates remain open. "
            "Proved implications intact. Density does not imply Iso_H."
        ),
    }


# ---------- T4 GO / SOC / AFE-Moll ----------
def package_T4():
    return {
        "status": "T4_OTL_ARMS_EXECUTED",
        "GO": {
            "definition": "infinitely many t_n with hybrid Omega scale AND gap >= theta * mean_gap",
            "classical": "mean gaps yes; hybrid Omega on-line fixed X programme-accepted; JOINT no",
            "resolution_today": False,
        },
        "SOC": {
            "on_line_typical": "PROVED (sqrt log log)",
            "on_line_strong_model": "ACCEPTED for fixed X (Im D_X)",
            "strong_loglog_OPC_Core": "OPEN",
            "off_line_transfer": "OPEN (needs path + M1.2; FE bookkeeping only hygiene)",
            "resolution_today": False,
        },
        "AFE_Moll": {
            "surface": "AFE dual sums F + chi G + R",
            "forbidden": "Levinson/Conrey zero-count mollifiers",
            "construction": "not found",
            "objective": "amplify Im log P_X / A_X at O-TL locations",
            "resolution_today": False,
        },
        "joint_for_O_TL": {
            "need_all": ["kappa (T2)", "GO", "SOC strong+transfer", "AFE-Moll"],
            "all_open": True,
        },
        "resolution_today": False,
        "conclusion": (
            "All three O-TL arms (GO, SOC, AFE-Moll) remain open; with kappa (T2) the AND-cut is fully open. "
            "No arm closed today."
        ),
    }


def main():
    out = Path(__file__).resolve().parents[1]
    T1, T2, T3, T4 = package_T1(), package_T2(), package_T3(), package_T4()
    results = {
        "status": "RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF",
        "date": "2026-08-08",
        "mandate": "Rational-4 tracks from Pass3 explore",
        "avoid": [
            "absolute far cosmetics",
            "RW-only kappa as theorem",
            "Soundararajan-as-Form-C",
            "Levinson-as-O-Moll",
            "residual=>RH",
        ],
        "T1_Form_C": T1,
        "T2_kappa": T2,
        "T3_DH_IsoH": T3,
        "T4_OTL_arms": T4,
        "scoreboard": {
            "T1_Form_C": False,
            "T2_kappa_p_gt_1": False,
            "T3_DH": False,
            "T3_Iso_H": False,
            "T4_GO": False,
            "T4_SOC": False,
            "T4_AFE_Moll": False,
            "B_theta": False,
            "O_TL": False,
            "RH": False,
            "unconditional_resolution_count": 0,
        },
        "global_conclusion": (
            "Rational-4 executed under avoid-list discipline. Form C blocked by fixed-frequency "
            "multiplicative large-value barrier; kappa p>1 not obtained; DH/Iso_H ceilings unchanged; "
            "GO/SOC/AFE-Moll all open. Unconditional resolution count still zero."
        ),
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

    path = out / "rh_rational4_tracks_results.json"
    path.write_text(json.dumps(clean(results), indent=2), encoding="utf-8")
    print("OK", path)
    print("T1", T1["resolution_today"], T1["obstruction"]["name"])
    print("T2 p>1", T2["unconditional_p_gt_1"], "abs_enough_local", len(T2["absolute_enough_local"]))
    print("T3", T3["resolution_today"])
    print("T4", T4["resolution_today"], "all_open", T4["joint_for_O_TL"]["all_open"])
    print(results["global_conclusion"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
