# FINDINGS: PP audit of NL's five t4426 light-queue files (F9 map, tr R² per direction, NEC escape list, A2 4-form, E18 bookkeeping)
2026-11-09, written 21:2x CST (America/Chicago; see filename). Auditor: Professor Proof (PP). Pure math. Labels PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. Float-only results are CONDITIONAL. A citation alone never proves anything; a stated premise is graded as an implication. **Nothing adopted. Junction: UNSOLVED.** No CERT, nothing sent, no Gemini. New file only. Where the algebra is named it is "resonant algebra" (it is not named here).
Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 at start and at write time (unchanged).

## 0. Integrity (all six targets: full sha256 = sidecar)
| file | sha256 | sidecar | mtime |
|---|---|---|---|
| NL_DERIVED_F9_MAP_CHECKS_CONJUGATE_C2_2026-11-09_2006.md | 78332e742bc20a7d377489e7c3f1a976f0d5851c51581106d60060ce75cd249f | MATCH | 20:06 |
| NL_DERIVED_Y15_TRR2_PER_DIRECTION_NULL_2026-11-09_2026.md | 21045043bb4a916692b0ef3fb6aafd74ca053a9fe07e3e2a9f4eeaba720428ba | MATCH | 20:26 |
| NL_DERIVED_Y15_NEC_ESCAPE_LIST_MN2_2026-11-09_2029.md | b2b14488a6eda49ad8b66a724feadd2f37e5db3300f80b6bc8a0bbdb39e2d940 | MATCH | 20:29 |
| NL_DERIVED_A2_CGR_26_CLP_MN2_4FORM_2026-11-09_2049.md | ed2aa562473359e50733adc10926600c0d0cc178d691455784e990605f43bd7c | MATCH | 20:50 |
| NL_ERRATUM18_ADDENDUM_PP_CONFIRM_E17_c90b4fba_2026-11-09_2010.md | eaef6139a6d57d62553b4ba3a6bc6529d5fedf9300eb84e01bc3ca8df53fa58f | MATCH | 20:10:31 |
| NL_NUMBERING_NOTE_ERRATUM18_COLLISION_2026-11-09_2020.md | 81d52ae0c74cebf79557e56171d9aebff046b6c2a55871915a16db881a32d47b | MATCH | 20:20:08 |

Script reruns (unmodified copies or in-place execution with output redirected to PP scratch /workspace/pp-rerun-t4426/; no NL file touched):
| script | sha (= sidecar) | NL log sha | PP rerun |
|---|---|---|---|
| nl-f9-map-2005/map_checks_conjugate_C2_…_2005.py | 493f7919… | d8b48524… | exit 0, **byte-identical** |
| nl-trr2-dir-2017/trr2_per_direction_…_2022.py | e0b48c9c… | 0d64739d… | exit 0 (16.7 s), **byte-identical** |
| nl-a2-cgr-2032/cgr_clp_g4_compare_…_2041.py | 57c2693a… | 450ffdc0… | exit 0 (39 s), **byte-identical** |
| (2048 flux log 68357b21…) | — | — | **no script on disk**: the 2048 "log" is a hand-written summary of interactive runs (see fix A2-a) |
Originals unchanged: /workspace/nl-cand-1854/map_checks.py = 11e97edf… (as NL states).

PP exact scripts (new, additive, each with sidecar; filename times are labels, not run times):
- /workspace/pp-a2-exact-2026-11-09/pp_a2_frame_exact_2026-11-09_2120.py = 8a3e4c6c01c83b7f9f2d33b4bf794d82fe85d5cdedb583e35d5e4411e5e892e0, log 1e40f493ec4dda4415cc66d0e423128245f8ee8f27daf6797097b481f4992347 (component identity, exact; its flux line used a wrong push-forward constant 2/3 and is superseded by the next script).
- /workspace/pp-a2-exact-2026-11-09/pp_a2_flux_fix_2026-11-09_2124.py = 83772b5b77186cb4997c06dc224b85c2cce20cec8f051df40537c8acc913ea63, log 6b7e0663c03b277b00b725ae8d8a67ed0f7327ecce9a6c1f775b9b0c1cd1e744 (exact flux).
- Abandoned, kept unedited: pp_a2_exact_2026-11-09_2105.py (brute-force 11D sympy; killed, empty log e3b0c442…), pp_a2_flux_exact_2026-11-09_2118.py (timed out, empty log). Neither is used.

