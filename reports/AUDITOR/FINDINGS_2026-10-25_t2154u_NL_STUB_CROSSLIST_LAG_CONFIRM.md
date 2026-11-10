# FINDINGS t2154u — NL stub cross-list lag cleanup (t2153u) CONFIRM
Date: 2026-10-25 ~21:54 CDT (America/Chicago). Auditor, CONFIRM-only. No physics invented; tip not edited; no messages sent.

## Verdict: MATCH-with-SF

## Hashes (sha256sum recomputed)
| File | Claimed | Live | Result |
|---|---|---|---|
| obs-bridge-NL-61Omega-photon-brane.md | 6f0f9a7a… | 6f0f9a7acb44a6ac7d0ff74241ecda2c7e9fe01e2c8aa7b464c45901208193db | MATCH |
| …pre-crosslist-lag-fc14a0a3.md | fc14a0a3… | fc14a0a3a26668df19888de68933fb41c55aa67d7523be7538c5def9ea6873b0 | MATCH |
| ACK_STUB_CROSSLIST_LAG_t2153u_2026-10-25.md | 515496c5… | 515496c5f810bdf6d0e7b148457cc206f9495285d0f315eeb1d1be911f7437cb | MATCH |
| residual-c-field-WRITTEN_PREMISES_DRAFT.md (tip) | d0b1e301… | d0b1e3016182eab1522c5fa6b2743e7c8c48d5446d8b0e59b3acfdd61bb09851 | MATCH (LOCK) |

## Content
- Diff pre→live: only cross-list/lag rows (lines 22, 28, 36, 47, 50, 53, 62-63, 65-67, 70) plus appended t2153u log line. Rows retired ABSENT→AUTHOR-WRITTEN with W-NL-* cites only. No new physics/numbers ("no numeric DE value written").
- Cites present: Q4 Write f7a862b0… / MATCH fcf1a1e4…; pursue Write d2a28943… / MATCH 77c6f643… (21 hits in stub, present in ACK).
- Q7 KEEP; Bridge PARTIAL / READY NO; Soft SF packaging (f_*/Ω/ω) Owner-hold — stated in stub and ACK.
- tip_touched (NL): NO. Tip drift d5f8b9d3…→d0b1e301… is external (MR1 R18 fold), not NL.

## Soft SF
1. Tip Soft SF rebind: stub log line and ACK cite tip d5f8b9d3…; live LOCK tip is d0b1e301…. Rebind NL tip-pin to d0b1e301… at next packaging pass.
2. Stub row 36 still reads "Auditor CONFIRM pending" though pursue Write has Auditor MATCH 77c6f643… (stale label, cite-only fix).
3. Soft SF packaging hold (f_*/Ω/ω) remains Owner-hold.
