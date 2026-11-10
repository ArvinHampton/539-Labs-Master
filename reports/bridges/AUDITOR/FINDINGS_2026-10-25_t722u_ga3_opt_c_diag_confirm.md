# FINDINGS — Auditor CONFIRM t722u GA3 opt (c) diagnostics (2026-10-25 CDT, America/Chicago)
Package: BRIDGE_C_35/deduce_t722u_ga3_opt_c_diag/ — Residual-vs-Resonant lock. DIAGNOSTICS-ONLY / class C / NOT Cat A / NOT Bridge-closing. PASS/FAIL not altered.

## 1. Hashes (recomputed) — 10/10 MATCH
PREREG 36b663d3…f5 MATCH | RESULTS 9aa52f19…7a MATCH | SHA256SUMS 6313548b…5d MATCH (sha256sum -c 9/9 OK) | STREAM_IDLE_LOCAL 32d1640b…a320 MATCH | FINDINGS draft 43ef4a7e…dd MATCH (not authoritative) | diag table bd63821f…18 MATCH | slash_regen c97ec8d5…3d MATCH | diag_out 0d637ec9…f1 MATCH | inventory file 95d85226…36 MATCH | inventory SUMS af40a090…f8 MATCH (-c 3/3 OK, includes t722u entry). Also: diag.py 77580b51… (in SUMS), Ξ file 35b186f9… recomputed MATCH.

## 2. Ordering — OK
PREREG.md mtime 11:18:59.83 CDT, PREREG.sha256 11:18:59.83; RESULTS 11:20:02; commands.log diag run 11:19:37. PREREG before RESULTS.

## 3–4. Scope / Ξ source — OK
RESULTS + draft: DIAGNOSTICS-ONLY, NOT Cat A, NOT Bridge-closing, NO ledger fill, R-C1 BLOCKED, G-A3 NOT filled. diag.py loads only Xi_regen_N106.tsv with in-script assert sha 35b186f9…; 0 occurrences of ledger 7dbd63af… in script; RESULTS states ledger Ξ unused.

## 5. Premises — OK
P2, ψ t713s4484, t712s4471, t720u R-D3, t722u (c) cited in PREREG and RESULTS.

## 6. Force criteria — as RESULTS states
F1 FAIL; F2 δ≡0 NOT forced; F3 PASS (nonzero defect) but controlled = NO (ε→0 unstable, tail majorant diverges at ε=0, W₇-endpoint convention-sensitive), consistent with PREREG criterion "F3 controlled iff E_δ≪|δ_ε| AND ε→0 stable". Labels consistent; no mislabel. Bridge YES / δ≡0 / residual-C newly forced: NO/NO/NO.

## 7. Soft S1–S4 — documented in RESULTS (tol σ retention; W₇ shifted-endpoint convention needs AUTHOR choice; mixed regularization; Ξ 9-term/N106 limit).

## 8. No Cat A fill claim; no R-C1 unblock claim. No SF.

## 9. Baselines
selectors 437d4571… cited (PREREG+RESULTS); G-A1b b34aebe6… and menu 2e1dec49… cited in PREREG only; BLOCKED 1749576a… stands (cited both).

## 10. Status
Bridge PARTIAL; READY NO; residual-C OPEN; no order78 (RESULTS). CORE_FREEZE and SF-W7-3 present in PREREG.

## Soft SF (minor, no PASS/FAIL change)
- SF-a: RESULTS omits CORE_FREEZE / SF-W7-3 and G-A1b b34aebe6… / menu 2e1dec49… citations (present in PREREG only).
No invent / Cat A / R-C1 / ledger SF.

## Verdict: CONFIRM — MATCH. DIAGNOSTICS COMPLETE. G-A3 NOT filled; R-PKG1 BLOCKED 1749576a… stands; R-C1 BLOCKED.
