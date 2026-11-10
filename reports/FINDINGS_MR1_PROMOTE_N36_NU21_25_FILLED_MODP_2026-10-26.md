# FINDINGS — MR1 PROMOTE N36 ν=21,25 → FILLED-MODP (Rec A AUTO) — 2026-10-26
Mode: Soft-SF Write-only. Proof standard. Cat-A invent: NONE. Char-0: NOT invented. No Eigen contact. CF980 runner: not touched.

## Authority (live sha256 verified at start — all MATCH)
- OWNER_WRITE fe16077f09d135ffd0cf480b703624de0a63a2c4b0aad1f81605c27bf1d2407e
- ASSIGN 6ec4c9bec0d4db255cefd680681c22d7686eb595fac4e166e6f4933aab6abfc7
- Source FINDINGS 27b1c5e82aa8d3720767cd1eb4296aeb3eef93cbd434287e16ad3c821b797460
- Candidate 56e9be7d1ae06d7e35473ce17aaca85234c65b05ca8e837adc9ffd33f95b44f9
- tip_pre 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91
- tip_end 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91  (tip_touched NO)

## Per-ν (from candidate, p=7840981)
| ν | comp | source_cols | nz | first3 | weight/tier |
|---|---|---|---|---|---|
| 21 | 28 | c28_e3/20 | 40/503 | 0:1960245;1:2940368;3:4900613 | 4 / 1-odd-w4 |
| 25 | 25 | c25_e5/28 | 1/503 | 446:1 | 4 / 1-odd-w4 |
on_mesh_N18: NO(>18) → YES. status: OPEN-OFF-MESH → FILLED-MODP.

## CSV sha256 before → after
- TE-SIMPSON-FILL-MODP_N18: 533217dbbf7821760a7d38294bc820c68419464fd187104e158392e4dda00636 → 453d3c4fc1607465ec37d67c9c13a4963256eaa84fddacee7637508ad3e6ecfd
- TE-SIMPSON-FILL-SCHEDULE_TORD_N18: 8423cb32dce8e5976a60a31a64683443b7021afb8676e9d83c9eee8a72c65c20 → f7ec76eff6b8888039e65cac8babaecd47285699fedca6577ca20df3ca2a6ea5
- TE-SIMPSON-FILL-MODP-N36_N18: 20c93d258f070bc5deefb8fcf26e869010332afc56884e3808a26d46b3619fa3 → 24fc6122187d67de956aa4aef8abeb57850dbfed5b67ea2a80e5d394a5ef9289 (rows appended; source_rows_sha=candidate; w1_sha/basis_sha = NA-HOLD, not invented)
.sha256 sidecars refreshed for all three.

## STATUS
STATUS MATCH — ν=21 and ν=25 both written consistently across MODP, SCHEDULE, MODP-N36.
Global HOLD: all FILLED-MODP HELD for CF980 CERT-under-H_work. G1/G4a OPEN. Kerr BLOCKED. No Eigen.

## Rec A
Rec A-1: candidate exponent denominators (/20, /28) differ from existing /140 convention of N36 rows; and W1/basis sha for ν=21,25 not attested in candidate — owner to confirm 503-basis identity (e707cc96?) before CF980 CERT lift.
