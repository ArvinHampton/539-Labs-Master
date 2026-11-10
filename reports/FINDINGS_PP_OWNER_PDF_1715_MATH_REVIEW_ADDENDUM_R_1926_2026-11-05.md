# ADDENDUM R — Owner t4118 orbit table + capacity claims (relay-based; bounded 48-element enumeration; No CERT; no .tex)

## Table (VERIFIED exactly)
- The 28 orbits partition all 48 elements of C2×C4×C6, with no overlaps.
- The map π(j,k,l) = (j, 2−k, −l) equals c ↦ c⁻¹w⁻² for w = y. Every listed orbit is π-stable, so the twisted symmetry a_c = a_{c⁻¹w⁻²} HOLDS for this table.
- The self-loop is the element c with cy = e, which is y³ = O2. It has weight 0, which is consistent.
- Degree = 127 + 39√35. I confirm the Owner's value.
- Positivity HOLDS for this table, unlike Addendum Q: every weight is positive, including B = 6 − √35 ≈ 0.084.

## Spectrum of the shifted operator Σ_c a_c R_{cy}
- All 48 eigenvalues are real, as expected for a real symmetric operator. They take 13 distinct values.
- The largest is 127 + 39√35 ≈ 357.73, on the trivial character. The smallest in absolute value is ≈ 2.916.
- There are NO zero eigenvalues, so the shifted operator is invertible for this table. This is a numeric check; the minimum |λ| is far from 0.
- Repeated eigenvalues (the χ / χ⁻¹ degeneracy) are unavoidable for a symmetric operator and do NOT mean loss of rank.
- Keep the raw convolution Σ a_c R_c separate from the shifted Σ a_c R_{cy}. The results above are for the shifted one.

## Core errors (confirmed)
- **The pairing map.** The pairing on indices is translation by t = (1,2,3), not π.
  - With F_{χ,g} = χ(g)/√48, we get F R_t F* = diag χ(t) = diag (−1)^{p+q+r}. This is diagonal, not dense.
  - So B_F = B F*, and the complementary-selector rank 24 from Addendum Q still stands. "Dense mixing" is FALSE.
- **Linear independence.** The 28 variables include α_2 = 0, so they cannot be independent.
  - The values lie in Q(√35), which spans at most 2 dimensions over Q(i, √3).
  - Using u + vξ also spans at most 2 and takes the coefficients out of the field.
  - Independence would not imply rank 48 in any case. Rank is decided by B itself.

## Capacity claims
- Take N := Π_i ||h_i||_1 and let W be any signed sum over valid paths, each term bounded by the product of the coefficient magnitudes.
  - |W| ≤ N is VALID, by the triangle inequality.
  - Equality holds iff every contributing path term has the same phase and every path counted in N is valid. Cancellation lowers |W|. Enlarging the allowed path set can only raise the bound.
- **N vs spectral radius.** For the regular representation, each ρ(|h_i|) has constant row sum, so spr(ρ(|h_i|)) = ||h_i||_1 exactly.
  - So N = Π spr(ρ(|h_i|)). Writing it as ≤ is correct but loose.
  - spr(ρ(|T_combined|)) ≤ Π ||h_i||_1, with possible strict inequality. So "N ≤ spr(|T_combined|)" is FALSE in general.
- **The signed bound |W| ≤ Π spr(ρ(h_i)): VALID only in one case.**
  - It holds when W is a single coefficient of the product h_M⋯h_1. By Fourier inversion, |coeff_g| ≤ max_χ |τ(χ)| ≤ Π_i max_χ |λ_i(χ)| = Π spr(ρ(h_i)).
  - For any other path restriction it is UNSUPPORTED. The signed spr can be much smaller than ||h_i||_1, so it is a different bound from N.
  - It is OPEN until W is defined.
- **The M3 / two-node example** (h1 = [0]⁺, h2 = −[0] + [1] + 3[2], W = 0, N = 2) is undefined as stated: the group, the paths, the sign convention and the norm are all missing.
- **NP-completeness:** UNSUPPORTED. There is no reduction.

## Final report
The claim "dense mixing + linear independence ⇒ rank 48" is FALSE. The rank-24 witness stands, so no sign-off.

## OPEN
- The physical choice of selectors.
- The definition of W.
- The N/W/capacity link.

## R.1 — EXACT spectrum (symbolic over Q(√35, i, √3); bounded 48-character evaluation) + wording errata

**Method.** λ(χ_pqr) = Σ_c a_c χ(cy), evaluated with ω = 1/2 + i√3/2. Every value simplifies exactly into Q(√35).

**Exact eigenvalues (value: multiplicity).**
- 127 + 39√35: 1 (trivial character)
- 1 − 9√35: 2
- 5 − 9√35: 2
- 23 − 9√35: 1
- −5 − √35: 2
- −3 − √35: 4
- −1 − √35: 24
- 1 − √35: 4
- 3 − √35: 2
- −25 + 7√35: 1
- −23 + 7√35: 2
- −19 + 7√35: 2
- −17 + 7√35: 1

The multiplicities sum to 48. There are 13 distinct values.

**PROOF of no zero eigenvalue.** Each eigenvalue has the form u + v√35 with u, v ∈ ℤ and v ≠ 0. Since √35 is irrational, none of them is 0. So the shifted operator is INVERTIBLE exactly (over every field containing Q(√35)).

**Wording errata to R.**
- Positivity: all 47 active weights are positive. The excluded O2 has weight 0.
- Capacity equality: equality requires all path terms to share one phase and every omitted path term to be zero. It does not literally require every counted path to be valid.
- Signed spectral bound: it is SUFFICIENT for a single coefficient of the product. Other linear functionals are left unspecified. Replace "only case" with this.
