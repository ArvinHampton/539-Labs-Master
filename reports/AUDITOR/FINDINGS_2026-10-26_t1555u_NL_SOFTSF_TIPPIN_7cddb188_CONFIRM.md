# FINDINGS: Auditor CONFIRM, NL tip re-pin t229u (Physicist loop-break) onto live tip LOCK 7cddb188

- Date: 2026-10-26 ~16:00 CDT (America/Chicago)
- Mode: write-only CONFIRM. No tip fold, no tip re-pin, tip not edited.

## Verdict: MATCH-with-SF

## Hashes (recomputed on disk)
| Item | Claimed | Disk | Result |
|---|---|---|---|
| Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` (start = end, mtime 2026-10-26 10:31:22 CDT) | 7cddb188… | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | MATCH |
| Stub `/workspace/obs-bridge-NL-61Omega-photon-brane.md` (mtime 13:40:47 CDT) | POST dc17b39b… | dc17b39b55f23baa7af198b58ad17642f49a42f2e29f55c8467a74f075c9839b | MATCH |
| Stub backup `.pre-softsf-tippin-9c5a947b.md` | PRE 9c5a947b… | 9c5a947b8028a291a65c3f16f8257f5410e89db662882184d9148507fb600035 | MATCH |
| Auditor tip LOCK FINDINGS (P5a) t1034u | f4671188… | f4671188791c7c4cb164b6ac60211eda2d7281e7337a6cd9cba65e8b1c072c20 (sidecar agrees) | MATCH |
| NL FINDINGS t229u | (n/a) | 124a3cd3abd4e377a644a52496b67420e5acfceb19facbcac1c2a9770f724200 | recorded |

## Checks
1. Tip sha 7cddb188 unchanged vs LOCK; mtime predates the t229u edit (10:31 vs 13:40 CDT). tip_touched NO.
2. NL FINDINGS cites (tip live, tip_pre ea4eb298, stub PRE/POST, backup, P5a f4671188) all match disk.
3. diff PRE→POST: rows 31–38 and t164u status line swap active pin ea4eb298 → 7cddb188 with ea4eb298 moved into pre-pin history; one appended t229u log line; one wording change in the t222u log line. No physics content changed. Cite-only stub pin confirmed; tip not modified.
4. Status carried in stub and NL FINDINGS: invent HOLD tip fill else; F3 CLOSED; Bridge PARTIAL / READY NO. Card4: not stated in NL FINDINGS or stub; no Card4 status asserted here.

## SF flags (packaging only)
- SF-1: the t222u historical log line was edited in place ("Components HOLD (Owner Park)" → "Components tip-era open/B-HOLD"). Declared in NL FINDINGS Edit item 2, but it rewrites a history line rather than only appending. Not a verdict change.
- SF-2: Card4 status not stated; left unasserted.
- SF-3: NL FINDINGS does not record its own sha256 sidecar; disk value recorded above.

No physics invented; no verdicts altered.
