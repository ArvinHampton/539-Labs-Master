# NL DERIVED: Y16, the stress of the HW wall's −½tr R² term and whether it can supply the fibre-NEC violation
Author: Non Local Path (NL). Everything below is an **NL derived proposal**.

Authority:
- **OW 9bb1858c** (voice, 18:05; sha verified) directs pursuing Y14, Y15 and Y16, and calls Y16 the only route that could change the junction verdict.
- **The ordering "Y16 first" comes from Physicist's 18:05 relay, not from Owner text.**
- **OW 19a88b19** (18:06) has since lifted HOLD 587eca0c and adopted MN N=2 as the working vacuum, CONDITIONAL per PP 384096a8. NL adopts nothing. No source, b or vacuum is adopted here. The junction for MN N=2 stays UNSOLVED in that record.
- **PP fe0c3d92**, fix 1, is used here: Y3 in its k = t̂ + ê form.

Limits: Γ = Bolza (7ff8299d). No MR2 curvature numbers. No CERT. No Gemini. No outside services: the only citation is HW hep-th/9603142, whose title was checked on arXiv at 17:48. Tip 7cddb188 untouched.

Usage: 43.0% at the start and 43.9% at the halfway point.

Scripts, with sidecars, in /workspace/nl-junction-1806/: y16.py and y16_1812.log. The log reproduces the round-S⁴ value ∫Riem² = 64π² exactly, as a check of the code.

Conventions (PP):
- K_ab = ∇_a n_b, k_t := −K(t̂,t̂), S_ab = −(2/κ²)(K_ab − h_ab K) on the 10D Z₂ wall.
- ℓ_P = 1, 2κ² = (2π)⁸, T_M5 = (2π)⁻⁵.
- N = 4880 is **N_flux** (face.py: L₇ = 2(πN)^{1/3}). The face charge is 2N_flux = 9760.

## 0. Starting identity (PP fix 1)
- **Q15 (PROVED).** For a static face and k = t̂ + ê:
  - K(ê,ê) − k_t = −(κ²/2)[(1/λ²)tr|F(k,·)|² + S_M5(k,k) + S_R²(k,k)].
  - The E₈ term is ≥ 0 because F(k,·) ⊥ k, and the M5 term is ≥ 0.
  - **S_R² is the only term without a fixed sign.** The junction's fibre deficit needs K(fib) − k_t > 0, i.e. S(k,k) < 0.

## 1. The term
- **Q2 (CONDITIONAL, premise).**
  - The wall action is −(1/4λ²)∫√h (|F|² − ½Riem²), with Riem² = R_abcd R^abcd.
  - It uses the **intrinsic Levi-Civita curvature of the induced 10D metric h**. Extrinsic curvature enters only implicitly, through the Gauss equation. No explicit extrinsic, normal-bundle or flux-torsion (Ω₋-type) pieces are included. HW fix the tr R² combination by anomaly cancellation; its supersymmetric completion in the action is inferred, not quoted.
- **Q1 (CONDITIONAL).** The relative sign comes from the trace convention: tr F² and tr R² are taken the same way, and tr R_ab R^ab = −Riem² for so(1,9). With YM sign-correct (−|F|²/4λ²), this gives **L_R = +c Riem² with c = 1/(8λ²) > 0**. This is the same sign structure as the heterotic Riem² term (not cited).
- **Q0 (CONDITIONAL, HW printed λ² = 2π(4πκ²)^{2/3}).** λ² = (2π)⁷, and **u := 8π²/(λ²T_M5) = 2.000** (y16 log). λ⁶ ∝ κ⁴; the coefficient and its later revisions are CONDITIONAL.
- **Q3 (PROVED, variation).** T_ab = −4c R_acde R_b^{cde} + c h_ab Riem² + (four-derivative ∇∇R terms). The derivative terms vanish on locally symmetric products.

## 2. End faces (signs explicit)
**UV end** (AdS₇ × S⁴). The constant-r face metric tends to flat⁴ × H²(ρ → ∞) × round S⁴(R₄).
- **Q4a (PROVED, in terms of c).**
  - Energy density ρ_R = S_tt = −c(24/R₄⁴ + 4/ρ⁴). This is negative energy, with negative tension along x.
  - S(k,k) is −24c/R₄⁴ for fibre ê, −8c/ρ⁴ for Σ ê, and 0 for x ê.
