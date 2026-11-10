# AUDITOR FINDINGS — CONFIRM t761u inventory #5 G-A3 reopen (AUTHOR-WRITTEN catalogue + menu)
Date: 2026-10-25 13:02 CDT (America/Chicago). Lock: Residual-vs-Resonant. Package: BRIDGE_C_35/deduce_t761u_ga3_reopen_written/ (not edited).

## Verdict: MATCH (CONFIRM). NOT Cat A. G-A3 NOT reopened — still PAUSED (t725u). Rec G-α KEEP PAUSED. Soft SF: NONE.

## Live shas (recomputed)
- DRAFT 395c625d2bf52843ee318012c10be0b732db97c4bc55913a9e612ac09898615d
- PREREG 090466595b1bebd2b7878bd1716847a7bc339ade37675da3b7db3a8c33bf8f7e
- RESULTS f258bca200ccbc6b6340e1c397098e9259a072a5f0e857b6b93ff0cf413203c1
- SUMS e3b7d0dff20589cdcebd628311b3d7e85be150177861cbfdeda9cba3488d97df
- MENU 07c8df15bd39183f47020cb502bb0a203d10b816229c1dc4904a1e445338f45b
All match claims.

## Checks
1. `sha256sum -c SHA256SUMS`: 6/6 OK (draft, PREREG, RESULTS, menu, logs/PREREG.sha256, logs/verify_basis.txt).
2. verify_basis.txt: 22/22 basis files re-verified live OK — AW-α aac04151…, O-α b467bb54…, PB-α c26b5f72…, E-α LOCK 82d6976d…/72b9cfb4…/106e11ec…, Written E c85448e8…, t713u 49bd0b24…/c4755206…/a520614b…, REJECTED 4da09dec…, t718u a05693fb…/2e1dec49…, t721u 9e0c3705…/7d324d73…/1749576a…, t722u 9aa52f19… / CONFIRM 4ad006b7…, X4 2bb870b4…, schema v2 8d247feb…, MASTER 544de792…, B3-α b96ff7bd…, T-α 5f5f2832…. AUDIT_STATUS live 93ce87c4… at build (append-only; this audit appends).
3. Ordering: PREREG mtime 13:00:21.759 < RESULTS 13:00:21.763 CDT. RESULTS cites PREREG via logs/PREREG.sha256 (full sha 09046659…bf8f7e, OK, in SUMS); full sha also in STREAM LOCK L49. Note (non-SF): RESULTS body does not inline the full PREREG sha.
4. Verbatim: no written_lines*.txt. Quoted AUDIT_STATUS L408 (REJECT t717u, 4da09dec soft-SF-if-accepted) and L422 (PAUSE G-A3 t725u) match live lines byte-for-byte. Note (non-SF): DRAFT cites AUDIT_STATUS "af26d751…" while verify_basis records 93ce87c4…; both are append-only snapshots, quoted lines verified live.
5. Soft SF scan: silent reopen NO (PREREG/RESULTS/menu/draft all state G-A3 PAUSED, reopen only via new PREREG after explicit Arvin ACCEPT); 4da09dec revived NO (cited only as REJECTED, all menu options ban reuse); R-PKG1 auto-run NO (G-δ menu-only, NOT recommended); numeric cells NO; Cat A claim NO (F-nothing-CatA YES). Rec = G-α KEEP PAUSED; nothing adopted.
6. STREAM LOCK: BRIDGE_C_35/STREAM_IDLE_LOCAL.md L49 — shas match all five live values.
7. Force criteria unaltered vs PREREG: F-nothing-CatA YES; F-G-A3-reopen NO; F-δ≡0 NO; F-Bridge-YES NO; F-4da09dec-revived NO; F-numeric-cells NO; F3 real-x not claimed. No PASS/FAIL changed.
8. E-α timing: RESULTS/draft say E-α Auditor CONFIRM pending/not landed. E-α MATCH 0aaec40d13228770a4647189566017f65ff6d4c7ff8ce95586f513c80ceef956 (file mtime 12:59:57 CDT, ~24 s before package SUMS 13:00:21) — race at build; verify_basis notes file present. Not a mismatch; E-α now CONFIRMed.

## Standing
AW-α aac04151… / O-α b467bb54… / PB-α c26b5f72… / E-α 0aaec40d… stand. Prior G-A3 CONFIRM 4ad006b7… diagnostics-only; G-A3 PAUSED. 4da09dec… stays REJECTED. Bridge PARTIAL; READY NO; residual-C OPEN; R-C1 stands; X4 ABSENT; no order78.
