# order36 PREREG: RG33, leakage as a span projection (written and hashed before numerics)
Terminology: the companion Gauss-mean span is the column span of G = A0/I (216 × 105 over the grid; rank 36 = dim V, ambient). The law vector is the 35-component law vector; 36 is used only for this ambient span rank.
Objects (order35 definitions, unchanged):
- S = C2b(−1/x), exactly split by L_B (ii) into S_in (characteristics reducing to companions) and S_out;
- X = x·35^{−1/2}·M·C2b(x);
- r = ‖S − proj_X S‖/‖S‖ (κ free, w = −1).
## Grid handling (fixed in advance)
- Span projection is across grid points (functions of x). On the 7-point order20 grid the span of the companion columns has rank ≤ 7, so every vector of 7 values lies in it, the leftover is 0 by construction, and the test is non-discriminating.
- The 7-point run is reported only as this trivial control (expected leftover ≈ 0).
- Primary grid G48: the 48 points of XS with the smallest |num(x)|·den(x) (ties by |num|), listed in scripts/o36.py by that rule. Rank of G on G48 is reported; required: 36, else VOID.
- Everything is reported both globally (Frobenius over G48 × 105) and point by point (per-x r with the global κ̂, and per-x leftover share).
## Projection
P_G = orthogonal projector onto colspan(G|G48) (SVD, relative threshold 1e−9), applied column-wise. Leftover O⊥ = (I − P_G)S_out.
## RG33 prediction (no fit)
r_pred = ‖O⊥‖_F/‖S‖_F. PASS iff |r_pred − r_meas(G48)|/r_meas(G48) ≤ 1e−6; FAIL iff ≥ 1e−2; else inconclusive.
Also reported: ‖(I−P_G)S‖/‖S‖, ‖(I−P_G)S_in‖/‖S‖, ‖(I−P_G)X‖/‖X‖; Spearman correlation across x between per-point r and per-point leftover share.
Prediction (blind): FAIL. The coefficients of the inside terms depend on x, so even S_in need not lie in the column span, and the law direction X is built from Bernoulli sums. No identity links the leftover to r.
Category: B unless an exact identity is found and proved (then a v11 candidate).
Controls: D0 = S_in + S_out = SC19[2] on G48 (≤ 1e−10); C2b on G48 from order19 arrays.
Naming: RG* only, no labels L1–L7. Geometric only; MAPS_CANDIDATES untouched; no Resonant objects; no bridge claim; E1–E3 OPEN; Ξ not identified.
