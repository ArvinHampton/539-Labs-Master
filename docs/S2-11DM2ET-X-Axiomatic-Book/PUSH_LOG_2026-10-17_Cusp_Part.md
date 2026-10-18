PUSH LOG
Cusp part, 2026-10-17
Standalone push-log entry (pure copy-and-create; no existing PUSH_LOG or index edited).

Branch. main
Parent tip. 2ba5641b5e57eedb091890a50a4f6b91ead11924
Ledger commit. c8d1545 (1/10). Supporting files in commits 2/10 to 9/10 (the GitHub connector accepts at most 4 files per call). This log is commit 10/10 and cannot carry its own SHA without an edit; the SHA is reported in the session report.

Created (all under docs/S2-11DM2ET-X-Axiomatic-Book/):
- U1_LEDGER_Cusp_Part_2026-10-17.md (Cat A)
- CatB_Notes_Cusp_Part_2026-10-17.md (Cat B)
- ERRATUM_psi_Conditions_Removed_Cusp_Claim_2026-10-17.md (withdraws the u_L cusp claim of the package a814a86..2ba5641 without editing it)
- Cusp_Part_2026-10-17/ : 2026-10-17-Cusp-Part.md (verbatim report) + 16 .py + 13 .txt + 3 .json (verbatim)
- PUSH_LOG_2026-10-17_Cusp_Part.md (this file)

Skipped (binaries, logs, bytecode):
- class_counts.npy (7,680,256 bytes), lam.npy (7,680,256 bytes), region_counts.npy (1,920,160 bytes): NumPy binaries.
- fitF.pkl (56,833 bytes), cusp_chars.pkl (9,488 bytes): Python pickles.
- fitF.log (4,069 bytes), comp_genus_run.log (1,222 bytes): run logs (text, but not .py/.txt/.json/.md).
- __pycache__/ (family.cpython-313.pyc, uvec.cpython-313.pyc).

Verdict. u_L (and u_R) pure Eisenstein, independent of PARI; scalar psi = psi_Eis (psi_cusp = 0). The 72-dim family splits exactly as 60 Eisenstein + 12 cusp (S/T-equivariant); the cusp part lives in the 24 beta = -a, 7-denominator components, exact combinations of 12 dihedral forms from the 24 conductor-(2 sqrt35) pure-type characters. Earlier "nonzero cusp part of u_L" withdrawn (split_neg.py omitted cone T-).

Hygiene. Additions only. No locks altered. Cat A and Cat B in separate files. No HQCC, TPC or RH claim. Residual is not Resonant (539 is a count). CORE_FREEZE untouched.
