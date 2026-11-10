# MAPS_LEDGER (C1–C15, E1–E3). Written 2026-10-24 22:20 CDT (America/Chicago). Read-only; no statuses were invented.
Prov = the source of the status. PAPER = hashed RESULTS/data. CHAT = acceptance or gate by message only.

| Map | Status | Cat | Source (Prov) | Notes |
|---|---|---|---|---|
| C1 | FAIL | B | MAPS RESULTS (PAPER) | ord = 294; the post-hoc observation is not upgraded |
| C2 | FAIL | B | MAPS RESULTS (PAPER) | residues {2,2,1} |
| C3 | OPEN | B | MAPS RESULTS (PAPER) | C3_RUN dir exists; not re-audited this pass |
| C4 | FAIL | B | MAPS RESULTS (PAPER) | |
| C5 | FAIL | B | MAPS RESULTS (PAPER) | |
| C6 | OPEN | — | PI_MAX_PURSUE RESULTS (PAPER) | no written letter→M_S map; order59 RG49 confirms that M_S is ABSENT |
| C7 | FAIL | B | BATCH2 (PAPER) | ord(M_T) = 140 |
| C8 | FAIL | B | BATCH2 (PAPER) | depth 29 |
| C9 | FAIL | B | BATCH2 (PAPER) | 434 ≠ 521 |
| C10 | FAIL* | A (computation) | DISCOVER_PI_RULE T2 (PAPER); Π accepted (CHAT) | *Older OPEN rows (BATCH2–7, C11 NOTES) are stale. The FAIL is conditional on Π*_max, a free extremal choice. |
| C11 | FAIL | A | C11_GRADING_ACCEPT (PAPER); g accepted (CHAT) | S verified against test.json; not blind (disclosed) |
| C12 | FAIL | B | BATCH3 (PAPER) | S = ∅ |
| C13 | VOID | B | BATCH3 (PAPER) | gate 297 ≠ 353 |
| C14 | FAIL | B | BATCH3 (PAPER) | |
| C15 | FAIL | B | BATCH4 closeout (PAPER) | k = 105 |
| E1–E3 | OPEN | — | BATCH3–7 rows, order50 (PAPER) | no definition in the MAPS corpus; traced to v12 Open problem 1 |

Objects: Π*_max = (01)^269 0, sha256 c2c26fda…8d87 (recomputed OK). g = (−1)^τ: 268 values of +1, 271 of −1. P_res: u ≡ 3 mod 9 (PI_MAX_PURSUE PREREG:2). All three are agent-discovered; acceptance is CHAT only.

## Erratum 2026-10-24 ~22:19 CDT (Auditor)
- C3 row above is stale. On-disk verdict: **FAIL (Cat B)**, C3_RUN/RESULTS.md (scripts hash OK; ../PREREG.md fdd4c2be… OK). MAPS RESULTS.md:8 OPEN row predates the run. Not a new verdict.
- C10 recommended wording: see FINDINGS_2026-10-24_continue.md §2 (W-C10 still OPEN).
