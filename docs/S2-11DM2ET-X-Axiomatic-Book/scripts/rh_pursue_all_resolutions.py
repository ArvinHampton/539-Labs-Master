#!/usr/bin/env python3
"""
Pursue all for resolutions (2026-08-08):
  MA8 EF-dual far hybrid U for kappa
  MA6 n-aspect Diophantine at fixed gamma*
  MA1 Weil-smoothed Form C
  Remaining MA2-MA7, MA9 (analytic where possible)
  Standard gates: Form C, kappa, DH/Iso_H, GO/SOC/AFE-Moll

RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF · ZLA
Does not prove RH, O-TL, Form C, kappa p>1, B_theta.
"""
from __future__ import annotations

import json
import math
from pathlib import Path


def pursue_MA8():
    """
    Dualize far hybrid U-sum via explicit formula / Mellin to prime side.
    U(s, rho') ~ 1/((s-rho') log X) for Re(s-rho')log X >= 0 model (E1).
    Far sum_far U along a path in s.

    Attempt: write sum_{rho' far} U(s,rho') as integral of psi or as Dirichlet poly.
    Classical: log zeta(s) = -sum_rho log(s-rho) + ... (Hadamard)
    partial: sum_{rho} 1/(s-rho) = zeta'/zeta(s) + 1/2 log pi + 1/2 psi(s/2) ... (xi logarithmic derivative)

    So sum_rho 1/(s-rho) is EXPLICITLY the logarithmic derivative of xi/zeta structure.
    Far sum of U ~ (1/log X) * sum_far 1/(s-rho') is a truncated piece of -zeta'/zeta + arch.

    KEY IDENTITY (classical):
      -zeta'/zeta(s) = sum_n Lambda(n) n^{-s}   (Re s > 1)
      and meromorphic continuation:
      -zeta'/zeta(s) = sum_rho 1/(s-rho) - sum_n 1/(s+2n) + ... (partial fraction of xi)

    Therefore far zero sum of 1/(s-rho) = -zeta'/zeta(s) - near zeros - trivial - arch.
    This IS the dualization of far U (up to the log X factor and E1 shape).

    Consequence for kappa:
      far_signed U ~ (1/log X) * ( -zeta'/zeta(s) - sum_near 1/(s-rho) - trivial )
    On a path near the critical strip, -zeta'/zeta(s) is large near zeros and moderate off zeros.
    Upper-bounding far U becomes upper-bounding zeta'/zeta minus near contribution —
    which is the classical problem of growth of zeta'/zeta, NOT easier than kappa a priori.

    Partial win: far absolute majorant can be replaced by
      |far U| << (1/log X) * ( |zeta'/zeta(s)| + |near sum| + O(log(|t|+2)) )
    If path stays away from zeros by delta, |zeta'/zeta| << log^2 |t| classical.
    That gives path-away-from-zeros bounds — useful for M1.2 only on zero-free path segments.

    For paths that must approach a zero (O-TL), zeta'/zeta blows up — dual form explains why.
    """
    # Numeric: classical |zeta'/zeta(sigma+it)| << log^2(|t|) for sigma fixed > 1, or in ZF region
    rows = []
    for sigma in [0.6, 0.75, 0.9, 1.1]:
        for t in [1e6, 1e12, 3e12]:
            # schematic classical bounds:
            # Re s>1: |zeta'/zeta| <= -zeta'/zeta(sigma) ~ 1/(sigma-1)
            # critical strip crude: log^2 |t|
            if sigma > 1:
                bound = 1.0 / (sigma - 1.0)
            else:
                bound = (math.log(t + 2)) ** 2
            U_proxy = bound / 14.0  # / log X with logX~14
            rows.append({
                "sigma": sigma, "t": t,
                "zeta_prime_zeta_bound_schematic": bound,
                "far_U_proxy_over_logX14": U_proxy,
                "proxy_le_0.4": U_proxy <= 0.4,
            })

    away_hits = [r for r in rows if r["proxy_le_0.4"] and r["sigma"] > 1]
    strip_hits = [r for r in rows if r["proxy_le_0.4"] and r["sigma"] <= 1]

    return {
        "status": "MA8_EXECUTED",
        "identity": {
            "name": "Far-U / logarithmic-derivative dual",
            "formula": (
                "sum_rho 1/(s-rho) = -zeta'/zeta(s) - (trivial zeros contrib) + archimedean "
                "(partial fraction of xi); far piece = full - near - trivial - arch"
            ),
            "U_model": "U ~ 1/((s-rho') log X) so sum_far U ~ (1/log X) * sum_far 1/(s-rho')",
            "standing": "classical identity surface — recorded as programme dual for far U",
        },
        "consequence": {
            "kappa_rewritten": (
                "kappa problem equivalent (up to near-zero and arch errors) to controlling "
                "zeta'/zeta(s) along M1.3 paths, minus near zeros already separated"
            ),
            "why_not_easier": (
                "On paths approaching zeros, zeta'/zeta has poles; upper bounds require "
                "distance-to-nearest-zero control — which is GO/gap territory"
            ),
            "zero_free_path_segments": (
                "Away from zeros / in ZF region near sigma=1, classical |zeta'/zeta| bounds "
                "give far U << (log^2|t|)/log X — may be small; does not cover approach-to-zero arcs"
            ),
        },
        "numeric_proxy_rows": rows,
        "away_sigma_gt_1_hits": away_hits,
        "strip_hits": strip_hits,
        "resolution": {
            "kappa_p_gt_1": False,
            "new_identity": True,
            "links_kappa_to_GO": True,
            "note": "MA8 succeeds as identity dual; estimate still open; correlation kappa↔GO strengthened",
        },
        "conclusion": (
            "Far hybrid U dualized to zeta'/zeta via classical partial fractions. "
            "kappa becomes control of zeta'/zeta on paths; near zeros need gap control (GO). "
            "No p>1 kappa theorem, but the dual is no longer missing."
        ),
    }


