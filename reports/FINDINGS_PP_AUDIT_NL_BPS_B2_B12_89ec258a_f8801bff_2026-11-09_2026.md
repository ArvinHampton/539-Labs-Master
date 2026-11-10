# FINDINGS — PP audit of NL B2 check (89ec258a…), NL B12 χ-dependent walls (f8801bff…), NL Erratum 18-B12 (92dded27…), plus confirmation of NL Erratum 18 (2003, af7a8199…) — 2026-11-09 20:26 CST (America/Chicago)
Auditor: Professor Proof (PP). Pure math. Labels PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. Float-only results are CONDITIONAL. A citation alone never makes a result PROVED (OW 3f160803 + 36683379). Authority OW d5eaeef3. **Nothing adopted. Junction: UNSOLVED.** No CERT, no sends, no Gemini. New file only. Companion to FINDINGS_PP_AUDIT_NL_BPS_CALIBRATED_WALL_704df3ee_2026-11-09_2020.md (5f2de6f9…; "the 2020 file").
Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 at start and at write time (unchanged).
Erratum naming: two NL files are numbered 18. Cited here as **Erratum 18** (2003, af7a8199…) and **Erratum 18-B12** (2019, 92dded27…). A third file, NL_ERRATUM18_ADDENDUM_PP_CONFIRM_E17_c90b4fba_2026-11-09_2010.md (eaef6139…, sidecar MATCH), is on disk and was not requested for audit.
Typo note on the 2020 file (not edited): in §1 B5 "twisted DΜ" reads "twisted Dμ".

## 0. Integrity and reruns
| file | sha256 | sidecar |
|---|---|---|
| NL_DERIVED_BPS_B2_SUPERPOTENTIAL_CHECK_2026-11-09_2012.md | 89ec258a33794a3e8cb91bd997d735851730193420d233918684c36a57a64a54 | MATCH |
| NL_DERIVED_BPS_B12_CHI_DEPENDENT_WALLS_2026-11-09_2017.md | f8801bff1d93d39ef541c4842e049bd90fb7689e77dd5dfa7ff21e372979e54c | MATCH |
| NL_ERRATUM18_B12_D4_CONSTANT_2026-11-09_2019.md | 92dded27f75e8f70b05cc50ad2e1f6805d5820129e73b7cda9e85590517475bd | MATCH |
| NL_ERRATUM18_ACCEPT_PP_99593076_84f49882_d365c611_2026-11-09_2003.md | af7a8199fadc6df06beb7d03e32f68e6a98bf3ecfd11602efa5fd633b567eadd | MATCH |
| /workspace/nl-bps-b2-2011: n2_moment_maps.py/.log, bkv_signflip.py/.log | 709543f7…/00165bd9…, f17b40b2…/a41b2489… | all MATCH |
| /workspace/nl-bps-b12-2015: hw_bps_identity_c6.py/.log, level0_hw_trace.py/.log | e3b71810…/e0f57add…, 698c4f8e…/f05a9483… | all MATCH |
- **Reruns** (PP scratch /workspace/pp-audit-bps-b2b12): all four scripts exit 0 in < 5 s, and **all four logs are byte-identical** to NL's.
- **Sidecar timing.** The b2 sidecars were written in the same second as the logs (20:11:42); the b12 sidecars at 20:17:30, after the runs. Both are post-run integrity sidecars, not freezes (fix G1).
- **PP scripts** (each .py sidecar frozen before its run):
  - pp_b2_w.py ed9672a3… / .log f42aeed6…
  - pp_d5_sign.py bd080e33… / .log e6a79571…
  - The 2020 file's pp_bps_audit.py 6e032abf… also applies here.

## 1. B2 check file (89ec258a…, NL 4/3/0/0)
- **C1 (PROVED, agree).**
  - Rerun identical: (D.14) with (D.19) and (D.21) reproduces the (5.16) potential at z = 0 for all (Σ, Ω, ϕ).
  - (5.16) at w = 0 equals (3.8).
  - g_xy = diag(6/Σ², 2/Ω²).
  - These are exact derivations from the cited CGR data.
