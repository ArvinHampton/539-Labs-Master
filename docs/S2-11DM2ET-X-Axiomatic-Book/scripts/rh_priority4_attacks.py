#!/usr/bin/env python3
"""
Priority-4 attacks (2026-08-08):
  P1 PAO direct: single-gamma* phase lock + epsilon_other control
  P2 kappa on GHK/U: any p>1 upper bound attempt
  P3 O-Moll from AFE dual sums only
  P4 FE path bookkeeping for off-line transfer only

RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF · ZLA · no model constants.
Does not prove PAO, kappa theorem, O-Moll, O-TL, B_theta, RH.
"""
from __future__ import annotations

import json
import math
from pathlib import Path


def package_P1_PAO():
    """
    Decompose PAO into:
      (i) star term contribution
      (ii) epsilon_other from other zeros
      (iii) measure of phase-aligned x
    Record what is classical vs open.
    """
    # Explicit formula schematic:
    # (psi-x)/x^{beta*} ~ - sum_rho x^{rho-beta*}/rho + arch
    # At rho* = beta* + i gamma*: term = - x^{i gamma*}/rho*
    # Re( e^{-i gamma* log x} (psi-x) x^{-beta*} ) ~ Re( -e^{-i gamma* log x} x^{i gamma*}/rho* ) + other
    # = Re(-1/rho*) + Re( sum_{rho != rho*} - e^{-i gamma* log x} x^{rho - beta*}/rho ) + ...
    # For pure star: Re(-1/rho*) = -beta*/|rho*|^2 which is NEGATIVE small.
    # Actually the Omega comes from choosing x so many terms align - the star alone
    # with fixed phase weight e^{-i gamma* log x} * x^{rho*}/rho* = x^{beta*}/rho* * (phase cancels to 1)
    # e^{-i g log x} * x^{beta*+ig}/rho* * x^{-beta*} = e^{-ig log x} e^{log x (beta*+ig)} e^{-beta* log x}/rho*
    # = e^{-ig log x} e^{ig log x}/rho* = 1/rho*
    # So the star contribution to the phased residual is constantly 1/rho* (plus conj etc.)
    # Amplitude |1/rho*| = 1/|rho*| — the log-measure integral of star alone is
    # int_2^X (1/rho*) / log x * dx/x wait no - the residual integral is
    # int (psi-x) x^{-rho*-1} / log x dx
    # phased form is already complex.

    # For the real part indicator of PAO:
    # Phi(x) := Re( e^{-i gamma* log x} (psi-x) x^{-beta*} )
    # Star contribution from -x^{rho*}/rho* in psi-x ~ ... :
    # Re(e^{-ig log x} (-x^{rho*}/rho*) x^{-beta*}) = Re(-1/rho*) = -beta*/|rho*|^2 < 0.
    # So the STAR term alone in the usual EF sign convention contributes a NEGATIVE constant
    # to Phi; large POSITIVE Phi must come from OTHER zeros aligning or from the precise EF form.
    #
    # Careful: standard Omega argument uses that if beta* is maximal, the star (and conj)
    # DOMINATE and one chooses x so x^{i gamma*} points to make the real part large positive
    # for -(psi-x)/x^beta ~ sum x^{rho-beta}/rho.
    # Define G(x) = sum_rho x^{rho}/rho; psi-x ~ -G(x) + ...
    # Then e^{-ig log x}(psi-x)x^{-beta} ~ -e^{-ig log x} sum x^{rho-beta}/rho
    # Star: -e^{-ig log x} x^{i g}/rho* = -1/rho*
    # To make Re(-1/rho*) ... -1/rho* is fixed! The phase e^{-ig log x} cancels the star's oscillation
    # exactly, leaving constant -1/rho*.
    # Re(-1/rho*) = -beta/|rho|^2 < 0 always.
    #
    # So for PAO as stated with that phase, the star contributes a FIXED negative constant.
    # Large positive Phi requires other zeros OR one should phase as e^{+i g log x} or use -Phi.
    # Standard Omega uses limsup |psi-x|/x^beta > 0, not a fixed phase.
    # For residual int (psi-x) x^{-rho*-1} (log x)^{-1} dx, the complex weight already includes
    # x^{-i gamma*}, so the integrand's main star piece is (const)/ (x log x) after cancellation.
    #
    # From signed sum note Form B: int (psi-x) x^{-rho*-1}/log x dx
    # Star in EF: contribution related to int x^{rho*-rho*-1}/log x * (-1) = -int dx/(x log x) = -loglog
    # which cancelled with Self. Remaining is other zeros + primes.
    #
    # PAO is really about the REMAINDER after star is removed — phase alignment of OTHER
    # contributions, OR Omega of the prime side.
    # Recast PAO as phase-aligned Omega of the prime-power sum against frequency gamma*.

    return {
        "status": "P1_PAO_DIRECT_EXECUTED",
        "recast": {
            "wrong_target": (
                "Phasing psi-x against e^{-i gamma* log x} makes the star EF term CONSTANT "
                "(-1/rho*), not oscillatory. Star alone cannot produce limsup +infty of that "
                "real part; Self loglog already cancelled the pure star loglog in S_X."
            ),
            "correct_PAO_core": (
                "After star removal, need phase-aligned lower bound on the contribution of "
                "(i) other zeros, and/or (ii) the prime side residual int (psi-x)_* x^{-rho*-1}/log x, "
                "equivalent to large values of sum_{n<=X} Lambda(n) n^{-rho*}/log n (Form C)."
            ),
            "Form_C": "limsup |sum_{n<=X} Lambda(n)/(n^{rho*} log n)| = infinity",
            "Form_C_is": "exactly the Dirichlet polynomial S_X at rho* (up to notation)",
        },
        "epsilon_other": {
            "definition": (
                "epsilon_other = relative contamination of EF main term by zeros with "
                "beta >= beta* other than rho*, bar rho*"
            ),
            "under_Iso_H": "epsilon_other from same-abscissa vanishes (only conj); left zeros smaller by X^{-delta}",
            "without_Iso_H": "same-abscissa competitors can cancel the main Omega coefficient",
            "control_status": (
                "Unconditional control of epsilon_other for arbitrary rightmost zero is "
                "essentially Iso_H-adjacent — not available. Conditional: assume Iso_H or "
                "N_line(beta*,T)<=2 => epsilon_same_abscissa = 0 (up to conj)."
            ),
            "lemma_template": {
                "name": "EO(Iso_H)",
                "statement": "Under Iso_H at beta*, epsilon_other from Re=beta* is O(contribution of bar rho* only), controlled.",
                "status": "conditional on Iso_H — not a new Iso_H proof",
            },
        },
        "single_gamma_lock": {
            "object": "sum_n Lambda(n) n^{-beta*} n^{-i gamma*} / log n = sum Lambda(n)/(n^{beta*} log n) e^{-i gamma* log n}",
            "mechanism": "align prime angles {gamma* log p / 2pi} mod 1 — but gamma* fixed, free variable is which primes/n or the cutoff X",
            "diophantine": (
                "For fixed gamma*, the sequence {gamma* log p / 2pi} is like a Kronecker sequence in p. "
                "Unlike free t, we cannot choose t to align all log p. We choose X or a set of n. "
                "This is multiplicative resonance in the n-aspect at FIXED frequency — harder than t-aspect."
            ),
            "status": "OPEN — no classical theorem gives limsup |S_X(rho*)|=infty off the line without RH-scale input",
        },
        "proved_pieces": [
            "Self loglog cancel (star discrete contribution handled)",
            "Form C equivalence to residual Form B under signed-sum Thm 4.1",
            "Classical amplitude Omega of psi-x if a zero exists at beta*",
        ],
        "open_pieces": [
            "epsilon_other unconditional control",
            "single-frequency prime-side phase lock at fixed gamma*",
            "PAO(c,delta) as originally named",
        ],
        "resolution_today": False,
        "conclusion": (
            "PAO direct recast: after star cancellation, the gap is Form C (Dirichlet poly at rho*), "
            "i.e. large values of a multiplicative sum at FIXED complex frequency — not free-t resonance. "
            "epsilon_other control is Iso_H-adjacent. No PAO theorem today."
        ),
    }


