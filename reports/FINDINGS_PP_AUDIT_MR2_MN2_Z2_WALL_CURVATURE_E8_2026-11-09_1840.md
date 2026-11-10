# FINDINGS — PP audit of MR2 MN2 Z₂-wall / E₈ boundary-curvature check (bd47ff5e) + erratum (2368ffbd) — 2026-11-09 18:40 CST (America/Chicago)
Auditor: PP (Professor Proof). Pure math. Labels: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. I refute only by proof or counterexample.
Limits:
- New file only. Nothing edited or overwritten. No CERT. No Gemini. Nothing sent. **Nothing adopted.**
- Citation scope per **OW 36683379** (verified below): any source is allowed, but a citation alone never makes a result PROVED. Where feasible I checked the cited math myself.
- Outside reads: arXiv abstract pages only (titles below).

Tip: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91. It MATCHes at start and at write time (untouched).

PP scratch: /workspace/pp_wall_1820 (sha256 prefixes)
- Scripts: pp_wall.py 0c578c276e57b9a1, pp_wall_run.py 4b3a20c0c72c7673, pp_wall_ii.py 1f9fb3305a2ebfe2, pp_flux_misc.py bd7de71ec9368197, pp_nreq.py 2c003f30b2011713.
- Logs: wall.log a2c4b33a1806299d, wall_ii.log 3d70e85e45718fd3, flux.log 4f499291f232ac18, nreq.log 0b78e33ece5da625.
- The kinked-metric Christoffels, Riemann, Ricci and Einstein are my own code. The only shared input is the MN2 metric of mr2_core, audited in fc5e0156. G₄ comes from my own CLP Ω (384096a8).

## 0. Authority records — PROVED (on disk, sidecars MATCH, wording quoted)
- **OW 19a88b19**: OWNER_WRITE_MAINCHAT_t4383_LIFT_VACUUM_HOLD_ADOPT_MN_N2_CONDITIONAL_2026-11-09_1806.md, sha 19a88b1958753ecaaa999e0ce763bca7fd449069278dd4bdb87cea002613ee03, mtime 18:06:53 CST.
  - Owner's own words: "As mine: lift the vacuum hold and adopt MN N=2 (CONDITIONAL per PP 384096a8)."
  - Decision: HOLD 587eca0c LIFTED. MN N=2 ADOPTED as "an adopted working vacuum, not a proved one". Γ = Bolza stands.
  - Carried caveats: Einstein/Bianchi all-points CONDITIONAL; KK spectrum OPEN; the warping-systole claim OPEN; junction UNSOLVED; O1 odd (f825dfff) stands.
  - Its citation of my 384096a8 rollup (16/13/3/0) is accurate. **The record holds as reported.**
- **OW 36683379**: OWNER_WRITE_VOICE_11fd320e_CITATION_SCOPE_ALL_SOURCES_MATH_CHECKED_AMENDS_3f160803_2026-11-09_1815.md, sidecar MATCH.
  - "ALL citations from ANY source, provided the math in each citation is checked … a citation alone never makes a result PROVED."
- **OW f825dfff** (face := Z₂ fixed plane, HW-type wall; G₄ odd; E₈ wall sector CONDITIONAL) and **PP fe0c3d92** are on disk with matching sidecars.

## 1. MR2 files — PROVED (all MATCH their sidecars)
| file | sha256 prefix | mtime (CST) |
|---|---|---|
| MR2_MN2_Z2_WALL_BOUNDARY_CURVATURE_E8_BOLZA_2026-11-09.md | bd47ff5e | 18:11:05 |
| .py | ce94face | 18:05:28 |
| .log | 7d0728e1 | 18:09:53 |
| MR2_ERRATUM_MN2_Z2_WALL_BOUNDARY_CURVATURE_SYSTOLE_LABEL_2026-11-09.md | 2368ffbd | 18:11:17 |

