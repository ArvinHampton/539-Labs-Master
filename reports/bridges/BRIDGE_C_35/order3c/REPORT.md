# REPORT — Bridge C order3c (analytic O(1) term)
PREREG sha256 cd14c9ab…d8ad (unchanged). Scripts are hashed in scripts/SHA256SUMS.

## Statement (proved below)
Notation is as in order2 entry 107. For a piece with basis U, offset c, companion (α,β), x = h/m and N = 2m:
- Q̃(s) = p s1² + q s1s2 + r s2², positive on the closed quadrant, with q > 0 and Δ = q² − 4pr > 0;
- E(s) = Q̃(s) + l1s1 + l2s2 + Q0, with Q0 = Q(α+c);
- f is N-periodic on Z²_{≥0}, with |f| = 1.

Then, as t → 0+:

Σ_{s∈Z²_{≥0}} f(s)e^{−tE(s)} = t^{−1}mean(f)Ar + t^{−1/2}A1_P + A2_P + O(t^{1/2}),

A2_P = mean(f)(½K(l) − Q0Ar) + W_1 l2/(2r) + W_2 l1/(2p) + (q/4)(V_1/r + V_2/p) + C,

where:
- K(l) = ∫∫_{R²_{≥0}}(l1u1 + l2u2)²e^{−Q̃(u)}du;
- W_i = N^{−1}Σ_z f(z)B1(z_i/N);
- V_i = Σ_z f(z)B2(z_i/N);
- C = Σ_z f(z)B1(z1/N)B1(z2/N);
- z runs over {0,…,N−1}².

For a wall {c + bu : b ≥ 0}, with l_u = B(u, α+c), the constant term is −mean(f)·l_u/(2Q(u)) − Σ_{b<N} f(b)B1(b/N).

Hence A2 = Σ_pieces σ_P A2_P + Σ_walls σ_w(wall constant) for every companion and every x. This uses the same signed piece/wall decomposition as entry 107.

In polar coordinates, K_ij = ½∫_0^{π/2} e_i(θ)e_j(θ)/φ(θ)² dθ, with e = (cos θ, sin θ) and φ(θ) = Q̃(e(θ)). (Ar = ½∫dθ/φ was checked against the entry-107 closed form to 1e-12.)

## Proof
**(i) One-variable Euler–Maclaurin.** Let h be C³ on [0,∞) with h, h′, h″, h‴ integrable, and y0 ∈ [0,1). Then

Σ_{m≥0} h(N(y0+m)) = N^{−1}∫_0^∞ h − B1(y0)h(0) − (N/2)B2(y0)h′(0) + R_3,

with |R_3| ≤ (N²/6)·sup|B̃3|·∫_0^∞|h‴|. This is the standard periodic-Bernoulli form of Euler–Maclaurin applied to H(y) = h(Ny) on [y0,∞), written relative to the base point 0.

**(ii) Scaling.** Put F_t(s) = e^{−tE(s)}. On the closed quadrant Q̃(s) ≥ κ|s|² for some κ > 0, since q > 0 and p, r > 0 for all pieces. So:
- every ∂^a F_t is bounded by C_a t^{|a|/2}(1 + (√t|s|)^{|a|})e^{−tκ|s|²/2};
- hence ∫_0^∞|∂_i^k F_t(s)| ds_i = O(t^{(k−1)/2}) uniformly in the other variable;
- ∫∫|∂^a F_t| = O(t^{|a|/2 − 1}).

**(iii) Iteration.** Fix a residue class z = (α′,β′). Apply (i) in s2 (step N, offset β′/N), then apply (i) in s1 to each resulting term.

Main terms that survive at order t^0 or lower:
- N^{−2}∫∫F_t;
- −N^{−1}B1(β′/N)∫_0^∞F_t(s,0)ds and −N^{−1}B1(α′/N)∫_0^∞F_t(0,s)ds;
- −½B2(β′/N)∫_0^∞∂_2F_t(s,0)ds and −½B2(α′/N)∫_0^∞∂_1F_t(0,s)ds;
- +B1(α′/N)B1(β′/N)F_t(0,0).

