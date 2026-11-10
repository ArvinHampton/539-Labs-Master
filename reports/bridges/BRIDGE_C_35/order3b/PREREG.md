# PREREG: order3b. Locating the shadow Ξ by regrouping A1 across D, R, W
Written 2026-10-24, before any order3b run. Category B tests on top of a Category A regrouping. CORE_FREEZE is respected; nothing in order2/order3 is modified (read-only imports only).

## Objects
A1 is the t^{-1/2} coefficient (entry 107, order2). order3 Map 1 gives the exact split A1 = D + R + W[1] + W[7/2] + W[595/2].

New quantity: R is split by ray quadratic value, R[7/2] (rays ±(0,1)) and R[595/2] (rays ±(21,−1)). By order3 Map 1, R = R[7/2] + R[595/2]. Computed at the same 216 points XS (order2 lib2), 105 companions.

Data: order3/data/parts.npz (read-only) plus the new data/rays_split.npz.

## Groupings (fixed now)
**Q-class groups:**
- G[1] = W[1]
- G[7/2] = W[7/2] + R[7/2]
- G[595/2] = W[595/2] + R[595/2]
- G[D] = D

**Theta-characteristic groups (by column):**
- Θ1 = K2 ∪ K3 (characteristics (a+μ,0) and (μ,a); 70 columns), the pair exchanged by (α,β) → (−β,α).
- Θ2 = K4 (characteristics (μ,0); 35 columns).

These apply to A1, and to each Q-class group (8 more block tests).

## Closure test (same convention as order3)
A group F is closed at weight w iff rank[F(x) | diag(|x|^w)F(−1/x)] = rank F(x). The SVD threshold is 1e-9 relative, over the 216 points.

## Sign control (gating; it must pass before any verdict is read)
Using A0 from parts.npz:
- rank 36 and closed at w=1;
- joint rank > 36 at w=−1.

If the control fails, Map 2 is void.

## Predictions and verdict rules
- **P-Q (Q-class localisation).** Exactly one of G[1], G[7/2], G[595/2], G[D] is not closed at w=½ (and at w=1). All the others close at w=½ or at w=1.
  - Verdict "localised in class X" if this holds.
  - "Not localised by Q-class" if two or more fail.
- **P-Θ (characteristic localisation).** For A1 at w=½: exactly one of Θ1, Θ2 closes.
  - "Localised in the other characteristic" if this holds.
  - "Not localised by characteristic" if neither closes.
  - If both close, that contradicts order3 (A1 not closed). Flag it as an anomaly.
- **Descriptive only:** the A0 restricted to Θ1 and Θ2, and per-group ranks.

## Map 1 (Category A check)
R[7/2] + R[595/2] must equal order3 R to ≤1e-12 at every point. If not, stop.

## Run order
Hash → scripts + SHA256SUMS → Map 1 → sign control → closure tests → RESULTS/NOTES/REPORT.

nice, OMP_NUM_THREADS=1, ulimit -v 3000000. No pushes.
