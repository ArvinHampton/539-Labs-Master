U1-LEDGER-CUSP-PART
Cusp part of the Maass lift u: u_L pure Eisenstein, exact 60 + 12 Eis/cusp split, explicit dihedral data, scalar psi = psi_Eis
Category A ledger only. Category B items are in CatB_Notes_Cusp_Part_2026-10-17.md.
2026-10-17

PURE MATH. 539 is a COUNT. Residual is not Resonant. CORE_FREEZE untouched. No locks altered.
No HQCC termination claim. Twin Prime and RH unclaimed.

Parent tip. 2ba5641b5e57eedb091890a50a4f6b91ead11924 (main).
Source (verbatim copy). Cusp_Part_2026-10-17/2026-10-17-Cusp-Part.md with scripts and outputs in the same folder (the report's "2026-10-17-cusp-part/" refers to that folder). Binaries and logs not included (see PUSH_LOG).
Builds on. U1_LEDGER_psi_Conditions_Removed_2026-10-17.md (a814a86). Withdrawal of its cusp claim: ERRATUM_psi_Conditions_Removed_Cusp_Claim_2026-10-17.md.
Notation. L = Z^2, A = [[2,7],[7,7]], Q2 = x^2 + 7xy + 3.5y^2 (odd lattice, w_c = (1/10,-1/35)); a = (7/10,-1/5); gamma = [[-1,-7],[2,13]], eps = 6 + sqrt35; K = Q(sqrt35); f = p2 p5 inf1 inf2. Dictionary: (X,Y) = 70 nu, beta_nu = (2X+7Y) + Y sqrt35, N(beta_nu) = 19600 Q2(nu); for the coset a, N a = 20 Q2.
u_L = u_{a,0}, u_R = sum_p u_{p,-a}; the lift sums over the four sign regions S+, S-, T+, T- (cones F, -F, T, -T mod gamma^2).


1. Region <-> ray-class bijection (Cat A)

Cl+_f = Z/8 x Z/2. Each sign region of u_L is exactly one ray class:
  S+ -> (5,0), S- -> (1,0), T+ -> (1,1), T- -> (5,1).
The dictionary is elementary. Lattice counts equal the PARI ideal counts in each class for every n <= 60,000, all four regions, max difference 0 (ideal_counts.txt; an early mismatch above n ~ 29,000 was box truncation, gone with a larger box).
Key relation (hand proof, section 6): with d = (4,0) the class of a totally negative element = 1 mod f,
  S- = S+ + d, T- = T+ + d.


2. u_L is exactly Eisenstein (Cat A; independent of PARI)

Since S- = S+ + d and T- = T+ + d, every character chi enters 1_{S+} + 1_{S-} and 1_{T+} + 1_{T-} with a factor (1 + chi-bar(d)). Characters with chi(d) = -1 (j odd) drop out; these are exactly the non-sigma-invariant ones.
  u_L(w) = (1/4) sum_{j in {0,2,4,6}} e(-j/8) [ U^cos_{chi_{j,0}}(w) + i U^sin_{chi_{j,1}}(w) ],
  U^{cos/sin}_chi(w) = sqrt(y) sum_{a in O, (a,10)=1} chi(a) K_0(2 pi N a y/20) {2cos, 2sin}(2 pi N a x/20).
The 8 surviving characters are genus characters chi = psi o N (psi mod 20, psi(7) = chi(p7)); table in the report, section 2 (genus_chars.txt, matched on all primes < 3000).
Coefficients: lambda_chi(n) = 1_{(n,10)=1} sum_{d|n} psi(d) (psi chi_140)(n/d). Check: A(n) = #(S+ u S-) and B(n) = #(T+ u T-) equal this formula for every n <= 60,000 (errors 7.4e-16, 1.1e-15; eis_decomp.txt). Genus-periodicity mod 280: A and B 0 of 48 non-constant classes; T+ alone 6 of 48.
Infinity types: (0,0) gives cos, (1,1) gives sin; mixed types cancel.
PARI independence: the hand certifications in section 6 (Cl(K), |Cl+_f| = 16, S-/T- relations, the 8 genus characters) give the result with no PARI input; the class-field step "sigma-invariant => psi o N" is not needed.
(Naming these pieces Maass-Eisenstein series E_{psi, psi chi_140}(., 1/2) is standard; see Cat B notes. The coefficient identification is Cat A.)
Consequence: u_R = sqrt35 u_L o S is also Eisenstein.


3. Scalar psi = psi_Eis (Cat A, given section 2)

psi(x) = (x/(pi sqrt35))(int_0^{i inf}[u_R, R_x^{1/2}] - log eps/2) and the split-contour form use only u_L and u_R. Both are Eisenstein, so psi_cusp = 0 and psi = psi_Eis. The earlier rational checks and Bernoulli/Shintani values of psi are Eisenstein quantities. At rationals psi_Eis is an exact finite Bernoulli/Shintani sum.


4. The 72 = 60 + 12 split and the 24 cusp components (Cat A as computation; class data mod m from PARI)

Every one of the 140 components is exactly a ray-class theta series mod m = p2^3 p5 p7 inf1 inf2 (Cl+_m = Z/24 x Z/2 x Z/2): fits c(g n) = sum_{N a = n} F(class_m a), n coprime to 70, up to the cone-complete range (<= 54,880); max residual over all 280 fits 4.4e-14 (fitF.txt, component_split.json).
Character split of the sigma-symmetrised F: mixed-type content <= 1e-29 everywhere; 116 components pure Eisenstein (cusp content <= 3e-30); 24 components pure cusp (Eisenstein content <= 8e-31).
Equivariance: T block-diagonal exactly; S: |sum_{c' Eis} S_{c,c'} u_{c'}| <= 9.0e-17 for cusp rows c and |sum_{c' cusp} S_{c,c'} u_{c'}| <= 3.4e-16 for Eisenstein rows (coefficientwise, 1027 frequencies; equiv_check.txt).
Dimensions in the 72-dim P-invariant representation: cusp 12, Eisenstein 60 (cusp_checks.txt). The split is S/T-equivariant (numerical verification as above).
The 24 cusp components: beta = -a with 7-denominator alpha in a + L' (labels idx: alpha*70 | beta*70 = (-49,14)):
  alpha = (49,66),(49,6),(49,16),(49,26),(49,36),(49,46): idx 73, 75, 77, 79, 81, 83
  alpha = (63,62),(63,2),(63,12),(63,22),(63,32),(63,52): idx 85, 87, 89, 91, 93, 97
  alpha = (7,58),(7,68),(7,8),(7,18),(7,38),(7,48): idx 99, 101, 103, 105, 109, 111
  alpha = (21,64),(21,4),(21,24),(21,34),(21,44),(21,54): idx 113, 115, 119, 121, 123, 125
u_L and every label entering u_R are among the 116 Eisenstein components. Side check: the S/T span of u_L has dimension 36 of 72 (span_check.txt), consistent with u_L not reaching the cusp part.


5. Dihedral characters of conductor (2 sqrt35) and the exact combinations (Cat A as computation; group structure from PARI)

Characters chi = chi_{j,l,1}, j odd mod 24, l in {0,1}: 24 characters, all of conductor f_chi = p2^2 p5 p7 = (2 sqrt35) (norm 140). l = 0: infinity type (0,0); l = 1: type (1,1). sigma acts by j -> 13j; orbits {1,13},{3,15},{5,17},{7,19},{9,21},{11,23}. Orders 24 (j prime to 6), 8 (j in {3,9,15,21}).
Up to chi ~ chi o sigma: 12 classes (6 with l = 0, 6 with l = 1), one dihedral form each:
  u_chi(z) = sqrt(y) sum_{n>=1} lambda_chi(n) K_0(2 pi n y) {2cos(2 pi n x) (l = 0); 2i sin(2 pi n x) (l = 1)},
  lambda_chi(n) = sum_{a in O, N a = n} chi(a)  (chi(a) = 0 unless (a, 2 sqrt35) = 1).
lambda_chi multiplicative; lambda_chi(p) = chi(p) + chi(p') (split), 0 (inert), lambda_chi(p^2) = chi((p)) (inert).
Moduli table (bigray.txt): non-sigma-invariant pure-type characters occur first at p2^2 p5 p7 (24 of them); at p2 p5 p7, p2 p5^2 p7, p2 p5 p7^2 all non-invariant characters are mixed type.
Exact combinations in the cusp components: u_c(w) = sum_{12 forms chi} 2 Fhat_c(chi) u_chi(w/140), Fhat_c(chi) = (1/48) e(k_{c,chi}/60); phases in component_split.json (recognised as k/60 with error 6e-9 from 1e-14-accurate fits). Fhat_-/Fhat_+ = +1 (l = 0), -1 (l = 1). Coefficients at norms not coprime to 70 vanish identically in the cusp components. Example c = 73: k = 7, 57, 47, 37, 27, 17 for j = 1, 3, 5, 7, 9, 11 (l = 0); l = 1 shifted by 30.
Status: the counts, conductors and coefficient formulas are computations; the group structure Z/24 x Z/2 x Z/2, the sigma-action and the conductors are PARI output (only the order |Cl+_(2 sqrt35)| = 96 is hand-certified). Maass-form / newform / level / nebentypus statements are Cat B.


6. Hand certifications (Cat A)

Cl(K) = Z/2 (Minkowski bound sqrt140/2 ~ 5.92; 3 inert; p2 non-principal since x^2 - 35y^2 = +-2 has no solution mod 5; p2^2 = (2), p2 p5 = (5 + sqrt35); eps = 6 + sqrt35 from sqrt35 = [5; 1, 10]).
|Cl+_f| = 16 (h phi(f) 2^2/[U : U_{f,1}] = 2*4*4/2; U_{f,1} = <eps>).
S- = S+ + d, T- = T+ + d (beta(-nu) = -beta(nu); a -> -a is beta0 -> -beta0; d != 0 since -eps^k = -1 mod p5; sigma(S+) = S-).
The 8 genus characters (psi o N well defined on Cl+_f for psi mod 20; distinct by Dirichlet on split primes, chi_140 not a character mod 20; psi o N(d) = 1; |G| = 16 forces exactly 8 characters with chi(d) = 1).
|Cl+_m| = 96 for m = (2 sqrt35) inf1 inf2 (2*48*4/4; eps = -1 mod p7, eps^2 = 1 mod m, eps^2 totally positive).


7. Cusp-row cocycle values (Cat A)

For c in the cusp set, Phi_c(x) = -(2/pi)[-|x| J_U(x) + J_{u_c}(-1/x)] (no constant terms). At rationals Phi_c equals the exact kappa (Bernoulli/Shintani cone) sum, verified to 2e-14 in the previous report. Nonzero: |Phi_c| <= 0.53 at the 7 test rationals; Phi_73(1) = 0.1204464700 + 0.1764374221 i (phi_cusp_rows.txt).


8. Premise correction (Cat A)

Mod p2 p5 inf1 inf2, the non-sigma-invariant characters all have MIXED sign type: they give weight-1 holomorphic dihedral forms, not lambda = 1/4 Maass forms, and their coefficients cancel in the full lift u (section 2). Maass-type (pure-type) cusp characters first appear at modulus (2 sqrt35) inf1 inf2 (section 5).


9. Not claimed

Maass/Hecke theoretical status of the 12 forms (cuspidality, newform, level 19600, nebentypus): Cat B. LZ/L-value reading of the cusp rows: Cat B. Any closed form for psi_Eis. Written-out EM / interchange error terms. No HQCC, TPC or RH statement.

Hygiene. Pure copy-and-create; no existing file modified or renamed; no locks altered. Cat A only here. CORE_FREEZE untouched.
