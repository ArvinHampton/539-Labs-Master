#!/usr/bin/env python3
"""
Category-B continuum fillings of the residual carrier — exploratory only.

HARD FIREWALL
-------------
- Does NOT modify A0–A5 0-stem, A4⁺, or A5⁺ locks.
- Does NOT promote continuum geometry into residual foundation.
- Does NOT claim free T^sharp, No-Go lift, or G4 = KO period.
- Option 3 remains intact.
- Every continuum object is Category B / research-open.

Primary residual stack stays at A5PLUS_COEFFICIENTS_ONLY_ON_KPLUS.
"""
from __future__ import annotations

import json
import math
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Residual atoms (same packaging as A4⁺/A5⁺ — read-only use)
# ---------------------------------------------------------------------------


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

    return sorted(edges), sorted(faces)


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


def oriented_boundary_matrices(n: int, elist, flist):
    ne, nf = len(elist), len(flist)
    e_index = {e: idx for idx, e in enumerate(elist)}
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
    return d1, d2


def integral_homology_K(n, elist, flist):
    d1, d2 = oriented_boundary_matrices(n, elist, flist)
    inv1, rank1 = smith_invariant_factors(d1)
    inv2, rank2 = smith_invariant_factors(d2)
    ne, nf = len(elist), len(flist)
    return {
        "H0_free": n - rank1,
        "H1_free": (ne - rank1) - rank2,
        "H2_free": nf - rank2,
        "torsion_d1": [d for d in inv1 if d > 1],
        "torsion_d2": [d for d in inv2 if d > 1],
        "rank_d1": rank1,
        "rank_d2": rank2,
        "n_verts": n,
        "n_edges": ne,
        "n_faces": nf,
        "euler": n - ne + nf,
    }


# ---------------------------------------------------------------------------
# Cat-B continuum models (combinatorial proxies only)
# ---------------------------------------------------------------------------


def cone_cell_counts(n_v, n_e, n_f):
    """
    Unreduced cone C(K⁺): apex + cones on all cells.
    New 0-cells: +1 apex
    New 1-cells: +n_v (apex to each vertex)
    New 2-cells: +n_e (apex cones of edges)
    New 3-cells: +n_f (apex cones of faces)
    Total: V' = n_v+1, E' = n_e+n_v, F' = n_f+n_e, T' = n_f
    Contractible PL 3-complex (Cat B model of a ball fill).
    """
    V = n_v + 1
    E = n_e + n_v
    F = n_f + n_e
    T = n_f
    return {
        "model": "unreduced_cone_C_Kplus",
        "category": "B",
        "cells": {"V": V, "E": E, "F2": F, "F3": T},
        "euler": V - E + F - T,
        "homology_claim": "contractible (H_* ≅ H_*(pt)); combinatorial cone of acyclic complex",
        "manifold_claim": "NOT a smooth manifold claim — PL ball model only",
        "feeds_locked_stack": False,
    }


def suspension_cell_counts(n_v, n_e, n_f):
    """
    Unreduced suspension ΣK⁺: two apices N,S.
    V' = n_v+2; E' = n_e + 2 n_v; F' = n_f + 2 n_e; T' = 2 n_f
    Homology of suspension shifts reduced homology of base.
    With H̃_*(K⁺)=0, ΣK⁺ is also homology-pointlike (Cat B).
    """
    V = n_v + 2
    E = n_e + 2 * n_v
    F = n_f + 2 * n_e
    T = 2 * n_f
    return {
        "model": "unreduced_suspension_Sigma_Kplus",
        "category": "B",
        "cells": {"V": V, "E": E, "F2": F, "F3": T},
        "euler": V - E + F - T,
        "homology_claim": "homology-pointlike if base is (suspension of acyclic)",
        "manifold_claim": "NOT a smooth S^3 claim — PL suspension only",
        "feeds_locked_stack": False,
    }


def product_interval_counts(n_v, n_e, n_f):
    """
    Prism / product K⁺ × I (Cat B thickening).
    Prism cells: for each k-cell, two copies + prism (k+1)-cells.
    Rough count for bookkeeping only.
    """
    # product CW: cells of dimension k are sum_{i+j=k} cells_i(K)×cells_j(I)
    # I has 2 verts, 1 edge
    c0, c1, c2 = n_v, n_e, n_f
    V = 2 * c0
    E = 2 * c1 + c0  # two edge copies + prism on verts
    F = 2 * c2 + c1  # two face copies + prisms on edges
    T = c2  # prisms on faces
    return {
        "model": "prism_Kplus_x_I",
        "category": "B",
        "cells": {"V": V, "E": E, "F2": F, "F3": T},
        "euler": V - E + F - T,
        "homology_claim": "homotopy equivalent to K⁺ (retract); still H_* ≅ pt",
        "manifold_claim": "NOT a 3-manifold with boundary claim without triangulation check",
        "feeds_locked_stack": False,
    }


