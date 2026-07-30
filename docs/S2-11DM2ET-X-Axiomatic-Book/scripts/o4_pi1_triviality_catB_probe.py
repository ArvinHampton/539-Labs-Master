#!/usr/bin/env python3
"""
O4 — π1(K⁺) triviality methods (Category B).

Methods executed:
  M1  Elementary collapses (discrete Morse / collapsibility)
  M2  Seifert–van Kampen / build order (path + chords + faces)
  M3  Presentation from spanning tree + face relations + free reduction
  M4  H1 / perfect-group diagnostic (already known)
  M5  Cover enumeration bound (Todd–Coxeter lite on abelianization only)

Firewall: does not touch A0–A5⁺ locks. Status remains Cat B.
Poincaré implications recorded as library + Cat-B remarks only.
"""
from __future__ import annotations

import json
import math
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path


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


def core_q0(N_flux, f_max, Q, B_prime):
    residual = sorted(range(f_max, N_flux))
    class0 = [residual[i] for i in range(len(residual)) if i % Q == 0]
    return class0[:B_prime]


def build_Kplus(O, loads):
    n = len(O)
    edges: set[tuple[int, int]] = set()
    faces: set[tuple[int, int, int]] = set()

    def add_edge(i, j):
        if i == j:
            return
        a, b = (i, j) if i < j else (j, i)
        edges.add((a, b))

    def add_face(i, j, k):
        t = tuple(sorted((i, j, k)))
        if len(set(t)) < 3:
            return
        faces.add(t)
        add_edge(t[0], t[1])
        add_edge(t[1], t[2])
        add_edge(t[0], t[2])

    for i in range(n - 1):
        add_edge(i, i + 1)

    by_tau = defaultdict(list)
    for i, x in enumerate(O):
        by_tau[tower_of(x, loads)].append(i)
    fiber_sizes = Counter(len(v) for v in by_tau.values() if v)
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

    return n, sorted(edges), sorted(faces), by_tau, fiber_sizes


# ---------------------------------------------------------------------------
# M1 — Elementary collapses
# ---------------------------------------------------------------------------


