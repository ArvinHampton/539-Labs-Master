# AMEND — MR1 S2–S4 close of B§III Appell→R_c, revised per PP audit
Date: 2026-11-09 (America/Chicago). Author: Math Research 1. This file is additive. It does not overwrite anything.
Amends: `FINDINGS_MR1_B_SEC3_APPELL_RC_S2_S4_CLOSE_ADOPTED_DEFS_2026-11-09.md`, sha 48a2d68710e8ca7725ac064237641abaac1ca184f2f8977486988560a0741dfb.
PP audit: `FINDINGS_PP_AUDIT_MR1_S2_S4_APPELL_RC_2026-11-09_1516.md` (66a69888…). Verdict MATCH, sidecar OK, no numerical errors. All PP fixes below are adopted as given.
Authority: Owner blueprint 5a6e7177 (O6), with κ fixed as an Owner definition (OW 45aeba5f / 5a6e7177).
Limits: tip 7cddb188… untouched; no CERT; nothing sent outside; no Gemini.

## Changes
1. **R1, PROVED (unchanged).** PP certified it with PARI (bnfcertify = 1). The field discriminant is 140, O_K = ℤ[√35], and the fundamental unit ε = 6+√35 has norm +1. So Λ₀ = Reg/√10 = 0.7835772176.
2. **R2, PROVED. The basis is changed.** The proof now rests on the PARI-certified h(140) = 2 and the Dirichlet class number formula: L(1,χ₁₄₀) = 2·h·Reg/√140 = 2 ln ε/√35 = 0.83767928… (PARI lfun agrees to about 77 digits). Therefore Λ₀ = √(7/8)·L(1,χ₁₄₀). The 2·10⁶-term partial sum (h ≈ 1.999995) is kept as supporting evidence only, not as proof.
3. **S2a is now "CLOSED BY DEFINITION", not PROVED.** R_c is an Owner definition, so B§III does not need a derivation for R_c to be well-defined.
4. **S3b is no longer REFUTED.** It now carries three separate labels:
   - 1.59543 ≠ κ: PROVED. The difference is κ − 1.59543 = 2.19×10⁻³.
   - B's value is SUPERSEDED by the Owner definition of κ.
   - B's Appell–Lerch evaluation is OPEN, because the object it refers to is undefined.

   Remark: B's 1.59543 (lines 31–32, no computation shown) would imply Λ₀ = 2/1.59543² = 0.785732. This matches Pack H, which makes it a third unsourced value, alongside 0.7858 and the adopted 0.7835772.
5. **S4a now has a single label: CONDITIONAL.** The condition is the Owner's adopted definitions. κ is then a closed form in ln(6+√35) and √10 with no fitted input, and R_c depends further only on ℓ_P.
6. **The original file's line 26, "ties it to the Weil(140) side of Local's O1/O2", is now a REMARK.** It is not a result.

## Revised table
| Item | Label |
|---|---|
| S1 circularity | PASS (unchanged) |
| R1 Λ₀ = Reg(ℚ(√35))/√10 | PROVED (PARI-certified) |
| R2 Λ₀ = √(7/8)·L(1,χ₁₄₀) | PROVED (certified h=2 + class number formula) |
| S2a R_c well-defined | CLOSED BY DEFINITION |
| S2b Appell–Lerch link | OPEN |
| S2c tree spectral-radius match | OPEN |
| S3a κ = 1.5976222400652… | PROVED |
| S3b 1.59543 ≠ κ | PROVED; B's value SUPERSEDED; B's Appell–Lerch evaluation OPEN |
| S3c old 0.7858 / 1.5954 / 0.785732 inputs | FLAG: downstream values to be recomputed |
| S3d units (R_c/ℓ_P = κ) | PROVED |
| S4a no empirical input | CONDITIONAL (on Owner definitions) |
| S4b physical derivation | OPEN |
| S4c √10 normalization | OPEN |
| Weil(140) tie | REMARK |

Local's note: Local independently confirmed R2. Local also reports that its earlier verdict Λ₀ ≠ π/4 (aca84cf4…) no longer depends on rounding, since 0.7835772 ≠ 0.7853982. MR1 agrees with this. No CERT.
