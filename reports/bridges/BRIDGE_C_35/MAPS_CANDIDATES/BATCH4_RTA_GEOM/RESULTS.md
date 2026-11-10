# RESULTS: BATCH4_RTA_GEOM
PREREG.md sha256 d4f727655004cf599d2a0c2564109913c02f8e0a30ab9dbb8b3474c0aa189475, hashed before tests. Script scripts/b4.py (hash in scripts/SHA256SUMS); data data/b4.json; log logs/b4.log. Under 1 s.

| Map | Prediction | Measured | Verdict | Cat |
|---|---|---|---|---|
| C15 closeout | 8 \| k, k = #companions with A2c ≠ 0 | k = 105 (every column nonzero; min column max 6.14; no gap hit) | **FAIL** (105 = 8·13 + 1) | B (float data from order18 CO = corner(), RG4) |
| C16 | tower-change edges are equidistributed over i mod 8 (max − min ≤ 1) | counts [27, 28, 40, 26, 27, 27, 39, 27]; gate Σδf = 241 OK | **FAIL** | B (exact integers) |
| C17 | tower occupancy (n_t) is a palindrome | gates OK (242 towers, 353 pairs); head 3,2,2,3,… vs tail …,2,2,1 | **FAIL** | B (exact) |
| C18 | v_r = v_{1−r} on fibres (P-even reversal symmetry) | v = −[27, 28, 40, 26, 27, 27, 39, 27]; v₀ = −27 vs v₁ = −28 | **FAIL** | B (exact) |
| C6, C10, C11, E1–E3 | — | still no written Π, ±1 grading or path predicate | **OPEN** | B |

No bridge passed. No bridge claim.

Post-hoc (not preregistered, no verdict change):
- The C16/C18 peaks at classes 2 and 6 come from the arithmetic of 9j against tower widths 21/20. Mod 8 these align with period 4. This is a carrier-internal artifact, not modular structure.
- C15: A2c is nonzero on every one of the 105 companions, so A2c has full support. This agrees with order18/19 ("P-even and nonzero").
