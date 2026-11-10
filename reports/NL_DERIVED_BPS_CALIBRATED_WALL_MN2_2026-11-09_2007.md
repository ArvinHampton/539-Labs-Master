# NL DERIVED: BPS / calibrated ℤ₂ wall on MN N=2 — Killing-spinor sector, first-order junction, and the K7 loophole
2026-11-09, 20:07 CST (America/Chicago). **NL derived proposal.** Nothing here is adopted. Junction status: **UNSOLVED** (19a88b19), unchanged.
Authority: **OW t4426 d5eaeef3** ("Pursue all open"; item 1, BPS/calibrated-wall search). Also OW 90cec14c, 9bb1858c, b0b9ae7f, f825dfff (odd HW-type ℤ₂, N_M5 + n_inst = 2N_flux = 9760), 7ff8299d (Σ = Bolza), 8b26c786/49b04146 (KK Group A scope), 3f160803 + 36683379 (citations: math checked; a citation never makes a claim PROVED), f1d167d1 (nomenclature; the resonant algebra is not used in this file).
Inputs: NL 1948 KK counting (9a29b6da…) and PP audit FINDINGS_PP_AUDIT_NL_JSC_KK_OPERATOR_COUNTING_9a29b6da_2026-11-09_1956.md (K6 → OPEN; **K6′: expected dimension ≤ −(1 + n_rel) ≤ −2, CONDITIONAL** — used here as the deficit a BPS wall would have to remove); NL 1943 truncation status; NL Y15 1955 and PP audit FINDINGS_PP_AUDIT_NL_Y14_STAGE2_Y15_FIBRE_ISRAEL_2026-11-09_1953.md (I2 + Y15-IR stand; I1 needs the no-x-legs hypothesis); PP C6 (FINDINGS_PP_AUDIT_NL_t4407_…_1935 §1.2; clarification …GARBLED_LINES_…_1958).
Source: Cheung–Gauntlett–Rosen, arXiv 1906.08900 (CGR), eqs. (2.5), (3.1), (3.3), (3.7), (3.8), (5.15)–(5.22), (6.1), (6.2), read from /workspace/pp-audit-kk/cgr.txt. Bergshoeff–Kallosh–Van Proeyen hep-th/0007044 (BKV) cited for the sign-flipping-W mechanism only (not re-derived; see B2).
Scripts: /workspace/nl-bps-2002/ — w_superpotential.py a3921623… / .log a7c88fe3…; bps_wall_faces.py 96916231… / .log 8de6c3c6…; c6_check.py cbdc1dfa… / .log 2f243aec…; each with a .sha256 sidecar.
Limits: new files only. No CERT, no Gemini, no external sends, no agent messages. Tip 7cddb188… checked before and after.

**Tally: PROVED 8 · CONDITIONAL 4 · OPEN 1 · REFUTED 0 · total 13**

**Wall-source hypotheses, carried as separate branches (Owner has NOT decided):**
- **[χU] χ-uniform:** wall sources (M5 + instanton density) uniform on S⁴ w.r.t. the round measure, so P := ⟨μ₁² + μ₂²⟩_n = 2/5.
- **[χS] χ-smeared:** any density n(χ) ≥ 0 on S⁴ with ∫n = 9760, so P ∈ [0, 1]; includes the pole-localised limit P = 0 (sources at μ₁ = μ₂ = 0).

## 1. Superpotential and Killing-spinor sector of MN2
- **B1 (PROVED; w_superpotential.py, exact sympy).** In the CGR (φ, λ) sector (ψ = 0, T_αβ = δ, L = R − 30(dφ)² − 30(dλ)² − V, V from (3.8)):
  - W = (g/2)[e^{−2φ}(2e^{−6λ} + 3e^{4λ}) + l e^{−8φ+6λ}] = (g/2)[e^{−2φ} Tr T + l e^{−8φ+6λ}] satisfies **V = (1/30)|∂W|² − (4/3)W²** identically.
  - Derivation of the normalisation: 1D Lagrangian e^{4A}(12A′² − 30X′² − V) for ds² = dr² + e^{2A}dx²; Hamiltonian constraint V = 30X′² − 12A′²; the ansatz A′ = −W/3, X′ = W_X/30 closes. The script checks that the first-order system implies both scalar equations and the A equation (residuals 0).
  - Within the three-exponential ansatz the only solutions are ±W.
  - For l = −1: ∇W = 0 exactly at CGR (6.1) (e^{30φ} = e^{10λ} = 2), W* = 3·2^{1/3}g/2, and A′ = −1/L gives g²L² = 2^{4/3} = CGR (6.2).
