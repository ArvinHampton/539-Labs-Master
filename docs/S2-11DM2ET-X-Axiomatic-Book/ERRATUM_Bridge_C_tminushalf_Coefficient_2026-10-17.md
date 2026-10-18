ERRATUM
Bridge Series C: t^-1/2 coefficient of C, obstruction 2 for C, scalar W_7 reading, |G| pattern
2026-10-17

Pack+(S). Erratum only. Pure copy-and-create: no existing file is modified or renamed; no lock altered. CORE_FREEZE untouched. No HQCC, TPC or RH claim.
Applies to the Bridge C package pushed d9d2a00..cdded52 (main). Evidence: U1_LEDGER_P_s_Structure_RayClass_2026-10-17.md and P_s_Structure_2026-10-17/ (em.py, em_exact.py, closed_forms.py, em_check.py, hs_decomp_check.py, gauss_pattern.py, weil_test.py and outputs).
All cited lines verified on main at cdded52. Paths below are under docs/S2-11DM2ET-X-Axiomatic-Book/.


E1. t^-1/2 coefficient of C

Was: about 0.8174 (numerical fit). Read:
a_C = sqrt(pi)(833 + 204 sqrt14 - 14 sqrt1190)/2380 = 0.8291426171...
(explicit Euler-Maclaurin expression evaluated to 30 digits; radical form identified by PSLQ at 30 digits; confirmed numerically, remainder ~ sqrt(t) down to t = 2.5e-5). The earlier fit was biased.
Lines:
- CatB_Notes_Bridge_C_Residual_Law_2026-10-17.md lines 23-24 (B4 "t^{-1/2} coefficient of C (fit only) ... About 0.8174 ... Not derived analytically").
- Bridge_C_Residual_Law_2026-10-17/2026-10-17-Bridge-C-Residual-Law.md line 174 (B4, "about 0.8174 from the fit") and line 197 (next step (c), now done).
- CatB_Notes_Bridge_C_Residual_Law_2026-10-17.md line 37 (OPEN "Analytic t^{-1/2} coefficient of H_s / C"): now closed up to the PSLQ identification of the radical form; H_s: a_H = sqrt(pi)(sqrt1190 - 17 sqrt14)/170.


E2. Obstruction 2 for C upgraded to Cat A over the complex numbers

Since a_C != 0, C * g = F is impossible for holomorphic modular g != 0 and F of any weight, level or multiplier, with arbitrary complex coefficients (same argument as for C_third). Cat A; the nonvanishing rests on the 30-digit value 0.8291..., far from 0.
Lines:
- U1_LEDGER_Bridge_C_Residual_Law_Obstruction_2026-10-17.md line 50 ("C * g != F with complex coefficients: NOT claimed here (Cat B ...)"): read as Cat A.
- Bridge_C_Residual_Law_2026-10-17/2026-10-17-Bridge-C-Residual-Law.md line 21 ("With complex coefficients it is Cat B"): read as Cat A.


E3. Scalar W_7 failure explained (obstruction 3 verdict stands)

The leading 1/t radial profiles obey the weight-1 Weil law (S and T) on the 35-element discriminant group, on all tested points (Cat A as finite checks; the general proof is Cat B). Under that law W_7-type maps mix components, so a scalar relation between G(x) and G(-1/(7x)) is not expected; the zero-pattern and phase mismatches are vector mixing, not a contradiction with modularity of the vector.
The verdict of obstruction 3 is unchanged: no scalar W_7 / Fricke law at any weight and constant lambda.
Lines (read with this explanation):
- U1_LEDGER_Bridge_C_Residual_Law_Obstruction_2026-10-17.md lines 53-58 (obstruction 3) and lines 65-66 (verdict; "open route is VECTOR-VALUED").
- Bridge_C_Residual_Law_2026-10-17/2026-10-17-Bridge-C-Residual-Law.md lines 22-25 and 144-148 (scalar W_7 slash obstruction).
Status of the vector-valued route now: leading order holds on all tested points; an exact vector-valued modular law with algebraic data is ruled out by Baker; the quadrant-cone vector fails at order t^-1/2; beyond leading order with fundamental-domain cones is OPEN (Cat B evidence only). See the P_s ledger, section 6.
- CatB_Notes_Bridge_C_Residual_Law_2026-10-17.md lines 15-16 (B2 vector-valued law "Not attempted"): leading order now checked as above.


E4. |G| pattern proved

Was: observed only (m < 30). Now PROVED (Cat A): G(h/m) = 0 if 2 | m or 5 | m; |G(h/m)| = 1/m if gcd(m,70) = 1; |G(h/m)| = sqrt7/m if 7 | m and gcd(m,10) = 1 (verified on all 3374 coprime pairs with m <= 105).
Lines:
- CatB_Notes_Bridge_C_Residual_Law_2026-10-17.md lines 10-11 (B1 "|G| pattern (observed only) ... Not proved") and line 37 (OPEN "Proof of the |G| pattern").
- Bridge_C_Residual_Law_2026-10-17/2026-10-17-Bridge-C-Residual-Law.md line 112 and self-audit line 182 ("observed for m < 30 and not proved").


Unchanged. Obstructions 1 and 3 and the shared-remainder identities of the Bridge C ledger. No claim that C, C_third or E is quantum modular.

Hygiene. Corrections of reading and status only. Cat A / Cat B separation as in the ledgers and Cat B notes. CORE_FREEZE untouched.
