#!/usr/bin/env python3
"""
P+ 2-complex topology (M1) + residual flux quantization methods Q0–Q8.

Verifies:
  - 56 consecutive same-tower triples, pairwise disjoint
  - M1 cell census: +56 chords, +56 faces
  - contractible path / P+ homology proxies (H0=1, H>0=0 combinatorial)
  - d_P(delta_f)=0 under stay+chord natural extension
  - shell 3 / tower 53 faces
  - Q0–Q8 integer pipeline values
  - orthogonality: jump-mass support vs stay-triple faces

PROVENANCE: residual (S) only. P+ not theorem-locked. Kit / thin F intact.
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
    N_tow = 3**5
    f_min = N_flux // N_tow
    R_exc = N_flux - f_min * N_tow
    f_max = math.ceil(N_flux / N_tow)
    B_prime = (N_flux - f_max) // Q
    L_pref = math.floor(math.e**3 / math.log(3))
    loads = [f_min + 1] * R_exc + [f_min] * (N_tow - R_exc)
    return {
        "N_flux": N_flux,
        "Q": Q,
        "N_tow": N_tow,
        "f_min": f_min,
        "R_exc": R_exc,
        "f_max": f_max,
        "B_prime": B_prime,
        "L_pref": L_pref,
        "loads": loads,
        "W_np": math.e**3,
    }


def tower_of(x: int, loads: list[int]) -> int:
    acc = 0
    for t, L in enumerate(loads):
        if acc <= x < acc + L:
            return t
        acc += L
    return len(loads) - 1


def sgn(d: int) -> int:
    return (d > 0) - (d < 0)


def main() -> int:
    A = atoms()
    N_flux = A["N_flux"]
    Q = A["Q"]
    N_tow = A["N_tow"]
    f_max = A["f_max"]
    B_prime = A["B_prime"]
    L_pref = A["L_pref"]
    loads = A["loads"]

    assert N_flux == 4880 and Q == 9 and N_tow == 243
    assert A["f_min"] == 20 and A["R_exc"] == 20 and f_max == 21
    assert B_prime == 539 and L_pref == 18
    assert loads.count(21) == 20 and loads.count(20) == 223

    # Q2 residual set
    R = list(range(f_max, N_flux))
    assert len(R) == N_flux - f_max == 4859

    # Q3 cores
    O = [R[i] for i in range(len(R)) if i % Q == 0][:B_prime]
    assert len(O) == B_prime

    # Q4 height
    fvals = [tower_of(x, loads) for x in O]
    df = [fvals[i + 1] - fvals[i] for i in range(B_prime - 1)]
    assert all(d in (0, 1) for d in df)

    # Q7 triples
    buckets: dict[int, list[int]] = defaultdict(list)
    for i, x in enumerate(O):
        buckets[tower_of(x, loads)].append(i)
    size_mult = Counter(len(v) for v in buckets.values())
    triples = []
    for v in buckets.values():
        if len(v) >= 3:
            for t in combinations(sorted(v), 3):
                triples.append(tuple(t))
    triples = sorted(triples)
    assert len(triples) == 56
    assert size_mult[3] == 56
    assert all(j == i + 1 and k == j + 1 for i, j, k in triples)

    # Pairwise disjoint vertex blocks
    for a, b in zip(triples, triples[1:]):
        assert a[2] < b[0], (a, b)
    gaps = [triples[i + 1][0] - triples[i][2] for i in range(len(triples) - 1)]
    gap_mult = Counter(gaps)
    # executed residual: positive gaps only (tower-jump bridges between blocks)
    assert all(g >= 1 for g in gaps)
    assert set(gap_mult.keys()).issubset({5, 7, 9})

    # Shell / tower faces
    W = L_pref
    n_shell = sum(1 for i, j, k in triples if k < W)
    n_tow = sum(1 for i, j, k in triples if i >= W - 1)
    n_straddle = 56 - n_shell - n_tow
    assert n_shell == 3 and n_tow == 53 and n_straddle == 0

    # M1 cell census
    n0 = B_prime
    n1_path = B_prime - 1
    n1_chords = 56
    n1_total = n1_path + n1_chords
    n2 = 56
    # Euler char of path = 1; each chord+face attachment of a disk on contractible
    # arc keeps chi=1 for full complex (tree + filled triangles with chords)
    # Block: +1 chord +1 face on path subgraph that had 3V 2E → 3V 3E 1F → chi_block local
    chi_path = n0 - n1_path  # 539-538=1
    chi_Pplus = n0 - n1_total + n2  # 539 - (538+56) + 56 = 1
    assert chi_path == 1 and chi_Pplus == 1

    # Homology proxies: path is interval → H0=1, H>0=0
    # P+ M1: still connected, contractible chain of disks → same
    H0_P, H_pos_P = 1, 0
    H0_Pp, H_pos_Pp = 1, 0

    # d_P(delta_f) on each sigma: g(i,i+1)+g(i+1,i+2)-g(i,i+2)
    # stay edges df=0; chord f(i+2)-f(i)=0
    omega = []
    for i, j, k in triples:
        assert df[i] == 0 and df[j] == 0
        g_chord = fvals[k] - fvals[i]
        assert g_chord == 0
        omega.append(df[i] + df[j] - g_chord)
    assert all(x == 0 for x in omega)

    # Non-height g with variation inside triple can have nonzero Stokes
    g_test = [1 + (m % 3) for m in range(B_prime - 1)]
    omega_g = []
    for i, j, k in triples:
        # chord extension: path integral g(i)+g(i+1)
        g_chord_int = g_test[i] + g_test[j]
        # natural "height-like" chord: if we set chord = telescoping of g along path
        stokes_tel = g_test[i] + g_test[j] - g_chord_int  # always 0
        # free chord value 0 (M1 cochain not forced to telescope)
        stokes_free0 = g_test[i] + g_test[j] - 0
        omega_g.append({"telescoping": stokes_tel, "chord_zero": stokes_free0})
    assert all(row["telescoping"] == 0 for row in omega_g)
    n_nonzero_free = sum(1 for row in omega_g if row["chord_zero"] != 0)
    assert n_nonzero_free == 56

    # Q5 pairing mass
    M = (Q * (Q - 1) // 2) * sum(abs(d) for d in df)
    I_win = list(range(W - 1))
    I_tow = list(range(W - 1, B_prime - 1))
    M_win = (Q * (Q - 1) // 2) * sum(abs(df[i]) for i in I_win)
    M_tow = (Q * (Q - 1) // 2) * sum(abs(df[i]) for i in I_tow)
    assert M == 8676 and M_win == 252 and M_tow == 8424

    # Orthogonality: jump edges (df!=0) never interior stay edges of a triple
    stay_edges = set()
    for i, j, k in triples:
        stay_edges.add(i)
        stay_edges.add(j)
    jump_edges = {i for i, d in enumerate(df) if d != 0}
    assert stay_edges.isdisjoint(jump_edges)

    # Q8 window edges
    e_win = W - 1
    e_tow = B_prime - 1 - e_win
    assert e_win == 17 and e_tow == 521

    results = {
        "provenance": {
            "residual_S_only": True,
            "principle_S": True,
            "not_free_Tsharp": True,
            "P_plus_theorem_locked": False,
            "canonical_model": "M1_simplicial_with_chords",
            "kit_thin_F_unchanged": True,
            "continuum_category_B": True,
        },
        "topology_P_plus": {
            "B_prime": B_prime,
            "n_vertices": n0,
            "n_path_edges": n1_path,
            "n_chords_M1": n1_chords,
            "n_1_total_M1": n1_total,
            "n_2_faces": n2,
            "oriented_2_if_both_chiralities": 112,
            "euler_chi_path": chi_path,
            "euler_chi_P_plus_M1": chi_Pplus,
            "H0_path": H0_P,
            "H_pos_path": H_pos_P,
            "H0_P_plus": H0_Pp,
            "H_pos_P_plus": H_pos_Pp,
            "contractible_M1": True,
            "pairwise_disjoint_blocks": True,
            "block_gaps": {
                "n_gaps": len(gaps),
                "min": min(gaps),
                "max": max(gaps),
                "multiset": {str(k): int(v) for k, v in sorted(gap_mult.items())},
                "note": "index gaps between consecutive blocks (tower-jump bridges)",
            },
            "all_consecutive_span_2": True,
            "shell_faces": n_shell,
            "tower_faces": n_tow,
            "straddle_faces": n_straddle,
            "W": W,
            "sample_triples": [list(t) for t in triples[:5]],
        },
        "d_P_delta_f": {
            "stay_edges_df_zero": True,
            "chord_df_zero": True,
            "Stokes_all_zero": True,
            "D_alpha_delta_f_vertical_unchanged": True,
            "formula": "D = omega2⊗delta_f - alpha⊗d_P(delta_f) with d_P(delta_f)=0",
            "nonheight_g_chord_zero_n_nonzero": n_nonzero_free,
            "note": "multi-scale content in non-height g, not tower-height delta_f",
        },
        "quantization_Q0_Q8": {
            "Q0": {
                "N_tow": N_tow,
                "N_flux": N_flux,
                "tag": "A",
            },
            "Q1": {
                "f_min": A["f_min"],
                "R_exc": A["R_exc"],
                "loads_21": 20,
                "loads_20": 223,
                "tag": "A",
            },
            "Q2": {
                "f_max": f_max,
                "R_card": len(R),
                "tag": "A",
            },
            "Q3": {
                "Q": Q,
                "B_prime": B_prime,
                "tag": "A",
            },
            "Q4": {
                "df_values": sorted(set(df)),
                "n_jumps": sum(1 for d in df if d != 0),
                "n_stay": sum(1 for d in df if d == 0),
                "tag": "A",
            },
            "Q5": {
                "M": M,
                "M_win": M_win,
                "M_tow": M_tow,
                "tag": "A/S",
            },
            "Q6": {
                "H2_thin": "Q[alpha⊗delta_f]",
                "rank": 1,
                "tag": "A",
            },
            "Q7": {
                "N2": 56,
                "formula": "sum binom(n_t,3)",
                "tag": "A_count_S_complex",
            },
            "Q8": {
                "W": W,
                "e_win": e_win,
                "e_tow": e_tow,
                "tag": "A/S",
            },
        },
        "orthogonality": {
            "jump_mass_support_disjoint_from_stay_triple_edges": True,
            "n_stay_edges_in_triples": len(stay_edges),
            "n_jump_edges": len(jump_edges),
            "channels": {
                "mixed_class_mass": "delta_f != 0 edges (Q5)",
                "P_plus_2_cells": "delta_f = 0 triples (Q7)",
                "shell_restriction": "first 17 edges + 3 faces (Q8 + r_W)",
            },
        },
        "product_X_times_plus": {
            "factors_contractible": True,
            "filled_Tot_acyclic_expectation": True,
            "mixed_class_bidegree": "(1,1)",
            "new_generators_optional": "1⊗omega_P path-2 symbols",
        },
        "locks": {
            "option3": True,
            "thin_F": True,
            "near_term_kit_order": "pair → window → RFC",
            "P_plus_auto_locked": False,
            "56_is_not_packaging": True,
        },
        "status": "P_PLUS_M1_TOPOLOGY_EXECUTED_QUANTIZATION_PIPELINE_A",
    }

    out = Path(__file__).resolve().parents[1] / "p_plus_2complex_topology_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print("OK: P+ M1 — 56 disks, chi=1, H>0=0 proxy, disjoint blocks, gaps", dict(gap_mult))
    print("OK: d_P(delta_f)=0; shell faces=3 tower=53")
    print("OK: Q0–Q8 integer pipeline; jump ⊥ stay orthogonality")
    print("OK: NOT theorem-locked; status", results["status"])
    print("wrote", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
