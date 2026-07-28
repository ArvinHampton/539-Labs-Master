#!/usr/bin/env python3
"""Verify structural claims for L_body = N_flux//9 - f_max under principle (S)."""
from __future__ import annotations

import math
import sys


def main() -> int:
    N = math.floor(math.e**3 * 3**5)  # 4880
    T = 3**5  # 243
    Q = 9
    fmin = N // T
    R = N - fmin * T
    fmax = math.ceil(N / T)
    BQ = N // Q
    r = N % Q
    Lpref = math.floor(math.e**3 / math.log(3))

    assert N == 4880 and T == 243, (N, T)
    assert fmin == 20 and R == 20 and fmax == 21, (fmin, R, fmax)
    assert BQ == 542 and r == 2 and Lpref == 18, (BQ, r, Lpref)

    L_body = BQ - fmax
    assert L_body == 521
    assert L_body == N // 9 - fmax

    L_pack = Lpref + L_body
    L_pack_prime = (N - fmax) // Q
    assert L_pack == 539 == L_pack_prime

    # Identity: 18+521 agrees with single-shot at this flux
    assert Lpref == fmax + (r - fmax) // Q

    # Without (S): two seed-quantum residuals remain
    assert {BQ - fmin, BQ - fmax} == {522, 521}

    # Rival extras principle (S'): packaging 539, not body 521
    assert BQ - math.ceil(R / Q) == 539

    # Uniqueness table (seed-quantum class)
    seed_class = {fmin: BQ - fmin, fmax: BQ - fmax}
    assert seed_class[fmax] == 521 and seed_class[fmin] == 522

    # Fragility of Lpref identity off-model flux
    def id_rhs(n: int) -> int:
        fm = math.ceil(n / T)
        rm = n % Q
        return fm + (rm - fm) // Q

    assert id_rhs(4880) == Lpref
    assert id_rhs(4881) != Lpref  # single-shot and 18+body diverge nearby

    print("OK: forced atoms fmax=21 BQ=542")
    print("OK: L_body=521 under (S); without (S) {521,522} open")
    print("OK: L_pack = L_pack' = 539 at N_flux=4880")
    print("OK: rival (S') BQ-ceil(R/9)=539 (packaging, not body)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
