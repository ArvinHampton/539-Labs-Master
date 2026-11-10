# round2 PREREG: T3 itinerary words → weights on residues mod k

Frozen 2026-10-23 (CDT) before any round-2 script was run. Lock: these are maps from the crypto map T3 to residues mod k. A "confirmed" outcome would only be a candidate bridge to OccFilt_k(∞). It would not be a proof.

## Objects
- Words w = (r_0, …, r_{j−1}) ∈ {0,1,2}^j. By P2/entry 47, the words of length j correspond bijectively to n mod 3^j: n has itinerary prefix w iff T3^i(n) ≡ r_i mod 3 for i < j.
- Branch data: (b_r, d_r) = (1, 0), (4, 2), (2, −1) for r = 0, 1, 2, so that T3(n) = (b_r n + d_r)/3 when n ≡ r mod 3.
- Affine data of the word: B_0 = 1, C_0 = 0, B_{i+1} = b_{r_i} B_i, C_{i+1} = b_{r_i} C_i + d_{r_i} 3^i. Then 3^j T3^j(n) = B_w n + C_w for every n in the cylinder of w (proof in RESULTS, R0). B_w is the multiplier and C_w the translation constant. C_w depends on the order of the letters, not only on how many of each letter there are.
- Weights: μ^B_{k,j}(c) = 3^{−j} #{w : B_w ≡ c mod k} and μ^C_{k,j}(c) = 3^{−j} #{w : C_w ≡ c mod k}. These are uniform weights on words, which by P2 is Haar measure on Z₃ and also the exact count over integers n ∈ [0, 3^j).

## Maps
- **R-B (multiplier map):** w ↦ B_w mod k. Before any test this is reduced to a group-theoretic statement (RESULTS, R1). If R1 settles it, it is recorded as a proved no-go and not tested.
- **R-C (translation map):** w ↦ C_w mod k. This statistic is order-sensitive. Neither P2 nor P3 fixes its law: P3 concerns T3^j(n) mod M as n varies, while C_w is a function of the word alone. It is tested.

## Prediction and test (R-C)
- k ∈ K = {4, 5, 7, 8, 11, 12, 13}, j = 120. μ^C_{k,120} is computed exactly with big-integer counts (dynamic programming over the state C mod k, with 3^i mod k known).
- Sq_k = {x² mod k}. Excess e_k = μ^C(Sq_k) − |Sq_k|/k. Leak λ_k = μ^C(non-squares).
- **Weak prediction** at k: e_k ≥ 0.02. **Strong prediction** at k: λ_k ≤ 10⁻⁶, i.e. the itinerary weights live on the squares, which is what OccFilt_k(∞) = Sq_k would need.
- **Open class target** (k = 4, 8, 12; MIX classes c = 0 for k = 4, c = 1 for k = 8, c ∈ {0, 4} for k = 12): μ^C(c) > 10⁻⁶ at each MIX class. This is a prediction that MIX classes ∈ OccFilt_k(∞). It is reported as a conditional prediction only, because the true answer is open. It can only be falsified (mass ≤ 10⁻⁶), not confirmed.
- **Decision:** R-C is confirmed as a candidate iff the weak prediction holds at ≥ 5 of the 7 values of k AND the strong prediction holds at ≥ 1 of them. Otherwise it is falsified.
- **Multiple testing:** Holm over the 7 values of k at α = 0.01. Since μ^C is computed exactly, each "p-value" is 0 (the prediction holds) or 1 (it fails), and Holm leaves these unchanged. The correction is vacuous and is stated only for completeness.
- **Stability check** (descriptive only, not a decision): the same quantities at j = 60.

Runs use `nice -n 19`, `OMP_NUM_THREADS=1` and `ulimit -v 3000000`, one job at a time.
