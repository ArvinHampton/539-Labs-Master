# FINDINGS: PP audit of NL Erratum 20 (6b10854d…) and NL D6 nonlinear (r,χ) KSE checkpoint (ff2c74bc…)
2026-11-09, 21:23 CST (America/Chicago). Auditor: Professor Proof (PP). Pure math. Labels PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. Float-only results are CONDITIONAL; a citation alone never proves; a stated premise is graded as an implication. **Nothing adopted. Junction: UNSOLVED.** No CERT, nothing sent, no Gemini. New file only. Companion: FINDINGS_PP_AUDIT_NL_t4426_FIVE_FILES_2026-11-09_2122.md (3fa2e067…).
Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 at start and at write time (unchanged).

## 0. Integrity
| file | sha256 | sidecar |
|---|---|---|
| NL_ERRATUM20_ACCEPT_PP_8c57e68b_0a82cf18_2026-11-09_2056.md | 6b10854d0b83439f8a19f12a1466ef28e7456f9bc3ee8fab32982948cc000ffe | MATCH (20:56) |
| NL_DERIVED_BPS_D6_NONLINEAR_RCHI_KSE_2026-11-09_2100.md | ff2c74bc527b512a8a13d55ee89c03e56b059ba722710dd056d336901df9396f | MATCH (21:00) |
Sources cited by E20 verified: PP 8c57e68b… (FINDINGS_PP_CONFIRM_NL_ERRATUM19_…_2032), PP 0a82cf18… (FINDINGS_PP_AUDIT_MR2_CROSSCHECK_NL_BPS_1aa88a30_…_2034), MR2 68f082e9…, target E19 d3dd5a4c… — all match.
Scripts:
| script | sha (= sidecar) | sidecar timing | PP rerun |
|---|---|---|---|
| nl-e20-z1/z1_check.py | 313d2be8… | .py 20:56:29, sidecar 20:56:59 = **after** the run (log 20:56:59); disclosed by E20 ✓ | exit 0, **byte-identical** (1ad3137b…) |
| nl-bps-d6-2057/z2_centre_flow_faces.py | 21bcbc3f… | frozen 20:57:39 before log 20:57:48 ✓ | exit 0, **byte-identical** (03b2db8b…) |
| nl-bps-d6-2057/z2_scan_v3.py | 80fad08e… | frozen 20:58:31 before log 20:59:08 ✓ | exit 0, **byte-identical** (738f6e81…) when run from its own path (stderr carries the script path) |
| nl-bps-d6-2057/z2_scan_wide.py | 2b13a81b… | frozen 20:58:05 ✓ | exit 1 (crash, as disclosed); **stdout byte-identical** (0a5377d0…). NL's kept log is stdout only: the RuntimeWarning and the ValueError traceback ("initial state y0 must be finite") are not in it. |
PP exact script (new): /workspace/pp-d6-exact-2026-11-09/pp_d6_exact_2026-11-09_2112.py = c39b3a8548a91cce5f72b3ba210c528eabd8c78610a9934a4852f7a30ec558ae, log de12f16ee2a84733e649fdb54b489e6fe4cf37177ee29f5299cbb1bcd7f33d3e (both with sidecars; exit 0).

## A. NL Erratum 20 (2056): **FAITHFUL**; NL 6/0/1/0 arithmetic correct; PP distinct-claim tally 2/0/1/0 (+4 bookkeeping rows)
- **H1–H4 applied faithfully.** E20-1 = H1 (distinct E19 tally 12/3/3/1 = 19; 20d = E19-6; 20a/c/d/e ⊂ E19-10; 20a = 2017 D6) ✓. E20-2 = H2 (rename 20b to "NEC-compatible D5 sign at a χ-dependent wall (D6 (c))") ✓. E20-3 = H3 (analytic chain; 8.9e-16 / 15.6 as float cross-check only) ✓ — the chain is quoted correctly (x-row, Σ₁-row, 3!-ordered sum, Γ_{Σ₁}Γ^{Σ₂} = Γ^{Σ₁Σ₂}, +σ/2). E20-4 = H4 ✓.
- **Z1 matches PP exactly.** z1_check rerun byte-identical: G = diag(60,60,3); ∇V = 0 at MN2; m²L² = {12, −4, 0}; ∂³_wV|_{MN2} = −24·2^{2/3}g². Exponents μL ∈ {0, 4} follow from μ² − 4μ − m²L² = 0 with m² = 0 ✓ (stated in E20-5; the script prints the masses and the cubic, not the exponents). W₃ exponent +4 ✓.
- **Z2 is OPEN** (E20-6) ✓. Its asymptotics w ≈ −1/(2^{2/3}g²L·r) agree with PP's exact computation (§B, D6-6).
- **Re-scoping (E20-7):** P1 (E19-3), P3 (E19-4), D3 (E19-18), B6 and the K7 / E19-9 no-wall closure now carry "level 0 with W-flow kept sides" ✓; outside that scope (non-W kept sides creeping along w) they are OPEN ✓; applies in both [χU] and [χS] ✓.
- **Post-run z1_check sidecar disclosed** ✓ (mtimes confirm).
| item | NL | PP | note |
|---|---|---|---|
| E20-1 | PROVED | bookkeeping (accept) | tally arithmetic, not a math claim |
| E20-2 | PROVED | bookkeeping (accept) | rename |
| E20-3 | PROVED | PROVED (= E19-15, not new) | restates a counted result |
| E20-4 | PROVED | bookkeeping (accept) | note |
| E20-5 | PROVED | **PROVED** | exact, rerun identical, = PP Z1 |
| E20-6 | OPEN | **OPEN** | = PP Z2 |
| E20-7 | PROVED | **PROVED (scoping implication)** | |
NL 6/0/1/0 = 7 is arithmetically correct. PP counts distinct new mathematical claims as **2/0/1/0 = 3** (E20-5, E20-7; E20-6), with E20-1/2/4 as bookkeeping and E20-3 a restatement of E19-15.
Fixes (optional, bookkeeping): **E20-a** carry H1/H2/H4 rows as hygiene without a PROVED label, and mark E20-3 as "= E19-15, not re-counted" (the same inflation pattern PP flagged in H1). **E20-b** If the μL ∈ {0,4} exponents are to be "re-derived in z1_check", print them in the script (currently they follow by hand from m²L² = 0).

