# Auditor FINDINGS — NL t182u Soft SF tip-pin rebind → 59491fde… CONFIRM
Stamp: 2026-10-26 00:54 CDT (America/Chicago). CONFIRM-only; no physics invented; tip not edited; no messages sent.

## Verdict: MATCH-with-SF

## Hashes (sha256sum recomputed)
| # | Item | Claimed | Actual | Result |
|---|---|---|---|---|
| 1 | Tip at NL stamp (FINDINGS t182u before=after) | 59491fde5bd60e27ba2379345e7c26762d94e6a7574a85ac6984e1b8fda863f2 | stated in NL FINDINGS; tip_touched NO | MATCH (cited) |
| 2 | Live tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md | 86e439a8… (post-stamp race) | 86e439a8a3e32ce9c301547902a4ed8f0a49423b16a5feba3d36b68018150ea9 | MATCH — Soft SF tip race (pin 59491fde… ≠ live) |
| 3 | Stub /workspace/obs-bridge-NL-61Omega-photon-brane.md post | 4056f6ea… | 4056f6eaa15b9b650d4cae46d9ae921f99f8b9ca7a0a55b10d93fdc2512999f3 | MATCH |
| 3b | Backup /workspace/obs-bridge-NL-61Omega-photon-brane.pre-softsf-tippin-92bbb082.md (= pre) | 92bbb082… | 92bbb0823da41d10619bb43b3e073a74a87720781db918842dc9643f67ec8006 (sidecar agrees) | MATCH |
| 4 | NL FINDINGS_NL_SOFTSF_TIPPIN_REBIND_t182u_2026-10-26.md | 122aed71… | 122aed71503b9c4533b49e80d9991cc176f4aa1c9fe719351e123b743f1bc3db | MATCH |
| 5 | NL ACK_NL_SOFTSF_TIPPIN_REBIND_t182u_2026-10-26.md | 053cf822… | 053cf8220f7e63ba8a1f39d77d8fc04ed0d3401bb4969cad2db034de9c82494d | MATCH |
| 6 | Prior Soft SF R37 CONFIRM (t0050u) | 572d76d9… | 572d76d92f421dfe97fb93d955829da8065eacd0091158ee6aab6c9c260d2782 | MATCH |
| 7 | Prior NL tip pin CONFIRM (t0049u) | a1bd94cd… | a1bd94cd5d519da03847c22ad8b99be7a69be35cb7c3e85e416669bc8b87d336 | MATCH |

## Content checks (diff backup → live stub)
- Diff confined to rows 31–38, t164u status line (L76), and appended t182u log line: pin f97d54c9… → 59491fde… with pre-pin history f97d54c9… / 64d23f39… / d88b4dae… / d0b1e301… / d5f8b9d3…. PASS
- t170u/t172u/t177u log lines unchanged (history). PASS
- Soft SF F3 OPEN; packaging Owner-hold; Q7 KEEP; STOPPED KEEP; cite-only; sealed packs unchanged; Bridge PARTIAL / READY NO. PASS

## Soft SF flags
- Invent: NO
- tip_touched YES (NL): NO
- tip Soft SF race: YES — NL pin 59491fde… ≠ live tip 86e439a8… (post-stamp, expected per Soft SF R38 F3 APPLY; not an NL fault; next rebind needed)
- Soft SF F3 closed: NO (stays OPEN in stub)
- Packaging beyond Owner-hold: NO
- Q7 change: NO
