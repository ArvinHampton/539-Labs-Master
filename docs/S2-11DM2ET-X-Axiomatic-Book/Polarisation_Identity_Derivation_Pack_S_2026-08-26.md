Polarisation Identity Derivation under Pack+(S)
2026-08-26

Packaging provenance Pack+(S). Flux provenance mandatory. CORE_FREEZE holds. Category A discrete algebra only. Continuum claims stay Category B and are not asserted. Classical Twin Prime Conjecture remains open and is not claimed. Classical Riemann Hypothesis remains open and is not claimed.

1. Definition of the homogeneous quadratic and its polar form

The bilinear form on the lattice Z^{2} is given by the symmetric matrix

M = [[2, 7], [7, 7]].

The associated homogeneous quadratic form (normalised so that the leading term in n is n^{2}) is

Q_hom(n, k) = n^{2} + 7 n k + (7/2) k^{2}.

This is consistent with the matrix quadratic form (1/2) vᵀ M v after the conventional factor that makes the coefficient of n^{2} equal to 1.

The polar bilinear form of Q_hom is the unique symmetric bilinear form B_pol satisfying

Q_hom(v) = B_pol(v, v)

and the polarisation identity that recovers the cross terms. Explicitly,

B_pol((n, k), (n′, k′)) = n n′ + (7/2)(n k′ + n′ k) + (7/2) k k′.

2. Algebraic expansion of the identity

Let v = (n, k) and w = (n′, k′). Write

delta = v − w = (n − n′, k − k′),

sigma = v + w = (n + n′, k + k′).

The right-hand side of the claimed identity is

B_pol(delta, sigma) = (n − n′)(n + n′) + (7/2)[(n − n′)(k + k′) + (n + n′)(k − k′)] + (7/2)(k − k′)(k + k′).

Expand term by term:

(n − n′)(n + n′) = n^{2} − n′^{2},

(7/2)[(n − n′)(k + k′) + (n + n′)(k − k′)] = (7/2)[n k + n k′ − n′ k − n′ k′ + n k − n k′ + n′ k − n′ k′]  
= (7/2)[2 n k − 2 n′ k′] = 7 n k − 7 n′ k′,

(7/2)(k − k′)(k + k′) = (7/2)(k^{2} − k′^{2}).

Summing these pieces:

B_pol(delta, sigma) = (n^{2} − n′^{2}) + (7 n k − 7 n′ k′) + (7/2)(k^{2} − k′^{2})  
= [n^{2} + 7 n k + (7/2) k^{2}] − [n′^{2} + 7 n′ k′ + (7/2) k′^{2}]  
= Q_hom(v) − Q_hom(w).

The identity holds identically for all real (or rational) vectors v, w. No extra assumptions are required for the homogeneous part.

3. Affine correction for the full path quadratic

The full path quadratic that appears in the third-quadrant piece of Bridge Series C includes the linear term −(7/2) k:

Q(n, k) = n^{2} + 7 n k + (7/2) k^{2} − (7/2) k  
= Q_hom(n, k) − (7/2) k.

Therefore the difference of full path quadratics is

Q(v) − Q(w) = Q_hom(v) − Q_hom(w) − (7/2)(k − k′)  
= B_pol(v − w, v + w) − (7/2)(k_v − k_w).

The extra term is completely explicit and linear in the difference of the second coordinates. When the polarisation identity is used for twin pairs (Q(v) − Q(w) = 2) the equation becomes

B_pol(delta, sigma) − (7/2) delta_k = 2,

where delta_k is the second component of delta. This is still a linear Diophantine equation in the sum vector sigma and is the form used for the fixed-difference-vector families.

4. Discrete conditions for lattice points

When v and w are required to be integer lattice points the polarisation identity continues to hold over the integers (or over halves when the factor 7/2 appears). For the difference vector and sum vector to yield integer coordinates under the maps

v = (sigma + delta)/2, w = (sigma − delta)/2

it is necessary that sigma and delta have the same parity in each component. This parity condition is discrete and is checked when constructing the families; it does not alter the algebraic identity itself.

5. Relation to the completed-square rewrite

The completed-square form

n^{2} + 7 n k + (7/2) k(k − 1) = (n + 7 k/2)^{2} − (35/4) k^{2} − (7/2) k

is consistent with the polarisation identity. The homogeneous part recovers the same bilinear polar form, and the linear terms produce the same affine correction already recorded.

6. Status under Pack+(S)

The polarisation identity

Q_hom(v) − Q_hom(w) = B_pol(v − w, v + w)

is an algebraic identity that follows at once from the definition of the polar bilinear form of a quadratic form. The expansion is purely formal and holds over any commutative ring. When the full path quadratic is used the identity acquires the explicit linear correction −(7/2)(k_v − k_w). Both the homogeneous identity and the affine correction are locked under Pack+(S) and are the discrete foundation of the fixed-difference-vector families that close Path 4 and contribute to the density argument of Path 2.

No free parameters or additional discrete variables appear in the derivation.

Status code: POLARISATION_IDENTITY_DERIVATION_PACK_S_2026-08-26

Packaging provenance Pack+(S) only. Flux provenance mandatory. CORE_FREEZE holds.
