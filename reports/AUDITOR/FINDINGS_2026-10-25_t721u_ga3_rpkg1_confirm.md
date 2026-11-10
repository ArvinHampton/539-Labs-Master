# FINDINGS — Auditor CONFIRM deduce_t721u_ga3_rpkg1 (R-PKG1 / P2)
Date 2026-10-25 ~11:16 CDT (America/Chicago). Residual-vs-Resonant lock. Auditor recomputed all hashes; draft 7a445d8d… not used as authority. No physics invented; PASS/FAIL unaltered.

## Hash table (recomputed)
| Item | Claimed | Recomputed | |
|---|---|---|---|
| PREREG.md | 9e0c3705… | 9e0c3705655d…1f47 | MATCH |
| RESULTS.md | 7d324d73… | 7d324d735f85…6e1f | MATCH |
| SHA256SUMS | 3f557c8a… | 3f557c8acbef…c94f | MATCH |
| blank table (author_candidates/…BLOCKED) | 90ebe1e8… | 90ebe1e89139…9e44 | MATCH |
| BRIDGE_C_35/STREAM_IDLE_LOCAL.md | c6ab7cc2… | c6ab7cc251d0…7769 | MATCH |
| BRIDGE_C_35/inventory_check/SHA256SUMS | a08d0597… | a08d0597e384…b157 | MATCH |
| ledger Ξ snapshot (logs/) | 7dbd63af… | 7dbd63af5afb…ff47 | MATCH |
| FINDINGS draft | 7a445d8d… | 7a445d8d5bb1…43c6 | MATCH |
| baseline selectors | 437d4571… | 437d4571e0f7… | MATCH |
| baseline G-A1b | b34aebe6… | b34aebe65a3f… | MATCH |
| baseline menu | 2e1dec49… | 2e1dec49fc0b… | MATCH |
Package `sha256sum -c SHA256SUMS`: 8/8 OK. inventory_check `-c`: 7/7 OK, 0 fail.

## Checks
1. Hashes MATCH; SUMS OK; inventory OK — PASS.
2. PREREG before RESULTS: PREREG.sha256 records 9e0c3705…; mtimes PREREG 11:12:57 < RESULTS 11:13:21 CDT; RESULTS cites unchanged PREREG hash — PASS.
3. Blocker honest: ledger snapshot (7dbd63af…) L37–50 gives Ξ_even/odd = Σ χ(k) q^{−35k²/4−7k/2} ϑ(q; n+7k/2) with χ_even/odd, ϑ_even/odd never defined; n free in general form. Corpus grep log 35 lines, no definitions. Blank table: all 4 rows "—" for ψ/h/slash/δ — PASS; no invent.
4. Premises cited: t712s4471, t720u (R-PKG1), t721u (P2), R-E2, R-B0 in PREREG and RESULTS — PASS.
5. F1 n/a; F2 δ≡0 NOT forced; F3 n/a; Bridge YES/δ≡0/residual-C newly forced NO/NO/NO — PASS.
6. Baselines stand (recomputed above) — PASS.
7. Bridge PARTIAL; READY NO; residual-C OPEN — PASS.
8. CORE_FREEZE, SF-W7-3, no order78 stated in PREREG; RESULTS "No order78" — PASS.
9. No fill, no Cat A claim ("Class C, NOT Cat A"); unblock options (a)/(b)/(c) left to author, not taken — PASS.

## Soft SF (flag only)
- SF-soft-1 (minor): G-A1b baseline b34aebe6… not cited by hash in package PREREG/RESULTS (only 437d4571, 2e1dec49); baseline recomputes MATCH.
- SF-soft-2 (minor): inventory_check/SHA256SUMS does not list deduce_t721u files; STREAM_IDLE_LOCAL does reference the package.
- No invent / Cat A misuse SF.

## Verdict
CONFIRM: MATCH. G-A3 BLOCKED at RG-0 (ledger Ξ symbolic) honest. Bridge PARTIAL | READY NO | residual-C OPEN. NOT Cat A. No order78.
