#!/usr/bin/env python3
"""
Verify T3 integrality, mixed-scale g_s residue vanishing, and 539 arithmetic.

Category A arithmetic only. Residual Discrete Algebra (539 COUNT) != Resonant.
Residual-flux provenance mandatory. Continuum ARCHIVE.

2026-08-21
"""

from __future__ import annotations

import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def t3_rational(n: int) -> Fraction:
    r = n % 3
    if r == 0:
        return Fraction(n, 3)
    if r == 1:
        return Fraction(4 * n + 2, 3)
    return Fraction(2 * n + 1, 3)


def t3_floor(n: int) -> int:
    r = n % 3
    if r == 0:
        return n // 3
    if r == 1:
        return (4 * n + 2) // 3
    return (2 * n + 1) // 3


def t3_exact(n: int) -> int:
    """Exact-integer form equivalent to canonical floor T3."""
    r = n % 3
    if r == 0:
        return n // 3
    if r == 1:
        return (4 * n + 2) // 3
    return (2 * n - 1) // 3


def pochhammer_neg(s: int, n: int, deg: int) -> dict[int, int]:
    """Power series of 1 / (-q^s; q^s)_n truncated at deg. Keys = exponents."""
    coeff = {0: 1}
    for j in range(1, n + 1):
        nxt: dict[int, int] = defaultdict(int)
        power = s * j
        # 1 / (1 + q^{s j}) = sum_{m>=0} (-1)^m q^{m s j}
        m = 0
        while m * power <= deg:
            sign = 1 if m % 2 == 0 else -1
            for e, c in coeff.items():
                ne = e + m * power
                if ne <= deg:
                    nxt[ne] += sign * c
            m += 1
        coeff = {e: c for e, c in nxt.items() if c}
    return coeff


def g_s_coeffs(s: int, deg: int) -> dict[int, int]:
    out: dict[int, int] = defaultdict(int)
    n = 0
    while n * n <= deg:
        rec = pochhammer_neg(s, n, deg - n * n)
        for e, c in rec.items():
            out[n * n + e] += c
        n += 1
    return {e: c for e, c in out.items() if 0 <= e <= deg and c}


def main() -> None:
    non_integral = []
    for n in range(50):
        val = t3_rational(n)
        if val.denominator != 1:
            non_integral.append(
                {
                    "n": n,
                    "n_mod_3": n % 3,
                    "value": str(val),
                    "branch": "(2n+1)/3",
                }
            )

    exact_matches_floor = all(t3_exact(n) == t3_floor(n) for n in range(200))

    g7 = g_s_coeffs(7, 80)
    squares_mod_7 = {0, 1, 2, 4}
    violations = sorted(e for e in g7 if (e % 7) not in squares_mod_7)
    residues = sorted({e % 7 for e in g7})

    e3 = math.exp(3)
    n_flux = math.floor(e3 * 3**5)
    # B' = floor((N_flux - f_max)/9) == 539  =>  4880 - 9*539 - 8 <= f_max <= 4880 - 9*539
    # 9*539 = 4851; 4880-4851 = 29; so 21 <= f_max <= 29
    fmax_lo = n_flux - 9 * 539 - 8
    fmax_hi = n_flux - 9 * 539

    results = {
        "date": "2026-08-21",
        "t3_rational_non_integral_0_49_count": len(non_integral),
        "t3_rational_non_integral_sample": non_integral[:5],
        "all_failures_mod_3_equal_2": all(x["n_mod_3"] == 2 for x in non_integral),
        "t3_exact_equals_floor_0_199": exact_matches_floor,
        "g7_degree": 80,
        "g7_vanishing_violations": violations,
        "g7_nonzero_residues_mod_7": residues,
        "packaging": {
            "539_factor": 7**2 * 11,
            "fibre": 3 * 68 + 5 * 67,
            "window_body": 18 + 521,
        },
        "n_flux_floor_e3_3_5": n_flux,
        "f_max_interval_for_B_prime_539": [fmax_lo, fmax_hi],
        "hygiene": "Residual Discrete Algebra (539 COUNT) != Resonant",
    }

    print(json.dumps(results, indent=2))
    out = Path(__file__).with_name("verify_gs_euler_g7_t3_results.json")
    try:
        out.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    except OSError:
        pass


if __name__ == "__main__":
    main()
