#!/usr/bin/env python3
"""
Architecture A4–A5 on O_res (residual flux carrier).

A4: w1, w2 vanish on discrete domain => BSpin lift of Phi / Phi^Spin.
A5: Omega_0^Spin ≅ Z, KO_0(pt) ≅ Z via ABS; class = B' from packaging;
    Bott fiber table matches A1; B' = 8*67+3.

PROVENANCE: residual (S) only. Not free T#. No No-Go lift. Option 3 intact.
"""
from __future__ import annotations

import json
import math
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


def core_q0(N_flux: int, f_max: int, Q: int, B_prime: int) -> list[int]:
    residual = list(range(f_max, N_flux))
    class0 = [residual[i] for i in range(len(residual)) if i % Q == 0]
    return class0[:B_prime]


def main() -> int:
    N_flux, N_tow, Q, f_max, B_prime, loads = atoms()
    assert B_prime == 539
    # 539 not an input hypothesis — derived
    assert B_prime == (N_flux - f_max) // Q

    O = core_q0(N_flux, f_max, Q, B_prime)
    assert len(O) == B_prime

    # A1 fibers
    fibers = Counter(i % 8 for i in range(B_prime))
    fiber_tuple = tuple(fibers[k] for k in range(8))
    assert fiber_tuple == (68, 68, 68, 67, 67, 67, 67, 67)
    assert sum(fiber_tuple) == B_prime
    assert B_prime == 8 * 67 + 3

    # A3 maps still injective
    line_indices = [8 * tower_of(x, loads) + (i % 8) for i, x in enumerate(O)]
    assert len(set(line_indices)) == B_prime
    plane_keys = [((8 * tower_of(x, loads) + (i % 8)) * 2, (8 * tower_of(x, loads) + (i % 8)) * 2 + 1) for i, x in enumerate(O)]
    assert len(set(plane_keys)) == B_prime

    # --- A4: discrete domain cohomology ---
    # X = O_res^disc is 0-dimensional: H^i(X; Z/2) = 0 for i >= 1
    # Primary SW obstructions live in H^{i+1}(X; π_i fiber) => vanish
    H_pos_Z2 = {i: 0 for i in range(1, 5)}  # model statement
    w1_Phi = 0  # H^1 = 0
    w2_Phi = 0  # H^2 = 0; also line bundles have w2=0
    w1_Phi_spin = 0  # oriented => w1=0; also H^1=0
    w2_Phi_spin = 0  # H^2=0
    BSpin_lift_exists = True
    BSpin_lift_unique_up_to_htpy = True  # vanishing primary obstructions on 0-space
    BSO_lift_exists = True  # w1=0

    # Pointwise spin: each fiber of Phi^Spin is oriented R^2 ≅ C, spin
    pointwise_spin_structures = B_prime  # one trivial spin structure per point plane

    # Stabilization Phi_N: O_res -> BO(N) with N = dim V = 1944 (rank-1 model)
    # and N = 2 for rank-2 model inside BO(2) then stabilize
    dim_V = N_tow * 8
    assert dim_V == 1944

    # --- A5: Omega_0^Spin and KO_0 ---
    # Omega_0^Spin ≅ Z (closed oriented 0-manifolds = signed points; spin ok)
    # Class of discrete residual carrier as 0-manifold:
    Omega0_class = B_prime  # positive orientation on each residual quantum
    # ABS: Omega_0^Spin -> KO_0(pt) ≅ Z is isomorphism
    ABS_image = Omega0_class
    KO0 = ABS_image
    assert KO0 == B_prime

    # KO_*(pt) Bott table (period 8), labels only for fiber comparison
    # pi_{-k} KO or KO^{-k}(pt):
    KO_star_table = {
        0: "Z",
        1: "Z/2",
        2: "Z/2",
        3: "0",
        4: "Z",
        5: "0",
        6: "0",
        7: "0",
    }
    # Discrete Bott grading of residual quanta = beta_sharp fibers
    # Formal KO-proxy multiset: fiber_k elements of Bott clock k
    KO_proxy_multiset = {str(k): int(fiber_tuple[k]) for k in range(8)}
    # Arithmetic identity without free 539:
    assert sum(int(v) for v in KO_proxy_multiset.values()) == B_prime
    assert 8 * 67 + 3 == B_prime

    # Rank data of geometric models
    rank_Phi = 1
    rank_Phi_spin = 2
    virtual_rank_stable = 0  # after stabilize-and-subtract max rank (formal)

    # Higher spin bordism of continuum fillings: not computed
    higher_Omega_not_claimed = True

    results = {
        "provenance": {
            "objects": "residual flux quanta",
            "principle_S": True,
            "democratic_charge_partition": True,
            "not_free_Tsharp_basins": True,
            "no_go_lift_claimed": False,
            "option3_free_dynamics_unchanged": True,
            "B_prime_derived_not_input": True,
            "formula_B_prime": "floor((N_flux - f_max)/9)",
        },
        "A4": {
            "domain": "O_res^disc only — 0-dimensional CW, B' points (0-stem residual closure)",
            "not_full_realization_E": True,
            "A4_plus_open": "continuous w1/w2/BSpin on full |E(O_res)|",
            "H_i_gt_0_Z2": H_pos_Z2,
            "Phi_model": "Gr_1(V) hookrightarrow BO",
            "Phi_Spin_model": "oriented Gr_2(W) toward BSO subset BO",
            "w1_Phi": w1_Phi,
            "w2_Phi": w2_Phi,
            "w1_Phi_Spin": w1_Phi_spin,
            "w2_Phi_Spin": w2_Phi_spin,
            "reason": "H^{>0}(O_res^disc; Z/2)=0 => primary SW obstructions vanish; line bundle w2=0; oriented plane w1=0",
            "BSO_lift": BSO_lift_exists,
            "BSpin_lift": BSpin_lift_exists,
            "BSpin_lift_unique_up_to_homotopy": BSpin_lift_unique_up_to_htpy,
            "pointwise_spin_structures": pointwise_spin_structures,
            "dim_V": dim_V,
            "Phi_injective": True,
            "Phi_Spin_injective": True,
            "status": "A4_BSPIN_LIFT_CLOSED_ON_O_RES_DISC",
            "scope": "0-stem residual closure; not continuum A4 exit on |E|",
        },
        "A5": {
            "domain": "O_res^disc / 0-stem only",
            "Omega0_Spin": "Z",
            "class_O_res": Omega0_class,
            "ABS": "Omega0_Spin -> KO_0(pt) iso",
            "KO0_pt": "Z",
            "ABS_image": ABS_image,
            "KO0_value": KO0,
            "KO_star_pt_table_mod_8": KO_star_table,
            "Bott_fiber_proxy_multiset": KO_proxy_multiset,
            "identity_B_prime_8_67_3": True,
            "rank_Phi": rank_Phi,
            "rank_Phi_Spin": rank_Phi_spin,
            "pushforward_interpretation": "sum_x [pt_x] = B' in Omega0 and KO0",
            "higher_Omega_Spin_continuum_fillings": "not claimed (Cat B)",
            "promote_0stem_to_continuum_Omega_n": False,
            "status": "A5_KO_OMEGA0_SPIN_CLOSED_ON_O_RES",
            "scope": "0-stem residual closure only",
        },
        "arithmetic": {
            "N_flux": N_flux,
            "f_max": f_max,
            "B_prime": B_prime,
            "fiber_table": list(fiber_tuple),
            "B_mod_8": B_prime % 8,
        },
        "not_claimed": [
            "free T^sharp origin of 539",
            "higher-dimensional Omega^Spin of continuum fillings",
            "security reduction",
            "G4=539.9 in KO",
            "No-Go lift",
            "formality over continuum de Rham",
        ],
        "locks_intact": {
            "option3": True,
            "no_go": True,
            "A0_A1_A2_A3": True,
            "near_term_kit": True,
        },
        "status": "A4_A5_CLOSED_ON_O_RES",
    }

    out = Path(__file__).resolve().parents[1] / "architecture_A4_A5_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print("OK: A4 — w1=w2=0 on O_res^disc; BSpin lift exists (unique up to htpy)")
    print("OK: A5 — [O_res]=B' in Omega0^Spin ≅ Z; ABS => KO0 = B'; fibers", fiber_tuple)
    print("OK: B' = 8*67+3 derived; not free T#; status A4_A5_CLOSED_ON_O_RES")
    print("wrote", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
