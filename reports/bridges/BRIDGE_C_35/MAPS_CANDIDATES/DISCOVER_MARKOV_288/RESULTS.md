# RESULTS: DISCOVER_MARKOV_288
PREREG.md sha256 8f2aa764f5328981bb0dfcde52d6f349a90715cb2296d3b0753b784a0bee3e60, hashed after exploration and before the fresh run. Fresh seeds b"fresh-s", s<3000, 539 steps: 1,617,000 steps, 179,867 hits (rate 0.11124, prediction 1/9).

| β̂ | predicted ρ (DM1) | measured | count |
|---|---|---|---|
| 0 | 1/32 = 0.03125 | 0.03178 | 5716 |
| 1 | 8/32 = 0.25000 | 0.24928 | 44837 |
| 2 | 3/32 = 0.09375 | 0.09405 | 16917 |
| 3 | 0 | 0.00009 | 16 (prefix) |
| 4 | 7/32 = 0.21875 | 0.21676 | 38987 |
| 5 | 8/32 = 0.25000 | 0.25110 | 45165 |
| 6 | 5/32 = 0.15625 | 0.15687 | 28215 |
| 7 | 0 | 0.00008 | 14 (prefix) |

Next-hit kernel (DM2), share of fibres 1 and 5 for the next hit: row A (previous hit in {0,2,4,6}) predicted 5/24 = 0.2083 and 7/24 = 0.2917, measured 0.2096 and 0.2940. Row B (previous hit in {1,5}) predicted 7/24 and 5/24, measured 0.2928 and 0.2110.

| Test | Measured | Threshold | Verdict |
|---|---|---|---|
| T1 marginal χ² | 6.74 | ≤ 20.52 | PASS |
| T2 forbidden {3,7} share | 1.67·10⁻⁴ | ≤ 10⁻³ | PASS |
| T3a kernel row A χ² | 5.23 | ≤ 20.52 | PASS |
| T3b kernel row B χ² | 1.91 | ≤ 20.52 | PASS |
| T4 row B vs i.i.d. ρ (non-vacuity) | 1174.6 | > 20.52 | PASS |

**Overall: PASS** (Category B numerical; DM1/DM2 Category A as statements about the lifted chain). **Bridge: NO** (residual-internal; no Π accepted).

## Lemmas
- **DM0 (modulus):** T3 mod M factors through u mod 3M. u mod M does not determine it (3-way branch), so a chain on Z/M is the lifted chain, which assumes the next 3-adic digit is equidistributed. 72 is the minimal modulus carrying q, β̂ and Lemma V. Results at 72/144/216/288 are identical, so 288 is sufficient.
- **DM1:** stationary hit rate 1/9; hit law ρ = (1,8,3,0,7,8,5,0)/32. This **matches MF2 ρ_res exactly** (independent re-derivation at 288, fresh seeds).
- **DM2 (new, refines MF2):** hits are not i.i.d. on fibres. The next-hit law depends only on [previous ∈ {1,5}], with ±1/12 moving between fibres 1 and 5. The stationary average of the two rows recovers ρ.
- Lemma V consistent: closure of {u ≢ 0 mod 4} is asserted in code. The 30 forbidden-fibre hits are all initial-prefix hits.