def pursue_MA6():
    """
    Metric Diophantine: distribution of {gamma* log p / (2pi)} for primes p.
    Form C leading piece: sum_p p^{-beta*} e^{-i gamma* log p}.
    If gamma* log p mod 2pi were free to choose, we'd align; gamma* is fixed.

    What can be said unconditionally?
    - (log p) are linearly independent over Q with 1? log p independent over Q.
    - Sequence p |-> {alpha log p} for alpha = gamma*/(2pi):
      This is NOT a standard Kronecker sequence n*alpha; it's log p * alpha.

    Known: under various hypotheses, log p mod 2pi/gamma is dense if gamma ≠0.
    Density of {gamma log p / 2pi} in [0,1]: expected if gamma/(2pi) is fixed nonzero.

    For large values of sum_{p<=Y} p^{-beta*} e^{-i gamma* log p}:
    - This is a Dirichlet poly over primes at complex s=beta*+i gamma*.
    - Related to log zeta(s) ~ sum p^{-s} for Re s>1; at beta*<1 it's the partial sum of -zeta'/zeta pieces.

    Actually sum_p p^{-rho*} is essentially the partial Euler factor of -zeta'/zeta or log zeta.
    |sum_{p<=Y} p^{-rho*}| large is related to zeta having a zero or pole nearby —
    circular for Form C at the zero itself.

    CIRCULARITY BARRIER (named):
      Evaluating large prime sums at s=rho* where zeta(rho*)=0 is entangled with the zero;
      standard Euler product identities fail at zeros. Form C is not a free Diophantine sum
      independent of the zero condition.

    Metric results about equidistribution of {gamma log p} for almost all gamma do NOT
    give the specific gamma* of a zero.
    """
    return {
        "status": "MA6_EXECUTED",
        "diophantine_object": "{gamma* log p / 2pi} mod 1",
        "linear_independence": "log p independent over Q — density heuristics for generic gamma",
        "barrier": {
            "name": "Zero-Entangled Frequency Barrier (ZEFB)",
            "statement": (
                "The frequency gamma* is not a free Diophantine parameter; it is the ordinate "
                "of a zero of zeta. Large-value questions for sum Lambda(n) n^{-rho*} are "
                "entangled with the vanishing of the Euler product / zeta at rho*. "
                "Almost-all gamma metric theorems do not transfer to zero ordinates."
            ),
        },
        "what_was_checked": [
            "Generic equidistribution heuristics — insufficient for zero ordinates",
            "Partial sum of p^{-rho*} vs log zeta / zeta' — singular at zeros",
            "No metric theorem found that forces limsup |S_X(rho*)|=infinity at a zero",
        ],
        "resolution": {
            "Form_C": False,
            "new_barrier_named": "ZEFB",
            "relation_to_FFML": (
                "ZEFB is the arithmetic dual of FFML: FFML blocks free-t methods; "
                "ZEFB blocks treating gamma* as a generic Diophantine frequency"
            ),
        },
        "conclusion": (
            "MA6 does not yield Form C. Named ZEFB: zero-entangled frequency blocks generic "
            "Diophantine transfer. FFML+ZEFB together fence free-t and generic-n Diophantine attacks."
        ),
    }


