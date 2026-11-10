# NOTES: L3_INDEPENDENCE
## Lemmas
- **(Category A, static, CRT).** For any c mod 2^k and a mod 3, the integers with u ≡ c (mod 2^k) and u ≡ a (mod 3) have density 1/(3·2^k).
  - The T3 branch is set by u mod 3, while u mod 2^k is set by low binary digits. These are independent coordinates of Z/(3·2^k).
  - This is why the uniform-lift chain is natural. It says nothing about orbits.
- **(Category A, from earlier work.)** Lemma V: after the opening run of pure ÷3 steps, u ≢ 0 mod 4 for every later step. Confirmed again here, with 0 violations after burn-in.
- **(Category B, upgraded evidence.)** Along real T3 orbits, u mod 3 is uniform and independent of u mod 8 and of u mod 64, within the pre-registered tolerance:
  - TV distance 0.0023 from (1/3) × law8.
  - Maximum conditional deviation 0.005, which is consistent with sampling noise.
  - The measured defect on the fibre law is ≤ 5.2·10⁻⁴.
- **MF3 remains Category B.** No orbit-level proof exists. That would need equidistribution of the 3-adic digits that the map consumes, given the 2-adic history. The numbers are consistent with zero dependence. The bounded defect is < 0.0006 on each fibre and < 0.006 in TV.

## Caveat
The thinning is every 8th step. Residual autocorrelation would only inflate χ² values, and all of them came out small.

## Next residual-internal step
Try to make MF3 exact in a skew-product form. Write T3 on Z₂ × Z₃ as a 2-adic map driven by the 3-adic digit stream. Then test, or prove, that the branch sequence (u_i mod 3) is i.i.d.-uniform conditioned on past 2-adic states, e.g. by n-gram (block) tests of the branch word up to length 6 against 3^−L. If those tests pass, the fibre law becomes a theorem conditional on a single digit-normality hypothesis. Any Resonant-side fibre weighting still needs Arvin's sign-off under the lock.

CORE_FREEZE respected: new folder only. No push or send. The order*/ folders and RTA_FOUNDATION_BOUND were not touched. C6, C10, C11 and E1–E3 were not touched, and no grading or Π was accepted.
