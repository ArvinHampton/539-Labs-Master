# FINDINGS — PP audit of MR2 SU(2)_R lift and edge cases (b0c6e848) and MR2 erratum per PP fc93b8c0 (00b1a96a)

Auditor: Professor Proof (PP). Date: 2026-11-09 (America/Chicago). This file is additive. I sent no messages and filed no CERT, no adoption and no Gemini.
Rules: refute only by proof or counterexample. Under the citation scope (OW 36683379), a citation alone is never PROVED.
Tip check: `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, checked before and after. Unchanged.

## 0. Inputs (every sha256 equals its sidecar; all re-hashed this turn)
| file | sha256 | mtime (CST) |
|---|---|---|
| MR2_MN2_KK_A_SU2R_FLAT_CONNECTIONS_LIFT_AND_EDGE_CASES_AUT48_2026-11-09.md | b0c6e848c1ae557b… | 19:19:23 |
| …same .py | 02b945002aff3728… | 19:18:14 (before log ✓ frozen) |
| …same .log | 2aadaee3a59cb956… | 19:18:19 |
| MR2_ERRATUM_PINPLUS_KK_SU2R_PER_PP_fc93b8c0_2026-11-09.md | 00b1a96ac964e24b… | 19:22:54 |
| …same .py | 69bab9a4988d9148… | 19:22:07 (before log ✓ frozen) |
| …same .log | c083b1dd11724c13… | 19:22:12 |
| cited: MR2_ERRATUM2_MN2_Z2_WALL_CURVATURE_PER_PP_aeb9ab13_2026-11-09.md | 5511845e… | (sidecar match) |

**Reruns** (scratch dir `/workspace/audit-scratch/pp_1925_audit/`, every file with a sidecar):
- `err_rerun.log` c083b1dd is byte-identical to MR2's log.
- `lift_rerun.log` 4ce0d4f8 is identical to MR2's log except the runtime line.
- The embedded sha guards (88949658, 2f0e1220) both MATCH.

**Independent PP code:**
- `pp_1925_rs.py` 63f4e122 / `pp_1925_rs.log` 91857ca8. It is my own Reidemeister–Schreier over GL(2,3): BFS transversal, my own rewriting, GF(2) solver, Q₈ quaternion arithmetic and 2O. It repeats the whole check for **all 48** generating (2,3,8)-pairs in GL(2,3), so the result does not depend on MR2's choice of (x_A, y_A).
- I also reused my 1852 FEM (`pp_1852_audit/pp_fem238.log`, all four 1-dim Isom characters).

## Part L — b0c6e848 (SU(2)_R lift and edge cases)

**L1. Shas, sidecars and frozen order. PROVED.**

**L2. Rerun. PROVED.**

**L3. Construction. PROVED (independent).**
- Schreier rank 49 = 1 + 48·(2−1).
- H₁(Σ;ℤ₂) has dim 4 (= 2g).
- There are 0 nonzero Aut⁺-invariant characters.
- Identical for all 48 generating pairs. All x have det −1.

**L4. (a) The k=3 point lifts to SU(2) with the same class as the Fuchsian lift. PROVED. A third proof, structural:**
- Take any representation in which x, y and z = (xy)⁻¹ have exact orders 2, 3 and 8, in SO(3) or PSL(2,ℝ).
- Then every lift has x̃² = −1, and z̃⁸ = −1 because a rotation by 2πk/8 with k odd lifts to an element of order 16.
- The sign of ỹ³ can be chosen by the sign of the lift.
- So the relator vector b on the Schreier generators is **forced by the orders alone**: (a,c,d) = (1,1,1), or (1,0,1) after normalization. The k=3 system is therefore literally the Fuchsian (spin-structure) system, and it is solvable because spin structures exist.
- My code solves it for both normalizations.

**L5. (b) None of the 16 lifts is Aut⁺-invariant. PROVED (independent).**
- PP count: 0 fixed lifts, for both normalizations and all 48 pairs.
- PP **orbit sizes are 4 + 6 + 6**. This matches the theta-characteristic orbits from the independent Weierstrass-point machinery (88949658 [W]: odd 6; even 4 + 6).
- Caveat on MR2's "[FC] control": it is **not an independent control**. It uses the same b vector, so it returns the same count by construction (MR2's own line "[FC] … same relator vector b: True").
- The independent control is the orbit-structure match, which PP supplies here.

**L6. Affine versus linear (the parent's subtlety). PROVED.**
- The linear part has no nonzero fixed vector (L3). That alone does **not** decide whether the affine action has a fixed point.
- PP tested both directly:
  - The linear torsor (b = 0, i.e. the trivial connection, or the MN pair s + s_R) has exactly **1** fixed point, namely 0.
  - The affine torsor (b = b_F) has **0** fixed points.
- So the obstruction is a nonzero class in H¹(Aut⁺; H¹(Σ;ℤ₂)), not a consequence of having no invariant characters.
- "Twisting by a ℤ₂ character" is already included, because the 16 lifts *are* all the character twists.

**L7. Meaning of "invariant up to gauge". PROVED.**
- MR2 tests whether the isomorphism class is invariant: ρ∘g_* ~ ρ under SU(2) conjugation. That is the **weakest** sensible notion, so nonexistence under it implies nonexistence of any Aut⁺-equivariant structure.
- The center ±1 acts trivially by conjugation. In the dense case the gauge is forced to be ±(lift of φ(δ)).
- Out(SU(2)) = 1, so allowing an "automorphism of SU(2)_R" adds nothing.
- Conjugation by O(3) equals conjugation by SO(3), since −I is central, so an O(3)-type R-identification adds nothing either.
- Checking only the generators x, y is enough, because they generate Δ⁺ and π₁ acts trivially on classes.

**L8. (c) Dihedral case (unique axis): no invariant point. Agree. PROVED.**
- χ (composition with O(2)/SO(2)) is nonzero for a non-abelian O(2)-image that is not inside SO(2).
- Any gauge preserves the unique axis, so χ∘g = χ. That would put χ in H¹(Σ;ℤ₂)^{Aut⁺} = 0, a contradiction.

**L9. (d) V₄ point. PROVED (independent), with a gap in MR2's w₂ justification.**
- PP finds:
  - Aut⁺ orbits on nonzero characters are 3 + 12.
  - The 3-orbit together with 0 is a subspace W.
  - The Klein point is SO(3)-invariant.
  - A Q₈ lift exists.
  - **0 of 16** Q₈ lifts are invariant, with all 48 h ∈ 2O tested.
- **Gap:** MR2 writes "w₂ = ⟨χ₁∪χ₂,[Σ]⟩ = 0 because squares vanish". The vanishing of squares only reduces w₂ = α² + β² + αβ to αβ. It does not show that αβ = 0.
- **Correct reason (PP proof):** cup product on H¹(Σ;ℤ₂) is the nondegenerate intersection form, and it is Aut⁺-invariant. So W^⊥ is also an invariant 2-plane. By uniqueness W^⊥ = W, i.e. W is Lagrangian, and αβ = 0.
- Sensitivity check: over all 105 pairs of distinct nonzero characters, 45 are Q₈-liftable and 60 are obstructed. That is exactly the count for a nondegenerate symplectic form on 𝔽₂⁴ (15·6/2 = 45), so the test is sensitive.

**L10. §4 completeness. PROVED, with a wording fix.**
- My case split for SU(2)-irreducible ρ:
  - Ad ρ irreducible. Then it has trivial centralizer, since an odd-dimensional real irrep has commutant ℝ. These are classified by Hom(Δ⁺, SO(3)).
  - Ad ρ reducible. Then Ad ρ ⊂ O(2)_ℓ. If it is not in SO(2), either the axis is unique (dihedral), or Ad ρ preserves ≥ 2 lines and so lies in V₄ (Klein).
- MR2 §4(c) says "Ad ρ ⊂ O(2) is not abelian". That excludes V₄, which is abelian, while its next bullet treats V₄. Replace it with "Ad ρ reducible and not contained in SO(2)".

**L11. (e) The invariant SU(2)_R locus is {trivial}. CONDITIONAL, on the single premise Δ⁺/π₁Σ = Aut⁺ (Bolza uniformization, PP S9).**
- Everything else is PROVED: L3–L10 and fixes F5–F7 below.
- The k=3 root premise is removable (see F8).

**L12. λ₁ = 3.8388872588 is a 3-dim Aut⁺ irrep. CONDITIONAL on the Strohmaier–Uski multiplicity 3 (arXiv:1110.2150 v4), which is a citation.**
- The irreducibility step is PROVED.
  - The Aut⁺-trivial isotypic part is NN ⊕ DD.
  - The Aut⁺-sgn isotypic part is DN ⊕ ND. The reason: sgn is fixed by K-conjugation, so it extends to the two Isom characters, and no 2-dim Isom irrep restricts to sgn ⊕ sgn.
  - PP 1852 FEM: the lowest nonzero eigenvalues in these sectors are NN 23.0786, DD 222.3711, DN 32.6737, ND 91.4649. All are > λ₁.
  - So a 3-dimensional λ₁ eigenspace contains no 1-dim character, and 3 cannot split as 2 + 1 or 1 + 1 + 1.
- J acts trivially, since χ₅(J) = χ₆(J) = +3. This too is CONDITIONAL on the multiplicity.
- MR2 should cite all four sectors. The "below 23.0786" bound needs DN and ND, not only NN.

**L13. 3 vs 3⊗sgn; levels 2–5; charged S⁴ towers. OPEN. Agree.**
- 3 vs 3⊗sgn is decidable via the two Isom extensions of each 3-dim Aut⁺ irrep, i.e. the irrep-BC FEM that MR2 proposes.

## Part F — MR2 erratum 00b1a96a (responses to PP fc93b8c0 fixes 1–8)

**F0. Shas, frozen order and byte-identical rerun. PROVED.**

**F1. r̃W̃r̃⁻¹ = −W̃ for both (i) and (ii). PROVED.**
- It matches my fc93b8c0 gamma-word table (3 non-ρ gammas give (−1)³).
- MR2's log checks M(1+W̃)/2M⁻¹ = (1−W̃)/2 for both.

**F2. rW also maps W̃ to −W̃. PROVED.** This matches my fc93b8c0 P10 row "rW for (i): ANTICOMMUTE". W acts trivially on the wall.

**F3. New wording. PROVED (correct).**
- "Not inside; at the open lower endpoint; unresolved 1.55e-4 offset" is exactly my fix 3.
- The reference 5511845e is verified on disk. Its Fix 6 makes 1.2876 and 1.0316 measure- and location-dependent and non-physical, consistent with PP 1846 S13r.

**F4. Row 11 is superseded by 8399be55 rows 7, 9 and 11. PROVED (correct bookkeeping).**

**F5. Retraction and replacement. PROVED (checked rigorously).**
- Closed subgroups of SO(3) are, up to conjugacy, finite (C_n, D_n, T, O, I), SO(2), O(2) or SO(3).
- T, O and I have element orders ≤ 5 (T has 1,2,3; O has 1,2,3,4; I has 1,2,3,5). So they have no element of order 8.
- In C_n or D_n, and also in SO(2) or O(2), the elements of order 3 and 8 are not reflections (those have order 2), so they lie in the rotation part about one axis. Then x = (yz)⁻¹ lies there too.
- For coaxial rotations, x = π and y = ±2π/3 force z = −(π ± 2π/3) ≡ ±π/3, which has **order 6 ≠ 8**. Contradiction.
- So the closure of the image is SO(3), i.e. the image is dense.
- The argument uses only the exact orders, not the numeric tilt.
- **b0c6e848 never uses the false lemma.** grep of its .md, .py and .log finds no "orders 3 and 8" anywhere. It uses density, which is now correctly proved, and transfers it to π₁ by finite index (PP fc93b8c0 S7).

**F6. Trivial-generator case. PROVED.**
- x = 1 ⇒ y² = y³ = 1 ⇒ trivial.
- z = 1 ⇒ trivial.
- y = 1 ⇒ the image is ⟨x⟩ ≅ ℤ₂ (or trivial).
- Δ⁺ab = ℤ₂, generated by x.
- x_A ∉ SL(2,3). PP independently confirms that every generating pair has det x = −1, which is forced: the only det-1 involution is −I, which is central and cannot generate together with y.
- So the character is det∘(Δ⁺ → Aut⁺), which is trivial on π₁ given the kernel premise.

**F7. Fermion target and the w₂ reduction. PROVED, with a strengthening.**
- The branching is correct: Spin(5) ⊃ (Spin(2) × Spin(3))/ℤ₂ gives 4 → 2_{+1/2} ⊕ 2_{−1/2}.
- **About the parent's question.** A (Spin × SU(2))/ℤ₂-type structure does in general allow w₂(TX) = w₂(E) ≠ 0. Here the combined condition is w₂(TΣ) + w₂(L) + w₂(E₃) = 0. The cross term w₁(L)w₁(E₃) vanishes because both are orientable.
  - w₂(TΣ) = χ(Σ) mod 2 = 0.
  - w₂(L) = deg L mod 2 = ±2 ≡ 0.
  - So the "spin^h" freedom buys nothing and the condition is exactly w₂(E₃) = 0.
  - **The earlier conclusion is unchanged.**
- **Strengthening.** Premise (b) (the 7D fermion content) can be replaced by an 11D theorem:
  - TY ⊕ ℝ ≅ π*TΣ ⊕ π*(E₅ ⊕ ℝ), so w₂(TY) = π*(w₂TΣ + w₂E₅).
  - π* is injective on H², since the S⁴ fibre is 3-connected.
  - Spin structures on Y form a torsor over H¹(Y;ℤ₂) = H¹(Σ;ℤ₂).
- **The combined-structure claim is PROVED.** The class of (s, s_R, ρ̃) modulo diagonal twists is ρ̃ + (s + s_R). Since s + s_R lives in the linear J[2]-set (with d₀ = 0 fixed, PP L6), the map is an Aut⁺-equivariant bijection onto the ρ̃-torsor.
  - The ρ̃-torsor has 0 fixed points for k=3 (L5) and for V₄ (L9).
  - For the MN background (trivial ρ, linear torsor) there is exactly one fixed point, d₀.
  - This agrees with 8399be55 A3 and PP's earlier [Z]/[D] checks.

**F8. Closed result: the invariant SU(2)_R locus is {trivial} (also for the combined structure); SO(3)_R has 3 invariant points (trivial, k=3, Klein). CONDITIONAL, on (a) Bolza uniformization only.**
- Premise (b) is removable: see F7, via the 11D route.
- Premise (c), the "k=3 root to 1e-6", is removable:
  - **MR2's root is float-only.** It is bisection with 80 iterations, with no interval or Krawczyk certification.
  - It does not need certification. The root has the closed form cos ψ = cos(3π/8)/sin(π/3) = 0.441885, so ψ = 1.113098, and |cos ψ| < 1 certifies that it exists.
  - Every GF(2) result depends only on the exact orders (L4), not on ψ.
- The SO(3) count of 3 is PROVED given (a):
  - The abelian SO(2) case reduces to 2-torsion via J ∈ [Aut⁺, Aut⁺], hence to an invariant character, hence trivial.
  - The dihedral case is excluded (L8).
  - k=3 and the Klein point are unique up to gauge: ψ ↔ π−ψ conjugate, and S₄ induces GL(W).

## Rollup
| part | PROVED | CONDITIONAL | OPEN | REFUTED |
|---|---|---|---|---|
| L (b0c6e848) | 10 (L1–L10) | 2 (L11, L12) | 1 (L13) | 0 |
| F (00b1a96a) | 8 (F0–F7) | 1 (F8) | 0 | 0 |

**TOTAL: PROVED 18 · CONDITIONAL 3 · OPEN 1 · REFUTED 0 = 22.**

MR2 applied my fc93b8c0 fixes 1–8: all eight are applied correctly. Fix 7 goes beyond my request (the combined structure), and that extension is correct. There are no disagreements.

## Fix list for MR2
1. (b0c6e848 §3) Replace "w₂ = 0 because squares vanish" with: squares vanish, so w₂ = αβ; and αβ = 0 because W is the unique invariant 2-plane, hence W = W^⊥ is Lagrangian.
2. (b0c6e848 §1 / [FC]) Do not call [FC] an independent control. It shares b by construction. Add the orbit decomposition 4 + 6 + 6 of the 16 lifts and match it to the theta-characteristic orbits (88949658 [W]), which is the independent check.
3. (b0c6e848 §4(c)) Change "Ad ρ ⊂ O(2) is not abelian" to "Ad ρ reducible, not contained in SO(2)", since V₄ is abelian.
4. (b0c6e848 §0/§1; erratum Fix 8) Drop premise (c). Cite the closed form cos ψ = cos(3π/8)/sin(π/3), and note that b = (1, c, 1) is forced by the exact orders. State plainly that the bisection root is float-only and uncertified, and that it is not needed.
5. (Erratum Fix 7/8) Replace premise (b) with the 11D statement w₂(TY) = π*(w₂TΣ + w₂E₅), π* injective. Spell out why the (Spin × SU(2))/ℤ₂ freedom is vacuous here: w₂TΣ = w₂L = 0.
6. (b0c6e848 §0) State the invariance notion: invariance of the isomorphism class up to SU(2) gauge, the weakest notion. Then non-existence for it implies non-existence of any equivariant structure. Note that Out(SU(2)) = 1 and the center acts trivially.
7. (b0c6e848 §5) For "no 1-dim character below 23.0786", cite all four sectors: NN 23.0786, DD 222.3711, DN 32.6737, ND 91.4649. Also cite the isotypic-decomposition argument.
8. (Tally) Count "PROVED with CONDITIONAL premise" rows as CONDITIONAL in rollups, so that grades compare across files.
