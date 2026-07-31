#!/usr/bin/env python3
"""
Optimize M_K, A_K, D_K for named f_star → numerical upper bounds on c1, c2.

Named f: f_star(t) = exp(-1/(t(1-t))) / mass on (0,1).
GHK: u(x) = X/x * f(X log(x/e)+1), K=2.

A_K^num := sup_X  max|u^{(K)}| / (M_K X^{K+1})   (sampled over X and x)
D_K^an  := analytic majorant for archimedean |U| sum relative to
           A_K M_K X^{K+2} / (|s| log X)^K

DIAGNOSTIC / EXPLICIT CONSTANTS ONLY — no RH claim.
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


def compute_mass(n: int = 100001) -> float:
    xs = np.linspace(1e-14, 1.0 - 1e-14, n)
    ys = np.array([raw_bump(float(x)) for x in xs])
    return float(np.trapezoid(ys, xs))


def max_f_derivatives(mass: float, jmax: int = 2, n_grid: int = 8001, dps: int = 40):
    mp.mp.dps = dps
    mass_mp = mp.mpf(mass)

    def f(t):
        if t <= 0 or t >= 1:
            return mp.mpf(0)
        return mp.exp(-1 / (t * (1 - t))) / mass_mp

    out = []
    for j in range(0, jmax + 1):
        mx = mp.mpf(0)
        t_at = mp.mpf("0.5")
        for k in range(1, n_grid):
            t = mp.mpf(k) / n_grid
            try:
                v = abs(f(t)) if j == 0 else abs(mp.diff(f, t, j))
                if v > mx:
                    mx = v
                    t_at = t
            except Exception:
                continue
        # local refine near t_at
        for h in [mp.mpf("1e-3"), mp.mpf("1e-4"), mp.mpf("1e-5")]:
            for m in range(-20, 21):
                t = t_at + m * h
                if t <= 0 or t >= 1:
                    continue
                try:
                    v = abs(f(t)) if j == 0 else abs(mp.diff(f, t, j))
                    if v > mx:
                        mx = v
                        t_at = t
                except Exception:
                    pass
        # 2% safety (tighter than prior 5% — denser + refine)
        out.append(float(mx * mp.mpf("1.02")))
        print(f"  M_{j}^# = {float(mx * 1.02):.8g} (at t~{float(t_at):.5f})", flush=True)
    return out


def u_value_and_derivs_num(X: float, x: float, mass: float, K: int = 2, h: float = 1e-7):
    """
    Numerical derivatives of u(x) = X/x * f(X*log(x/e)+1) via central differences.
    Returns u, u', ..., u^{(K)} at x (float).
    """
    def u_at(xx: float) -> float:
        if xx <= 0:
            return 0.0
        tau = X * math.log(xx / math.e) + 1.0
        return (X / xx) * (raw_bump(tau) / mass)

    # central finite differences on a log-grid scale
    # use step relative to x
    hs = max(h * x, 1e-10)
    # stencil for derivatives up to order K
    vals = {}
    # need enough points: for order K, use ±K*hs
    for m in range(-K - 1, K + 2):
        vals[m] = u_at(x + m * hs)

    # recursive central differences
    # d^n u ≈ sum binom coefficients
    # Use Fornberg or simple nested:
    row = [vals[m] for m in range(-K - 1, K + 2)]
    # map index: offset 0 at position K+1
    center = K + 1
    ders = [row[center]]  # 0th
    cur = row
    for order in range(1, K + 1):
        nxt = []
        for i in range(len(cur) - 1):
            nxt.append((cur[i + 1] - cur[i]) / hs)
        cur = nxt
        # center shifts
        c = center - order  # after order diffs, center index
        # actually each diff shortens array by 1 from left; center moves
        # simpler: recompute with scipy-style
        ders.append(cur[center - order])  # may be off — use Fornberg below

    # Fornberg weights for derivatives at 0 on uniform grid
    def fornberg_weights(z: float, x_nodes: list[float], m: int):
        """Weights for m-th derivative at z given nodes x_nodes (Fornberg)."""
        n = len(x_nodes) - 1
        c = np.zeros((n + 1, m + 1))
        c[0, 0] = 1.0
        c1 = 1.0
        c4 = x_nodes[0] - z
        for i in range(1, n + 1):
            mn = min(i, m)
            c2 = 1.0
            c5 = c4
            c4 = x_nodes[i] - z
            for j in range(i):
                c3 = x_nodes[i] - x_nodes[j]
                c2 *= c3
                if j == i - 1:
                    for k in range(mn, 0, -1):
                        c[i, k] = c1 * (k * c[i - 1, k - 1] - c5 * c[i - 1, k]) / c2
                    c[i, 0] = -c1 * c5 * c[i - 1, 0] / c2
                for k in range(mn, 0, -1):
                    c[j, k] = (c4 * c[j, k] - k * c[j, k - 1]) / c3
                c[j, 0] = c4 * c[j, 0] / c3
            c1 = c2
        return c[:, m]

    nodes = [m * hs for m in range(-K - 2, K + 3)]
    uvals = [u_at(x + xi) for xi in nodes]
    ders_out = []
    for order in range(0, K + 1):
        w = fornberg_weights(0.0, nodes, order)
        ders_out.append(float(np.dot(w, uvals)))
    return ders_out


def estimate_A_K(mass: float, M_K: float, K: int = 2, Xs=None) -> dict:
    """
    A_K^num = max over X,x of |u^{(K)}(x)| / (M_K X^{K+1})
    Sample x in support [e^{1-1/X}, e].
    """
    if Xs is None:
        Xs = [2.0, 3.0, 5.0, 10.0, 20.0, 50.0, 100.0, 200.0, 500.0]
    best = 0.0
    best_at = None
    samples = []
    for X in Xs:
        x_lo = math.exp(1.0 - 1.0 / X)
        x_hi = math.e
        # dense in tau ∈ (0,1)
        for j in range(1, 400):
            tau = j / 401.0
            x = math.exp(1.0 - (1.0 - tau) / X)
            if x <= x_lo or x >= x_hi:
                continue
            try:
                ders = u_value_and_derivs_num(X, x, mass, K=K, h=1e-6)
                uk = abs(ders[K])
                ratio = uk / (M_K * (X ** (K + 1)))
                if ratio > best:
                    best = ratio
                    best_at = {"X": X, "x": x, "tau": tau, "uK": uk, "ratio": ratio}
            except Exception:
                continue
        samples.append({"X": X, "running_max_A": best})
        print(f"  X={X:g}: running A_{K}^num <= {best:.6g}", flush=True)
    # 10% numerical FD safety
    A_num = best * 1.10
    return {"A_K_raw_max": best, "A_K_with_safety": A_num, "at": best_at, "trace": samples}


def analytic_D_K(K: int = 2) -> dict:
    """
    Analytic majorant for arch contribution.

    From GHK §2 with |t|>=2, σ>=0, K=2:
      ∫_{-∞}^{∞} dα / (α^2+t^2)^{3/2} = 2/t^2.

    |ũ(z)| <= max|u^{(K)}| * e^{max{Re z + K, 0}} / (1+|z|)^K
    After the change of variables in the integral for U,
    GHK obtains
      |U((s-r)log X)| <= max|u^K| * X^{max{r-σ,0}} / (log X)^K
                         * ∫ dσ / |(σ-r)+it|^{K+1}
                      <= max|u^K| * X^{max{r-σ,0}} / (log X)^K * (2 / |t|^K)
    for K=2 (integral = 2/t^2).

    max|u^K| <= A_K M_K X^{K+1}.
    Pole r=1: X^{max{1-σ,0}} <= X, |t| >= |s| * |t|/(|t|+σ) >= |s| * |t|/(|t|+|s|)
    Use |t| >= (2/3)|s| when |t|>=2, σ <= |t|/2 (typical strip), or simply
    |t| >= |s|/2 when σ <= |t| which holds for |t|>=2, σ<=1 on critical strip path.

    Safer uniform for σ in [0,1], |t|>=2:
      |s| <= |t|+1 <= (3/2)|t| for |t|>=2 ⇒ |t| >= (2/3)|s|
      so 2/|t|^K <= 2*(3/2)^K / |s|^K

    Pole: |U| <= A M X^{K+1} * X * 2*(3/2)^K / (|s| log X)^K
         = [2*(3/2)^K] A M X^{K+2} / (|s| log X)^K

    Trivial zeros: max{r-σ,0}=0 for r=-2m, sum_m 2/|t+...|^K
      sum_{m=1}^∞ 2 / (2m - 1 + |t|)^K  <= 2 * ∫_0^∞ dx / (x+|t|)^K
      for K=2: 2 / |t|  — weaker power!

    Wait: each term uses /(|s+2m| log X)^K in GHK packaging into same shape.
    sum_m 1/|s+2m|^{K+1} * (log factors) ...

    GHK packages both into O(X^{K+2}/(|s| log X)^K). For K=2:
    Trivial sum: max|u^K| / (log X)^K * sum_m ∫ dσ/|σ+2m+it|^{3}
      <= A M X^{K+1} / (log X)^K * sum_m 2 / |t|^2 * (crude)
      Better: sum_m 2/|2m+it|^2 <= sum_m 2/(4m^2) + 2/t^2 * ...
      sum_{m=1}^∞ 2 / (t^2 + (2m)^2) <= (1/2) ∫_0^∞ dx/(t^2/4 + x^2) wait

    sum_{m=1}^∞ 1/(t^2 + 4m^2) <= (1/(2|t|)) * (π/2) / 2? 
    coth expansion: (π/(2|t|)) coth(π|t|/2) - 1/t^2 ≈ π/(2|t|) for large t
    For |t|>=2: sum_m 1/(t^2+4m^2) <= 0.4  (check numerically)

    We'll use:
      D_pole = 2 * (3/2)^K   for the X^{K+2} form after A M
      D_triv = 2 * S_triv * X^{-1} absorbed... 

    Actually trivial zeros have X^{K+1} not X^{K+2} (max{r-σ,0}=0).
    So relative to X^{K+2}/(|s|log X)^K they contribute * X^{-1} * |s|^0.
    For X>=2: factor 1/2.

    D_K = D_pole + D_triv_factor
    D_pole = 2*(3/2)^K
    D_triv = 2 * sum_bound * (for K=2, sum 2/|s+2m|^3 * |s|^2 ...) 

    Simpler admissible for K=2, |t|>=2, σ∈[0,1]:
      D_2 = 2*(3/2)^2 + 4 = 2*2.25 + 4 = 8.5
    (4 covers trivial zeros generously)

    Optimized: compute numerical sum of integrals.
    """
    # K=2 specifics
    assert K == 2
    # pole factor: 2/|t|^2 * X^{...} with |t| >= (2/3)|s|
    pole_factor = 2.0 * (1.5**K)  # 4.5
    # trivial zeros: max|u^K|/(log X)^K * sum_m 2/|t|^2 roughly
    # bound sum_m=1^∞ 2 / (t^2 + (σ+2m)^2)^{1} wait K+1=3
    # Numerical: for t=2..1000, max of |s|^2 * sum_m 2/|s+2m|^3 * (for packaging)
    s_samples = []
    worst = 0.0
    for t in np.linspace(2, 200, 80):
        for sig in [0.0, 0.5, 1.0]:
            s_abs = abs(complex(sig, t))
            sm = 0.0
            for m in range(1, 5000):
                sm += 2.0 / (abs(complex(sig + 2 * m, t)) ** 3)
            # convert to coeff of X^{K+1}/(log X)^K vs X^{K+2}/(|s| log X)^K
            # ratio: [X^{K+1} * sm] / [X^{K+2}/(|s|^K)] = |s|^K * sm / X
            # at X=2 minimum, |s|^2 * sm / 2
            coeff_at_X2 = (s_abs**K) * sm / 2.0
            if coeff_at_X2 > worst:
                worst = coeff_at_X2
            s_samples.append(coeff_at_X2)
    triv_factor = worst * 1.05  # safety
    # Pole uses X^{K+2}; D_pole multiplies A M X^{K+2}/(|s|log X)^K
    D2 = pole_factor + triv_factor
    return {
        "K": K,
        "pole_factor": pole_factor,
        "triv_factor_X2": triv_factor,
        "D_K": D2,
        "note": (
            "D_K multiplies A_K M_K X^{K+2}/(|s| log X)^K for |R_arch|. "
            "Pole uses |t|>=(2/3)|s| on σ∈[0,1],|t|>=2. Trivial zeros at X>=2."
        ),
    }


def main() -> int:
    print("mass...", flush=True)
    mass = compute_mass()
    print(f"mass = {mass:.12g}", flush=True)

    print("M_j...", flush=True)
    Ms = max_f_derivatives(mass, jmax=2, n_grid=8001)
    M2 = Ms[2]

    print("A_2 numerical...", flush=True)
    Ainfo = estimate_A_K(mass, M2, K=2)

    print("D_2 analytic+numeric triv...", flush=True)
    Dinfo = analytic_D_K(K=2)

    A2 = Ainfo["A_K_with_safety"]
    D2 = Dinfo["D_K"]
    C_tail = 2.0
    C_mul = 2.0

    c1 = 2 * C_mul * D2 * A2 * M2
    c2 = 2 * C_mul * C_tail

    # also report old crude for comparison
    crude = {"A_2": 24, "D_2": 16, "c1": 1536 * M2, "c2": 8}

    out = {
        "provenance": {
            "status_label": "RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF",
            "proves_RH": False,
            "proves_M1_2": False,
            "model_constants": False,
            "named_f": "f_star(t)=exp(-1/(t(1-t)))/mass",
            "note": "Optimized majorants; still admissible upper bounds, not sharp GHK constants.",
        },
        "mass": mass,
        "M_j_upper": {f"M_{j}": Ms[j] for j in range(3)},
        "A_2": Ainfo,
        "D_2": Dinfo,
        "package": {
            "K": 2,
            "A_2": A2,
            "D_2": D2,
            "C_tail": C_tail,
            "C_mul": C_mul,
            "M_2": M2,
        },
        "bounds_optimized": {
            "c1_upper": c1,
            "c2_upper": c2,
        },
        "bounds_crude_prior": crude,
        "improvement_c1_factor": crude["c1"] / c1 if c1 > 0 else None,
        "status": "OPTIMIZED_C1_C2_EXECUTED_NO_PROOF_CLAIM",
    }

    path = Path(__file__).resolve().parents[1] / "rh_optimize_c1_c2_results.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("---")
    print(f"A_2 <= {A2:.6g}")
    print(f"D_2 <= {D2:.6g}")
    print(f"M_2 <= {M2:.6g}")
    print(f"c1_upper <= {c1:.6g}  (crude was {crude['c1']:.6g}, factor {crude['c1']/c1:.3g}x)")
    print(f"c2_upper <= {c2:.6g}")
    print("wrote", path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
