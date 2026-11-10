# PREREG (order 3 step): where the shadow enters the normalized Bridge Series q^{-7/20}·C

Owner: Arvin Hampton (539 Labs). Written 2026-10-24, about 8:45 AM CDT (America/Chicago), before any computation in this folder.
Folder: `reports/bridges/BRIDGE_C_35/order3/` (new files only; not pushed). Parent results: `../RESULTS.md` (leading order), `../order2/RESULTS.md` (order-2 theorem; ledger v8 entries 104–109).
Rules: CORE_FREEZE; Category A = proof or exact/interval certificate; Category B = floating point. No TPC/RH claim. Residual-vs-Resonant lock: only a map defined here that predicts something new and passes counts. Ledger not edited.

## 0. The claim to be tested, and how it is made precise
Arvin's claim: "A1(−1/x) minus |x|^{−1/2} times its explicit S-image is a smooth function of x built from unary thetas of the wall directions (Q(u) = 1, 7/2, 595/2); this locates where the shadow Ξ enters."
As stated, the claim needs an S-image for A1. The order-2 theorem (ledger entry 107) splits A1 into three kinds of terms, each with a different transformation behaviour:
- **Drift part D.** −Σ_pieces ε·mean_piece(f)·(l1 J_a + l2 J_b). Each mean_piece(f) is a Gauss mean over a coset of the sublattice U·Z² + c. This is the weight-1 type, as at leading order.
- **Ray part R.** Σ_rays ±½·(√π/2)Q(u)^{−1/2}·mean_b f(c+bu), the 1-D Gauss means of the unary thetas along u = (0,±1) (Q = 7/2) and u = ±(21,−1) (Q = 595/2). This is the weight-1/2 type: a 1-D Gauss reciprocity is expected.
- **Sawtooth wall part W.** −Σ_pieces ε·(√π/2)(r^{−1/2}W_1 + p^{−1/2}W_2), with W_i = N^{−1}Σ_z f(z)B1(z_i/N). Grouped by the Q-value of the wall direction along which the Gaussian integral runs:
  - W[1]: orthant edge (1,0);
  - W[7/2]: edges ±(0,1);
  - W[595/2]: edges ±(21,−1).
Precise form of the claim, preregistered as three maps:
- the S-image exists exactly (zero defect) for D (weight 1) and for R (weight 1/2);
- for W it does not exist in finite form;
- so the non-modular (shadow) part of A1 is located exactly in the sawtooth wall terms W, built from unary-theta Gauss means of the wall directions with sawtooth weights in the transverse direction.
A full proof that the W-defect is a smooth function is NOT attempted. That step is the classical quantum modularity of partial-theta constant terms, and it is declared open (§5).

## 1. Map 1: structural identity (Category A, proof in RESULTS)
For each piece and each z1 residue, W_1 = Σ_{z1=0}^{N−1} B1(z1/N)·γ(z1), where γ(z1) = N^{−1}Σ_{z2 mod N} f(z1,z2) is the 1-D Gauss mean, at x, of the unary theta along u2 through the point α+c+z1u1. W_2 is the analogue with the roles of u1 and u2 exchanged.
New content: A1 = D + R + W, written with explicit wall unary-theta data. It is checked numerically by summing the parts back to A1 (float, |difference| ≤ 1e−12 required) at all test points.

## 2. Map 2: closure tests per part (Category B), with a sign control that must pass first
Data: all 105 companions S_{α,β} (definition of order2/PREREG §1), points x ∈ X216 (216 rows), values at x and at −1/x.
Convention (fixed): for a family F (columns = companions), F is "S-closed with weight w" iff F(−1/x) = |x|^{−w}·M·F(x) for one fixed matrix M. Test statistic: r_F = numerical rank of F; r_{F,w} = numerical rank of [F | diag(|x|^{w})·F(−1/x)]. Numerical rank = number of singular values > 1e−9·σ_max. Closed iff r_{F,w} = r_F. If r_F = 216, the test is inconclusive for F.
**Sign control (must pass before any verdict is read).**
- (i) A0 with w = 1 gives r = r_{A0} = 36.
- (ii) A0 with the wrong sign (row factor |x|^{−1}) gives r > 36.
If either fails, Map 2 is void.
Predictions:
- P-D: D is closed with w = 1.
- P-R: R is closed with w = 1/2.
- P-W: W is not closed with w = 1/2, and not closed with w = 1. The same holds for each group W[1], W[7/2], W[595/2] separately (w = 1/2).
Outcome rule:
- all of P-D, P-R, P-W hold: "shadow located in W" (Category B);
- P-D or P-R fails: the claim is falsified in its precise form (the S-image does not exist even for the Gauss-mean parts);
- P-W fails for a group: that group carries no obstruction.

## 3. Map 0: numerical anchor with the t-grid fixed now (Category B)
For q^{−7/20}C at x ∈ {1, 1/2, 1/3, 2/3, 1/4, 1/5, 1/6} the grid is t_j = 2^{−j}·0.5/(297.5·(2m)²), j = 0..5. It is scaled to the denominator m and to the long edge (21,−1) with Q = 595/2 = 297.5. Lattice sums are truncated at Q(a+v) ≤ 40/t_min, with a box-edge assert.
- (a) Fit (t·S − A0)/√t to c1 + c2√t + c3 t. Pass if |c1 − A1| ≤ 1e−3·max(|A1|, 0.05); falsify if > 1e−2·max(|A1|, 0.05).
- (b) Descriptive, no verdict: the O(1) coefficient A2(x) ≈ fit of S − A0/t − A1/√t to c + c′√t + c″t on the same grid. It is reported to show the size of the next term only.

## 4. What would count as a link
Only Map 2 with all predictions holding and the control passing. It would say: the obstruction to a finite vector-valued law at order 2 (order2 Map 3) comes entirely from the sawtooth wall terms, while the Gauss-mean parts carry exact weight-1 and weight-1/2 laws. It is Category B (rank evidence). The Category A part is Map 1, the explicit identity.

## 5. Declared open / not attempted
- Smoothness of the W-defect on R∖{0}, and the identification of Ξ with the weight-3/2 unary thetas of the walls: not attempted.
- An exact proof of P-D and P-R (Gauss reciprocity for coset means and 1-D means): not attempted here.
- The analytic O(1) coefficient: not attempted.
- g_k, T3, 539: not used. s = 33/39 work: on hold.

## 6. Order
Hash → scripts (SHA256SUMS) → Map 1 check → sign control → Map 2 → Map 0 → RESULTS. Deviations go to NOTES.md with times.