## 1. NL_DERIVED_F9_MAP_CHECKS_CONJUGATE_C2 (2006): **VERIFIED, 2/0/0/0 confirmed**
PP by hand. P₂ = diag(0,1). For U = [[a,b],[c,d]]: P₂Ū = [[0,0],[c̄,d̄]], UP₂ = [[0,b],[0,d]], so P₂Ū − UP₂ = [[0,−b],[c̄,d̄−d]] ✓. In SU(2), c = −b̄, d = ā; b = 0 forces c = 0, and d real with |d| = 1 gives d = ±1, so U = ±I ✓. For U(θ) = diag(e^{−iθ},e^{iθ}): P₂Ū(θ) − U(θ)P₂ = diag(0, e^{−iθ} − e^{iθ}) = diag(0, −2i sin θ) ✓, and P₂Ū(θ) − U(−θ)P₂ = 0 identically ✓. The condition T1(1⊗U) = (1⊗U)T1 for T1 = (A₀⊗P₂)∘K is P₂Ū = UP₂ ✓.
| item | NL | PP | reason |
|---|---|---|---|
| F9-cex | PROVED | **PROVED** | exact 2×2 algebra (by hand + sympy lines in the log) |
| F9-b | PROVED | **PROVED** | exact; commutant = centre ℤ₂; T1U(θ) = U(−θ)T1 |
Fix F9-1 (wording, no grade): T1 = (A₀⊗P₂)∘K has rank-deficient P₂, so it is **antilinear, not antiunitary**, and "T1⁻¹" is undefined. State the result as the intertwining T1U(θ) = U(−θ)T1 and drop "T1 U T1⁻¹" (or say "on the range of T1" with T1 restricted, as NL partly does). "Commutant" means the solution set of P₂Ū = UP₂.

## 2. NL_DERIVED_Y15_TRR2_PER_DIRECTION_NULL (2026): **VERIFIED numerically; one grade change; NL 3/5/1/0 → PP 2/6/1/0**
Rerun byte-identical. Recomputed: 1/3.493642e-3 = 286.2 and 1/1.746821e-3 = 572.5 ✓; u = 1 values are exactly half of u = 2 because c = 1/(8λ²) ∝ u ✓; L₇ = 2(π·4880)^{1/3} = 49.684382, L₇/g_c = 24.842191 ✓; κ² = 128π⁸ ✓. Both χ-branches agree, as an implication (R2-chi).
PP exact additions: on the unit round S⁴, Riem² = 2n(n−1) = 24, I(ê) = 2(n−1) = 6, ∫Riem² = 24·(8π²/3) = 64π² ✓. The UV integrated supply is **exactly −u M5 units**: c·64π²/T_M5 = [u/(16(2π)⁷)]·64π²·(2π)⁵ = u. The UV pointwise S_R = −24c/R₄⁴ ✓.
| item | NL | PP | reason |
|---|---|---|---|
| R2-round | PROVED | **PROVED** | analytic (above) |
| R2-Y16 | PROVED | **CONDITIONAL** | ∫Riem² = 1038.933973 and 3.2896 M5 units are float quadrature (n = 24 Gauss–Legendre). A float reproduction of a float number is still float-only. |
| R2-sign | COND | **COND** | float grid; ∇∇R and twist omitted |
| R2-IR | COND | **COND** | float; the 286 / 572 shortfalls hold on the n = 24 grid only |
| R2-warp | COND | **COND** | the "few-percent" bound 6max|H|²/max I = 0.0385 is an order estimate, not a proved inequality |
| R2-Σ | COND | **COND** | |
| R2-UV | COND | **COND** | uses |S_req| ≈ 2/(L₇κ²) (approximate k at the UV end); integrated −u is exact (PP) |
| R2-chi | PROVED | **PROVED (implication)** | face geometry independent of n(χ) on this face |
| R2-int | OPEN | **OPEN** | |
PP tally **2/6/1/0 = 9**.
Fixes: **T2-1** R2-Y16 → CONDITIONAL (float). **T2-2** R2-C4 carries "(PROVED, given K4 …)" in the text but is excluded from the tally; mark it "restatement of K4, no label" to avoid a hidden tenth row. **T2-3** "Smoothness … precludes a jump by 10² in the last 1% of Δ̃" is a heuristic, not a bound; either evaluate I at the X₁ pole analytically or say "not checked". **T2-4** Say that the UV |S_req| uses an approximate k. **T2-5** Optional: cite PP's exact −u for the integrated UV supply.

