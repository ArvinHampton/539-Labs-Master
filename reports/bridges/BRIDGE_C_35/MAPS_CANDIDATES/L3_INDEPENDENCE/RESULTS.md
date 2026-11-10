# RESULTS: L3_INDEPENDENCE
PREREG.md sha256 5e9d28ff1785e76f3b8612edabf01c3f01df6e339e34304e86b1fb80c6336bcb. It was hashed after exploration (data/explore.sha256) and before the holdout run (scripts/test.py → data/test.json, logs/test.log).

Holdout: seeds 'l3holdout-0..5999' × 539 steps, with a 20-step burn-in. L3a uses every 8th step (n = 390,000). L3b uses all hits (346,349).

| Check | Measured | Threshold | Verdict |
|---|---|---|---|
| A1 χ² indep. u mod 3 vs u mod 8 | 7.74 (df 10) | ≤ 29.59 | PASS |
| A2 fully specified (1/3)·w/32 | χ² = 11.42 (df 17), TV = 0.0023 | ≤ 40.79, ≤ 0.006 | PASS |
| A3 max conditional deviation from 1/3 | 0.0051 | ≤ 0.02 | PASS |
| A4 χ² indep. u mod 3 vs u mod 64 | 94.95 (df 94) | ≤ 142.12 | PASS |
| A5 states with u ≡ 0 mod 4 after burn-in | 0 | = 0 | PASS |
| L3b fibre law max abs deviation | 5.2·10⁻⁴ | ≤ 0.005 | PASS |
| L3b χ² on the six open fibres | 3.94 (df 5) | ≤ 20.52 | PASS |

Measured u mod 8 law (classes 1, 2, 3, 5, 6, 7): .2190, .2510, .1561, .0312, .2496, .0931. Predicted: .21875, .25, .15625, .03125, .25, .09375.
The hit fibre law was (.0307, .2500, .0938, 0, .2184, .2505, .1567, 0), with zero hits in fibres 3 and 7 after burn-in.

**L3a: PASS (Category B). L3b: PASS (Category B). Bridge: NO** (residual-internal only).
