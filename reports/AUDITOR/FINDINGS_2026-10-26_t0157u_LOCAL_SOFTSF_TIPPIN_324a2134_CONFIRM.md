# Auditor FINDINGS — Local STREAM Soft SF tip-pin rebind → 324a2134… CONFIRM
2026-10-26 ~01:57 CDT (America/Chicago). CONFIRM-only; cite-only; no physics invented; tip not edited; no messages.

## Verdict: MATCH-with-SF (rebind correct at write time ~01:01 CDT; live tip since moved)

## Hash recompute (sha256sum, ~01:58 CDT)
| Item | Claimed | Recomputed | Result |
|---|---|---|---|
| Live tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md | 324a2134… | 5569b14f4b1bbeceba1a6c33ae4cd48bfdc6630484a6bd5b8a0caef3866dfa93 (mtime 01:04 CDT) | SF: tip race (Path C P2 vacate/cusp B1) |
| Tip backup .pre-p2-vacate-cusp-b1-324a2134.md | 324a2134… | 324a21346dfd20c300628491615b00c38e1225c1563f2400bf25747edee30204 | MATCH |
| STREAM live BRIDGE_C_35/STREAM_IDLE_LOCAL.md | 8534516a… | 8534516a0853cc0035695ed181558cb4409fa473b3041bcb74c3d59c9ce49aec (mtime 01:01 CDT) | MATCH |
| STREAM backup .pre-softsf-tippin-324a2134-e80ef994-2026-10-26 | e80ef994… | e80ef99468977ed2883e35cd2c597749ff39cfe952b2d3a4846c585a33336398 | MATCH |
| Local FINDINGS grok-batches/LOCAL-SOFTSF-TIPPIN-324a2134-PATH-C-REBIND_2026-10-26.md | f4bc385a… | f4bc385aee71213504d3a77d9aca1378dca32e1b4a0b2e8594e6c8356f5c97b5 | MATCH |
| Auditor t0059u Path C FINDINGS | 3422bd85… | 3422bd8571243dc665b727dd7d1be5a7f70455422b65f2a6115f4bae3329f6c3 | MATCH |
| Prior Local MATCH t0056u | 2eea23dd… | 2eea23ddf6905f42ed592ede868d5b104cdf9a493b9786286dd59e590fa2ccd1 | MATCH |

## Content checks (STREAM ~01:01 CDT entry)
- Pins live tip Soft SF LOCK 324a2134… (was 86e439a8…), cites Auditor MATCH-with-SF 3422bd85… — MATCH
- Cites FINDINGS f4bc385a… — MATCH
- tip_touched Local NO — MATCH (STREAM mtime 01:01 precedes tip change 01:04; Local edited STREAM only)
- Soft SF F3 CLOSED (MR1 §1r) cited, Local no invent — MATCH
- Packaging a7c6872b… stands — MATCH
- HOLD μ₁₀/L-1 — MATCH
- Bridge PARTIAL / READY NO / NOT Cat A — MATCH
- Prior rebind MATCH 2eea23dd… CLOSED — MATCH

## Soft SF
- SF1 tip race: live tip 324a2134… → 5569b14f… at 01:04 CDT (external, Path C P2 vacate/cusp B1); STREAM pin 324a2134… now pre-pin history; Local rebind to 5569b14f… + CONFIRM needed.
- SF2 packaging a7c6872b… cite inherited-only (soft, carried from t0056u).
- No invent; no F3 reopen; FREEZE invent else respected; tip not touched by Local.
