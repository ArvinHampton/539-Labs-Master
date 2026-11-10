# Soft SF FINDINGS: PP audit of NL_DERIVED_PROPOSAL_K3S2_BLOCK_SOURCES_AND_PREV_EMBEDDING_2026-11-09_1310.md (sha be7382b4…, verified MATCH)

- **Authority:** OWNER_WRITE_CALL_e9c1dbda (sha 33d25a79…, verified). Physicist relayed the request.
- **Rules:** additive file. Tip 7cddb188 untouched. No CERT. Nothing sent outside.
- **Method:** hand derivation plus python/numpy/sympy. A full 11D tensor build of F was run in Lorentzian signature; no scratch files were kept.

**Verdict: CONFIRM both parts.** There are caveats, but nothing is refuted.

## Part 1: K3×S² block sources

| # | Claim | PP verdict |
|---|---|---|
| 1.1 | The Einstein blocks are G₅ = 6k²−K_S, G_K3 = 10k²−K_S and G_S² = 10k². | **PROVED.** Ric = (−4k², 0, K_S)·g and R = −20k² + 2K_S, so G = Ric − ½Rg reproduces all three. |
| 1.2 | dF = 0, d*F = 0, F∧F = 0. | **PROVED.** J is parallel and self-dual on K3, so *F = ±q·vol(AdS₅)∧J is closed. Also vol(S²)∧vol(S²) = 0, so no Chern–Simons source is generated. |
| 1.3 | F² = 48q², and (FF − ⅛gF²) has blocks (−6, 0, +6)q². | **PROVED.** In the numerical 11D build with J_ijJ^ij = 4, F² = 48 and the blocks are AdS₅ (time and space) −6, K3 0, S² +6. The S² value comes from FF = 12q² − 6q², and the K3 value from 6q² − 6q². |
| 1.4 | The unique solution is K_S = 4k², Λ₁₁ = −6k², λq² = 2k²/3. | **PROVED.** The linear system in (K_S, Λ₁₁, λq²) has determinant −6 ≠ 0, so the solution is unique, and sympy confirms it. q is real iff λ > 0, which holds for the standard λ = 1/12. The geometry does not depend on λ, so the C1 normalization dispute changes q only. |
| 1.5 | Λ₁₁ = 0 has no solution with k ≠ 0. | **PROVED.** sympy returns no solution, matching NL's −4k² = −10k² contradiction. |
| 1.6 | L7′ as a replacement for L7. | **CONDITIONAL** on adopting the ansatz with zero torsion and zero matter. The link to Φ/V₃₅ is **OPEN**, as NL says. |

**Caveats.** NL makes no claim beyond the scope below; this table just records it.
- J may be any unit element of the hyperkähler sphere aI + bJ + cK. Each choice gives the same blocks.
- The uniqueness in 1.4 is within the ansatz only. Adding a vol(K3) term, or using a non-parallel ω₂, is **OPEN**.
- Λ₁₁ = −6k² equalling the 5D value is an observation, not a derived identity.
- Stability and the 4D content are **OPEN**.

## Part 2: P_rev embedding on H⊗ℂ²

| # | Claim | PP verdict |
|---|---|---|
| 2.1 | P̂(ψ⊗v) = Aψ ⊗ U·v̄ is antiunitary, and P̂² = (γ⁰γ⁰*) ⊗ (UŪ). | **PROVED.** It is a tensor product of two antilinear maps, so it is well defined, and P̂²(ψ⊗v) = A²ψ ⊗ UŪv. |
| 2.2 | Option M (Majorana, U = σx): P̂² = −1 and P̂HP̂⁻¹ = −H. | **PROVED.** Numerically, with an all-imaginary Majorana basis (Clifford checked): A² = −1, σxσx = 1, and γ⁰H̄γ⁰⁻¹ = −H. σx swaps e₁ and e₂. |
| 2.3 | Option D (Dirac, U = iσy): P̂² = −1, and AHA⁻¹ ≠ ±H. | **PROVED.** Numerically A² = +1 and (iσy)(iσy)‾ = −1. Explicitly, AHA⁻¹ = −α_x p_x + α_y p_y − α_z p_z + βm, which is neither ±H. |
| 2.4 | The rank obstruction is removed. | **PROVED**, but only under NL's reinterpretation that H₋ = H⊗e₂ has the same rank as H₊. This departs from the literal "H₋ = H₊⊗ℂ²" (rank 2r). That is why adopting it is **CONDITIONAL** on the Owner. |
| 2.5 | P_rev = P̂∘ι. | **PROVED**, with one sign. For Option D, iσy·e₁ = −e₂, so P̂∘ι(ψ) = −Aψ⊗e₂. This overall phase is harmless. |
| 2.6 | The physical reading. | **OPEN.** |

- **Note on Option M.** An antiunitary P̂ with P̂HP̂⁻¹ = −H commutes with e^{−iHt}. It is a particle-hole type symmetry mapping E to −E, not a time reversal. This is consistent with my B3 result: there is no negative inertial mass.
- **Adoption status.** B2 now has two proved models, M and D. It stays **CONDITIONAL** until the Owner picks one. Option M is the only one that is also a symmetry of free Dirac dynamics.

## Rollup
PROVED 11, CONDITIONAL 2 (1.6 and the adoption in 2.4), OPEN 3 (Φ link, wider flux family, physical reading), REFUTED 0. No CERT. REPORTS ONLY.
