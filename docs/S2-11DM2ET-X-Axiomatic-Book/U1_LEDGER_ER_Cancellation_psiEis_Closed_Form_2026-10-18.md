U1-LEDGER-ER-CANCELLATION-psiEis-CLOSED-FORM
E_R cancellation proved: Herglotz closed form for psi_Eis (Theorem 1) and E_R in closed form (Theorem 2)
Category A, audited once (verdict PASS WITH FIXES; all fixes applied in rev 2), given the earlier Cat A inputs (I1)-(I3). Category B items are in CatB_Notes_ER_Cancellation_2026-10-18.md.
2026-10-18

PURE MATH. 539 is a COUNT. Residual is not Resonant. CORE_FREEZE untouched. No locks altered.
No HQCC termination claim. Twin Prime and RH unclaimed.

Parent tip. c5a565e3bb7db3fc7159ee0ce29e79611a1c7098 (main).
Sources (verbatim copies) in ER_Cancellation_2026-10-18/:
- 2026-10-18-ER-Cancellation-Proof.md (rev 1, unchanged), 2026-10-18-ER-Cancellation-Proof-rev2.md (rev 2, the version of record), 2026-10-18-ER-Cancellation-Audit.md (audit report);
- proof/ = the reports' "2026-10-18-ER-cancellation/" (rev-1 scripts, plus em_check2.py / em_check_corrected.txt new in rev 2); audit/ = "2026-10-18-ER-cancellation-audit/".
Audit. Written up as an independent audit by Grok Bot with from-scratch numerical code (one read-only reuse flagged: the rational kappa reference uses hp_check.psi_exact from the audited folder). It is one audit pass, not a formal verification and not an external referee.
Builds on. U1_LEDGER_psiEis_Herglotz_and_Cusp_Lvalues_2026-10-17.md (fae9aee); U1_LEDGER_Cusp_Part_2026-10-17.md (c8d1545); U1_LEDGER_psi_Conditions_Removed_2026-10-17.md (a814a86); U1_LEDGER_psi_Cocycle_LewisZagier_2026-10-17.md (7519051).
Notation. 8 genus characters chi = chi_{j,l}, j in {0,2,4,6}, l in {0,1}; psi mod 20; a(m) = psi(m) 1_{(m,10)=1} (period 20); b(k) = psi(k) chi_140(k) (period 140); eta_a = eta_b, eta_a eta_b = 1 (chi_140 even); rho_n = -bhat(n)/(2 pi i 140), rho_0 = 0, sum_s rho_s = 0; bhat(n) = sum_{r mod 140} b(r) e(rn/140), acheck(k) = sum_{r mod 20} a(r) e(kr/20); w_chi = e(-j/8)/16; psi_Gamma = digamma.


1. Statements

Theorem 1 (Cat A, audited once, given I1-I3). For Re z > 0 (indeed on U = H u {Re z > 0}):
  Psi(z) = E_L(-1/z) - (z/sqrt35) E_R(z) = (1/8) sum_{j in {0,2,4,6}, l in {0,1}} e(-j/8) R_{j,l}(z),
  R_chi(z) = sum_{m>=1} a_chi(m) sum_{s=1}^{140} rho_s^chi psi_Gamma(s/140 + m/(20z)).
On H the left side is the q-series; elsewhere on U it is the continuation from (I3).

Theorem 2 (Cat A, audited once, given I1-I3). E_R in closed form via Gauss-sum duals at level 140:
  E_R(z) = (sqrt35/140) sum_chi w_chi sum_{n,k>=1} bhat_chi(n) acheck_chi(k) e(nkz/140).
This is an explicit Eisenstein decomposition of E_R. No arithmetic (Gauss-sum or ideal-theoretic) proof of Theorem 2 is given; it follows from the analytic argument.

Corollary (Cat A, given I1-I3 and R1). For rational x > 0, Psi(x) equals the exact Bernoulli/kappa value psi(x) = kappa_L(-1/x) - (x/sqrt35) sum kappa_R(x). So the Herglotz form gives the exact Bernoulli values at rationals. The Corollary depends on R1.


2. Inputs (earlier Cat A; checked numerically by the audit, NOT re-audited)

