# RESULTS: BATCH2
PREREG.md sha256 7d88884cec365b4c184be5ebd04b0bd20308e277c47b86b789243d3570b4fb95, hashed before tests. Script scripts/b2.py (hash in scripts/SHA256SUMS); data data/b2.json; log logs/b2.log. Exact integer arithmetic, under 1 s.

| Map | Prediction | Measured | Verdict | Cat |
|---|---|---|---|---|
| C7 | 49 \| ord(M_T), 11 ∤ ord(M_T) | ord(M_T) = 140 = 2²·5·7 | **FAIL** (7 divides it, 49 does not) | B |
| C8 | max free T3 depth on [1,539] = 18 | 29 (n = 487); all n reach 1 | **FAIL** | B |
| C9 | #{depth ≤ 14} = 521 | 434 | **FAIL** | B |
| C10 | Π splits into 4 segments ordered by theta norms | no written Π | **OPEN** | B |
| C11 | ±1 balance on the 8 fibre blocks from P-even A₁ = 0 | no written grading | **OPEN** | B |

No bridge claim. Post-hoc only: ord(M_T) = 140 equals the discriminant of Q(√35), consistent with the T-law of a level-140 Weil-type representation; this is expected modular structure, not a residual link.
