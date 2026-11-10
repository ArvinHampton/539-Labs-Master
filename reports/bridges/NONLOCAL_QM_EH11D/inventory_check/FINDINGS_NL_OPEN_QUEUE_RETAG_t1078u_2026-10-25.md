# FINDINGS — NL open-queue RETAG after t1078u — 2026-10-25 ~19:31 CDT (America/Chicago)
**Status:** RETAG only from Owner Write `3cad20f6…`. invent-ban ON. residual-C LOCKED tip `492fb3ac…` not edited. Not Cat A. No mechanism invent.

Prior FINDINGS `48cb5f3a…` (Auditor MATCH-with-SF `e42f3e3c…`; SF-1 clerical OPEN-count only). This file supersedes **status tags** for Q2/Q4/Q7/Q8/Q10 only; other Q rows unchanged.

## Re-tagged queue (delta)
| Q | Prior tag (48cb5f3a…) | New tag (t1078u) | Leftover |
|---|---|---|---|
| Q1 | POINTER-ACKED | POINTER-ACKED | — |
| Q2 | NEED WRITE | **PARTIAL-CLOSED** | mech / puncture Ω-topology ABSENT-hold |
| Q3 | POINTER-ACKED | POINTER-ACKED | DE link NEED WRITE |
| Q4 | NEED WRITE | **ABSENT-hold** | gaps 5,7 behind Owner hold |
| Q5 | ABSENT | ABSENT | geo→alg force |
| Q6 | ABSENT | ABSENT | reverse-parity PT / json |
| Q7 | OPEN | **OPEN-proof-gated KEEP** | L6, L7 EH-FF1 |
| Q8 | OPEN | **ABSENT-hold** (f_*); Ω₁₁D UNAFFECTED | f_* closed forms |
| Q9 | STOPPED | STOPPED | No NL2 |
| Q10 | OPEN | **PARTIAL-CLOSED** | mech ABSENT-hold |
| Q11–Q13 | POINTER-ACKED | POINTER-ACKED | — |
| Q14–Q16 | STOPPED | STOPPED | three-needs / EH-field-vars / entangle-catalog |
| Q17 | LOCKED Local | LOCKED Local | residual-C read-only |

## Counts after retag
- PARTIAL-CLOSED: 2 (Q2, Q10)
- ABSENT / ABSENT-hold: 4 (Q4, Q5, Q6, Q8-f_*)
- OPEN-proof-gated: 1 (Q7)
- POINTER-ACKED: 5 (Q1, Q3, Q11, Q12, Q13)
- STOPPED: 4 (Q9, Q14, Q15, Q16)
- LOCKED Local: 1 (Q17)
- NEED WRITE remaining Owner-facing: Q3 DE link only (plus leftovers under ABSENT-hold)

## Status line
Bridge **PARTIAL** · residual-C **LOCKED** (digest `964294cc…` / tip `492fb3ac…`) · READY **NO** · invent-ban **ON** · No NL2 · No mechanism invent.
