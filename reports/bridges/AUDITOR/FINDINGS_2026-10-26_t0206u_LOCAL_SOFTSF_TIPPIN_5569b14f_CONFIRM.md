# Auditor FINDINGS — Local Soft SF STREAM tip Soft SF rebind → 5569b14f — CONFIRM — 2026-10-26 02:06 CDT (America/Chicago)

Verdict: **MATCH-with-SF**

## Recomputed sha256
- Tip Soft SF LOCK live `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md`: `5569b14f4b1bbeceba1a6c33ae4cd48bfdc6630484a6bd5b8a0caef3866dfa93` — MATCH
- Tip LOCK Auditor FINDINGS t0159u: `43fbe91aa86f9d8c184d328bc82e1b82b210ce554654f694258c896f0a6ec759` — MATCH
- Local FINDINGS `grok-batches/LOCAL-SOFTSF-TIPPIN-5569b14f-P2VACATE-CUSP-B1-REBIND_2026-10-26.md`: `9c8409982ebb98f5a106738aefa25669b15f241884b927bf94f895a6bfa28772` — MATCH
- STREAM live `BRIDGE_C_35/STREAM_IDLE_LOCAL.md`: `e0be3e4998d8ad22e1cc8b5bd98d846ebf6d4b0be5ccb36ae39348a7c52fe7ec` — MATCH
- STREAM backup `BRIDGE_C_35/.pre-softsf-tippin-5569b14f-8534516a-2026-10-26`: `8534516a0853cc0035695ed181558cb4409fa473b3041bcb74c3d59c9ce49aec` — MATCH

## tip_touched
Tip mtime 01:04:52 CDT < FINDINGS 02:04:31 / STREAM 02:04:31 CDT. tip_touched Local **NO**. Live tip unchanged since pin → no Soft SF tip race.

## STREAM diff (backup→live)
Append-only (+2 entries after line 162): (a) record of prior Auditor Soft SF CONFIRM a192858f (CLOSED) + race note; (b) rebind entry pinning tip 5569b14f, citing tip LOCK MATCH-with-SF 43fbe91a, Soft SF F3 CLOSED, HOLD μ₁₀/L-1, Bridge PARTIAL / READY NO / NOT Cat A, FINDINGS sha 9c840998. No F3 reopen; no new physics content (ρ(−I)=S_lab⁻² / Γ₀(49) are restatements of prior CLOSED items).

## Soft SF flags
- SF1: Local FINDINGS does not embed live STREAM sha (by design, avoids cycle) — confirmed here as e0be3e49.
- SF2: STREAM entry (a) was authored by Local summarizing Auditor history; content consistent with prior FINDINGS.
- Pack is tip pin rebind only; no new Author-Write invent. Soft SF invent HOLD intact.
