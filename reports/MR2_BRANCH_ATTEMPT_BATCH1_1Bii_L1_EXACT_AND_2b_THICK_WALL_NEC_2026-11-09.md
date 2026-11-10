# MR2 branch attempt (OW t4436): batch-1 branches B1-1b-ii (lemma L1, interval-certified) and B1-2b (thick wall ε_y = R_S4: null-energy lemma TW)
2026-11-09, written 22:03 CST (America/Chicago, box clock). Author: MR2. Additive; nothing edited; nothing adopted; no CERT, no Gemini, nothing sent, no agent messaged. Junction **UNSOLVED**. Register: MR2_BRANCH_REGISTER_ALL_OPEN_PATHS_PER_OW_t4436_2026-11-09.md (c5a65972…). Companion: MR2_BRANCH_ATTEMPT_BATCH2_PHI2_PHI3_W2_W3_G2_RC_MN2_RICCI_CLOSED_FORM_2026-11-09.md (04b94770…). **All grades are MR2's proposal, pending PP audit;** only a PP-audited PROVED/REFUTED keeps or drops a branch. Recommended 1a/2a are not adopted.

## Scripts and logs (/workspace/mr2-branch-2134/; each .py frozen with its sidecar before it ran; sha = sidecar; mtimes CST)
| file | .py sha256 | .log sha256 | .py → .log |
|---|---|---|---|
| L1_trRR_interval_2026-11-09_2200 | 7fee50e3dbbb2b4fb5752699453ff81a320a2f79d88d3428c1e4e86a8f55c210 | 4ef804a800a2014833be182d469f282f94bbb78e3e3df8ec045da0e553648877 | 21:55:17 → 21:55:19 |
| L1_trRR_validate_v2_2026-11-09_2157 (crashed: sin(interval)) | 9fa277665e1888c1684facc2bae99ec08d3eac586f096f6a062c26f05b93cca3 | 3fac0882d13b802b94067525eaf0e7ef61a9011f068dc7a1ffae97da96a36e24 | 21:56:11 → 21:56:11 |
| L1_trRR_validate_v3_2026-11-09_2158 | 9f79038d78f75d242de47d48c92b1c938b7479f9d2d14a5a9961fe7f421b8d66 | 18268d8dbb0d4f057ec01427a721b6fe6b6d9797d8b5e068fa4824625a93560c | 21:56:18 → 21:57:00 |
| TW_null_energy_2026-11-09_2201 | 19abe063f6bdb861b1433f5b05d5d77950f658b19a7e253c16ca27ee01f6d5d9 | 572db442dde7919ac77dd9c669ed910ba44c28e25184453aec024ddd1e6f4b0d | 21:59:50 → 21:59:53 |
Self-flags: (i) the hh:mm in the script names / "FROZEN" header lines are my estimates, up to 5 min ahead of the box clock; mtimes are authoritative. (ii) In the v3 log the second point's print label reads "(1,1,1/3,1/4)" (hard-coded); the actual point is (r, y, μ₁, μ₂) = (1, 1, 1/2, −1/5), as set in the script's PT list. (iii) Correction to the companion batch-2 file's tally sentence: its parenthetical "PROVED 9 (…)" list is garbled; the stated count **8/3/1/4 = 16** with the listed PROVED rows is the one to use.

Metric: the MN2 uplift of frozen 516438eb, in the (μ₁, μ₂) chart (as in the companion file). Interval arithmetic: mpmath.iv at 40 digits, radical constants evaluated as intervals.

