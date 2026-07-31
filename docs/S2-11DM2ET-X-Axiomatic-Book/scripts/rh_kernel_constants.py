#!/usr/bin/env python3
"""
Explicit majorants for C_u^(0), C_u^(1) for one fixed GHK-admissible cutoff.

Pure computation: fix f on [0,1], define u via GHK change of variables,
bound |Im U(z) + Arg z| for small z and |U(z)| for large z via E1 series /
integration-by-parts majorants.

Status: KERNEL_CONSTANTS_NO_RH_CLAIM
"""
from __future__ import annotations

import json
import math
from pathlib import Path

try:
    import mpmath as mp
except ImportError:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "mpmath", "-q"])
    import mpmath as mp

mp.mp.dps = 40


# ---------------------------------------------------------------------------
# Fixed smooth bump f on [0,1], mass 1
# Standard C^∞ flat bump: f(t) ∝ exp(-1/(t(1-t))) on (0,1), 0 elsewhere
# ---------------------------------------------------------------------------

def _raw_bump(t: mp.mpf) -> mp.mpf:
    if t <= 0 or t >= 1:
        return mp.mpf(0)
    return mp.exp(-1 / (t * (1 - t)))


def _normalize_mass() -> mp.mpf:
    # ∫_0^1 raw_bump
    return mp.quad(lambda t: _raw_bump(mp.mpf(t)), [0, 1])


_MASS = _normalize_mass()


def f(t: mp.mpf) -> mp.mpf:
    """Mass-1 smooth density on [0,1]."""
    return _raw_bump(t) / _MASS


def max_f_derivative_bound(K: int = 4) -> dict:
    """
    Numerical max of |f| and crude |f'| on a grid (for Mellin/power constants).
    Not a rigorous certified max — labelled as numerical majorant candidates.
    """
    N = 4000
    max_f = mp.mpf(0)
    max_fp = mp.mpf(0)
    h = mp.mpf("1e-6")
    for i in range(1, N):
        t = mp.mpf(i) / N
        ft = f(t)
        if abs(ft) > max_f:
            max_f = abs(ft)
        # central difference for f'
        fp = (f(t + h) - f(t - h)) / (2 * h)
        if abs(fp) > max_fp:
            max_fp = abs(fp)
    return {
        "max_abs_f_grid": float(max_f),
        "max_abs_fp_grid": float(max_fp),
        "note": "Grid maxima — use as provisional majorants, not certified.",
    }


# ---------------------------------------------------------------------------
# GHK u via u(x) = X f(X log(x/e) + 1) / x on support [e^{1-1/X}, e]
# Change of variables: let τ = X log(x/e) + 1 ∈ [0,1] ⇒ x = e · exp((τ-1)/X)
# dx/x = dτ / X, so ∫ u(x) dx = ∫ f(τ) dτ = 1. Good.
# ---------------------------------------------------------------------------

def x_of_tau(tau: mp.mpf, X: mp.mpf) -> mp.mpf:
    return mp.e * mp.exp((tau - 1) / X)


def log_x_of_tau(tau: mp.mpf, X: mp.mpf) -> mp.mpf:
    return 1 + (tau - 1) / X  # since log x = 1 + (τ-1)/X


# ---------------------------------------------------------------------------
# E1 bounds
# ---------------------------------------------------------------------------

def E1_small_remainder(z: mp.mpc) -> mp.mpc:
    """E1(z) + γ + log z  (principal), series."""
    # series: -sum_{k≥1} (-z)^k /(k k!)
    s = mp.mpc(0)
    term = mp.mpc(1)
    for k in range(1, 80):
        term *= -z / k
        s += term / k
    return -s  # E1 + γ + log z = -sum (-z)^k/(k k!) wait
    # Standard: E1(z) = -γ - log z - sum_{k=1}^∞ (-z)^k /(k · k!)
    # so E1 + γ + log z = - sum (-z)^k /(k k!)
    # and sum (-z)^k /(k k!) = s if term accumulates (-z)^k / k! then /k
    # Let me recompute carefully below.


def E1_plus_gamma_log(z: mp.mpc) -> mp.mpc:
    """E1(z)+γ+log(z) via series (Arg in (-π,π))."""
    s = mp.mpc(0)
    zk = mp.mpc(1)
    for k in range(1, 100):
        zk *= -z / k  # zk = (-z)^k / k!
        s += zk / k
    return -s


