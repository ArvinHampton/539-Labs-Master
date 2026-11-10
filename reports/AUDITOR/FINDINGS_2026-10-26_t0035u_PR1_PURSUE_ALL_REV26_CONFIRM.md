# AUDITOR FINDINGS — PR1 PURSUE-ALL t86u catalog rev. 26 CONFIRM
2026-10-26 ~00:35 CDT America/Chicago. CONFIRM-only; no physics invented; tip not edited; no messages sent.

## Verdict: MATCH-with-SF

## Hashes (sha256sum, live)
| Item | Claimed | Live | Result |
|---|---|---|---|
| Catalog `/workspace/obs-data-PR1-HEPP-QM-GR.md` rev.26 | 1fddb37c289f48cd36bcb19ddabdec8c448907be7e194c018e8395da7cf3b795 | 1fddb37c289f48cd36bcb19ddabdec8c448907be7e194c018e8395da7cf3b795 | MATCH (mtime 00:34:33 CDT) |
| Catalog backup `.pre-pursue-t86u-7690e0a9.md` | 7690e0a9… | 7690e0a93f2f6756a59ee3fa51917e4c5f96290f8b5e5d8df0c888abe8598cb8 | MATCH |
| PR1 FINDINGS `quantum-comp/reports/PR1_PURSUE_ALL_t86u_2026-10-26.md` | cd1725afd9ae872dad0143a1914d3b5b50e3f902cd9b0283d63bee5974926e30 | same | MATCH (mtime 00:34:41 CDT) |
| Prior Soft SF stamp `FINDINGS_2026-10-25_t2204u_PR1_SOFTSF_STAMP_FIX_CONFIRM.md` | 876400fc… | 876400fcebc5333befa5df6a24f15fdc52ff9275bc0bacc1e8674b5c9e6c9e4f | MATCH |
| Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` | d0b1e301…09851 (LOCK) | **d88b4dae527d2eec9f1112427160130fbc12fcd7044bae151a7359efcd4b21d6** | MOVED (mtime 00:35:18 CDT) |
| Tip backup `.pre-1o-park-write-fold-d0b1e301.md` | — | d0b1e3016182eab1522c5fa6b2743e7c8c48d5446d8b0e59b3acfdd61bb09851 | = prior LOCK |

## Tip move
Diff backup→live: only an inserted §1o "MR2 PARK-WRITE Soft SF fold — awaiting Auditor re-CONFIRM" (MR2 writer, base d0b1e301). No PR1 content in the delta. Fold landed ~37 s after PR1 wrote, so PR1's "tip = LOCK d0b1e301, no drift" was true at write time. **tip_touched (by PR1) = NO.**

## Content checks (diff vs 7690e0a9 backup: 3 hunks only — header rev line, §4.1 caveat line 292, changelog rev.26 line 329)
- GW250114 journal refs CLOSED [V]: PRL 135, 111403 (2025) DOI 10.1103/kw5g-d732; companion PRL 136, 041403 (2026) DOI 10.1103/6c61-fm1n. Citations only. Measured rows UNCHANGED. PASS (Auditor did not re-fetch APS; bibliographic only).
- A/B: still CITE-ONLY pending Owner R23. Not promoted. PASS.
- C: ABSENT pending Owner. Not invented. PASS.
- Bridge PARTIAL / READY NO; invent-ban held; no new numbers. PASS.

## Soft SF
1. **Tip race:** catalog rev.26 + PR1 FINDINGS cite tip d0b1e301 (LOCK). Live tip is now d88b4dae (MR2 §1o fold, awaiting Auditor re-CONFIRM). Cites are stale but were not wrong at write time. Fix: re-bind the tip pointer to d88b4dae (or whatever tip results after the §1o re-CONFIRM) in the next PR1 rev.
2. **Timestamp:** changelog rev.26 says "~00:40 CDT", but the catalog mtime is 00:34:33 CDT. Cosmetic.

No hard SF: nothing invented, tip_touched NO, A/B not promoted, C not invented, measured rows unchanged beyond the cites.
