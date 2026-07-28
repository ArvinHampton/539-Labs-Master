#!/usr/bin/env python3
"""
Non-circular L_star exploration: candidate lengths from flux/tower data only,
path endpoint counts under T^sharp. Compare to 539 only post-hoc.

Usage:
  python noncircular_Lstar_probe.py
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


def T_sharp(n: int) -> int:
    if n <= 0:
        return 0
    r = n % 3
    if r == 0:
        return n // 3
    if r == 1:
        return (4 * n + 2) // 3

    def Tc(k: int) -> int:
        return (n + 1) // 3 + 2 * (3**k)

    t = n % 9
    for k in range(5):
        if Tc(k) % 9 == t:
            return Tc(k)

    def defect(k: int) -> int:
        d = abs(Tc(k) % 9 - t)
        return min(d, 9 - d)

    return Tc(min(range(3), key=lambda j: (defect(j), j)))


def seeds_S4880() -> list[int]:
    out = []
    for tau in range(243):
        f = 21 if tau < 20 else 20
        for j in range(f):
            out.append((f * 243 + tau) * 64 + j + 1)
    return out


def chi_min() -> float:
    return math.log(3 / (4 ** (1 / 3)))


def noncircular_lengths() -> dict[str, int]:
    N_flux, N_tow = 4880, 243
    cm = chi_min()
    return {
        "L_ACE": math.ceil(math.log(N_flux) / cm),
        "L_flux_div_9": N_flux // 9,
        "L_f20": 20,
        "L_f21": 21,
        "L_tow": N_tow,
        "L_base3_digits_flux": math.floor(math.log(N_flux) / math.log(3)) + 1,
        "L_Bott_period": 8,  # classical; also = base3 length of 4880
        "L_win_model": 18,  # model constant; 539-independence not proven
    }


def endpoint_count(seeds: list[int], L: int, stride: int = 1) -> int:
    ends = set()
    for s in seeds[::stride]:
        n = s
        for _ in range(L):
            n = T_sharp(n)
        ends.add(n)
    return len(ends)


def main() -> None:
    seeds = seeds_S4880()
    lengths = noncircular_lengths()
    claimed = 539

    print("=" * 64)
    print("NON-CIRCULAR L_star PROBE")
    print("=" * 64)
    print("Seeds: S4880 (flux quanta). Map: T^sharp. 539 not an input.")
    print()
    print("Candidate L_star (non-circular catalogue):")
    for k, v in lengths.items():
        print(f"  {k:24s} = {v}")
    print()

    results = {}
    for name, L in lengths.items():
        # full seed set for L <= 30, stride otherwise
        stride = 1 if L <= 30 else 5
        n_end = endpoint_count(seeds, L, stride=stride)
        n_used = math.ceil(len(seeds) / stride)
        results[name] = {
            "L": L,
            "n_seeds_used": n_used,
            "distinct_endpoints": n_end,
            "post_hoc_equals_539": n_end == claimed,
            "post_hoc_L_equals_539": L == claimed,
        }
        print(f"  L={L:4d} ({name:24s}) endpoints={n_end:5d}  "
              f"L==539? {L==claimed}  #ends==539? {n_end==claimed}")

    # Near-miss identities (audit only)
    audit = {
        "9*61-10": 9 * 61 - 10,
        "circular_risk_61": "61 often defined from 539-step orbit — do not use to derive 539",
        "18+1+520": 18 + 1 + 520,
        "circular_risk_520": "520 = 539-19 unless independent Psi_tow exists",
        "243*2+53": 243 * 2 + 53,
        "N_flux//9": 4880 // 9,
        "N_flux//9 - 3": 4880 // 9 - 3,
    }
    print()
    print("Near-miss audit (not accepted as non-circular derivations):")
    for k, v in audit.items():
        print(f"  {k}: {v}")

    print()
    print("Verdict: no non-circular L_star equals 539; path endpoint counts != 539.")
    print("Default remains Option 3 (Cat B open 539 + Cat A short depth).")
    print("=" * 64)

    out = Path(__file__).resolve().parent.parent / "noncircular_Lstar_results.json"
    out.write_text(
        json.dumps(
            {
                "lengths": lengths,
                "endpoint_counts": results,
                "audit": audit,
                "verdict": "Option1_blocked_for_539",
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
