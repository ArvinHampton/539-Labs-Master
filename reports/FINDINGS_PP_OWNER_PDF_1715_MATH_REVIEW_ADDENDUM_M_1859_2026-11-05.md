# ADDENDUM M — Owner t4106 boundary-selector proposal (relay-based; bounded; No CERT; no .tex)

## Claims checked
- **Joint constraint C0x0 + C_M x_M = 0.** Row k reads γ_k x0(Ω_k) + μ_k x_M(Λ_k) = 0. This is a cancellation between the two ends. It does NOT force x_M(Λ_k) = 0 or x0(Ω_k) = 0 separately. So the claim "C_M forces exit zeros" is FALSE as stated.
- **Correct construction for independent end constraints.** Split the boundary space as E = E0 ⊕ E_M, and set:
  - C0 = [S0; 0]
  - C_M = [0; S_M]
  - B = [S0; S_M P]
  
  The solutions are then ker S0 ∩ ker(S_M P). Unique (trivial) iff B is injective.
- **Conditions on the selectors (needed, not optional):**
  - The labels must be sets, not single labels.
  - The weights must be nonzero.
  - Uniqueness requires enough rows: rank B = 48.
  - Duplicate rows add no rank.
  - The values of γ alone do not make the map injective.
  - Prescribing nonzero exit values needs an inhomogeneous right-hand side b.
- **Claim that "uniqueness aligns nonzero Fourier sums with independent row ranks": NOT ESTABLISHED.**
  - Counterexample: C0 = I, C_M = −I, P = I gives B = 0, so the solution space is all of ℂ⁴⁸, even though every block has full rank. P = I is realized with M = 2 by T1 = R3, T2 = R47, since 3·47 = 141 ≡ 1 mod 140 and both primes are in the list.
  - Converse: C0 = I, C_M = 0 gives uniqueness for ANY P, including a singular one. So nonzero Fourier sums are neither sufficient nor necessary.
- **Correct Fourier form.** Let V be the character eigenvector matrix over ℂ, so P = V diag(τ) V⁻¹ with τ(χ) = Π_i λ_i(χ). Then rank B = rank(C0 V + C_M V diag(τ)). Coordinate selectors are generally NOT diagonal in the Fourier basis.

## Corrections to the source wording
- **Parity.** Under J = diag χ140, it is the coordinate split and inert classes that are swapped. Each character eigenline is PRESERVED by convolution, not swapped. Addendum L's parity statement is about coordinate blocks and stands. Conjugation by J maps the χ-line to the χ·χ140-line.
- **Eigenvalue convention.** With R_c v_g = v_{cg}, take v_χ = Σ_g χ(g⁻¹) v_g. Then R_c v_χ = χ(c) v_χ.
- **"Circulant" wording.** "Group circulant" on U140 is valid. It is NOT an ordinary 48-cyclic circulant, because U140 ≅ C2×C4×C6 is noncyclic.

## Bounded criterion (return)
Solutions ≅ ker[C0 + C_M P]. Unique iff rank(C0 V + C_M V diag τ) = 48. For split selectors, unique iff ker S0 ∩ ker(S_M P) = 0.

## OPEN
- The physical choice of Ω, Λ, γ, μ.
- The N/W/capacity link.
- The full 48×11 table: not requested, not computed.
