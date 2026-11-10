# FINDINGS: PP audit of NL face-source templates (1711) and non-constant faces / localized M5s / O1 attempt (1713). 2026-11-09 (America/Chicago, CST)
Agent: Professor Proof (Soft SF). Additive file; nothing edited. No CERT. No message sent. Public arXiv source read only (hep-th/9903214; citations CONDITIONAL). No Gemini. LOCK 96f8d42e §4 not used. No MR2 numbers used. Convention G = ½T^(EH) (OW 2d1e877e). No vacuum adopted (HOLD aaadb280). b not fixed. O1 not declared.
Tip: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, re-hashed: **MATCH (untouched)**.

Targets:
- (1) NL_DERIVED_FACE_SOURCE_TEMPLATES_FIBRE_SIGMA_G4LEGS_2026-11-09_1711.md, sha 53096d433d062f51e0fc078d4bdd5faee333cbcf7edadd66c2a0b3fd4d2e7fb7 (= sidecar).
- (2) NL_DERIVED_JUNCTION_NONCONSTANT_FACE_LOCALIZED_M5_2026-11-09_1713.md, sha e2065e05c7d552117895351482cbb3838fcd651bb8873cd6398d0e35b12fd389 (= sidecar).
PP scratch: /workspace/audit-scratch/pp_facesrc_1720/ (every file has a .sha256 sidecar)
- pp_algebra.py 8b6ac993… / .log 2bbeca3e… (T0, B1 sign, A2 factor)
- pp_nonconst_K.py 16e613fe… / .log 0983da23…; pp_nonconst_K2.py c3f6e12b… / .log 5ffc41eb… (symbolic extrinsic curvature of graph faces)
- pp_dense.py 9c71b372… / .log b7580c71… (dense pointwise NEC, w, k_x−K, A2 factor)
- pp_nreq_mono.py 49a75166… / .log 4bcf94e2… (N_req monotonicity, quadrature bias)
- reruns of NL scripts: templates_rerun.log 67c7d2aa…, parity_rerun.log 9d408e5b…, dedup_rerun.log 09446574…, face_rerun.log 036955e7…
- clp/main.tex cbdaa9d1… (arXiv hep-th/9903214 source, CONDITIONAL citation)

## Rollup
PROVED 31 · CONDITIONAL 21 · OPEN 5 · REFUTED 4 · PENDING 0 (61 graded items).
- Headline 1: the constant-face no-go structure (T0, E1, B1 value, A1, AB1, NC2, NC3) is confirmed. The extra stress a pure-M5 Z₂ face needs violates the fibre NEC on the IR-kept side, so no positive-tension brane mix can supply it (PROVED at the end faces, CONDITIONAL in the interior on dense numerics, which I reproduced). N_b = 4880 has no solution (CONDITIONAL, numerical monotonicity of N_req confirmed).
- Headline 2: **NC1 is over-claimed.** It is PROVED (given J1, |z| ≤ 1) for faces r_b(μ). For faces that depend on a twisted angle φ_i, NL0's "Σ stays Lie-dragged" step is REFUTED by a symbolic counterexample, so that sub-class is OPEN and belongs in NC4.
- Headline 3: four wording/number errors (E4 "w_fib ≤ −1.2", B1 printed sign, 1713 tally row "8", PD4 "≥ 2.5×10⁻⁵") need additive fixes. None changes a conclusion.
- O1 stays **OPEN**. Both parity branches are reported correctly. No Owner record fixes the Z₂ action.

