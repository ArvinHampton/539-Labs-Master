#!/usr/bin/env python3
"""
Verify Steps 1–8 of Foundational Arithmetic Packaging.

Canonical writeup: Foundational_Arithmetic_Packaging.md
"""
from __future__ import annotations

import math
import sys


def main() -> int:
    # Step 1 — instanton weight
    e3 = math.e**3
    series = sum(3**k / math.factorial(k) for k in range(0, 60))
    assert abs(series - e3) < 1e-12

    # Step 2 — flux budget
    N_flux = math.floor(e3 * 3**5)
    assert N_flux == 4880

    # Step 3 — towers and democratic seeds
    N_tow = 3**5
    assert N_tow == 243
    f_min = N_flux // N_tow
    R = N_flux - f_min * N_tow
    f_max = math.ceil(N_flux / N_tow)
    assert f_min == 20 and R == 20 and f_max == 21
    assert (N_tow - R) == 223
    assert 21 * R + 20 * (N_tow - R) == N_flux

    # Step 4 — charge-sector budget
    B_Q = N_flux // 9
    assert B_Q == 542
    rem = N_flux % 9
    assert rem == 2

    # Step 5 — prefix
    ratio = e3 / math.log(3)
    L_pref = math.floor(ratio)
    assert L_pref == 18
    assert abs(ratio - 18.28264359534713) < 1e-10
    # continued fraction leading term
    assert math.floor(ratio) == 18

    # Step 6 — Principle (S): selector among seed-quantum residuals
    open_pair = {B_Q - f_min, B_Q - f_max}
    assert open_pair == {522, 521}
    # (S) selects f_max
    L_body = B_Q - f_max

    # Step 7 — residual under (S)
    assert L_body == 521
    assert L_body == N_flux // 9 - f_max
    L_pack_prime = (N_flux - f_max) // 9
    assert L_pack_prime == 539

    # Coherence identity at model flux
    assert L_pref == f_max + (rem - f_max) // 9
    assert L_pref + L_body == L_pack_prime

    # Step 8 — composite packaging
    L_pack = L_pref + L_body
    assert L_pack == 539 == L_pack_prime
    # No 539 on defining RHS atoms
    atoms = {N_flux, N_tow, f_max, f_min, B_Q, L_pref, L_body}
    assert 539 not in atoms

    print("OK: Steps 1–5 Category A integers verified")
    print(f"OK: Step 6 (S) selects L_body={L_body} from open pair {sorted(open_pair)}")
    print(f"OK: Step 7 L_body={L_body}, L_pack'={L_pack_prime}")
    print(f"OK: Step 8 L_pack={L_pack} (non-circular under (S))")
    print("Q.E.D. arithmetic packaging")
    return 0


if __name__ == "__main__":
    sys.exit(main())
