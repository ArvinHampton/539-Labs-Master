U1-LEDGER-psiEis-HERGLOTZ-AND-CUSP-LVALUES
psi_Eis as twisted Herglotz functions; cusp rows via Hecke L-values at s = 0; PARI-free Cl+_(2 sqrt35)
Mixed status: each item carries its own label (Cat A proved / Cat A numerical / proof pending). Category B items are in CatB_Notes_psiEis_Lvalues_2026-10-17.md.
2026-10-17

PURE MATH. 539 is a COUNT. Residual is not Resonant. CORE_FREEZE untouched. No locks altered.
No HQCC termination claim. Twin Prime and RH unclaimed.

Parent tip. 5b85559d0373949e87935dd52b735a0a78f0af32 (main).
Source (verbatim copy). psiEis_Lvalues_2026-10-17/2026-10-17-psiEis-and-Lvalues.md with scripts, outputs and logs in the same folder (the report's "2026-10-17-psiEis-Lvalues/" refers to that folder). Pickles and bytecode not included (see PUSH_LOG).
Builds on. U1_LEDGER_Cusp_Part_2026-10-17.md (c8d1545): u_L pure Eisenstein, psi = psi_Eis, 72 = 60 + 12, 12 dihedral forms from 24 characters of conductor (2 sqrt35).
Notation. psi_Gamma = Gamma'/Gamma (digamma). psi_{j,l}: the 8 genus Dirichlet characters of the Cusp-Part ledger section 2 (j in {0,2,4,6}, l in {0,1}; conductor | 20; psi(7) = chi_{j,l}(p7)); psi' = psi chi_140. Psi(z) = E_L(-1/z) - (z/sqrt35) E_R(z).


1. Herglotz-type closed form for psi_Eis

For x > 0:
  psi(x) = psi_Eis(x) = (1/8) sum_{j in {0,2,4,6}} sum_{l in {0,1}} e(-j/8) R_{j,l}(x),
  R_{j,l}(z) = sum_{m>=1, (m,10)=1} psi_{j,l}(m) sum_{s=1}^{140} rho_s^{(j,l)} psi_Gamma(s/140 + m/(20z)),
  rho_s = -(1/(2 pi i 140)) sum_{r mod 140} psi'(r) e(rs/140)  (= -tau(psi') conj(psi'(s))/(2 pi i 140) when psi' is primitive mod 140).
