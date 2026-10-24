# RESULTS (order 2): t^{-1/2} terms of q^{-7/20}·C and of the 105-series companion

2026-10-24, runs 08:23–08:29 AM CDT (America/Chicago). PREREG.md sha256 059257dbd42b33c5e2d4f3ad7a6797081bbb454a7655c1268c52fc09a599f3fd, hashed before any run and re-verified after (OK). Script hashes: `scripts/SHA256SUMS`. Data: `data/`. Logs: `logs/`. Notation: PREREG §1.

## Verdicts
| Map | Prediction | Verdict | Category |
|---|---|---|---|
| 1, formula | Explicit closed form for the order-2 profile A1 | **Proved** (theorem below). Validation: reproduces the written a_P = 0.5256172043 to 10 digits; the piece decomposition reproduces A0 = I·G to 1e−17 | A |
| 1, preregistered numerics | ≥ 95 % pass, none falsify | **Falsified by its own rule** (33 pass, 24 inconclusive, 39 falsify of 96). Cause found: the t-grid was scaled to m but not to the long cone edge u1 = (21,−1). Disclosed post-hoc rerun with a grid scaled to Q(u1)·(2m)²: all 9 points tested, across every failing denominator class plus controls, agree with the formula to ≤ 1e−5 | B |
| 2 | A1(x) ≠ 0 on the leading-order zero set | **Confirmed**: 106 of 106 points certified nonzero (interval arithmetic), min \|A1\| = 0.1229 | A |
| 3 (as preregistered) | No single-weight closure at order 2 | **Invalid by the preregistered rule**: the control failed because the prereg wrote the weight factor with the wrong sign | — |
| 3 (corrected convention, disclosed deviation) | same | Control passes (rank 36 = 36). Order 2: rank A = 105, rank [A \| B_w] = 138 for w = 1/2 and 1, so **not closed**; well conditioned (σ_min/σ_max ≥ 0.013) | B |

## Theorem (order-2 expansion; Map 1)
Setting. Fix one of the 105 pairs (α,β) and a rational x = h/m (m ≥ 1, either sign of h; for x = 0 take m = 1). Put N = 2m. For a piece (sign ε, offset c ∈ Z², basis U = (u1,u2) with integer columns) let
- p = Q(u1), r = Q(u2), q = B(u1,u2), Q̃(z) = Q(Uz), l_i = B(α+c, u_i);
- f(z) = e(x·Q(α+c+Uz) + B(α+c+Uz, β)) for z ∈ Z²;
- E(z) = Q(α+c+Uz) = Q̃(z) + l1 z1 + l2 z2 + Q(α+c).
Then, as t → 0+,
t·Σ_{z∈Z²_{≥0}} f(z)e^{−tE(z)} = mean(f)·Ar + t^{1/2}·[ −mean(f)(l1 J_a + l2 J_b) − (√π/2)( r^{−1/2} W_1 + p^{−1/2} W_2 ) ] + O(t),
where mean(f) = N^{−2}Σ_{z mod N} f(z), W_i = N^{−1}Σ_{z mod N} f(z)·B1(z_i/N), B1(y) = y − ½ (z_i taken in {0,…,N−1}), Ar = ∫∫_{R²_{≥0}} e^{−Q̃}, J_a = ∫∫ z1 e^{−Q̃}, J_b = ∫∫ z2 e^{−Q̃}, with closed forms
Ar = log((q+√Δ)/(q−√Δ))/(2√Δ), Δ = q² − 4pr; J_a = (√π/4)·(2/(4pr−q²))·(2√r − q/√p); J_b = (√π/4)·(2/(4pr−q²))·(2√p − q/√r).
For a 1-D wall {c + b·u : b ≥ 0}: t·Σ_{b≥0} f(c+bu)e^{−tQ(α+c+bu)} = t^{1/2}·(√π/2)·Q(u)^{−1/2}·mean_{b mod N} f(c+bu) + O(t).
Summing over the decomposition of PREREG §2 (the orthant; −1 times the 21 pieces r·e1 + Nu1 + Nu2 of K₊; +1 times the 21 pieces of K₋ = −K₊; the four wall corrections ±½) gives A0 and A1 for S_{α,β}, in particular for q^{−7/20}C = S_{a,0}.

