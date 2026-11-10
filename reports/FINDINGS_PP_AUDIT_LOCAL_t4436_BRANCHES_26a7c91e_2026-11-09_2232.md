# PP AUDIT — Local t4436 ALL MENU BRANCHES (26a7c91e…, filed 22:24 CST)

- **Auditor:** Professor Proof (PP). Same PP rules: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING; float-only = COND; a citation never makes PROVED (OW 3f160803 as amended by 36683379, strict); refute only by proof or counterexample. Labels below are PP's.
- **Audited file:** reports/FINDINGS_LOCAL_t4436_ALL_MENU_BRANCHES_2026-11-09_2224.md: sha256 26a7c91e… matches its sidecar; 282 lines.
- **Evidence:** evidence_local_t4436_branches_2026-11-09/ has 70 entries.
  - Every sidecar verifies, including __pycache__/s4c…pyc.
  - The only file without a sidecar is s1e_oc2_small_levels_p11.log. It is still running (PID 932685; at 22:30 CST it had reached level 784, char −4), so it is not final.
  - PP wrote nothing in this directory and did not touch the running s1e, ob_v3 or chain jobs.
- **PP scratch:** /workspace/audit-scratch/pp_t4436_26a7c91e/. Every file has a sidecar.
  - copy_s4c.py: a verbatim copy of Local's s4c, imported from the PP scratch with bytecode writing disabled.
  - pp_alpha3_spot.py / .log
  - pp_alpha3_param_solved.py / .log
  - pp_j3_rank.py / .log (PARI 2.17.2 via cypari2)
- **Tip:** 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, unchanged before and after this audit.
- **Separation:** this rollup is separate from the PP Bridge C rollup (46/11/5/2/1 + V₈₄, PP 0f1d3361), which this file does not change.

## 1. REF rows (audited hardest)

### Oc-3: hypothesis "R8 Ξ is a nonzero element of W₄ = K"

**PP: REFUTED (valid), and stronger than Local claims.**

- **Truncation needs no Sturm bound.** Non-membership by truncation is exact: if the coefficient vectors of K's basis, truncated at n ≤ 1200, admit no nonzero combination supported on t·□, then no nonzero F ∈ K has that support. Truncation can only add solutions, never remove them. So the question "does t ≤ 400 reach the Sturm bound?" does not arise for this direction. (Sturm, 42 at level 196, is needed only for membership claims.)
- **The bound t ≤ 400 is unnecessary.** K → (c(1), c(2), c(3), c(5)) is injective: pivots n = 1, 2, 3, 5 (PP 2155 scratch pp_a5_a6_check.log). If t is squarefree and t ∉ {1, 2, 3, 5}, then 1, 2, 3, 5 ∉ t·□, so c(1) = c(2) = c(3) = c(5) = 0 and F = 0. Together with s1c for t ∈ {1, 2, 3, 5}, the K statement holds for **every** squarefree t. This is PROVED and needs no computation beyond the pivots.
  - Fix O1: drop "t ≤ 400" from the K part of the REF row.
- **Ξ_odd row: PROVED.** Exponents (k+½)² lie in ¼+ℤ. After q ↦ q^t with t squarefree (so 4 ∤ t), they lie in t/4 + tℤ, which is never integral. Membership in K forces 1-periodicity, so Ξ_odd = Ξ − Ξ_even is 1-periodic, and Fourier uniqueness then gives Ξ_odd = 0.
- **Literal reading ≡ 0: PROVED** (k ↦ −k).
- **χ₋₇ identity: PROVED.** The shift by 7m does not change a sum over ℤ, and χ₋₇ is odd, so the terms for k and −k agree.
- **u ∈ S: CONDITIONAL [T-theta1], tag correct.** The truncated consistency for n ≤ 600 is not a membership proof. u ∉ K is exact.
- **Scope.** The REF is scoped correctly to single-square-class readings. Readings that mix several square classes are not covered. Ξ_RTA itself stays OPEN (undefined coefficients).

### J-1: hypothesis "J-1 carries Ξ" at level 980

**PP: REFUTED (valid), for every character, not only 1 and χ₁₄₀.**

- **No Sturm bound is needed.** A mod-p rank rise of an integer coefficient matrix implies a rise over ℚ, so non-membership is exact. The Sturm bound (weight 2, level 980: 2·[SL₂:Γ₀(980)]/12 = 336) matters only for "in" claims.
- **All characters (PP proof).** Suppose f_Ξ ∈ M₂(Γ₀(980), ψ) for some ψ mod 980.
  - f_Ξ ∈ S₂(Γ₀(19600)) with trivial character (PP V7).
  - Γ₀(19600) ⊂ Γ₀(980), and the lower-right entries d of Γ₀(19600) run over all units mod 19600. These reduce onto all units mod 980.
  - Hence ψ(d) = 1 for every d, so ψ is trivial. That contradicts pp_2g_980 (rank 145→146 in S₂ and 192→193 in M₂).