def C_u1_from_series(X: float = 10.0, n_samples: int = 40) -> dict:
    """
    For |z|≤1: U(z) = ∫ u(x) E1(z log x) dx
    = -log z - γ - ∫ u log log x dx + R(z)
    with |R(z)| ≤ |z| · ∫ u |log x| · e  roughly from |E1+γ+log(z log x)| ≤ e |z log x|
    when |z log x| ≤ 1, and more carefully:
    |E1(w)+γ+log w| ≤ sum |w|^k/(k k!) ≤ |w| sum |w|^{k-1}/(k!) ≤ |w| e^{|w|}
    For |w|≤ Wmax with Wmax = |z| * max log x ≤ |z| * 1 (since log x ≤ 1 on supp for large X? 
    log x ∈ [1-1/X, 1], so |log x| ≤ 1).
    Thus for |z|≤1, |w|≤1:
    |E1(w)+γ+log w| ≤ |w| e ≤ e |z|  (since |log x|≤1)
    Also log w = log z + log log x, so
    U(z) = ∫ u [ -γ - log z - log log x + r(w) ] dx
    with |r| ≤ e |z|.
    Hence |U(z) + log z + γ + c_u| ≤ e |z|, c_u = ∫ u log log x.
    Therefore |Im U(z) + Arg z| ≤ e |z|  for |z|≤1 on principal sheet.
    So C_u^(1) ≤ e  is a rigorous majorant independent of u (only needs |log x|≤1 on supp).
    """
    Xmp = mp.mpf(X)
    # compute c_u = ∫_0^1 f(τ) log(log x(τ)) dτ
    def integrand(tau):
        tau = mp.mpf(tau)
        lx = log_x_of_tau(tau, Xmp)
        # log x ∈ (0,1] for X≥1; need log log x = log(lx)
        if lx <= 1:
            # lx ≤ 1 always here; for lx close to 1-1/X > 0
            return f(tau) * mp.log(lx)
        return f(tau) * mp.log(lx)

    c_u = mp.quad(integrand, [0, 1])

    # Numerical check of remainder at sample z
    max_rem = mp.mpf(0)
    samples = []
    for k in range(n_samples):
        # sample z on circle |z|=0.5 and |z|=1
        for r in [mp.mpf("0.25"), mp.mpf("0.5"), mp.mpf("1.0")]:
            ang = 2 * mp.pi * k / n_samples
            z = r * mp.exp(mp.j * ang)
            if abs(mp.arg(z)) > mp.pi - mp.mpf("0.05"):
                continue

            def U_integrand(tau):
                tau = mp.mpf(tau)
                lx = log_x_of_tau(tau, Xmp)
                w = z * lx
                return f(tau) * mp.ei(-w) * (-1)  # wait: E1(w) = -Ei(-w) for Arg
                # mpmath: e1(w) is E1(w)

            # Use mp.e1
            def Uint(tau):
                tau = mp.mpf(tau)
                lx = log_x_of_tau(tau, Xmp)
                return f(tau) * mp.e1(z * lx)

            try:
                Uval = mp.quad(Uint, [0, 1])
            except Exception:
                continue
            # predicted: -log z - γ - c_u
            pred = -mp.log(z) - mp.euler - c_u
            rem = abs(Uval - pred)
            if rem > max_rem:
                max_rem = rem
            samples.append(
                {
                    "r": float(r),
                    "arg": float(ang),
                    "rem": float(rem),
                    "e_abs_z": float(mp.e * abs(z)),
                }
            )

    return {
        "C_u1_rigorous_majorant": float(mp.e),
        "derivation": (
            "|E1(w)+γ+log w| ≤ |w|e^{|w|} ≤ e|z| for |z|≤1, |log x|≤1 on GHK support; "
            "hence |Im U + Arg z| ≤ e|z| so C_u^(1) ≤ e."
        ),
        "c_u_for_X": float(c_u),
        "X": X,
        "max_numerical_remainder_on_samples": float(max_rem),
        "sample_count": len(samples),
        "status": "C_u1_BOUND_RIGOROUS_e",
    }