## 0. Integrity and authority
- **I1 [PROVED].** Both targets equal their sidecars. All 11 artifacts in /workspace/nl-junction-1705/ (face.py fd309c48…, flowlin.py b72d2296…, templates.py abe4a288…, templates.log = templates_full.log 67c7d2aa…, parity_lprime.py 48f25c60…, parity_lprime.log d8c83ccc…, parity_lprime_full.log 9d408e5b…, parity_interior.log 1d772126…, pointwise_p3b_dedup.py 9c7541ea…, pointwise_p3b_dedup.log 09446574…) equal their sidecars. Upstream NL 1655 (3cd6c8d3…) and erratum 5 (59218e61…) equal their sidecars. face.py and flowlin.py are byte-identical to the 1646 copies that PP audited in cb4d26b0.
- **I2 [PROVED].** parity_lprime.log = the first 6 lines of parity_lprime_full.log, and parity_interior.log = its last 5 lines (diff empty). NL's description is accurate.
- **I3 [PROVED].** Tip 7cddb188… MATCH (see header).
- **I4 [PROVED].** I re-ran templates.py, parity_lprime.py and pointwise_p3b_dedup.py from scratch copies. The outputs are **byte-identical** to templates_full.log (67c7d2aa…), parity_lprime_full.log (9d408e5b…) and pointwise_p3b_dedup.log (09446574…). face.py rerun reproduces the IR fixed-point N_req(x) = 12568.6 / 12252.1 / 12812.2 / 12942.4.
- **A-1 [PROVED]. OW 7b5a725b is on disk:** OWNER_WRITE_MAINCHAT_t4350_t4352_NL_SOURCE_TEMPLATES_XI_CURVE_NONCONSTANT_FACE_O1_OPEN_2026-11-09_1703.md, sha 7b5a725befe67c64a52878a348190a20cda891b8c0618e51a47820cd7c76010d = sidecar. It records the Owner's widget answers (t4350, t4352) and authorizes:
  - NL compute GO for (1) face stress-energy templates (fibre pressure, anisotropic Σ tension, G₄ legs), with the curvature deficit and b per source, and (2) non-constant-radius faces and localized M5s;
  - no source adopted; J7 OPEN; b OPEN; O1-dependent results given for both parities or marked CONDITIONAL;
  - Ξ := the curve 49a1⊗χ₁₄₀; O1 stays OPEN; the even-parity item of voice OW 1cb3b8d5 is WITHDRAWN;
  - HOLD aaadb280 and the 5f59e33e neutral items unchanged; tip untouched; no CERT; no Gemini.
- **A-2 [PROVED]. OW 9a8ced02 is on disk:** OWNER_WRITE_VOICE_9c8fa1db_t4355_O1_EVEN_PARITY_LOCK_ONLY_BY_DERIVATION_2026-11-09_1705.md, sha 9a8ced02a7053846d9f91c6600ad01e3c08673162045d5d910f5e4889c5757ba = sidecar. It authorizes nothing new to compute. It is a condition: even Z₂ parity of G₄ may be locked **only** by a derivation that PP has audited, never by declaration; until then O1 is OPEN, even parity is a CANDIDATE, and O1-dependent results are given for both parities or marked CONDITIONAL. It supersedes any reading of 1cb3b8d5 as selecting even parity. (1cb3b8d5 itself is still on disk, sha = sidecar, superseded.)
- **Compliance:** both NL files stay within A-1 and A-2: no source adopted, no vacuum adopted, b never fixed, both parities reported, neither parity declared.

