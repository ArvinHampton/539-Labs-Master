# AUDITOR FINDINGS — PR1 Soft SF tip-pin 788defed CONFIRM (t2135u)
Date: 2026-10-25 ~21:40 CDT (America/Chicago). Mode: CONFIRM-only. No physics invented, no tip edit, no messages sent.

## Verdict: MATCH-with-SF (non-blocking)

## Checks
| Item | Claimed | Recomputed | Result |
|---|---|---|---|
| Catalog rev.22 `/workspace/obs-data-PR1-HEPP-QM-GR.md` | c22a46ff… | c22a46ff55a5ddaef826b8ab9656d35bfdeb7b4794db60230616fdbc9840cee1 | MATCH |
| Base `obs-data-PR1-HEPP-QM-GR.pre-tippin-788defed-36700ecb.md` | 36700ecb… | 36700ecb565d5b8f49bebad7d0d62d7470ccb27a27b78202f09641a4ac507ebb | MATCH |
| Diff base→rev.22 | live cites only + changelog | 6 lines changed (header rev list; Post-LOCK pointer; Item-4 W4 parenthetical; Footer rev.14; Footer; footer LOCK bullet) + rev.22 changelog line added; 90bbf508→788defed in live cites | MATCH |
| History lines (rev.12/16/20/21/post-wave-4 Soft SF) | untouched | not in diff | MATCH |
| tip_touched | NO | Catalog only cites tip; PR1 diff has no tip write. Tip mtime 21:33:53 CDT is an MR2 §1m relabel (another lane) | MATCH |
| Live tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` | d5f8b9d3… (LOCK) | d5f8b9d33e855d85c4792325d9aa11714bc61e21c6856893fbb355e18ae00c04 | MATCH (tip LOCK) |
| Catalog live cites vs tip | 788defed | 788defed ×7 hits; d5f8b9d3 ×0 | LAG (SF-1) |

## Soft findings
- **SF-1 (Soft SF tip race):** the tip moved to d5f8b9d3… at 21:33:53 CDT, 11 s before the catalog write at 21:34:04 CDT. Live cites still point at 788defed…, which is now one tip behind. This does not block: history is untouched, tip_touched is NO, the LOCK_DIGEST 964294cc… is kept, and a rebind is pending. To fix it, rebind only the 6 live-cite lines 788defed→d5f8b9d3 and keep 788defed as prior/superseded. Wait for the hygiene re-CONFIRM of d5f8 first.
- **SF-2:** the rev.22 changelog cites R8 APPROVED and §1m re-CONFIRM 3b01ef79…. 3b01ef79 matches HASH_INTEGRITY. The R8 Owner approval was not verified by the Auditor.

Bridge PARTIAL / READY NO / not Cat A. invent-ban ON.