- **C2 (PROVED, agree; normalisation consistent with 2020 B1).**
  - W_B1 = −2√3 gP. PP derived this independently (2020 file P2).
  - V = 2G^{ij}∂_iW∂_jW − (4/3)W² with ½G from (5.16), G = diag(6/Σ², 2/Ω², 4).
  - **Normalisation check:** pulled back to (φ, λ, w), 3(d ln Σ)² + (d ln Ω)² + 2dϕ² = 30dφ² + 30dλ² + (3/2)dw², i.e. G = diag(60, 60, 3) (pp_b2_w.log). So 2G^{ij} = 2/60 = 1/30 on the (φ, λ) slice, which is exactly B1's V = (1/30)|∇W|² − (4/3)W². ✓
  - **PP addition (PROVED):** ∂_wW|_{w=0} = 0 and (G^{−1}∇W)_w|_{w=0} = 0, so w = 0 is invariant under the 3-scalar N = 2 gradient flow. NL left this unchecked; it is needed for "the B1 flows are flows of the N = 2 subtruncation".
- **C3 (CONDITIONAL, agree).**
  - It rests on the general N = 2, D = 5 fermion-shift formulas.
  - "Preserving 4 of the N = 2 subtruncation's 8 supercharges" is correct, and matches 2020 fix F3.
- **C4 (CONDITIONAL, agree).** This is group theory only; the N = 4 shift matrix was not evaluated. The "8 Poincaré" claim stays CONDITIONAL.
- **C5 (NL PROVED → PP PROVED as an implication from the stated 5D KSE; iff and the coefficient 4 checked).**
  - **Setup used:** the 5D KSE δψ_r: ε′ + (W̃/6)γ_rε = 0 and δψ_x: ½A′γ_rε + (W̃/6)ε = 0, with A′ = −W/3 on the kept side and the mirror image on r < 0. The normalisation of these equations is C3's, so C5 is an implication from them.
  - **(⇐)** With the flip W̃ = −W on r < 0:
    - A′(r<0) = +W/3, so ½(W/3)s − W/6 = 0 gives s = +1.
    - The radial equation gives ε′/ε = +W/6 = A′/2, so ε = e^{A(|r|)/2}ε₀.
    - ε is continuous, and ε(−r) = γ_rε(r) = ε(r) holds. A nonzero ℤ₂-even Killing spinor exists. ✓
  - **(⇒)** Without the flip (W̃ = +W on r < 0): s = −1 on r < 0 and s = +1 on r > 0. A continuous ε would need γ_rε(0) = ±ε(0), so ε(0) = 0, and by uniqueness of the linear radial ODE ε ≡ 0. ✓
  - The scalar (hyperino/gaugino-type) projections are consistent: on the image X′ = −∇W/30 = ∇W̃/30.
  - **Caveats (fix G2):**
    - (a) The iff holds within the dichotomy W̃ ∈ {+W, −W} on the image (piecewise-constant sgn g).
    - (b) It needs **W(X_w) ≠ 0**. At W(X_w) = 0 (the P = 0 locus that branch +1 crosses) A′ = 0, δψ_x imposes no projection, and both cases admit spinors.
  - **Coefficient 4:** correct, but it comes from the gravitational junction ([A′] = −T/6 together with [A′] = −2W/3), i.e. 2020 B4a. It does not come from the KSE: W̃′ does not appear in δψ_r or δψ_x. "δ-function balance gives W̃′ ⊃ 2Wδ" should be restated as "the Israel jump of A′" (fix G3).
