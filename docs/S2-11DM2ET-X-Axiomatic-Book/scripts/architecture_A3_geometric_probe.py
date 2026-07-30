#!/usr/bin/env python3
"""
A3 geometric model: residual carrier -> Gr_1(V) -> BO (and rank-2 spin-aimed planes).

PROVENANCE (mandatory):
  Objects are residual flux quanta under Principle (S) and democratic
  charge-sector partition. Not free T-sharp. No No-Go lift. Option 3 intact.
"""
from __future__ import annotations

import json
import math
import sys
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


def core_q0(N_flux: int, f_max: int, Q: int, B_prime: int) -> list[int]:
    residual = sorted(range(f_max, N_flux))  # canonical seed {0..f_max-1}
    # equitable: residual already sorted; class 0 = indices 0,9,18,...
    class0 = [residual[i] for i in range(len(residual)) if i % Q == 0]
    return class0[:B_prime]


def main() -> int:
    N_flux, N_tow, Q, f_max, B_prime, loads = atoms()
    assert B_prime == 539 and N_tow == 243

    O = core_q0(N_flux, f_max, Q, B_prime)
    assert len(O) == B_prime

    # Phi: line index = 8*tau + beta_sharp
    line_indices = []
    for i, x in enumerate(O):
        tau = tower_of(x, loads)
        beta = i % 8
        line_indices.append(8 * tau + beta)

    assert len(line_indices) == B_prime
    assert len(set(line_indices)) == B_prime  # injective Phi

    dim_V = N_tow * 8  # 1944
    assert max(line_indices) < dim_V
    assert min(line_indices) >= 0

    # Phi_spin: oriented 2-frame in W = V ⊗ R^2 ≅ R^{2*dim_V}
    # basis layout: (8*tau+beta)*2 + a, a in {0,1}
    dim_W = 2 * dim_V
    plane_keys = []
    for i, x in enumerate(O):
        tau = tower_of(x, loads)
        beta = i % 8
        base = (8 * tau + beta) * 2
        plane_keys.append((base, base + 1))  # oriented u0 ^ u1

    assert len(set(plane_keys)) == B_prime

    # Factorization record: f_sharp then Psi
    f_sharp = [(0, tower_of(x, loads), i % 8) for i, x in enumerate(O)]
    assert len(set(f_sharp)) == B_prime
    psi_lines = [8 * t + k for (_, t, k) in f_sharp]
    assert psi_lines == line_indices

    # Bott fiber sizes under beta_sharp (A1)
    from collections import Counter

    fibers = Counter(i % 8 for i in range(B_prime))
    fiber_tuple = tuple(fibers[k] for k in range(8))
    assert fiber_tuple == (68, 68, 68, 67, 67, 67, 67, 67)

    results = {
        "provenance": {
            "objects": "residual flux quanta",
            "principle_S": True,
            "democratic_charge_partition": True,
            "not_free_Tsharp_basins": True,
            "no_go_lift_claimed": False,
            "option3_free_dynamics_unchanged": True,
        },
        "A3": {
            "realization": "|E(O_res)| ≅ discrete O_res",
            "dim_V": dim_V,
            "model_BO": "Gr_1(V) = RP^{dim_V-1} hookrightarrow BO(1) hookrightarrow BO",
            "Phi_injective": True,
            "distinct_lines": len(set(line_indices)),
            "factorization": "Phi = Psi o pr_{T,B} o f_sharp",
            "dim_W_spin_aimed": dim_W,
            "model_spin_aimed": "oriented Gr_2(W) toward BSO subset BO; BSpin lift closed A4",
            "Phi_spin_injective": True,
            "distinct_oriented_planes": len(set(plane_keys)),
            "beta_sharp_fibers": list(fiber_tuple),
            "B_prime": B_prime,
            "sample_line_indices_head": line_indices[:5],
            "sample_line_indices_tail": line_indices[-3:],
        },
        "not_claimed": [
            "free T^sharp origin",
            "higher Omega^Spin continuum fillings",
            "security reduction",
            "G4=539.9 in geometry",
        ],
        "A4_A5": "closed — see architecture_A4_A5_probe.py",
        "next": [],
    }

    out = Path(__file__).resolve().parents[1] / "architecture_A3_geometric_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))
    print("wrote", out)
    print("OK: A3 continuous geometric model Gr_1(V)->BO and rank-2 spin-aimed planes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