(I1) Genus decomposition E_L = sum_chi w_chi G_chi(./20) (Cusp-Part sections 2, 5). Audit check: exact for 20Q <= 2000.
(I2) Poisson S-law u_L(-1/w) = u_R(w)/sqrt35 (psi Conditions-Removed section 2).
(I3) Green-form lemma (C = -pi/2) and the Stokes/period formula continuing Psi to Re z > 0 (psi Conditions-Removed section 1; psi-Cocycle A3). Audit check: period formula matches the q-series on H and Herglotz off H to ~1e-16.


3. Proof outline (rev 2)

- Lemma 1 (Mittag-Leffler): B(u) = sum_n rho_n/(u - n/140) = sum_s rho_s pi cot pi(u - s/140) (Liouville in e(u)).
- Lemma 2: phi(X) := sum_s rho_s psi_Gamma(s/140 + X) = -140 sum_{n>=1} rho_n/(n + 140X).
- Lemma 3: R holomorphic on U (G1 fix (a)); |R(z)| <= C(1+|z|) on S = {1 <= Re z <= 141, Im z <= -1} (G2: Abel summation of the odd-character tail).
- Prop. 4: G_chi(-1/(20z)) = 2R_chi(z) + T_chi(z) on H. So Theorem 1 is equivalent to (*) sum_chi w_chi T_chi(z) = (z/sqrt35) E_R(z) on H.
- Lemma 5 (two-variable summation by parts, uniform O(|w|^-3) kernel bounds), Lemma 6 (inner m-sum via cot), Prop. 7: T_chi(z) = (z/140) sum_{n,k>=1} bhat(n) acheck(k) e(nkz/140), absolutely convergent; trivial character via a second-order summation by parts (the cancelled constant (2/5) sum rho_n/(nz) is genuinely nonzero).
- Liouville step: D = Psi - 2 sum w_chi R_chi = z P(z), P 140-periodic with only positive frequencies (E_R has no constant term: nu = 0 not in F); P extends to an entire function of q' = e(z/140) with P(0) = 0; Lemma 8 gives |Psi| <= C(1+|z|)^2 on S, hence |P| <= C(1 + log|q'|); Cauchy estimates give P = 0. This proves (*) (Theorem 2) and Theorem 1.
- R2 (section 6.1): termwise Green-form integration by dominated convergence (O(X) gamma-orbits with |Q| <= X; decay e^{-2 pi n0 (y+s)}, n0 = min|Q| > 0).
- R1 (section 6.2): sector-uniform two-variable Euler-Maclaurin of order 3, all remainders bounded: f(e(x)e^{-t}) = s/t + h t^{-1/2} + kappa + O(|t|^{1/2}) uniformly for |arg t| <= pi/2 - delta, |t| <= 1, with the real-t coefficients. Then continuity of Psi at x (Theorem 1) forces the y^-1 and y^-1/2 coefficients to cancel and gives the Corollary.


4. Status of R1 and R2

R2: proved (Cat A).
R1: a complete standard argument after the G3 fix (Cat A as written proof; standard Euler-Maclaurin estimate).
Corollary: depends on R1.


5. Audit record

Verdict: PASS WITH FIXES. No fatal error found. 3 fixable gaps, 8 minor issues; none changes a statement. All fixes applied in rev 2.
Gaps:
- G1: R holomorphic only on Re z > 0 in rev 1, but used on H. Fix (a) adopted: Lemma 3 extended to U = H u {Re z > 0}.
- G2: odd-character tail in the growth bound only conditionally convergent; fixed by Abel summation, R = O(1+|z|) on S.
- G3: R1 remainder bookkeeping incomplete; rev-1 "t^{+-1/2} terms vanish" claim invoked without reference. Fixed: full order-3 two-variable EM with every remainder bounded; the vanishing claim removed and replaced by the cancellation argument.
Minor:
- m1: |P| <= C(1 + log|q'|), not squared.
- m2: uniformity of O(|w|^-3) over the lattice stated.
- m3: R = O(1+|z|), not O(|z| log|z|).
- m4: symmetric m-limit vs per-residue limits differ by O(1/M).
- m5: inert p: r_chi(p) = 0 and r_chi(p^2) = psi(p)^2.
- m6: R2 counts O(n) gamma-orbits (not lattice points) with |Q| <= n; decay e^{-2 pi n0 (y+s)}.
- m7: psi(x) = kappa-value needs R1, now stated.
- m8: nu = 0 not in F, so E_R has no constant term; frequencies in (2/140)Z, with proof.
One deviation from the audit: the auditor's 1D Euler-Maclaurin remainder sign (-1)^{p+1} Btilde_p(u-y)/p! is wrong for odd p; the author used the correct (-1)^{p+1} Btilde_p(y-u)/p!, verified to 1e-31 for p = 1, 2, 3 (proof/em_check2.py -> em_check_corrected.txt; the auditor's form fails, proof/em_check_auditor_sign.txt). The bounds use only |Btilde_p|, so the argument is unaffected.


