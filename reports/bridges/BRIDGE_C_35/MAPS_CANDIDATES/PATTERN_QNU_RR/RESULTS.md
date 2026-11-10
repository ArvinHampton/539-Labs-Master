# RESULTS: PATTERN_QNU_RR (Map-PQR1)
PREREG sha256 1858b03e721ebfe5ecfb2c43f127a89409b66585744b2fd7bc9264b44965b7d5. Hashed after explore and before test. test.py recomputes the result in exact Fractions and matches explore.

| fibre | ρ_res (MF2) | ρ_mod (140-label pool, 140·Q mod 8) |
|---|---|---|
| 0 | 1/32 | 1/8 |
| 1 | 1/4 | 0 |
| 2 | 3/32 | 1/4 |
| 3 | 0 | 1/4 |
| 4 | 7/32 | 1/8 |
| 5 | 1/4 | 0 |
| 6 | 5/32 | 0 |
| 7 | 0 | 1/4 |

- PF1 escaped: 5 fibres carry mass.
- P1 (exact equality): false. TV = 3/4.
- ρ_mod puts mass 1/2 on {3,7}, where ρ_res is 0, and misses 1, 5 and 6.
- Non-vacuous.

**Verdict: FAIL (Category A).** Bridge: **NO.**
