# FINDINGS — NL PURSUE-ALL APPROVED t2101u (route to Auditor)
- A: /workspace/quantum-comp/reports/OWNER_WRITE_NL_PURSUE_ALL_APPROVED_t2101u_2026-10-25.md sha256 b3f2ac7e59457446d4fac5c2256d250f014e15d9d0c532efa68a736607625d6a
- B: /workspace/quantum-comp/reports/bridges/NONLOCAL_QM_EH11D/inventory_check/ACK_OWNER_WRITE_NL_PURSUE_ALL_APPROVED_t2101u_2026-10-25.md sha256 ea6b4fb738c78845195a0515cd9fd66ac50c081ffd45a94bd2b1a742167aa872
- Tip 3d47ce497f812792a900cb103baff6ddfe838058d7883399239cd7763ba7bf79 untouched (verified; no drift).
## Re-search
| Stopper | t1145u hits | t2101u hits | New human lines | Status |
|---|---|---|---|---|
| Q4 (gap/bridge-force syn) | 6 | 6 | 0 | ABSENT-hold KEEP |
| Q8 f_* | 0 | 0 | 0 | ABSENT-hold KEEP |
| H (Hamiltonian) | 746 | 746 | 0 | OPEN KEEP (generic mentions; no Owner Write fixing H) |
| ψ (state) | 734 | 734 | 0 | OPEN KEEP |
| ρ₊₋ | 19 | 19 | 0 | CONSTRAINT-NONE KEEP |
| Φ(y) | 216 | 216 | 0 | Φ(y)→ρ₊₋U ABSENT KEEP |
| ER=EPR | 83 | 83 | 0 | no elevate |
| Tr ρ / e^{-|Δt|} | 0 | 0 | 0 | ABSENT |
Corpus: A22_grok_export_search/chats, 777 files, 0 files newer than t1145u hits json. Script 2e2c0bf977b4f61e7acbd786963219a9e6b36ce5a3ed07b68b755b0ba7e6caaf; hits dbee25556add73af040d0d9e81bcdd779bff720c606517f9556096b0a42c5fe1 (set-diff vs t1145u = 0 on every key). Negative evidence: no new Owner/human Write since t1145u.
## Result
No elevate (Q4, Q8 f_*, H, ψ, Φ(y)→ρ₊₋U unchanged). Queue recount unchanged vs t1218u/t1145u: Q4,Q8 ABSENT-hold; H,ψ OPEN; Φ(y)↔ρ₊₋U ABSENT; Q7 proof-gated; Q9/Q14–16 STOPPED.
## Soft SF hygiene note
"Fold pending" in NL apply Write f1258aba… is superseded by fold MATCH 9667f44e… (Auditor Soft SF on FINDINGS d9724521…). No historical rewrite.
## STREAM
Parent/inventory_check line-count drift (130 vs 118) clerical only; pursue line appended to both.
CONSTRAINT-NONE KEEP. Bridge PARTIAL / READY NO.
