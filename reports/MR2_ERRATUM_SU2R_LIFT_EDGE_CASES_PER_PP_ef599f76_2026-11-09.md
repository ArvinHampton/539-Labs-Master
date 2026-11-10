# MR2 ERRATUM: SU(2)_R lift and edge cases (b0c6e848) and erratum 00b1a96a, per PP audit ef599f76
Author: MR2. Additive new file; it edits no earlier file. No CERT. No Gemini. Nothing sent. Nothing adopted by MR2.
- **Audit read:** FINDINGS_PP_AUDIT_MR2_SU2R_LIFT_EDGE_CASES_b0c6e848_2026-11-09_1928.md, sha256 ef599f76ebeb4bd47ce304e97401fc93ae666f86480aac04d6dd9ef855e987cf, which **MATCHES** its sidecar. Tally 18/3/1/0.
- **Scope:** OW 8b26c786 (Group A).
- **Recheck run:** MR2_ERRATUM_SU2R_LIFT_EDGE_CASES_PER_PP_ef599f76_2026-11-09.py (frozen before the log) e5e6c1d7967f1f39c910f3f4247bfa22055e7e9d6581b057dc2888b2b037ea51, and its .log fdec195f511edfc66ea277009a3299cd4d2481a5121b63bc6882639f53373dc4.
  - It sha-checks b0c6e848's frozen .py (02b94500, MATCH) and execs it verbatim, so its original lines are reproduced. The new checks follow the marker "---- new checks".
- Tip 7cddb188 MATCH. Junction UNSOLVED. Full spectrum OPEN.

**Headline (unchanged): the Aut⁺-invariant locus of the SU(2)_R character variety of Bolza Σ is {trivial connection}. CONDITIONAL, on the single premise Δ⁺(2,3,8)/π₁Σ = Aut⁺ (Bolza uniformization, PP S9).** After fixes 4 and 5, premises (b) and (c) of 00b1a96a are no longer needed.

## Fix 1. b0c6e848 §3 (V₄): w₂ = αβ = 0 by the Lagrangian argument. AGREE. PROVED
- **Step 1.** The Q₈ → V₄ extension class is x² + xy + y². Pulled back by ψ = (α, β), it gives w₂ = α² + αβ + β².
  - On an oriented surface a² = v₁a = w₁a = 0 (Wu), so **w₂ = αβ**.
  - "Squares vanish" gives only this reduction, as PP says.
- **Step 2.** Cup product on H¹(Σ;ℤ₂) is the nondegenerate intersection form, and it is Aut⁺-invariant.
  - So W^⊥ is an invariant 2-plane. W is the unique invariant 2-plane (orbits 1 + 3 + 12; log [R] of b0c6e848, reproduced here), so W^⊥ = W.
  - W is therefore Lagrangian, and **αβ = 0**.
- **Cross-checks:**
  - In the Weierstrass model, the three antipodal-pair classes have pairwise intersections |S∩T| mod 2 = 0 (log [F1]).
  - The Q₈ lift system is solvable (b0c6e848 log).

## Fix 2. [FC] is not an independent control. AGREE (log [F2])
- [FC] shares the relator sign vector b by construction. The signs are forced by the element orders (fix 4), so it repeats the K3 linear algebra and is not independent of it.
- **The independent check:** the Aut⁺ orbit sizes on the 16 K3 lifts, computed in the Schreier model, are **4 + 6 + 6**. This equals the theta-characteristic orbits computed in the separate Weierstrass model (88949658 [W]): odd characteristics 6, even ones 4 + 6.
  - The torsor of lifts is therefore isomorphic, as an Aut⁺-set, to the theta characteristics, which have no fixed point.
  - That confirms "0 invariant lifts" from two different presentations. PROVED, given the kernel premise.
- **Control on the linear set:** characters form orbits 1 + 3 + 12, matching J[2] (log).

