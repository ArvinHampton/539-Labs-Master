# Non Local Path: DERIVED PROPOSALS, K3×S² block sources for a repaired L7, and the P_rev codomain and embedding, 2026-11-09 ~13:10 CST
Authority: Owner write-and-derive grant, Nov 9 ~1:00 PM CST. Additive file. Tip 7cddb188 untouched. No CERT. Nothing sent outside.
Everything below is a DERIVED PROPOSAL by NL. It is not Owner or corpus text, and any physics built on it stays CONDITIONAL until the Owner adopts it. Numerical checks were done in python3; nothing was saved apart from this file.

## Part 1: Block sources on AdS₅(k) × K3 × S²
Geometry: warp e^{−2ky} (AdS₅, Ric = −4k²g), Ricci-flat hyperkähler K3, round S² with Gaussian curvature K_S. Einstein blocks, as coefficients of g:
G₅ = 6k² − K_S,  G_K3 = 10k² − K_S,  G_S² = 10k². PROVED.
Prior constraints: an isotropic internal source forces K_S = 0 (NL item 14(i)). PP's lemma: a source isotropic over AdS₅×S² forces K_S = −4k². So the flux must have legs on S².

Ansatz (derived): F₄ = q·vol(S²)∧J, where J is a parallel Kähler 2-form of the K3 hyperkähler structure, with J_ik J_j^k = g_ij and J_ij J^ij = 4. Torsion and matter are set to zero.
- dF = 0. J is self-dual, so *F = ±q·vol(AdS₅)∧J and d*F = 0. F∧F = 0, since vol(S²)∧vol(S²) = 0. So the Chern–Simons term does not source anything. PROVED.
- F² = 48q². F_MPQR F_N^PQR is 0 on AdS₅, 6q²g on K3 and 12q²g on S². Hence (FF − ⅛gF²) has blocks −6q² on AdS₅, 0 on K3 and +6q² on S². PROVED, checked numerically.
- Field equations G + Λ₁₁g = λ(FF − ⅛gF²), where λ is the normalization constant (λ = 1/12 in the standard convention; the Owner's convention is pending):
  - AdS₅: 6k² − K_S + Λ₁₁ = −6λq²
  - K3: 10k² − K_S + Λ₁₁ = 0
  - S²: 10k² + Λ₁₁ = 6λq²
- Unique solution, given k ≠ 0 (PROVED; checked numerically):
  **K_S = 4k²** (round S² of radius 1/(2k)), **λq² = 2k²/3**, **Λ₁₁ = −6k²**.
  The geometric results, K_S and Λ₁₁, do not depend on λ. Only q depends on the normalization.
- Corollary (PROVED within the ansatz): Λ₁₁ = 0 has no solution with k ≠ 0. Setting Λ₁₁ = 0, the K3 equation gives K_S = 10k² and the S² equation gives λq² = 5k²/3, but then the AdS₅ equation reads −4k² = −10k², a contradiction. So this repair requires a nonzero Λ₁₁, which matches the Owner's nonzero Λ₁₁ and makes the theory non-supersymmetric (consistent with flag (j)).
- Proposed L7′, replacing L7: K_S = 4k², Λ₁₁ = −6k², λq² = 2k²/3. Status: CONDITIONAL on adopting the ansatz, zero torsion and zero matter. The link to the original Φ (−Φ/96 and Φ/144) remains OPEN, because Φ "over V₃₅" is undefined. Note that Λ₁₁ = −6k² equals the Λ₅ value numerically. That is an observation, not a derived identity.
- Not claimed: uniqueness of the flux ansatz. Adding F ∝ vol(K3) gives a wider family, which is OPEN. Stability is OPEN, and so is the 4D/SM content.

## Part 2: P_rev codomain and embedding
PP correction accepted: with H₋ ≅ H₊⊗ℂ² fibrewise, an anti-diagonal Q on H₊⊕H₋ gives Q² = diag(BA, AB), and that cannot equal ±1 by rank. So B2 stays CONDITIONAL on ι.

Derived proposal: read the Owner's H₊⊗ℂ² as the combined two-sector space 𝓗 = H⊗ℂ², with sectors H₊ = H⊗e₁ and H₋ = H⊗e₂. Both sectors then have equal rank, and the rank obstruction does not apply. Let A = γ⁰KΠ, define ι(ψ) = ψ⊗e₁, and set
  P̂(ψ⊗v) = Aψ ⊗ U·v̄, with U a 2×2 unitary and v̄ complex conjugation on ℂ².
Then P̂ is antiunitary and P̂² = (γ⁰γ⁰*) ⊗ (U·Ū). PROVED.
- Option M (recommended): Majorana representation with U = σ_x. P̂ swaps the sectors (anti-diagonal), P̂² = (−1)(+1) = −1, and P̂(H⊗1)P̂⁻¹ = −H⊗1 for the free Dirac H. All three hold. PROVED.
- Option D: Dirac or chiral representation with U = iσ_y. P̂ swaps the sectors and P̂² = (+1)(−1) = −1. But A H A⁻¹ ≠ ±H, so it is not a symmetry of the free Dirac dynamics. PROVED.
- With either option, the Owner's map is recovered as P_rev = P̂∘ι: ψ ↦ γ⁰ψ*(−x,t) ⊗ (sector-label vector in H₋) (for Option M, the label is e₂). In Option D the −1 comes from the ℂ² factor, which is a Kramers-type structure. Under either option the "topological phase" is not needed.
- Status: the construction and its properties are PROVED. Adopting it as the definition of P_rev is CONDITIONAL on the Owner's choice of option, and the B2 label follows that choice. The physical reading (mirror sector, inter-brane boundary) is OPEN.
