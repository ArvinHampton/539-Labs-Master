# PROOF — Hankel positivity replaces the "det(H) ≠ 0 eliminates ghosts" claim

## Correction of the PDF claim. Status of PDF claim: FALSE as stated
"det(H) ≠ 0 eliminates negative-norm ghosts" is false: non-singularity says nothing about sign of eigenvalues.

Counterexample (1 line): moments (m_0,m_1,m_2) = (1,2,1), H = [[1,2],[2,1]], det H = −3 ≠ 0, eigenvalues 3 and −1; v = (1,−1) gives vᵀHv = −2 < 0 (a "negative-norm" direction).

## Theorem H1 (necessity of PSD). Status: PROVED
If m_k = ∫ x^k dμ(x) for a positive Borel measure μ on ℝ with finite moments, then every Hankel H_N = (m_{j+k})_{j,k=0..N} is positive semidefinite.
Proof: for v ∈ ℝ^{N+1}, vᵀH_N v = Σ_{j,k} v_j v_k ∫x^{j+k}dμ = ∫ (Σ_j v_j x^j)² dμ ≥ 0. ∎
Stieltjes variant (supp μ ⊆ [0,∞)): additionally the shifted Hankel (m_{j+k+1}) ⪰ 0, same proof with weight x ≥ 0. PROVED.

## Theorem H2 (Hamburger/Stieltjes converse). Status: CITED (not reproved)
A real sequence is a Hamburger moment sequence iff all H_N ⪰ 0 (with the standard positive-definite/flat-extension refinements). Refs: Akhiezer, *The Classical Moment Problem* (1965); Schmüdgen, *The Moment Problem* (2017).

## Note on the minors test. Status: PROVED
PSD ⇔ **all principal** minors ≥ 0 — leading principal minors ≥ 0 is NOT sufficient: [[0,0],[0,−1]] has leading minors 0, 0 but eigenvalue −1. (Leading minors > 0 strictly ⇔ positive definite, Sylvester.) Use all principal minors or eigenvalues.

## EFT link. Status: CITED framework; application invented pending mathematical proof / ABSENT
In the positivity-bounds literature (Adams–Arkani-Hamed–Dubovsky–Nicolis–Rattazzi 2006; Bellazzini et al. 2020 "Positive moments for scattering amplitudes"; Arkani-Hamed–Huang–Huang 2021 "EFThedron"; Remmen & Trebat-Leder / Caron-Huot–Van Duong 2021) unitarity + analyticity + Froissart-type boundedness write forward-limit Wilson coefficients g_n as moments of a positive spectral density, hence their Hankel matrices are PSD (Theorem H1 applied). That is the correct replacement for the PDF's ghost claim.
- Wilson coefficients g_2, g_3, g_4 of THIS pipeline: **ABSENT** — no amplitude, no Mellin–Barnes kernel, no residues are given in the PDF; nothing was computed here. Any statement "g_2 > 0 hence ghosts eliminated" is invented pending mathematical proof.
- Also: Hankel positivity is a consistency (necessary) condition on coefficients; it does not by itself prove absence of ghosts in a specified theory.
