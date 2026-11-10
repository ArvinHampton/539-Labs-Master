# order35 PREREG: RG32, quantitative L_B leakage (written and hashed before numerics)
Sources (read-only):
- order20 Prop. L_B (Category A since v7);
- order20/scripts/o20.py for Gmean, ck, lam and the B1 evaluation of (ii);
- order19/data/rg5_arrays.npz: C2b = C[2] at x, SC[2] at −1/x;
- the symbols.reduce companion reduction.
Law metric (as orders 31–34, w = −1): X(x) = x·35^{−1/2}·M·C2b(x), S = C2b(−1/x), r = min_κ ‖S − κX‖/‖S‖ = ‖S − proj_X S‖/‖S‖.
## Grid (fixed)
P7 = {1, 1/2, 2, 1/3, 3, 2/3, 3/2} (the order20 B1 points; these have small N′, so the exact evaluation is feasible) × all 105 companions.
The full 216-point grid is NOT used: the L_B right-hand side needs N′²·35 Gauss means per entry, with N′ up to 88.
Disclosure: the reference value r = 0.0030492 is a full-grid number. The RG32 comparison is between prediction and measurement on P7, where r_meas(P7) is recomputed directly from the order19 arrays.
## Exact decomposition
For each (x, j), L_B (ii) writes S_j as a sum of terms t_{k,p} = N′²c′_k e(B(α,β+λ′_k))/(|x|√35) · G_{β+λ′_k+p, −α}(x), with k mod N′ and p ∈ A^{−1}Z²/Z².
- A term is "inside" iff reduce(β+λ′_k+p, −α) succeeds, i.e. its characteristic is one of the 105 companions up to the reduction rules. Otherwise it is "outside".
- S = S_in + S_out.
Control D0: ‖S_in + S_out − SC[2]‖_max ≤ 1e−10 on P7.
## RG32 prediction (no fit)
r_leak = ‖S_out − proj_X S_out‖/‖S‖ (outside-companion mass orthogonal to the law direction, computed from S_out and X only).
PASS iff |r_leak − r_meas(P7)|/r_meas(P7) ≤ 1e−6. FAIL iff ≥ 1e−2. Else inconclusive.
Diagnostic H1 (Category A candidate): S_in ∈ span{X} on P7, i.e. ‖S_in − proj_X S_in‖/‖S_in‖ ≤ 1e−10. RG32 PASS essentially requires H1 together with orthogonality bookkeeping; H1 is reported separately.
Also reported: the outside mass share ‖S_out‖/‖S‖; κ̂; and the k = 0 inside part.
Prediction (blind): FAIL. The inside part contains plain-Gauss-mean terms (from k = 0), whereas X is built from Bernoulli sums, so I expect H1 to fail.
## (0,1)-edge cones (r ≈ 0.022)
L_B is proved only for the ρ2 Bernoulli coordinate. The B2 sums on ((1,n),(0,1)) cones use sheared coordinates, so no exact L_B formula is available without a new statement. They are declared OUT OF SCOPE for RG32 (not tested; no new Bernoulli objects introduced).
v11 only if RG32 PASS gives a provable exact statement.
Naming: RG* only, no labels L1–L7. Geometric only; MAPS_CANDIDATES untouched; no Resonant objects; no bridge claim; E1–E3 OPEN; Ξ not identified.
