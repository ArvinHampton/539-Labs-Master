#!/usr/bin/env python3
"""
Minimal P+ multi-scale residual research programme (§2.7):

1. Oriented same-tower path 2-cells (56 triples)
2. omega_P(delta_f) by discrete Stokes (two conventions)
3. Recompute D(alpha⊗delta_f) vertical piece + thin-F H2 ranks
4. Report dim H2(F+) proxy and survival of [alpha⊗delta_f]
5. Does NOT auto-lock P+ — research results only

PROVENANCE: residual (S) only. No continuum Cartan. Option 3 / thin F kit intact.
"""
from __future__ import annotations

import json
import math
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

import numpy as np


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


def path_integral(fvals: list[int], i: int, j: int) -> int:
    """Net 0-cochain difference f(j)-f(i) along residual path (i < j)."""
    return int(fvals[j] - fvals[i])


def stokes_path_integrated(fvals: list[int], i: int, j: int, k: int) -> int:
    """dg(i,j,k) with g-hat(a,b)=f(b)-f(a); always 0 for exact f."""
    return (
        path_integral(fvals, i, j)
        + path_integral(fvals, j, k)
        - path_integral(fvals, i, k)
    )


def stokes_chord_zero(df: list[int], i: int, j: int, k: int) -> int:
    """
    Stokes with only 1-skeleton consecutive edges valued; chords 0.
    For consecutive triple (m,m+1,m+2): df[m]+df[m+1].
    For non-consecutive: sum path edges on boundary arcs that are consecutive pairs only.
    """
    # Boundary edges of abstract 2-simplex: (i,j), (j,k), (k,i)
    # Only consecutive path edges contribute.
    total = 0
    if j == i + 1:
        total += df[i]
    if k == j + 1:
        total += df[j]
    # reverse chord (k,i) never consecutive when i<j<k unless degenerate
    return total


