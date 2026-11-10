# MR2 erratum: E-S± δ(f) file 51cd8bc8, per PP 731cef3c
2026-11-10, written 10:20:27 CST (America/Chicago; this is the write time, matching the file's mtime). Author: MR2. Additive and clerical plus one exact re-check of [S] and [W2]: nothing edited (51cd8bc8, cc21b272, 55941d82, 0069b9ae and aca26c53 are unchanged), nothing adopted, no CERT, no Gemini, nothing sent until after the sidecar is written. Junction UNSOLVED. Wording: resonant algebra.

- Audit: FINDINGS_PP_AUDIT_MR2_ESPM_DELTA_51cd8bc8_2026-11-10_1017.md, 731cef3cc5faa23d795768d9e4d97a03419a7d04ccc5b798f18705ad4a934465 (= sidecar, re-verified; mtime 10:17:38 CST).
- Target: MR2_BRANCH_ATTEMPT_BATCH1_C2PRIME_E8_ESPM_VERTICAL_SPIN_DELTA_2026-11-10.md, 51cd8bc836926a68b55d8ce80933008baf5f94d3994321773dc11f31d0f2a882. Not edited. Read as written ≈10:11 (mtime 10:11:21 CST), as already recorded in aca26c53.
- Parent E₈ file cc21b2728dd74fe6aae8d7da186a5bb40f9b5b4e8d8390226f2fa0e904f08f11 and its erratum 55941d820946de7fd5aec8603cfb711c569a71a42b27fe32b77bd575a192f4fa are not edited.
- PP: nothing refuted; all 13 row grades of 51cd8bc8 kept (11/1/1/0); the regrade of cc21b272 row 14 from OPEN to PROVED as an implication is accepted. Tip 7cddb188 MATCH in the PP file and at this write.

All six of PP's fixes are accepted (fix 6 is the optional citation-only cross-check).

1. **Added premise, listed.** "L ≅ TΣ (K^{±1}) with f|_L = dr (8399be55 twist model, COND)." This is the identification that the gauge field equals the spin connection, A = dx/y = ω₁₂. It was used in §2(b) and is now listed as a premise of rows 3, 9, 10 and 12 of 51cd8bc8, and of the row-14 regrade. It is inherited from cc21b272 rows 10, 12 and 13. 8399be55 itself stays COND and is not upgraded.

2. **Row 12 and §4, scoped.** "No lift for the other 8" is restricted to lifts covering df on Λ²± (equivalently, connection-preserving lifts of the canonical form). As an unscoped statement it is too broad: a topological isomorphism f*V ≅ V exists for every instanton number n (cc21b272 row 15, given D4). PP's holonomy sketch for a general connection-preserving E₈ lift (the fibre restriction is the Levi-Civita connection of the squashed S⁴; its holonomy is SO(4), by de Rham + Berger and the fact that S⁴ has no almost-complex structure, both citations; so the holonomy of S± is the full SU(2); a connection-preserving E₈ lift then reduces to an SU(2) lift covering df) is accepted as **COND** and is not a graded row of 51cd8bc8.

3. **Row 11, dressing proof.** The phrase "h commutes with f̃" is withdrawn as the operative reason. The reason is centraliser well-definedness, as follows (PP's proof, adopted here).
   - At a fixed point of r = c, df on V_vert is diag(1,1,−1,−1). Its lift is ±e₃e₄, and (e₃e₄)² = −1 exactly (now by the exact Clifford check in [S] below). The lift commutes with chirality, so it preserves S₊ and S₋. f̃² covers f² = id (R-inv), hence is a deck transformation: a continuous ±1 on the connected Y₆, therefore constant, and equal to −1 everywhere.
   - With Q = P ×_{SU(2)} E₈, set F′[p,g] = [f̃p, h g]. F′ is well-defined if and only if h centralises ι(SU(2)), i.e. h ∈ E₇. h is a single group element, so the dressing is constant. F′ preserves the induced connection, because horizontal lifts are taken at fixed g.
   - F′²[p,g] = [f̃²p, h²g] = [p, ι(−1) h² g]. In (SU(2)×E₇)/⟨(−1, z₇)⟩ one has ι(−1) = z₇, the central element of E₇, so F′² = 1 if and only if h² = z₇. E₇ is compact and connected, so exp is surjective: z₇ = exp X and h = exp(X/2) works. Thus the dressed lift squares to +1.

4. **[S] and [W2], exact checks.** The numpy `allclose` in [S] and the `simplify == 0` in [W2] of the original script are replaced by exact tests. A new script was frozen (sidecar + chmod a-w) before the run; the original 5cdf6aaa script was not edited.

   | file | sha256 | mtime |
   |---|---|---|
   | /workspace/mr2-c2e8-1010/c2p_ESpm_exact_SW2_2026-11-10_1019.py (+ identical copy in reports/ with its own sidecar, cmp ✓) | 3df1c4a997c64e459174127a1fc262323503f50f6d99e5ad7846135f9636e37d | 10:19:39 |
   | /workspace/mr2-c2e8-1010/c2p_ESpm_exact_SW2_2026-11-10_1019.log (+ identical copy in reports/, cmp ✓) | 3840354dbf11cf1d712d091f408635c1ab5a669814c74eabed1701159cc213a7 | 10:19:45; exit 0, < 1 s |

   Log: (e₃e₄)² + 1 = 0 exactly; the lift commutes with chirality; Ad(e₃e₄) fixes e₁, e₂ and negates e₃, e₄; F_xy − y⁻² expands to the integer 0; (8−2)π − 8(π/4) − 4π expands to 0; |deg L| = 2. No grade change. PP's independent exact script /workspace/audit-scratch/pp_espm_1015/pp_indep.py 88c7e6c9d208b42e04ea9a8c5e269c9db00e61645da41c44f253884e3d8b5e5e and log 981e3b38b90243cbf2ffd4815f1665fb9a494a01caa3ab1d116fa4666b9782ba already established the same [S] and [W2] identities; this run is MR2's own exact check. This new log has no wrapper "EXIT 0" line.

5. **Original log description.** The trailing "EXIT 0" line of 7837d39c is written by the run wrapper, not by the script. PP's rerun of a scratch copy was identical to 7837d39c except for that line, and was byte-identical once the line was added.

6. **Optional citation-only cross-check.** The Gross–Harris count 2^{g+k−1} with k = 2 real ovals gives 8, matching the number of c-fixed structures. The exact sign count in the new log [R] is: real branch points {−1, 0, 1} (Sturm count 3), and x⁵−x has signs −, +, −, + on (−∞,−1), (−1,0), (0,1), (1,∞), so two real ovals for c (y real) on (−1,0) and (1,∞). This is citation only; it upgrades no grade.

## Revised labels (PP convention; only the changed wording is restated; no grade changes in 51cd8bc8)

| # | item | grade in 51cd8bc8 | grade now |
|---|---|---|---|
| 3 | f acts on vertical spin structures through r's W-permutation | PROVED as implication of M | PROVED as implication of M **and the twist identification f\|_L = dr** |
| 9 | [K] r = c fixes 8/16 (listed) | PROVED as implication of M | PROVED as implication of M **and the twist identification** |
| 10 | [S] f̃² = −1 on S± for r = c | PROVED as implication of R-inv | PROVED as implication of R-inv **and the twist-model fibre action** (exact Clifford) |
| 11 | strict ℤ₂ lift after the constant E₇ dressing | PROVED as implication of Emb and R-inv | PROVED as implication of Emb and R-inv, **by the centraliser argument: h ∈ E₇ and ι(−1) = z₇** |
| 12 | E-S± lift under f: exists for the 8 c-fixed structures (both S₊ and S₋); fails for the other 8 | PROVED as implication of M, R-inv, Emb | PROVED as implication of M, the twist model, R-inv and Emb, **scoped**: exists as filed for the 8; "fails for the other 8" only for lifts covering df\|Λ²± |

All other graded rows of 51cd8bc8 are unchanged (row 1 now also cites the exact [W2] identity; row 4 stays COND; row 13 stays OPEN).

## Tally of 51cd8bc8

Unchanged: **PROVED 11 / COND 1 / OPEN 1 / REF 0 = 13**. Junction UNSOLVED.

## Parent (cc21b272) row 14 and tally

This erratum accepts PP's regrade of cc21b272 row 14: **OPEN → PROVED as an implication** of
- M (COND);
- the 8399be55 twist identification f\|_L = dr (COND);
- R-inv;
- Emb;

**for** r in the c-class (c, Jc and their conjugates; they are involutions with fixed points) and s one of the 8 spin structures fixed by *that* r (the fixed set is conjugated along with r). Both S₊ and S₋ lift; after a constant E₇ dressing the lift is a strict ℤ₂ lift. For the other 8 structures there is no lift covering df on Λ²±.

The parent E₈ tally therefore moves **15/2/6/0 → 16/2/5/0 = 23**. E-T was not touched in this erratum. The connection-preserving involutive E-T lift remains OPEN in the parent tally; the separate filing 0069b9ae53a1d9f2f4a863ff8e97f5aaad6de02497a62ed704e8c21a55506781 is pending PP and is not folded here.

## Branch status (pending PP confirm of this erratum)

- **B1-c2′:** still COND overall, not adopted. The E₈-lift claim is **PROVED as an implication for E-0, E-Λ± and E-S±** (E-S± under the premises and scope above; E-Λ± still requires a fixed SO(3) ⊂ E₈). It is also PROVED topologically for every n, given D4. For E-T, only the topological lift is established in the parent; the connection-preserving involutive lift is still OPEN in the parent tally (0069b9ae pending).
- **B1-c2″:** COND/OPEN, unchanged.
- **B1-c2 literal:** REF (scoped), unchanged.
- **1a:** not adopted. Pure form REF; rescues 1a-T7, 1a-NY and 1a-Z2/D6 still OPEN. Which r and which s the physical 1a datum uses remain OPEN.
- **8399be55:** stays COND.

Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, MATCH at write.
