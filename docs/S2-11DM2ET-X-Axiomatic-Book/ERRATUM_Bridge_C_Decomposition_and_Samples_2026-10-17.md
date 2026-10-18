ERRATUM
Bridge Series C: decomposition range, coefficient set, Fricke samples, and the cone-sum wording
2026-10-17

Pack+(S). Erratum only. Pure copy-and-create: no existing file is modified or renamed by this note; no lock is altered.
Read the cited lines with the corrections below. CORE_FREEZE untouched. No HQCC, TPC or RH claim.
Evidence. Bridge_C_Residual_Law_2026-10-17/ (report, identities.py/.txt, diag.py, audit_misc.py/.txt, roots_of_unity.*, fricke_profile.*, w7_phase.*). Ledger: U1_LEDGER_Bridge_C_Residual_Law_Obstruction_2026-10-17.md.
All cited lines were verified on main at 495a0bc.


E1. C = C_axis + C_third holds only through q^293 (not as an identity)

C = C_axis + C_third + C_mixed, and C_mixed vanishes exactly through q^293 but not beyond (exact computation through q^3000).
First terms: C_mixed = -1/2 q^294 + 1/2 q^301 - q^330 + q^337 - q^368 + q^375 - ...
The -1/2 q^294 comes from the point (21,-1), which lies on the c2 wall n + 21k = 0 (weight 1/2), outside the orthant. Mixed-quadrant points such as (22,-1) at q^330 and (-22,1) at q^337 lie inside the H_s cones but outside the orthant.
Exactly: C_mixed = -H_s - q^8 f_{2,7,7}(-q^10,-q^14,q) - C_axis (checked through q^3000).

Coefficient value set. {0, 1, 3/2} holds through q^101 only. First coefficient 2 at q^102 (then 121, 170, 183, 196, 253, 289); first coefficient 3 at q^144; 1/2 appears from q^294. Value set through q^3000: {0, 1/2, 1, 3/2, 2, 3}. The residue support {0,1,2,4} mod 7 is correct for all terms.

Overstating lines (docs/S2-11DM2ET-X-Axiomatic-Book/):
- Residual_Law_for_Bridge_C_Status_Freeze_2026-08-24.md line 10: "Residual Bridge Series C := P_orth − H_s = C_axis + C_third". Read: = C_axis + C_third + C_mixed, C_mixed = 0 through q^293 only.
- Discrete_Bridge_E8_to_Fifth_Order_2026-08-24.md line 9: "Decomposition C7 = C_axis + C_third, coefficients restricted to {0,1,1.5}". Read: decomposition through q^293 only; coefficients in {0,1,1.5} through q^101 only.
- 42_Discrete_Contacts.md line 34 (contact 26): "C = P_orth - H_s = C_axis + C_third ... Coeffs in {0,1,1.5}". Same correction; the "locked" status of the contact is not altered by this note, only the reading of the decomposition and coefficient range.
Correct as written (no change needed):
- Pursue_All_C_Closure_Status_2026-08-23.md lines 45-46 (C = C_axis + C_third + C_mixed, C_mixed = 0 through degree 293) and line 48 (value set {0,1,1.5} through degree 80).
- Residual_Bridge_Series_C_Definition.md line 56 (value set {0,1,1.5} through degree 100).


E2. residual_slash automorphy factor has the wrong weight (for the leading singularity of C)

Residual_Fricke_Magnitude_Verification_Slash_C_2026-08-25.md line 24: residual_slash(x) := |7x|^{-1/2} * residual_factor(x).
The leading singularity of C at rational x is I * G(x)/t. On the common support of G(x) and G(-1/(7x)) the magnitudes obey an exact weight-1 relation, |7x|^{-1} * 7^{-1/2}, not |7x|^{-1/2}; off the common support (178 of 270 test rationals, including the sample point 5/7) no scalar relation of any weight holds. So |7x|^{-1/2} is not the weight of C's leading singularity. (This corrects the weight reading only; it does not claim the samples are wrong.)


E3. The Fricke samples are not radial values of C

The published complex sample markers (Residual_Fricke_Magnitude_Verification_Slash_C_2026-08-25.md line 19; the ratios derived from them are at line 16) do not match radial values of C, C_third or P_s: direct computation gives |C(0.995 e(x))| about 19.5, 18.5, 19.9, 54.0 at x = 1/7, 3/7, 5/7, 1, against sample magnitudes 19.80, 1.82, 9.24, 20.90. Their prescription remains unrecovered, as Master already says (Pursue_All_C_Closure_Status_2026-08-23.md line 50).
Radial values diverge like 1/t as rho -> 1, so they cannot serve as finite continuous targets; the finite targets are the singular coefficients I * G(x) (ledger, section 4).


E4. The 4-point recovery is a fit, not a test

residual_factor = a + bt + ct^2 + d/(1+t^2) has 4 parameters fitted to 4 ratios (interpolation determinant 36.14118 != 0). Reproducing the 4 ratios "to machine precision" is automatic and is not a test of the law. This agrees with U1_LEDGER_P_SLASH_Remark85_Interp_Prod_Obstruction_2026-09-01.md lines 36-37 ("interpolation uniqueness ... not uniqueness of residual_slash").


E5. Correction to our own 2026-10-17 wording: Q_+ is indefinite

Q_+ = Q_s = n^2 + 7nk + (7/2)k(k+1) is INDEFINITE (disc 35, signature (1,1)). It is positive only on the closed orthant. So sum_{n>=0,k>=1} q^{Q_+} is a cone partial sum of an indefinite form, not a "positive-definite-cone" sum, and it cannot be split by inclusion-exclusion into full lattice theta functions: the full-lattice sum sum_{Z^2} q^{Q_s} diverges.
Read "positive-definite-cone partial sum" / "positive-cone remainder" as "orthant (cone) partial sum of the indefinite form Q_+" at:
- U1_LEDGER_OCCFILT7_INF_THEOREM_L_Cthird_Zwegers_2026-10-17.md lines 65 and 121
- CatB_Notes_OccFilt7_Inf_Theorem_L_Cthird_2026-10-17.md line 77
- Executive_Summary_2026-10-17_OccFilt7_Inf_Theorem_L.md line 14
- Open_Paths_After_OccFilt7_Inf_Theorem_L_2026-10-17.md line 12
- OccFilt7_Inf_Theorem_L_2026-10-17/2026-10-17-Levers-1-2-Hecke-g7-Cthird.md lines 76 and 136 (verbatim session copy)
The conclusions there are unchanged: the remainder is not a theta function, and C_third alone is not shown to be mock modular (OPEN).

Hygiene. Corrections of reading only; no new claim about the objects beyond the cited computations. Cat A / Cat B separation as in the ledger and the Cat B notes. CORE_FREEZE untouched.