## B1-1b-ii: lemma L1 (tr R∧R on the φ₂ fixed set F₁₀)
- **Validation of the Riemann routine:** applied to the full 11D metric at (α, β) = (1/3, 2/7) and contracted, it gives R ∈ [5.551455102913087315403678361125889151, …346582582], matching 516438eb (5.551455102913087315403678).
- **F₁₀ = {φ₂ ∈ {0, π}}** (μ₂ ∈ (−1, 1) real). Since g_{φ₂,·} has no off-diagonal entries (a₂ = 0), the induced 10D metric is the 11D metric with the φ₂ row/column removed (batch 1 §0). The Pontryagin 4-form is computed in **coordinate components** P_{cdef} ∝ Σ_{a,b}[R^a_{b cd}R^b_{a ef} − R^a_{b ce}R^b_{a df} + R^a_{b cf}R^b_{a de}] (Lorentzian kept; no frame needed).
- **Result:** at (r, y, μ₁, μ₂) = (1, 1, 1/3, 1/4), exactly one of 210 components has an interval excluding 0: **P_{x y μ₁ φ₁} = −1.16119299337891068720** (width < 10⁻³⁰). At (1, 1, 1/2, −1/5): **P_{x y μ₁ φ₁} = −2.10578925447730114**. All other components' intervals contain 0.
- **Grade:** "tr R∧R ≢ 0 on F₁₀" **COND → PROVED** (computer-assisted, interval; b964cad1 B1's upgrade path). L1's restriction argument was already PROVED (b964cad1 B1). "Pointwise nonzero everywhere on F₁₀" stays **OPEN**.
- **Consequence (b964cad1 B2):** "(b-ii) a nontrivial E₈ field F ≠ 0 is required" **COND → PROVED** (given the HW boundary condition tr F² = ½ tr R² pointwise). Not changed: E₈ connection existence COND; backreaction OPEN; (b-ii) with the 1a wall W REF given HW; P as the face REF.
- Consistency: P ∝ vol(Σ) ∧ dμ₁ ∧ dφ₁ at these points, as expected from the twist (a₁ = 1 couples Σ to φ₁). It is exact (L2, p₁(F₁₀) = 0), with zero integral over every 4-cycle (unchanged).

## B1-2b: thick wall ε_y = R_S4 — lemma TW
**Setting.** Near the face, g = e^{2ω(z)}ĝ with ω = (1/6) ln Δ(z) (z internal), ĝ = F(dρ² + e^{2A(ρ)}η_{μν}dx^μdx^ν) + ĝ₆(z), a product. MN2 bulk: A_ρ = ±1; the doubled kink has A_ρ going from +1 to −1 across the face. This is the configuration whose thin limit gives the batch-1 L3 deficit S(k,k) = −2k/κ².

**Premises.**
- **P-i:** inside the wall, ĝ₆ and Δ (hence ω) are unchanged; only A varies.
- **P-ii:** |A_s| ≤ k_s across the wall (e.g. any monotone interpolation). Here s is proper transverse distance at fixed z, so A_s = ±k_s in the bulk, with k_s = 1/√(Δ^{1/3}F) (ℓ units).

**Lemma TW (PROVED, as an implication of P-i and P-ii).** Fix z and take any g-null k = t̂ + ê with ê an internal unit vector. Then
- R_kk = A_ss + 4A_s² + C(z, ê), where C does not depend on A;
- hence ∫_wall (R_kk − R_kk^bulk) ds = −2k_s + 4∫(A_s² − k_s²) ds ≤ −2k_s;
- so if ε_s·R_kk^bulk(ê) < 2k_s, then R_kk < 0 somewhere on that transverse line. By the null Einstein equation κ²T_kk = R_kk, the **total** null energy is negative there. 11D flux stress obeys the NEC, so the wall must contain NEC-violating sources.

*Proof.*
- For the product ĝ, the Ricci tensor splits. R̂_{t̂t̂} (ĝ-unit) = F⁻¹(A_ρρ + 4A_ρ²), and R̂_{êê} = Ric(ĝ₆)(ê, ê) is A-independent.
- The conformal change gives R_ab = R̂_ab − 9[∇̂_a∇̂_bω − ∂_aω∂_bω] − (…)ĝ_ab. The last term drops on null k.
- ∂_ρω = 0, and in the product Γ̂^m_{tt}, Γ̂^m_{te} have no internal component. Therefore ∇̂_t∇̂_tω = ∇̂_t∇̂_eω = 0, and ∂_tω = 0. The ω-terms reduce to the A-independent ê-ê part.
- Rescaling to g-units at fixed z (a constant factor) turns F⁻¹(A_ρρ + 4A_ρ²) into A_ss + 4A_s².
- In the bulk, A_ss = 0 and A_s² = k_s². Integrating A_ss over the wall gives −2k_s, and P-ii makes the second term ≤ 0. Finally, R_kk^bulk is constant along the line. ∎

This reproduces, as MR2's own derivation under P-i and P-ii, the content previously carried only by citation from NL JS-A L5 (b964cad1 B5: "not rederived by MR2"). Thin limit: ε_s → 0 gives back L3's −2k.

**Numbers (PROVED, interval-certified; TW_null_energy log).** Take ε_s = R_S4 = ℓ/2 and ê = ∂_y/|∂_y| (the H² direction orthogonal to the twist), with R_kk^bulk = R_t̂t̂ + R_êê of MN2 (all bulk values > 0, as the flux NEC requires):

| (μ₁, μ₂) | k_s | R_kk^bulk(ê_y) | ε_sR_kk^bulk − 2k_s |
|---|---|---|---|
| (1/3, 1/4) | 1.27198 | 3.04553 | **−1.02120** |
| (9/10, 1/10) | 1.37380 | 1.20535 | **−2.14493** |
| (1/10, 9/10) | 1.26097 | 3.16413 | **−0.93988** |
| (1/10, 1/10) | 1.26097 | 3.16413 | **−0.93988** |

The other directions (μ₁, μ₂, φ₁, φ₂) give positive margins, which is not needed. The width threshold for forced violation along ê_y is ε_s < 2k_s/R_kk^bulk: **2.2795ℓ ≈ 113.3 ℓ_p** at (9/10, 1/10) and **0.8353ℓ ≈ 41.5 ℓ_p** at (1/3, 1/4) (ℓ = 49.684 ℓ_p).

**Consequences (MR2 proposal).**
- **B1-2b "a resolved wall of width R_S4 (24.84 ℓ_p) evades the NEC deficit" (with internal metric and Δ fixed): REFUTED, as an implication of P-i and P-ii.** The same holds for every width below ≈ 113 ℓ_p, which covers Rc-1 (1.60 ℓ_p) and the thin wall 2a.
- The identification "wall thickness = R_S4" itself stays **OPEN**: it is a definition, and nothing above refutes it as a thickness.
- A thick wall that **changes the internal metric or Δ** violates P-i. It is outside this lemma and belongs to 1a-T7 (NL lead), consistent with b964cad1 B5's 2c′ ("thickness is not the lever; changing face data is").
- Caveat, not covered: G₄ must flip sign across the wall (b964cad1 B5). P-i fixes the metric but does not fix how the flux stress is distributed. The lemma bounds the **total** null energy from geometry alone, so the flux distribution does not enter the conclusion. Whether a P-i metric is compatible with a sign-flipping G₄ at all is a further constraint, unchecked here; it can only remove configurations.

## Branch status changes (MR2 proposal; pending PP audit)
| branch | before | after |
|---|---|---|
| B1-1b-ii: L1 tr R∧R ≢ 0 on F₁₀ | COND | **PROVED** (interval) |
| B1-1b-ii: F ≠ 0 required | COND | **PROVED** (given HW) |
| B1-1b-ii overall | bulk orbifold, viable; face REF | unchanged: viable as a bulk orbifold. Next: E₈ embedding normalisation (~1 h) |
| B1-2b as NEC escape (fixed internal metric) | OPEN (via NL L5 citation) | **REFUTED** (implication of P-i, P-ii) |
| B1-2b identification ε_y = R_S4 | OPEN | OPEN |
| B1-2a / Rc-1 thin walls | Israel/L3 NEC deficit | also covered by lemma TW (consistent with L3) |

**Tally of this file:** PROVED 4 (routine validation, L1 ≢ 0, F ≠ 0 given HW, lemma TW) · COND 0 · OPEN 2 (L1 everywhere; 2b identification) · REF 1 (2b as NEC escape under P-i, P-ii) = 7. Plus the numbers table (PROVED, interval), counted inside "REF 1".

Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, untouched.
