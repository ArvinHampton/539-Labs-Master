# order33 RESULTS
PREREG sha256 886159282d45a48155f068625164b3e98253c82d4a8262b185fe189944a4c672 (hashed before numerics).
Test set: CO and ((1,0),(n,1)), n = 1..8 (9 cones). Criterion: w* = −1, |κ̂−1| ≤ 0.01, r ≤ 0.10. Every piece is non-vacuous (d′ from span{CO, Γ_γCO, vtx}: T_e1 0.299; T_other 0.99–1.0; T_BB 0.85–1.0).
## Control
max|T_e1 + T_other + T_BB − stored Cor| = 5.7e−14: PASS.
## RG29: PASS (Category B)
| piece | cones meeting near-law | r(−1) | κ̂ |
|---|---|---|---|
| T_e1 | 9/9 | 0.0030 (all cones) | 1.0000 |
| T_other | 1/9 (K only) | 0.021 (K), 0.041 → 0.192 (n = 1..8; fails r for n ≥ 2 and κ for n ≥ 6) | 0.975–0.999 |
| T_BB | 0/9 | 0.18 (K), 0.35 → 0.59 | 0.78–0.99 |
| T_e1+T_other | 9/9 | 0.0031–0.0037 | 1.0000 |
| T_e1+T_BB | 9/9 | 0.059–0.094 (= Cor's r) | 0.996–0.9995 |
| Cor | 8/9 (K = CO is excluded as span-vacuous by construction) | 0.058–0.094 | ≈0.998 |
Hypothesis H holds as written. Prediction PASS (recorded as the hypothesis with doubt): correct.
## RG30
Defect share ‖R(T_other+T_BB)‖²/‖R(Cor)‖²: median 0.9986; cosine with R(Cor): median 0.9992. Accounts for most: YES.
Directions across cones: pairwise |cos| min 0.0015, mean 0.022. Scattered: YES.
## Sharper reading (descriptive, Category B; post-hoc but disclosed)
- The B2 part T_e1+T_other obeys the law to r ≈ 0.003 on every cone; this sum is the B2 part of the corner. The near-law defect is carried by the B̄1B̄1 term T_BB, and T_other alone fails only because it is a piece of a law-obeying sum.
- T_e1 is one fixed vector up to scale. In the basis ((1,0),(n,1)) the second coordinate is b = ν2 for every n, and B = 2n+7, so T_e1(n) = ((2n+7)/7)·T_e1(K). This holds exactly by the formula, and ‖R(T_e1)‖/(2n+7) = 0.38451 for all n. It explains why every e1-cone shares the T_e1 behaviour.
- T_e1 itself misses the law by r = 0.0030. That is small but not zero, so it is not an exact law; it is Category B.
## Category
A: nothing new proved. The identity T_e1(n) = ((2n+7)/7)T_e1(K) is an immediate consequence of the corner formula; I note it but do not add it to the paper. v11: no. Ξ: not identified. E1–E3 OPEN.