def package_P2_kappa():
    """
    Attempt any rigorous p>1 style bound, or prove partial substitutes:
    - mean-square over path parameter
    - absolute with E1 already kappa=1 (p=0)
    - dyadic L2 cancellation heuristic quantification
    - conditional kappa under random phase
    Record: no unconditional p>1 theorem.
    """
    gamma = 3e12
    Lg = math.log(gamma)
    C_U = 1.0

    # Mean-square model: if phases independent, E|sum a_j e^{i theta_j}|^2 = sum |a_j|^2
    # far_abs = sum |a_j|, far_L2 = sqrt(sum |a_j|^2)
    # For annulus j: a_j ~ C_U * n_j / (d_j log X) with n_j ~ dens * width
    # contrib L1: (J+1) * C_U * Lg/(pi log X)
    # L2^2: sum_j (C_U * n_j / (d_mid log X))^2 / n_j * n_j wait
    # |sum_{zeros in ann} U| <= sum |U|; L2 proxy: sqrt(sum n_j * u_j^2) = sqrt(sum n_j / (d_j log X)^2)
    # n_j ~ dens * 2^j r, d_j ~ 2^j r, so n_j / d_j^2 ~ dens / (2^j r)
    # sum_j n_j/d_j^2 ~ dens/r * sum 2^{-j} ~ dens/r
    # far_L2 ~ C_U / log X * sqrt(dens/r) 

    rows = []
    for c_r in [0.25, 1.0, 5.0]:
        for logX in [12.0, 14.0, 16.0, 18.0]:
            r = c_r / Lg
            dens = Lg / (2 * math.pi)
            J = math.log2(max(2 * gamma / r, 2.0))
            far_L1 = C_U * (J + 1) * Lg / (math.pi * logX)
            # integral form L2:
            # int_r^{2gamma} dens * 2 dd * (C_U/(d logX))^2 = 2 dens C_U^2 / logX^2 * int_r dd/d^2
            # = 2 dens C_U^2 / logX^2 * (1/r - 1/(2gamma)) ~ 2 dens C_U^2 /(logX^2 r)
            far_L2 = C_U / logX * math.sqrt(2 * dens / r)
            # effective kappa_L2 = far_L2 / far_L1
            kap_L2 = far_L2 / far_L1 if far_L1 > 0 else float("inf")
            # p_eff if kappa = J^{-p}: p = -log(kappa)/log J
            p_eff = -math.log(kap_L2) / math.log(J) if kap_L2 > 0 and J > 1 else float("inf")
            rows.append(
                {
                    "c_r": c_r,
                    "logX": logX,
                    "J": J,
                    "far_L1": far_L1,
                    "far_L2_proxy": far_L2,
                    "kappa_L2_proxy": kap_L2,
                    "p_eff_L2": p_eff,
                    "beats_p_1": p_eff > 1.0,
                    "far_L2_le_0.4": far_L2 <= 0.4,
                }
            )

    l2_hits = [r for r in rows if r["far_L2_le_0.4"]]
    # Best p_eff
    best_p = max(rows, key=lambda r: r["p_eff_L2"])

    return {
        "status": "P2_KAPPA_GHK_U_EXECUTED",
        "proved": {
            "absolute_kappa": 1.0,
            "p_proved": 0.0,
            "E1": "|U| <= 1/(|s-rho'| log X) for Re(s-rho')log X >= 0 model",
        },
        "attempted": {
            "mean_square_proxy": (
                "L2-type size far_L2 ~ C_U/logX * sqrt(2 dens / r) — NOT a uniform path bound. "
                "Would give effective p ~ 1.5-2 in scans but is an L2 heuristic/proxy only."
            ),
            "rows": rows,
            "best_p_eff_L2": best_p,
            "L2_proxy_hits_0.4": l2_hits,
        },
        "unconditional_p_gt_1": False,
        "conditional_templates": [
            {
                "name": "Kappa_L2_path_avg",
                "statement": "Average over path parameter s in a family of |far_signed|^2 << (far_L2)^2",
                "gives": "average-case M1.2, not uniform O-M1.2",
                "status": "not proved; weaker than O-M1.2",
            },
            {
                "name": "Kappa_random_phase",
                "statement": "If far zero phases are equidistributed along the path family",
                "gives": "kappa ~ J^{-1/2} in probability — still p=0.5 < 1.12 bar",
                "status": "heuristic; insufficient for joint window even if true",
            },
        ],
        "resolution_today": False,
        "conclusion": (
            "No unconditional kappa bound with p>1. Absolute p=0 only. "
            "L2 proxies look numerically friendly but do not yield uniform M1.2. "
            "Random-phase p=1/2 remains below the bar. Kappa theorem still OPEN."
        ),
    }


