# PI_MAX_PURSUE — PREREG (written before tests)
Rule accepted (Arvin, 2026-10-24, "Max... Pursue"): Π := Π*_max = (01)^269 0 (DISCOVER_PI_RULE RP4), plus g=(−1)^τ, P_res (u≡3 mod 9). CORE_FREEZE. C10 FAIL (closed), C11 FAIL (closed); not re-run.

## Tests (predefined, Category A, exact)
- PM1 (identity): sha256(bytes(Π)) built as [0,1]*269+[0] equals c2c26fdae7b1e1f677799f9a6a210c429ea9c1f4b23f48ae1bbc66aab54f8d87 (DISCOVER_PI_RULE/data/tests.json). PASS iff equal.
- PM2 (word facts): len=539, #1s (hits)=269, #0s=270, minimal period 2, digram counts 01=269, 10=269, 00=11=0. Recorded as data, not as a bridge.
- C6 gate (decision rule): C6 runs only if the written sources (MAPS_CANDIDATES/PREREG Map-C6; A35 REPORT; BRIDGE_C_35 REPORT entry 94; PATTERN_S_MARKOV) give a map letter∈{0,1} → power of M_S. If no such clause is written, C6 = OPEN. Note: "539 mod 4 = 3" alone is word-independent, so it cannot test Π (vacuous) and does not count.
- RP-PI1 gate (new map): a Residual↔Resonant prediction counts as forced only if a written identity ties 269, 270, period 2, or digram mass "01" to a written modular object with no free assignment. Candidates checked: (a) period 2 ↔ ord(M_S²)=2 (S²=P); (b) period 2 ↔ the period-2 closed class (0,1)↔(1,0) of the |S|² chain (PATTERN_S_MARKOV); (c) 269/270 ↔ written integers 539=18+521, 105, 35, 7²·11, 140, 72; (d) "01" mass 269/538 ↔ shadow/theta statistic. Any candidate needing a letter→state assignment or an unwritten identity is dropped (OPEN), not tested.
Bridge claim: only on a non-vacuous PASS of a forced map.
