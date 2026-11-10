# order31 PREREG (written and hashed before numerics)
Data: order30/data/o30_cones.npz (read-only), with 31 unimodular cones: K and the Stern–Brocot cones of depths 1–4 (30). Also order28 J1, J2 (γ⁻¹-images of K2, K1) for RG26.
Law family (same as used for CO in order29/30): r(w) = min_κ ‖S − κ x^{−w}35^{−1/2}MY‖/‖S‖, w ∈ {−1, −½, 0, ½, 1}; the best weight is w* = argmin r. The near-law is read at w = −1 (κ̂, r).
Non-vacuity span: W′ = span{CO, Γ_γCO, vtx} (vtx is the constant vertex vector at x and −1/x). Cone i counts as non-vacuous iff d′_i > 1e−3.
## RG25a: is the near-law generic?
Criterion per cone: w* = −1, |κ̂ − 1| ≤ 0.01, and r ≤ 0.10.
PASS (generic): all non-vacuous cones satisfy it. FAIL: more than 25% violate. Else inconclusive.
Prediction (based on the order30 observation, so not blind): PASS.
## RG25b: does the miss track the arc length?
Over all 30 depth-1..4 cones: Pearson ρ_p and Spearman ρ_s between r_i (w = −1) and ℓ_i = arccosh(uᵀAv/(2√(Q(u)Q(v)))).
Verdicts: "proportional" if ρ_p ≥ 0.9 and a through-origin fit r ≈ cℓ has relative residual ≤ 0.1. "Independent" if |ρ_s| ≤ 0.3. "Intermediate" otherwise.
Prediction (blind): independent.
Also reported: Spearman of r_i against log-depth and against max(|u|, |v|).
## RG26: Γ_γ transport invariance of the near-law (predefined consistency check)
Since Γ_γ is unitary, commutes with M, and Γ_γCor_C = Cor_{γ⁻¹C} (v9/v10), r and κ̂ are identical for C and γ⁻¹C.
Test on (K2, J1) and (K1, J2): |Δr| ≤ 1e−12 and |Δκ̂| ≤ 1e−12, PASS; > 1e−9 FAIL.
Prediction: PASS. This is a consequence of a proved result, not new evidence.
## Controls
C1 npz '(1, 0)_(0, 1)' = CO ≤ 1e−12. C2 ‖R(CO)‖ = 54.4056376674763. C3 L = arccosh(√3.5) = ½log(6+√35).
Naming: no labels L1–L7 used. Rules: geometric only; MAPS_CANDIDATES untouched; no Resonant objects; no bridge claim; E1–E3 OPEN; Ξ not identified.
