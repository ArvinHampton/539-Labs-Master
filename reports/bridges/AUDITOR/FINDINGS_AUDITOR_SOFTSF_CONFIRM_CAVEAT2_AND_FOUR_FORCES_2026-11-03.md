# FINDINGS: Auditor hash-only confirm — caveat-2 Owner Write/LOCK + four-forces Soft SF REFUSE

- Date/time: 2026-11-03 ~12:52 CST (America/Chicago)
- Reports only. No RECS. No CERT. Tip untouched. Content not evaluated.

## Packet 1 — OWNER_WRITE caveat 2
| Path | Computed sha256 | Sidecar | Result |
|---|---|---|---|
| /workspace/quantum-comp/reports/OWNER_WRITE_CAVEAT2_NARROW_ALL_FOUR_CLPLUS_V35_2026-11-03.md | e4ef0a810d1be98f9995c3120cc60954b6120632419a6f443cf451cef2c09f3e | present, first token equal | MATCH |

## Packet 2 — OW caveat 2 Owner LOCK
| Path | Computed sha256 | Sidecar | Result |
|---|---|---|---|
| /workspace/reports/539labs/ow/OW_caveat2_narrow_all_four_Owner_LOCK_2026-11-03.md | 625b65290f45d17d78795a9255808e277a622408e861f157a6a999002f58413e | present, first token equal | MATCH |

## Packet 3a — systemic Soft SF REFUSE (prior)
Already Soft SF NO-SIDECAR: a1bb2988… + ATTACH 6b5359ed… — FINDINGS f9b615d1…. Not re-hashed here.

## Packet 3b — four-forces Soft SF REFUSE
| Path | Computed sha256 | Sidecar | Result |
|---|---|---|---|
| /workspace/reports/539labs/ow/OW_four_forces_structural_SoftSF_REFUSE_2026-11-03.md | 58885bf3d06609603ec34acd3ab81f0958788eaf5ae3166e0de3817d047254ab | absent | NO-SIDECAR (bytes=claim) |
| /workspace/reports/539labs/ow/ATTACH_four_forces_t3459u_bcb7cf05.txt | bcb7cf05f1592085f49609c1f9fcf6e529e66d7693d6dcccd67049eaac07457f | absent | NO-SIDECAR (bytes=claim) |

Counts this report (packets 1, 2, 3b): MATCH 2 / NO-SIDECAR 2 / MISMATCH 0.

Tip: residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, tip_touched = NO.
Kerr UNLOCKED (fa7c879c); Layer2 ABSENT; No CERT; REPORTS ONLY, no RECS.