Cross terms and remainders:
- B1·(N/2)B2·∂F_t(0,0) = O(t^{1/2});
- (N/2)B2(α′/N)·∂_1F_t(0,0) = O(t^{1/2});
- the R_3 terms are O(N²∫|∂³F_t|) = O(t^{1/2}), by (ii);
- the s-integrals of the s2-remainders are O(N²·∫∫|∂_2³F_t|·…) = O(t^{1/2}), by (ii).

So every neglected term is O(t^{1/2}).

**(iv) Each surviving term to O(t^{1/2}).**
- *Area term.* Substitute u = √t s: ∫∫F_t = t^{−1}∫∫e^{−Q̃(u) − √tL(u) − tQ0}. Taylor's theorem with the majorant from (ii) gives t^{−1}Ar − t^{−1/2}(l1J_a + l2J_b) + (½K(l) − Q0Ar) + O(t^{1/2}).
- *Edge integrals.* ∫_0^∞F_t(s,0)ds = ½√(π/(tp)) − l1/(2p) + O(t^{1/2}), since ∫_0^∞ue^{−pu²} = 1/(2p). Likewise ∫_0^∞F_t(0,s)ds = ½√(π/(tr)) − l2/(2r) + O(t^{1/2}).
- *Derivative integrals.* ∫_0^∞∂_2F_t(s,0)ds = −t∫(qs + l2)e^{−t(ps² + l1s + Q0)}ds = −q/(2p) + O(t^{1/2}). Similarly ∫_0^∞∂_1F_t(0,s)ds = −q/(2r) + O(t^{1/2}).
- *Corner.* F_t(0,0) = 1 + O(t).

**(v) Summing.** Multiply by f(z) and sum over z. The class factors give:
- mean(f) from the N^{−2} term;
- W_i from the N^{−1}B1 terms;
- V_i from the B2 terms;
- C from the corner term.

Collecting the t^0 parts gives A2_P. The t^{−1} and t^{−1/2} parts reproduce entry 107, which is a consistency check.

**Walls.** These are the one-variable case of (i) with h(b) = e^{−tQ(α+c+bu)}, and the constant term comes from the same edge-integral expansion.

**Assembly.** Summing over the signed pieces and walls gives A2. The decomposition is the finite signed identity of entry 107 (orthant, 2×21 pieces, 4 half-weight walls), so the O(t^{1/2}) remainders add up to O(t^{1/2}). ∎

**Category:** A. This is a finite formula with an explicit remainder order. The constants in O(t^{1/2}) depend on N and the piece and are not made numerically explicit.

## Sign control (gating)
The formula was recomputed with the corner term C sign-flipped. Of the 9 x values, 7 have |C_total| > 0.05; x = 1/2 has C_total = 0. At every x with |C_total| > 0.05, the flipped formula fails:
- err_flipped from 0.25 to 2.92, all > 1e-2;
- the check discriminates. **Passed.**

## Map N (Category B): brute-force series S_{a,0}
Grid: t_j = 2^{−j}·0.5/(297.5(2m)²), j = 0..7. Fit on {1, t^{1/2}, t, t^{3/2}}.

| x | A2 (formula) | c0 (fit) | rel. err | verdict |
|---|---|---|---|---|
| 1 | −0.3232819 − 0.4449593i | −0.3232819 − 0.4449593i | 4.4e-10 | pass |
| 1/2 | ≈0 (1.6e-15) | 2.1e-8 | 2.1e-8 | pass |
| 1/3 | 0.2436643 + 0.3827023i | 0.2436643 + 0.3827023i | 2.1e-9 | pass |
| 2/3 | −0.4528349 + 0.0278183i | same to 1e-9 | 1.7e-9 | pass |
| 1/4 | 2.4890282 + 0.2339631i | 2.4890281 + 0.2339631i | 5.1e-8 | pass |
| 1/5 | 1.1047360 − 0.1395606i | same to 1e-8 | 5.0e-9 | pass |
| 1/6 | 2.3314379 + 1.8879612i | 2.3314376 + 1.8879609i | 1.4e-7 | pass |
| 1/7 | 1.0780550 − 0.3522517i | same to 1e-8 | 8.5e-9 | pass |
| 3/7 | 0.5314255 + 0.3597670i | same to 2e-8 | 1.7e-8 | pass |

**Verdict: pass, 9/9.** The largest relative error is 1.4e-7 (threshold 1e-3). These A2 values also reproduce the descriptive order3 Map 0 estimates.
