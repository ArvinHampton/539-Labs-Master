# Auditor FINDINGS: NL t177u Soft SF tip-pin rebind to f97d54c9… (CONFIRM-only)
2026-10-26 ~00:49 CDT (America/Chicago). Hashes recomputed with sha256sum. Tip not edited, no messages sent.

## Verdict: MATCH-with-SF
Every NL claim matches except claim 1. The live tip moved after the claim was written, so the tip pin ≠ the live tip.

## Hash checks
1. Live tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md: claimed f97d54c940e878b3d65c3a21b0fa462cee0391cddf04c0a2a5098cbf671d3a85. Recomputed **59491fde5bd60e27ba2379345e7c26762d94e6a7574a85ac6984e1b8fda863f2**. File mtime 2026-10-26 00:49:45 CDT. **MISMATCH. This is a tip race from an outside edit**, made after t177u and the 00:47 LOCK CONFIRM. The NL diff touches only the stub, so the NL claim tip_touched NO still holds for NL.
2. Stub post: 92bbb0823da41d10619bb43b3e073a74a87720781db918842dc9643f67ec8006 MATCH. Backup .pre-softsf-tippin-2c893547.md = 2c893547c7e348aa71def2bde0ed9a9f42f83a0c0da3b9098a8707133c901162 MATCH (prior stub). The diff from backup to post is limited to rows 31–38, the t164u status line and one added t177u log line.
3. NL FINDINGS 3ec9875dca5d93bdb6175ad9e9feba521c62fc9d94164bbda1594882698527ed MATCH.
4. NL ACK a76f4d59d10e386b0ffce5cee490ccc7773933a58e828907d753ccad5c53660d MATCH. The .sha256 sidecars are present.
5. Prior Auditor 7959fdd3b6a9d9f7f4db33ed88f6388d928749182bf6717a6a2060f2a46e7e62 MATCH.
6. Prior Auditor 1fb6751d3012872caaf42f7bee4909d09447adaed2169e218b6c42493f044816 MATCH.

## Content checks
- Rows 31–38 and the t164u status line now point to tip pin f97d54c9…. Pre-pin history 64d23f39… / d88b4dae… / d0b1e301… / d5f8b9d3… is present. MATCH.
- The t170u and t172u log lines are unchanged and kept as history. MATCH.
- t177u line: Soft SF F3 OPEN (not closed), Packaging Owner-hold, Q7 KEEP, cite-only, sealed packs unchanged, Bridge PARTIAL / READY NO. MATCH.

## Soft SF flags
- **SF-1 tip Soft SF race:** the pin f97d54c9… ≠ the live tip 59491fde…, which changed at 00:49:45 CDT after the LOCK. The new tip has no LOCK/CONFIRM yet. NL needs to rebind once the new tip is LOCKed.
- Invent: none. NL tip_touched YES: none found. F3 closed without evidence: none. Packaging beyond Owner-hold: none. Q7 change: none.