*Proof.*
(a) **Periodicity.** For u ∈ Z² and w = α+c+Uz, the phase changes under w ↦ w + Nu by x(N·B(w,u) + N²Q(u)) + N·B(u,β). Since Aμ ∈ Z² and Aa = (0, 7/2), the vector Aα lies in Z² or in (0, 7/2) + Z², so B(w,u) ∈ ½Z and x·N·B(w,u) ∈ (h/m)(2m)(½Z) ⊂ Z. Next, Q(u) ∈ ½Z gives x·N²Q(u) ∈ 2mhZ. Finally, β ∈ {0, a} and B(u,a) = (7/2)u₂ ∈ ½Z give N·B(u,β) ∈ Z. So f is N-periodic in each z_i. (The scripts also assert this for every piece and point used.)
(b) **Decomposition.** K₊ ∩ Z² = ⊔_{r=0}^{20} (r e1 + N u1 + N u2). For n = 21j + r with 0 ≤ r < 21, the condition n + 21k ≥ 0 is equivalent to k ≥ −j, and then (n,k) = r e1 + j u1 + (k+j) u2. The walls n = 0 and n + 21k = 0 are the rays N u2 and N u1 of the r = 0 piece, and every other piece lies in the interior. Hence H_7 = Σ_{K₊ pieces} − ½(two K₊ walls) − [Σ_{K₋ pieces} − ½(two K₋ walls)], and the origin gets weight 0 = w(0). C = P_orth − H_7, with P_orth the closed orthant (weight 1).
(c) **Bounds.** For every piece, q ≥ 0 and p, r > 0 (orthant: p = 1, q = 7, r = 7/2; K± pieces: p = 595/2, q = 140, r = 7/2), so Q̃(z) ≥ κ|z|² on z ≥ 0 with κ = min(p,r). Then E(z) ≥ (κ/2)|z|² − C₀, |∇E| ≤ C(|z|+1) and |∇²E| ≤ C. With F_t = e^{−tE} and 0 < t ≤ 1, there is a constant K (depending on the piece, x, α, β) with:
  - F_t ≤ K e^{−tκ|z|²/2};
  - |∇F_t| ≤ K t(|z|+1) e^{−tκ|z|²/2};
  - |∇²F_t| ≤ K (t + t²(|z|+1)²) e^{−tκ|z|²/2}.
(d) **One-dimensional lemma.** Let g ∈ C²[0,∞) with g, g′, g″ integrable, and let 0 ≤ α′ < N be an integer. Then
  Σ_{j≥0} g(α′+Nj) = N^{−1}∫_0^∞ g − B1(α′/N)·g(0) + R, with |R| ≤ C_N( sup_{[0,N]}|g′| + ∫_0^∞|g″| ).
  Proof. Put h(s) = g(α′+Ns). Euler–Maclaurin to second order gives Σ_{j≥0} h(j) = ∫_0^∞ h + ½h(0) − P₂(0)h′(0) − ∫_0^∞ P₂({s})h″(s)ds, with P₂(y) = ½(y² − y + 1/6), so |P₂| ≤ 1/12. Here h′(0) = Ng′(α′) and ∫|h″| ≤ N∫|g″|. Also ∫_0^∞ h = N^{−1}∫_0^∞ g − N^{−1}∫_0^{α′} g, with ∫_0^{α′} g = α′g(0) + O(N² sup_{[0,N]}|g′|), and ½h(0) = ½g(0) + O(N sup|g′|). Since ½ − α′/N = −B1(α′/N), the lemma follows.
