# FINDINGS — MR1 named gaps G1-mem + G-PATH-A + G-A2 STATUS (Soft SF, write-only) — 2026-10-27 11:23 CDT (America/Chicago)

Tip Soft SF LOCK `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` re-verified, tip_touched **NO**. Kerr BLOCKED. Mesh CANCELLED. NO RECS. No invent. No Owner Write. No CSV edits. Exact-ν stays Owner/Eigen Write-gated; this pack does not close it.

## Cites (full sha256 re-verified this run)
| Item | File | sha256 | Verify |
|---|---|---|---|
| Tip | residual-c-field-WRITTEN_PREMISES_DRAFT.md | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | MATCH |
| OW blanket | grok-batches/OWNER_WRITE_BLANKET_OWNER_PURSUE_WRITE_AUTHORITY_ALL_LANES_2026-10-26.md | 9b993a72bcdfed3fe2d78c15cbe76d0c8197958ca5ac60111546cd5e7ec6498b | MATCH |
| G1-mem rebuild LIVE | FINDINGS_MR1_NAMED_GAPS_G1MEM_REBUILD_LIVE_2026-10-26.md | 3f14f6d8d454efbe30ffe123737824a25eebede6e880531dae85248b9be64b3a | MATCH |
| Named gaps G1+PATH-A | FINDINGS_MR1_NAMED_GAPS_G1MEM_GPATHA_STATUS_2026-10-26.md | 27dd3cc38f9dde89db02a3b96d31fff91790c4f75df680189b35f6be223eddc3 | MATCH |
| Path (a) ABSENT | FINDINGS_MR1_PATH_A_EXACT_RHOBAR_SOFTSF_CORPUS_2026-10-26.md | f0f61da0c5beda8d89f7671b78bac2c96d4386af7e00cd6a4581d3f5447c1b01 | MATCH |
| G-BASIS-89+G-A2 | FINDINGS_MR1_NAMED_GAPS_GBASIS89_GA2_STATUS_2026-10-26.md | 243f9cc504e10879dee57c43755913aa2698e64a6256d340a949e50b628a2adf | MATCH |
| Card1F Step3 | FINDINGS_MR1_NAMED_GAPS_CARD1F_STEP3_STATUS_2026-10-26.md | cf59ba1395dc4b7e520a85627ec28b13550e350932ea8c8705f34e12c6e1e6ad | MATCH |
| ROLLUP POST | FINDINGS_MR1_NAMED_GAPS_OPEN_BOARD_ROLLUP_POST_G4AB_GAPE_2026-10-26.md | da25ef01762b6d8785f6f41aff211e81c76f4852f4f4a1245fc49db986f3ba4f | MATCH |
| Lit deepen (cite only; Gap-E/G4a/G4b/Rec A-1 not reopened) | FINDINGS_MR1_LIT_DEEPEN_GAPE_G4AB_RECA1_HYGIENE_2026-10-27.md | e5b4e69d055cedb5956209b266501b945076a78d69b2a4b006e0666a15d17a41 | MATCH |
| Eigen G1MEM (lineage d768dbd9…) | grok-batches/EIGEN-TE-RHOBAR-N36-G1MEM_2026-10-26.md | d768dbd926715938f952851947680790589892359c31865634abdb7c27fab29d | PRESENT, MATCH |
| Eigen G1MEM ack | grok-batches/EIGEN_ACK_RULE3_G1MEM_ASSIGN_2026-10-26.md | cc18bc0442d390a6f4192dbcbb896e20c2a4e3863327398af158388791f3b6fe | PRESENT |
| Card-1A Owner Write (context, pre-existing) | OWNER_WRITE_TE_RHOBAR_TARGET_SPACE_592_SEED_CARD1A_2026-10-26.md | dede8346d5639ebc9b2667af36728d894c12c7cefc4b2bfac1db6bc866de8c2a | PRESENT (already cited lineage; not new) |
| solve42g progress ROOT30 | grok-batches/EIGEN-TE-RHOBAR-Q89-ZETA49-SOLVE42G-PROGRESS_ROOT30_2026-10-27.md | 77cf385b28f398ddc583cb8800d8d430bdda89527a90bd409ab979fe83451c3f | PRESENT |

## 1. G1-mem: OPEN / GAP STANDS
- The Eigen G1MEM card (d768dbd9…) states GAP. P1 (char-0 rank) is ABSENT. P2 (coordinated Kr plus Q(ζ49) CRT and an exact char-0 polar-part = 0 check) is ABSENT.
- Live read-only check at about 11:22 CDT: `rebuild_e1_extra_then_crt.sh` (PID 2815455) is still waiting. Its log says "wait solve42g for e1 p=7872341" at 11:18, 11:20 and 11:21 CDT. `resume_solve42g_serial.sh` (PID 2816202) is LIVE, and solve42g is cooking root (args 6 1027606441 32). ROOT30 progress: 30/42 roots on disk, all MATCH 89/89.
- No Kr CRT artifact, no Q(ζ49) CRT success artifact, and no char-0 certificate was found (scan of grok-batches/ and quantum-comp/ since 2026-10-26 21:35 CDT). The rebuild is blocked behind solve42g. The COOK pulse from 11:19 CDT agrees: OPEN.
- Not updated to MATCH.

## 2. G-PATH-A: OPEN STANDS
- Path (a) ABSENT (f0f61da0…) and named gaps (27dd3cc3…) re-verified. The disk scan found no new path-(a) exact-ρ̄ identification and no new Card-1A ID artifact. The only Card-1A file is the pre-existing Owner Write dede8346…, which is already in the lineage. The solve42g progress files are G-BASIS-89 compute and do not identify path (a). WRITE_NL_GAP_IA_…PATH_AC is a nonlocal lane and is not a path-(a) ID.

## 3. G-A2: OPEN STANDS
- The pack 243f9cc5… has a₂ = dim M₂ unpinned at 33 ≤ a₂ ≤ 112, and Card1F Step3 (cf59ba13…) is consistent with that. A scan of .md files newer than 21:35 CDT for a pin of the form "a₂ =" / "dim M₂ =" turned up only the prior G-A2/rollup packs and their Auditor mirrors. No new pin was found.

## Board one-liners
- G1-mem: OPEN / GAP STANDS. The rebuild is LIVE but blocked waiting on solve42g (30/42). Kr CRT and the char-0 cert are ABSENT.
- G-PATH-A: OPEN STANDS. No new path-(a) or Card-1A identification is on disk.
- G-A2: OPEN STANDS. a₂ is still unpinned, 33 ≤ a₂ ≤ 112.

ABSENT notes: /workspace/eigen-n36-503/ is absent (the artifacts are under grok-batches/eigen-n36-503/). The Q(ζ49) Kr CRT artifact, the char-0 polar check output, and an a₂ pin are all ABSENT.
