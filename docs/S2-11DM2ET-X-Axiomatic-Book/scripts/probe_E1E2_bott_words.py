#!/usr/bin/env python3
"""Low-cost E1–E2 style residue-word probes (Bott research notes)."""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path


def T3(n: int) -> int:
    if n <= 0:
        return 0
    r = n % 3
    if r == 0:
        return n // 3
    if r == 1:
        return (4 * n + 2) // 3
    return (2 * n + 1) // 3


def word(n0: int, mod: int, L: int) -> tuple[int, ...]:
    w = []
    n = n0
    for _ in range(L):
        w.append(n % mod)
        n = T3(n)
    return tuple(w)


def main() -> int:
    N_flux = math.floor(math.e**3 * 3**5)
    N_tow = 3**5
    L = 8  # Bott period

    results = {
        "N_flux": N_flux,
        "N_tow": N_tow,
        "word_length": L,
        "mod8_words_1_to_Nflux": len({word(s, 8, L) for s in range(1, N_flux + 1)}),
        "mod8_words_1_to_Ntow": len({word(s, 8, L) for s in range(1, N_tow + 1)}),
        "branch_mod3_words_1_to_Nflux": len({word(s, 3, L) for s in range(1, N_flux + 1)}),
        "charge_mod9_words_1_to_Nflux": len({word(s, 9, L) for s in range(1, N_flux + 1)}),
        "Bott_arith": {
            "N_flux_mod8": N_flux % 8,
            "N_tow_mod8": N_tow % 8,
            "L_pack_mod8": ((N_flux - math.ceil(N_flux / N_tow)) // 9) % 8,
        },
        "equals_539": {},
    }
    for k in (
        "mod8_words_1_to_Nflux",
        "mod8_words_1_to_Ntow",
        "branch_mod3_words_1_to_Nflux",
        "charge_mod9_words_1_to_Nflux",
    ):
        results["equals_539"][k] = results[k] == 539

    out = Path(__file__).resolve().parents[1] / "e1e2_bott_word_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))
    print("wrote", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
