# ADDENDUM Q — Owner t4116 "full rank proof" + coefficient proposal (relay-based; bounded by hand; No CERT; no .tex)

## A. Rank proof — FALSE
**Setup.** S0 = [I24 0], S_M = [0 I24], T = [0 Θ_A; Θ_B 0].

**Exact B.**
- S_M T = [Θ_B 0], so B = [I 0; Θ_B 0].
- Rank 24. Kernel = 0 ⊕ F²⁴.
- Gram matrix B*B = diag(I + Θ_B*Θ_B, 0), so det = 0 for EVERY coefficient choice.
- Step 3 of the proof itself finds B(0,v) = 0. Saying "HΨ removes it" does not repair this. The factor in det Gram = det(I + Θ_B*Θ_B)·det H24 is fabricated.
- Any linear BHΨ with 48 unknowns has rank ≤ 24, so the kernel remains.

**Repairs (conditional).**
- (i) With S_M = [I 0] and the same T: S_M T = [0 Θ_A], so B = diag(I, Θ_A), which has rank 48 iff Θ_A is invertible.
- (ii) With complementary selectors and T = I (realized by the 2-layer product R47·R3): B = I48.

**Caveat on bases.** The χ ↔ χη permutation is J acting in the Fourier basis. It is not diagonal there, and it is not the original convolution. S0, S_M and T must all be written in one coherent basis.

## B. Coefficient proposal on S = {x, y, y², z, z², z³, xy, xz, yz, xy², xz², yz²}
- **Positivity is FALSE:** 2 − √35 < 0 and 5 − √35 < 0.
- **w is unspecified.** Twisted closure a_c = a_{c⁻¹w⁻²} is FALSE in general.
  - Witness: take w = y. Then for c = x, c⁻¹w⁻² = x·y² (x has order 2, y has order 4).
  - But a_x = 1 + √35 while a_{xy²} = 3 + 2√35.
- **Outside S.** The cyclic recursion a_f(c) is undefined on those orbits. Setting the self-loop to 0 overlaps S whenever w⁻¹ ∈ S.
- **Field.** K = Q(√35) is NOT the splitting field; the character values need L = Q(√35, i, √3). The transcendental ξ is unused, and if it were used the coefficients would leave K.
- **Printed λ_pqr = Σ_c σ(a_c)(−1)^p i^q ω^r is WRONG.**
  - It omits the coordinates of c. It factors as A·(−1)^p i^q ω^r, which takes at most 12 distinct values, not 48.
  - Example: frequencies (0,0,0) and (0,2,3) both give A, since i²ω³ = 1.
  - Correct form: λ(χ_pqr) = Σ_c a_c (−1)^{p x_c} i^{q y_c} ω^{r z_c}, with the shift by w if h is defined with [c w].
  - Distinct spectral values ≠ invertibility. Invertibility means no λ is zero.
- **Inert support.** The original inert-support conditions are not specified for the new S.
- **Group presentation.** As written, it lacks commutator relations. Stipulating the abelian isomorphism U140 ≅ C2 × C4 × C6 repairs this.

## Status
Neither a sign-off nor any capacity statement is possible until the structural rank error in A is fixed.

OPEN: the physical α, Ω and Λ, and the N/W/capacity link.
