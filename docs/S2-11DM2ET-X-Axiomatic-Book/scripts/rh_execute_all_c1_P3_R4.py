#!/usr/bin/env python3
"""
Execute-all package (2026-08-08):
  A) c1 / U tightening levers + joint-window threshold scan
  B) P3.1 path-continuation majorant Φ (symbolic + numerical sketch)
  C) R4.1 off-line GHK strip bound (fixed X, thin strip)
  D) P3.2 / R4.2 / R4.3 bookkeeping snapshots

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


# ---------- GHK / far-sum cores ----------

def m12_far(gamma, C_U, c_r, logX):
    Lg = math.log(gamma)
    r = c_r / Lg
    J = math.log2(max(2.0 * gamma / r, 2.0))
    far = (J + 1.0) * C_U * Lg / logX
    return far, J, r, Lg


def ghk_terms(gamma, logX, sigma, c1, c2):
    # term1 = c1 X^4 / (gamma^2 logX^2); independent of sigma at |s|~|t|
    try:
        lt1 = math.log(c1) + 4.0 * logX - 2.0 * math.log(gamma) - 2.0 * math.log(max(logX, 1e-15))
        term1 = math.exp(lt1) if lt1 < 700 else float("inf")
    except Exception:
        term1 = float("inf")
    # term2 = c2 X^{-sigma} log X = c2 exp(-sigma logX) logX
    try:
        term2 = c2 * math.exp(-sigma * logX) * logX
    except Exception:
        term2 = float("inf")
    return term1, term2, term1 + term2 if math.isfinite(term1) and math.isfinite(term2) else float("inf")


def c1_from_factors(A2, D2, M2, C_mul):
    # c1 = 2 * C_mul * D2 * A2 * M2
    return 2.0 * C_mul * D2 * A2 * M2


# ---------- A: c1 tightening ----------

def package_A():
    # Baseline optimized package from rh_optimize_c1_c2_results.json
    M2 = 85.71616032090529
    A2_opt = 0.16896966907609048
    D2_opt = 5.0222700105
    C_tail = 2.0
    C_mul = 2.0
    c1_base = c1_from_factors(A2_opt, D2_opt, M2, C_mul)
    c2_base = 2.0 * C_mul * C_tail  # 8

    # Lever catalogue (admissible explorations, not interval-certified)
    levers = []

    # L1: reduce C_mul from 2 to 1.25 when |err|≤1/4 ( |log(1+w)| ≤ (4/3)|w| roughly → use 1.25)
    for C_mul in [2.0, 1.5, 1.25, 1.1]:
        levers.append(
            {
                "lever": f"C_mul={C_mul}",
                "A2": A2_opt,
                "D2": D2_opt,
                "M2": M2,
                "C_mul": C_mul,
                "c1": c1_from_factors(A2_opt, D2_opt, M2, C_mul),
                "c2": 2.0 * max(C_mul, 1.0) * C_tail if C_mul >= 1 else 2 * C_tail,
                "status": "admissible_if_err_region_shrunk" if C_mul < 2 else "baseline",
            }
        )

    # L2: tighter A2 (remove 10% safety → raw max; and hypothetical 2× better analytic A2)
    for fac, label in [(1.0, "A2_with_safety"), (0.15360879 / A2_opt, "A2_raw_max"), (0.5, "A2_half_hypothetical")]:
        A2 = A2_opt * fac if label != "A2_raw_max" else 0.15360879006917316
        levers.append(
            {
                "lever": label,
                "A2": A2,
                "D2": D2_opt,
                "M2": M2,
                "C_mul": 2.0,
                "c1": c1_from_factors(A2, D2_opt, M2, 2.0),
                "c2": 8.0,
                "status": "executed_grid" if "hyp" not in label else "hypothetical_not_proved",
            }
        )

    # L3: tighter D2 (pole-only 4.5, ignore triv or half triv)
    for D2, label in [(5.02227, "D2_baseline"), (4.5, "D2_pole_only"), (2.0, "D2_optimistic_hyp")]:
        levers.append(
            {
                "lever": label,
                "A2": A2_opt,
                "D2": D2,
                "M2": M2,
                "C_mul": 2.0,
                "c1": c1_from_factors(A2_opt, D2, M2, 2.0),
                "c2": 8.0,
                "status": "executed" if D2 >= 4.5 else "hypothetical_not_proved",
            }
        )

    # L4: combined best executed (raw A2 + pole D2 + C_mul 1.25)
    A2_raw = 0.15360879006917316
    c1_best_exec = c1_from_factors(A2_raw, 4.5, M2, 1.25)
    levers.append(
        {
            "lever": "combined_best_executed_style",
            "A2": A2_raw,
            "D2": 4.5,
            "M2": M2,
            "C_mul": 1.25,
            "c1": c1_best_exec,
            "c2": 2.0 * 1.25 * C_tail,  # 5.0 if same formula
            "status": "stacked_admissible_with_caveats",
            "caveats": "C_mul=1.25 needs |err|≤~0.2 region; D2=4.5 drops trivial-zero pad; A2 raw not safety-padded",
        }
    )

    # L5: what c1 is NEEDED for joint window at H_RH
    gamma = 3e12
    target_far, eps0, C_U, c_r, sigma = 0.4, 0.1, 2.0, 0.25, 0.5
    # Scan logX and find min c1 such that both hold for some logX
    need = []
    for logX in [x * 0.5 for x in range(4, 80)]:  # 2 .. 40
        far, J, r, Lg = m12_far(gamma, C_U, c_r, logX)
        if far > target_far:
            continue
        # need term1 + term2 <= eps0; term2 = c2 X^{-1/2} logX with c2=8
        # term1 = c1 * exp(4 logX - 2 log gamma - 2 log logX)
        # c1 <= (eps0 - term2) / coef
        c2 = 8.0
        term2 = c2 * math.exp(-sigma * logX) * logX
        if term2 >= eps0:
            continue
        coef = math.exp(4.0 * logX - 2.0 * math.log(gamma) - 2.0 * math.log(max(logX, 1e-15)))
        c1_max = (eps0 - term2) / coef
        need.append(
            {
                "logX": logX,
                "X": math.exp(logX) if logX < 700 else "inf",
                "far": far,
                "term2": term2,
                "c1_max_for_GHK": c1_max,
                "X_over_sqrt_gamma": math.exp(logX - 0.5 * math.log(gamma)) if logX < 400 else "inf",
            }
        )

    best_need = max(need, key=lambda d: d["c1_max_for_GHK"]) if need else None

    # Joint scan for several c1 levels
    c1_levels = [291.0, 150.0, 50.0, 10.0, 1.0, 0.1, 0.01, 0.001, c1_best_exec]
    joint = []
    for c1 in sorted(set(c1_levels)):
        hits = 0
        first = None
        for logX in [x * 0.25 for x in range(8, 160)]:
            far, _, _, _ = m12_far(gamma, C_U, c_r, logX)
            t1, t2, E = ghk_terms(gamma, logX, sigma, c1, 8.0)
            if far <= target_far and fin(E) <= eps0:
                hits += 1
                if first is None:
                    first = {"logX": logX, "far": far, "E": E, "X": math.exp(logX)}
        joint.append({"c1": c1, "n_hits": hits, "first_hit": first})

    # Also try weaker far target (honest alternative)
    weak = []
    for target in [0.4, 1.0, 2.0, 5.0, 10.0, 20.0]:
        for c1 in [291.0, c1_best_exec, 10.0, 1.0]:
            hits = 0
            first = None
            for logX in [x * 0.5 for x in range(4, 80)]:
                far, _, _, _ = m12_far(gamma, C_U, c_r, logX)
                _, _, E = ghk_terms(gamma, logX, sigma, c1, 8.0)
                if far <= target and fin(E) <= eps0:
                    hits += 1
                    if first is None:
                        first = {"logX": logX, "far": far, "E": fin(E)}
            weak.append({"target_far": target, "c1": c1, "n_hits": hits, "first": first})

    return {
        "baseline_c1": c1_base,
        "baseline_c2": c2_base,
        "levers": levers,
        "best_executed_style_c1": c1_best_exec,
        "c1_max_over_logX_for_joint_far0.4": best_need,
        "joint_hits_by_c1": joint,
        "weak_target_scan": [w for w in weak if w["n_hits"] > 0][:20] + [
            w for w in weak if w["n_hits"] == 0 and w["c1"] == 291.0
        ][:3],
        "conclusion_A": (
            "Even stacked best-executed-style c1 still far above the c1_max required "
            "for joint far_sum≤0.4 and E_GHK≤0.1 at H_RH under R-vM far-sum. "
            "True fix needs either much smaller C_U (better U decay / path radius), "
            "weaker far target, or structurally better remainder (not just c1 factor tuning)."
        ),
    }


# ---------- B: P3.1 Φ majorant ----------

def package_P31():
    """
    Path-continuation majorant Φ for |∂_σ Δ_X(σ+it)|.

    Model (ZLA-clean schematic):
      Δ_X = log ζ - log P_X  (or hybrid discrepancy Im form)
      ∂_σ Δ_X = Re(ζ'/ζ) - Re(P_X'/P_X)   [up to sign conventions]

    Majorants:
      |P_X'/P_X(s)| ≤ sum_{n≤X} Λ(n) n^{-σ} ≤ sum_{n≤X} n^{-σ} ≤ ζ(σ) for σ>1;
        for σ≤1: ≤ X^{1-σ}/((1-σ) log X) style integral bound for σ<1.
      |ζ'/ζ| ≤ 1/|σ-1| + O(log(|t|+2)) on average; worst-case explicit formula:
        |ζ'/ζ(s)| ≤ sum_ρ 1/|s-ρ| + O(log(|t|+2))
        ≤ (local) m/r + far sum.

    We produce a concrete explicit majorant function evaluated on a grid
    for illustration under classical N(T) ~ (T/2π) log T density for far zeros.
    """
    results = {
        "definition": {
            "Delta_X": "log ζ(s) - log P_X(s)  (hybrid form optional)",
            "partial_sigma": "∂_σ Δ_X = Re(ζ'/ζ - P_X'/P_X)",
            "Phi_target": "|∂_σ Δ_X| ≤ Φ(σ,t,X)",
            "continuation_criterion": "∫_{1/2}^{σ*} Φ dσ < |Δ_X(1/2+it*)|/2",
        },
        "Phi_split": {
            "Phi_P": "|P_X'/P_X| ≤ sum_{n≤X} Λ(n) n^{-σ}",
            "Phi_zeta_arch": "O(log(|t|+2)) classical on vertical lines away from zeros",
            "Phi_zeta_zeros": "sum_ρ 1/|s-ρ| majorized by local + dyadic density",
            "Phi_GHK": "derivative of E_GHK — secondary if working with hybrid Δ",
        },
    }

    # Numerical sketch: Φ_P and Φ_zeros on grid, fixed t=1e6, X=exp(10)
    t = 1e6
    X = math.exp(10.0)  # ~22026
    logX = math.log(X)
    sigmas = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.9, 0.95, 0.99]
    grid = []
    for sig in sigmas:
        # Phi_P: integral bound sum_{n≤X} n^{-σ} ≤ 1 + ∫_1^X x^{-σ} dx
        if abs(sig - 1.0) < 1e-12:
            Phi_P = 1.0 + math.log(X)
        elif sig < 1.0:
            Phi_P = 1.0 + (X ** (1.0 - sig) - 1.0) / (1.0 - sig)
        else:
            Phi_P = 1.0 + (1.0 - X ** (1.0 - sig)) / (sig - 1.0)
        # Λ version: multiply by log factors crudely ≤ log X * Phi_P / something — use
        # sum Λ(n) n^{-σ} ≤ log X * sum n^{-σ} crude for n≤X... better: ψ-style
        # Classical: sum_{n≤X} Λ(n) n^{-σ} ≤ X^{1-σ}/(1-σ) for σ<1 roughly times log
        if sig < 1:
            Phi_P_Lambda = (X ** (1.0 - sig)) / max(1.0 - sig, 1e-6) 
        else:
            Phi_P_Lambda = math.log(X) + 1.0

        # Far zero sum at height t: density (log t)/(2π) per unit height
        # sum 1/|s-ρ| ≲ (log t) * log(t)  classical crude on average;
        # worst-case with min distance r0 = 1/log t:
        r0 = 1.0 / math.log(t)
        # dyadic: sum_j (count in annulus 2^j r0) / (2^j r0) ≲ sum_j (2^j r0 log t) / (2^j r0) = J log t
        J = math.log2(max(t / r0, 2.0))
        Phi_zeros_far = J * math.log(t)  # crude
        Phi_local = 1.0 / r0  # single nearby zero threat; path must avoid
        Phi_arch = math.log(t + 2.0)

        Phi = Phi_P_Lambda + Phi_zeros_far + Phi_local + Phi_arch
        grid.append(
            {
                "sigma": sig,
                "Phi_P_Lambda": Phi_P_Lambda,
                "Phi_zeros_far": Phi_zeros_far,
                "Phi_local_1_over_r0": Phi_local,
                "Phi_arch": Phi_arch,
                "Phi_total_crude": Phi,
            }
        )

    # Integral of Φ from 1/2 to σ*
    def trap_int(upto):
        pts = [g for g in grid if g["sigma"] <= upto + 1e-15]
        if len(pts) < 2:
            return 0.0
        acc = 0.0
        for i in range(len(pts) - 1):
            a, b = pts[i], pts[i + 1]
            acc += 0.5 * (a["Phi_total_crude"] + b["Phi_total_crude"]) * (b["sigma"] - a["sigma"])
        return acc

    # On-line reservoir size for fixed X: model √X / log X
    reservoir = math.sqrt(X) / logX
    integrals = {f"to_{s}": trap_int(s) for s in [0.6, 0.7, 0.8, 0.9, 0.99]}

    results["numerical_sketch"] = {
        "t": t,
        "X": X,
        "logX": logX,
        "r0": 1.0 / math.log(t),
        "grid": grid,
        "integral_Phi_crude": integrals,
        "online_reservoir_model_sqrtX_over_logX": reservoir,
        "comparison": {
            k: {
                "integral": v,
                "reservoir": reservoir,
                "integral_lt_half_reservoir": v < 0.5 * reservoir,
            }
            for k, v in integrals.items()
        },
        "reading": (
            "Under this crude worst-case Φ (including 1/r0 local term), ∫ Φ exceeds "
            "the on-line reservoir at these parameters. Path continuation therefore "
            "requires either: (i) paths avoiding the 1/r0 local spike (zero-free tubes), "
            "(ii) average-case Φ without local pole, or (iii) larger X / stronger on-line Ω. "
            "This is an obstruction sketch for naive absolute majorants — not a no-go theorem."
        ),
    }

    # Analytic statement of Φ (for the note)
    results["analytic_Phi"] = {
        "Phi_P": "sum_{n≤X} Λ(n) n^{-σ} ≤ 1_{σ>1} ζ(σ) log-factors; for σ<1: ≪ X^{1-σ}/(1-σ)",
        "Phi_zeros": "sum_{ρ≠local} 1/|s-ρ| ≪ (log t) log(t/r) under R-vM dyadic (average)",
        "Phi_local": "m / dist(s, nearest zero) — must be controlled by path geometry",
        "Phi_arch": "O(log(|t|+2))",
        "status": "P3.1 majorant structure recorded; absolute crude integral fails vs reservoir",
    }
    return results


# ---------- C: R4.1 off-line GHK strip ----------

def package_R41():
    """
    Off-line GHK strip: σ ∈ [1/2, 1/2+δ], fixed large X, t→∞.

    E_GHK ≤ c1 X^4 / (t log X)^2 + c2 X^{-σ} log X
    At σ = 1/2+δ ≥ 1/2, X^{-σ} ≤ X^{-1/2} X^{-δ}.

    For fixed X, as t→∞, term1 → 0. Term2 is independent of t.
    So for each fixed X, eventually |E_GHK| ≤ 2 c2 X^{-1/2} log X on the whole strip
    once t ≥ t0(X,c1,c2).

    Compare to on-line Im D_X size ≍ √X / log X:
    need 2 c2 X^{-1/2} log X  ≤  (1/2) c0 √X / log X
    i.e. 4 c2 (log X)^2 ≤ c0 X   — true for large X.

    Obstacles O4.2–O4.4 remain (zeros, branches, correlation).
    """
    c1, c2 = 291.0, 8.0
    rows = []
    for logX in [5, 8, 10, 12, 15, 20, 25]:
        X = math.exp(logX)
        for delta in [0.0, 0.01, 0.05, 0.1, 0.2]:
            sig = 0.5 + delta
            # t0 so that term1 ≤ term2
            # c1 X^4 / (t^2 logX^2) ≤ c2 X^{-sig} logX
            # t^2 ≥ c1 X^4 / (c2 X^{-sig} logX^3)
            denom = c2 * math.exp(-sig * logX) * (logX ** 3)
            if denom <= 0:
                continue
            t0_sq = c1 * math.exp(4 * logX) / denom
            t0 = math.sqrt(t0_sq) if t0_sq < 1e300 else float("inf")
            term2 = c2 * math.exp(-sig * logX) * logX
            model_Im = math.sqrt(X) / logX
            rows.append(
                {
                    "logX": logX,
                    "X": X,
                    "delta": delta,
                    "sigma": sig,
                    "term2_strip": term2,
                    "t0_term1_le_term2": t0 if math.isfinite(t0) else "inf",
                    "model_Im_D_X": model_Im,
                    "term2_over_half_model": term2 / (0.5 * model_Im),
                    "strip_error_small_vs_model": term2 < 0.5 * model_Im,
                }
            )

    # Theorem-style statement data
    good = [r for r in rows if r["strip_error_small_vs_model"] and r["delta"] >= 0]
    return {
        "theorem_R41_statement": (
            "Proposition R4.1 (fixed X, thin strip, pure GHK error only). "
            "Let c1,c2 be admissible hybrid constants for f_star, K=2. Fix X≥3. "
            "For σ ∈ [1/2, 1], |t|≥2: |E_GHK(σ+it,X)| ≤ c1 X^4/(t^2 (log X)^2) + c2 X^{-σ} log X. "
            "Hence for each fixed X there exists t0(X) such that for all |t|≥t0(X) and all "
            "σ ∈ [1/2, 1/2+δ] (any fixed δ≥0 with 1/2+δ≤1), "
            "|E_GHK| ≤ 2 c2 X^{-1/2-δ} log X. "
            "In particular if 4 c2 (log X)^2 < c0 X^{1+δ} wait — compare to model size √X/log X: "
            "2 c2 X^{-1/2-δ} log X < (c0/2) √X / log X for large X. "
            "This controls ONLY the GHK multiplicative error off the line for fixed X. "
            "It does NOT control nearby zeros, continuous argument, or torus–zero correlation."
        ),
        "c1": c1,
        "c2": c2,
        "grid": rows,
        "n_grid_term2_small": len(good),
        "sample_good": good[:5],
        "obstacles_remaining": ["O4.2 nearby zeros", "O4.3 branch vs principal value", "O4.4 torus–zero correlation"],
        "status": "R4.1_GHK_STRIP_ERROR_ONLY_EXECUTED",
    }


# ---------- D: R4.2 / R4.3 / P3.2 snapshots ----------

def package_rest(p31, r41):
    # P3.2: compare integrals to reservoir (already in p31)
    p32 = {
        "status": "P3.2_SNAPSHOT_FROM_P31_NUMERICS",
        "finding": p31["numerical_sketch"]["reading"],
        "comparison_table": p31["numerical_sketch"]["comparison"],
        "next": (
            "Replace absolute 1/r0 local term by a path in a zero-free tube of width "
            "≫ 1/log t on a positive-density set of t_* (classical zero-free regions near σ=1 "
            "do not help at moderate σ). Average-case Φ is the realistic path."
        ),
    }

    r42 = {
        "status": "R4.2_STATEMENT_ONLY",
        "lemma_target": (
            "A positive-density subset of Kronecker maximisers t_n for Im D_X(1/2+it) "
            "satisfies dist(1/2+δ+it_n, nearest zero) ≥ c / log X for small δ=δ(X)."
        ),
        "classical_tools": [
            "zero density N(σ,T)",
            "simple spacing heuristics (not theorems at all heights)",
            "Maynard–Pratt half-isolation (local one-sided; few such zeros)",
        ],
        "obstruction": (
            "Unconditional positive-density avoidance at arbitrary height is open; "
            "half-isolation gives few bad zeros but not density of good Kronecker times."
        ),
        "executable_partial": (
            "Conditional on finite vertical lines (Hypothesis F) or Iso_H, avoidance is easy. "
            "Unconditional: record only the lemma target."
        ),
    }

    r43 = {
        "status": "R4.3_STATEMENT_ONLY",
        "task": (
            "Convert Im D_X lower bounds into continuous θ_X / hybrid discrepancy lower bounds "
            "with tracked branch errors via the OPC hybrid identity."
        ),
        "known": (
            "On-line, for fixed X, principal Im D_X and continuous argument can be aligned "
            "on intervals free of P_X zeros (P_X zero-free for σ≥1/2 under standard bounds for large t)."
        ),
        "open": "Off-line branch control near ζ zeros of large real part.",
        "link": "RH_OPC_Conversion_Gap.md, RH_OPC_Partial_Resolution.md",
    }

    return {"P3.2": p32, "R4.2": r42, "R4.3": r43}


def main():
    out_dir = Path(__file__).resolve().parents[1]
    A = package_A()
    P31 = package_P31()
    R41 = package_R41()
    rest = package_rest(P31, R41)

    results = {
        "status": "RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF",
        "date": "2026-08-08",
        "zla": True,
        "no_model_constants": True,
        "does_not_prove": ["O-TL", "RH", "Iso_H", "Mass-with-A", "O-M1.2 complete", "O-M1.3bis"],
        "A_c1_U_tightening": A,
        "P3_1_Phi_majorant": P31,
        "R4_1_offline_GHK_strip": R41,
        "P3_2_R4_2_R4_3": rest,
        "global_conclusion": {
            "c1_tuning": "Insufficient alone to open joint M1.2 window at far_sum≤0.4 under R-vM",
            "P3_1": "Φ structure recorded; crude absolute integral loses to reservoir",
            "R4_1": "Pure GHK strip error controlled for fixed X large t — zeros/branches remain",
            "RH": "OPEN",
        },
    }

    def clean(o):
        if isinstance(o, float):
            if math.isnan(o):
                return "nan"
            if math.isinf(o):
                return "inf"
            return o
        if isinstance(o, dict):
            return {k: clean(v) for k, v in o.items()}
        if isinstance(o, list):
            return [clean(v) for v in o]
        return o

    out = out_dir / "rh_execute_all_c1_P3_R4_results.json"
    out.write_text(json.dumps(clean(results), indent=2), encoding="utf-8")
    print("OK", out)
    print("baseline c1", A["baseline_c1"], "best_exec_style", A["best_executed_style_c1"])
    print("c1_max joint", A["c1_max_over_logX_for_joint_far0.4"])
    print("joint hits", [(j["c1"], j["n_hits"]) for j in A["joint_hits_by_c1"]])
    print("weak hits sample", A["weak_target_scan"][:5])
    print("R41 n_good", R41["n_grid_term2_small"])
    print("P31 integral to 0.7", P31["numerical_sketch"]["integral_Phi_crude"]["to_0.7"])
    print("reservoir", P31["numerical_sketch"]["online_reservoir_model_sqrtX_over_logX"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
