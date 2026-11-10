# FINDINGS — PP audit of NL t4407 candidate files: junction sources (1859), b/J7 (1900), bulk→H⊗ℂ² map + Φ Q3 (1901), VOID notice (1902) — 2026-11-09 19:35 CST (America/Chicago)
Auditor: Professor Proof (PP). Pure math. Labels: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. **Nothing is adopted; the Owner chooses. Recommendations are NL's opinions; PP grades the math only.**
No CERT. No messages or external sends. No Gemini. Tip 7cddb188 read-only (untouched). Lock 96f8d42e §4 stays purged. Additive new file.

## 0. Authority and integrity
- OW b0b9ae7f (t4407, "Pursue all for resolutions"): file sha256 b0b9ae7f… = sidecar (MATCH). OW 90cec14c (t4415, "S4 breathing mode. Pursue it."): MATCH. OW 8b26c786 (t4414, Group A): MATCH. Citation scope OW 3f160803 amended by 36683379 applied: a citation never upgrades to PROVED.
- Full sha256 = sidecar (all MATCH):
  - NL_CANDIDATES_JUNCTION_SOURCES_MN2_VS_PP_aeb9ab13_2026-11-09_1859.md 9987bdcd023e94b1de0c40f142caa96417612edb1fe2ac380eceb18489582012
  - NL_CANDIDATES_B_J7_2026-11-09_1900.md 0a461c8ffe071edd2889f21990cf5b75180ea8e27b2ffe04297c004c67fc06c6
  - NL_CANDIDATES_BULK_TO_HC2_MAP_PHI_Q3_2026-11-09_1901.md ff95449ae3c374ea3975df2ec142681c0b1a3fa39fb5a3322431df33bba85c55
  - NL_VOID_NOTICE_ERRATUM15_DRAFT_1851_2026-11-09_1902.md da1b893d29b2e4d14726788b8bdd897beaaba3ac2269d1baa1d107fa8d300813
  - /workspace/nl-cand-1854/: clp_face_lemma.py 4bf4ed0d…, .log 2cdd6e37…, map_checks.py 11e97edf…, .log 4e70e9a4…, phi_mn2.py 022b0752…, .log 0bb298b5…, phi_exact.py 052fea13…, .log 5eeb94e2… (all MATCH).
- **Reruns:** all four NL scripts rerun by PP; outputs byte-identical to NL's logs (exit 0).
- **PP independent scripts** (/workspace/pp-audit-t4407-nl/, MANIFEST.sha256):
  - pp_israel_face_q.py 13679d18… (exact sympy Israel conditions from the full 10D face metric in coordinates, twist included, transformed to the twist-adapted frame), round-X log pp_israel_face_round.log 7e2fc241…
  - pp_c6_m5wall.py 9843d792… / .log 6b5e8add… (11D EOM of the C6 M5 wall, exact)
  - pp_file3_checks.py 63d71712… / .log bf3c7d7f… (MC1 antiunitary check, exact Φ(s), interval monotonicity, L5)
  - pa1.log ae794ab1… (30-digit quadrature of Φ̄).
- Records used: PP aeb9ab13 (MN2 wall Israel, convention S_ab = −(1/κ²)([K_ab] − h_ab[K]), [K]=2K on the ℤ₂ plane), PP 384096a8 gate logs (/workspace/pp_gate_1750/einstein60.log, G²), PP 9dde377d (FINDINGS_PP_DERIVE_11D_MAP_1328 B2), NL 1655 (J1c/J6/J7).

---
## 1. File 1 — junction sources (1859) — PRIORITY (per OW 90cec14c)

