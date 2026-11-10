# ADDENDUM P — Owner t4114 proposed resolutions (relay-based; no source file; bounded; No CERT; no .tex)

All verdicts below follow from earlier exact checks (Addenda J–O) or are elementary. No new computation was done.

1. **Degree.**
   - The proposed D_σ(v) = Σ_i σ(Σ_c a_{c⁻¹w_i⁻²}[c w_i]) is INVALID. Three reasons:
     - σ: F → ℝ is applied to an element of the group algebra, which is not in F.
     - It includes the self-loop.
     - It sums across layers.
   - REPAIR: the per-layer degree is δ_i = Σ_{c ≠ w_i⁻¹} σ(a_{i,c}), and the symmetry condition a_{i,c} = a_{i,c⁻¹w_i⁻²} is VALID.
   - There is no automatic "topological stability."
2. **Fourier.**
   - The claim that each χ-line is preserved is correct.
   - Replacing U140 by a cyclic Z/MZ is INVALID: U140 ≅ C2 × C4 × C6 is not cyclic, so the frequency set is the 48 characters of U140, not a "topological choice."
   - λ_i(χ) = Σ_c a_{i,c} χ(c w_i) holds only for h_i = Σ_c a_{i,c}[c w_i]. That changes the original inert family.
   - The parity theorem then needs η(c w_i) = −1 for every active term.
3. **Pairing Ψ(I) = Π_{k=1}^{24}(⌊I/12⌋Λ_k + Ω_k).**
   - This is NOT an index map, and its symbols are undefined.
   - Counterexample: taking every Ω_k = 1 and every Λ_k = 0 gives Ψ ≡ 1.
   - Keep the corrected formula I′ = I + 24 + 12(−1)^⌊I/12⌋ + 3(−1)^⌊I/3⌋ mod 48.
4. **Stacked boundary B = [S0; S_M T].**
   - The construction is correct. The claim that stacking guarantees rank 48, or det(B†B) ≠ 0, is FALSE.
   - Counterexample: S0 = S_M = e1^T and T = I (realized as R47 R3). B then has two identical rows, so rank 1, nullity 47, and the Gram determinant is 0.
   - Stacking removes the cancellation between the two ends, but ker S0 ∩ ker(S_M T) can still be nonzero.
   - REPAIR: the solution is unique iff rank B = 48. Equivalently, det(B*B) ≠ 0 with B* the conjugate transpose over ℂ, or the transpose after a real embedding. This is the standard Gram criterion; it is not guaranteed by the construction.
5. **B HΨ = 0.** Undefined: HΨ needs a defined domain and x0.
6. **Positive N–W capacity.** No inference is possible.
7. **Page 12.** The repair is VALID: column rank n0, plus the converse, plus the statement that uniqueness is not stability. Delete the unsupported topology and splitting text.

## OPEN
- The physical choice of α, Ω and Λ, and the actual rank of B.
- The N/W/capacity link.
