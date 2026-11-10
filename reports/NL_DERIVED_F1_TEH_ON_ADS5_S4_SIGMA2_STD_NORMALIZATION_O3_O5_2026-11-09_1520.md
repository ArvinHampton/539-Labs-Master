# NL DERIVED (F1, O3 + O5): T^(EH) on AdS₅×S⁴×Σ₂ with the standard flux normalization, 2026-11-09 15:20 CST
Author: Non Local Path (NL). New dated file; nothing edited. Tip 7cddb188… untouched. No CERT. Nothing sent outside.
Authority: OW 5a6e717732c413a39c89d9b95c9b17455ecf4da8dd64e8bb9d879f427e6a845c (NL go O3, O5; Λ₀ and R_c as definitions). Vacuum: OW 7708ec5d / RECORD 5b4592d4 (AdS₅×S⁴×Σ_g, CONDITIONAL). Parameters from PP 4660b73e, 4d07bd1b, 9dde377d.
Scripts: /workspace/nl-1511/f1_teh_vacuum.py (21e96ef9…), log f1_teh_vacuum.log (253b967a…). sympy for the 11D tensors, mpmath (30 digits) for numbers.
Everything below is CONDITIONAL on OW 5a6e7177 and OW 7708ec5d. N = 4880 and g = 2 are chosen inputs, not forced.

## 1. Block check of T^(EH) (PROVED, sympy)
Metric ds² = e^{−2ky}η + dy² + r²dΩ₄² + ρ²ds²(Σ), with r = √6/(4k), ρ = 1/(2k). Σ is treated locally as H² of radius ρ (Σ₂ = H²/Γ has the same local geometry).
- Einstein tensor, mixed components G^M_M: −6k² on all five AdS₅ directions (including y), +6k² on S⁴, −6k² on Σ. Off-diagonal Ricci vanishes. R₁₁ = 4k².
- Flux G = q vol(S⁴_r): G_MPQR G_N^PQR = 6q² g_MN on S⁴ and 0 elsewhere; G² = 24q².
- T^(EH)^M_M = (1/6)GG − (1/48)G² gives −q²/2 on AdS₅, +q²/2 on S⁴, −q²/2 on Σ. The standard stress T_std = (1/12)(GG − (1/8)gG²) gives exactly half: −q²/4, +q²/4, −q²/4.
- The block pattern (−, +, −) matches the Einstein tensor in every block, so a single constant closes all three blocks.

## 2. Convention that makes it consistent (PROVED)
- T^(EH) = 2·T_std identically (any F). So with the standard field G_std, quantized as ∫_{S⁴}G_std = (2πℓ_P)³N and with action (1/2κ₁₁²)∫(R − ½|G|²), the Einstein equation reads
  **G_MN = ½ T^(EH)_MN(G_std) = T_std(G_std)**, satisfied at q₀ = 2√6 k (all 11 components, residual 0).
- Equivalent form: G_MN = κ₁₁² T^(EH)_MN(F) with F := G_std/(√2 κ₁₁), i.e. the T^(EH) form arises from L_F = −(1/48)F² placed outside the 1/2κ² factor (NL 1232 item 11). In κ-absorbed units the F amplitude is 2√3 k = q₀/√2 (sympy solve).
- Using G_MN = T^(EH)(G_std) with the standard quantum on G_std fails: residual ±6k² in every block (PROVED, sympy). That reading would change k by 2^{−1/6} and breaks Dirac pairing, the same issue as PP 4660b73e A3. So O3 + O5 together fix the ½ convention above. This is NL derived, CONDITIONAL on OW 5a6e7177.

