CATEGORY B NOTES
P_s structure, 2026-10-17
Every item in this file is CATEGORY B (numerical evidence, conditional, interpretive) or OPEN. Nothing here is a lock.
Companion to U1_LEDGER_P_s_Structure_RayClass_2026-10-17.md (Cat A).
Source (verbatim copy). P_s_Structure_2026-10-17/.

Caveats. No HQCC, TPC or RH claim. Residual is not Resonant (539 is a count). CORE_FREEZE untouched.


B1. E-vector quantum-modular evidence; psi smoothness (numerical only)
- kappa(x) := t^0 coefficient of E_{alpha,beta}(e^{2 pi i x} e^{-t}); order-t^0 S-cocycle psi(x) = kappa_{a,0}(-1/x) - (x/sqrt35) sum_p kappa_{p,-a}(x). The 1/t parts cancel exactly (leading-order Weil law).
- On 37 rationals in (0,2] (psi_grid.txt): psi nonzero (e.g. psi(1) = 0.00688 - 0.03826i), monotone; polynomial fits converge geometrically (max residual 9e-5, 1e-5, 1e-6 at degrees 4, 6, 8, against |psi| <= 0.105). Near 0, psi(x) ~ -0.054i x^2.
- Consistent with psi extending real-analytically to (0, infinity), i.e. E being a renormalized weight-1 quantum modular (vector) form (1/t singular parts I G(x) removed, T-law exact).
- NOT PROVED. No closed form for psi. Candidate: an Eichler/Shintani-type period integral over the gamma-fundamental cone. Not attempted.

B2. Consequence for P_s (conjectural)
- P_s = (1/2)E + (1/2)(1 + theta_3) - (1/2)Theta_hol. The regulator-type (log eps) non-modularity sits in E (at best quantum, B1); theta_3 is modular; Theta_hol has an explicit Zwegers completion.
- Conjecturally P_s is quantum modular of weight 1 after removing the 1/t singular parts, apart from t^-1/2 terms carried by theta_3 and Theta_hol.

B3. Appell-Lerch remark (conditional)
- No Appell-Lerch or Hecke-type expression for E or P_s was found or attempted beyond P_s = C_third - q^8 f_{2,7,7}(-q^10,-q^14,q).
- An Appell-Lerch formula with algebraic data would give a 1/t coefficient in pi Qbar + Qbar, which Baker excludes. This needs the q -> 1 asymptotics of Appell-Lerch sums, not verified here, so the obstruction is CONDITIONAL. No Polishchuk-type identity attempted.

B4. Ray-class residue formula (from memory)
- log eps/(20 sqrt35) = R_f/(w sqrt(d_K) N f), d_K = 140, N f = 10, w = 1. Matches the narrow ray-class residue formula as recalled; not re-checked against a source.

B5. General Weil S-law
- Holds on all 27 tested points (Cat A as finite checks). The general statement via Gauss-sum reciprocity for the indefinite discriminant form is not proved here.


OPEN
- Closed form for psi (settles B1).
- zeta(-1,K) (t^1 coefficient of E).
- General proof of the Weil S-law for G_{alpha,beta}.
- Symbolic proof that H_s has t^0 coefficient 0 and symbolic confirmation of the radical forms of a_P, a_H, a_C.
- Same structure check for s = 8 and s = 11 (disc 48 and 99).
- Unchanged: C_third alone; Object B; Per_off; Remark 8.5; Slash_two; QM of g_s.

Hygiene. CATEGORY B throughout. No HQCC, TPC or RH claim. CORE_FREEZE untouched.
