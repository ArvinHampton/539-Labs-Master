# NL DERIVED: Y15. Can mirror-pair E₈ stress plus the wall content satisfy the fibre Israel equations at the odd HW-type wall on MN2?
Author: Non Local Path (NL). Everything below is an **NL derived proposal**. Nothing is adopted.

Authority: OW 9bb1858c (Y15); OW b0b9ae7f (t4407, verified); OW 19a88b19 (MN N=2 working vacuum, CONDITIONAL; junction UNSOLVED); OW f825dfff (face = ℤ₂ fixed plane, HW-type; G₄ odd given P-b); OW 36683379 (citations: math checked). Naming rule OW f1d167d1: no affected names appear.
Inputs: Y14 stage 2 (NL_DERIVED_Y14_NONBPS_E8_EXISTENCE_MN2_STAGE2_2026-11-09_1950.md), which keeps existence (CONDITIONAL), so Y15 is not moot. MR2 bd47ff5e (Israel weights −6k / 0 / −8k at the wall). NL 1655 J3/P3 (extrinsic curvature on constant-r faces). PP fe0c3d92 / 5374a906 (fibre-NEC no-go for every E₈ field, PROVED). NL Y16 1813 with erratum 14 (tr R² term).
Limits: new file only. No CERT, no Gemini, nothing sent, no agent messaged. Tip 7cddb188… before and after.
Script: /workspace/nl-junction-1851/y15.py and y15_run.log (sidecars).

## 1. Equations
- Odd ℤ₂ wall, IR side kept (NL 1655 P3): S_ab = −(2/κ²)(K_ab − h_ab K).
- **Y15-1 (PROVED; arithmetic cross-check with MR2).** At the exact MN2 IR face, k_Σ = k_fib = 0 and K = 4k_x with k_x < 0 (J3a). Put k := −k_x > 0. Then S^x_x = −6k/κ², S^Σ_Σ = −8k/κ², S^fib = −8k/κ²·δ. This is MR2's 6 : 8 : 8 (x : Σ : fibre), and S(ℓ,ℓ) = −2k/κ² for null ℓ = t̂ + ê.
- Wall content tested: (i) any E₈ field on the wall, i.e. fibre legs F_fib plus the forced Σ legs Φ·F_tw (stage 2 T1–T3), including every mirror pair and every single block; (ii) smeared M5s, S = −σP_wv on the 6D worldvolume, σ of either sign for I1 and σ ≥ 0 for I2; (iii) the HW tr R² term (Y16).

## 2. Two identities for E₈ + M5
Write ε_f = ½|F_fib|² and ε_Σ = ½|Φ|²|F_tw|² (physical metric, ≥ 0). The YM stress gives S^x_x = −ε_f − ε_Σ, S^Σ_Σ = ε_Σ − ε_f, and S^fib = τ − ε_Σδ, where τ is the traceless 4D YM stress of F_fib.
- **I1 (PROVED).** S^Σ_Σ − S^x_x = 2ε_Σ ≥ 0. M5s add nothing to this difference, because their stress is isotropic on x ⊕ Σ. The value of σ cancels.
- **I2 (PROVED; = PP fe0c3d92 / 1800 Y3-ineq, re-derived here with the Σ legs).** For ℓ = t̂ + ê with ê a fibre unit vector, S(ℓ,ℓ) = ε_f + ε_Σ + σ + τ(ê,ê) − ε_Σ = |F(ê,·)|² + σ ≥ 0 when σ ≥ 0. The Σ legs drop out because F_tw has no fibre index.
- **Required values** (any constant-r face): S^Σ_Σ − S^x_x = −(2/κ²)(k_Σ − k_x), and S(ℓ,ℓ) = −(2/κ²)(k_ê − k_x).
  - So E₈ + M5 can work only where k_Σ ≤ k_x **and** k_ê ≤ k_x for every fibre eigendirection ê.

