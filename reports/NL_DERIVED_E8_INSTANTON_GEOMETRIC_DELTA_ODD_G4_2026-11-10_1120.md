# NL DERIVED: E₈ instanton stress vs the geometric delta in M5s + E₈ instantons = 2N_flux, under odd G₄ — geometry demands algebra (HW-type Z₂ fixed plane)
2026-11-10, written 11:20:43 CST (America/Chicago). Author: Non Local Path (NL). Everything below is an **NL derived proposal**. Additive new file; no existing file edited, renamed, deleted or chmod-ed. Wording: resonant algebra. **Junction UNSOLVED.** No CERT. No Gemini. No external sends. No agent messages.

## Header
**Authority (each sha re-hashed by NL = its sidecar):**
- OW **1108** call-83d7a0fa, OWNER_WRITE_CALL_83d7a0fa_PURSUE_HW_ODD_G4_BRIDGE_C_CLOSING_IMPLICATIONS_2026-11-10_1108.md, sha **c6375f853020e8e994125e1b42acffe830350db0b116b60f0f5f75abbb5f84ca**: pursuit directive only (NL item 1). Read in full.
- OW **1117** call-83d7a0fa, OWNER_WRITE_CALL_83d7a0fa_REVERSE_ENGINEER_FROM_GEOMETRY_2026-11-10_1117.md, sha **bff79185f361bf461194c8d8c9590a4dc7ad0e520ce2f985f41048453545a2f4**: method directive: reverse engineer from the geometry and report which geometric features force which algebraic forms. Hence §1 comes first.
- Standing **t4436** (32881263…): the math leads; every option is a labelled branch; only PP-audited PROVED/REFUTED keep or drop a branch; nothing adopted by fiat.
- **t4431** (f700141d…): 90% stop lifted; the plan's 100% limit still applies. Usage was not checked for this file.
- **f825dfff** (t4369): face = Z₂ fixed plane (HW-type wall); O1 odd, CONDITIONAL on P-b; E₈ wall sector CONDITIONAL.
- **7ff8299d** (t4377): earlier NL E₈-stress job. It stays on record, but see the dead-assumption sentence.
- The ant-colony/Taormina context record 6436510d… is not used.
- Agent-relayed text is not Owner text. The verbatim Owner words for 1108 come from MR2's note 79710111…, read as a cross-check only.

**Dead working assumption (Owner, 1108):** every prior calculation that assumed a pure uncharged M5-brane stack is dead as the working assumption for this pursuit. Nowhere below is "all 9760 units are uncharged M5s" used. Sources are split as N_M5 + n_inst = 2N_flux, and the instanton piece is isolated. The dead-assumption files are read only, not edited.

**Nothing adopted:**
- N = 4880 and total charge 9760 are **labelled test targets** from 1108, not physical inputs.
- The tension-to-charge figures 1.26–1.33 and 5/3, and NL's earlier interval (1.255, 1.667), are **not adopted**. On-record N_req values appear only as test targets, marked CONDITIONAL.
- 1a is not adopted as the physical wall. B1-c2′ overall is not adopted as the KK scope. The E₈ wall sector stays CONDITIONAL, gated by instanton backreaction.
- MR2's 1a, C2′, ESPM-delta and wall-Bianchi files (e.g. PP e2750e28 on MR2 79795981) were read as literature only, not as NL's working geometry or branch status.
- Starting from the junction does not treat it as solved.

**Tip:** /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 at 11:10, 11:18 and 11:19 CST before writing, and re-hashed after writing (see the sidecar check in the report back). Never edited.

**Script** (new directory /workspace/nl-e8-delta-1110/; all files mode 444; the .py sidecar was frozen before the run and the .log sidecar sealed after):
- e8delta.py sha **13bcf9038f6be227536e3b2209a2958259d2819df6599c6e6a721e8431db25e8** (frozen 11:15:31.318 CST; run started 11:15:31.32, exit 0)
- e8delta_run.log sha **e9a8cfe94a21e2e7d02a87a3e8aa89cb478db707bedb50c2d1918e95426979da** (sealed 11:15:36 CST). 26/26 PASS.
- Zero tests are sympy `expand(...) == 0` on polynomials with exact coefficients, or exact Fraction/Rational comparisons. There is no simplify()==0 and no allclose. The YM stress is checked per Lie generator: tr with a positive Killing form is a sum of identical copies, so one generator is fully general.

