#!/usr/bin/env python3
"""
Named GHK bump f and numerical M_j = max |f^{(j)}| on (0,1).

f_raw(t) = exp(-1/(t(1-t))) on (0,1), f = f_raw / mass.
Used with the majorant tree in RH_M1_2_Explicit_Hybrid_Constants.md
to produce admissible (crude) upper bounds on c1, c2 for K=2.

DIAGNOSTIC / EXPLICIT-CONSTANTS ONLY — no RH / M1.2 proof claim.
Status: RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

try:
    import mpmath as mp
except ImportError as e:
    raise SystemExit("mpmath required") from e


def raw_bump(t: float) -> float:
    if t <= 0.0 or t >= 1.0:
        return 0.0
    return math.exp(-1.0 / (t * (1.0 - t)))


def compute_mass(n: int = 50001) -> float:
    xs = np.linspace(1e-12, 1.0 - 1e-12, n)
    ys = np.array([raw_bump(float(x)) for x in xs])
    return float(np.trapezoid(ys, xs))


def max_derivative(j: int, mass: float, n_grid: int = 4001, dps: int = 35) -> float:
    mp.mp.dps = dps
    mass_mp = mp.mpf(mass)

    def f(t):
        # t is mpmath mpf
        if t <= 0 or t >= 1:
            return mp.mpf(0)
        return mp.exp(-1 / (t * (1 - t))) / mass_mp

    mx = mp.mpf(0)
    # denser near ends where bump flattens but derivatives can spike
    for k in range(1, n_grid):
        t = mp.mpf(k) / n_grid
        try:
            if j == 0:
                v = abs(f(t))
            else:
                v = abs(mp.diff(f, t, j))
            if v > mx:
                mx = v
        except Exception:
            continue
    # safety factor 1.05 for grid undershoot — still explicit
    return float(mx * mp.mpf("1.05"))


def main() -> int:
    mass = compute_mass()
    Ms = []
    for j in range(0, 5):
        n_grid = 2001 if j <= 2 else 1501
        mj = max_derivative(j, mass, n_grid=n_grid)
        Ms.append(mj)
        print(f"M_{j} <= {mj:.6g} (with 5% grid safety)", flush=True)

    # Majorant package from RH_M1_2_Explicit_Hybrid_Constants.md (crude, admissible)
    A2 = 24
    D2 = 16
    C_tail = 2
    C_mul = 2
    M2 = Ms[2]
    c1_upper = 2 * C_mul * D2 * A2 * M2  # = 1536 * M2
    c2_upper = 2 * C_mul * C_tail  # = 8

    out = {
        "provenance": {
            "status_label": "RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF",
            "proves_RH": False,
            "proves_M1_2": False,
            "model_constants": False,
            "note": (
                "Admissible majorants only; not sharp GHK implied constants. "
                "See RH_M1_2_Explicit_Hybrid_Constants.md and RH_M1_2_Named_f_ci_Bounds.md"
            ),
        },
        "named_f": {
            "formula": "f(t) = exp(-1/(t(1-t))) / mass on (0,1), 0 at endpoints",
            "mass_raw_trapezoid": mass,
            "class": "C^infty compactly supported in (0,1) after extension by 0",
        },
        "M_j_upper": {f"M_{j}": Ms[j] for j in range(5)},
        "majorant_package": {
            "K": 2,
            "A_2": A2,
            "D_2": D2,
            "C_tail": C_tail,
            "C_mul": C_mul,
            "formula_c1": "2*C_mul*D_2*A_2*M_2",
            "formula_c2": "2*C_mul*C_tail",
        },
        "bounds": {
            "c1_upper": c1_upper,
            "c2_upper": c2_upper,
            "c3": "symbolic under HD — not numerical here",
        },
        "status": "NAMED_F_M_K_BOUNDS_EXECUTED_NO_PROOF_CLAIM",
    }

    path = Path(__file__).resolve().parents[1] / "rh_named_f_M_K_results.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("c1_upper <=", c1_upper)
    print("c2_upper <=", c2_upper)
    print("wrote", path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
