# FINDINGS — MR1 Soft SF hygiene fold §1l re-CONFIRM (t2101u)
Date: 2026-10-25 ~21:12 CDT (America/Chicago) · Auditor · CONFIRM-only · no tip edits · no messages

## Verdict: **MATCH**

## 1. Shas
| Artifact | Expected | Actual | |
|---|---|---|---|
| Stamp OWNER_WRITE_MR1_EXACT_C_HYGIENE_FOLD_t2101u_2026-10-25.md | ed5f57b8…39a2 | ed5f57b8dc916bcdcf065647ed720c8e374cb107de328523c19bbf413d4d39a2 | MATCH |
| Backup .pre-mr1-hygiene-fold-23644d6a.md | 23644d6a…4bf8 | 23644d6a1baa568b81078cf91957ab0deb5e412035cbd52c8d81dc76f75e4bf8 | MATCH |
| Live tip AFTER | e7b9a633…6ce6 | e7b9a6338cbeff33f5d018771eeb6cecc53258dfe6eec34332db1180fb656ce6 | MATCH |
| Sidecar .md.sha256 content | e7b9a633… | e7b9a6338cbeff33f5d018771eeb6cecc53258dfe6eec34332db1180fb656ce6 | MATCH |

## 2. Diff tip vs backup
Exactly 2 changed lines (170, 177) — both in §1l:
- l.170 heading: "pending Auditor re-CONFIRM of this fold" → "Auditor MATCH-with-SF FINDINGS_2026-10-25_t1218u_MR1_EXACT_C_FOLD_RECONFIRM.md 9667f44e…".
- l.177 Status: "await Auditor re-CONFIRM" → "re-CONFIRM landed (9667f44e…); CLOSED c21eb995…; pre-hygiene tip 23644d6a…; READY NO; Bridge PARTIAL; NOT Cat A".
With lines 170/177 removed, tip and backup are byte-identical (cmp) → no reopen of W₇, Γ₀(49), gens, k, ρ, exact-c μ₁₀, V₄₂, N₂, §1k. MATCH (hygiene only).

## 3. Cited artifacts
- FINDINGS_2026-10-25_t1218u_MR1_EXACT_C_FOLD_RECONFIRM.md sha256 = 9667f44eaeebc69fdb680720bbbe42d7af51764ccd0174d9587b0ffb34e51399 — MATCH (full sha in tip).
- reports/MR1_EXACT_C_FOLD_CLOSED_t1218u_2026-10-25.md sha256 = c21eb9950e3007540e7447cc48c7558d7bfd7e8ad48f8c5a2a0fe96e73fd1c69 — MATCH.

## 4. Gates
Bridge PARTIAL · READY NO · NOT Cat A — stated in §1l Status, unchanged elsewhere. MATCH.

## 5. Soft SF
- None new. Closes MR2 hygiene re-CONFIRM (f93f0744…) SF-1 (stale §1l await).

Sources: tip e7b9a633…; backup 23644d6a…; stamp ed5f57b8….
