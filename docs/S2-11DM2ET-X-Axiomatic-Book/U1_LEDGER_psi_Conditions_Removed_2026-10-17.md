U1-LEDGER-psi-CONDITIONS-REMOVED
psi cocycle: conditions C1 and C2 discharged; full 140-label family; all rows
Category A. Remaining inputs are listed in section 0 (standard analytic facts and PARI). Category B items are in CatB_Notes_psi_Conditions_Removed_2026-10-17.md.
2026-10-17

PURE MATH. 539 is a COUNT. Residual is not Resonant. CORE_FREEZE untouched. No locks altered.
No HQCC termination claim. Twin Prime and RH unclaimed.

Parent tip. c86008940539e5d186049cbeea69d1f400a958c3 (main).
Source (verbatim copy). psi_Conditions_Removed_2026-10-17/2026-10-17-psi-Conditions-Removed.md with scripts and outputs in the same folder (the report's "2026-10-17-psi-conditions/" refers to that folder). S_matrix.npy, T_matrix.npy, phi_rows.npy not included (binary).
Builds on. U1_LEDGER_psi_Cocycle_LewisZagier_2026-10-17.md (7519051), conditions C1-C5 in its section 0. Corrections to its component-count wording: ERRATUM_psi_Cocycle_Component_Count_2026-10-17.md.
Notation. L = Z^2, Gram A = [[2,7],[7,7]], det A = -35, L' = A^{-1}Z^2, |L'/L| = 35; a = (7/10, -1/5); gamma, eps, K as in the P_s and psi ledgers. T_n(w) = sqrt(y) K_0(2 pi |n| y) e(nx); R_z(w) = Im w/((w-z)(wbar-z)); [u,v] = u_w v dw + u v_wbar dwbar.


0. Status of the psi ledger's conditions

C1 (Green-form constant C = -pi/2, previously 30-digit quadrature only): DISCHARGED by the written proof in section 1.
C2 (S-law u_L(-1/w) = u_R(w)/sqrt35, previously numerical to 6e-11): DISCHARGED by the Poisson-summation proof in section 2, which is independent of Borcherds.
C3 (Borcherds 1998 Thm 4.1): no longer needed for the S-law.
C4 (Lewis-Zagier 2001): no longer needed; the section 1 proof does not depend on it (cited for context).
REMAINING (not written out; standard):
R1 = C5. Uniform sectorial Euler-Maclaurin radial expansions (Re t > 0), so non-tangential boundary values are allowed.
R2. Interchange of the Fourier sum and the Green-form integral (K_0 series uniformly convergent on y >= 1): not written out.
R3. PARI (cypari2 2.2.4): the class group is certified (bnfcertify = 1); the ray-class routines are standard algorithms NOT independently certified. Affects section 5 only.


1. Green-form lemma, written proof (Cat A)

For z in H, F_n(z) := int_z^{z+i inf} [T_n, R_z^{1/2}] (vertical ray). Then F_n(z) = -(pi/2) e(nz) for n > 0; F_n = 0 for n < 0; int_z^{z+i inf}[sqrt(y), R_z^{1/2}] = 1/2.
Proof.
(i) Closedness: Delta_w R_z^{1/2} = (1/4) R_z^{1/2}; d_wbar R_z = i/(2(wbar-z)^2); d[u,v] = (u_{w wbar} v - u v_{w wbar}) dwbar ^ dw, zero for equal eigenvalues (sympy, all residuals 0; lemma_symbolic.txt).
(ii) Holomorphy: R_z is holomorphic in z; the endpoint d_zbar term -T_n(z) v_wbar(z) vanishes since R^{-1/2} -> 0 like |w-z|^{1/2}; convergence uniform at both ends. So F_n is holomorphic on H.
(iii) Translation covariance: F_n(z + xi) = e(n xi) F_n(z), so F_n = C_n e(nz).
(iv) n < 0: F_n bounded as y -> infinity while |e(nz)| grows, so C_n = 0.
(v) n > 0, Laplace's method as y -> infinity: with a = 2 pi n, K_nu(X) = sqrt(pi/(2X)) e^{-X}(1 + O(1/X)) (DLMF 10.40.2), the main term tends to (sqrt(pi a)/2) s^{-1/2} e^{-as} under a dominating bound, integral pi/2; the other terms are O(y^{-1/2}). Since F_n e^{ay}/e(nx) = C_n for every y, C_n = -pi/2.
(vi) n = 0: (y/2) int s^{-1/2}(2y+s)^{-3/2} ds = (1/4) B(1/2,1) = 1/2.
The earlier 30-digit quadrature is now a cross-check only.


2. S-law and T-law, derived (Cat A)

Poisson summation at a fixed majorant: Theta_{alpha,beta}(-1/tau) = |tau| (e(B(alpha,beta))/sqrt35) sum_{p in L'/Z^2} Theta_{p-beta, alpha}(tau) (Gaussian transform factor det(M/i)^{-1/2} = |tau|/sqrt35).
Integrating over the geodesic of <gamma^k> (k = 2) and multiplying by sqrt(y):
  u_{alpha,beta}(-1/w) = (e(B(alpha,beta))/sqrt35) sum_p u_{p-beta, alpha}(w).
Constant term sqrt(y) log eps exactly when alpha in Z^2. For (alpha,beta) = (a,0), with u_{p,a} = u_{-p,-a}, this is u_R/sqrt35: the old S-law (C2) is proved.
Reductions: u_{alpha+n,beta} = u_{alpha,beta} (n in Z^2); u_{alpha,beta+mu} = e(B(alpha,mu)) u_{alpha,beta} (mu in L'); u_{-alpha,-beta} = u_{alpha,beta}.
T-law (odd lattice): Q is not integral on Z^2, so Z^2 is ODD. Characteristic vector w_c = A^{-1}(0,1/2) = (1/10, -1/35), e(Q(n)) = e(B(n,w_c)), w_c = a mod L'.
  u_{alpha,beta}(w+1) = e(-Q(alpha) - B(alpha,w_c)) u_{alpha, alpha+beta+w_c}(w).
The naive even-lattice T-law fails by O(1).


3. The 140-label family and the 72-dimensional PSL2(Z) representation (Cat A)

Labels: alpha in ({0,a} + L')/Z^2 (70 classes), beta in {0,-a}: 140 labels (labels.txt).
S matrix: every row has exactly 35 entries of modulus 1/sqrt35; unitary. T matrix: monomial, unitary.
S^2 = P exactly, P the label map (alpha,beta) -> (-alpha,-beta). On the P-invariant subspace (dimension 72): S^2 = I and (ST)^3 = I.
So the family carries a 72-dimensional representation of PSL2(Z). The earlier 36 components are not closed under T.
Numerical verification of the derived formulas (slaw_check.txt, dump_matrices.txt): S unitary 6.7e-16, T unitary 4.4e-16, S^2 = P 6.1e-16; on the P-invariant subspace |S^2 - I| 4.2e-16, |(ST)^3 - I| 1.3e-15; applied to u, |(ST)^3 u - u| 3.3e-15.


4. All 140 rows (Cat A: derived formulas, verified numerically)

Phi(x) := kappa(-1/x) - |x| S kappa(x), kappa the vector of exact radial constant terms; row (a,0) reproduces the old psi (Phi_(a,0)(1)/2 = 0.0068839937604 - 0.0382597122170 i).
Closed form for every row u, with U the S-row combination and J_v(z) = int_i^{i inf}[v, R_z^{1/2}]:
  Phi_u(x) = -(2/pi) [ |x| a_0(U)/2 - a_0(u)/2 - |x| J_U(x) + J_u(-1/x) ].
Three-term cocycle relation: Phi(z) = T Phi(z/(z+1)) + (z/(z+1)) T S T Phi(z+1).
Numerical verification, all 140 rows (slaw_check.txt, rows_check.txt; x in {1, 1/3, 2, 3/5, 7/4, -1, -2/3}; three points y ~ 1 for u):
- S-law |u(-1/w) - S u(w)| <= 1.2e-15; T-law |u(w+1) - T u(w)| <= 7e-16; |P u - u| <= 5.6e-16.
- Singular parts cancel 9.0e-16; no t^-1/2 terms 5.7e-16; P kappa = kappa 5.3e-15.
- Closed form vs exact Bernoulli sums 2.3e-14.
- Three-term relation at z in {1, 1/2, 2/3, 3/2}: 7.0e-15.
Consequence (given R1, R2): every row of the S-cocycle is real-analytic on R \ {0}; the full 72-dimensional E/f-vector is a vector-valued quantum modular form of weight 1 for the factor |cx+d|.


5. Zeta value and Eisenstein/cusp content

zeta(-1,K) = 29/60 confirmed (Cat A, exact; shintani_check.txt): 5 Shintani cones [r, gamma r), r = (1,0), (1,1), (1,2), (2,1), (3,2), |det| = 2, 23, 58, 43, 130, each split into |det| classes; each gives zero t^{-+1/2} terms, zeta_E(0) = 1/10, zeta_E(-1) = 29/1200, so zeta(0,K) = 1/10, zeta(-1,K) = 29/60.
PARI data (R3; rayclass_pari.txt): Cl = Z/2, Cl+ = (Z/2)^2, fundamental unit 6 + sqrt35, bnfcertify = 1; ray class group mod p2 p5 inf1 inf2 = Z/8 x Z/2 (order 16); sigma: g1 -> 5 g1, g2 -> 4 g1 + g2; primes over 13 in [1,0], [5,0]; p7 in [1,1].
Positive frequencies (f = 2E) are pure Eisenstein (Cat A CONDITIONAL on the PARI ray-class group): sigma-invariant characters (j even, 8 of them) are genus characters (Kronecker-Weber), so their thetas are Eisenstein; sigma-non-invariant pairs cancel in theta_K (coefficient proportional to 1 + (-1)^j = 0 for odd j). Numerical support: r_K(n) = h(n mod 280) sum_{d|n} (35/d), h in {0, 1/2}, for n < 60000 coprime to 70 (split_test.txt).
Negative frequencies carry a NONZERO dihedral cusp part (existence Cat A CONDITIONAL on the PARI ray-class group): negative-norm vectors of u_L lie in the sigma-fixed class [1,1] (starting at norm 7, p7), whose coefficients 2 chi-bar([1,1]) do not vanish for odd j; numerically r''(p) in {0,2} is not periodic mod 280 or 560 (split_neg.txt). Hence u_L and u_R = sqrt35 u_L o S have nonzero cusp content.
The explicit split and eigenform identification are Cat B (notes B1).


6. Extends

The psi ledger (7519051) is upgraded: conditions C1 and C2 discharged, C3 and C4 not needed for the S-law; its Cat B note B1 (other rows) is closed (all 140 rows checked) and B4 (independent check of zeta(-1,K)) is closed. The quantum-modularity statement now rests only on R1 and R2 (R3 enters only section 5). No older file edited.


7. Not claimed

The cusp eigenbasis, infinity types, or the split psi = psi_Eis + psi_cusp. Anything for s = 8, 11. Certification of PARI's ray-class routines. No HQCC, TPC or RH statement.

Hygiene. Pure copy-and-create; no existing file modified or renamed; no locks altered. Cat A only here. CORE_FREEZE untouched.