## 3. NL_DERIVED_Y15_NEC_ESCAPE_LIST_MN2 (2029): **VERIFIED; NL 5/3/3/1 confirmed; wording fixes; Z2 missing (file predates PP 0a82cf18)**
PP by hand:
- **E2-need.** NEC along t̂+ê: ρ + P_e ≥ 0 per direction; summing the 6 internal directions, τ = −ΣP_e/ρ ≤ 6. Required: ρ = 6k/κ², P_e = −8k/κ², so τ = 48/6 = 8 > 6 and ρ + P_e = −2k/κ² < 0 in each direction (= S(ℓ,ℓ) = −(2/κ²)(k_v − k_x)) ✓. L2: Σσ_i = ρ and Σp_iσ_i = −ΣP = 8ρ give Σ(p_i − 8)σ_i = 0; with p_i ≤ 6 and ρ > 0 some σ_i < 0 ✓.
- **E2-MO5.** Every 6D-worldvolume object filling ℝ^{1,3} has p = 2 internal directions; with thin-brane stress (ρ_i = σ_i, P = −σ_i along the worldvolume, 0 transverse), the internal trace is −2Σσ_i = −2ρ = −12 (units k/κ²) ≠ −48 for every choice of signs and smearings, since ρ ≠ 0. This is a **proof** that no such mix works, so the claim is REFUTED by proof (premise: the thin-brane stress form; worldvolume-flux stress belongs to E3) ✓.
- **E1-C4.** k_fib = −2k_x ≤ k_x ⇔ k_x ≥ 0; k_Σ = k_x ✓. At k_x = 0 all K vanish (a trivial face); a nontrivial face needs k_x > 0.
- **E6-sign.** Flipping the normal flips K: ρ = −6k/κ², P_e = +8k/κ², ρ + P_e = +2k/κ² ≥ 0. So NEC **holds**, and the obstruction is ρ < 0, which violates the **weak** energy condition, not NEC. In constituent form Σσ_i = −6k/κ² < 0, so some σ_i < 0 (reduces to E2) ✓.
| item | NL | PP | note |
|---|---|---|---|
| E1-IR | PROVED | **PROVED (impl.)** | given face.py k_x = −Δ̃^{−1/6}/L₅ |
| E1-C4 | PROVED | **PROVED** | algebra; not a solution |
| E1-ex | OPEN | **OPEN** | covers D6 (B12 D6) ✓ |
| E2-need | PROVED | **PROVED** | |
| E2-MO5 | REFUTED | **REFUTED** | by proof, given thin-brane stress |
| E2-obj | OPEN | **OPEN** | the hep-th/9603142 "no bare boundary cosmological term" is cited, not re-derived; it does not raise any grade here |
| E3-NEC | PROVED | **PROVED (impl. of L1)** | |
| E3-viol | OPEN | **OPEN** | |
| E4-HW | COND | **COND** | rests on the float file in §2 |
| E4-higher | COND | **COND** | power counting |
| E5-int | COND | **COND** | finite grid |
| E6-sign | PROVED | **PROVED** | wording fix N3-1 |
PP tally **5/3/3/1 = 12** (matches NL).
**Coverage of PP's open items:**
- **D6 (χ-dependent walls): covered** (E1-ex: "Finite-amplitude χ-dependent BPS walls remain OPEN (B12 D6)").
- **Z2 (w-creep flows into MN2 along the marginal w, PP 0a82cf18 / 1aa88a30 audit, 20:34): NOT covered.** E1-ex invokes B12 D3 for "every face of a W-flow in the CGR (φ,λ) sector", which does not reach non-W centre-manifold kept sides with w ≠ 0. The file (20:29) predates PP's Z2 (20:34), so this is not an error. **Erratum 20 should add Z2** to E1-ex / E5. (NL's Erratum 20, 2056, does add it as E20-6 in its register; that file is audited separately in FINDINGS_PP_AUDIT_NL_E20_AND_D6.)
Fixes: **N3-1** E6-sign: replace "σ < 0 or an equivalent NEC-violating ingredient" by "σ < 0 / negative energy density (a WEC violation; NEC itself holds on the UV-kept side)". **N3-2** E2-MO5: call it "refuted by the L3 trace argument (a proof)", not a counterexample, and state the thin-brane stress premise. **N3-3** E1-C4: note k_x = 0 is the trivial face; a nontrivial E1 realization needs k_x > 0. **N3-4** Add Z2 to E1-ex / E5 (via Erratum 20, as done in E20-6).

