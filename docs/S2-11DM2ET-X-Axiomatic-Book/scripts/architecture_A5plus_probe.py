#!/usr/bin/env python3
"""
A5⁺ — integral H_*(K⁺) and AHSS skeleton for Ω_*^Spin / KO_* on primary K⁺.

PROVENANCE (mandatory): residual flux quanta under Principle (S) + democratic
charge-sector partition. Not free T-sharp. No No-Go lift. Option 3 intact.

Depends on A4⁺ primary domain A2_enrich (path + same-tower + triangle fill).
Does not reopen A4/A5 0-stem. Does not claim continuum manifold fillings.
"""
from __future__ import annotations

import json
import math
import sys
from collections import defaultdict
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
    """
    Integer Smith normal form diagonal (nonzero invariant factors) + rank.
    Optimized for sparse ±1 incidence matrices.
    """
    if A.size == 0:
        return [], 0
    M = A.astype(object).copy()
    m, n = M.shape
    inv: list[int] = []
    r = 0
    for k in range(min(m, n)):
        # find nonzero entry of minimal abs in submatrix
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

        # Euclidean clear column and row until pivot divides all
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
            # divisibility condition on trailing block
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


def integral_homology(n: int, elist, flist):
    d1, d2 = oriented_boundary_matrices(n, elist, flist)
    ne, nf = len(elist), len(flist)

    inv1, rank1 = smith_invariant_factors(d1)
    torsion1 = [d for d in inv1 if d > 1]
    free_coker1 = n - rank1

    inv2, rank2 = smith_invariant_factors(d2)
    torsion2 = [d for d in inv2 if d > 1]
    free_H1 = (ne - rank1) - rank2
    free_H2 = nf - rank2

    euler_cells = n - ne + nf
    euler_hom = free_coker1 - free_H1 + free_H2

    def snf_summary(inv):
        if not inv:
            return {"all_ones": True, "count": 0, "min": None, "max": None}
        return {
            "all_ones": all(d == 1 for d in inv),
            "count": len(inv),
            "min": min(inv),
            "max": max(inv),
        }

    return {
        "n_verts": n,
        "n_edges": ne,
        "n_faces": nf,
        "rank_d1": rank1,
        "rank_d2": rank2,
        "torsion_from_d1": torsion1,
        "torsion_from_d2": torsion2,
        "H0_free": free_coker1,
        "H1_free": free_H1,
        "H2_free": free_H2,
        "H0_expected": "Z if connected (rank 1)",
        "euler_cells": euler_cells,
        "euler_homology_free": euler_hom,
        "connected": free_coker1 == 1 and not torsion1,
        "acyclic_positive": free_H1 == 0 and free_H2 == 0 and not torsion2,
        "SNF_d1_diag_summary": snf_summary(inv1),
        "SNF_d2_diag_summary": snf_summary(inv2),
    }


def gf2_rank(rows: list[list[int]]) -> int:
    if not rows:
        return 0
    M = [[abs(x) % 2 for x in row] for row in rows]
    m, n = len(M), len(M[0])
    r = 0
    for c in range(n):
        piv = None
        for i in range(r, m):
            if M[i][c]:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(m):
            if i != r and M[i][c]:
                for j in range(c, n):
                    M[i][j] ^= M[r][j]
        r += 1
        if r == m:
            break
    return r


def f2_betti(n, elist, flist):
    ne, nf = len(elist), len(flist)
    e_index = {e: i for i, e in enumerate(elist)}
    d0 = [[0] * n for _ in range(ne)]
    for ei, (i, j) in enumerate(elist):
        d0[ei][i] = 1
        d0[ei][j] = 1
    d1 = [[0] * ne for _ in range(nf)]
    for fi, (i, j, k) in enumerate(flist):
        for pair in ((i, j), (j, k), (i, k)):
            a, b = (pair if pair[0] < pair[1] else (pair[1], pair[0]))
            d1[fi][e_index[(a, b)]] = 1
    r0 = gf2_rank([row[:] for row in d0])
    r1 = gf2_rank([row[:] for row in d1]) if nf else 0
    b0 = n - r0
    b1 = (ne - r0) - r1
    b2 = nf - r1
    return {"beta0_F2": b0, "beta1_F2": b1, "beta2_F2": b2}


OMEGA_SPIN_PT = {
    0: "Z",
    1: "Z/2",
    2: "Z/2",
    3: "0",
    4: "Z",
    5: "0",
    6: "0",
    7: "0",
}
KO_PT = {
    0: "Z",
    1: "Z/2",
    2: "Z/2",
    3: "0",
    4: "Z",
    5: "0",
    6: "0",
    7: "0",
}