**Conventions (PP):**
- K_ab = ∇_a n_b and k_t := −K(t̂,t̂). On the 10D Z₂ wall, S_ab = −(2/κ²)(K_ab − h_ab K).
- The wall is ℝ^{1,3} × Σ × fibre, with Y₆ = Σ ⋉ S⁴, Σ = Bolza (genus 2).
- "u" is the BPS instanton energy per unit charge in M5 units: u = 8π²/(λ²T_M5).

**Tally (header = body, items listed in §7):** PROVED **22** · CONDITIONAL **16** · OPEN **5** · REFUTED **2** = **45**.

---

## 1. Geometry → demanded algebra (lead section, per 1117)
Each row starts from a geometric feature of the HW-type fixed plane, the brane configuration or the junction, and states the algebraic form that feature forces.

| # | geometric feature | algebra it forces | label |
|---|---|---|---|
| GA1 | Codimension-1 **Z₂ fixed plane**: orientation-reversing x¹¹, two-sided mirror | The jump is doubled, [K] = 2K⁺. Israel: K_ab − h_abK = −(κ²/2)S_ab. Inverse: K = κ²S/18, K_ab = −(κ²/2)(S_ab − h_abS/9). Null k: S(k,k) = −(2/κ²)K(k,k). | PROVED (algebra; Y0) |
| GA2 | Fixed plane with **P-b** (the Z₂ includes C∧G∧G and C∧I₈) | C_tan is odd. Then G_tan(0⁺) = −G_tan(0⁻), and the jump is 2G_tan(0⁺) = (closed wall 4-form density). The boundary value of G_tan is fixed pointwise by the wall charge density: G_tan(0⁺) = ½ × (M5 density + I₄). | CONDITIONAL (P-b; HW boundary condition) |
| GA3 | A **10D boundary with chiral bulk fields** (gravitational anomaly inflow) | One E₈ vector multiplet per wall (rank 248) and the specific 4-form I₄ = (tr F∧F − ½tr R∧R)/16π² in dG₄. λ⁶ ∝ κ⁴. | CONDITIONAL (HW 9603142; not re-derived) |
| GA4 | **Fibre S⁴** (stably trivial tangent bundle: TS⁴ ⊕ ℝ = ℝ⁵) | p₁(TS⁴) = 0, so ∫_{S⁴} tr R∧R = 0 for every metric (warped or squashed). **The geometric part of the charge is exactly 0**, and the fibre-integrated Bianchi has no curvature correction: N_M5 + n_inst = 2N_flux. | PROVED (p₁ step; 1750 E1-p₁) |
| GA5 | Static face, Poincaré-invariant along x; **product wall ℝ^{1,3} × Σ² × fibre⁴**; a magnetic E₈ field with legs on Y₆ | The stress is forced into blocks. x-block −ρη_μν exactly. Y₆ blocks S_ab = (1/λ²)Σ_c tr F_acF_bc − ρδ_ab. x–Y₆ and t–Y₆ mixed blocks vanish. Trace −6ρ. | PROVED (e8delta C1a–C1e) |
| GA6 | **4-dimensional fibre** (Hodge ⋆ on Λ², ⋆² = 1) | Λ² = Λ⁺ ⊕ Λ⁻. Pointwise Bogomolny: ρ − q/2 = ½Σ_{3 pairs}(F − ⋆F)² ≥ 0, where q is the topological density. Equality holds iff F is self-dual (SD). The SD stress is the smeared-M5 equation of state. | PROVED (C2a–C2e) |
| GA7a | **Warped wall**: weight W = c_x²c_Σ = Δ̃e^{4f+2g}, not a conformal factor of g₄ | The weighted equation D(W⋆₄F) = 0 with SD F forces dW ∧ F = 0, so F = 0 wherever dW ≠ 0. Static finite-size SD fields vanish; the BPS sector is forced to **zero size** (point-like, M5-like). | PROVED (for the stated equation; 1800 Y6-math, PP fe0c3d92) |
| GA7b | The same, applied to the full HW system | Requires a constant face, a fibre-only field, and neglect of the C₃–tr F∧F couplings and of tr R². | CONDITIONAL (Y6-phys) |
| GA8 | **Junction geometry at the end faces**: flow-face extrinsic curvature with K(ê_fib,ê_fib) − k_t > 0, i.e. w_fib = −6/5 (UV), −4/3 (IR) | The geometry demands wall stress with **S(k,k) < 0** along fibre null directions, i.e. NEC-violating algebra. Every E₈ field (electric legs included) gives S(k,k) = Σ_{c∉{t,j}} F(k,e_c)² ≥ 0. Every positive-tension brane gives ≥ 0, **whatever its charge**. So no E₈ + positive-tension-brane content supplies the demanded form. | PROVED given J1 (C1f, C3, C6) |
| GA8-int | The same on interior flow faces | As GA8, from the 1711 E2 and Y15-int numerics. | CONDITIONAL |
| GA9 | Junction, positively: **what does supply S(k,k) < 0 of size O(N)?** | Only objects outside {E₈ YM, positive-tension branes} remain: negative-tension or orientifold-like content, higher-derivative wall stress, or a non-constant or backreacted face. Of these, the HW tr R² term has the right sign at the UV end but is O(1/N) (Y16 Q7). The algebraic object the junction demands at O(N) is not identified. | OPEN |
| GA10 | **Σ hyperbolic with twist** (charged fibre blocks forced to carry Σ legs Φ·F_tw) | S^Σ_Σ − S^x_x = (1/λ²)|F(ê_σ,·)|² ≥ 0. Σ legs push the Σ–x difference in a fixed sign; M5s of either sign cancel from it. | PROVED (C1g; Y15 I1) |
| GA11 | **Mirror doubling acts on geometry and flux alike**: [K] = 2K⁺ and [G_tan] = 2G⁺ | The factor 2 cancels in every tension-to-charge ratio. The odd projection does not rescale u or N_req/(2N_flux). | PROVED (C5) |
| GA12 | **Small-instanton geometry** (a zero-size SD instanton at y₀ coincides with an M5 at y₀; both carry the same weight W(y₀)) | If energy is continuous in the size → 0 limit, the energy per charge must match: **u = 1**. | PROVED (as an implication) |
| GA13 | HW-printed λ² (u = 2) together with GA12's continuity | Contradiction: a jump of (u − 1)·W(y₀)·T_M5 per unit charge at zero size. | REFUTED (by GA12) |
| GA14 | u = 1 as the physical value | Conrad hep-th/9708031 / Lü hep-th/9711014 give λ⁶/κ⁴ = (4π)⁵, so u = 1 exactly (e8delta C4a reproduces u = 2 / u = 1 from the two λ²). The anomaly derivation is not re-checked. | CONDITIONAL (PP-1) |