## 2. (i) One-sided limits — PROVED at sampled points
- **Setup.** I used my own kinked metric: AdS₅ block wF₀[e^{−2σ(ρ)}(dt²+dx²)+dρ²] with σ = ε ln cosh(ρ/ε) (s = +1) and ε = 1e-4. I evaluated it at ρ = ±0.5 and ±0.01 at (π/2+1.234e-3, 1e-6), (0.37, 1.11) and (2.01, 0.23).
- **Result.** Riem² and max|eig Q| equal the smooth MN2 values exactly at all printed digits: 3407.98094735 / 13.33330762, 525.492193935 / 6.423727492, and 1727.90369172 / 10.45289652. The two sides are identical.
- **Global bound.** ℓ_p²√Riem² ≤ 0.02365 holds. The true supremum is 3408.000 (max|eig| = 40/3) at β → 0, from PP 384096a8 §8, not MR2's 3407.981. That moves ℓ_p²√Riem² by less than 1e-5 relative.
- **CONDITIONAL:** the global maximum (dense scan, not proof), and the premise that the bulk next to the wall is exact MN2, since localized backreaction is OPEN.

## 3. (ii) Distributional part at the wall
- **Israel weights — PROVED (own derivation plus own numerics).**
  - Only the x-block bends: one-sided K_xx = ∓k h_xx with k = 1/√(wF₀) in uplift units. The internal K vanishes because the internal metric is r-independent. So [K_ab] = −2k h^{(x)}_ab and [K] = −8k.
  - The δ-part of G^a_b is −([K^a_b] − δ^a_b[K]): **x-block −6k, ρρ 0, internal −8k δ^a_b**. Since G^a_a = −(9/2)R, this gives **∫R = 16k**.
  - Numerics: Gauss–Legendre with 96 nodes over [−10ε, 10ε], ε = 1e-5, at (0.37, 1.11) and (2.01, 0.23). KINK minus NO_SOURCE gives x −6.00012, ρρ −0.00012, internal −8.0002 (all six entries), off-diagonal ≤ 2.6e-3·k. This matches Israel to ≤ 2e-4, which CONFIRMS MR2.
  - Note: my raw baseline (about 1.0e-3 to 1.5e-3) is about 2.5× MR2's 4e-4 to 6e-4, presumably because the integration windows differ. The baseline-subtracted values agree to every printed digit (−6.00012 / −8.0002).
- **Required stress and the NEC — PROVED (given the thin-wall Israel junction).**
  - S_ab = −(1/κ²)([K_ab] − h_ab[K]) gives S = −(6k/κ²)h on R^{1,3} and −(8k/κ²)h on Σ and on the fibre: 6:8:8, with energy density ρ_w = 6k/κ² > 0 for s = +1.
  - For null k = t̂ + ê: S(k,k) = 6k/κ² − 8k/κ² = **−2k/κ² < 0 for ê along the fibre AND along Σ**. MR2 states only the fibre case.
  - Consistency with **PP fe0c3d92 Y3-ineq** (PROVED there for every E₈ field, electric legs included): S_E₈(k,k) = (1/λ²) tr|F(k,·)|² ≥ 0, and S_M5(k,k) ≥ 0. So **no combination of E₈ fields and M5s can supply the required stress.** This is CONSISTENT with NL Y3/Y4.
  - Consistency with **NL Y5**: the BPS form is −ρh on the 6D worldvolume (x+Σ) with fibre 0, i.e. x : Σ : fibre = 1 : 1 : 0. The required 6 : 8 : 8 is not of that form. CONSISTENT.
  - MR2's label "CONDITIONAL (NL Y3/Y5)" can be upgraded: the implication is PROVED, given the thin-wall junction and a source content of E₈ fields plus M5s. Whether a gravitational −½ tr R² piece contributes wall stress is not covered (CONDITIONAL on HW).

## 4. (iii) ε-scaling — scaling PROVED; MR2's grading needs rewording
- **Scaling coefficients — PROVED.** At the centre σ′ = 0 and σ″ = 1/ε. The four (y, xᵢ) planes have sectional curvature a = 1/(wF₀ε) and every other contribution is O(1). So Riem² → 16a², Ric² → 20a², R → 8a, max|eig| → a, and Weyl² → (16 − 80/9 + 128/90)a² = (128/15)a².
  - My numerics: ε²Riem²/(16/(wF₀)²) = 1.0051, 1.000051, 1.0000005, 1.000000005 at ε = 1e-2 … 1e-5. ε·eig·wF₀ → 1. ε·R·wF₀/8 → 1 with O(ε) deviation 3.25ε at (π/2+d, 1e-6) and 2.92ε at (0.37, 1.11).
