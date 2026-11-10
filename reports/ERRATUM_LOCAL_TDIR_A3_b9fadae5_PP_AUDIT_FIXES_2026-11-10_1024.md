# ERRATUM (Local-derived) to FINDINGS_LOCAL_t4436_TDIR_GAUSS_AND_A3_L1_CHI_M7_2026-11-10_1016.md (b9fadae5…) and to the 65/15 figure in the 1017 rollup erratum, applying PP audit f66e0b90. 2026-11-10, written 10:24 CST (America/Chicago)

- **Scope.** Additive. The 1016 findings file and the 1017 rollup erratum are NOT edited, deleted, renamed or moved. No CERT. No Gemini. Nothing sent outside. Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, checked before and after writing. "Resonant algebra" (RTA historical alias only). A citation alone never makes a claim PROVED (OW 36683379). **Nothing is adopted.**
- **Source audit:** FINDINGS_PP_AUDIT_LOCAL_TDIR_A3_b9fadae5_2026-11-10_1019.md, sha256 f66e0b90a68afd244eeeb0322bbbf4acd8b11a6619796d1cabdd6955b4660f74 (verified on disk; matches the stated sha).
- **Authority.** Owner t4436. Running jobs were not disturbed: s1e (PID 932685), chain_v2 (PID 1015729), s2e (PIDs 1088107/1088109), and pp_ttheta1_check.

## F1. In §3, the general inversion constant is √f/G

1016 §3 writes Θ(1/u,χ) = (G/√f) u^{1/2} Θ(u,χ). The identity already recorded in 1016 §2 is

Θ(u,χ) = (G/√f) u^{-1/2} Θ(1/u,χ).

Solving for the inverted series, the general constant is √f/G:

Θ(1/u,χ) = (√f/G) u^{1/2} Θ(u,χ).

Writing G/√f in place of √f/G is valid here only because G/√f = 1 (for χ₁₄₀ one has G = √140, so G/√f = 1; the odd companion used in the same section is G/(i√7) = 1). The functional-equation form Λ(s,χ) = (G/√f) Λ(1−s,χ) is taken from the §2 identity, not from the inverted constant, and is unaffected. Both root numbers remain +1.

## F2. L1 and L2 in the a-3 proof

The evaluation L(1, χ₋₇) = π/√7 does not use the class number formula, GRH, or h(−7). Two analytic steps that 1016 left implicit are recorded here, following PP's audit (and using PP's elementary proof of L1).

**L1 (pointwise sawtooth series).** For 0 < x < 1, Σ_{n=1}^N sin(2π n x)/n → π(1/2 − x). Proof:

- Write S_N(x) = Σ_{n=1}^N sin(2π n x)/n. Then S_N(1/2) = 0, and S_N′(y) = π( sin((2N+1)π y)/sin(π y) − 1 ).
- So for 0 < x ≤ 1/2: S_N(x) = π(1/2 − x) − π ∫_x^{1/2} sin((2N+1)π y)/sin(π y) dy.
- The integral is O(1/N) by one integration by parts, since 1/sin(π y) is C¹ on [x, 1/2].
- For x > 1/2, use S_N(1−x) = −S_N(x).

**Application of L1 at conductor 7.** Let χ = χ₋₇. For a = 1, …, 6, set x = a/7 ∈ (0,1) and pass to the limit in L1. Multiply by χ(a) and sum over a. The inner trigonometric sums are

Σ_{a=1}^6 χ(a) sin(2π n a / 7) = Im( Σ_a χ(a) e(n a / 7) ) = Im( χ(n) G(χ) ).

By F3 below, G(χ) = i√7, so Im(χ(n) G(χ)) = χ(n) √7 (and the sum vanishes when 7 | n). Symmetric finite sums are used throughout, so no rearrangement arises. One obtains

(1/7) Σ_{a=1}^6 a χ(a) = −(√7/π) · lim_{N→∞} Σ_{n≤N} χ(n)/n.

The left-hand side is (1/7)·(−7) = −1 by the exact sum recorded below, so the series Σ χ₋₇(n)/n converges to π/√7.