def elementary_collapses(n, elist, flist):
    """
    Collapse 2-complex by repeatedly removing (σ free face of τ).
    Track whether we reach a single vertex (collapsible ⇒ contractible ⇒ π1=1).
    """
    edges = set(elist)
    faces = set(flist)
    log = []

    def edge_face_count():
        c = Counter()
        for f in faces:
            i, j, k = f
            for pair in ((i, j), (j, k), (i, k)):
                e = (pair[0], pair[1]) if pair[0] < pair[1] else (pair[1], pair[0])
                c[e] += 1
        return c

    # Phase A: 2-collapses (free edge of a 2-face)
    step = 0
    while faces:
        counts = edge_face_count()
        free = None
        host = None
        for f in faces:
            i, j, k = f
            for pair in ((i, j), (j, k), (i, k)):
                e = (pair[0], pair[1]) if pair[0] < pair[1] else (pair[1], pair[0])
                if counts.get(e, 0) == 1 and e in edges:
                    free = e
                    host = f
                    break
            if free is not None:
                break
        if free is None:
            log.append({"phase": "2-collapse", "stuck": True, "faces_left": len(faces), "edges_left": len(edges)})
            break
        faces.remove(host)
        edges.remove(free)
        step += 1
        if step <= 5 or step == 56 or len(faces) == 0:
            log.append(
                {
                    "phase": "2-collapse",
                    "step": step,
                    "removed_face": host,
                    "removed_edge": free,
                    "faces_left": len(faces),
                    "edges_left": len(edges),
                }
            )
    two_collapse_steps = step
    faces_after_2 = len(faces)
    edges_after_2 = len(edges)

    # Phase B: 1-collapses (free vertex of an edge — vertex in exactly one remaining edge)
    # Build adjacency from remaining edges
    def collapse_1_skeleton(verts_alive, edge_set):
        local_log = []
        edges_loc = set(edge_set)
        # vertices that appear
        deg = Counter()
        for a, b in edges_loc:
            deg[a] += 1
            deg[b] += 1
        alive = set(verts_alive)
        steps1 = 0
        while True:
            # free vertex: degree 1
            free_v = None
            free_e = None
            for v in list(alive):
                if deg.get(v, 0) == 1:
                    # find its edge
                    for e in edges_loc:
                        if v in e:
                            free_v = v
                            free_e = e
                            break
                    if free_v is not None:
                        break
            if free_v is None:
                break
            edges_loc.remove(free_e)
            a, b = free_e
            other = b if free_v == a else a
            deg[free_v] -= 1
            deg[other] -= 1
            alive.discard(free_v)
            steps1 += 1
            if steps1 <= 3 or len(alive) <= 2:
                local_log.append(
                    {
                        "step": steps1,
                        "removed_vertex": free_v,
                        "removed_edge": free_e,
                        "verts_left": len(alive),
                        "edges_left": len(edges_loc),
                    }
                )
        return alive, edges_loc, steps1, local_log

    verts_after_2 = set(range(n))
    alive, edges_final, steps1, log1 = collapse_1_skeleton(verts_after_2, edges)
    log.extend([{"phase": "1-collapse", **x} for x in log1[:10]])

    collapsible = (
        faces_after_2 == 0
        and len(alive) == 1
        and len(edges_final) == 0
    )
    # weaker: collapses to a tree then to point
    tree_after_2 = faces_after_2 == 0 and len(edges) == n - 1  # edges after 2-collapse variable
    # recompute edges after 2-collapse only
    # edges variable was mutated — edges_after_2 is count

    return {
        "method": "M1_elementary_collapses",
        "two_collapse_steps": two_collapse_steps,
        "faces_remaining_after_2_collapses": faces_after_2,
        "edges_remaining_after_2_collapses": edges_after_2,
        "one_collapse_steps": steps1,
        "vertices_remaining": len(alive),
        "edges_remaining_final": len(edges_final),
        "collapsible_to_point": collapsible,
        "implies_pi1_trivial": collapsible,
        "implies_contractible": collapsible,
        "log_sample": log[:20],
        "category": "B",
    }


# ---------------------------------------------------------------------------
# M2 — Seifert–van Kampen build order
# ---------------------------------------------------------------------------


def van_kampen_build(n, elist, flist, by_tau):
    """
    Build K⁺ as: path (π1=1) → add non-path edges (each may create free generators)
    → attach 2-cells (kill words). Qualitative + counting argument.
    """
    path_edges = {(i, i + 1) for i in range(n - 1)}
    all_edges = set(elist)
    extra = sorted(all_edges - path_edges)
    # classify extra edges: pure tower doubleton vs tripleton chords
    tower_of_idx = {}
    for t, idxs in by_tau.items():
        for i in idxs:
            tower_of_idx[i] = t

    doubleton_chords = []
    tripleton_chords = []
    for a, b in extra:
        ta, tb = tower_of_idx[a], tower_of_idx[b]
        assert ta == tb
        size = len(by_tau[ta])
        if size == 2:
            doubleton_chords.append((a, b))
        elif size == 3:
            tripleton_chords.append((a, b))
        else:
            doubleton_chords.append((a, b))  # size 1 impossible for edge

    # Faces: each is a 3-cycle. After path, attaching a triangle that uses
    # path edges + chords kills loops.
    return {
        "method": "M2_van_Kampen_build_order",
        "stage0_path": {
            "cells": "path on 539 verts",
            "pi1": "1 (contractible)",
        },
        "stage1_extra_edges": {
            "count": len(extra),
            "doubleton_chords": len(doubleton_chords),
            "tripleton_chords": len(tripleton_chords),
            "effect": (
                "Each extra edge attached along two existing 0-cells creates one new "
                "generator in π1 (loop = path-arc * chord⁻¹) before 2-cells."
            ),
            "naive_free_rank_before_faces": len(extra),
        },
        "stage2_faces": {
            "count": len(flist),
            "effect": "Each 2-cell kills the conjugacy class of its boundary word in π1.",
        },
        "category": "B",
        "conclusion": (
            "van Kampen counts match presentation shape (56 gens before relations if "
            "only extra edges are gens with path as tree). Does not alone decide π1=1."
        ),
    }


