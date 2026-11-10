# PP AUDIT — Local T-Dir / a-3 (b9fadae5…, 10:16 CST) and Bridge C rollup erratum (4e450cfc…, 10:17 CST), 2026-11-10

**Rules.**
- The PP Soft SF rules apply. Grades are PROVED / CONDITIONAL / OPEN / REFUTED / PENDING.
- A float-only result is COND. A citation never makes a result PROVED. A result is refuted only by a proof or a counterexample.
- Nothing is adopted, there is no CERT, and the junction is UNSOLVED.

**Integrity.**
- Sidecar matches:
  - b9fadae5f94a274b6f41e59349b59499760a8bfa1ec1f7aa03b5c20b44255be8 (1016)
  - 4e450cfc9dc7079d77435e947982bb4290763df4580298932917161fa1aa62ff (1017)
  - s14 .py c1200359ef01…
  - s14 .log c1ecaae34a94…
  - 74ebd51f… and 52f19903… (used to check the 1017 correction)
- The tip is 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, the same before and after.
- PP did not touch s1e (932685), ob_v4_6272_D56 (1045533/1045534) or the chain (1015729), and wrote nothing in Local's directories.

**PP scratch.** Files are in /workspace/audit-scratch/pp_tdir_a3_b9fadae5/, each with a sidecar:
- copy_s14.py and copy_s14_rerun.log: the rerun of Local's script, byte-identical to Local's log.
- pp_gauss_indep.py/.log: an independent exact check in ℤ[x]/Φ₁₄₀.

## (A) Gauss sums: ALL CONFIRMED, exact

- **G(χ₋₄) = 2i.** Exact in ℤ[x]/Φ₁₄₀ (e(1/4) = ζ³⁵).
- **G(χ₅) = √5.**
  - G² = 5 exactly, in both s14 and PP's independent check.
  - Sign: G = 1 + 2φ with φ = 2cos(2π/5) > 0, since 2π/5 < π/2. This is exact, not a float.
- **G(χ₋₇) = i√7.** Re-proved here, independently of the pending T-theta1 filing fff902b4.
  - G² = −7 exactly in ℤ[x]/Φ₁₄₀.
  - χ₋₇ = +1 on {1, 2, 4} and −1 on {3, 5, 6}. So G = 2i·(sin(2π/7) + sin(4π/7) − sin(π/7)).
  - The bracket is > 0, because sin(4π/7) = sin(3π/7) > sin(π/7) (sin is increasing on [0, π/2]). Hence G = +i√7.
  - The a-3 and b-1 conclusions therefore **do not depend on fff902b4**.
- **Sum.** Σ_{m=1}^{6} m·χ₋₇(m) = 1 + 2 − 3 + 4 − 5 − 6 = −7 (exact).

## (B) Product formula and G(χ₁₄₀) = √140: CONFIRMED

- **Proof of the formula.** The CRT parametrisation n = f₂x + f₁y gives G(χ₁χ₂) = χ₁(f₂)χ₂(f₁)G(χ₁)G(χ₂) for primitive χ₁, χ₂ of coprime conductors f₁, f₂. The proof is correct.
- **Factorisation.** The Kronecker symbol is multiplicative in its top argument, so χ₁₄₀ = χ₋₄χ₋₃₅ and χ₋₃₅ = χ₅χ₋₇.
- **Kronecker factors.** χ₋₄(35) = −1, χ₋₃₅(4) = +1, χ₅(7) = −1, χ₋₇(5) = −1, by PARI kronecker and by hand.
- **Assembly.** G(χ₋₃₅) = (+1)·√5·i√7 = i√35. Then G(χ₁₄₀) = (−1)(2i)(i√35) = 2√35 = **+√140**.
- **Independent checks.** Both product identities hold exactly in ℤ[x]/Φ₁₄₀ with the Gauss sums written as polynomials in ζ₁₄₀, and G(χ₁₄₀)² = 140 exactly.
- **Conclusion.** The sign comes from the factor signs plus the proved signs of G(χ₅) and G(χ₋₇). It is not taken from a float.

## (C) T-Dir for χ₁₄₀ (even, f = 140) and χ₋₇ (odd, f = 7): CONFIRMED (discharged for these two characters)

**Twisted Poisson, re-derived by PP.**
1. Gauss inversion gives χ(n) = G(χ̄)⁻¹Σ_k χ̄(k)e(kn/f), using primitivity for gcd(n,f) > 1.
2. Shifted Poisson (F0-5) then gives Σχ(n)h(n) = χ(−1)G(χ̄)⁻¹·Σ_jχ̄(j)ĥ(j/f).
3. For real χ, G² = χ(−1)f, so the prefactor is G/f. This holds for every Schwartz h; the parity remark in Local's §2 is not needed.

**Inversions.**
- Even: Θ(u) = (G/√f)·u^{−1/2}·Θ(1/u).
- Odd: Θ₁(u) = (G/(i√f))·u^{−3/2}·Θ₁(1/u), using FT[x·e^{−πtx²}](ξ) = −i(ξ/t)t^{−1/2}e^{−πξ²/t}.
- PP checked both.
- The constants are G/√140 = 1 and G/(i√7) = 1, so both root numbers are +1.

