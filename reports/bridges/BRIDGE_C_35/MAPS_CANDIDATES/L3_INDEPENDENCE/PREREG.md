# PREREG: L3_INDEPENDENCE
Written after exploration (data/explore.sha256: explore.py, common.py, explore.log) and before any holdout.
Explore used seeds 'l3explore-*', 300×539 steps, skipping the first 20 steps. Explore results: mod-8 χ²_ind = 18.8 (df 10), χ²_full = 31.1 (df 17), TV = 0.0051. Mod-64 χ²_ind = 130.8 (df 94).

To reduce autocorrelation along orbits, the holdout samples every 8th step, after a 20-step burn-in.

Holdout: seeds 'l3holdout-d', d = 0..5999, 539 steps each, thinned every 8th step after i ≥ 20. These seeds are distinct from explore-, holdout-, mfexplore-, mfholdout- and l3explore-.

Nulls:
- L3a (independence and uniformity on the closed class {u ≢ 0 mod 4}):
  - A1: χ² independence of u mod 3 vs u mod 8 ≤ 29.59 (df 10, p = 0.001).
  - A2: fully specified null P(a, c) = (1/3)·w_c/32, with w = {1:7, 2:8, 3:5, 5:1, 6:8, 7:3}. Requires χ² ≤ 40.79 (df 17) and TV ≤ 0.006.
  - A3: max_c |P(u mod 3 = a | u mod 8 = c) − 1/3| ≤ 0.02.
  - A4 (deeper): χ² independence of u mod 3 vs u mod 64 ≤ 142.12 (df 94).
  - A5: zero states with u ≡ 0 mod 4 after burn-in.
- L3b (fibre-law stability): using all hits after burn-in (not thinned), the fibre law must stay within max|Δ| ≤ 0.005 of (1,8,3,0,7,8,5,0)/32, and its χ² on the six open fibres must be ≤ 20.52. Note that thinning applies only to L3a.

Verdicts: L3a PASS iff A1–A5 all pass. L3b PASS iff both of its conditions pass.
Non-vacuity: A2 and L3b are non-uniform, fully specified laws. A1 and A4 could still pass under an arbitrary mod-8 marginal.
