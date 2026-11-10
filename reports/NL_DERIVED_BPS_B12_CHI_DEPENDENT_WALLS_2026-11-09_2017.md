# NL DERIVED: B12 — χ-dependent BPS ℤ₂ walls on MN2/Bolza: an 11D HW-BPS junction identity, a near-MN2 (linearised) no-go, and what stays open
2026-11-09, 20:17 CST (America/Chicago). **NL derived proposal.** Nothing adopted. Junction: **UNSOLVED** (19a88b19), unchanged.
Authority: **OW t4426 d5eaeef3** ("Pursue all open"). Follow-up to NL_DERIVED_BPS_CALIBRATED_WALL_MN2_2026-11-09_2007.md (704df3ee…) item B12, and to NL_DERIVED_BPS_B2_SUPERPOTENTIAL_CHECK_2026-11-09_2012.md (89ec258a…). Also OW f825dfff, 7ff8299d, 19a88b19, 90cec14c, 3f160803 + 36683379 (citations: math checked), f1d167d1 (the resonant algebra is not used here).
Respects: PP Y15 audit (…_1953, 077e417d escape list: k_v ≤ k_x pointwise or an NEC-violating source); PP KK audit (…_1956): K6 OPEN, **K6′ ≤ −(1 + n_rel) ≤ −2** CONDITIONAL is the deficit; PP C6 (flat Σ only).
Scripts: /workspace/nl-bps-b12-2015/ — hw_bps_identity_c6.py e3b71810… / .log e0f57add…; level0_hw_trace.py 698c4f8e… / .log f05a9483…; each with a .sha256 sidecar.
Limits: new files only. No CERT, no Gemini, nothing sent, no agent messaged. Tip 7cddb188… checked before and after.

**Tally: PROVED 4 · CONDITIONAL 2 · OPEN 1 · REFUTED 0 · total 7**

**χ branches:** **[χU]** χ-uniform sources (P = 2/5); **[χS]** any n(χ) ≥ 0, including pole-localised. D1–D4 are pointwise in χ and independent of the wall content, so they hold in both branches. D5–D7 are stated per branch.

**Scope of the "linearisation".** The request was to linearise the 11D Killing-spinor equations (KSE) in (r, χ) about MN2, breathing mode included. What I did:
- derived the *exact* (nonlinear) jump condition that the 11D KSE impose at a HW-type ℤ₂ wall (D1);
- evaluated it at and near the exact MN2 face (D4; this is the linearised statement);
- evaluated it on every level-0 face (D3).

I did **not** solve the bulk KSE for χ-dependent backgrounds at finite amplitude (D6, OPEN).

