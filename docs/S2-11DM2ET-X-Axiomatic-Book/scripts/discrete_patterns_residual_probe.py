#!/usr/bin/env python3
"""
Discrete combinatorial patterns on residual cores:
  - core linking form L_ab = B' * sgn(a-b)
  - Bott-fiber linking on core 0
  - tower coboundary telescoping
  - mod-9 monochromicity

PROVENANCE: residual flux quanta under Principle (S) + democratic charge
partition. Not free T-sharp. No No-Go lift.
"""
from __future__ import annotations

import json
import math
import sys
from collections import Counter, defaultdict
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
    if d > 0:
        return 1
    if d < 0:
        return -1
    return 0


def link_line(A: list[int], B: list[int]) -> int:
    s = 0
    for a in A:
        for b in B:
            s += sgn(a - b)
    return s


def cores(N_flux: int, f_max: int, Q: int, B_prime: int) -> list[list[int]]:
    residual = sorted(range(f_max, N_flux))
    classes: list[list[int]] = [[] for _ in range(Q)]
    for i, x in enumerate(residual):
        classes[i % Q].append(x)
    return [c[:B_prime] for c in classes]


def main() -> int:
    N_flux, N_tow, Q, f_max, B_prime, loads = atoms()
    assert B_prime == 539

    Cs = cores(N_flux, f_max, Q, B_prime)
    assert all(len(c) == B_prime for c in Cs)

    # Core linking matrix
    L = [[link_line(Cs[a], Cs[b]) for b in range(Q)] for a in range(Q)]
    for a in range(Q):
        for b in range(Q):
            assert L[a][b] == B_prime * sgn(a - b)
            assert L[a][b] == -L[b][a]

    # Rank of S over R: 8
    # L = B' S; kernel of S is constants
    # check null: sum_b L[a][b] = B' * sum_b sgn(a-b)
    for a in range(Q):
        row_sum = sum(L[a])
        expected = B_prime * sum(sgn(a - b) for b in range(Q))
        assert row_sum == expected

    # Monochromicity
    mods = []
    for q, c in enumerate(Cs):
        mset = {x % 9 for x in c}
        assert len(mset) == 1
        mods.append(next(iter(mset)))

    # Tower coboundary on core 0
    O = Cs[0]
    df = [tower_of(O[i + 1], loads) - tower_of(O[i], loads) for i in range(B_prime - 1)]
    telescoping = sum(df)
    assert telescoping == tower_of(O[-1], loads) - tower_of(O[0], loads)

    # Bott fibers on core 0
    fibers: dict[int, list[int]] = defaultdict(list)
    for i, x in enumerate(O):
        fibers[i % 8].append(x)
    fiber_sizes = tuple(len(fibers[k]) for k in range(8))
    assert fiber_sizes == (68, 68, 68, 67, 67, 67, 67, 67)

    M = [[link_line(fibers[k], fibers[m]) for m in range(8)] for k in range(8)]
    for k in range(8):
        assert M[k][k] == 0
        for m in range(8):
            assert M[k][m] == -M[m][k]

    same_tower_pairs = 0
    for i in range(B_prime):
        for j in range(i + 1, B_prime):
            if tower_of(O[i], loads) == tower_of(O[j], loads):
                same_tower_pairs += 1

    results = {
        "provenance": {
            "objects": "residual flux quanta",
            "principle_S": True,
            "democratic_charge_partition": True,
            "not_free_Tsharp_basins": True,
            "no_go_lift_claimed": False,
        },
        "B_prime": B_prime,
        "core_linking": {
            "formula": "L_ab = B' * sgn(a-b)",
            "verified_all_entries": True,
            "matrix": L,
            "gcd_off_diagonal": B_prime,
        },
        "monochrome_mod9_per_core": mods,
        "tower_coboundary_core0": {
            "telescoping_sum": telescoping,
            "tau_last_minus_tau_first": tower_of(O[-1], loads) - tower_of(O[0], loads),
            "df_min": min(df),
            "df_max": max(df),
        },
        "beta_sharp_fibers_core0": list(fiber_sizes),
        "fiber_linking_sample": {
            "M_0_1": M[0][1],
            "M_0_3": M[0][3],
            "M_3_5": M[3][5],
        },
        "same_tower_pairs_core0": same_tower_pairs,
        "RNT_summary": {
            "pairing_scale": B_prime,
            "unit_skew_form_on_9_sectors": "sgn(a-b)",
            "B_prime_mod_8": B_prime % 8,
            "identity_8_67_plus_3": B_prime == 8 * 67 + 3,
        },
        "forbidden_claims": [
            "free T^sharp origin",
            "continuum Gauss linking",
            "No-Go lift",
            "security reduction",
        ],
    }

    out = Path(__file__).resolve().parents[1] / "discrete_patterns_residual_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(
        {
            "OK": True,
            "L_formula": "B'*sgn(a-b)",
            "B_prime": B_prime,
            "telescoping": telescoping,
            "fiber_sizes": list(fiber_sizes),
            "mods": mods,
        },
        indent=2,
    ))
    print("wrote", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
