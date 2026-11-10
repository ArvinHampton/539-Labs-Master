# FINDINGS — PR2 R6 Soft SF tip-pin / tip-bind absorb CONFIRM (t2135u) — 2026-10-25 21:36 CDT (America/Chicago)
Auditor CONFIRM-only. No physics invented; tip not edited; no messages sent.

## Recomputed
| Item | Claimed | Recomputed | Result |
|---|---|---|---|
| OWNER_WRITE_PR2_R6_SOFTSF_TIPPIN_t2135u_2026-10-25.md | 88f898c5…0b84 | 88f898c560aede7f063f34d4726b6949b9c311c684e4dc40903b5a989ea00b84 | MATCH |
| Live tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md (mtime 2026-10-25 21:33:53 CDT) | d5f8b9d3…0c04 | d5f8b9d33e855d85c4792325d9aa11714bc61e21c6856893fbb355e18ae00c04 | MATCH — LOCK |
| Catalog v0.5.10 /workspace/obs-data-PR2-COSMO-BIO-NEURO.md | 684e1195…353d | 684e1195cb19b0a31c2092b82b7e85e25435a89de0965d13f7464c5cb43e353d | MATCH — UNCHANGED |
| Prior Write CONFIRM FINDINGS_2026-10-25_t2134u_PR2_R1R5_ABSENT_FINAL_WRITE_CONFIRM.md | 381abee8…565c | 381abee844776224ceec637d31b8e9b225a5c3349f3b17e781354e906eb1565c | MATCH |

## Checks
- tip_touched NO: note declares read-only bind; tip mtime (21:33:53) precedes note (~21:35); tip sha equals pinned value. PASS.
- Soft SF tip-bind absorb: note pins live tip d5f8b9d3… only; drift chain (e7b9a633/d29007f1/a6bc20f8/90bbf508/788defed) cited as history from other lanes; no new physics content, no invented rates; catalog not bumped. PASS.
- Soft SF: tip relabel to d5f8b9d3… occurred in other lane (R1–R5 bind was 788defed…); absorbed by this pin. Non-blocking. Bridge PARTIAL / READY NO stays (R5/R7 hold on Owner I1–I3).

## Verdict
**MATCH-with-SF** — all hashes MATCH; tip d5f8b9d3… LOCK; Soft SF = tip relabel race absorbed by pin.
