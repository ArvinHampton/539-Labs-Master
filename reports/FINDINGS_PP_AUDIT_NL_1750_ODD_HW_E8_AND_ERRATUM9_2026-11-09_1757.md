# FINDINGS: PP audit of NL 1750 (odd HW wall: μ-dependent and time-dependent faces, localization, E₈ sector) and NL erratum 9 (O1 wording). 2026-11-09 (America/Chicago, CST)
Agent: Professor Proof (Soft SF). Additive new file; nothing edited. No CERT. No message sent. Nothing adopted. Only public arXiv API metadata was read (citations CONDITIONAL). No Gemini. Lock 96f8d42e §4 not used. HOLD 587eca0c / aaadb280 unchanged. b not fixed.
Tip: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, re-hashed: **MATCH (untouched)**.
Depends on: PP FINDINGS_PP_AUDIT_NL_ERRATUM7_AND_1736_NOGOS_2026-11-09_1753.md (7f0ce656…) and its rollup erratum (724325dd…), the "§B verdict"; also PP 1bd92da7 (erratum 8 / OW f825dfff).
Convention: K_ab = e_a^M e_b^N ∇_M n_N; ρ = (2/κ²)(k_x − K) (NL/1711).

Targets:
- (1) NL_DERIVED_ODD_HW_WALL_E8_MU_TIME_LOCALIZATION_2026-11-09_1750.md, sha 4d9c9951eedc43b359d63842ad1535084b43bf893eca3125a4c7b06c0014468a (= sidecar).
- (2) NL_ERRATUM9_O1_WORDING_ACCEPT_PP_1bd92da7_2026-11-09_1750.md, sha 76ec4e75d73c12700c038b8eb00d047df85148f789c3f9d2d375ad50890aba1f (= sidecar).
PP scratch: /workspace/audit-scratch/pp_1750_audit/ (sidecars written)
- checks_rerun.log 22fb858c… (rerun of NL checks.py; byte-identical to checks_1750.log)
- arxiv_pp.xml 87991921… (PP's own arXiv API fetch; byte-identical to NL's arxiv_raw.xml)
- pp_ym_checks.py 9733f505… / .log d14aa421… (SD identity, traceless fibre stress, Bogomolny). Note: the log's parenthetical "T00 zero iff SD or ASD" is loose. The **full** fibre block vanishes iff F is SD or ASD; T00 alone vanishes on a larger set.

## Rollup
PROVED 22 · CONDITIONAL 16 · OPEN 4 · REFUTED 0 · PENDING 0 (42 graded items).
- **μ-dependent static faces (K1/K2): PROVED for MN2 and MN1, CONDITIONAL for BBBW z = 2 and also z = 3** (both rest on min Q = 2.0000; NL omitted z = 3). This holds for any face independent of σ, of every twisted φ, and of at least one x^α or t; no minimum is needed. The "or" in the relay is a conjunction: σ AND twisted φ AND one x.
- **Faces with σ or twisted-φ dependence (K4):** the B2 dependence is now discharged (PP §B verdict: B2 PROVED given J1, every z, for static C² faces attaining a global minimum). K4 stays CONDITIONAL, on uniform C² bounds for x-translates and on inf r_b staying away from the throat r*.
- **Time-dependent faces:** T2 PROVED for every z; T1 PROVED for MN2/MN1 and CONDITIONAL for z = 2, 3; full x or t dependence OPEN (T3). Agreed.
- **Localization:** the NEC ⇒ k_t ≥ k_a algebra is PROVED. "Backreaction must reverse the sign, an O(1) change" is CONDITIONAL, because it is shown only for constant-r faces and their neighbours. "Every admissible source obeys the NEC" is CONDITIONAL on dropping the HW wall's tr R² term. The bound is OPEN.
- **E₈:** the YM NEC (E2) is PROVED, and the self-dual-instanton stress = smeared-M5 tension (E3) is PROVED; I checked it on the 10D wall, with the wv block (t, x, Σ) carrying P = −ρ, the fibre block 0, and mixed terms 0. The BPS count gap [1.255, 1.667) is unchanged (CONDITIONAL). Only non-BPS E₈ energy could close the count gap (OPEN), and never the fibre-NEC deficit.
- **Six arXiv citations: titles and authors match** (independent fetch). Content remains CONDITIONAL.
- **Erratum 9: all 4 PP wording fixes applied.** Fix 4 holds: no NL file cites "odd case only" as Owner text, and the 1750 header attributes it to Physicist's 17:46 relay. Tally 1/3/1/0 is correct.
- Tallies: 1750's 10/13/4/0 = 27 matches its item lists.