def pursue_MA1():
    """
    Weil explicit formula: for nice even test function h,
    sum_rho h(gamma) = (stuff with h-hat on primes) + archimedean.
    Smoothed Form C: replace sharp cutoff sum_{n<=X} by smooth weight.

    Define S_h(rho*) = sum_n Lambda(n) n^{-rho*} g(log n) for smooth g supported on [0, log X].
    By Mellin/Weil, this relates to sum over zeros of a transform of g shifted by rho*.

    At s=rho*, the dual zero sum has a diagonal term from rho* itself and off-diagonals.
    Self contribution is controlled (like self loglog).
    Off-diagonal zero sums reappear — similar to pre-signed-sum difficulty.

    Smoothing helps analysis of remainders; does not remove FFML/ZEFB for limsup of unsmoothed S_X.
    Conditional: if one only wants limsup of smoothed sums, still need lower bound mechanism.
    """
    return {
        "status": "MA1_EXECUTED",
        "smoothed_form_C": {
            "definition": "S_g(rho*) = sum_n Lambda(n) n^{-rho*} g(log n), g smooth, supp in [0,L]",
            "Weil_dual": "expressible via sum_rho hat{g}-type transforms + archimedean",
            "self_term": "controllable (smooth analog of self loglog)",
            "off_diagonal": "returns zero sums — same difficulty class as pre-Thm-4.1",
        },
        "comparison_to_unsmoothed": {
            "advantages": ["better remainder estimates", "justifies interchange", "flexible weights"],
            "does_not_give": "automatic limsup infinity for unsmoothed Form C",
            "FFML": "still applies to free-t methods on smoothed sums",
            "ZEFB": "still applies — frequency still gamma*",
        },
        "resolution": {
            "Form_C_unsmoothed": False,
            "smoothed_Form_C_lower_bound": False,
            "identity_surface_recorded": True,
        },
        "conclusion": (
            "Weil-smoothed Form C is a legitimate identity surface for future work; "
            "no lower bound obtained; does not bypass FFML/ZEFB."
        ),
    }


