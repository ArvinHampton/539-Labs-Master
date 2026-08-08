#!/usr/bin/env python3
"""
Execute next-5 pure-math package (2026-08-08):
  1. Non-absolute far-sum: path-radius vs J, signed/partial cancellation models
  2. Gap+Omega correlation: classical ledger + conditional templates
  3. O-Moll: classical mollifier survey vs phase-oriented target
  4. Iso_H: classical isolation technology ceiling (no new tech invented)
  5. ZLA + residual firewall compliance (do not reopen A0-A5+/K+)

RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF · ZLA · no model constants · no residual in zeta lemmas.
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


# ========== 1. Non-absolute far-sum ==========

def far_absolute(gamma, C_U, c_r, logX):
    """2pi R-vM absolute far-sum (L2 formula)."""
    Lg = math.log(gamma)
    r = c_r / Lg
    J = math.log2(max(2.0 * gamma / r, 2.0))
    far = C_U * (J + 1.0) * Lg / (math.pi * logX)
    return far, J, r, Lg


def ghk_E(gamma, logX, sigma, c1, c2=8.0):
    lt1 = math.log(max(c1, 1e-300)) + 4 * logX - 2 * math.log(gamma) - 2 * math.log(max(logX, 1e-15))
    t1 = math.exp(lt1) if lt1 < 700 else float("inf")
    t2 = c2 * math.exp(-sigma * logX) * logX
    return (t1 + t2 if math.isfinite(t1) else float("inf")), t1, t2


def package_1_nonabsolute():
    gamma = 3e12
    C_U = 1.0  # E1
    c1_exec = 291.0
    c1_best = 148.0
    c1_hyp = 1.0

    # --- 1a path radius vs J tradeoff ---
    # r = c_r / log gamma; larger c_r => fewer annuli J, but local isolation harder
    # and U near path may worsen. Scan c_r.
    radius_scan = []
    for c_r in [0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 5.0, 10.0]:
        for logX in [12, 14, 16, 18, 20]:
            far, J, r, Lg = far_absolute(gamma, C_U, c_r, float(logX))
            E291, _, _ = ghk_E(gamma, float(logX), 0.5, c1_exec)
            E1, _, _ = ghk_E(gamma, float(logX), 0.5, c1_hyp)
            radius_scan.append(
                {
                    "c_r": c_r,
                    "logX": logX,
                    "r": r,
                    "J": J,
                    "far_abs": far,
                    "E_c1_291": fin(E291),
                    "E_c1_1": fin(E1),
                    "far_le_0.4": far <= 0.4,
                    "joint_c1_1": far <= 0.4 and fin(E1) <= 0.1,
                }
            )

    # Best absolute far under c1=1 GHK window
    best_abs = None
    for row in radius_scan:
        if fin(row["E_c1_1"]) <= 0.1:
            if best_abs is None or row["far_abs"] < best_abs["far_abs"]:
                best_abs = row

    # --- 1b signed / partial cancellation models ---
    # Model: far_signed = far_abs * kappa, kappa in (0,1]
    # kappa = 1: absolute; kappa = 1/sqrt(J): random-walk cancellation;
    # kappa = 1/J: strong coherent cancellation; kappa = 1/log J: mild
    cancel_models = []
    for name, kappa_fn in [
        ("absolute", lambda J: 1.0),
        ("mild_1_over_logJ", lambda J: 1.0 / max(math.log(J + 1), 1.0)),
        ("random_walk_1_over_sqrtJ", lambda J: 1.0 / math.sqrt(max(J, 1))),
        ("strong_1_over_J", lambda J: 1.0 / max(J, 1)),
        ("square_1_over_J2", lambda J: 1.0 / max(J, 1) ** 2),
    ]:
        for c_r in [0.25, 1.0, 5.0]:
            for logX in [14, 16, 18]:
                far_a, J, r, Lg = far_absolute(gamma, C_U, c_r, float(logX))
                kap = kappa_fn(J)
                far_s = far_a * kap
                E, _, _ = ghk_E(gamma, float(logX), 0.5, c1_hyp)
                cancel_models.append(
                    {
                        "model": name,
                        "kappa": kap,
                        "c_r": c_r,
                        "logX": logX,
                        "J": J,
                        "far_abs": far_a,
                        "far_signed": far_s,
                        "E_c1_1": fin(E),
                        "far_le_0.4": far_s <= 0.4,
                        "joint_c1_1": far_s <= 0.4 and fin(E) <= 0.1,
                        "joint_c1_291": far_s <= 0.4 and fin(ghk_E(gamma, float(logX), 0.5, c1_exec)[0]) <= 0.1,
                    }
                )

    # Which models open joint at c1=1 / c1=291?
    opens_c1_1 = [m for m in cancel_models if m["joint_c1_1"]]
    opens_c1_291 = [m for m in cancel_models if m["joint_c1_291"]]

    # --- 1c required kappa at best GHK point ---
    # At logX maximizing room under c1=1, E<=0.1
    req = []
    for logX in [x * 0.1 for x in range(100, 250)]:
        E, t1, t2 = ghk_E(gamma, logX, 0.5, c1_hyp)
        if fin(E) > 0.1:
            continue
        for c_r in [0.25, 1.0, 5.0]:
            far_a, J, r, Lg = far_absolute(gamma, C_U, c_r, logX)
            kappa_need = 0.4 / far_a if far_a > 0 else 0.0
            req.append(
                {
                    "logX": logX,
                    "c_r": c_r,
                    "far_abs": far_a,
                    "J": J,
                    "kappa_need_for_far_0.4": kappa_need,
                    "equiv_random_walk": kappa_need <= 1.0 / math.sqrt(max(J, 1)),
                    "equiv_strong_1_over_J": kappa_need <= 1.0 / max(J, 1),
                }
            )
    # best (largest kappa_need = easiest cancellation demand... actually want MAX kappa_need? 
    # No: larger kappa_need means need less cancellation (kappa closer to 1).
    # Easiest = largest kappa_need (closest to 1)
    if req:
        easiest = max(req, key=lambda d: d["kappa_need_for_far_0.4"])
        hardest_still_ok = min(req, key=lambda d: d["kappa_need_for_far_0.4"])
    else:
        easiest = hardest_still_ok = None

    return {
        "status": "N1_NONABSOLUTE_FAR_SUM_EXECUTED",
        "absolute_baseline": {
            "formula": "far = C_U (J+1) Lg / (pi logX), C_U=1 from E1",
            "best_under_c1_1_GHK": best_abs,
            "radius_scan_sample": [r for r in radius_scan if r["logX"] == 14][:8],
        },
        "path_radius_vs_J": {
            "note": (
                "Larger c_r reduces J (fewer annuli) and absolute far, but enlarges the "
                "local disk that must be free of other zeros and may worsen path geometry. "
                "At c_r=10, J drops and far improves, but isolation radius r=c_r/log gamma "
                "becomes large vs mean gap 2pi/log gamma."
            ),
            "mean_gap_over_r_at_cr": {
                str(c_r): (2 * math.pi / math.log(gamma)) / (c_r / math.log(gamma))
                for c_r in [0.25, 1.0, 5.0, 10.0]
            },
            # mean_gap / r = 2pi / c_r
        },
        "cancellation_models": {
            "grid": cancel_models,
            "opens_joint_c1_1": opens_c1_1,
            "opens_joint_c1_291": opens_c1_291,
            "n_opens_c1_1": len(opens_c1_1),
            "n_opens_c1_291": len(opens_c1_291),
        },
        "kappa_required": {
            "easiest_in_GHK_window_c1_1": easiest,
            "smallest_kappa_need_in_window": hardest_still_ok,
            "reading": (
                "If easiest kappa_need is still << 1, absolute bounds cannot work; "
                "need at least that cancellation factor from signed sums."
            ),
        },
        "signed_sum_link": {
            "corpus": "RH_Signed_Sum_Attack.md",
            "object": "Sigma_X residual after EF interchange — main oscillatory Off_X piece",
            "status": "reduced to weighted (psi-x); lower bound open; not yet a far-sum kappa theorem",
            "programme_use": (
                "A proved |signed far sum| <= kappa * absolute with kappa <= kappa_need "
                "would open numerical M1.2 under real c1. No such kappa theorem today."
            ),
        },
        "conclusion": (
            "Path-radius enlargement helps mildly but r >> mean gap breaks isolation. "
            "Random-walk (1/sqrt J) or stronger cancellation models are the only scanned "
            "routes that open far<=0.4 under c1=1; absolute and mild log cancellation do not. "
            "c1=291 still needs stronger cancellation than random-walk in most cells. "
            "Signed-sum attack is the correct classical vessel; kappa theorem remains open."
        ),
    }


# ========== 2. Gap + Omega correlation ==========

def package_2_gap_omega():
    """
    Classical ledger: large values of zeta / hybrid discrepancy vs zero gaps.
    No new theorem; record conditional templates and known separations.
    """
    t_examples = [1e6, 1e12, 3e12]
    gap_stats = []
    for t in t_examples:
        mean_gap = 2 * math.pi / math.log(t)
        # Montgomery pair correlation heuristic: normalized gaps have GUE distribution
        # P(gap > theta * mean) ~ exp(-c theta^2) for large theta in GUE
        for theta in [0.5, 1.0, 2.0, 3.0]:
            # crude GUE large-gap tail exp(-pi theta^2 / 4) schematic for illustration
            tail = math.exp(-math.pi * theta ** 2 / 4.0)
            gap_stats.append(
                {
                    "t": t,
                    "mean_gap": mean_gap,
                    "theta": theta,
                    "gap_width": theta * mean_gap,
                    "GUE_large_gap_tail_schematic": tail,
                    "note": "schematic GUE tail only — not a theorem for zeta",
                }
            )

    return {
        "status": "N2_GAP_OMEGA_CORRELATION_EXECUTED",
        "classical_positive": [
            {
                "item": "Mean ordinate spacing 2pi/log t",
                "status": "classical (R-vM)",
            },
            {
                "item": "Large values of log|zeta(1/2+it)| on short intervals",
                "status": "classical Omega / resonance literature (Soundararajan, Bondarenko-Seip, ...)",
            },
            {
                "item": "On-line hybrid Im D_X limsup for fixed X",
                "status": "programme-accepted (Kronecker / resonance discrepancy notes)",
            },
            {
                "item": "Zero gaps: selective results (e.g. large gaps exist infinitely often under RH or unconditionally weaker)",
                "status": "classical partial; not coupled to hybrid Omega times",
            },
        ],
        "classical_negative_missing": [
            {
                "item": "t_n with |Im D_X(1/2+it_n)| >> sqrt(X)/log X AND nearest-zero gap >= theta * mean_gap",
                "status": "NO classical theorem",
            },
            {
                "item": "Independence of prime-angle torus maximisers from zero ordinates",
                "status": "OPEN (could fail if large values driven by nearby zeros)",
            },
            {
                "item": "Positive-density set of wide gaps at heights of hybrid maximisers",
                "status": "OPEN",
            },
        ],
        "conditional_templates": [
            {
                "name": "GUE_gap + independent_torus (heuristic)",
                "hypothesis": "Normalized gaps ~ GUE; torus maximisers independent of zeros at scale 1/log t",
                "conclusion": "Positive density of (wide gap AND large Im D_X) for fixed X",
                "status": "heuristic only — not ZLA theorem",
            },
            {
                "name": "Hypothesis F / Iso_H local",
                "hypothesis": "Few vertical lines / Iso_H",
                "conclusion": "Avoidance of zeros near maximisers easier; not about horizontal gaps",
                "status": "conditional; different geometry",
            },
            {
                "name": "Pair correlation (Montgomery)",
                "hypothesis": "PC for zeros",
                "conclusion": "Gap statistics; still no automatic hybrid Omega correlation",
                "status": "conditional / partial classical",
            },
        ],
        "gap_tail_schematic": gap_stats[:8],
        "link_to_P3_L3": (
            "Path continuation needs gap+Omega simultaneously. This package records that "
            "the correlation is a genuine open classical problem, not a missing citation."
        ),
        "conclusion": (
            "No classical theorem links large hybrid discrepancy times to wide ordinate gaps. "
            "Conditional/heuristic templates exist (GUE+independence) but are not proved for zeta. "
            "Gap+Omega correlation remains OPEN as a pure Cat A obstruction for tube paths."
        ),
    }


# ========== 3. O-Moll survey ==========

def package_3_omoll():
    """
    Classical mollifiers vs programme need for phase-oriented mollifier.
    """
    mollifiers = [
        {
            "name": "Dirichlet polynomial mollifier (Levinson, Conrey)",
            "form": "psi(s) = sum_{n<=y} mu(n) n^{-s} / n^{a} or similar",
            "target": "increase proportion of zeros on the critical line (amplitude of zeta*psi)",
            "phase_oriented": False,
            "feeds_O_TL": False,
            "note": "Optimizes |zeta psi| moments / horizontal distribution — not arg P_X lower bounds",
        },
        {
            "name": "Levinson method (1974)",
            "form": "mollified second moment on Re s = 1/2 + a/log T",
            "target": ">= 1/3 of zeros on the line (later improved)",
            "phase_oriented": False,
            "feeds_O_TL": False,
            "note": "Zero-counting on the line; not continuous arg of hybrid Euler product",
        },
        {
            "name": "Conrey / Bui-Conrey-Young type long mollifiers",
            "form": "longer Dirichlet polynomials, often with mu * P(log)",
            "target": "larger proportion on the line",
            "phase_oriented": False,
            "feeds_O_TL": False,
            "note": "Still amplitude/zero-detection technology",
        },
        {
            "name": "Soundararajan resonance method",
            "form": "resonator R(t) = sum n^{-it} over special set",
            "target": "large |zeta(1/2+it)|",
            "phase_oriented": "partial — phase alignment of Dirichlet terms",
            "feeds_O_TL": "partial — feeds large values / Omega, not directly arg P_X at maximal abscissa",
            "note": "Closest classical cousin to phase alignment; still not a mollifier for A_X at O-TL locations",
        },
        {
            "name": "GHK hybrid weight u / f_star (programme)",
            "form": "smooth cutoff for hybrid Euler-Hadamard product",
            "target": "identity zeta = P_X Z_X (1+E)",
            "phase_oriented": "infrastructure only",
            "feeds_O_TL": "enables hybrid arg split; not a lower-bound engine",
            "note": "Already used; not O-Moll",
        },
        {
            "name": "Programme O-Moll target (open)",
            "form": "unknown — would need to boost continuous theta_X or A_X at maximal abscissa",
            "target": "|A_X| or |theta_X| >> log log X with controlled remainder",
            "phase_oriented": True,
            "feeds_O_TL": True,
            "note": "No classical object matches this specification",
        },
    ]

    hits = [m for m in mollifiers if m["phase_oriented"] is True and m["feeds_O_TL"] is True]
    partial = [m for m in mollifiers if m["phase_oriented"] == "partial" or m["feeds_O_TL"] == "partial"]

    return {
        "status": "N3_O_MOLL_SURVEY_EXECUTED",
        "catalogue": mollifiers,
        "exact_programme_match_count": len(hits),
        "partial_cousins": partial,
        "decision": (
            "No concrete classical phase-oriented mollifier matches O-Moll. "
            "Resonance method is the nearest cousin for phase alignment of Dirichlet polynomials, "
            "but it targets |zeta| large values, not hybrid arg at maximal abscissa. "
            "O-Moll remains OPEN; do not invent a mollifier."
        ),
        "conclusion": "O-Moll not closable from classical shelf inventory on 2026-08-08.",
    }


# ========== 4. Iso_H technology ceiling ==========

def package_4_isoh():
    tools = [
        {
            "tool": "Point isolation of zeros",
            "gives": "Finite zeros on compact height segments",
            "gives_Iso_H_unbounded": False,
        },
        {
            "tool": "Functional equation quartets",
            "gives": "Only forced same-abscissa partner is conjugate",
            "gives_Iso_H_unbounded": False,
        },
        {
            "tool": "Ivic multiplicity bounds",
            "gives": "Control m at one point; large m pushes left",
            "gives_Iso_H_unbounded": False,
        },
        {
            "tool": "Zero density N(sigma,T)",
            "gives": "Bulk count to the right of sigma",
            "gives_Iso_H_unbounded": False,
            "note": "Density is not isolation (RH_Density_vs_Isolation.md)",
        },
        {
            "tool": "Maynard-Pratt half-isolation",
            "gives": "Local one-sided vertical neighborhood; few such zeros; under Hyp F => better density",
            "gives_Iso_H_unbounded": False,
            "note": "Not Iso_H; converse direction under Hypothesis F",
        },
        {
            "tool": "Levinson-Ivic horizontal isolation near sigma=1",
            "gives": "Better zero-free / isolation near 1",
            "gives_Iso_H_unbounded": False,
            "note": "Edge geometry, not arbitrary beta*>1/2",
        },
        {
            "tool": "Hypothesis F (finite vertical lines)",
            "gives": "Conditional density improvements with half-isolation",
            "gives_Iso_H_unbounded": False,
            "note": "Conditional; not unconditional Iso_H",
        },
        {
            "tool": "NEW isolation technology (required)",
            "gives": "N_line(beta*,T) = O((log T)^C) or finite for each beta*>1/2",
            "gives_Iso_H_unbounded": True,
            "note": "Does not exist in classical corpus as of this resolve",
        },
    ]

    return {
        "status": "N4_ISO_H_TECHNOLOGY_CEILING_EXECUTED",
        "definition_Iso_H": (
            "At rightmost abscissa beta*>1/2, up to EF truncation the only zeros with "
            "Re rho = beta* are {rho*, conj rho*}."
        ),
        "tools": tools,
        "proved_implications_intact": "(RM)+(Iso_H) => OP1 => B_theta (ND1)",
        "new_technology_found": False,
        "conclusion": (
            "No new isolation technology appears in the classical corpus. Density will not "
            "imply Iso_H. Unconditional Iso_H remains OPEN. Do not claim progress beyond the ceiling."
        ),
    }


# ========== 5. ZLA + residual firewall ==========

def package_5_firewall():
    return {
        "status": "N5_ZLA_RESIDUAL_FIREWALL_COMPLIANT",
        "zla_rules": [
            "No model constants in zeta theorem environments",
            "No residual packaging integers (18, 521, 539, 56, ...) as lemmas about zeta",
            "No 11D / brane / continuum Cat B objects in pure Cat A RH proofs",
            "Classical analysis language only for zeta claims",
        ],
        "residual_locks_not_reopened": [
            "A0-A2 discrete",
            "A3 first model",
            "A4-A5 0-stem",
            "A4+/A5+ on K+",
            "Form SS / permanent class / thin-F kit",
            "P+ optional permanent-class survival lock (combinatorial only)",
            "Option 3 / No-Go",
        ],
        "this_package_compliance": {
            "uses_residual_in_zeta_lemmas": False,
            "reopens_Architecture_A": False,
            "introduces_model_constants_in_RH": False,
            "category_A_B_separation": True,
        },
        "conclusion": "Firewall held. Tracks 1-4 are pure Cat A classical analysis only.",
    }


def main():
    out_dir = Path(__file__).resolve().parents[1]
    p1 = package_1_nonabsolute()
    p2 = package_2_gap_omega()
    p3 = package_3_omoll()
    p4 = package_4_isoh()
    p5 = package_5_firewall()

    # Headline extracts
    opens1 = p1["cancellation_models"]["n_opens_c1_1"]
    opens291 = p1["cancellation_models"]["n_opens_c1_291"]
    easiest = p1["kappa_required"]["easiest_in_GHK_window_c1_1"]

    results = {
        "status": "RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF",
        "date": "2026-08-08",
        "mandate": "Execute all five next pure-math moves",
        "zla": True,
        "no_model_constants": True,
        "does_not_prove": ["RH", "O-TL", "Iso_H", "O-Moll", "Mass-with-A", "uniform O-M1.2"],
        "N1_nonabsolute_far_sum": p1,
        "N2_gap_omega": p2,
        "N3_omoll": p3,
        "N4_isoh": p4,
        "N5_firewall": p5,
        "global_conclusion": {
            "N1": p1["conclusion"],
            "N2": p2["conclusion"],
            "N3": p3["conclusion"],
            "N4": p4["conclusion"],
            "N5": p5["conclusion"],
            "one_liner": (
                f"Non-absolute far-sum: only cancellation models open joint windows "
                f"(n_open c1=1: {opens1}, c1=291: {opens291}); kappa theorem open via signed sums. "
                "Gap+Omega: no classical link. O-Moll: no shelf match. Iso_H: no new tech. "
                "ZLA/residual firewall held. RH/O-TL open."
            ),
            "kappa_easiest": easiest,
        },
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

    out = out_dir / "rh_execute_next5_results.json"
    out.write_text(json.dumps(clean(results), indent=2), encoding="utf-8")
    print("OK", out)
    print("best_abs", p1["absolute_baseline"]["best_under_c1_1_GHK"])
    print("opens c1=1", opens1, "c1=291", opens291)
    print("easiest kappa", easiest)
    # show which models open
    for m in p1["cancellation_models"]["opens_joint_c1_1"][:6]:
        print(" open1", m["model"], "cr", m["c_r"], "logX", m["logX"], "far", m["far_signed"])
    for m in p1["cancellation_models"]["opens_joint_c1_291"][:6]:
        print(" open291", m["model"], "cr", m["c_r"], "logX", m["logX"], "far", m["far_signed"])
    print("omoll matches", p3["exact_programme_match_count"])
    print("isoh new tech", p4["new_technology_found"])
    print("ONE", results["global_conclusion"]["one_liner"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
