#!/usr/bin/env python3
"""
G-F pairing and packaging-window filtration on residual product cells.

1) Kronecker pairing of alpha⊗delta_f with mixed squares S(a,b;i)
2) Window filtration using W = L_pref = 18 path vertices (17 edges)
3) Simple path-order surrogate: reverse df (destroys forward residual order)

PROVENANCE: residual (S) only. Not empirical biology. Not free T-sharp.
"""
from __future__ import annotations

import json
import math
import sys
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


def pairing_mass(df, Q=9):
    """Sum |alpha(a,b)*df[i]| over a<b and edges i."""
    n_pairs = Q * (Q - 1) // 2  # combinations
    # for a<b, alpha(a,b)=-1 always, so |alpha*df|=|df|
    # over all oriented a!=b would double; we use a<b
    return n_pairs * sum(abs(x) for x in df)


def main() -> int:
    N_flux, Q, f_max, B_prime, L_pref, loads = atoms()
    assert L_pref == 18 and B_prime == 539

    residual = list(range(f_max, N_flux))
    O = [residual[i] for i in range(len(residual)) if i % Q == 0][:B_prime]
    fvals = [tower_of(x, loads) for x in O]
    df = [fvals[i + 1] - fvals[i] for i in range(B_prime - 1)]

    # Full pairing mass
    n_sq = (Q * (Q - 1) // 2) * (B_prime - 1)
    Sigma = pairing_mass(df, Q)
    nonzero = sum(
        1
        for i in range(B_prime - 1)
        for a, b in combinations(range(Q), 2)
        if sgn(a - b) * df[i] != 0
    )
    # a<b => sgn=-1; nonzero when df!=0
    assert nonzero == (Q * (Q - 1) // 2) * sum(1 for x in df if x != 0)

    # Window: 18 vertices => edges i=0..16
    W = L_pref
    n_win_edges = W - 1  # 17
    n_tow_edges = (B_prime - 1) - n_win_edges  # 521
    assert n_tow_edges == 521
    df_win = df[:n_win_edges]
    df_tow = df[n_win_edges:]
    Sigma_win = pairing_mass(df_win, Q)
    Sigma_tow = pairing_mass(df_tow, Q)
    assert Sigma_win + Sigma_tow == Sigma

    ratio = Sigma_win / Sigma if Sigma else None
    target = L_pref / B_prime  # 18/539

    # Graph beta1 (independent G layer)
    V = Q * B_prime
    E = Q * (B_prime - 1) + B_prime * (Q * (Q - 1) // 2)
    beta1 = E - V + 1
    assert beta1 == 36 * B_prime - 8

    # Surrogate: reverse path order of df
    df_rev = list(reversed(df))
    Sigma_rev = pairing_mass(df_rev, Q)
    # same mass (absolute); order-sensitive diagnostic: correlation of df with index
    # use signed sum on a fixed orientation a=0,b=1: sum df
    signed = sum(df)
    signed_rev = sum(df_rev)
    assert signed_rev == signed  # reverse preserves sum
    # order-sensitive: cumulative transport in window vs tower
    cum_win = sum(df_win)
    cum_tow = sum(df_tow)

    # Mixed cycle census (square boundaries): each square gives one mixed 4-cycle
    n_mixed_square_cycles = n_sq

    results = {
        "provenance": {
            "residual_S_only": True,
            "not_free_Tsharp": True,
            "not_empirical_biology": True,
            "not_security_reduction": True,
        },
        "G_F_pairing": {
            "definition": "<alpha⊗delta_f, S(a,b;i)> = alpha(a,b)*delta_f(i)",
            "n_squares_a_lt_b": n_sq,
            "n_nonzero_pairings": nonzero,
            "Sigma_abs_mass": Sigma,
            "formula_Sigma": "C(9,2) * sum|df|",
            "n_mixed_square_cycles": n_mixed_square_cycles,
            "graph_beta1": beta1,
        },
        "window_filtration": {
            "W_L_pref": W,
            "n_window_edges": n_win_edges,
            "n_tower_edges": n_tow_edges,
            "Sigma_win": Sigma_win,
            "Sigma_tow": Sigma_tow,
            "ratio_Sigma_win_over_Sigma": ratio,
            "target_L_pref_over_B_prime": target,
            "sum_df_win": sum(df_win),
            "sum_df_tow": sum(df_tow),
            "sum_abs_df_win": sum(abs(x) for x in df_win),
            "sum_abs_df_tow": sum(abs(x) for x in df_tow),
            "note": "homological shell diagnostic under (S), not MT peak recovery",
        },
        "surrogate_note": {
            "df_reverse_preserves_Sigma_abs": Sigma_rev == Sigma,
            "interpretation": "absolute pairing mass is order-insensitive; window split uses residual order prefix",
        },
        "unification_reading": "preserve mixed class and pairings under refinement — not one PDE",
        "locks_respected": {
            "thin_complex_H2": "Q[alpha⊗delta_f]",
            "option3_free_Tsharp": True,
            "emp_18_521_peaks_not_claimed": True,
            "dictionary_is_cat_B_RFC": True,
        },
        "kit_doc": "Near_Term_Unification_Kit.md",
    }

    out = Path(__file__).resolve().parents[1] / "gf_pairing_window_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print("OK: G-F pairing Sigma =", Sigma, "nonzero cells", nonzero)
    print(
        "OK: window edges",
        n_win_edges,
        "tower edges",
        n_tow_edges,
        "ratio",
        round(ratio, 6),
        "vs target",
        round(target, 6),
    )
    print("wrote", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
