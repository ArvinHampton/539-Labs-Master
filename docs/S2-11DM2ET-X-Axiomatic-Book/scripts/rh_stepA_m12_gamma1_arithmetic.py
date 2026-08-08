#!/usr/bin/env python3
"""
Step A/B arithmetic for RH solid direction 1.
RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF · ZLA · no model constants.
Does not prove O-TL / RH / Iso_H / Mass-with-A.
"""
from __future__ import annotations

import json
import math
from pathlib import Path


def fin(x, default=float("inf")):
    if isinstance(x, (int, float)) and math.isfinite(x):
        return float(x)
    return default


def gap_table():
    rows = []
    for b in [0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 0.98]:
        theta = 3.0 * (1.0 - b) / (2.0 - b)
        A_gm = 15.0 / (5.0 * b + 3.0)
        theta_gm = A_gm * (1.0 - b)
        if b <= 0.625:
            B1, zone = 8.604, "CS low [0.50,0.625]"
        elif b <= 0.875:
            B1, zone = 22.44, "CS mid [0.625,0.875]"
        else:
            B1, zone = None, "beyond CS; Bellotti-type near 1"
        rows.append(
            {
                "beta_star": b,
                "theta_Ingham_CS": theta,
                "theta_Guth_Maynard": theta_gm,
                "A_Guth_Maynard": A_gm,
                "CS_B1": B1,
                "CS_zone": zone,
                "N_shape": f"<< T^{theta:.4f} (log T)^3 [CS/Ingham]",
                "polylog_N_vert": False,
                "gap": f"must kill positive power T^{theta:.4f}",
            }
        )
    return rows


def m12_far(gamma, C_U, c_r, logX):
    Lg = math.log(gamma)
    r = c_r / Lg
    J = math.log2(max(2.0 * gamma / r, 2.0))
    # #A_j = 2^j r * Lg  => contrib_j = C_U * Lg / logX ; sum_j=0..J
    far = (J + 1.0) * C_U * Lg / logX
    compact = C_U * (Lg ** 2) / logX
    return {"far": far, "compact": compact, "J": J, "r": r, "Lg": Lg, "logX": logX}


def ghk(gamma, logX, c1=291.0, c2=8.0):
    # term1 = c1 * X^4 / (gamma^2 logX^2), logX = log X
    try:
        lt1 = math.log(c1) + 4.0 * logX - 2.0 * math.log(gamma) - 2.0 * math.log(max(logX, 1e-15))
        term1 = math.exp(lt1) if lt1 < 700 else float("inf")
    except Exception:
        term1 = float("inf")
    try:
        term2 = c2 * math.exp(-0.5 * logX) * logX
    except Exception:
        term2 = float("inf")
    total = term1 + term2 if math.isfinite(term1) and math.isfinite(term2) else float("inf")
    X = math.exp(logX) if logX < 700 else float("inf")
    return {"X": X, "term_X4": term1, "term_Xinv": term2, "E": total}


def add_row(rows, typ, meta, gamma, logX, target_far, eps0, C_U=2.0, c_r=0.25):
    m = m12_far(gamma, C_U, c_r, logX)
    g = ghk(gamma, logX)
    e = fin(g["E"])
    row = {
        "type": typ,
        **meta,
        "logX": logX,
        "X": g["X"] if math.isfinite(fin(g["X"])) else "inf",
        "far_sum": m["far"],
        "far_compact": m["compact"],
        "E_GHK": e if math.isfinite(e) else "inf",
        "term_X4": g["term_X4"] if math.isfinite(fin(g["term_X4"])) else "inf",
        "term_Xinv": g["term_Xinv"] if math.isfinite(fin(g["term_Xinv"])) else "inf",
        "far_ok": m["far"] <= target_far,
        "ghk_ok": e <= eps0,
        "both_ok": m["far"] <= target_far and e <= eps0,
    }
    rows.append(row)
    return row


def scan(gamma=3e12, target_far=0.4, eps0=0.1):
    Lg = math.log(gamma)
    rows = []
    for A_X in [4, 6, 8, 10, 12, 16, 20, 32, 64, 128, 256, 512, 1024, 2048]:
        logX = A_X * math.log(Lg)
        add_row(rows, "polylog_X", {"A_X": A_X}, gamma, logX, target_far, eps0)
    for a, c in [(0.5, 0.1), (0.5, 0.25), (0.5, 0.5), (0.6, 0.2), (1 / 3, 1.0), (0.4, 0.5)]:
        logX = c * (Lg ** a)
        if logX >= 0.49 * Lg:  # X >= gamma^0.49
            continue
        add_row(rows, "exp_log_power", {"a": a, "c": c}, gamma, logX, target_far, eps0)
    for delta in [0.005, 0.01, 0.02, 0.05, 0.08, 0.1, 0.15, 0.2]:
        logX = delta * Lg
        add_row(rows, "power_X", {"delta": delta}, gamma, logX, target_far, eps0)
    both = [r for r in rows if r["both_ok"]]
    return {
        "gamma": gamma,
        "n": len(rows),
        "n_both_ok": len(both),
        "n_far_only": sum(1 for r in rows if r["far_ok"] and not r["ghk_ok"]),
        "n_ghk_only": sum(1 for r in rows if r["ghk_ok"] and not r["far_ok"]),
        "first_both_ok": both[0] if both else None,
        "rows": rows,
    }


