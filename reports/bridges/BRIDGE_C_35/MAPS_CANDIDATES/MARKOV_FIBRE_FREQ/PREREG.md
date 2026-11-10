# PREREG: MARKOV_FIBRE_FREQ
Written after exploration (scripts/explore.py, logs/explore.log, hashes in data/explore.sha256), before any holdout test.

Model: lifted Markov chain of T3 on u mod M = 2^k·27. Each residue r mod M is lifted uniformly to its 3 lifts mod 3M, and T3(lift) mod M is taken. Long-run distribution comes from power iteration. Fibre of a hit u≡3 (mod 9) is β̂ = ((u−21)/9) mod 8. Equivalently β̂ ≡ u − 5 (mod 8).

Prediction (Category B model output; stable for k = 3,5,7,9,11, i.e. already exact at M = 216):
P(β̂ = 0..7 | hit) = (1, 8, 3, 0, 7, 8, 5, 0) / 32
= 0.03125, 0.25, 0.09375, 0, 0.21875, 0.25, 0.15625, 0. Hit rate is 1/9.

Holdout: seeds sha3_512(b'mfholdout-%d') for d = 0..2999, each run for 539 T3 steps. All hits are counted. These seeds differ from 'explore-', 'holdout-' and 'mfexplore-'.

Tests:
- M1: χ² over the six open fibres {0,1,2,4,5,6} against the predicted (renormalized) frequencies must be ≤ 20.52 (df = 5, p = 0.001). → PASS/FAIL
- M2: the share of hits in fibres {3,7} must be ≤ 0.001. These are the prefix exceptions under Lemma V.
- M3 (non-vacuity): the uniform-on-six null must be rejected, with χ² > 20.52. If M1 passes and M3 fails, the verdict is VACUOUS.
- Overall PASS requires M1, M2 and M3 to all pass.
