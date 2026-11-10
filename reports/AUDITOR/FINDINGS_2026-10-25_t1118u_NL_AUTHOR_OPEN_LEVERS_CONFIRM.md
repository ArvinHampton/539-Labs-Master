# AUDITOR FINDINGS — NL t1118u Author open-levers pack CONFIRM — 2026-10-25 ~20:40 CDT (America/Chicago)
**Verdict: MATCH-with-SF** (soft SF only: SF-P provenance, SF-W4–W8 on file; no hard FAIL).

## Hashes (all MATCH)
- Stamp `reports/coordinator/OWNER_AUTHORITY_SEARCH_PURSUE_WRITE_APPLY_t1118u_2026-10-25.md` — `c1d59d58d391e03340eb2b79391d519fa4eac6f7259239d16a4599ff387ee014` MATCH (Owner grant ~20:13 CDT; Non Local Path + Auditor covered; invent-ban LIFTED Author-scope)
- A Write `reports/OWNER_WRITE_NL_AUTHOR_OPEN_LEVERS_t1118u_2026-10-25.md` — `a6cc1ab26e2c8221bde24e77d5d39c4c0ac7fc29f327a8aa68204e9b681691ce` MATCH
- B ACK `reports/bridges/NONLOCAL_QM_EH11D/inventory_check/ACK_OWNER_WRITE_NL_AUTHOR_OPEN_LEVERS_t1118u_2026-10-25.md` — `796bf8759d1d500d396ff5a1b6315e1a7cf0d7cb447d5b7beaa9cd10a0971822` MATCH (ACKs A sha exactly)
- C RETAG `reports/bridges/NONLOCAL_QM_EH11D/inventory_check/FINDINGS_NL_OPEN_QUEUE_RETAG_t1118u_2026-10-25.md` — `3d61e20d796af144431b521188daf153922cabaa1646cdeb12a97ee7af791dde` MATCH (cites A + B shas exactly)
- residual-C `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` — `492fb3ac95c20e9117594639eb5947c90785a09e93da8301d6e83980c490a6fa` MATCH before and after this write; untouched.

## Per-lever (A / B / C consistency)
| Lever | Claim | A | B | C | Result |
|---|---|---|---|---|---|
| Φ(y) | W-NL5 Written | Written formula label | WRITTEN | ABSENT-hold→WRITTEN | PASS (spot-check eb22cd97:136 human-turn text present) |
| ER=EPR / 540 s | W-NL6 Written framing | Written framing; t1086u hold released; 540 s stays Cat B | WRITTEN | →WRITTEN | PASS (spot-check a3424458:137 text present) |
| Q10 mech | W-NL7 Written-partial | partial; 61 not promoted; stub untouched | WRITTEN partial | Q10 PARTIAL-CLOSED (mech label) | PASS |
| coeffs | W-NL8 Partial | N_worm, Tr ρ=1, g₁₁ Written; H, ψ, ε_S8, δ(t), Φ OPEN | same | open list in Q10 | PASS |
| Q4 | ABSENT-hold | 2 irrelevant hits | ABSENT-hold | KEEP | PASS |
| Q8 f_* | ABSENT-hold; Ω₁₁D UNAFFECTED | 0 human hits; no Ω₁₁D change | same | KEEP; UNAFFECTED | PASS (Auditor grep: only f_* hit ba343229:106/108 is an assistant turn — claim holds) |

## Queue-17 check
C counts 4+3+1+4+4+1 = 17; tag counts unchanged vs t1086u; Q17 LOCKED Local; NEED WRITE 0. PASS.

## Soft SF (on file, not FAIL)
- SF-P: human turns often Arvin-pasted Grok-origin text; elevation = Author adoption under t1118u, not independent derivation (continues t1086u SF-P/W1–W3).
- SF-W4 Φ(y) form variants unresolved; SF-W5 Tr ρ=1 vs e^{−|Δt|/τ_ent} tension; SF-W6 τ_ent triple conflict (GM/c³ · 539/539.9 s · 233.38 as) — W-NL1 GM/c³ kept, no choice Written; SF-W7 Φ overload in Δt_11D; SF-W8 Ω₁₁D variants not Written.
- Stub `64e17d5f…` cited as untouched; pack does not edit it.

## Status flags
Bridge PARTIAL · READY NO · not Cat A · residual-C LOCKED tip 492fb3ac… MATCH · invent-ban LIFTED (Author scope) · Ω₁₁D UNAFFECTED · no Bridge C content.