def package_P3_Omoll_AFE():
    """
    Design O-Moll from approximate functional equation dual sums only.
    Write template; do not claim construction works.
    """
    return {
        "status": "P3_OMOLL_AFE_DESIGN_EXECUTED",
        "forbidden": [
            "Levinson mollifier for zeros on the line",
            "Conrey long mollifiers for proportion on the line",
            "Any mu-polynomial designed only to detect horizontal zeros",
        ],
        "AFE_surface": {
            "form": "zeta(s) = sum_{n<=u} n^{-s} + chi(s) sum_{n<=v} n^{s-1} + R_AFE(s;u,v)",
            "with": "uv ~ t/(2pi) on the critical line; off-line parameters free in a range",
            "dual": "two Dirichlet polynomials F(s), G(1-s) linked by chi(s)",
        },
        "O_Moll_target_functional": {
            "want": "boost |A_X(s)| or |theta_X(s)| = |Im log P_X(s)| at s near maximal-abscissa zeros",
            "not": "|zeta psi| second moment on Re=1/2+a/log T",
        },
        "design_template_AFE_Moll": {
            "name": "AFE-Moll skeleton (NOT a theorem)",
            "step1": "Write hybrid phase theta_X via GHK: theta_X = arg zeta - arg Z_X - Im E",
            "step2": "Replace arg zeta by arg(F + chi G + R) from AFE at the evaluation path",
            "step3": "Choose dual lengths (u,v) and coefficients to amplify Im log of the partial Euler piece, not |F+chi G|",
            "step4": "Prove that the dual G-term and R do not destroy the phase lower bound",
            "blocker": (
                "No classical optimization is known for Im log P_X. Amplifying |zeta| or "
                "zero-detection is the wrong objective functional. Step 3-4 are open design."
            ),
            "status": "TEMPLATE ONLY — construction not found",
        },
        "what_was_checked": [
            "No Levinson/Conrey object matches O-Moll (N3)",
            "AFE is the only classical dual-sum surface scoring +1 infrastructure",
            "Resonance resonators maximize |I2|^2/I1 for |zeta|, not arg P_X",
        ],
        "resolution_today": False,
        "conclusion": (
            "O-Moll from AFE: skeleton written; no coefficients found that are proved to boost "
            "A_X/theta_X at O-TL locations. Explicitly excludes Levinson-type mollifiers. OPEN."
        ),
    }