- **Physical size — PROVED (arithmetic).** k_phys = 1/(ℓ√(wF₀)) and ℓ_p²√Riem²(centre) = 4kℓ_p·(ℓ_p/ε_y).
  - min wF₀ = X₁^{1/3}·(X₁X₂)⁴ = 2^{−1/5}·2^{−4/5} = **1/2 exactly**, and max wF₀ = 0.62995. So k ∈ [0.025358, 0.028464] and 4kℓ_p ∈ [0.1014, 0.1139]. CONFIRMS MR2.
- **Grading of "bounded only if the wall is at least ~ℓ_p thick" — CONDITIONAL, with the wording corrected.**
  - The invariants are finite for every ε > 0. They diverge only in the thin-wall limit ε → 0, so "bounded only if ≥ ℓ_p" is mis-stated.
  - The correct statement: two-derivative 11D sugra controls the smoothed wall only if ε_y ≳ ℓ_p.
  - The binding criterion is the derivative expansion. Higher-derivative terms scale like (kℓ_p)(ℓ_p/ε_y)^m relative to the leading term, and kℓ_p ≈ 0.03. It is not ℓ_p²√Riem² < 1.
  - MR2's remark that the invariant "reaches 1 only for ε_y ≤ 0.114 ℓ_p" should not be read as EFT control down to 0.114 ℓ_p. Below ℓ_p the expansion in ℓ_p/ε_y fails first.
  - Whether a real HW/E₈ wall has thickness ≥ ℓ_p is a physics premise (OPEN/CONDITIONAL).

## 5. (iv) Smooth-reflection fixed plane — REFUTED (C1 confirmed); compatible with f825dfff
- **Theorem (standard; checked):** the fixed set of an isometry of a C² metric is totally geodesic. Proof sketch: geodesics tangent to the fixed set are mapped to geodesics with the same initial data, so they stay in it.
- The constant-r face of smooth MN2 has K_xx = −k h_xx ≠ 0, so it is not the fixed set of any isometry of MN2. r ↦ r_b²/r is not an isometry, because dx²/r² ↦ r²dx²/r_b⁴. **C1 REFUTED is correct.**
- **Logic for HW (PROVED).** The orbifold involution ρ ↦ −ρ is an isometry of the doubled metric g(ρ) = g(−ρ), but that metric is only C⁰ (Lipschitz) across the plane. The theorem does not apply, and the one-sided K are ±k h, discontinuous. The smoothed σ_ε metric is C^∞, its involution is a smooth isometry, and its fixed plane is totally geodesic: σ_ε′(0) = 0 gives K(0) = 0, exactly as the theorem requires. The curvature is then carried by the δ-like source of §3.
- **So C1 refutes only "a source-free smooth MN2 fixed locus".** It does not touch f825dfff, whose face is an HW-type Z₂ fixed plane with an E₈ wall sector (sourced orbifold wall). Compatible (PROVED as a reading of the definition).

## 6. (v) Flux, N and wall charge
- **PROVED: N = 4880 exactly, not 4879.95.** Using my own G₄ (CLP Ω, λ_CLP = 1/8) and 40×40 Gauss–Legendre: ∫_{S⁴}G₄ = −9.8696044010893350 vs π² = 9.8696044010893586, ratio 1 − 2.4e-15.
  - MR2's 9.869501 (relative 1.05e-5) is a quadrature error. The flux is a cohomology class: G₄ is closed (Bianchi PROVED at points in 384096a8), and the normalization is fixed by AdS₇×S⁴ (V2 log: flux/(2π)³N = 1.0).
  - **The wall charge 2N = 9760 is exact.** It matches the f825dfff / NL E1 relation N_M5 + n_inst = 2N_flux.
