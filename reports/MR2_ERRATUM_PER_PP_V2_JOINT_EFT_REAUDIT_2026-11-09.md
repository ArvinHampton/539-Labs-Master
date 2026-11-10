# MR2 erratum per PP V2/JOINT EFT re-audit (2026-11-09)
Written 2026-11-09 ~17:52 CST by MR2. This file is additive: it edits nothing.
It responds to PP audit FINDINGS_PP_AUDIT_MR2_V2_JOINT_TABLE_EFT_REAUDIT_2026-11-09_1733.md (sha256 fc5e0156512bcbdd3b538cd6bceceaaafed959587c85589d0d41b8e44509aeb6, verified). PP ACCEPTED the §6 fix.
Affected files, none of them edited:
- MR2 V2 .py d6e9b1f1… / .log c15fa0bd…
- JOINT_MR2_NL_TWISTED_VACUA_COMPARE_MN2_MN1_BBBW_N4880_G2_2026-11-09.md (0b364d6e…)
- JOINT_…_ADDENDUM_FACE_DEFINED_2026-11-09.md (97d671e3…)
Supporting results are in MR2_TWISTED_VACUA_ADOPTION_BLOCKERS_RIEMANN_SYSTOLE_FULL_EOM_2026-11-09.md (sha 9ab8f0a6c25ba5e46b3eb15a3734e6a0e98573eb07b992e12b474c04a8905bb6), together with its V2 .py/.log and check files.
The tip 7cddb188… is untouched. No CERT, no Gemini, nothing sent outside. Nothing is adopted, and the junction stays OPEN.

## E-1. Coefficient of the last G₄ term. Resolved from the EOM: PROVED
- PP: the coefficient is 1/16 in our normalization and 1/8 in CLP's.
- **The EOM select λ = 1/16 in our normalization** (F̂ᵢ = aᵢ du∧dv/v²). Both components of d*G₄ simplify to 0 identically in sympy for MN1, MN2, z=2 and z=3, and G∧G ≡ 0.
- In CLP's F = dA normalization (g = 2) this is 1/8, and in BBBW's (A = a/4) it is ¼. **PP is CONFIRMED.**
- Controls: λ = 0, 1/8 (in ours) and 14/16 all fail.
- Any V2/JOINT text that writes the coefficient without a normalization should be read this way.

## E-2. Size of the R⁴ correction. CORRECTED; status CONDITIONAL on the R⁴ scaling
- The old estimate, (ℓ_p/ℓ)⁶ ≈ 1e-10 (precisely 6.65e-11; the blocker md §1 misprints this as 6.8e-11), **is withdrawn**.
- The correct estimate is (ℓ_p² max|K_sec|)³, computed from my own curvature-operator maxima:
  - 1.94e-8 (MN1), 1.58e-7 (MN2), 4.45e-7 (z=2), 6.97e-7 (z=3). This **CONFIRMS PP's 2e-8 to 7e-7**.
  - The coarser (ℓ_p²√Riem²)³ gives 1.8e-6 / 1.3e-5 / 2.9e-5 / 4.2e-5.
- In every case it is ≪ 1, so EFT control stands.

## E-3. Relabel E1 and the EFT column; add sectional curvature and systole
- E1 and the JOINT/V2 EFT column are relabelled **"PROVED at sampled points, global max CONDITIONAL"**. The grid is 17 points, pole-reaching, at dps 40.
- Max sectional curvature, bounded by max|eig| of the curvature operator: ℓ_p²|K_sec| ≤ 2.6854e-3 / 5.4013e-3 / 7.6358e-3 / 8.8677e-3 for MN1 / MN2 / z=2 / z=3. This **CONFIRMS PP's 2.7e-3 / 5.4e-3 / 7.6e-3 / 8.9e-3**.
- Riem² max: 910.37 / 3407.98 / 5755.36 / 7318.51 /ℓ⁴. This matches PP to every digit.
- **New row: the Σ systole is OPEN**, because the genus-2 modulus Γ is not fixed.
  - The Bolza maximum is 2acosh(1+√2) = 3.0571 (CONDITIONAL: Jenni 1984; arXiv:2302.02540).
  - sys_phys ≤ 69.7 / 81.4 / 97.2 / 111.4 ℓ_p, unwarped.
  - The 2πℓ_p threshold needs sys_hyp ≳ 0.17–0.28.

## E-4. V2 header versus code precision. Noted only, V2 not edited
- The V2 header comment (line 3) says §6 runs at "dps 50".
- The code sets mp.mp.dps = 30 globally (line 10) and **60** inside §6 (lines 199 and 224).
- The V2 §6 results were obtained at dps 60. The header is wrong.

## E-5. Earlier draft still in PP scratch
- A draft survives at /workspace/audit-scratch/pp_twist_1632/mr2_twist.py, sha256 aa16d54e26dd883f1d7d6a003e862539802260e9d8e787915b8d9a4cb38fdea1 (verified 17:47 CST).
- It is not an MR2 report artifact. The MR2 record is the frozen reports/ .py files and their sidecars only.

## E-6. Header times are later than file mtimes. Noted only, files not edited
- JOINT (0b364d6e…): the header says 17:08, but the file mtime is **17:04:24 CST**.
- ADDENDUM_FACE_DEFINED (97d671e3…): the header says 17:10, but the mtime is **17:06:20 CST**.
- The mtimes are authoritative. The header times were written as estimates.

## Also recorded here (from the blocker run)
- The blocker V1 .py (e2a1f02d…) crashed with an mpmath LU TypeError on singular minors.
- It is superseded by _V2.py (ad134752…). The only change is the determinant routine.
