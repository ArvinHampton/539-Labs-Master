# ADDENDUM H — Owner 18:43 cascade (same review; exact linear algebra by hand; relay-based; No CERT; no .tex)
## Block-diagonal A = diag(T1..TM): F=⊕_{i=1}^M L_{i-1} → B=⊕_{i=1}^M L_i
- PROVED: dimF − dimB = Σd_{i-1} − Σd_i = d0 − dM, independent of the T_i.
- PROVED (rank–nullity): dimF − dimB = dim ker A − dim coker A. This is NOT dim coker A.
- Counterexample 1: M=1, L0=L1=K, T1=0. Then dimF−dimB=0, but coker A=1 (and ker=1).
- Counterexample 2: M=2, L_i=K², T1=T2=Q=diag(1,0). Then coker A=2, but the global Q·Q=Q has coker 1. A block-diagonal map treats the transfers as independent and does not encode the ordered composition.
- "dim_K F = exact original N" and "dim_K B = exact original |W|" are DEFINITIONS. A direct sum counts layer occurrences, not whole paths, and gives no complex weight. Equivalence with the original N/W is OPEN. Choosing K=ℚ(√35) is a stipulation (not refuted, but it needs a stated equivalence to the original).
- "Block lower-diagonal" is a misnomer: the displayed A is block-DIAGONAL.
## Constructive replacement (PROVED, a new object, not project closure)
- D: ⊕_{i=0}^M L_i → ⊕_{i=1}^M L_i, D(x0..xM) = (x_i − T_i x_{i-1})_{i=1..M}. Its matrix is block bidiagonal [−T_i  I].
- D is surjective by forward recursion (x_i = y_i + T_i x_{i-1}), so coker D = 0.
- ker D = the compatible trajectories x_i = T_i x_{i-1}, and ker D ≅ L0 (via x0). Check: dim ker D = d0 = dim source − dim target.
- Endpoint evaluation on ker D gives x_M = T_M⋯T_1 x0, which recovers the global product.
- This is NOT the original free path space unless proved.
## Symmetric Cayley C^i_xy = φ_i(x⁻¹y)
- Needed hypotheses:
  - G_i = U140 with w_i a unit.
  - φ_i(g) = a_{i, g·w_i⁻¹}.
  - φ symmetric ⇔ a_{i,c} = a_{i, c⁻¹w_i⁻²}.
  - Positivity requires a chosen real embedding of K; membership in K does not give it.
  - Connectivity ⇔ supp φ generates G. Symmetry alone gives neither positivity nor connectivity.
- Uniform degree = Σ_{g≠e} φ(g) = Σ_c a_{i,c} − a_{i,w_i⁻¹}. This holds only under the above (not by "matching coefficients").
- Notation: use n_i (dimension) and δ_i (degree); currently d_i is overloaded.
## K4 appendix / P
- Agrees with Addendum G: B factor, spectrum {0,6,8,10}, triangle basis.
- P is the same 3×6 matrix with rank 3; the physical routing is stipulated.
## Requested draft / 11 inert-prime entries
No exact list of 11 entries or representation exists on record. I did not invent one. The inert classes mod 140 are listed in Addendum C.
Original N/W/capacity: OPEN.