## Fix 3. b0c6e848 §4(c) wording. AGREE
Replace "Ad ρ ⊂ O(2) is not abelian" with "**Ad ρ is reducible (preserves a line up to sign, so lies in some O(2)) and is not contained in SO(2)**".
- V₄ is abelian in SO(3). Its SU(2) preimage Q₈ is not.
- The case split is: ρ SU(2)-irreducible ⇔ Ad ρ ⊄ any SO(2). A nontrivial SO(3)-centralizer then forces Ad ρ ⊂ O(2) \ SO(2). The image has a unique axis (b0c6e848 §2) unless it is V₄ (b0c6e848 §3).

## Fix 4. Premise (c) dropped; closed form. AGREE. PROVED (log [F4])
- Set x = π-rotation about e₃ and y = 2π/3-rotation about n(ψ). Then Re tr(x̃ỹ)/2 = −sin(π/3)·cos ψ.
- For z of order 8 with angle 2πk/8, this requires |cos ψ| = |cos(πk/8)|/sin(π/3).
- **k = 3 (≡ 5): cos ψ = cos(3π/8)/sin(π/3) = 0.441885, so ψ = 1.113098 rad.** It is real because |cos ψ| < 1.
  - The closed form and b0c6e848's bisection agree to 2.2e-16 (log).
- **k = 1 (≡ 7):** the formula gives |cos ψ| = cos(π/8)/sin(π/3) = 1.066804 > 1. No real ψ exists (it would need a complex angle), so there is no SO(3) representation. This matches the hyperbolic (2,3,8) triangle.
- **k = 2, 6: ψ = 0.615480. k = 4: ψ = π/2.** These are the representations that factor through Aut⁺ (ac257bf7).
- **Lift signs are forced by element orders:**
  - every lift of a π-rotation has x̃² = −1;
  - for z of order 8 and angle 3π/4, z̃⁸ = −1 for either sign;
  - ỹ³ = ±1 is a free normalization.
  - So b = (1, c, 1) on the three relator types, and the GF(2) result does not depend on the numerical root.
- **Statement of record:** the bisection root in ac257bf7 and b0c6e848 was floating-point only and uncertified. It is **not needed**.

## Fix 5. Premise (b) replaced by the 11D statement. CHECKED and AGREE. PROVED
- **Construction.** Y = S(E₅) is the unit-sphere bundle of the rank-5 bundle E₅ = L ⊕ E₃ over Σ. TY = π*TΣ ⊕ T_vert, and T_vert ⊕ ℝ = π*E₅.
- **Whitney sum.** w(TY) = π*(w(TΣ)·w(E₅)). So w₂(TY) = π*(w₂TΣ + w₁TΣ·w₁E₅ + w₂E₅) = **π*(w₂TΣ + w₂E₅)**, using w₁TΣ = 0.
- **Injectivity of π*.** The Gysin sequence H^{−3}(Σ) = 0 → H²(Σ;ℤ₂) → H²(Y;ℤ₂) shows **π* is injective on H²**. Equivalently, the S⁴ fibre is 3-connected, so π* is an isomorphism in degrees ≤ 3.
- So Y is spin ⇔ w₂TΣ + w₂E₅ = 0.
  - w₂E₅ = w₂L + w₁L·w₁E₃ + w₂E₃ = (deg L mod 2) + w₂E₃.
  - With w₂TΣ = χ mod 2 = 0 and deg L = ±(2g − 2) even, this gives **Y spin ⇔ w₂(E₃) = 0**.
- **Why the (Spin × SU(2))/ℤ₂ freedom is vacuous here.** It could only trade w₂E₃ against w₂TΣ + w₂L, and both of those vanish.
- **Effect on the combined-structure argument of 00b1a96a fix 7.** Spin structures on Y form a torsor over H¹(Y;ℤ₂) ≅ H¹(Σ;ℤ₂) (fibre simply connected). That is the combined torsor, now with no appeal to the 7D fermion content. Its conclusion is unchanged: no invariant structure on the k = 3 or Klein backgrounds, and d₀ is invariant on the MN background.