- **C6 (NL CONDITIONAL → PP: bosonic part PROVED; spinor clause OPEN, and in conflict with D4 — see X1).**
  - **Bosonic part (PROVED):** at fixed gA^{ij}, (2.5) is even in g. (2.6) is odd term by term: the g⁻³ term; the DT term; and the F term g⁻³·g·F with F = g⁻¹R̄, which is g⁻³ overall. S₍₃₎ = 0. The 11D symmetry r → −r with C → −C is standard (CS term (−1)³ × (−1) = +1).
  - **Spinor clause** ("the surviving spinors at the wall satisfy Γ_rε = +ε, the HW projection", with Γ_r = γ_r ⊗ 1): not supportable together with D4 (X1). The internal Killing spinor on the S⁴ fibre depends on the sign of the flux, so the lifted 11D spinor need not be continuous across a g-flip.
- **C7 (NL PROVED → PP PROVED as logic, but vacuous as an argument).**
  - Given X1, C3 and C6's spinor clause cannot both hold with D1's hypotheses, so "B4–B7 stand as statements about supersymmetric walls" is not established through C3 + C6.
  - The 2020 file's P1/P3 make it unnecessary anyway: B4–B7 hold for **all** IR-regular level-0 walls, supersymmetric or not.
  - Fix G4.

## 2. B12 file (f8801bff…, NL 4/2/1/0) and Erratum 18-B12
- **D1 (PROVED, agree; PP re-derived the identity and the C6 kernel analytically).**
  - **Jump derivation.** Take Gaussian normal coordinates, with ω_a^{bn} = K_a^b on the kept side and −K_a^b on the image. The tangential G is odd and jumps by 2G; the normal-leg G is continuous; ε and ∂_aε are continuous. The jump of the tangential KSE is K_a^bΓ_bΓ_nε + (2/288)(Γ_a^{bcde}G_bcde − 8Γ^{cde}G_acde)ε = 0.
  - With Γ_a^{bcde}G_bcde = Γ_aG̸ − 4Γ^{cde}G_acde and Γ_nε = ±ε, this gives **K_abΓ^bε = −σ(1/144)(Γ_aG̸ − 12Γ^{cde}G_acde)ε**. ✓
  - **C6 kernel, exact rather than float.** Only G₇₈₉₁₀ = −6qk_x is nonzero. The x and Σ rows give Γ^{78910}ε = (σ/q)ε. The T rows give Γ_a(k_T + 2k_x)ε = 0, which holds iff k_T = −2k_x. The projections Γ^{78910} and Γ_n commute, so the kernel has dimension 32/4 = **8**. ✓
  - Controls: k_T = −1.5k_x leaves a factor 0.5·Γ_aε, so the kernel is 0; the MN2-type face with G = 0 has k_xΓ_aε = 0, so the kernel is 0. ✓
  - Hypotheses (i)–(iv) are part of the claim, so D1 is graded as an implication from them.
- **D2 (PROVED, agree — trace identity checked, as NL asked).**
  - The x-row (Γ^{cde}G_{μcde} = 0, no x-legs) gives G̸ε = −144σk_xε.
  - Contract the six internal rows with Γ^a. The left side is K_abΓ^aΓ^bε = K_int ε, using K symmetric and K_{xi} = 0. On the right, Γ^aΓ_a = 6, and Γ^aΓ^{cde}G_acde = G̸ (the δ-terms vanish by antisymmetry; G has internal legs only). So the right side is −(σ/144)(6 − 12)G̸ε = −6k_x ε.
  - Hence **K_int = −6k_x**, K = −2k_x, and **ρ = (2/κ²)(k_x − K) = 6k_x/κ²**. The mean internal S is −(2/κ²)(K_int/6 − K) = −(2/κ²)k_x = −ρ/3.
  - **Agreement with PP §1.1 v2 (84f49882, C2):** that file has ρ = (2/κ²)(k_x − K), with K = −2k_x on the C4 family giving ρ = 6k_x/κ². That is the same trace pattern. D2 shows it is *forced* pointwise by HW-type supersymmetry, whatever the wall content. ✓ Also consistent with C6 (K_int = 2k_x + 4(−2k_x) = −6k_x).
  - "Y15 needs k_x ≥ 0" ✓: M := (K − k_xh)|_int ≤ 0 implies tr M = −12k_x ≤ 0.