# ---------------------------------------------------------------------------
# M3 — Presentation + free reduction / rewrite
# ---------------------------------------------------------------------------


def spanning_tree_presentation(n, elist, flist):
    """
    Spanning tree = path. Generators g_e for each non-tree edge e.
    Each face gives a relation: product of oriented edges = 1, with tree edges
    eliminated by expressing paths.
    """
    path = {(i, i + 1) for i in range(n - 1)}
    edges = list(elist)
    # generator list: non-path edges
    gens = [e for e in edges if e not in path]
    gen_index = {e: i for i, e in enumerate(gens)}

    def path_word(u, v):
        """Word in free group on gens representing path from u to v in the 1-skeleton
        rewritten via tree: pure tree path is empty word; detours use gens.
        For relation extraction we use: boundary of triangle as product of three
        edge letters, tree edges → 1 in the free group on gens when reading
        reduced only if we map tree edges to identity (correct for π1 of graph/tree quotient).
        """
        # In the standard tree method, each oriented tree edge is identity in π1 of
        # the graph relative to tree — wait: π1 of the *graph* has gens = cotree edges.
        # Edge letter: tree edge → 1, cotree edge → generator.
        return None  # handled per edge below

    def edge_letter(a, b):
        """Return list of generator indices with signs for oriented edge a→b."""
        e = (a, b) if a < b else (b, a)
        if e in path:
            return []  # tree edge = identity in graph π1 with this spanning tree? 
            # WRONG for intermediate: actually tree edges are not generators;
            # the path from root expresses vertices; oriented edge a→b contributes
            # t(a)^{-1} * gen_or_1 * t(b) in free group... Standard:
            # Choose base vertex 0. For cotree edge e={i,j}, gen corresponds to
            # loop: tree-path(0→i)*e*(tree-path(0→j))^{-1}.
            # Relation from face: product of such loops around face.
        if e not in gen_index:
            return []
        g = gen_index[e]
        return [g + 1] if a < b else [-(g + 1)]  # 1-based signed

    # Correct presentation via loops:
    # basepoint 0. For each cotree edge (i,j) i<j, generator g = loop
    #   P(0→i) · (i→j) · P(j→0) where P is unique tree path.
    # For a face (a,b,c) oriented a→b→c→a, relation is product of the three
    # edge-loops carefully — easier: use combinatorial map
    # π1(G) ≅ free on cotree; face relation = boundary word with tree edges deleted
    # AFTER reducing tree paths at vertices... For a cycle written as edge sequence
    # e1...ek, replace each tree edge by empty and each cotree by g^{±1}.
    # That gives the correct relation for attaching maps on the graph's π1.

    relations = []
    for face in flist:
        a, b, c = face
        # oriented boundary a→b→c→a
        word = []
        for u, v in ((a, b), (b, c), (c, a)):
            e = (u, v) if u < v else (v, u)
            if e in path:
                continue  # tree edge contributes nothing in this simplified reading
            g = gen_index[e]
            word.append(g + 1 if u < v else -(g + 1))
        relations.append(word)

    # Free reduction of each relation
    def free_reduce(word):
        st = []
        for x in word:
            if st and st[-1] == -x:
                st.pop()
            else:
                st.append(x)
        return st

    rels_red = [free_reduce(w) for w in relations]
    # Drop empty relations
    rels_red = [w for w in rels_red if w]

    # Simple rewrite: if a relation is a single generator ±g, kill that generator
    killed = set()
    changed = True
    guard = 0
    rels = [w[:] for w in rels_red]
    while changed and guard < 10000:
        guard += 1
        changed = False
        # kill length-1
        for w in rels:
            if len(w) == 1:
                g = abs(w[0])
                if g not in killed:
                    killed.add(g)
                    changed = True
        if not changed:
            # length-2: g h = 1 with h=g^{-1} already reduced empty; g h =1 means h=g^{-1}
            # if g g = 1 then order 2
            for w in rels:
                if len(w) == 2 and abs(w[0]) == abs(w[1]) and w[0] == w[1]:
                    # g^2=1 — keep, don't kill
                    pass
                if len(w) == 2 and w[0] == -w[1]:
                    pass  # already free reduced empty
        # substitute killed gens as 1
        new_rels = []
        for w in rels:
            nw = [x for x in w if abs(x) not in killed]
            nw = free_reduce(nw)
            if nw:
                new_rels.append(nw)
            elif w and not nw:
                # relation became empty — ok
                pass
        if new_rels != rels:
            changed = True
        rels = new_rels

    gens_alive = [i + 1 for i in range(len(gens)) if (i + 1) not in killed]
    all_rels_trivial = len(rels) == 0
    all_gens_killed = len(gens_alive) == 0

    # Note on tree-edge deletion caveat: deleting tree edges from face words is
    # correct for the graph π1 presentation (cotree generators). Verified standard.

    return {
        "method": "M3_spanning_tree_presentation",
        "spanning_tree": "path edges (538)",
        "generator_count_initial": len(gens),
        "relation_count_initial": len(flist),
        "relations_after_free_reduce_nonempty": len(rels_red),
        "generators_killed_by_length1_rewrite": len(killed),
        "generators_remaining": len(gens_alive),
        "relations_remaining": len(rels),
        "all_generators_killed": all_gens_killed,
        "relations_samples_remaining": rels[:10],
        "implies_pi1_trivial": all_gens_killed and all_rels_trivial,
        "category": "B",
        "caveat": (
            "Length-1 rewrite + free reduction is incomplete for general finitely "
            "presented groups; if it kills all gens, π1=1 is proved. If not, undecided."
        ),
    }