### 1.1 Priority check 1: the CLP no-go (C1) — **REFUTED claim upheld; no-go PROVED within an explicit scope**
PP's own proof (independent of NL's code):
- Face metric at constant r: ds²₁₀ = Δ̃^{1/3}[e^{2f}dx² + e^{2g}ds²_Σ] + g_c^{−2}Δ̃^{−2/3}Σ_a X_a^{−1}(dμ_a² + μ_a²Dφ_a²), X_a = e^{2λ_a}, λ₀ = −2(λ₁+λ₂), Δ̃ = D = Σ X_aμ_a². Unit normal n = Δ̃^{−1/6}∂_r. Shape-operator eigenvalues (times Δ̃^{1/6}): k_x = f′ + D′/6D, k_Σ = g′ + D′/6D, k_{φ_i} = −D′/3D − λ_i′, μ-block = −D′/3D·1 + ½G⁻¹∂_rG.
- **C2 (PROVED, analytic).** The induced determinant of Σ X_a^{−1}dμ_a² on S² is (Π_a X_a^{−1})·D (Cauchy–Binet / normal-vector formula), so ½tr(G⁻¹∂_rG) = λ₁′+λ₂′ + ½D′/D. Hence Σk_fib = −(4/3)D′/D + ½D′/D = **−(5/6)D′/D**, and K = 4f′+2g′+D′/6D, so **k_x − K = −(3f′+2g′)**. Exact sympy confirms both identities at 5 exact rational points × 4 choices of (X₁,X₂,a₁,a₂) (pp_israel_face logs: residual 0).
- Source content and conditions (κ²S^a_b = −2(K^a_b − δ^a_bK)):
  - smeared M5 on x×Σ: S = −σ on x and Σ, 0 on fibre ⇒ k_Σ = k_x and every fibre eigenvalue = K;
  - E₈ with F on fibre only: T_x = T_Σ = −¼F², fibre trace of T = 0 ⇒ k_Σ = k_x and Σk_fib = 4K;
  - any mix of the two ⇒ the weaker pair (k_Σ = k_x, Σk_fib = 4K).