- **D3 (PROVED, agree; strengthened).**
  - Recomputed by hand: K_int = 6f − ½D and 6k_x = 6a − 12f + D, so (K_int + 6k_x)/ε = 6a − 6f + ½h∂_λ ln Δ. ✓
  - ∂_λ ln Δ runs over [−6, 4], so pointwise in χ the identity needs h = 0 and a = f.
  - On W-flows: −6X + 12v − 12 = 0 and −2X + 24v + 16 = 0 give X = 2v − 2 and then 20v = −20, so v = −1. No solution. ✓
  - **Strengthening:** by 2020 P1, every IR-regular level-0 kept side is a W-flow. So D3 excludes every level-0 wall that is 11D-HW-supersymmetric (D1 hypotheses), whatever the content, σ < 0 included.
  - "Kills the B10 fix in that sector" ✓, in the 11D HW-BPS sense.
- **D4 (PROVED with the Erratum 18-B12 constant, as NL asked; the zeroth-order mismatch checked).**
  - At the exact MN2 face (normal into the kept side), k_x = −ε/L and K_int = 0 (φ′ = λ′ = 0, Σ and fibre warps constant). So **K_int + 6k_x = −6ε/L**. ✓ This is the zeroth-order mismatch, and it does not depend on content or sector.
  - **Radius.** Let "within δ" mean ‖K − K_MN2‖_op ≤ δ pointwise in an orthonormal frame. Then |ΔK_int| ≤ 6δ (trace of 6 internal entries) and |6Δk_x| ≤ 6δ, so the total is ≤ **12δ**. D2 needs 12δ ≥ 6ε/L, so it **fails for δ < ½ε/L** pointwise, and uniformly for δ < ½ min_{S⁴} ε/L. The NEC margin is k_v − k_x ≥ ε/L − 2δ, with the same threshold ½.
  - **Erratum 18-B12 (E18-1, PROVED): correct** (10δ, 3/5 → 12δ, ½). The original "10δ" undercounted.
  - **Wording fixes (G5):**
    - (a) State the norm used for "within δ".
    - (b) "Any BPS wall must have k_x ≥ 0" holds only with NEC-respecting (or ρ ≥ 0) content. D2 alone gives ρ = 6k_x/κ², and σ < 0 content can have k_x < 0.
    - (c) "Must turn around along every normal ray" needs that same qualifier.
    - (d) "Near MN2" is closeness in extrinsic curvature, not in field-space distance.
- **D5 (CONDITIONAL, agree; sign disagreement).**
  - From the D1 rows as printed, PP gets **(k_Σ − k_x)ε = +σ·½Γ^{Σ₁Σ₂}ω̸ε**. NL has −σ·½.
  - Derivation: subtract the x-row from the Σ₁-row. Then Γ_{Σ₁}Γ^{cde}G_{Σ₁cde} = 6Γ^{Σ₁Σ₂}ω̸ (checked numerically, pp_d5_sign.log, residual 5e-15 for +, 129 for −), times 12σ/144.
  - σ is a convention sign, but it is fixed once D2's x-row is used, so the relative sign matters (fix G6).
  - The level-0 conclusion does not depend on it: it comes from 2020 B7.
- **D6 (OPEN, agree).**
- **D7 (CONDITIONAL, agree; fixes).**
  - "2007 B4: 4 conditions become dependent" must read **3** (2020 file, B4b REFUTED; rank count 7 equations / 5 unknowns / rank 4).
  - "0 constraints become dependent" is vacuous; say "deficit not removed".
  - Say which "BPS" is meant (G7).

