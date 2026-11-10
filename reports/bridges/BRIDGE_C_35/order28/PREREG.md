# order28 PREREG (written and hashed before numerics)
W = span{CO, Γ_γCO}, stacked over x and −1/x on the 216-point grid. R(Y) = Y(−1/x) − x·35^{−1/2}·M·Y(x). Non-vacuity (mandatory): d(Y) = ‖Y − proj_W Y‖/‖Y‖ > 1e−3, else VACUOUS.
## Controls
C1 corner(K) = CO ≤ 1e−12. C2 R(CO) abs reproduces 54.41 (order25 R_total 54.4114…; tolerance 1e−6 relative to the stored value, computed in-script).
## RG19 — A2_lines (LN, SLN from order18)
Weight-1 law: PASS abs ≤ 1e−8; FAIL rel = abs/‖SLN‖ ≥ 1e−3; else inconclusive. Non-vacuity d(LN) > 1e−3.
Explanation measure (Category B): ‖R(LN+CO)‖ compared with ‖R(CO)‖; cosine between R(LN) and −R(CO).
Prediction (not blind: order19 found ‖R(A2)‖ = 54.4 ≈ ‖R(CO)‖): ‖R(LN)‖ ≪ ‖R(CO)‖. Possibly PASS (lines exact). The near-law defect is not explained by the lines.
## RG20 — non-automorph unimodular cones
Cones (continued-fraction or Farey subdivisions of the boundary rays): K1 = cone((1,0),(1,1)), K2 = cone((1,1),(0,1)) (order23 subdivision of K); J1 = cone((7,−1),(20,−3)), J2 = cone((20,−3),(13,−2)) (mediant subdivision of γ⁻¹K).
Exact geometric identities (fixed): Cor_{K1}+Cor_{K2} = CO + ¼vtx and Cor_{J1}+Cor_{J2} = Γ_γCO + ¼vtx (subdivision, v8) — controls, so these sums are VACUOUS objects by construction.
Test objects: the antisymmetric combinations A_K = Cor_{K1} − Cor_{K2} and A_J = Cor_{J1} − Cor_{J2}, plus each single cone.
Each object: non-vacuity d > 1e−3; weight-1 law PASS abs ≤ 1e−8; FAIL rel ≥ 1e−3; else inconclusive.
Primary verdict RG20 = the verdict for A_K (A_J reported as well).
Explanation (Category B): the fraction of ‖R(CO)‖² captured by the least-squares projection of R(CO) onto span{R(A_K), R(A_J), R(LN)}.
Predictions (blind): A_K and A_J FAIL (relative error of order 0.01–0.1); single cones FAIL.
Rules: no Resonant objects; MAPS_CANDIDATES and DISCOVER_GRADING_PATH untouched; no bridge claim; E1–E3 OPEN; Ξ not identified.