- So the χ₁₄₀ computation (s7: dims 152/184; rank_p 152→153 and 184→185) is correct but redundant.
- Fix J1: replace "trivial or χ₁₄₀ nebentypus" with "any nebentypus mod 980 (PP argument)".

### H-3: no unitary ι: ℂ^d → ℂ^d ⊗ ℂ²

**PP: REFUTED (valid) for every finite d ≥ 1.**

- At d = 0 both spaces are 0, so ι exists trivially.
  - Fix H1: write "every finite d ≥ 1".
- **Odd-d sub-REF: valid.** Suppose ((A⊗σ_x)K)² = (AĀ ⊗ 1) = −1. Then AĀ = −1_d, so det(AĀ) = |det A|² ≥ 0, while det(−1_d) = −1 for odd d. Contradiction.
- **Even-d PROVED row: valid** (the example squares to −1).

### α-4: α ≡ 1

**PP: REFUTED (valid).**

- PP recomputed tt* exactly (pp_alpha3_spot.log): the identity coefficient is 11 and nonidentity terms are present.
- "Not a similitude": the multiple λ·1 has tt* = 11λ²·1 + (nonzero off-identity part), so tt* is never a scalar multiple of [1]. This is exact and does not even need α-3's completeness.

### c-3: vol(K₂₃)⁻¹ ≈ 1.0019 ≠ contour

**PP: REFUTED (valid).** This is a trivial exact rational comparison against a 377-digit integer.

- Fix C1: state the Haar normalisation used for vol(K₂₃).

### V-3

**PP: REFUTED** (PP 320c8c7e; carried).

### O5-3: no ι, two rows

**PP: REFUTED (valid).**

- **First row.** A unitary ι with ιH = (H⊗1₂)ι maps the λ-eigenspace of H (dimension k) isomorphically onto that of H⊗1₂ (dimension 2k). For finite k ≥ 1 that is impossible.
- **Second row (O5-3a).** A(H_D+V)A⁻¹ = −H_D + V ≠ −(H_D + V) for scalar V ≠ 0.
- **O5-3b, T-Weyl row:** CONDITIONAL, correct. The branch exists only once an isolated eigenvalue exists. Note that this conditional existence is what makes the first REF row bite for O5-3b. Without a bound state, the "all sub-branches" REF for ι is itself conditional for O5-3b.
  - Fix O5: state "REF for every V having an isolated finite-multiplicity eigenvalue; O5-3b falls under it subject to T-Weyl".

## 2. Other rows checked

### α-3: complete classification, 70 solutions

**PP: PROVED (accepted) as exact computer algebra.** The logic is sound.

PP checks (pp_alpha3_spot, pp_alpha3_param_solved):

- **(a) Sieve is sound and recounts to 38.**
  - For g ≠ 1, the coefficient of [g] in tt* is a sum of monomials α_aα_b with ab⁻¹ = g.
  - If exactly one unordered monomial appears, its coefficient is 1 or 2 (2 when g² = 1). That forces a zero entry, contradicting full support on T.
  - The 2047 − 11 supports with |T| ≥ 2 reduce to 38 (sizes 4:6, 5:6, 6:10, 7:4, 8:8, 9:3, 10:1).
- **(b) The 16-sign split is complete.**
  - For real χ, χ(t*) = χ(t), so χ(t)² = χ(tt*) = 1, giving χ(t) = ±1.
  - Every solution has some sign vector, so the split loses nothing.
  - Using only 4 of the real characters adds necessary conditions only, so completeness is unaffected.
- **(c) The 608 jobs recount the same way by linear structure.**
  - 100 are linear-inconsistent, matching Local.
  - 146 are forced-zero. The product of the substituted α's is the zero polynomial, so some α_k ≡ 0. This is sound, because ℚ[τ] is a domain.
  - 64 have no free parameter.
  - 298 are parametric.
  - Local's 72 "solved" = 64 parameter-free + 8 parametric. Local's 290 "GB=[1]" = the other 290 parametric jobs.
  - A random sample of 12 parametric jobs re-run with Local's code gives 11 GB=[1] and 1 solved, consistent.
- **(d) Where completeness could leak, it does not.**
  - s4c's only possible leaks are sympy.solve and its `is_real` filter. These are used only in the 8 parametric "solved" jobs.
  - PP printed their saturated z-free Gröbner bases. Each is triangular, {4τ_i² − 1, 2τ_j ∓ 1}, with exactly 2 complex solutions, both real and both listed. They are complete by inspection.
  - The 32 empty parameter-free jobs (s4d) are unique linear solutions that fail the quadratic equations: exact.