## 1. File (1), templates (1711)
My algebra (pp_algebra.log) uses ρ = (2/κ²)(k_x − K), w_a = −(k_a − K)/(k_x − K), and NEC_a: ρ + P_a = (2/κ²)(k_x − k_a).
- **F1 T0 [PROVED given J1].** IR end (k_Σ = k_fib = 0, K = 4k_x): w_Σ = w_fib = −4/3. UV end (k_Σ = k_x, k_fib = 0, K = 6k_x): w_Σ = −1, w_fib = −6/5. These end values are z-independent. **The interior values are z-dependent and are not confined to the end-value interval:** dense pointwise scan (pp_dense.log) gives w_fib ∈ [−1.3421, −1.1687] (BBBW z=3) and [−1.3379, −1.1778] (z=2), and S⁴-averaged w_fib reaches −1.190. So "w_fib runs from −4/3 to −6/5" is correct only as endpoint values.
- **F2 E1 [PROVED].** At the end faces ρ + P_fib = (2/κ²)k_x < 0 (k_x < 0 on the IR-kept side), and ρ + P_Σ = (2/κ²)k_x < 0 at the IR end.
- **F3 E2 [CONDITIONAL, numerical; independently reproduced].** On 283/231/310/326 faces (MN2/MN1/z=2/z=3), R/R₀ ∈ [1.0005, ~2000], pointwise over the 120×60 S⁴ grid and all four fibre directions, max (ρ + P_fib)/|k_x| = −0.879 / −0.958 / −0.816 / −0.784 < 0. This matches NL's upper margin −0.78. The Σ NEC is also violated, tending to 0⁻ (max −1.2×10⁻⁷).
- **F4 E3 [CONDITIONAL; NL labels PROVED].** The UV-kept WEC violation uses k_x − K > 0, which is analytic only at the end faces (3|k_x|, 5|k_x|). In the interior it is numerical: my dense min of (k_x − K)/|k_x| is 3.0017 > 0. So E3 should be "PROVED at end faces, CONDITIONAL in the interior".
- **F5 E4 bound [PROVED].** For any static superposition of positive-tension branes (time in every worldvolume), T(k,k) = Σ σ_i(1 − |P_i e|²) ≥ 0 for every null k = t + e. This holds for aligned and tilted worldvolumes. Hence ρ + P_a ≥ 0 and w_a ≥ −1 in every direction. The same holds for any face source obeying the NEC (e.g. branes carrying worldvolume flux that obey the DEC). NL's definition ("M5, M2, wrapped in any directions, smeared or not", with P = −ρ_i along the worldvolume and 0 transverse) covers only aligned Nambu–Goto branes. It is adequate for the conclusion, but should be stated in the NEC form above.
- **F6 E4 sub-claim "required w_fib ≤ −1.2 in between" [REFUTED].** Counterexample at the same evidential level as the claim: NL's own templates_full.log gives averaged w_fib(φ₂) = −1.1925 (z=3, R/R₀ = 3) and −1.1956 (z=2, R/R₀ = 3). My pointwise maxima are −1.1687 / −1.1778, a margin of about 0.03, far above the grid quadrature error (~10⁻⁴). The conclusion survives because it rests on NEC (F3), not on the −1.2 bound.
- **F7 E4 conclusion [CONDITIONAL].** No brane mix can supply the IR-kept fibre stress: PROVED at the end faces, CONDITIONAL on F3 in the interior. NL's scope note says the same.
- **F8 A1 [PROVED].**
- **F9 A2, |z| ≤ 1 [PROVED given J1].** From face.py's rhs_r, which PP matched to B3W (A.15) in cb4d26b0 B2: g′ − f′ = −A₁ − A₂ = ⅛e^{f−2g}Q with Q = (1+z)e^{−2λ₁} + (1−z)e^{−2λ₂}. This is an exact sympy match to NL's formula, and Q > 0 for |z| ≤ 1.
- **F10 A2, z ∈ {2, 3} [CONDITIONAL, numerical].** NL's premise "λ₂ ≥ λ₁" is sufficient but not sharp. The sharp criterion for z > 1 is Q > 0 ⇔ λ₂ − λ₁ > ½ln((z−1)/(z+1)), which is −0.549 for z=2 and −0.347 for z=3. Numerically min Q = 2.000 along both flows, attained at the UV where λ → 0. z ≤ −1 follows by the 1↔2 mirror. Also, for g = 2, p + q = 2g − 2 = 2 (B3W, CONDITIONAL citation), so z ∈ ℤ and NL's gap 1 < z < 2 is empty.
  - The log line "min (g′−f′)/|f′| = 0.0000e+00", printed under the text "(>0 ⇒ …)", is a deep-UV underflow: e^{f−2g} → 0 as f, g → ∞. It is not a zero. The log should report min Q.
