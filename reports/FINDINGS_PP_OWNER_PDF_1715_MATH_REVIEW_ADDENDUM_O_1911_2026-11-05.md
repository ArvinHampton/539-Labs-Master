# ADDENDUM O — Owner integrated manuscript 1910 (txt 1089 lines, sha e2133c10…; pdf sha 79dc8da3…; No CERT; no .tex/compile)

## How this was checked
- I read the txt source directly. The regression sites were located and read in full: L100–120, L229–236, L356–420, L458–505, L670–875 and L885–935.
- The pdf renders the LaTeX source itself. It shows broken underscores and line breaks (`\mathcal{L}0`, `x{i-1}`, `#\left{`, stray `●`). It is not a compiled manuscript.
- Rendering problems are kept separate from the math below.

## Retained correct
- D with ker D ≅ L0.
- The CRT tuples and the field L = Q(√35, i, √3) (L684).
- The 11-term expansion λ_i (L695–704). All exponents match Addendum N.
- χ(3) = (−1)^a (−i)^b ω^c (L750) is correct.
- η = (−1)^{x+y+z}, the relation τ(χη) = (−1)^M τ(χ), and rank T = 2·#{pairs with τ ≠ 0} (L807–828) are all PROVED.
- K4 retained.
- L871–874 (parity does not govern C0 + C_M T) is correct.

## Regressions and errors
1. **L100–120.** The symmetry condition given is the untwisted a_c = a_{c⁻¹}. It must be the shifted condition a_c = a_{c⁻¹w⁻²}. The counterexample is w = 3 with a_1 = 2 (Addendum K). The degree must also carry σ.
2. **L229–236.** "Capacity cycles imply obstruction/topology" and an automatic torus are NOT established, and the torus claim is false. With all 48 weights positive the graph is K48, with b1 = 1081. Backtracks are not homology.
3. **L376–413.**
   - The proof says "full ROW injectivity". It must be full COLUMN rank n0.
   - The "iff" needs the converse: if rank < n0, a nonzero x0 exists in the kernel.
   - The uniqueness proved here is not stability (L420).
4. **L458–505.**
   - The claims of capacity collapse and kernel behaviour for ramified and split primes are UNSUPPORTED.
   - They contradict the document's own caveat at L503–505.
   - The claim that inert primes "preserve field extensions" is still unsupported.
5. **Boundary.** The boundary kernel depends on C0 and C_M as well as α.
6. **L722–795, character translation.**
   - This section conflates a ∈ {0,1} with the parity of the η coordinates.
   - Convolution PRESERVES each χ-eigenline. R_3 multiplies it by the phase χ(3) and does not move it to another frequency.
   - J = diag η preserves its own ± eigenspaces (the split and inert classes). It is each T_i that swaps them, since J T_i = −T_i J. In the Fourier picture, J maps the χ-line to the χη-line.
7. **L845, pairing formula: WRONG.**
   - With I = 24a + 6b + c, the floor(I/6) formula fails on 24 of the 48 indices, namely those with b = 1 or 2 (I = 6–17 and 30–41); it is correct for b = 0 and b = 3. For example, I = 6 gives 21, but the true partner is 45.
   - The correct formula is I′ = I + 24 + 12(−1)^⌊I/12⌋ + 3(−1)^⌊I/3⌋ mod 48. I verified this on all 48 indices.
   - The 24 listed pairs (L857–867) are ALL correct. The list disagrees with the printed formula.
8. **L885–931, selectors.**
   - Joint rows γ_k x0(Ω_k) + μ_k x_M(Λ_k) = 0 express cancellation, not separate zeros.
   - Use the split form S0/S_M: B = [S0; S_M T].
   - "Fourier sums align with row ranks" is NOT established. Witness: C0 = I, C_M = −I, T = R47 R3 = I gives B = 0.

## OPEN
- The physical choice of α, Ω and Λ.
- The N/W/capacity link.
- The physical meaning of the boundary rank.

No integration and no master write were done.

## O.1 errata (7:12 PM CST, per Physicist's review)
Three narrow corrections were made in the text above:
- the range of indices where the formula fails;
- J preserves its eigenspaces, and T_i swaps them;
- the provenance wording was dropped.
No new research.