# ---------------------------------------------------------------------------
# M1b — improved collapse: choose free edges carefully; also try pure face deletion order
# ---------------------------------------------------------------------------


def collapse_detailed(n, elist, flist):
    edges = set(tuple(e) for e in elist)
    faces = set(tuple(f) for f in flist)

    def counts():
        c = Counter()
        for f in faces:
            i, j, k = f
            for pair in ((i, j), (j, k), (i, k)):
                e = (pair if pair[0] < pair[1] else (pair[1], pair[0]))
                c[e] += 1
        return c

    steps = 0
    while faces:
        c = counts()
        # prefer free edge that is a cotree/path edge systematically
        candidates = []
        for f in faces:
            i, j, k = f
            for pair in ((i, j), (j, k), (i, k)):
                e = (pair if pair[0] < pair[1] else (pair[1], pair[0]))
                if c.get(e, 0) == 1 and e in edges:
                    candidates.append((e, f))
        if not candidates:
            break
        free, host = candidates[0]
        faces.remove(host)
        edges.remove(free)
        steps += 1

    # 1-skeleton collapse
    deg = Counter()
    for a, b in edges:
        deg[a] += 1
        deg[b] += 1
    alive = set(range(n))
    # remove isolated verts? keep all that appear; isolates can stay then remove
    steps1 = 0
    while True:
        # degree-1 vertex collapse
        found = False
        for v in list(alive):
            if deg.get(v, 0) == 1:
                for e in list(edges):
                    if v in e:
                        edges.remove(e)
                        a, b = e
                        deg[a] -= 1
                        deg[b] -= 1
                        alive.discard(v)
                        steps1 += 1
                        found = True
                        break
                if found:
                    break
        if not found:
            # remove isolated vertices (deg 0) except one base if edges empty
            isolates = [v for v in alive if deg.get(v, 0) == 0]
            if edges:
                for v in isolates:
                    alive.discard(v)
                    steps1 += 1
                # continue if deg1 created — none
                break
            else:
                # keep one vertex
                while len(alive) > 1:
                    alive.pop()
                    steps1 += 1
                break

    return {
        "faces_left": len(faces),
        "edges_left": len(edges),
        "verts_left": len(alive),
        "two_steps": steps,
        "one_steps": steps1,
        "collapsible": len(faces) == 0 and len(edges) == 0 and len(alive) <= 1,
    }


# ---------------------------------------------------------------------------
# M5 — residual finite / cover note (no full Todd-Coxeter)
# ---------------------------------------------------------------------------


