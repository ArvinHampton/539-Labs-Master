# RESULTS: BATCH3_RTA_GEOM
PREREG.md sha256 b57478f74b920a6a059391ea2d937a6f1659b824baa2a8a2e32bdcae8aba21b2, hashed before tests. Script scripts/b3.py (hash in scripts/SHA256SUMS); data data/b3.json; log logs/b3.log. Exact integer arithmetic, under 1 s.

| Map | Prediction | Measured | Verdict | Cat |
|---|---|---|---|---|
| C12 | norm-form set S ⊂ O_res is non-empty and equidistributed over β♯ | S = ∅ | **FAIL** | B |
| C13 | reversal σ preserves same-tower adjacent pairs; gate: count = 353 | reproduced 297 adjacent pairs (≠ 353) | **VOID** (gate failed, by rule) | B |
| C14 | S_Q non-empty and disjoint from S | S_Q = ∅ | **FAIL** | B |
| C15 | 8 \| k (order19 A2c nonzero count) | awaits order19 | **OPEN** | B |
| C6, C10, C11, E1–E3 | — | no written Π, grading or predicate found | **OPEN** | B |

## Structural reasons (Category A, elementary, found after the run; verdicts unchanged)
- C12/C14: every x ∈ O_res satisfies 3 | x and 9 ∤ x (x = 21+9j ≡ 3 mod 9). Mod 3: a² − 35b² ≡ a² + b² and 2a²+14ab+7b² ≡ a² + (a+b)². Both vanish mod 3 only when 3 | a and 3 | b, which forces 9 | value. So no x ∈ O_res is represented by either form (Category A). The maps were badly posed, and this is not a near-miss.
- C13: the written "353 same-tower pairs" is Σ_t C(n_t, 2) (all unordered pairs within a tower). Recomputed post-hoc: 353 exactly. Adjacent pairs number 538 − Σδf = 538 − 241 = 297. The gate used the wrong reading, so the verdict is VOID. A re-test would need a new prereg.