- **F11 A2 / NC1 for |z| ≥ 4 [OPEN].** There are no numerics. Not needed for the MR2/NL candidates.
- **F12 A3 [CONDITIONAL].** Agreed. It is analytic at the end faces.
- **F13 B1 value [PROVED].** σ_Σ^ex = (2/κ²)(k_Σ − k_x) = −ρ(1 + w_Σ) > 0. Positivity uses k_Σ − k_x = n^r(g′ − f′) > 0, so it inherits F9/F10's z scope.
- **F14 B1 as printed in 1711, "= ρ(w_Σ + 1)" [REFUTED, sign].** ρ(1 + w_Σ) − σ_Σ^ex = (4/κ²)(k_x − k_Σ) ≠ 0 (pp_algebra.log). §E of 1713 corrects it correctly. However, §E says "the first form" was mis-signed, when it was **the second form** (ρ(w_Σ+1)); the first form, (2/κ²)(k_Σ − k_x), was right. Conclusions B1–B3 are unchanged (PROVED).
- **F15 B2 [CONDITIONAL].** Agreed. The exact IR fixed-point face gives res_fib = 4.000 (face_rerun.log).
- **F16 B3 [PROVED].**
- **F17 AB1 [PROVED].** At constant r, K is diagonal in the horizontal frame: K(E_σ, ∂_φ) = 0 because the A-terms cancel. So fibre pressure in the μ-block eigenframe plus Σ tension closes every component.
- **F18 AB2 [CONDITIONAL, numerical; monotonicity confirmed].** Sorted in R/R₀, N_req(x) is strictly increasing on [1.0002, ~10⁶] for every candidate (600–770 faces each) and then saturates at roundoff (steps ~10⁻¹¹). So N_req is injective and b = N_req⁻¹(N_b) is unique where it exists.
  - Quadrature bias: the exact AdS₇ face gives 16268.5 on NL's grid vs. the analytic 10N/3 = 16266.7 (+1.1×10⁻⁴ relative). Grid values above 10N/3 near the UV are this bias, not non-monotonicity.
  - The range is (N_req^IR, 10N/3) ≈ (12.25k–12.94k, 16.27k), open at the UV end. N_b = 4880 has no solution.
- **F19 AB3 [CONDITIONAL].**
- **F20 G0 [CONDITIONAL on CLP].** I read arXiv hep-th/9903214, eq. s4f4red, i.e. (4.2). It gives **★F₄** (a 7-form), not F₄. NL's three leg types are correct as the legs of the 11D dual G₄:
  - (α) from the ε₇ terms;
  - (β) dr∧fib³, from ★̄dX_α∧d(μ_α²);
  - (γ) Σ²∧fib², from d(μ_i²)∧Dφ_i∧★̄F_i.
  - The metric in (4.1) matches face.py with g = 2.
- **F21 (β) = 0 ⇔ λ₁′ = λ₂′ = 0 [PROVED given CLP; PP].** Σ_α X_α⁻¹★̄dX_α∧d(μ_α²) = ★̄dr∧[(6λ₁′+4λ₂′)d(μ₁²) + (4λ₁′+6λ₂′)d(μ₂²)]. The coefficient matrix has determinant 20 ≠ 0.
- **F22 G1 [PROVED].** 2κ²T_M5 = (2π)³ℓ_P³ is consistent with face.py (κ² = 128π⁸, T_M5 = (2π)⁻⁵).
- **F23 G2-odd [CONDITIONAL].** The ratio N_req/(2N_flux) ∈ [1.255, 1.667] is arithmetic-correct and N-independent (N_req ∝ N).
- **F24 G2-even [CONDITIONAL].** Agreed.
- **F25 G3 [CONDITIONAL; NL labels PROVED].** It relies on F7 (interior numerics) and PD4 (numerics). Also, its odd-case ratio argument ignores the x tension carried by the (γ)-leg M5s that G2-odd itself requires (they wrap ℝ^{1,3}). Their normalization is OPEN (X2), so "no solution since ratio > 1" is not established. The fibre-NEC obstruction (F5/F7) is unaffected.
- **F26 1711 tally 11/10/4/0 [PROVED as bookkeeping].** Consistent with its own item list. PP's regrading is above.

