# AUDITOR FINDINGS — CONFIRM deduce_t736u_gr2 (t736u G-R2 F≠0 on x>0) — 2026-10-25 America/Chicago
Lock: Residual-vs-Resonant. Auditor did not invent physics or alter PASS/FAIL.
## Hash recompute — ALL MATCH
PREREG bc2edb71…7997 MATCH; RESULTS 825489d5…9caa MATCH; SUMS 7a5f092e…d1e2 MATCH; AUTHOR-CANDIDATE e9f4a477…fd96 MATCH; FINDINGS draft ea4a6afe…3b25 MATCH (non-authoritative); INVENTORY e5a03999…274f MATCH; logs/exact_root_check 184ea131…935e MATCH.
sha256sum -c package SHA256SUMS: 9/9 OK. logs/PREREG.sha256 OK (bc2edb71…). INVENTORY lists all 9 files + SUMS: complete.
Baselines live-recomputed: 437d4571… = AUDITOR/FINDINGS_t695u_local_accept MATCH; b34aebe6… = AUDITOR/FINDINGS_t704u_accept_confirm MATCH; R-UQ0 RESULTS 3181e59e… = deduce_t734u_accept/RESULTS.md MATCH (unchanged; Auditor CONFIRM 7e20e84c… stands).
## Checks
1. Hashes/SUMS/inventory: PASS.
2. PREREG before RESULTS: PASS (mtime 11:46:43 < 11:47:01 CDT; RESULTS line 2 cites PREREG hash; Expected F-R2a–d pre-stated, force criteria pre-stated).
3. No Cat A without Arvin ACCEPT: PASS. t736u = PURSUE; RESULTS F-R2c NO; G-R2 = OPEN CHECK (DEDUCED-passing), pending ACCEPT. R-UQ0 / G-A1c CLOSED not treated as changed.
4. Claims: F-R2a Written proof ABSENT — PASS (search_hits only open-check statements). F-R2b DEDUCED — PASS; Auditor independently re-ran sympy exact real_roots(P) = [], P(−3)=874171907/2560000>0; label DEDUCED-on-fit, NOT Cat A. Grid min 3.1599 marked informational, not promoted. F-R2c NO — PASS. F-R2d menu R-NV0/1/2 labelled AUTHOR-CANDIDATE, "nothing adopted" — PASS. No new selector/law invented — PASS.
5. Baselines 437d4571… + b34aebe6… + 3181e59e… cited and stand: PASS.
6. Posture: Bridge PARTIAL; READY NO; residual-C OPEN; R-C1 STANDS; G-A3 PAUSED; X4 ABSENT 2bb870b4…; CORE_FREEZE + SF-W7-3 (PREREG); no order78; Bridge YES/δ≡0/residual-C newly forced NO/NO/NO: PASS.
7. G-R2 closure not invented: PASS (OPEN until Arvin ACCEPT on menu).
## Soft SF
NONE. Informational (not SF): logs/baseline_sha_verify.txt omits 437d4571…/b34aebe6… (cited abbreviated in RESULTS; Auditor verified live). Caveat x=1 node 1.1e-7 vs t713u 4-dec values is disclosed. CORE_FREEZE/SF-W7-3 stated in PREREG not RESULTS — consistent.
## Verdict
CONFIRM — MATCH. G-R2: Written ABSENT-with-gap + DEDUCED nonvanishing on exact fit + AUTHOR-CANDIDATE menu R-NV0/1/2; NOT Cat A; OPEN; awaits Arvin ACCEPT/decline.
