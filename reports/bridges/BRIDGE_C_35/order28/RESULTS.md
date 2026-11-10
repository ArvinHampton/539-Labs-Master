# order28 RESULTS
PREREG sha256 033d322e64c07f3bd6ada371208a5cb624efa6b2303f78cfd2eb37b948013d3c (hashed before numerics).
Non-vacuity: d = relative distance from W = span{CO, Γ_γCO}, threshold 1e−3.
| object | d | ‖R‖ abs | rel | verdict |
|---|---|---|---|---|
| C1 corner(K)=CO | | 0.0 | | PASS |
| C2 R(CO) vs order25 | | 54.406 | 0.0 err | PASS |
| subdivision K1+K2 = CO+¼vtx | | 2.2e−14 | | PASS (control) |
| subdivision J1+J2 = Γ_γCO+¼vtx | | 2.2e−14 | | PASS (control) |
| **RG19** A2_lines LN | 0.998 | 189.25 | 1.78 | **FAIL** |
| **RG20** A_K = Cor_{K1}−Cor_{K2} | 0.580 | 224.90 | 0.147 | **FAIL** |
| A_J = Cor_{J1}−Cor_{J2} | 0.580 | 224.90 | 0.147 | FAIL |
| K1 / K2 / J1 / J2 | 0.38 / 0.92 / 0.92 / 0.38 | 109.9 / 121.9 / 121.9 / 109.9 | 0.094 / 0.252 / 0.252 / 0.094 | FAIL |
Every test object passes non-vacuity: these are genuinely new directions.
## RG19 explanation
‖R(A2)‖ = ‖R(LN+CO)‖ = 184.84 against ‖R(CO)‖ = 54.41. The lines do not cancel the corner defect; the full A2 is further from the law than its corner part. cos(R(LN), −R(CO)) = 0.224.
**Prediction miss (disclosed):** I predicted ‖R(LN)‖ ≪ ‖R(CO)‖ from a recalled order19 value. The order19 L0 value 54.4 was the corner/affine law, not the full A2. The prediction was wrong; the verdict FAIL stands.
## RG20 explanation
The least-squares span of {R(A_K), R(A_J), R(LN)} captures 16.6% of ‖R(CO)‖². That is no explanation.
Post-hoc observation: J1 = γ⁻¹K2 and J2 = γ⁻¹K1 (γ⁻¹(1,1) = (20,−3)). So the mediant subdivision of γ⁻¹K is the γ⁻¹-transport of the K subdivision. The J objects are Γ_γ-images of the K objects (matching norms to 1e−13) and add nothing independent; this follows from the v8 transport proposition.
## Category
A: nothing new (subdivision and transport identities were already in v8). B: all numbers above. v11: no. Ξ: not identified. E1–E3 OPEN.
Blind/consistency: RG20 blind (predicted FAIL, correct). RG19 prediction relied on a misremembered order19 value (wrong).
