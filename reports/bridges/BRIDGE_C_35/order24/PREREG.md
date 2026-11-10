# PREREG order24 — γ-orbit maps RG12 (γ-average) and RG13 (γ-defect)
Written 2026-10-24 (America/Chicago) BEFORE any order24 numerics. CORE_FREEZE. MAPS_CANDIDATES untouched; no Resonant objects. Inputs read-only: order18 a2_arrays.npz (CO, SCO), order23 scripts/cornerlib.py (corner formula, copied). k := 35^{−1/2}. Cor_K as in paper v8 Prop. cor; Γ_g as in Prop. transport; K = R²_{≥0}.

## Objects (fixed)
- γ = [[−1,−7],[2,13]]; γK = cone((−1,2),(−7,13)); γ⁻¹K = cone((13,−2),(7,−1)). Both unimodular with Q(u1)=1, Q(u2)=7/2, B=7.
- One period of cones about K (symmetric): {γK, K, γ⁻¹K}.
- **RG12 object:** Avg := ⅓(Cor_{γK} + Cor_K + Cor_{γ⁻¹K}), computed directly from the corner formula at x and at −1/x.
- **RG13 object:** D := Cor_{γ⁻¹K} − Cor_K at x and at −1/x.
- Law ℒ (fixed, no fitted scalar): Y(−1/x) = x·kM·Y(x) on the 216 points x ∈ XS.

## Metrics and thresholds (absolute primary)
For Y ∈ {Avg, D}: a(Y) = ‖Y(−1/x) − x kM Y(x)‖_F; s(Y) = ‖Y(−1/x)‖_F. PASS iff a ≤ 1e−8 AND non-vacuous; FAIL iff a ≥ 1e−3·s; else inconclusive. Relative a/s and a fitted-κ relative residual reported (not used for the verdict).
Non-vacuity: RG12 requires ‖Avg − CO‖_F/‖CO‖_F ≥ 1e−3; RG13 requires ‖D‖_F/‖CO‖_F ≥ 1e−3 (γ moves the object; contrast σ = id in order23).

## Controls
- C1: corner formula on K reproduces CO and SCO (max abs ≤ 1e−9).
- C2: transport: Γ_γ CO = Cor_{γ⁻¹K} and Γ_γ⁻¹ CO = Cor_{γK} at x and −1/x (max abs ≤ 1e−9).
- C3 (reported): commutator ‖Γ_γ M − M Γ_γ‖_max. If 0, then a(Γ X) relates to a(X) by Γ and the γ-orbit cannot remove a law defect that Γ preserves; this is recorded as the structural reason, not as a verdict.

## Predictions
RG12 FAIL; RG13 FAIL (if C3 = 0, the defects are (Γ±…)-images of the CO defect, which is nonzero by order19).
Any pass is residual-internal geometry, not a Residual↔Resonant bridge. E1–E3 OPEN.
nice, OMP_NUM_THREADS=1, <3 GB; no push/sends; new files only.