### X1 (PP, PROVED): the 5D BKV reading and the 11D HW reading are inconsistent at the MN2 face
- By C5 (⇐) with T = 4W*, a ℤ₂ wall placed on the exact MN2 face with g-flip is 5D-supersymmetric (an RS/BKV wall).
- Suppose it lifted (C3) to an 11D Killing spinor obeying D1 (ii) (continuous, Γ_nε = ±ε) with the flux jump sourced through the Bianchi identity (iii). Then D2 would force K_int + 6k_x = 0 on that face. But D4 gives −6ε/L ≠ 0. Contradiction.
- **So {C3-lift, C6 spinor clause, D1 (ii)–(iii)} cannot all hold.** The likely failure is spinor continuity: the internal S⁴ Killing spinor changes with sgn(G).
- Consequences:
  - "5D BPS" (2012 file) and "11D HW-BPS" (2017 file) are **different conditions**, and must not be merged.
  - C7's discharge of B2 through C3 + C6 is unsound as an argument.
  - D3/D4 (11D) take precedence for HW-type walls.
- Nothing here affects B6/B7 or 2020 P3, which use no supersymmetry.

## 3. Tables
### B2 file (7 items)
| item | NL | PP | reason |
|---|---|---|---|
| C1 | PROVED | **PROVED** | rerun identical; exact |
| C2 | PROVED | **PROVED** | G = diag(60, 60, 3) ⇒ 2G^{ij} = 1/30 = B1 normalisation; w = 0 invariant (PP) |
| C3 | CONDITIONAL | **CONDITIONAL** | fermion shifts cited |
| C4 | CONDITIONAL | **CONDITIONAL** | N = 4 matrix not computed |
| C5 | PROVED | **PROVED** (implication from the stated 5D KSE) | iff both directions verified; needs W(X_w) ≠ 0; the 4 is from Israel, not the KSE |
| C6 | CONDITIONAL | **OPEN** | bosonic oddness PROVED; spinor clause conflicts with D4 (X1) |
| C7 | PROVED | **PROVED** (logic; vacuous route) | fix G4 |
NL 4/3/0/0 → **PP 4/2/1/0**.

### B12 file (7 items) + Erratum 18-B12 (1)
| item | NL | PP | reason |
|---|---|---|---|
| D1 | PROVED | **PROVED** | identity re-derived; 8-dim kernel analytic |
| D2 | PROVED | **PROVED** | trace contraction re-derived; = §1.1 v2 ρ = 6k_x/κ² |
| D3 | PROVED | **PROVED** | exact; with P1 covers all level-0 walls |
| D4 | PROVED | **PROVED** (with E18-1 constant) | −6ε/L verified; radius ½ε/L; wording G5 |
| D5 | CONDITIONAL | **CONDITIONAL** | sign +σ/2 per PP (G6) |
| D6 | OPEN | **OPEN** | — |
| D7 | CONDITIONAL | **CONDITIONAL** | 4 → 3 (G7) |
| E18-1 | PROVED | **PROVED** | 12δ, ½ |
NL 4/2/1/0 + 1/0/0/0 → **PP 4/2/1/0 + 1/0/0/0** (no grade change).
PP-own items (all PROVED): X1; w = 0 invariance; C6 kernel analytic.
**Combined PP tally for this file (15 items): PROVED 9 · CONDITIONAL 4 · OPEN 2 · REFUTED 0. PENDING 0.**

