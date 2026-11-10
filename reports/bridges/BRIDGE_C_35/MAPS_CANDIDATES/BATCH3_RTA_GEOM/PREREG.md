# PREREG: BATCH3_RTA_GEOM (Map-C12 to Map-C15; status of C6/C10/C11/E1–E3)
Written 2026-10-24 at about 7:05 PM CDT, before any BATCH3 test. Owner: Arvin Hampton. New files only. CORE_FREEZE. All maps are **Category B**; a pass is a survived prediction, not a bridge. No Π, grading or T3 q-series is invented. 67/68 are not targets. Runs: nice, OMP_NUM_THREADS=1, ulimit -v 3000000. Order19 (affine A2c) is not touched.

## Written residual objects used (sources quoted in reports/crypto/RPP_spec_v1/RESIDUAL_T3_predicate_sources.md §2)
- O_res = the 539 least labels of the charge class C_{q⋆} in Ω′ after clearing f_max = 21 (Object539_NonCircular_Construction §3.5). Canonical core: x_j = 21 + 9j, j = 0..538 (as reproduced there: x = 21+9j).
- Fibres: β♯(x_j) = j mod 8 on the sorted index (Discrete_Patterns_Residual_Carrier §0).
- Towers: Ω = {0..4879} cut into 243 consecutive blocks, the first 20 of size 21 and the rest of size 20; τ(x) = block index. The written count is 353 same-tower adjacent pairs.
- **Search result (task 1):** no written 539-step Π, no ±1 grading on O_res and no path predicate exist (see NOTES for the paths searched). C6, C10, C11 and E1–E3 stay OPEN and are not re-hashed.

## Map-C12: orthant-angle norm form → equidistribution over the fibres
Source: ε = 6+√35 (orthant angle ½ log ε), with norm form N(a,b) = a² − 35b². Target: O_res with β♯.
Prediction (NEW): let S = {x ∈ O_res : x = |a² − 35b²| for some integers a, b}. The counts of S in the 8 β♯-fibres differ by at most 1 (max − min ≤ 1), and S ≠ ∅.
PASS iff both. (Search bound |b| ≤ 200, which exceeds the reduction bound √(x·ε/35) ≈ 41.)

## Map-C13: RG1′ reflection → carrier reversal
Source: RG1′ (zeros iff ρ_m or ρ_u preserves the companion; an endpoint reflection). Target: sorted core with towers τ.
Prediction (NEW): the reversal σ(j) = 538 − j maps the set of same-tower adjacent pairs {(j, j+1) : τ(x_j) = τ(x_{j+1})} onto itself.
PASS iff σ preserves the set exactly. Also required: the reproduced pair count equals the written 353 (a gate; if the gate fails, the result is VOID, not FAIL).

## Map-C14: law-vector form vs norm form (two classes of disc 140) → O_res
Source: 2Q(n) = 2n₁² + 14n₁n₂ + 7n₂² (discriminant 140, the 35-component law vector form) vs a² − 35b² (disc 140). Target: O_res.
Prediction (NEW): S_Q = {x ∈ O_res : x = |2a²+14ab+7b²|} and S (from C12) are disjoint, and S_Q is non-empty.
PASS iff both. (Search |a|, |b| ≤ 300.)

## Map-C15: order19 A2c corner → fibre count (feeds from order19). OPEN
Prediction: let k = the number of the 105 companions with P-even corner A2c ≠ 0 (order19 exact output). Then k ≡ 0 (mod 8), i.e. it is compatible with an equivariant spread over the 8 β♯-fibres.
PASS iff 8 | k. Next measurement: read k from order19's final data once it is complete. Do not compute it here.
