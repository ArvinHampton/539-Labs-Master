# order36 NOTES
- Two leakage definitions have now failed: by characteristic (order35) and by plain-Gauss span (order36). Both S and X sit outside the plain span by the same 37%.
- The natural reference space for C2b is the span of the Bernoulli-sum columns {C2b_l} themselves, together with the order20 RG7 joint-rank picture. That is where the fixed-M law lives.
- Grid dependence is now the most concrete pattern: the miss concentrates at small-denominator x and shrinks as the grid fills in (0.0585 → 0.019 → 0.003).
- Open next step (order37, not started): preregister RG34, a per-point law miss as a function of the denominator of x. Hypothesis to fix before testing: per-point r(x) for C2b decays like c·den(x)^{−p}, with p and c fixed by a stated rule (e.g. from L_B, where N′ = 2|num(x)| and the aliasing weights c′_k ∝ 1/k² suggest p = 2). Test on the full 216 grid using stored arrays only (cheap). Thresholds fixed in advance.
- Naming: RG* only, no labels L1–L7. Geometric only; MAPS_CANDIDATES untouched; no Resonant objects; no bridge claim; CORE_FREEZE. nice, OMP_NUM_THREADS=1, 3 GB, ~15 min; no push or sends; new files only.