- **(e) The 48 + 22 solutions are verified exactly** (tt* = [1]). The b = 111 lemma was checked by hand: tt* = ¼[(2+a+a⁻¹) + (2−a−a⁻¹)] + ¼b·0 = 1.
- **Residual trust:** the 290 GB=[1] verdicts rest on sympy's exact Buchberger implementation.
  - Fix A1: add sympy (exact groebner, gauss_jordan_solve) to the disclosed computational base next to PARI. Optionally emit cofactor certificates 1 = Σ c_i g_i for the 290 jobs, which can be checked by expansion.

### J-3: rank 1 = analytic rank 1

PP was skeptical here as asked.

**(i) Algebraic rank: PROVED within the PARI computational base.**

- PP re-ran PARI 2.17.2 (pp_j3_rank.log):
  - 49a1: conductor 49, torsion [2], ellrank [0,0].
  - Ξ: conductor 19600, torsion [2], ellrank [1,1], minimal model [0,0,0,−42875,−4201750].
  - Both 2-isogenous curves give the same bounds ([0,0] and [1,1]).
- PARI's ellrank documentation states that the 2-Selmer rank C, the 2-torsion rank T and s are computed **unconditionally**, with r₂ = C − T − s ≥ rank. The PARI maintainers also state that GRH is not used for curves with a rational 2-torsion point, which is the case for both curves.
- The upper bound needs no GRH and no BSD, and is unconditional relative to PARI.
- The explicit point is exact: P = (8730, 810550) is on the curve and ellorder = 0, so it has infinite order. ĥ ≈ 6.782 is illustration only.
- E(K) ⊗ ℚ ≅ E(ℚ) ⊗ ℚ ⊕ Ξ(ℚ) ⊗ ℚ is elementary (± eigenspaces of σ). Q(√140) = Q(√35).
- Fix J3a: cite the ellrank documentation sentence and the 2-torsion fact in the row, so it is clear the upper bound is not GRH-conditional.

**(ii) Analytic rank 1: PROVED** (PP 5bf1e1dc E11b).

- L(E,1) ≠ 0 and L′(Ξ,1) ≠ 0 are certified by arb balls, and ε(Ξ) = −1.
- L(J,s) = L(E,s)L(Ξ,s): the isogeny of row 106 gives V_ℓ(J) ≅ V_ℓ(E) ⊕ V_ℓ(Ξ). Local factors come from inertia invariants of V_ℓ, so this is elementary.

**(iii) "Rank = analytic rank, no GZK": PROVED.** It is two separately proved numbers.

**(iv) T-cond downgrade: correct under the strict rule.** At p = 2, Ξ is wildly ramified. Isogeny invariance of the Swan part is not covered by the elementary V_ℓ argument, so the conductor row correctly stays COND while the L-function row is PROVED. The split is consistent.

### Other branches

- **V-2: PROVED (valid).**
  - θ₁ = θ_{L₁} ∈ M₁(Γ₀(7), χ₋₇) (PP 0f1d3361 §4), so θ₁² ∈ M₂(Γ₀(7)) and θ₁(7τ)² ∈ M₂(Γ₀(49)).
  - PP re-derived the Fricke computation: g₊(−1/(49τ)) = 49τ²g₊(τ), so g₊|W₄₉ = +g₊.
  - The q-expansion −6 + 4q + … shows g₊ ≠ 0.
  - The 2205 certificate is used correctly (as membership of θ₁ only).
- **Oc-1: valid.** W₄ = K by rank: PROVED. T-Wald, C2/C3: correct COND tags. TT-1 carried from PP 0f1d3361.
- **Oc-2: PROVED rows valid.**
  - The restriction to quadratic characters is justified.
  - The Hasse row is valid: |a_p| ≤ 2√p < p+1.
  - The 784 row: **PENDING (correct).** s1e is not final.
- **J-2:**
  - The 2800/3920 non-membership is valid (mod-p rank rise is exact for "out"; the 49a1 control behaves correctly).
  - **9800: PENDING (correct).**
- **H-2 real-structure row: PROVED (valid).**
  - C² = 1 gives UŪ = 1, so U = Uᵀ; Takagi gives U = QQᵀ, so C = QKQ⁻¹.
  - In odd dimension C² = −1 is impossible, because det(UŪ) = |det U|² ≥ 0.
- **a-2/a-3: T-CNF tag correct.**
  - Note: PARI quadclassunit is GRH-conditional. h(140) = 2 and ε = 6 + √35 (√35 = [5; 1, 10]) are elementary by reduction theory and continued fractions.
  - Fix CNF: record this so T-CNF is the only remaining condition.