## 4. NL_DERIVED_A2_CGR_26_CLP_MN2_4FORM (2049): **PROVED EXACTLY by PP; NL 2/0/3/0 confirmed (now on exact grounds)**
NL's evidence was float (component match at ~8 points to 3.5e-15; Gauss–Legendre flux). On that basis alone both items would be CONDITIONAL. PP has now proved both symbolically.
**A2-comp, exact proof (pp_a2_frame_exact).** Use the coframe (du, dv, dα, dβ, Φ₁ = dφ₁ + du/v, dφ₂), a shear of determinant 1, so Hodge duals and orientation are unchanged. Since Dμ^{1,2} involve du only through Φ₁ (gA^{12}·μ shift), the 6D internal metric is block-diagonal in this coframe: D^{1/3}e^{6φ}/(g²v²)(du² + dv²) ⊕ H_{αβ} ⊕ diag(q₁, q₂). PP verified exactly that the off-block entries vanish, q₁ = conf₄μ₁²/X₁, q₂ = conf₄μ₂²/X₂, and det H = conf₄²·Δ·sin²α/(X₀X₁X₂) (this is NL's N9 fibre-determinant lemma, checked here as a polynomial identity). The CLP 7-form is dx^{01234}∧β with β = U_CLP vol₅vol_Σ du∧dv + λX₁^{−2}(⋆̄F¹)·d(μ₁²)∧Φ₁, so ⋆₁₁Ω = −(conf₇w₅)^{−5/2}⋆₆β exactly. With Δ = Y⁶, every component of CGR(2.6) + ⋆₁₁CLP(4.2) reduces to 0 modulo Y⁶ = Δ(α,β) and sin² + cos² = 1 (Gröbner remainder 0) on all four frame components, for **all** (z, v, u) and all angles in the fundamental domain α∈(0,π), β∈(0,π/2), φ_i free. Also U_CLP = g·U_CGR exactly, and the CGR (u,v,α,β) frame component vanishes identically.
**A2-flux, exact proof (pp_a2_flux_fix).** det[μ | ∂μ] = −sin³α sinβ cosβ (exact, φ-independent), so the fibre component is G = U Δ^{−2} sin³α sinβ cosβ / g³. Δ and U depend only on s = μ₁²: Δ = b − (b−a)s, U = 2(a²s + b²(1−s)) − Δ(2a+3b), with a = 2^{−3/5}, b = 2^{2/5}. Push-forward (by hand: t = cos²β, then s = (1−x²)t with x = cos α, giving ½∫_{−1}^{1}∫_0^{1−x²}F ds dx = ∫_0^1 F(s)√(1−s) ds) reduces the integral to ∫_0^1 U/Δ² √(1−s) ds; with u = √(1−s) the integrand is −4u²(u²+3)/(u²+1)², whose integral is exactly −2 (= −4[1 + π/4 − 2(π/8 + 1/4)]). Hence **∫_{S⁴}G₄(CGR) = (2π)²·(−2)/g³ = −8π²/g³ = −π² at g = 2, exactly**, and the CLP side is +8π²/g³ by A2-comp. PP also found the integral is −2 for every ratio k = X₀/X₁ on the X₀ = X₂ line (as expected of a closed form; T-independence).
| item | NL | PP | reason |
|---|---|---|---|
| A2-comp | PROVED | **PROVED (exact, PP)** | implication of the transcriptions of CGR (2.6) and CLP (4.2) as coded, λ_CLP = 1/8, and the √|g| Hodge convention; NL's float match alone would be COND |
| A2-flux | PROVED | **PROVED (exact, PP)** | signed value −8π²/g³ for CGR in the (α,β,φ₁,φ₂) orientation |
| A2-DT | OPEN | **OPEN** | |
| A2-S | OPEN | **OPEN** | |
| A2-offvac | OPEN | **OPEN** | |
PP tally **2/0/3/0 = 5**.
Fixes: **A2-a** The 2048 "log" (68357b21…) has no script on disk; it is a hand-written summary of interactive runs, so it is not reproducible. File the script, or cite PP's exact proof instead. **A2-b** Cite PP's exact proofs as the basis of both PROVED labels; the 3.5e-15 match and the 36×36 quadrature are float cross-checks only. **A2-c** State the flux with its sign and orientation: ∫G₄(CGR) = −8π²/g³ on (α,β,φ₁,φ₂) with β∈[0,π/2], not only "in magnitude". **A2-d** The 2035 and 2040 compile-failed drafts have no sidecars; add sidecars or say so. **A2-e** The 2041 .py sidecar was written at 20:49, after the 20:41 run; "frozen before execution" rests on the 20:40 mtime only — disclose as post-run sidecar.

## 5. Bookkeeping: E18 Addendum (2010) and Numbering note (2020): **FAITHFUL**
- The Addendum quotes PP c90b4fba (sha c90b4fba2339d758…, matches) correctly: Erratum 17 faithful to all 14 fixes; tallies 5/3/1/1, 7/10/2/1, 4/2/1/1; ST1 CONDITIONAL. The nit matches c90b4fba line 78 verbatim in substance: printed relΔ 2.063e-6, 5.044e-6 (5.043e-6 once), 8.741e-6, 1.328e-5; range 2.06e-6 – 1.33e-5. PP re-read st1_Nseq_…_1958.log (sha e98dd4f5…, as cited): values present on every face, one 5.043e-6 print ✓. E17 line 68 does say "2×10⁻⁶ to 1×10⁻⁵" ✓. PP rerun sha b38abc60… quoted correctly ✓.
- E18A-N13 is labelled PROVED as "a record check of the printed relΔ". PP accepts it as a record check (1/0/0/0). Optional: carry it as hygiene with no label, as the Numbering note does.
- Numbering note: af7a8199… (E18), eaef6139… (Addendum) and 92dded27… (Erratum 18-B12) all match their sidecars; the "next erratum is 19" statement matches what was filed (E19 2029, E20 2056) ✓. 0/0/0/0 ✓.
- Timestamps: PP c90b4fba 20:03:48 → E18 20:03:56 (8 s later; consistent with "filed before the confirmation arrived", since the relay reached NL later) → Addendum 20:10:31 → Erratum 18-B12 20:18:22 → Note 20:20:08. Consistent. Nits: **B-1** the Note's header says 20:19 but filename and mtime say 2020; **B-2** Erratum 18-B12 is named _2019 but written 20:18:22. No grade effect.

## 6. Summary
| file | NL | PP | verdict |
|---|---|---|---|
| F9 map (2006) | 2/0/0/0 | **2/0/0/0** | VERIFIED; wording fix F9-1 |
| tr R² per direction (2026) | 3/5/1/0 | **2/6/1/0** | R2-Y16 → COND (float); fixes T2-1..5 |
| NEC escape list (2029) | 5/3/3/1 | **5/3/3/1** | VERIFIED; fixes N3-1..4; Z2 to be added (done in E20-6) |
| A2 4-form (2049) | 2/0/3/0 | **2/0/3/0** | both PROVED, now exactly by PP; fixes A2-a..e |
| E18 Addendum (2010) | 1/0/0/0 | **1/0/0/0** | FAITHFUL |
| Numbering note (2020) | 0/0/0/0 | **0/0/0/0** | FAITHFUL; timestamp nits B-1, B-2 |
Junction UNSOLVED; count gap unchanged; nothing adopted. No CERT. Nothing sent.
Tip at write time: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (unchanged).