- **B2 (CONDITIONAL; on W being the gravitino-shift superpotential, not only a "fake" one).** Under this hypothesis:
  - MN2 carries the full 16 supercharges of 5D N = 4 (8 Poincaré + 8 superconformal; CGR §6.1 calls the vacuum maximally supersymmetric; citation only).
  - W-flows and any constant-r wall can preserve at most the **8 Poincaré** supercharges (projection γ_r ε = ±ε). The 8 superconformal ones are not γ_r-eigenspinors of fixed sign and are broken by any wall at finite r.
  - The odd HW-type ℤ₂ projection (Γ^{n}ε = ε on the wall) is compatible with those 8 iff W flips sign across the wall (BKV mechanism; in our language G₄ odd, flux N → −N, jump 2N = 9760 per f825dfff).
  - Evidence, not proof: W = (g/2)(Σ² + …) has the h^I P_I form of CGR's N = 2 subtruncation (5.15)–(5.22): with w = 0, Σ² = e^{−2φ−6λ}, Σ^{−1}Ω^{−1} = e^{−2φ+4λ}, Σ^{−1}Ω^{−1}e^{2ϕ} = e^{−8φ+6λ} (the l-term). Its critical point is the known supersymmetric vacuum. I did not compute the moment-map normalisations or the 11D Killing spinors.
- **B3 (PROVED; exact eigenvalues).** Linearised W-flow at MN2: δX′ = (1/30)Hess W · δX has exponents **−2/L** (eigenvector δφ : δλ = −3 : 1; this is the Δ = 6 mode on its source branch z^{4−Δ}) and **+2/L** (eigenvector 1/3 : 1; the Δ = 2, BF-saturated mode).
  - With A′ = −W/3 < 0, r → +∞ is the IR. So **IR-regular BPS flows into MN2 form a single curve** through MN2 (two branches), modulo r-shifts: dimension 1 in the 2D field space.
  - This is consistent with K1/K2: Δ = 6 costs 1 and Δ = 2 costs 2 at second order. BPS fixes the Δ = 6 vev branch automatically.
  - Traced toward the UV (bps_wall_faces.log): branch −1 runs to large φ with λ → 0 (W → 0⁺); branch +1 runs into a singular region (W changes sign). Neither branch is needed below.

## 2. First-order (BPS) ℤ₂ junction in the level-0 sector
- **B4 (PROVED).** Add a wall −∫√h T(φ, λ) at r_w with the IR side kept and the ℤ₂ image. From the 1D action, [A′] = −T/6 and 60[X′] = T_X. With ℤ₂ ([Y′] = 2Y′(r_w⁺)) and a W-flow on the kept side:
  - **T = 4W and ∇T = 4∇W at (φ_w, λ_w).**
  - Positive tension ⇔ W(φ_w, λ_w) > 0, consistent with the IR side kept.
  - **K7 mechanism, made explicit:** if T ≡ 4W identically, all three junction conditions and the Hamiltonian constraint hold at every point of every W-flow. The wall set is then the whole field space. Its intersection with the 1D IR-regular BPS curve (B3) is 1-dimensional (the wall position): non-negative, against the second-order expectation of K6′ (≤ −2). So such a wall would make **4** conditions dependent and remove the K6′ deficit completely.