**What the geometry forces, in one line:**
- The fixed plane forces the doubled Israel algebra and an odd G_tan whose boundary value equals half the wall charge (GA1, GA2).
- S⁴ forces a curvature-free charge equation (GA4).
- The 4D fibre forces Bogomolny, i.e. BPS ⇔ SD ⇔ M5 equation of state (GA6).
- The warp forces BPS instantons to zero size, so they are M5-like (GA7).
- The junction forces NEC-violating wall algebra, which E₈ YM cannot provide (GA8, GA9).

## 2. What "the exact geometric delta in the anomaly-matching equation" can mean
Set-up (charge side). The fibre-integrated Bianchi identity at the odd wall is

  N_M5 + n_inst + n_R = 2N_flux, with n_inst = (1/8π²)∫_{S⁴} tr F∧F and n_R = −(1/2)(1/8π²)∫_{S⁴} tr R∧R.

The target 2N_flux = 9760 at N_flux = 4880 is a 1108 label (e8delta C4d).

Set-up (tension side). The Israel x-equation, integrated over the fibre with √g₄, defines a **source-free geometric number**: N_req T_M5 := ∫(2/κ²)(k_x − K)√g₄ d⁴y. Its definition uses no source model.

Five precise candidates:
- **D-A, the charge delta.** The geometric (curvature) term n_R in the anomaly-matching equation.
- **D-B, the integrated tension–charge delta.** Δ_N := N_req − 2N_flux.
- **D-C, the pointwise x-block delta.** Δ(y) := ρ_req(y)/T_M5 − q_tot(y), with ρ_req = (2/κ²)(k_x − K) and q_tot the local wall charge density.
- **D-D, the full tensor delta.** Δ_ab := S_ab^req − S_ab^sources, in every block.
- **D-E, the odd-G₄ boundary-value delta.** G_tan(0⁺) − ½(q_M5 + I₄).

