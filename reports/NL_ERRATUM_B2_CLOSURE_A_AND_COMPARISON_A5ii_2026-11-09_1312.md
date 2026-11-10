# NL erratum: closure (A) item A-5(ii) and the comparison row (additive)

Date: 2026-11-09, about 13:12 CST (America/Chicago). Author: Non Local Path (NL).

Status: additive erratum. It does not edit any earlier file. Not a CERT. B2 stays OPEN.

## Files this erratum applies to (left unchanged)

- `NL_DERIVED_B2_CLOSURE_A_DIRECT_SUM_NONLOCAL_IOTA_2026-11-09_1315.md`, sha256 988f1436f5c75ace3b64029654f664faa0fd8d7aab540798a17d08d7fadd4bfc
- `NL_B2_CLOSURES_A_VS_B_COMPARISON_2026-11-09_1316.md`, sha256 cd227dc78ad88360666b1353368c3dd2b499f3204103d4459ee51ec56922bdcc

## Source of the correction

PP's audit `FINDINGS_PP_SOFTSF_AUDIT_NL_B2_CLOSURES_A_B_COMPARISON_2026-11-09_1309.md`, sha256 f95223774c21222c9e8ca71dbf711fb1234f6fad69a553e32daf495c2245b0ce.

## E1. A-5(ii) is withdrawn and REFUTED by proof (NL agrees)

My claim was that H₋ = −A H₊ A⁻¹ is necessarily non-local because ι is non-local. That claim is false.

**Proof (PP's argument, checked independently by NL).**

1. H_D on L²(ℝ³, ℂ⁴) is absolutely continuous, with spectrum (−∞, −m] ∪ [m, ∞) and uniform multiplicity ℵ₀. To see this, apply Foldy–Wouthuysen, which gives multiplication by ±ω(p). Each level set of ω is a sphere.
2. H_D ⊗ 1₂ on L²(ℝ³, ℂ⁸) has the same spectrum, the same spectral type and the same multiplicity.
3. By Hahn–Hellinger, there is a unitary V with V H_D V⁻¹ = H_D ⊗ 1₂.
4. In the Majorana representation, γ⁰KΠ conjugates H_D to −H_D. Taking ι = V then gives H₋ = −A H₊ A⁻¹ = H_D ⊗ 1₂, which is local.
5. So a fixed-t symmetry with local H₋ can be achieved, but only for a suitably chosen non-local ι.

## E2. Corrected entry for closure (A)

| Item | Status |
|---|---|
| (A) is a fixed-t symmetry with local H₋ for a suitable non-local ι (ι = V) | PROVED |
| H₋ is local under the Hermite-interleaving ι of A-3 | OPEN |

A-5(i) and A-5(iii) stand as PROVED: the Owner's formula holds only up to ι, and ι is non-canonical.

## E3. Corrected comparison row

The row in the comparison file reading "(A): non-local −U dynamics" is replaced by:

> (A): fixed-t symmetry with local H₋ for a suitable non-local ι; locality under the Hermite ι OPEN.

## E4. Sharper uniqueness for Option M (PP, PROVED)

Within (B), Option M is unique up to phase, with U = e^{iθ}σ_x. It is the only choice that swaps the sectors, has P̂² = −1, and is a fixed-t symmetry of free Dirac.

## E5. Assessment (unchanged in substance)

(A) still fails two of the three criteria:

- its formula holds only up to ι, not literally;
- P² = ±1 is a convention, not forced.

So Option M remains the only closure that meets all three criteria. Adoption is the Owner's choice, and B2 is not closed.

Labels: PROVED (E1, E2 first row, E4); OPEN (Hermite-ι locality); REFUTED (A-5(ii) as stated); CONDITIONAL (adoption).
