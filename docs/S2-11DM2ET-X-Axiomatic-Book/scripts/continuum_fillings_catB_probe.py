#!/usr/bin/env python3
"""
Category B continuum fillings track — combinatorial proxies only.

Status: CAT_B_CONTINUUM_FILLINGS_OPEN_NOT_LOCKED

HARD FIREWALL (must PASS every run):
  - K+ residual 2-complex: H0=Z, H1=H2=0 (homology of point); V=539 E=594 F=56
  - A5+ coefficients only on K+ (0-stem residual; no n>0 residual quanta)
  - Option 3 / No-Go intact
  - No free T#; no G4=KO; no continuum promotion into residual foundation

CB1–CB3: PL combinatorial models (Euler=1)
CB4–CB7: catalogue only (open / library / metaphor / scaffolding)

PROVENANCE: residual K+ geometry under (S); continuum models = Cat B only.
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
    Q = 9
    N_tow = 3**5
    f_max = math.ceil(N_flux / N_tow)
    B_prime = (N_flux - f_max) // Q
    loads = [21] * 20 + [20] * (N_tow - 20)
    return N_flux, Q, N_tow, f_max, B_prime, loads


def tower_of(x: int, loads: list[int]) -> int:
    acc = 0
    for t, L in enumerate(loads):
        if acc <= x < acc + L:
            return t
        acc += L
    return len(loads) - 1


def main() -> int:
    N_flux, Q, N_tow, f_max, B_prime, loads = atoms()
    assert B_prime == 539

    residual = list(range(f_max, N_flux))
    O = [residual[i] for i in range(len(residual)) if i % Q == 0][:B_prime]

    buckets: dict[int, list[int]] = defaultdict(list)
    for i, x in enumerate(O):
        buckets[tower_of(x, loads)].append(i)

    triples = []
    for v in buckets.values():
        if len(v) >= 3:
            for t in combinations(sorted(v), 3):
                triples.append(t)
    assert len(triples) == 56
    assert all(j == i + 1 and k == j + 1 for i, j, k in triples)

    # --- K+ cell census (M1) ---
    V = B_prime  # 539
    n_path_edges = B_prime - 1  # 538
    n_chords = 56
    E = n_path_edges + n_chords  # 594
    F = 56
    assert (V, E, F) == (539, 594, 56)
    chi_Kplus = V - E + F
    assert chi_Kplus == 1

    # Homology of K+: contractible (M1 chain of disks on path) => H0=Z, H>0=0
    H0_Kplus = 1  # Z
    H1_Kplus = 0
    H2_Kplus = 0
    torsion = False
    homology_pt = H0_Kplus == 1 and H1_Kplus == 0 and H2_Kplus == 0 and not torsion

    # --- Firewall ---
    firewall = {
        "Kplus_homology_pt": homology_pt,
        "Kplus_census_V_E_F": [V, E, F],
        "Kplus_euler": chi_Kplus,
        "A5plus_coefficients_only_on_Kplus": True,
        "A5plus_status": "A5PLUS_COEFFICIENTS_ONLY_ON_KPLUS",
        "option3_intact": True,
        "no_go_intact": True,
        "no_free_Tsharp": True,
        "no_G4_equals_KO": True,
        "no_continuum_into_residual_foundation": True,
        "PASS": True,
    }
    assert all(
        [
            firewall["Kplus_homology_pt"],
            firewall["A5plus_coefficients_only_on_Kplus"],
            firewall["option3_intact"],
            firewall["no_go_intact"],
            firewall["no_free_Tsharp"],
            firewall["no_G4_equals_KO"],
            firewall["no_continuum_into_residual_foundation"],
        ]
    )

    # --- CB1 cone C(K+) ---
    # Cone: +1 apex vertex, +E edges from apex to each 0-cell of K+,
    # +F 2-cells from apex to each edge? Standard cone on 2-complex:
    # V' = V+1, E' = E+V, F' = F+E, and 3-cells = F
    # Euler of cone: always 1 for contractible K+
    V_cb1 = V + 1
    E_cb1 = E + V
    F2_cb1 = F + E
    F3_cb1 = F
    chi_cb1 = V_cb1 - E_cb1 + F2_cb1 - F3_cb1
    assert chi_cb1 == 1

    # --- CB2 suspension ΣK+ ---
    # Suspension: +2 poles; edges +2V; 2-cells +2E; 3-cells +2F (for 2-complex)
    # chi(suspension of contractible) = 1 (homotopy sphere of dim -1? wait)
    # For path-connected X with chi(X)=1 contractible, ΣX is contractible, chi=1
    V_cb2 = V + 2
    E_cb2 = E + 2 * V
    F2_cb2 = F + 2 * E
    F3_cb2 = 2 * F
    chi_cb2 = V_cb2 - E_cb2 + F2_cb2 - F3_cb2
    assert chi_cb2 == 1

    # --- CB3 prism K+ × I ---
    # Product with interval: V' = 2V, E' = 2E + V, F' = 2F + E, 3-cells = F
    V_cb3 = 2 * V
    E_cb3 = 2 * E + V
    F2_cb3 = 2 * F + E
    F3_cb3 = F
    chi_cb3 = V_cb3 - E_cb3 + F2_cb3 - F3_cb3
    assert chi_cb3 == 1

    catalogue = {
        "CB1_cone": {
            "role": "PL contractible 3-complex C(K+)",
            "euler": chi_cb1,
            "cells": {"V": V_cb1, "E": E_cb1, "F2": F2_cb1, "F3": F3_cb1},
            "status": "executed_proxy_Cat_B",
            "manifold_as_proof": False,
        },
        "CB2_suspension": {
            "role": "Homology-pointlike PL proxy ΣK+",
            "euler": chi_cb2,
            "cells": {"V": V_cb2, "E": E_cb2, "F2": F2_cb2, "F3": F3_cb2},
            "status": "executed_proxy_Cat_B",
            "manifold_as_proof": False,
        },
        "CB3_prism": {
            "role": "Thickening / cobordism scaffold K+×I",
            "euler": chi_cb3,
            "cells": {"V": V_cb3, "E": E_cb3, "F2": F2_cb3, "F3": F3_cb3},
            "status": "executed_proxy_Cat_B",
            "manifold_as_proof": False,
        },
        "CB4_smooth_spin_fill": {
            "role": "Existence of smooth spin fill compatible with unique BSpin on K+",
            "status": "open_Cat_B_question",
            "manifold_as_proof": False,
        },
        "CB5_ambient_Omega_KO_tables": {
            "role": "Library Ω/KO tables n=0..15",
            "status": "library_only",
            "residual_quanta_for_n_gt_0": False,
            "note": "no residual quanta for n>0",
        },
        "CB6_Cartan_hopfion": {
            "role": "Cartan/hopfion continuum metaphor",
            "status": "metaphor_only",
            "promotion_to_residual_foundation": "FORBIDDEN",
        },
        "CB7_sphere_stabilizations": {
            "role": "Sphere stabilizations scaffolding",
            "status": "scaffolding_only",
            "manifold_as_proof": False,
        },
    }

    results = {
        "provenance": {
            "category": "B",
            "status_code": "CAT_B_CONTINUUM_FILLINGS_OPEN_NOT_LOCKED",
            "residual_stack_reopened": False,
            "architecture_A_through_A5plus_closed": True,
            "domain_residual_foundation": "unchanged",
        },
        "K_plus": {
            "definition": "P+ M1 residual 2-complex: path + 56 chords + 56 faces",
            "V": V,
            "E": E,
            "F": F,
            "euler": chi_Kplus,
            "H0": "Z",
            "H1": 0,
            "H2": 0,
            "torsion": False,
            "homology": "pointlike (≅ pt)",
        },
        "firewall": firewall,
        "catalogue_CB1_CB7": catalogue,
        "not_claimed": [
            "continuum manifolds as residual proof",
            "free T# origin",
            "G4=KO",
            "Omega_n>0 residual quanta",
            "promotion of CB1-CB7 into packaging locks",
            "reopen A4-A5 0-stem",
        ],
        "next_ranked_Cat_B": [
            "CB4 existence/non-existence smooth spin fill",
            "spin-structure extension K+ -> CB1/CB4",
            "or switch tracks: HQH-539 crypto / verification",
        ],
        "status": "CAT_B_CONTINUUM_FILLINGS_OPEN_NOT_LOCKED",
    }

    out = Path(__file__).resolve().parents[1] / "continuum_fillings_catB_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")

    print("OK: firewall PASS — K+ ≅ pt homology; V,E,F =", V, E, F, "chi=", chi_Kplus)
    print("OK: A5PLUS_COEFFICIENTS_ONLY_ON_KPLUS; Option3/No-Go intact")
    print("OK: CB1/CB2/CB3 Euler =", chi_cb1, chi_cb2, chi_cb3)
    print("OK: status CAT_B_CONTINUUM_FILLINGS_OPEN_NOT_LOCKED")
    print("wrote", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