## 3. The isolated E₈ instanton stress under odd G₄
- **S1 [PROVED; C2a–C2d]. Fibre-only, SD (BPS) field.**
  - S^inst_ab = (1/λ²)tr(F_acF_b^c − ¼h_abF²) has worldvolume (t, x, Σ) block −ρ_inst h_ab, fibre block 0 and mixed blocks 0.
  - Trace −6ρ_inst.
  - **Pointwise ρ_inst = q_inst/2** in field units, i.e. ρ_inst(y)√g₄ = u T_M5 × (instanton charge density)(y).
  - Israel then gives K^wv = κ²ρ/6 and K^fib = −κ²ρ/3 (ratio −2, the smeared-M5 face).
- **S2 [PROVED; C1, C2e, C2f]. General static magnetic field on Y₆.**
  - x-block −ρη.
  - Σ block (1/λ²)Σ_c tr F_σcF_τc − ρδ, and fibre block (1/λ²)Σ_c tr F_acF_bc − ρδ.
  - Σ–fibre mixed block (1/λ²)Σ_c tr F_σcF_ac. It must vanish wherever the face's K is block-diagonal.
  - For fibre-only fields the fibre block is traceless.
  - The excess energy over BPS is pointwise ρ − q/2 = ½Σ(F − ⋆F)² ≥ 0.
- **S3 [PROVED]. C∧G∧G content.** C∧G∧G is metric-independent, so its variation with respect to h_ab is zero. It adds **no** stress, localized or bulk. It is Z₂-invariant under P-b.
- **S4 [OPEN]. C∧I₈ (C∧X₈) content.** Its stress is metric-dependent through curvature. Since ∂₁₁G_tan has a δ-jump at the odd wall, a δ-supported stress of the form (jump of G_tan) × (curvature)³ may appear.
  - Coefficient and sign: OPEN.
  - Naive scaling, ℓ_P⁶/L⁶ ∝ N⁻² relative to the source tension: not proved.
- **S5 [CONDITIONAL; HW/standard sugra; 1711 G1]. Bulk G₄ stress.**
  - The bulk G₄ kinetic stress is continuous across the wall, because odd G squared is even. So odd G₄ produces **no** δ-stress from the kinetic term, and the odd projection acts on the instanton's charge (GA2, D-E), not on S^inst.
  - S^inst itself is built from the Z₂-invariant wall field A and is neither projected nor doubled. The doubling sits in [K] and [G] and cancels in ratios (GA11).
  - CONDITIONAL on the HW treatment of the δ(0)-type terms in the G₄ action.
- **S6 [CONDITIONAL]. Normalization.** ρ_inst in M5 units carries u (GA14).
  - The tensor's **form**, i.e. its blocks, signs and trace, is normalization-free.

Short formula: **S^inst_ab = (1/λ²)tr(F_acF_b^c − ¼h_abF_cdF^cd).** For BPS fibre fields this is diag(−ρh_wv, 0_fib) with ∫ρ√g₄ = u·n_inst·T_M5; under odd G₄ the field is unprojected and the jump is doubled in both K and G₄.

## 4. Tests: does the localized instanton stress make up the exact geometric delta?
- **D-A [PROVED; GA4].** n_R = 0 exactly. **There is no geometric charge delta to make up.**
  - n_inst is a share of 2N_flux, not a correction to it.
  - The tr R² term has zero charge but nonzero wall energy (Y16 Q5: −u M5 units per fibre at the UV end). Instanton energy is ≥ 0 (C1c) and does not cancel it.