- **b-1: T-Dir correct.** The Gauss sum values √140 and i√7 are Gauss's theorem, so the tag is right. The 76 digits are float illustration only.
- **b-2 exponents: PROVED (valid).** {1, 3, …, 45} ∪ {23}; Σ(2e+1) = 1081 + 47 = 1128.
  - **Kostant downgrade to COND [T-Kostant]: correct.**
- **c-1: PROVED (valid).** The recursion N(n) = (q^{n−1}+1)N(n−1) with N(0) = 1 is proved.
- **c-2: REGRADED by PP from PROVED to CONDITIONAL [T-fam].**
  - "One SO-orbit has ∏_{i=1}^{n−1}(q^i+1) members" is supported only by brute force at small (n,q). Brute force cannot reach (24, 23).
  - The general claim needs two things:
    - the parity lemma (same family ⇔ even codim of U∩W, and this is an equivalence relation);
    - Witt transitivity of SO on a family.
  - With the parity lemma, equal family sizes follow. For anisotropic v, the reflection r_v satisfies dim(U ∩ r_vU) = n − 1. If r_vU = U then U ⊂ v^⊥, which is impossible by dimension. So r_v swaps the families, giving each N(n)/2.
  - Fix C2: either prove the parity lemma and Witt step on F0, or tag T-fam/T-Witt.
  - This is not a refutation; the count is almost certainly right.

## 3. Tags and t4436 discipline

- **New tags.** T-Wald, T-theta1, T-spin, T-CNF, T-Dir, T-Kostant, T-Weyl, F-V42, tip §1u and REC are named and scoped correctly. T-cond and T-Kostant are correct strict-rule downgrades.
- **Suggested PP addition:** T-fam (c-2).
- **Dischargeable soon:**
  - T-theta1, by the PP 2205 method.
  - T-cond at odd primes, via V_ℓ.
- **Tag-count line:** consistent with the rows (17 COND occurrences).
- **Discipline, mostly OK.**
  - Every menu option is a branch (28 in the table, 9 items).
  - Conflicts (a-1/a-2/a-3; b-1 sensitivity vs b-2 insensitivity; c-1 vs c-2's factor 2) stay separate.
  - Nothing is adopted.
  - Bridge C stays PARTIAL.
  - Fix D1: "Branches REFUTED (dropped once PP-audited)" should read "closed as REFUTED and kept on record". Under t4436 every option remains a recorded branch.

## 4. Tally

- **Local:** 96 rows, 63 / 17 / 5 / 9 / 2. PP recounted 63 / 17 / 5 / 9 / 2 = 96 from the row tags, and the per-item splits match.
- **PP-ruled tally** (one regrade: c-2 PROVED → COND): **96 rows: PROVED 62 · CONDITIONAL 18 · OPEN 5 · REFUTED 9 · PENDING 2.**
  - O-c 12/5/2/1/1
  - V₈₄ 6/2/0/1/0
  - J 16/3/2/1/1
  - H₊U 5/0/1/2/0
  - LD-O3a 6/3/0/0/0
  - LD-O3b 4/3/0/0/0
  - LD-O3c **2/1**/0/1/0
  - α 6/0/0/1/0
  - O5 5/1/0/2/0
- **Refutations of Local: none.** Every REF row is upheld.
- **Strengthened, as PP proofs:** Oc-3 now covers all squarefree t; J-1 now covers all characters.

## 5. Fixes for Local (priority: true)

- **O1:** Oc-3 REF covers all squarefree t (pivot argument). Drop "≤ 400" in the K statement.
- **J1:** J-1 REF covers every nebentypus mod 980 (PP argument). The χ₁₄₀ computation is optional corroboration.
- **H1:** H-3 should read "every finite d ≥ 1".
- **C1:** c-3: state the Haar normalisation.
- **C2:** c-2 is PROVED → COND [T-fam] unless the parity lemma and Witt step are proved.
- **O5:** O5-3 "all sub-branches" for O5-3b is subject to T-Weyl. Say so.
- **A1:** α-3: disclose sympy (exact) in the computational base. Optionally add cofactor certificates for the 290 GB=[1] jobs.
- **J3a:** J-3 rank row: cite that ellrank's r₂ is unconditional (2-Selmer; both curves have rational 2-torsion, so no GRH).
- **CNF:** a-2: h(140) = 2 and ε = 6 + √35 by reduction theory and continued fractions. Do not rely on GRH-conditional quadclassunit.
- **D1:** say "closed as REFUTED, kept on record" instead of "dropped".
- **Pending:** finish s1e at 784 (6 characters) and the J-2 9800 test when memory allows. Do not disturb ob_v3.