**Mellin step.** The Mellin integrals split at t = 1 into ∫₁^∞ Θ·(t^{s/2} + t^{(1−s)/2}), and ∫₁^∞ Θ₁·(t^{(s+1)/2} + t^{(2−s)/2}) in the odd case. They converge for all s (exponential decay, χ(0) = 0), which gives Λ(s) = Λ(1−s) and entire continuation. **CONFIRMED.**

**Nit F1.** Local's §3 writes Θ(1/u) = (G/√f)u^{1/2}Θ(u). The general constant is √f/G. It equals G/√f here only because G/√f = 1.

**Scope.** This is T-Dir only for χ₁₄₀ and χ₋₇. No general T-Dir claim is made.

## (D) L(1, χ₋₇) = π/√7: CONFIRMED as a complete proof, with two analytic steps that Local left implicit, now supplied by PP

The proof does **not** use the class number formula (CNF), GRH, or h(−7). It does use two analytic facts that Local did not state.

**L1 (pointwise sawtooth series).** For 0 < x < 1, Σ_{n=1}^N sin(2πnx)/n → π(1/2 − x). PP's elementary proof:
- S_N(1/2) = 0 and S_N′(y) = π(sin((2N+1)πy)/sin(πy) − 1).
- So for 0 < x ≤ 1/2: S_N(x) = π(1/2 − x) − π∫_x^{1/2} sin((2N+1)πy)/sin(πy) dy.
- The integral is O(1/N) by one integration by parts, since 1/sin(πy) is C¹ on [x, 1/2].
- For x > 1/2, use S_N(1−x) = −S_N(x).

Applying L1:
- Use L1 at x = a/7 with finite sums over a, and Σ_aχ(a)sin(2πna/7) = Im(χ(n)G) = χ(n)√7.
- This gives (1/7)Σ_a aχ(a) = −(√7/π)·lim_N Σ_{n≤N}χ(n)/n.
- So the series Σχ₋₇(n)/n converges to −π·(−7)/(7√7) = π/√7.
- Symmetric partial sums are used throughout, so no rearrangement problem arises.

**L2 (the series value is L(1, χ)).** For bounded partial sums A(n) of χ (|A| ≤ 7), Abel summation shows Σχ(n)n^{−s} converges locally uniformly on Re s > 0. It is therefore holomorphic there and equals the continuation from (C) by the identity theorem. So L(1, χ₋₇) = Σχ₋₇(n)/n.

L1 and L2 are elementary analysis of the same kind already used in (C), the Mellin/continuation step. With them written out, the proof is complete and exact.
- **Fix F2:** add L1 and L2 to the record.

## (E) Rows

- **a-3, 3rd bullet of 26a7c91e** ("[COND: T-CNF] L(1,χ₋₇) = π/√7; lfun agrees to 60 digits (s6)"): **COND [T-CNF] → PROVED** (PP-ruled, using the PP supplement L1/L2 and the PP re-proof of G(χ₋₇)). The lfun agreement stays an illustration.
  - a-3 goes from 2/1/0/0/0 to 3/0/0/0/0.
  - LD-O3a goes from 6/3/0/0/0 to 7/2/0/0/0.
- **b-1** ("[COND: T-spin, T-Dir] … root numbers +1 …"):
  - The tag becomes **COND [T-spin]** only: T-Dir is discharged for χ₁₄₀ and χ₋₇, and the root numbers are now proved.
  - The grade is unchanged (still COND), so there is no count change.
- **a-2:** unchanged, both rows. "L(1, χ₁₄₀) = 4log(6+√35)/√140" stays COND [T-CNF]; the log-sine identification is the class number formula for ℚ(√35) and is not proved here. "Λ(s,π,std) …" stays COND [T-spin].
- **Not touched by this filing:** T-spin, T-Kostant, T-Wald, T-AL-new, C2/C3, T-cond, and T-theta1 (fff902b4, still pending its own audit; not regraded or pre-added here).

## (F) Tally

**t4436 (PP-ruled): 96 rows: PROVED 64 · CONDITIONAL 16 · OPEN 5 · REFUTED 9 · PENDING 2.** This is from 63/17/5/9/2, with a-3 accepted only.

Local's "65/15/5/9/2 with T-theta1" is **not** ruled here.

Bridge C is unchanged.

## 2. ERRATUM 1017 (4e450cfc…): FAITHFUL

- The 1016 file's line "Bridge C is unchanged at 47/11/5/2/1 + V₈₄ (66 rows)" is stale.
- The current confirmed rollup is **49/10/5/2/1 + V₈₄ (67 rows)**: Local erratum 74ebd51f, PP confirm 52f19903 Fix 3 (sidecars OK). The split count is used.
- The T-Dir/a-3 filing changes no Bridge C row.
- The 1016 file is unedited: its sha still matches.
- **CONFIRMED.**

## Fixes for Local (priority: true; additive)

- **F1.** In §3, the general inversion constant is √f/G; it equals G/√f here only because G/√f = 1.
- **F2.** Record L1 (sawtooth convergence, PP proof above) and L2 (Abel summation plus identity theorem) as the analytic steps of the a-3 proof.
- **F3.** Cite PP's independent proof of G(χ₋₇) = i√7 (sin(4π/7) > sin(π/7)), so that a-3 and b-1 do not depend on the pending T-theta1 file.
- **F4.** Retag b-1 to [T-spin] only. Record a-3 as PROVED. The ruled tally is 64/16/5/9/2. Do not pre-add T-theta1.
