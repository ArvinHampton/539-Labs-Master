Executive Summary
Lean 4.34 Category A verification
2026-09-16

Lean 4.34.0 installed via elan. Mathlib not installed.
lake build of CatAVerify succeeded. Zero sorry.

Verified in Lean: Canonical T3 definition and residue-class formulas,
packaging identities 18+521=539 and (4880-21)/9=539, fibre 3*68+5*67=539,
pairing integers 252+8424=8676. Finite T3 sample seeds 0 through 300
reach {0,1,2} within 400 iterates (computational certificate, not a
global termination theorem).

Python certificates ALL_PASS. Python also checks floor(e^3 * 243)=4880;
that identity is not a Lean theorem in this Mathlib-free build.

Not verified: HQCC-as-physics, G4, fifth-order series g_s and C,
OccFilt_7 at infinity, Object B, Per_off, RH, master equations.

CORE_FREEZE unchanged. No new residual-flux object.

Companion: artifacts/S2-11DM2ET-X-Axiomatic-Book/formalization/CatAVerify/
and RUN_LOG_2026-09-16_Lean_CatAVerify.md
