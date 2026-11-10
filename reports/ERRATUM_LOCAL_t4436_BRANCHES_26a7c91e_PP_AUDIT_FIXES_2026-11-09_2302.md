# ERRATUM (Local-derived) to FINDINGS_LOCAL_t4436_ALL_MENU_BRANCHES_2026-11-09_2224.md (sha 26a7c91e…): PP audit fixes, 2026-11-09 23:02 CST (America/Chicago)

- **Status:** additive erratum. 26a7c91e is not edited; it stays the record of what was filed. Where a row below differs from 26a7c91e, this erratum supersedes the wording (or proposes a grade for PP to rule); it changes nothing else.
- **Audit answered:** FINDINGS_PP_AUDIT_LOCAL_t4436_BRANCHES_26a7c91e_2026-11-09_2232.md (sha b6c246a85851c0603eaa5dc706093ff7ed310a0728a1962fd17f6a78cb0a55ea, sidecar checked). PP upheld every REF row and ruled **62 / 18 / 5 / 9 / 2** (96 rows), after regrading c-2 PROVED → COND [T-fam].
- **Authority and discipline:** Owner t4436, "Let the math lead the pursuits on all open paths". Every menu candidate stays a labelled branch. **Nothing is adopted.** A citation alone never makes a claim PROVED (OW 36683379). "Resonant algebra" is used throughout; RTA appears only as a historical alias.
- **Rules kept:**
  - Additive files only. Nothing was deleted, renamed, moved or overwritten. Failed launches stay on disk (s9 crashed; the s11 log is empty; see §E).
  - No CERT, no Gemini, nothing sent outside.
  - The t4407/t4429 dirs, the A5/A6/ob_v2/O-b fallback stream and its running ob_v3 job were not touched.
  - J-2 at 9800 was **not** started; the other stream will run it as s2e.
  - Tip sha: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (unchanged; checked by this generator at write time).

## F. Fixes, in PP's order

### O1 (Oc-3): the K statement holds for every squarefree t, with no Sturm bound

Replacement REF row (Local-derived):

> [REF] Hypothesis "R8's Ξ is a nonzero element of W₄ = K" (the Oc-1 identification) is REFUTED for every reading of R8 whose q-expansion lies in a single square class t·□, for **every squarefree t**, plus non-integral exponents.

Proof:
- K → (c(1), c(2), c(3), c(5)) is injective, with pivots n = 1, 2, 3, 5 (PP 2155 scratch pp_a5_a6_check.log).
- If t ∉ {1, 2, 3, 5}, none of 1, 2, 3, 5 lies in t·□. Then F ∈ K supported on t·□ has c(1) = c(2) = c(3) = c(5) = 0, so F = 0.
- For t ∈ {1, 2, 3, 5}, the exact s1c computation applies.
- Truncation can only add solutions, so non-membership needs no Sturm bound.
- The Ξ_odd row covers the non-integral part.

Scope is unchanged: single-square-class readings only, and Ξ_RTA stays OPEN. The s1c sweep over t ≤ 400 remains as corroboration. Grade: REF (unchanged).

### J1 (J-1): the REF holds for every nebentypus mod 980

Replacement REF row (Local-derived):

> [REF] Hypothesis "J-1 carries Ξ" is REFUTED for **any nebentypus ψ mod 980**, in S₂ and in M₂.

Proof (PP argument, restated):
1. Suppose f_Ξ ∈ M₂(Γ₀(980), ψ).
2. f_Ξ ∈ S₂(Γ₀(19600)) with trivial character (PP V7), and f_Ξ ≠ 0.
3. For each unit d mod 19600 there are a, b with ad − 19600b = 1. So [[a,b],[19600,d]] ∈ Γ₀(19600) ⊂ Γ₀(980) has lower-right entry d.
4. Units mod 19600 surject onto units mod 980.
5. Hence f_Ξ = f_Ξ|γ = ψ(d)f_Ξ for every unit d mod 980. So ψ ≡ 1.
6. That contradicts pp_2g_980 (trivial character: rank 145→146 in S₂, 192→193 in M₂; a mod-p rank rise is exact for non-membership).

The s7 χ₁₄₀ computation (dims 152/184; ranks 152→153, 184→185) is kept as optional corroboration only. Grade: REF (unchanged).

### H1 (H-3)

