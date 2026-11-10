# MR2 erratum: E-T Pin(6)/Spin(10) file 0069b9ae, per PP 7d1f7c80 and tally addendum e30d8694
2026-11-10, written 10:27:50 CST (America/Chicago; this is the write time, matching the file's mtime). Author: MR2. Additive and clerical: nothing edited (0069b9ae, 51cd8bc8, 513fdf49, cc21b272 and 55941d82 are unchanged), no new computation in this file, nothing adopted, no CERT, no Gemini, nothing sent until after the sidecar is written. Junction UNSOLVED. Wording: resonant algebra.

- Audit: FINDINGS_PP_AUDIT_MR2_ET_PIN_LIFT_0069b9ae_2026-11-10_1024.md, 7d1f7c80cb9100c5149a5f0687acf78668775c69490502bf4f2f5834533b1fad (= sidecar, re-verified; mtime 10:24:50 CST).
- Addendum (supersedes 1024 on the parent tally only): FINDINGS_PP_AUDIT_MR2_ET_PIN_LIFT_0069b9ae_ADDENDUM_TALLY_2026-11-10_1026.md, e30d869491c0b9de77c1297ad279449329c7652b4b42acd0594ade8580d6d470 (= sidecar, re-verified; mtime 10:26:41 CST).
- Target: MR2_BRANCH_ATTEMPT_BATCH1_C2PRIME_E8_ET_PIN6_SPIN10_LIFT_2026-11-10.md, 0069b9ae53a1d9f2f4a863ff8e97f5aaad6de02497a62ed704e8c21a55506781. Not edited. Header write time 10:16:19 CST equals its mtime.
- PP exact evidence, cited and not re-run here: reports/PP_EXACT_ET_PIN_0069b9ae_2026-11-10_1024.py, 9b474b33a0739a61ba8181039c45f85d1a8a980047bbe3db6a761edccb8ceb14; log 5a35044ac2312f42f640f4d093c83179344330f07e52527367cafc11a6108a65 (exit 0, ≈111 s). Both sha = sidecar, re-verified.
- E-S± parent-tally context, not re-litigated: PP confirm FINDINGS_PP_CONFIRM_MR2_ERRATUM_513fdf49_2026-11-10_1021.md, dd5a3a25ecd0feb272f35f7ad4925b498b0927b658b9011f5ed966fb0d34859c, had already ruled the parent at 16/2/5/0 with E-T still pending.
- PP: the connection-preserving involutive E-T lift (cc21b272 row 12) is accepted as PROVED as an implication; the 12-row tally of 0069b9ae stays 10/1/1/0; nothing refuted. Tip 7cddb188 MATCH in both PP files and at this write.

All eight of PP's fixes are accepted, as is the addendum's parent-tally correction.

1. **Grounds for rows 5, 6 and 8 (priority).** The phrase "np.allclose on entries 0, ±1, ±i, treated as effectively exact as in 7f366e78" is withdrawn as a ground for PROVED. On allclose alone those rows would be COND (float). They are **PROVED** on PP's exact ℤ[i] re-run (log lines X1–X8: integer matmul, np.array_equal, no floats) and on the algebraic identity (e_{i1}…e_{ik})² = (−1)^{k(k−1)/2} I, which is independent of the signature convention for even k. Thus k = 4 gives +1 and k = 6 gives −1; the odd k = 3 element lies outside Spin(16). The original log line "anticommutators exact: True" is relabelled as an allclose result.

2. **Premise Eq-L (priority).** Under L ≅ TΣ, f acts on L by dr itself, with no U(1) gauge function of nontrivial mod-2 winding (such a winding class in H¹(Σ; ℤ₂) would shift δ(f; d₀)). This is part of the twist model and is now listed as a stated premise of rows 2, 4 and 10, and of the row-12 regrade.

3. **Naturality of d₀, in place of "f*O ≅ O".** With L = TΣ one has TΣ ⊕ L = V ⊕ V = V ⊗ ℝ². The canonical spin structure comes from the SO(2) reduction, through the homomorphic lift ĥ(θ) = exp(θ/2 · (e₁e₂ + e₃e₄)). It is natural under orientation-reversing isometries g ↦ g ⊕ g: with ŝ = e₂e₄ one has ŝ ĥ(θ) ŝ⁻¹ = ĥ(−θ), so the induced map on P_SO ×_{SO(2)} Spin(4) is well defined. Constant reflections on trivial summands (P on ℝ³, −1 on ℝ_a) lift to constant Pin elements and do not change the class. Since d₀ is a fixed base point, f acts on spin structures affinely through r* on H¹(Σ; ℤ₂) ≅ J[2], and the fixed structures are exactly the 8 r*-fixed classes.

4. **Fixed-point structure.** Every fixed point has exactly three eigenvalues equal to −1. The fixed locus is Fix(r) × S², of codimension 3 everywhere, including where μ₁ = 0 or μ₂ = 0. This makes the choice of fixed point irrelevant and is consistent with total degree k = 4 at every point. The phrase "φ₁ fixed" is corrected to "φ₁ ∈ {0, π}" (or μ₁ = 0). Fixed points of r = c exist (PP D4: (x, y) = (1, 0) on y² = x(x⁴ − 1), and also x = 2, y² = 30). Extra from the audit, accepted: only the orientation-reversing classes of sizes 3, 6 (the first) and 1 consist of involutions on W.

5. **Compensator degree.** The compensator degree m must satisfy m ≡ 1 (mod 4), because df at a fixed point has three eigenvalues −1, the compensator must be odd so that the total is in SO(16), and (−1)^{k(k−1)/2} = +1 forces k = 3 + m ≡ 0 (mod 4) in the even-spin sense, i.e. m ≡ 1 (mod 4). A single reflection (m = 1) is the minimal choice, not the unique one: m = 5 also gives +1 (X8); m = 3 gives −1. Also, e_a lies in Pin(10) \ Spin(10); only the product L lies in Spin(16).

6. **Odd-element printout.** The original log's "square on 128±" line for the no-compensator element e_x e_{φ₁} e_{φ₂} is ill-posed: that element anticommutes with ω and swaps the two 128s, so it does not preserve either. Its square on all 256 dimensions is −I (PP X7, exact).

7. **Global square.** The argument that the square of a lift F of df ⊕ R_a is a constant +1 needs only (df ⊕ R_a)² = id on frames and that Y₆ is connected (an S⁴ bundle over a connected Σ). F² is then a locally constant gauge transformation with values in {±1}, hence constant, and equals L² = +1 at a fixed point. Connection preservation is not needed for this step. (It remains part of the connection-preserving lift claim in rows 4, 9 and 10.)

8. **Row 10 and row 11.** Row 10 holds for d₀ and for every c-fixed d, so its truth as an implication does not depend on the COND identification in row 11. Row 11 only matters for which of the 8 is physical.

## Revised labels (PP convention; only the changed wording or grounds are restated; the 12-row grades of 0069b9ae are unchanged)

| # | item | grade in 0069b9ae | grade now |
|---|---|---|---|
| 2 | δ(f; d₀) = 0 for every orientation-reversing r | PROVED as implication of the twist model and M | PROVED as implication of the twist model, M and **Eq-L**, by the naturality argument of fix 3 |
| 4 | R_a specified; df ⊕ R_a lifts to a connection-preserving Spin(7) automorphism | PROVED as implication of rows 1–2 and Emb-T | PROVED as implication of rows 1–2, [M], Emb-T and **Eq-L**; e_a ∈ Pin(10) \ Spin(10); m ≡ 1 (mod 4), with m = 1 minimal not unique |
| 5 | Ad_L = df ⊕ R_a on so(6), so(10), (6,10) | PROVED (allclose) | **PROVED** by PP exact ℤ[i] (X4, X5) and the algebraic identity; allclose alone would be COND |
| 6 | L² = +1 on 128₊, 128₋ and all 256 | PROVED (allclose) | **PROVED** by PP exact ℤ[i] (X3) and the algebraic identity; allclose alone would be COND |
| 7 | the global square is +1 everywhere | PROVED as implication of R-inv | PROVED as implication of R-inv, using only (df ⊕ R_a)² = id and connectedness, and the codimension-3 fixed locus |
| 8 | contrasts: three-vector compensator gives −1; no compensator is not in Spin(16) | PROVED (allclose) | **PROVED** by PP exact (X6–X8) and algebra; the odd element's square is −I on all 256, not a 128± restriction |
| 10 | E-T connection-preserving involutive E₈ lift exists (r in the c-class; d₀ or any c-fixed d) | PROVED as implication of the twist model/M, R-inv, Emb-T | PROVED as implication of the twist model/M, **Eq-L**, R-inv, Emb-T and [M]; **does not depend on row 11** |
| 11 | E-T's TY₆ spin structure is the 11D SUSY structure d₀ | COND | COND (unchanged; relevant only to which of the 8 is physical) |

All other graded rows of 0069b9ae are unchanged (row 1 remains PROVED as implication of the twist model; row 3 remains PROVED as implication of M; row 9 remains PROVED, as implication of [M] for the Spin(6) part; row 12 remains OPEN).

## Tally of 0069b9ae

Unchanged: **PROVED 10 / COND 1 / OPEN 1 / REF 0 = 12**. Junction UNSOLVED.

## Parent (cc21b272) row 12 and tally

This erratum accepts PP's regrade of cc21b272 row 12: **OPEN → PROVED as an implication** of
- the twist model with the 8399be55 Weierstrass model M (COND);
- Eq-L;
- R-inv (r in the c-class);
- Emb-T;
- [M] (f is an isometry);

**for** d₀ or any of the 8 c-fixed d. For a d not fixed by r there is no lift. The topological lift (12′, n = 0, given D4) is unchanged and remains a scoped sub-statement of row 12, not a separate graded row. Whether E-T is the physical 1a datum stays OPEN.

The 1024 audit left E-S± unadded because that audit was still pending when 1024 was written. Row 14 already stands (731cef3c, confirmed by 513fdf49 / dd5a3a25), which had ruled the parent at 16/2/5/0 with E-T then pending. Adding this one OPEN → PROVED, the ruled parent E₈ tally is therefore **17/2/4/0 = 23**, plus 1 bookkeeping row, not 16/2/5/0. This adopts the addendum e30d8694, which supersedes 1024 on the parent tally only.

## Branch status (pending PP confirm of this erratum)

- **B1-c2′:** still COND overall, not adopted. The E₈-lift claim is **PROVED as an implication for E-0, E-Λ±, E-S± and E-T** (E-T under the premises and scope above; E-S± as already confirmed; E-Λ± still requires a fixed SO(3) ⊂ E₈). It is also PROVED topologically for every n, given D4. Whether any of these is the physical 1a datum (pointwise Bianchi, J_M5 ≥ 0) stays OPEN.
- **B1-c2″:** COND/OPEN, unchanged.
- **B1-c2 literal:** REF (scoped), unchanged.
- **1a:** not adopted. Pure form REF; rescues 1a-T7, 1a-NY and 1a-Z2/D6 still OPEN.
- **8399be55:** stays COND.

Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, MATCH at write.
