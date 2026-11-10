# FINDINGS: PP audit of NL 79ad0c64 (E₈ instanton stress vs the geometric delta under odd G₄; geometry → algebra, per OW 1108 and OW 1117)
2026-11-10, written 11:37:34 CST (America/Chicago). Author: **Professor Proof (PP), Soft SF audit.** Additive new file; no existing file edited, renamed, deleted or chmod-ed. **Nothing adopted.** **Junction UNSOLVED.** No CERT. Wording: resonant algebra. No message sent (no SendToAgent, no SendToUser, no external send).

## 0. Authority (each sha re-hashed by PP = its sidecar)
- **OW 1108** OWNER_WRITE_CALL_83d7a0fa_PURSUE_HW_ODD_G4_BRIDGE_C_CLOSING_IMPLICATIONS_2026-11-10_1108.md, sha c6375f853020e8e994125e1b42acffe830350db0b116b60f0f5f75abbb5f84ca = sidecar. Pursuit only. NL item 1 (does the localized E₈ instanton stress make up the exact geometric delta in M5s + E₈ instantons = 2N at N = 4880, charge 9760; isolate the instanton tensor under odd G₄). N = 4880 and 9760 are labelled test targets, not adopted. Tension-to-charge figures (1.26–1.33, 5/3, NL's interval) not adopted. 1a not adopted. E₈ wall sector CONDITIONAL, gated by backreaction. The pure-uncharged-M5 premise is dead as the working assumption, not refuted by fiat.
- **OW 1117** OWNER_WRITE_CALL_83d7a0fa_REVERSE_ENGINEER_FROM_GEOMETRY_2026-11-10_1117.md, sha bff79185f361bf461194c8d8c9590a4dc7ad0e520ce2f985f41048453545a2f4 = sidecar. Method directive; does not cancel 1108; PP audits as filed; no first-prove; no regrade by fiat.
- **Standing t4436** OWNER_WRITE_MAINCHAT_t4436_LET_MATH_LEAD_ALL_OPEN_PATHS_2026-11-09_2127.md, sha 328812635d807f5cb7d1e5e6b5df7f89512060c36c090a2a191526ab7e90fd46 = sidecar.
- f825dfff (t4369) OWNER_WRITE_MAINCHAT_t4369_FACE_Z2_FIXED_PLANE_HW_WALL_G4_ODD_O1_RESOLVED_2026-11-09_1745.md, sha f825dfffb8cd17a7f3f57a2b0a70bd0d9c9d73f215febffdbd2ca95b494d7cd1 = sidecar.
- Agent-relayed text (NL's request message) is not treated as Owner text. MR2 1a / C2′ / ESPM-delta / wall-Bianchi files (incl. PP e2750e28 on MR2 79795981) are literature only for this audit.

## 1. Integrity
| object | sha256 (PP re-hash) | = sidecar | mode | note |
|---|---|---|---|---|
| NL filing NL_DERIVED_E8_INSTANTON_GEOMETRIC_DELTA_ODD_G4_2026-11-10_1120.md | 79ad0c6417e825d4fee8d412af62a767688b883a88c39c6a6affd716ce4ffa29 | yes | 644 (sidecar 644) | header "written 11:20:43 CST" = mtime 11:20:43.98 CST ✓. Mode 644 is NL convention: nit only. |
| /workspace/nl-e8-delta-1110/e8delta.py | 13bcf9038f6be227536e3b2209a2958259d2819df6599c6e6a721e8431db25e8 | yes | 444 | mtime 11:15:31.314; sidecar 11:15:31.318 |
| /workspace/nl-e8-delta-1110/e8delta_run.log | e9a8cfe94a21e2e7d02a87a3e8aa89cb478db707bedb50c2d1918e95426979da | yes | 444 | mtime 11:15:32.18; sidecar 11:15:36 |
| PP fe0c3d92 (FINDINGS_PP_AUDIT_NL_1800_E8_STRESS_BOLZA_AND_ERRATA10_11_2026-11-09_1807.md) | fe0c3d92fdfac839653f9358f0a2c193c91a9e9dd42d46bbcbc6d58e1b794ae3 | yes | — | Y0, Y3-ineq, Y5, Y6-math/phys, Y11 |
| PP bf4773a8 (FINDINGS_PP_AUDIT_NL_1750_ODD_HW_E8_AND_ERRATUM9_2026-11-09_1757.md) | bf4773a80192a5d34905237c5a3942aa2c601af6f3189c479d9d6f80e1b63d73 | yes | — | E1-p₁, E2, E2-end, L3-sources |
| PP 149be02a (FINDINGS_PP_AUDIT_NL_Y16_TRR2_WALL_STRESS_AND_ERRATUM12_2026-11-09_1826.md) | 149be02a794917d92f36c7a2383bbb4eb74623bb4f7b57dd111ad09f73ba7293 | yes | — | Q5, Q7, Q11a/b, Q12a, PP-1 |
| PP f3c5d73f (FINDINGS_PP_AUDIT_NL_FACE_SOURCES_NONCONSTANT_LOCALIZED_M5_2026-11-09_1730.md) | f3c5d73f371b31a75a87021452251af77b9d2d37e7fb6b955f647ed84192d523 | yes | — | F1 T0 [PROVED given J1]; interior w_fib numerics |
| PP 5cbd050a (FINDINGS_PP_AUDIT_NL_JUNCTION_AND_XI_FRICKE_2026-11-09_1702.md) | 5cbd050abc2fe085f715d548fffb58b202d7c685a54070c288972b5150cb0fcb | yes | — | **J1 source: J1 is CONDITIONAL (CLP/BBBW)** |
| PP 077e417d (FINDINGS_PP_AUDIT_NL_Y14_STAGE2_Y15_FIBRE_ISRAEL_2026-11-09_1953.md) | 077e417db7f24ece269d7dcde21bc89e260bbe1102d985c63ab60aa94813c23b | yes | — | Y15-1, I1, I2, Y15-trace, Y15-IR, S11/S12′ |
| NL 1711 (NL_DERIVED_FACE_SOURCE_TEMPLATES_FIBRE_SIGMA_G4LEGS_2026-11-09_1711.md) | 53096d433d062f51e0fc078d4bdd5faee333cbcf7edadd66c2a0b3fd4d2e7fb7 | yes | — | T0, E1, E4, AB1, AB2, G2-odd, G3 |
| NL 1800 (NL_DERIVED_E8_INSTANTON_STRESS_ODD_HW_WALL_BOLZA_2026-11-09_1800.md) | 859328a2003242ca59109ffb699ba69995f4d5c9dec0055e49d16adc4e2d379d | yes | — | Y8 normalization |
| NL Y16 (NL_DERIVED_Y16_HW_TRR2_WALL_STRESS_NEC_2026-11-09_1813.md) | 7270a6b35c97822a4efe37b7f6e78d94efafd0ae44d298ba70554e926c9d5237 | yes | — | Q5 wording |
| NL 1713 (NL_DERIVED_JUNCTION_NONCONSTANT_FACE_LOCALIZED_M5_2026-11-09_1713.md) | e2065e05c7d552117895351482cbb3838fcd651bb8873cd6398d0e35b12fd389 | yes | — | context only |
| Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | — | 644 | mtime 2026-11-06 14:38:54 CST; see custody (§8) |

**Integrity finding I-1 (priority).** NL states "26/26 PASS" (filing header and relayed message). The frozen log has **23** `[PASS]` lines and 0 `[FAIL]` (C1a–g 7, C2a–f 6, C3 1, C4a–g 7, C5 1, C6 1 = 23), plus the summary line "ALL PASS". The run is clean; the count is misstated. (PP P10c.)

**Method claim, verified by reading e8delta.py.** No `simplify()==0`, no `allclose`, no numpy. Zero tests are `sp.expand(e)==0` on exact-coefficient polynomials (C1, C2, C3, C4b, C5) and exact `Fraction`/int comparisons (C4d–C4g, C6). **Exception (nit):** C4a tests `sp.nsimplify(8π²/(λ²T_M5)) == 2 / == 1`. That is neither expand==0 nor a Rational comparison; here it is exact anyway (sympy evaluates the expression to the integer before `nsimplify` acts; PP P7b reproduces it with `cancel`). `float()` appears only in printed labels. The one-generator reduction is stated in a comment; PP P3f checks it exactly for two orthonormal generators (the stress is the sum of per-generator stresses), so it is justified for any positive-definite tr.

## 2. Evidence (PP)
Directory /workspace/quantum-comp/reports/evidence_pp_audit_nl_e8_delta_79ad0c64_2026-11-10/ (every file 444, each with a `.sha256` sidecar that verifies with `sha256sum -c`):
| file | sha256 | content |
|---|---|---|
| e8delta_copy.py | 13bcf9038f6be227536e3b2209a2958259d2819df6599c6e6a721e8431db25e8 | byte-identical copy of NL's frozen script (`cmp` clean) |
| e8delta_rerun.log | e9a8cfe94a21e2e7d02a87a3e8aa89cb478db707bedb50c2d1918e95426979da | PP re-run, exit 0, **byte-identical** to NL's e8delta_run.log (`cmp` clean; no cosmetic differences) |
| pp_exact_checks.py | 0c4d3f5b6df867933cd587c7d675c9f52fee81d5119e71332f437e04e064fa4a | PP's independent exact checks P1–P10 (sympy 1.14.0; zero tests via `Poly(...).is_zero`, `cancel`, exact Rational/Fraction) |
| pp_exact_checks.log | 8eab5efc11247a081814f9471e68c98ddcde041b41277ab08ca4be8a9c6b66f6 | 51/51 PASS, exit 0, deterministic (a second run is byte-identical) |

Disclosure: PP's first draft of P3b had an index-contraction bug in PP's own check (it contracted the covector F(k,·) with k through η). It was corrected to v_b k^b before sealing; the sealed log is the final run. This does not touch NL's script.

What the PP checks establish (independent implementations, not re-runs of NL code):
- **P1 (GA1/Y0):** in 10 wall dimensions, K = κ²S/18, K_ab = −(κ²/2)(S_ab − h_abS/9), and S(k,k) = −(2/κ²)K(k,k) for k = t̂ + ê_j, every j (general diagonal K, exact).
- **P2 (T0 end values, J1 as premise):** IR K = 4k_x gives w_fib = w_Σ = −4/3; UV K = 6k_x gives w_fib = −6/5, w_Σ = −1; at both ends **S(t̂+ê_fib, t̂+ê_fib) = (2/κ²)k_x** and S(k,k)·ρ_req = −c·k_x²/κ⁴ with c = 12 (IR), 20 (UV). So sign S(k,k) = −sign ρ_req at the end faces.
- **P3 (C1a–g, C3, YM S(k,k) ≥ 0 including electric legs):** for a general 45-component field and arbitrary k, S(k,k) = ⟨F(k,·),F(k,·)⟩_η − ¼η(k,k)F² exactly, and F(k,k) = 0; for null k = (1,n), |n| = 1, ⟨v,v⟩_η = |n|²|v_s|² − (n·v_s)² ≥ 0 by the Lagrange identity (checked exactly). So **S^YM(k,k) ≥ 0 for every null k, not only k = t̂ + ê_j**. C3's coordinate form and C1a–g are reproduced exactly. Two-generator additivity (P3f).
- **P4 (C2a–f, Bogomolny):** with ⋆ built from ε (not a hard-coded table), ⋆² = 1; ρ − q/2 = ⅛Σ_ordered(F−⋆F)² = ½Σ_{3 pairs}(F−⋆F)²; SD ⇒ fibre block 0, mixed 0, worldvolume −ρh, ρ = q/2; general fibre field ⇒ fibre block traceless; Israel response K^wv = κ²ρ/6, K^fib = −κ²ρ/3, ratio −2 (S1/Y5).
- **P5 (GA7a algebra):** for the SD 3-parameter family, the map F ↦ v∧F has M(v)ᵀM(v) = |v|²𝟙₃, so v ≠ 0 and v∧F = 0 force F = 0.
- **P6:** a positive-tension brane with any worldvolume containing t has S(t̂+ê_j, t̂+ê_j) = T·[ê_j ∉ worldvolume] ≥ 0, whatever its charge.
- **P7 (C4a, PP-1, normalization):** HW-printed λ² = 2π(4πκ²)^{2/3} = (2π)⁷ (convention 2κ² = (2π)⁸ℓ_P⁹, T_M5 = (2π)⁻⁵ℓ_P⁻⁶); u := 8π²/(λ²T_M5) gives 2 (HW) and 1 (λ² = 2(2π)⁷); λ² = 2(2π)⁷ gives λ⁶/κ⁴ = (4π)⁵ exactly; convention-free, (4π)⁵ / (HW 128π⁵) = 8, so the λ² ratio is 2. **And:** the BPS energy is (1/2λ²)∫tr F∧F (P4e), so the energy per unit charge is 8π²/λ² **iff** the unit charge is ∫tr F∧F = 16π² (GA3's I₄ = (tr F∧F − ½tr R∧R)/16π²). With §2's n_inst = (1/8π²)∫tr F∧F it would be 4π²/λ² = u/2 (P7f). See finding N-1.
- **P8 (C4b, C4c, C4e):** C4b/C4c exact. 10N/3 at N = 4880 is 48800/3, and 16266.7 is its one-decimal print (P8c); 16266.7/9760 ≠ 5/3 (P8e). C4e encodes UV as `Fr(10*Nf,3)`, so "5/3 exactly" is true **by construction**: it is exact only as the arithmetic of the on-record formula N_req^UV = 10N/3 (1711 AB2, itself given J1). The other four N_req are exact rationals of one-decimal prints (P8f).
- **P9 (D-A side sentence):** Y16 Q5's fibre-integrated tr R² energy −8π²/λ² plus one I₄-unit of BPS energy +8π²/λ² sums to 0 exactly.
- **P10:** §7 counts equal list lengths (22/16/5/2), 45 distinct items, no double count; the NL log has 23 checks.

## 3. Priority items (NL's audit-first list)

### 3.1 D-D: filed REFUTED given J1
- **J1 source and status.** J1 = constant-r faces of the CLP/BBBW BPS flows, **CONDITIONAL** (PP 5cbd050a). The end values are T0 / F1 **[PROVED given J1]** (NL 1711 T0; PP f3c5d73f F1). PP P2 reproduces w_fib = −6/5 (UV) and −4/3 (IR), and w_Σ = −1, −4/3, exactly.
- **Sign chain, checked.** GA1 (P1): S(k,k) = −(2/κ²)K(k,k). For a static Poincaré-invariant face, K(k,k) = K(ê_fib,ê_fib) − k_t, so at the end faces (k_fib = 0, k_t = k_x) S(k,k) = (2/κ²)k_x (P2). The required ρ_req = (2/κ²)(k_x − K) = −(6/κ²)k_x (IR), −(10/κ²)k_x (UV). In the IR-kept pairing (1711 §0 P3: k_x < 0, ρ_req > 0) this gives S(k,k) < 0, i.e. w_fib < −1: C6's comparison is the correct reading **only together with ρ_req > 0**, which C6 itself does not test (P2 does). Sources: S^YM(k,k) ≥ 0 for every field and every null k (C3; PP P3), and S^brane(k,k) ≥ 0 for every positive-tension brane of any charge (P6). Their sum cannot equal a stress with S(k,k) < 0, so the makeup equation has no solution on those faces.
- **Audit-support remark (short, elementary; scope only; it does not raise any grade).** By P2, sign S(k,k) = −sign ρ_req at both end faces. So in the UV-kept pairing the same source set fails through ρ_req < 0 instead (all admitted sources have ρ ≥ 0). The no-makeup conclusion at the end faces therefore does not depend on which side is kept, but it does depend on J1 and on k_x ≠ 0.
- **Ruling: D-D REFUTED given J1 stands, as an implication-grade.** Precisely: *J1 ⇒ the claim "localized E₈ YM stress (BPS or not) plus positive-tension branes of any charge equals the required wall stress" is false on the constant, unbackreacted end faces.* It is **not** a refutation of the geometry, of J1, or of the E₈ wall sector (which stays CONDITIONAL, gated by backreaction, O5).
- **Scope corrections (priority).**
  - (a) The tally entry must carry "given J1, constant unbackreacted end faces" (as GA8 does).
  - (b) Source set: the claim covers {E₈ YM, positive-tension branes}. V's sentence "D-D holds without dropping tr R²" is right **only at leading order in 1/N** (Y16 Q7/Q11a, PROVED given J1). At N = 4880 it is CONDITIONAL (Q11b). The C∧X₈ δ-stress (S4) and the other same-order terms (Y16 Q14) are OPEN.
  - (c) Interior faces: GA8-int CONDITIONAL is the correct scope. Interior pointwise w_fib ∈ [−1.342, −1.169] (BBBW) is float numerics (PP f3c5d73f; 1711 E2), so it stays CONDITIONAL. Backreacted faces: OPEN (O5).

### 3.2 GA12 / GA13 (and C4a, GA14)
- **GA12.** The argument has three premises:
  - **(C)** the energy is continuous in the size → 0 limit;
  - **(I)** a zero-size SD instanton at y₀ is one M5 at y₀ with energy W(y₀)T_M5 per unit charge, i.e. the small-instanton identification (Y7, Ganor–Hanany/Seiberg–Witten, CONDITIONAL);
  - **(N)** the unit charge is ∫tr F∧F = 16π², which is the normalization u's definition needs (P7e).
  Under C ∧ I ∧ N the BPS energy per charge is the size-independent u·W(y₀)T_M5, so u = 1. **Ruling: PROVED as an implication of C ∧ I ∧ N only.** The row names C but not I or N. Its "PROVED" in §7 is fair only with all three named; it is **not** an unconditional PROVED of u = 1. PP-1 (149be02a) already said u = 1 "is what the small-instanton ↔ one-M5 tension match requires", with the instanton-energy normalization not re-checked. GA12 restates that remark.
- **GA13.** The contradiction is u = 2 ∧ C ∧ I (∧ N) ⇒ ⊥: there is a jump of (u − 1)W(y₀)T_M5 per unit charge. **Ruling: REFUTED stands only for that conjunction.** The HW-printed λ² (u = 2) **alone is not refuted**. A refutation of the printed normalization would need a proof that C and I hold, and neither is proved. In addition, "HW-printed ⇔ u = 2" itself holds only under N (finding N-1). The tally entry must read "GA13 REFUTED (conjunction u = 2 ∧ C ∧ I); not a refutation of HW's printed λ²". D-B2's "GA13 refutes u = 2 with continuity" is correctly worded; V must not shorten it.
- **C4a [algebra PROVED].** From the two λ² values: u = 8π²(2π)⁵/(2π)⁷ = 2 and u = 8π²(2π)⁵/(2·(2π)⁷) = 1, exactly (P7b). The cited λ⁶/κ⁴ = (4π)⁵ is consistent with λ² = 2(2π)⁷ under 2κ² = (2π)⁸ℓ_P⁹ (P7c), and the factor-8 ↔ factor-2 relation is convention-free (P7d). The normalizations were not re-derived as physics.
- **GA14 stays CONDITIONAL** on the Conrad/Lü anomaly derivation, which is not re-checked, and on N.

### 3.3 D-A / GA4 (p₁(TS⁴) = 0 ⇒ n_R = 0)
- Prior result: 1750 E1-p₁ **[PROVED]** (PP bf4773a8), re-confirmed as Y16 Q12a **[PROVED]** (PP 149be02a). The argument is that TW|_{S⁴} = TS⁴ ⊕ (trivial normal bundle of a fibre), and TS⁴ ⊕ ℝ = Tℝ⁵|_{S⁴}. Pontryagin classes are stable, so p₁(TW|_{S⁴}) = 0. ∫_{S⁴} tr R∧R is the Chern–Weil number of the restricted bundle for **any** connection on it, so it is 0 for the restricted 10D/11D Levi-Civita connection, warped or squashed.
- **Ruling: D-A and the GA4 p₁ step are PROVED.** Scope wording: "for every smooth connection on TM|_{S⁴}", which is stronger and more accurate than "for every metric" on S⁴. It assumes a smooth closed fibre. With backreacted, localized M5 points on the fibre (O5) the restricted metric can be singular, and the statement would need re-proof there. The rest of GA4 ("N_M5 + n_inst = 2N_flux") is the HW Bianchi identity, which stays CONDITIONAL (R5). The row already says "(p₁ step)".
- **n_R prefactor.** Its ratio to n_inst (−½) matches I₄'s (tr F∧F − ½tr R∧R). Its absolute prefactor (1/8π²) does not match GA3's 1/16π²; see N-1. This is harmless for D-A because the integral is 0.
- **The extra sentence is not licensed by the p₁ step.** "Instanton energy (≥ 0) does not cancel the UV tr R² wall energy (Y16 Q5)" is not argued: a sign alone cannot show that a nonnegative quantity fails to cancel a negative one. As an integrated-energy statement it is false on the record's own numbers. Y16 Q5 gives −8π²/λ² per fibre, which is PROVED in λ units, and one I₄-unit of BPS charge carries +8π²/λ², so they sum to 0 exactly (P9). (Whether a static unit-charge BPS configuration exists on the warped face is a separate question; cf. GA7a.) The sentence is not a tallied row, so there is **no tally effect**. Fix: strike it, or state the exact sense (pointwise profile, fibre-NEC supply per direction, or existence) and argue it.

### 3.4 §1 geometry → algebra rows, especially GA8 and GA7a
- **GA8 [PROVED given J1: stands, with premises named].** C1f and C3 (P3) give S^YM(k,k) ≥ 0 for every field and every null k, electric legs included. P6 covers branes. C6's fractions are exact (−6/5, −4/3 < −1, P2). The step "w_fib < −1 ⇔ S(k,k) < 0" needs ρ_req > 0, i.e. the **IR-kept** pairing (1711 §0, analytic at the ends: 3|k_x|, 5|k_x|). The row must name J1 **and** the IR-kept pairing. C6 alone is a comparison of two J1 inputs with −1, not a test of the geometric demand; P1 and P2 supply the chain.
- **GA7a [PROVED for the stated equation: stands, scoped as in PP fe0c3d92 Y6-math].** PP fe0c3d92 ruled Y6-math **PROVED for the stated equation**. That stated equation is the 10D wall action restricted to fields on the fibre (legs **and** dependence), giving D(W⋆₄F) = 0 with W = c_x²c_Σ = Δ̃e^{4f+2g}, on a **constant** face (dW = dΔ̃). W is not a conformal factor of g₄, and the critical set of Δ̃|_{S⁴} has empty interior, so a smooth static SD field vanishes identically and BPS instantons appear only at zero size. PP P5 re-checks the algebraic core: v∧F = 0 with v ≠ 0 forces SD F = 0. The row's "static finite-size SD fields vanish" uses fe0c3d92's empty-interior strengthening, which is proved for constant faces only, so the row must say "constant face, fibre-only fields". "M5-like" is right only in the point-support sense; identifying them as M5s is Y7/I (CONDITIONAL). GA7b = Y6-phys, CONDITIONAL ✓.
- The other GA rows are in §4.

### 3.5 D-B1, V, and the scope of the lead "No"
- **D-B1 [CONDITIONAL on u = 1: stands].** C4b/C4c are exact (P8a,b). Further premises: the HW charge equation (R5, CONDITIONAL), BPS energy u per charge (S1 and N-1), and x-tension = energy density for static Y₆ fields (C1a). With these, BPS trades leave T unchanged.
- **D-B2 [CONDITIONAL: stands, wording fix].** Its inequality is exact (u ≥ 1 + Δ_N/(2N) from n_inst ≤ 2N_flux, for u > 1 and Δ_N > 0). "Survives only if both fail" is too strong as a necessity claim: ¬GA7b is necessary only under I (zero-size instantons count as M5s with energy 1 per charge). Without I, u ≠ 1 with C failing is enough to keep the branch even when GA7b holds. The numeric n_inst targets (2808.6 … 6506.7) are CONDITIONAL, unadopted prints.
- **D-B3 OPEN ✓. D-C CONDITIONAL ✓** (u = 1, GA2, BPS/SD fibre-supported fields). **D-E CONDITIONAL ✓**: a charge identity, not a stress statement.
- **C4d–C4g** (12568.6, 1.2878, …) are CONDITIONAL, unadopted test targets and support no PROVED grade. Nothing in the filing uses them for one ✓. **C4e "5/3 exactly":** exact only as arithmetic of the on-record formula N_req^UV = 10N/3 (given J1). C4e builds it in by construction, and 16266.7 is the print of 48800/3 (P8c–e).
- **V [CONDITIONAL: stands; the headline must be scoped (priority)].** The bold "**No.**" reads as an unconditional closing, and it is not one. The ruled content, sense by sense:
  - **D-A:** there is nothing to make up (PROVED).
  - **D-B:** BPS makeup is none if u = 1 (CONDITIONAL). With u ≠ 1 it needs ¬C (and ¬GA7b under I) (CONDITIONAL). Exact non-BPS makeup with profile is **OPEN** (D-B3). So **V does not establish "No" in the integrated tension–charge sense.**
  - **D-C:** CONDITIONAL; BPS/SD fibre fields only.
  - **D-D:** REFUTED given J1 on constant unbackreacted end faces, for the source set {E₈ YM, positive-tension branes}. With tr R² included this holds at leading order in 1/N only; at N = 4880 CONDITIONAL (Q11b); C∧X₈ OPEN (S4).
  - **D-E:** yes, but as a charge identity.
  - Backreacted faces: **OPEN** (O5).
  Suggested headline: "No in senses D-A (PROVED) and D-D (given J1, constant unbackreacted end faces); CONDITIONAL in D-B1/D-C; not established in D-B3 or on backreacted faces."

### 3.6 R9: reopening 1711 AB2 and G2-odd
- **What 1711 actually says.** AB1 [PROVED given J1] solves the x-equation with a smeared M5 stack, N_b T_M5ρ(y) = (2/κ²)(k_x − K), and puts all non-x blocks on the template sources (a)+(b), which carry zero x-tension. AB2 [CONDITIONAL] gives b = N_req(x)⁻¹(N_b) and "N_b = 4880 has none". **AB2 also states the general relation N_bT_M5 = (2/κ²)∫(k_x − K) − ∫σ_x^ex for extra x-tension, with b fixed only once the source's equation of state is given.** G2-odd [CONDITIONAL on O1 = odd] gives N_b = 2N_flux from the (α)-leg jump and the charge-vs-tension ratio N_req/(2N_flux) ∈ [1.255, 1.667]. G3 [PROVED given G0] concludes "N_req⁻¹-type in the odd case (AB2 with N_b = 2N_flux): no solution, since the ratio is > 1".
- **Ruling on fairness.**
  - For **G2-odd/G3**, the reopening is **fair in substance**: "no solution" identifies all of the face charge 2N_flux with tension-equals-charge M5s and allows no other x-tension, which is the now-dead premise.
  - For **AB2**, it is **partly unfair**. AB2's general σ_x^ex relation does not rely on that identification. Only its pure-M5 special case ("N_b = 4880 has none") does.
  - **The old "no solution" is an implication of the dead premise** (pure M5 stack, tension = charge, no other x-tension), and it stays on record as that. The premise is dead as the working assumption, not refuted by fiat, so **AB2, G2-odd and G3 keep their filed grades as implications of their premises.** Recording them as "OPEN, reopened" would be a regrade by fiat of prior rows and is not accepted.
- **R9 as a new item [OPEN: accepted].** "b for a given split" with b = N_req⁻¹(2N_flux + (u − 1)n_inst + ε_ex) matches AB2's σ_x^ex form, with σ_x^ex = the instanton x-tension (C1a: x-tension = energy density). Scope: this reading uses the **x-equation only**. The fibre and Σ blocks still need non-E₈, NEC-violating content at the end faces (D-D/GA9), as in AB1's (a)+(b) premise. Count: R9 stays OPEN (1), recast as a new item rather than a reopening.

## 4. Row-by-row verdicts (NL grade → PP grade; basis)
| row | NL | PP | basis / required scope |
|---|---|---|---|
| GA1 | PROVED | PROVED | P1; = Y0 (fe0c3d92) |
| GA2 | COND | COND | P-b, HW boundary condition |
| GA3 | COND | COND | HW 9603142, not re-derived. Nit: "rank 248" → dimension 248 |
| GA4 | PROVED (p₁) | PROVED (p₁ step) | §3.3: smooth connections on TM\|_{S⁴}; charge equation part stays COND (R5) |
| GA5 | PROVED | PROVED | C1a–e = P3e (static magnetic fields, legs on Y₆) |
| GA6 | PROVED | PROVED | C2a–e = P4a–e |
| GA7a | PROVED (stated eq.) | PROVED (stated eq.) | §3.4: constant face, fibre-only legs and dependence; "M5-like" = point support only |
| GA7b | COND | COND | = Y6-phys |
| GA8 | PROVED given J1 | PROVED given J1 | §3.4: name J1 **and** the IR-kept pairing (ρ_req > 0) |
| GA8-int | COND | COND | float numerics (f3c5d73f, 1711 E2) |
| GA9 | OPEN | OPEN | — |
| GA10 | PROVED | PROVED | C1g = P3e; premise: no x-legs (built into C1; cf. 077e417d I1) |
| GA11 | PROVED | PROVED (implication) | C5 is a tautology. The [G_tan] doubling needs GA2/P-b (COND); name P-b |
| GA12 | PROVED (impl.) | PROVED (implication of C ∧ I ∧ N) | §3.2; not an unconditional PROVED of u = 1 |
| GA13 | REFUTED | REFUTED (conjunction u = 2 ∧ C ∧ I) | §3.2; HW-printed λ² alone not refuted |
| GA14 | COND | COND | PP-1; anomaly derivation not re-checked; and N |
| S1 | PROVED | PROVED | C2a–d = P4d,e,g. The M5-unit sentence depends on N (N-1) |
| S2 | PROVED | PROVED | C1, C2e,f = P3e, P4b,f. Nit: say which sum in ½Σ(F−⋆F)² (3 pairs) |
| S3 | PROVED | PROVED | metric-independent CS term ⇒ no stress. The "Z₂-invariant under P-b" clause is COND (P-b) |
| S4 | OPEN | OPEN | — |
| S5 | COND | COND | 1711 G1; HW δ(0) treatment |
| S6 | COND | COND | — |
| D-A | PROVED | PROVED | §3.3. The extra sentence on tr R² energy is unsupported and false as an integrated statement (P9); strike or restate |
| D-B1 | COND (u = 1) | COND | §3.5 |
| D-B2 | COND | COND | §3.5: "only if both fail" needs I for the ¬GA7b part |
| D-B3 | OPEN | OPEN | — |
| D-C | COND | COND | u = 1, GA2; BPS/SD fibre fields |
| D-D | REFUTED given J1 | REFUTED given J1 (implication) | §3.1: constant unbackreacted end faces; source set {E₈ YM, positive-tension branes}; tr R² leading order only |
| D-E | COND | COND | charge identity, not stress |
| V | COND | COND | §3.5: the headline "No" must be scoped sense by sense |
| R1 | PROVED | PROVED | Y0 (fe0c3d92) |
| R2 | PROVED | PROVED | Y1-stress (fe0c3d92) |
| R3 | PROVED | PROVED (bookkeeping) | its members include Y4-end and E2-end, which are PROVED **given J1**; label them |
| R4 | PROVED | PROVED | Y5/E3 |
| R5 | COND | COND | HW Bianchi; p₁ step PROVED |
| R6 | PROVED | PROVED | Y9 |
| R7 | PROVED | PROVED | Y11 + pointwise C2e (P4b). Y11's "8π²\|k\|" is in Y8's normalization (N-1) |
| R8 | COND | COND | wording: "holds iff u = 1 … or via GA7b + GA12" is self-contradictory. Write "holds if u = 1, or under GA7b with I" |
| R9 | OPEN (reopened) | OPEN (new item; not a reopening) | §3.6: AB2/G2-odd/G3 keep their filed grades as implications of the dead premise |
| R10 | PROVED | PROVED | definition (source-free N_req); its numerics COND |
| R11 | PROVED | PROVED (bookkeeping) | matches 077e417d. Name I1's no-x-legs premise; Y15-IR's REFUTED is scoped to the IR-kept side, σ ≥ 0 |
| R12 | PROVED given J1 | PROVED given J1 | Y16 Q7/Q11a (149be02a) |
| R13 | COND | COND | S11-count/S12′ (077e417d) |
| R14 | COND | COND | L3-sources (bf4773a8) |
| O5 | OPEN | OPEN | — |

## 5. Additional findings
- **N-1 (normalization, priority).** The filing's charge normalization is internally inconsistent by a factor 2:
  - GA3 writes I₄ = (tr F∧F − ½tr R∧R)/16π².
  - §2 writes n_inst = (1/8π²)∫tr F∧F and n_R = −½(1/8π²)∫tr R∧R.
  - u = 8π²/(λ²T_M5) is the BPS energy per unit charge only if the unit is ∫tr F∧F = 16π² (P7e). Under §2's normalization it would be u/2 (P7f): HW-printed ⇒ 1 and Conrad/Lü ⇒ ½.
  - The inconsistency is inherited from NL 1800 Y8 ("/16π², tr normalized so that one minimal instanton gives 1", next to n_inst = (1/8π²)∫tr F∧F). PP-1 (149be02a) left the instanton-energy normalization unchecked.
  - Effect: there is no effect on the form statements (blocks, signs, traces, Bogomolny, NEC, D-A, D-D). The **u-value identifications** in GA12–GA14, C4a's physical reading, S1's M5-unit sentence, D-B1/D-B2, and the R9 restatement all carry N.
  - No grade moves, because those rows are already CONDITIONAL or implications. NL should fix one normalization in an additive erratum.
- **N-2 (nit).** C5 and C4g are tautologies, and C6 compares inputs. They are fine as bookkeeping but are not evidence for the geometric chain, which P1/P2 supply.
- **N-3 (nit).** C4a uses `nsimplify` (§1).

## 6. Tally effect
- **Ruled tally: PROVED 22 · CONDITIONAL 16 · OPEN 5 · REFUTED 2 = 45. NL's counts stand.** No row changes label class.
- Mandatory scope relabels in the tally line, each an implication-grade:
  - GA8 and D-D "given J1, constant unbackreacted end faces"; GA8 also "IR-kept pairing";
  - GA11 "given P-b";
  - GA12 "implication of C ∧ I ∧ N";
  - GA13 "REFUTED: conjunction u = 2 ∧ C ∧ I, not HW's printed λ²";
  - R3 "members Y4-end and E2-end given J1";
  - R9 "new OPEN item, not a reopening of AB2/G2-odd".
- **Other standing tallies: unchanged by this file.** In particular, the 1711 tally (11/10/4/0), the 1800 tally as revised (13/11/3/2), the Y16 and 077e417d tallies, and PP rollups are not rewritten. AB2, G2-odd and G3 keep their filed grades as implications of the pure-M5 premise. N-1 is flagged against NL 1800 Y8 for NL's additive erratum, with no regrade here.

## 7. Fixes for an additive NL erratum (do not edit 79ad0c64, e8delta.py or e8delta_run.log)
**Priority (NL should act):**
1. Integrity count: "26/26 PASS" → **23/23 PASS** (filing header and any messages that repeat it).
2. N-1: fix one charge normalization. Either n_inst = (1/16π²)∫tr F∧F and n_R = −(1/32π²)∫tr R∧R to match GA3 and u = 8π²/(λ²T_M5), or redefine u. Then restate GA12–GA14, C4a's reading, S1's M5-unit sentence, D-B1/D-B2 and R9 in that normalization.
3. GA12/GA13: name premises C, I and N. GA13 must read "REFUTED (conjunction u = 2 ∧ C ∧ I); HW's printed λ² alone is not refuted". The tally line follows.
4. D-D / GA8: tally entries carry "given J1 (CONDITIONAL, CLP/BBBW), constant unbackreacted end faces". GA8 also needs "IR-kept pairing (ρ_req > 0)". Source set {E₈ YM, positive-tension branes}. V's "holds without dropping tr R²" → "at leading order in 1/N (Q11a); at N = 4880 CONDITIONAL (Q11b); C∧X₈ OPEN (S4)".
5. V: replace the bold unconditional "No." with the sense-by-sense headline of §3.5. In particular, "No" is **not established** in sense D-B3 or on backreacted faces (O5).
6. D-A: strike or restate the sentence "instanton energy (≥ 0) does not cancel it [the tr R² wall energy]"; as an integrated statement it is false (P9).
7. R9: recast as a new OPEN item ("b for a given split", x-equation only). State that 1711 AB2/G2-odd/G3 keep their filed grades as implications of the pure-M5 (tension = charge, no other x-tension) premise. Note that AB2 already contained the σ_x^ex generalization, so "their conclusions equate tension units with charge 2N_flux" is accurate for G2-odd/G3 and for AB2's special case only.

**Non-priority (nits):**
8. GA4: "for every metric" → "for every smooth connection on TM|_{S⁴} (closed smooth fibre)"; backreacted localized M5 points fall under O5.
9. GA7a: add "constant face; fibre-only legs and dependence (fe0c3d92 Y6-math)"; "M5-like" = point support (identification = Y7/I, CONDITIONAL).
10. GA11: name P-b for the flux doubling.
11. D-B2: "only if both fail" → "requires u ≠ 1 and ¬C; ¬GA7b is additionally required under I".
12. R8 wording (§4). R3: mark Y4-end and E2-end "given J1". R11: name I1's no-x-legs premise.
13. C4e: say "5/3 exactly as the arithmetic of N_req^UV = 10N/3 (given J1); 16266.7 is its print"; C4e is by construction. C4a: note `nsimplify`. C5, C4g and C6 are bookkeeping comparisons, not tests of the geometric chain.
14. GA3 "rank 248" → "dimension 248". S2/D-B3: specify the sum in ½Σ(F − ⋆F)² (3 pairs, = ¼ over all 6 a<b).
15. Mode 644 on the filing and sidecar (NL convention): optional.

## 8. Custody
- Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, mtime 2026-11-06 14:38:54 CST, **before** (11:26 CST) = **after** (re-hashed after this write; see report-back). Never opened for writing.
- NL filing, sidecar, e8delta.py, e8delta_run.log and their sidecars: read and hashed only, untouched; the shas are unchanged at the end of the audit.
- Running Local jobs (s1e, chain_v2, s2e, wait_then_ob_v5) and other agents' directories and frozen scripts: untouched.
- New files are only this findings file, its sidecar, and the PP evidence directory (§2).

Nothing adopted. Tip 7cddb188 untouched. Junction UNSOLVED. No CERT. Resonant algebra.
