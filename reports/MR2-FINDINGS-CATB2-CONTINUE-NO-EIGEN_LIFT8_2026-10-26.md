# MR2 FINDINGS — CatB-2 CONTINUE, no Eigen (lift-eight) — 2026-10-26 ~17:35 CDT (America/Chicago)
Status: **PARTIAL** (residual→resonant map statement filled, scoped to the St⊗χ slice; ρ̄|₇ ABSENT)
Authority (live sha256): ASSIGN 12f57687…2d37 | OW lift-eight 3c95fd9c…4634 | OW proof-standard/no-CatA-gate ef6da7e7…6192 | prior DEEPEN 4889a85f…e7de030 (read in full, not contradicted) | prior PURSUE 02aab8ae…312d | MR2 P5a reverse-engineer 2b49ca25…a9cec | Local R-H map 9910ade2…1290 | MR2 discipline-search ternary geom dc0420a8…0829 (now located on disk; corrects prior "not located")
tip Soft SF LOCK start/end 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | tip_touched NO | no Eigen material read or used | Kerr BLOCKED (untouched) | Bridge PARTIAL READY NO | **does NOT prove P5a**
Standard: Owner proof standard. Each claim below is marked [PROVED] (with its argument), [CITE] (Cat A literature), or [GAP-n] (named and unproven).

## 1. ρ̄|₇ Written scan → **ABSENT**
I scanned OWNER_WRITE_* and MR1_* for an Owner-Written local type of ρ̄ at 7. The only hits are OW lift-eight line 18 ("Written-only ρ̄|₇ when on disk") and OW NEXTSTEP line 21 ("still ABSENT"). Both are directives, not a Written type. The {3,5,6}/7 float hint (Card1D/MR1) stays a non-Written hint. **ABSENT.**

## 2. Residual→resonant map statement (St⊗χ slice only) [Cat B]
Setup: X = S₄(Γ₀(49)) with trivial character, the scalar part. Its 7-new part has dim 8 (prior DEEPEN). Write X^{St} for the subspace whose local type at 7 is St⊗χ₋₇. The other types are PS or SC.
- **Lemma A [PROVED, standard local argument + CITE Atkin–Li]:** dim X^{St} = 1, spanned by f⊗χ₋₇, where f is the unique newform in S₄(Γ₀(7)). Proof sketch: (i) A twist-minimal newform at level 7² with St-type at 7 would need conductor exponent 1, which is a contradiction. So every St-type newform at 49 is a twist (St⊗χ) of a level-7 newform by a character χ of conductor 7. (ii) For the twist to have trivial character, χ² = 1, so χ = χ₋₇. (iii) dim S₄(Γ₀(7)) = 1 (table, computed). ∎ This matches the prior DEEPEN saturation.
- **Definition (residual class):** a residual class on the slice is a nonzero class [c] ∈ C_har(SL₂ℤ[1/7], P²_{ℤ₇}) ⊗ 𝔽₇ (Teitelbaum lattice, rank 2 = Darmon two copies of the 1-dim slice). This class must satisfy two conditions: it is not the reduction of a cochain whose St-form is ≡ 0, and it is congruent mod 7 to the cochain attached to f⊗χ₋₇.
- **Definition (resonant close):** the residual class is resonant if there exists ρ̄-isotypic data (a ρ̄-twisted harmonic cocycle) whose reduction equals [c]. This means a nonzero map Hom_{SL₂(ℤ/7)}(ρ̄|₇, St⊗χ-slice) ≠ 0 at the mod-7 level.
- **Proposition B [PROVED conditional]:** if ρ̄|₇ restricted to the 7-component has no constituent isomorphic to a character (scalar), then the Hom is 0 and there is no resonant close on the slice. Proof: the slice is 1-dim, so as an SL₂ representation it is a character, and Schur's lemma gives the result. ∎ The hypothesis = **[GAP-1]**: ρ̄|₇ is unknown (ABSENT). Under the float hint, a 3-dim irreducible (Nobs–Wolfart) would satisfy the hypothesis, giving *no resonance on the slice*. That is a conditional non-resonance statement, **not** a vanishing of the 592-space.
- **[GAP-2]:** the integral structure gives the cochain lattice no ρ̄-multiplicity. Even if ρ̄|₇ contains a character, the multiplicity of the St slice inside the 592 remains unproven.
- **[GAP-3]:** everything outside the slice (PS/SC, i.e. 7 of the 8 new dims, plus the 503/89 split) is outside Teitelbaum theory at 7² [CITE Teitelbaum 1990; Darmon 2001 §1 needs p‖N]. No statement.
- Relation to MR2 P5a R6 (2b49ca25…): this section is the precise form of R6. R6 does not reach 0 at κ=4, and P5a remains open.

## 3. Adjacent material (no merge)
- Local R-H map 9910ade2…: this is the P-even local branch toward BH mechanics. It is *adjacent residual language* (Bridge C leg, tip 7cddb188…). Distinction: R-H is an Owner-defined physics lane, and BT/St is a p-adic automorphic slice. No identification is claimed. Merging them would be a Soft SF overclaim.
- Ternary-geom discipline search dc0420a8…: located on disk and cited only. It adds no level-49 constraint beyond Lemma A.

## 4. Vanish-queue / Card5
No unassigned geometric vanish row can be filled cite-grounded without Eigen. **No stub opened.**

## 5. Fillable vs blocked
- Filled: the ABSENT stamp, Lemma A (proved), the residual/resonant definitions, Proposition B (conditional), and the R6 precise form.
- Blocked: GAP-1 (Written ρ̄|₇), GAP-2 (multiplicity), and GAP-3 (PS/SC/503/89).

## Soft SF risks — Auditor press YES
1. Reading Prop B under the float hint as proved non-resonance (it depends on GAP-1).
2. Reading slice non-resonance as P5a vanishing (dim 592 ≠ 0 stands).
3. Merging R-H lane language with the BT slice.