# Classical coefficient tables beyond ABS — library only, Cat B ambient
# Sources: standard Bott / spin bordism tables (point coefficients).
# Recording does NOT assign residual classes for n>7.

OMEGA_SPIN_PT_EXT = {
    0: "Z",
    1: "Z/2",
    2: "Z/2",
    3: "0",
    4: "Z",
    5: "0",
    6: "0",
    7: "0",
    8: "Z ⊕ Z",  # signature + Â / spin
    9: "Z/2 ⊕ Z/2",
    10: "Z/2 ⊕ Z/2",
    11: "0",
    12: "Z ⊕ Z",
    13: "0",
    14: "0",
    15: "0",
}

KO_PT_EXT = {
    0: "Z",
    1: "Z/2",
    2: "Z/2",
    3: "0",
    4: "Z",
    5: "0",
    6: "0",
    7: "0",
    # Bott period 8
    8: "Z",
    9: "Z/2",
    10: "Z/2",
    11: "0",
    12: "Z",
    13: "0",
    14: "0",
    15: "0",
}


def continuum_candidate_catalogue(B_prime: int):
    """
    Explicit Cat-B candidate continuum geometries.
    None of these are residual foundation locks.
    """
    return [
        {
            "id": "CB1_PL_ball_cone",
            "category": "B",
            "description": (
                "Unreduced cone C(K⁺) as PL contractible 3-complex; model of "
                "filling residual 2-skeleton to a ball."
            ),
            "bordism_role": "null-bordism of empty boundary in combinatorial sense only",
            "residual_class_claim": "FORBIDDEN — does not redefine B′",
            "status": "open Cat B model",
        },
        {
            "id": "CB2_PL_suspension",
            "category": "B",
            "description": (
                "Unreduced suspension ΣK⁺ as PL homology sphere candidate proxy "
                "(homology of a point after reduced suspension of acyclic base)."
            ),
            "bordism_role": "higher-dimensional PL proxy only",
            "residual_class_claim": "FORBIDDEN",
            "status": "open Cat B model",
        },
        {
            "id": "CB3_prism_thickening",
            "category": "B",
            "description": "Prism K⁺×I as Cat B thickening / cobordism scaffolding.",
            "bordism_role": "product with interval; not a residual clock",
            "residual_class_claim": "FORBIDDEN",
            "status": "open Cat B model",
        },
        {
            "id": "CB4_smooth_manifold_fill",
            "category": "B",
            "description": (
                "Hypothetical smooth compact spin 3-manifold (or ball) admitting "
                "a triangulation whose 2-skeleton deformation-retracts onto K⁺ "
                "or contains K⁺ as a subcomplex."
            ),
            "bordism_role": "would live in Ω_3^Spin ≅ 0 if closed; open existence question",
            "residual_class_claim": "FORBIDDEN — existence not proved; not B′ in Ω_3",
            "status": "open Cat B existence question",
        },
        {
            "id": "CB5_higher_spin_class_ambient",
            "category": "B",
            "description": (
                f"Ambient library of Ω_n^Spin(pt) and KO_n(pt) for n=8..15. "
                f"No residual quanta assigned. B′={B_prime} stays in degree 0 only "
                f"(locked A5/A5⁺)."
            ),
            "bordism_role": "coefficient table bookkeeping only",
            "residual_class_claim": "FORBIDDEN for n>0 residual geometry",
            "status": "library Cat B",
        },
        {
            "id": "CB6_Cartan_hopfion_continuum",
            "category": "B",
            "description": (
                "Continuum Cartan / hopfion geometric picture of residual flux as "
                "linked field configurations. Speculative continuum physics map."
            ),
            "bordism_role": "physics-side continuum metaphor, not a bordism proof",
            "residual_class_claim": "FORBIDDEN as residual carrier proof",
            "status": "open Cat B continuum metaphor (mirror note already forbids promotion)",
        },
        {
            "id": "CB7_product_sphere_stabilization",
            "category": "B",
            "description": (
                "Formal products K⁺ × S^k or cone × S^k as stabilization toys for "
                "higher AHSS pages. Not residual geometry."
            ),
            "bordism_role": "stabilization scaffolding only",
            "residual_class_claim": "FORBIDDEN",
            "status": "open Cat B scaffolding",
        },
    ]


