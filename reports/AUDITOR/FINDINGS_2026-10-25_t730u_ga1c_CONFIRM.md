# AUDITOR FINDINGS — CONFIRM deduce_t730u_ga1c (t730u G-A1c) — 2026-10-25 America/Chicago
Lock: Residual-vs-Resonant. Auditor did not invent physics or alter PASS/FAIL.
## Hash recompute — ALL MATCH
PREREG 8b9768ab…1215 MATCH; RESULTS 74e5b80f…c8b4 MATCH; SUMS 72a21a21…5d0f MATCH; STREAM_IDLE_LOCAL f61f3105…9c9b MATCH; Menu 97f4e1fb…6d76 MATCH; FINDINGS draft 7b8425f9…8503 MATCH (non-authoritative); INVENTORY b28f53ab…1785 MATCH; inventory_check/SHA256SUMS 15686d91…8de5 MATCH.
sha256sum -c package SHA256SUMS: 9/9 OK. PREREG.sha256 OK. inventory_check SUMS -c OK. STREAM line 32 LOCK cites matching PREREG/RESULTS/SUMS.
## Checks
1. Hashes/SUMS/inventory: PASS.
2. PREREG before RESULTS: PASS (mtime 11:29:47 < 11:30:23 CDT; RESULTS cites PREREG hash; Expected outcomes pre-stated).
3. Menu AUTHOR-CANDIDATE, NOT Cat A; invent-ban: PASS. R-UQ0 = scope-exclusion of Written 4-param family (R-DS0-style), R-UQ1 = ABSENT supply placeholder (no selector given), R-UQ2 none. No new selector/number invented; kernel_check.txt is structure-only illustration.
4. F-A1c1 NO (DEDUCED), F-A1c2 YES, F-A1c3 YES-AUTHOR-CANDIDATE — recorded in RESULTS, consistent with PREREG: PASS.
5. UNIQUE-in-family/PARTIAL unchanged; Bridge YES/δ≡0/residual-C newly forced NO/NO/NO: PASS.
6. Baselines 437d4571… (Cat A) and b34aebe6… (R-DS0 CONFIRM) cited and stand; G-A3 PAUSED; X4/R-C1 untouched: PASS.
7. No Cat A without Arvin ACCEPT: PASS (default if no ACCEPT: G-A1c OPEN).
8. Bridge PARTIAL; READY NO; residual-C OPEN; CORE_FREEZE; SF-W7-3; no order78: PASS.
## Soft SF
NONE. Note (informational, not SF): RESULTS labels F-A1c3 "YES, AUTHOR-CANDIDATE only" vs author context "AUTHOR-CANDIDATE" — semantically equivalent. X4 not mentioned in package text beyond "X4/R-C1 untouched" — consistent.
## Verdict
CONFIRM — MATCH. G-A1c: ABSENT-with-gap + AUTHOR-CANDIDATE menu (R-UQ0 rec), NOT Cat A; awaits Arvin ACCEPT/decline.
