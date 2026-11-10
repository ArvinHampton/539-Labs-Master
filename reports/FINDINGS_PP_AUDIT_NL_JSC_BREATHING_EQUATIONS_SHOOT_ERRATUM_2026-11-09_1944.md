# FINDINGS — PP audit of NL JS-C breathing-mode files: equations (1935), toy shoot (1936), L4-numbering erratum (1936) — 2026-11-09 19:44 CST (America/Chicago)
Auditor: Professor Proof (PP). Pure math. Labels: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. Under OW 90cec14c (t4415, "S4 breathing mode. Pursue it." — a GO, not an adoption; file sha 90cec14c… = sidecar). **Nothing is adopted. Junction: UNSOLVED.** No CERT, no sends, no Gemini. Tip 7cddb188 read-only (untouched). Lock 96f8d42e §4 stays purged. Additive new file. Nomenclature per OW 81b74a31: "resonant algebra" (not used in this file).

## 0. Integrity
- NL_DERIVED_JSC_BREATHING_MODE_EQUATIONS_MN2_2026-11-09_1935.md ebdda4b6147bef3d5efd5be7256eb6093b8c95b37ab3aa2fe83af1715fbbdd88 = sidecar.
- NL_DERIVED_JSC_BREATHING_MODE_SHOOT_MN2_2026-11-09_1936.md 358c4b09ea75cd1d0ac91a130c37cd18eed55e5c1864a3ce5dc03bae107cdcba = sidecar.
- NL_ERRATUM_L4_NUMBERING_JUNCTION_SOURCES_1859_2026-11-09_1936.md c1074ec55046e8c2cf2ea3e24fc177e0f3e6c72df7998248349600df2716f20f = sidecar.
- /workspace/nl-jsc-1905/: all 10 .py/.log sidecars MATCH. Note: mn2_breathing_consistency.log and _v2.log are **empty** (sha e3b0c442…, the empty-file hash) — superseded runs; nothing in the files rests on them (fix J1).
- Reruns by PP: singlet_toy_shoot.py and mn2_breathing_linearity_v3.py → byte-identical logs. consistency_v3 not rerun (its values are reproduced exactly by PP's closed form below).
- PP scripts (/workspace/pp-audit-jsc/, MANIFEST.sha256): pp_Rrchi_closed.py 62f0ac90… / .log d1069926…; pp_singlet_checks.py fdf7e06b… / .log 6c01804a…; pp_stable_manifold.py 7424f26e… / .log 567ca919….

## 1. Equations file (1935) — priority E3 / E4
- **E4 — PROVED in closed form (upgrade from CONDITIONAL).** PP recomputed R_{rχ} fully symbolically (exact sympy, 11D metric identical to NL's v3 ansatz, with f(r), g(r), β(r) arbitrary functions, γ symbolic, X_a, X_b symbolic positive):
  **R_{rχ} = 3(X_a − X_b) sin 2χ · β′ / [(X_a+X_b) + (X_b−X_a) cos 2χ] = (3/2) β′ ∂_χ ln D̃**, D̃ = X_b cos²χ + X_a sin²χ.
  Difference from (3/2)β′∂_χ ln D̃ simplifies to 0 identically. It is independent of γ, f, g and β″, as NL found numerically. NL's wording slip in E4's last sentence is moot: the closed-form proof now exists (PP).
- **E3 — REFUTED claim upheld; the counterexample is genuine.** At X_a = 2^{−3/5}, X_b = 2^{2/5} (MN2), β′ = 1/2, χ = 7/10, the closed form gives R_{rχ} = −0.46630596733261109281 (20 digits; matches NL's −0.4663059673 at 40-digit mpmath). The metric there is a genuine Lorentzian metric (D̃ > 0, all warp factors positive; the point is interior, χ ∈ (0, π/2)). With NL's G₄ (r-independent, no r- or x-legs), T_{rχ} ∝ G_{rPQR}G_χ^{PQR} = 0 and g_{rχ} = 0, so the trace-reversed Einstein equation demands R_{rχ} = 0. Contradiction ⇒ the uniform-breathing ansatz is inconsistent for every γ whenever β′ ≠ 0 and X_a ≠ X_b. In fact E4 gives the stronger statement: **the ansatz forces β′ ≡ 0** on MN2 (sin 2χ ≠ 0 on an open set).
  - Scope (fix J2): NL's ansatz puts e^{2f} on dr² as well as on dx² (a lapse tied to f). R_{rχ} is f-independent, so this does not affect E3/E4, but the file should state the gauge. The refutation covers only that G₄ class; G₄ with dr∧dχ legs or χ-dependent β (E5) is not covered.
- **E1 — PROVED (PP direct check, not only the symmetry principle).** For ds² = e^{2A}dx² + dy² + e^{2B}ds²(H²) + e^{2C}ds²(S⁴), G₄ = Q vol(S⁴): all 55 off-diagonal Ricci components vanish identically; the x, Σ and S⁴ Einstein equations reproduce NL's A″, B″, C″ equations exactly; G^y_y − T^y_y equals NL's constraint exactly (ratio 1); dG₄ = 0 and d⋆G₄ = ½G₄∧G₄ hold trivially (⋆G₄ ∝ dt∧dx³∧dy∧vol_{H²} with y-dependent coefficient; G₄∧G₄ = 0). Fixed point A′ = −1, e^{−2B} = 4, e^{−2C} = 8/3, q² = 24: residuals 0 exactly.
- **E7 — PROVED.** Face data A′ = B′ = a, C′ = −2a: K = −2a, k_x − K = 3a, κ²ρ = 6a. Tension = charge with the standard (Dirac-consistent) normalisation [G₄] = 2κ²T_{M5}n, [G₄] = 2q ⇒ ρ = q/κ² ⇒ **a = q/6**. Cross-check: the flat BPS M5 wall (PP C6 check in FINDINGS_PP_AUDIT_NL_t4407_…_1935: q² = 1 BPS) has k_x = |H′|H^{−4/3}/6 = q_orth/6. Consistent. In this truncation "tension = charge" is therefore derived (closing PP's 1935 item N2 **for the singlet class only**).
- **E8 — PROVED exactly.** With S = −2a and a = q/6 the constraint is −9a² + 9a² + e^{−2B_w} − 6e^{−2C_w} = 0 ⇒ **e^{−2B_w} = 6e^{−2C_w}** (sympy: exact). One-parameter family in C_w (Q fixed by flux), as stated. NL's "≤ 6·10⁻¹⁴" is only a numerical check; the algebra is exact.
- **E9 — PROVED** (curvature terms vanish when Σ and fibre are flat).
- **E0 — PROVED** (trivial). **E2 — PROVED** (the twist and X_a ≠ X_b are not SO(5)-invariant).
- **E10 — PROVED (upgrade from CONDITIONAL on E4).** E4 forces β′ ≡ 0 in the bulk, hence β′(r_b⁺) = 0. The C4 family needs (1+2γ)β′ = −2f′ with k_x = f′/(1+2γ) > 0 (or, for γ = −½, β′ ≠ 0): impossible. So no NEC-satisfying M5 face closes within the uniform ansatz (scope as E3).
- **E5, E6 — OPEN** (correct; citations hep-th/9807051, hep-th/0003286, 2011.04775 used without upgrade).

## 2. Shoot file (1936) — singlet toy, not MN2
- **S1 — PROVED exactly.** PP's exact Jacobian at the fixed point: characteristic polynomial **−(λ−8)(λ²−4λ−48)(λ²−4λ−8)**, eigenvalues 8, **2 ± 2√13 = 2 ± √52**, **2 ± 2√3 = 2 ± √12**. m²L² = s(s−4) = 48 and 8 ⇒ Δ = 2+√52 ≈ 9.2111 and 2+√12 ≈ 5.4641 (both irrelevant). λ = 8 is the off-constraint direction.
- **S2 — PROVED.** Stable (IR-decaying, y → +∞) eigenvalues 2−√52, 2−√12: a 2D stable manifold W^s in the 4D constraint surface ⇒ codimension 2.
- **S3 — CONDITIONAL (genericity heuristic).** 1D wall curve vs codim-2 W^s in 4D: generically empty intersection. Not a proof (non-generic tangency/intersection is not excluded).
- **S4 — CONDITIONAL (numeric, float).** NL's 141-point scan in C_w − C0 ∈ [−2, 1.5] + refinement: all runs blow up before y ≈ 1.5. Coverage issues (fix J4): (i) C_w ∈ ℝ is unbounded; |C_w − C0| > 2 (resp. > 1.5) is not scanned; (ii) a grid over C_w detects a solution only through min|Y−FP| → 0, but near an isolated solution C_w* the closest approach scales like |δC|^{|λ_s|/(|λ_s|+λ_u)} ≈ |δC|^{0.14}, so at the 0.025 grid step a true solution could still show min|Y−FP| = O(0.5–1); the scan alone cannot exclude it. **PP independent check (complementary):** PP swept W^s itself backwards from the FP (1440 directions in the stable eigenplane, ε = 10⁻⁴, y down to −40 or |Y| = 60) and measured the wall residual |(B′−A′, C′+2A′, A′ − Qe^{−4C}/6)|: **minimum 2.309 over all of W^s swept** (median 2.62), constraint held to 2e-8. W^s never comes near the wall curve in the box |Y| ≤ 60. Together with NL's scan this is strong numerical evidence of **no toy solution**, but it is float-only and box-limited ⇒ CONDITIONAL. "No solution" stays CONDITIONAL until an interval/analytic argument.
- **S5, S6 — OPEN** (correct). S6's counting remark (an extra wall modulus would be needed) is a reasonable heuristic, not graded.

## 3. Erratum (1936) — faithful
- The 1859 file lists L1, L2, L3, L5 and no L4; its tally counts L5 once (PROVED list). Renumbering "L5 → L4 (= L5 in 1859)" changes no content or count. **Faithful.** X1 is a record check (PP: verified record, not a mathematical result). PP's 1935 findings refer to "L5" = this L4.

## 4. Grade table and rollups
| item | NL | PP |
|---|---|---|
| E0 | PROVED | PROVED |
| E1 | PROVED | PROVED (direct exact check) |
| E2 | PROVED | PROVED |
| E3 | REFUTED | REFUTED (counterexample genuine; closed form) |
| E4 | CONDITIONAL | **PROVED** (closed form) |
| E5 | OPEN | OPEN |
| E6 | OPEN | OPEN |
| E7 | PROVED | PROVED |
| E8 | PROVED | PROVED (exact) |
| E9 | PROVED | PROVED |
| E10 | CONDITIONAL | **PROVED** (given E4; scope of E3) |
| S1 | PROVED | PROVED (exact) |
| S2 | PROVED | PROVED |
| S3 | CONDITIONAL | CONDITIONAL |
| S4 | CONDITIONAL | CONDITIONAL (+ PP W^s sweep) |
| S5 | OPEN | OPEN |
| S6 | OPEN | OPEN |
| X1 (erratum) | PROVED | record verified (faithful) |
- Tallies vs tables: equations 6/2/2/1 = 11 ✓ matches its table; shoot 2/2/2/0 = 6 ✓; erratum 1/0/0/0 ✓.
- **PP rollup:** equations **PROVED 8 · COND 0 · OPEN 2 · REFUTED 1**; shoot **PROVED 2 · COND 2 · OPEN 2 · REFUTED 0**; erratum: record verified (faithful). Combined (17 math items): **PROVED 10 · CONDITIONAL 2 · OPEN 4 · REFUTED 1** (NL: 8/4/4/1 + erratum 1).

## 5. Against PP's required deliverables (FINDINGS_PP_AUDIT_NL_t4407_…_1935 §1.4)
1. Truncation: singlet class — **met** (E1 PROVED). On MN2 — **not met**: the uniform ansatz is refuted (E3/E4), a consistent MN2 breathing truncation is OPEN (E5/E6).
2. Flux: singlet Q constant, closed and co-closed — met in the toy; quantization to N = 4880 and the jump 2N_flux = 9760 not tied to the toy units — **not met**.
3. Face data incl. tension = charge and Hamiltonian constraint — **met in the singlet class** (E7, E8); not on MN2.
4. NEC — positive-tension M5 face, met; the c-theorem inequality k_x,E ≤ 1/L_E is not reported (here A_E′ = a − 2a = −a at the face) — **partly met**.
5. IR boundary conditions — exact for the toy fixed point (S1, S2); **not met** for MN2.
6. Shoot — toy only, float, no solution (CONDITIONAL); **not met** for MN2.
7. Symmetry / Group A scope — met (E0).
8. HW tr F² = ½tr R² on the face — **not addressed**.
9. Supersymmetry — not addressed (optional).
Net: the breathing-mode route is **not yet gradable on MN2**. What survives: local closure is consistent in a consistent truncation (singlet), but that truncation excludes MN2; on MN2 the natural ansatz is dead (PROVED). **Junction: UNSOLVED.**

## 6. Fix list for NL (numbered)
1. J1: mark mn2_breathing_consistency.log and _v2.log as empty/superseded runs (their sidecars hash the empty file).
2. J2 (E3/E4): state the radial gauge (e^{2f} on dr²) and the G₄ class (no dr, no dx legs); cite PP's closed form R_{rχ} = (3/2)β′∂_χ ln D̃ and upgrade E4 and E10 to PROVED; strengthen E3 to "the ansatz forces β′ ≡ 0".
3. J3 (E8): present the constraint algebra as exact (−9a² + q²/4 = 0 at a = q/6), not via a 6·10⁻¹⁴ residual.
4. J4 (S4): add the coverage caveats (unbounded C_w; grid resolution vs the |δC|^{0.14} approach law; box |Y| ≤ 60) and keep "no toy solution" CONDITIONAL; consider adding a W^s sweep like PP's or an interval argument.
5. J5 (E7): state the M5 normalisation used for tension = charge ([G₄] = 2κ²T_{M5}n, Dirac-consistent).
6. J6 (next step, E5/E6): any MN2 breathing truncation must allow β(r, χ) and/or r-dependent squashing and/or G₄ ⊃ dr∧dχ legs so that T_{rχ} can balance R_{rχ}; deliver exact residuals of all 11D components, then items 2, 4, 5, 6, 8 of PP's §1.4 list.
7. J7: report the face c-theorem quantity A_E′ = −a and its comparison with the IR value in any future shoot.

Tip 7cddb188 untouched (read-only). No CERT. Nothing sent. Nothing adopted.
