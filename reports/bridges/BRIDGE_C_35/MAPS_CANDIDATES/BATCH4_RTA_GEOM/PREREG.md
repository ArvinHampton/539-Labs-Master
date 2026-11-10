# PREREG: BATCH4_RTA_GEOM (C15 closeout; Map-C16, C17, C18)
Written 2026-10-24 at about 7:10 PM CDT, before any BATCH4 test. Owner: Arvin Hampton. New files only. CORE_FREEZE. All maps are **Category B**; a pass is a survived prediction, not a bridge. No quadratic-form → O_res maps. No Π, grading or T3-orbit carrier function is invented. order20 and the paper stream are not touched. Runs: nice, OMP_NUM_THREADS=1, ulimit -v 3000000. 67/68 are not targets.

Written residual objects (paths in NOTES):
- Core x_j = 21+9j (j = 0..538).
- Fibres β♯(x_j) = j mod 8.
- Towers τ: blocks of Ω = {0..4879}, the first 20 of size 21 and the rest of size 20.
- f(i) = τ(x_i), δf(i) = f(i+1) − f(i) on path edges e_i, i = 0..537.
- Product complex X_× = K_9 × P_{B′} with α(a,b) = sgn(a−b) and the mixed cochain α⊗δf on squares S(a,b;i) (Residual_Product_Complex.md).

## C15 closeout (prediction unchanged from BATCH3 PREREG, sha256 b57478f7…21b2)
k := #{companions c ∈ 0..104 : max over the 216 points of |A2_corner[:,c]| > 1e−10}, read from order18/data/a2_arrays.npz, array CO (A2_corner, RG4).
Gap guard: the result is VOID if any column max lies in [1e−13, 1e−7].
PASS iff 8 | k.

## Map-C16: β♯ equidistribution of tower changes (RG1′-type sector split → fibres)
Source: the P-odd/P-even split is balanced by the RG1′ reflections (order16). Target: the edges with δf(i) ≠ 0, classed by β♯ of the start index, i mod 8.
Prediction (NEW): the 8 class counts satisfy max − min ≤ 1.
Gate: Σδf = 241 (written). If the gate fails → VOID.

## Map-C17: palindromic tower occupancy (endpoint reflection ρ → core reversal)
Source: the RG1′ endpoint reflection. Target: n_t = #{j : τ(x_j) = t} over the touched towers, in tower order.
Prediction (NEW): the sequence (n_t) is a palindrome.
Gate: Σ_t C(n_t, 2) = 353 and 242 touched towers (both written). If the gate fails → VOID.

## Map-C18: permanent-class fibre pairing has the reversal symmetry
Source: P-even corner A2c (order18; P-even = invariant under the reflection P). Target: v_r = ⟨α⊗δf, Σ_{i ≡ r (8)} S(0,8;i)⟩ = α(0,8)·Σ_{i≡r} δf(i), r = 0..7.
The core reversal sends edge i ↦ 537 − i, which induces r ↦ (1 − r) mod 8.
Prediction (NEW): v_r = v_{(1−r) mod 8} for all r ("P-even" on the fibres).
PASS iff it holds exactly.
