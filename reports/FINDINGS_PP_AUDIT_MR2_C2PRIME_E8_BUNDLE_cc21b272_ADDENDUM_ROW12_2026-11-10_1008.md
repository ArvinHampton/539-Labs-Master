# PP addendum to FINDINGS_PP_AUDIT_MR2_C2PRIME_E8_BUNDLE_cc21b272_2026-11-10_1007.md (51198d6f…): row 12 (E-T)
New additive file. The 1007 file is unchanged and read-only. **On row 12 and on the tally, this addendum supersedes it.** Junction UNSOLVED. Nothing adopted.

## Correction: row 12 (E-T) equivariant lift goes from PROVED (as implication) to **OPEN**. Topological lift PROVED.
The 1007 file accepted MR2's row 12. On re-check, the step from "df is an isometry" to "an E₈ bundle automorphism" has a gap.

1. **f reverses the orientation of Y₆.** Its Jacobian is diag(−1, −1, −1) on {x, φ₁, φ₂}, so det = −1. df is therefore an automorphism of TY₆ in O(6) \ SO(6).
2. **SO(6) itself is not a subgroup of E₈ through the standard routes.**
   - Through SO(6) × SO(10) ⊂ SO(16): the preimage in Spin(16) is Spin(6), and the semispin quotient (Spin(16)/⟨ω⟩) does not remove Spin(6)'s −1 because ω ∉ Spin(6). The image is Spin(6) ≅ SU(4).
   - In (SU(4) × Spin(10))/ℤ₄ ⊂ E₈, SU(4)/ℤ₂ alone does not embed.
3. **So the standard embedding E-T needs the spin lift of TY₆.**
   - The spin lift exists because w₂(TY₆) = π*(w₂Σ + w₂L) = 0.
   - The automorphism must then act through Pin(6), extended by a compensating reflection in the Spin(10) factor.
   - That requires that **f preserves the chosen spin structure** (a δ ∈ H¹(Y₆; ℤ₂) ≅ H¹(Σ; ℤ₂) check), and that **the lifted involution squares to +1, not to the central/−1 element on the 128**.
   - Neither was computed. This is the same unverified-check status as row 14, so OPEN.
4. **What remains PROVED:** n = 0 by D2. With D4 (COND, cited), E-T is topologically trivial, so a bundle isomorphism f*V ≅ V exists (an implication of D4, as row 15 with n = 0). Under r̃ (orientation-preserving on Y₆), row 12's SO(6)-level statement is unaffected, but the same spin/Pin caveat applies to the E₈ lift.

E-Λ± (row 13) stays PROVED as an implication, provided a group embedding SO(3) ⊂ E₈ is fixed (an SO(3) subgroup is assumed; this is part of MR2's unspecified embedding). In that case functoriality of associated bundles plus df² = id suffices. **MR2 must state this as a premise.**

## Revised PP tally (supersedes 1007)
**PROVED 15 · COND 2 · OPEN 6 · REF 0 = 23**, plus 1 bookkeeping row. The changes vs MR2 are row 12 (PROVED → OPEN) and row 14 (COND → OPEN).

Branch verdict, revised: the E₈ lift is PROVED as an implication for **E-0 and E-Λ±** (with the premises in 1007 §E plus a fixed SO(3) ⊂ E₈). For E-T, only the topological lift is established; the connection-preserving involutive lift is OPEN. B1-c2′ stays COND overall, not adopted.

## Added fixes for MR2
- **7. priority:true.** Row 12: regrade to OPEN for the connection-preserving involutive E₈ lift. Keep "topological lift (n = 0, D4)" as an implication. Either:
  - specify the compensating reflection in Spin(10), and prove that f preserves the spin structure of TY₆ and that the Pin lift squares to +1 in E₈; or
  - leave the row OPEN.
- **8.** Row 13: state the premise "a fixed SO(3) ⊂ E₈ subgroup embedding".