def ahss_skeleton(homology: dict, B_prime: int):
    H0 = homology["H0_free"]
    H1 = homology["H1_free"]
    H2 = homology["H2_free"]
    torsion_ok = not homology["torsion_from_d1"] and not homology["torsion_from_d2"]
    pointlike = H0 == 1 and H1 == 0 and H2 == 0 and torsion_ok and homology["connected"]

    e2_spin = {}
    e2_ko = {}
    for q in range(0, 8):
        row_s = {}
        row_k = {}
        for p in range(0, 3):
            if p == 0 and H0 == 1:
                row_s[f"p={p}"] = f"H0 ⊗ Ω_{q} ≅ {OMEGA_SPIN_PT[q]}"
                row_k[f"p={p}"] = f"H0 ⊗ KO_{q} ≅ {KO_PT[q]}"
            else:
                row_s[f"p={p}"] = "0"
                row_k[f"p={p}"] = "0"
        e2_spin[f"q={q}"] = row_s
        e2_ko[f"q={q}"] = row_k

    return {
        "pointlike_integral_homology": pointlike,
        "E2_spin_skeleton": e2_spin,
        "E2_ko_skeleton": e2_ko,
        "predicted_Omega_Spin_Kplus_through_7": {str(n): OMEGA_SPIN_PT[n] for n in range(8)},
        "predicted_KO_Kplus_through_7": {str(n): KO_PT[n] for n in range(8)},
        "residual_0_class": {
            "Omega_0_Spin_Kplus": f"Z with residual class = B' = {B_prime}",
            "KO_0_Kplus": f"Z with ABS image = B' = {B_prime}",
            "higher_through_7": (
                "isomorphic to coefficients of a point (no extra classes from topology)"
                if pointlike
                else "pointlike hypothesis failed — recheck SNF"
            ),
        },
        "AHSS_collapse_argument": (
            "E2 concentrated on p=0 column; no room for d_r differentials into/out of "
            "nonzero positive-p groups; AHSS collapses to Ω_n^Spin(pt) and KO_n(pt) "
            "through degree 7 (ABS range)."
            if pointlike
            else "collapse not claimed: homology not that of a point"
        ),
        "ABS_range": "degrees 0..7 (MSpin → ko is 7-connected)",
        "status_code": (
            "A5PLUS_COEFFICIENTS_ONLY_ON_KPLUS"
            if pointlike
            else "A5PLUS_OPEN_OR_OBSTRUCTED"
        ),
    }


def main() -> int:
    N_flux, N_tow, Q, f_max, B_prime, loads = atoms()
    assert B_prime == 539 and N_tow == 243
    O = core_q0(N_flux, f_max, Q, B_prime)
    assert len(O) == B_prime

    elist, flist = build_Kplus_A2_enrich(O, loads)
    n = B_prime
    print(
        f"K+ A2_enrich: V={n} E={len(elist)} F={len(flist)}",
        flush=True,
    )

    hom = integral_homology(n, elist, flist)
    print(
        f"H0={hom['H0_free']} H1={hom['H1_free']} H2={hom['H2_free']} "
        f"torsion1={hom['torsion_from_d1']} torsion2={hom['torsion_from_d2']}",
        flush=True,
    )

    f2 = f2_betti(n, elist, flist)
    print(f"F2 betti: {f2}", flush=True)

    ahss = ahss_skeleton(hom, B_prime)

    results = {
        "provenance": {
            "objects": "residual flux quanta",
            "principle_S": True,
            "democratic_charge_partition": True,
            "not_free_Tsharp_basins": True,
            "no_go_lift_claimed": False,
            "option3_free_dynamics_unchanged": True,
            "A4_0stem_intact": True,
            "A5_0stem_intact": True,
            "A4plus_intact": True,
            "domain": "primary K⁺ A2_enrich only",
        },
        "Kplus": {
            "mode": "A2_enrich",
            "n_verts": n,
            "n_edges": len(elist),
            "n_faces": len(flist),
            "B_prime": B_prime,
        },
        "integral_homology": hom,
        "F2_betti_check": f2,
        "AHSS": ahss,
        "theorems_candidate": [
            "A5⁺.1: integral H_*(K⁺) ≅ H_*(pt) (H0=Z, H>0=0) on primary A2_enrich.",
            "A5⁺.2: AHSS for Ω_*^Spin(K⁺) and KO_*(K⁺) collapses to coefficient groups through degree 7.",
            "A5⁺.3: residual 0-class remains B′ in Ω_0^Spin(K⁺) ≅ Z and KO_0(K⁺) ≅ Z.",
            "A5⁺.4: no extra residual bordism/KO classes from primary K⁺ topology in ABS range.",
        ],
        "not_claimed": [
            "free T^sharp origin",
            "No-Go lift",
            "continuum manifold fillings of residual geometry",
            "G4=539.9 identified with KO period",
            "security reduction",
            "Ω_n for n>7 beyond coefficient table",
            "bott_graph secondary mode as primary domain",
        ],
        "status_code": ahss["status_code"],
    }

    out = Path(__file__).resolve().parents[1] / "architecture_A5plus_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print("wrote", out)
    if ahss["status_code"] != "A5PLUS_COEFFICIENTS_ONLY_ON_KPLUS":
        print("FAIL: A5⁺ not closed as coefficients-only", file=sys.stderr)
        return 1
    if f2 != {"beta0_F2": 1, "beta1_F2": 0, "beta2_F2": 0}:
        print("FAIL: F2 betti mismatch vs A4⁺", file=sys.stderr)
        return 1
    print("OK: A5⁺ integral H_*(K⁺) ≅ pt; AHSS coefficients-only through degree 7")
    return 0


if __name__ == "__main__":
    sys.exit(main())
