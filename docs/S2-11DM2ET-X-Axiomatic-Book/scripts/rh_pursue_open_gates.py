#!/usr/bin/env python3
"""
Pursue that which is open (2026-08-08):
  Form C | kappa p>1 | Iso_H | DH | GO | SOC strong+offline | AFE-Moll | B_theta | O-TL | RH

RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF · ZLA
Does not claim RH/O-TL/Form C/B_theta unconditional proofs.
"""
from __future__ import annotations

import json
import math
from pathlib import Path


def open_Form_C():
    """
    Zero-aware (non-circular) attempt sketch + terminal status.
    Escape: Iso_H/DH or non-circular EF feedback.
    """
    return {
        "gate": "Form_C",
        "standing_before": "OPEN",
        "attempt": {
            "zero_aware_sketch": (
                "Write S(X;rho*) via Thm 4.1 as residual int(psi-x). "
                "Subtract principal singular part of zeta'/zeta near other zeros; "
                "ask whether the star zero forces a slow oscillation in psi-x "
                "detectable after removing near contamination (epsilon_other). "
                "Under Iso_H, epsilon_other from same abscissa vanishes — reduces to classical "
                "Omega amplitude with controlled phase from conjugate only. "
                "Without Iso_H, multi-zero contamination blocks the reduction."
            ),
            "what_can_be_proved_today": [
                "Form B <-> Form C (already closed)",
                "Under Iso_H: epsilon_other controlled (conditional template EO(Iso_H) already named)",
                "Unconditional Form C: still blocked by FFML+ZEFB for free/generic methods",
            ],
            "non_circular_EF_feedback": {
                "status": "OPEN design",
                "idea": "Use vanishing order at rho* only through local Hadamard factor (s-rho*)^m, not through assuming large prime sums",
                "blocker": "Local factor gives self loglog already cancelled; remainder is global",
            },
        },
        "standing_after": "OPEN",
        "advance": "Zero-aware sketch recorded; still requires Iso_H or new technology for unconditional Form C",
        "closed": False,
    }


def open_kappa():
    """
    Use MA8 dual: bound zeta'/zeta on path segments.
    Split path: away-from-zeros vs approach arcs.
    """
    rows = []
    # Away: |zeta'/zeta| << log^2 t, far U ~ that / log X
    for logX in [12, 14, 16, 18]:
        for t in [1e6, 1e12, 3e12]:
            bound = (math.log(t + 2)) ** 2
            U = bound / logX
            rows.append({
                "regime": "away_crude_strip",
                "logX": logX, "t": t,
                "U_proxy": U,
                "U_le_0.4": U <= 0.4,
            })
    # Near sigma=1 in classical ZF: |zeta'/zeta| << log t
    for logX in [12, 14, 16]:
        for t in [1e12, 3e12]:
            bound = math.log(t + 2)
            U = bound / logX
            rows.append({
                "regime": "near_sigma_1_ZF",
                "logX": logX, "t": t,
                "U_proxy": U,
                "U_le_0.4": U <= 0.4,
            })

    away_ok = sum(1 for r in rows if r["regime"] == "away_crude_strip" and r["U_le_0.4"])
    zf_ok = sum(1 for r in rows if r["regime"] == "near_sigma_1_ZF" and r["U_le_0.4"])

    return {
        "gate": "kappa_p_gt_1",
        "standing_before": "OPEN",
        "attempt": {
            "split": "path = away-from-zeros segments + approach arcs",
            "away": "MA8 + classical |zeta'/zeta| bounds may give small far U — partial, not full M1.2",
            "approach": "requires dist(s, zeros) control = GO input; no unconditional kappa p>1",
            "rows_sample": rows[:6],
            "away_cells_U_le_0.4": away_ok,
            "zf_cells_U_le_0.4": zf_ok,
        },
        "standing_after": "OPEN",
        "advance": (
            "Segmented path analysis: away arcs potentially controllable via MA8+classical bounds; "
            "approach arcs remain GO-blocked. No p>1 theorem on full M1.3 paths."
        ),
        "closed": False,
        "partial": "away-segment conditional template named Kappa_away",
    }


def open_Iso_H():
    return {
        "gate": "Iso_H",
        "standing_before": "OPEN",
        "attempt": {
            "tools_rechecked": [
                "finite-height verification — only up to T0",
                "FE conjugate — only bar rho*",
                "density — dead edge to isolation",
                "half-isolation / Hyp F / Ivic — local or conditional",
            ],
            "new_technology": False,
        },
        "standing_after": "OPEN",
        "advance": "Ceiling confirmed; no new isolation method",
        "closed": False,
    }


def open_DH():
    # Ingham-shape exponents still positive at moderate sigma
    dens = []
    for sig in [0.55, 0.6, 0.7, 0.8, 0.9, 0.99]:
        th = 3 * (1 - sig) / (2 - sig)
        dens.append({"sigma": sig, "T_power_shape": th, "polylog": th <= 0})
    return {
        "gate": "DH",
        "standing_before": "OPEN",
        "attempt": {
            "target": "N(beta*,T)=O((log T)^C) at moderate beta*",
            "classical_shape": dens,
            "near_1_only_log_power": True,
        },
        "standing_after": "OPEN",
        "advance": "No polylog at moderate beta*; implication to B_theta remains conditional",
        "closed": False,
    }


