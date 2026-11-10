# AUDITOR FINDINGS — NL W-PO-2 continuous Cat A extract — CONFIRM
Timestamp: 2026-10-24 23:50 CDT (America/Chicago)
Map: NON-LOCAL only (NONLOCAL_QM_EH11D). Not mixed with Local G1 b63db28c… or order77 1775ac9f…. CORE_FREEZE intact. Soft flags only; no PASS/FAIL altered; no invent.

## Hash integrity
- Live path: reports/bridges/NONLOCAL_QM_EH11D/inventory_check/
- FINDINGS_W_PO2_CONTINUOUS_EXTRACT_2026-10-24.md ced7d7b797e2e1de38bd9be1736bf08b6148baae55ed7ba17440d86eb331ef79 MATCH
- SHA256SUMS 3ef6281d628294da4aa455c10ba72f2f4a450afd254bdfb1c8ae660b9ba61526 MATCH; sha256sum -c: 12/12 OK, rc=0
- theorems/periodic-table-codex.txt fc74986a000b0f4d535aff78ef7efa5af9d2096fc39e21123b15a6a145bfa409 MATCH

## Claims
| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 1 | Cat A ABSENT Ω₀, f_warp, f_curv, f_b | CONFIRMED | Independent rg (chats excluded): Ω₀/Omega_0 hits only homonyms (solar Ω(θ) solar-oscillatory.txt / A27 txt; Ω_0^Spin in oct17-master A-series). f_* only in chat pins, audit notes, NL1 run.py (sympy undefined Function symbols, no numerics), STREAM_IDLE (quotes t591u Cat B). |
| 2 | Z_eff symbol-only in codex | CONFIRMED | Lines 48/62 F_Coulomb,rel with Zeff undefined; no rule/table. No *periodic_table*/*zeff* file on disk; .npz files present are unrelated Bridge C/heavy-daily. |
| 3 | Chat near-misses Cat B only | CONFIRMED | OMEGA_F_FACTOR_TABLES (t614u), BRIDGE_C_35/pins P_orth/PIN_LEDGER (t591u), all chat-sourced. |
| 4 | No Drive/paper for W-PO-3 | CONFIRMED (on-disk) | No on-disk Drive extract with f_*/Ω₀ definitions; see SF-2. |
| 5 | Extract-only; no invent; no NL2 | CONFIRMED | No NL2 path anywhere; prereg has only EH_* and NL1_OMEGA_FTOTAL. |
| 6 | W-PO-2 OPEN narrowed; W-PO-3 OPEN | CONFIRMED | Consistent with prior c3764d87…. |

## Soft flags
- SF-1: Codex renders the symbol as "Zeff" (no underscore); literal grep 'Z_eff' = 0 hits. Cosmetic; claim stands.
- SF-2: Auditor did not re-query live Google Drive this pass; W-PO-3 "no Drive/paper" rests on on-disk extracts + prior DRIVE_HUNT note.
- SF-3: NL1 run.py names f_warp/f_curv/f_b as symbolic sympy Functions — not Cat A values; ensure never cited as a table.

## Open set
- W-PO-2: OPEN (narrowed) — Ω₀, f_warp, f_curv, f_b, Z_eff rule/table all lacking Cat A.
- W-PO-3: OPEN — no Drive/paper original.

## Disposition
CONFIRM coordinator extract. No closure. No NL2. No invented f_* / Ω₀.