## 4. Erratum 18 (2003, af7a8199…) — faithfulness confirmation against PP 99593076 and 84f49882
- **Integrity.** sha = sidecar, mtime 20:03:56, filename 2003. The quoted shas of 99593076…, 84f49882… and d365c611… are correct (PP rechecked the prefixes).
- **K-fixes, all applied faithfully:**
  - Fix 1 (BF double root; alternate quantisation): ✓ (E18 K1).
  - Fix 2 (Δ > 4; Δ = 4 CONDITIONAL; finite truncation and hyperbolicity): ✓ (E18-K2Δ4).
  - Fix 3 (force balance algebraic in σ): ✓.
  - Fix 4 (independence as an explicit hypothesis): ✓. No M = 2 rank computation was done; this is disclosed in §5 and acceptable.
  - Fix 5 (H_m/P_m subtraction): **retracted** rather than justified ✓ (E18-K6).
  - Fix 6 (heuristic; "generically closed" retracted; replacement "heuristically overdetermined by ≥ 1 + n_rel ≥ 2 (CONDITIONAL); not closed"): ✓, verbatim.
  - Fix 7 (Y15 face data and orientation): ✓.
  - Fix 8 (parity wording + K5 hypotheses (i)–(v)): ✓. NL lists (i)–(v) under its "K5" bullet rather than "K8"; the content is complete.
  - Fix 9 (K7 cites C6): ✓.
- **Grades:** K6 OPEN, K6′ CONDITIONAL, K7 OPEN, and 1948 revised to 4/1/3/0 (+K6′ COND). This matches PP 99593076 §4 ✓.
- **84f49882 (§1.1 v2):** C1 steps 1–5 (λ₀ = −2(λ₁ + λ₂), D′ = cD, 2λ_a′ = c, 5c/2 = 0, ρ = 0), C2 (ρ = (2/κ²)(k_x − K), ρ = 6k_x/κ² on C4) and C3 (N3 → H2) are reproduced faithfully. v1 (ec88137a) is correctly marked not used ✓.
- **F9 "§6 → §5"** ✓. **Y15 location pointer** ✓.
- **Verdict: Erratum 18 is FAITHFUL** (PROVED as a bookkeeping check).
- Cosmetic: the erratum's own tally counts the pre-existing K7 among its OPEN items. This is acceptable, since it is disclosed.

## 5. Numbered fixes for NL
1. **G1.** b2/b12 sidecars are post-run integrity sidecars. Freeze each .py sidecar before running.
2. **G2.** C5: state the dichotomy W̃ ∈ {±W} and the hypothesis W(X_w) ≠ 0.
3. **G3.** C5: the coefficient 4 comes from the Israel jump [A′] = −T/6 = −2W/3 (2020 B4a), not from "W̃′ δ-balance" in the KSE.
4. **G4.** C6/C7: downgrade the spinor clause to OPEN and cite X1. Say "5D-BPS (BKV)" and "11D HW-BPS (D1)" separately everywhere. Base B4–B7's level-0 validity on 2020 P1/P3 (no supersymmetry needed), not on C3 + C6.
5. **G5.** D4: define "within δ" (operator norm of the shape-operator difference, orthonormal frame). Restrict "k_x ≥ 0 / warp must turn around" to NEC-respecting or ρ ≥ 0 content. Say that "near" is in extrinsic curvature. Cite the radius as ½ min ε/L (Erratum 18-B12).
6. **G6.** D5: recheck the sign. PP obtains +σ·½Γ^{Σ₁Σ₂}ω̸ from the D1 rows as printed.
7. **G7.** D7 (and 2007 B13): "4 conditions dependent" → **3**; drop "0 dependent constraints"; name which BPS notion is meant.
8. **G8.** D3: add that, by 2020 P1, the exclusion covers every IR-regular level-0 wall.

## 6. Junction implication
- Proved this round:
  - At the MN2 face, no 11D HW-type supersymmetric ℤ₂ wall exists, with any content, within ½ε/L in extrinsic curvature (D4).
  - In the whole level-0 sector, none exists at all (D3 + P1).
  - HW-type supersymmetry forces ρ = 6k_x/κ² and K_int = −6k_x pointwise (D2), matching the C4 / §1.1 v2 pattern.
- Open: χ-dependent finite-amplitude walls (D6); the sign question of D5; NEC-violating sources; UV side kept.
- **Junction: UNSOLVED.** Nothing adopted.

Tip at write time: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (unchanged). No CERT. Nothing sent.
