# FINDINGS — NL open-queue RETAG after t1086u — 2026-10-25 ~19:54 CDT (America/Chicago)
**Status:** RETAG from Owner Write `7dc255dabab32a2edc7e1fcae4b14c26d6727121c7626ee2c80547caf91b95df` (ACK `99e3af2de8c211172d3b5045a49e62906ab493ec49df781bf3232e552f284b52`). Supersedes tags for Q3, Q6 only (plus N-6 record). Prior RETAG t1078u `1f72353e…`. invent-ban ON. Not Cat A.

| Q | Prior (1f72353e…) | New (t1086u) | Leftover / basis |
|---|---|---|---|
| Q1 | POINTER-ACKED | POINTER-ACKED | — |
| Q2 | PARTIAL-CLOSED | PARTIAL-CLOSED | mech ABSENT-hold |
| Q3 | POINTER-ACKED (DE link NEED WRITE) | **PARTIAL-CLOSED (definition)** | Item4 W4.2 (`3193335f…`): "DM … convert to DE … then undergo parity reversal in stellar cores through D2-brane interaction with the −U reverse-parity sector" + W-RP1 −U parity label. DE→star-throat mechanism/rates ABSENT-hold |
| Q4 | ABSENT-hold | ABSENT-hold | no new corpus (see search) |
| Q5 | ABSENT | ABSENT | geo→alg force; untouched |
| Q6 | ABSENT | **PARTIAL-CLOSED (definition)** | W-RP1/W-RP2/W-RP3 Written labels; periodic_table_539labs.json + Z-rows ABSENT |
| Q7 | OPEN-proof-gated | **OPEN-proof-gated KEEP** | no Lean proof written |
| Q8 | ABSENT-hold (f_*) | ABSENT-hold; Ω₁₁D UNAFFECTED | — |
| Q9 | STOPPED | STOPPED | — |
| Q10 | PARTIAL-CLOSED | PARTIAL-CLOSED | mech ABSENT-hold; W-NL2 adds horizon-wormhole label only |
| Q11–13 | POINTER-ACKED | POINTER-ACKED | — |
| Q14–16 | STOPPED | STOPPED | — |
| Q17 | LOCKED Local | LOCKED Local | residual-C read-only |

## N-6 proof-status discrepancy — reconcile (record only)
Corpus (from `FINDINGS_T875U_NL_L1_L7_THEOREMS` :22–25 and `FINDINGS_T876U_NL_L1_L7_ZENODO_ALIGN` :27–31): (a) Wrap 09-28 "L5 is the only finished theorem"; (b) Zenodo EH1 App. C "Lean source: L5, L7. No kernel run here."; (c) Lean header 09-29 "built L1-L7 … linter warnings only", no sorry/axiom. Reconcile: dates are ordered (09-28 → 09-29), consistent with a later build superseding the Wrap, but assumption ledger shows L2–L4, L6 rest on defs/hypotheses (L6 needs hK, L7 needs h1,h2). **Record:** "built" ≠ "derived from 11D metric"; L5 is the only theorem the three sources agree on. Not resolved by kernel run (none performed). No invent.

## Search log (Q4/Q8/Q10 mech)
Searched human turns of eb22cd97, eda69302, bdda1270 for ρ/wormhole/Ω_11D/Δt_11D/N⁻Z⁻ terms. Found Ω_11D normalisation label (/workspace/quantum-comp/reports/s_family_paths/…/eda69302:134 "Derived from the M-theory metric…") — no f_* closed form, no post-collision photon dynamics, no coupling rule, no ER-EPR mechanism → Q4/Q8/Q10 mech stay ABSENT-hold. Other 31 reverse-parity chats not re-read this pass.

## Counts
PARTIAL-CLOSED 4 (Q2, Q3, Q6, Q10) · ABSENT/ABSENT-hold 3 (Q4, Q5, Q8-f_*) · OPEN-proof-gated 1 (Q7) · POINTER-ACKED 4 (Q1, Q11, Q12, Q13) · STOPPED 4 (Q9, Q14–16) · LOCKED 1 (Q17) = 17. NEED WRITE remaining: 0 (leftovers under ABSENT-hold).

## Status line
Bridge **PARTIAL** · residual-C **LOCKED** (tip `492fb3ac…` MATCH) · READY **NO** · invent-ban **ON** · No NL2 · not Cat A.