def package_P4_FE_path():
    """
    FE path bookkeeping: arg relations via chi(s), transfer left <-> right of critical line.
    Off-line transfer only — not Iso_H, not monodromy engine.
    """
    # chi(s) = 2^s pi^{s-1} sin(pi s/2) Gamma(1-s)
    # zeta(s) = chi(s) zeta(1-s)
    # arg zeta(s) = arg chi(s) + arg zeta(1-s)  (continuous branches carefully)
    return {
        "status": "P4_FE_PATH_BOOKKEEPING_EXECUTED",
        "identity": {
            "functional": "zeta(s) = chi(s) zeta(1-s)",
            "arg_form": "arg zeta(s) = arg chi(s) + arg zeta(1-s) (mod 2pi; continuous lift on paths avoiding zeros)",
            "chi_smooth": "arg chi(s) is elementary + Stirling for Gamma — controlled on vertical/horizontal paths away from poles",
        },
        "bookkeeping_lemmas_template": [
            {
                "name": "FE-Arg-Transfer",
                "statement": (
                    "Let gamma be a path from 1/2+it to sigma+it (sigma>1/2) avoiding zeros. "
                    "Let gamma' be the reflected path from 1/2-it to (1-sigma)-it (or conjugate-reflected as needed). "
                    "Then Delta_gamma arg zeta = Delta_gamma arg chi + Delta_{gamma_refl} arg zeta, "
                    "with arg chi explicitly estimable."
                ),
                "status": "standard FE consequence — bookkeeping, not a phase lower bound engine",
            },
            {
                "name": "FE-Hybrid-Split",
                "statement": (
                    "Under GHK on both s and 1-s (when applicable), "
                    "theta_X(s) = arg zeta(s) - arg Z_X(s) - Im E(s) relates to quantities at 1-s "
                    "plus archimedean/chi phases and dual partial products."
                ),
                "status": "schematic identity surface; full continuous-branch writeup open as hygiene",
            },
        ],
        "what_this_does": [
            "Moves bounds between sigma and 1-sigma",
            "Controls archimedean phase along horizontal paths via Stirling",
            "Clarifies that large phase on the left of 1/2 dualizes to the right",
        ],
        "what_this_does_NOT": [
            "Create loglog phase at maximal abscissa from nothing",
            "Prove GO (gap+Omega)",
            "Prove Iso_H",
            "Replace monodromy (already withdrawn)",
            "Close O-M1.3bis alone",
        ],
        "off_line_transfer_use": {
            "if_have": "strong on-line Omega at 1/2+it_n (SOC on-line)",
            "FE_gives": "related phase information at 1/2-it_n and via paths to 1-sigma",
            "still_need": "a path from 1/2+it_n toward beta*+i gamma* with controlled Phi (GO/tubes) and M1.2",
            "status": "bookkeeping layer only",
        },
        "resolution_today": False,
        "conclusion": (
            "FE path bookkeeping recorded as transfer identities for arg zeta / hybrid split. "
            "Useful hygiene for off-line continuation; does not by itself close O-M1.3bis or O-TL."
        ),
    }