def open_GO():
    return {
        "gate": "GO",
        "standing_before": "OPEN",
        "attempt": {
            "need": "hybrid Omega scale AND gap >= theta * mean gap, infinitely often",
            "have": "mean gaps classical; hybrid Omega on-line fixed X accepted; JOINT open",
            "link_to_kappa": "MA8 approach arcs need dist to zeros — GO is the natural input",
            "conditional_template": "GO(theta,X) already named in H4",
        },
        "standing_after": "OPEN",
        "advance": "Joint still missing; structural necessity for kappa approach arcs reaffirmed",
        "closed": False,
    }


def open_SOC():
    return {
        "gate": "SOC_strong_offline",
        "standing_before": "OPEN (typical closed)",
        "attempt": {
            "typical": "CLOSED at sqrt(log log)",
            "strong_loglog": "OPEN",
            "offline_transfer": "OPEN — FE bookkeeping only (P4); needs path + M1.2",
            "cannot_fake": "Do not claim typical = O-TL scale",
        },
        "standing_after": "OPEN",
        "advance": "No strong loglog; transfer still blocked by path package",
        "closed": False,
        "partial_closed": "typical on-line Omega",
    }


def open_AFE_Moll():
    return {
        "gate": "AFE_Moll",
        "standing_before": "OPEN",
        "attempt": {
            "surface": "AFE dual F + chi G + R",
            "objective": "amplify Im log P_X / A_X — not |zeta| or zero count",
            "forbidden": "Levinson/Conrey",
            "construction": "still empty — no coefficient optimization found for Im log P_X",
            "design_check": (
                "Any mollifier M that is a short Dirichlet poly multiplies zeta ~ F+chi G; "
                "arg(M zeta) = arg M + arg zeta; arg M is a controlled Dirichlet poly phase. "
                "To boost theta_X = Im log P_X one would need M to correlate with the partial Euler phase, "
                "not with full zeta. That correlation is not classical."
            ),
        },
        "standing_after": "OPEN",
        "advance": "Design constraint sharpened (mollify Euler phase not zeta zeros); construction still empty",
        "closed": False,
    }


def open_B_theta():
    return {
        "gate": "B_theta",
        "standing_before": "OPEN",
        "attempt": {
            "OR_cut": ["Form_C", "Iso_H", "DH"],
            "all_inputs_open": True,
            "proved_imps": "intact",
        },
        "standing_after": "OPEN",
        "advance": "No OR-input closed this round",
        "closed": False,
    }


def open_O_TL():
    return {
        "gate": "O_TL",
        "standing_before": "OPEN",
        "attempt": {
            "AND_cut": ["kappa", "GO", "SOC_strong_offline", "AFE_Moll"],
            "all_inputs_open": True,
            "partial": "typical Omega only",
        },
        "standing_after": "OPEN",
        "advance": "No AND-arm closed this round; kappa segmented analysis is partial only",
        "closed": False,
    }


def open_RH():
    return {
        "gate": "RH",
        "standing_before": "OPEN",
        "attempt": {
            "primary": "O_TL still open",
            "B_theta": "related engine, not proved implication to RH",
            "no_shortcut": "residual algebra forbidden (ZLA); GRH hypothesis not a proof",
        },
        "standing_after": "OPEN",
        "advance": "None — superordinate gate",
        "closed": False,
    }


def main():
    out = Path(__file__).resolve().parents[1]
    gates = [
        open_Form_C(),
        open_kappa(),
        open_Iso_H(),
        open_DH(),
        open_GO(),
        open_SOC(),
        open_AFE_Moll(),
        open_B_theta(),
        open_O_TL(),
        open_RH(),
    ]
    closed_now = [g["gate"] for g in gates if g.get("closed")]
    results = {
        "status": "RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF",
        "date": "2026-08-08",
        "mandate": "Pursue that which is open",
        "zla": True,
        "gates": {g["gate"]: g for g in gates},
        "newly_closed": closed_now,
        "partial_advances": [
            "Form_C: zero-aware sketch; needs Iso_H or new tech",
            "kappa: segmented away/approach; Kappa_away template; approach=GO",
            "AFE_Moll: objective sharpened to Euler phase not zero-count",
            "GO: necessity for kappa approach arcs reaffirmed",
        ],
        "still_open": [g["gate"] for g in gates if not g.get("closed")],
        "unconditional_resolutions": 0,
        "global_conclusion": (
            "All ten open gates pursued. None closed. Partial advances: zero-aware Form C sketch; "
            "kappa path segmentation (away vs GO-blocked approach); AFE-Moll objective sharpened. "
            "OR-cut and AND-cut inputs all remain open. RH/O-TL open."
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

    path = out / "rh_pursue_open_gates_results.json"
    path.write_text(json.dumps(clean(results), indent=2), encoding="utf-8")
    print("OK")
    print("newly_closed", closed_now)
    print("still_open", len(results["still_open"]))
    for g in gates:
        print(g["gate"], "closed" if g["closed"] else "OPEN", "|", g["advance"][:70])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
