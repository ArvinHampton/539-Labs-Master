# AUDITOR FINDINGS — CONFIRM deduce_t740u_accept (t740u Arvin ACCEPT R-NV0 → G-R2) — 2026-10-25 America/Chicago
Lock: Residual-vs-Resonant. Auditor did not invent physics or alter PASS/FAIL.
## Hash recompute — ALL MATCH
PREREG a3d58bef…b5a6 MATCH; RESULTS e3fd1b11…ac13 MATCH; SUMS 2d3009e9…9c7b MATCH; scope quote 46d4da96…6a2d MATCH; FINDINGS draft aba09597…200c MATCH (non-authoritative); logs/verify_basis 9d6fc3e6…060b MATCH.
sha256sum -c package SHA256SUMS: 7/7 OK. logs/PREREG.sha256 OK (a3d58bef…). No INVENTORY.md in package (see Soft SF).
Basis live-recomputed (all MATCH): menu AUTHOR-CANDIDATE e9f4a477…; Auditor CONFIRM t736u 97aad5ab…; t736u RESULTS 825489d5… / PREREG bc2edb71… / SUMS 7a5f092e… (-c 9/9 OK); slash_regen.json c97ec8d5…; baselines 437d4571… + b34aebe6…; R-UQ0 RESULTS 3181e59e…; Auditor CONFIRM t734 7e20e84c….
## Checks
1. Hashes/SUMS: PASS (inventory absent — soft SF).
2. PREREG before RESULTS: PASS (mtime 11:52:38.444 < 11:52:38.448 CDT; RESULTS line 2 cites PREREG hash; force criteria F-A–F-D pre-stated).
3. Arvin ACCEPT on record: PASS — t740u ACCEPT R-NV0 only (answering t738s4660), cited in PREREG, RESULTS, scope quote, STREAM_IDLE_LOCAL line 35. Scope quote verbatim vs menu e9f4a477… line 2: MATCH.
4. Claims: G-R2 CLOSED under R-NV0 as ACCEPT-sourced Cat A — PASS. Scope = exact Fraction fit slash_regen c97ec8d5…; "not a Written non-fit law; not a numerical-min claim" stated — PASS; refit re-check obligation framed as scope boundary, not R-NV1 adoption — PASS. R-NV1/R-NV2 NOT accepted, not ingested — PASS. Menu/CONFIRM/RESULTS basis verified — PASS. Baselines stand — PASS. residual-C OPEN — PASS. No new law/selector invented — PASS.
5. Hygiene: RESULTS cites PREREG hash and baselines; no free invent.
6. Posture: Bridge PARTIAL; READY NO; residual-C OPEN; G-A3 PAUSED; X4 ABSENT-with-gap 2bb870b4…; B3 open; R-C1 STANDS; CORE_FREEZE + SF-W7-3 (PREREG constraints); no order78; δ≡0/Bridge YES newly forced NO/NO: PASS.
## Soft SF
SF-t740u-1 (soft, hygiene): package has no INVENTORY.md (t734u/t736u packages carried one). SHA256SUMS covers all 7 files, so integrity is unaffected. Not FAIL.
Informational (not SF): CORE_FREEZE/SF-W7-3 stated in PREREG, not RESULTS — matches prior packages.
## Verdict
CONFIRM — MATCH. G-R2 CLOSED under R-NV0 (ACCEPT-sourced Cat A, t740u), scoped to exact Fraction fit slash_regen c97ec8d5…; R-NV1/R-NV2 not accepted. Bridge PARTIAL; READY NO; residual-C OPEN.