(e) **Two dimensions.** Fix a residue (α′,β′) mod N.
  - *Sum over z1.* For each z2 ≡ β′, apply (d) to g(s) = F_t(s, z2). The remainders summed over z2 are O(Σ_{b≥0} t(b+N+1)e^{−tκb²/2}) + O(Σ_b e^{−tκb²/2}(t^{1/2} + t^{3/2}(b+1)²)), and both are O(1).
  - *First term.* This leaves Σ_{z2≡β′} N^{−1}∫_0^∞ F_t(s,z2) ds. Apply (d) to g(b) = N^{−1}∫_0^∞ F_t(s,b) ds. By (c), sup_{[0,N]}|g′| = O(1) and ∫|g″| ≤ ∫∫|∂_b²F_t| = O(1).
  - *Second term.* Σ_{z2≡β′} B1(α′/N)F_t(0,z2) = B1(α′/N)·N^{−1}∫_0^∞ F_t(0,b) db + O(1), by first-order Euler–Maclaurin: the error is at most sup F_t + ∫|∂_bF_t(0,b)| db = O(1).
  - *Result.* Σ_{z≡(α′,β′), z≥0} F_t(z) = N^{−2}∫∫F_t − N^{−1}B1(β′/N)∫_0^∞F_t(s,0)ds − N^{−1}B1(α′/N)∫_0^∞F_t(0,b)db + O(1).
  Multiply by f(α′,β′) and sum over residues.
(f) **Integrals.**
  - Substituting z = u/√t: ∫∫F_t = t^{−1}∫∫ e^{−Q̃(u) − √t(l1u1 + l2u2) − tQ(α+c)} du = t^{−1}(Ar − √t(l1J_a + l2J_b)) + O(1). Taylor's theorem applies, with an integrable majorant from (c).
  - ∫_0^∞F_t(s,0)ds = ½√(π/(tp)) + O(1) and ∫_0^∞F_t(0,b)db = ½√(π/(tr)) + O(1).
  - Multiplying by t gives the stated expansion.
  - The 1-D wall statement is (d) at zeroth order together with ∫_0^∞ e^{−tQ(α+c+bu)}db = ½√(π/(tQ(u))) + O(1).
(g) **Closed forms.** Write z = ρ(1,λ). Then Ar = ∫_0^∞ dλ/(2Q̃(1,λ)) and J_a = (√π/4)∫_0^∞ Q̃(1,λ)^{−3/2} dλ. The antiderivative 2(2rλ+q)/((4pr−q²)√(rλ²+qλ+p)) of (rλ²+qλ+p)^{−3/2} gives J_a. J_b follows by exchanging the roles of the two coordinates (λ = z1/z2). For Ar, the roots of rλ²+qλ+p are negative since q > √Δ. ∎

**Corollary 1.** A0 = I·G_{α,β}(x) for each companion, and I·G_{a,0} for q^{−7/20}C. The K₊ and K₋ pieces cancel at this order, as in the parent Lemma 2: each sector's residue mean equals the full mean asymptotically, and K₋ = −K₊.
**Corollary 2 (new).** A1(x)/√π is an algebraic number for every rational x and every companion. The transcendental log ε of the leading order does not occur at order 2: all ingredients are cyclotomic numbers, rationals, and square roots of p, r and 4pr − q².
**Checks.**
- `data/validate.json`: orthant only, x = 0, (α,β) = (a,0): the formula gives 0.5256172043318 against the written a_P = 0.5256172043.
- The piece decomposition reproduces A0 = I·G for 63 (family, μ, x) cases, including negative x, with maximum difference 1.4e−17.

