#!/usr/bin/env python3
"""
Shell restriction r_W boolean + multi-W curve + P+ same-tower triple count.

r_W != 0  <=>  M(I_win) > 0
Status at W=18: SURJECTIVE_BOTH_SHELL_AND_TOWER

PROVENANCE: residual (S) only. Not biology peaks. Option 3 intact.
"""
from __future__ import annotations

import json
import math
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path


def atoms():
    N_flux = math.floor(math.e**3 * 3**5)
    Q = 9
    f_max = math.ceil(N_flux / 243)
    B_prime = (N_flux - f_max) // Q
    L_pref = math.floor(math.e**3 / math.log(3))
    loads = [21] * 20 + [20] * (243 - 20)
    return N_flux, Q, f_max, B_prime, L_pref, loads


def tower_of(x: int, loads: list[int]) -> int:
    acc = 0
    for t, L in enumerate(loads):
        if acc <= x < acc + L:
            return t
        acc += L
    return len(loads) - 1


def sgn(d: int) -> int:
    return (d > 0) - (d < 0)


def pairing_mass_on_edges(df: list[int], edge_indices: list[int], Q: int = 9) -> int:
    """M(I) = sum_{a<b} sum_{i in I} |alpha(a,b)*df[i]| = C(9,2)*sum_{i in I}|df[i]|."""
    return (Q * (Q - 1) // 2) * sum(abs(df[i]) for i in edge_indices)


def main() -> int:
    N_flux, Q, f_max, B_prime, L_pref, loads = atoms()
    assert L_pref == 18 and B_prime == 539

    residual = list(range(f_max, N_flux))
    O = [residual[i] for i in range(len(residual)) if i % Q == 0][:B_prime]
    fvals = [tower_of(x, loads) for x in O]
    df = [fvals[i + 1] - fvals[i] for i in range(B_prime - 1)]

    W = L_pref
    I_all = list(range(B_prime - 1))
    I_win = list(range(W - 1))  # 0..16
    I_tow = list(range(W - 1, B_prime - 1))

    M_all = pairing_mass_on_edges(df, I_all, Q)
    M_win = pairing_mass_on_edges(df, I_win, Q)
    M_tow = pairing_mass_on_edges(df, I_tow, Q)
    assert M_win + M_tow == M_all
    assert M_all == 8676 and M_win == 252 and M_tow == 8424

    rW_nonzero = M_win > 0
    tower_mass = M_tow > 0
    if rW_nonzero and tower_mass:
        status = "SURJECTIVE_BOTH_SHELL_AND_TOWER"
    elif rW_nonzero and not tower_mass:
        status = "PURE_SHELL"
    elif not rW_nonzero and tower_mass:
        status = "PURE_TOWER_RELATIVE"
    else:
        status = "VANISHING"

    assert rW_nonzero and status == "SURJECTIVE_BOTH_SHELL_AND_TOWER"

    # Multi-W curve
    Ws = [5, 10, 15, 18, 30, 45, 90, 180, 270, 539]
    curve = []
    for w in Ws:
        I = list(range(min(w - 1, B_prime - 1)))
        Mw = pairing_mass_on_edges(df, I, Q)
        curve.append(
            {
                "W": w,
                "edges": len(I),
                "M_win": Mw,
                "frac": Mw / M_all if M_all else 0.0,
                "target_W_over_B": w / B_prime,
                "rW_nonzero": Mw > 0,
            }
        )
    assert all(row["rW_nonzero"] for row in curve)

    # P+ same-tower triples
    buckets: dict[int, list[int]] = defaultdict(list)
    for i, x in enumerate(O):
        buckets[tower_of(x, loads)].append(i)
    size_mult = Counter(len(v) for v in buckets.values())
    towers_ge3 = sum(1 for v in buckets.values() if len(v) >= 3)
    n_triples = sum(len(list(combinations(v, 3))) for v in buckets.values() if len(v) >= 3)
    assert towers_ge3 == 56 and n_triples == 56
    assert size_mult[3] == 56 and size_mult[2] == 185 and size_mult[1] == 1

    # Window vs tower triple placement
    triples_in_win = 0
    triples_in_tow = 0
    for v in buckets.values():
        if len(v) < 3:
            continue
        for triple in combinations(sorted(v), 3):
            # triple "in window" if all indices < W
            if max(triple) < W:
                triples_in_win += 1
            elif min(triple) >= W - 1:
                triples_in_tow += 1
            else:
                # spans shell boundary
                pass

    results = {
        "provenance": {
            "residual_S_only": True,
            "not_free_Tsharp": True,
            "not_MT_peak_claim": True,
            "kit_order_unchanged": "pair → window → RFC",
            "P_plus_not_auto_locked": True,
        },
        "r_W": {
            "W": W,
            "definition": "r_W != 0 <=> M(I_win) > 0",
            "M_all": M_all,
            "M_win": M_win,
            "M_tow": M_tow,
            "frac_win": M_win / M_all,
            "target_18_over_539": W / B_prime,
            "rW_nonzero": rW_nonzero,
            "tower_mass": tower_mass,
            "status": status,
            "diagnostic": "Shell sees the coupling; tower dominates its mass.",
        },
        "multi_W_curve": curve,
        "P_plus": {
            "status": "counted_not_locked",
            "towers_ge3": towers_ge3,
            "same_tower_unordered_triples": n_triples,
            "size_multiset": {str(k): int(v) for k, v in sorted(size_mult.items())},
            "triples_fully_in_window_i_lt_W": triples_in_win,
            "formula_D_alpha_delta_f": "omega2⊗delta_f - alpha⊗omega_P(delta_f)",
            "omega_P_on_minimal_P": 0,
            "next": "define omega_P Stokes; recompute dim H2(F+)",
        },
        "locks_intact": {
            "option3": True,
            "thin_F_H2": "Q[alpha⊗delta_f]",
            "near_term_kit_order": True,
        },
    }

    out = Path(__file__).resolve().parents[1] / "shell_restriction_rW_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print("OK: r_W(18) != 0 —", status)
    print("OK: M_win,M_tow,M =", M_win, M_tow, M_all)
    print("OK: multi-W all rW!=0; P+ triples =", n_triples, "(not locked)")
    print("wrote", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
