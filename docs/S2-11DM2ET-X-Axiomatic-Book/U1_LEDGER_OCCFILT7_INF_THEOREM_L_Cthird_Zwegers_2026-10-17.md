U1-LEDGER-OCCFILT7-INF-THEOREM-L
OccFilt_7(infty) = {0,1,2,4} CLOSED (Cat A, computer-assisted, audited once)
C_third as an HM double sum. Zwegers completion of Theta_hol. C_third alone OPEN.
Category A ledger only. Category B items are in CatB_Notes_OccFilt7_Inf_Theorem_L_Cthird_2026-10-17.md.
2026-10-17

PURE MATH. 539 is a COUNT. Residual is not Resonant. CORE_FREEZE untouched. Twin Prime and RH unclaimed.
Book HQCC is not Canonical T3. Nothing here bears on, uses, or extends HQCC termination claims.

Parent tip. 48684e3e43326733c9a08dba15e6556f6396de0e (main).
Parent locks, not edited. 85b082a U1-LEDGER-P-g7-inf. 8d03b56 / 38e47a1 U1-LEDGER-OCCFILT7-INF written-data obstruction + wrap. 4bb6391 / 9c341c2 U1-LEDGER-PHI-STABILIZATION-OCCFILT-IDS + PUSH_LOG SHA stamp. e18ca14 42 Discrete Contacts. 3de76f6 Remark 8.5 kernel, Slash_two empty.
Source reports and scripts (verbatim copies). OccFilt7_Inf_Theorem_L_2026-10-17/
 2026-10-17-Residual-Identities-Mock-Theta-Status.md (+ 2026-10-17-mock-theta-check/)
 2026-10-17-Levers-1-2-Hecke-g7-Cthird.md, incl. Follow-up (+ 2026-10-17-levers-1-2/)
 2026-10-17-Lever-3-OccFilt7-Lower-Bound.md, incl. route 3, independent audit, Post-audit patches rev 2 (+ 2026-10-17-Lever-3-OccFilt7-Lower-Bound/)
Citations used. HM = Hickerson-Mortenson, arXiv:1208.1421. Zwegers = S. Zwegers, Mock Theta Functions, PhD thesis, Utrecht 2002, arXiv:0807.4834v1. No other citation is relied on in this ledger.

Caveats (binding on every item below).
Computer-assisted where marked. Theorem L had ONE independent referee audit (adversarial line-by-line reading of the interval code) and rev 2 patches; it is NOT a formal verification and should get a second reader before being called a theorem in print.
No TPC claim. No RH claim. Distinct from HQCC termination claims. Residual is not Resonant; 539 is a count. CORE_FREEZE untouched.


1. C_third as an HM double sum (Cat A, elementary)

Master definition (Residual_Twin_Support_Path1_Empirical_Locks_2026-08-24.md, Residual_False_Theta_Construction_Attempt_C_2026-08-23.md).
C_third = sum_{n,k>=1} q^{Q_-(n,k)}, Q_-(n,k) = n^2 + 7nk + (7/2)k(k-1).
Q_+(n,k) = Q_-(n,k) + 7k = n^2 + 7nk + (7/2)k(k+1).

Identity.
C_third(q) = q^8 f_{2,7,7}(-q^10, -q^14, q) + sum_{n,k>=0} q^{Q_+(n,k)}
f_{a,b,c} as in HM Definition 0.2 (eq. 0.4).
Proof. r = n-1, s = k-1 gives Q_- = 8 + 2C(r,2) + 7rs + 7C(s,2) + 10r + 14s. x = -q^10, y = -q^14 cancel (-1)^{r+s}. The r,s >= 0 orthant of f is C_third. The r,s < 0 orthant enters with sign -1; (r,s) = (-1-n, -1-k) turns it into sum_{n,k>=0} q^{Q_+(n,k)}.
Checked by exact integer coefficients to q^500 (cthird.txt).
Discriminant b^2 - ac = 49 - 14 = 35. Signature (1,1). Matches Master disc 35.

HM scope. f_{2,7,7} lies outside the hypotheses of HM Theorems 0.3, 0.4, 0.6, 0.9, 0.10, 0.11.
Thm 0.4 needs a | b and c | b; 2 does not divide 7. Thms 0.3, 0.6, 0.9, 0.10, 0.11 need a = c; 2 != 7. Residue splits r = m r', s = n s' give (2m^2, 7mn, 7n^2) and never satisfy the divisibility (also searched m, n < 30: none). Parity splitting (HM Prop 5.1) keeps (a,b,c).
So no HM Appell-Lerch formula with citation exists for f_{2,7,7} as stated.