## 3. Numbers at N = 4880, g = 2, standard normalization (CONDITIONAL on the chosen inputs; arithmetic PROVED)
| quantity | value (ℓ_P units) |
|---|---|
| k = √(3/8)(πN)^{−1/3} | 0.0246505 ℓ_P⁻¹ |
| r (S⁴) = (πN)^{1/3} | 24.8422 |
| ρ (Σ₂) = 1/(2k) | 20.2836 |
| L_AdS = 1/k | 40.5671 |
| flux check q₀·Vol(S⁴_r)/(2π)³ | 4880.000 |
| Area(Σ₂) = 4π(g−1)ρ² | 5170.09 ℓ_P² |
| Vol(S⁴_r) = (8π²/3)r⁴ | 1.00237×10⁷ ℓ_P⁴ |
| internal volume V₆ = Vol(S⁴)·Area(Σ₂) | 5.18235×10¹⁰ ℓ_P⁶ |
| G₁₁ = (2π)⁸/(16π) = 16π⁷ | 4.83247×10⁴ ℓ_P⁹ |
| G₅ = G₁₁/V₆ (standard KK on M₆; not in 9dde377d) | 9.32487×10⁻⁷ ℓ_P³ |
| V₇eff = V₆(1 − e^{−2kb})/(2k), kb → ∞ (9dde377d B2/B3) | 1.05116×10¹² ℓ_P⁷ |
| G₄ = G₁₁/V₇eff, kb → ∞ | 4.59725×10⁻⁸ ℓ_P² |
| G₄ at kb = 0.8 (EH's "kb ≈ 0.80"), 1, 2 | 5.7602×10⁻⁸, 5.3168×10⁻⁸, 4.6830×10⁻⁸ ℓ_P² |
- b (the −U face position) is not fixed by any adopted record, so G₄ is OPEN beyond the kb → ∞ limit; the table only shows its b-dependence.
- These agree with PP 4d07bd1b §3 and 4660b73e C1 (r, k, L, ρ, area).

## 4. Λ₀ and R_c (definitions; values PROVED, comparison only)
- Λ₀ := ln(6+√35)/√10 = 0.7835772176. κ = √(2/Λ₀) = 1.5976222401. R_c := κℓ_P = 1.59762 ℓ_P. (Agrees with PP 4f370d8f.)
- Side fact (PROVED): 6+√35 is the fundamental unit of ℚ(√35) (6² − 35·1² = 1, and y = 1 is minimal), so ln(6+√35) is the regulator of ℚ(√35), the V₃₅ field of OW c290a274. No physical meaning is claimed.
- Comparison, not a match: r/R_c = 15.549, ρ/R_c = 12.696, L/R_c = 25.392. R_c is 1/12.7 to 1/25.4 of the vacuum lengths and sits at the Planck scale. No adopted equation ties R_c to the vacuum (PP 1ab88ebd B1 agrees). Its physical role is OPEN.

## 5. Sugra validity (CONDITIONAL on the EFT criterion lengths ≫ ℓ_P)
- N = 4880 ≫ 1 holds.
- Curvatures in ℓ_P⁻²: AdS₅ sectional k² = 6.08×10⁻⁴; S⁴ sectional 8k²/3 = 1.62×10⁻³; Σ₂ Gauss |−4k²| = 2.43×10⁻³ (largest); R₁₁ = 4k² = 2.43×10⁻³. (ℓ_P/r)⁶ = 4.25×10⁻⁹.
- All curvature radii are ≥ 20 ℓ_P, so the two-derivative sugra truncation is controlled at this N. A geometric object of size R_c = 1.6 ℓ_P (curvature 1/R_c² = 0.39 ℓ_P⁻²) would not be.
- Stability is not addressed here: PP 4660b73e C4 (probe-M5 instability) and C5 (non-SUSY, Ooguri–Vafa, a conjecture) stand. C5 stays OPEN.

## Labels tally
- PROVED 5: block pattern of T^(EH) vs Einstein tensor (§1); T^(EH) = 2T_std and the ½ convention closes all blocks (§2); the G = T^(EH)(G_std) reading fails (§2); arithmetic of §3/§4 values; regulator side fact.
- CONDITIONAL 4: the adopted convention (on OW 5a6e7177); all numbers at N = 4880, g = 2; sugra validity (EFT criterion); everything as a statement about the model (on OW 7708ec5d).
- OPEN 3: G₄ beyond kb → ∞ (b unfixed); physical role of R_c and Λ₀; C5 / full stability.
- REFUTED 0 (the failed reading in §2 is a convention mismatch, recorded as PROVED-fails, not a refutation of any adopted record).
NL derived proposal: the ½ convention statement in §2. Nothing here is Owner text.
