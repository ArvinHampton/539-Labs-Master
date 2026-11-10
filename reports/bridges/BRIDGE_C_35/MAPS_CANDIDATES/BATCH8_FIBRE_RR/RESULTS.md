# RESULTS: BATCH8_FIBRE_RR (Map-FRR1)
PREREG.md sha256 b75fa7dadfea3c1ed223bf8c25b51d8b68524841887a3db42b50b7dc62947c2d. Hashed after exploration (data/explore.sha256) and before scripts/test.py ran (logs/test.log, data/test.json).
Authorization: Arvin's "Build" (2026-10-24, America/Chicago), for this map only.

| fibre | ρ_res (Residual, Cat. A) | ρ_res_mod (170n² mod 8) |
|---|---|---|
| 0 | 1/32 | 1/2 |
| 1 | 1/4 | 0 |
| 2 | 3/32 | 1/2 |
| 3 | 0 | 0 |
| 4 | 7/32 | 0 |
| 5 | 1/4 | 0 |
| 6 | 5/32 | 0 |
| 7 | 0 | 0 |

- P1 (exact equality): **false**. TV = 7/8.
- Supports: Resonant {0,2} vs Residual {0,1,2,4,5,6}.
- Zeros on {3,7}: yes. But that is an **accident** of the square-class obstruction, not an independent reason; fibres 1,4,5,6 also vanish.
- Non-vacuity: the committed map is not uniform on the six open fibres. The test is non-vacuous.

**Verdict: FAIL (Category A: exact rational arithmetic).** Bridge: **NO.** No Residual↔Resonant claim.
