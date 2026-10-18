CATEGORY B NOTES
E_R cancellation / psi_Eis closed form, 2026-10-18
Every item in this file is CATEGORY B (context, interpretation) or OPEN. Nothing here is a lock.
Companion to U1_LEDGER_ER_Cancellation_psiEis_Closed_Form_2026-10-18.md (Cat A, audited once).
Source (verbatim copy). ER_Cancellation_2026-10-18/.

Caveats. No HQCC, TPC or RH claim. Residual is not Resonant (539 is a count). CORE_FREEZE untouched.


B1. Class-number-formula remark (context only; not used in the proof)
- For the trivial genus character, the constant cancelled in Prop. 7, (2/5) sum rho_n/(nz), is genuinely nonzero (0.0036057 + 0.0048075 i at z = 0.6 + 0.45 i). Numerically sum_n rho_n/n = i log eps/(70 pi) to 15 digits; this matches the class number formula for Q(sqrt35) with h = 2. Standard theory, not re-proved; context only.

B2. Lewis-Zagier interpretation
- R_chi read as the Lewis-Zagier Eisenstein period function at s = 1/2 for (psi, psi chi_140) (LZ Ch. IV): interpretation, not checked.

B3. Observed linear growth
- |Psi(z)|/|z| -> 0.0666 ~ log eps/(2 pi sqrt35) on S (audit growth.txt). Observation only; Lemma 8 proves the weaker C(1+|z|)^2, which suffices.


OPEN
- Arithmetic (Gauss-sum or ideal-theoretic) proof of Theorem 2; simplification of the imprimitive Gauss sums.
- Re-audit of the inputs (I1) genus decomposition, (I2) Poisson S-law, (I3) Green-form continuation (checked numerically only in this round).
- Hand redo of the p2^3 p5 p7 class assignment used in the Cusp-Part 60 + 12 split (still PARI).
- Certification of PARI lfun values used for the cusp-row L(0) identity.
- Algebraicity of individual R_chi at rationals.
- Maass/Hecke status of the 12 dihedral forms (Cusp-Part notes B1).
- s = 8, 11 analogues.
- Unchanged: C_third alone; Object B; Per_off; Remark 8.5; Slash_two; QM of g_s.

Hygiene. CATEGORY B throughout. No HQCC, TPC or RH claim. CORE_FREEZE untouched.
