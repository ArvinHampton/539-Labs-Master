# FINDINGS — MR1 fill-first N36 after Eigen Written map (2026-10-26)

STATUS: **PARTIAL** (N6 filled; N36 ABSENT per Written map; exact char-0 still OPEN)

## Authority
- Eigen map MATCH: `67a5a6a3aecf468fbcf8000b1d3295daf4dd64a1769b703b9b8e34abcbd4b14d` (EIGEN-TE-RHOBAR-N36-TORD-CSV-MAP_2026-10-26.md) — verified
- CLOSED_A `3242e26ef3b79795d89953593ce7b6676e119f8a2e8d6a324da8ae1fe741042a`
- MR1 ASSIGN `3df683d210e6232446995bac6114a73e443900d0ec1ff654b1f4d37914a4a769`
- Eigen map ASSIGN `c471c8326e77186f8e1089d9e62d77a3fde7dc1ef0e1502dc9b39cc82bf4b442`
- Prior MODP_CELLS PARTIAL `3dce9e1f6a2d69e249c2bf5cd79e988150b729cf4d02e71be89ca3e5d3e13656`

## Tip Soft SF
`residual-c-field-WRITTEN_PREMISES_DRAFT.md` start = end = `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91`; tip_touched NO.

## Invent HOLD
No 503-basis invented. No N6 columns (`a0_*_e1/140`, `a1_*_e9/140`) used for N36. No scaling/width/Ind rewrite invented.

## Cell table (p=1027606441)
| family | ν | status | coefficient |
|---|---|---|---|
| N36 | 0 | VACUOUS | VACUOUS |
| N36 | 1 | ABSENT-WRONG-PIECE (OPEN) | OPEN / ABSENT-WRONG-PIECE (map §4) |
| N36 | 4 | ABSENT-NO-503-BASIS (OPEN) | OPEN |
| N36 | 9 | ABSENT-WRONG-PIECE (OPEN) | OPEN / ABSENT-WRONG-PIECE (map §4) |
| N36 | 14 | ABSENT-NO-503-BASIS (OPEN) | OPEN |
| N36 | 16 | ABSENT-NO-503-BASIS (OPEN) | OPEN |
| N36 | 21, 25 | OPEN-OFF-MESH | OPEN (unchanged) |
| N6 | 1 | FILLED-MODP (preserved) | a0_c0_e1/140, nz=1/89 |
| N6 | 9 | FILLED-MODP (preserved) | a1_c0_e9/140, nz=89/89 |
| N6 | 29, 81, 109, 121 | OPEN-OFF-MESH | OPEN (unchanged) |

Counts: VACUOUS 1; ABSENT-WRONG-PIECE 2; ABSENT-NO-503-BASIS 3; FILLED-MODP 2; OPEN-OFF-MESH 6 (total 14).

Map cited: sha `67a5a6a3…4b14d`. The RHOS 89-CSV is the N6-piece image only; not a basis for the 503-dim N36 piece.
Eigen owns the exact char-0 lift of the 89/N6 basis under CLOSED_A `3cf5735c…` (path (b) CRT); untouched here.

## Updated artifacts
- grok-batches/TE-SIMPSON-FILL-SCHEDULE_TORD_N18_2026-10-26.csv (+ .sha256)
- grok-batches/TE-SIMPSON-FILL-MODP_N18_2026-10-26.csv (+ .sha256)

## RECOMMEND-FIRST (needed — 503 gap)
- **A (recommended):** Authorize Eigen (or Owner Write) to construct / ship an explicit 503-piece (N36) mod-p basis through q^18 so MR1 can fill N36 ν=1,4,9,14,16 FILLED-MODP cite-only.
- B: Leave N36 ABSENT; no 503 authorize.
- C: Other / Owner specify.
