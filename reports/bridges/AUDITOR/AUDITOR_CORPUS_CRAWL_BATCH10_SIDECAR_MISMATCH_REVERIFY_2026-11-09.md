# AUDITOR — Corpus crawl batch 10 — re-verification of the 14 B9-1 sidecar mismatches — 2026-11-09

Role: Auditor. Report-only. Written 2026-11-09 ~13:30 CST (America/Chicago). Authority: Owner "All haults lifted" (12:34 CST, pt1864u). Nothing modified or moved; no sidecars created; no CERT; no external sends; no verdict changed. Reconstruction hashing done in memory/scratch only. Tip sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91: MATCH.
Classes: AMENDED-IN-PLACE (benign = no change to any mathematical statement; substantive = a mathematical statement or claim-status changed), SIDECAR-STALE, UNDETERMINED, plus NOT-A-MISMATCH where the batch-09 parse was wrong.

## 0. Additive correction to batch 09 (563c6793…) — not an overwrite
- §4 "each mismatched in 6 locations" → **5 locations** (top-level, AUDITOR/, bridges/AUDITOR, bridges/PHYSICIST, bridges/PROFESSOR_PROOF). The count of 10 paths is unchanged.
- §4 counts: batch 09 read only the first hash line of each sidecar. Four sidecars carry several entries. With path-aware parsing: **MATCH 6347, MISMATCH 20** (not 6346 / 21). The orphan count of 233 is unchanged.
- B9-1 "NEW": 3 of the 14 (SMITH LOCK, EIGEN_ACK, NL_WORKING_THREAD) were already listed as MISMATCH in FINDINGS_AUDITOR_SOFTSF_CONFIRM_RUN_ALL_2026-10-31 (sha bbed96cff3631d0b6ba055099c3655f9d3658ae3e72177c40a617c4f456312e4, :19–21) and INVENTORY_AUDITOR_FULL_CORPUS_2026-10-31. The current hashes equal the ones computed on 10-31, so there has been no further change since 10-31.

## 1. Results (6 distinct contents; 14 paths)
| # | Record (paths) | Current | Sidecar | Class |
|---|---|---|---|---|
| 1 | GR paper, 5 paths | de755741… | e140947e… | AMENDED-IN-PLACE, substantive (math display fix) + benign editorial; sidecar knowingly left historical |
| 2 | GR paper pins, 5 paths | 47ea689a… | 6f01d93b… | same as #1 |
| 3 | FINDINGS_AGENT_LOOSEN…9ee0f248 (top only) | aea5bebc… | 9b047680… | UNDETERMINED (divergent copies); no math change |
| 4 | EIGEN_ACK_PRIMARY_MESH… (top) | b3e7159e… | 707a6dc0… | AMENDED-IN-PLACE, benign (append-only VOID block) |
| 5 | NL_WORKING_THREAD_RPPT_MC… (top) | 0b91b476… | 7bdf9fc1… | AMENDED-IN-PLACE, benign (two append-only stamps) |
| 6 | OWNER_WRITE_SMITH…LOCK (top) | dff6222a… | 08e40042… (line 1) / dff6222a… (line 2) | NOT-A-MISMATCH (2-entry sidecar; line 1 hashes the candidate body, line 2 = MATCH) |

## 2. Detail

### #1/#2 GR paper and citation pins (5 mirrors each; all mirrors byte-identical to top-level)
- Chain, from backups in /workspace/audit-scratch (outside reports/, not modified):
  - paper e140947e → bd39eb4c (ternary-floor-correction-20261105, ledger 84eeb544…) → de755741 (candidate-count-clarification-20261105, ledger 4288e07e…);
  - pins 6f01d93b → 0009e735 → 47ea689a.
  - The sidecar-hash content survives as backups/00-…, 01-… in ternary-floor-correction (hash = sidecar, exact).
