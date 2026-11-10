# Soft SF FINDINGS: PP audit of Local's Ξ / Fricke W₇ / Γ₀(49) proof-logic draft (Nov 9 ~12:20 CST) — CONFIRM with two fixes
Prepared 2026-11-09, audit ~12:30 CST (America/Chicago).

**Authority.** Owner DIRECT on Nov 9 at 12:29 CST, relayed by Physicist: additive new dated files only. No CERT. tip 7cddb188 untouched.

**Rollup CONFIRMED:** 9 PROVED (C1–C8, C18), 3 CONDITIONAL (C9–C11), 6 OPEN (C12–C17), 0 REFUTED.

## Focus items

### C7 — PROVED, citation FIX
- dim S₂(Γ₀(49)) = genus = 1, spanned by f = 49a1. This curve has CM by Z[(1+√−7)/2] and rank 0.
- Rank 0 gives root number +1, so f|W = −f.
- On H¹, tr W = −2, so the Lefschetz count is 2 − (−2) = 4 fixed points.
- Riemann–Hurwitz gives 0 = 2(−2) + r, so r = 4, and X₀(49)⁺ has genus 0 (C8).
- **FIX:** the E7 in MR1CD L29 is not this newform. Per bridges/LOCAL/FINDINGS_MR1_RESONANT_MATH_PREDICTIONS_NT_MODULAR_HECKE_HOLD_INVENT_2026-11-05.md L75–81, E7 is "V₃₅ ∩ D₇V₃₅ = 0", a leading-order result for the Γ₀(7) neighbor. Cite LMFDB 49.2.a.a or Cremona 49a1, together with Atkin–Lehner, instead.

### C9 — CONDITIONAL, correct
- Standard fact: W_m acts on J_{k,m} as (−1)^k. DMZ §4.6 was not re-read, so the label stays CONDITIONAL.
- **FIX (naming):** T:22 says DMZ's W₄₉ is the Jacobi operator and is not Fricke. C2's phrase "tip W₇ = Fricke W₄₉" should write W_49^Fricke, or τ ↦ −1/(49τ), so that C9 does not appear to constrain C2.

### C10 — CONDITIONAL, forced
- Read unrestricted, T:316's "scalar f|W₇ = ±f excluded" is REFUTED by C7 (49a1 satisfies f|W = −f).
- It is valid only as a constraint on the residual carrier V.

### C11 — CONDITIONAL on R26/R36, consistent
- W ∉ Γ₀(49) (C3), and det W = 49, so W ∉ SL₂(Z).
- Therefore the level-140 SL₂(Z) representation ρ (C14) does not define ρ(W) without a written extension.
- This is consistent with T:217 and T:309 (P2 VACATED).

### C18 — PROVED (Ligozat verified)
In each case the weight is 3, and Σδr and Σ(7/δ)r are both ≡ 0 mod 24:

| η-quotient | Σδr | Σ(7/δ)r | order at ∞ | order at 0 |
|---|---|---|---|---|
| h = (η(z)η(7z))³ | 24 | 24 | 1 | 1 |
| u = η⁷(z)/η(7z) | 0 | 48 | 0 | 2 |
| v = η⁷(7z)/η(z) | 48 | 0 | 2 | 0 |

The character is (−7/·), which is odd and consistent with the odd weight. Source: bridges/EIGEN/MR2-FINDINGS-DUAL-CONTINUE-gap-filtr-68_2026-10-27.md L14.

## Other items
- **C1–C6 and C8:** consistent.
- **C4 re-check:** index 56, 8 cusps, ν₂ = 0, ν₃ = 2, g = 1.
- **C12–C17:** remain OPEN (undefined or unwritten), not refuted.

REPORTS ONLY. No CERT.
