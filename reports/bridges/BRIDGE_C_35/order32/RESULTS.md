# order32 RESULTS
PREREG sha256 d1a77766ed79b5347646c9e4b90e9e0784efd504b37db07e8cc551f2ac1900ad (hashed before numerics; not rehashed).
Criterion (as in order31): w* = −1, |κ̂−1| ≤ 0.01, r(−1) ≤ 0.10. All cones non-vacuous (d′ from span{CO, Γ_γCO, vtx}: 0.32–0.999).
## RG27: PASS (Category B)
| set | n | criterion as predicted | details |
|---|---|---|---|
| E (edge e1) | 10 | 10/10 satisfy | r 0.068–0.094, κ̂ 0.996–0.9995, |Im κ̂| ≤ 0.005 |
| C (no e1-orbit edge) | 28 | 28/28 violate | r 0.247–0.567, κ̂ 0.81–0.97 |
| blind subset E (new) | 6 | 6/6 | ((1,0),(n,1)) n = 5..8: r 0.0763, 0.0746, 0.0676, 0.0702 |
| blind subset C (new) | 2 | 2/2 | ((1,5),(0,1)) r 0.296; ((1,6),(0,1)) r 0.258 |
Disclosure (post-hoc): ((1,0),(8,−1)) = h((1,0),(1,1)) and ((1,0),(9,−1)) = h((1,0),(2,1)), since h = [[1,7],[0,−1]] fixes e1. Their values are identical to their preimages, so only 4 of the 6 "new" E cones are independent blind tests (all passed).
## RG27G: PASS (consistency with proved transport)
γ⁻¹-images ((13,−2),(72,−11)) and ((13,−2),(85,−13)) satisfy the criterion; Δr ≤ 1.1e−16, Δκ̂ ≤ 3.3e−16 against their E preimages.
## RG28: FAIL (scatter)
Over the 10 E cones the unit residual directions R(Cor_C)/‖R‖ have pairwise |cos| min 0.0021, mean 0.064, and top-singular-value share 0.20. Each e1-cone has a small relative miss (~7–9%), but the misses point in essentially orthogonal directions. There is no common defect direction. Prediction "intermediate" (blind): wrong (stronger scatter than expected).
## Reading
The near-law is a property of having the minimal vector e1 (or its ⟨γ,h⟩-orbit) as an edge. This is confirmed on new cones (Category B). The defect itself is cone-specific, not one shared vector.
Category A: none new. v11: no. Ξ: not identified. E1–E3 OPEN.
