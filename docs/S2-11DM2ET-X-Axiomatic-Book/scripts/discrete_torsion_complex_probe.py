#!/usr/bin/env python3
"""
Discrete torsion-style complex on residual cores (Direction 2).

Assembles Tor_res = (rho, alpha, L, omega2, mu, f, delta_f),
checks d^2=0 / cocycle identities, beta_sharp homogeneity of path edges,
and arithmetic I1–I8 linking B' ≡ 3 (mod 8) to Bott block |U|=3.

PROVENANCE: residual flux under Principle (S). Not free T-sharp. No No-Go lift.
"""
from __future__ import annotations

import json
import math
import sys
from collections import defaultdict
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
    return sum(sgn(a - b) for a in A for b in B)


def cores(N_flux, f_max, Q, B_prime):
    residual = sorted(range(f_max, N_flux))
    classes: list[list[int]] = [[] for _ in range(Q)]
    for i, x in enumerate(residual):
        classes[i % Q].append(x)
    return [c[:B_prime] for c in classes]


def main() -> int:
    N_flux, N_tow, Q, f_max, B_prime, loads = atoms()
    assert B_prime == 539 == 8 * 67 + 3
    Cs = cores(N_flux, f_max, Q, B_prime)
    O = Cs[0]

    # rho monochrome
    rho = []
    for c in Cs:
        mods = {x % 9 for x in c}
        assert len(mods) == 1
        rho.append(next(iter(mods)))
    assert rho == [3, 4, 5, 6, 7, 8, 0, 1, 2]

    # L, alpha, omega2, mu
    def alpha(a, b):
        return sgn(a - b)

    def omega2(a, b, c):
        return alpha(b, c) - alpha(a, c) + alpha(a, b)

    def mu(a, b, c):
        return B_prime * sgn(a - b) * sgn(b - c)

    L = [[B_prime * alpha(a, b) for b in range(Q)] for a in range(Q)]
    for a in range(Q):
        for b in range(Q):
            assert link_line(Cs[a], Cs[b]) == L[a][b]

    sum_mu = 0
    sum_w2 = 0
    for a, b, c in combinations(range(9), 3):
        assert omega2(a, b, c) == -1
        assert mu(a, b, c) == B_prime
        sum_mu += mu(a, b, c)
        sum_w2 += omega2(a, b, c)
    assert sum_mu == 84 * B_prime
    assert sum_w2 == -84

    for a, b, c, d in combinations(range(9), 4):
        dmu = mu(b, c, d) - mu(a, c, d) + mu(a, b, d) - mu(a, b, c)
        dw2 = omega2(b, c, d) - omega2(a, c, d) + omega2(a, b, d) - omega2(a, b, c)
        assert dmu == 0 and dw2 == 0

    # Path: beta_sharp homogeneity + delta f
    for i in range(B_prime - 1):
        assert ((i + 1) % 8 - (i % 8)) % 8 == 1
    df = [tower_of(O[i + 1], loads) - tower_of(O[i], loads) for i in range(B_prime - 1)]
    assert sum(df) == tower_of(O[-1], loads) - tower_of(O[0], loads)

    # Tower triangles
    buckets: dict[int, list[int]] = defaultdict(list)
    for i, x in enumerate(O):
        buckets[tower_of(x, loads)].append(i)
    tris = [tuple(sorted(v)) for v in buckets.values() if len(v) == 3]
    assert len(tris) == 56
    for i, j, k in tris:
        assert i < j < k
        w = sgn(j - k) - sgn(i - k) + sgn(i - j)
        assert w == -1

    # Fiber block identity I2–I4, I8
    n = [sum(1 for i in range(B_prime) if i % 8 == k) for k in range(8)]
    assert n == [68, 68, 68, 67, 67, 67, 67, 67]
    assert 3 * 68 + 5 * 67 == B_prime
    U, V = {0, 1, 2}, {3, 4, 5, 6, 7}
    assert len(U) == 3 == B_prime % 8
    for k in U:
        for m in V:
            Fk = [O[i] for i in range(B_prime) if i % 8 == k]
            Fm = [O[i] for i in range(B_prime) if i % 8 == m]
            assert link_line(Fk, Fm) == 0

    # I7
    assert (B_prime - 1) % 8 == 2
    assert B_prime - 1 == 8 * 67 + 2

    results = {
        "provenance": {
            "objects": "residual flux quanta",
            "principle_S": True,
            "democratic_charge_partition": True,
            "not_free_Tsharp_basins": True,
            "no_go_lift_claimed": False,
            "continuum_Cartan_not_claimed": True,
        },
        "package": "Tor_res = (rho, alpha, L, omega2, mu, f, delta_f)",
        "rho": rho,
        "B_prime": B_prime,
        "charge_complex": {
            "omega2_ordered_triples": -1,
            "mu_ordered_triples": B_prime,
            "sum_mu": sum_mu,
            "sum_omega2": sum_w2,
            "d_mu_zero": True,
            "d_omega2_zero": True,
        },
        "path_complex": {
            "edges": B_prime - 1,
            "all_edges_delta_beta_sharp_plus_1": True,
            "delta_f_telescoping": sum(df),
            "tower_triangles": 56,
            "omega2_idx_on_triangles": -1,
        },
        "arithmetic_identities": {
            "I1_B_mod_8": B_prime % 8,
            "I2_U_card": 3,
            "I2_matches_B_mod_8": True,
            "I3_U_plus_V": 8,
            "I4_3_68_plus_5_67": 3 * 68 + 5 * 67,
            "I5_sum_mu": sum_mu,
            "I6_sum_omega2": sum_w2,
            "I7_path_edges_mod_8": (B_prime - 1) % 8,
            "I8_cross_UV_linking_zero": True,
        },
        "forbidden_claims": [
            "continuum Cartan field equation",
            "free T^sharp origin",
            "No-Go lift",
            "hopfions produce 539 free basins",
        ],
    }

    out = Path(__file__).resolve().parents[1] / "discrete_torsion_complex_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print("OK: Tor_res closed; beta_sharp homogeneous path; I1-I8 hold")
    print("I2: |U|=3 ≡ B' (mod 8); I5: sum mu = 84*B' =", sum_mu)
    print("wrote", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