## 0. Integrity and authority
- **I1 [PROVED].** Both targets equal their sidecars. /workspace/nl-junction-1746/: checks.py 648f0763…, checks_1750.log 22fb858c…, arxiv_titles_1747.txt 039c8be2…, arxiv_raw.xml 87991921… all equal their sidecars. PP 1bd92da7… equals its sidecar.
- **I2 [PROVED].** checks.py rerun from a scratch copy is byte-identical to checks_1750.log. The sympy Σ-lift residual is 0, max|T| for SD is 1.8×10⁻¹⁵, and min T(k,k) is 2.567 > 0.
- **I3 [PROVED].** Tip MATCH.
- **I4 [PROVED].** OW f825dfff is on disk, sha f825dfffb8cd17a7… = sidecar. Owner words: "As mine: the face is a Z2 fixed plane (Horava-Witten-type wall); G4 parity odd per PP 544fc7b0, with an E8 wall sector CONDITIONAL." It contains **no NL assignment**. 1750 states this correctly (header lines 4–5) and attributes "odd case only / drop the even branch" to Physicist's 17:46 relay, not to Owner text. `rg` over NL_* files finds no Owner attribution of it anywhere. 1750's statements of O1 odd (CONDITIONAL on P-b), E₈/n_inst CONDITIONAL and N_M5 + n_inst = 2N_flux match the record.
- **I5 [PROVED, title level].** PP's own export.arxiv.org fetch (byte-identical to NL's raw XML) gives: hep-th/9510209 Hořava–Witten "Heterotic and Type I String Dynamics from Eleven Dimensions"; hep-th/9603142 Hořava–Witten "Eleven-Dimensional Supergravity on a Manifold with Boundary"; hep-th/9602120 Ganor–Hanany "Small E₈ Instantons and Tensionless Non-critical Strings"; hep-th/9603003 Seiberg–Witten "Comments on String Dynamics in Six Dimensions"; hep-th/9803205 Freed–Harvey–Minasian–Moore "Gravitational Anomaly Cancellation for M-Theory Fivebranes"; 1404.3887 Ohmori–Shimizu–Tachikawa "Anomaly polynomial of E-string theories". All six match 1750 §4. Contents are CONDITIONAL.

