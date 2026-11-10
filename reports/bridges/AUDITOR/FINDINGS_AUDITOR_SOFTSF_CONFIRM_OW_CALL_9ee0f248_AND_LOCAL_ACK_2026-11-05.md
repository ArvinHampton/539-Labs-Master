# FINDINGS: Auditor hash-only confirm — OW call-9ee0f248 + Local ACK pair

- Date/time: 2026-11-05 ~11:46 CST (America/Chicago)
- Reports only. No RECS. No CERT. Tip untouched. Content not evaluated.

| Path | Computed sha256 | Sidecar | Result |
|---|---|---|---|
| /workspace/quantum-comp/reports/OWNER_WRITE_CALL_9ee0f248_LOCAL_FILTER_AND_PRIMARIES_PULL_2026-11-05.md | bf49d032168fce29cce5e3dbca423cd8ff3a70b49f871dbf19377618576d1f3e | present, first token equal | MATCH |
| /workspace/quantum-comp/bridges/AUDITOR/OWNER_WRITE_CALL_9ee0f248_LOCAL_FILTER_AND_PRIMARIES_PULL_2026-11-05.md | bf49d032168fce29cce5e3dbca423cd8ff3a70b49f871dbf19377618576d1f3e | present (points to reports copy), bytes equal reports copy | MATCH (mirror) |
| /workspace/quantum-comp/reports/FINDINGS_LOCAL_SOFTSF_ACK_OW_CALL_9ee0f248_FILTER_RECLAIM_CLOSED_FULL_STOP_IDLE_2026-11-05.md | 01a913679d8a7ed9401646915541b3bf3b87689ed8ca5435183750113fd545b1 | present, first token equal | MATCH |
| /workspace/quantum-comp/reports/PRESS_LOCAL_SOFTSF_ACK_OW_CALL_9ee0f248_PP_AUDITOR_2026-11-05.md | 71fed011ead0266c7ac55977fb5e7bc8c61ccfcedf4d2ea6e2be9bf9416d1206 | present, first token equal | MATCH |

Counts: MATCH 4 / NO-SIDECAR 0 / MISMATCH 0.

Footnotes, recorded only (not evaluated): Local Path routed Soft SF→PP→Keeper Write-only; content of filter/reclaim/full-stop claims not evaluated. Auditor grants no CERT, release, route, or halt lift.

Tip: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, tip_touched = NO.
Kerr UNLOCKED (fa7c879c); Layer2 ABSENT; No CERT; REPORTS ONLY, no RECS. Gemini unsent.
