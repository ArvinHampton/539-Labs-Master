# PREREG (order 2): the t^{-1/2} terms of the normalized Bridge Series q^{-7/20}·C and of its 105-series companion

Owner: Arvin Hampton (539 Labs). Written 2026-10-24, about 8:30 AM CDT (America/Chicago), before any computation in this folder.
Folder: `reports/bridges/BRIDGE_C_35/order2/` (new files only). Parent: `reports/bridges/BRIDGE_C_35/` (RESULTS.md there: Theorem 1, Lemma 2, Theorem 3).
Rules: CORE_FREEZE (H_s not redefined; no certifier code touched; A35 `symbols.py` imported read-only). Category A = proof or exact/interval certificate; Category B = floating point. No TPC/RH claim. Residual-vs-Resonant lock: a link counts only as a map defined here that predicts something new and passes. Ledger not edited.

## 1. Objects (all written; notation of ledger v7 §3)
- A = [[2,7],[7,7]], Q(ν) = ½νᵀAν, B(ν,β) = νᵀAβ, a = (7/10, −1/5), D, MU (A35 order), sym_pair (A35): K2_μ ↔ (α,β) = (a+μ, 0), K3_μ ↔ (μ, a), K4_μ ↔ (μ, 0), with μ the A35 representatives in [0,1)².
- Weight on Z² (RTA manuscript §9): wt(v) = 1[n ≥ 0, k ≥ 0] − w(v), w(v) = ½(sgn B(c1,v) − sgn B(c2,v)) = ½(sgn n + sgn(n+21k)), c1 = (−1,1), c2 = (−4,1).
- **Companion series (the 105 shifted and twisted cone series), defined here:** for each of the 105 pairs (α,β),
  S_{α,β}(τ) = Σ_{v∈Z²} wt(v)·e(B(α+v,β))·e(τQ(α+v)).
  For (α,β) = (a,0) (that is, K2_0): Q(a+v) = Q_7(v) − 7/20, so S_{a,0} = q^{−7/20}·C, the normalized Bridge Series adopted by Arvin.
- Radial expansion at q = e(x)e^{−t}, x = h/m: t·S(e(x)e^{−t}) = A0(x) + A1(x)·t^{1/2} + O(t). By the parent Lemma 2 (generalized to (α,β); proof to be written), A0 = I·G_{α,β}(x). A1 is the order-2 ("t^{−1/2}") profile.

## 2. Map 1: explicit order-2 formula (prediction: exact closed form; new)
Decomposition, fixed now: orthant = one piece (U = I, offset 0, walls weight 1). K₊ = {n ≥ 0, n+21k ≥ 0} = ⊔_{r=0}^{20} (r·e1 + N·u1 + N·u2), u1 = (21,−1), u2 = (0,1); K₋ = −K₊; walls of K₊ (n = 0 and n+21k = 0) lie in the r = 0 piece and get weight ½ (subtracted as 1-D sums); origin weight 0.
Predicted formula for a piece with basis U = (u1,u2), offset c, p = Q(u1), r = Q(u2), q = B(u1,u2), N = 2m, f(z) = e(x·Q(α+c+Uz) + B(α+c+Uz,β)) on z ∈ (Z/N)²:
A1_piece = −mean(f)·(l1·J_a + l2·J_b) − (√π/2)·[ r^{−1/2}·N^{−1}Σ_z f(z)B1(z_1/N) + p^{−1/2}·N^{−1}Σ_z f(z)B1(z_2/N) ],
with l_i = B(α+c,u_i), B1(y) = y − ½, J_a = (√π/4)·(2/(4pr−q²))·(2√r − q/√p), J_b = (√π/4)·(2/(4pr−q²))·(2√p − q/√r).
A 1-D wall {c + b·u : b ≥ 0} contributes (√π/2)·Q(u)^{−1/2}·mean_{b mod N} f(c+bu) to A1.
Consequence (new, Category A once proved): A1(x)/√π is an algebraic number for every rational x (no log ε at order 2).
Validation (pre-stated): for the orthant alone at x = 0 (f ≡ 1), the formula must give the written constant a_P = 0.5256172043 (Residual-Law A2 Lemma 1).
**Numerical test (Category B), on S_{a,0} = q^{−7/20}C.** Points: x ∈ X216 with m ≤ 10 (96 points). Denominator-scaled t-grid: t_j = τ_j/m², τ_j = 0.02·2^{−j}, j = 0..5 (so t·(2m)² ≤ 0.08 throughout). Lattice sums truncated at Q(a+v) ≤ 40/t_min (+ check that the truncation box is not reached). Statistic: fit y(t) = (t·S − A0)/√t by least squares to c1 + c2·t^{1/2} + c3·t on the six t_j, A0 = I·G_{a,0}(x) exact. ref_x = max(|A1_pred(x)|, 0.05). Pass if |c1 − A1_pred| ≤ 0.02·ref_x; falsify if > 0.10·ref_x; else inconclusive. Overall: confirmed if ≥ 95 % pass and none falsify; falsified if any point falsifies.

## 3. Map 2: order 2 is the true leading order on the leading-order zero set (prediction: nonvanishing)
Z0 = {x ∈ X216 : 2 | m or 5 | m}, where A0 = I·G = 0 for q^{−7/20}C (ledger entry 18). **Prediction: A1(x) ≠ 0 for every x ∈ Z0**, i.e. t·|q^{−7/20}C| ~ |A1(x)|·t^{1/2} there.
Test (Category A): evaluate the Map 1 formula in mpmath interval arithmetic (60 digits); nonzero certified if the interval for |A1|² excludes 0. Any certified zero falsifies the prediction (the point is listed). Also reported: the RTA Fricke-sample image y = −1/5 (W_7 image of x = 5/7), outside X216's positive range, evaluated the same way.

## 4. Map 3: vector-valued law at order 2 (Residual-Law B3; prediction: none)
**Prediction: the order-2 profiles of the 105 companions are not closed under x ↦ −1/x with a single weight**, for w = 1/2 and w = 1: there is no 105 × 105 matrix M with A1_j(−1/x) = |x|^{w}·Σ_k M_jk·A1_k(x) for all x.
Test (Category B, float64): rows x ∈ X216 with m ≤ 12 (138 points). A = [A1_j(x)], Bw = [|x|^{−w}·A1_j(−1/x)]. Numerical rank by SVD, rank = number of singular values > 10^{−9}·σ_max (a gap ≥ 10^4 at the cut is required, else inconclusive). Closure would force rank[A | Bw] = rank A. Not closed if rank[A | Bw] > rank A for that w.
Control (must pass for the test to be valid): the same test on the leading profiles A0_j = I·G_j with w = 1 must give rank[A0 | B1] = rank A0 = 36 (parent Theorem 3 / entry 40). If the control fails, Map 3 is declared invalid.
What a "not closed" outcome means: no finite vector-valued modular law at order 2 in the span of these 105 profiles (evidence only), consistent with a quantum-modular / shadow structure. It does not exclude a law in a larger space.

## 5. Not attempted / declared
- The O(1) term, period functions and Ξ: not attempted. g_k, T3, O_res, 539: no written object links them; not used.
- s = 33 / s = 39 sector_exact: on hold (memory); not used.
- Proof of the Map 1 formula (2-D Euler–Maclaurin with explicit O(1) remainder) is to be written in RESULTS; without it Map 1 is Category B only.

## 6. Order
Hash → scripts (hashes in scripts/SHA256SUMS) → validation (a_P) → Map 1 exact values → Map 2 → Map 1 numerics → Map 3 → RESULTS. Changes after hashing go in NOTES.md with times; predictions, statistics and thresholds do not change.
