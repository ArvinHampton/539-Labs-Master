# NL DERIVED PROPOSAL: B2 closure (B), two-sector space H⊗ℂ², Options M and D, 2026-11-09 13:15 CST
Owner directive: voice, ~1:06 PM CST, relayed by Physicist. NL leads (B). Additive file. Tip 7cddb188 untouched. No CERT. Nothing sent outside. B2 is NOT closed here; it closes only after the comparison file and PP's audit.
This is a derived proposal by NL, not Owner text. It supersedes nothing; it expands Part 2 of NL_DERIVED_PROPOSAL_K3S2_BLOCK_SOURCES_AND_PREV_EMBEDDING_2026-11-09_1310.md (be7382b4…).

Setup. H = L²(ℝ³)⊗ℂ⁴ is the Dirac space. 𝓗 = H⊗ℂ² is the two-sector space, with H₊ = H⊗e₁ and H₋ = H⊗e₂. Both sectors have equal fibre rank 4, so PP's rank obstruction does not apply. Let Π be the map x↦−x and K_tot the complex conjugation on 𝓗. Define
  P̂ = (γ⁰Π ⊗ U)·K_tot,  U ∈ U(2).
Then P_rev := P̂∘ι with ι(ψ) = ψ⊗e₁, which gives P_rev ψ = γ⁰ψ*(−x,t) ⊗ Ue₁. This is the Owner's formula, placed in H₋ when Ue₁ ∈ ℂe₂.

B-1 (PROVED). P̂ is antiunitary, because γ⁰ is unitary, Π is unitary, U is unitary and K_tot is antiunitary.
B-2 (PROVED). P̂² = (γ⁰Π⊗U)K(γ⁰Π⊗U)K = γ⁰γ⁰* ⊗ UŪ, using Π² = 1 and Π commuting with K.
B-3 (PROVED, classification). P̂ swaps the sectors iff U = [[0,a],[b,0]] with |a| = |b| = 1. Then UŪ = diag(a b̄, b ā). So P̂² = ±1 iff a b̄ ∈ {+1, −1}, and in that case P̂² = (γ⁰γ⁰*)·(a b̄). The case a b̄ = +1 is σ_x-type; the case a b̄ = −1 is iσ_y-type.
B-4 (PROVED, numerical check). γ⁰γ⁰* is +1 in the Dirac and chiral representations and −1 in the Majorana representation.
Option M: Majorana representation with U = σ_x. P̂ swaps the sectors and P̂² = (−1)(+1) = −1. With H_tot = H_D⊗1, P̂ H_tot P̂⁻¹ = −H_tot (numerically verified for free Dirac H_D). Since P̂ is antiunitary with t fixed, −H is exactly the dynamical-symmetry condition. PROVED.
  Remark (PROVED): with H_tot = H_D⊗σ_z instead, P̂ commutes with H_tot, because σ_xσ_zσ_x = −σ_z. An antiunitary operator that commutes with H and keeps t fixed maps solutions to time-reversed solutions, so it is not a symmetry with t fixed. H_D⊗1 is the right choice.
Option D: Dirac or chiral representation with U = iσ_y. P̂ swaps the sectors and P̂² = (+1)(−1) = −1, with the −1 supplied by the ℂ² factor (a Kramers-type structure). But γ⁰KΠ H_D (γ⁰KΠ)⁻¹ ≠ ±H_D (numerical), so P̂ is not a fixed-t symmetry of free Dirac dynamics. PROVED.
Not needed: the "topological phase from the 35-component vector". By B-2 a phase cannot change P̂².
Status: construction PROVED. Adopting it as P_rev is CONDITIONAL on the Owner's option. The physical reading (mirror sector, inter-brane boundary) is OPEN.
