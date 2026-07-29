#!/usr/bin/env python3
"""
Discrete combinatorial patterns on residual cores (dir. 1 extended):
  - core linking L_ab = B' * sgn(a-b)
  - fiber linking closed form
  - same-tower incidence spectrum
  - 2-cochains omega2 = d alpha, mu Massey-style cocycle

PROVENANCE: residual flux under Principle (S) + democratic charge partition.
Not free T-sharp. No No-Go lift.
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


def sgn(d: int) -> int:
    return (d > 0) - (d < 0)


def link_line(A, B) -> int:
    s = 0
    for a in A:
        for b in B:
            s += sgn(a - b)
    return s


def cores(N_flux, f_max, Q, B_prime):
    residual = sorted(range(f_max, N_flux))
    classes: list[list[int]] = [[] for _ in range(Q)]
    for i, x in enumerate(residual):
        classes[i % Q].append(x)
    return [c[:B_prime] for c in classes]


def main() -> int:
    N_flux, N_tow, Q, f_max, B_prime, loads = atoms()
    assert B_prime == 539
    Cs = cores(N_flux, f_max, Q, B_prime)

    # --- Core linking ---
    L = [[link_line(Cs[a], Cs[b]) for b in range(Q)] for a in range(Q)]
    for a in range(Q):
        for b in range(Q):
            assert L[a][b] == B_prime * sgn(a - b)

    # --- Fiber linking closed form ---
    O = Cs[0]
    fibers = defaultdict(list)
    for i, x in enumerate(O):
        fibers[i % 8].append(x)
    n = [len(fibers[k]) for k in range(8)]
    assert tuple(n) == (68, 68, 68, 67, 67, 67, 67, 67)
    M = [[0] * 8 for _ in range(8)]
    for k in range(8):
        for m in range(8):
            actual = link_line(fibers[k], fibers[m])
            if n[k] == n[m]:
                expected = n[k] * sgn(k - m)
            else:
                expected = 0
            assert actual == expected, (k, m, actual, expected)
            M[k][m] = actual

    # --- Same-tower incidence ---
    buckets: dict[int, list[int]] = defaultdict(list)
    for i, x in enumerate(O):
        buckets[tower_of(x, loads)].append(i)
    size_mult = Counter(len(v) for v in buckets.values())
    assert size_mult[1] == 1 and size_mult[2] == 185 and size_mult[3] == 56
    assert sum(s * c for s, c in size_mult.items()) == B_prime
    edges = sum(len(v) * (len(v) - 1) // 2 for v in buckets.values())
    assert edges == 353
    eigs: list[int] = []
    for v in buckets.values():
        nn = len(v)
        eigs.append(nn - 1)
        eigs.extend([-1] * (nn - 1))
    ecount = Counter(eigs)
    assert ecount[2] == 56 and ecount[1] == 185 and ecount[0] == 1 and ecount[-1] == 297
    assert sum(eigs) == 0
    assert len(buckets) == 242

    # --- 2-cochains ---
    def alpha(a, b):
        return sgn(a - b)

    def omega2(a, b, c):
        return alpha(b, c) - alpha(a, c) + alpha(a, b)

    def mu(a, b, c):
        return B_prime * sgn(a - b) * sgn(b - c)

    def d_mu(a, b, c, d):
        return mu(b, c, d) - mu(a, c, d) + mu(a, b, d) - mu(a, b, c)

    def d_omega2(a, b, c, d):
        return omega2(b, c, d) - omega2(a, c, d) + omega2(a, b, d) - omega2(a, b, c)

    for a, b, c in combinations(range(9), 3):
        assert omega2(a, b, c) == -1
        assert sgn(a - b) * sgn(b - c) * sgn(c - a) == 1

    for a, b, c, d in combinations(range(9), 4):
        assert d_mu(a, b, c, d) == 0
        assert d_omega2(a, b, c, d) == 0

    # Tower coboundary telescoping
    df = [tower_of(O[i + 1], loads) - tower_of(O[i], loads) for i in range(B_prime - 1)]
    assert sum(df) == tower_of(O[-1], loads) - tower_of(O[0], loads)

    results = {
        "provenance": {
            "objects": "residual flux quanta",
            "principle_S": True,
            "democratic_charge_partition": True,
            "not_free_Tsharp_basins": True,
            "no_go_lift_claimed": False,
        },
        "B_prime": B_prime,
        "core_linking_formula": "B'*sgn(a-b)",
        "fiber_linking": {
            "closed_form": "n_k*sgn(k-m) if n_k==n_m else 0",
            "fiber_sizes": n,
            "matrix": M,
            "blocks": {"U": [0, 1, 2], "V": [3, 4, 5, 6, 7], "cross": 0},
        },
        "same_tower_incidence": {
            "size_multiset": {str(k): int(v) for k, v in sorted(size_mult.items())},
            "towers_touched": 242,
            "edges": edges,
            "eigenvalue_multiset": {str(k): int(v) for k, v in sorted(ecount.items())},
            "rank_Z": 242,
        },
        "two_cochains": {
            "omega2_on_ordered_triples": -1,
            "omega2_is_coboundary_d_alpha": True,
            "mu_is_2_cocycle_on_ordered_4_sets": True,
            "triple_sign_product_ordered": 1,
        },
        "tower_coboundary_telescoping": sum(df),
    }

    out = Path(__file__).resolve().parents[1] / "discrete_patterns_residual_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print("OK: core linking, fiber closed form, incidence spectrum, 2-cochains")
    print("fiber form: n*sgn if equal size else 0; blocks U(68)/V(67), cross=0")
    print("incidence eigs:", dict(ecount))
    print("wrote", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
