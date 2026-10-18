U1-LEDGER-psi-COCYCLE-LEWISZAGIER
psi, the order-t^0 S-cocycle of the fundamental-domain E-vector: closed form and analyticity
Category A CONDITIONAL. Every Cat A statement below holds subject to the conditions in section 0. Category B items are in CatB_Notes_psi_Cocycle_2026-10-17.md.
2026-10-17

PURE MATH. 539 is a COUNT. Residual is not Resonant. CORE_FREEZE untouched. No locks altered.
No HQCC termination claim. Twin Prime and RH unclaimed.

Parent tip. 72194992ddc71ca68a58ddae907a5a4d83d98e10 (main).
Source (verbatim copy). psi_Cocycle_2026-10-17/2026-10-17-psi-Cocycle.md with scripts and outputs in the same folder (the report's "2026-10-17-psi-cocycle/" refers to that folder). maass_vectors.pkl is not included (binary pickle).
Builds on. U1_LEDGER_P_s_Structure_RayClass_2026-10-17.md (fa44606). Notation as there: Q2 = x^2 + 7xy + (7/2)y^2, a = (7/10, -1/5), gamma = [[-1,-7],[2,13]], eps = 6 + sqrt35, I = log eps/(2 sqrt35), ray class K mod p2 p5 inf1 inf2, F = C0 union rho2 C0 = [e1, gamma e1).
E-vector. E_{alpha,beta}(tau) = sum_{nu in F cap (alpha+Z^2)} e(B(nu,beta)) e(tau Q2(nu)); E_L := E_{a,0}, E_R := sum_p E_{p,-a} (p over the 35 classes of A^{-1}Z^2/Z^2).
psi(x) := kappa_L(-1/x) - (x/sqrt35) sum_p kappa_{p,-a}(x), kappa = t^0 radial coefficient.


0. Conditions (the Cat A statements depend on these)

C1. Green-form constant C = -pi/2: from 30-digit quadrature only (n = 1, 2, 3 at two points z; ratio -1.5707963267949, imaginary parts < 1e-30; lemma_c1.txt). Not derived by hand. The n < 0 value 0 and the n = 0 value 1/2 are derived.
C2. S-law u_L(-1/w) = u_R(w)/sqrt35: checked numerically to 6e-11 at three points (maass_lift.txt; residual attributed to truncation). Not derived symbolically for these coset/character components. T-law u_L(w+1) = e(13/20) u_L(w) exact.
C3. Borcherds, Automorphic forms with singularities on Grassmannians, Invent. Math. 132 (1998), Thm 4.1: statement checked online (Siegel theta of signature (b+,b-) transforms with (c tau+d)^{b+/2}(c taubar+d)^{b-/2} rho_L; here |c tau+d|). Its application to these components is condition C2.
C4. Lewis-Zagier, Period functions for Maass wave forms I, Ann. Math. 153 (2001), arXiv:math/0101270, Ch. II sec. 2: cited (table of contents checked online); A2 is its s = 1/2 case.
C5. Non-tangential validity of the Euler-Maclaurin radial expansions (boundary values): standard; numerical fits consistent; not re-derived.
Context only, not used as proof: Bruggeman-Lewis-Zagier, Mem. AMS 237 (2015) no. 1118.


1. The E-vector is the Lewis-Zagier periodic function of lambda = 1/4 Maass forms (Cat A conditional on C2, C3)

u_L(w) = sqrt(y) sum_{nu in (a+Z^2)/<gamma>} K_0(2 pi |Q2(nu)| y) e(Q2(nu) x)
u_R(w) = sqrt(y) [ log eps + sum_{0 != nu in A^{-1}Z^2/<gamma>} e(B(nu,-a)) K_0(2 pi |Q2(nu)| y) e(Q2(nu) x) ]
Siegel-theta lift (weight (1/2,1/2)) over the closed gamma-geodesic, times sqrt(y). Each term is a Laplace eigenfunction with lambda = 1/4 (s = 1/2), weight 0.
Positive Fourier coefficients: f_{u_L} = 2 E_L, f_{u_R} = 2 E_R (automorph -rho1 maps S+ to S-, fixes a mod Z^2, preserves phases, permutes the p; numerically identical for norms <= 25, deviations 0 and 5e-14).
So the E-vector is the Lewis-Zagier holomorphic periodic function f(z) = sum_{n>0} A_n e(nz) of (u_L, u_R).


2. Closed form for psi (Cat A conditional on C1-C5)

For x > 0:
psi(x) = (x/(pi sqrt35)) ( int_0^{i inf} [u_R, R_x^{1/2}] - (log eps)/2 ),
R_x(w) = Im w/((w-x)(wbar-x)), [u,v] = u_w v dw + u v_wbar dwbar (Green 1-form).
For x < 0: the same formula with |x| in the prefactor (psi_- := kappa_L(-1/x) - (|x|/sqrt35) sum kappa(x)), and psi_-(-x) = conj psi(x).
Proof route: Green-form lemma (A2: int_z^{z+i inf}[sqrt(y) K_0(2 pi n y) e(nx), R_z^{1/2}] = C e(nz), n > 0; 0 for n < 0; 1/2 for the constant), pullback by w -> -1/w using C2, Stokes/closedness, continuation of Psi(z) = E_L(-1/z) - (z/sqrt35) E_R(z) to C minus iR, boundary values by C5.


3. Exact algebraic values at rationals and agreement (Cat A as finite computation)

psi(h/m) is a finite Shintani/Bernoulli sum over residue classes mod 4m (B2, B1*B1, roots of unity; fastkappa.py), hence algebraic, in Q(zeta_N, sqrt35).
Period integral vs exact values: 84 rationals (44-point grid incl. the 37 earlier points; 40 random rationals, denominators <= 60, both signs): max deviation 1.12e-13 (psi_all.txt, psi_period.txt). Example psi(1) = 0.0068839937604 - 0.0382597122170 i by both routes.
Negative side: period(|x|) vs psi_- exact to 1.6e-14 at 5 points (neg_side2.txt); psi_-(-x) = conj psi(x) to 7.7e-14 (psi_all.txt). With the holomorphic factor x instead, the cocycle grows like 1/y at x < 0 (neg_side.txt).
Independent continuation check: holomorphic polynomial fit using Im z >= 0.01 reproduces real-axis exact values to 2e-12 at 169 rationals (lz_test.txt); K = 1/sqrt35 is the only constant for which singular parts cancel (lz_K.txt).


4. Analyticity and exceptional set (Cat A conditional on C1-C5)

psi is real-analytic on R \ {0} (holomorphic on Re z > 0 and, separately, on Re z < 0) for the automorphy factor |cx+d|.
Exceptional set for S: {0}. T acts by phases (trivial cocycle); S and T generate, so every h_gamma is real-analytic off gamma^{-1} infinity.
At 0: psi(x) ~ -0.0549 i x^2 + 0.0206 x^3 (numerical, from x = 0.01, 0.05); not analytic at 0 (the two sides are conjugate).
Conclusion: the E-vector is a vector-valued quantum modular form of weight 1 in Zagier's sense for the real automorphy factor |cx+d| (equivalently weight (1/2,1/2), the f-function of a lambda = 1/4 Maass form), conditionally on C1-C5.


5. Zeta values (Cat A; exact rational arithmetic; zeta_values.py / zeta_values.txt)

zeta_E(s) := sum_{nu in F cap (a+Z^2)} Q2(nu)^{-s}; full 2-D Euler-Maclaurin to order t^1; t^{-1/2}, t^{1/2} coefficients vanish (symbolic).
zeta_E(0) = 1/10, zeta_E(-1) = 29/1200. With N a = 20 Q2(nu): zeta(0,K) = 1/10, zeta(-1,K) = 20 zeta_E(-1) = 29/60.
Numerical check: (direct - 2I/t - 1/10 + (29/1200)t)/t^2 = 0.1593, 0.1624, 0.1640 at t = 0.02, 0.01, 0.005. Consistent with Siegel-Klingen rationality (named; theorem number not re-checked). Not cross-checked against an independent cone decomposition (Cat B note B4).


6. s = 8 and s = 11 (exact pieces)

Q_s = n^2 + snk + (s/2)k(k+1) = Q2_s(nu) + s/(4(s-2)), a_s = (s/(2(s-2)), -1/(s-2)); rho1, rho2 automorphs swapping a_s and -a_s; gamma_s = [[-1,-s],[2,2s-1]] (trace 2s-2); F = C0 union rho2 C0 is a gamma_s fundamental domain in S+.
Identity 2P_s = E_s + 1 + theta_3 - Theta_hol,s: by the same cone bookkeeping only; NO series check was run for s = 8, 11.
Residues: s = 8, D = 48, 2I = log(7+4 sqrt3)/(4 sqrt3), field Q(sqrt3); s = 11, D = 99, 2I = log(10+3 sqrt11)/(3 sqrt11), field Q(sqrt11).
Cone-zeta values (exact): s = 8: zeta_E(0) = 1/6, zeta_E(-1) = 5/36. s = 11: zeta_E(0) = 7/18, zeta_E(-1) = 1129/1296. t^{+-1/2} coefficients 0; numerical remainders O(t^2).
Baker obstruction carries over verbatim (log-unit term irrational over the algebraic coefficients).
Not claimed for s = 8, 11: psi, Maass lift, ray-class identification (Cat B note B2).


7. Extends the P_s ledger's Cat B item (note; no older file edited)

U1_LEDGER_P_s_Structure_RayClass_2026-10-17.md section 8 and CatB_Notes_P_s_Structure_2026-10-17.md item B1 listed "quantum modularity of the E-vector (numerical evidence)" as Category B, "no closed form for psi". This ledger supplies the closed form: the E-vector is now quantum modular, CONDITIONALLY on C1-C5, with the |cx+d| automorphy factor (not the holomorphic factor cx+d). The P_s ledger's Cat B items B2 (consequence for P_s), B3 (Appell-Lerch, conditional) and B4 (residue formula from memory) are not affected. P_s ledger "Next steps" (a) closed form for psi and (b) zeta(-1,K) are addressed here. Only the (a,0) row of the S-cocycle was computed (Cat B note B1).


8. Not claimed

Unconditional status for any statement in sections 1, 2, 4. Rows other than (a,0). The Eisenstein/cusp decomposition of u_R. Anything about psi_s for s = 8, 11. No HQCC, TPC or RH statement.

Hygiene. Pure copy-and-create; no existing file modified or renamed; no locks altered. Cat A (conditional) only here. CORE_FREEZE untouched.
