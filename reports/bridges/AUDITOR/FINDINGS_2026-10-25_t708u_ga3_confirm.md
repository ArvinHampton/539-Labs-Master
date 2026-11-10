# Auditor FINDINGS — t708u G-A3 h-table (Residual-vs-Resonant CONFIRM)
Stamp: 2026-10-25 10:35 CDT (America/Chicago). Auditor independent recompute; executor draft (89842fa1…) NOT used as authority.
Authority: t708s4448 AUTHOR DIRECTIVE (Arvin PURSUE G-A3 h-table Written/AUTHOR-CANDIDATE).
Package: reports/bridges/BRIDGE_C_35/deduce_t708u_ga3/

## Hash verification (sha256 recomputed)
| Artifact | Recomputed | Verdict |
|---|---|---|
| PREREG.md | 5c65afec75cdebc9965a9f7ce9c3d78f04ac447bc96e5250188339facd8f4949 | MATCH |
| RESULTS.md | 1c0e12ca78666028fcf136f8c3283644d010d2a3ec111c4bc0ce779b4c676309 | MATCH |
| SHA256SUMS (pkg) | 483cd14ef05a50a911019b090e493f9a669b200d15ef45d33ab6618d20d718f4 | MATCH; -c 4/4 OK (PREREG, PREREG.sha256, RESULTS, schema) |
| author_candidates/AUTHOR_CANDIDATE_GA3_h_table_schema_v2_2026-10-25.md | 8d247feb4f1b644dfbaf1d28237eaddfe9ba45c82d40464a2290d4721b0f8051 | MATCH; in SUMS |
| ../STREAM_IDLE_LOCAL.md | 67e4b8311905f9375ba0485892817f754b397bccaadd69a06e24b0c623705057 | MATCH (L25 t708 LOCK line consistent) |
| ../inventory_check/SHA256SUMS | d9f692de8e11c84790c30575f1a70a8858a064d24f9cead30856707adf26e27c | MATCH; -c 60/60 OK |

## Order
PREREG mtime 10:31:42.700 CDT; PREREG.sha256 10:31:42.704; schema 10:31:54; RESULTS 10:32:08.200; SUMS 10:32:08.204; executor draft 10:32:35. PREREG.sha256 records 5c65afec… = current. PREREG before RESULTS: CONFIRMED.

## Scoping / fences
- Schema header "AUTHOR-CANDIDATE (NOT Cat A until Arvin ACCEPT)"; all Table H cells EMPTY; extends (not replaces) P-B3 5f60d40f…. No numeric h/δ/outer_* anywhere: CONFIRMED.
- RG-H1 Written h ABSENT-with-gap (7368b855 L50 "not yet tabulated"); RG-H2 NOT forced; supply list to Arvin stated.
- Bridge YES newly forced: NO (RG-H4; even with h, samples ≠ δ≡0, plus G-A1c/G-R2).
- CORE_FREEZE + SF-W7-3 stated; Closure-tree 8de53093/3405fac1 excluded; no order78 dir exists.
- No use of new candidate as Cat A found; residual_slash column cites existing Cat A 437d4571… only.

## Baselines (stand, recomputed)
- Selectors CONFIRM FINDINGS_2026-10-25_t695u_local_accept.md 437d4571e0f707460c7ac2a7dd983d0649161dd7975779101907eaedba7d7476 — present/unaltered.
- G-A1b CLOSED R-DS0 FINDINGS_2026-10-25_t704u_accept_confirm.md b34aebe65a3f57eff1690dde5fce01efa8e3722331e1098ee5f6efb578c905ac — present/unaltered.
- NL FINDINGS_2026-10-25_t685u_nl_identity_accept.md 29ebbdd81d8df406db33e5d63bea221c828b742dfe24a7aaff07ab684ea78d54 — unaltered.

## Status
G-A3: AUTHOR-CANDIDATE schema v2 (NOT Cat A until Arvin ACCEPT) / Written ABSENT-with-gap. UNIQUE-in-family/PARTIAL; G-A1c, G-R2, G-A3 open. Bridge PARTIAL; READY NO; residual-C OPEN.

## Soft SF
None.

## Verdict
CONFIRM (all 6 hashes MATCH; 4/4; 60/60; order OK; fences hold). PASS/FAIL not altered.