Master sign convention (Cat A). H_s-weight -1 on third-quadrant points contributes +1 to C. The weight -1 statements and the explicit +1 sums on Master are consistent (Levers 1-2 md, F2).


2. Zwegers completion of Theta_hol (Cat A by citation plus direct substitution)

Source. Zwegers thesis, arXiv:0807.4834v1: section 2.2 setup, Definition 2.1, Proposition 2.4, Corollary 2.9 (4)-(5).
Setting. A = [[2,7],[7,7]], det A = -35, Q(r,s) = r^2 + 7rs + (7/2)s^2, type (1,1).
c1 = A^{-1}e1 = (-1/5, 1/5), B(c1,nu) = nu_1.
c2 = -A^{-1}e2 = (-1/5, 2/35), B(c2,nu) = -nu_2.
Q(c1) = -1/10 < 0. Q(c2) = -1/35 < 0. B(c1,c2) = -1/5 < 0, so c1, c2 lie in the same component; with c0 = c1 both are in C_Q.
Every hypothesis of Definition 2.1, Proposition 2.4 and Corollary 2.9 holds.
Characteristic a = (-7/10, 1/5), b = 0. With nu = (n,k) + a: Q(nu) = Q_-(n,k) - 7/20. B(c1,nu) = n - 7/10 and B(c2,nu) = -(k + 1/5), never 0 (no boundary ambiguity). As y -> infinity, rho -> sgn(n - 7/10) + sgn(k + 1/5): 2 on {n>=1, k>=0}, -2 on {n<=0, k<=-1}, 0 elsewhere.

Holomorphic-part identity (exact integers, to q^399; zwegers_check.txt).
Theta_hol(q) := sum_{n>=1,k>=0} q^{Q_-} - sum_{n<=0,k<=-1} q^{Q_-} = q^8 f_{2,7,7}(-q^10, -q^14, q) + theta_3(q), theta_3(q) = sum_{n in Z} q^{n^2}.
Equivalently Theta_hol = C_third + sum_{n>=1} q^{n^2} - sum_{n>=0,k>=1} q^{Q_+(n,k)}.

Completion (q = e^{2 pi i tau}, y = Im tau).
theta_{a,0}(tau) = q^{-7/20} [ 2 Theta_hol(q) - sum_{(n,k) in Z^2} ( sgn(n-7/10) beta(10(n-7/10)^2 y) + sgn(k+1/5) beta(35(k+1/5)^2 y) ) q^{Q_-(n,k)} ]
10 = 1/(-Q(c1)), 35 = 1/(-Q(c2)). beta(x) = int_x^infty u^{-1/2} e^{-pi u} du (Zwegers Lemma 1.7).
theta_{a,0} transforms by Cor. 2.9 (4)-(5) as weight 1, vector-valued over the 35 classes of A^{-1}Z^2/Z^2.
So Theta_hol = q^8 f_{2,7,7}(-q^10, -q^14, q) + theta_3(q) has a weight-1 completion (it is (1/2) q^{7/20} times the holomorphic part of theta_{a,0}).

C_third ALONE IS STILL OPEN.
C_third = Theta_hol - sum_{n>=1} q^{n^2} + sum_{n>=0,k>=1} q^{Q_+(n,k)}.
The remainder sum_{n>=0,k>=1} q^{Q_+} is a positive-definite-cone partial sum, not a theta function. C_third alone is NOT shown to be mock modular. Theta_third completion is CLOSED for the Zwegers piece Theta_hol and OPEN for C_third itself.
Not reconciled. Master's H_s cone uses c1 = (-1,1), c2 = (-4,1) (Review_Missed_Variables_Bridge_C_2026-08-23.md l.55); different setup.
The numerical Cor. 2.9(5) checks (~1e-16) are Cat B (see Cat B notes).


3. Theorem L and OccFilt_7(infty) (Cat A, computer-assisted, audited once)

