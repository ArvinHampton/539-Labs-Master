# order30 RESULTS
PREREG sha256 f599d527d3942fbf75466c87f83e6719334ac2d0721cf493ff57cb62dc79b570 (hashed before numerics).
Run note: the first run was interrupted after depth 1 (partial log logs/o30_run1_interrupted.log, kept). The unchanged script was rerun in full (logs/o30_run2.log); its depth-1 numbers are identical.
## Controls (all PASS)
C1 corner(K) = CO: 0.0. C2 ‖R(CO)‖ = 54.406: rel err 0.0. C3 subdivision sum: ≤ 2.0e−13 (n ≤ 4). C4 Σℓ = L: ≤ 1.3e−14. arccosh(√(7/2)) = ½log(6+√35): 0.0.
## RG23 (primary): arc-length weights W_n = Σ (ℓ_i/L) Cor_{C_i}: FAIL
| n | cones | d (non-vac) | ‖R(W_n)‖ | e_n = ‖R(CO)+R(W_n)‖/‖R(CO)‖ | |cos| | best-scale s_n (λ) | near-law of W_n (κ free) |
|---|---|---|---|---|---|---|---|
| 1 | 2 | 0.188 | 37.2 | 1.499 | 0.571 | 0.821 (−0.84) | 0.0577, κ = 0.998 |
| 2 | 4 | 0.275 | 46.7 | 1.496 | 0.293 | 0.956 (−0.34) | 0.0783, κ = 0.998 |
| 3 | 8 | 0.326 | 50.0 | 1.505 | 0.229 | 0.973 (−0.25) | 0.0842, κ = 0.995 |
| 4 | 16 | 0.305 | 45.9 | 1.422 | 0.185 | 0.983 (−0.22) | 0.0777, κ = 0.999 |
e_4 = 1.42 ≥ 0.1 and c_4 = 0.18 ≤ 0.99, so FAIL. The divergence flag is not raised: ‖R(W_n)‖ stays bounded at about 46–50, unlike order29's Alt_n. The arc-length rule converges in size but does not cancel R(CO); R(W_n) is nearly orthogonal to R(CO) and increasingly so. Prediction FAIL correct (blind).
## RG24 (secondary): uniform average U_n: FAIL by rule, non-discriminating
t_n = 0.490, 0.735, 0.857, 0.918 (n = 1..4); d(CO − U_n) = 0.0069 (> 1e−3, passes the written threshold).
Disclosure (post-hoc): by the subdivision identity, U_n = 2^{−n}(CO + ¼(2ⁿ−1)vtx) exactly. So CO − U_n = (1−2^{−n})(CO − ¼vtx) lies in span{CO, vtx}, and t_n → ‖R(CO − ¼vtx)‖/‖R(CO)‖. RG24 carries no information beyond CO and the constant vertex vector. The PREREG non-vacuity span should have included vtx (lesson recorded).
Near-law residual of U_n: 0.062, 0.072, 0.105, 0.182 (κ 0.998 → 0.975).
## Descriptive finding (Category B)
Every corner object tested (CO, W_1..W_4) shows the same near-law, with κ = 0.995–0.999 and residual 0.058–0.084, including objects far from span{CO, Γ_γCO} (d up to 0.33). The near-law therefore looks generic to unimodular cone corners and not specific to K. Not preregistered; to be tested as a hashed map.
## Answers
No combination cancels R(CO) under the arc-length rule. Category A: none new. v11: no. Ξ: not identified. E1–E3 OPEN.
