Matrix Analogues s=5, s=8, s=11 Residues and Twin Pairs under Pack+(S)
2026-08-26

Packaging provenance Pack+(S). Flux provenance mandatory. CORE_FREEZE holds. Category A discrete only. Continuum claims stay Category B. Classical Twin Prime Conjecture remains open and unclaimed.

(The phrase twin pairs means pairs of values of the quadratic form that differ by 2. No claim is made about classical primes.)

1. Common structure

For each integer s the matrix

M_s = [[2, s], [s, s]]

has determinant -s(s-2). The associated homogeneous quadratic (normalised so the leading term is n^{2}) is

Q_hom(n, k) = n^{2} + s n k + (s/2) k^{2}.

The polarisation identity holds formally in every case. Signature is (1,1) for every s examined (eigenvalues of opposite sign).

An affine version is obtained by adding the linear term -(s/2) k, exactly as for the locked s=7 path quadratic.

2. Residue patterns and twin pairs

s=7 (packaging value, locked case)
Residues of the form mod 7: {0, 1, 2, 4}.
Twin classes (0,2) and (2,4) both lie in the set. Twin pairs exist with positive density. Paths 2 and 4 closed under Pack+(S).

s=11 (packaging value)
Residues of the affine form mod 11: {0, 1, 3, 4, 5, 9}.
Twin pairs exist and are abundant (hundreds observed in moderate lattice boxes). No modular obstruction. Consistent with packaging arithmetic PW(7,11;3^5).

s=5
Residues of the form mod 5: {0, 1, 4}.
Twin pairs exist and are numerous. No modular obstruction. s=5 is not a packaging value for the residual series g_s or Bridge Series C.

s=8
Residues of the homogeneous form mod 8: {0, 1, 4, 5}.
Residues of the affine form mod 8: {0, 1, 4}.
No pair of residues in either set differs by 2 mod 8. Twin pairs are modularly forbidden. Detailed calculation:

Q_hom(n,k) ≡ n^{2} + 4 k^{2} (mod 8)
because 8 n k ≡ 0. Squares mod 8 are 0,1,4. 4k^{2} is 0 when k even and 4 when k odd. All combinations yield only {0,1,4,5}. The required partners for difference 2 (2,3,6,7) lie outside the set.

3. Comparison and correlation with packaging

Both packaging values that appear in Packaging–Weyl PW(7,11;3^5) and in the residual series g_s (namely s=7 and s=11) admit twin pairs under their bilinear forms. The non-packaging value s=8 is the one for which twin pairs are modularly obstructed. This is a clean discrete correlation under Pack+(S).

Signature (1,1) is common to all four values, so hyperbolic lattice-point growth is available in every case. Twin-support statements parallel to Paths 2 and 4 arise only when the residue pattern permits difference 2.

4. Status

The s=5, s=8 and s=11 matrix analogues are Category A discrete under Pack+(S). Twin pairs exist for s=5,7,11 and are modularly forbidden for s=8. The obstruction for s=8 is elementary modular arithmetic and is locked. Parallel twin-support theory for s=8 does not arise. The packaging values s=7 and s=11 both support twin pairs, consistent with the residual packaging arithmetic already used for Bridge Series C.

No free parameters appear. No contradiction with the locked s=7 package or with CORE_FREEZE appears. Continuum claims stay Category B. Classical Twin Prime Conjecture remains open and unclaimed.

Status code: MATRIX_ANALOGUES_s5_s8_s11_PACK_S_2026-08-26