Definitions.
g_7(q) = sum_{n>=0} q^{n^2} / (-q^7;q^7)_n. g_7(d) = sum_n phi_n((d-n^2)/7), phi_n(m) = [x^m] prod_{j<=n} 1/(1+x^j).
a_n(m) = (-1)^m phi_n(m) = [x^m] A_n >= 0, A_n(x) = prod_{odd j<=n}(1+x^j) / prod_{k=floor(n/2)+1}^{n}(1-x^{2k}).
(-1)^d g_7(d) = E_d - O_d, E_d = sum_{n even} a_n((d-n^2)/7), O_d = sum_{n odd} a_n((d-n^2)/7).
Allowed d: d mod 7 in {0,1,2,4}. Off these classes g_7(d) = 0 identically (squares mod 7).

Theorem L. Let eta = 0.2272, n1 = 900, D0 = 8,890,003. For every allowed d >= D0,
E_d <= (1 - eta) O_d, hence g_7(d) = (-1)^d (E_d - O_d) != 0.
Exact margin 1 - 0.77273278 - 10^-6 = 0.2272662... (worst block ratio, class 2, plus tail allowance eta_t = 10^-6).
D0 = ceil((n1/alpha1)^2); (900/alpha1)^2 = 8,890,002.97.

Proof skeleton (route 3; all constants from mpmath.iv interval arithmetic; floats only choose free parameters).
R1. Local CLT for the tilted model at r = e^{-u/n}: |P(S=m) - g(m-mu)| <= delta/(sqrt(2 pi) sigma), delta = D1 + D2 + D3, written proof in the Lever 3 md (rev 2). delta <= 0.1517943 (rounded outward 0.151795) on every u-cell used, for n >= 893; D2 <= 2.1e-25, D3 <= 1.8e-15. Uniformity in n by Lemma S.
R2/R3. Block lemma. Disjoint blocks of n-width <= 14 per class (base residue mod 14 + offsets {0,5,7,12}, {0,1,7,8}, {0,3,7,10}, {-7,0,7}). For n >= 900 and base saddle u_b in [0.3, 1.6], Sigma_E / Sigma_O <= 0.72313 / 0.73974 / 0.77273 / 0.73562 for classes 0 / 1 / 2 / 4. Minimum odd-side factor 1 - gfac - delta >= 0.78507 > 0 (asserted, rev 2).
Window. Bases with alpha_b in [0.30185026151, 0.70434264606] have u_b in [0.3, 1.6]; for d >= D0 every such base has n_b >= n1.
R4. Tails. Even terms outside the window (at most sqrt d of them) total <= 10^-6 o*, where o* is a central odd term. Psi_low = inf_{u in [0.5,0.75]} F(alpha*, u) >= 0.395568. Max tail gap -0.014809 <= -2.5/sqrt(D0); T(D0) <= -6.80 with eta_t = 10^-6; T(d) decreasing for d >= D0.
Class-0 pairing. d = 0 mod 7 forces n = 0 mod 7, so parity alternates along n = 7l. Block: e_{14l} <= 0.72313 * (1/2)(o_{14l-7} + o_{14l+7}). Each odd layer is used by two adjacent blocks with weight 1/2, total weight <= 1.
Assembly. E_d = E_good + E_bad <= 0.772733 O_blocks + 10^-6 o* <= (1 - 0.22726) O_d (blocks disjoint, class-0 weights sum to 1, O_blocks and o* <= O_d).
Audit. Independent referee pass: sound with fixable gaps; all seven issues patched in rev 2 and pass; full rerun reproduces every constant (Psi_low and T(D0) moved favourably). Checksums: lemmaL/route3/SHA256SUMS.

Non-vanishing certificate (Cat A, computational).
g_7(d) != 0 for every allowed d with 247 < d <= 10^9 (cert1e9; cert1e8 to 10^8; g7mod to 10^7 also covers d < D0).
Exact uint64 arithmetic mod p0 = 4611686018427387847 (< 2^62), no floating point; g_7(d) mod p0 != 0 implies g_7(d) != 0.
Count. 571,428,548 allowed d shown nonzero + 24 zeros = 571,428,572 = #{allowed d <= 10^9}.
Zeros = Miss_7 = {2,7,14,16,18,21,28,32,35,36,42,43,44,57,60,63,78,79,85,100,107,135,191,247} (true zeros, exact values). D1e9.zeros byte-identical to D1e8.zeros.

CONCLUSION. OccFilt_7(infty) = {0,1,2,4} CLOSED. 247 is the last zero of g_7 on the allowed classes.
Since D0 = 8,890,003 <= 10^9 (indeed <= 10^7), Theorem L plus the certificate cover every allowed d > 247.

