# PROOF_LAMBDA22 — invariants, projections and a helical action for Λ_22 ∈ {ℤ^22, D_22} (2026-10-31)
Label: lattice choice **invented pending Owner choice**; "helical" meaning **invented pending Owner choice / invented pending mathematical proof**. Mathematical statements below are marked PROVED / PARTIAL / NF-WHY. REPORTS ONLY; No RECS; no certification language. tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` NOT touched. First-prove authority for Λ_22 granted by Owner. Inputs: LEAD_PI_LAMBDA22.md, THEOREMS.md (Lemma L2a), PROOF_22_TO_13_AND_WILSON.md, DEFINITIONS.md. Script: `scripts/verify_lambda22.py`.

Notation. ℤ^22 ⊂ R^22 standard inner product. D_22 = {x ∈ ℤ^22 : Σx_i ≡ 0 mod 2}. Write x = (x', y), x' ∈ R^13 (coords 1..13), y ∈ R^9 (coords 14..22). From L2a: F = 13×13 real-DFT matrix (rows u_0, c_k, s_k, k=1..6) is orthogonal; Π_helix = [F | 0] (13×22); P = Π_helix^T Π_helix; Π_c = [I_13 | 0] (coordinate projection).

## (i) Basic invariants — PROVED
1. ℤ^22: Gram (standard basis) = I_22, det = 1 ⇒ unimodular. e_1·e_1 = 1 odd ⇒ odd lattice. Minimal norm 1 (any nonzero integer vector has Σx_i² ≥ 1), attained by ±e_i: 44 minimal vectors.
2. D_22: index 2 in ℤ^22 (kernel of the surjection ℤ^22 → ℤ/2, x ↦ Σx_i mod 2). Hence det D_22 = [ℤ^22 : D_22]² · det ℤ^22 = 4. Explicit basis b_1 = e_1+e_2, b_i = e_i − e_{i−1} (i=2..22) has Gram det 4 (script). det ≠ 1 ⇒ **D_22 is not unimodular**; discriminant group D_22^*/D_22 has order 4 (it is ℤ/2×ℤ/2 since 22 is even — standard, Conway–Sloane SPLAG Ch. 4 §7.1; not needed below).
3. D_22 is even: x·x = Σx_i² ≡ Σx_i ≡ 0 mod 2. Minimal norm 2: nonzero even-sum integer vector cannot have norm 1 (that is ±e_i, odd sum); ±e_i±e_j attain 2; there are 4·C(22,2) = 924 of them.

## (ii) No even unimodular lattice in dimension 22 — PROVED (by citation of a standard theorem)
Theorem (standard). If L is a positive-definite even unimodular lattice of rank n, then n ≡ 0 mod 8. More generally for an indefinite or definite even unimodular ℤ-lattice, signature ≡ 0 mod 8.
Sources: J.-P. Serre, *A Course in Arithmetic*, GTM 7, Ch. V, §2 (Theorem 2 and its corollary: the signature of an even unimodular form is ≡ 0 mod 8); Milnor–Husemoller, *Symmetric Bilinear Forms*, Ch. II §5 (Theorem 5.1 / Cor. 5.2: signature of an even unimodular lattice ≡ 0 mod 8). Proof idea (Serre): a characteristic vector w (x·x ≡ x·w mod 2 ∀x) satisfies w·w ≡ σ mod 8 (van der Blij), and for even L, w = 0 is characteristic, so σ ≡ 0 mod 8. [Exact theorem numbering in Milnor–Husemoller should be checked against the edition at hand; the statement is not in doubt.]
Corollary: 22 ≢ 0 mod 8 ⇒ no even unimodular lattice in rank 22. Consistent with (i): ℤ^22 is unimodular but odd; D_22 is even but det 4. So the Owner phrase "unimodular root lattice" in dim 22 cannot mean an even unimodular one; any root lattice of rank 22 containing only norm-2 roots and unimodular would be even unimodular — impossible. Hence no rank-22 root lattice is unimodular (PROVED).

## (iii) Images under Π_c, Π_helix, P — discrete, not dense — PROVED
Key fact: every row of Π_helix (equivalently im P) is supported on coordinates 1..13, and span{u_0,c_k,s_k} = R^13 × {0} = span{e_1..e_13} (L2a caveat). Therefore P = diag(I_13, 0_9) **exactly** — a rational (indeed coordinate) projector, even though the basis vectors have entries in ℚ(√13, cos 2π/13, sin 2π/13). Proof: P is the orthogonal projector onto its image; the image is span{e_1..e_13}; the orthogonal projector onto a subspace is unique. (Numerically max|P − diag(I_13,0)| ≈ 1e-15.)

Lemma A. Π_c(ℤ^22) = ℤ^13 and Π_c(D_22) = ℤ^13. Proof: ⊆ trivial. For ⊇ on D_22: given a ∈ ℤ^13, take x = (a, (Σa_i mod 2), 0,…,0) ∈ D_22; Π_c x = a. ∎ (Remark: Π_c restricted to D_22 has kernel {(0,y): Σy even} = D_9; it is *not* injective, but the image is the full ℤ^13, not a D-type lattice. A D_13 image arises only if one restricts to D_22 ∩ (R^13×0).)
Lemma B. P(ℤ^22) = P(D_22) = ℤ^13 × {0}: discrete lattice of det 1 in im P ≅ R^13. Proof: P = diag(I_13,0) and Lemma A. ∎
Lemma C. Π_helix(Λ) = F·Π_c(Λ) = Fℤ^13 for Λ = ℤ^22 and Λ = D_22. Since F is orthogonal (L2a), Fℤ^13 is a lattice in R^13 isometric to ℤ^13: discrete, det 1, odd unimodular, minimal norm 1. ∎ (Π_helix = F Π_c since Π_helix = [F|0].)
So for the **actual** Π of L2a, the image is **discrete in all cases** — the irrationality of the Fourier entries is irrelevant because they only rotate inside a rational coordinate subspace. PROVED.

Contrast (when density does occur) — PROVED. General criterion (standard): for an orthogonal projector Q onto a subspace W ⊂ R^n, Q(ℤ^n) is discrete iff W^⊥ ∩ ℤ^n has rank n − dim W (i.e. ker Q is a rational subspace); equivalently iff W is rational. Sketch: Q(ℤ^n) ≅ ℤ^n / (ℤ^n ∩ ker Q) as a group; if ker Q is rational this quotient is free of rank dim W and Q(ℤ^n) is a lattice in W (it is the dual-type projection lattice); if not, the rank of Q(ℤ^n) exceeds dim W, and a finitely generated subgroup of R^d of rank > d containing a spanning set is not discrete (a discrete subgroup of R^d has rank ≤ d), and its closure contains a nontrivial subspace. Concrete example: n=2, W = R·(1,√2): Q(a,b) = ((a+b√2)/3)(1,√2), and {a+b√2} is dense in R (rank 2 subgroup of R, Kronecker) — script shows gaps < 0.0021 mod 1 for |a|,|b| ≤ 300. A 22→13 analogue: any Π whose rows mix coordinates 14..22 with irrational weights relative to 1..13 (e.g. row v_1 = (e_1+√2 e_14)/√3) gives a non-discrete image. None of these is the L2a Π.

## (iv) Helical action — definition invented pending Owner choice; invariance PROVED
Definition H (invented pending Owner choice). Fix A ∈ GL_9(R) with A^13 = I. The 13-fold screw σ_A acts on R^22 by σ_A(x', y) = (S x', A y), S = cyclic shift (Sx')_n = x'_{n−1 mod 13}. A lattice Λ is *helical* iff σ_A Λ = Λ. Default: A = I_9 (the 9 extra coordinates are "axial", fixed). Other natural choice: A a permutation matrix of order dividing 13 — on 9 points only the identity, so A permutation ⇒ A = I_9.
Prop H1 — PROVED. ℤ^22 is σ_A-invariant iff A ∈ GL_9(ℤ) (with A^13 = I). Proof: σ_A preserves ℤ^22 iff its matrix diag(S,A) and its inverse are integral iff A, A^{-1} integral. ∎ In particular true for A = I_9.
Prop H2 — PROVED. D_22 is σ_A-invariant iff A ∈ GL_9(ℤ) and every column sum of A is odd. Proof: (⇐) integrality as in H1; parity: Σ(σ_A x) = Σx' + Σ_j c_j y_j ≡ Σx' + Σ y_j ≡ Σx ≡ 0 (c_j = column sums, odd); same for σ_A^{-1} = σ_A^{12}. (⇒) 2e_j, e_1±e_j ∈ D_22 and σ_A e_1 = e_2 ∈ ℤ^22 force σ_A e_j ∈ ℤ^22, so A integral; taking x = e_1 + e_{13+j} ∈ D_22 gives parity 1 + c_j ≡ 0, so c_j odd. ∎ For A = I_9: invariant.
Prop H3 (fixed sublattice, A = I_9) — PROVED. Fix(σ) on R^22 = {(t·1_13, y)}, dim 10. 
 - ℤ^22 ∩ Fix = ℤ·(1_13,0) ⊕ ℤ^9 (since t·1_13 ∈ ℤ^13 iff t ∈ ℤ); Gram diag(13,1,…,1), det 13, rank 10, odd, minimal norm 1.
 - D_22 ∩ Fix = {(a·1_13, y) : a ∈ ℤ, y ∈ ℤ^9, 13a + Σy ≡ a + Σy ≡ 0 mod 2}: index 2 in the previous, det 4·13 = 52, rank 10. Isometric to the even-sum sublattice of ⟨13⟩ ⊕ ℤ^9 (norm of (a,y) is 13a²+|y|²); minimal norm 2 (e.g. y = e_1+e_2, a=0). It is even: norm 13a²+|y|² ≡ a + Σy_j ≡ 0 mod 2. det 52 verified by script.
Prop H4 — PROVED. Π_helix and P intertwine: Π_helix ∘ σ = (F S F^T) ∘ Π_helix and P σ = σ P (since P = diag(I,0) commutes with diag(S,A)); F S F^T is block-diagonal with 1 and six 2×2 rotations by 2πk/13 (L2a). So the image lattices Fℤ^13 are invariant under the rotation F S F^T — "helical" in the Definition-H sense.
NF-WHY: any statement that Definition H captures tubulin/microtubule helicity (13 protofilaments, 3-start helix seam, 9 extra coordinates' physical meaning) — not a mathematical claim; no definition on disk. Non-identity A with A^13 = I in GL_9(ℤ): exists? Φ_13 has degree 12 > 9, so any integral A with A^13 = I has only eigenvalue 1, hence (being of finite order, diagonalizable) A = I_9. PROVED: over ℤ (indeed ℚ), A^13 = I on rank 9 forces A = I_9. So for integral lattices Definition H reduces uniquely to A = I_9.

## Status table
| Claim | Status |
|---|---|
| det ℤ^22 = 1, odd unimodular, min norm 1 | PROVED |
| det D_22 = 4, even, not unimodular, min norm 2 (924 roots) | PROVED |
| No even unimodular lattice in dim 22 (Serre GTM 7 Ch. V §2; Milnor–Husemoller Ch. II §5) | PROVED (by citation; idea sketched) |
| No unimodular rank-22 root lattice | PROVED |
| P = diag(I_13,0) exactly; P(Λ) = ℤ^13×0 for both Λ | PROVED |
| Π_c(ℤ^22) = Π_c(D_22) = ℤ^13 | PROVED |
| Π_helix(Λ) = Fℤ^13 discrete, det 1, both Λ | PROVED |
| Rationality criterion; density for irrational subspaces (example) | PROVED (standard) |
| Helical invariance: ℤ^22 iff A∈GL_9(ℤ); D_22 iff also odd column sums; A^13=I integral ⇒ A=I | PROVED |
| Fixed sublattices: det 13 (ℤ^22), det 52 even (D_22), rank 10 | PROVED |
| Λ_22 choice; meaning of "helical"; any physics | invented pending Owner choice / NF-WHY |
