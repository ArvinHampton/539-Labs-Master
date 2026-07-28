#!/usr/bin/env python3
"""
Architecture A discrete probe on O_res carrier.

PROVENANCE (mandatory):
  Objects are residual flux quanta under Principle (S) and democratic
  charge-sector partition. Not free T-sharp basins. Does not lift No-Go.

See: Architecture_A_Ores_Programme.md, Object539_NonCircular_Construction.md
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
    return N_flux, N_tow, Q, f_min, R_exc, f_max, B_prime


def tower_loads(N_tow: int, f_min: int, R_exc: int) -> list[int]:
    return [f_min + 1] * R_exc + [f_min] * (N_tow - R_exc)


def tower_of(x: int, loads: list[int]) -> int:
    acc = 0
    for t, L in enumerate(loads):
        if acc <= x < acc + L:
            return t
        acc += L
    return len(loads) - 1


def equitable_classes(residual: list[int], Q: int) -> list[list[int]]:
    classes: list[list[int]] = [[] for _ in range(Q)]
    for i, x in enumerate(sorted(residual)):
        classes[i % Q].append(x)
    return classes


def cores_from_seed(N_flux: int, f_max: int, Q: int, B_prime: int, seed: set[int]):
    residual = [x for x in range(N_flux) if x not in seed]
    classes = equitable_classes(residual, Q)
    return [sorted(c)[:B_prime] for c in classes]


def main() -> int:
    N_flux, N_tow, Q, f_min, R_exc, f_max, B_prime = atoms()
    assert B_prime == 539
    loads = tower_loads(N_tow, f_min, R_exc)
    assert sum(loads) == N_flux

    provenance = {
        "objects": "residual flux quanta",
        "principle_S": True,
        "democratic_charge_partition": True,
        "not_free_Tsharp_basins": True,
        "no_go_lift_claimed": False,
        "count_formula_RHS": "floor((N_flux - f_max)/9)",
    }

    # Canonical seed
    seed0 = set(range(f_max))
    cores = cores_from_seed(N_flux, f_max, Q, B_prime, seed0)
    O = cores[0]
    assert len(O) == B_prime

    beta = Counter(x % 8 for x in O)
    mod9 = set(x % 9 for x in O)
    towers = [tower_of(x, loads) for x in O]
    pairs = {(towers[i], O[i] % 8) for i in range(len(O))}
    triples_9 = {
        (q, tower_of(x, loads), x % 8) for q, core in enumerate(cores) for x in core
    }

    fiber_table = {str(k): beta[k] for k in range(8)}
    # 8*67+3 structure
    floor_fiber = B_prime // 8
    excess = B_prime % 8

    # Seed equivariance sample: fiber floor always B'//8?
    random.seed(1)
    fiber_floors = []
    inject_ok = 0
    for _ in range(50):
        seed = set(random.sample(range(N_flux), f_max))
        O_r = cores_from_seed(N_flux, f_max, Q, B_prime, seed)[0]
        b = Counter(x % 8 for x in O_r)
        fiber_floors.append(min(b.values()))
        pr = {(tower_of(x, loads), x % 8) for x in O_r}
        if len(pr) == B_prime:
            inject_ok += 1

    results = {
        "provenance": provenance,
        "atoms": {
            "N_flux": N_flux,
            "N_tow": N_tow,
            "Q": Q,
            "f_max": f_max,
            "B_prime": B_prime,
        },
        "canonical_core_q0": {
            "cardinality": len(O),
            "monochrome_mod9": sorted(mod9),
            "bott_fibers": fiber_table,
            "fiber_sum": sum(beta.values()),
            "floor_B_prime_over_8": floor_fiber,
            "B_prime_mod_8": excess,
            "identity_8floor_plus_excess": floor_fiber * 8 + excess == B_prime,
            "unique_tower_bott_pairs": len(pairs),
            "classifying_map_injective": len(pairs) == B_prime,
            "unique_towers_touched": len(set(towers)),
        },
        "nine_cores": {
            "cardinality_union": sum(len(c) for c in cores),
            "each_size": [len(c) for c in cores],
            "each_mod9": [sorted({x % 9 for x in c}) for c in cores],
            "unique_q_tower_bott_triples": len(triples_9),
            "classifying_map_injective": len(triples_9) == 9 * B_prime,
        },
        "obstruction_O2": {
            "free_Z8_action_possible": (B_prime % 8 == 0),
            "reason": "8 does not divide B_prime" if B_prime % 8 else "8 divides B_prime",
        },
        "seed_equivariance_sample_50": {
            "min_fiber_values_seen": sorted(set(fiber_floors)),
            "injective_tower_bott_count": inject_ok,
        },
        "classical_bott_table_labels_only": {
            "0": "Z/2",
            "1": "Z/2",
            "2": "0",
            "3": "Z",
            "4": "0",
            "5": "0",
            "6": "0",
            "7": "Z",
        },
        "forbidden_claims": [
            "free T^sharp origin of 539 objects",
            "No-Go lift for lambda=ln3/539 from democracy alone",
            "pi_k(O) produces resonant trajectories",
        ],
    }

    out = Path(__file__).resolve().parents[1] / "architecture_A_ores_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))
    print("wrote", out)

    # Assertions for CI-style use
    assert results["canonical_core_q0"]["classifying_map_injective"]
    assert results["nine_cores"]["classifying_map_injective"]
    assert results["canonical_core_q0"]["identity_8floor_plus_excess"]
    assert not results["obstruction_O2"]["free_Z8_action_possible"]
    print("OK: Architecture A discrete layer on O_res")
    return 0


if __name__ == "__main__":
    sys.exit(main())
