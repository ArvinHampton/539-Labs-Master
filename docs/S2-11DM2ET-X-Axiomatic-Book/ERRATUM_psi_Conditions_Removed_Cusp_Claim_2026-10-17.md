ERRATUM
Withdrawal: "u_L's negative frequencies carry a nonzero dihedral cusp part"
2026-10-17

Erratum only. Pure copy-and-create: no existing file is modified or renamed; no lock altered. CORE_FREEZE untouched. No HQCC, TPC or RH claim.
Applies to the psi conditions-removed package pushed a814a86..2ba5641 (main). Evidence: U1_LEDGER_Cusp_Part_2026-10-17.md and Cusp_Part_2026-10-17/ (ideal_counts.*, eis_decomp.*, genus_chars.*, fitF.*, component_split.json, cusp_checks.*, equiv_check.*).
All cited lines verified on main at 2ba5641. Paths below are under docs/S2-11DM2ET-X-Axiomatic-Book/.


W1. Claim withdrawn

WITHDRAWN: "Negative frequencies [of u_L] carry a nonzero dihedral cusp part", and "u_L and u_R = sqrt35 u_L o S have nonzero cusp content".
Cause: psi_Conditions_Removed_2026-10-17/split_neg.py counted only the cone T+ and omitted its partner T- = -(T-cone). T+ alone shows 6 of 48 non-constant residue classes mod 280; T+ together with T- shows 0 of 48 (Cusp_Part_2026-10-17/ideal_counts.txt). The negative-norm vectors of u_L lie in the two classes (1,1) (T+) and (5,1) (T-), not in the single class [1,1].
Correct statement: u_L and u_R are pure Eisenstein, at positive and negative frequencies (Cat A; exact coefficient match for every n <= 60,000, plus a hand proof independent of PARI). Hence the scalar psi has psi_cusp = 0, psi = psi_Eis. The cusp part of the 72-dim family lives in the 24 components with beta = -a and 7-denominator alpha in a + L' (12-dimensional), not in u_L or u_R.

Lines:
- U1_LEDGER_psi_Conditions_Removed_2026-10-17.md line 80 ("Negative frequencies carry a NONZERO dihedral cusp part ... Hence u_L and u_R = sqrt35 u_L o S have nonzero cusp content"): withdrawn. Line 81 ("The explicit split and eigenform identification are Cat B (notes B1)"): the split is now done (Cusp Part ledger, sections 2-5). Line 79 (positive frequencies pure Eisenstein, conditional on PARI): stands, and is now independent of PARI.
- CatB_Notes_psi_Conditions_Removed_2026-10-17.md lines 10-13 (B1: "The negative-frequency pieces are expected to be Maass's dihedral lambda = 1/4 cusp forms ...", "the cusp part must be an even/odd combination with vanishing positive coefficients", "The split psi = psi_Eis + psi_cusp was not computed") and line 22 (OPEN "Cusp eigenbasis and psi_Eis / psi_cusp split"): superseded; psi_cusp = 0 for the scalar psi; the cusp eigenbasis is in the Cusp Part ledger section 5.
- psi_Conditions_Removed_2026-10-17/2026-10-17-psi-Conditions-Removed.md section 4.2, lines 158-162 ("Negative frequencies: nonzero dihedral cusp part" through "vanishing positive coefficients") and line 166 (Cat B split), plus the summary table line 14 and line 21: withdrawn / superseded as above.
- PUSH_LOG_2026-10-17_psi_Conditions_Removed.md line 18 ("nonzero dihedral cusp part at negative frequencies"): withdrawn.
Same expectation, read with this correction (earlier package):
- CatB_Notes_psi_Cocycle_2026-10-17.md line 19 ("u_R ... presumably decomposes into lambda = 1/4 Eisenstein and dihedral cusp forms"): u_R is pure Eisenstein.


W2. Premise adjusted

Mod p2 p5 inf1 inf2 the non-sigma-invariant characters have mixed sign type and cancel in the full lift; they are not lambda = 1/4 Maass characters. Pure-type (Maass) cusp characters first appear at modulus (2 sqrt35) inf1 inf2.


Unchanged. Sections 1-4 of the psi conditions-removed ledger (C1, C2 discharged; 140-label family; 72-dim representation; all rows; zeta(-1,K) = 29/60), and the positive-frequency Eisenstein statement.

Hygiene. Withdrawal and correction only. CORE_FREEZE untouched.