def C_u0_large_z(X: float = 10.0, delta: float = 0.2) -> dict:
    """
    For |z|≥1 and |Arg z| ≤ π - δ:
    |E1(z)| ≤ e^{-Re z} / |z| * (1 + O(1/|z|)) ≤ C(δ)/|z|.

    Integration by parts: E1(z) = e^{-z}/z · ∫_0^∞ e^{-t}/(1+t/z) dt
    so |E1(z)| ≤ e^{-Re z}/|z| · ∫_0^∞ e^{-t} / (1 - |t/z|)_+ ...
    Standard bound: for |Arg z| ≤ θ < π,
    |E1(z)| ≤ e^{-Re z} / (|z| sin φ) or simpler:
    |E1(z)| ≤ e^{-x cos φ} / (r) where z=re^{iφ}, for |φ|<π/2 use cos.
    
    Safe majorant used here (NIST / standard):
    For |Arg z| ≤ π - δ with δ∈(0,π):
      |E1(z)| ≤ e^{-Re^+ z} / (|z| · sin(δ/2))   [conservative]
    More elementary for Re z ≥ 0: |E1(z)| ≤ 1/|z|.
    For Re z < 0 but |Arg|≤π-δ: |E1(z)| ≤ e^{-Re z}/(|z| c_δ).

    On GHK support log x ∈ [1-1/X, 1] ⊂ (0,1], so
    U(z) = ∫ f(τ) E1(z · log x(τ)) dτ
    |U(z)| ≤ sup_{ℓ∈[1-1/X,1]} |E1(z ℓ)|.

    For |z|≥1, |Arg z|≤π-δ, |E1(zℓ)| ≤ M_δ / |zℓ| ≤ M_δ / (|z|(1-1/X)).

    We take M_δ from numerical max of |E1(w)|·|w| on the arc |w|≥1-1/X, |Arg|≤π-δ.
    """
    Xmp = mp.mpf(X)
    lmin = 1 - 1 / Xmp
    # Sample on |z|=1..20, Arg in [-(π-δ), π-δ]
    M = mp.mpf(0)
    n_r, n_a = 30, 60
    pi = mp.pi
    max_arg = pi - mp.mpf(delta)
    for i in range(n_r):
        r = 1 + mp.mpf(i) * 20 / n_r
        for j in range(n_a + 1):
            ang = -max_arg + 2 * max_arg * j / n_a
            z = r * mp.exp(mp.j * ang)
            for ell in [lmin, mp.mpf(1)]:
                w = z * ell
                try:
                    val = abs(mp.e1(w)) * abs(w)
                except Exception:
                    continue
                if val > M:
                    M = val

    # Also analytic majorant for Re z ≥ 0: |E1|≤1/|z| ⇒ M≥1
    # For the strip, use M_num
    C_u0 = M / lmin  # |U| ≤ M/(|z| lmin) * mass 1 ⇒ C_u0 = M/lmin for min(1,1/|z|) form
    # For |z|≥1: |U| ≤ C_u0 / |z| with C_u0 = M/lmin
    # For min(1, 1/|z|): when |z|≥1, 1/|z|≤1 so |U|≤ C_u0 min(1,1/|z|) if C_u0≥1
    # Need also |z|<1 large bound separately — for medium we use min(1,1/|z|)
    # Bound |U|≤ max(sup_{|z|<1}|U|, C_u0) * min(1,1/|z|) roughly

    # Bound |U| for |z|≤1: from small-z expansion |U| ≤ |log z| + γ + |c_u| + e
    # worst |log z| on |z|≥ r_loc is large near 0 — local region excluded.
    # For medium |z|≥1: C_u0 as above.

    return {
        "delta": delta,
        "X": X,
        "M_delta_num_max_abs_E1_times_abs_w": float(M),
        "lmin": float(lmin),
        "C_u0_for_abs_U_le_C_over_abs_z": float(M / lmin),
        "C_u0_working_majorant": float(max(M / lmin, mp.mpf(1))),
        "note": (
            "Numerical max of |E1(w)|·|w| on sampled arc |Arg|≤π-δ, |w|≥lmin. "
            "Treated as working majorant; not interval-arithmetic certified."
        ),
        "status": "C_u0_WORKING_NUMERICAL_MAJORANT",
    }


def main() -> None:
    f_stats = max_f_derivative_bound()
    c1 = C_u1_from_series(X=10.0)
    c0 = C_u0_large_z(X=10.0, delta=0.2)

    # Package freeze used by M1.2 sketches
    package = {
        "u_family": "GHK: u(x)=X f(X log(x/e)+1)/x, f=normalized flat bump on [0,1]",
        "C_u1_rigorous": c1["C_u1_rigorous_majorant"],
        "C_u0_working": c0["C_u0_working_majorant"],
        "C_u0_status": c0["status"],
        "C_u1_status": c1["status"],
        "f_grid_stats": f_stats,
        "details_C_u1": c1,
        "details_C_u0": c0,
        "NO_RH_CLAIM": True,
    }

    out = Path("/workspace/rh/rh_kernel_constants_results.json")
    out.write_text(json.dumps(package, indent=2))
    print(json.dumps(package, indent=2))
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