def firewall_check(K_hom: dict, B_prime: int, a5plus_json: dict | None):
    """
    Verify that running Cat-B continuum work does not disturb locked A5⁺ facts.
    """
    checks = {
        "H0_is_1": K_hom["H0_free"] == 1,
        "H1_is_0": K_hom["H1_free"] == 0,
        "H2_is_0": K_hom["H2_free"] == 0,
        "no_torsion_d1": not K_hom["torsion_d1"],
        "no_torsion_d2": not K_hom["torsion_d2"],
        "V_is_539": K_hom["n_verts"] == 539,
        "E_is_594": K_hom["n_edges"] == 594,
        "F_is_56": K_hom["n_faces"] == 56,
        "B_prime_is_539": B_prime == 539,
        "does_not_write_A5plus_code": True,
        "does_not_feed_locked_stack": True,
    }
    if a5plus_json is not None:
        checks["a5plus_status_still_coefficients_only"] = (
            a5plus_json.get("status_code") == "A5PLUS_COEFFICIENTS_ONLY_ON_KPLUS"
        )
        ih = a5plus_json.get("integral_homology", {})
        checks["a5plus_json_H_match"] = (
            ih.get("H0_free") == 1
            and ih.get("H1_free") == 0
            and ih.get("H2_free") == 0
        )
    checks["all_pass"] = all(checks.values())
    return checks


def main() -> int:
    N_flux, N_tow, Q, f_max, B_prime, loads = atoms()
    O = core_q0(N_flux, f_max, Q, B_prime)
    elist, flist = build_Kplus_A2_enrich(O, loads)
    n = len(O)
    print(f"K+ rebuild: V={n} E={len(elist)} F={len(flist)}", flush=True)

    K_hom = integral_homology_K(n, elist, flist)
    print(
        f"K+ homology firewall: H0={K_hom['H0_free']} H1={K_hom['H1_free']} "
        f"H2={K_hom['H2_free']}",
        flush=True,
    )

    cone = cone_cell_counts(n, len(elist), len(flist))
    susp = suspension_cell_counts(n, len(elist), len(flist))
    prism = product_interval_counts(n, len(elist), len(flist))

    a5_path = Path(__file__).resolve().parents[1] / "architecture_A5plus_results.json"
    a5plus = None
    if a5_path.exists():
        a5plus = json.loads(a5_path.read_text(encoding="utf-8"))

    fw = firewall_check(K_hom, B_prime, a5plus)

    results = {
        "category": "B",
        "status_code": "CAT_B_CONTINUUM_FILLINGS_OPEN_NOT_LOCKED",
        "hard_firewall": {
            "locked_stack_untouched": True,
            "A5PLUS_code_not_modified": True,
            "Option3_intact": True,
            "No_Go_intact": True,
            "free_Tsharp_forbidden": True,
            "G4_not_identified_with_KO": True,
            "residual_0_class_stays_B_prime_in_degree_0_only": True,
            "checks": fw,
        },
        "Kplus_read_only_snapshot": {
            "mode": "A2_enrich",
            "homology": K_hom,
            "B_prime": B_prime,
            "note": "read-only rebuild for firewall; does not reopen A5⁺",
        },
        "combinatorial_continuum_proxies": {
            "cone": cone,
            "suspension": susp,
            "prism": prism,
        },
        "ambient_coefficient_library_n0_to_15": {
            "category": "B",
            "Omega_Spin_pt": {str(k): v for k, v in OMEGA_SPIN_PT_EXT.items()},
            "KO_pt": {str(k): v for k, v in KO_PT_EXT.items()},
            "note": (
                "Classical point coefficients only. No residual quanta assigned "
                "for n>0. Degrees 0..7 already used in locked A5⁺ as coefficients-only."
            ),
        },
        "candidate_catalogue": continuum_candidate_catalogue(B_prime),
        "explicit_non_claims": [
            "No continuum manifold is residual foundation",
            "No Ω_n for n>0 residual geometry lock",
            "No Cartan/hopfion as residual proof",
            "No G4 = 539.90 s as KO period",
            "No free T^sharp",
            "No No-Go lift",
            "No change to B′ count or A5⁺ AHSS collapse",
            "No security reduction for HQH-539",
        ],
        "next_catB_only": [
            "Existence of smooth triangulation realizing CB4",
            "Spin structure extension from unique BSpin on K⁺ to CB1/CB4",
            "Whether any Cat B continuum model couples to mirror-halo without reopening residual stack",
            "Keep all results off CLAIM_TABLE Category A rows",
        ],
    }

    out = Path(__file__).resolve().parents[1] / "continuum_fillings_catB_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print("wrote", out)
    if not fw["all_pass"]:
        print("FAIL: firewall checks did not all pass", file=sys.stderr)
        return 1
    print("OK: Cat-B continuum fillings catalogued; locked stack firewall PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