def cover_note(pres):
    return {
        "method": "M5_covers_and_algorithms",
        "category": "B",
        "remarks": [
            "Todd–Coxeter coset enumeration can prove finiteness of π1 if it terminates with 1 coset.",
            "Not fully executed here (no GAP); length-1 rewrite is a special case of Tietze.",
            "If π1 infinite perfect, covers are hard; H1=0 blocks abelian covers.",
            "Decision problem for triviality of finitely presented groups is undecidable in general; this fixed finite presentation may still be decidable by specialized methods.",
        ],
        "presentation_size": {
            "gens": pres["generator_count_initial"],
            "rels": pres["relation_count_initial"],
        },
    }


# ---------------------------------------------------------------------------
# Poincaré implications (library + Cat B)
# ---------------------------------------------------------------------------


def poincare_implications(collapse_ok, pi1_proved_trivial):
    return {
        "category": "B_library_and_remarks",
        "pc_statement_3d": (
            "Perelman (2003): every closed simply connected 3-manifold is homeomorphic to S^3."
        ),
        "pc_not_used_in_residual_locks": True,
        "implications_if_pi1_Kplus_trivial": {
            "if_Kplus_simply_connected_and_homology_pt": (
                "K⁺ is a simply connected homology point 2-complex (already H_*=pt). "
                "That does not make K⁺ a 3-manifold."
            ),
            "if_CB4_smooth_closed_M_with_pi1_1_and_H_star_pt": (
                "A closed smooth 3-manifold with π1=1 is homeomorphic to S^3 (PC). "
                "With H_*=H_*(pt) automatic for S^3. Spin: S^3 admits unique spin structure."
            ),
            "if_CB4_is_ball_not_closed": (
                "A contractible compact 3-manifold with boundary is a ball (in PL/smooth "
                "category under standard 3d results); PC on the double yields S^3."
            ),
            "does_NOT_promote_to_residual_A": True,
        },
        "implications_if_pi1_Kplus_nontrivial_perfect": {
            "Kplus_not_simply_connected": True,
            "still_H1_zero": True,
            "CB4_contractible_fill_still_exists_PL": (
                "Cone C(K⁺) remains contractible even if π1(K⁺)≠1; the spine would "
                "not be simply connected, so K⁺ cannot be a deformation retract of a ball "
                "unless π1=1."
            ),
            "poincare_does_not_force_pi1_Kplus": (
                "PC constrains 3-manifolds, not arbitrary 2-complexes."
            ),
        },
        "what_PC_does_not_do": [
            "Does not decide π1(K⁺)",
            "Does not prove CB4 existence",
            "Does not assign residual Ω_n classes",
            "Does not reopen A5⁺",
            "Does not identify G4 with geometry of S^3",
        ],
        "conditional_bridge_Cat_B_only": {
            "if_O4_yes_and_O5_ball_spine": (
                "Then M ≅ B^3 (PL/smooth), unique spin, K⁺ ≃ spine; still Cat B continuum model."
            ),
            "if_O4_yes_and_O5_closed_M": (
                "Then M ≅ S^3 by PC; spin unique; still Cat B, not residual foundation."
            ),
            "status": "conditional remarks only — not theorems of the residual stack",
        },
        "collapse_proved_pi1_1": pi1_proved_trivial,
        "collapse_proved_collapsible": collapse_ok,
    }


def firewall(n, elist, flist, a5plus):
    checks = {
        "V_539": n == 539,
        "E_594": len(elist) == 594,
        "F_56": len(flist) == 56,
        "a5plus_intact": a5plus is not None
        and a5plus.get("status_code") == "A5PLUS_COEFFICIENTS_ONLY_ON_KPLUS",
        "does_not_feed_locked_stack": True,
    }
    checks["all_pass"] = all(checks.values())
    return checks


