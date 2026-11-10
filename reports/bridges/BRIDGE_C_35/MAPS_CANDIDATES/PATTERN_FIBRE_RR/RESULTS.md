# RESULTS: PATTERN_FIBRE_RR (Map-PFR1)
PREREG sha256 8b00bced504370a7ea0c9baa1e15e82af33aa065dd7127f848cafcdfccf3331a. Hashed after explore (data/explore.sha256) and before test (logs/test.log, data/test.json). test.py recomputes the label set independently and matches explore.

| fibre | ρ_res (MF2) | ρ_mod (140-label pool, (10u)² mod 8) |
|---|---|---|
| 0 | 1/32 | 1/4 |
| 1 | 1/4 | 1/2 |
| 2 | 3/32 | 0 |
| 3 | 0 | 0 |
| 4 | 7/32 | 1/4 |
| 5 | 1/4 | 0 |
| 6 | 5/32 | 0 |
| 7 | 0 | 0 |

- P1 (exact equality): false. TV = 1/2.
- Supports: {0,1,4} vs {0,1,2,4,5,6}.
- Zeros on {3,7}: yes, but this is a consequence of the square-class obstruction. 2, 5 and 6 vanish too.
- Non-vacuous: ρ_mod is not uniform on the six open fibres.

**Verdict: FAIL (Category A, exact rationals).** Bridge: **NO.**