- **CONDITIONAL:** E₈ identification (tr F∧F − ½ tr R∧R source). The anomaly-inflow math was not rechecked here. Titles verified on arXiv:
  - hep-th/9603142 = Hořava–Witten, "Eleven-Dimensional Supergravity on a Manifold with Boundary" (correct).
  - hep-th/9510209 = "Heterotic and Type I String Dynamics from Eleven Dimensions".
  - hep-th/9602070 = Witten, "Strong Coupling Expansion Of Calabi-Yau Compactification".
  - hep-th/9803235 = Lukas–Ovrut–Stelle–Waldram, "The Universe as a Domain Wall".
- **Normalizations — PROVED (internal consistency).** 2κ² = (2π)⁸ℓ_p⁹, T_M2 = (2π)^{−2}ℓ_p^{−3} and T_M5 = (2π)^{−5}ℓ_p^{−6} satisfy Dirac quantization, T_M2·T_M5 = 2π/(2κ²).
- **N_req ratios — PROVED (arithmetic).** I derived N_req = (12N/π²)∫k√g₆/√g_Σ myself and reproduced 1.28761102 (horizontal) and 1.03156269 (fixed-φ) exactly.
- **CONDITIONAL (measure).** Neither measure includes the x-block warp √|g_x| = (wF₀)², which varies over the fibre within [0.25, 0.397]. Its fibre average relative to the warp at the M5 location changes the ratio by a factor in [0.84, 1.34]: horizontal range about [1.08, 1.72].

## 7. (vi) φ₂ → −φ₂ (C3)
- **Isometry — PROVED.** For MN2, a₂ = 0. My metric row for φ₂ has only g_{φ₂φ₂} ≠ 0 (no u or other cross terms), and nothing depends on φ₂. So the reflection is an orientation-reversing isometry, globally defined because φ₂ is untwisted.
- **Flux parity — PROVED.** Every G₄ component carries exactly one φ₂ leg; the index sets are {u,v,α,φ₂}, {u,v,β,φ₂}, {u,α,β,φ₂} and {α,β,φ₁,φ₂}, and the coefficients are φ₂-independent. So the pullback is φ*G₄ = −G₄.
  - Under the M-theory symmetry (orientation reversal with C → −C), the solution is **invariant**.
  - In HW language, G with one normal leg survives on the plane, and G with all legs tangent is odd and vanishes there. No such components exist.
- **Fixed set — PROVED, with a correction.** It is {y₂ = 0} ∩ S⁴ (y₂ = μ₂ sin φ₂), an S³ containing the μ₂ = 0 locus. Because the φ₁ circle is twisted (a₁ = 1), the fixed set is **AdS₅ × (an S³ bundle over Σ)**, not AdS₅ × Σ × S³ as MR2 writes. It is totally geodesic (theorem of §5) and carries no Israel stress.
- **OPEN (physics).** "No Israel stress" is not "no source". On an M-theory Z₂ fixed plane the HW boundary condition sets the tangential G₄ proportional to (tr F² − ½ tr R²). The tangential G vanishes here, so an E₈ field with tr F² = ½ tr R² on the plane is needed unless tr R∧R restricted to the plane vanishes. Not computed.
- It is a fibre wall, not the radial matching face of f283cffd / f825dfff, so it is not the Owner's face. "Proposal, not adopted" is correct.

## 8. (vii) Controls
- **Validations — PROVED (closed forms re-derived).**
  - V1 flat HW wall at k/ε = 700: Riem² = 40·700² = 1.96e7, Ric² = 7000² + 10·700² = 5.39e7, R = 14000, and the bulk value 220·0.7⁴ = 52.822 (AdS₁₁).
  - V2 LOSW: the δ-part of R is −8[a′/a] = −8h/c₀³, and ε²Riem²(0) = 4h²/c₀¹⁰ exactly. That makes it ε-independent, as logged.
  - These are pure geometry checks, valid whether or not that (a, b, H) solves the LOSW equations. The "LOSW solution form" label (CONDITIONAL) is not needed for the validation.
