# PREREG order23 — corrected RG9b; geometric near-law RG10; σ-transport RG11
Written 2026-10-24 (America/Chicago) BEFORE any order23 numerics. CORE_FREEZE. MAPS_CANDIDATES untouched; no Resonant objects. Inputs read-only: order18 a2_arrays.npz (CO = A2_corner, and SCO at −1/x), order22 scripts (corner formula, copied). k := 35^{−1/2}. Corner_{(u1,u2)} as in order22 PREREG (half weights on rays, ¼ at the vertex).

## 1. RG9b corrected (vertex term)
K1 = cone(e1,(1,1)), K2 = cone((1,1),e2). Exact weights: on K's interior and on the ray (1,1) the two subcones add to 1; on the rays e1, e2 they give ½ as K does; at ν = 0 they give ½ against ¼. Hence
  Corner_{K1} + Corner_{K2} − ¼·[α ∈ Z²]·e(B(0,β)) = Corner_K,   with e(B(0,β)) = 1.
(the t^0 coefficient of a single point is its weight times its phase). Metric: max abs over 216×105. PASS ≤ 1e−12; FAIL ≥ 1e−9.

## 2. RG11 (σ-transport, residual-internal)
σ(ν) = (−ν1−7ν2, ν2) preserves Q and fixes ĉ′ (exact check in script). Γ_σ = monomial reduction matrix of (σα_j, σβ_j). Prediction: Γ_σ·CO = Corner_{σK}, σK = cone((−1,0),(−7,1)) (σ⁻¹ = σ). PASS: max abs ≤ 1e−9 and ‖Γ_σCO − CO‖/‖CO‖ ≥ 1e−3; "vacuous" if σ-covariant; FAIL ≥ 1e−6.

## 3. RG10 (primary, geometric near-law)
U := Corner_K + Corner_{σK} (the two orthant arcs about ĉ′ forming one unit arc), at x and at −1/x. Law (fixed in writing, no fitted scalar): U(−1/x) = x·kM·U(x).
Primary metric absolute: a10 = ‖U(−1/x) − x kM U(x)‖_F over 216 points. Non-vacuity: ‖U‖_F ≥ 1e−3‖CO‖_F (else "vacuous").
PASS iff a10 ≤ 1e−8 and non-vacuous; FAIL iff a10 ≥ 1e−3·‖U(−1/x)‖_F; else inconclusive. Secondary (reported only): relative residual with one fitted κ, compared with CO's 0.058 (order19).
Prediction: FAIL (σ commutes with nothing that would remove the P-even obstruction of Prop. noaffine on Q^×; on x>0 alone no prediction of closeness).
## Controls
C1: corner formula reproduces CO (≤1e−9). C2: Γ_σ·G = G for Gauss means (≤1e−12).
A pass of any map here is residual-internal geometry, not a Residual↔Resonant bridge. E1–E3 OPEN.
nice, OMP_NUM_THREADS=1, <3 GB; no push/sends; new files only.
