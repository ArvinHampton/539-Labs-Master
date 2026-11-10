# MR2 ERRATUM: KK truncation file ecee2668, per PP audit 1fe6c574
Author: MR2. Additive new file: it does not edit ecee2668 (.md ecee2668…, .py 88949658…, .log a2d105e6…), which stay as filed. No CERT. Nothing sent. Nothing adopted by MR2.
- Context: PP audit FINDINGS_PP_AUDIT_MR2_KK_TRUNCATION_BOLZA_48_96_WALL_Z2_2026-11-09_1858.md (sha 1fe6c574…, rollup 25/3/2/1). The Owner chose Group A in OW 8b26c786 (t4414, 19:05; "Group A"), which is a scope choice.
- Each of PP's fixes 1–6 was verified independently before being accepted. Fix 7 is MR2's own consequence of the Pin⁺ file.
- Junction UNSOLVED. Full spectrum OPEN. Count gap unchanged.

## Fix 1. Δ correction disclosure (PP R5)
- **What changed.** In §7 of the .md (row "(A) only (DD levels)"), the Δ for the DD level **394.578** (m²L₅² = 2λ = 789.16) was first written as **30.13**. It was corrected to **30.16** before the sidecar was written and before distribution, and no copy of the earlier text was kept.
- **Sources.** The old value comes from MR2's own session record, not from disk. PP inferred the right level.
- **Check.** Δ = 2 + √(4 + 789.156) = **30.1630**. So the filed 30.16 is correct and 30.13 was an arithmetic typo. PROVED (recomputed).
- **Policy going forward.** Any pre-distribution correction is disclosed inside the file itself. The Pin⁺ file 8399be55 does this for its own tally fix.

## Fix 2. SU(2)_R flat connections: added to OPEN (PP A4-gap)
- **PP's counterexample is verified. PROVED.**
  - Let w = iσ₂. Then wσ₃w⁻¹ = −σ₃, so w·exp(iθσ₃)·w⁻¹ = exp(−iθσ₃).
  - Every abelian SU(2) line ρ = exp(iθσ₃) has ρ∘J_* = ρ⁻¹ = wρw⁻¹. So **J does not remove SU(2)_R lines up to gauge**.
  - The ecee2668 statement "all 16 Wilson-line modes removed" holds as stated, meaning U(1) and ℤ₂ lines under the canonical lift without gauge dressing.
- **New OPEN row:** Aut⁺-invariance of the SU(2)_R character variety of π₁(Σ) up to gauge, including torsion points with g·θ = χ(g)·θ.
- This item has since been started; see the follow-on file MR2_MN2_KK_A_SU2R_FLAT_CONNECTIONS_AUT48_2026-11-09 if it is present on disk, which carries its own labels.

## Fix 3. §4 wording (PP A5)
- J acts trivially on H¹(Σ;ℤ₂), since −1 ≡ +1 mod 2, and it fixes all 6 Weierstrass points. So **J fixes all 16 theta characteristics**.
- The non-invariance of the bare Σ spin structures comes **only** from the GL(2,3) → S₄ permutation action on the Weierstrass points. The orbits are: odd 6; even 4 + 6.
- PROVED: recomputed in the Pin⁺ log, [D] line "16/16".

## Fix 4. λ₁ row regraded (PP T4)
- The §10 row "'λ₁ ≈ 3.8388976 is Bolza's' (job brief): REFUTED" becomes **"corrected (self-correction per ERRATUM2 7b9ebdaf): 3.8388976481 is the KMP genus-2 bound; Bolza λ₁ = 3.8388872588, CONDITIONAL on Strohmaier–Uski"**.
- I agree that a REFUTED grade needs an in-repo proof or counterexample. Neither MR2 nor PP recomputed the 3-dimensional eigenvalue.

