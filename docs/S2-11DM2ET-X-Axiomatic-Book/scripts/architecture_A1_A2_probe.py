#!/usr/bin/env python3
"""
A1 seed equivariance / beta_sharp normal form + A2 constant simplicial lift checks.

PROVENANCE: residual flux quanta under Principle (S) + democratic charge partition.
Not free T-sharp. No No-Go lift.
"""
from __future__ import annotations

import json
import math
import random
import sys
from collections import Counter
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


def core_q0(N_flux: int, f_max: int, Q: int, B_prime: int, seed: set[int]) -> list[int]:
    residual = sorted(x for x in range(N_flux) if x not in seed)
    class0 = [residual[i] for i in range(len(residual)) if i % Q == 0]
    return class0[:B_prime]


def fiber_tuple(seq_mod: list[int]) -> tuple[int, ...]:
    c = Counter(seq_mod)
    return tuple(c[k] for k in range(8))


def main() -> int:
    N_flux, N_tow, Q, f_max, B_prime, loads = atoms()
    assert B_prime == 539

    provenance = {
        "objects": "residual flux quanta",
        "principle_S": True,
        "democratic_charge_partition": True,
        "not_free_Tsharp_basins": True,
        "no_go_lift_claimed": False,
    }

    # Expected index fiber table for B' = 8*67+3
    expected_index = fiber_tuple([i % 8 for i in range(B_prime)])
    assert expected_index == (68, 68, 68, 67, 67, 67, 67, 67)
    assert 8 * 67 + 3 == B_prime

    random.seed(0)
    index_tables: set[tuple[int, ...]] = set()
    ambient_mins: list[int] = []
    inj_sharp = 0
    inj_amb = 0
    n_trials = 100

    for _ in range(n_trials):
        seed = set(random.sample(range(N_flux), f_max))
        O = core_q0(N_flux, f_max, Q, B_prime, seed)
        assert len(O) == B_prime
        index_tables.add(fiber_tuple([i % 8 for i in range(len(O))]))
        amb = [x % 8 for x in O]
        ambient_mins.append(min(Counter(amb).values()))
        if len({(tower_of(x, loads), i % 8) for i, x in enumerate(O)}) == B_prime:
            inj_sharp += 1
        if len({(tower_of(x, loads), x % 8) for x in O}) == B_prime:
            inj_amb += 1

    assert index_tables == {expected_index}
    assert inj_sharp == n_trials

    # Canonical seed ambient vs sharp
    O0 = core_q0(N_flux, f_max, Q, B_prime, set(range(f_max)))
    amb0 = fiber_tuple([x % 8 for x in O0])
    sharp0 = fiber_tuple([i % 8 for i in range(len(O0))])

    # Affine ambient cannot match index table (sample)
    affine_hits = 0
    random.seed(1)
    for _ in range(30):
        seed = set(random.sample(range(N_flux), f_max))
        O = core_q0(N_flux, f_max, Q, B_prime, seed)
        hit = False
        for a in range(1, 8, 2):
            for b in range(8):
                if fiber_tuple([(a * x + b) % 8 for x in O]) == expected_index:
                    hit = True
                    break
            if hit:
                break
        if hit:
            affine_hits += 1

    # A2: constant simplicial map = function on 0-cells; check injectivity
    f_sharp = [(0, tower_of(x, loads), i % 8) for i, x in enumerate(O0)]
    assert len(set(f_sharp)) == B_prime

    # Optional 1-skeleton counts on canonical core
    same_tower_edges = 0
    for i in range(B_prime):
        for j in range(i + 1, B_prime):
            if tower_of(O0[i], loads) == tower_of(O0[j], loads):
                same_tower_edges += 1
    index_adj = B_prime - 1
    # same beta_sharp fiber: for each fiber, C(n,2)
    sharp_fib = Counter(i % 8 for i in range(B_prime))
    same_beta_edges = sum(n * (n - 1) // 2 for n in sharp_fib.values())

    # Nerve face check on a sample 2-simplex in BG_B (Z/8)
    def d0(g):
        return g[1:]

    def d1(g):
        return ( (g[0] + g[1]) % 8, ) + g[2:] if len(g) > 1 else ()

    def d2(g):
        return g[:-1]

    g = (3, 5, 2)
    assert d0(g) == (5, 2)
    assert d1(g) == ((3 + 5) % 8, 2)
    assert d2(g) == (3, 5)

    results = {
        "provenance": provenance,
        "A1": {
            "B_prime": B_prime,
            "expected_index_fibers": list(expected_index),
            "identity_8_67_plus_3": True,
            "trials": n_trials,
            "index_fiber_tables_unique": len(index_tables),
            "index_matches_expected_all_trials": True,
            "ambient_min_fiber_range": [min(ambient_mins), max(ambient_mins)],
            "injective_tower_beta_sharp": inj_sharp,
            "injective_tower_beta_ambient": inj_amb,
            "canonical_ambient_fibers": list(amb0),
            "canonical_sharp_fibers": list(sharp0),
            "affine_ambient_match_index_table_hits": affine_hits,
            "affine_trials": 30,
            "normal_form": "beta_sharp(x_i) = i mod 8",
        },
        "A2": {
            "model": "constant simplicial sets E(O_res) -> E(X_disc)",
            "f_sharp_injective_on_0_simplices": True,
            "nerve_Z8_face_identities_sample": True,
            "optional_1_skeleton_canonical": {
                "index_adjacent_edges": index_adj,
                "same_beta_sharp_edges": same_beta_edges,
                "same_tower_edges": same_tower_edges,
            },
            "continuous_BO_BSpin": "deferred to A3-A5",
        },
        "forbidden_claims": [
            "free T^sharp origin",
            "No-Go lift",
            "ambient x mod 8 fibers seed-invariant",
        ],
    }

    out = Path(__file__).resolve().parents[1] / "architecture_A1_A2_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))
    print("wrote", out)
    print("OK: A1 normal form + A2 constant simplicial lift")
    return 0


if __name__ == "__main__":
    sys.exit(main())
