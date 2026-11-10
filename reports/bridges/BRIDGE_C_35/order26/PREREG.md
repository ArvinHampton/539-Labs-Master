# order26 PREREG (written and hashed before any numerics)
Objects (fixed): K=cone((1,0),(0,1)); γ⁻¹K=cone((13,−2),(7,−1)); between-cone B=cone((7,−1),(1,0)) (det 1, unimodular; the region between γ⁻¹K and K).
Note: γ⁻¹K∪B=cone((13,−2),(1,0)) has det 2 and B∪K has det 7, so B is the only unimodular piece of the region; no further subdivision is available inside cornerlib (unimodular only).
D := Cor_{γ⁻¹K} − Cor_K (= −2Y_−, order25). vtx_j = [α_j ∈ Z²] (order23 vertex vector). All on the order18 grid XS (216 points), 105 companions, also at −1/x.
## Controls (must pass, else stop)
C1 corner(K)=CO ≤1e-12; C2 Γ_γ·CO = Cor_{γ⁻¹K} ≤1e-12; C3 Y_− = −½D ≤1e-12; C4 order25 RG15 abs reproduced within 1e-9 of 52.0306.
## I1 exact identity (primary, Category A candidate)
For each (s,t) ∈ {±1}×{0,±¼}: e(s,t)=max|D − s·Cor_B − t·vtx| (both x and −1/x). PASS if min e ≤ 1e-10; FAIL if min e ≥ 1e-6; else inconclusive.
Non-vacuity: ‖Cor_B‖/‖D‖ ≥ 1e-3.
Also reported (Category B): least squares D ≈ a·Cor_B + b·vtx, relative residual.
## RG17 law-defect carry (primary map)
β = least squares of R(Y_−) on P_−R(Cor_B) (R(Y)=Y(−1/x) − x·35^{−1/2}·M·Y(x)). r = ‖R(Y_−) − β P_−R(Cor_B)‖/‖R(Y_−)‖ (absolute residual also reported).
PASS r ≤ 1e-6; FAIL r ≥ 0.1; else inconclusive. Non-vacuity: ‖P_−R(Cor_B)‖/‖R(Y_−)‖ ≥ 1e-3.
## RG17′ secondary: Cor_B itself against the weight-1 law
abs=‖R(Cor_B)‖, rel=abs/‖Cor_B(−1/x)‖. PASS abs ≤1e-8; FAIL rel ≥ 1e-3; else inconclusive. Non-vacuity ‖Cor_B‖≥1e-3‖CO‖.
## Predictions (blind for I1/RG17; C4 reuses order25 numbers = consistency)
I1: FAIL expected (no reason a γ-difference equals one cone corner). RG17: FAIL expected. RG17′: FAIL expected (single-cone corners fail the law in order23/24).
Rules: Category A vs B separate; no Resonant objects; MAPS_CANDIDATES untouched; no bridge claim; E1–E3 OPEN; Ξ not identified.
