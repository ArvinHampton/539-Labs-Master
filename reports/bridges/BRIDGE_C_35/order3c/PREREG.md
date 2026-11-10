# PREREG: order3c. The analytic O(1) term A2
Written 2026-10-24, before any order3c run.

## Claim (to be proved in RESULTS, Category A if the proof is complete)
For a piece P (sign σ, offset c, basis U, period N=2m), write:
- Q̃(z) = p z1² + q z1z2 + r z2²;
- E(z) = Q̃(z) + l1z1 + l2z2 + Q0, with Q0 = Q(α+c);
- f N-periodic, as in order2 entry 107.

As t→0+:

Σ_{z≥0} f(z)e^{−tE(z)} = t^{−1}mean(f)Ar + t^{−1/2}A1_P + A2_P + O(t^{1/2}),

A2_P = mean(f)(½K(l) − Q0·Ar) + W_1·l2/(2r) + W_2·l1/(2p) + (q/4)(Σ_z f B2(z1/N)/r + Σ_z f B2(z2/N)/p) + Σ_z f B1(z1/N)B1(z2/N),

where:
- K(l) = ∫∫_{u≥0}(l1u1 + l2u2)² e^{−Q̃(u)} du;
- W_i = N^{−1}Σ_z f B1(z_i/N);
- sums run over z mod N in {0..N−1}²;
- B1(y) = y−½ and B2(y) = y²−y+1/6.

For a ray {c+bu: b≥0} with period N:

Σ_b f e^{−tQ(α+c+bu)} = t^{−1/2}(√π/2)Q(u)^{−1/2}mean f + [−mean(f)·B(u,α+c)/(2Q(u)) − Σ_{b mod N} f(b)B1(b/N)] + O(t^{1/2}).

A2 = Σ_pieces σ·A2_P + Σ_walls (signed)·(ray constant).

## Numerical check (Map N, Category B)
Series: the normalized RTA series S_{a,0}, i.e. Σ wt(v) e(xQ(a+v)) e^{−tQ(a+v)} (as in order3 map0).

x set: {1, 1/2, 1/3, 2/3, 1/4, 1/5, 1/6, 1/7, 3/7}.

t-grid, scaled to the denominator and the long edge (21,−1) with Q=595/2:
- t_j = 2^{−j}·0.5/(297.5·(2m)²), j = 0..7.
- Fit (S − A0/t − A1/√t) on {1, t^{1/2}, t, t^{3/2}}.
- Report the constant c0.

Criteria, with err = |c0 − A2|/max(1,|A2|):
- pass if err ≤ 1e-3;
- falsify if err > 1e-2;
- inconclusive between.

Overall: pass if all x pass; falsified if any x falsifies.

## Sign control (gating)
Recompute A2 with the B1·B1 corner term sign flipped. It must fail (err > 1e-2) at ≥ 1 x where |Σ f B1B1| > 0.05. Otherwise the check is not discriminating and the verdict is void.

## Run order
Hash → scripts + SHA256SUMS → sign control → Map N → RESULTS/NOTES/REPORT.

Same rules as before; no pushes; no ledger edits.
