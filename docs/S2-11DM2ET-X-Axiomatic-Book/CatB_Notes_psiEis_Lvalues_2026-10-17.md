CATEGORY B NOTES
psi_Eis Herglotz form and cusp-row L-values, 2026-10-17
Every item in this file is CATEGORY B (unproved step, cited theory, interpretation) or OPEN. Nothing here is a lock.
Companion to U1_LEDGER_psiEis_Herglotz_and_Cusp_Lvalues_2026-10-17.md.
Source (verbatim copy). psiEis_Lvalues_2026-10-17/.

Caveats. No HQCC, TPC or RH claim. Residual is not Resonant (539 is a count). CORE_FREEZE untouched.


B1. E_R cancellation (not proved)
- Step 4 of the derivation: the Lambert-series remainder, summed over the 8 genus characters, cancels against (z/sqrt35) E_R(z). Expected to be the Gauss-sum (Poisson) duality, i.e. the S-law. Verified only through the end identity (33 digits on the real axis; complex points). Not written out. Until it is, the full Herglotz identity is numerically verified with proof pending.

B2. u_R's Eisenstein basis (unidentified)
- er_fit.py: a naive fit of u_R's coefficients to genus-pair divisor sums failed (residual 4). u_R is Eisenstein (Cusp-Part ledger) but its own Eisenstein basis was not identified. Not needed for the closed form.

B3. Lewis-Zagier readings
- R_chi as the Lewis-Zagier Eisenstein period function at s = 1/2 for (psi, psi') (LZ Ch. IV): interpretation, not checked.
- Central values L(1/2, u_chi) as Mellin/integral data of Phi rather than point values: standard LZ expectation, not tested.
- Functional equations of the individual R_chi (Radchenko-Zagier style): not derived.
- The Gamma-factor zero pattern (type (0,0) double zero at s = 0; mixed L(0) = 0): Hecke functional equation as theory; observed in PARI values.

B4. PARI lfun
- Correctness of PARI's lfun is assumed; internally consistent (functional equation to 1.8e-15; Bernoulli values reproduced to ~1e-14).

B5. Citations and status
- Zagier, A Kronecker limit formula for real quadratic fields, Math. Ann. 213 (1975): context only; NOT checked online this session.
- Radchenko-Zagier, J. reine angew. Math., doi:10.1515/crelle-2023-0009, arXiv:2012.15805: checked online in the previous session.
- Lewis-Zagier, Ann. Math. 153 (2001), arXiv:math/0101270: verified earlier.
- Maass, Math. Ann. 121 (1949) 141-183: bibliographic data verified.
- Hecke functional equation for Grossencharaktere: cited generically.


OPEN
- Proof of the E_R cancellation (B1).
- Algebraicity of individual R_chi at rationals.
- u_R Eisenstein basis (B2).
- Hand redo of the class assignment mod p2^3 p5 p7 used in the Cusp-Part fits (the group at (2 sqrt35) is now hand-certified).
- Written EM / interchange error terms (unchanged from the Cusp-Part notes B5).
- Maass/Hecke status of the 12 forms (unchanged, Cusp-Part notes B1).
- s = 8, 11 analogues (unchanged).
- Unchanged: C_third alone; Object B; Per_off; Remark 8.5; Slash_two; QM of g_s.

Hygiene. CATEGORY B throughout. No HQCC, TPC or RH claim. CORE_FREEZE untouched.
