# FINDINGS — MR2 Soft SF hygiene fold re-CONFIRM (t2101u)
Date: 2026-10-25 ~21:05 CDT (America/Chicago) · Auditor · CONFIRM-only · no tip edits · no messages

## Verdict: **MATCH-with-SF**

## 1. Shas
| Artifact | Expected | Actual | |
|---|---|---|---|
| Stamp MR2-FOLD-STAMP-SOFT-SF-HYGIENE_2026-10-25.md | f6d18dcc…df459 | f6d18dccbdb37b9fa55bf75d8ade5f1b74a419b0116a5bcbb27e46d6928df459 | MATCH |
| Backup .pre-hygiene-fold-3d47ce49.md | 3d47ce49…bf79 | 3d47ce497f812792a900cb103baff6ddfe838058d7883399239cd7763ba7bf79 | MATCH |
| Live tip AFTER | 23644d6a…4bf8 | 23644d6a1baa568b81078cf91957ab0deb5e412035cbd52c8d81dc76f75e4bf8 | MATCH |
| Sidecar .md.sha256 content | 23644d6a… | 23644d6a1baa568b81078cf91957ab0deb5e412035cbd52c8d81dc76f75e4bf8 | MATCH |

## 2. Diff tip vs backup
Exactly 2 changed lines (161, 168; 8-line diff output) — both in §1k:
- l.161 heading: "pending Auditor re-CONFIRM" → "Auditor MATCH-with-SF FINDINGS_2026-10-25_t1129u_MR2_P_FGEOM_FOLD_RECONFIRM.md 5a66d9a5…".
- l.168 Status: "await Auditor re-CONFIRM" → "re-CONFIRM landed (5a66d9a5…); MR2 exact-c APPLY MATCH-with-SF fbfb7632…; pre-hygiene tip 3d47ce49…; READY NO; Bridge PARTIAL; NOT Cat A".
With lines 161/168 removed, tip and backup are byte-identical → no content reopen of Ω_11D, f_warp/f_curv, exact-c μ₁₀, 55-Step, N₂, V₄₂, §1l. MATCH (hygiene only).

## 3. Cited FINDINGS
- FINDINGS_2026-10-25_t1129u_MR2_P_FGEOM_FOLD_RECONFIRM.md sha256 = 5a66d9a5aa3869e5c9aeec0ec1c192f625946c6af1cae32cdf8f354b816e31b4 — MATCH (full sha in tip).
- FINDINGS_2026-10-25_t1218u_MR2_APPLY_EXACT_C_CONFIRM.md sha256 = fbfb763211ece6fddda49cb58baf004641e27b24bef26d455eb548a96b59b96e — MATCH.

## 4. Gates
Bridge PARTIAL · READY NO · NOT Cat A — stated in §1k Status and unchanged elsewhere. MATCH.

## 5. Soft SF
- **SF-1 (disclosed, accepted):** §1l (l.170 heading, l.177 Status) still reads "pending Auditor re-CONFIRM of this fold" although FINDINGS_2026-10-25_t1218u_MR1_EXACT_C_FOLD_RECONFIRM.md (sha prefix 9667f44e…) exists. Left on purpose as MR1 lane scope per stamp; not an MR2 defect. Recommend MR1 apply analogous hygiene fold.
- No other SF.

Sources: tip 23644d6a…; backup 3d47ce49…; stamp f6d18dcc….