## 2. File (2), non-constant faces / localized M5 / O1 (1713)
I computed K_ab = ∇_a n_b symbolically for graph faces in a 6D model metric that keeps every structure NL uses: Killing x; warps c_a(r, μ); Σ = H²; one fibre angle μ; one circle φ twisted by A = q ds₁/s₂ (F ∝ vol_Σ). See pp_nonconst_K*.log.
- **N1 NL0 for faces independent of twisted φ [PROVED].** Normal, induced-metric tilt and the Lie-drag formula k_a = ½n(ln c_a) hold for x, for φ when the face depends only on σ, and for x and Σ when the face depends only on μ. Symbolic residuals are 0.
- **N2 NL0 bullet "x and Σ stay Lie-dragged" for faces depending on a twisted φ [REFUTED, counterexample].** For r = P(μ, φ), the face-tangent horizontal lift of ∂_{s₁} is F₁ = ∂_{s₁} − A_{s₁}(∂_φ + P_φ∂_r). Then K(F₁,F₁)/h − ½n(ln c_Σ) ∝ q²c_φ[2c_Σc_rc_μP_φφ + O(P_φ²)] ≠ 0, and K(F₁,F₂) ∝ qP_φ ≠ 0. At a point with P_φ = 0 and P_φφ ≠ 0 the residual is nonzero for any warps. So NL's justification "F_i(n,∂_φ) = 0" does not make Σ Lie-dragged.
  - Global point: on a circle with F_i ≠ 0, a face that "depends only on fibre coordinates" in the gauge-covariant sense (horizontal derivative D_σr_b = 0) must have ∂_{φ_i}r_b = 0, by integrability (F∂_φ r_b = 0). So the twisted-φ-dependent class is really a mixed (σ, φ) class.
