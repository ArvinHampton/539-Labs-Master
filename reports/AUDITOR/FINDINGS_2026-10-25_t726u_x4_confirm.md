# FINDINGS — Auditor Residual-vs-Resonant CONFIRM — t726u X4 (deduce_t726u_x4)
Written 2026-10-25 11:30 CDT (America/Chicago). Auditor only: no physics invented, PASS/FAIL not altered.
## 1 Hashes (recomputed) — ALL MATCH
PREREG 4618f824…ee417 MATCH | RESULTS c261a8bd…9ca7e MATCH | SHA256SUMS a0f140dc…a7eb27 MATCH | STREAM_IDLE_LOCAL 2c219203…3624 MATCH (L31 LOCK line cites PREREG/RESULTS/SUMS) | Candidate 2bb870b4…1d76 MATCH | FINDINGS draft 147d751e…fa7fa MATCH (non-authoritative) | INVENTORY_t726u_X4 581a4610…955d MATCH | inventory_check/SHA256SUMS 93da3d6a…4d3d MATCH.
sha256sum -c: package 12/12 OK; PREREG.sha256 OK; inventory_check 9/9 OK. logs/ 5 grep logs match LOG_SHAS.txt.
## 2 Ordering — PASS
PREREG mtime 11:25:11 CDT; logs 11:25:26; RESULTS 11:26:00. RESULTS cites PREREG sha "hashed before this file".
## 3 Labeling / invent-ban — PASS
Outcome AUTHOR-CANDIDATE, explicitly "NOT Cat A". Candidate gives no χ/ϑ definitions, no outer_* coefficients; ACCEPT items (i)–(vi) all marked ABSENT. Only DEDUCED content is parity arithmetic 7k/2 → 7m / 7m+7/2, labeled "not identification". HD L24 quote verified verbatim against 552541cf (incl. "(or its residual χ-twisted analogue)").
## 4 F-X4a/b/c/d — as RESULTS states (not altered)
F-X4a NO; F-X4b NO/ABSENT; F-X4c NO; F-X4d PARTIAL-YES. Consistent with PREREG outcome rule (a,b,c not all YES ⇒ not Cat-A-forced; d yes ⇒ AUTHOR-CANDIDATE). PARTIAL-YES vs rule's binary "d=YES" — treated as YES for outcome; noted, not an SF.
## 5 Identity / walls — PASS
Identity NOT Cat-A-forced; R-C1 wall STANDS; Bridge YES / δ≡0 / residual-C newly forced = NO/NO/NO.
## 6 G-A3 — PASS
"G-A3 PAUSED untouched"; no fill, R-D3/R-E2/R-PKG1 re-run, or t722u (c) diag claims in RESULTS or candidate.
## 7 Candidate revision citation — PASS
156ea029480afe79…320a resolves to deduce_t682u/author_candidates/AUTHOR_CANDIDATE_X4_chi_theta_outer_identity_sketch_2026-10-25.md. Sources 7dbd63af (pins ledger), 552541cf (HD, 4 copies), d12dd01d (EXTRACT_T635U), eb17f7e3 (MISSED_VARS) all recomputed MATCH.
## 8 Baselines
437d4571 (t695u), b34aebe6 (t704u), 2e1dec49 (t718u), 4ad006b7 (t722u), 1749576a (t721u) present in HASH_INTEGRITY; not consumed by this X4 package (N/A, no conflict).
## 9 State — PASS
Bridge PARTIAL; READY NO; residual-C OPEN; CORE_FREEZE + SF-W7-3 in PREREG; no order78.
## 10 Soft SF — NONE
No Cat A without Arvin ACCEPT; no χ/ϑ invent; no (c)-diag/G-A3 bleed.
## Verdict: MATCH — CONFIRM AUTHOR-CANDIDATE (NOT Cat A).
