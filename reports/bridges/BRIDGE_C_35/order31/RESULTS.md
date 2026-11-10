# order31 RESULTS
PREREG sha256 d289ca53d42172deae9568740512a68b174e984ac94a363a73484cd86699a27c (hashed before numerics). Data read-only from order30 and order28.
## Controls (all PASS)
C1 stored K corner = CO: 0.0. C2 ‖R(CO)‖ = 54.406: rel 0.0. C3 arccosh(√3.5) = ½log(6+√35): 0.0.
## RG25a: is the near-law generic? FAIL (Category B)
All 30 subdivision cones are non-vacuous (d′ from span{CO, Γ_γCO, vtx} between 0.34 and 0.998). 26 of 30 violate the criterion (w* = −1, |κ̂−1| ≤ 0.01, r ≤ 0.10). The best weight is w* = −1 for every cone.
The four that satisfy it are exactly the cones with edge ray (1,0):
| cone | ℓ | r | κ̂ |
|---|---|---|---|
| K = ((1,0),(0,1)) | 1.239 | 0.0585 | 0.998 |
| ((1,0),(1,1)) | 0.788 | 0.0936 | 0.996 |
| ((1,0),(2,1)) | 0.601 | 0.0920 | 0.997 |
| ((1,0),(3,1)) | 0.491 | 0.0867 | 0.996 |
| ((1,0),(4,1)) | 0.417 | 0.0772 | 0.9995 |
All other cones: r = 0.25–0.57 and κ̂ = 0.81–0.97 with Im κ̂ up to −0.16. The cones with edge (0,1) are the next best (r 0.25–0.30).
Prediction PASS (not blind, based on the order30 observation): **wrong**. The order30 "generic" observation came from arc-weighted sums dominated by the (1,0)-edge cones, not from single cones.
## RG25b: does the miss track the arc length? Intermediate (Category B)
Pearson(r, ℓ) = −0.883, Spearman = −0.817. Through-origin fit r ≈ cℓ has relative residual 0.92 (not proportional). Spearman(r, max|coords|) = +0.578.
The miss shrinks as the arc grows, which is the opposite of proportional. Prediction "independent" (blind): **wrong**. Verdict by rule: intermediate.
## RG26: Γ_γ transport invariance: PASS (consistency with v9/v10, not new evidence)
(K2, J1): Δr = 0, Δκ̂ = 7e−18. (K1, J2): Δr = 1.4e−17, Δκ̂ = 3.3e−16.
## Post-hoc reading (disclosed; not a verdict)
The near-law is attached to the edge ray e1 = (1,0) (Q(e1) = 1, the minimal vector) rather than to cones in general. Every cone with that edge has r < 0.1 and κ̂ ≈ 1 regardless of its arc length; cones without it do not. The negative r–ℓ correlation is largely explained by this, because the e1-cones are the longest at each depth.
## Category, answers
Near-law generic for unimodular cone corners: **no**. Miss tracks arc length: **not proportionally**; strong negative rank correlation, mostly an e1-edge effect. Category A: none new (RG26 follows from proved transport). v11: no. Ξ: not identified. E1–E3 OPEN.