- **Diff 1 (floor fix), line 36 only, in both files:** the n ≡ 2 branch changed from `(2n+1)/3` to `⌊(2n+1)/3⌋`.
  - Math: for n = 3k+2, (2n+1)/3 = (6k+5)/3 is not an integer. The old display was not a map ℕ→ℕ.
  - The new display is the canonical floor map (n//3, (4n+2)//3, (2n+1)//3; batch 06b K-src) → the correction is PROVED correct. This is a substantive change to a mathematical statement, in the direction of correctness.
  - The ledger SUMMARY says the edit was one substitution, that all other bytes were verified, and that "source hashes in old sidecars are historical".
- **Diff 2 (count clarification):** §6 L71–75, §9 L103, new ref [12].
  - "45 of 72 provable candidates" is now qualified as a primary-tag tally (46/47 counting any tag).
  - The earlier claim "the remaining 27 are not provable in their current form" is **retracted** ("not a claim that they are impossible to prove").
  - Display math is byte-identical (paper); in the pins only a line-number shift (80→82).
  - Class: substantive change to a claim-status statement; no theorem altered.
- **Citations:**
  - Sidecar hashes: e140947e is cited in 183 files, 6f01d93b in 123.
  - Current hashes: de755741 in 71 files, 47ea689a in 53, including FINDINGS_AGENT_SOFTSF_VERIFY_CANDIDATE_COUNT_CLARIFICATION (78faf679…) and FINDINGS_PP_SOFTSF_AUDIT_CANDIDATE_COUNT_CLARIFICATION (0268f75d…: "successor hashes are de755741… and 47ea689a…").
  - Intermediate hashes bd39eb4c / 0009e735 are cited by the Agent TRACE/VERIFY records and by FINDINGS_DF_SOFTSF_AMEND_G15_CITATION_PINS_VERSION_CHAIN (345222c4…), which was audited by PP (5fbd6068…) and Keeper (95d57624…).
  - PP 0268f75d :11 noted that no verbatim OWNER_WRITE exists for the 14:11 "Apply" instruction.
- Cross-reference: paper §9 L103 lists "H²(F) ≅ ℚ·[s_αδ]" as established. Per batch 07 (1a48abce…), that holds only for the truncated F; this is a scope note, not an edit.

### #3 FINDINGS_AGENT_LOOSEN…9ee0f248
- The sidecar hash 9b047680 is held by 9 mirrors (bridges/AUDITOR, AUDITOR/, bridges/PHYSICIST, bridges/PROFESSOR_PROOF and nested copies). The top-level copy is aea5bebc.
- Full diff:
  - The two are separately worded REVISE drafts: top-level headed "~12:12+", mirrors "~12:13".
  - Neither is a prefix or append of the other.
- Citations:
  - aea5bebc is cited in the Auditor digest since v16 (:67, :88: "Agent Cat B REVISE aea5bebc…, no dedicated Auditor CONFIRM").
  - REPORT_AGENT_CAT_B…53991ebf (6db164ec…) :177 calls the top-level copy "reports/ drift aea5bebc… left alone" and the bridges copies 9b047680 the prior FINDINGS.
- Order of writes is not recoverable (Nov 6 bulk copy reset mtimes) → UNDETERMINED.
- Math: both state the same statuses — EX/FA NOT-FEASIBLE, PA PARTIAL, G4a/G4b OPEN STANDS, W₇ CLOSED ABSENT, P2 VACATED, Gap-E LOCKED OPEN, no CERT, invent HOLD 1fadc632 — and contain no theorem statement → **no math claim changed** (framing and wording only).

### #4 EIGEN_ACK_PRIMARY_MESH_LOCAL_NL_AGENT
- Removing the trailing block "## VOID — SUPERSEDED by CANCEL OW 419af1a2…" (lines 15–16) reproduces 707a6dc0 exactly → append-only amendment.
- The sidecar hash is cited by EIGEN_ACK_STOP_PRIMARY_MESH_CANCELLED :5 ("Eigen mesh ACK 707a6dc0… — VOID"). The VOID block mirrors that record.
- No math → benign.

### #5 NL_WORKING_THREAD_RPPT_MC_NUCLEAR_SCALE
- Truncating before "## Deepen stamp" gives 7bdf9fc1 exactly. Truncating before "## Hybrid MC first-move stamp" gives e4a4622e exactly.
- e4a4622e is cited as "updated; was 7bdf9fc1" in PR1-FINDINGS-NL-PAIR…RANK20-DW7 :13, :80.
- Both additions are stamps (FINDINGS pointers ce6520ce…, 6bbc198e…; tip_touched NO).
- 7bdf9fc1 is pinned by OWNER_WRITE_CANDIDATE_NON_LOCAL_PATH… :23 and OWNER_WRITE_NL_CARD10… :23. Those pins now point to a prefix of the current file.
- No math → benign.

### #6 OWNER_WRITE_SMITH_BRIDGE_C_RR_DICTIONARY_LOCK
- The sidecar has two lines: 08e40042 …/OWNER_WRITE_SMITH_BRIDGE_C_RR_DICTIONARY_2026-10-26.md (the locked candidate body, which still matches) and dff6222a …/…_LOCK_2026-10-26.md (MATCH).
- The LOCK stamp's own hash dff6222a is cited by OWNER_WRITE_CANDIDATE_LOCAL_ZWEGERS… :16.
- The 10-31 Auditor flag and the batch-09 flag are both parse artifacts → NOT-A-MISMATCH.

## 3. Math-claim change summary
- Changed: the GR paper and pins T₃ display, residue-2 branch (2n+1)/3 → ⌊(2n+1)/3⌋. This is a correction, now consistent with the canonical T₃.
- Changed: the paper's claim-status sentence "27 not provable in their current form" was retracted.
- Unchanged: #3 (statuses identical), #4, #5, #6.

## 4. Blockers
- B9-1 is narrowed:
  - real mismatches 13 paths / 5 contents;
  - 0 unexplained content changes;
  - all predecessor contents are recovered or reconstructed except #3's write order.
- B10-1: the paper and pins sidecars were knowingly left historical (ledger). This needs an Owner sidecar-policy decision (joins C17-1/B6-1).
- B10-2: LOOSEN top-level vs mirror divergence is UNDETERMINED.
- B10-3: no verbatim OWNER_WRITE exists for the count-clarification apply (PP 0268f75d :11).
- B10-4: B9 parser corrected (multi-entry sidecars: 4).

Next: OWNER_WRITE batches 11–13.