- **D-B1 [CONDITIONAL on u = 1, GA14].** Tension in M5 units is T = N_M5 + u·n_inst + ε_ex = 2N_flux + (u − 1)n_inst + ε_ex (C4b).
  - At u = 1, dT/dn_inst = 0 (C4c). Trading M5s for BPS instantons changes nothing, and BPS instantons make up **none** of Δ_N.
  - Δ_N is split-invariant under BPS trades. This statement is derived, not asserted by fiat.
- **D-B2 [CONDITIONAL on u ≠ 1 and on failure of GA12-continuity and of GA7b].** For a BPS split to make up Δ_N exactly, n_inst = Δ_N/(u − 1) ≤ 2N_flux, i.e. u ≥ 1 + Δ_N/(2N_flux) (C4g).
  - At u = 2, the on-record targets (CONDITIONAL, not adopted) need n_inst = Δ_N ∈ {2808.6, 2492.1, 3052.2, 3182.4, 6506.7} (MN2, MN1, z=2, z=3, UV). All are ≤ 9760 (C4f).
  - But GA13 refutes u = 2 with continuity, and GA7 forces static BPS instantons on constant flow faces to zero size. **The branch survives only if both fail.**
- **D-B3 [OPEN].** **Exact** makeup by non-BPS excess, ε_ex = Δ_N, with ε_ex = ∫½Σ(F − ⋆F)²/(λ²T_M5) (S2).
  - Magnitude closure is on record as CONDITIONAL (Y14 stage 2 S11/S12′, u-dependent).
  - Exact equality with the pointwise profile is not shown.
- **D-C [CONDITIONAL on u = 1 and GA2].** For BPS sources at u = 1, ρ_BPS(y) = T_M5 q_tot(y) pointwise (S1 plus M5s). The odd-G₄ boundary condition fixes q_tot(y) = 2G_fib^flow(r_b, y)/(2π)³.
  - So the pointwise delta Δ(y) = ρ_req(y)/T_M5 − 2G_fib^flow(y)/(2π)³ is **purely geometric and flux-determined**, the same for every M5/instanton split.
  - Only non-BPS density ½Σ(F − ⋆F)² can shift it, and it must match the profile of Δ(y), not just its integral.
- **D-D [REFUTED, proof given J1 at the end faces; interior per GA8-int].** Claim tested: "localized E₈ stress (BPS or not), with any M5 content, equals the exact tensor delta".
  - GA8 demands S(k,k) < 0 in the fibre directions. C3 gives S^inst(k,k) ≥ 0 for every field, and positive-tension branes of any charge give ≥ 0.
  - Required w_fib = −6/5 and −4/3 < −1 ≤ w_a (C1f, C6).
  - This holds with or without the dead assumption.
- **D-E [CONDITIONAL; GA2].** In the G₄ sense the instanton density **does** enter exactly: G_tan(0⁺) = ½(q_M5 + q_inst + I₄^R), with I₄^R integrating to 0 (GA4).
  - This is a charge identity. It does not enter the stress.
- **V [CONDITIONAL]. Verdict.**
  - **No.** The localized instanton stress does not make up the exact geometric delta.
  - (i) The charge-side geometric delta is 0, so there is nothing to make up (D-A).
  - (ii) The integrated tension–charge delta is untouched by BPS instantons if u = 1 (D-B1). BPS makeup needs u ≠ 1 plus failure of GA12 and GA7b (D-B2). Exact non-BPS makeup is OPEN (D-B3).
  - (iii) The tensor delta is never made up (D-D).
  - The only "exact" sense in which instantons fill the delta is the odd-G₄ boundary value (D-E): a charge statement, not a stress statement.
  - Restrictions: D-B1 and D-C hold for BPS/SD, fibre-supported fields only. D-D holds without dropping tr R², because the tr R² stress is O(1/N) by Y16 Q7, which is PROVED given J1.

## 5. Re-examination of prior NL claims without the uncharged-M5-stack assumption
All files below were read only; each sha equals its sidecar.

