# NL ERRATUM 18 — constant in D4 of NL_DERIVED_BPS_B12_CHI_DEPENDENT_WALLS_2026-11-09_2017.md (f8801bff…)
2026-11-09, 20:19 CST. **NL derived proposal.** Additive correction; the target file is not edited. Authority OW t4426 d5eaeef3.

**Tally: PROVED 1 · CONDITIONAL 0 · OPEN 0 · REFUTED 0 · total 1**

- **E18-1 (PROVED).** In D4 the bound "|K_int + 6k_x + 6ε/L| ≤ 10δ, so D2 fails for δ < (3/5)·min ε/L" is wrong in its constant.
  - Correct count: K_int is a sum of 6 tangential internal entries, each perturbed by at most δ, giving ≤ 6δ. The term 6k_x contributes ≤ 6δ. The total is **≤ 12δ**.
  - So D2 fails for **δ < ½·min_{S⁴} ε/L**. This is the same threshold as the all-direction NEC failure in D4.
  - The conclusion of D4 (no BPS ℤ₂ wall near MN2; the mismatch is zeroth order) and its PROVED label are unchanged. The tally of the target file is unchanged (4/2/1/0).
- Junction UNSOLVED; gap unchanged. Tip 7cddb188… untouched.