- **N3 NC1 for r_b(μ), |z| ≤ 1 [PROVED given J1].** With P_φ = 0 every residual vanishes. k_Σ − k_x = n^r(g′ − f′) > 0, so worldvolume isotropy fails. The extension to φ_j-dependence is valid only for circles with F_j = 0.
- **N4 NC1 for r_b(μ), z ∈ {2, 3} [CONDITIONAL, numerical].** As in F10.
- **N5 NC1 for faces depending on a twisted φ_i [OPEN].** Move to NC4. Partial lead, not adopted: in a local axial gauge (A_{s₂} = 0), the ∂_{s₂} direction is horizontal, tangent and orthogonal to the fibre, and K(∂_{s₂},∂_{s₂})/h = ½n(ln c_Σ) exactly (symbolic residual 0). That still forces g′ = f′ locally, but this holds only for faces that are σ-independent in such a gauge, which is a gauge-dependent and non-global class.
- **N6 NC2 [PROVED given J1, every real z].** For r = R(σ): K(x,x)/h, K(φ,φ)/h and K(μ,μ)/h each equal ½n^r∂_r ln c_a (symbolic residual 0), and n^μ = 0. The gradient and Hessian of r_b enter only the Σ block and the Σ–fibre off-diagonals. So the PP lemma (fibre entries = K, k_wv = k_x, K = −2k_x) gives k_{φ_i} + 2k_x = n^r(2f′ − λ_i′) = 0 pointwise. Then λ₁′ = λ₂′ = 2f′, which contradicts (A.15) for z ≥ −1 (eq3) and for z ≤ 1 (eq4). The reduction is valid. The NC2 class (φ-independent) is gauge-invariant and globally defined.
- **N7 NC2 second obstruction [PROVED].** K(∂_φ, E_σ) ∝ q c_φ ∂_σR ≠ 0 wherever ∇_Σ r_b ≠ 0 and F ≠ 0 (symbolic). This agrees with NL's ½c_φgF_i(n, E_σ) up to normalization. For MN2 it applies to i = 1 only.
- **N8 NC3 [PROVED].** The Israel stress is G₄-free (G1), and the conditions are homogeneous, so the result is independent of N_b and of the O1 branch.
- **N9 NC4 [OPEN].** Agreed, now including N5. Remark: on mixed (σ, μ) faces the identity picks up n^μ∂_μ ln μ_i, so the NC2 argument does not carry over automatically.
- **N10 L1 algebra [PROVED].** For H = R³/ρ³, a tube ρ = const has k_wv = 1/(2R) = 1/L₇ and k_Ω = 0, so K = 6k_wv.
- **N11 L1 interpretation [CONDITIONAL].** A tube around a localized stack is not the junction face: the stack sits inside the face at codimension 4. "Localization reproduces the AdS₇ end, so no pure-M5 face" is heuristic.
- **N12 L2 [CONDITIONAL].** Agreed.
- **N13 L3 [PROVED given Bianchi and P3].** Odd: N_b = 2N_flux; even: net N_b = 0. Both branches are given.
- **N14 L4 "δN_req = 0 at linear order" [CONDITIONAL].** The label is right, but the premise is understated. dvol₄ is Δ̃-warped and the S⁴ is squashed, so round-S⁴ ℓ ≥ 1 harmonics are not orthogonal to constants under the measure used in N_req. Also, (localized − smeared) is an O(1) δ-function difference, so "linear order" needs a named small parameter.
- **N15 L5 [CONDITIONAL].** **N16 L6 [CONDITIONAL].** **N17 L7 [OPEN].** Agreed.
- **N18 PD1 [PROVED given σ a symmetry of 11D sugra].** Φ(r′) = s₁₁s₄Φ(r) with s₁₁ = s_r s_x s_Σ s₄ and s_r = −1. So Φ is odd ⇔ s_x s_Σ = +1. This is consistent with PD2: a worldvolume-orientation-preserving σ maps an M5 to an M5 (net charge allowed), and a reversing σ maps an M5 to an anti-M5 (net charge 0).
  - Leg parities: with (α) even, (β) is odd (one dr) and (γ) is even, for either way of realizing s_x s_Σ = −1 (with compensating φ_i → −φ_i when Σ is reversed). Both branches are reported correctly in G2-odd/G2-even, L3, PD2 and PD4.
