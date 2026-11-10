# AGENT RULE-5 REVIEW — MR1 named gaps G1-mem + G-PATH-A + G-A2 STATUS (Soft SF) — 2026-10-27 11:26 CDT (America/Chicago)

Lane: Agent. Write-only Soft SF → Auditor. Tip LOCK 7cddb188… tip_touched NO. Kerr BLOCKED. Mesh CANCELLED. No RECS.

## Subject (live sha256 vs claimed)
| File | Claimed | Live | Result |
|---|---|---|---|
| FINDINGS_MR1_NAMED_GAPS_G1MEM_GPATHA_GA2_STATUS_2026-10-27.md | 6d9b08876178508c2608b92f58caedb032da457c0050c9692c97ece5a00746c4 | same | MATCH |
| SOFTSF_PRESS_MR1_NAMED_GAPS_G1MEM_GPATHA_GA2_STATUS_2026-10-27.md | 2278fef8e770b13faa8a7400a3de8c655084f35d2369e71b6d46609d4a3edee8 | same | MATCH |
| Auditor mirrors (bridges/AUDITOR/) | — | cmp both | OK (no restore needed) |

## Authority cites (live re-hash)
| Item | sha256 prefix | Result |
|---|---|---|
| Tip residual-c-field-WRITTEN_PREMISES_DRAFT.md | 7cddb188ca34… (full match) | MATCH |
| OW blanket | 9b993a72bcdf… | MATCH |
| G1-mem rebuild LIVE | 3f14f6d8d454… | MATCH |
| G1mem/GPATHA status | 27dd3cc38f9d… | MATCH |
| GBASIS89+GA2 | 243f9cc504e1… | MATCH |
| G-EXACT compute blocked | e9f257741bbd… | MATCH |
| Path (a) ABSENT | f0f61da0c5be… | MATCH |
| Card1F Step3 | cf59ba1395dc… | MATCH |
| POST rollup | da25ef01762b… | MATCH |
| Agent R5 lit deepen | f3dfb0bf7f49… | MATCH |
| Agent R5 POST rollup | c89de2084250… | MATCH |
| MR1 lit deepen | e5b4e69d055c… | MATCH |
| Eigen G1MEM card | d768dbd92671… | MATCH |
| solve42g PROGRESS ROOT30 | 77cf385b28f3… | MATCH |

## Spot-checks
- G1-mem: PID 2815455 (rebuild_e1_extra_then_crt.sh) and PID 2816202 (resume_solve42g_serial.sh) are both live. Each has about 4h41m elapsed. The watch log still says the rebuild is waiting on solve42g. No progress file past ROOT30 and no Kr/Q(ζ49) CRT or char-0 cert artifact turned up in the scan. GAP STANDS is consistent.
- G-PATH-A: no new path-(a)/Card-1A ID artifact beyond the cited lineage. OPEN STANDS is consistent.
- G-A2: the 243f9cc5… pack has 33 ≤ a₂ ≤ 112 and no newer pin was found. OPEN STANDS is consistent.
- Exact-ν stays Owner/Eigen Write-gated. The subject does not invent a close. Read-only only: no compute started, nothing killed, no CSV edits.

## Verdict: **ACCEPT**

## Board
- G1-mem: OPEN / GAP STANDS. The rebuild is LIVE but blocked on solve42g (30/42). Kr CRT and char-0 are ABSENT.
- G-PATH-A: OPEN STANDS.
- G-A2: OPEN STANDS (a₂ unpinned, 33–112).

## Explicit
- tip_pre = tip_end = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91; tip_touched NO. Kerr BLOCKED. Mesh CANCELLED. No RECS.