Supersession (no file edited). This supersedes the status "infinitude after 247 OPEN" / "Infinity UNOCCUPIED as an integer statement" recorded in the earlier OccFilt_7 written-data obstruction (ledger 8d03b56, wrap 38e47a1) and the "Not OccFilt_7(infty)" scope note of PhiStab Close (A) (4bb6391 / 9c341c2). Those files are left unchanged. Their Close (C) remains true as a statement about written Master data alone; the closure here is new computer-assisted work, not a derivation from written Master identities.


4. Other Cat A facts (one line each)

A1 Positivity. (-1)^m phi_n(m) = a_n(m) = [x^m] prod_{odd j<=n}(1+x^j) prod_{k=floor(n/2)+1}^{n}(1-x^{2k})^{-1} >= 0 (y = -x substitution; checked exactly n <= 60, m <= 3000).
A2 E-O split. g_7(-q) = E(q) - O(q), E = sum_k T_{2k}, O = sum_k T_{2k+1}, T_n(q) = q^{n^2} (-q^7;q^14)_{ceil(n/2)} / (q^{14(floor(n/2)+1)};q^14)_{ceil(n/2)}, each T_n with non-negative coefficients.
A3 Ladder. T_{2k+1} = T_{2k} q^{4k+1}/(1-q^{14k+7}) and (1+q^{14k+14}) T_{2k+2} = q^{4k+3} T_{2k+1}; hence coefficientwise E_d <= O*_d := sum_{n odd} a_n((d-(n+1)^2)/7), d >= 1.
L1 Ladder at fixed m. A_{2k+1} = A_{2k}/(1-x^{2k+1}) and A_{2k+1} = (1+x^{2k+2}) A_{2k+2}; so a_{2k+1}(m) >= a_{2k}(m), a_{2k+2}(m) (odd layers are local maxima in n).
L2 Mod-7 obstruction. [q^d]T_n, [q^d]T_{n'} both nonzero only if n' = +-n mod 7; no term-by-term positivity certificate inside a layer pair (n, n+1).
L3 Pole-order obstruction. For layers n, n' >= 3 and fixed shift s: if ceil(n/2) > ceil(n'/2), a_n(m) <= a_{n'}(m+s) fails for all large m; if s < 0 it fails at m = 0 (n = 2 is a genuine exception).
Exact range. O_d > E_d exactly for every allowed d in (1127, 10^6]. Last d with E_d >= O_d: 1127 (class 0), 407 (class 1), 247 (class 2), 60 (class 4).
Effective growth (computer-assisted). For allowed d >= D0: 0.398263 sqrt(d) - (3/4) log d - 2.99 <= log|g_7(d)| <= 0.39900 sqrt(d) + (1/2) log d + 1.11 + log(1 + d^{-1/2}). (Pins the exponent to [0.398263, 0.398875]; not the multiplicative asymptotic.)
Closed forms, as algebraic identities only. With y the root of y^7 + y^2 = 1: max_alpha min_u F = sqrt((Li2(y^2) + 7 ln^2 y)/7) = 2 sqrt(V/7), and (1 - sqrt(1-y^2))/y = (1 - y^{3.5})/y. That these are the growth exponent and lim E/O is Cat B.
Lever 1 (Cat A part). g_1 = 5th-order f_0 and g_2 = 3rd-order phi by definition (HM eqs. (4.11)/(4.5)); HM (0.3) matched by exact coefficients through q^200; HM (4.5) third line matched through q^180. No known identification exists for s = 7, 8, 11 on Master or in the classical lists checked (absence of a known identity, not a non-existence proof).
Moved to Cat B (judgment, per source md). "No terminating Bailey pair for s >= 3" rests on truncated computations and a non-exhaustive search; it is Cat B in the Levers 1-2 md and is recorded in the Cat B notes, not here.


5. Unchanged open items

C_third alone (positive-cone remainder). Object B. Per_off. Remark 8.5. Slash_two. QM of g_s for s = 7, 8, 11 (CONJECTURE). Two-sided effective bound on E_d/O_d (not achieved).


6. Hygiene

Pure copy-and-create. No existing Master file modified, renamed or deleted. Source reports copied verbatim.
Computer-assisted; one audit; not a formal verification. No TPC or RH claim. Distinct from HQCC termination claims. Residual is not Resonant (539 is a count). CORE_FREEZE untouched.