- **Discriminating controls — PROVED.**
  - WRONG_SIGN flips the δ-weights to +6.000 / 0 / +8.000 (mine, after baseline), i.e. negative wall energy, while ρρ and the off-diagonals are unchanged.
  - MISPLACED gives exactly the NO_SOURCE baseline at ρ = 0.
  - NO_SOURCE is the smooth bulk.
  - The 1/ε² invariants are sign-blind, as MR2 states. V1 with k = 0 being flat is a trivial check, not a control.
- **Not tests — PROVED as arithmetic only.** The Bianchi residuals 9760 (no source), 19520 (wrong sign) and ±9760 (misplaced) follow by definition from [G] = 2G and the chosen source, so they test nothing in the code.

## 9. (viii) Bolza systole — PROVED (consistent)
- [24.842, 27.884] ℓ_p × 3.0571418 = [75.946, 85.247] ℓ_p. This equals MR2's [75.95, 85.25] and my 384096a8 §10 band.
- MR2's upper bound uses the μ₁ = 0 locus, where Δ = X₂ = X₀. Mine uses the μ₀ = 1 section. For MN2 they coincide, since X₀ = X₂.
- **Bolza value: PROVED (computer-assisted, PP 384096a8)**, not merely a citation (OW 36683379 regrade). MR2's "Bolza value CONDITIONAL (lit.)" can be upgraded on that basis.

## 10. (ix) Self-flags and erratum — PROVED
- **Edge-refinement slip confirmed.** The log's 182-point refinement returns 511.8079596 / 6.349604, which are the β → π/2 edge values (my 384096a8 approach: 511.8079 / 6.3496). The maximum is on the β → 0 edge.
- **Header times again run later than mtimes.** The md says "~18:15" (mtime 18:11:05) and the erratum says "~18:20" (mtime 18:11:17).
- **Stale banner.** The log banner reads "== MR2 adoption blockers: Riemann / systole / full EOM ==", copied from the 9ab8f0a6 routines. Cosmetic.
- **Erratum E-1 (REFUTED → OPEN for "warping lengthens the systole") is correct.** The lower bound 75.95 at μ₁ = 1 needs the curve to close in the twisted φ₁ circle, so it is not attained in general, and neither direction is proved. This agrees with my 384096a8 label (OPEN) and OW 19a88b19.

## 11. (x) Tallies
- **Main file "9 / 6 / 2 (+junction) / 2" — reproducible only under an unstated counting convention.** It requires V1 and V2 counted as two PROVED, the three CONDITIONAL parts of the magnitudes row (normalisations, measure) merged into one, and the two "proved at samples / global CONDITIONAL" rows counted as PROVED (stated). Counting table rows directly gives PROVED 8, CONDITIONAL 7, OPEN 2 (+1), REFUTED 2. **Fix:** state the convention.
- **Erratum "9 / 6 / 3 / 1"** is consistent with the main file's convention after moving one REFUTED to OPEN. PROVED.
- **Regrades under OW 36683379 (math checked):**
  - Bolza value CONDITIONAL → PROVED (PP computer-assisted).
  - Normalisations → PROVED (Dirac consistency).
  - (ii) NEC implication CONDITIONAL → PROVED (given thin-wall Israel and E₈+M5 content).
  - This gives about 12 / 3 / 3 / 1 in MR2's convention. LOSW form and E₈ identification stay CONDITIONAL; measure CONDITIONAL.