- **B5 (PROVED; scaling lemma).** Use the 11D metric of CGR (2.5)+(3.1): the x-block is Δ^{1/3}e^{−4φ}g₅, the Σ-block is Δ^{1/3}e^{6φ}, and the S⁴ block g^{−2}Δ^{−2/3}T^{−1} has no φ. Any wall constituent that fills ℝ^{1,3}, with positive energy and no x-legs (Poincaré; PP's I1 hypothesis), then has a 5D effective tension of the form c·e^{aφ}F(λ) with **c ≥ 0 and a ≤ −2**:
  - an object wrapping x and p of the Σ directions: a = −8 + 3p (−8, −5, −2);
  - YM energy ½|F|² on the 10D wall: a = −2 (fibre legs only, which includes instantons self-dual on the S⁴ 4-planes); a = −8 (one Σ leg); a = −14 (two Σ legs, e.g. the twist legs Φ·F_tw);
  - smeared M5 on x×Σ at any S⁴ point: a = −2, F(λ) ∝ P e^{−6λ} + (1 − P)e^{4λ}.
- **B6 (PROVED, scope: level-0 (φ, λ) sector, wall content as in B5; its supersymmetric reading rests on B2).** For Σ = H²/Γ (l = −1, Bolza included), **no first-order (BPS) ℤ₂ wall with the IR side kept exists, in either branch [χU] or [χS].**
  - Proof: the φ-condition of B4 combined with T = 4W gives Σ_i c_i(a_i + 2)e^{a_iφ}F_i = 4(W_φ + 2W) = −12gl e^{6λ−8φ} = **+12g e^{6λ−8φ} > 0**.
  - By B5 the left side is ≤ 0. The obstruction is independent of P, the smearing profile, and the n_inst/N_M5 split.
  - Flat-Σ check (l = 0): W_φ = −2W identically, and the λ-condition forces P = 2/5 exactly (round-uniform), with the tension fixed by W (tension = charge). This **reproduces PP C6**: a BPS M5 wall exists for flat Σ only, and it fails on H² by exactly the Σ-curvature term l e^{−8φ+6λ}.

## 3. 11D check against Y15 (pointwise k_v ≤ k_x)
- **B7 (PROVED; exact identity in bps_wall_faces.py).** On the uplift of **any** point of **any** W-flow, take the unit normal into the kept side and any χ. Then
  - **k_Σ − k_x = (−l g/2) Δ^{−1/6} e^{2φ} e^{6λ−8φ}**, which is **> 0 for l = −1**.
  - Hence S(ℓ, ℓ) = −(2/κ²)(k_Σ − k_x) < 0 for ℓ = t̂ + ê_Σ: every BPS face in this sector violates the NEC along Σ, pointwise on S⁴.
  - By PP's I1 (given no x-legs) no YM + M5 content of either sign of σ can source it, and no σ ≥ 0 / NEC-respecting matter can source it at all.
  - This is the 11D form of B6 and of Y15's requirement. The grid check (any φ, λ ∈ [−0.6, 0.6]) gives min(k_Σ − k_x) = +5.6×10⁻⁴ > 0.
- **B8 (CONDITIONAL; floating point).** On sampled faces along both branches of the IR-regular BPS curve (bps_wall_faces.log), k_v ≤ k_x also fails in **every fibre direction** (χ, the SO(2) circle, the SO(3) S²), with margins ≈ −0.5 to −0.7 (g = 1 units) near MN2. So the BPS faces fail PP's escape condition "k_v ≤ k_x pointwise for every Σ and fibre direction" in all directions, not just along Σ.
- **B9 (PROVED; exact).** No face of the uplifted CGR (φ, λ) sector, BPS or not, has pure smeared-M5 Israel data (P_fib = 0 in every fibre direction and P_x = P_Σ). The conditions are 5h = 0, 5f − a = 0 and 2f + h − 4a = 0 (with a = A′, f = φ′, h = λ′), whose only solution is a = f = h = 0, i.e. no wall.
  - So K4's C4 face data (k_fib = −2k_x, k_Σ = k_x) **require fields outside the CGR truncation**, namely the S⁴ breathing mode. This is consistent with 1943 T3.
- **B10 (CONDITIONAL, on identifying 5D tension components with the 11D null-energy measure).** The minimal completion that makes T ≡ 4W is a positive M5-type part 2g e^{−2φ}Tr T (P = 2/5, i.e. [χU]) **plus a negative-tension part 2gl e^{−8φ+6λ}**.
  - At MN2 values: T_pos = 8·2^{1/3}g, T_neg = −2·2^{1/3}g, so **|T_neg| / T_net = 1/3**. This coincides with (saturates) the null-energy deficit bound Σ|σ_neg| ≥ ρ_w/3 of aeb9ab13 / MR2 batch-1 L3.
  - This quantifies PP's escape item "σ < 0" (077e417d): a BPS wall needs a negative-tension source equal to one third of the net tension. No known M-theory object supplies it (MO5 REFUTED earlier).

## 4. Independent check of PP C6 (citation checked, per OW 36683379)
- **B11 (PROVED; c6_check.py, exact sympy, all 11 diagonal components).** Setup: ds² = H^{−1/3}(dx₄² + dΣ²) + H^{2/3}(dr² + dy₄²), H = H₀ − cr, G₄ = qH′ dy¹²³⁴.
  - **Flat Σ:** every residual ∝ c²(q² − 1), so the equations hold iff **q² = 1**.
  - **Σ = H²** (ds² = (ds₁² + ds₂²)/s₂²): at q² = 1 the Σ components fail by exactly **−1/s₂²** (the Σ curvature); all other components vanish.
  - The off-diagonal Ricci components vanish because the metric is a warped product.
  - On constant-r faces k_Σ = k_x = c/(6H^{4/3}) and k_T/k_x = −2.
  - PP C6 is confirmed as stated (flat Σ only). B6 is the same obstruction for the full CGR (φ, λ) system, including the twist.

## 5. Beyond the level-0 class
- **B12 (OPEN).** χ-dependent BPS walls in the T7 sector are **not excluded**. This covers walls involving the S⁴ breathing mode (needed for C4 data, B9), non-round n(χ) in [χS] (which sources χ-dependent harmonics outside the truncation), and the pole-localised configuration P = 0 (probe M5s at μ₁ = μ₂ = 0 are the natural calibrated candidates; with backreaction 2N they are not probes).
  - Not done: the 11D Killing-spinor equations for cohomogeneity-two (r, χ) configurations with the HW projection.
  - **Necessary conditions any such wall must meet:** (i) Y15/PP, k_v ≤ k_x pointwise for every Σ and fibre direction, or an NEC-violating source; (ii) it must evade the B6/B7 mechanism, where Σ curvature enters the first-order equations with the sign that pushes k_Σ above k_x. In the level-0 sector this is exact; whether χ-dependence can reverse it is the open question.
  - In the level-0 sector all χ-dependence of the sources enters only through P, and the obstruction is P-independent.

## 6. K7 verdict and count
- **B13 (CONDITIONAL; the count is exact for the level-0 ODE system, and its extension to the full T7 sector is heuristic, like K6′).**
  - **[χU]:** in the level-0/cohomogeneity-one class **no BPS wall exists** (B6, B7). **0 constraints become dependent.** The K6′ deficit ≤ −(1 + n_rel) ≤ −2 stands as PP graded it (CONDITIONAL). K7 is closed in this class and OPEN beyond it (B12).
  - **[χS]:** same in the level-0 class, since the obstruction is P-independent: **0 dependent constraints**. Beyond it, K7 is OPEN (B12).
  - **What a BPS wall would do if one existed** (B4): it would make 4 conditions dependent and turn the expected dimension from ≤ −2 into +1 (the wall position), closing the count deficit. The minimal way to get one is the NEC-violating completion of B10.
  - The size of the count gap (Y14 stage 2) is unaffected. No item here changes it.

## 7. Junction and gap impact
- K7 is **not** resolved positively. The simplest BPS loophole is obstructed in the full level-0 sector (not only C6's harmonic ansatz), in both source branches. The obstruction is the Σ (Bolza) curvature, with sign fixed. The route is **not** "generically closed": K6 is OPEN, K6′ is a heuristic, and χ-dependent BPS walls (B12) remain OPEN.
- **Junction: UNSOLVED (unchanged). Count gap: unchanged.** Nothing is adopted.
- Lightest next steps: (a) settle B2 by computing CGR's N = 2 moment maps (P_I) and the gravitino shift in the (φ, λ, w) sector, about 30 min; (b) for B12, linearise the 11D Killing-spinor equations around MN2 in the T7 sector with the breathing mode and test whether a χ-dependent first-order wall can flip the sign in B7, about 2–3 h.

## 8. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 8 | B1, B3, B4, B5, B6, B7, B9, B11 |
| CONDITIONAL | 4 | B2, B8, B10, B13 |
| OPEN | 1 | B12 |
| REFUTED | 0 | — |

Check: 8 + 4 + 1 + 0 = 13.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
