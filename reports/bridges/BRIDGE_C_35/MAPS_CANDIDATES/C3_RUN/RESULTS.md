# RESULTS: Map-C3 run
Prereg: ../PREREG.md (sha256 fdd4c2be09aef174ab85bb5d7b72cce3cedc9d498b7f47d72814e90092dfa424, unchanged, verified OK). Script scripts/c3.py (hash in scripts/SHA256SUMS), data data/c3.json, log logs/c3.log. Exact mod-p linear algebra (python-flint), read-only imports of A35_lawspace_exact (symbols.py, exact_dim.py). Runtime ~12 s; ulimit -v 3 GB.

Method: rebuild the 69 symmetry relations, take the 36-symbol quotient basis (V), reduce the unnormalised S-matrix GS (= √35·M_S) to V, set P = GS²/35, check P² = I, then rank(P∓I).

| p | dim V | P² = I | rank(P−I) | rank(P+I) | dim V^{P=+1} | dim V^{P=−1} |
|---|---|---|---|---|---|---|
| 1 764 001 | 36 | yes | 0 | 36 | 36 | 0 |
| 6 468 001 | 36 | yes | 0 | 36 | 36 | 0 |
| 7 644 001 | 36 | yes | 0 | 36 | 36 | 0 |

**P = I on V** at all three primes.

Preregistered checks:
- dim V^{P=−1} ∈ {1, 18, 21, 20}: measured 0 → fails.
- dim V^{P=−1} − dim V^{P=+1} ≡ 1 (mod 2): measured −36 ≡ 0 → fails.

**Verdict: Map-C3 FAIL** (Category B; candidate dead as stated). No bridge claim.

Why (Category A remark, not new evidence): −I is an automorph of A, so G_{−α,−β} = G_{α,β}. P is the map (α,β) ↦ (−α,−β), so it acts trivially on V. The P-odd/P-even split therefore lives on the 105 symbols, not on the function space V. C3 could not have passed as worded.

Post-hoc only (not preregistered, not upgraded): on the 105 symbols, rank(P−I) = 51 and rank(P+I) = 54. That gives +1-eigenspace dim 54 and −1-eigenspace dim 51 at all three primes. Any map using 54/51 needs a new prereg.
