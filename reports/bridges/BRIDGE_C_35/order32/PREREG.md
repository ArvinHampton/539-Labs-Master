# order32 PREREG (written and hashed before numerics)
Near-law criterion (identical to order31 RG25a): law family r(w) = min_κ ‖S − κx^{−w}35^{−1/2}MY‖/‖S‖, w ∈ {−1, −½, 0, ½, 1}. Criterion: w* = −1, |κ̂ − 1| ≤ 0.01 and r(−1) ≤ 0.10.
Non-vacuity: d′ from span{CO, Γ_γCO, vtx} > 1e−3.
## Cone sets (fixed now; all unimodular with Q > 0 on the closed cone)
E (e1 = (1,0) is an edge ray):
- order31: ((1,0),(n,1)) for n = 1..4, from order30 data.
- new: ((1,0),(n,1)) for n = 5..8; ((1,0),(8,−1)); ((1,0),(9,−1)).
The cone ((1,0),(7,−1)) = hK is excluded, because it equals CO and so is vacuous.
C (control: e1 is not an edge, and the edge is not in the ⟨γ,h⟩-orbit of e1, which is {e1, (13,−2), (−1,2), …}):
- order31: all 26 depth-1..4 Stern–Brocot cones without edge (1,0).
- new: ((1,5),(0,1)); ((1,6),(0,1)).
G (transport images, a separate prediction): γ⁻¹ applied to ((1,0),(5,1)) and ((1,0),(6,1)), giving ((13,−2),(72,−11)) and ((13,−2),(85,−13)). Edge γ⁻¹e1 = (13,−2).
## RG27
PASS iff every non-vacuous cone in E satisfies the criterion AND every non-vacuous cone in C violates it. FAIL if either condition fails for more than 10% of its set. Else inconclusive.
Separate prediction RG27G: G cones satisfy the criterion, since by the v9/v10 transport r and κ̂ are equal to those of their E preimage to 1e−12.
Predictions: RG27 PASS, which is not blind for the 30 order31 cones (they were used to form the hypothesis). It is blind for the 8 new E cones and the 2 new C cones; the blind subset is reported separately. RG27G PASS (consistency).
## RG28 (residual direction across E)
Unit vectors û_C = R(Cor_C)/‖R(Cor_C)‖ (w = −1, κ = 1, stacked over the grid) for the C ∈ E that pass.
Statistics: the pairwise |cos| (min and mean), and the share σ₁²/Σσ² of the top singular value of the matrix [û_C].
"Parallel" PASS if min |cos| ≥ 0.99. "Scatter" FAIL if mean |cos| ≤ 0.5. Else intermediate.
Prediction (blind): intermediate.
Naming: RG* only; no labels L1–L7. Geometric only; MAPS_CANDIDATES untouched; no Resonant objects; no bridge claim; E1–E3 OPEN; Ξ not identified.
