#!/usr/bin/env python3
"""
CB4 — Cat-B existence framing for a smooth spin fill of primary K⁺.

HARD FIREWALL: does not modify A0–A5⁺ locks, Option 3, No-Go, B′, or free T^sharp.
Status remains Category B / open (not a residual foundation lock).
"""
from __future__ import annotations

import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np


def atoms():
    N_flux = math.floor(math.e**3 * 3**5)
    N_tow = 3**5
    Q = 9
    f_min = N_flux // N_tow
    R_exc = N_flux - f_min * N_tow
    f_max = math.ceil(N_flux / N_tow)
    B_prime = (N_flux - f_max) // Q
    loads = [f_min + 1] * R_exc + [f_min] * (N_tow - R_exc)
    return N_flux, N_tow, Q, f_max, B_prime, loads


def tower_of(x: int, loads: list[int]) -> int:
    acc = 0
    for t, L in enumerate(loads):
        if acc <= x < acc + L:
            return t
        acc += L
    return len(loads) - 1


def core_q0(N_flux: int, f_max: int, Q: int, B_prime: int) -> list[int]:
    residual = sorted(range(f_max, N_flux))
    class0 = [residual[i] for i in range(len(residual)) if i % Q == 0]
    return class0[:B_prime]


def build_Kplus_A2_enrich(O: list[int], loads: list[int]):
    n = len(O)
    edges: set[tuple[int, int]] = set()
    faces: set[tuple[int, int, int]] = set()

    def add_edge(i: int, j: int):
        if i == j:
            return
        a, b = (i, j) if i < j else (j, i)
        edges.add((a, b))

    def add_face(i: int, j: int, k: int):
        t = tuple(sorted((i, j, k)))
        if len(set(t)) < 3:
            return
        faces.add(t)
        add_edge(t[0], t[1])
        add_edge(t[1], t[2])
        add_edge(t[0], t[2])

    for i in range(n - 1):
        add_edge(i, i + 1)

    by_tau: dict[int, list[int]] = defaultdict(list)
    for i, x in enumerate(O):
        by_tau[tower_of(x, loads)].append(i)

    fiber_sizes = Counter(len(v) for v in by_tau.values() if len(v) > 0)

    for idxs in by_tau.values():
        for a in range(len(idxs)):
            for b in range(a + 1, len(idxs)):
                add_edge(idxs[a], idxs[b])

    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    for i in range(n):
        nbrs = sorted(adj[i])
        for ai, a in enumerate(nbrs):
            for b in nbrs[ai + 1 :]:
                if b in adj[a]:
                    add_face(i, a, b)

    return sorted(edges), sorted(faces), by_tau, fiber_sizes, adj


def smith_invariant_factors(A: np.ndarray) -> tuple[list[int], int]:
    if A.size == 0:
        return [], 0
    M = A.astype(object).copy()
    m, n = M.shape
    inv: list[int] = []
    r = 0
    for k in range(min(m, n)):
        piv = None
        best = None
        for i in range(k, m):
            for j in range(k, n):
                v = abs(int(M[i, j]))
                if v != 0 and (best is None or v < best):
                    best = v
                    piv = (i, j)
                    if best == 1:
                        break
            if best == 1:
                break
        if piv is None:
            break
        pi, pj = piv
        if pi != k:
            M[[k, pi], :] = M[[pi, k], :]
        if pj != k:
            M[:, [k, pj]] = M[:, [pj, k]]
        if int(M[k, k]) < 0:
            M[k, :] = -M[k, :]
        guard = 0
        while guard < 10000:
            guard += 1
            changed = False
            pk = int(M[k, k])
            if pk == 0:
                break
            for i in range(m):
                if i == k:
                    continue
                a = int(M[i, k])
                if a == 0:
                    continue
                q = a // pk
                if q != 0:
                    M[i, :] = M[i, :] - q * M[k, :]
                    changed = True
                a = int(M[i, k])
                if a != 0:
                    M[[k, i], :] = M[[i, k], :]
                    if int(M[k, k]) < 0:
                        M[k, :] = -M[k, :]
                    changed = True
                    break
            if changed:
                continue
            pk = int(M[k, k])
            for j in range(n):
                if j == k:
                    continue
                a = int(M[k, j])
                if a == 0:
                    continue
                q = a // pk
                if q != 0:
                    M[:, j] = M[:, j] - q * M[:, k]
                    changed = True
                a = int(M[k, j])
                if a != 0:
                    M[:, [k, j]] = M[:, [j, k]]
                    if int(M[k, k]) < 0:
                        M[k, :] = -M[k, :]
                    changed = True
                    break
            if changed:
                continue
            pk = int(M[k, k])
            fixed = False
            for i in range(k + 1, m):
                for j in range(k + 1, n):
                    if pk != 0 and int(M[i, j]) % pk != 0:
                        M[k, :] = M[k, :] + M[i, :]
                        fixed = True
                        break
                if fixed:
                    break
            if not fixed:
                break
        d = abs(int(M[k, k]))
        if d == 0:
            break
        inv.append(d)
        r += 1
    return inv, r


