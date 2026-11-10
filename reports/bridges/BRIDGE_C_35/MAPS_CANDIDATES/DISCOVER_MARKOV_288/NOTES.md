# NOTES: DISCOVER_MARKOV_288
- Order: explore.py and explore2.py hashed, then run (data/explore.sha256), then PREREG hashed, then test.py run once. Runtime < 1 s each; nice, OMP=1, ulimit 3 GB.
- Disclosure: MF2 already had ρ at M=216. DM1 re-derives it, and the new content is DM0 (modulus sufficiency) and DM2 (the kernel).
- Caveat: the lifted-chain assumption (3-adic digit equidistribution) is the model. It is not proved for SHA3 seeds; it is confirmed numerically only.
- Next grading step: DM2 gives a 2-state automaton {A,B} on hits. Note that P(next ∈ {1,5}) = 1/2 in both rows, so the indicator [β̂∈{1,5}] is uncorrelated at lag 1. The structure is in the 1-vs-5 split: after a {1,5} hit, fibre 1 is favoured (7/24) over 5 (5/24); otherwise it is the reverse. Next: a prereg of the exact lag-k joint law (k ≥ 2) and of the signed statistic (−1)^[β̂=5] restricted to {1,5} hits, from the same 288 chain. Any use as a C11 grading still needs Arvin to accept g/P_res first.
- No L1–L7 names. order*/geometric packages and v12 paper not touched. No push, no sends.
