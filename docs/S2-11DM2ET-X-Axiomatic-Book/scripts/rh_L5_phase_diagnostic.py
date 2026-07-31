#!/usr/bin/env python3
"""
L5 numerical diagnostic for RH pure Cat A track.

Computes continuous theta_x = arg P_x(sigma+it) and smoothed A_X
on the critical line (first known zeros) vs off-line test points.

DIAGNOSTIC ONLY — cannot prove RH.
No model constants (no G4, mu, E_leak, 539.9).

Status label: RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF
See: RH_Target_Lemma_Sketch_Literature_L5.md Part III
     RH_L1_Phase_Functional_CatA.md
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# First ordinates of nontrivial zeros on Re s = 1/2 (Odlyzko tables; public)
# ---------------------------------------------------------------------------
FIRST_ZERO_ORDINATES = [
    14.134725141734693,
    21.022039638771555,
    25.010857580145689,
    30.424876125859513,
    32.935061587739190,
    37.586178158825672,
    40.918719012147495,
    43.327073280914999,
    48.005150881167160,
    49.773832477672302,
    52.970321477714461,
    56.446247697063395,
    59.347044002602353,
    60.831778524609810,
    65.112544048081607,
]


def sieve_primes(n: int) -> list[int]:
    """Primes in [2, n]."""
    if n < 2:
        return []
    n = int(n)
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            is_prime[i * i : n + 1 : i] = b"\x00" * (((n - i * i) // i) + 1)
    return [i for i in range(2, n + 1) if is_prime[i]]


def factor_log(p: int, sigma: float, t: float) -> complex:
    """
    Principal complex log of (1 - p^{-s})^{-1} = -log(1 - p^{-s}).
    Returns complex log (re = log|factor|, im = principal arg).
    """
    # p^{-s} = exp(-s log p)
    log_p = math.log(p)
    # p^{-sigma-it} = exp(-sigma log p) * exp(-i t log p)
    mag = math.exp(-sigma * log_p)
    ang = -t * log_p
    re_ps = mag * math.cos(ang)
    im_ps = mag * math.sin(ang)
    # 1 - p^{-s}
    a = 1.0 - re_ps
    b = -im_ps
    # -log(1-p^{-s}) = log 1/(1-p^{-s})
    # log(a+ib)
    mod2 = a * a + b * b
    if mod2 < 1e-30:
        # nearly singular factor — should not happen for sigma>0 finite p
        return complex(0.0, 0.0)
    log_mod = 0.5 * math.log(mod2)
    arg = math.atan2(b, a)
    # -log(w)
    return complex(-log_mod, -arg)


def cumulative_theta_U(
    primes: list[int], sigma: float, t: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Along primes p_1,...,p_N:
      theta[k] = continuous arg P_{p_k}  (sum of principal args of factors)
      U[k]     = log |P_{p_k}|
      xs[k]    = p_k  (so theta is for x = p_k)

    Continuous branch: sum of principal args of successive Euler factors
    starting from P=1 (standard L1 discrete path).
    """
    n = len(primes)
    theta = np.zeros(n, dtype=np.float64)
    U = np.zeros(n, dtype=np.float64)
    xs = np.zeros(n, dtype=np.float64)
    th = 0.0
    u = 0.0
    for k, p in enumerate(primes):
        dlog = factor_log(p, sigma, t)
        u += dlog.real
        th += dlog.imag  # principal arg increments; continuous along prime path
        theta[k] = th
        U[k] = u
        xs[k] = float(p)
    return xs, theta, U


def theta_at_x(
    xs: np.ndarray, theta: np.ndarray, U: np.ndarray, x: float
) -> tuple[float, float]:
    """theta_x, U_x for given x by last prime <= x."""
    if x < xs[0]:
        return 0.0, 0.0
    # rightmost index with xs[i] <= x
    i = int(np.searchsorted(xs, x, side="right") - 1)
    i = max(0, min(i, len(xs) - 1))
    return float(theta[i]), float(U[i])


def phi_bump(v: float) -> float:
    """
    C^infty-style bump on (1,2), zero outside, nonnegative.
    phi(v) ~ exp(-1/((v-1)(2-v))) on (1,2), normalized later.
    """
    if v <= 1.0 or v >= 2.0:
        return 0.0
    w = (v - 1.0) * (2.0 - v)
    if w <= 0.0:
        return 0.0
    return math.exp(-1.0 / w)


