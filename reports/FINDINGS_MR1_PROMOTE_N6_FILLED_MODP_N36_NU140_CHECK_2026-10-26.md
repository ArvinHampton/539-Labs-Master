# FINDINGS — MR1 Promote N6 FILLED-MODP + N36 ν=/140 check (Rec A AUTO) — 2026-10-26
Soft-SF Write-only. tip_touched NO. Eigen contact NONE. Cat-A invent NONE. CERT NOT claimed.

## Authority (verified live sha256 at start)
- OW 10791f24497f65c7c8fb57c3623a2a396ffb9068e41898b27f4c4165f6851b3b ✓
- ASSIGN 9db9c8e68effa605c2dd57707e531043a403c82fc3a918fc11d236894fbf4fc5 ✓
- FINDINGS N6 D1 c2deddc5dbc2ce15ea464c238583536febde24af5acd9ef60eb988b726025a7b ✓
- N6_D1_nu_columns_modp.csv 9b9b73c04564f257bc2a7da9a57efb696e69e550e2a66a4da842ba9cacb26429 ✓
- tip_pre = tip_end = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (identical)

## Operative CSVs
| file | before | after |
|---|---|---|
| TE-SIMPSON-FILL-SCHEDULE_TORD_N18 | d3f12c981ec72b901ae7e97b76ac4a70c9cdd356ddda2eb5a721453d656f56f9 | 8423cb32dce8e5976a60a31a64683443b7021afb8676e9d83c9eee8a72c65c20 |
| TE-SIMPSON-FILL-MODP_N18 | 9df646a935931fb70a523edf4e52190bbb08381fd24b51d8c4441873d827ccf3 | 533217dbbf7821760a7d38294bc820c68419464fd187104e158392e4dda00636 |
Sidecars `.sha256` refreshed. TE-SIMPSON-FILL-MODP-N36_N18 is N36-only → untouched.

## 1–2. N6 promotion (p=1027606441, on_mesh_N18=YES corrected from NO(>18), w=4, tier 1-odd-w4, status FILLED-MODP, HOLD CF980)
| ν | source_col | nz | first |
|---|---|---|---|
| 29 | a2_c0_e29/140 | 89/89 | 0:225650609;1:522387538;2:367160988 |
| 81 | a3_c0_e81/140 | 89/89 | 0:200307986;1:78319815;2:139970354 |
| 109 | a4_c0_e109/140 | 89/89 | 0:6839830;1:583863915;2:778245974 |
| 121 | a5_c0_e121/140 | 89/89 | 0:754394536;1:881713098;2:82808653 |
Copied verbatim from the D1 artifact (full vectors there). Notes stamp HOLD + OW/artifact/FINDINGS shas. Schedule rows mirror with pointer to mod-p CSV. No OPEN-OFF-MESH remains for N6.

## 3. N36 ν=21,25 check — MATCH (candidates only, NOT written to operative CSVs)
Proof: the 503-block basis CSV `eigen-n36-503/n36_basis_q18_inf_modp.csv` (sha e707cc96…) has 36 components × 18 columns labelled cA_e{x} (reduced fractions). Leading exponents×140 of the 36 seed components are
[1,4,9,14,16,21,25,29,30,36,44,46,49,50,56,60,64,65,70,74,81,84,85,86,100,105,106,109,114,116,120,121,126,130,134,140].
Exactly one column equals 21/140=3/20 (`c28_e3/20`, component 28) and exactly one equals 25/140=5/28 (`c25_e5/28`, component 25) — the same unique-match criterion asserted in export36.sage.
Method validation: extracting columns c31_e1/140, c9_e1/35, c34_e9/140, c20_e1/10, c6_e4/35 from the basis CSV reproduces all 5 existing rows of n36_mr1_nu_rows_modp.csv (5e3c3155…) byte-exact.
Candidates (p=7840981, MODP-D1 candidate, HOLD):
- ν=21: comp 28, `c28_e3/20`, nz=40/503, first=0:1960245;1:2940368;3:4900613
- ν=25: comp 25, `c25_e5/28`, nz=1/503, first=446:1
Artifact: `mr1-n6-modp-q121-d1/N36_NU21_25_CANDIDATE_cols_modp_NOT_OPERATIVE.csv` sha 56e9be7d1ae06d7e35473ce17aaca85234c65b05ca8e837adc9ffd33f95b44f9.
N36 21,25 rows in operative CSVs left OPEN-OFF-MESH unchanged (promotion needs separate Owner Write). Char-0 not claimed (QQ lift m7_crt2 is NOTCERT).

## 4. Global HOLD
All 11 FILLED-MODP rows (prior 7 + 4 new) HELD for CF980 CERT. G4a/G1 OPEN. Kerr BLOCKED. No CF980 more-primes work started.

## STATUS
N6 promote: MATCH. N36 ν=/140 check: MATCH (columns exist; candidates on disk). Overall STATUS: MATCH.

## Rec A next
Owner Write to promote N36 ν=21 (comp 28) and ν=25 (comp 25) to FILLED-MODP @p=7840981 under HOLD from the candidate artifact; relabel on_mesh_N18=YES, w=4 (odd ν, tier 1-odd-w4).
