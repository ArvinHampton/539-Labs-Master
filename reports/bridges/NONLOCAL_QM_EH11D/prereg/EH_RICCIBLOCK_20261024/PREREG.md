# EH-RB1 prereg (written 2026-10-24 ~22:10 CDT, before run)
Identity (fully written in EH1 23010998 txt, quoted):
- :18 "ds2 = e−2A(y) ημν dxμ dxν + dy2 + e2B ĝab dza dzb" ; :21 "B constant. R̂ab = κint ĝab."
- :29 "A = ky" (L5); :30 (L6) "Gμν/g = Gyy = 6k2−3K , Gab/g = 10k2−2K"
- :118 "L6. Contract Fin 11. Rext/g=Ryy=−4k2, Rfib/g=K." ; :88 "K … κint e−2B"
- :43 "On the lock: R = 28k2, Gμν = Gyy = −18k2 g, Gab = −6k2 g." (with :38 K=8k2)
Not covered by l7_recheck / EH-FF1 (those take L6 blocks as given; neither computes curvature from the metric nor checks R=28k²).
Convention dependence: NONE on Φ≡G² or 8πG11 (pure geometry; Φ never enters). K=8k² used only for P3.
Method: SymPy, diagonal-metric Christoffel/Ricci computed from scratch on the 11D metric with A=ky, B constant, ĝ = round S^6 of radius r (κint=5/r²), Lorentzian η=diag(−1,1,1,1).
Predictions (all must hold for PASS):
 P1 R_μν/g_μν = R_yy = −4k² (each μ); R_ab/g_ab = κint e^{−2B} = K (each a).
 P2 R = −20k² + 6K; G_μν/g = G_yy = 6k²−3K; G_ab/g = 10k²−2K (exact).
 P3 With K=8k²: R=28k², G_ext=G_yy=−18k², G_fib=−6k².
Non-vacuous controls (must FAIL the written blocks, else test is vacuous → FAIL):
 C1 same pipeline with A=ky² (non-linear warp) ⇒ R_yy ≠ −4k².
 C2 wrong dimension split (3 ext dims instead of 4, fibre 7 → still 11D) ⇒ G_ext ≠ 6k²−3K.
FAIL if any P fails or any control matches.