The row should read: "[REF] For **every finite d ≥ 1** there is no unitary ι: ℂ^d → ℂ^d⊗ℂ² (d ≠ 2d)." At d = 0 both spaces are 0 and ι exists trivially. Grade: REF (unchanged).

### C1 (c-3): Haar normalisation stated

**Setup.**
- L = H^{24} is the split unimodular ℤ₂₃-lattice of rank 48. 𝒢 = SO(L) is the smooth split reductive ℤ₂₃-group scheme, of relative dimension 48·47/2 = 1128.
- K₂₃ = 𝒢(ℤ₂₃).
- ω is a generator over ℤ₂₃ of the invariant top forms of 𝒢.

**Normalisation used.** The Haar measure is Weil's canonical measure |ω|₂₃. By smoothness and Hensel's lemma, the fibres of 𝒢(ℤ₂₃) → 𝒢(F₂₃) are cosets of measure 23^{−1128}, so

vol(K₂₃) = #SO₄₈⁺(F₂₃) · 23^{−1128} = (1 − 23^{−24}) · ∏_{i=1}^{23} (1 − 23^{−2i}),

with #SO⁺₄₈(F_q) = q^{552}(q^{24}−1)∏_{i=1}^{23}(q^{2i}−1). s11b checks this identity exactly and gives 1/vol = 1.0018975264…, which reproduces the carried 1.0019.

**Result.** The REF is unchanged: 1/vol(K₂₃) is a rational number in (1, 1.002), while the contour 2∏(23^i+1) is a 377-digit integer. Under the other common normalisation, vol(K₂₃) = 1, the comparison 1 ≠ contour is equally a REF. Grade: REF (unchanged).

### C2 (c-2): proof on linear algebra alone; T-fam discharged; **PROVED proposed, for PP to rule**

**Statement.** Let q be odd and n ≥ 1. Let (V, B) be the split nondegenerate symmetric bilinear space of dimension 2n over F_q, and X the set of n-dimensional totally singular subspaces ("Lagrangians").
- #X = N(n) = ∏_{i=0}^{n−1}(q^i+1) (c-1, PROVED).
- Claim: SO(V) has exactly two orbits on X, each of size ∏_{i=1}^{n−1}(q^i+1) = N(n)/2. They are swapped by any reflection.

**(a) Witt step: O(V) is transitive on X.**
- Let U ∈ X. Induct on n to build a basis e₁…e_n of U and f₁…f_n of V with B(e_i,e_j) = B(f_i,f_j) = 0 and B(e_i,f_j) = δ_ij.
  - Pick e₁ ∈ U∖0. By nondegeneracy there is x with B(e₁,x) = 1.
  - Put f₁ = x − ½B(x,x)·e₁. Then B(f₁,f₁) = B(x,x) − B(x,x)·B(e₁,x) − 0 = 0 and B(e₁,f₁) = 1. Here 2 is invertible because q is odd.
  - H₁ = ⟨e₁,f₁⟩ is a hyperbolic plane and V = H₁ ⊥ H₁^⊥.
  - U₁ := U ∩ f₁^⊥ has dimension n−1, since B(e₁,f₁) ≠ 0 gives U ⊄ f₁^⊥. Also U₁ ⊂ e₁^⊥, because U is totally singular. So U₁ ⊂ H₁^⊥, U = ⟨e₁⟩ ⊕ U₁, and U₁ is an (n−1)-dimensional totally singular subspace of the 2(n−1)-dimensional nondegenerate H₁^⊥.
  - Apply induction to U₁ ⊂ H₁^⊥. At n = 1, H₁ is the whole space.
- Given U, W ∈ X with such bases (e,f) and (e′,f′), the linear map e_i ↦ e′_i, f_i ↦ f′_i preserves B (same Gram matrix) and sends U to W.

**(b) The stabiliser of U lies in SO(V).**
- In the basis (e,f), B has Gram matrix [[0,I],[I,0]], and g ∈ Stab(U) has block form [[A,C],[0,D]].
- gᵀBg = [[0, AᵀD],[DᵀA, CᵀD+DᵀC]]. Setting this equal to B forces AᵀD = I.
- So det g = det A · det D = det(AᵀD) = 1.

