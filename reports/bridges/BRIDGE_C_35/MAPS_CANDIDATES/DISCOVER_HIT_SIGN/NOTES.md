# NOTES: DISCOVER_HIT_SIGN
- Order: explore.py hashed and run (data/explore.sha256), then PREREG.md hashed (PREREG.sha256), then scripts/test.py run once (scripts/SHA256SUMS). All runs under 2 s; nice, OMP=1, ulimit 3 GB.
- Lemmas: DM3 (lag ≥ 2 independence: the hit-fibre process is exactly 1-step dependent and ρ-mixing after one hit); DM4 (β̂ ∈ {1,5} ⇔ u ≡ 6, 2 mod 8, s = χ₄(u/2)); DM5 (sign mean 0, autocorrelation 0, conditional ∓1/6). Identical at M = 72 and 288.
- Obstruction (sign): the only convention is χ₄ vs −χ₄. Any ±1 on {1,5} has zero self-correlation under the chain, because rows 1 and 5 of K₁ are equal. So no sign on {1,5} can be a dynamical grading, and no s ↔ g link is computable.
- Model caveat: equidistribution of lifts is assumed, and it is confirmed numerically only.
- Next step: the hit-fibre process is now fully characterised (ρ plus the lag-1 kernel; fibre-to-fibre dependence vanishes from lag 2). The residual-path side has no more exact content at this depth. Grading progress now needs Arvin's decision on g/P_res as the C11 grading and predicate, or a written Π. Optional check: the dependence of hit *gaps* (step counts between hits) on fibre, from the same chain.
- No L1–L7. order*/v12 paper untouched. CORE_FREEZE: this folder only. No push or send.
