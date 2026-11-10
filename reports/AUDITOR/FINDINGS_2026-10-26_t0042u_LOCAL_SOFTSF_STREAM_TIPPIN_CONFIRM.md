# Auditor FINDINGS — Local STREAM tip Soft SF rebind CONFIRM — 2026-10-26 ~00:42 CDT (America/Chicago)

**Verdict: MATCH-with-SF**

## Recomputed sha256
| Claim | Path | Claimed | Recomputed | Result |
|---|---|---|---|---|
| 1 FINDINGS packet | /workspace/grok-batches/LOCAL-SOFTSF-TIPPIN-64d23f39-STREAM-CONFIRM_2026-10-26.md | 7d94910d… | 7d94910da18c8371e5d6854713d9aa44c4a9775522b75ad193010e44cdd7cbcd | MATCH |
| 2 STREAM tip-pin | quantum-comp/reports/bridges/BRIDGE_C_35/STREAM_IDLE_LOCAL.md | acf3721a… | acf3721a85615d42dd61eaa2e30ce8035fe75886669c172c62e61b4c2c3f7fc3 | MATCH |
| 2b backup | STREAM_IDLE_LOCAL.md.pre-softsf-tippin-64d23f39-1bfc9e3d-2026-10-26 | exists | exists | MATCH |
| 3 Tip live | /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md | 64d23f39… | 64d23f39975cfafc91582d86c192612544ddf11aebe7dddb7a359ef5354f47ff | MATCH |
| 4 Packaging | BRIDGE_C_35/AUTHOR_WRITE_MU10_GEO_INVARIANT_LOCAL_2026-10-25.md | a7c6872b… | a7c6872bd9d773313075a3a3755c295572cc0051f7ccc678696b0b638ac7c299 | MATCH (stands) |
| 5 Prior PURSUE-ALL | AUDITOR/FINDINGS_2026-10-26_t0037u_LOCAL_PURSUE_ALL_OPEN_CONFIRM.md | 1306e3db… | 1306e3db0e55b5b63d2bd105b6bf4017f4225d28362abcb1332cc33706bf1203 | MATCH |

## Content checks
- diff backup→STREAM: one appended log line only (tip-pin d88b4dae… → 64d23f39…, tip_touched Local NO, packaging a7c6872b… stands, no Local invent). Tip-pin only.
- Invent: none. tip_touched: NO (tip sha equals expected live LOCK). Packaging: unchanged.

## Soft SF
- SF-1: STREAM appended line also restates Owner t1586u / MR1 ρ(W₇) Author-Write context — narrative beyond pure tip-pin; no premise content, no invent.
- SF-2: Packet cites MR1 pack `ad3829c6…` / R36 `98a09683…`; not in this CONFIRM scope (not recomputed here).
- No tip race observed (tip = 64d23f39… at check time). No packaging invent.

Auditor did not edit the tip; no messages sent.
