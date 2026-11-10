# NOTES: PATTERN_BNU_RR
## Lemma PB1 (Category A)
B(ν,a) = (7/2)ν2, since Aa = (0,7/2). With ν2 = α2 + n2 and 35α2 ∈ Z, 10·B(ν,a) = 35ν2 = 35α2 + 35n2. Since 35 ≡ 3 is a unit mod 8, each label's fibre is uniform on Z/8. So **every** non-negative label pool gives exactly (1/8,…,1/8).
The B(ν,a) fibre therefore carries no label information mod 8, and it cannot produce zeros at 3 and 7.
The signed w-content (explore, R=200) is also near-uniform (0.119–0.129).

## Lemma PB2 (Category A)
The T-phase 140(Q(α)+B(α,w_c)) is one value per α, with β-independent fibre. So the 140-label pool is a fixed finite multiset: (16,11,0,9,19,6,0,9)/70.
It is non-zero on {3,7} and zero on {2,6}, so no label pool under the T-fibre can match MF2's support pattern unless some labels get weight 0.
Restricting to a subset of labels would be a selection made after looking, so it is not done.

## Observation (post hoc, not a claim)
PBR2 empties the even fibres {2,6}. Earlier maps emptied {1,5,6} (PQ1/PS1). MF2 empties {3,7}. No written reduction maps one zero pattern to another.

## Status of written Resonant fibre coordinates (all tested)
| Coordinate | Map | Result |
|---|---|---|
| unary n² | BATCH8 | FAIL |
| shifted u² | PF1 | FAIL |
| 140Q | PQ1, PS1 | FAIL |
| 10B(ν,a) | PB1 | uniform, FAIL |
| T-phase | PB2 | FAIL |

## Next pattern step
The remaining written structure is the **S-law** (l.274): the label mixing u_{α,β}(−1/w) = e(B(α,β))/√35 Σ_p u_{p−β,α}.
- A pattern-forced test is the Markov-type step on labels given by |S|² (the transition matrix from S, the way MF2 is a Markov law on the residual side), with its stationary law pushed to a written fibre coordinate (T-phase or 140Q). This makes the comparison object a Markov stationary law on both sides.
- Alternatively: Arvin's written Π / grading, if it is ever supplied.