- Proof: Σk_fib = 4K and K = 4k_x + 2k_Σ + Σk_fib ⇒ K = −2k_x, Σk_fib = −8k_x. With C2: −(5/6)D′/D = −8f′ − (4/3)D′/D ⇒ **½D′/D = −8f′, constant on S⁴**. Σ_a(2λ_a′ − c)X_aμ_a² ≡ 0 on S⁴ ⇒ 2λ_a′ = c ∀a; λ₀′+2λ₁′... i.e. Σ_a weighted λ₀′ = −2(λ₁′+λ₂′) ⇒ 5c/2 = 0 ⇒ c = 0 ⇒ λ′ = 0, f′ = 0, g′ = f′ = 0, all k = 0, ρ = −(2/κ²)(3f′+2g′) = 0. **PROVED.**
- Independent exact check (round X, twist a=(1,0)): linsolve over 5 exact points gives the unique solution (f′,g′,λ₁′,λ₂′) = 0 for M5, E₈-fibre and M5+E₈-fibre. Non-round-X exact linsolve runs were still in progress when this file was written (PENDING, not needed: the analytic proof above is for arbitrary X).
- **Scope (must be stated by NL; fix F1):** (i) cohomogeneity-one ansatz (all fields depend on r only; Σ homogeneous); (ii) gauge fields r-independent on the face (no F_{rΣ}); (iii) M5s wrap x×Σ (M5s on fibre 2-cycles or with Σ×fibre legs are not covered — they break k_Σ = k_x and belong to C10); (iv) the smeared stress is diagonal in the **twist-adapted frame** E_u = ∂_u − g_cA_i∂_{φ_i}. PP found that in the coordinate basis K^{φ_i}{}_u = g_cA_i(k_{φ_i} − k_Σ) ≠ 0; imposing "S^{φ}{}_u = 0" in coordinates would wrongly kill even the C4 family (PP's first run showed exactly that artefact). Hypothesis (iv) is the correct gauge-covariant smearing and is what NL's script implicitly uses.
- "Any r_b, BPS or not" is correct within (i)–(iv): the proof uses only first derivatives at the face, never the bulk EOM.

### 1.2 Priority check 2: breathing-mode local closure (C4) — **PROVED (Israel algebra only); "tension = charge" NOT proved on the twisted S⁴**
- Ansatz: fibre metric × e^{2β}, 7D block (incl. dr²) × e^{2γβ}. Then k_x = f′+D′/6D+γβ′, k_Σ = g′+D′/6D+γβ′, every fibre eigenvalue shifts by +β′, normal lapse × e^{γβ} (homogeneous).
- PP analytic derivation (M5 on x×Σ): k_{φ1} = k_{φ2} ⇒ λ₁′ = λ₂′ where μ₁μ₂ ≠ 0; the φ-equation reads −½D′/D = λ₁′ + 6f′ + (6γ+3)β′ (after g′ = f′ from k_Σ = k_x), RHS constant on S⁴ ⇒ D′/D constant ⇒ λ′ = 0 (as in 1.1). Remaining: β′ = K ⇒ **(1+2γ)β′ = −2f′**.
- **General solution (exact sympy, round X; also for M5+E₈-fibre):** (f′, g′, λ₁′, λ₂′, β′) = β′·(−(γ+½), −(γ+½), 0, 0, 1). For γ ≠ −½ this is NL's family λ′=0, g′=f′, β′ = −2f′/(1+2γ). **For γ = −½ the solution still exists** (f′=g′=0, β′ free); NL's "every γ tested" should read "every γ" (fix F2).
- On the family, at every test point (exact): Δ̃^{1/6}·k_x = k_Σ = f′/(1+2γ); every fibre eigenvalue = **−2k_x**; K = −2k_x; fibre stress S_fib = 0 exactly (pure-M5 form); **κ²ρ = 6k_x** (ρ/k_x = 6). Hence k_Σ = k_x, k_fib = −2k_x **PROVED**.
- **Signs / NEC (C5) — PROVED.** In the aeb9ab13 convention (normal into the kept side), ρ = −(2/κ²)(k_x − K)·(−1) = (2/κ²)(k_x−K) = 6k_x/κ². ρ > 0 ⇔ k_x > 0. M5 stress: ρ+P = 0 on worldvolume, ρ > 0 transverse ⇒ NEC (indeed DEC) holds iff ρ ≥ 0. Cross-check: exact MN2 (f′ = −k, rest 0) gives ρ = 6k/κ², reproducing aeb9ab13. 5D Einstein frame: d ln √g₆/dr = 2k_Σ + Σk_fib = −6k_x ⇒ A_E′ = k_x + (1/3)(−6k_x) = **−k_x** (PROVED; RS-like, same sign as the MN2 IR where A_E′ = −k).
- **"Tension = charge": not established by C4.** C4 fixes ρ = 6k_x/κ² for any k_x > 0; it says nothing about the G₄ jump. BPS tension = charge is PROVED only in the flat analogue C6 (below). On the twisted, CLP-warped S⁴ it is **OPEN** (needs the G₄ junction [G₄] = 2G₄|_face = κ²-normalised M5 charge density and the bulk flux profile with β). The relay summary "tension = charge (PROVED algebra)" over-states NL's file (the file itself only asserts it in the JS-C definition). Fix F3.
- **Consistent truncation of the breathing mode — OPEN.** C4 is pure kinematics of a metric ansatz at a hypersurface and does not need a truncation. The breathing mode is a known consistent truncation on the round S⁴ with Freund–Rubin flux alone (Bremer–Duff–Lü–Pope–Stelle, hep-th/9807051 — cited, not re-derived; citation alone does not upgrade). Its consistency **together with** the CLP U(1)² scalars, the gauge fields and the Bolza twist is not on record and is generically false for massive modes (the breathing mode is massive, Δ = 8 type). Grade: OPEN. An alternative that avoids the issue: solve the full 11D cohomogeneity-two (r, μ₁) PDE system with the ansatz as boundary data.
- C6 (PROVED, exact 11D EOM): ds² = H^{−1/3}(dx₄² + dΣ²) + H^{2/3}(dr² + dT⁴), H = H₀ − c r (r>0), G₄ = q H′ vol_{T⁴}: all 11 diagonal Einstein residuals vanish iff **q² = 1** (BPS: tension = charge), and k_T/k_x = −2, k_Σ = k_x, k_x > 0 for c > 0 (PROVED). **Flat Σ only:** with Σ = H² the Σ-components fail by −1/s₂² (the Σ curvature) — so C6 is an analogue, not a twisted-MN2 solution. NL should say "flat Σ (T² or ℝ²)" (fix F4). G₄ ∝ H′ is odd across the doubled wall (PROVED).

### 1.3 Remaining file-1 items
| item | NL | PP verdict | notes |
|---|---|---|---|
| L1 τ ≤ 6 for NEC sources; wall needs τ = 8 | PROVED | **PROVED** (given N1 thin-wall Israel, N3 exact-MN2 bulk) | Poincaré kills S_{μe}; NEC on t+e for each internal eigen-direction, summed. The direct per-direction form (S_req(k,k) = −2k/κ² for every internal ê, aeb9ab13) is stronger than the trace; NL may cite either. ρ>0 needed only to divide. |
| L2 Σ(p_i−8)σ_i = 0 ⇒ some σ_i < 0 | PROVED | **PROVED** | if all σ_i ≥ 0 the sum is ≤ 0 with equality only if ρ = 0 ≠ 6. |
| L3 6D-worldvolume mixes | REFUTED | **REFUTED (by proof)** | trace −2ρ = −12 ≠ −48. |
| L5 thick wall still NEC-violating | PROVED | **PROVED with an added hypothesis** | R(k,k) = A″+4A′²+Ric_int(e,e) verified for g_int ρ-independent; O(L(k²+|Ric|)) needs sup|A′| = O(k) (e.g. monotone smoothing). "Whatever the smoothing" is false without it (fix F5). 1/k ≈ 37 ℓ_p ✓ (L₅ = 37.6537 ℓ_p). |
| A1 σ_w = 8, σ₀ = −2 | PROVED | **PROVED** (unique) | saturates MR2's L3 bound |σ_neg| ≥ ρ_w/3 exactly (cross-check with MR2 batch 1). |
| A2 σ_w = 10, σ₃ = −4 | PROVED | **PROVED** (unique) | |
| A3 σ_w 3.341, σ_f 9.318, σ₀ −11.318 | COND | **CONDITIONAL** (1.288 measure) | arithmetic reproduced. |
| A4 negative-tension object in M-theory | OPEN | **OPEN** | citation hep-th/9603142 used correctly (no upgrade). |
| B1 tr R² closes junction | REFUTED | **REFUTED** (rests on PP 149be02a) | |
| B2 Casimir ≲ 10⁻⁶ | COND | **CONDITIONAL** | 256/37.654¹⁰ = 4.47e-14; ρ_w = 6/(L₅·(2π)⁸/2) = 1.31e-7; N⁻³ scaling ✓ (N^{−10/3}/N^{−1/3}). |
| B3 (ℓ_p/L₅)⁶ | COND | **CONDITIONAL** | 3.5e-10 ✓. |
| C1 | REFUTED | **REFUTED (by proof), scope 1.1** | |
| C2 | PROVED | **PROVED (analytic)** | |
| C3 | PROVED | **PROVED** | f′=λ′=0: κ²ρ = −4g′ (ρ>0 ⇔ g′<0 ✓), w = (−1, −½, −1) ✓, NEC ✓; not M5/E₈ (x≠Σ pressure). |
| C4 | PROVED | **PROVED (Israel algebra only)** | γ = −½ included; tension = charge OPEN (F3). |
| C5 | PROVED | **PROVED** | |
| C6 | PROVED | **PROVED (flat Σ)** | F4. |
| C7 | OPEN | **OPEN** | |
| C8 | COND | **CONDITIONAL** (DFGK counting cited) | |
| C9 | PROVED | **PROVED** (trivial: β is an SO(5) singlet, Σ-constant) | |
| C10 | OPEN | **OPEN** | add M5s on fibre 2-cycles (scope iii). |
- **Tally check:** header 11/4/3/3 = 21 matches the §6 table and the body item count (L1,L2,L3,L5,A1–A4,B1–B3,C1–C10 = 21). L4 skip cosmetic. **PP grades agree 11/4/3/3**, with the scope/hypothesis fixes F1–F5.
- **PP new items (not in NL's tally):** N1 twist-adapted-frame requirement (PROVED); N2 "tension = charge on twisted S⁴" (OPEN); N3 breathing-mode consistent truncation with CLP + twist (OPEN); N4 c-theorem necessary condition (below; CONDITIONAL on a 5D Einstein-scalar description).

### 1.4 What NL's breathing-mode equations (~21:30 CST) and IR shoot (~23:30 CST) must establish for PP to grade the route
1. **Equations / truncation.** Either (a) a derivation that the ansatz {CLP U(1)² (f, g, λ₁, λ₂, A^i twist, 3-form) + β with weight γ} is a consistent truncation of 11D sugra on the Bolza-twisted S⁴ (all 11D EOM components, including the μ-dependent ones, reduce to the ODEs; show the off-diagonal (r, μ) Einstein equations and the G₄ equation close), or (b) the full 11D cohomogeneity-two PDE system in (r, μ₁) with no truncation claimed. State γ (Einstein-frame value −4/5 if that is the convention) and the β kinetic/potential terms. Exact symbolic residuals required.
2. **Flux.** G₄ ansatz with β; Bianchi dG₄ = 0 in the bulk; ∫_{S⁴}G₄ = (2π)³N ℓ_p³ with N = 4880 constant in r (topological, unchanged by β); [G₄] at the face = 2G₄ (odd, f825dfff) equal to the face M5 charge 9760 (+ n_inst).
3. **Face data.** The Israel conditions in the twist-adapted frame: λ′ = 0, g′ = f′, (1+2γ)β′ = −2f′ (or γ = −½ branch), ρ = 6k_x/κ² > 0, **plus** the β junction condition (from the β kinetic term, sourced by the M5 coupling to β, if any) and the Hamiltonian constraint at the face. **Tension = charge must be derived** (BPS calibration or the explicit G₄ jump vs ρ), not assumed.
4. **NEC.** Bulk: automatic for 11D sugra fields (state it). Face: only positive-tension M5/E₈ (ρ ≥ 0). Necessary condition (PP N4, CONDITIONAL on a 5D Einstein-scalar reduction): with NEC, A_E″ ≤ 0, so A_E′ is non-increasing from −k_x(E-frame) at the face to −1/L₅,E in the IR ⇒ **k_x,E ≤ 1/L₅,E**. Report this inequality at the face.
5. **IR boundary conditions.** Approach to the exact MN2 AdS₅ × Bolza × S⁴ fixed point (X₁ = 2^{−3/5}, X₀ = X₂ = 2^{2/5}, L₅/L₇ = 2^{−2/5}): linearized modes around MN2 including β (dimensions Δ from the mass of β around MN2), which modes are normalizable/irrelevant, and the count of free parameters vs constraints (this is C8; it must be derived, not cited).
6. **Shoot.** Interval or high-precision (≥ 30 digits) integration with error control from face data to the IR; residual of all EOM along the solution; the value of the free parameter(s) (k_x, i.e. r_b or u_b) selected; whether a solution exists for the charge 9760 exactly. Float-only integration will be graded CONDITIONAL.
7. **Symmetry / scope.** β and all fields invariant under Group A = Aut⁺(Bolza) × wall ℤ₂ (OW 8b26c786); β ℤ₂-even, G₄ ℤ₂-odd.
8. **HW boundary condition.** Tangential G₄ on the face ∝ (tr F² − ½tr R²): compute tr R∧R restricted to the face with β ≠ 0, and the E₈ content needed (cf. MR2 batch-1 L1/L2).
9. **Supersymmetry (optional, J7 OPEN):** whether the configuration preserves any supercharges.

---
## 2. File 2 — b and J7 (1900)
- **Two meanings of b — kept separate: yes, with one notation collision.** §1 states both correctly (record check: 9dde377d B2 is the face separation y ∈ [0, b] with V₇eff = V̂₆e^{6B}(1−e^{−2kb})/(2k); NL 1655 J1c/J6 is the face position r_b with R_Σ(b) ↔ b undefined — both verified on disk). b-1 defines b := u_b (position meaning) **and** in b1a takes the 9dde377d interval length → ∞. No conclusion is wrong (b1a is about the interval length only, independent of u_b), but the same letter carries both meanings inside b-1, and file 3 PI2 ("kb → ∞ under b-1") inherits it. Fix F6: write b_int (9dde377d) and u_b / r_b (1655).
- **J7-2 bound (J7c) — REFUTED claim upheld, PROVED given explicit hypotheses:** (H1) thin-wall Israel at two derivatives; (H2) the bulk next to the wall is exact MN2 (N3); (H3) every J7-2 contribution to the face stress satisfies the NEC; (H4) the bulk G₄ is bounded (jump, no δ-part), so its stress carries no δ-weight (T_G is quadratic in G — PP re-derived 1711 G1). Proof (direct form): S_req(k,k) = −2k/κ² < 0 for k = t̂+ê (ê fibre or Σ); a sum of NEC sources has S(k,k) ≥ 0. Trace form: sum over the 6 internal eigen-directions, ρ = 6 > 0 ⇒ τ ≤ 6 < 8.
  - H3 is PROVED for positive-tension branes and for any two-derivative worldvolume p-form/YM field: T(k,k) = |i_kF|²/(p−1)! ≥ 0 because i_kF is orthogonal to the null k, hence spacelike or null. For the full non-linear (PST) M5 worldvolume action H3 is cited, not re-derived: that slice is CONDITIONAL. The refutation of "J7-2 closes the exact-MN2 wall" stands for all two-derivative content.
  - JS-C evades the bound only by dropping H2, not by any J7-2 content.
| item | NL | PP |
|---|---|---|
| §1 record readings (b ×2, J7 wording) | PROVED ×2 | **verified record readings** (correct; not mathematical results — PP does not count them as PROVED; fix F7) |
| b1a V₇eff → V̂₆e^{6B}/(2k) | PROVED | **PROVED** (k>0) |
| b1b N_b ∈ [12568.6, 16266.7) | COND | **CONDITIONAL** (P3c numerics) |
| b2a second plane −9760 | PROVED | **PROVED** given no bulk sources between the planes (Stokes on S¹×S⁴) |
| b2b second plane negative tension | PROVED | **PROVED** given J1 and exact MN2 between the planes (RS1 mirror) |
| b2c stabilization | OPEN | **OPEN** |
| b3a | REFUTED | **REFUTED (by proof)** via L1 (H1, H2) |
| b3b | REFUTED | **REFUTED (by proof)** via C1, within the §1.1 scope |
| b3c | COND | **CONDITIONAL** (C8) |
| J7a deficit (1.341, 3.341, 8.000) | COND | **CONDITIONAL** (σ_M = 6/1.28777) |
| J7b NEC of Δ | PROVED | **PROVED**; the Σ value ρ+P = (6−σ_M)−(8−σ_M) = −2 exactly is **independent of the 1.288 measure** (only the fibre −6.659 depends on it). Upgrade note F8. |
| J7c | REFUTED | **REFUTED (by proof)** given H1–H4 (above) |
| J7d closes locally | PROVED | **PROVED (Israel only)**; G₄ junction / tension = charge OPEN (F3) |
| J7e global | OPEN | **OPEN** |
| Remark: b at E₈ density peak | REFUTED (uncounted) | **REFUTED**, but restate: for a wall-localized density the radial profile is δ(r−r_b), whose peak is r_b for every r_b, so the rule is vacuous (selects nothing); NL's "a point of the face, not a radius" is correct for the Σ×S⁴ maximum. |
- **Tally check:** 7/3/2/3 = 15 matches NL's stated convention (record readings counted as 2 PROVED). **PP rollup for file 2: PROVED 5 (math) + 2 record readings, CONDITIONAL 3, OPEN 2, REFUTED 3 (+1 uncounted remark).**

---
## 3. File 3 — bulk→H⊗ℂ² map and Φ Q3 (1901)
The map has no definition on record; NL states an assumed setup. Items that depend on the setup are graded CONDITIONAL on it; pure algebra and pure sugra facts are graded on their own.
| item | NL | PP | reason |
|---|---|---|---|
| Mc χ₀ exists | OPEN | **OPEN** | |
| MA1 wall ℤ₂ = S is a symmetry | PROVED | **CONDITIONAL** (setup) | [1⊗σ_x, H_D⊗1] = 0 is trivial algebra; that this S *is* the wall ℤ₂ and H_tot = H_D⊗1 is the assumed map. |
| MA2 A₀⊗1 commutes with S | PROVED | **PROVED** (algebra) | σ_x real in the e-basis. |
| MA3 P₋ does not preserve S-even | PROVED | **PROVED** (algebra); "T1 must be read as A₀⊗1" CONDITIONAL (setup) | |
| MA4 sheet e₂ carries −N_flux | PROVED | **CONDITIONAL** (setup ι_A + f825dfff) | |
| MA5 ±U superselection incompatible | PROVED | **CONDITIONAL** (setup) | |
| MA6 / MB3 HW chiral projection | COND | **CONDITIONAL** (cited) | |
| MB1 A₀γ⁵A₀⁻¹ = γ⁵ (Majorana) | PROVED | **PROVED** (γ⁵ imaginary, anticommutes with γ⁰) | |
| MB2 [S′, H_D⊗1] = 0 ⇔ m = 0 | PROVED | **PROVED** (γ⁵ commutes with α_i, anticommutes with β) | |
| **MC1** T1 breaks SU(2)_R to U(1)_{T₃} | PROVED | **REFUTED (counterexample)** | T1 is antiunitary (K = complex conjugation in the e-basis, NL's own A0c2 convention). T1U = UT1 ⇔ P₂Ū = UP₂ ⇔ U = diag(u₁,u₂) with u₂ real ⇒ in SU(2): **U = ±1 only**. Counterexample U = diag(e^{−iπ/2}, e^{iπ/2}): P₂Ū − UP₂ = diag(0, −2i) ≠ 0. Correct statement (PROVED): T1U(θ)T1⁻¹ = U(−θ) on its range, so T1 **normalizes** U(1)_{T₃} (acts as charge conjugation on it) and its commutant in SU(2)_R is the centre ℤ₂. NL's script tested only the linear projector |e₂⟩⟨e₂| (fix F9). |
| MC2 | OPEN | **OPEN** | |
| PP1 L7a pointwise on every solution | PROVED | **PROVED** (setup-independent) | R_xx = −g_xxG²/144 for x with no G legs; R = G²/144 ⇒ G^x_x = −G²/96. |
| PP2 Φ·L₇² on MN2 | PROVED (computer-assisted) | **PROVED (exact)**, setup-independent; MN2 EOM status as in 19a88b19/384096a8 | PP closed form: **Φ(s)·L₇² = 192(3s²−14s+20)(2−s)^{−7/3}**, s = sin²χ = μ₁². dΦ/ds = 64(3s²−20s+56)(2−s)^{−10/3} > 0 (discriminant 400−672 < 0; also interval-checked), so Φ is strictly increasing: **range [480·2^{2/3}, 1728] = [761.95250494…, 1728] exactly**. |
| — match to PP's G² | "all printed digits" | **CONFIRMED** | PP 384096a8 gate log einstein60.log (MN2): G² = 771.30442, 1311.8244, 1061.6417, 768.79915 at (a,b) = (0.37,1.11), (2.01,0.23), (1.0,0.5), (2.6,1.3); NL exact-L₅ values 771.304421636, 1311.82436347, 1061.64171981, 768.799153302 agree to every printed digit (float-L₅ script: rel. ≤ 5.2e-8, from the 8-digit L₅ input). Endpoints: PP corners G² = 761.9525 (μ₀ = ±1) and 1728.0 (μ₁ → 1). |
| PP3 L₅/L₇ = 2^{−2/5} | COND | **PROVED** (upgrade) | exact from PP's own MN2 fixed point (mr2_core/pp_einstein par_of: AdS₅ factor ef² = X₀^{−2} = 2^{−4/5}, X₀ = 2^{2/5}). |
| PP4 Φ-P needs no b | PROVED | **PROVED** | |
| PP5 max = 1728 coincidence | OPEN | **OPEN** | |
| PA1 Φ̄ = 1018.336 | PROVED (quadrature) | **CONDITIONAL** (numeric, not interval) | PP 30-digit quadrature with the exact Φ(s): 1018.33579197…, NL's trapezoid 1018.335763 agrees to the printed 1018.336. |
| PA2 linearity | PROVED | **PROVED** | |
| PA3 measure | COND | **CONDITIONAL** | NL's weight cos²χ sinχ D^{−1/2} is √g₆ (PP check of the D powers: 1/3 − 4/3 + 1/2 = −1/2). |
| PI1 (MR2, uncounted) | — | not graded here | |
| PI2 | OPEN | **OPEN** | uses b_int (F6). |
- **Tally check:** header 13/4/4/0 = 21 matches NL's table. **PP rollup for file 3: PROVED 9, CONDITIONAL 7, OPEN 4, REFUTED 1 (MC1).**

---
## 4. VOID notice (1902)
- sha256 da1b893d29b2e4d14726788b8bdd897beaaba3ac2269d1baa1d107fa8d300813 = sidecar (MATCH). Content: declares NL_ERRATUM15_..._1851 VOID (tally-header mismatch), superseded by ..._1852 (414bdc4d…), 1851 left unmodified. **Consistent with the additive-only rule; no math content.** PP accepts it as hygiene.

---
## 5. PP rollup (this audit)
| file | PROVED | CONDITIONAL | OPEN | REFUTED | notes |
|---|---|---|---|---|---|
| 1 junction sources | 11 | 4 | 3 | 3 | agrees with NL; scope/hypothesis fixes F1–F5 |
| 1 PP new items | 1 (N1) | 1 (N4) | 2 (N2 tension = charge, N3 truncation) | 0 | |
| 2 b/J7 | 5 (+2 record readings) | 3 | 2 | 3 (+1 remark) | |
| 3 map / Φ | 9 | 7 | 4 | 1 (MC1) | PP3 upgraded; PA1, MA1, MA4, MA5 downgraded |
| 4 VOID notice | — | — | — | — | hygiene, accepted |
| **total** | **26 (+2 record)** | **15** | **11** | **7 (+1 remark)** | PENDING: non-round-X exact linsolve reruns (redundant with the analytic proof) |

Key verdicts: **CLP no-go (C1): REFUTED claim upheld — PROVED within scope.** **Breathing-mode closure (C4): PROVED as Israel algebra (λ′=0, k_Σ=k_x, k_fib=−2k_x, κ²ρ = 6k_x > 0, NEC-satisfying); tension = charge and the truncation are OPEN.** **J7-2 bound: PROVED given H1–H4.** Junction remains **UNSOLVED**.

## 6. Fix list for NL (numbered)
1. F1 (1859 C1): state the scope — cohomogeneity-one, r-independent twist, M5s on x×Σ only, stress diagonal in the twist-adapted frame E_u = ∂_u − g_cA_i∂_{φ_i}; put M5s on fibre 2-cycles into C10.
2. F2 (C4): "for every γ tested" → "for every γ"; give the γ = −½ branch (f′ = g′ = 0, β′ free, k_fib = −2k_x). Add the analytic proof (λ′ = 0 from constancy of D′/D) instead of the rank-only check.
3. F3 (C4 / J7d / relay): "tension = charge" is not derived on the twisted S⁴; label it OPEN until the G₄ junction is computed. Do not report it as PROVED algebra.
4. F4 (C6): say "flat Σ (T² or ℝ²)"; on H² the harmonic-function form fails by the Σ curvature.
5. F5 (L5): add the hypothesis sup|A′| = O(k) (e.g. monotone smoothing); drop "whatever the smoothing".
6. F6 (1900 b-1, 1901 PI2): separate symbols b_int (9dde377d interval) and u_b/r_b (1655 position).
7. F7 (1900 tally): record readings are not PROVED mathematics; list them as "record, verified".
8. F8 (J7b): note that the Σ entry −2 is measure-independent.
9. F9 (1901 MC1): REFUTED as stated; correct to "commutant {±1}; T1 normalizes U(1)_{T₃} with θ → −θ". Fix map_checks to conjugate the ℂ² factor (as A0c2 already does).
10. F10 (1901): mark MA1, MA4, MA5 CONDITIONAL on the assumed setup; PA1 CONDITIONAL (numeric) or redo with interval quadrature on the exact Φ(s); PP3 can be upgraded to PROVED by citing PP's exact MN2 fixed point (2^{−4/5} = ef²).
11. F11 (breathing-mode deliverables): meet §1.4 items 1–9 in the ~21:30 and ~23:30 files.

## 7. Per-topic candidate grading summary for the Owner (PP grades the math; recommendations are NL's)
- **Junction sources (MN2 wall).**
  - JS-A (negative-tension sector): bookkeeping PROVED (A1/A2; A1 is the minimal negative tension, exactly ρ_w/3); needs an object not known in M-theory (OPEN). Math-sound, physics-unsupported.
  - JS-B (quantum / higher-derivative): not viable (B1 REFUTED; B2, B3 negligible, CONDITIONAL).
  - JS-C (near-wall backreaction): inside CLP impossible (PROVED no-go); with the S⁴ breathing mode the face equations close locally (PROVED algebra), NEC-satisfying. Open: tension = charge, consistent truncation, IR connection. **The only candidate with no NEC-violating matter; status OPEN, pursued per OW 90cec14c.**
- **b.** b-1 (single wall, RS2 label u_b): PROVED/COND bookkeeping, selects nothing; b-2 (two-wall interval): forces a negative-tension −9760 plane (PROVED), stabilization OPEN; b-3 (dynamical): exact-MN2 and CLP versions REFUTED, breathing-mode version CONDITIONAL (counting cited).
- **J7.** J7-1 (deficit tensor definition): CONDITIONAL on measure, NEC violation along Σ measure-independent; J7-2 (G₄ legs / worldvolume flux): REFUTED given H1–H4; J7-3 (J7 = 0 with backreaction): locally PROVED (Israel), globally OPEN.
- **Bulk→H⊗ℂ² map.** M-A: algebra PROVED, physics CONDITIONAL on the assumed setup; M-B: forces m = 0 (PROVED); M-C: NL's U(1)_{T₃} residual symmetry claim REFUTED — only ±1 commutes with T1.
- **Φ Q3.** Φ-P (pointwise): PROVED exactly on MN2, b-free, range [480·2^{2/3}, 1728] L₇⁻², matches PP's G²; Φ-A: CONDITIONAL (measure, numeric); Φ-I: needs b, OPEN.

Tip 7cddb188 untouched (read-only). No CERT. Nothing sent. Nothing adopted.