6. Independent numerics

check                               | rev 1                  | audit (independent code)
split G = 2R + T, all 8 characters  | 7e-14                  | <= 8e-34 (<= 2e-35 for the 7 nontrivial characters; 5 points incl. Re z < 0)
Theorem 2                           | N <= 5600, 4.6e-14     | N <= 14000, 1.8e-15; all 627 nonzero coefficients identical as A + B phi in Z[phi]
Theorem 1 on H                      | -                      | 5.5e-35 (6 points, 36 digits)
Theorem 1 off H (Re z > 0)          | 2e-12                  | 2.5e-16 (5 points, double); 9.2e-16 at z = 3-3i, 10-10i, 20-40i (growth.py)
Theorem 1 at rationals              | 5.7e-33                | 5.7e-35 (8 rationals; kappa reference reuses hp_check.psi_exact, not independent); from-scratch period formula 5.7e-17 (double)
Other audit checks: kernel identities exact (sympy); Lemma 1 <= 5e-29; I1 coefficient check exact (20Q <= 2000); growth |Psi|/|z| -> 0.0666 ~ log eps/(2 pi sqrt35) on S (observed, not proved; Lemma 8 proves the weaker bound).


7. Upgrades recorded (note; no older file edited)

- U1_LEDGER_psiEis_Herglotz_and_Cusp_Lvalues_2026-10-17.md lines 26-27 ("E_R half: NOT PROVED"; "full identity ... NUMERICALLY VERIFIED, PROOF PENDING") and line 74 (not claimed: proof of the E_R cancellation): the closed form for psi_Eis is now Cat A (Theorem 1 and Corollary), audited once, given I1-I3 and (for the Corollary) R1. CatB_Notes_psiEis_Lvalues_2026-10-17.md B1 (line 10) and OPEN line 34: closed. Its B2 ("u_R's Eisenstein basis unidentified"): Theorem 2 gives an explicit Eisenstein decomposition of E_R (positive part of u_R).
- U1_LEDGER_psi_Conditions_Removed_2026-10-17.md lines 21-23, conditions R1 (= C5, uniform sectorial Euler-Maclaurin / non-tangential limits) and R2 (Fourier-sum / Green-integral interchange): DISCHARGED by rev 2 sections 6.2 and 6.1 (R1 after the G3 fix). Its line 72 ("Consequence (given R1, R2)") no longer carries those conditions. CatB_Notes_psi_Conditions_Removed_2026-10-17.md OPEN line 20: closed. R3 (PARI) is unaffected.


8. What remains

- The p2^3 class-assignment step behind the Cusp-Part 60 + 12 split (ideals assigned to classes mod p2^3 p5 p7 inf1 inf2) still uses PARI.
- PARI lfun values (cusp-row L(0) identity) are uncertified.
- No arithmetic proof of Theorem 2.
- The Lewis-Zagier interpretation of R_chi (Eisenstein period functions at s = 1/2) is Cat B.
- Inputs I1-I3 not re-audited in this round.


9. Not claimed

Anything beyond Theorems 1, 2 and the Corollary. Formal verification. No HQCC, TPC or RH statement.

Hygiene. Pure copy-and-create; no existing file modified or renamed; no locks altered. CORE_FREEZE untouched.
