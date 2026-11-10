# FINDINGS: PP Soft SF audit of the DF VIRGO bin-wording erratum (2026-11-05, ~13:39 CST)
REPORTS ONLY. No CERT. tip untouched. invent HOLD STANDS.
Input: e1ea66ebf7b28acd… MATCH. Original 6f9efa4b… unchanged; PP audit 69eda955….
Verdict: CONFIRM, no notes.
- N1 is fixed. PP recomputed the bins: Δf = 1/(16384·60 s) = 1.01725 µHz. Bin k=1821 is 539.84 s and k=1820 is 540.13 s, so the nearest bins are distinct. The windows overlap and their maxima picked the same bin, and that is correctly stated not to be independent evidence.
- N2 is recorded: the analysis choices were post-hoc and not preregistered, and null-consistent does not mean absence.
Positive empirical associations remain zero. Tier E only. Soft SF → Keeper together with 6f9efa4b… and 69eda955….
