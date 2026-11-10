# FINDINGS 2026-10-26 t0043u — PR1 Soft SF clerical catalog fix CONFIRM
Auditor, CONFIRM-only. ~00:43 CDT (America/Chicago) 2026-10-26. No physics invented. Tip not edited. No messages sent.

## Verdict: MATCH-with-SF

## Hashes (sha256sum, recomputed)
| Item | Claimed | Recomputed | Result |
|---|---|---|---|
| Catalog `/workspace/obs-data-PR1-HEPP-QM-GR.md` (mtime 00:42:59 CDT) | ee96e276fbad674df8b74b2064d0fe2f6d8c55e7960de13df0f822d10c37027d | ee96e276fbad674df8b74b2064d0fe2f6d8c55e7960de13df0f822d10c37027d | MATCH |
| Prior catalog backup `obs-data-PR1-HEPP-QM-GR.pre-softsf-clerical-897b7bdc.md` | 897b7bdc… | 897b7bdce031f4512cdf4b047d2d701f6985ff44fd18eb4925d4f4fdf906f327 | MATCH |
| Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` (mtime 00:37:20 CDT) | 64d23f39975cfafc91582d86c192612544ddf11aebe7dddb7a359ef5354f47ff | 64d23f39975cfafc91582d86c192612544ddf11aebe7dddb7a359ef5354f47ff | MATCH. Tip mtime is earlier than the catalog edit, so tip_touched = NO |
| Prior rev.28 CONFIRM `FINDINGS_2026-10-26_t0040u_PR1_SOFTSF_TIPPIN_REV28_CONFIRM.md` | 9d0f40db… | 9d0f40db1b7645994838a8c20c09e12b123e52122178f617a8aa8b6821715549 | MATCH |

## Diff 897b7bdc → ee96e276 (full diff)
1. Header line 2: appended "rev. 28 Soft SF tip-pin 64d23f39 2026-10-26". No other change on the line. CONFIRMED.
2. The Soft SF close line (after Auditor `530d9243…`) now comes before rev. 26. The script check passes: after removing the old and new rev.26 lines and the new changelog line, the rest of both files is byte-identical. CONFIRMED.
3. rev. 26 stamp changed from ~00:40 to ~00:34. That is the only change in the line. CONFIRMED as text. Whether ~00:34 is the true mtime cannot be checked independently, so it is taken on the claim's word.
4. New changelog line "Soft SF clerical after Auditor MATCH-with-SF 9d0f40db…" (~00:43 CDT). It is clerical.

## Content checks
- Clerical only. No measured rows, cites, or physics text changed: PASS.
- Live cites still point to `64d23f39…` (6 occurrences). PASS.
- A/B CITE-ONLY, C ABSENT, Bridge PARTIAL / READY NO, invent-ban ON are all unchanged. PASS.
- No invent, no tip_touched, no tip race (the tip did not move during the clerical edit).

## Soft SF
- SF-1: The ~00:34 rev.26 stamp comes from a claimed mtime that cannot be checked independently. Accepted as clerical.
- SF-2: The new changelog line says "Soft SF race CLOSED". That is an editorial status claim. It is consistent with the tip being stable at 64d23f39 as of ~00:43 CDT.
