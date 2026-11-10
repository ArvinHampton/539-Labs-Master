# PP CONFIRM — Local erratum 74ebd51f (applies PP discharge 001d3235). 2026-11-10 10:16 CST (America/Chicago)

- Target: ERRATUM_LOCAL_B2_B3_PP_TWIST_DISCHARGE_001d3235_2026-11-10_1015.md, sha256 74ebd51f387ca94f1257c7086bedec5ae6a5152afbf8e1c120847e4dedf7923f = sidecar. mtime 10:15:00 CST, matching the header. Tip 7cddb188 unchanged. Source discharge 001d3235 still matches its sidecar (not edited). No CERT, nothing adopted, O-b stays OPEN, junction UNSOLVED.

All three fixes are applied faithfully. Local correctly records this as PP's discharge, not a Local proof of TW(r).

- Fix 1: B2 is retagged from Shimura 1973 Lemma 3.6 to TW(r) and split. B2 (2 ≤ r ≤ 30) is PROVED, covering the Bridge C instance r = 5. B2-general is CONDITIONAL [T-twist-general]. B2′ stays PROVED and needs no modularity. The note that r = 2 has no primitive character and is a certificate check only is correct ( (Z/2Z)× is trivial).
- Fix 2: B3 is PROVED as a sufficient reduction only, citing TW(5). Existence of G and the converse are not claimed. O-b stays OPEN.
- Fix 3: the rollup is the split count 49 PROVED / 10 COND / 5 OPEN / 2 REF / 1 PENDING + V₈₄ (67 rows). The CONDITIONAL, OPEN, REFUTED and PENDING lists match PP 001d3235. The unsplit alternative is not used.

T-theta1 (fff902b4) is correctly left ungraded here, and the t4436 tally correctly stays 63/17/5/9/2 pending the separate audit.

No grade change and no fixes.
