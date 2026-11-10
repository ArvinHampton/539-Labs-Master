# PREREG order19 — affine law for A2c; profile obstruction; Map RG5
Written 2026-10-24 (America/Chicago) BEFORE any order19 numerics. CORE_FREEZE. Inputs read-only: order4b/data/A2.npz, order18/data/a2_arrays.npz (A2_lines, A2_corner at x and −1/x). A2c := A2_lit − A2_lines (= A2_corner by order18 RG4). k := 35^{−1/2}.

## 1. Exact value of c (derived here, before numerics)
Write τ = x + iε (ε = t/2π) and F(y0+z) ~ a0/w + a1 w^{−1/2} + a2 + O(w^{1/2}) with w = −iz (the expansion in t = 2πw; a0 = A0/2π, a1 = A1(2π)^{−1/2}, a2 = A2). For −1/τ: −1/τ − (−1/x) = iε/(x(x+iε)), so w = ε/(x² + ixε), 1/w = x²/ε + ix, w^{−1/2} = |x|ε^{−1/2}(1 + O(ε)).
Suppose F(−1/τ) = τ k M F(τ). Order ε^{−1}: a0(−1/x)x² = x kM a0(x). Order ε^{0}: a2(−1/x) + ix·a0(−1/x) = kM(x a2(x) + i a0(x)). By the ε^{−1} relation, ix·a0(−1/x) = i kM a0(x), so the A0 terms cancel exactly:
  **c = 0**, and the affine law is A2c(−1/x) = x·kM·A2c(x).
(The a1 term contributes only at order ε^{1/2}.) No fitting of c is performed.

## 2. Category A obstruction (written here)
**Proposition O2.** Let a2, a0 : Q^× → C^105 with a0(−1/x) = x^{−1}kM a0(x) for all x. If for some constant c, a2(−1/x) = x·kM a2(x) + c·M a0(x) for all x ∈ Q^×, then P a2 = −a2.
Proof. Apply at −1/x: a2(x) = (−1/x)kM a2(−1/x) + cM a0(−1/x) = −k²M² a2(x) − (c/x)kM² a0(x) + cM·x^{−1}kM a0(x) = −P a2(x), using M² = 35P. ∎
A2c is P-even (order18 RG3/RG4: A2c = A2_corner, ½A2(S^E)). Hence **no affine law of this form, for any c, holds for A2c on all of Q^× unless A2c ≡ 0**. The numerical test below is on x > 0 only (XS ⊂ (0,3]), where the obstruction does not by itself decide.

## 3. Test L0 (Category B)
Residual R = A2c(−1/x) − x·kM·A2c(x) on the 216 points x ∈ XS. **Primary metric (absolute):** ‖R‖_F. PASS if ‖R‖_F ≤ 1e−9; FAIL if ‖R‖_F ≥ 1e−4; else inconclusive. Relative ‖R‖_F/‖A2c(−1/x)‖_F is reported. Control C0 (A0 fixed-M law, absolute ‖·‖_F ≤ 1e−10) gates. Order18 already recorded FAIL for pure w = −½ and w = 0 (and w = −1 with free scalar, r = 0.058); not re-run, only reaffirmed by citation.
**Prediction:** L0 FAIL.

## 4. Map RG5 (residual-internal, NEW, exploratory)
A2_corner = C11 + ½C2a + (7/4)C2b with C11 = Σ_r f_r B̄1(ρ1/N)B̄1(ρ2/N), C2a = Σ_r f_r B2(ρ1/N), C2b = Σ_r f_r B2(ρ2/N). Statement: none of C11, C2a, C2b separately satisfies the x>0 law X(−1/x) = x^{w}·kM X(x) for w ∈ {−1, 0, 1} (absolute residual ≥ 1e−4 for each, i.e. FAIL of every law). Falsified (RG5 FAIL) if any component passes (≤ 1e−9). Prior: uncertain.
No Resonant-side object is used or invented; E1–E3 OPEN; no bridge claim.
Runs: nice, OMP_NUM_THREADS=1, <3 GB; no push/sends; new files only.
