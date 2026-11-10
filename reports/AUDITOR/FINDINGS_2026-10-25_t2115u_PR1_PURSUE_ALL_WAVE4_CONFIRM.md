# AUDITOR FINDINGS — PR1 PURSUE-ALL wave-4 (catalog rev.20) CONFIRM
2026-10-25 ~21:22 CDT (America/Chicago). CONFIRM-only. No tip/catalog edits. No messages.

**Verdict: MATCH-with-SF**

## Hash checks
| Item | Expected | Live | Result |
|---|---|---|---|
| Lane FINDINGS PR1_PURSUE_ALL_WAVE4 | 8d1076d6… | 8d1076d653256d98b423847c684380f9244e413f5e52889a97aacd18b39a6a6d | MATCH |
| Catalog obs-data-PR1-HEPP-QM-GR.md (rev.20) | e630415a… | e630415ae12e3efd53755e628a1c115ee246f6cbc417162dee2841997ab0f6d7 (mtime 21:17:48 CDT) | MATCH |
| Backup .pre-rev20-f38f394a.bak | f38f394a… | f38f394a97d854565d09c6f34fad7bcbfaf390c11e3aecfb463bef859496da46 | MATCH |
| ABSENT A | f91cf8e8… | f91cf8e8ff69…a16a8b3 | MATCH |
| ABSENT B | e14c7647… | e14c7647d7e0…c6600a2 | MATCH |
| ABSENT C | 6cff39fe… | 6cff39fea72b…db06229b | MATCH |
| Live tip residual-c-field-WRITTEN_PREMISES_DRAFT.md | a6bc20f8… | **90bbf5089eddea8b0a52370cbb69b78d714b9bad9230dffe80ca19a8c5ef4882** (mtime 21:18:50 CDT) | DRIFT (SF-1) |

## Claims
- Lane: intermediate fa6dfe35… → final e630415a… (Soft-SF fix) — consistent with live. OK.
- tip_touched by PR1 = **NO**: lane reports NO; tip mtime 21:18:50 postdates catalog write 21:17:48; drift chain e7b9a633→d29007f1→a6bc20f8→90bbf508 all external (MR2/MR1), not PR1.
- A/B/C ABSENT-hold, wave-4 note in all three writes: CONFIRMED.
- LVK OPEN; GP-A [V5-held]; Bridge PARTIAL / READY NO; not Cat A: CONFIRMED in lane text.
- Catalog live-tip cites rebound to d29007f1… (lines 16, 206, 283, 311, 314); 3d47ce49… retained as historical §2F fold cite.

## Soft SFs (non-blocking)
- SF-1: Catalog/lane cite d29007f1… as live tip; live is now 90bbf508… (prior brief bind a6bc20f8… also superseded, ~21:18:50 CDT, out-of-lane writer). Rebind on next PR1 catalog touch.
- SF-2: Lane line 4 lists rebind target e7b9a633… then later d29007f1… — superseded within the same FINDINGS; final text consistent.

Prior rev.19 CONFIRM: MATCH-with-SF e42a6bc8….