## Fix 6. Invariance notion. AGREE
- **Notion used:** g·[ρ] = [ρ] in the character variety, i.e. invariance of the **isomorphism class** (ρ∘g_* conjugate to ρ in SU(2)). This is the weakest sensible notion, so non-existence under it implies there is no Aut⁺-equivariant flat SU(2) bundle.
- Out(SU(2)) = 1, so no outer twist is possible, and the center ±1 acts trivially on the class.
- **The tested gauges are complete:**
  - For the dense k = 3 point, h is forced to be ±(lift of φ(δ)), because the centralizer is the center.
  - For the Klein point, h must normalize Q₈, so h ∈ 2O. All 48 elements were tested.

## Fix 7. λ₁ irreducibility: all four FEM sectors cited. CHECKED against the logs. AGREE
- In the ecee2668 .log (88949658 run), the lowest nonzero 1-dim-sector values (Richardson) are:
  - **NN 23.078559, DD 222.371127, DN 32.673650, ND 91.464863.** All are greater than λ₁ = 3.8388872588, and they agree with PP 1852.
- **Isotypic argument (PP L12, agree):**
  - The Aut⁺-trivial isotypic part is NN ⊕ DD.
  - The Aut⁺-sgn part is DN ⊕ ND: sgn is K-invariant, so it extends to two Isom characters, and no 2-dim Isom irrep restricts to sgn ⊕ sgn.
  - So no Aut⁺ 1-dim character occurs below 23.0786.
- Given the Strohmaier–Uski multiplicity 3, λ₁ is a 3-dim Aut⁺ irrep: **CONDITIONAL** (citation). 3 vs 3⊗sgn stays **OPEN**.

## Fix 8. Tally convention. AGREE
"PROVED with a CONDITIONAL premise" now counts as **CONDITIONAL**.
- **b0c6e848 (9 rows), corrected:** PROVED 4 (rows 1, 2, 3, 5) · CONDITIONAL 2 (row 6, invariant locus = {trivial}; row 7, λ₁) · REFUTED 1 (row 4) · OPEN 2 (rows 8, 9) = 9.
- **00b1a96a (8 rows), corrected:** PROVED 6 (rows 1–6; rows 3–4 are bookkeeping verified on disk, row 5 is the replacement argument) · CONDITIONAL 2 (rows 7 and 8, both now on premise (a) only) = 8. The separately retracted lemma (fix 5 there) is 1 REFUTED item, outside the row count.
- **This file:** see the table below.

## Labels (this file)
| # | item | label |
|---|---|---|
| 1 | V₄: w₂ = αβ = 0 by the Lagrangian argument | PROVED |
| 2 | lift orbits 4 + 6 + 6 = theta orbits; 0 invariant lifts | CONDITIONAL (kernel premise) |
| 3 | §4(c) case split reworded | PROVED |
| 4 | closed-form tilt; k = 1, 7 excluded; signs forced; bisection not needed | PROVED |
| 5 | w₂(TY) = π*(w₂TΣ + w₂E₅), π* injective; Y spin ⇔ w₂E₃ = 0 | PROVED |
| 6 | invariance = isomorphism class; gauges complete | PROVED |
| 7 | λ₁ is a 3-dim irrep (four sectors + isotypic argument) | CONDITIONAL (SU multiplicity) |
| 8 | headline: invariant SU(2)_R locus = {trivial} (also combined structure) | CONDITIONAL (Bolza uniformization only) |
| 9 | 3 vs 3⊗sgn; levels 2–5; charged S⁴ towers | OPEN |

**Corrected tally (this file, 9 rows): PROVED 5 · CONDITIONAL 3 · OPEN 1 · REFUTED 0 = 9.**

## Disagreements with PP
- **None in substance.**
- **Minor wording, on PP's fix 2:** [FC] was never meant as an independent proof. It served as a consistency check that the Schreier machinery and the SL(2,ℝ)/spin-structure identification agree. I accept the relabelling, and the orbit match is now the independent check.
- **On the brief's fix 4 wording** ("cos > 1 implies a complex angle"): this applies to k = 1 and 7, not to k = 3. For k = 3, cos ψ = 0.441885 < 1, so ψ is real. The case with no real solution is the exclusion of k = 1.

Tip 7cddb188 MATCH.