def required(gamma=3e12, target_far=0.4, C_U=2.0, c_r=0.25):
    Lg = math.log(gamma)
    r = c_r / Lg
    J = math.log2(max(2.0 * gamma / r, 2.0))
    logX_need = (J + 1.0) * C_U * Lg / target_far
    g = ghk(gamma, logX_need)
    return {
        "gamma": gamma,
        "logX_needed_for_far": logX_need,
        "X_needed": math.exp(logX_need) if logX_need < 700 else "inf",
        "X_over_gamma": math.exp(logX_need - Lg) if logX_need - Lg < 700 else "inf",
        "E_GHK_at_needed_X": fin(g["E"]) if math.isfinite(fin(g["E"])) else "inf",
        "joint_feasible_loose": fin(g["E"]) <= 0.1 and logX_need < 0.5 * Lg,
    }


def main():
    out_dir = Path(__file__).resolve().parents[1]
    gaps = gap_table()
    s1 = scan(3e12)
    s2 = scan(1e30)
    r1 = required(3e12)
    r2 = required(1e30)

    def score(r):
        far = fin(r["far_sum"])
        eg = fin(r["E_GHK"])
        return max(far / 0.4, eg / 0.1)

    top = sorted(s1["rows"], key=score)[:10]
    # strip heavy
    def slim(r):
        keys = [
            "type",
            "A_X",
            "a",
            "c",
            "delta",
            "logX",
            "X",
            "far_sum",
            "E_GHK",
            "far_ok",
            "ghk_ok",
            "both_ok",
        ]
        return {k: r[k] for k in keys if k in r}

    results = {
        "status": "RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF",
        "date": "2026-08-08",
        "zla": True,
        "no_model_constants": True,
        "does_not_prove": [
            "O-TL",
            "RH",
            "Iso_H",
            "Mass-with-A",
            "unconditional uniform M1.2",
        ],
        "density_input": {
            "primary": "Chourasiya-Simonic arXiv:2507.15184",
            "H_RH": 3e12,
            "local_count": "R-vM scale #zeros in height H << H log gamma",
        },
        "step_B_gap_table": gaps,
        "step_A_required_H_RH": r1,
        "step_A_required_1e30": r2,
        "step_A_scan_H_RH": {
            "n_strategies": s1["n"],
            "n_both_ok": s1["n_both_ok"],
            "n_far_only": s1["n_far_only"],
            "n_ghk_only": s1["n_ghk_only"],
            "first_both_ok": slim(s1["first_both_ok"]) if s1["first_both_ok"] else None,
            "top_tradeoffs": [slim(r) for r in top],
            "tension": (
                "Far-sum wants large log X; GHK c1 X^4/(gamma log X)^2 wants small X. "
                "Joint window under c1=291 is the arithmetic content of Step A."
            ),
        },
        "step_A_scan_1e30": {
            "n_both_ok": s2["n_both_ok"],
            "first_both_ok": slim(s2["first_both_ok"]) if s2["first_both_ok"] else None,
        },
        "conclusion": {
            "polylog_density_moderate_sigma": "OPEN — theta(beta*)>0 for all tabulated beta*<=0.98",
            "step_A_arithmetic": (
                "Under R-vM local counts + programme c1=291,c2=8, the joint window "
                "(far_sum<=0.4 and E_GHK<=0.1) is empty at H_RH=3e12 across polylog/exp/power X trials. "
                "Required log X for far-sum alone already forces X so large that term_X4 explodes. "
                "Honest obstruction: either tighten c1 (better GHK weight / U decay) or accept "
                "weaker remainder targets. Not a completed numerical gamma1 theorem."
            ),
            "O_M1_2": "Architecture accepted; constants recorded; joint numerical gamma1 under current c1 NOT closed",
            "O_TL": "OPEN",
            "RH": "OPEN",
        },
    }

    def clean(o):
        if isinstance(o, float):
            if math.isnan(o) or math.isinf(o):
                return "inf" if math.isinf(o) else "nan"
            return o
        if isinstance(o, dict):
            return {k: clean(v) for k, v in o.items()}
        if isinstance(o, list):
            return [clean(v) for v in o]
        return o

    out = out_dir / "rh_stepA_stepB_results.json"
    out.write_text(json.dumps(clean(results), indent=2), encoding="utf-8")
    print("OK", out)
    print("both_ok@3e12:", s1["n_both_ok"], s1["first_both_ok"])
    print("required logX@3e12:", r1["logX_needed_for_far"])
    print("E_GHK at needed X:", r1["E_GHK_at_needed_X"])
    print("top:", slim(top[0]))
    print("theta 0.55", gaps[0]["theta_Ingham_CS"], "0.80", gaps[5]["theta_Ingham_CS"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
