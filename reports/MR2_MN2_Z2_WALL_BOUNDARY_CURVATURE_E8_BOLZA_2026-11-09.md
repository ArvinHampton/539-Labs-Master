# MR2 — Wall-boundary curvature check: MN N=2 on the Z₂ fixed plane (HW-type wall, odd G₄, localized E₈ source), N=4880, g=2, Γ = Bolza
Written 2026-11-09 ~18:15 CST by MR2 (executor). Additive file; no existing file edited. Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md re-verified sha 7cddb188… (unchanged). No CERT, no Gemini, nothing sent outside.

Authority (all sha-verified this run):
- OW 7ff8299d… (t4377, 17:53): Owner approved this job and adopted Γ := Bolza.
- OW f825dfff… (t4369, 17:45): face := Z₂ fixed plane (HW-type wall); O1 odd (CONDITIONAL on P-b); E₈ wall sector CONDITIONAL. The face itself is the 10D matching hypersurface of OW f283cffd… (16:44).
- OW 19a88b19… (t4383, 18:06): vacuum HOLD lifted; **MN N=2 adopted as a working vacuum, CONDITIONAL (PP 384096a8), not proved.** Junction is UNSOLVED for MN N=2; the pure-M5 no-go and NL's E₈ wall results (NL 1800, 859328a2) stand.
- Neutral: DP-a no stance; b, J7, junction OPEN except what is established below; no source adopted.
Builds on: MR2 9ab8f0a6… (blocker md) with V2 .py ad134752… (routines exec'd verbatim after sha check), erratum 2efef556…; NL 4d9c9951…, erratum 76ec4e75…, NL 1800 859328a2….

## Files (reports/)
| file | sha256 |
|---|---|
| MR2_MN2_Z2_WALL_BOUNDARY_CURVATURE_E8_BOLZA_2026-11-09.py | ce94face6c8395ef1bee10f82e4b80408239157fc7a141b4a2d7fb0411fbbdf3 (frozen chmod a-w before the run) |
| MR2_MN2_Z2_WALL_BOUNDARY_CURVATURE_E8_BOLZA_2026-11-09.log | 7d0728e1b41767c117e9057248d12f8ad5996ceab25da891bbc610c989dfdc7c (exit 0, 245 s, dps 40) |
| this .md | see .md.sha256 |

## 0. Model (what is computed)
- MN2 fixed point (z=1, a₁=1, a₂=0): X₁=0.659754, X₂=X₀=1.319508, e^{2f₀}=0.574349, e^{2g₀}=0.287175; uplift units, physical metric ℓ²×, ℓ = 49.6844 ℓ_p.
- AdS₅ radial coordinate ρ = ln r. The wall sits at constant ρ = 0 (a constant-r face, the class NL/PP call "constant faces").
- Z₂ fixed plane modelled the HW/orbifold way: the bulk on both sides is exact MN2 and the transverse profile is the Z₂-even kink, g_xx = wF₀ e^{−2σ(ρ)}, σ_ε = s·ε ln cosh(ρ/ε) (ε → 0 gives s|ρ|). G₄ is extended odd: G(ρ) = sgn(ρ)·G_MN2.
- The E₈ source is whatever the Israel condition and the HW Bianchi identity demand at the wall; it is a δ-function (or thickness-ε) source in ρ. The HW linear-order warp (Witten hep-th/9602070; LOSW hep-th/9803235, "The Universe as a Domain Wall") is used only as a validation case (§V). For MN2 the kink is fixed by the bulk and is O(1), not a small HW correction (consistent with NL L2).
- Cases: KINK s=+1 (r > r_b region kept on both sides), WRONG_SIGN s=−1 (r < r_b kept), NO_SOURCE (smooth MN2, no wall), MISPLACED (kink at ρ=0.3, wall presumed at ρ=0).

## V. Validation of the routine (PROVED, in-repo, log §V1–V2)
- **Flat-space HW-type wall in 11D** (ds² = dy² + e^{2A}η₁₀, A = −kε ln cosh(y/ε)): Riem², Ric², R match the exact closed forms to every printed digit at y = 0 and ±0.3. Bulk value 220k⁴ (AdS₁₁) reproduced. Weyl² ≈ 1e-34, as it must be for an umbilic wall. **k = 0 (no source) gives exactly flat: all invariants 0.**
- **LOSW 5D domain wall** (a = H^{1/2}, b = H², H = c₀ + h|y| smoothed): ∫R dY → −8h/c₀³ = −1.456532 (numerics −1.42896, −1.45373, −1.45625 at ε = 1e-2, 1e-3, 1e-4, converging as O(ε)); ε²Riem²(0) = 0.04642441618 = 4h²/c₀¹⁰ exactly. LOSW solution form: CONDITIONAL (hep-th/9803235 §4; equation number not re-verified this pass; title verified on arXiv 18:07 CST).

## 1. Compatibility of the f825dfff fixed plane with MN2
- **C1 (PROVED, in-repo + standard geometry). As a smooth fixed locus of an isometry, a constant-r (or any non-totally-geodesic) face is REFUTED.** The fixed set of an isometric reflection is totally geodesic; a constant-r face of MN2 has K_xx = −k h_xx ≠ 0 (k = 1/√(wF₀) uplift), so it cannot be one. Also the AdS₅ warp is monotone in r, so no reflection r ↦ r_b²/r-type isometry of MN2 fixes it. Matches NL L1/L2.
- **C2 (PROVED, in-repo). As an orbifold / HW gluing it is COMPATIBLE**, with sources required:
  - The metric is Z₂-even: all metric functions continuous across the wall, normal derivatives odd (the kink). Each side is exact MN2.
  - All nonzero G₄ components are tangent to a constant-r wall (index sets {u,v,α,φ₂}, {u,v,β,φ₂}, {u,α,β,φ₂}, {α,β,φ₁,φ₂}; none has an r leg). So "G₄ odd" means G jumps from −G to +G: [G₄] = 2G₄|_wall ≠ 0.
  - Bulk equations hold on both sides: Einstein is quadratic in G; Maxwell holds because G∧G ≡ 0 for MN2 (9ab8f0a6, PROVED identically).
  - The Bianchi identity then requires a wall 4-form source J = 2G₄|_wall δ(wall). Flux check: |∫_{S⁴}G₄| = 9.869501 vs π² = 9.869604 (rel. 1e-5, quadrature), i.e. N = 4879.95 ≈ 4880; **wall charge 2N = 9760**, which is the f825dfff/NL E1/Y8 relation N_M5 + n_inst = 2N_flux. That the source is E₈ (tr F∧F − ½tr R∧R) is CONDITIONAL (HW hep-th/9603142).
- **C3 (PROPOSAL, not adopted; OPEN as physics).** Every G₄ component carries a φ₂ leg, and with a₂ = 0 the metric is φ₂-independent with no φ₂ cross terms (log). So φ₂ → −φ₂ is an orientation-reversing isometry of MN2 under which G₄ is odd: a genuine M-theory Z₂ (parity + C → −C). Its fixed plane AdS₅ × Σ × S³_eq is totally geodesic and smooth, with no Israel stress. It is a fibre wall, not the radial matching hypersurface of f283cffd, so it is not the Owner's face. Recorded only as a proposal.

## 2. Answers
### (i) One-sided bulk limits — **BOUNDED. PROVED at sampled points; global max CONDITIONAL (dense scan)**
- At ρ = ±0.5 and ±0.01 (KINK, ε = 1e-4) on the 17-point pole-reaching grid, both sides are identical and equal to the MN2 bulk of 9ab8f0a6:
  Riem² ∈ [511.808, 3407.981]/ℓ⁴, Ric² ≤ 3311.984, Weyl² ∈ [297.901, 1939.188], R ∈ [5.2913, 11.99997]/ℓ², max|eig Q| = 13.333308/ℓ².
- The one-sided limits exist, are finite and are equal on the two sides (Z₂ image). They are ρ-independent (AdS₅ homogeneity) and Γ-independent (local quotient), so Bolza changes nothing here.
- ℓ_p²-scaled: ℓ_p²√Riem² ≤ 0.02365, ℓ_p²|K_sec| ≤ 5.401e-3.
- Premise: the bulk next to the wall is exact MN2. Localized (non-smeared) E₈/M5 backreaction along the wall would deform it, and that is OPEN (NL Y14/Y15; nonlinear localization L5).

### (ii) Distributional part at the wall — **a δ-function in Ricci with finite weight. PROVED (numerics match Israel to ≤ 1e-4 after the bulk baseline is removed)**
- ∫G^a_b dy across [−10ε, 10ε], ε = 1e-5, at 3 angle points, in units of k = 1/√(wF₀):
  - KINK: x-block −6.0005 to −6.0007; ρρ −0.0005 to −0.0007; internal 6-block −7.9996 to −8.0007; off-diagonal ≤ 1.1e-3.
  - NO_SOURCE baseline is about 4e-4 to 6e-4 on every entry. That is the 2Δ × bulk contribution. Subtracting it leaves −6.0001 / −0.0001 / −8.000 to within about 2e-4.
  - Israel prediction: x −6k, ρρ 0, internal −8k δ^a_b. Equivalently, with S_ab = −(2/κ²)(K_ab − h_abK) (PP/NL convention), S = −(6k/κ²)h on R^{1,3} and −(8k/κ²)h on Y₆; ∫R dy = 16k.
- This is the standard Israel δ-curvature. It is not a divergence of the smooth invariants.
- What it implies for the source (CONDITIONAL on HW and NL Y2/Y5, which are already filed):
  - The required stress is anisotropic: x : Σ : fibre = 6 : 8 : 8 (tension units k/κ²).
  - BPS E₈/M5 sources give 6D worldvolume −ρh with fibre 0 (NL Y5).
  - For s = +1, S(k,k) = −2k/κ² < 0 for null k along t + fibre. So the fibre-NEC deficit is reproduced independently, consistent with NL Y3/Y4: no E₈ field can supply it.
  - **Junction for constant-r faces stays UNSOLVED** (OW 19a88b19). This check adds an independent numerical confirmation of the required S_ab, not a solution.

### (iii) Thin-wall limit of the smoothed profile — **the quadratic invariants DIVERGE as 1/ε². PROVED in-repo**
- At the wall centre the relative deviation from the thin-wall coefficients is 6.6e-2, 6.5e-3, 6.5e-4, 6.5e-5 at ε = 1e-2, 1e-3, 1e-4, 1e-5, i.e. O(ε).
- The coefficients are ε²Riem² → 16/(wF₀)², ε²Ric² → 20/(wF₀)², ε²R² → 64/(wF₀)², ε²Weyl² → (128/15)/(wF₀)², ε·R → +8/(wF₀), ε·max|eig Q| → 1/(wF₀).
- Log-log slopes are −1.99955, −2.0000051, −2.000001 for Riem², and −1.99686 → −1.99998 for Weyl².
- **Weyl² diverges too.** That is because the kink is non-umbilic: only the 4 x-directions bend. An umbilic wall (V1 check) has Weyl² = 0.
- R and the sectional curvature diverge only as 1/ε, as δ-approximants.
- Physical size (CONDITIONAL on the wall-thickness premise ε_y ≳ ℓ_p): ℓ_p²√Riem²(centre) = 4kℓ_p²/ε_y, which is 0.101–0.114 at ε_y = ℓ_p. It reaches 1 only for ε_y ≤ 0.114 ℓ_p. So the smoothed wall stays inside the EFT for any Planck-thick or thicker wall. The divergence is a thin-wall (classical HW δ) artefact at the scale where the R⁴/M-theory wall structure takes over (OPEN).

## 3. Magnitudes at N = 4880
These are CONDITIONAL on the standard normalisation 2κ² = (2π)⁸ℓ_p⁹ and T_M5 = 1/((2π)⁵ℓ_p⁶); the arithmetic is PROVED.
- D ∈ [0.659754, 1.319508], so D^{1/6} ∈ [0.933033, 1.047294].
- Wall extrinsic curvature k = 1/(ℓ√(wF₀)) ∈ [0.025358, 0.028464]/ℓ_p, against L₅ = 37.6537 ℓ_p.
- δ-weight ∫R dy = 16k ∈ [0.4057, 0.4554]/ℓ_p.
- Israel wall energy density ρ_w = 6k/κ² ∈ [1.2528e-7, 1.4062e-7] ℓ_p⁻¹⁰. Internal pressures are −8k/κ².
- **Compared with the M5 flux scale:** the BPS count needed to carry ρ_w is N_req = (12N/π²)∫k√det g₆/√det g_Σ (measure validated: Vol(round S⁴, ½) = π²/6 to 15 digits).
  - Horizontal Σ measure: N_req/(2N_flux) = 1.2876.
  - Fixed-φ embedding: N_req/(2N_flux) = 1.0316.
  - The horizontal value lies inside NL's count gap (1.255, 1.667). The choice of measure is CONDITIONAL. In both cases ρ_w is the same order as, and at least as large as, the BPS energy of the 2N = 9760 units of charge the Bianchi identity forces. The count matches to O(1); the anisotropy (ii) is what fails.

## 4. Controls
- **NO_SOURCE:** at ρ = 0, bounded MN2 bulk values (Riem² max 3407.98) at ε = 1e-4 and 1e-5, with no ε-dependence. ∫G dy ≈ 4e-4 to 6e-4 (bulk only), and the flat V1 case is exactly 0. But odd G₄ without a source violates Bianchi by 2N = 9760 units at the wall, and Israel needs K = 0, which MN2 constant-r faces violate. **FAILS as a fixed plane, as required.**
- **WRONG_SIGN (s = −1):** quadratic coefficients unchanged (Riem² 6.4e9 at ε = 1e-4, 6.4e11 at 1e-5). R flips sign (−1.27e5 to −1.60e5 at 1e-4). The Israel integrals flip to +6k / 0 / +8k, i.e. negative wall energy density −6k/κ². A positive-energy E₈ source with s = −1 gluing, or a wrong-sign Bianchi source (residual 4N = 19520), **FAILS. The δ-part CHANGES as required; the 1/ε² scaling is sign-blind.**
- **MISPLACED (kink at ρ = 0.3):** at the presumed wall ρ = 0 the values are bounded bulk ones (3407.98) and ∫G dy ≈ baseline. The divergence moves to ρ = 0.3 (6.4e9). The Bianchi residual is +9760 at ρ = 0 and −9760 at ρ = 0.3. **FAILS, as required.**
- Nothing was tuned. Parameters are the 9ab8f0a6 fixed point, and the ε list was fixed in advance.

## 5. Γ = Bolza (adopted, 7ff8299d)
- The invariants in (i)–(iii) are local, so they are independent of Γ (PROVED: a locally isometric quotient). Bolza changes none of them (consistent with NL Γ1).
- **Global scan** (25×13 = 325 points incl. 1e-6 edges): Riem² max 3407.980947 and max|eig Q| 13.333308, both at (α, β) = (π/2+d, 1e-6). Ric² max 3311.984, Weyl² max 1939.188, |R| max 11.99997. This reproduces the 17-point maxima, so no larger value was found. **Global max CONDITIONAL** (dense sampling, not a proof).
  - Slip, recorded honestly: my 182-point 1D edge refinement ran along β = π/2 and α = 1e-6, not the edge where the maximum sits (β → 0, α ≈ π/2). It is uninformative for the maximum (it found 511.81 and 6.35).
- **Systole** with Γ = Bolza:
  - sys_hyp = 2 arccosh(1+√2) = 3.057142 (CONDITIONAL: Jenni 1984, arXiv:2302.02540).
  - ρ_Σ = 26.6252 ℓ_p; unwarped 81.397 ℓ_p.
  - 11D warped bounds (PROVED arithmetic): sys₁₁ ∈ [75.95, 85.25] ℓ_p. The lower bound is ρ_Σ·min D^{1/6}·sys. The upper bound is the horizontal lift closed on the μ₁ = 0 locus, where the twisted circle shrinks.
  - ρ_Σ D^{1/6} ∈ [24.842, 27.884], which CONFIRMS PP's [24.8, 27.9].
  - The thresholds (2πℓ_p needs sys_hyp ≳ 0.25) are cleared by more than 10×.
  - "Warping lengthens the systole" is **REFUTED as stated**: min D^{1/6} = 0.933 < 1, so the lower bound (75.95) is below the unwarped 81.40. The correct statement is that warping changes it by a factor in [0.933, 1.047]. That is consistent with OW 19a88b19 listing the claim as OPEN.

## 6. Labels
| item | label |
|---|---|
| V1 flat HW wall closed forms; k=0 flat; V2 LOSW δ-weight and ε² coefficient | PROVED |
| LOSW solution form (hep-th/9803235 §4) | CONDITIONAL |
| C1: constant-r face as a smooth isometric fixed plane | REFUTED |
| C2: orbifold/HW gluing compatible; metric Z₂-even with kink; G₄ tangent and odd, [G₄] = 2G₄, wall charge 2N | PROVED |
| C2: source is E₈ (tr F² − ½tr R²) | CONDITIONAL (HW 9603142) |
| C3: φ₂-reflection fibre wall | PROPOSAL (not adopted); physics OPEN |
| (i) one-sided bulk limits bounded and equal | PROVED at sampled points; global CONDITIONAL; exact-MN2-near-wall premise CONDITIONAL |
| (ii) δ-function Ricci with Israel weights −6k/0/−8k; ∫R dy = 16k | PROVED |
| (ii) BPS E₈/M5 cannot supply the 6:8:8 stress (fibre-NEC deficit) | CONDITIONAL (NL Y3/Y5; confirms them) |
| (iii) Riem², Ric², R², Weyl² ∝ 1/ε² (slope −2.000) | PROVED |
| (iii) bounded for ε_y ≳ ℓ_p (ℓ_p²√Riem² ≤ 0.114) | CONDITIONAL (thickness premise) |
| magnitudes (k, ρ_w, N_req/2N) | arithmetic PROVED; normalisations CONDITIONAL; measure choice CONDITIONAL |
| controls (no source, wrong sign, misplaced) | fail or change as required (PROVED) |
| Bolza systole bounds [75.95, 85.25] ℓ_p | PROVED arithmetic; Bolza value CONDITIONAL |
| "warping lengthens systole" | REFUTED as stated |
| junction for MN N=2 | UNSOLVED / OPEN (not changed) |
| localized (non-smeared) source backreaction; wall micro-structure below ℓ_p | OPEN |

Tally: PROVED 9, CONDITIONAL 6, OPEN 2 (C3 physics, localized backreaction/micro-structure) + junction OPEN carried, REFUTED 2 (C1; warping-lengthens-systole). The 2 proved-at-samples/global-conditional rows are counted under PROVED with their caveats.

## 7. Open items, resolution path and ETA
| item | path | ETA |
|---|---|---|
| Global max proof of the MN2 invariants | Analytic: invariants are rational in (cos²α, sin²β) at fixed X; maximise symbolically, or rerun the edge refinement on β → 0 | 30–45 min |
| Localized-source backreaction near the wall | Cohomogeneity-2 relaxation with a pointlike or finite-size source on the fibre; joint with NL Y14 | days |
| Wall micro-structure for ε_y < ℓ_p | Beyond sugra (R⁴/HW wall); no in-repo path | — |
| C3 fibre wall (if the Owner wants it pursued) | Owner decision first; then the HW anomaly check on S³_eq | 1–2 h after a decision |
