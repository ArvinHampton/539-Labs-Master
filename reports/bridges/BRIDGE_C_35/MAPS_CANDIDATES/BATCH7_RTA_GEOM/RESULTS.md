# RESULTS: BATCH7_RTA_GEOM
PREREG.md sha256 f817ce4d2c613813e01198c75ad4b65f63581deeaf77efe048fb01c9c1509a33, hashed after the modular-table script and before any K⁺ computation. Scripts: scripts/modular_table.py, scripts/b7.py (hashes in scripts/SHA256SUMS). Data: data/modular_table.json, data/b7.json. Logs: logs/. Exact ranks (python-flint, fmpz and nmod), with ∂₂∂₁ = 0 asserted. Under 1 s.

Gate: (V, E, F) = (539, 594, 56). OK.
β(Q) = (1, 0, 0). β(F_p) = (1, 0, 0) for every p ∈ {2, 5, 7, 3, 11, 13, 17, 19, 23, 29}. No rank drop at any tested prime, so there is no torsion at the tested primes.

| Map | Prediction | Measured | Verdict | Vacuous? |
|---|---|---|---|---|
| C25 | β(F_p) differs for some p \| 140 vs the controls | identical at all primes | **FAIL** | — |
| C26 | torsion ≠ 0, supported in {2, 5, 7} | no torsion at tested primes | **FAIL** | — |
| C27 | form SS over F_p fails to collapse iff p \| 140 | no written F_p matrices | **OPEN** | — |
| C6, C10, C11, E1–E3 | — | blocked | OPEN | — |

**Bridge: NO.**

Post-hoc (Category A remark, no verdict change): the written facts β = (1,0,0) over F₂ with χ = 1, plus no rank drop at the 10 tested primes, mean K⁺ is Z-acyclic at those primes. Full Z-acyclicity would need either a Smith normal form or the remaining primes dividing the elementary divisors; a contractibility argument (already claimed in the written lock) would cover it. K⁺ homology is blind to every prime, so no modular split can be read from it.
