# PREREG: DISCOVER_PI_RULE
Written 2026-10-24 ~9:05 PM CDT after exploration (scripts/explore.py, data/explore.json, hash data/explore.sha256), before tests. Owner: Arvin Hampton. New files only. CORE_FREEZE. Residual-vs-Resonant lock. No C11 re-run. Labels RP*/Π* only.

## Exploration facts used (Category A, proofs in NOTES.md)
- RP1 (word = seed mod 3^n): the T3 branch word of length n is a bijection of x mod 3^n onto {0,1,2}^n. Every word is realised; seeds form one residue class mod 3^539.
- RP2 (P_res is local): u ≡ 3 (9) ⇔ w_i = 0 and w_{i+1} = 1. P_res constrains words only through the 2-letter pattern "01".
- RP3 (carrier walk empty): T3(O_res) ∩ O_res = ∅, since T3(21+9j) = 7+3j ≡ 1 (3).
- RP4 (extremal word): over w_0..w_539 (hits at steps 0..538), the maximum hit count is 270, reached by exactly one word, (01)^270. Its 539-step word is Π*_max = (01)^269 0.
- C1 literal: σ(i) = sorted O_res[i] is forced and unique, but its branch word is Π*_C1 = 0^539. That is the trivial-seed word x = 3^539 z.

## Candidate rules (neither is in a written source)
- Π*_C1: forced by C1 alone. Not a T3 trajectory through O_res (RP3).
- Π*_max: forced only after choosing the objective "maximise P_res hits", plus the convention that w_539 counts. That is an extremal choice, so it is a free choice.

## Tests (deterministic, exact)
- T1 (Map-C10 on Π*_C1): the prediction is exactly 4 maximal constant-branch segments with lengths ordered like 1/34 < 5/2 < 35/4. Expected: FAIL (1 segment).
- T2 (Map-C10 on Π*_max): same prediction. Expected: FAIL (539 segments).
- T3c (robustness): count the words with the maximum hit count when hits are restricted to steps 0..537 (no w_539). Prediction: more than 1, i.e. the RP4 uniqueness depends on that convention.
- Map-C6: NOT RUN. "Word read mod 4 has M_S-order profile" has no operational definition in the source, and making one up would be an invention.
Verdict rule: a unique Π is "found" only if a rule needing no free choice yields a non-degenerate T3 word. Otherwise the verdict is OBSTRUCTION. Bridge: NO in all cases.