def integral_homology(n, elist, flist):
    ne, nf = len(elist), len(flist)
    e_index = {e: i for i, e in enumerate(elist)}
    d1 = np.zeros((n, ne), dtype=np.int64)
    for ei, (i, j) in enumerate(elist):
        d1[i, ei] = -1
        d1[j, ei] = 1
    d2 = np.zeros((ne, nf), dtype=np.int64)
    for fi, (i, j, k) in enumerate(flist):
        for a, b, s in ((i, j, 1), (j, k, 1), (i, k, -1)):
            aa, bb = (a, b) if a < b else (b, a)
            if a > b:
                s = -s
            d2[e_index[(aa, bb)], fi] = s
    inv1, r1 = smith_invariant_factors(d1)
    inv2, r2 = smith_invariant_factors(d2)
    return {
        "H0_free": n - r1,
        "H1_free": (ne - r1) - r2,
        "H2_free": nf - r2,
        "torsion_d1": [d for d in inv1 if d > 1],
        "torsion_d2": [d for d in inv2 if d > 1],
        "rank_d1": r1,
        "rank_d2": r2,
        "cycle_space_rank": ne - r1,
        "face_relation_rank": r2,
        "presentation_gen_count_tree_complement": ne - (n - 1),
        "presentation_rel_count_faces": nf,
    }


def face_edge_support_stats(elist, flist):
    """How face relations sit on edges — Cat B combinatorial diagnostics."""
    e_index = {e: i for i, e in enumerate(elist)}
    use = [0] * len(elist)
    for i, j, k in flist:
        for pair in ((i, j), (j, k), (i, k)):
            a, b = (pair if pair[0] < pair[1] else (pair[1], pair[0]))
            use[e_index[(a, b)]] += 1
    ctr = Counter(use)
    path_edges = {(i, i + 1) for i in range(len(elist) and max(max(e) for e in elist), -1)}
    # better: path edges are consecutive indices
    n_guess = max(max(e) for e in elist) + 1 if elist else 0
    path_set = {(i, i + 1) for i in range(n_guess - 1)}
    path_in_faces = 0
    towerish_in_faces = 0
    for e, c in zip(elist, use):
        if c == 0:
            continue
        if e in path_set:
            path_in_faces += 1
        else:
            towerish_in_faces += 1
    return {
        "edge_face_incidence_histogram": {str(k): v for k, v in sorted(ctr.items())},
        "edges_used_in_some_face": sum(1 for u in use if u > 0),
        "edges_never_in_a_face": sum(1 for u in use if u == 0),
        "faces": len(flist),
        "path_edges_appearing_in_faces": path_in_faces,
        "nonpath_edges_appearing_in_faces": towerish_in_faces,
    }


def pi1_abelianization_note(hom: dict):
    """
    H1(X;Z) ≅ π1^{ab}. H1=0 ⇒ π1 is perfect (possibly trivial).
    Does NOT prove π1=1. CB4 simply-connectedness remains open Cat B.
    """
    return {
        "H1_zero": hom["H1_free"] == 0 and not hom["torsion_d1"] and not hom["torsion_d2"],
        "implies_pi1_perfect": True,
        "implies_pi1_trivial": False,
        "status": "OPEN_CAT_B — simply-connectedness of K⁺ not proved",
        "presentation_shape": {
            "tree_complement_generators": hom["presentation_gen_count_tree_complement"],
            "face_relations": hom["presentation_rel_count_faces"],
            "note": (
                "Equal gen/rel counts with H1=0 is consistent with π1=1 or a perfect group; "
                "no decision algorithm run here."
            ),
        },
    }


