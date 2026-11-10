# MR2 branch attempt (OW t4436): B1-1b-ii, "L1 everywhere" — closed form of the tr R∧R component on F₁₀
2026-11-09, written 22:10 CST (America/Chicago, box clock). Author: MR2. Additive; nothing edited or adopted; no CERT, no Gemini, nothing sent, no agent messaged. Junction **UNSOLVED**. Follows MR2_BRANCH_ATTEMPT_BATCH1_1Bii_L1_EXACT_AND_2b_THICK_WALL_NEC_2026-11-09.md (3da6285a…). **Grades are MR2's proposal, pending PP audit.**

## Scripts and logs (/workspace/mr2-branch-2134/; frozen before running, sidecars MATCH)
| file | .py sha256 | .log sha256 | .py → .log (CST) |
|---|---|---|---|
| L1_everywhere_symbolic_2026-11-09_2204 | 2f2b9d4f1d974934e673b25ad92c11b1c53a42a449e12942ad567bf573c2dc71 | 264fdf1da0d77ef20fcb495a0c7a8dc775a11b6578103ab654c86e8ed669313e | 22:02:59 → 22:03:25 |
| L1_Nprime_roots_2026-11-09_2208 | 16859a5ca0fa45943b2671a78ffb2b797eb25ebe2d9177208a4f4b85979de247 | c66f73ed999b3436be4d0727de2ac99b4748fb6ae8bd7de6ae0d53bf176d0efb | 22:08:04 → 22:08:04 |

## Results
- **E1 (PROVED, exact symbolic).** On F₁₀, in the chart (μ₁, μ₂, φ₁) with p = μ₁²:
  - P_{x y μ₁ φ₁} = 2μ₁N′/D, where N′ = −½·2^{4/5}(p−2)(p+2)²(p²+4p−6) and D = 2^{1/5}Δ³(p−2)²(2^{3/5}Δ^{2/3}·Δ^{4/3}… ) > 0. Exactly: D = 2^{1/5}d⁹(p−2)²(2^{3/5}d⁶ + 4d³p + 2^{7/5}p²), with d³ = Δ = 2^{2/5}(1 − p/2) > 0.
  - **P_{x y μ₂ φ₁} ≡ 0.**
  - Check: at μ₁ = 1/3 the closed form gives −1.161192993378910693119…, matching the interval value −1.16119299337891068720.
  - The factorisation of N′ was checked by hand expansion: −½(p−2)(p+2)²(p²+4p−6) = −p⁵/2 − 3p⁴ + p³ + 18p² + 4p − 24.
- **E2 (PROVED).** N′ has no root in [0, 1] (Sturm count 0; the roots are −2 (double), 2 and −2 ± √10). Its values are N′(0) = −24·2^{4/5} and N′(1) = −(9/2)·2^{4/5}. Hence:
  - **tr R∧R ≠ 0 at every point of F₁₀ with 0 < μ₁ < 1.** A single nonzero component suffices.
  - **At μ₁ = 0** it is also nonzero. With X + iY = μ₁e^{iφ₁}, dμ₁∧dφ₁ = dX∧dY/μ₁, so the Cartesian component is 2N′/D ≠ 0.
- **E3 (COND).** On the circle locus {μ₁ = 1} (μ₀ = μ₂ = 0; AdS₅ × Σ × S¹_{φ₁}), the 1-form dμ₁ vanishes, because μ₁ is maximal there, while c = 2μ₁N′/D stays finite. So the found term c·dx∧dy∧dμ₁∧dφ₁ → 0. tr R∧R therefore **vanishes on {μ₁ = 1} if** the other 208 coordinate components vanish identically. Evidence: their intervals contain 0 at two points (40-digit intervals); P_{x y μ₂ φ₁} ≡ 0 is symbolic. A full symbolic check of the remaining components was not run (est. ~30 min).

## Status change (B1-1b-ii)
| row | before | after |
|---|---|---|
| L1 "pointwise nonzero everywhere on F₁₀" | OPEN | split: **nonzero on F₁₀ \ {μ₁ = 1}: PROVED** (E1, E2); **vanishes on {μ₁ = 1}: COND** (E3). If E3 is confirmed, the original "everywhere" wording is **REFUTED**. |
| (b-ii) F ≠ 0 required | PROVED (companion file) | unchanged. The HW condition tr F² = ½ tr R² allows F = 0 on a codim-2 locus, and needs F ≠ 0 on the open dense set. |

Tally of this file: PROVED 2 (E1, E2) · COND 1 (E3) · OPEN 0 · REF 0.

Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, untouched.