### Numerical test of Map 1 (Category B)
- **Preregistered** (`data/map1_numeric.json`): t_j = 0.02·2^{−j}/m². By denominator: m = 1, 7 pass (21/21); m = 5: pass or inconclusive; m = 3: inconclusive; m = 10: half pass, half falsify; every point with m ∈ {2, 4, 6, 8} falsifies; m = 9: falsify or inconclusive. Totals: 33 pass, 24 inconclusive, 39 falsify. Recorded verdict: **falsified**.
- **Cause.** The K± pieces have the edge u1 = (21,−1) with Q(u1) = 297.5. Their Euler–Maclaurin regime needs t·Q(u1)·N² ≪ 1. The prereg grid had t·N² ≤ 0.08, so t·Q(u1)·N² ran from about 0.74 up to 24.
- **Post-hoc** (`scripts/posthoc_map1_conescale.py`, `data/posthoc_map1_conescale_*.json`): grid t_j = 2^{−j}·0.5/(297.5·(2m)²), sums streamed row by row. At x = 1/2, 1/3, 1/4, 5/6, 3/8, 2/9, 3/10, 1/5 and the control 1/7, the fitted coefficient equals the predicted A1 to ≤ 1e−5 relative.

## Map 2: nonvanishing on the leading-order zero set (Category A)
**Statement.** For every x ∈ Z0 = {x ∈ X216 : 2 | m or 5 | m} (105 points) and for y = −1/5, A1(x) ≠ 0 for q^{−7/20}C. Since A0(x) = 0 there, t·|q^{−7/20}C(e(x)e^{−t})| = |A1(x)|·t^{1/2} + O(t). So at these points the normalized Bridge Series grows exactly like t^{−1/2}, with a nonzero explicit constant.
**Certificate** (`data/map2_interval.json`). The theorem's formula was evaluated in mpmath interval arithmetic at 60 digits. Exact rational histograms by phase were computed first, then the cosines and sines were evaluated as intervals. The interval for |A1|² excludes 0 at all 106 points; the maximum width is 6e−59 and the minimum |A1| is 0.12292. Rigour rests on the theorem above.
**RTA Fricke sample.** At y = −1/5 (the W_7 image of x = 5/7, where the leading order vanishes) |A1| = 0.428589. So the RTA sample at x = 5/7 has a definite order-2 partner.
**Descriptive (Category B).** |A1(1/2)| = |A1(5/2)| = 0.44311346272638 = √π/4 to 15 digits. Not proved.

## Map 3: no single-weight vector law at order 2 (Category B)
Data: `data/map3_profiles.npz` (A0, A1 at x and at −1/x for the 105 companions and 138 points) and `data/map3_closure.json`.
- **As preregistered** (B_w = |x|^{−w}·A1(−1/x)), the control on the leading profiles fails: rank 72 instead of 36. The leading law reads A0(−1/x) = |x|^{−1}·M·A0(x) (parent Theorem 3), so the correct row factor is |x|^{+w}. By the prereg's own rule Map 3 is **invalid** as written.
- **Corrected convention** (B_w = |x|^{+w}·A1(−1/x); a disclosed deviation):
  - control: rank[A0 | B_1] = 36 = rank A0;
  - order 2: rank A1 = 105 (σ_min/σ_max = 0.0026), and rank[A1 | B_w] = 138 (full row rank, σ_min/σ_max ≈ 0.013) for w = 1/2 and w = 1.
  - A closure would force rank ≤ 105. So **the order-2 profiles have no vector-valued law of weight 1/2 or 1 within their own span**.
- **Additional observation.** The 105 order-2 profiles are linearly independent on 138 points, against only 36 at leading order. The order-2 data do not factor through V.

## New Category A facts (proposed, ledger not edited)
1. An explicit, proved order-2 (t^{−1/2}) formula for q^{−7/20}C and for each of the 105 companion series at every rational. Error O(t) after multiplying by t; full proof above.
2. A1/√π is algebraic at every rational: the order-2 term carries no log(6+√35).
3. A1 ≠ 0 at all 106 tested points where the leading term vanishes (interval certificate). There t^{−1/2} is the exact growth order of q^{−7/20}C.

## Not shown / limits
- Map 3 is floating point and finite (138 points), so it is Category B. It does not exclude a law in a larger space, for example with period functions or the shadow Ξ added.
- The O(1) term, quantum-modular period functions and Ξ were not attempted. No statement here concerns g_k, T3, 539, Resonant Number Theory, TPC or RH.