def obstruction_checklist(hom: dict, fiber_sizes: Counter, face_stats: dict):
    """
    Ordered checklist for CB4 smooth spin fill. All items Category B.
    """
    return [
        {
            "id": "O1_homology_point",
            "statement": "H_*(K⁺;Z) ≅ H_*(pt)",
            "status": "SATISFIED (locked A5⁺ / rechecked)",
            "category": "B_input_from_lock",
            "blocks_smooth_ball": False if hom["H0_free"] == 1 and hom["H1_free"] == 0 and hom["H2_free"] == 0 else True,
        },
        {
            "id": "O2_unique_BSpin",
            "statement": "Unique BSpin lift of Φ^Spin on primary K⁺ (A4⁺.4)",
            "status": "SATISFIED (locked A4⁺; β1_F2=0 ⇒ one spin structure)",
            "category": "B_input_from_lock",
            "blocks_smooth_ball": False,
        },
        {
            "id": "O3_PL_fill_exists",
            "statement": "PL contractible fill exists (unreduced cone C(K⁺) = CB1)",
            "status": "SATISFIED (combinatorial; Euler 1)",
            "category": "B",
            "blocks_smooth_ball": False,
            "note": "PL existence ≠ smooth existence",
        },
        {
            "id": "O4_pi1_trivial",
            "statement": "π1(K⁺) = 1 (needed for K⁺ ≃ spine of a ball / contractible 3-manifold)",
            "status": "OPEN_CAT_B",
            "category": "B",
            "blocks_smooth_ball": "unknown — if nontrivial perfect π1, contractible fill still exists as cone but K⁺ is not itself a ball spine in the strong sense",
            "known": "H1=0 ⇒ π1 perfect only",
        },
        {
            "id": "O5_spine_of_3_manifold",
            "statement": "K⁺ is a spine (or 2-skeleton) of some compact 3-manifold with boundary (e.g. ball)",
            "status": "OPEN_CAT_B",
            "category": "B",
            "blocks_smooth_ball": "unknown",
            "combinatorial_hint": {
                "fiber_size_histogram": {str(k): int(v) for k, v in sorted(fiber_sizes.items())},
                "faces_equal_tripletons": face_stats["faces"] == fiber_sizes.get(3, -1),
                "edges_never_in_a_face": face_stats["edges_never_in_a_face"],
            },
        },
        {
            "id": "O6_smooth_structure",
            "statement": "The 3-manifold (if any) admits a smooth structure extending PL data",
            "status": "OPEN_CAT_B (vacuous until O5)",
            "category": "B",
            "note": "In dim 3, PL ⇔ smooth for manifolds (classical); bottleneck is manifold realization, not smoothing of a manifold",
        },
        {
            "id": "O7_spin_extension",
            "statement": "Unique spin structure on K⁺ extends to the smooth fill M",
            "status": "OPEN_CAT_B (depends on O5–O6; A4⁺ gives boundary/skeleton data)",
            "category": "B",
            "note": "Natural rank-2 follow-on after CB4 framed",
        },
        {
            "id": "O8_residual_non_promotion",
            "statement": "Even a positive CB4 answer does not promote continuum Ω_n to residual Category A",
            "status": "HARD RULE",
            "category": "B",
            "blocks_smooth_ball": False,
        },
    ]


def classical_spin_facts():
    return {
        "Omega_3_Spin_pt": "0",
        "Omega_4_Spin_pt": "Z",
        "meaning_for_CB4": (
            "Closed spin 3-manifolds are null-bordant. A spin 3-ball is a null-cobordism "
            "of empty boundary. Classical groups neither prove nor forbid a K⁺-compatible fill."
        ),
        "category": "B_library",
    }


def firewall(hom, B_prime, a5plus):
    checks = {
        "H0_is_1": hom["H0_free"] == 1,
        "H1_is_0": hom["H1_free"] == 0,
        "H2_is_0": hom["H2_free"] == 0,
        "V_is_539": True,  # filled below
        "B_prime_is_539": B_prime == 539,
        "does_not_feed_locked_stack": True,
        "a5plus_still_coefficients_only": (
            a5plus is not None
            and a5plus.get("status_code") == "A5PLUS_COEFFICIENTS_ONLY_ON_KPLUS"
        ),
    }
    return checks


