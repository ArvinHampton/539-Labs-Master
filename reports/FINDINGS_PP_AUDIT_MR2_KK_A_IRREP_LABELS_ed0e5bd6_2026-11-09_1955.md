# FINDINGS — PP Soft SF audit of MR2 "KK Group A irrep labels of the low Bolza levels" (ed0e5bd6), under OW 8b26c786
Date: 2026-11-09, ~19:58 CST (America/Chicago). Auditor: Professor Proof (PP), executor run. Owner: Arvin.
Scope: OW 8b26c786 ("Group A" = Aut⁺(Bolza), order 48, × wall ℤ₂ as KK scope; a choice, not a result). Nothing adopted. Junction UNSOLVED. Labels: PROVED / COND / OPEN / REF / PENDING. Float-only numerics = COND; a citation alone never makes a result PROVED (OW 3f160803 as amended by 36683379).

## 0. Custody (re-hashed live; file = .sha256 sidecar)
| File | sha256 | sidecar |
|---|---|---|
| MR2_MN2_KK_A_IRREP_LABELS_BOLZA_LOW_LEVELS_AUT48_2026-11-09.md | ed0e5bd6976ec217613ce73c22116b3f04c393dc0331e2572393e78707bfc310 | MATCH |
| ….py (frozen, mode r--r--r--) | ff80054190db1d7ef0ce365cdf9784afe5f21e067f63f74d3e12c2501cd08ea7 | MATCH |
| ….log | 6383cd412278cf9976820b6019bded1cf702bedda993243b0939c7b18f8bde90 | MATCH |
| MR2_MN2_KK_TRUNCATION_BOLZA_AUT48_ISOM96_WALL_Z2_2026-11-09.py (reused) | 88949658116586c63dc4785fc31c222eed6d9ef44afbefbc6e40a4946b20b26c | MATCH |
| PP FINDINGS_PP_AUDIT_MR2_KK_TRUNCATION_BOLZA_48_96_WALL_Z2_2026-11-09_1858.md | 1fe6c5746510abc0f007de6e3281fba3b5145ddb9250965a07fefc73d705005c | MATCH |
| PP FINDINGS_PP_CONFIRM_MR2_ERRATUM_69a10b84_2026-11-09_1932.md | 985d404d4135eed68d28697c2d57b980b776d81f9f2380d71cedd01683b4a11d | MATCH |
Tip 7cddb188 untouched. No CERT. No Gemini. Nothing sent outside. No existing file edited.
PP scratch (box): /workspace/pp_audit_kk/ — rerun of a copy of the frozen .py (rerun.log), independent FEM (klein.py, klein.log), exact GL(2,3) group theory (gl23.py), Aut(Isom) enumeration (inline, built on MR2's exact multiplication table).

## 1. Checks
**(a) Group theory — exact (gl23.py: GL(2,3) as 2×2 matrices over F₃, integer arithmetic only).**
- |GL(2,3)| = 48. There are 8 classes, of sizes 12, 6, 6, 6, 8, 8, 1, 1, with orders 2, 8, 8, 4, 6, 3, 1, 2.
- 3-dim characters, computed from the action on P¹(F₃) ≅ 4 points (S₄ = PGL(2,3)):
  - χ_perm3 = fix − 1 takes the values (+1, −1, −1, −1, 0, 0, +3, +3).
  - χ_rot3 = χ_perm3·det takes the values (−1, +1, +1, −1, 0, 0, +3, +3).
  - Both have ⟨χ,χ⟩ = 1 and ⟨χ_perm3, χ_rot3⟩ = 0. det = −1 on both order-8 classes.
  - MR2's **3** (character +1 on order-8 elements; log chi_5) is χ_rot3, the cube-rotation rep. MR2's **3⊗sgn** is χ_perm3.
- **Aut(GL(2,3)), computed by exhaustive search over generator images (orders 2 and 8) with a full homomorphism check:**
  - |Aut| = 48, |Inn| = 24, **|Out| = 2**.
  - 24 of the 48 automorphisms swap the two order-8 classes.
  - **Every automorphism fixes χ_rot3 and χ_perm3.**
  - So "3 and 3⊗sgn are swapped by no automorphism" is **PROVED (exact)**. Reason: both characters are constant on the union of the order-8 classes; automorphisms preserve element order; and the two 3-dim irreps differ there (+1 vs −1).
  - MR2's stated reason ("det is the unique nontrivial 1-dim character, so the label is invariant") is **insufficient**. It only shows that σ maps the pair {3, 3⊗det} to itself compatibly with ⊗det. It does not show that σ fixes 3.
- **Aut(Isom), order 96. Enumerated all images of the Coxeter triple (involutions with product orders 8, 2, 3) with a full homomorphism check on MR2's exact multiplication table:**
  - |Aut(Isom)| = 192, |Z| = 2, |Inn| = 48, so **|Out(Isom)| = 4**.
  - Induced permutations of the 13 irreps: {id, (I11 I12), (I2 I4)(I7 I10), (I2 I4)(I7 I10)(I11 I12)}.
  - Automorphisms that preserve the holomorphic subgroup Aut⁺ (96 of 192) induce only {id, (I11 I12)}.
  - Consequences, both PROVED (exact):
    - (i) MR2's caveat 6 is correct: the I11/I12 labels depend on the triple, and the Aut⁺ labels do not.
    - (ii) **New caveat.** An automorphism that does *not* preserve Aut⁺ swaps I10 (Aut⁺: 3) with I7 (Aut⁺: 3⊗sgn). The headline label is therefore meaningful only because the triple was drawn from the *antiholomorphic* involutions, i.e. those with D J_c = −J_c D on H¹. MR2's script does this (inv_anti), so the headline stands. The file should state this dependence.
- MR2's 13-irrep table (1⁴ 2² 3⁴ 4³, Σd² = 96) and the I13 → 2′⊕2″ restriction (⟨χ,χ⟩₄₈ = 2) are reproduced by the rerun. The multiplication table is combinatorially exact, and the character values are within 3e-14 of algebraic integers.

**(b) FEM — rerun plus an independent FEM.**
- *Rerun:* a copy of the frozen .py, with sha ff800541… verified, gives a log identical to 6383cd41… except the runtime line (27.7 s vs 40.0 s).
- *Independent PP FEM (klein.py):* the (2,3,8) triangle in the **Klein model**, where it is an exact straight Euclidean triangle: A = 0, B = (tanh d_AB, 0), C = tanh d_AC·e^{iπ/8}, with cosh d_AB = cos(π/3)/sin(π/8) and cosh d_AC = cot(π/8)/√3.
  - Method: P2 Lagrange elements; the anisotropic metric is handled by 64-point quadrature (g⁻¹ = s(I − xxᵀ), √det g = s^{−3/2}, s = 1 − |x|²). The FEM area is 0.1308996938996 = π/24 exactly.
  - This shares no mesh, element or assembly code with MR2. Sector boundary conditions come from π(r_i) for π = the B3 mirror rep T (= I10) and its twists by 1-dim characters.
  - Edge assignment: r_AB ↔ mirror e₃ (edge on the real axis), r_AC ↔ e₂ − e₃ (ray at π/8), r_BC ↔ e₁ − e₂ (opposite A). These are the same mirrors as MR2's [C] lines; their product orders 4, 2, 3 in O(3) match angles π/8, π/2, π/3 modulo J.
  - Uniform refinements m = 8, 16, 32, 64. Observed convergence rate 15.1–15.8 (≈ 16 = h⁴, as expected for P2 eigenvalues). Richardson extrapolation with the observed rate:
| Sector (Isom; Aut⁺ content) | PP extrapolated eigenvalues | m = 64 raw | Strohmaier–Uski value (as listed in MR2 .py) |
|---|---|---|---|
| I10 = T (3) | **3.83888725875**, 18.65881962461 | 3.83888726272, 18.65882002533 | 3.8388872588422, 18.658819627260 |
| I9 = T⊗(−,−,−) (3) | 40.115892, 97.877713 | — | — |
| I8 = T⊗(−,+,+) (3⊗sgn) | 15.04891613096, 50.554168 | 15.04891638256 | 15.048916133267 |
| I7 = T⊗(+,−,−) (3⊗sgn) | 28.07960572816, 62.635667 | 28.07960637290 | (28.0796057…, the next level above 25.5) |
| I1 (trivial; NN) | 0, 23.07855847748, then 74.92672660, 116.60257854 (m = 64) | 23.07855899236 | 23.078558481382 |
| I2 (DD) | 222.371113, 394.577661 | 222.37134694 | — |
  - λ₁ agrees with SU to 9e-11. λ₁ lies in the T (= I10, Aut⁺ **3**) sector as a simple sector eigenvalue, so its multiplicity is 3 = dim × 1 copy. Neither 3⊗sgn sector (I7, I8) has an eigenvalue below 15.0489. So **λ₁ is 3, not 3⊗sgn**: COND (float FEM, two independent discretisations, and (U)).
  - Conforming FEM values are upper bounds, which is consistent with every raw value lying above the extrapolated value and above SU. Labelling λ₁ rigorously would also need a *lower* bound above 3.8389 on the I7/I8 sectors, which neither file has. That is why the label stays COND.
  - The SU values were not re-fetched from the paper. PP's independent FEM reproduces the listed SU values to ≤ 3e-9, which verifies those numbers numerically (COND).
  - Levels 5.3536 (I12), 8.2496 (I5), 14.7262 (I11) and 20.5199 (I13) were checked by the rerun only, not by the independent FEM.
  - Multiplicity bookkeeping: 3 + 4 + 2 + 4 + 3 + 3 + 4 + 1 = 24 nonzero eigenvalues below 25.5, with each level a single irrep of copy number 1. This is arithmetic-consistent. The Weyl leading term 25.5 is a heuristic count check, not a completeness proof.

**(c) Invariant eigenvalues.** The Aut⁺-invariant functions are exactly the I1 ⊕ I2 sectors: they are the only Isom irreps whose Aut⁺ restriction contains the trivial rep (log [C]; consistent with B2). PP's FEM gives:
- I1: 0, 23.0785585, 74.9267, 116.6026.
- I2: lowest 222.3711.

So the Aut⁺-invariant eigenvalues below 25.5 are {0, 23.0786}, and 23.0786 is the first nonzero invariant. This is consistent with PP 1fe6c574 (0, 23.0786, 74.927, 116.603, 222.371 …): COND (float, with large gaps of ≥ 51 but no rigorous enclosure).

**(d) 985d404d residuals.**
- Residual 1 (one premise convention, R1): **PARTIALLY applied.**
  - This file uses one premise (U), grades abstract group theory PROVED and Bolza-level conclusions COND, which is the R1 pattern.
  - It does **not** restate the tallies of b0c6e848, 00b1a96a or 69a10b84 under one convention, which is what residual 1 asked.
- Residual 2 ("+--" sign formatting in the [F4] log lines, k = 5, 6, 7): **NOT applied.**
  - No corrected [F4] log or erratum for 69a10b84 exists on disk after 19:32. The only later MR2 files are batch 2 and this one, and this log contains no "+--" because it has no F4 lines.
  - The defect is cosmetic; the values were already confirmed.

## 2. Grade table
| # | MR2 claim | MR2 | PP | PP note |
|---|---|---|---|---|
| 1 | λ₁ = 3.8389 eigenspace = Aut⁺ irrep 3 | COND (U) | **COND** | Confirmed by the independent Klein P2 FEM (λ₁ = 3.83888725875 in sector I10; 3⊗sgn sectors start at 15.0489). Float, no lower bound. The orientation dependence (B2) must be stated. |
| 2 | Irrep decomposition of all levels < 25.5; 23.0786 = trivial | COND (U) | **COND** | Independently confirmed for I1, I2, I7–I10. I5, I11–I13 by rerun only. |
| 3 | 3 vs 3⊗sgn labels intrinsic (automorphism-invariant) | PROVED | **PROVED (by PP's exact computation; MR2's argument insufficient)** | Out(GL(2,3)) = ℤ₂. The outer class swaps the two order-8 classes, and every automorphism still fixes both 3-dim characters. |
| 4 | Isom: 13 real irreps (1⁴ 2² 3⁴ 4³); I13 → 2′⊕2″ | PROVED | PROVED (computer-assisted) | Exact multiplication table; characters are algebraic integers to 3e-14; rerun identical. |
| 5 | SU multiplicities (3,4,2,4,3,3,4,1) agree with FEM | COND | COND | PP FEM agrees with the SU values to ≤ 3e-9 on the levels it computed. A citation does not upgrade the result. |
| 6 | I11/I12 labels triple-dependent; Aut⁺ labels not | PROVED (remark) | **PROVED (by PP's exact enumeration)** | MR2 gave no computation. PP: Aut⁺-preserving outer automorphisms induce exactly (I11 I12). |
| 7 | Levels > 25.5, rigorous FEM bounds, charged S⁴ towers | OPEN | OPEN | — |
| B1 (PP) | Out(GL(2,3)) = ℤ₂, \|Aut\| = 48 | — | PROVED (exact) | gl23.py |
| B2 (PP) | Out(Isom) = ℤ₂ × ℤ₂ (\|Aut\| = 192). Non-Aut⁺-preserving automorphisms swap I10 ↔ I7 (3 ↔ 3⊗sgn) and I2 ↔ I4 | — | PROVED (exact enumeration) | The headline needs the triple to be antiholomorphic. MR2's script ensures this. |
| B3 (PP) | Independent Klein-model P2 FEM spectrum per sector (table above) | — | COND (float) | h⁴ convergence, rate ≈ 15.5. |
| B4 (PP) | Aut⁺-invariant eigenvalues < 25.5 are {0, 23.0786}; next 74.927; I2 from 222.371 | — | COND (float) | Consistent with 1fe6c574. |
| B5 (PP) | Naming: the *permutation*-standard 3 of S₄ has χ(4-cycle) = −1 and is MR2's 3⊗sgn. MR2's 3 is the cube-rotation rep | — | PROVED (exact) | Calling 3 "the standard rotation rep" is ambiguous; label it by character. |

**Rollup.**
- MR2: PROVED 3 · COND 3 · OPEN 1 · REF 0.
- PP on MR2's claims: **PROVED 3 · COND 3 · OPEN 1 · REF 0** (same labels). Claims 3 and 6 are PROVED by PP's computation, not by MR2's text.
- PP-added rows: PROVED 3 (B1, B2, B5) · COND 2 (B3, B4).
- Headline: **λ₁ is the Aut⁺ irrep 3, not 3⊗sgn — CONDITIONAL** on (U) and float FEM, now confirmed by two independent discretisations.

## 3. Fixes for MR2 (numbered)
1. **Claim 3 proof:** replace "det is the unique nontrivial 1-dim character, so the label is invariant" with a valid argument. Automorphisms preserve element order; χ₃ ≡ +1 and χ₃⊗det ≡ −1 on *all* order-8 elements; GL(2,3) has exactly two 3-dim irreps. So every automorphism fixes both. Optionally cite PP's exact Out(GL(2,3)) = ℤ₂ check.
2. **Orientation dependence (new):** state that the Aut⁺ labels are intrinsic only after fixing the holomorphic subgroup. Automorphisms of Isom that exchange holomorphic and antiholomorphic cosets swap I10 ↔ I7, i.e. 3 ↔ 3⊗sgn. Record that the Coxeter triple was drawn from antiholomorphic involutions (D J_c = −J_c D), which is what makes the headline well defined.
3. **Claim 6:** add the computation (Aut(Isom) enumeration, |Out| = 4, Aut⁺-preserving part induces only (I11 I12)), or cite PP's. Grade it as a computed result, not a "remark".
4. **Naming:** drop "standard" in "standard rotation rep T1 of S₄". The permutation-standard rep has χ(4-cycle) = −1 (your 3⊗sgn). Keep the character-based definition (+1 on order-8 elements).
5. **Rigour note:** add explicitly that the FEM labels stay COND until a lower bound on the I7/I8 (3⊗sgn) sector eigenvalues above 3.8389 is available. Conforming FEM gives only upper bounds. A Lehmann–Goerisch or Temple-type enclosure would upgrade the headline.
6. **985d404d residual 1:** restate the b0c6e848 / 00b1a96a / 69a10b84 tallies under the single R1 convention in an additive file. Applying it in this file alone does not close the residual.
7. **985d404d residual 2:** issue the cosmetic [F4] sign-format correction ("+--" → "−" for k = 5, 6, 7) in an additive erratum. It is still outstanding.
8. **Weyl check wording:** call the 24-vs-25.5 Weyl comparison a heuristic count check, not evidence of completeness. Completeness below 25.5 rests on each sector's FEM having computed past 25.5, which it did.

Status unchanged: Group A is the Owner's scope choice (8b26c786), not a result; Group B not adopted; full spectrum OPEN; junction UNSOLVED. Tip 7cddb188 untouched. No CERT. No Gemini. Nothing sent outside.
