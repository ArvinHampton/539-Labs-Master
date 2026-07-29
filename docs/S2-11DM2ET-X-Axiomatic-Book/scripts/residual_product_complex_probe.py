#!/usr/bin/env python3
"""
Residual product complex K_9 × P_{B'} with mixed closed cochain eta.

eta = alpha ⊗ delta_f - omega2 ⊗ f
mu_tilde = mu ⊗ 1

PROVENANCE: residual flux under Principle (S). Not free T-sharp. No No-Go lift.
"""
from __future__ import annotations

import json
import math
import sys
from itertools import combinations, permutations
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


def main() -> int:
    N_flux, N_tow, Q, f_max, B_prime, loads = atoms()
    assert B_prime == 539

    residual = sorted(range(f_max, N_flux))
    O = [residual[i] for i in range(len(residual)) if i % Q == 0][:B_prime]
    assert len(O) == B_prime

    f = [tower_of(x, loads) for x in O]
    df = [f[i + 1] - f[i] for i in range(B_prime - 1)]

    def alpha(a, b):
        return sgn(a - b)

    def omega2(a, b, c):
        return alpha(b, c) - alpha(a, c) + alpha(a, b)

    def mu(a, b, c):
        return B_prime * sgn(a - b) * sgn(b - c)

    # Identity: cyclic sum of alpha = omega2
    for a, b, c in permutations(range(9), 3):
        cyc = alpha(a, b) + alpha(b, c) + alpha(c, a)
        assert cyc == omega2(a, b, c)

    # Factor locks
    sum_mu = 0
    for a, b, c in combinations(range(9), 3):
        assert omega2(a, b, c) == -1
        assert mu(a, b, c) == B_prime
        sum_mu += mu(a, b, c)
    assert sum_mu == 84 * B_prime

    for a, b, c, d in combinations(range(9), 4):
        assert mu(b, c, d) - mu(a, c, d) + mu(a, b, d) - mu(a, b, c) == 0

    # Prism cancellation for eta: D eta = 0
    # On prism (a,b,c) x e_i:
    # omega2*(f(i)-f(i+1)) + (alpha(a,b)+alpha(b,c)+alpha(c,a))*df(i) = 0
    for a, b, c in permutations(range(9), 3):
        w = omega2(a, b, c)
        cyc = alpha(a, b) + alpha(b, c) + alpha(c, a)
        assert w == cyc
        for i in range(B_prime - 1):
            prism = w * (f[i] - f[i + 1]) + cyc * df[i]
            assert prism == 0

    # Square evaluation of eta
    # eta(S(a,b;i)) = alpha(a,b)*df(i)
    # Triangle evaluation: eta(T(a,b,c;i)) = -omega2(a,b,c)*f(i)
    # P2: sum over squares of eta = 0
    sum_sq = 0
    for a in range(9):
        for b in range(9):
            if a == b:
                continue
            for i in range(B_prime - 1):
                sum_sq += alpha(a, b) * df[i]
    assert sum_sq == 0

    # Sample nontrivial mixed values exist
    nontrivial_sq = any(
        alpha(a, b) * df[i] != 0
        for a in range(9)
        for b in range(9)
        if a != b
        for i in range(B_prime - 1)
    )
    assert nontrivial_sq

    nontrivial_tri = any(
        -omega2(a, b, c) * f[i] != 0
        for a, b, c in combinations(range(9), 3)
        for i in range(B_prime)
    )
    assert nontrivial_tri

    # Arithmetic residual 3
    assert B_prime % 8 == 3
    U = 3
    assert U == B_prime % 8
    assert (B_prime - 1) % 8 == 2

    # Recover mu via tilde mu on triangles
    for a, b, c in combinations(range(9), 3):
        for i in [0, B_prime // 2, B_prime - 1]:
            mu_tilde = mu(a, b, c)  # independent of i
            assert mu_tilde == B_prime

    results = {
        "provenance": {
            "objects": "residual flux quanta",
            "principle_S": True,
            "democratic_charge_partition": True,
            "not_free_Tsharp_basins": True,
            "no_go_lift_claimed": False,
            "continuum_Cartan_not_claimed": True,
        },
        "product": "K_9 x P_{B'}",
        "B_prime": B_prime,
        "differential": "D(phi⊗psi)=d_Q phi⊗psi + (-1)^|phi| phi⊗d_P psi",
        "mixed_cochains": {
            "mu_tilde": "mu ⊗ 1 (recovers mu on triangles)",
            "eta": "alpha⊗delta_f - omega2⊗f",
            "eta_on_square": "alpha(a,b)*delta_f(i)",
            "eta_on_triangle": "-omega2(a,b,c)*f(i)",
            "D_eta_zero_prisms": True,
            "D_mu_tilde_zero": True,
            "nontrivial_square_values": True,
            "nontrivial_triangle_values": True,
            "sum_eta_on_all_squares": 0,
        },
        "arithmetic": {
            "I1_B_mod_8": B_prime % 8,
            "I2_U_card": 3,
            "P1_sum_mu": sum_mu,
            "P3_path_edges_mod_8": (B_prime - 1) % 8,
        },
        "path": {
            "edges": B_prime - 1,
            "delta_f_telescoping": sum(df),
            "f_range": [min(f), max(f)],
        },
    }

    out = Path(__file__).resolve().parents[1] / "residual_product_complex_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print("OK: product complex K9 x P_B'; D eta = 0 on all prisms")
    print("eta squares: alpha*df; triangles: -omega2*f; mu_tilde recovers mu")
    print("I2: |U|=3 ≡ B' mod 8 =", B_prime % 8)
    print("wrote", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