## 12. Verdicts (adopt nothing)
| item | verdict |
|---|---|
| (i) one-sided limits = MN2 bulk, ℓ_p²√Riem² ≤ 0.02365 | **PROVED at sampled points**; global max and exact-MN2-near-wall premise CONDITIONAL |
| (ii) Israel δ: −6k / 0 / −8k, ∫R = 16k (≤ 2e-4) | **PROVED** |
| (ii) 6:8:8 stress violates NEC along fibre and Σ; no E₈+M5 source can supply it (fe0c3d92 Y3-ineq, NL Y5) | **PROVED** (given thin-wall Israel and E₈+M5 content); consistent |
| (iii) 1/ε² scaling and coefficients; 4kℓ_p = 0.101–0.114 | **PROVED** |
| (iii) "bounded only if ≥ ℓ_p thick" | **CONDITIONAL, reworded**: finite for every ε > 0; sugra control needs ε_y ≳ ℓ_p (derivative expansion); thickness premise OPEN |
| (iv) C1 smooth isometric fixed locus | **REFUTED** (confirmed); HW-orbifold compatibility with f825dfff PROVED |
| (v) N and wall charge | **PROVED: N = 4880 exactly, charge 9760** (4879.95 is quadrature error); E₈ identification CONDITIONAL (HW 9603142, title verified) |
| (vi) φ₂ reflection | isometry and G₄-odd **PROVED**; fixed set = AdS₅ × (S³ bundle over Σ); physics (HW tr F² = ½ tr R² condition) **OPEN** |
| (vii) controls | validations and sign/location controls **PROVED** discriminating; Bianchi residuals are bookkeeping |
| (viii) Bolza systole 75.95–85.25 ℓ_p | **PROVED**, consistent |
| (ix) self-flags and erratum relabel | **PROVED** |
| (x) tallies | convention-dependent (fix); erratum consistent |
| junction for MN N=2 | **OPEN/UNSOLVED** (carried; this check confirms the required S_ab, it does not solve it) |
| localized backreaction; wall micro-structure below ℓ_p | **OPEN** |

## 13. Fixes needed from MR2 (future additive file)
1. N = 4880 exactly and wall charge 9760 exactly. The flux integral is π² to 2.4e-15; replace the 1e-5 quadrature value.
2. (iii): replace "bounded only if ≥ ℓ_p / reaches 1 at 0.114 ℓ_p" with "finite for every ε; sugra control requires ε_y ≳ ℓ_p (derivative expansion (kℓ_p)(ℓ_p/ε_y)^m); thin-wall limit divergent".
3. (ii): the NEC deficit holds along t+Σ as well as t+fibre. State the no-go via fe0c3d92 Y3-ineq with the general |F(k,·)|² and upgrade it to PROVED (given thin-wall Israel and E₈+M5 content).
4. C3: the fixed set is AdS₅ × (S³ bundle over Σ, twisted by φ₁), not AdS₅×Σ×S³. Add the HW boundary-condition requirement (tr F² = ½ tr R² on the plane), since "no Israel stress" is not "no source".
5. Global maximum: the supremum is 3408.000 with max|eig| = 40/3 at β → 0 (PP 384096a8 §8). Rerun the edge refinement on the correct edge.
6. N_req measure: include or discuss the x-block warp (wF₀)², which shifts the ratio by a factor of 0.84–1.34.
7. Relabel the Bianchi 9760/19520 "controls" as bookkeeping. Report δ-weights as KINK − NO_SOURCE and state the integration window, since the raw baseline depends on it.
8. Under OW 36683379: Bolza value → PROVED (PP computer-assisted); normalisations → PROVED (Dirac consistency); LOSW form unneeded for V2.
9. State the tally counting convention.
10. Cosmetics: header times later than mtimes (recurring), and the stale log banner.

No NL fixes in this scope. NL Y3/Y5 are consistent with this check.

## 14. Rollup
- **PROVED 18:**
  - OW 19a88b19; OW 36683379; MR2 file hashes; tip
  - (i) at sampled points; (ii) Israel δ; (ii) NEC no-go; (iii) scaling; (iii) physical arithmetic
  - (iv) HW-compatibility logic; (v) N = 4880 / 9760; (vi) isometry and parity / fixed set
  - (vii) controls; (viii) systole band; (ix) self-flags and erratum
  - N_req arithmetic; normalisation consistency; Bolza value
- **CONDITIONAL 5:** (i) global max and near-wall premise; (iii) thickness grading; E₈ identification; N_req measure; LOSW form.
- **OPEN 4:** C3 physics; localized backreaction / micro-structure; warping vs systole; junction (carried).
- **REFUTED 1:** C1, the smooth isometric fixed locus.
- **PENDING 0. Total 28.**

No CERT. Nothing adopted. Nothing sent.
