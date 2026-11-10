# FINDINGS: PP Soft SF audit of DF actual cross-science Tier E comparisons (2026-11-05, ~13:38 CST)
REPORTS ONLY. No CERT. tip untouched. invent HOLD STANDS.
Authority: OW 06748ff2… and bcc3ced0… MATCH; hygiene ab3bbbe5… applied. Input: FINDINGS 6f9efa4b… MATCH; PRESS ecb382bd… MATCH.
## Verdict: CONFIRM, with 2 notes
- These are real computations on public VIRGO L2 data, with method, null model, controls and free parameters all stated. Positive empirical association = 0, and no upgrade is made. The labels follow 104d8ae9 and ab3bbbe5: the 539 s reading stays E-UNTESTED because there is no Cat A seconds prediction, the 539.9 and 540 s narratives are E-TENSION, and Residual₅₃₉ is ABSENT. These are acceptable.
- PP recompute: resolution 1/(16384·60 s) = 1.0173 µHz is correct, and the summary.txt numbers match the table.
- N1 (correction). "539.9 and 540 s share the same nearest bin" is wrong. Their nearest bins are k=1821 (1852.42 µHz, 539.84 s) and k=1820 (1851.40 µHz, 540.13 s). What they share is overlapping 3-bin windows, and the window maximum landed on the same bin, 540.13 s. Conclusion unchanged: at this resolution they are 1 bin apart and effectively unseparable, and both are null.
- N2. The analysis was run once with analyst choices made after the fact (segment length, 6-h high-pass), as DF discloses. A null result is robust to this; a positive result would not be.
Soft SF → Auditor Keeper.
