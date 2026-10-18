# ERRATUM: Theorem F, function span 42 = 36 + 6 (2026-10-18)
Affects: Bridge C Consolidated rev2, §3 (Theorem F) and §7.2 (the 60 + 12 split); the Cusp Part ledger (2026-10-17); the ψ_Eis ledger (2026-10-17). Additions only; no earlier file is edited.

## Correction (Cat A, numerical, residuals ≤ 1e-15)
1. The 72-dim P-invariant subspace Fix(P) ⊂ C^140 of label space carries the representation S² = (ST)³ = I. **This part stands.**
2. The 140 lift functions u_{α,β} are linearly dependent. Their values u(w) span a subspace **V ⊂ Fix(P) of dimension 42**, not 72. V is the column span of the 140 × 1495 Fourier coefficient matrix (|Q| ≤ 60). The singular values drop from 17.1 to 1.8e-13, and the rank is the same at |Q| ≤ 25. V and the 98-dim relations kernel are S- and T-invariant.
3. V = V_Eis ⊕ V_cusp with **dim V_Eis = 36** and **dim V_cusp = 6**. Each summand is S- and T-invariant (residuals ≤ 8e-16). **The invariance of the split stands.**
4. The stated "Eisenstein rows rank 60, cusp rows rank 12 in the 72" came from projecting label rows onto Fix(P) and taking ranks. That depends on the coordinates. Those row spans are not S-invariant (residual 0.2–0.4) and are not function spaces. **Withdrawn.**
5. Cusp count: 24 non-σ-invariant characters form 12 σ-pairs. That gives 12 distinct dihedral Maass forms, all occurring. They occur only in 6 fixed linear combinations, so the cusp dimension is 6. Any "12-dim cusp part" statement is replaced by "12 forms, 6-dim realised span".

## Open (not claimed)
- Whether the 30-dim complement of V in Fix(P) is realised by any functions. The positive-frequency partners f span the same 42 (Cat A), so they do not realise it.
- What structure produces the 6 cusp combinations.

Evidence: S_Spectrum_2026-10-18/ (split_V.*, cusp_count.*, fpart_rank.*).
