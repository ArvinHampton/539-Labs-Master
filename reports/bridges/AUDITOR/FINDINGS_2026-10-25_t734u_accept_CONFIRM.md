# AUDITOR FINDINGS — CONFIRM deduce_t734u_accept (2026-10-25, America/Chicago)
Lock: Residual-vs-Resonant. No physics invented; no PASS/FAIL altered.
Verdict: **MATCH** | Soft SF: **none**

## Hashes (recomputed sha256)
| Item | Claimed | Result |
|---|---|---|
| PREREG.md | 7eabf4e7c4ea6c12bd10bcaa23f43764dd07913570d83abc8872121d0b17a7f5 | MATCH |
| RESULTS.md | 3181e59e0cb81668fe008028d35ccdee8536bd25158aed650cb57728d2631c60 | MATCH |
| SHA256SUMS | 2bc298849d288761372f37fee96c3de258359f4388ff137c93456b138eb0b245 | MATCH |
| STREAM_IDLE_LOCAL.md | aad054e2d592e126c1f503374f4ff9fa08e509dd895144704bba53a30aa99772 | MATCH |
| RUQ0_ACCEPT_SCOPE_QUOTE_t734u.md | af56dfdcc70a2fe08c1c5a7ead86ab4d90b52c6b2cea80722cf7535aff503553 | MATCH |
| FINDINGS_DRAFT | a49fb8a671d0133aab51cd79da765b45825bb420790573f89d44ba6d2970ae61 | MATCH |
| INVENTORY_t734u_RUQ0_accept | 9e545a89a2158c2b69a3f0a931d8b6b94e28fe6bcfd49cfd55570be4bfebab82 | MATCH |
| inventory_check/SHA256SUMS | 9467d78ee0d9b363b3fa3826544900896e0a1547b7a07b54f614f7ac3d8937e1 | MATCH |
| Basis menu GA1c_CLOSURE_MENU_t730u.md | 97f4e1fb79dc… | MATCH (live) |
| Prior CONFIRM t730u | ea7a223c16a7… | MATCH (live) |
- Package SHA256SUMS -c: all entries OK (PREREG, PREREG.sha256, RESULTS, draft, scope quote); last entry deduce_t734u_accept/PREREG.md is parent-relative, OK from BRIDGE_C_35 (hygiene note only, not SF).
- PREREG.sha256 -c: OK. Inventory SUMS -c: all OK incl. INVENTORY_t734u.

## Ordering
PREREG mtime 11:43:28 CDT < RESULTS 11:43:46 CDT; RESULTS cites PREREG 7eabf4e7… "(unchanged)". OK.

## ACCEPT basis
Arvin t734u ACCEPT **R-UQ0 only** (answering t732s4628) of menu 97f4e1fb…; scope quote verbatim from menu line 2; prior CONFIRM ea7a223c… re-verified in RESULTS. Cat A is ACCEPT-sourced and limited to R-UQ0 scope-exclusion. R-UQ1/R-UQ2 explicitly NOT accepted, NOT ingested.

## Claims verified
- G-A1c CLOSED under R-UQ0, ACCEPT-sourced Cat A, scope-exclusion only (Written 4-param F=a+bt+ct²+d/(1+t²), t=7x−3, S-B1′∧S-B1 + Object A; wider O(t²) pole-free class OUT; off-sample 13eb50e6 B7/OB4 still recorded) — CONFIRMED
- Uniqueness scope-complete (UNIQUE-in-family) — CONFIRMED
- residual-C OPEN (G-A3 PAUSED, X4 ABSENT-with-gap 2bb870b4…, G-R2, B3) — CONFIRMED
- δ≡0 / Bridge YES newly forced: NO / NO (F-C) — CONFIRMED
- Baselines 437d4571… + b34aebe6… stand, cited — CONFIRMED
- No invent; no wider uniqueness proof asserted — CONFIRMED

## Soft SF
None.

## Posture
Bridge PARTIAL; READY NO; residual-C OPEN; CORE_FREEZE + SF-W7-3 hold; no order78. G-A3 PAUSE and X4 ABSENT-with-gap unchanged.
