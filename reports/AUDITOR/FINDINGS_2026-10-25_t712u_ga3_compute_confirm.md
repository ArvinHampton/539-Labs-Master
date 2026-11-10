# FINDINGS — Auditor CONFIRM t712u G-A3 AUTHORIZED compute (deduce_t712u_ga3_compute)
Stamp: 2026-10-25 ~10:42 CDT (America/Chicago). Residual-vs-Resonant lock. Auditor-authored (executor draft 95c4e4e2… NOT used as authority). No physics invented; PASS/FAIL unaltered.
Authority: t712s4471 — Arvin AUTHORIZED G-A3-only compute (new-table ban lifted for h-table schema 8d247feb… only; invent-ban holds elsewhere).

## Hash verification (recomputed)
| Artifact | Claimed | Recomputed | |
|---|---|---|---|
| PREREG.md | 25341d71ab3d0fdd8755e90cf1ab61dcf5e2be84615166c9bff51a0cf8f94df0 | same | MATCH |
| RESULTS.md | 333fa5bc39064b88f6d720c4b2728242c5174300773c68ff32bda031d4725840 | same | MATCH |
| package SHA256SUMS | 565d42701d96165d8674295f5c2e31a009ec816606d75e4664c1267280dc3476 | same | MATCH |
| BRIDGE_C_35/STREAM_IDLE_LOCAL.md | 5c508383d942ce71bcd98ef4473026e43f151239004b12f56e8b6c39aa7ce7bb | same | MATCH |
| BRIDGE_C_35/inventory_check/SHA256SUMS | 4475b5ce8bc278d071b34d7c7ec7a75c0c584fdea725339e2b7f06cf387c42ea | same | MATCH |
| logs/input_gate.log | 13d218500f012b5d9a1dc5ae91383d433a69e9e07aefb3f56b902b1dcb25d486 | same | MATCH |
| executor draft (info only) | 95c4e4e25659686aab3c9b18f7bcf976abe4d45ddc4274fdaa3776791dc4850c | same | MATCH (non-authoritative) |

- Package `sha256sum -c`: 5/5 OK (PREREG, PREREG.sha256, RESULTS, draft, input_gate.log). Inventory: 66/66 OK.
- PREREG before RESULTS: PREREG.sha256 records 25341d71…; RESULTS cites it; mtimes PREREG 10:38:32 < gate log 10:38:40 < RESULTS 10:39:11 CDT. MATCH.

## Scoping / fences
- RG-C0 gate BLOCKED with documented, path-cited blockers B-ψ (ψ(x) symbol-only in Ξ/Eichler chain; psi-Cocycle 1be7f7d1… ψ not identified with Bridge C ψ in writing), B-path (0→i∞ vs i∞→x; branch unspecified — visible directly in input_gate.log rg output, b329c67c L21 / 552541cf L46 vs 1bab65c4 L32), B-coeff (Ξ table "selected support…", partial entries, semantics/normalization unstated). No invent: ψ≡0 partial explicitly refused. MATCH.
- author_candidates/ is EMPTY (no filled h-table). Schema 8d247feb4f1b644dfbaf1d28237eaddfe9ba45c82d40464a2290d4721b0f8051 recomputed unchanged; empty AUTHOR-CANDIDATE; NOT Cat A. No filled values ⇒ none treated as Cat A. MATCH.
- Invent-ban held elsewhere; scope Local Bridge C only; no nonlocal EH11D/Ω₁₁D/F_total.

## Force criteria / verdicts
- F1 NOT EVALUABLE; F2 δ≡0 NOT forced; F3 NOT EVALUABLE. Bridge YES / δ≡0 / residual-C newly forced: NO / NO / NO. MATCH.
- Bridge PARTIAL; READY NO; residual-C OPEN. MATCH.
- CORE_FREEZE; SF-W7-3 (Continue_Closure excluded) honored; no order78 dir or action. MATCH.

## Baselines stand (recomputed)
- Selectors Cat A 437d4571e0f707460c7ac2a7dd983d0649161dd7975779101907eaedba7d7476 — stands.
- G-A1b CLOSED R-DS0 b34aebe65a3f57eff1690dde5fce01efa8e3722331e1098ee5f6efb578c905ac — stands.
- G-A3 schema draft CONFIRM 6228303851d0dbdebeb6e2a1032af898b0af14d659c6b0b44180f9ff3b290c21 — stands (no filled ACCEPT package).
- NL 29ebbdd81d8df406db33e5d63bea221c828b742dfe24a7aaff07ab684ea78d54 — untouched.

## Soft SF
None. (No invent; no Cat A; no filled values.) Cosmetic note only, not SF: source 1bab65c4 L30 exponent typo "(w − x)^{-−1/2}" — supports B-coeff/B-path ambiguity, no action.

## Verdict
CONFIRM — t712u G-A3 AUTHORIZED compute BLOCKED at input gate (ψ / path / coeff semantics); no fill; NOT Cat A; F1 n/a, F2 not forced, F3 n/a; Bridge PARTIAL / READY NO / residual-C OPEN. Unblock requires Arvin supply: ψ definition (or ACCEPT of psi-Cocycle identification), path+branch, coeff semantics+normalization+N_trunc.
