#!/usr/bin/env python3
"""Muon g-2 Path A prefactor + window average / Path B residual.

S2-11DM2ET-X / HQCC oscillatory correction:
  delta a_mu^(55) = A * sin(2*pi*t/T + phi0)

Path A: long-window mean -> 0 (bound A*T/(2*pi*Tw))
Path B: residual ~ eps * A with eps = 61/4880

Run: python3 muon_g2_prefactor_average.py
"""
from __future__ import annotations

import json
import math
from pathlib import Path

A_AMP = 2.51e-9
T_FLUX = 539.90  # seconds
EPS = 61 / 4880
A_EXP_ERR = 14.5e-11
DELTA_LAT = 38e-11
DELTA_LAT_ERR = 63e-11


def mean_residual(T_days: float, phi0: float = 0.0) -> float:
    T_sec = T_days * 86400.0
    omega = 2.0 * math.pi / T_FLUX
    mean = (1.0 / T_sec) * (1.0 / omega) * (
        -math.cos(omega * T_sec + phi0) + math.cos(phi0)
    )
    return A_AMP * mean


def bound_residual(T_days: float) -> float:
    T_sec = T_days * 86400.0
    return A_AMP * (T_FLUX / (2.0 * math.pi * T_sec))


def max_abs_mean(T_days: float, n_phase: int = 720) -> tuple[float, float]:
    best = 0.0
    best_phi = 0.0
    for i in range(n_phase):
        phi = 2.0 * math.pi * i / n_phase
        r = abs(mean_residual(T_days, phi))
        if r > best:
            best = r
            best_phi = phi
    return best, best_phi


def main() -> None:
    windows = [1, 7, 30, 365]
    window_rows = []
    for d in windows:
        b = bound_residual(d)
        m0 = mean_residual(d, 0.0)
        mx, ph = max_abs_mean(d)
        window_rows.append(
            {
                "T_days": d,
                "bound": b,
                "bound_e11": b * 1e11,
                "mean_phi0": m0,
                "mean_phi0_e11": m0 * 1e11,
                "max_abs_mean": mx,
                "max_abs_mean_e11": mx * 1e11,
                "max_phi": ph,
                "bound_over_exp_err": b / A_EXP_ERR,
            }
        )

    path_b = EPS * A_AMP
    results = {
        "formula": "delta_a_mu_55 = A * sin(2*pi*t/T + phi0)",
        "A_amp": A_AMP,
        "A_amp_e11": A_AMP * 1e11,
        "T_flux_s": T_FLUX,
        "eps": EPS,
        "eps_pct": EPS * 100.0,
        "path_A": {
            "statement": "long-window average nulls oscillatory term",
            "windows": window_rows,
        },
        "path_B": {
            "statement": "residual ~ eps * A if topological absorption incomplete",
            "residual": path_b,
            "residual_e11": path_b * 1e11,
            "over_exp_err": path_b / A_EXP_ERR,
            "over_lat_err": path_b / DELTA_LAT_ERR,
        },
        "external": {
            "a_exp_err_e11": A_EXP_ERR * 1e11,
            "delta_lat_e11": DELTA_LAT * 1e11,
            "delta_lat_err_e11": DELTA_LAT_ERR * 1e11,
        },
        "verdict": "Path A primary; Path B sub-dominant residual; eps matches O(1%) pipi",
    }

    out = Path(__file__).resolve().parents[1] / "muon_g2_resolution_results.json"
    # when run from repo book root scripts/, parents[1] is book dir
    print(json.dumps(results, indent=2))
    try:
        out.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {out}")
    except OSError:
        pass

    # sanity checks
    assert EPS == 0.0125
    assert bound_residual(30) < A_EXP_ERR
    assert path_b < A_EXP_ERR
    print("OK: Path A 30d bound and Path B residual both < exp error")


if __name__ == "__main__":
    main()