- **R1 [PROVED, survives] Y0.** The Israel inversion is pure algebra.
- **R2 [PROVED, survives] Y1-stress.** The formula, sign and trace (C1b); the HW coefficient is S6.
- **R3 [PROVED, survives]** Y2, Y3-ineq, Y4-end, 1750 E2 and E2-end. They use only the YM sign and S_brane(k,k) ≥ 0 for positive-tension branes of **any** charge (C1f, C3), never tension = charge.
- **R4 [PROVED, survives] Y5/E3.** Smeared-M5-like SD stress (C2a–C2c).
- **R5 [CONDITIONAL, survives] Y8/E1/Q12a.** N_M5 + n_inst = 2N_flux. This is itself the split, HW-CONDITIONAL, with the p₁ step PROVED.
- **R6 [PROVED, survives] Y9.** Σ-wrapped instantons are absent from the fibre tadpole.
- **R7 [PROVED, survives and strengthened] Y11.** Weighted Bogomolny, now also pointwise (C2e).
- **R8 [CONDITIONAL, narrowed] Y10, 1750 E4 and L4.** "BPS n_inst leaves the count gap unchanged" did not assume all units are M5s. It does assume an energy per charge of 1 for instantons, so it holds iff u = 1 (GA14), or via GA7b + GA12. It is not unconditional.
- **R9 [OPEN, reopened] 1711 AB2 and G2-odd.** Their conclusions "b = N_req⁻¹(N_b), N_b = 2N_flux, no solution" equate tension units with charge 2N_flux, which is the dead assumption.
  - Restated: b = N_req⁻¹(2N_flux + (u − 1)n_inst + ε_ex). The old form is recovered at u = 1, ε_ex = 0.
  - b for a given split is OPEN.
- **R10 [PROVED].** N_req is defined source-free (§2). Its numerics are CONDITIONAL and not adopted.
  - The reading "the gap means no solution" needed the dead assumption.
  - The gap now reads: tension that must be carried by non-BPS E₈ excess, u ≠ 1, or uncharged/NEC-violating content.
- **R11 [PROVED, survives] Y15-1, I1, I2, Y15-trace, Y15-IR (REFUTED) and E17-NEC-IR.** I1 holds for σ of either sign; I2 needs only σ ≥ 0. Neither uses charge–tension identification.
- **R12 [PROVED given J1, survives] Y16 Q7/Q11a.** The requirement is geometric, ∝ N; the R² supply is N-independent.
- **R13 [CONDITIONAL, unchanged] Y14 stage 2 S11-count/S12′.** "Count gap closes in magnitude": already a split with non-BPS energy; u-dependent.
- **R14 [CONDITIONAL, unchanged] L3-sources.** The tr R² neglect caveat (PP bf4773a8).

## 6. OPEN items and the gating
- GA9: the algebraic source the junction demands at O(N).
- S4: δ-stress from C∧X₈ at the odd wall.
- D-B3: exact non-BPS makeup of Δ_N, with profile.
- R9: b given a split.
- **O5 [OPEN]. Instanton backreaction across the flow**, the 1108 gate. This needs non-constant or backreacted faces (1750 K5, T3, L5).
  - GA7, GA8 and D-D are proved on constant flow faces of the unbackreacted flow only.
  - A backreacted face changes k_a, and hence N_req and Δ(y), themselves.

## 7. Tally (header = body)
| label | count | items |
|---|---|---|
| PROVED | 22 | GA1, GA4, GA5, GA6, GA7a, GA8, GA10, GA11, GA12, S1, S2, S3, D-A, R1, R2, R3, R4, R6, R7, R10, R11, R12 |
| CONDITIONAL | 16 | GA2, GA3, GA7b, GA8-int, GA14, S5, S6, D-B1, D-B2, D-C, D-E, V, R5, R8, R13, R14 |
| OPEN | 5 | GA9, S4, D-B3, R9, O5 |
| REFUTED | 2 | GA13, D-D |

Check: 22 + 16 + 5 + 2 = 45.

Junction UNSOLVED. Count gap: not asserted unchanged by fiat. It is split-invariant only under u = 1 for BPS trades (D-B1, CONDITIONAL). Nothing adopted. No CERT. Tip 7cddb188… untouched.
