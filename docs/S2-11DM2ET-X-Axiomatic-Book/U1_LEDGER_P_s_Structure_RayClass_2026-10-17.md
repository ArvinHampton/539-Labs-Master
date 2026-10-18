U1-LEDGER-P_s-STRUCTURE-RAYCLASS
Exact structure of the orthant series P_s (shared remainder of Bridge C and C_third)
PARTIAL STRUCTURE (exact) with sharpened obstructions. No closed modular identity for P_s in the classes tested.
Category A ledger only. Category B items are in CatB_Notes_P_s_Structure_2026-10-17.md.
2026-10-17

PURE MATH. 539 is a COUNT. Residual is not Resonant. CORE_FREEZE untouched. No locks altered.
No HQCC termination claim. Twin Prime and RH unclaimed.

Parent tip. cdded5235428f4d6c3ec7b80b5958ed209e8a434 (main).
Source (verbatim copy). P_s_Structure_2026-10-17/2026-10-17-P_s-Structure.md with scripts and outputs in the same folder (the report's "2026-10-17-P_s-structure/" refers to that folder).
Prior package. U1_LEDGER_Bridge_C_Residual_Law_Obstruction_2026-10-17.md (d9d2a00). Corrections to it: ERRATUM_Bridge_C_tminushalf_Coefficient_2026-10-17.md.
Notation. P_s = sum_{n,k>=0} q^{Q_s(n,k)}, Q_s = n^2 + 7nk + (7/2)k(k+1) (Residual_Bridge_Series_C_Definition.md l.15, l.29). eps = 6 + sqrt35 (fundamental unit, N(eps) = +1). I = log eps/(2 sqrt35) = 0.2094198203147146...


1. Exact decomposition (Cat A; exact to q^3000; structure.py / structure.txt)

2 P_s = E + 1 + theta_3 - Theta_hol
theta_3 = sum_{n in Z} q^{n^2}. Theta_hol = Zwegers weight-1 holomorphic part (U1_LEDGER_OCCFILT7_INF_THEOREM_L_Cthird_Zwegers_2026-10-17.md, section 2).
E := R + C_third + sum_{n>=1} q^{n^2}, R = sum_{n>=0,k>=1} q^{Q_s}.
Odd part: R - (C_third + sum_{n>=1} q^{n^2}) = -Theta_hol (exact to q^3000).


2. Orthant = half a fundamental domain for eps (Cat A; symbolic checks)

Completing the square: Q_s(v) = Q2(v+a) + 7/20, Q2(x,y) = x^2 + 7xy + (7/2)y^2, a = (7/10, -1/5).
In nu = v + a coordinates: rho1 = [[1,7],[0,-1]], rho2 = [[-1,0],[2,1]] are integral reflections (det -1) preserving Q2, fixing the walls nu2 = 0 and nu1 = 0 of the quadrant C0.
gamma = rho2 rho1 = [[-1,-7],[2,13]], eigenvalues 6 +- sqrt35 (gamma <-> eps).
rho1, rho2 swap a+Z^2 with -a+Z^2; gamma preserves a+Z^2. Coset points never lie on the walls.
C0 union rho2 C0 is a fundamental domain for <gamma> on the positive sector S+. The orthant minus its k = 0 row is exactly half of it.
E = sum_{v: v+a in F} q^{Q_s(v)} for any gamma-fundamental cone F = [r, gamma r) in S+ (exact to q^3000 for r = (1,0), (1,1), (7,-1), (1,2)).
Hecke odd partner. E_{-a} = E_a (exact to q^3000), so the sign-twisted partner E_a - E_{-a} vanishes for this coset (checked to q^3000). E has no modular odd companion.


3. E is a ray-class generating function (Cat A as algebra)

(X,Y) = 10 nu, beta = (2X + 7Y) + Y sqrt35 in Z[sqrt35]. Q2(nu) = N(beta)/400 and beta(gamma nu) = eps beta(nu): checked symbolically.
beta runs over beta0 + 10 p2, beta0 = -2 sqrt35, p2 = (2, 1 + sqrt35) (ramified over 2). nu in S+ <=> beta totally positive.
With d' = p2^2 p5 and f = p2 p5: a := (beta) d'^{-1} runs over one narrow ray class K modulo f inf1 inf2 (containing p7 (alpha1) for alpha1 = 1 mod^x f, sgn alpha1 = (-,+)).
Totally positive units = 1 mod^x f are exactly eps^Z, so gamma-orbits <-> ideals in K.
N a = 20 Q_s(v) - 7, hence
E(q) = sum_{a in K} q^{(N a + 7)/20}.
First norms 13, 73, 133, 153, 173 (all = 13 mod 20).
Status. The key identities (Q2 = N(beta)/400, beta(gamma nu) = eps beta) are symbolic checks. The ideal-theoretic bookkeeping (d', f, the class K, the orbit <-> ideal bijection) was done by hand. Standard inputs: Z[sqrt35] is the maximal order (35 = 3 mod 4); unit group +-eps^Z.


4. Radial asymptotics at q = e^{-t} (Cat A as scoped; em.py, em_exact.py, closed_forms.py, em_check.py, hs_decomp_check.py)

Series     t^-1   t^-1/2                                          t^0
P_s        I      a_P = sqrt(pi)(49 - 2 sqrt14)/140 = 0.5256172043  (11 - 7I)/20 = 0.4767030629
C_third    I      -a_P                                            (11 - 7I)/20
E          2I     0                                               (1 - 7I)/10
H_s        0      a_H = sqrt(pi)(sqrt1190 - 17 sqrt14)/170 = -0.3035254127   0 (to 30 digits only)
C          I      a_C = sqrt(pi)(833 + 204 sqrt14 - 14 sqrt1190)/2380 = 0.8291426171   (11 - 7I)/20

Status of each entry.
- Symbolic (sympy, residual 0 to 165 digits): all t^-1 entries; the t^0 entries of P_s, C_third (same as P_s), R and E; E's t^-1/2 = 0.
- a_P: derived as an explicit Euler-Maclaurin expression; the radical form agrees to 30 digits (sympy left one elementary integral unevaluated, so the radical form is confirmed numerically, not symbolically).
- a_H and a_C: explicit Euler-Maclaurin expressions evaluated to 30 digits; the radical forms are PSLQ identifications at 30 digits. H_s's t^0 = 0 holds to 30 digits only (not proved symbolically).
- H_s cone decomposition used for a_H: exact to q^2000. All coefficients also confirmed numerically (remainder ~ sqrt(t) down to t = 2.5e-5; ~ t for E).

zeta(0,K) = 1/10 (Cat A): from Hecke's expansion E(e^{-t}) = e^{-7t/20}[20 Res/t + sum_j zeta(-j,K)(-t/20)^j/j!] and the symbolic t^0 coefficient (1 - 7I)/10. Residue Res_{s=1} zeta(s,K) = log eps/(20 sqrt35). Consistent with Siegel-Klingen rationality.
Mellin form. Z(s) = sum_{(n,k)>=0, !=0} Q_s(n,k)^{-s}: simple poles at s = 1 (residue I) and s = 1/2 (residue (49 - 2 sqrt14)/140); Z(0) = -(9 + 7I)/20. The log eps in Z(0) comes from the 7/20 shift; the ray-class value 1/10 is rational.
Consistency: the t^-1/2 coefficient of Theta_hol is forced to be sqrt(pi) - 2 a_P = sqrt(pi)(21 + 2 sqrt14)/70.
Consequence: a_C != 0, so C * g = F is impossible for holomorphic modular g != 0, F of any weight, level, multiplier, with complex coefficients (same argument as for C_third). Obstruction 2 for C is upgraded to Cat A over C; nonvanishing of a_C rests on the 30-digit evaluation of an explicit expression (0.8291...), far from 0.


5. Gauss-mean pattern: PROVED (Cat A; gauss_pattern.py / gauss_pattern.txt)

G(h/m) = (2m)^{-2} sum_{n,k mod 2m} e(h Q_s(n,k)/m), gcd(h,m) = 1:
G = 0 if 2 | m or 5 | m; |G| = 1/m if gcd(m,70) = 1; |G| = sqrt7/m if 7 | m and gcd(m,10) = 1.
Proof: shift k -> k + m (2 | m); quadratic Gauss sums after completing the square (m odd); shift by m/5 (5 | m); CRT for the 7-part. Verified on all 3374 coprime pairs with m <= 105, zero mismatches.


6. Vector-valued route

Leading order (Cat A on all tested points; weil_test.py / weil_test.txt). G_{alpha,beta}(x) = mean over nu in alpha + Z^2 of e(x Q2(nu) + B(nu,beta)).
S-law G_{a,b}(-1/x) = (1/(sqrt35 x)) e(B(a,b)) sum_{p in A^{-1}Z^2/Z^2} G_{b+p,-a}(x): holds to 1e-14 in all 27 tests (components (a,0), (p,-a), (a+p7, p2), 9 values of x incl. zeros of G). T-law exact. This is Zwegers Cor. 2.9(4)-(5) transported to radial profiles (weight-1 Weil representation, 35-element discriminant group). Finite floating-point checks (errors <= 1.5e-14). The general statement (Gauss-sum reciprocity) is Cat B as a theorem.
Exact vector law ruled out (Cat A, via Baker): at the cusp pair (0, infinity) an exact vector-valued modular law with algebraic data would force I in pi Qbar + Qbar, excluded by Baker's theorem (Q2 has no nonzero rational zeros, 35 not a square).
Quadrant cones fail at t^-1/2 (Cat A, finite computation; weil_order2*.py/.txt): the weight-1 S-law at order t^-1/2 fails, |LHS|/|RHS| from 0.49 to 2.97 over 16 tests under either wall convention. Caveat: the order-t^-1/2 formula is this pass's own derivation and assumes sector-uniform expansions; the failure is O(1).
E-vector (gamma-fundamental cones): t^-1/2 coefficient <= 5e-15 for every component at every tested x, consistent with section 4.


7. Cited theorems and their status

- Zwegers, Mock Theta Functions, thesis, arXiv:0807.4834, Cor. 2.9(4)-(5): checked against a local copy of the thesis text.
- Hecke: meromorphic continuation of ray-class partial zeta functions, single simple pole at s = 1. Named; theorem number not re-checked.
- Siegel-Klingen: rationality of zeta(-j, K). Named; theorem number not re-checked. Used only as a consistency check.
- Baker, Linear forms in the logarithms of algebraic numbers I, Mathematika 13 (1966). Named; theorem number not re-checked.
- Ray-class residue formula log eps/(20 sqrt35) = R_f/(w sqrt(d_K) N f): from memory, not re-checked against a source (Cat B note B4); the residue value itself comes from the symbolic t^-1 coefficient of E.


8. Not claimed

psi real-analytic or E quantum modular (Cat B). Any vector law beyond leading order. An Appell-Lerch obstruction (conditional, Cat B). No HQCC, TPC or RH statement.

Hygiene. Pure copy-and-create; no existing file modified or renamed; no locks altered. Cat A only here. CORE_FREEZE untouched.