## B. NL D6 nonlinear (r,χ) KSE checkpoint (2100), PARTIAL: **VERIFIED; NL 4/2/2/0; PP 4/2/2/0 with scope wording on D6-6; count fix on the Z2 scan**
**D6-2 / D6-3, exact (PP script).** With commuting eigenvalues Γ^{Σ12} = is₁, Γ^{χν} = is₂, Γ^{θφ} = is₃ and the D1 rows k_aε = −(σ/144)(G̸ − 12Γ_aΓ^{cde}G_{acde})ε:
- G̸ε = 24(−s₂s₃f₄ − s₁s₂ω₁ − s₁s₃ω₂)ε ⇒ k_x = (α+β₁+β₂)/6 ✓ exact;
- k_Σ − k_x = −(β₁+β₂)/2, k_χ − k_x = −(α+β₁)/2, k_θ − k_x = −(α+β₂)/2 ✓ exact;
- the D5 form (k_Σ − k_x) = +(σ/2)Γ^{Σ12}ω̸ reproduces −(β₁+β₂)/2 exactly ✓ (consistent with E19-15's +σ/2);
- NEC (k_v ≤ k_x for all six) ⇔ β₁+β₂ ≥ 0, α+β₁ ≥ 0, α+β₂ ≥ 0 ✓; summing gives 2(α+β₁+β₂) = 12k_x ≥ 0 ✓.
- **New PP observation:** K_int + 6k_x = 6k_x + tr M + 6k_x, with tr M = −2(α+β₁+β₂) = −12k_x, so **D2 (K_int = −6k_x) holds identically for all (α, β₁, β₂)**. D2 is automatic for D6-2 data; it is not an extra condition.
- Example α = β₁ = β₂ = b > 0: k_x = b/2 > 0, M = −b·𝟙 on all six directions, k_Σ − k_x = −b < 0 (NEC-compatible D5 sign) ✓, and b = 2k_x holds identically ✓.
- **Not claimed as a wall** ✓: D6-3 says "only that the local data are consistent. It is not a wall"; the summary box says "No candidate wall found".
**D6-4 (COND)** ✓: the ω₂ twist charge ∝ l rests on bulk Bianchi with no other sources meeting C₄ and C₄ non-degenerate on the kept side — stated conditions; COND is right.
**D6-5 (OPEN)** ✓: η = sgn(σs₁s₃Φ_tw) needs the bulk Killing spinor. The η = −1 NEC conditions α ≥ |β₂|, β₁ ≥ |β₂| follow from D6-2 with β₂ = −|β₂| ✓ (PP by hand).
**D6-6, exact (PP script).** V0 = −3·2^{2/3}g², L² = 2·2^{1/3}/g² (g²L² = 2^{4/3}) ✓; ∂²_wV = ∂_w∂_φV = ∂_w∂_λV = 0 at MN2 ✓ (no Hessian mixing); ∂³_wV = −24·2^{2/3}g² ✓. With w'' + 4A'w' = G_ww⁻¹∂_wV (G_ww = 3; the same convention as z2_scan_v3's rhs), A' = −1/L, and w'' dropped (it is O(w³)), the slow-manifold equation is w' = c w² with
  **c = −(L/4)(1/3)(½)∂³_wV = 2^{2/3}g²L = 2^{4/3}g > 0** (2.5198 at g = 1) ✓.
  Exact solution w(r) = −1/(c r − 1/w₀): for w₀ < 0 it is defined for all r ≥ 0 and tends to 0⁻ as r → +∞; for w₀ > 0 it blows up at r = 1/(c w₀) ✓. Substituting w = −1/(c(r−r₀)) into the full w equation leaves only the w'' term, 2^{2/3}/(2g(r₀−r)³) = O(r⁻³), so the leading order is consistent ✓. Slaved shift (δφ, δλ) = (1/5, 13/30)·w² **exactly** (NL's 0.2, 0.4333 from the script) ✓.
  Grade: **PROVED** as the leading-order slow-manifold reduction, with the sign of c and the one-sidedness. The existence of genuine second-order flows with this asymptotics (a 1-dim centre manifold, and its uniqueness or non-uniqueness) rests on the centre-manifold theorem, which is classical but cited. That part is a premise; it is not proved here.
**Z2 scan (D6-7): COND, and it does not close Z2** ✓. NL correctly states "A finite scan cannot make this PROVED" and "Z2 verdict: OPEN". Reruns are identical. Minimum worst-direction margin over all logs is **+0.4314** (z2_scan_v3, w₀ = −0.30, d₆ = −0.30) ✓; "NEC-respecting face found: False" in both scans ✓; min D2 ratio 1.014e-2 (w₀ = −0.3, d₆ = −0.15) ✓; min k_Σ − k_x ≈ −1.93 ✓.
- **Count fix:** z2_scan_v3 has 52 grid points with 16 skipped, i.e. **36 real flows**. The "48" is 36 (v3) + 12 (z2_centre_flow_faces, a different grid: w₀ ∈ {−0.02, −0.05, −0.10, −0.20}, d₆ ∈ {−0.02, 0, +0.02}). The text's grid (w₀ ∈ {−0.01, −0.03, −0.1, −0.3}, d₆ ∈ {−0.30 … +0.10}) describes only the 36. The crashed z2_scan_wide (9 flows before the crash) is presumably not counted.
- Additional COND reasons: the initial data are only O(w²)-slaved (crude at |w₀| = 0.3, as NL says); a 9×7 (χ,θ) grid; A' is computed from the Hamiltonian constraint with a max(·,0) clip in the integrand.
**D6-1 (PROVED)** accepted as an implication of the stated warped-product x-row ∂̸Aε = −(1/144)G̸ε (premise), with ε and G odd. PP did not re-derive that x-row.
**D6-8 (OPEN)** ✓.
| item | NL | PP | note |
|---|---|---|---|
| D6-1 | PROVED | **PROVED (impl.)** | given the stated x-row |
| D6-2 | PROVED | **PROVED (exact, impl. of D1 rows)** | PP exact |
| D6-3 | PROVED | **PROVED** | local data only; not a wall |
| D6-4 | COND | **COND** | |
| D6-5 | OPEN | **OPEN** | |
| D6-6 | PROVED | **PROVED (leading order)** | existence via the centre-manifold theorem is a premise |
| D6-7 | COND | **COND** | float, finite sample; not a closure of Z2 |
| D6-8 | OPEN | **OPEN** | |
PP tally **4/2/2/0 = 8** (matches NL). Status PARTIAL is accurate.
Fixes: **D6-a** Z2 scan count: "36 real flows (z2_scan_v3) + 12 (z2_centre_flow_faces) = 48", with both grids stated. **D6-b** D6-3: D2 is an identity for D6-2 data (tr M = −12k_x), so "requires b = 2k_x ✓" should read "holds identically". **D6-c** D6-6: write c = 2^{4/3}g (= 2^{2/3}g²L), the exact slaving (1/5, 13/30)w², and "leading order; existence of the centre-manifold flow by the (cited) centre-manifold theorem". **D6-d** D6-8: "Within the truncation that family fails the 11D NEC (D3, D6-7)" mixes a PROVED result (D3, W-flows) with float evidence (D6-7, Z2 flows); say so explicitly. **D6-e** z2_scan_wide's kept log is stdout only; note that the traceback (y0 non-finite) is not in it.

## Summary
| file | NL | PP | verdict |
|---|---|---|---|
| Erratum 20 (2056) | 6/0/1/0 | 2/0/1/0 distinct (+4 bookkeeping/restated) | FAITHFUL to H1–H4, Z1, Z2; re-scoping correct |
| D6 checkpoint (2100) | 4/2/2/0 | **4/2/2/0** | VERIFIED; D6-2/3/6 exact; Z2 scan COND and Z2 stays OPEN |
Junction UNSOLVED; D6 and Z2 OPEN; nothing adopted. No CERT. Nothing sent.
Tip at write time: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (unchanged).
