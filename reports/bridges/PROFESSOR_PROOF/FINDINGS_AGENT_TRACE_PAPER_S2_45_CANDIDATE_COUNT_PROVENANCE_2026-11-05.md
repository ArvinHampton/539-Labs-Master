# FINDINGS — Agent Soft SF — Trace PAPER_S2 "45 of 72" candidate-count provenance — 2026-11-05

## Authority
Physicist Soft SF relay; Owner position16394 in-scope; ALL_RECOMMENDED 865d3a37f1c13431c78672847dcd33007b3467df92f1e7c8602057f257b1bf3b in-scope. Gap source: PR1 FINDINGS `reports/PR1-FINDINGS-RECONCILE_45_CANDIDATE_ABSORB_AMEND_2026-11-05.md` sha 83cdf23d645b49118980c9ddb9285d0eb804b014318c7e867af0a9794906963f — rehash MATCH. Cited, not rewritten: PR1 M1 = 45-ID list / rule ABSENT; M2 = provenance of paper "45" (asserted, unsourced to IDs).

## Tip
`/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` BEFORE 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 / AFTER 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91. tip_touched NO.

## FYI absorb — stale /workspace/reports/ floor fix
`/workspace/reports/PAPER_S2_…_2026-11-05.md` = bd39eb4ce49fdf92dcd77ab0db9c518913f2e1e9aa0c5a844cdb44824cc21cf6 MATCH; `/workspace/reports/PAPER_S2_…_CITATION_PINS_2026-11-05.md` = 0009e7356d91b6da2c3b1cfe7c4713de1df91f4cc7632835e90d4711555d18cf MATCH; both equal bridges/AUDITOR copies. Addendum ledger `/workspace/audit-scratch/ternary-floor-correction-20261105/addendum-workspace-reports/ledger.json` records predecessor e140947e… → bd39eb4c… and → 0009e735…. Not re-edited.

