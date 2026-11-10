# Soft SF FINDINGS: PP audit of NL's B2 closures (A) and (B) and their comparison

**Files audited (all hashes MATCH):**
- NL_DERIVED_B2_CLOSURE_B_TWO_SECTOR_HxC2_OPTIONS_M_D_2026-11-09_1315.md (5907eaf3…)
- NL_DERIVED_B2_CLOSURE_A_DIRECT_SUM_NONLOCAL_IOTA_2026-11-09_1315.md (988f1436…)
- NL_B2_CLOSURES_A_VS_B_COMPARISON_2026-11-09_1316.md (cd227dc7…)

**Authority:** OWNER_WRITE_CALL_e9c1dbda (33d25a79…). The request to audit both closures was relayed by Physicist, citing an Owner DIRECT at ~1:06 PM CST.

**Ground rules:** additive file only. Tip 7cddb188 untouched. No CERT. Nothing sent outside.

**Pending:** Local's construction-A file has not landed yet. It will be audited separately.

**Verdict:** CONFIRM (B) and CONFIRM (A), with one correction: A-5(ii) is REFUTED by counterexample. The comparison table needs one row fixed. The uniqueness of Option M is PROVED, with a sharper statement than NL gives.

## Closure (B)
- **B-1 and B-2: PROVED.** P̂ = (γ⁰Π⊗U)K is antiunitary, and P̂² = γ⁰γ⁰* ⊗ UŪ.
- **B-3: PROVED.** For U = [[0,a],[b,0]], UŪ = diag(a b̄, b ā), and b ā is the complex conjugate of a b̄. An antiunitary operator can only square to a real scalar, so P̂² = ±1 iff a b̄ = ±1. In that case P̂² = (γ⁰γ⁰*)·(a b̄). I checked this numerically. The value of a b̄ is invariant under an overall phase U → e^{iθ}U.
- **B-4: PROVED.** In the chiral representation I checked numerically that γ⁰H̄γ⁰⁻¹ ≠ ±H, as in the Dirac representation.
- **Option M: PROVED.** For an antiunitary P̂ with P̂HP̂⁻¹ = −H, P̂(−iHt)P̂⁻¹ = −iHt, so P̂ commutes with e^{−iHt}. This is exactly the condition for a symmetry at fixed t.
- **Remark on H_D⊗σ_z: PROVED.** The conjugation gives (−H)⊗(−σ_z), so P̂ commutes with H, which makes it time-reversal type.
- **Option D: PROVED.**

**Uniqueness of Option M (new, PROVED).** Fix A = γ⁰KΠ. KΠ fixes p, so AHA⁻¹ = −H iff γ̄⁰ = −γ⁰ and γ̄ⁱ = −γⁱ. That is, iff every γ^μ is purely imaginary, which is the Majorana class.
- Given Majorana, P̂² = −(a b̄). So P̂² = −1 forces a b̄ = +1, which means U = e^{iθ}σ_x.
- **Conclusion:** within closure (B), Option M is the unique closure (up to phase) that is sector-swapping, has P̂² = −1 and is a fixed-t symmetry of free Dirac.
- **Caveat:** "Majorana" is a choice of the antiunitary γ⁰K, not just a choice of basis. Under ψ → Sψ the operator γ⁰K changes but its square does not.

## Closure (A)
- **A-1: PROVED.**
- **A-2: PROVED.** No x-local A exists. If A is local, W = A∘(ΠK) is unitary from L²⊗ℂ⁴ to L²⊗ℂ⁸ and intertwines M_f. The multiplicities are uniformly 4 and 8, so W cannot exist (Hahn–Hellinger / multiplicity theory).
- **A-3: PROVED.** The interleaved Hermite map sends an orthonormal basis bijectively onto an orthonormal basis, so it is unitary.
- **A-4: PROVED, and more general than stated.** For any bijective ι, not only the Hermite one, B = εA⁻¹ gives Q² = ε with either sign. So P² = ±1 is a convention in (A).
- **A-5(i) and A-5(iii): PROVED.**
- **A-5(ii): REFUTED by counterexample.** The claim is that H₋ = −AH₊A⁻¹ is "non-local because ι is".
  - **Construction.** H_D on L²(ℝ³,ℂ⁴) and H_D⊗1₂ on L²(ℝ³,ℂ⁸) are both absolutely continuous on (−∞,−m]∪[m,∞) with uniform multiplicity ℵ₀. By Foldy–Wouthuysen they become multiplication by ±ω(p), whose level sets are spheres. So a unitary V with V H_D V⁻¹ = H_D⊗1₂ exists.
  - **Result.** Take ι = V and A = V∘A_M, where A_M is the Majorana γ⁰KΠ. Then H₋ = −AH_DA⁻¹ = H_D⊗1₂, which is local, even though ι is not.
  - **Correct statement.** ι is necessarily non-local (A-2), but H₋ can be chosen local. For the specific Hermite ι, whether H₋ is local is OPEN.
- **A-6: PROVED.**

## Comparison table
- **Row "Fixed-t symmetry of free Dirac" for (A): correct it.** It should read "yes, with local H₋ = H_D⊗1₂ for a suitable non-local ι (PP counterexample)", not "only with non-local H₋".
- **All other rows: CONFIRM.**
- **NL's assessment stands.** (A) still fails two criteria: the Owner formula holds only up to ι, and P² is a convention rather than forced. So Option M remains the unique closure meeting all three criteria (literal local formula, forced P² = −1, fixed-t symmetry).

## Rollup
PROVED 14 (B-1 to B-4, Option M, the σ_z remark, Option D, Option M uniqueness, A-1 to A-4, A-5(i) and (iii), A-6). CONDITIONAL 1 (adoption, which is the Owner's choice). OPEN 2 (locality for the Hermite ι, physical reading). REFUTED 1 (A-5(ii) as stated).

No CERT. REPORTS ONLY.
