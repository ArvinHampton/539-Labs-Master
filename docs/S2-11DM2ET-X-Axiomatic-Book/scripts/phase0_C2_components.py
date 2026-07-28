#!/usr/bin/env python3
"""
Phase 0 executable probe: package C2 — components of the physical graph.

Builds a finite directed graph under T^sharp with vertices {1,...,N_cut}
and edges n -> T^sharp(n) when the image is in range (or collapse to 1 if hit).

Reports weakly connected components (undirected) and number of trees flowing to 1.

Does NOT insert 539 into the graph definition.
Compares component counts to 539 only post-hoc.

Usage:
  python phase0_C2_components.py --Ncut 5000
  python phase0_C2_components.py --Ncut 20000
"""
from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict, deque
from pathlib import Path


def T_sharp(n: int) -> int:
    if n <= 0:
        return 0
    r = n % 3
    if r == 0:
        return n // 3
    if r == 1:
        return (4 * n + 2) // 3
    def Tc(k):
        return (n + 1) // 3 + 2 * (3**k)

    t = n % 9
    for k in range(5):
        if Tc(k) % 9 == t:
            return Tc(k)

    def defect(k):
        d = abs(Tc(k) % 9 - t)
        return min(d, 9 - d)

    k = min(range(3), key=lambda j: (defect(j), j))
    return Tc(k)


def Ncut_from_flux(c: int = 2) -> int:
    """Cutoff from flux only: 3^(ceil(log3 N_flux)+c)."""
    N_flux = 4880
    log3 = math.log(N_flux) / math.log(3)
    return int(3 ** (math.ceil(log3) + c))


def build_next(N_cut: int) -> dict[int, int]:
    nxt = {}
    for n in range(1, N_cut + 1):
        m = T_sharp(n)
        if m < 1:
            m = 1
        if m > N_cut:
            # project large images back by iterating until in range or cap
            steps = 0
            while m > N_cut and steps < 100:
                m = T_sharp(m)
                steps += 1
            if m > N_cut or m < 1:
                m = 1
        nxt[n] = m
    return nxt


def weakly_connected_components(nxt: dict[int, int]) -> list[set[int]]:
    """Undirected components of the functional graph."""
    und: dict[int, set[int]] = defaultdict(set)
    for a, b in nxt.items():
        und[a].add(b)
        und[b].add(a)
    seen = set()
    comps = []
    for v in und:
        if v in seen:
            continue
        comp = set()
        dq = deque([v])
        seen.add(v)
        while dq:
            x = dq.popleft()
            comp.add(x)
            for y in und[x]:
                if y not in seen:
                    seen.add(y)
                    dq.append(y)
        comps.append(comp)
    return comps


def basins_to_one(nxt: dict[int, int]) -> dict[int, int]:
    """For each node, eventual image under iteration if it reaches 1 within bound."""
    reach = {}
    for n in nxt:
        x = n
        seen = set()
        ok = False
        for _ in range(len(nxt) + 5):
            if x == 1:
                ok = True
                break
            if x in seen:
                break
            seen.add(x)
            x = nxt.get(x, 1)
        reach[n] = 1 if ok else 0
    return reach


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--Ncut", type=int, default=0, help="0 => from flux formula")
    ap.add_argument("--c", type=int, default=2, help="extra log3 powers in Ncut_from_flux")
    args = ap.parse_args()

    N_cut = args.Ncut if args.Ncut > 0 else Ncut_from_flux(args.c)
    nxt = build_next(N_cut)
    comps = weakly_connected_components(nxt)
    sizes = sorted((len(c) for c in comps), reverse=True)
    reach = basins_to_one(nxt)
    n_reach1 = sum(reach.values())

    # post-hoc comparisons (not used in construction)
    claimed = 539
    report = {
        "package": "C2",
        "N_cut": N_cut,
        "N_cut_formula": "3**(ceil(log3(4880))+c)" if args.Ncut == 0 else "manual",
        "c": args.c if args.Ncut == 0 else None,
        "n_vertices": N_cut,
        "n_edges": len(nxt),
        "n_weak_components": len(comps),
        "component_size_max": sizes[0] if sizes else 0,
        "component_size_top10": sizes[:10],
        "n_vertices_reaching_1": n_reach1,
        "fraction_reaching_1": n_reach1 / N_cut,
        "post_hoc": {
            "claimed_539": claimed,
            "n_components_equals_539": len(comps) == claimed,
            "abs_diff_components_vs_539": abs(len(comps) - claimed),
        },
        "phase0_note": "If n_weak_components != 539, H0 for this C2 realization fails; refine N_cut or package",
        "gaps": {
            "G0.1_Psi_tow": "520 not derived from (20,21,243) alone in this script",
            "G0.2_Sigma_seed": "seed multiset not used in C2 graph (all n<=N_cut)",
        },
    }

    print("=" * 64)
    print("PHASE 0 — Package C2 finite-graph probe")
    print("=" * 64)
    print(f"N_cut = {N_cut}  (vertices)")
    print(f"Weakly connected components = {len(comps)}")
    print(f"Top component sizes = {sizes[:8]}")
    print(f"Vertices reaching 1 = {n_reach1} ({100*n_reach1/N_cut:.1f}%)")
    print()
    print("--- Post-hoc vs claimed 539 ---")
    print(f"  |n_components - 539| = {abs(len(comps)-539)}")
    print(f"  equal? {len(comps)==539}")
    print()
    print("H0 for this C2 realization:", "HOLD" if len(comps)==539 else "FAIL / needs refinement")
    print("=" * 64)

    out = Path(__file__).resolve().parent.parent / "phase0_C2_results.json"
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
