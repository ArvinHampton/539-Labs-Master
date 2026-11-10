# ADDENDUM L — Owner t4104 grounded coordinate formula (relay-based; bounded exact check; No CERT; no .tex)

## Setting
- L_i = F[U140], n = 48, basis v_g (units in order), ψ(r,s) = g_r g_s⁻¹ mod 140.
- Then T_i = Σ_k α_ik R_{p_k}, where R_c is the regular permutation v_g ↦ v_{cg}. This is a convolution (group-algebra) family.
- U140 is abelian, so the left and right actions agree. Labelling it the "right" action is harmless.
- The arbitrary-ψ rank-1 counterexample (Addendum K) no longer applies.

## Status of the claims
- **The α are unspecified.** So this is a valid family of operators, not a fixed operator. The sentence "entry nonzero iff match" holds only when α_ik ≠ 0.
- **Parameter dependence (K.1 stands).** D has kernel of dimension 48 and cokernel 0 for every choice of T_i. Only the boundary kernel ker(C0 + C_M P) depends on the parameters, and it also depends on C0 and C_M, not only on α.

## PROVED consequences (exact)
- **Fourier transform over ℂ.** For each character χ of U140, T_i acts on the χ-eigenline with symbol λ_i(χ) = Σ_k α_ik χ(p_k).
  - T_i is invertible iff all 48 symbols λ_i(χ) are nonzero.
  - The product P = T_M⋯T_1 has symbol Π_i λ_i(χ), so rank P = #{χ : Π_i λ_i(χ) ≠ 0}.
  - If F ≠ ℂ, the same holds after extending scalars, since rank is unchanged.
- **Parity.** Every p_k ∈ K90 has χ140(p_k) = −1 (all 11 checked).
  - Let J = diag(χ140(g)). The 24 split and 24 inert classes are swapped by each R_{p_k}, so each T_i is block off-diagonal and J T_i J = −T_i (verified exactly for all 11).
  - Hence J P J = (−1)^M P.
- **Rank is not forced by the primes.** Exact ranks:
  - rank R3 = 48 (invertible).
  - rank(R3 + R11) = 36 (singular). The reason: R3 + R11 = R3(I + R97), with 3⁻¹·11 = 97 mod 140.
  - 97² = 29, 97³ = 13, 97⁴ = 1, so R97 has 12 cycles of length 4, and I + R97 has nullity 12 and rank 36 (verified).

## Not established / OPEN
- How the physical boundary blocks C0 and C_M are chosen is not determined by the primes.
- The link to the original N, W and capacity is OPEN.
- "Preserves field extensions" remains UNSUPPORTED.

## Syntax
- Correct `\operatorname{\operatorname{coker}}` to `\operatorname{coker}`. No file assembled or compiled.
- The request to integrate this or lay out the boundary blocks was not acted on: no explicit file-write was authorized.