## Fix 5. §9 count-gap interval (PP J2)
- For the adopted MN2 vacuum the interval is **(1 + 2808.6/9760, 1.6667) = (1.287766, 1.6667)**. The arithmetic was recomputed: 1.2877664. The input values are CONDITIONAL on NL S13 and PP 1846 (5374a906).
- MR2's 1.287611 lies **below the open lower end by 1.55e-4**. It is outside the interval, not inside it. The ecee2668 phrase "1.288 inside [1.255, 1.667)" used the all-candidate interval and is withdrawn for MN2.
- **1.032 (fixed-φ measure) is flagged as gauge-dependent**, per PP 5374a906 S13r. Under pure-gauge shifts of the φ₁ origin over Σ, PP gets 0.9934, 0.9046 and 0.7139. It must not be quoted as a gap comparison. MR2 never claimed it was physical; what is refuted is its invariance.
- The count gap is still unchanged by A (Γ-independence, PROVED).

## Fix 6. §10 tally reconciled with the 19 rows (PP O2)
Row assignment in table order, as filed:

| # | row | grade |
|---|---|---|
| 1 | closure, orders, character tables | PROVED |
| 2 | equalities 48, 96; GL(2,3) | CONDITIONAL |
| 3 | (2,3,8) triangle, characters ↔ boundary conditions | PROVED |
| 4 | invariant Σ-levels | mixed (PROVED numerically; bounds above 28.08 OPEN) |
| 5 | irreducible labels | OPEN |
| 6 | Wilson-line modes removed | mixed (PROVED; linear masslessness CONDITIONAL) |
| 7 | no ℤ₂ lines or bare spin structures | mixed (PROVED counting; identification CONDITIONAL) |
| 8 | unique SUSY spin structure | CONDITIONAL |
| 9 | (B) internal | REFUTED |
| 10 | (B) dressed is a symmetry | PROVED (given bd47ff5e) |
| 11 | Pin⁺, R-dressed lifts | OPEN |
| 12 | wall-ℤ₂ parities | mixed (PROVED; orbifold BCs CONDITIONAL) |
| 13 | H⁰(K), H⁰(K²) | PROVED |
| 14 | Σ-constant masses | mixed |
| 15 | spin-2 = 2Δ_Σ | mixed (identity PROVED; Bachas–Estes CONDITIONAL) |
| 16 | other towers, full spectrum | OPEN |
| 17 | junction | UNSOLVED |
| 18 | count gap | mixed |
| 19 | λ₁ wording | REFUTED |

- **As filed (19 rows):** PROVED 4 · mixed 7 · CONDITIONAL 2 · OPEN 3 · REFUTED 2 · UNSOLVED 1. This equals PP's per-row reading. The filed line "PROVED 9 · CONDITIONAL 4 · OPEN 3 · REFUTED 2 · mixed 4 · UNSOLVED 1" (23) was wrong: it counted component labels inside mixed rows as separate entries. That line is REFUTED and withdrawn.
- **Corrected (20 rows), after fixes 2, 4 and 7:**
  - row 19 → CONDITIONAL;
  - new row 20, SU(2)_R flat connections up to gauge → OPEN;
  - row 10 → mixed (fix 7);
  - row 11 → superseded (fix 7).
  - Result: PROVED 3 · mixed 8 · CONDITIONAL 3 · OPEN 4 · REFUTED 1 · UNSOLVED 1 = 20. Row 11 is counted under OPEN as filed; its content is superseded.

## Fix 7 (MR2's own, from the Pin⁺ file 8399be55)
- **Row 10.** "(B) dressed with P or T is a symmetry" was PROVED only at the bosonic level (f*G = orientation·G). With the wall ℤ₂ included, the lifts of (i) and (ii) anticommute with W̃ = Γ_ρ and flip the 10D wall chirality. They are therefore **REFUTED as M-theory symmetries of the HW-walled background**, given the HW premise.
  - Only the φ₂-dressed variants (i′) and (ii′) survive, and they are CONDITIONAL.
  - All of this is moot under OW 8b26c786. Row 10 becomes mixed.
- **Row 11.** Pin⁺ for A × wall is now **CONDITIONAL**: it passes, subject to four premises listed in the Pin⁺ file §A.

## Unchanged
All Σ-levels, masses, Δ values (all PP-recomputed and correct), the (B)-internal refutation, junction UNSOLVED, and full spectrum OPEN. Tip 7cddb188 MATCH.
