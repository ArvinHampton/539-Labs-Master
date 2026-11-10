# FINDINGS — MR1 Blanket: Rec A-1 stamp (N36 ν=21,25) + exact-ν CERT Alt B 7/7 packaging (2026-10-26 ~21:20 CDT America/Chicago)

## STATUS: **MATCH** — both Soft SF Writes done; no residue/coefficient_modp changed; tip_touched NO.

Authority: OW blanket 9b993a72b… (verified); MR1 ACK Soft SF 6132c467…. Rec A-1 from FINDINGS_MR1_COOK_RESUME_MATHLIT_G1_N36N6_PACKAGING sha 6ed0fc314c63… (verified) + OW basis-ID confirm 4103ea927c99… item 1 (verified).
CERT sources (verified): Alt B FINDINGS fa47db06e268…46b32; CRT_LIFT_SCALED70_CF980.csv 338c9a12cbac…8aaf; WRITTEN_CHOICES_MR1_CF980_ALT_B_V42 255b5a1079cf…5de8.

## Tip LOCK
residual-c-field-WRITTEN_PREMISES_DRAFT.md sha = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (expected 7cddb188…dfc91) → **tip_touched NO**.

## Pre/post shas
| file | pre | post |
|---|---|---|
| TE-SIMPSON-FILL-MODP_N18_2026-10-26.csv | 38534aa1102da03cf96d7d76cdd454f8ef0530c4ef12439ec0cbf3c4346010f3 | dbc71a0ccb5dd3972bbb22a7549a73244e33c8d390823c22503086fbb2587538 |
| TE-SIMPSON-FILL-SCHEDULE_TORD_N18_2026-10-26.csv | 4de5113b477836c6347d33d7142d4dfcdfd001fbb1b32085b62f5b2fabb6976e | 94fa21376fb0f728b991b500c9ab57bec6123af5eae25b606e6599adfaff0158 |
| TE-SIMPSON-FILL-MODP-N36_N18_2026-10-26.csv | 0e17098c61b5ee7823dad690fa998389a84e504055e599ca31c36a423deacbf2 | unchanged (w1_sha/basis_sha for ν=21,25 already full ee9c36f9…/e707cc96…, not NA-HOLD) |
| NEW TE-SIMPSON-FILL-EXACT-ALTB_N18_2026-10-26.csv | — | ad32226631e88c230234f2b24b32cf05ae40c84ddd90d3407b4d6e63776cc65f |
Backups: /workspace/grok-batches/backup_pre_edit/*.pre_blanket_recA1_altb (+ sidecars). All .sha256 sidecars rewritten.

## Edits (complete list)
Task 1 (Rec A-1), MODP CSV: N36 ν=21,25 notes += "Rec A-1 stamp: basis sha e707cc96; W1 sha ee9c36f9 (…)"; source_cols normalized to "seed comp 28 e21/140" / "seed comp 25 e25/140" (comp/exponent equal: 3/20=21/140, 5/28=25/140). Status FILLED-MODP and HOLD CF980 kept. SCHEDULE: same stamp appended to coefficient field for ν=21,25.
Task 2 (Alt B 7/7), MODP + SCHEDULE: status FILLED-MODP → CERT-under-H_work (existing house label) for N36 ν=1,4,9,14,16 and N6 ν=1,9 only; note appended "EXACT-ALTB: … Alt B redefinition cell, NOT Card-1A/Eigen identity; path (a) OPEN … fa47db06 + 338c9a12 + 255b5a10; coords in TE-SIMPSON-FILL-EXACT-ALTB_N18…; MODP residues unchanged". coefficient_modp columns untouched (mod-p only).
Companion CSV: one row per cell with D_clear, nz count, max|70c|, pointer to CRT lift rows (N36 ν=1,9: c=0, no rows), matching Alt B FINDINGS table (nz 0/20/0/21/17/23/23; heights 0/6/0/5/8/24/24).
Not done (by brief): no exact ν=21,25; N6 ν=29,81,109,121 unchanged.

## Gaps left open (named)
- path (a): Alt B cells NOT identified with Card-1A/Eigen cells.
- G1-mem Eigen-side GAP open (Rec A-2 not started).
- G-EXACT: CERT rests on CRT + p4 check (direct CF(140) run unfinished), per Alt B FINDINGS.
- Kerr BLOCKED; no ρ̄ invented; no tip-fold; no RECS.