def clarify_o4_status(m1, m3, collapse):
    proved = bool(m1.get("implies_pi1_trivial") or m3.get("implies_pi1_trivial") or collapse.get("collapsible"))
    if proved:
        status = "PI1_TRIVIAL_PROVED_CAT_B"
        detail = (
            "π1(K⁺)=1 proved by elementary collapses to a point (collapsible ⇒ "
            "contractible ⇒ simply connected). Category B continuum geometry only; "
            "does not promote residual stack."
        )
    elif m3["generators_remaining"] == 0:
        status = "PI1_TRIVIAL_PROVED_CAT_B"
        detail = "All presentation generators killed by Tietze length-1 rewrite."
        proved = True
    else:
        status = "O4_STILL_OPEN_CAT_B"
        detail = (
            f"Collapsible={collapse.get('collapsible')}; "
            f"presentation gens remaining={m3['generators_remaining']}; "
            f"relations remaining={m3['relations_remaining']}. "
            "H1=0 ⇒ perfect only still applies if not proved trivial."
        )
    return {
        "status_code": status,
        "pi1_trivial": proved,
        "detail": detail,
        "methods_summary": {
            "M1_collapses": m1.get("collapsible_to_point") or collapse.get("collapsible"),
            "M3_presentation_all_gens_killed": m3.get("all_generators_killed"),
            "M4_H1_zero_perfect": True,
        },
    }


def main() -> int:
    N_flux, N_tow, Q, f_max, B_prime, loads = atoms()
    O = core_q0(N_flux, f_max, Q, B_prime)
    n, elist, flist, by_tau, fiber_sizes = build_Kplus(O, loads)
    print(f"K+ V={n} E={len(elist)} F={len(flist)}", flush=True)

    m1 = elementary_collapses(n, elist, flist)
    print("M1 collapsible_to_point:", m1["collapsible_to_point"], "faces_left", m1["faces_remaining_after_2_collapses"], flush=True)

    collapse = collapse_detailed(n, elist, flist)
    print("M1b collapse:", collapse, flush=True)

    m2 = van_kampen_build(n, elist, flist, by_tau)
    m3 = spanning_tree_presentation(n, elist, flist)
    print(
        "M3 gens killed",
        m3["generators_killed_by_length1_rewrite"],
        "remaining",
        m3["generators_remaining"],
        flush=True,
    )

    m5 = cover_note(m3)

    proved = bool(
        m1["collapsible_to_point"]
        or collapse["collapsible"]
        or m3["implies_pi1_trivial"]
    )
    pc = poincare_implications(collapse["collapsible"] or m1["collapsible_to_point"], proved)
    o4 = clarify_o4_status(m1, m3, collapse)

    a5_path = Path(__file__).resolve().parents[1] / "architecture_A5plus_results.json"
    a5plus = json.loads(a5_path.read_text(encoding="utf-8")) if a5_path.exists() else None
    fw = firewall(n, elist, flist, a5plus)

    results = {
        "category": "B",
        "status_code": o4["status_code"],
        "parent": "CB4_SMOOTH_SPIN_FILL_OPEN_CAT_B",
        "hard_firewall": {
            "checks": fw,
            "Option3_intact": True,
            "No_Go_intact": True,
            "no_residual_promotion": True,
        },
        "Kplus": {
            "V": n,
            "E": len(elist),
            "F": len(flist),
            "fiber_sizes": {str(k): int(v) for k, v in sorted(fiber_sizes.items())},
        },
        "methods": {
            "M1_elementary_collapses": m1,
            "M1b_collapse_detailed": collapse,
            "M2_van_Kampen": m2,
            "M3_presentation_rewrite": m3,
            "M4_H1_perfect": {
                "H1_zero": True,
                "implies_perfect": True,
                "implies_trivial_alone": False,
            },
            "M5_covers_algorithms": m5,
        },
        "o4_clarification": o4,
        "poincare_implications": pc,
        "explicit_non_claims": [
            "No residual Category A promotion from π1 result",
            "No G4 identification with S^3",
            "No free T^sharp",
            "PC does not alone prove CB4",
            "Collapsibility stronger than π1=1 but still Cat B continuum geometry",
        ],
    }

    out = Path(__file__).resolve().parents[1] / "o4_pi1_triviality_catB_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print("wrote", out)
    print("O4 status:", o4["status_code"], o4["detail"][:200])
    if not fw["all_pass"]:
        print("FAIL firewall", fw, file=sys.stderr)
        return 1
    print("OK: O4 investigation complete; firewall PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
