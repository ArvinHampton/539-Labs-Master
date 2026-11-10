# round2 RESULTS

Run on 2026-10-23 at about 10:15 PM CDT, after PREREG.sha256 was written (10:13 PM CDT; it was re-verified after the run: OK). Script `scripts/rc.py` (hash in `logs/SCRIPT_SHA256.txt`), output `logs/rc.log`. Run with `nice -n 19`, `OMP_NUM_THREADS=1`, `ulimit -v 3000000`; it took under 1 s. All distributions are exact big-integer counts over the 3^j words.

## Proofs

**R0 (affine form on a cylinder).** Let w = (r_0,…,r_{j−1}) and let n ∈ ℕ₀ satisfy T3^i(n) ≡ r_i mod 3 for i < j. Define B_w and C_w as in PREREG. Then 3^j T3^j(n) = B_w n + C_w.
*Proof.* Write u_i = T3^i(n). If u ≡ r mod 3 then T3(u) = (b_r u + d_r)/3. For r = 0: u/3. For r = 1, u = 3q+1: (4u+2)/3 = 4q+2. For r = 2, u = 3q+2: (2u−1)/3 = 2q+1. The claim holds for j = 0 (B = 1, C = 0). Assume 3^i u_i = B_i n + C_i. Then 3^{i+1} u_{i+1} = 3^i (b_{r_i} u_i + d_{r_i}) = b_{r_i}(B_i n + C_i) + d_{r_i} 3^i = B_{i+1} n + C_{i+1}. ∎ (The script also checks this for every n < 3^7.)

**R1 (the multiplier map is a proved no-go).** B_w = 2^{a(w)} with a(w) = 2·#{i : r_i = 1} + #{i : r_i = 2}. Under uniform words, a is a sum of j independent variables, each uniform on {0, 1, 2}.
1. Odd k. Let t = ord_k(2). As j → ∞, μ^B_{k,j} tends to the uniform measure on the subgroup ⟨2⟩ ⊂ (Z/k)^×. In particular μ^B_{k,j}(0) = 0 for all j. Since 0 ∈ Sq_k, the support of μ^B can never equal Sq_k. Its limit equals Sq_k ∖ {0} iff ⟨2⟩ = (Z/k)^{×2}.
2. k = 4, 8: μ^B_{k,j}(0) → 1. k = 12: μ^B_{12,j} → ½δ_4 + ½δ_8, and 8 is not a square mod 12.

Hence for no k in {4, …, 13} is the limiting support of μ^B equal to Sq_k.
*Proof.* B multiplies by b_r ∈ {1, 4, 2} = {2⁰, 2², 2¹}, so B_w = 2^{a(w)}.
- (1) 2^a mod k depends only on a mod t. For a character ψ(x) = e(hx/t) of Z/t with h ≢ 0 mod t, E[ψ(a)] = ((1 + ζ + ζ²)/3)^j with ζ = e(h/t) ≠ 1. Also |1 + ζ + ζ²| < 3, since equality in the triangle inequality forces ζ = 1. So E[ψ(a)] → 0 and a mod t becomes uniform. 2^a is a unit mod odd k, so it is never 0. The criterion for Sq_k ∖ {0} is the definition of equality of the two subgroups.
- (2) P(a ≤ 2) = P(at most two letters non-zero, in total weight ≤ 2) → 0. For a ≥ 3 we have 8 | 2^a. Mod 12, 2^a ≡ 4 for even a ≥ 2 and ≡ 8 for odd a ≥ 3, and a mod 2 becomes uniform by (1) with t = 2. Squares mod 12 are {0, 1, 4, 9}. ∎

By the preregistered rule R-B is recorded as a **proved no-go** and was not tested. The script's B-distributions at j = 120 agree with R1 (logs).

**R2 (R-C is not forced by P2/P3).** P2 says words are uniform. P3 concerns T3^L(n) mod M as n varies. C_w is a fixed integer function of w, and its law under uniform w is not determined by either statement. (For example, at k = 8 the exact law is non-uniform; see below.) So the test is not vacuous. ∎

## Test of R-C (translation map), j = 120, exact

| k | |Sq_k|/k | μ^C(Sq_k) | excess | leak (non-squares) | weak | strong |
|---|---|---|---|---|---|---|
| 4 | 0.5 | 0.25 | −0.25 | 0.75 | no | no |
| 5 | 0.6 | 0.6 | 0.0 | 0.4 | no | no |
| 7 | 0.5714 | 0.5714 | 0.0 | 0.4286 | no | no |
| 8 | 0.375 | 0.21875 | −0.156 | 0.78125 | no | no |
| 11 | 0.5455 | 0.5455 | 0.0 | 0.4545 | no | no |
| 12 | 0.3333 | 0.1667 | −0.167 | 0.8333 | no | no |
| 13 | 0.4615 | 0.4615 | 0.0 | 0.4615 | no | no |

- Weak predictions hold at 0 of 7 k, and strong at 0 of 7. Holm is vacuous: every p is 1. **R-C is falsified.**
- For odd k, μ^C is uniform to all printed digits at j = 60 and j = 120. Whether it is uniform in the limit is not proved here (Category B).
- For even k it is not uniform, and it puts *less* mass on squares than uniform does.

**Open-class target (k ≡ 0 mod 4), MIX classes, j = 120:**

| k | MIX class c | μ^C(c) | prediction "c ∈ OccFilt" (mass > 10⁻⁶) |
|---|---|---|---|
| 4 | 0 | 3^{−120} ≈ 5.6·10⁻⁵⁸ | falsified |
| 8 | 1 | 0.21875 | holds (conditional only; the true answer is open) |
| 12 | 0 | 3^{−120} | falsified |
| 12 | 4 | 0 | falsified |

The finite certificates give no zeros of g_k in MIX classes for d in (2000, 2·10⁷] (A39). So the R-C prediction "MIX class ∉ OccFilt" at k = 4 and 12 points against the available evidence. It does not prove anything about OccFilt.

## Descriptive notes
- The law of C_w mod 4 at j = 60 and j = 120 is (0, ¼, ½, ¼). The value at class 0 is exactly 3^{−j}. The step rule C ↦ b_r C + d_r 3^i mod 2 sends C to C for r = 0, to 0 for r = 1 and to 1 for r = 2. So C_w is odd iff the last non-zero letter of w is 2. No further analysis was done.
- The laws at j = 60 and j = 120 agree to the printed digits for every k.
