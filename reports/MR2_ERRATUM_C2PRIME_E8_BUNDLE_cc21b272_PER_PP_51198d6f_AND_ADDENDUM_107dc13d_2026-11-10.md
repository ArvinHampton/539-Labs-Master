# MR2 erratum: c2′ E₈ bundle file cc21b272, per PP 51198d6f and addendum 107dc13d
2026-11-10, written ≈10:09 CST (America/Chicago, box clock; mtimes authoritative). Author: MR2. Additive and clerical: nothing edited (cc21b272 is unchanged), no new computation in this file, nothing adopted, no CERT, no Gemini, nothing sent until after the sidecar is written. Junction UNSOLVED. Wording: resonant algebra.

- Audit: FINDINGS_PP_AUDIT_MR2_C2PRIME_E8_BUNDLE_cc21b272_2026-11-10_1007.md, 51198d6fd2056673a01d22aff38147ffe626dab29d26de471a4c90ca73978deb (= sidecar, re-verified).
- Addendum (supersedes 1007 on row 12 and on the tally): FINDINGS_PP_AUDIT_MR2_C2PRIME_E8_BUNDLE_cc21b272_ADDENDUM_ROW12_2026-11-10_1008.md, 107dc13de4a9a8ea097908d639f5c6e951539c1972c7f64f5f0425bb9f18501d (= sidecar, re-verified).
- Target: MR2_BRANCH_ATTEMPT_BATCH1_C2PRIME_E8_BUNDLE_UNDER_1A_R_TILDE_INVARIANCE_2026-11-10.md, cc21b2728dd74fe6aae8d7da186a5bb40f9b5b4e8d8390226f2fa0e904f08f11. Not edited.
- PP: nothing refuted. Tip 7cddb188 MATCH in both PP files and at this write.

All eight of PP's fixes are accepted.

1. **Rows 10, 12 and 13: added premise.** "r ∈ Isom(Bolza) \ Aut⁺ is chosen to be an involution (a reflection)." f² = id and the ℤ₂-equivariance need that, because Isom(Bolza) \ Aut⁺ also contains orientation-reversing isometries of order greater than 2. Row 10 stays **PROVED as an implication**, with the premise widened to "the 8399be55 twist model and r an involution".

2. **Row 14 (E-S±): COND → OPEN.** A vertical spin structure exists (w₂ = π*(c₁(L) mod 2) = 0 because deg L is even): **PROVED**, as a sub-statement. Whether f preserves one (the δ ∈ H¹(Σ; ℤ₂) check) was not computed in cc21b272, so the lift claim is **OPEN**.

3. **Row 12 (E-T), per the addendum, which supersedes 1007 on this row.** The connection-preserving involutive E₈ lift is regraded **PROVED → OPEN**. f reverses the orientation of Y₆ (Jacobian diag(−1,−1,−1) on {x, φ₁, φ₂}, det = −1), so df is in O(6) \ SO(6). The standard embedding needs the spin lift of TY₆ and a Pin(6) action extended by a compensating reflection in the Spin(10) factor. Two checks were not done: that f preserves the spin structure on TY₆, and that the lifted involution squares to +1 (not to the central/−1 element) on the 128. The topological lift remains **PROVED as an implication** of D4 (n = 0 by D2). To restore the connection-preserving claim: specify the compensating Spin(10) reflection, and prove those two checks.

4. **Row 6: stays PROVED.** Cite PP's structural exact argument (PP's replacement of the script's `simplify == 0` test; PP reran the script, log byte-identical to 73ced586): no metric entry depends on x, φ₁, φ₂, x³ or the AdS translations; the only off-diagonal pairs are (x, φ₁) and (μ₁, μ₂); for each map, every nonzero g_ij has s_i s_j = +1. So r̃, P, f and c2′ are exact isometries of the chart metric.

5. **Header time.** Read cc21b272 as written **≈10:03** (mtime 10:03:24 CST). The original "≈10:02–10:10" runs past the mtime.

6. **Row 8 / [Q].** The control uses the 11D curvature restricted to Y₆ indices. It stays **COND** (float, one point). Naturality of tr R∧R does not depend on that choice (row 9 remains PROVED).

7. **Row 18 (M-loc).** The premise for f*G = +G, and hence for preservation of M5 charge, is the bd47ff5e index sets. The row stays **PROVED**, given that premise.

8. **Row 13 (E-Λ±).** State the premise "a fixed SO(3) ⊂ E₈ subgroup embedding". With that premise, the row stays **PROVED as an implication** of row 10 (with fix 1). The embedding index does not enter the lift.

## Revised labels (PP convention; only the changed rows are restated)
| # | item | grade in cc21b272 | grade now |
|---|---|---|---|
| 10 | f² = id with canonical lift | PROVED as implication of the twist model | PROVED as implication of the twist model **and r an involution** |
| 12 | E-T connection-preserving involutive E₈ lift | PROVED as implication of 10 | **OPEN** |
| 12′ | E-T topological lift (n = 0, given D4) | (included in 12) | PROVED as implication of D4 |
| 13 | E-Λ± lift under f; r̃ obstructed | PROVED as implication of 10 | PROVED as implication of 10 **and a fixed SO(3) ⊂ E₈** |
| 14 | E-S± lift under f | COND | **OPEN** (existence of a vertical spin structure, w₂ = 0: PROVED) |
| 6 | r̃, P, f, c2′ are isometries | PROVED (simplify==0) | PROVED (PP structural argument) |
| 8 | tr R∧R parity control, one point | COND (float) | COND (float; 11D curvature restricted to Y₆ indices) |
| 18 | M-loc invariant iff symmetric under φ₂ ↦ −φ₂; M5 charge preserved | PROVED | PROVED, given the bd47ff5e index sets |

All other graded rows of cc21b272 are unchanged.

## Tally
PP's tally, which this erratum adopts, is **15 PROVED / 2 COND / 6 OPEN / 0 REF = 23**, plus 1 bookkeeping row, and the junction UNSOLVED. This supersedes MR2's 16/3/4/0. The two grade changes versus cc21b272 are row 12 (connection-preserving lift PROVED → OPEN) and row 14 (COND → OPEN). Row 12′ (topological lift) is a scoped sub-statement, not an extra graded row.

## Branch status (pending PP confirm of this erratum)
- **B1-c2′:** still COND overall, not adopted. The E₈-lift claim is **PROVED as an implication for E-0 and E-Λ± only** (premises: HW normalisation, the 8399be55 twist model, r an involution, ℝ^{1,3}-invariance, and, for E-Λ±, a fixed SO(3) ⊂ E₈). It is also PROVED topologically for every n, given D4. For E-T, only the topological lift is established; the connection-preserving involutive lift is OPEN. E-S± is OPEN. Unchanged: Pin/Spin COND, D1 (7D↔11D) COND, SM COND.
- **B1-c2″:** COND/OPEN, unchanged.
- **B1-c2 literal:** REF (scoped), unchanged.
- **1a:** not adopted. Pure form REF; rescues 1a-T7, 1a-NY and 1a-Z2/D6 still OPEN.

Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, MATCH at write.