def main() -> int:
    N_flux, Q, f_max, B_prime, L_pref, loads = atoms()
    assert B_prime == 539 and L_pref == 18

    residual = list(range(f_max, N_flux))
    O = [residual[i] for i in range(len(residual)) if i % Q == 0][:B_prime]
    fvals = [tower_of(x, loads) for x in O]
    df = [fvals[i + 1] - fvals[i] for i in range(B_prime - 1)]

    def alpha(a, b):
        return sgn(a - b)

    def omega2(a, b, c):
        return alpha(b, c) - alpha(a, c) + alpha(a, b)

    # --- 1. Oriented same-tower 2-cells ---
    buckets: dict[int, list[int]] = defaultdict(list)
    for i, x in enumerate(O):
        buckets[tower_of(x, loads)].append(i)

    triples: list[tuple[int, int, int]] = []
    for v in buckets.values():
        if len(v) >= 3:
            for t in combinations(sorted(v), 3):
                triples.append(t)
    assert len(triples) == 56
    size_mult = Counter(len(v) for v in buckets.values())
    assert size_mult[3] == 56

    W = L_pref
    in_win = sum(1 for i, j, k in triples if k < W)
    in_tow = sum(1 for i, j, k in triples if i >= W - 1)
    straddling = 56 - in_win - in_tow
    consecutive = sum(1 for i, j, k in triples if j == i + 1 and k == j + 1)

    # --- 2. omega_P(delta_f) by Stokes ---
    omega_pi = [stokes_path_integrated(fvals, i, j, k) for i, j, k in triples]
    omega_cz = [stokes_chord_zero(df, i, j, k) for i, j, k in triples]
    assert all(x == 0 for x in omega_pi)
    assert all(x == 0 for x in omega_cz)
    omega_P_norm_pi = float(np.linalg.norm(omega_pi))
    omega_P_norm_cz = float(np.linalg.norm(omega_cz))

    # Non-exact test 1-cochain on path edges: g_i = 1 + (i % 3)
    g_test = [1 + (i % 3) for i in range(B_prime - 1)]
    # cumulative for path-integrated Stokes of arbitrary g
    cum = [0]
    for gi in g_test:
        cum.append(cum[-1] + gi)

    def stokes_g_pi(i, j, k):
        return (cum[j] - cum[i]) + (cum[k] - cum[j]) - (cum[k] - cum[i])

    omega_g_pi = [stokes_g_pi(i, j, k) for i, j, k in triples]
    omega_g_cz = [stokes_chord_zero(g_test, i, j, k) for i, j, k in triples]
    # path-integrated of ANY g is exact → Stokes 0
    assert all(x == 0 for x in omega_g_pi)
    # chord-zero can be nonzero when consecutive edges carry g
    n_g_cz_nonzero = sum(1 for x in omega_g_cz if x != 0)

    # --- 3–4. D(alpha⊗delta_f) and thin-F H2 ranks (F vs F+) ---
    # Minimal P: D(alpha⊗df) has triangle part omega2⊗df (bidegree bookkeeping)
    # and vertical alpha⊗omega_P; omega_P=0 ⇒ no new vertical 3-piece.
    tri_cells = []
    for i in [0, 50, 200, 400, 538]:
        for a, b, c in combinations(range(9), 3):
            tri_cells.append((a, b, c, i))
    sq_cells = []
    for i in range(0, B_prime - 1, 11):
        for a, b in combinations(range(9), 2):
            sq_cells.append((a, b, i))
    n2 = len(tri_cells) + len(sq_cells)

    def eval_f2(name: str) -> np.ndarray:
        v = np.zeros(n2)
        for k, (a, b, c, i) in enumerate(tri_cells):
            if name == "t_w":
                v[k] = omega2(a, b, c)
            elif name == "t_wf":
                v[k] = omega2(a, b, c) * fvals[i]
            elif name == "s_ad":
                v[k] = 0.0
        off = len(tri_cells)
        for k, (a, b, i) in enumerate(sq_cells):
            if name == "s_ad":
                v[off + k] = alpha(a, b) * df[i]
            else:
                v[off + k] = 0.0
        return v

    t_w = eval_f2("t_w")
    s_ad = eval_f2("s_ad")
    t_wf = eval_f2("t_wf")
    eta = s_ad - t_wf
    im = np.column_stack([t_w, eta])
    F2 = np.column_stack([t_w, s_ad, t_wf])
    rank_F2 = int(np.linalg.matrix_rank(F2, tol=1e-8))
    rank_im = int(np.linalg.matrix_rank(im, tol=1e-8))
    assert rank_F2 == 3 and rank_im == 2
    dim_H2_thin = rank_F2 - rank_im  # 1

    # s_ad not in im ⇒ permanent class survives (same as minimal F)
    coef, *_ = np.linalg.lstsq(im, s_ad, rcond=None)
    resid_norm = float(np.linalg.norm(s_ad - im @ coef))
    assert resid_norm > 1.0
    permanent_survives = True

    # F+ vertical 3-cells: charge edge × path triangle; values alpha(a,b)*omega_P(triple)
    # With omega_P(df)=0 both conventions → all zeros → closedness of s_ad not spoiled.
    n_vert = Q * (Q - 1) // 2 * len(triples)
    vert_pi = np.zeros(n_vert)
    vert_cz = np.zeros(n_vert)
    idx = 0
    for ti, (i, j, k) in enumerate(triples):
        op_pi = omega_pi[ti]
        op_cz = omega_cz[ti]
        for a, b in combinations(range(Q), 2):
            vert_pi[idx] = alpha(a, b) * op_pi
            vert_cz[idx] = alpha(a, b) * op_cz
            idx += 1
    assert np.allclose(vert_pi, 0) and np.allclose(vert_cz, 0)

    # Path H2 proxy: if d_P from path-integrated C1 vanishes on 2-cells,
    # then C2 / im d_P has rank = n_triples (formal free path 2-cocycles).
    path_H2_proxy_dim = len(triples)  # 56 under path-integral convention
    # Chord-zero d_P image rank from free edge 1-cochains on consecutive edges only
    # Map R^{B'-1} → R^{56}: each triple gets sum of its consecutive edge contribs
    A = np.zeros((len(triples), B_prime - 1))
    for t_idx, (i, j, k) in enumerate(triples):
        if j == i + 1:
            A[t_idx, i] = 1.0
        if k == j + 1:
            A[t_idx, j] = 1.0
    rank_dP_cz = int(np.linalg.matrix_rank(A, tol=1e-10))
    path_H2_cz_proxy = len(triples) - rank_dP_cz

    # Shell r_W unchanged (1-skeleton pairings)
    M_win = (Q * (Q - 1) // 2) * sum(abs(df[i]) for i in range(W - 1))
    rW_still = M_win > 0

    results = {
        "provenance": {
            "residual_S_only": True,
            "not_free_Tsharp": True,
            "no_continuum_Cartan": True,
            "P_plus_auto_locked": False,
            "option3_intact": True,
            "thin_F_kit_intact": True,
            "programme": "Shell_Restriction §2.7 minimal P+ research",
        },
        "construction": {
            "same_tower_unordered_triples": len(triples),
            "towers_ge3": 56,
            "size_multiset": {str(k): int(v) for k, v in sorted(size_mult.items())},
            "consecutive_index_triples": consecutive,
            "triples_fully_in_window_k_lt_W": in_win,
            "triples_fully_in_tower_i_ge_W_minus_1": in_tow,
            "triples_straddling_shell": straddling,
            "W": W,
            "sample_triples": [list(t) for t in triples[:5]],
        },
        "omega_P_delta_f": {
            "convention_path_integrated_Stokes": {
                "definition": "g-hat(a,b)=f(b)-f(a); dg=gij+gjk-gik",
                "all_zero": True,
                "L2_norm": omega_P_norm_pi,
            },
            "convention_chord_zero_Stokes": {
                "definition": "only consecutive 1-skeleton edges; chords 0",
                "all_zero": True,
                "L2_norm": omega_P_norm_cz,
                "reason": "all 56 triples are same-tower; consecutive df=0 on their edges",
            },
            "nonexact_test_g_i_equals_1_plus_i_mod_3": {
                "path_integrated_all_zero": True,
                "chord_zero_n_nonzero_triples": n_g_cz_nonzero,
                "chord_zero_L2": float(np.linalg.norm(omega_g_cz)),
                "note": "path-integral Stokes of any path 1-cochain vanishes (exact); chord-zero can act",
            },
        },
        "D_alpha_tensor_delta_f": {
            "formula": "omega2⊗delta_f - alpha⊗omega_P(delta_f)",
            "vertical_alpha_omega_P_path_integrated": "zero_vector",
            "vertical_alpha_omega_P_chord_zero": "zero_vector",
            "closedness_spoiled_by_P_plus": False,
            "minimal_P_omega_P": 0,
        },
        "H2_F_plus": {
            "thin_F2_rank": rank_F2,
            "thin_im_D1_rank": rank_im,
            "dim_H2_thin_proxy": dim_H2_thin,
            "permanent_class_survives": permanent_survives,
            "s_ad_residual_from_im": resid_norm,
            "path_H2_proxy_path_integrated": {
                "dim": path_H2_proxy_dim,
                "meaning": "formal free path 2-cocycles if d_P from path-integrated C1 is 0",
            },
            "path_H2_proxy_chord_zero": {
                "rank_im_dP": rank_dP_cz,
                "dim_coker_proxy": path_H2_cz_proxy,
            },
            "design_target_1_preserve_mixed_class": True,
            "design_target_2_secondary_path_2_room": path_H2_proxy_dim > 0 or path_H2_cz_proxy > 0,
            "status": "RESEARCH_STABLE_PERMANENT_CLASS_NOT_LOCKED",
        },
        "r_W_interaction": {
            "rW_nonzero_unchanged": rW_still,
            "M_win": M_win,
            "heuristic": "P+ is tower multi-scale; shell 1-skeleton pairings unchanged",
        },
        "lock_decision": {
            "auto_lock": False,
            "reason": (
                "Permanent class survives and omega_P(delta_f)=0 under residual geometry; "
                "path-2 secondary classes are convention-dependent proxies only. "
                "Keep as optional residual R&D; do not promote 56 to packaging integer."
            ),
            "optional_lock_candidate": "Residual_P_plus_MultiScale.md (research, not theorem lock)",
        },
    }

    out = Path(__file__).resolve().parents[1] / "residual_p_plus_multiscale_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print("OK: P+ triples =", len(triples), "consecutive =", consecutive)
    print("OK: omega_P(delta_f)=0 (path-int & chord-zero); permanent class SURVIVES")
    print("OK: dim H2 thin proxy =", dim_H2_thin, "; path H2 proxy =", path_H2_proxy_dim)
    print("OK: NOT auto-locked — research stable only")
    print("wrote", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
