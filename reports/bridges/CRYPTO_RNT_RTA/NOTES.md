# NOTES (proof and process problems found)

1. `h2.py` did not compute k = 17 although PREREG H2 listed it as descriptive. Not rerun after data were seen; no verdict depends on it.
2. H1's z-statistics treat per-seed shares as independent across seeds; seeds 10^12 + 7919j are deterministic and nearby trajectories can merge, so p-values are approximate. The verdict (1 of 4 pass) does not depend on this: three k fail on the excess threshold or sign, which is not a significance question.
3. CANDIDATE_MAPS M6 writes the third branch as (2n−1)/3; this equals 2k+1 for n = 3k+2. The RTA manuscript Def 2.1 writes (2n+1)/3 "by floor division"; floor((2n+1)/3) = 2k+1 for n = 3k+2, so the maps agree (ledger entry 43 records the non-integrality of the unfloored expression).
4. PREREG H2's sentence on the chance of both being extreme is a rough bound, not used for a decision.
5. INVENTORY's statement that no source explains m = 8 rests on rg searches of the local corpus only (R/crypto, SF/, MS/); Drive/Notion were not re-searched in this run (an earlier search found 0 Drive files, `RPP_spec_v1/RESIDUAL_T3_predicate_sources.md:24`).
6. Parity Dominance for odd k (A39 and ledger 91) is computer-assisted and only partly independently re-derived; nothing here re-audits it, and k = 67 is outside the proved range.
