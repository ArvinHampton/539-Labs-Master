# FINDINGS — t2101u LOCAL WAVE5 APPROVE/PURSUE-ALL CONFIRM (2026-10-25, America/Chicago)
Auditor CONFIRM-only. Verdict: **MATCH-with-SF**

## Hashes (verified ~21:05 CDT)
- Rollup grok-batches/LOCAL-RESOLUTION-WAVE5-APPROVE-PURSUE-2026-10-25.md: 64e846b827e13e7df8ae54cd2cb07b67ca6c27209ad265b4887510351a57c732 — MATCH
- Write BRIDGE_C_35/AUTHOR_WRITE_WAVE5_POSTURE_GEO_ITEM4_DEFER_LOCAL_2026-10-25.md: d42f6c9682720368913036af6c6dca7ce24663276e7806973bfb1146d7779d40 — MATCH
- STREAM BRIDGE_C_35/STREAM_IDLE_LOCAL.md (re-hashed live): bad6b3f9634a7c92e8e7b0653c26278061d702c9b6a93e43c1fefac7dc1429b3 — MATCH; Wave5 entry cites prior STREAM 3fed906d… (= t1218u Local CONFIRM) — MATCH
- Live tip residual-c-field-WRITTEN_PREMISES_DRAFT.md: **23644d6a1baa568b81078cf91957ab0deb5e412035cbd52c8d81dc76f75e4bf8** (≠ 3d47ce49…); sidecar .sha256 = 23644d6a… — see SF-1
- Backup .pre-hygiene-fold-3d47ce49.md: 3d47ce497f812792a900cb103baff6ddfe838058d7883399239cd7763ba7bf79 — MATCH to pinned LOCK

## Checks
| Claim | Result |
|---|---|
| Rec1 exact-c P1 CLOSED Cat B (1f6e3d2e… / 554a79ea…); no tip work | MATCH |
| Rec2 Geo Moved NO; clear-path = Written μ₁₀ geometric premise w/ source cite; no residual_B1 invented | MATCH |
| Rec3 P1 ρ ACCEPT efd90f85… kept; W₇/Γ₀(49)/ρ(γᵢ)/d± matrices ABSENT | MATCH |
| Rec4 Item4 form-only e692fd91… kept; rates DEFER→Owner/PR2; W4.5 barred | MATCH |
| Rec5 L-1 OPEN 2807ddda… kept; δ≡0 NOT asserted | MATCH |
| Rec6 #7/#8 HOLD; G-A3 RETIRED, not reopened; no Empty-LOCK | MATCH |
| Rec7 no Bridge YES/READY/Cat A from exact-c | MATCH |
| Tip start=end 3d47ce49… (Local) | MATCH as of Local write (files mtime 21:02:10 CDT); tip changed later 21:02:53 CDT by non-Local MR2 hygiene fold — SF-1 |
| No invent; Write/Rollup/STREAM mutually consistent; Bridge PARTIAL / READY NO / NOT Cat A | MATCH |

## Soft SF
- SF-1: Tip moved 3d47ce49… → 23644d6a… at 21:02:53 CDT (43 s after Local files) by MR2 Soft-SF hygiene fold (backup .pre-hygiene-fold-3d47ce49.md). Diff = 2 status lines only (§1k l.161 header and l.168 Status: "pending/await re-CONFIRM" → cites Auditor 5a66d9a5… and fbfb7632…). No premise/physics content change. Not attributable to Local; Local "tip end 3d47ce49…" true at write time but stale vs live. MR2 fold stamp grok-batches/MR2-FOLD-STAMP-SOFT-SF-HYGIENE_2026-10-25.md sha256 f6d18dccbdb37b9fa55bf75d8ade5f1b74a419b0116a5bcbb27e46d6928df459 (mtime 21:03:33 CDT). MR2 lane, not a Local defect. Expected LOCK pin 3d47ce49… is stale vs live 23644d6a…; the next Local/STREAM should re-pin to 23644d6a….
- SF-2: Write/Rollup/STREAM stamped "~21:05 CDT" vs mtime 21:02:10 CDT (cosmetic).

No physics invented; tip not edited by Auditor; no outbound messages.
