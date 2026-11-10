# FINDINGS — MR1 fill-first N36 mod-p Simpson/4Q cells (2026-10-26)

**STATUS: MATCH-MODP** — all five on-mesh N36 cells (ν=1,4,9,14,16) FILLED-MODP (p=7840981). No on-mesh cell left open.

## Authority (verified before writing)
- CLOSED_B owner card: 80ae4f5b53da8403c3d42cb401a484332aa444b7468f4e611d80f27ba95b92ac (both copies)
- ASSIGN MR1: 51f614de1772e403be39979faa3cc954083bceef490cbcb7707bd9b7aa00faec
- W1 seeds FINDINGS (MATCH mod p): ee9c36f9e5a23f3147bdbd104a4ba648cf8e9e2f3f22c750c0d143459364da96
- Rows: eigen-n36-503/n36_mr1_nu_rows_modp.csv 5e3c31555832444dcd6f90d96e0e75ab5df0f090cb47a81675eefa8140e900ba
- Basis cite: eigen-n36-503/n36_basis_q18_inf_modp.csv e707cc96b0cf9c40d671a78c164bcdff5e4f7f81915bc47782e3a909c74f984c
- Tip Soft SF LOCK: start = end = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91; **tip_touched: NO**

## Invent HOLD
FILLED-MODP only (cite-only from W1 rows CSV). Exact / char-0: **OPEN** (CRT not authorized by CLOSED_B). 89-CSV / N6 RHOS not used for N36.

## Cells
| fam | ν | status | p | seed comp | nz (of 503) | first coeffs |
|---|---|---|---|---|---|---|
| N36 | 0 | VACUOUS | – | – | – | – |
| N36 | 1 | FILLED-MODP | 7840981 | 31 | 338 | 18:7350919 19:4900613 20:7350920 |
| N36 | 4 | FILLED-MODP | 7840981 | 9 | 1 | 162:1 |
| N36 | 9 | FILLED-MODP | 7840981 | 34 | 327 | 18:980125 19:6860859 20:3920490 |
| N36 | 14 | FILLED-MODP | 7840981 | 20 | 1 | 360:1 |
| N36 | 16 | FILLED-MODP | 7840981 | 6 | 1 | 108:1 |
| N36 | 21,25 | OPEN-OFF-MESH | – | – | – | – |
| N6 | 1 | FILLED-MODP (unchanged) | 1027606441 | a0_c0_e1/140 | 1/89 | 0:1 |
| N6 | 9 | FILLED-MODP (unchanged) | 1027606441 | a1_c0_e9/140 | 89/89 | 0:854531552 … |
| N6 | 29,81,109,121 | OPEN-OFF-MESH | – | – | – | – |

Counts: FILLED-MODP 7 (N6 2 + N36 5); VACUOUS 1; OPEN-OFF-MESH 6 (N36 2 + N6 4); exact/char-0 OPEN on all 7 filled cells.

## Outputs (sha256)
- TE-SIMPSON-FILL-SCHEDULE_TORD_N18_2026-10-26.csv: 3460f2a5… → d3f12c981ec72b901ae7e97b76ac4a70c9cdd356ddda2eb5a721453d656f56f9
- TE-SIMPSON-FILL-MODP_N18_2026-10-26.csv: 583e3aff… → 9df646a935931fb70a523edf4e52190bbb08381fd24b51d8c4441873d827ccf3
- TE-SIMPSON-FILL-MODP-N36_N18_2026-10-26.csv (new): 20c93d258f070bc5deefb8fcf26e869010332afc56884e3808a26d46b3619fa3
- Backups .pre-n36-modp-closedb.bak: schedule 3460f2a598f435a5a0d44f05c6aec01b844f40861c80c9336b8d19daf839ddb0; modp 583e3aff32d807f30ac03200ff55cf5ea3178776ff237d56d5dfefd9242da419
- Sidecars .sha256 refreshed for the three CSVs.

## Soft SF
Soft SF → Auditor Write-only; no tip fold.