## 3. Result at the IR face
- **Y15-IR (REFUTED, by proof).** Claim tested: "On the exact MN2 IR face, the stress of mirror pairs (or of any E₈ field) together with smeared M5s satisfies the Israel equations at the odd wall."
  - By I1 the wall needs 2ε_Σ = −2k/κ² < 0, which is impossible.
  - By I2 it needs S(ℓ,ℓ) = −2k/κ² < 0, which is impossible.
  - Either proof is enough on its own.
- **Y15-trace (PROVED, a third and independent inconsistency).** The fibre trace gives −4ε_Σ = −32k/κ², so ε_Σ = 8k/κ². I1 gives ε_Σ = −k/κ². These cannot both hold. So the twist's Σ legs can never be what fixes the 6:8:8 pattern; they push the Σ–x difference the wrong way.

## 4. Interior faces
- **Y15-int (CONDITIONAL; J1b flow, face.py grid 120×60).** On all 398 sampled faces along the flow, and on the listed faces R/R₀ = 1.0001 … 100, **both** necessary conditions fail at **every** S⁴ grid point (y15_run.log).
  - min(k_Σ − k_x) falls from +2.54×10⁻² ℓ_P⁻¹ (IR) to +1.7×10⁻⁶ (R/R₀ = 100), so it tends to 0 only at the UV.
  - min_S⁴ (max_ê k_ê − k_x) ≥ +2.01×10⁻² ℓ_P⁻¹ on every face, including the UV limit, where k_fib → 0 and k_x → −1/L₇.
  - So I2 alone excludes every face, with margin O(1/L₇).

## 5. With the tr R² term
- **Y15-R2 (CONDITIONAL on Y16's integrated bound standing in for the integrated null component).** Required at the IR face: ∫S(ℓ,ℓ)dvol₄/T_M5 = −(1/3)·12568.6 = −4189.5 M5 units. From P3c, ∫(2/κ²)·3k = 12568.6, so ∫(2/κ²)k = 4189.5.
  - E₈ and M5 contribute ≥ 0 (I2).
  - Y16's tr R² term is a fixed 2–5 units: about 1.1–2.4 at u=1, twice that at u=2 (erratum 14).
  - It falls short by a factor of about 10³ under either u, so adding it does not change the verdict.

## 6. Junction status
- Y15 answers **no**. Mirror pairs, single blocks, smeared M5s and the HW tr R² term cannot satisfy the fibre Israel equations at the odd HW-type wall on MN2. This is proved at the IR face and numerically on all interior faces.
- The MN2 junction stays **UNSOLVED**. It is now excluded for this whole class of wall content, not only for BPS sources.
- The count-gap result of stage 2 (closes in magnitude, CONDITIONAL) does not help, because the obstruction is pointwise and component-wise, not a matter of total tension.
- **J7-src (OPEN).** What remains are sources outside this wall content: G₄ legs or worldvolume flux on the wall, a non-BPS exterior (P2′), localized M5s (J5), or a different face. These are the inputs for the junction-source options list against PP aeb9ab13 under OW b0b9ae7f.

## 7. Next steps and ETAs
- Junction-source options for MN2 against PP aeb9ab13 (2–3 candidates each, per OW b0b9ae7f): 2–3 h. Each candidate must beat I1 and I2, i.e. supply S^Σ_Σ − S^x_x < 0 and S(ℓ,ℓ) < 0. Ordinary matter with positive energy cannot do the second.
- Per-direction check of the Y16 tr R² stress against I2, to replace the integrated bound in Y15-R2: about 1 h.

## Tally (header checked against the item lists)
| label | count | items |
|---|---|---|
| PROVED | 4 | Y15-1, I1, I2, Y15-trace |
| CONDITIONAL | 2 | Y15-int, Y15-R2 |
| OPEN | 1 | J7-src |
| REFUTED | 1 | Y15-IR |

Check: 4 + 2 + 1 + 1 = 8.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
