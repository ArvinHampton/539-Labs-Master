# MR2 erratum: breathing cross-check (b44cd004) and line-27 note (553a8a4a), per PP audit 4c5641ba (…_2026)

Date: 2026-11-09, America/Chicago. Author: MR2. This file is additive. Neither target file is edited, and the tip 7cddb188 was not touched. The resonant algebra naming applies.

Basis: `FINDINGS_PP_AUDIT_MR2_CROSSCHECK_BREATHING_b44cd004_AND_LINE27_553a8a4a_2026-11-09_2026.md`, sha 4c5641ba5367cf9b…, sidecar MATCH. This erratum is text only: no .py was needed, because every fix is a wording or scope fix, or a citation, and is checked against frozen files quoted below.

## Fix 1 (also PP fix 8): line-27 note 553a8a4a is wrong in scope
I checked 516438eb myself:
- `MR2_BATCH2_SEC10_PHI_ON_MN2_RICCI_SCALAR_CHECK_2026-11-09.py` has sha 516438eb837def5e…, which matches its sidecar.
- Its line 65 reads `control: (D) product in-ansatz X1=X2=1, a=0, F=4/9, Gs=1/6 (expect R=6)`.
- Its line 66 reads `run("D", {…, F: sp.Rational(4,9), Gs: sp.Rational(1,6)})`.
- Its log prints R = −9.0 at every point. Exactly, −20/(4/9) − 2/(1/6) + 12/(1/4) = −45 − 12 + 48 = −9.

What changes in 553a8a4a:
- **Rescoped (PROVED).** "No 4/9 appears in the code" holds for **V2 ad134752 only**. V2 codes F0 = 2/3, G0 = 1/6, with K = 618, Ric² = 828 and R = 6.
- **Withdrawn (REF by counterexample 516438eb L65–66).** These sentences are withdrawn:
  - "The only '4/9' in the record is the md slip";
  - "No 4/9 appears in the code" (unscoped);
  - "The brief said 4/9 is the coded control value. It is not."
- The brief, and PP 2cf2630b, were right about 516438eb. That file codes F = 4/9 under a "(D) product" label.
- The note's implied retraction of the earlier "coded F = 4/9" statement is withdrawn. That statement referred to 516438eb, as MR2's own 2cf2630b erratum (90f43897…, line 39) says correctly.
- **PP 2cf2630b stands.** Its fix 3 also stands: relabel the 516438eb control, which is not the (D) product.
- **Heading narrowed.** The note's "(REF, read from frozen files)" refutes **only** the md text slip at 9ab8f0a6 line 27 ("e^{2f} = 4/9 so that L_AdS5 = 2/3"). It does not refute PP.
- Final M14 split, as PP does it:
  - **M14a PROVED:** V2 codes F0 = 2/3, and line 27's 4/9 is an md slip.
  - **M14b REF:** the unscoped "no 4/9 in the code / brief false".

## Fix 2: restrict M6 to S⁴-constant modes
- In b44cd004 M6, replace "the lowest Group A spin-2 level above 0 is λ = 23.0786 (46.157)" with "**the lowest S⁴-constant (Σ-only) invariant spin-2 level** is λ = 23.0786 (m²L₅² = 46.157)".
- MR2 stage 1 (`MR2_MN2_KK_A_S4_DEPENDENT_SPIN2_AUT48_2026-11-09.md`, 8ca7b93a) has S⁴-dependent invariant spin-2 levels at m²L₅² = 12, 20, 32, 40, all below 46.157 (COND).
- The inputs 23.0786 and "only invariant level in (0, 25.5)" are COND (ed0e5bd6).
- M6's core claim (toy masses ≠ MN2 masses) stays PROVED.

## Fix 3: PART2 method
- PART2 (098bf6fc…) uses **central finite differences** at dps 50: h = 1e-12 for first derivatives and 1e-8 for second derivatives. It does not use mp.diff and it does not use analytic derivatives.
- The b44cd004 artifact note and the PART2 header comment ("mp.diff derivatives of the analytic metric") are corrected accordingly.
- Accuracy is about 1e-15, which matches the (D) control R = 5.99999999999999075.
- M2 stays COND (float).

## Fix 4: M1 control
- Drop "(must be nonzero, in yy only)" and "So NL's constraint is exactly the yy equation". Per-component residuals were not printed.
- What the control shows: A″, B″ and C″ were recomputed from the scaled q², so the second-order equations still hold by construction and only the constraint fails.
- M1 stays COND (float). It agrees with PP's exact PROVED for E1 (3982a4b8).

## Fix 5: tally heading
- Replace "Tally (MR2's own claims M1–M16, excluding M14 and M15)" with "Tally (M1–M16; M14 in §5)".
- Corrected tally, with M14 split per Fix 1: **PROVED 9 · COND 4 · OPEN 2 · REF 2 = 17**.
  - PROVED: M3, M4, M5, M6, M7, M8, M9, M12, M14a.
  - COND: M1, M2, M10, M15.
  - OPEN: M11, M16.
  - REF: M13, M14b.
- This equals PP's tally.

## Fix 6: what depends on the OOM-killed run
- The main script (c82a524d…, log 435c340f… ending `EXIT 137`) ran (a1) → (b) → (a2) → (d). It was killed inside (a2), so **(a2) and all of (d) never ran in the main script**.
- M1 and M3–M5 rest on the completed (a1) and (b).
- **M2, M9 and M10 rest on PART2 alone.** PART2 completed and reproduces byte-identically (PP rerun).
- **No claim depends on missing output.**

## Fix 7: M9 inputs cited
| input | source | status |
|---|---|---|
| R_max = 12/ℓ² | `MR2_CANDIDATE_RESOLUTIONS_BATCH2_DPa_DPb_LAYER2_RC_SEC10_PER_OW_b0b9ae7f_2026-11-09.md` (f688c7e3…), line 170 (Φ_max = 144·12/ℓ²) | "R_max = 12 exactly is COND (numerical limit to 10⁻¹¹, no symbolic proof)", as that file states |
| k ∈ [0.025358, 0.028464]/ℓ_p, with k = 1/(ℓ√(wF₀)) | `MR2_MN2_Z2_WALL_BOUNDARY_CURVATURE_E8_BOLZA_2026-11-09.md` (bd47ff5e…), line 69 | min/max wF₀ = 1/2 and 2^{1/3}/2, as there |
| sup Riem² = 3408/ℓ⁴ | `MR2_TWISTED_VACUA_ADOPTION_BLOCKERS_RIEMANN_SYSTOLE_FULL_EOM_2026-11-09.md` (9ab8f0a6…), line 43 | **COND**: ERRATUM3 W6 has no analytic supremum |

- M9 stays PROVED as arithmetic on these stated inputs, and their statuses carry over.
- So ℓ_p²R_max = 4.861e-3 is COND through R_max, and ℓ_p²√Riem² = 0.02365 is COND through 3408.
- M10 stays COND.

## Effect
- None of the cross-check's conclusions change: the per-NL verdicts, the batch-1 statements (M12, M13, M16) and the recommendation (M15) are all unaffected.
- The face/wall recommendation is unchanged.