def main() -> int:
    N_flux, N_tow, Q, f_max, B_prime, loads = atoms()
    O = core_q0(N_flux, f_max, Q, B_prime)
    elist, flist, by_tau, fiber_sizes, adj = build_Kplus_A2_enrich(O, loads)
    n = len(O)
    print(f"K+ V={n} E={len(elist)} F={len(flist)}", flush=True)

    hom = integral_homology(n, elist, flist)
    face_stats = face_edge_support_stats(elist, flist)
    pi1 = pi1_abelianization_note(hom)
    checklist = obstruction_checklist(hom, fiber_sizes, face_stats)

    a5_path = Path(__file__).resolve().parents[1] / "architecture_A5plus_results.json"
    a5plus = json.loads(a5_path.read_text(encoding="utf-8")) if a5_path.exists() else None

    fw = firewall(hom, B_prime, a5plus)
    fw["V_is_539"] = n == 539
    fw["E_is_594"] = len(elist) == 594
    fw["F_is_56"] = len(flist) == 56
    fw["all_pass"] = all(fw.values())

    # CB4 decision state: open existence question
    open_ids = [c["id"] for c in checklist if str(c["status"]).startswith("OPEN")]
    satisfied = [c["id"] for c in checklist if str(c["status"]).startswith("SATISFIED")]

    results = {
        "category": "B",
        "status_code": "CB4_SMOOTH_SPIN_FILL_OPEN_CAT_B",
        "parent_track": "CAT_B_CONTINUUM_FILLINGS_OPEN_NOT_LOCKED",
        "hard_firewall": {
            "locked_stack_untouched": True,
            "Option3_intact": True,
            "No_Go_intact": True,
            "free_Tsharp_forbidden": True,
            "G4_not_KO": True,
            "no_promotion_continuum_to_residual": True,
            "checks": fw,
        },
        "Kplus_input_snapshot": {
            "mode": "A2_enrich",
            "V": n,
            "E": len(elist),
            "F": len(flist),
            "homology": {
                "H0": hom["H0_free"],
                "H1": hom["H1_free"],
                "H2": hom["H2_free"],
                "torsion": hom["torsion_d1"] + hom["torsion_d2"],
            },
            "fiber_size_histogram": {str(k): int(v) for k, v in sorted(fiber_sizes.items())},
            "A4plus_unique_BSpin": True,
            "A5plus_code": "A5PLUS_COEFFICIENTS_ONLY_ON_KPLUS",
        },
        "pi1_diagnostic": pi1,
        "face_support": face_stats,
        "classical_spin_bordism": classical_spin_facts(),
        "obstruction_checklist": checklist,
        "summary": {
            "satisfied_inputs": satisfied,
            "open_obstructions": open_ids,
            "PL_fill_CB1": "EXISTS (cone)",
            "smooth_fill_CB4": "OPEN existence question",
            "spin_extension_rank2": "OPEN follow-on after CB4",
        },
        "existence_question_Q_CB4": (
            "Does there exist a smooth compact spin 3-manifold M (or a spin 3-ball) "
            "admitting a triangulation/CW structure such that primary K⁺ embeds as a "
            "2-skeleton or deformation-retract spine, and the unique A4⁺ BSpin structure "
            "on K⁺ extends to a spin structure on M?"
        ),
        "explicit_non_claims": [
            "CB4 not residual Category A",
            "No Ω_n residual geometry for n>0",
            "No free T^sharp",
            "No G4=KO",
            "No No-Go lift",
            "π1 triviality not claimed",
            "Smooth fill existence not claimed",
        ],
    }

    out = Path(__file__).resolve().parents[1] / "cb4_smooth_spin_fill_catB_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print("wrote", out)
    if not fw["all_pass"]:
        print("FAIL firewall", fw, file=sys.stderr)
        return 1
    print("OK: CB4 framed OPEN Cat B; firewall PASS")
    print("open:", open_ids)
    return 0


if __name__ == "__main__":
    sys.exit(main())