## 1. The HW-BPS junction identity
- **D1 (PROVED: derivation plus an exact check on C6).**
  - **Hypotheses:**
    - (i) 11D KSE ∇_Mε + (1/288)(Γ_M^{NPQR} − 8δ_M^NΓ^{PQR})G_NPQR ε = 0 on both sides;
    - (ii) the ℤ₂ acts as r → −r, C → −C, ε(−r) = Γ_n ε(r), with ε continuous and nonzero at the wall, so Γ_nε = ±ε there;
    - (iii) wall sources enter only through the modified Bianchi identity, so there is no δ-localised G, as in HW;
    - (iv) 4D Poincaré: G has no x-legs and K^x_x = k_x is isotropic (PP's I1 hypothesis).
  - **Derivation.** The tangential spin connection jumps by K_abΓ^bΓ^n. The tangential G (odd) jumps by 2G|₀₊, while the normal-leg G (even) is continuous. Matching the jumps gives, for every tangential a,
    **K_abΓ^bε = −σ(1/144)(Γ_a G̸ − 12Γ^{cde}G_acde)ε**, with G̸ = Γ^{bcde}G_bcde over tangential G only and σ = ±1 a convention sign.
  - **Check (hw_bps_identity_c6.py, explicit 32×32 Clifford algebra).** C6 face data (k_Σ = k_x, k_T = −2k_x, G₇₈₉₁₀ = −6q k_x) give an **8-dimensional** solution space for all q = ±1, σ = ±1 and Γ_nε = ±ε (1/4-BPS, as expected for M5 + HW).
  - **Controls:** k_T = −1.5k_x (non-BPS) gives 0 solutions. The exact-MN2-type face (k_Σ = k_T = 0) with G = 0 gives 0 solutions.
- **D2 (PROVED; consequence of D1, independent of G, pointwise in χ, any wall content).**
  - The x-row gives G̸ε = −144σ'k_xε.
  - Contracting the internal rows with Γ^a gives tr_int(K − k_x h) = −12k_x. Hence:
    - **K_int = −6k_x**, K = −2k_x;
    - ρ = 6k_x/κ²;
    - mean internal pressure = −ρ/3.
  - So **every** supersymmetric HW-type wall has the C4/K4 trace pattern pointwise on S⁴: a pure-tension-like average, with the trace fixed by k_x.
  - The wall NEC (Y15: k_v ≤ k_x for all tangential v, including off-diagonal terms) is the matrix condition M := (K − k_x h)|_int ≤ 0. Since tr M = −12k_x, it needs **k_x ≥ 0**, i.e. non-negative tension.

## 2. Where D2 rules walls out
- **D3 (PROVED; exact, level0_hw_trace.py).** On the uplift of the CGR (φ, λ) sector, (K_int + 6k_x)/ε = 6A′ − 6φ′ + ½λ′∂_λ lnΔ.
  - ∂_λ lnΔ runs from −6 at χ = 0 to +4 at χ = π/2, so the identity holds pointwise in χ only if **λ′ = 0 and A′ = φ′** at the wall.
  - On W-flows this means W_λ = 0 and W_φ = −10W. With X = e^{−6φ+12λ} and v = e^{10λ} these become −6X + 12v − 12 = 0 and −2X + 24v + 16 = 0, whose only solution is v = −1 < 0. **No solution exists.**
  - So **no face of any W-flow in the level-0 sector can be a supersymmetric HW wall, whatever the wall content** (negative tension included). The exact MN2 face also fails: K_int + 6k_x = 6k_x = −6ε/L ≠ 0.
  - This is an 11D proof of 2007 B6 that needs neither B5's σ ≥ 0 nor the 5D effective-tension description. It also shows that the 5D negative-tension completion of 2007 B10 has **no** 11D HW-type realisation in the level-0 sector.
- **D4 (PROVED; the linearised statement, any sector including the S⁴ breathing mode and any χ-dependence, any content).**
  - At the exact MN2 IR face, k_x = −ε/L < 0 and K_int = 0 (with ε = Δ^{−1/6}e^{2φ} > 0), so K_int + 6k_x = −6ε/L.
  - Take any face (constant-r or a χ-dependent embedding) whose extrinsic curvature is within δ of the MN2 face, uniformly on S⁴. Then |K_int + 6k_x + 6ε/L| ≤ 10δ and k_v − k_x ≥ ε/L − 2δ.
  - For **δ < (3/5)·min_{S⁴}ε/L**, D2 fails, so the face is not supersymmetric. For δ < ½min ε/L the NEC fails in every tangential direction (Y15/PP).
  - Hence **linearising about MN2 cannot produce a BPS ℤ₂ wall**: the mismatch is already zeroth order. Any BPS wall must sit at finite distance from MN2, with **k_x ≥ 0 at the wall although k_x < 0 near the IR**, so the 11D x-warp must turn around along every normal ray between the wall and the IR.

## 3. The Σ-row (the B5/B7 mechanism, general form)
- **D5 (CONDITIONAL, on H_Σ: fields constant on Σ up to the twist (KK Group A), no single-Σ-leg G at the wall, K Σ-isotropic with K_{Σv} = 0).**
  - With ω_ij := G_{Σ₁Σ₂ij} (the twist flux, two Σ legs), the Σ-rows of D1 give
    **(k_Σ − k_x)ε = −σ·½Γ^{Σ₁Σ₂}ω̸ε**, with ω̸ = Σ_{i<j}ω_ijΓ^{ij} (direct algebra: the Σ-row contraction gives 12Σ_{i<j}G_{12ij}Γ^{12ij}).
  - So the NEC along Σ (k_Σ ≤ k_x) holds iff the twist flux at the wall has a definite sign relative to the spinor's twist projection.
  - In the level-0 sector this sign is fixed by l and is the wrong one: 2007 B7, k_Σ − k_x = (g/2)ε e^{6λ−8φ} > 0 for l = −1.
  - Whether χ-dependent T7 configurations (breathing mode, non-round n(χ)) can reverse it is not determined here. It needs the twisted Killing spinor's Γ^{Σ₁Σ₂} eigenvalue and ω at the wall.

## 4. Verdict
- **D6 (OPEN).** Finite-amplitude, χ-dependent supersymmetric ℤ₂ walls on Bolza are **neither found nor excluded**, in both [χU] and [χS].
  - **A candidate must satisfy all of the following:**
    - (a) D1/D2 pointwise on S⁴ (K_int = −6k_x);
    - (b) k_x ≥ 0 at the wall and finite distance from MN2 (D4);
    - (c) the D5 sign reversal relative to level-0, or else an NEC-violating source (PP 077e417d);
    - (d) M ≤ 0 (Y15) if the content is YM + σ ≥ 0 M5s;
    - (e) a bulk solution of the 11D KSE in (r, χ) that joins it to the IR-regular BPS set of MN2.
  - Level-0 W-flows fail (a) everywhere (D3). The breathing-mode (C4) face satisfies (a) in trace by construction (K4), but no bulk BPS solution reaching it has been exhibited.
  - Not done: the nonlinear (r, χ) KSE system, which is a PDE problem. Estimate ≥ 4–6 h, with no guaranteed decision.
- **D7 (CONDITIONAL; the counting inherits K6′'s heuristic status).** K7, per branch:
  - **[χU]:** in every class decided here (level-0 sector; any configuration near MN2) **no BPS wall exists, so 0 constraints become dependent**. The K6′ deficit ≤ −2 stands. Beyond these classes, OPEN (D6).
  - **[χS]:** same; D3 and D4 are profile-independent. **0 dependent constraints** in the decided classes; OPEN beyond.
  - A BPS wall, if one existed, would remove the deficit (2007 B4: 4 conditions become dependent).

## 5. Junction / gap impact
- No change. **Junction UNSOLVED; count gap unchanged.** The route is not called "closed": D6 is OPEN and K6′ is heuristic. Nothing adopted.

## 6. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 4 | D1, D2, D3, D4 |
| CONDITIONAL | 2 | D5, D7 |
| OPEN | 1 | D6 |
| REFUTED | 0 | — |

Check: 4 + 2 + 1 + 0 = 7.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
