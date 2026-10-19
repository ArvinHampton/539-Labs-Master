# U1 LEDGER — s = 7 local root numbers and Atkin–Lehner comparison (2026-10-18)

Package: `AtkinLehner_Local_2026-10-18/`. This replaces "Atkin–Lehner partial/open" in rev. 5 §13.8 (erratum (c)).
Pure copy-and-create. No locks altered. CORE_FREEZE holds. Distinct from HQCC termination claims. No TPC or RH claim. Convention: Cat A = proved or exact; floating-only/numerical/cited = Cat B. See ERRATUM_Rev5_PostPush_2026-10-18.md. Text outputs are verbatim in the package's OUTPUTS_BUNDLE_2026-10-18.txt (sha256 per member).

## Category A
- A1. Local root numbers ε_v (𝔭₂, 𝔭₅, 𝔭₇, ∞) for all 24 cusp characters are exact in Q(ζ₈₄₀) (Tate's local formulas), with |ε_v|² = 1. They are independent of the auxiliary element c, and the product is the same under both additive-character conventions.
- A2. ε_𝔭₂ is a 6th root of unity. ε_𝔭₅ is never a root of unity. ε_𝔭₇ is ±1 for k ≡ 3 mod 6 and otherwise not a root of unity. λ₂λ₅λ₇ = 1.
- A3. The global root numbers (as exact local products) have modulus 1 but are **not roots of unity**: their minimal polynomials are non-monic, e.g. 5t⁸ + 6t⁴ + 5.
- A4. The sector signs are not individual local root numbers. They are products of them: Z_p = ψ_𝔭(−1) = −1 at p = 5, 7, and S_p² = ω_{π_p}(−1) = −1 at 5 and +1 at 7.
- A5. [k,0,1] and [k,1,1] have identical finite local factors, so W(partner) = −W.

## Category B
- ∏_v ε_v = W (PARI lfunrootres, numerical, ≤ 2.7e−63).
- W_p ↔ S_p holds only up to a fixed unit (Atkin–Li normalisation, cited and not re-derived). W_p was not applied to the actual forms.
- That the sector is spanned by these characters is taken from earlier reports.

## Files not included
None.