**L2 (the series value is L(1, χ)).** The partial sums A(n) = Σ_{k=1}^n χ(k) are bounded, |A| ≤ 7. Abel summation therefore shows that Σ χ(n) n^{-s} converges locally uniformly on Re s > 0. The series is holomorphic there, and equals the analytic continuation of L(s,χ) already obtained from the Mellin split in 1016 §3 (T-Dir for χ₋₇), by the identity theorem (the two agree on Re s > 1). Hence L(1, χ₋₇) = Σ χ₋₇(n)/n = π/√7.

L1 and L2 are elementary analysis of the same kind already used in the Mellin/continuation step. With them written out, the a-3 proof is complete and exact. The 60-digit lfun agreement in s6 remains an illustration only.

## F3. Independent proof of G(χ₋₇) = i√7 (no dependence on T-theta1)

1016 carried G(χ₋₇) = i√7 from the pending T-theta1 filing FINDINGS_LOCAL_t4436_T_THETA1_UNARY_THETA_2026-11-10_1010.md (sha256 fff902b4ea0cde17b96b0da60318afe8446f4e209dcc2d24bd26cb78a320dc59). PP re-proved the same evaluation independently of that file, and that independent proof is the citation used from here on, for both a-3 and b-1:

- G² = −7 exactly in ℤ[x]/Φ₁₄₀.
- χ₋₇ = +1 on {1, 2, 4} and −1 on {3, 5, 6}. Hence G = 2i · (sin(2π/7) + sin(4π/7) − sin(π/7)).
- The bracket is positive, because sin(4π/7) = sin(3π/7) > sin(π/7) (sine is increasing on [0, π/2]). Therefore G = +i√7.

The a-3 and b-1 conclusions **do not depend on fff902b4**.

**Confirmed Gauss sums and the odd first-moment (PP-ruled, exact):**

- G(χ₋₄) = 2i.
- G(χ₅) = √5 (G² = 5 exactly; the sign is G = 1 + 2φ with φ = 2cos(2π/5) > 0, since 2π/5 < π/2).
- G(χ₋₇) = i√7, by the proof above.
- G(χ₁₄₀) = +√140, from the product formula and the factor signs: χ₋₄(35) = −1, χ₋₃₅(4) = +1, χ₅(7) = −1, χ₋₇(5) = −1, whence G(χ₋₃₅) = i√35 and G(χ₁₄₀) = (−1)·(2i)·(i√35) = 2√35 = +√140.
- Σ_{m=1}^6 m χ₋₇(m) = 1 + 2 − 3 + 4 − 5 − 6 = −7.

**T-Dir** is discharged for χ₁₄₀ and χ₋₇ only, with root numbers +1. No general T-Dir claim is made.

## F4. Grades and tallies (PP-ruled)

- **a-3** (3rd bullet of 26a7c91e): COND [T-CNF] → **PROVED** (PP-ruled, using L1, L2, and the independent evaluation of G(χ₋₇)). The row goes from 2/1/0/0/0 to 3/0/0/0/0; LD-O3a goes from 6/3/0/0/0 to 7/2/0/0/0.
- **b-1:** retagged to **COND [T-spin]** only. T-Dir is discharged for the two Dirichlet factors, and those root numbers are now proved. The grade is unchanged (still COND), so there is no count change.
- **a-2:** unchanged. L(1, χ₁₄₀) = 4log(6+√35)/√140 stays **COND [T-CNF]** (the log-sine identification is the class number formula for ℚ(√35) and is not proved here). The Λ(s,π,std) row stays COND [T-spin].
- **T-theta1** (fff902b4) is not upgraded here and is **not pre-added**. The 65/15/5/9/2 figure in the 1016 findings and the 1017 rollup erratum is dropped until that file is audited.
- **t4436 (PP-ruled):** 96 rows: **64 PROVED / 16 CONDITIONAL / 5 OPEN / 9 REFUTED / 2 PENDING.** This is from the previously ruled 63/17/5/9/2, with a-3 accepted only.
- **Bridge C:** unchanged, **49 PROVED / 10 CONDITIONAL / 5 OPEN / 2 REFUTED / 1 PENDING + V₈₄ (67 rows).** The T-Dir / a-3 filing changes no Bridge C row.

Nothing is adopted. Local-derived. Erratum only.
