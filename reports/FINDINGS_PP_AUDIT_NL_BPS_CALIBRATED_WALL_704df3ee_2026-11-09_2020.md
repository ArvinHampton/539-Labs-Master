# FINDINGS — PP audit of NL_DERIVED_BPS_CALIBRATED_WALL_MN2_2026-11-09_2007.md (704df3ee…) — 2026-11-09 20:20 CST (America/Chicago)
Auditor: Professor Proof (PP), Soft SF audit agent. Pure math. Labels PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. Float-only results are CONDITIONAL. A citation alone never makes a result PROVED (OW 3f160803 + 36683379). Authority: OW d5eaeef3 ("Pursue all open", NL item 1); OW b0b9ae7f (lanes propose, PP grades). **Nothing adopted. Junction: UNSOLVED.** No CERT, no sends, no Gemini. New file only; nothing edited. Nomenclature per OW 81b74a31 ("resonant algebra"); not used here.
Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 at start and at write time (unchanged).
Context read: PP 077e417d (Y14s2/Y15), PP 99593076 (K-counting, K6′, C6), PP §1.1 v2 clarification (…GARBLED_LINES_…_1958), MR2 aeb9ab13 + PP audits (L3: Σ|σ_neg| ≥ ρ_w/3).
"PROVED" below for derivations from CGR (arXiv 1906.08900) means: exact derivation from CGR (2.5), (3.1), (3.3), (3.8) taken as inputs, as in PP's K1/Y15 practice; MN2 (6.1)/(6.2) re-derived from (3.8) as a transcription check.

## 0. Integrity and reruns
| file | sha256 | sidecar | mtime (CST) |
|---|---|---|---|
| NL_DERIVED_BPS_CALIBRATED_WALL_MN2_2026-11-09_2007.md | 704df3ee0315f8b4a5ec7831c53a8593102e7773801bbcfcafc1ce175f7e9182 | MATCH | 20:08:23 |
| w_superpotential.py / .log | a392d53b… / a7c88fe3… | MATCH / MATCH | 20:03:11 / 20:03:12 |
| bps_wall_faces.py / .log | 96916231… / 8de6c3c6… | MATCH / MATCH | 20:06:32 / 20:06:33 |
| c6_check.py / .log | cbdc1dfa… / 2f243aec… | MATCH / MATCH | 20:06:01 / 20:06:03 |
- All six sidecars were written at 20:07:20, after the runs: post-run integrity sidecars, not frozen-before-run (same as 077e417d N3; fix F1).
- Filename time 2007 ≤ mtime 20:08:23: fine.
- **Reruns (PP, /workspace/pp-audit-bps-704df3ee, all exit 0, < 5 s each): all three logs byte-identical** to NL's (rerun_*.log carry the same sha256 as NL's logs).
- PP independent script: pp_bps_audit.py 6e032abf0182451dde43f7e6ec1b91b067afa29fcb8cafdecf58f693c8c28269 (sidecar written **before** the run), log pp_bps_audit.log d76d0cd1a0cd03f73f0e03758a66d73e034e7df6d0cd1c9270c06829cc68e855. Exact sympy except P4 (numpy rank at exact rational input).

## 1. Independent derivations
### B1 — superpotential (PROVED, agree)
- V = −L_pot from CGR (3.8) with ψ = 0, T = 1: V = g²[½l²e^{12λ−16φ} − 2l e^{−10φ} − ½e^{−4φ}(3e^{8λ} + 12e^{−2λ})].
- 1D reduction: for ds² = dr² + e^{2A}dx², √g R = e^{4A}(−8A″ − 20A′²) = −8(e^{4A}A′)′ + 12A′²e^{4A}, so L₁ = e^{4A}(12A′² − 30X′² − V). Hamiltonian constraint V = 30|X′|² − 12A′². With A′ = −W/3, X′ = ∇W/30: **V = (1/30)|∇W|² − (4/3)W²**. PP re-verified identically (P0), and checked the X-equation by hand: X″ + 4A′X′ = (1/900)W_{XY}W_Y − (2/45)WW_X = V_X/60. ✓
- ∇W = 0 at e^{30φ} = e^{10λ} = 2 (l = −1); W* = 3·2^{1/3}g/2; A′ = −1/L ⇒ L = 3/W*, **g²L² = 2^{4/3}**; independent check V* = −12/L² holds exactly.
- "Only ±W in the three-exponential ansatz": the coefficient system (2a₁b = 1, 2a₁a₂ = 3, 4a₂² = 9, 4b² = 1) has exactly two solutions. ✓ (scoped to that ansatz).
- Normalisation remark for the queued B2 file: the statement "V = 2|dW|² − (4/3)W²" can only be consistent with B1 if "|dW|²" there is taken in a different scalar metric/normalisation (CGR (5.16) kinetic terms, not the 30(dφ)² + 30(dλ)² of (3.7)); this is checked in the follow-up findings file, not here.

