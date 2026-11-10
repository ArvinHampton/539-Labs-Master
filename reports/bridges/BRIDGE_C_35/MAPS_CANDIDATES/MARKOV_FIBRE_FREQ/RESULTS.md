# RESULTS: MARKOV_FIBRE_FREQ
PREREG.md sha256 a56c5e85e7cd004abc56e40b0a5a86783b383f150ba5b90ec122832237200cc5. It was hashed after exploration (data/explore.sha256) and before the holdout run (scripts/test.py → data/test.json, logs/test.log).

Holdout: 3000 seeds 'mfholdout-d' × 539 steps = 1,617,000 steps, giving 179,050 hits (hit rate 0.11073).

| fibre β̂ | predicted (×1/32) | predicted | measured | count |
|---|---|---|---|---|
| 0 | 1 | 0.03125 | 0.03205 | 5739 |
| 1 | 8 | 0.25000 | 0.24959 | 44689 |
| 2 | 3 | 0.09375 | 0.09469 | 16955 |
| 3 | 0 | 0 | 0.00012 | 21 (prefix) |
| 4 | 7 | 0.21875 | 0.21654 | 38772 |
| 5 | 8 | 0.25000 | 0.25008 | 44777 |
| 6 | 5 | 0.15625 | 0.15677 | 28069 |
| 7 | 0 | 0 | 0.00016 | 28 (prefix) |

| Test | Measured | Threshold | Verdict |
|---|---|---|---|
| M1: χ² on the 6 open fibres vs prediction | 9.80 | ≤ 20.52 | PASS |
| M2: share of fibres {3,7} | 2.7·10⁻⁴ | ≤ 10⁻³ | PASS |
| M3: uniform-on-six null rejected (non-vacuity) | χ² = 42 684 | > 20.52 | PASS |

**Overall: PASS (Category B, numerical).** The result is non-vacuous: the relative rates on {0,1,2,4,5,6} = 1:8:3:7:8:5 are predicted and confirmed.
**Bridge: NO.** This is residual-internal only.

Post-test exact check (scripts/exact.py, logs/exact.log; sympy rational solve at M = 216): fibre law = (1/32, 1/4, 3/32, 0, 7/32, 1/4, 5/32, 0) and hit rate = 1/9 exactly. Both are Category A as statements about the lifted chain.
