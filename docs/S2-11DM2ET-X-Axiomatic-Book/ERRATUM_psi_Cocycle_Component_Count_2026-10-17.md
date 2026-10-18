ERRATUM
psi cocycle: component count, representation wording, rows checked, conditions C1 and C2
2026-10-17

Erratum only. Pure copy-and-create: no existing file is modified or renamed; no lock altered. CORE_FREEZE untouched. No HQCC, TPC or RH claim.
Applies to the psi package pushed 7519051..c860089 (main). Evidence: U1_LEDGER_psi_Conditions_Removed_2026-10-17.md and psi_Conditions_Removed_2026-10-17/ (family.py, dump_matrices.*, labels.txt, slaw_check.*, rows_check.*, lemma_symbolic.*).
All cited lines verified on main at c860089. Paths below are under docs/S2-11DM2ET-X-Axiomatic-Book/.


E1. Component count and representation

Was: a "36-component" vector / "36 rows", with the leading-order law described as the weight-1 Weil representation on the 35-element discriminant group.
Read: Z^2 with Gram [[2,7],[7,7]] is an ODD lattice. The closed family has 140 labels (alpha in ({0,a}+L')/Z^2, beta in {0,-a}), with the characteristic-vector T-law u_{alpha,beta}(w+1) = e(-Q(alpha) - B(alpha,w_c)) u_{alpha,alpha+beta+w_c}(w), w_c = (1/10,-1/35). The P-invariant subspace is 72-dimensional and carries a representation of PSL2(Z) (S^2 = I, (ST)^3 = I). The 36 earlier components are not closed under T.
Lines:
- CatB_Notes_psi_Cocycle_2026-10-17.md line 11 ("Only the (a,0) row of the 36-component S-cocycle was computed ... the other 35 rows were not checked numerically").
- psi_Cocycle_2026-10-17/2026-10-17-psi-Cocycle.md line 124 (B2, "every row of the 36-component vector").
Same wording, read with this correction (not part of the psi package):
- U1_LEDGER_P_s_Structure_RayClass_2026-10-17.md line 78 ("weight-1 Weil representation, 35-element discriminant group").
- P_s_Structure_2026-10-17/2026-10-17-P_s-Structure.md line 26 ("36-component family obey the exact weight-1 Weil law"), line 124 ("weight-1 Weil representation on the 35-element discriminant group"), line 133 ("all 36 components' data").
- ERRATUM_Bridge_C_tminushalf_Coefficient_2026-10-17.md line 31 ("weight-1 Weil law (S and T) on the 35-element discriminant group").
Note. The leading-order T-law tested in the P_s report (A5, line 123) already carried a characteristic shift, (1/2)A^{-1}A* = (1/2, 0), which is congruent to w_c mod L' (A((1/2,0) - w_c) = (1,3)); the finite numerical checks there stand. What changes is the description of the closed family and the representation it carries.


E2. All rows now checked

Was: only the (a,0) row checked.
Read: all 140 rows checked (S-law 1.2e-15, T-law 7e-16, closed forms 2.3e-14, three-term cocycle relation 7e-15): numerical verification of derived formulas.
Lines:
- U1_LEDGER_psi_Cocycle_LewisZagier_2026-10-17.md line 79 ("Only the (a,0) row of the S-cocycle was computed (Cat B note B1)") and line 84 ("Rows other than (a,0)").
- CatB_Notes_psi_Cocycle_2026-10-17.md line 11 (B1) and line 27 (OPEN "Rows other than (a,0)"; also "independent check of zeta(-1,K)", now done by 5 Shintani cones).


E3. Conditions C1 and C2 discharged

C1 (C = -pi/2): written proof. C2 (S-law u_L(-1/w) = u_R(w)/sqrt35): Poisson-summation proof independent of Borcherds. C3 and C4 are no longer needed for the S-law. C5 (non-tangential / uniform sectorial EM) remains, together with the unwritten Fourier-sum / Green-integral interchange; PARI's ray-class routines are not certified (affects only the Eisenstein/cusp statements).
Lines:
- U1_LEDGER_psi_Cocycle_LewisZagier_2026-10-17.md lines 18-19 (C1, C2), lines 20-21 (C3, C4), and the dependency labels at line 26 ("conditional on C2, C3"), line 35 and line 52 ("conditional on C1-C5"), line 57 ("conditionally on C1-C5"), line 79 ("CONDITIONALLY on C1-C5").
- CatB_Notes_psi_Cocycle_2026-10-17.md line 26 (OPEN "Symbolic derivation of ... C = -pi/2 and of the S-law ... (conditions C1, C2)"): closed.
Read those labels as conditional on C5 and the interchange only.


Unchanged. Every numerical value and formula in the psi ledger; zeta(0,K) = 1/10, zeta(-1,K) = 29/60; the s = 8, 11 statements and their Cat B status.

Hygiene. Corrections of wording and status only. CORE_FREEZE untouched.