- **N19 PD2 [PROVED].** **N20 PD3 [CONDITIONAL].** Agreed; it does not lock a parity.
- **N21 PD4 [CONDITIONAL, numerical].** The logic is right (with N21's (β) ⇔ λ′ step = F21). The quoted bound "≥ 2.5×10⁻⁵" is wrong: parity_lprime_full.log gives 2.4826×10⁻⁵ for z = 0. 1711's "> 2×10⁻⁵" is right. Also, the minima sit at the window edge R/R₀ ≈ 98–99 (decay toward the UV), and the sign-change test covers only R/R₀ ≤ 100.
- **N22 PD5 [PROVED].**
- **N23 O1 [OPEN].** No Owner record on disk fixes σ's action on (x, Σ, S⁴), and no derivation forcing a parity is on record. Per OW 9a8ced02 even parity remains a CANDIDATE, and odd is not PROVED. NL complies.
- **N24 §D fix 1 [PROVED].** "z ≥ −1" (eq3) and "z ≤ 1" (eq4) are applied, in §D and in NC2.
- **N25 §D fix 2 [PROVED].** Gauge h = f is stated; λ′ = 2f′ is reparametrization- and normal-orientation-invariant; E > 0 is not used.
- **N26 §D fix 3 [PROVED].** The original pointwise_p3b.py (577c1946…) dropped both terminal points and concatenated without unique, so only the shared start point r = 1 was duplicated (3537→3536, 3428→3427, 3561→3560, 3580→3579). The minima 1.8934/1.9873/1.8481/1.8248 (λ₁) and 2.0000/1.9873/2.0000/2.0000 (λ₂) are unchanged. The rerun is byte-identical. **PP retracts the "double-counted" wording of its own C3 (cb4d26b0):** exactly one duplicate existed.
- **N27 D4 [CONDITIONAL].** Agreed.
- **N28 §E correction [PROVED, value].** The value is right; the misattribution is noted in F14.
- **N29 1713 tally row "PROVED | 8" [REFUTED as printed].** The row lists 9 names (NL0, NC1 |z|≤1, NC2, NC3, L1, L3, PD1, PD2, PD5). NL's own note gives 9, and the correct NL tally is **9/9/4/0**. With PP's regrading (N2/N5 split, N11), the PP counts above supersede it.

## Fixes NL needs (additive erratum only; no conclusion changes)
1. 1713 tally row: change PROVED "8" to "9" (9/9/4/0).
2. 1713 §E: say the **second** form, ρ(w_Σ + 1), had the wrong sign. The first form, (2/κ²)(k_Σ − k_x), was correct.
3. 1711 E4: drop "required w_fib ≤ −1.2 in between" (counterexample: −1.1925 in NL's log; −1.1687 pointwise). Restate as: any NEC-satisfying face source (every static positive-tension brane superposition, aligned or tilted, including DEC-obeying worldvolume flux) has ρ + P_a ≥ 0, while the required stress has ρ + P_fib < 0 (E1 at the ends, E2 inside). Define "brane mix" that way.
4. 1711 T0 and §3: label "−4/3 → −1" and "−4/3 → −6/5" as endpoint values. State that the interior is z-dependent and non-monotone (pointwise w_fib ∈ [−1.342, −1.169] for BBBW).
5. Relabel E3 and G3 as "PROVED at end faces, CONDITIONAL in interior". In G3/G2-odd, either include the x tension of the (γ)-leg M5s in the x equation, or make the "ratio > 1 ⇒ no solution" step CONDITIONAL on X2.
6. NC1 / NL0: restrict the PROVED claim to r_b(μ), plus φ_j-dependence only on circles with F_j = 0. Withdraw the Lie-drag bullet for twisted-φ faces (PP counterexample N2) and move those faces to NC4. Optionally file the axial-gauge kernel-direction argument (N5) with its gauge and global caveat.
7. A2 / NC1 z range: replace "λ₂ ≥ λ₁" by the sharp criterion λ₂ − λ₁ > ½ln((z−1)/(z+1)) for z > 1 (mirror for z < −1). Note that z ∈ ℤ for g = 2 (p + q = 2), and that the numerics cover only z = 2, 3 (|z| ≥ 4 OPEN). In templates.py/log, report min Q (= 2.000) instead of min (g′−f′)/|f′|, which underflows to 0.
8. 1713 PD4: change "≥ 2.5×10⁻⁵" to "> 2×10⁻⁵" (log min 2.4826×10⁻⁵, z = 0). Note that the minimum sits at the R/R₀ = 100 window edge and that sign changes are tested only up to R/R₀ = 100.
9. 1711 G0: state that CLP (4.2) gives ★F₄ and that the listed legs belong to its 11D dual. Add the (β) = 0 ⇔ λ₁′ = λ₂′ = 0 step (coefficients [[6,4],[4,6]], det 20).
10. AB2: quote N_req to 4 significant figures, or with the grid bias (+1.86 at the exact AdS₇ face, i.e. 1.1×10⁻⁴). Make the interval open at the UV end, and cite monotonicity on R/R₀ ∈ [1.0002, ~10⁶].
11. L1 and L4: mark L1's interpretation CONDITIONAL (a tube around the stack is not the junction face). In L4, state the premise as orthogonality of (localized − smeared) to the Δ̃-warped dvol₄ measure, and name the expansion parameter.

Tip 7cddb188 untouched (MATCH). No CERT. No message sent. Nothing adopted.
