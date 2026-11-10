# PREREG: order4b. Does A2 satisfy a weight-0 vector law under S?
Written 2026-10-24, before any order4b run.

## Object
A2 is the O(1) coefficient, by the order3c formula (lib3c.A012, read-only import). It is computed for 105 companions at the 216 points XS and at −1/x. Data go to data/A2.npz.

## Tests (SVD threshold 1e-9)
- **T0 (pure weight-0 law):** rank[A2(x) | A2(−1/x)] = rank A2(x).
- **T1 (affine law, secondary):** A2(−1/x) ∈ colspan[A2(x), |x|^{1/2}A1(x), |x|A0(x)]. This is a rank test on the 216 rows, flagged inconclusive if the span rank is ≥ 216.
- **Descriptive:** the same test at w = ½ and w = 1.

## Sign control (gating; it must pass)
- A0 at w=1: rank 36 and closed.
- A0 at w=0: not closed.

This shows the test separates weights. If either fails, the verdicts are void.

## Verdicts
- **T0:** "weight-0 law holds (Category B)" if closed; otherwise "falsified".
- **T1:** reported as stated.

## Anchor and grid
A2 was validated in order3c Map N (9/9 pass) on t_j = 2^{−j}·0.5/(297.5(2m)²), which is scaled to the denominator and to Q(21,−1) = 595/2. Here we add one anchor: A012 at x=1 must reproduce the order3c value to 1e-12.

## Certification
The entries involve logs, √π and the K-integrals, so mod-p certification is not feasible. Verdicts are Category B.

## Run order
Hash → scripts + SHA256SUMS → anchor → control → T0/T1 → RESULTS/NOTES/REPORT. nice, OMP_NUM_THREADS=1, <3 GB per process. No pushes.