### B2 — supersymmetric reading (CONDITIONAL, agree; strengthened)
- **PP P2 (PROVED, algebra from cited CGR data):** with CGR (5.15), (5.22) (h^I satisfies C_IJK h^I h^J h^K = 1, checked) and the moment maps (D.19) at z = 0, w = 0: P ≡ ½h^I P_I has only an r = 3 component and **W = −2√3 g P³ exactly**. So NL's W is (up to sign and the constant) the N = 2 moment-map function, not just "a fake superpotential of the same form".
- Still CONDITIONAL on: (i) the standard N = 2, D = 5 statement that the gravitino shift is ∝ P^r σ_r (cited, not re-derived); (ii) "16 supercharges at MN2" (CGR §6.1, citation); (iii) the BKV sign-flip mechanism.
- Subtlety (fix F3): a flow of the N = 2 subtruncation is guaranteed ≥ 4 supercharges (half of N = 2's 8). Reaching 8 (4D N = 2 Poincaré) needs the other N = 4 gravitino-shift eigenvalue to coincide along the flow; "at most 8" is a correct upper bound, nothing more.
- **Irrelevant to the obstruction:** by P1 below, every IR-regular level-0 wall satisfies the B4 junction identities whether or not it is supersymmetric. B6/B7 need neither B2 nor BKV.

### B3 — IR-regular BPS curve (PROVED, agree) and PP P1 (PROVED, new)
- Hess W/30 at MN2 has eigenvalues ∓2/L, eigenvectors (−3, 1) and (1/3, 1). With A′ = −W/3 < 0, r → +∞ is the IR; only e^{−2r/L} = z^{−2} = z^{4−Δ}, Δ = 6, decays. The fixed point of the 2D gradient system is hyperbolic (a saddle), so by the stable-manifold theorem the IR-regular W-flows form one smooth curve (two branches + MN2). ✓
- **P1 (PROVED): every IR-regular second-order level-0 flow into MN2 is a W-flow.**
  - Second-order linearisation at MN2 (constraint surface, branch A′ < 0): μ² − 4μ/L − m² = 0 with m²L² ∈ {12, −4} gives μL ∈ {6, −2} and {2, 2} (P1 in the log). Hyperbolic; only one decaying exponent, so the stable manifold W^s(MN2) of the 4D constraint-surface flow is 1-dimensional.
  - The lifted W-curve (X, ∇W/30) is invariant (B1: W-flows solve the second-order equations) and converges to MN2, so it lies in W^s, which is 1D; hence they coincide locally, and by ODE uniqueness globally as trajectories.
  - Consistent with K2: 4 phase dimensions − 1 (Δ = 6) − 2 (Δ = 2) = 1.
- The UV tracing (branch −1 to large φ, λ → 0; branch +1 into W < 0) is float only: CONDITIONAL narrative inside B3, not part of the PROVED content.

### B4 — first-order ℤ₂ junction (identities PROVED; the "4 dependent" count REFUTED)
- **Identities, re-derived.** Vary L₁ − δ(r − r_w)e^{4A}T(X): 24[A′] = −4T ⇒ [A′] = −T/6; 60[X′] = T_X. ℤ₂ with the IR side kept (r > r_w): [A′] = 2A′(r_w⁺), [X′] = 2X′(r_w⁺). On a W-flow: **T = −12A′ = 4W, ∇T = 120X′ = 4∇W** at the wall point. Positive tension ⇔ W > 0. ✓
- **By P1 these are not a BPS assumption.** Every level-0 wall with an IR-regular kept side satisfies T(X_w) = 4W(X_w), ∇T(X_w) = 4∇W(X_w). In this class "BPS wall" and "wall" coincide.
- **Image side:** X̃(r) = X(2r_w − r) is a (−W)-flow, i.e. g → −g on the image. The BKV flip is automatic for a ℤ₂-symmetric geometry and adds no condition.
- **Explicit count (NL asked).**
  - Unknowns at the wall (kept side, A and r_w quotiented): u = (φ_w, λ_w, φ′_w, λ′_w, A′_w): **5**.
  - Equations: Hamiltonian constraint **1**; IR regularity **3** (Δ = 6 costs 1, Δ = 2 costs 2; K2); junction **3** ([A′], [φ′], [λ′]). Total **7**.
  - Generic T: Jacobian rank 5 → expected dimension 5 − 7 = **−2** (= K6′ with n_rel = 1). PP P4: at MN2 with T = 4W + δT (Hessian perturbed) the rank is 5, kernel 0.
  - T ≡ 4W: the IR-regular set is a smooth curve on which all three junction functions vanish identically, so their differentials kill its tangent τ; {E_H, E_IR} have rank 4 with kernel τ. **Total rank 4; solution set dimension 5 − 4 = +1** (the wall position). PP P4 confirms rank 4, kernel 1.
  - **Rank deficiency = 7 − 4 = 3, not 4.** The shift −2 → +1 is 3. Counting 4 dependencies would give +2, contradicting NL's own +1. The Hamiltonian constraint is not a new dependency: it holds on every bulk solution, whatever T is.
  - Equivalent wall-set bookkeeping: T ≡ 4W makes E_H dependent on the junction equations (wall set 1D → 2D: 1), and the IR curve lies inside the wall set (non-transversality: excess 2). Total 3.
- **Verdict B4:**
  - B4a (T = 4W, ∇T = 4∇W, positivity ⇔ W > 0): **PROVED**.
  - B4b ("would make **4** conditions dependent"): **REFUTED** by the rank computation above. Correct: 3, of 7 equations in 5 unknowns.
  - "−2 → +1": correct as a count. It is an expected-dimension heuristic; it proves neither existence nor non-existence.
  - Also: T ≡ 4W as functions is needed only for a 1-parameter family. A single wall needs only the 3 pointwise conditions at one point of the curve.

### B5 — φ-scaling of wall constituents (PROVED, scoped to the menu; universal clause OPEN)
- **What "a" is:** a := ∂_φ ln T_i, the logarithmic φ-derivative of the 5D Einstein-frame tension of constituent i, at fixed λ and fixed source data (charges, coordinate densities, gauge-field components).
- **Derivation.**
  - The 11D metric (CGR (2.5)+(3.1)) is x-block Δ^{1/3}e^{−4φ}e^{2A}η, Σ-block Δ^{1/3}e^{6φ}ĝ, fibre g^{−2}Δ^{−2/3}T^{−1}DμDμ (no φ). (3.1) is 5D Einstein frame: e^{−10φ}e^{6φ}e^{4φ} = 1.
  - An NG brane wrapping x and p horizontal Σ directions: e^{−8φ}·e^{3pφ}, so a = −8 + 3p.
  - YM: √h₁₀ ∝ e^{−2φ}, and each Σ index costs e^{−6φ}, so a = −2, −8, −14.
  - Localisation deltas are coordinate densities and carry no metric factor.
  - Smeared M5 on x × Σ: F = Pe^{−6λ} + (1 − P)e^{4λ}; at P = 2/5 this is (1/5)Tr T. ✓
- **Loophole 1 (twist mixing; form wrong, bound survives).**
  - An actual M5 sheet on x × Σ at a fibre point with μ₁² + μ₂² ≠ 0 has induced Σ metric Δ^{1/3}e^{6φ}ĝ + B, with B ≥ 0 φ-independent from the twisted DΜ. The connection is curved (deg L = 2), so horizontal sections do not exist off μ₁ = μ₂ = 0.
  - Then T is **not** of the form c·e^{aφ}F(λ). But a_eff = ∂_φ ln T satisfies **a_eff + 2 = −3(αb₁e^{6φ} + αb₂e^{6φ} + 2b₁b₂)/det ≤ 0**, i.e. a_eff ∈ [−8, −2] (PP P5, exact). The same holds for any tilted 2-surface in Σ × S⁴.
  - NL's form is exact for the horizontal smeared-fluid idealisation used in K4/Y15, and at the twist-fixed locus (P = 0).
- **Hypotheses actually used:**
  - (H1) 4D Poincaré invariance, i.e. no x-legs (I1's hypothesis);
  - (H2) energy is an NG volume (any embedding) or YM ½|F|², with metric dependence only through induced/inverse metric;
  - (H3) source data held fixed;
  - (H4) the CGR uplift.
- **Energy condition:** only positivity, c ≥ 0 and F ≥ 0 (positive tension). **No NEC is used.** The bound a ≤ −2 is structural (H2), not an energy condition (fix F5).
- **Excluded / loopholes not covered:**
  - (i) the HW −½ tr R² term: not positive, and it modifies the junction itself (Myers-type terms);
  - (ii) any positive-energy constituent whose energy grows with Σ size (a > −2). None is known in the menu: a KK monopole with NUT circle along Σ needs a Σ isometry, which Bolza lacks; with NUT along the fibre, a = −8 + 3p;
  - (iii) thick walls;
  - (iv) M5 WZ (C₆) couplings: topological, they implement g → −g (the flux jump) and do not enter the tension.
- **Verdict B5:** the a ≤ −2 statement (in the a_eff form) is **PROVED for the menu** {NG M5-type branes, smeared or not, any embedding; YM without x-legs}. The form "c·e^{aφ}F(λ)" is exact only for the horizontal idealisation (fix F4). The word "Any" (all positive-energy constituents) is **not proved: PP P6, OPEN.**
- **"On Bolza it cannot supply +12g e^{6λ−8φ}":** correct given the menu. Σ_i c_i(a_i + 2)e^{a_iφ}F_i ≤ 0 < 12g e^{6λ−8φ}. With a_eff: Σ_i(∂_φT_i + 2T_i) ≤ 0. ✓

### B6 — no level-0 ℤ₂ wall on H²/Γ (PROVED, scoped; strengthened by P1)
- W_φ + 2W = −3gl e^{6λ−8φ} (exact), so 4(W_φ + 2W) = +12g e^{6λ−8φ} for l = −1. Against B5 this is impossible, and P-independent. ✓
- Flat Σ (l = 0): only a = −2 pieces; T = 4W forces cP = 4g, c(1 − P) = 6g, so P = 2/5 and c = 10g. Reproduces C6. ✓
- By P1 the statement covers **all** level-0 walls with an IR-regular kept side, not only "first-order (BPS)" ones (fix F6).
- The 11D reading of the 5D φ-junction (as a projection of 11D Israel) is not shown. B7 supplies the 11D statement directly.

### B7 — 11D face identity (PROVED, agree; Y15 extended)
- In the connection-adapted coframe (ê_Σ, Dμ), the coframe is r-independent, so K is block-diagonal (NL's remark is correct).
- With unit normal n = Δ^{−1/6}e^{2φ}∂_r into the kept side: k_x = ε(A′ − 2φ′ + D′/6D), k_Σ = ε(3φ′ + D′/6D).
- So k_Σ − k_x = ε(5φ′ − A′), and on a W-flow this is **(ε/6)(W_φ + 2W) = −(gl/2)ε e^{6λ−8φ} > 0** (P3, exact). At exact MN2 it equals ε/L = k, reproducing Y15. ✓
- With S = −(2/κ²)(K − hK), S(ℓ,ℓ) = −(2/κ²)(k_Σ − k_x) < 0 for ℓ = t̂ + ê_Σ, at every point of S⁴ and every χ.
- **PP P3 (PROVED, P1 + B7 + PP NEC corollary 077e417d):** Y15's no-go extends from the exact MN2 face to **every face of every IR-regular level-0 kept side** (any wall position on the curve, both branches, both [χU]/[χS]). No NEC-respecting wall content works there. This needs no supersymmetry and no no-x-legs hypothesis (I2-type).
- Wording fixes (F7):
  - "every BPS face violates the NEC" should read "the **required** wall stress on every such face violates the NEC".
  - "no YM + M5 content of either sign of σ" holds for M5s on x × Σ (isotropic on x ⊕ Σ). M5s not wrapping Σ (p < 2) with σ < 0 do contribute negatively to S^Σ_Σ − S^x_x and are not excluded by I1.

### B8 (CONDITIONAL, agree)
- Float; the χ-grid minima of k_x − k_v are reproduced byte-for-byte.
- "Fails in every fibre direction" means each direction fails at some χ. Superfluous given B7.

### B9 (PROVED, agree; wording)
- Fibre metric re-derived: dχ² coefficient e^{6λ}sin²χ + e^{−4λ}cos²χ = e^{2λ}Δ (P7).
- PP imposed all four conditions (k_Σ = k_x, and k_χ = k_S¹ = k_S² = K); the only solution is a = f = h = 0. ✓
- Wording (F8): the result shows that C4 data need fields **outside the SO(2)×SO(3)-invariant (φ, λ) sector**. "Namely the S⁴ breathing mode" names one candidate. It is not proved necessary or sufficient.

### B10 (CONDITIONAL, agree; the coincidence is an identity)
- 4W = T_pos + T_neg exactly; at MN2, T_pos = 8·2^{1/3}g, T_neg = −2·2^{1/3}g, |T_neg|/T_net = 1/3. ✓
- **Not a coincidence (PP, exact):**
  - |T_neg|/T_net = (W_φ + 2W)/(6W) identically.
  - The 11D pointwise ratio |S(ℓ,ℓ)|/ρ_w = (k_Σ − k_x)/(k_x − K) equals 1/3 on the exact MN2 face, since K = 4k_x.
  - Both reduce to 2W*/(6W*) at MN2, where W_φ = 0. Off MN2 they differ (the 11D ratio depends on χ).
- "Saturates L3" stays CONDITIONAL on identifying a 5D integrated tension with the 11D pointwise σ (NL's stated condition).
- "Minimal" is not proved within 5D; it rests on L3 under that identification.
- **Missing alternative (F9):** besides c < 0 with a < −2, a positive-energy constituent with a > −2 (outside the B5 menu, P6) would also do. Neither is known in M-theory.

### B11 (PROVED, agree)
- Rerun byte-identical.
- The H² residual at q² = 1 simplifies: the numerator −6(H₀ − cr)³ gives exactly −1/s₂² (the H² Ricci). Flat Σ: ∝ c²(q² − 1). ✓
- Off-diagonal Ricci vanishes for this multiply-warped product (fibre metrics r-independent up to warp). ✓
- Scope: transverse flat ℝ⁴_y (C6's harmonic setup), not the S⁴ fibre.

### B12 (OPEN, agree).

### B13 / K7 verdict (CONDITIONAL, agree; scope made exact)
- **PROVED part (PP P3 + B6):**
  - Scope: the SO(2)×SO(3)-invariant level-0 (φ, λ) bulk, IR side kept, IR-regular kept side, l = −1.
  - (i) Every such wall obeys T = 4W, ∇T = 4∇W (P1 + B4a).
  - (ii) No NEC-respecting 11D wall content closes it, pointwise on S⁴ (B7). This covers both [χU] and [χS].
  - (iii) No B5-menu content closes it in 5D (B6).
- **Not covered:**
  - SO(3)-breaking r-only fields of CGR (w in T_αβ = diag(e^w, e^w, e^{−2w}), ψ/z^a), so "the cohomogeneity-one class" overstates the scope (F10);
  - χ-dependent / breathing / higher-KK (B12);
  - UV side kept;
  - tr R² and NEC-violating sources;
  - constituents with a > −2.
- "0 constraints become dependent" is vacuous where there are no solutions. Say "the K6′ deficit is not removed by any first-order mechanism in this class".
- "Would make 4 dependent" must read **3** (B4b).
- K6′ ≤ −2 stands (CONDITIONAL heuristic). K6 stays OPEN. K7 is **OPEN** overall, and closed (PROVED) only in the scope above.

## 2. Per-claim table
| item | NL | PP | reason |
|---|---|---|---|
| B1 | PROVED | **PROVED** | V = (1/30)\|∇W\|² − (4/3)W² re-derived; MN2 critical; g²L² = 2^{4/3}; V* = −12/L² |
| B2 | CONDITIONAL | **CONDITIONAL** | W = −2√3 g P³ exact (P2), but gravitino-shift relation, 16 Q, BKV cited; 8 vs ≥ 4 (F3) |
| B3 | PROVED | **PROVED** | exponents ∓2/L; hyperbolic saddle; UV tracing float (narrative) |
| B4a | PROVED | **PROVED** | T = 4W, ∇T = 4∇W re-derived; automatic by P1 |
| B4b ("4 dependent") | PROVED (in B4) | **REFUTED** | rank count: 7 eqs, 5 unknowns, rank 4 → deficiency 3; "4" contradicts −2 → +1 |
| B5 | PROVED | **PROVED (scoped to menu, a_eff form)** | twist mixing breaks the c·e^{aφ}F(λ) form but a_eff ∈ [−8, −2]; "any constituent" → P6 OPEN |
| B6 | PROVED | **PROVED** | sign identity exact; covers all level-0 walls by P1 |
| B7 | PROVED | **PROVED** | k_Σ − k_x = (ε/6)(W_φ + 2W) re-derived; wording F7 |
| B8 | CONDITIONAL | **CONDITIONAL** | float |
| B9 | PROVED | **PROVED** | all four conditions; "breathing mode" is a candidate only (F8) |
| B10 | CONDITIONAL | **CONDITIONAL** | 1/3 is an identity at MN2; identification hypothesis; a > −2 alternative (F9) |
| B11 | PROVED | **PROVED** | rerun identical; −1/s₂² exact |
| B12 | OPEN | **OPEN** | — |
| B13 (K7) | CONDITIONAL | **CONDITIONAL** | level-0 part PROVED (P3); scope F10; 4 → 3 |

**NL tally 8/4/1/0 (13). PP tally (14 rows, B4 split): PROVED 8 · CONDITIONAL 4 · OPEN 1 · REFUTED 1.**
PP-own items:
- P1 (IR-regular level-0 flows = W-flows): PROVED
- P2 (W = −2√3 gP³): PROVED (algebra from cited CGR data)
- P3 (Y15 extended to every IR-regular level-0 face): PROVED
- P4 (rank check): PROVED
- P5 (a_eff bound with twist): PROVED
- P6 (B5 for all positive-energy constituents): OPEN
- PENDING 0.

## 3. Numbered fixes for NL
1. **F1.** Sidecars are post-run integrity sidecars (20:07:20). Freeze .py sidecars before running.
2. **F2.** B4: replace "make **4** conditions dependent" with "rank deficiency **3**: 7 equations (1 Hamiltonian + 3 IR-regularity + 3 junction) in 5 unknowns, rank 5 generically (−2), rank 4 for T ≡ 4W (+1)". State that the Hamiltonian constraint is not a new dependency, and that a single wall needs only the 3 pointwise conditions.
3. **F3.** B2: cite the moment-map identity W = −2√3 gP³ (CGR (5.22), (D.19)). Replace "can preserve the 8 Poincaré" with "≥ 4 guaranteed by N = 2; 8 iff the second N = 4 gravitino-shift eigenvalue matches".
4. **F4.** B5: define a := ∂_φ ln T_i at fixed λ and source data. State hypotheses H1–H4. Replace "of the form c·e^{aφ}F(λ)" with "∂_φ ln T_i ≤ −2 (exact form c·e^{aφ}F(λ) for the horizontal smeared idealisation / P = 0)". Note the twist term B ≥ 0. Restrict "Any" to the menu, and list a > −2 constituents, tr R² and thick walls as not covered.
5. **F5.** B5: say that no energy condition beyond positive tension is used. The bound is structural.
6. **F6.** B6/B13: by P1 every IR-regular level-0 wall is first-order. Drop "BPS" as a restriction in this class.
7. **F7.** B7: "the required wall stress violates the NEC", and the I1 clause applies to M5s on x × Σ only (p < 2 M5s with σ < 0 are not excluded by I1).
8. **F8.** B9: "outside the SO(2)×SO(3)-invariant (φ, λ) sector; the breathing mode is one candidate".
9. **F9.** B10: state that 1/3 is the identity (W_φ + 2W)/(6W) at W_φ = 0, matching the 11D 1/3 on the exact MN2 face. Add "or a positive-energy constituent with a > −2" as the alternative completion.
10. **F10.** B13: replace "cohomogeneity-one class" with "SO(2)×SO(3)-invariant level-0 (φ, λ) bulk, IR side kept". List w, ψ/z^a, breathing, UV side, tr R², a > −2 as not covered. Replace "0 constraints dependent" with "deficit not removed".
11. **F11.** B3: mark the UV tracing as float (CONDITIONAL narrative).

## 4. Junction implication (plain)
- New and PROVED: for the MN2 odd HW-type wall with the IR side kept, Y15's no-go holds at **every** wall position along the level-0 (φ, λ) IR-regular family, not just at the exact MN2 face. Any such wall is automatically "first-order". Its required stress has negative null energy along Σ, pointwise on S⁴, so no NEC-respecting content (E₈ YM, σ ≥ 0 M5) closes it.
- Remaining escapes, all OPEN: χ-dependent / breathing-mode / SO(3)-breaking bulk (B12); a NEC-violating source (σ < 0 at ≥ ρ_w/3, large tr R², flux terms); a constituent with a > −2; or keeping the UV side.
- K6′ ≤ −2 stands as a CONDITIONAL heuristic. K7 is OPEN outside the level-0 scope.
- **Junction: UNSOLVED.** Nothing adopted.

Tip at write time: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (unchanged). No CERT. Nothing sent.