def make_phi_normalized(n_quad: int = 64) -> tuple[np.ndarray, np.ndarray]:
    """Return nodes v in [1,2] and weights for measure phi(v) dv with int_1^2 phi = 1."""
    # Gauss-like grid on (1,2)
    vs = np.linspace(1.0 + 1e-6, 2.0 - 1e-6, n_quad)
    raw = np.array([phi_bump(float(v)) for v in vs], dtype=np.float64)
    # trapezoid integral
    dv = vs[1] - vs[0]
    trap = getattr(np, "trapezoid", None) or getattr(np, "trapz")
    integ = float(trap(raw, vs))
    if integ <= 0:
        raise RuntimeError("phi normalization failed")
    weights = raw / integ  # density values; integrate f(v)*phi with trapezoid
    return vs, weights


def A_X_and_mean_U(
    xs: np.ndarray,
    theta: np.ndarray,
    U: np.ndarray,
    X: float,
    vs: np.ndarray,
    phi_density: np.ndarray,
) -> tuple[float, float]:
    """
    A_X = int theta_{e^u} phi(u/log X) du / log X
        = int_1^2 theta_{X^v} phi(v) dv
    (change of variables u = v log X).
    """
    if X <= math.e:
        raise ValueError("X must be > e")
    logX = math.log(X)
    theta_vals = []
    U_vals = []
    for v in vs:
        x = math.exp(v * logX)  # X^v
        th, u = theta_at_x(xs, theta, U, x)
        theta_vals.append(th)
        U_vals.append(u)
    theta_vals = np.asarray(theta_vals, dtype=np.float64)
    U_vals = np.asarray(U_vals, dtype=np.float64)
    # int f(v) phi(v) dv with phi_density already such that trapz(phi_density, vs)=1
    # A = trapz(theta * phi_density, vs) but phi_density is values of normalized phi
    trap = getattr(np, "trapezoid", None) or getattr(np, "trapz")
    A = float(trap(theta_vals * phi_density, vs))
    Umean = float(trap(U_vals * phi_density, vs))
    return A, Umean


def zeta_abs(sigma: float, t: float, dps: int = 25) -> float:
    try:
        import mpmath as mp

        mp.mp.dps = dps
        z = mp.zeta(mp.mpc(sigma, t))
        return float(abs(z))
    except Exception:
        return float("nan")


def run_battery(
    primes: list[int],
    sigma: float,
    t: float,
    X_list: list[float],
    vs: np.ndarray,
    phi_density: np.ndarray,
    label: str,
) -> dict:
    xs, theta, U = cumulative_theta_U(primes, sigma, t)
    zabs = zeta_abs(sigma, t)
    rows = []
    for X in X_list:
        if X > primes[-1]:
            continue
        A, Um = A_X_and_mean_U(xs, theta, U, X, vs, phi_density)
        th_X, U_X = theta_at_x(xs, theta, U, X)
        loglog = math.log(math.log(X)) if X > math.e else float("nan")
        rows.append(
            {
                "X": X,
                "theta_X": th_X,
                "U_X": U_X,
                "A_X": A,
                "U_mean_smooth": Um,
                "abs_A_over_loglog": abs(A) / loglog if loglog and loglog > 0 else None,
                "abs_theta_over_loglog": abs(th_X) / loglog if loglog and loglog > 0 else None,
            }
        )
    # peak |A_X| over grid
    if rows:
        peak = max(rows, key=lambda r: abs(r["A_X"]))
        peak_abs_A = abs(peak["A_X"])
        peak_ratio = peak.get("abs_A_over_loglog")
    else:
        peak_abs_A = None
        peak_ratio = None
    return {
        "label": label,
        "sigma": sigma,
        "t": t,
        "zeta_abs": zabs,
        "n_primes": len(primes),
        "x_max": float(primes[-1]),
        "theta_final": float(theta[-1]),
        "U_final": float(U[-1]),
        "peak_abs_A_X": peak_abs_A,
        "peak_abs_A_over_loglog": peak_ratio,
        "X_grid": rows,
    }


