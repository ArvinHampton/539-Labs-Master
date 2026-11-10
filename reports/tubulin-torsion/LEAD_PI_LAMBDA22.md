# LEAD_PI_LAMBDA22 — replacing the false Π and giving Λ_22 explicitly (Owner t63u, 2026-10-31)
Label: invented pending mathematical proof (applies to the choices/readings). The lemmas marked PROVED are proved here. REPORTS ONLY; No RECS; No CERT. tip LOCK 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 tip_touched NO. Kerr BLOCKED (see LEAD_KERR_STATUS.md). Does not load NP-hardness: Thm A/B already proved independently.

## A) Orthogonal projector of rank 13 — PROVED
Let v_1..v_13 ∈ R^22 be orthonormal (v_i^T v_j = δ_ij), e.g. the standard e_1..e_13. Set P = Σ_m v_m v_m^T.
- P^T = Σ (v_m v_m^T)^T = P.
- P² = Σ_{m,l} v_m (v_m^T v_l) v_l^T = Σ_m v_m v_m^T = P.
- P v_l = v_l, so the v's lie in im P and im P ⊂ span{v_m}. They are linearly independent: if Σ a_m v_m = 0, taking the inner product with v_l gives a_l = 0. So rank P = 13. (Also tr P = Σ‖v_m‖² = 13.)
- Gram G = [v_i^T v_j] = I_13, so det G = 1.
Existence: e_1..e_13 work, so a rank-13 orthogonal projector on R^22 exists. PROVED.

## B) Coordinate map Π_coord — PROVED
Π_coord = the 13×22 matrix with rows v_m^T. Then (Π_coord Π_coord^T)_{ij} = v_i^T v_j = δ_ij, so Π_coord Π_coord^T = I_13 and det = 1 ≠ 0. rank Π_coord = 13 means Π_coord is surjective onto R^13. Π_coord^T Π_coord = P (from A), and Π_coord is a co-isometry (partial isometry).
Corollary (PROVED): for any 22×22 G_22 of rank 22, Π_coord G_22 has rank 13, so det(Π_coord G_22 (Π_coord G_22)^T) > 0.
Contrast: the Owner's t60u matrix Π_{mn} ∝ cos(2πmn/13) uses only cosines. Row m equals row 13−m, so rank is 8 and det(ΠΠ^T)=0 (PROOF_22_TO_13_AND_WILSON.md). The fix is to put sines with cosines and normalize, as in C.

## C) Helical (13-cycle) flavor — construction PROVED; "helical" meaning invent-pending
Fix the coordinates 1..13 of R^22 as a 13-cycle, index n = 0..12, and set coordinates 14..22 to zero. Define:
- u_0 = (1/√13)(1,…,1)
- c_k(n) = √(2/13) cos(2πkn/13), s_k(n) = √(2/13) sin(2πkn/13), k = 1..6.
That gives 13 vectors, embedded as v_m = (u, 0_9) ∈ R^22.
Orthonormality (PROVED): for integer j ≢ 0 mod 13, Σ_{n=0}^{12} e^{2πijn/13} = 0. Product-to-sum then gives Σ cos·cos = (13/2)δ_kl, Σ sin·sin = (13/2)δ_kl, and Σ cos·sin = 0 for 1 ≤ k,l ≤ 6, because k±l ∈ [−5,12]\{0} is never ≡ 0 mod 13 unless k=l in the k−l term. The constant mode is orthogonal to all of them. So by B, Π_helix Π_helix^T = I_13 and rank = 13. Numerical check: max|ΠΠ^T−I| ≈ 1e-15, det = 1.
Shift invariance (PROVED): with S the cyclic shift on coordinates 1..13 (identity on 14..22), S c_k = cos(a)c_k ∓ sin(a)s_k (and the same for s_k), a = 2πk/13, and S u_0 = u_0. So the span is S-invariant.
Honest caveat: that span equals span{e_1..e_13}. The "helical" content is only the choice of basis (a real DFT), not a new subspace. Any physical/helical reading is invented pending mathematical proof.

## D) Λ_22 — choice invent-pending; lattice facts PROVED/standard
- Default reading: Λ_22 = ℤ^22 with the standard basis. Gram = I_22, det 1, unimodular, odd (e_1·e_1 = 1).
- FLAG: an even unimodular positive-definite lattice exists only when dim ≡ 0 mod 8 (standard theorem, Milnor–Husemoller/Serre). 22 ≢ 0 mod 8, so there is NO even unimodular lattice in dim 22. The Owner's "unimodular root lattice" is ambiguous. A root lattice in dim 22 is not unique (A_22, D_22, E_8⊕E_8⊕D_6, E_8⊕A_14, …), and the irreducible root lattices of rank 22 have det > 1 (A_22: 23, D_22: 4). Nothing like E8×E8×X is invented here.
- Alternative: Λ_22 = D_22 = {x ∈ ℤ^22 : Σx_i even}. It is even, det 4, not unimodular.
- The indefinite I_{21,1} is not chosen: nothing on disk calls for a Lorentzian signature.

## E) Projected object Π(ℤ^22)
- Rational rows (Π_coord = first 13 std coordinates): Π(ℤ^22) = ℤ^13, a lattice (PROVED, trivial). This drops the helical claim.
- Helical Π_helix from C: Π_helix = [F | 0] with F a real 13×13 orthogonal matrix. So Π_helix(ℤ^22) = F ℤ^13, the isometric image of ℤ^13. It is a discrete lattice of det 1 in R^13 (PROVED), even though F has entries in ℚ(√13, cos 2π/13, sin 2π/13).
- General warning (PROVED, standard): for a generic 13-dim subspace that is not spanned by integer-coordinate directions, e.g. rows mixing coordinates 14..22 with irrational weights, Π(ℤ^22) can be dense in R^13 (a ℤ-module of rank > 13). For such choices the projected object is only an invent-pending ℤ[ζ_13]-type module, not a discrete lattice. No discrete-lattice claim is made for them.

## Summary
PROVED: A, B (incl. det ΠΠ^T = 1), C orthonormality / rank 13 / shift-invariance, no even unimodular lattice in dim 22, Π(ℤ^22) is a lattice for options E(i)/E(helix-in-13-coords).
Invented pending mathematical proof: the choice Λ_22 = ℤ^22 (or D_22) as the Owner's reading, the 13-cycle coordinate choice, any helical/physical meaning, any Wilson/Kerr use.
