# Run log — Lean 4.34 CatAVerify

Date: 2026-09-16
Scope: Category A residual discrete arithmetic only.
Toolchain: Lean 4.34.0 (elan 4.2.4), lake 5.0.0, no Mathlib.
Project: artifacts/S2-11DM2ET-X-Axiomatic-Book/formalization/CatAVerify/

## Command

export PATH="$HOME/.elan/bin:$PATH"
cd artifacts/S2-11DM2ET-X-Axiomatic-Book/formalization/CatAVerify
lake build

Result: Build completed successfully (6 jobs). Zero sorry.

## Lean theorems that compiled

T3 residue formulas, fixed point 0, cycle {1,2}, sample 0 through 300.
Packaging 18+521=539, (4880-21)/9=539, fibre 3*68+5*67=539.
Pairing 252+8424=8676.

Not verified: HQCC-as-physics, G4, g_s, C, OccFilt_7(infty), Object B, Per_off, RH.

CORE_FREEZE unchanged. No new residual-flux object.
