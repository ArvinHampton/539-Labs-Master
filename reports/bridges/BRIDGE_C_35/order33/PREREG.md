# order33 PREREG (written and hashed before numerics)
Corner formula (cornerlib.corner; v8): for cone(u1,u2) with u1 = e1 = (1,0), and coordinates (a,b) of α+v in the basis (u1,u2),
Cor = Σ f·[ B̄1(a)B̄1(b) + (B/(4Q(u2)))·B2(a) + (B/(4Q(u1)))·B2(b) ], with B = u1ᵀAu2.
Pieces (fixed): T_BB = Σ f·B̄1(a)B̄1(b); T_other = Σ f·(B/(4Q(u2)))·B2(a); T_e1 = Σ f·(B/(4Q(e1)))·B2(b), with Q(e1) = 1.
Test set: CO = ((1,0),(0,1)) and the independent order32 E cones ((1,0),(n,1)), n = 1..8. The h-images are omitted because they duplicate n = 1, 2. Total 9 cones.
Law family and criterion (as order31/32): r(w) = min_κ‖S − κx^{−w}35^{−1/2}MY‖/‖S‖, w ∈ {−1, −½, 0, ½, 1}. Near-law: w* = −1, |κ̂−1| ≤ 0.01, r(−1) ≤ 0.10.
Non-vacuity per piece: d′ from span{CO, Γ_γCO, vtx} > 1e−3, and ‖piece‖ ≥ 1e−6‖Cor‖ (a smaller piece is reported as VACUOUS).
## Control
Reconstruction: max|T_e1 + T_other + T_BB − Cor| ≤ 1e−12 (both x and −1/x), and Cor matches order30/32 stored arrays to 1e−12.
## RG29
Per piece P ∈ {T_e1, T_other, T_BB}: piece-pass count p_P = number of the 9 cones meeting the near-law.
Hypothesis H (written now): T_e1 carries the near-law and T_other, T_BB do not.
RG29 PASS iff p(T_e1) = 9 and p(T_other) ≤ 1 and p(T_BB) ≤ 1. FAIL iff p(T_e1) ≤ 6. Else inconclusive.
Also reported: r and κ̂ per piece, and the pairwise sums T_e1+T_other and T_e1+T_BB.
Prediction (blind): uncertain. I record PASS as the hypothesis but expect a possible FAIL, because pieces are not separately modular.
## RG30 (run regardless; informative)
Defect share: s_C = ‖R(T_other+T_BB)‖²/‖R(Cor)‖² and cosine c_C = cos(R(T_other+T_BB), R(Cor)), with R at κ = 1, w = −1.
"Accounts for most" if median s_C ≥ 0.5 and median c_C ≥ 0.7. Scatter of the R(T_other+T_BB) directions: min and mean pairwise |cos|; scattered if mean ≤ 0.5.
Naming: RG* only, no labels L1–L7. Geometric only; MAPS_CANDIDATES untouched; no Resonant objects; no bridge claim; E1–E3 OPEN; Ξ not identified.