def pursue_remaining_MA():
    return {
        "MA2_Guinand_on_line": {
            "status": "reviewed",
            "resolution": False,
            "note": "On-line bookkeeping alternative; does not open off-line Form C or O-TL alone",
        },
        "MA3_XT_optimization": {
            "status": "executed_hygiene",
            "resolution": False,
            "note": "VK+EF joint uppers improve constants only; tabulated schematically in prior VK note",
        },
        "MA4_Landau_Ingham": {
            "status": "reviewed",
            "resolution": False,
            "note": "Amplitude Omega classical; epsilon_other still Iso_H-adjacent",
        },
        "MA5_pair_correlation": {
            "status": "reviewed",
            "resolution": False,
            "note": "Variance/typical size under PC; not limsup Form C at single rightmost zero",
        },
        "MA7_smoothed_overlap_MA1": {
            "status": "merged_with_MA1",
            "resolution": False,
        },
        "MA9_Bombieri_Vinogradov": {
            "status": "reviewed",
            "resolution": False,
            "note": "Averaged AP primes; not fixed complex rho*",
        },
        "MA10_OR_AND_strategy": {
            "status": "strategic_lock",
            "resolution": False,
            "note": "Effort: single B_theta gate cheaper than O_TL AND; still not RH",
        },
        "MA11_vacuous_if_RH": {
            "status": "conceptual_lock",
            "resolution": False,
        },
        "MA12_dual_lower_upper": {
            "status": "conceptual_lock",
            "resolution": False,
        },
    }


def pursue_standard_gates():
    return {
        "Form_C": {"open": True, "blockers": ["FFML", "ZEFB"]},
        "kappa_p_gt_1": {
            "open": True,
            "advance": "MA8 dual to zeta'/zeta; estimate open; linked to GO on approach arcs",
        },
        "DH": {"open": True},
        "Iso_H": {"open": True},
        "GO": {
            "open": True,
            "advance": "MA8 shows kappa on approach-to-zero arcs needs gap/distance control — GO correlation",
        },
        "SOC": {"open": True, "typical_proved": True},
        "AFE_Moll": {"open": True},
        "B_theta": {"open": True},
        "O_TL": {"open": True},
        "RH": {"open": True},
    }


def main():
    out = Path(__file__).resolve().parents[1]
    MA8 = pursue_MA8()
    MA6 = pursue_MA6()
    MA1 = pursue_MA1()
    rest = pursue_remaining_MA()
    gates = pursue_standard_gates()

    results = {
        "status": "RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF",
        "date": "2026-08-08",
        "mandate": "Pursue all for resolutions (MA1-MA12 + standard gates)",
        "zla": True,
        "MA8_EF_dual_kappa": MA8,
        "MA6_Diophantine": MA6,
        "MA1_Weil_smooth": MA1,
        "remaining_MA": rest,
        "gates": gates,
        "new_named_objects": [
            "Far-U / logarithmic-derivative dual (MA8 identity)",
            "ZEFB Zero-Entangled Frequency Barrier (MA6)",
            "GO↔kappa correlation via distance-to-zero in zeta'/zeta (MA8)",
        ],
        "unconditional_resolutions": 0,
        "scoreboard": {
            "identities_added": 2,
            "barriers_named": 1,
            "gates_closed": 0,
            "RH": "OPEN",
            "O_TL": "OPEN",
            "Form_C": "OPEN",
            "kappa_p_gt_1": "OPEN",
        },
        "global_conclusion": (
            "All resolution angles pursued. MA8: far U dualized to zeta'/zeta (identity win; kappa still open; "
            "links kappa to GO). MA6: ZEFB named — generic Diophantine does not transfer to zero ordinates. "
            "MA1: Weil-smoothed Form C surface recorded; no lower bound. Remaining MA: hygiene/locks only. "
            "Unconditional resolution count: 0. RH/O-TL open."
        ),
    }

    def clean(o):
        if isinstance(o, float):
            if math.isnan(o): return "nan"
            if math.isinf(o): return "inf"
            return o
        if isinstance(o, dict): return {k: clean(v) for k, v in o.items()}
        if isinstance(o, list): return [clean(v) for v in o]
        return o

    path = out / "rh_pursue_all_resolutions_results.json"
    path.write_text(json.dumps(clean(results), indent=2), encoding="utf-8")
    print("OK", path)
    print("MA8", MA8["resolution"])
    print("MA6", MA6["resolution"])
    print("MA1", MA1["resolution"])
    print("unconditional", 0)
    print(results["global_conclusion"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