def main() -> int:
    # --- diagnostic parameters (no model constants) ---
    x_max = 5000  # primes up to 5000 — enough for modest X grid
    n_zeros = 8
    deltas = [0.05, 0.1]
    # X grid: e^v with v such that X <= x_max
    # X in [e^3, e^8] roughly but cap by x_max
    X_list = []
    for v in np.linspace(2.5, math.log(x_max) - 0.05, 12):
        X_list.append(float(math.exp(v)))
    X_list = [X for X in X_list if X <= x_max]

    primes = sieve_primes(x_max)
    vs, phi_density = make_phi_normalized(48)

    results_online = []
    results_offline = []

    for t in FIRST_ZERO_ORDINATES[:n_zeros]:
        # on-line
        results_online.append(
            run_battery(
                primes, 0.5, t, X_list, vs, phi_density, label=f"online_sigma=0.5_t={t:.6f}"
            )
        )
        # off-line at same height
        for d in deltas:
            for sign in (+1, -1):
                sig = 0.5 + sign * d
                if sig <= 0.05 or sig >= 0.95:
                    continue
                results_offline.append(
                    run_battery(
                        primes,
                        sig,
                        t,
                        X_list,
                        vs,
                        phi_density,
                        label=f"offline_sigma={sig:.2f}_t={t:.6f}",
                    )
                )

    # summary comparisons: mean peak |A| online vs offline
    def mean_peak(rows: list[dict]) -> float | None:
        vals = [r["peak_abs_A_X"] for r in rows if r["peak_abs_A_X"] is not None]
        return float(np.mean(vals)) if vals else None

    def mean_ratio(rows: list[dict]) -> float | None:
        vals = [
            r["peak_abs_A_over_loglog"]
            for r in rows
            if r["peak_abs_A_over_loglog"] is not None
        ]
        return float(np.mean(vals)) if vals else None

    summary = {
        "n_online": len(results_online),
        "n_offline": len(results_offline),
        "mean_peak_abs_A_online": mean_peak(results_online),
        "mean_peak_abs_A_offline": mean_peak(results_offline),
        "mean_peak_abs_A_over_loglog_online": mean_ratio(results_online),
        "mean_peak_abs_A_over_loglog_offline": mean_ratio(results_offline),
        "interpretation": (
            "Finite-range diagnostic only. "
            "Larger offline |A_X| would be consistent with growth heuristics; "
            "no difference is inconclusive. NEVER claim RH from this output."
        ),
    }

    # branch sanity: |Delta theta| between successive X should not jump by ~2pi spuriously
    branch_warnings = []
    for r in results_online[:3]:
        ths = [row["theta_X"] for row in r["X_grid"]]
        for a, b in zip(ths, ths[1:]):
            if abs(b - a) > math.pi:
                branch_warnings.append(
                    {
                        "label": r["label"],
                        "delta_theta": b - a,
                        "note": "large theta jump between X grid points — check branch",
                    }
                )

    out = {
        "provenance": {
            "status_label": "RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF",
            "category": "A_diagnostic_only",
            "proves_RH": False,
            "model_constants": False,
            "L5_plan": "RH_Target_Lemma_Sketch_Literature_L5.md Part III",
            "L1_object": "theta_x = arg P_x, A_X smoothed",
        },
        "parameters": {
            "x_max": x_max,
            "n_primes": len(primes),
            "n_zeros": n_zeros,
            "deltas": deltas,
            "X_list": X_list,
            "phi": "C^inf bump on (1,2), normalized int_1^2 phi=1",
            "zero_ordinates_source": "Odlyzko public tables (first zeros)",
        },
        "summary": summary,
        "branch_warnings": branch_warnings,
        "online": results_online,
        "offline": results_offline,
        "diagnostic_checklist": {
            "online_A_mild": "inspect mean_peak_abs_A_over_loglog_online",
            "offline_larger": "compare mean_peak offline vs online",
            "branch_ok": len(branch_warnings) == 0,
            "never_claim_RH": True,
        },
        "status": "L5_DIAGNOSTIC_EXECUTED_NO_RH_CLAIM",
    }

    out_path = Path(__file__).resolve().parents[1] / "rh_L5_phase_diagnostic_results.json"
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")

    print("L5 diagnostic — NO RH CLAIM")
    print("primes <=", x_max, "count", len(primes))
    print("online points", len(results_online), "offline", len(results_offline))
    print(
        "mean peak |A_X| online/offline:",
        summary["mean_peak_abs_A_online"],
        summary["mean_peak_abs_A_offline"],
    )
    print(
        "mean peak |A|/loglog online/offline:",
        summary["mean_peak_abs_A_over_loglog_online"],
        summary["mean_peak_abs_A_over_loglog_offline"],
    )
    print("branch_warnings", len(branch_warnings))
    print("status L5_DIAGNOSTIC_EXECUTED_NO_RH_CLAIM")
    print("wrote", out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