- **Q4b (CONDITIONAL on Q1, c > 0).** In the fibre, K(ê,ê) − k_t = +12cκ²/R₄⁴ > 0. **That is NEC-violating, the sign the junction needs.**
- **Q5 (PROVED, in terms of λ).** Integrated over the fibre, both the energy and the fibre NEC supply are −64π²c = −8π²/λ², independent of R₄. That is −u T_M5 = **−2 M5 units** using Q0.

**IR end** (AdS₅ × Σ × squashed S⁴, at the IR fixed-point X_i).
- **Q6 (CONDITIONAL; fibre-intrinsic part only, with warp mixing and the twist dropped).** ∫_{S⁴}Riem² dvol is scale-invariant in 4D:

| candidate | ∫Riem² relative to round | n_R (M5 units) |
|---|---|---|
| MN2 | 1.645× | −3.29 |
| MN1 | 1.099× | −2.20 |
| z=2 | 2.135× | −4.27 |
| z=3 | 2.425× | −4.85 |

## 3. Interior and N-scaling
- **Q7 (PROVED given J1).** The flow in units of L₇ ∝ N^{1/3} is N-independent, and every term of T_ab from a four-derivative wall term scales as L⁻⁴. Integrated over the fibre (∝ L⁴), it gives an N-independent number of M5 units, finite on the smooth flow. The M5 requirements scale ∝ N. So the R² stress is **C_z/N relative to the requirement on every face, interior included, whatever the coefficient c is.**
- **Q8 (OPEN).** The sign of S_R²(k,k) on interior faces, where the ∇∇R terms do not vanish. It is not needed for the verdict, by Q7.

## 4. Verdict
- **Q11a (PROVED given J1, from Q7 and Q15). The junction verdict does not change at leading order in 1/N.** The R² term is the only source that can have the NEC-violating sign, and it does at the UV end (Q4b). But it is O(1/N) relative to the deficit, so the leading-order no-go stands.
- **Q10 (CONDITIONAL; Q0 and the 1711 template normalization).** At N_flux = 4880, the fibre deficit needs about ≥ 0.78 × 12252 ≈ 9.6×10³ M5 units of S(k,k). R² supplies 2–5 units, a fraction ≲ 5×10⁻⁴.
- **Q11b (CONDITIONAL). At N = 4880 the junction stays unsolved.** A coefficient error would have to be about 10³ to matter, and that is outside the derivative expansion.
- **Q12a (PROVED). The charge side is unchanged.** The tr R² term in the Bianchi identity integrates to 0 on S⁴ because p₁(TS⁴) = 0. So N_M5 + n_inst = 2N_flux is untouched.
- **Q12b (CONDITIONAL). The count gap status is unchanged.** The R² energy is −2 to −5 M5 units, the wrong sign. It *raises* the needed non-BPS excess by 2–5 units on (2492.1, 6506.7), and is 10³ too small to close it in any case.
- **Q13 (PROVED).** Bolza enters only through area(Σ) = 4π, which cancels against the M5's own Σ-wrapping. Q4–Q7 are local per unit Σ area. The H² piece is at most a −8c/ρ⁴ Σ-NEC term of the same O(1/N) size.
- **Q14 (OPEN).** Other corrections of the same order are not included: bulk R⁴, C₃∧X₈, flux torsion, and one-loop wall terms. By the Q7 scaling they are O(1/N) as well, so they cannot change the leading verdict either. Their exact coefficients are OPEN.

**Flag: the junction verdict is UNCHANGED, and the count-gap status is UNCHANGED.** Y16 is closed as a verdict-changing route at leading order. It remains only an O(10⁻⁴) correction.

Resolution path for the OPEN items:
- Q8: a full 10D T_ab on interior faces, with ∇∇R terms, warp and twist. About 2 h; not needed for the verdict.
- Q14: needs the full O(ℓ_P³/L³) M-theory boundary action, which depends on the literature. OPEN, low priority.

## Tally (header checked against the item lists)
| label | count | items |
|---|---|---|
| PROVED | 8 | Q3, Q4a, Q5, Q7, Q11a, Q12a, Q13, Q15 |
| CONDITIONAL | 8 | Q0, Q1, Q2, Q4b, Q6, Q10, Q11b, Q12b |
| OPEN | 2 | Q8, Q14 |
| REFUTED | 0 | — |

Check: 8 + 8 + 2 + 0 = 18.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