## 1. μ-dependent static faces
- **K1 [PROVED].** H² isometries ξ preserve ds²_Σ and F = vol, so A → A + dΛ_ξ. The lift ξ̃ = ξ + Λ_ξ∂_φ is an 11D Killing field (Δ̃ and the X's are Σ-independent). η = ξ̃ + const·∂_φ is Killing and equals the horizontal lift F at p. It is tangent wherever the face is independent of σ and of the twisted φ's, so B0b applies. n(|η|²) at p = |ξ|² n(c_Σ), because the c_φ(·)² correction vanishes to second order at p and n has no Σ legs. So K(F̂,F̂) = ½n(ln c_Σ). NL's sympy check on P(x, μ) uses the upper-half-plane translation lift, residual 0. This is consistent with PP N2: K1 excludes dependence on twisted φ.
- **K2a [PROVED given J1; MN2 z = 1, MN1 z = 0].** B0a gives K(F̂,F̂) = K(x̂_α,x̂_α); both are Killing, so n(ln c_Σ/c_x) = 0, and c_Σ/c_x = e^{2(g−f)} (Δ̃^{1/3} cancels) gives 2n^r(g′ − f′) = 0. This contradicts Q > 0, which is analytic for |z| ≤ 1. For static faces x̂_α can be t̂, so only σ- and twisted-φ independence are needed. μ and untwisted-φ (MN2: φ₂) dependence are free, and no minimum is needed.
- **K2b [CONDITIONAL; z = 2].** min Q = 2.0000 (resolve_1736.log).
- **K2c [CONDITIONAL; z = 3, PP addition].** The same log gives min Q = 2.0000 for z = 3, so z = 3 has the same status as z = 2. NL's §1/§5 and title omit z = 3; z ≤ −2 follows by mirror; |z| ≥ 4 OPEN.
- **K4 [CONDITIONAL].** With PP's §B verdict, the B2 input is PROVED: any static C² face attaining a global minimum of r has no solution, every z, without needing compactness once the minimum is attained. The translate-and-limit argument is sound in outline: x-translations are isometries, and the limit face attains inf r. It remains CONDITIONAL on (i) uniform C² (in fact C^{2,α}) bounds for the translates, and (ii) inf r_b > r*, so the limit lies in the regular flow region. Both are NL's K5.
- **K5 [OPEN].** Agreed.

## 2. Time-dependent faces
- **T1a [PROVED given J1; MN2, MN1].** The K2 argument goes through with spatial ∂_{x^α}. B0a still holds for moving branes (Nambu–Goto stress −σh^{wv} on the face lift); W⊥∂_φ survives because the t-lift ∂_t + ṙ_b∂_r ⊥ ∂_φ; n^r ≠ 0 for a timelike graph.
- **T1b [CONDITIONAL; z = 2 and z = 3].** Q numerics, as K2b/K2c.
- **T2 [PROVED given J1, every real z].** ∂_{φ_i} ∈ W⊥ and ∂_{x^α} ∈ W are tangent Killing fields; n^μ = 0; the c's are t-independent. So n^r(2f′ − λ_i′) = 0 contradicts B0d-1 (PP §B: PROVED, i = 1 for z ≥ −1, i = 2 for z ≤ 1).
- **T3 [OPEN].** Agreed.

## 3. Localization
- **L1 [PROVED].** As 1736 D1, with zero stress meaning no M5 and no E₈ stress.
- **L2-const [PROVED given J1, every real z].** "Flow faces" here means the constant-r faces. Via B0d, k_{φ_i} + 2k_x = n^r(2f′ − λ_i′) ≠ 0, so the z = 2 split (L2b) is unnecessary: L2b upgrades to PROVED by this route. For general faces, pointwise total geodesy is possible (PP §B, D2-general counterexample), so the statement must stay restricted to constant faces.
- **L2-inference [CONDITIONAL].** "Any localized configuration is an O(1) deformation" is heuristic beyond constant faces. "A perturbative bound does not exist" is not proved; it should read "no perturbative bound is available".
- **L3-alg [PROVED].** For a static face, S(k,k) = −(2/κ²)K(k,k) for a face-null k = t̂ + ê, and K(t̂,ê) = 0 (static). So NEC ⇔ K(ê,ê) ≤ k_t := −K(t̂,t̂) for every unit spatial ê. The file's "k_x ≥ k_a" is this with k_t = k_x, which holds for Poincaré-invariant faces; for general faces read k_t.
- **L3-sources [CONDITIONAL].** M5s in any orientation obey the NEC (erratum 7 fix 3 / PP F5), and E₈ YM does too (E2). But the HW wall action also carries the −½tr R² term at the same order in κ^{2/3} as tr F². That curvature-squared wall stress is not NEC-guaranteed. "All admissible sources obey the NEC" is therefore CONDITIONAL on neglecting it; it is subleading in ℓ_P/L, but this should be stated.
- **L3-conclusion [CONDITIONAL].** The constant-r flow faces violate the fibre NEC (1711 E1 at the end faces PROVED; E2 interior CONDITIONAL). That backreaction "must" reverse the sign of k_x − k_fib, an O(1) change, follows for faces C¹-close to constant slices, given the margin of −0.78 to −1.28 |k_x|. Non-constant faces in the unbackreacted geometry have free spatial Hessians and are not excluded by the NEC alone; they are excluded, where they are, by the pure-M5 Israel system (§B, K2, T2), not by L3.
- **L4 [CONDITIONAL].** Agreed. The charge side is N_M5 + n_inst = 2N_flux.
- **L5 [OPEN].** Agreed.

## 4. E₈ wall sector
- **E0 [CONDITIONAL, HW 9603142].** Agreed (λ² ∝ κ^{4/3}; no bare wall tension at leading order).
- **E1 [CONDITIONAL, HW]** 2N_flux = N_M5 + n_inst. **E1-p₁ [PROVED].** TW|_{S⁴} = TS⁴ ⊕ (trivial normal bundle of a fibre). p₁(TS⁴) = 0 because TS⁴ ⊕ ℝ = Tℝ⁵|_{S⁴}. ∫_{S⁴}tr R∧R is a characteristic number, independent of the warped or squashed connection, so it vanishes.
- **E2 [PROVED].** T(k,k) = Σ_A |F^A(k,·)|² with F(k,k) = 0, so F(k,·) ⊥ k is spacelike or null, and the norm is ≥ 0 (positive-definite Killing form normalization). **E2-end [PROVED given J1]:** cannot cure ρ + P_fib < 0 at the end faces. **E2-int [CONDITIONAL]:** relies on 1711 E2 numerics.
- **E3 [PROVED].** Checked on the 10D wall for an E₈ field with legs only on the 4D fibre, self-dual with respect to the induced (warped, squashed) fibre metric. Fibre block: F Fᵀ − ¼|F|²𝟙₄ = 0 identically (pp_ym_checks.log (a), symbolic). Mixed wv–fibre block: 0, since there are no wv legs. wv block on (t, x¹–x³, Σ²): T_μν = −¼|F|²h_μν, so ρ = ¼|F|², P_wv = −ρ, P_fib = 0. This is exactly the stress of M5s smeared over the fibre and wrapping (t, x, Σ), the same directions as the face M5 stack. Caveat: this needs the field to vary only along the fibre; Σ- or x-dependence adds wv legs.
- **E4 [CONDITIONAL, GH/SW + HW normalization].** Agreed: the count gap N_req/(2N_flux) is unchanged by n_inst. Minor: flow faces have R/R₀ > 1, so the range should be (1.255, 1.667), open at both ends (cf. PP §B fix 12).
- **E5 [CONDITIONAL].** The Bogomolny inequality itself is PROVED (|F|² − |F·⋆F| = sum of squares, pp_ym_checks.log), and the 25.5–66.7% excess is arithmetic-correct. But a non-self-dual field has a **nonzero, traceless** fibre stress (pp_ym_checks.log (b)). It therefore enters the fibre Israel equations as well as the x equation, so "could close the count gap" must also be checked against the fibre equations. "Never the junction" is right: the stress obeys the NEC (E2).
- **E5x [OPEN].** Agreed.
- **E6 [CONDITIONAL, FHMM/OST].** **E7 [CONDITIONAL, HW].** Agreed. E7 shares L3's tr R² caveat.
- **E-verdict [CONDITIONAL].** Agreed: PROVED at the end faces, CONDITIONAL in the interior; the count gap is not changed by BPS instantons.

## 5. Tallies
- **T-1750 [PROVED, bookkeeping].** PROVED 10 (K1, K2a, T1a, T2, L1, L2a, L3, E2, E2-end, E3), CONDITIONAL 13, OPEN 4, REFUTED 0: 27 ✓, matching the header. PP's regrading above supersedes it: L3 is split, L2b can be PROVED, and K2c (z = 3) is added.

## 6. Erratum 9 (vs PP 1bd92da7 N1–N4)
- **EF1 [PROVED, applied].** N1: "2N_flux on the covering space"; the per-fundamental-domain charge on face/τ is not stated (CONDITIONAL).
- **EF2 [PROVED, applied].** N2: domain = fibration-preserving τ with s₄ cancelling (8/8); mixing τ OPEN; time-reversal caveat CONDITIONAL.
- **EF3 [PROVED, applied].** N3: τ = id per f825dfff; O1 odd CONDITIONAL on P-b; E₈/n_inst CONDITIONAL; N_M5 + n_inst = 2N_flux; the erratum 8 O1-lock and τ-choice items are superseded; the P-nofix items are off-premise; framed as an alignment, not an error. ("Defined τ = id" is the derived equivalent of the Owner's "Z₂ fixed plane", as in PP N3.)
- **EF4 [PROVED, applied].** N4: no NL file (1750, erratum 8, erratum 9) cites "odd case only" as Owner text. 1750 attributes it to Physicist's 17:46 relay.
- **ET [PROVED].** Tally 1/3/1/0 = 5 matches PP's grades (S1 PROVED; N1, S3, W5 CONDITIONAL; S2 OPEN). Treating fix 4 as an untallied attribution note is acceptable.

## NL fixes (additive erratum only; none reverses a conclusion)
1. Add BBBW **z = 3** to K2 and T1 as CONDITIONAL (min Q = 2.0000 in resolve_1736.log), and z ≤ −2 by mirror; |z| ≥ 4 OPEN. The title and §5 list z = 2 only.
2. K2: state the hypothesis as a conjunction (independent of σ AND of every twisted φ AND of at least one x^α or t). For static faces, t serves.
3. K4: record that the B2 input is now PROVED (PP 7f0ce656). K4 stays CONDITIONAL only on uniform C^{2,α} bounds for x-translates and on inf r_b > r* (K5).
4. L2: restrict "flow faces nowhere totally geodesic" to constant-r faces and use k_{φ_i} + 2k_x = n^r(2f′ − λ_i′) ≠ 0 (B0d), which makes L2b PROVED for every z. Replace "a perturbative bound does not exist" with "no perturbative bound is available". Label the O(1)-deformation inference CONDITIONAL.
5. L3: write the NEC condition as K(ê,ê) ≤ k_t = −K(t̂,t̂), which equals k_x only for Poincaré-invariant faces. Mark "all admissible sources obey the NEC" CONDITIONAL on neglecting the HW wall tr R² term. Mark "backreaction must reverse the sign (O(1))" CONDITIONAL: it is shown only for faces near constant slices.
6. E3: state that the instanton varies only along the fibre and is self-dual with respect to the induced fibre metric; Σ- or x-dependence adds wv legs.
7. E4: range (1.255, 1.667), open at both ends.
8. E5: note that non-self-dual fields carry a nonzero, traceless fibre stress, which enters the fibre Israel equations. "Could close the count gap" must be checked against those as well.
9. Header line 9: the §B–§D audit is now filed (PP 7f0ce656 + rollup erratum 724325dd); update the dependence labels accordingly.

Tip 7cddb188 untouched (MATCH). No CERT. No message sent. Nothing adopted.
