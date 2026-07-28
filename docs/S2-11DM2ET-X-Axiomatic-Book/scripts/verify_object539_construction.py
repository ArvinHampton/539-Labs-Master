#!/usr/bin/env python3
"""
Verify non-circular combinatorial 539-object construction O_res.

See: Object539_NonCircular_Construction.md
"""
from __future__ import annotations

import math
import random
import sys


def equitable_partition(residual: set[int], q: int = 9) -> list[set[int]]:
    items = sorted(residual)
    classes: list[set[int]] = [set() for _ in range(q)]
    for i, x in enumerate(items):
        classes[i % q].add(x)
    return classes


def core_of(class_set: set[int], b_prime: int) -> set[int]:
    return set(sorted(class_set)[:b_prime])


def main() -> int:
    N_flux = math.floor(math.e**3 * 3**5)
    N_tow = 3**5
    Q = 9
    f_max = math.ceil(N_flux / N_tow)
    assert N_flux == 4880 and N_tow == 243 and f_max == 21

    N_prime = N_flux - f_max
    B_prime = N_prime // Q
    # Count formula: no numeral 539 on RHS
    assert B_prime == (N_flux - f_max) // 9
    assert B_prime == 539  # value check only

    Omega = set(range(N_flux))

    # Canonical seed + partition
    Seed = set(range(f_max))
    R = Omega - Seed
    assert len(R) == N_prime
    classes = equitable_partition(R, Q)
    sizes = [len(c) for c in classes]
    assert sum(sizes) == N_prime
    assert max(sizes) - min(sizes) <= 1
    assert min(sizes) == B_prime

    O_res = core_of(classes[0], B_prime)
    assert len(O_res) == B_prime == 539
    assert O_res.isdisjoint(Seed)
    assert O_res <= classes[0] <= R <= Omega

    # Nine parallel cores, pairwise disjoint, each size B'
    cores = [core_of(c, B_prime) for c in classes]
    assert all(len(c) == B_prime for c in cores)
    for i in range(Q):
        for j in range(i + 1, Q):
            assert cores[i].isdisjoint(cores[j])
    assert len(set().union(*cores)) == 9 * B_prime == N_prime - (N_prime % 9)

    # Stability: random seeds, equitable partition always min = B'
    random.seed(0)
    for _ in range(200):
        Seed_r = set(random.sample(range(N_flux), f_max))
        classes_r = equitable_partition(Omega - Seed_r, Q)
        assert min(len(c) for c in classes_r) == B_prime

    # Without (S): full Omega equitable split → min = floor(N/9) = 542
    full = equitable_partition(Omega, Q)
    assert min(len(c) for c in full) == N_flux // 9 == 542

    # Packaging agreement
    L_pref = math.floor(math.e**3 / math.log(3))
    L_body = (N_flux // 9) - f_max
    assert L_pref + L_body == B_prime == 539

    # 539 not in defining atoms
    atoms = {N_flux, N_tow, Q, f_max, N_prime, L_pref, L_body}
    assert 539 not in atoms

    print("OK: |O_res| = floor((N_flux - f_max)/9) =", len(O_res))
    print("OK: nine disjoint cores of size", B_prime)
    print("OK: 200 random seeds, equitable min always", B_prime)
    print("OK: without (S) min class =", N_flux // 9, "(not 539)")
    print("OK: non-circular combinatorial 539-set verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