**(c) Exactly two SO-orbits, of equal size, swapped by a reflection.**
- Let v = e₁ + f₁. Then B(v,v) = 2 ≠ 0, so r_v ∈ O(V) with det r_v = −1.
- Let H = Stab_O(U). By (b), H ⊂ SO.
- #(SO·U) = |SO|/|H| = (|O|/2)/|H| = #X/2, using (a) for |O|/|H| = #X.
- SO is normal in O, so r_v(SO·U) = SO·(r_vU) is an SO-orbit.
- It is disjoint from SO·U: if r_vU = sU with s ∈ SO, then s⁻¹r_v ∈ H ⊂ SO, which contradicts det = −1.
- So X = SO·U ⊔ SO·r_vU, each of size N(n)/2 = ∏_{i=1}^{n−1}(q^i+1).

**Remarks.**
- The parity lemma (same family ⇔ even codim of U∩W) is not needed for the count; it only identifies the two SO-orbits with the two parity families named in 26a7c91e. One direction is shown above: r_v changes dim(U∩gU) parity, since dim(U ∩ r_vU) = n−1 (PP's remark).
- The proof uses only linear algebra over F_q, with no citation.
- At (n,q) = (24,23) each orbit has ∏_{i=1}^{23}(23^i+1) members, and the Codex contour is exactly 2× this, i.e. #X (a-1/c-1).
- Corroboration (s11b, brute force): #X = 2, 8, 12, 80 and the orbit of U₀ under ⟨r_{v₀}r_w⟩ ⊂ SO has size 1, 4, 6, 40 at (n,q) = (1,3), (2,3), (2,5), (3,3), with r_{v₀}U₀ outside it in each case.

**Proposed row:**

> [PROVED, proposed; PP to rule] One SO-orbit on Lagrangians has ∏_{i=1}^{n−1}(q^i+1) members, for every odd q and n ≥ 1. The Codex contour is exactly 2× this (two orbits, swapped by r_v). Proof: (a)–(c) above. T-fam is discharged.

### O5 (O5-3)

Replacement REF wording (Local-derived):

> [REF] REF for every V having an isolated finite-multiplicity eigenvalue (k-dim eigenspace vs 2k); O5-3b falls under it subject to T-Weyl.

The "all sub-branches" claim for ι is therefore unconditional for every such V and for O5-3a, and conditional on T-Weyl for O5-3b. The O5-3b inversion row (PROVED) and the T-Weyl row (COND) are unchanged. Grades and counts: unchanged.

### A1 (α-3): computational base disclosed; cofactor certificates added

**Computational base, now disclosed:**
- PARI/GP 2.17.x (as before).
- **sympy**, exact over ℚ: `groebner` (lex, Buchberger), `Matrix.gauss_jordan_solve`, `solve` (used only in the 8 parametric "solved" jobs), and `expand`.
- **python-flint 0.9.0** `fmpq_mat` (exact rational rref), used only in the new certificate files.

**Cofactor certificates (new evidence, optional fix).** For a GB = [1] job with equations g_i, substituted α-product P and saturation variable z, each of the following identities is checked by exact `sympy.expand` and proves that the job has no full-support solution, without relying on Buchberger:
- 1 = Σ c_i g_i (equations only),
- 1 = Σ c_i g_i + c(zP − 1), or
- P^k = Σ c_i g_i.

Results:
- **s10:** degree bound D ≤ 4 for equations only, then D ≤ 3 with the saturation generator. It recounted **290** GB = [1] jobs (matching s4c and PP) and certified **96**.
- **s10b:** P^k, k ≤ 2, D ≤ 4 (D ≤ 3 when there are ≥ 6 τ's), run on the remaining 194. It certified **48** of them; 146 were not certified within the bounds; s10b status: second pass: 194 jobs; certified 48; still uncertified 146 [((3, 11, 47, 71, 79, 83), (1, -1, 1, 1)), ((3, 11, 47, 71, 7.
- **Total certified by expansion: 144 of 290.** The other **146** GB = [1] verdicts still rest on sympy's exact Buchberger (disclosed above).

Grade: α-3 stays **PROVED** as exact computer algebra (PP accepted). The certificates strengthen it and do not change it.

### α-3 and α-4 notes

- **α-3:** the 8 parametric "solved" jobs have triangular saturated z-free Gröbner bases {4τ_i² − 1, 2τ_j ∓ 1}, each with exactly 2 complex solutions, both real and both listed. So s4c's only possible leak (sympy.solve plus the `is_real` filter) does not leak. The 32 empty parameter-free jobs (s4d) are unique linear solutions that fail the quadratics. **α-3: PROVED.**
- **α-4:** the identity coefficient of tt* at α ≡ 1 is **exactly 11**. A multiple λ·1 has tt* = 11λ²·[1] + (nonzero off-identity part), so it is never a scalar multiple of [1] and never a similitude. **REF** (unchanged).

### J3a (J-3 rank row): no GRH in the upper bound

Add to the algebraic-rank row:
- PARI's ellrank computes the 2-Selmer rank C, the 2-torsion rank T and s **unconditionally**, with r₂ = C − T − s ≥ rank (ellrank documentation, as quoted by PP 2232 §2).
- The PARI maintainers state that GRH is not used for curves with a rational 2-torsion point. Both 49a1 and Ξ have rational 2-torsion (torsion ℤ/2 for each, s7; [0,0,0,−42875,−4201750] for Ξ).
- So the upper bounds [0,0] and [1,1] are unconditional relative to PARI. The lower bound comes from the exact point P = (8730, 810550), with ellorder 0.

Grade: PROVED (unchanged).

### CNF (a-2, a-3): h(140) = 2 and ε = 6+√35, elementary (no quadclassunit, no GRH)

Let K = ℚ(√35), d_K = 140 (35 ≡ 3 mod 4), and O_K = ℤ[√35].

**1. Minkowski/Lagrange bound.** Every ideal class contains an integral ideal of norm ≤ √140/2 < 5.92, i.e. of norm in {1,…,5}.

**2. Small primes.**
- 2 ramifies (2 | 140): (2) = 𝔭₂².
- 3 is inert, since (35/3) = (2/3) = −1, so no ideal of norm 3. Norm 4 is 𝔭₂² = (2), which is principal.
- 5 ramifies: (5) = 𝔭₅².
- So every class is represented by one of 1, 𝔭₂, 𝔭₅, 𝔭₂𝔭₅ (norm 10 is above the bound but is used below).

**3. 𝔭₂ is not principal.** That would need x² − 35y² = ±2. Mod 5 this is x² ≡ ±2, and squares mod 5 are {0,1,4}.

**4. 𝔭₅ is not principal.** That would need x² − 35y² = ±5. Then 5 | x; writing x = 5u gives 5u² − 7y² = ±1. Mod 5 this is 3y² ≡ ±1, but 3y² mod 5 ∈ {0,3,2} and ±1 ≡ {1,4}.
- s9b's printout writes "−7y² = 2y²". The value set {0,2,3} printed there is the same set, and the argument stands.

**5. 𝔭₂𝔭₅ is principal.** N(5+√35) = 25 − 35 = −10, and the only ideal of norm 10 is 𝔭₂𝔭₅ (both primes ramified). So [𝔭₅] = [𝔭₂]⁻¹ = [𝔭₂], since 𝔭₂² = (2).

**6. Conclusion: h = 2,** with Cl = {1, [𝔭₂]}.
- Cross-check (s9b): the reduced forms of discriminant 140 fall into **4** cycles, so h⁺ = 4. The fundamental unit has norm +1 (step 7), so h = h⁺/2 = 2.

**7. Fundamental unit.**
- √35 = [5; 1, 10] (period 2). The convergent before the period end is 6/1, and 6² − 35·1² = 1.
- y = 1 is the least positive y, so ε = 6+√35 is the fundamental unit.
- No unit has norm −1: x² − 35y² = −1 reduces mod 7 to x² ≡ −1, and −1 is not a square mod 7. This also matches the even period length.

**8. Consequence.** L(1,χ₁₄₀) = 2h·log ε/√140 = 4·log(6+√35)/√140 is now **COND [T-CNF] only**, where T-CNF is the Dirichlet class number formula; the h and ε inputs are proved.
- Similarly, for L(1,χ₋₇) = π/√7: the only reduced form of discriminant −7 is (1,1,2), so h(−7) = 1 and w = 2. This is elementary, and the row is T-CNF only.
- Evidence: s9b, a pure-integer script. s9 crashed on a too-narrow ρ window and is kept on record.

Grades: unchanged (COND [T-CNF]); the conditions are reduced to T-CNF alone.

### D1 (rollup wording)

Replace "Branches REFUTED (dropped once PP-audited)" with "**Branches closed as REFUTED, kept on record**: V-3, c-3, α-4, H-3 (every finite d ≥ 1), O5-3 (ι, for every V with an isolated finite-multiplicity eigenvalue; O5-3b subject to T-Weyl; the inversion survives in O5-3b), J-1 as a Ξ-carrier (any nebentypus mod 980)". The REFUTED sub-hypothesis "R8 Ξ is a nonzero W₄ element" becomes "every squarefree t". Under t4436 every option remains a recorded branch.

## P. Pending items

- **Oc-2 at level 784 (s1e):** still running (PID 932685). Lines recorded so far:
  - level 784, char 1: dim S = 36; T(121) eigenspace for a_11(Xi) = -4: 0; for a_11(49a1) = +4: 8; 20s
  - level 784, char -4: dim 0
  - The remaining characters (D = 8, −8, −7, 28, −56, 56) stay **PENDING**. Their result and the final s1e log sidecar will be recorded in a follow-up additive file; 26a7c91e's at-filing sidecar for the log stays as filed.
- **J-2 at 9800:** PENDING. The other stream will run it as s2e after ob_v3 closes. Local did not start it.

## R. Tally

- **PP-ruled (in force):** 96 rows: **PROVED 62 · CONDITIONAL 18 · OPEN 5 · REFUTED 9 · PENDING 2.**
- **Proposed by this erratum, subject to PP ruling:** 96 rows: **PROVED 63 · CONDITIONAL 17 · OPEN 5 · REFUTED 9 · PENDING 2.** The only change is c-2, COND [T-fam] → PROVED, by the C2 proof.
- All other fixes are wording or scope changes, or added evidence, with no grade change:
  - O1, J1, H1, O5 and D1 widen or sharpen the REF statements.
  - C1 states the normalisation.
  - A1 discloses the base and adds certificates.
  - J3a cites the unconditional bound.
  - CNF reduces a-2/a-3 to T-CNF alone.
- Bridge C stays PARTIAL. The PP Bridge C rollup 46/11/5/2/1 + V₈₄ (PP 0f1d3361) is separate and unchanged. Nothing is adopted.

## E. New evidence (evidence_local_t4436_branches_2026-11-09/; each file gets a .sha256 sidecar)

| File | sha256 |
|---|---|
| s10_alpha_gb1_cofactor_certificates.log | 666fe33375cde70b31150fa0982e8eb65192f96c1ab85a568748628a7ce1e85e |
| s10_alpha_gb1_cofactor_certificates.py | d62cc1e2312943d29109e57345f85dcb1c05651dd623b2f7ebb338e536dbd76a |
| s10_alpha_gb1_cofactor_certificates.txt | d14b4099f87df1b853683b985b56fd5dbf064ecabbd232621f5dcbc29958c87d |
| s10b_alpha_gb1_prodpower_certificates.log | fb8f130bef674237bd16bdf05fd26cd4ba935d40f3c1370c0c6e442a1fd65fc7 |
| s10b_alpha_gb1_prodpower_certificates.py | 3ed65848c0c607c298c1308503a5c7119a850c9a046de96311b434d5c63a8b1b |
| s10b_alpha_gb1_prodpower_certificates.txt | d067e454163d27fee9c6df839abde429ba61c4267a82be0bd222cf75b81d94d7 |
| s11_c2_so_orbits_c3_haar.log | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| s11b_c2_so_orbits_c3_haar.log | 646dc812eece777081fb33f91040db1466c541ced6da9ea2113d773c1576319a |
| s11b_c2_so_orbits_c3_haar.py | 435363cade6d115356b48b68bb0ff270515aeddcded2f63b205d3d06caafeaa0 |
| s9_cnf_h140_unit_elementary.log | eada2918f0adfdca2c3e055c1ae29ea7d856f50cca640ac0677958110d47c1b0 |
| s9_cnf_h140_unit_elementary.py | 39f8e78bf06e376f648964b37e38030a711630e98362e76f647fac9c33a0d589 |
| s9b_cnf_h140_unit_elementary.log | 7de78ec6664884534d5d521848b03b7bcb68f28d91729c5dacb315b08999a74c |
| s9b_cnf_h140_unit_elementary.py | 5cad5861db5308577c16893eabf1631a7e754f4ca91aaf5831e86db613e22776 |
| gen_erratum_t4436.py | a115e5d315cb109f07e5dcf898e8191ef986fe93de58ad9a75503625b2ed77ea |

- **Failed launches, kept on record:**
  - s9_cnf_h140_unit_elementary.py crashed; its .log holds only the first line, and the traceback went to the terminal.
  - s11_c2_so_orbits_c3_haar.log is empty: the launch failed before the script existed, and no s11 .py was ever written.
- gen_erratum_t4436.py is this file's generator; it refuses to overwrite.
