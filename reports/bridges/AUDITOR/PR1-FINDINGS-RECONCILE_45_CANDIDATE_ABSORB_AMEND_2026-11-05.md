# PR1 FINDINGS — Reconcile "45-candidate" vs ABSORB 0a4ddb32… / AMEND c5755654… (72 tags) — 2026-11-05
REPORTS ONLY. Soft SF. invent HOLD. No CERT. No RECS. No §6 body. Kerr BLOCKED. Documentary comparison only; PROVABLE-CANDIDATE ≠ proved. Tip LOCK 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 tip_touched NO.
Authority: Physicist bounded named gap under Owner position16394. Cites (not rewritten) prior PR1 named-gaps Soft SF e2ffbeba8b4aca8af93c620f46c628e85ce46d79ccc59124d83a0b26358333fb.

## HEADLINE
- Independent enumerated 45-member list on disk: **ABSENT**. "45" appears only as an asserted count (e.g. PAPER_S2 §6 / OW 53991ebf physics-paper prose "Of the 72 items, 45 …"), never with 45 enumerated IDs.
- ABSORB 0a4ddb32… is a **6-item PP FLAG absorb** (IDs 32, 53, 57, 59, 63, 69), **not** a 45-row candidate table.
- PROVABLE-CANDIDATE-bearing rows (machine parse of bold tags, §A from 953be83a… + §B from AMEND c5755654…): **46 pre-ABSORB** (§A 19 + §B 27); **47 post-ABSORB** (item 57 gains a PROVABLE-CANDIDATE subclaim). Neither equals 45.
- **Matched to a 45-list row: 0 (none — no 45-list rows exist).** **Unmatched-to-45-list: all 47** (below).
- Independently reproduces PR2 FINDINGS bb329b4f2a3fa0ebbfaf7e3b0e05bfbc1af909b47eabf97bc5e7f0f295d038af count (46/47); cite-only.

## Unmatched-to-45-list (post-ABSORB PROVABLE-CANDIDATE-bearing, 47)
§A (19): 1, 2, 3, 4, 7, 8, 10, 11, 12, 13, 15, 16, 20, 21, 24, 25, 27, 28, 29
§B (28 post-ABSORB): 32, 34, 36, 37, 38, 39, 40, 41, 43, 44, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 64, 66, 70
Mixed/conditional (candidate tag co-occurs with another tag or qualifier): 2, 3, 7, 15, 20, 21, 25, 57 (+ALREADY-ON-RECORD); 10, 11, 29 (+NEEDS-DEFINITION); 66, 70 (+NOT-MATH sub-reading); 24, 27 (conditional/finite-only in text). Pure-only-PROVABLE-CANDIDATE: 47 − 13 tagged-mixed = 34 by tag-set (24/27 qualifiers in prose only).
Identification rule tried: "45 = count of PROVABLE-CANDIDATE-bearing rows". Fails (46/47). No sub-rule selecting 45 is stated in any source; choosing one (e.g. dropping mixed rows) would invent a list → not done.

## Irreducible missing inputs
M1. Any artifact enumerating the 45 IDs (or the rule that yields 45 from 72). ABSENT on disk (searched reports/, bridges/, *45*, ABSORB*, "45 provable/candidate").
M2. Provenance of "45" in OW 53991ebf PHYSICS_PAPER / PAPER_S2 §6 line ~71 (count asserted, unsourced to IDs).

## ABSORB rewritten IDs (post tags)
32 PROVABLE-CANDIDATE (+conflict note) · 53 PROVABLE-CANDIDATE (no CERT of cocycle) · 57 ALREADY-ON-RECORD (odd-s bound, LEDGER v6 e14) + PROVABLE-CANDIDATE (d_cusp=0 at s=6,8,10) · 59 ALREADY-ON-RECORD (bounded 12≤s≤46 for s≡4,6 mod 8) · 63 NEEDS-DEFINITION · 69 NEEDS-DEFINITION.

## Full 72 tag inventory (post-ABSORB)
PC=PROVABLE-CANDIDATE AOR=ALREADY-ON-RECORD ND=NEEDS-DEFINITION NM=NOT-MATH
1 PC|2 AOR+PC|3 AOR+PC|4 PC|5 AOR+ND|6 ND|7 AOR+PC|8 PC|9 AOR|10 ND+PC|11 ND+PC|12 PC|13 PC|14 ND|15 AOR+PC|16 PC|17 AOR+ND|18 ND|19 ND|20 AOR+PC|21 AOR+PC|22 ND|23 ND|24 PC|25 AOR+PC|26 NM|27 PC|28 PC|29 ND+PC|30 NM
31 AOR|32 PC|33 AOR+ND|34 PC|35 AOR|36 PC|37 PC|38 PC|39 PC|40 PC|41 PC|42 AOR|43 PC|44 PC|45 AOR|46 PC|47 PC|48 PC|49 AOR|50 PC|51 PC|52 PC|53 PC|54 PC|55 PC|56 PC|57 AOR+PC|58 PC|59 AOR|60 PC|61 PC|62 PC|63 ND|64 PC|65 ND|66 NM+PC|67 ND|68 ND|69 ND|70 NM+PC|71 ND|72 ND+NM
(Item 70 separately PROVED Tier P per Haar FINDINGS 7ab0ed68… — cite only; filter tag remains PC.)

## Resonant mis-cite (63fa5d9f42b02950343f6b0882c8d2ac3332b142b0c768c4427ae81bf8dd4b89)
Line 14/120 cite "45 provable candidates | ABSORB 0a4ddb32…" and state ABSORB "not located on disk". Live: ABSORB IS on disk (sha MATCH) and contains 6 items, not 45. Its "27 PROVABLE-CANDIDATE in §B" = pre-ABSORB §B count (MATCH); post-ABSORB §B = 28. Mis-cite documented; file not edited.

## Sources (live sha256)
ABSORB 0a4ddb32f7f891b93c0db120de21638d3e5a30543eca0a9f59116866751ca570 MATCH · AMEND c57556545032be55772a96e0886d35cb8ed33e16f6ce375c23c6363a691301c9 MATCH · §A reports/FINDINGS_LOCAL_SOFTSF_FILTERED_PROVABLE_MATH_X_GROK_COSMIC_JOURNEY_2026-11-05.md 953be83a7e8031c41175fc4182ba89f0913b3755bfcf38d17449142759b024f9 FOUND/MATCH · Resonant 63fa5d9f… MATCH · PR2 72FILTER bb329b4f… (cite).

## Scope boundary
Documentary count/ID comparison only (within PR1 prerequisite lane). No filter items proved, no bridges, no 45-list invented. Reconciliation to a specific 45 set requires M1 → outside lane until supplied.
Tip BEFORE 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91.
