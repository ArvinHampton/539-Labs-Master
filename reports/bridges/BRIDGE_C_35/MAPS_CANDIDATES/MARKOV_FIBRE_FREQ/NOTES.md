# NOTES: MARKOV_FIBRE_FREQ
## Lemmas
- **MF1 (Category A, elementary; formerly mislabeled L1 — not Einstein–Hampton).** On a hit u = 21 + 9j, j ≡ u − 5 (mod 8). So β̂ is exactly the class of u mod 8, and the fibre law among hits is a 2-adic question.
- **MF2 (Category A, about the lifted chain; exact sympy solve, logs/exact.log; formerly mislabeled L2 — not Einstein–Hampton).**
  - The lifted chain mod 216 has a unique closed class {u ≢ 0 mod 4}. This is Lemma V.
  - Its stationary law factorizes: (u mod 8) is independent of (u mod 27). The mod-9 marginal is uniform, giving hit rate 1/9.
  - The u mod 8 law is (0, 7, 8, 5, 0, 1, 8, 3)/32 for u ≡ 0..7.
  - Hence the fibre law among hits is (1, 8, 3, 0, 7, 8, 5, 0)/32.
  - Refining to 2^k·27 for k = 5, 7, 9, 11 leaves it unchanged. The truncation is already exact at 2^3.
- **MF3 (Category B; formerly mislabeled L3 — not Einstein–Hampton).** Real T3 orbits from SHA3 seeds follow this law (holdout χ² = 9.8, df = 5). The open assumption is the heuristic that the branch (u mod 3) is equidistributed and independent of the low 2-adic digits. That is the uniform-lift step, and it is not proved for actual orbits.
- The zeros at fibres 3 and 7 are Lemma V. The nontrivial part is the 1:8:3:7:8:5 pattern, coming from the 2-adic Markov chain on u mod 8 driven by a uniform branch.

## Status
- Path→fibre is now predictable from first principles (residual-internal).
- Still OPEN: C6, C10, C11 and E1–E3. They are blocked on Arvin accepting a Π constraint / grading and a T3 q-series. No Residual↔Resonant map was tested, and no Resonant objects were created.

## Next step
Prove MF3 conditionally, or test it directly. Measure the joint law of (u mod 3, u mod 8) on orbits to check the independence that the uniform-lift step assumes. Then, under the lock, hash-preregister a map that compares the (1,8,3,0,7,8,5,0)/32 law against a pre-specified Resonant-side fibre weighting. That is the first object that could be a non-vacuous Residual↔Resonant test, and it needs Arvin's sign-off.

CORE_FREEZE respected. Only this new folder was written. No push and no send. Order28, RTA_FOUNDATION_BOUND and the order* folders were not touched.