For x < 0: psi(x) = conj psi(|x|). Equivalent Lewis-Zagier shape: R_{j,l}(z) = -140 z sum_{m>=1} sum_{n>=1} a(m) rho_n/(7m + n z), a(m) = psi(m) 1_{(m,10)=1}.
No elementary correction terms: no constant, no log, no polynomial (sum_s rho_s = 0; psi' never trivial).

STATUS.
- Derivation of the E_L half: Cat A (proved). Lambert part B(u) = sum_n rho_n/(u - n/140) by Liouville (same poles, 1-periodic, -> 0 at +-i inf since b(140) = 0, rho_0 = 0); split n > 0 gives R_chi exactly; the singular part rewrites as a Lambert series plus eta_a eta_b R_chi with eta_a eta_b = chi_140(-1) = +1.
- Cancellation of the remaining Lambert series against (z/sqrt35) E_R(z) (the E_R half): NOT PROVED (Cat B notes B1).
- The full identity is therefore NUMERICALLY VERIFIED, PROOF PENDING:
  44 grid rationals in [1/8, 2], denominators <= 8, 34 digits: |Delta| <= 5.7e-33 (hp_check.txt); e.g. psi(1) = 0.006883993760419869190321587 - 0.03825971221697307224258855 i;
  40 random rationals, denominators <= 60, both signs: 2.5e-12 (double precision; floor ~1.5e-12 set by scipy; complex_check.txt);
  off the real axis (holomorphic on Re z > 0): q-series Psi vs 34-digit Herglotz at z = 1+0.6i and 2+i: 2.9e-17 and 1.9e-16 (complex_hp.txt); five further complex points at the double-precision floor ~1.6e-12 (complex_check.txt).
Not tested: algebraicity of an individual R_{j,l}(x) at rationals (only the full combination is known to be algebraic).


2. Cusp rows via Hecke L-values at s = 0 (Cat A numerical, L-values from PARI lfun)

For every cusp row c of Phi and x in {1, 1/3, 2, 3/5, 7/4, -1, -2/3}:
  Phi_c(x) = kappa_c(-1/x) - |x| sum_{c' cusp} S_{cc'} kappa_{c'}(x),  kappa_c(h/k) = sum_{chi'} Ghat_{c,h/k}(chi') L_{m_k}(0, chi'),
chi' ray class characters of modulus m_k ((2 sqrt35) inf1 inf2 with extra powers of p2, p5, p7, (3) as k requires); Ghat an explicit finite Fourier coefficient built from Fhat_c(chi) = (1/48) e(k/60) and e(h N a/(140k)). For k without a factor 3: kappa_c(h/k) = (1/phi(140k)) sum_{psi mod 140k} tau(psi-bar) psi(h) sum_chi Fhat_c(chi) L(0, u_chi tensor psi); for 3 | k one extra term from ideals divisible by the inert prime 3.
Why s = 0 (Cat A): kappa_c(x) = Z_c(0; x), Z_c entire for cusp rows; e(h N a/(140k)) is a ray-class function for k built from 2, 5, 7 (checked on all classes up to norm 60,000).
Agreement: all 24 cusp rows at all 7 points vs the exact Bernoulli values, max deviation 4.0e-14 (x = 7/4: 3.4e-13 at the kappa(-4/7) step; cusp_rows_L*.txt). Example Phi_73(1) = 0.120446470003 + 0.176437422094 i.
Only the 12 totally odd (type (1,1)) cusp characters contribute; type (0,0) and mixed characters have L(0) = 0 (PARI values; the Gamma-factor reason is Cat B).
L(0) values are algebraic integers in Z[zeta_12], recognised to 1e-10: e.g. L(0, chi_{3,1,1}) = -12 + 4i, L(0, chi_{1,1,1}) = -(6+4 sqrt3) + (6 sqrt3 - 4) i, L(0, chi_{5,1,1}) = (4 sqrt3 - 6) - (4 + 6 sqrt3) i.
Functional-equation check: L(0,chi) = W(chi) 140 L(1, chi-bar)/pi^2 for the 12 totally odd cusp characters, max deviation 1.8e-15.
Central values do NOT give the point values: replacing every L(0) by L(1/2) gives Phi_73(1) = 0.0349 + 0.0748 i (max deviation 0.32 over the 24 rows); using only the 12 totally odd central values, 0.31 (central_test.txt). At x = 1 the 24 cusp-row values lie in a 6-dimensional space (one direction per sigma-pair of totally odd characters).
Central values L(1/2, u_chi) (PARI, 38 digits; lvalues.txt), all nonzero:
  (1,.,1)~(13,.,1): type (0,0) 1.109240202417 - 0.205788403698 i; type (1,1) 0.131513747745 + 0.708885114750 i
  (3,.,1)~(15,.,1): type (0,0) 1.057777176883 - 0.300492329005 i; type (1,1) -0.123002454086 - 0.432986722370 i
  (5,.,1)~(17,.,1): type (0,0) 0.514021161380 + 0.466537408032 i; type (1,1) 1.122786592523 - 1.237062791397 i
  j = 7, 9, 11 ~ 19, 21, 23: complex conjugates.
Dependence: the L-values come from PARI lfun (primitive characters via bnrmap, imprimitive Euler factors added; 38 digits). PARI's lfun is not certified; it is internally consistent here (functional equation; Bernoulli values reproduced to ~1e-14).


3. Hand certification of Cl+_(2 sqrt35) (Cat A; PARI-free, computer-assisted Smith form in hand_cert.py)

1 -> U/U_{m,1} -> (O/m)^x x {+-}^2 -> Cl+_m -> Cl -> 1, m = p2^2 p5 p7 = (2 sqrt35).
(O/(2))^x = <sqrt35> = Z/2; F5^x = <2> = Z/4; F7^x = <3> = Z/6. U = <-1, eps>: -1 -> (0,2,3;1,1), eps -> (1,0,3;0,0). Cl = Z/2 generated by p13 (x^2 - 35y^2 = +-13 insoluble mod 5; p13^2 = (22 + 3 sqrt35), totally positive), image (1,1,0;0,0).
Smith invariants [2, 2, 24], order 96 (= 2 * 48 * 4/4).
sigma trivial on residue coordinates, swaps signs; sigma(q) = [(13)] - q, [(13)] -> (0,3,3;0,0).
Of the 96 characters: 24 non-sigma-invariant of pure type, all of finite conductor p2^2 p5 p7 = (2 sqrt35) (12 type (0,0), 12 type (1,1)); 48 mixed; 24 sigma-invariant. All counts match PARI.
Consequence. The Cusp-Part reliance on PARI for the group structure, sigma-action, types and conductors at (2 sqrt35) is removed. Scope note: the Cusp-Part component fits (fitF.py) assigned ideals to classes mod p2^3 p5 p7 inf1 inf2 using PARI; this round certified the group at (2 sqrt35), where all 24 cusp characters have their conductor, and did not redo that class assignment by hand. PARI still supplies the L-values of section 2.


4. Supersedes (note; no older file edited)

CatB_Notes_Cusp_Part_2026-10-17.md:
- B4 "Herglotz closed form for psi_Eis (expectation, untested)" (lines 23-25) and OPEN "Elementary closed form for psi_Eis" (line 40): superseded by section 1 (closed form found; numerically verified, proof of the E_R half pending).
- B2 "PARI group structure at (2 sqrt35)" (lines 16-17) and OPEN "Hand certification of the structure of Cl+_(2 sqrt35)" (line 41): superseded by section 3.
- B3 "Lewis-Zagier / L-value reading of the cusp rows" (lines 19-20) and OPEN "Independent evaluation of the twisted central L-values ..." (line 43): the tested part is superseded by section 2. The point values at rationals are L(0) (edge) combinations, NOT twisted central values; the expectation stated there is not borne out. The LZ period-function identification itself remains Cat B.
Also U1_LEDGER_Cusp_Part_2026-10-17.md section 5 status ("group structure ... are PARI output (only the order ... is hand-certified)"): the group at (2 sqrt35) is now hand-certified (scope note in section 3).


5. Not claimed

A proof of the E_R cancellation. Identification of u_R's own Eisenstein basis (a naive divisor-sum fit failed, residual 4). The Lewis-Zagier reading of R_chi or of central values as Mellin data of Phi. Certification of PARI lfun. No HQCC, TPC or RH statement.

Hygiene. Pure copy-and-create; no existing file modified or renamed; no locks altered. CORE_FREEZE untouched.