## Method + search bounds
- Rehash of all chain files (below); rg for `\b45\b` in papers; rg -l phrases "45 of 72|45/72|45 provable|45 candidates|45 PROVABLE" over quantum-comp/reports, quantum-comp/bridges, /workspace/reports (max-depth 3); filename scan *45*/*FILTER*/*ABSORB*/*72*; pdftotext of RTA v16.
- Recount: python parse of PP audit §2 per-item table (72 rows, Tag column), primary tag = first listed tag; also "any mention" count. ABSORB six-item overrides applied for post-ABSORB.
- Stopped when list exhausted. Derived reproduction in `reports/agent_45_provenance_work/`.

## Exact paper quotes (bridges/AUDITOR; same in /workspace/reports)
PAPER bd39eb4c…:
- L71: "Of the 72 items, 45 are classed as provable candidates. … it does not mean that all 45 have been proved, and the remaining 27 are not provable in their current form." (cites [1])
- L73: "The Haar identity of Section 5 is one of the 45."
- L101: "…and a filtered inventory in which 45 of 72 claims are well-posed provable candidates."
CITATION_PINS 0009e735…: L71/L73/L101 same with [11]; L127 "[11] … Working inventory of 72 items with 45 classed as provable candidates; distinct from the Foundation Bound, version 16 [1]."
Note: "remaining 27 are not provable" is an over-reading — the 27 include ALREADY-ON-RECORD items and dual-tagged PROVABLE-CANDIDATE subclaims.

## Filter chain (rehash, all MATCH)
| Doc | sha256 |
|---|---|
| §A FINDINGS_LOCAL_SOFTSF_FILTERED_PROVABLE_MATH_X_GROK_COSMIC_JOURNEY | 953be83a7e8031c41175fc4182ba89f0913b3755bfcf38d17449142759b024f9 |
| AMEND dense | c57556545032be55772a96e0886d35cb8ed33e16f6ce375c23c6363a691301c9 |
| PP audit (11:51 CST) | 4e1cf03555cc495382e949c438a54edc768a6cef8d8cb1e80bdd4f1b26410aea |
| ABSORB (11:52 CST) | 0a4ddb32f7f891b93c0db120de21638d3e5a30543eca0a9f59116866751ca570 |
| PR2 (cite) | bb329b4f2a3fa0ebbfaf7e3b0e05bfbc1af909b47eabf97bc5e7f0f295d038af |

## Provenance chain (M2)
1. **Origin of "45":** PP audit 4e1cf035… §3 "Tag counts (canonical 1–72) — Primary tag (first listed; item 69 untagged): PROVABLE-CANDIDATE | 45" (with NEEDS-DEFINITION 14, ALREADY-ON-RECORD 9, NOT-MATH 3, UNTAGGED 1 = 72). Same section: "All tag mentions … PROVABLE-CANDIDATE 46". Earliest on-disk occurrence found.
2. Owner Write `bridges/PHYSICIST/OWNER_WRITE_CALL_53991ebf_AGENT_PHYSICS_PAPER_S2_11DM2ETX_INTERPRETATION_2026-11-05.md` sha 546a61dfe0cfe92b780f1d0fecf40a6a97eb8ca9e01df7688e4724bc767dc318 (13:01 CST) L16: "Local 72-item filter: 45 provable candidates (ABSORB 0a4ddb32…; PP CONFIRM)." Also AMEND_CITATIONS OW e053f34e746add667fd2d49ef79198cccaec5cd10cb713db575ef5d08fed18a5 L15.
3. Agent paper FINDINGS a7bf622f9072460aa9daa875719e2c5a7ef33694aa6d4d296e7db3eb16e33e82 (L9 OW parent 546a61df MATCH; L18 attributes "filter 45/72" to ABSORB 0a4ddb32…/dense c5755654…; L32 "45/72 PROVABLE-CANDIDATE stated"). Pins FINDINGS 6e5c3a93d73bdabc25ecd14d6cfb67543e5ffff1ba055a78e1d4a0dd266268ee L19 maps [11] to ABSORB 0a4ddb32….
4. **Plainly:** Agent Soft SF took the count "45" from the Owner Write summary (which traces to PP §3 primary-tag tally) and wrote it into §6 / conclusion / [11] **without an enumerated ID list and without stating the primary-tag rule**. ABSORB (cited as [11]'s source) contains no "45" tally. Documentary hygiene gap: count carried, rule and IDs not.
5. RTA v16 PDF `papers/RTA_FOUNDATION_BOUND/RTA_FOUNDATION_BOUND_v16.pdf` sha 1fe7b8a2e245e90009c41726db13518b4c752e99ba4e08b4ffd006d8a73c3297: pdftotext — no 72-item filter, no "provable candidate" inventory, no 45 tally (only unrelated "candidate"/numeric hits). The original [1] bundling (Agent FINDINGS L18 "via v16 attach") was unsupported; pins move to [11] correct in direction.

## Independent recount
| Rule | pre-ABSORB | post-ABSORB |
|---|---|---|
| Any PROVABLE-CANDIDATE tag (PR1/PR2 method) | 46 | 47 (57 gains PC subclaim) |
| Primary (first-listed) tag = PROVABLE-CANDIDATE (PP §3 rule) | 45 | 45 (57 primary stays ALREADY-ON-RECORD; 32,53 stay PC; 59/63/69 non-PC) |
Primary-rule IDs (mechanical reproduction from PP §2 table, not a Soft SF Written list): 1,2,3,4,7,8,10,12,13,15,16,20,21,24,25,27,28,29,32,34,36,37,38,39,40,41,43,44,46,47,48,50,51,52,53,54,55,56,58,60,61,62,64,66,70. Difference vs any-tag 46: item 11 (PP tag 'NEEDS-DEFINITION → PROVABLE-CANDIDATE', primary ND); post-ABSORB any-tag adds 57.
PR1/PR2 46/47 reproduced; 45 is reproduced only under PP's primary-tag rule. No new rule invented.

## M1 status
Selection rule yielding 45: **FOUND** — PP audit 4e1cf035… §3 "Primary tag (first listed)". Enumerated 45-ID list as a Soft SF Written artifact: **ABSENT** (searched bounds above). IDs are mechanically derivable from PP §2 table (reproduction recorded, not adopted).

## M2 status
**FOUND (chain)**: PP §3 4e1cf035… → OW 546a61df… → Agent paper. Paper states asserted-count-only, rule unstated, cites ABSORB/[11] which does not itself state 45.

## Correction recommendation (do not apply)
Owner Soft SF amend paper prose (§6 L71/73, conclusion L101, [11] L127) to either (a) state the rule: "45 of 72 by primary (first-listed) tag per PP audit 4e1cf035…; 46 pre-/47 post-ABSORB carry a provable-candidate tag in any position", citing filter + PP audit; or (b) drop "45" and cite measured 46/47. Also fix "remaining 27 are not provable" and [11] source pointer (ABSORB alone does not carry the tally). Optionally Owner Soft SF Writes the enumerated primary-tag list before reclaiming 45. Completed evidence untouched.

## Explicit
Agent Soft SF did NOT invent a 45-list or selection rule (rule is PP's, quoted). PROVABLE-CANDIDATE ≠ proved. No CERT / no RECS. invent HOLD STANDS; invent-pending EMPTY. Unpaid PRESS → PP then Keeper.