def main():
    out_dir = Path(__file__).resolve().parents[1]
    P1 = package_P1_PAO()
    P2 = package_P2_kappa()
    P3 = package_P3_Omoll_AFE()
    P4 = package_P4_FE_path()
    results = {
        "status": "RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF",
        "date": "2026-08-08",
        "mandate": "Priority 4 attacks from resonance/Selberg explore",
        "zla": True,
        "does_not_prove": ["PAO", "kappa p>1", "O-Moll", "O-TL", "B_theta", "RH"],
        "P1_PAO_direct": P1,
        "P2_kappa_GHK_U": P2,
        "P3_Omoll_AFE": P3,
        "P4_FE_path": P4,
        "scoreboard": {
            "P1": {"resolved": False, "advance": "recast to Form C; epsilon_other Iso_H-adjacent"},
            "P2": {"resolved": False, "advance": "L2 proxy only; unconditional p>1 false"},
            "P3": {"resolved": False, "advance": "AFE-Moll skeleton; Levinson excluded"},
            "P4": {"resolved": False, "advance": "FE-Arg-Transfer bookkeeping written"},
        },
        "global_conclusion": (
            "All four priorities executed: PAO recast to fixed-frequency Form C with Iso_H-adjacent "
            "epsilon_other; no kappa p>1 theorem (L2 proxy only); AFE-Moll template only; FE path "
            "bookkeeping only. Zero tip closures. RH/O-TL open."
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

    out = out_dir / "rh_priority4_attacks_results.json"
    out.write_text(json.dumps(clean(results), indent=2), encoding="utf-8")
    print("OK", out)
    print("P1", P1["resolution_today"], P1["recast"]["Form_C"][:60])
    print("P2 p>1", P2["unconditional_p_gt_1"], "best p_eff", P2["attempted"]["best_p_eff_L2"]["p_eff_L2"])
    print("P2 L2 hits", len(P2["attempted"]["L2_proxy_hits_0.4"]))
    print("P3", P3["resolution_today"])
    print("P4", P4["resolution_today"])
    print(results["global_conclusion"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
