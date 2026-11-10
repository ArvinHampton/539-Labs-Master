# AUDITOR — Corpus crawl batch 09 — hash-and-dedupe sweep of reports/ — 2026-11-09

Role: Auditor. Report-only. Written 2026-11-09 ~13:15 CST (America/Chicago). Authority: Owner "All haults lifted" (12:34 CST, pt1864u). Nothing modified or moved; no sidecars created; no CERT; no external sends. Hashes computed into /tmp/aud09 scratch (sha256sum over every regular file under /workspace/quantum-comp/reports, 2.0 GB; 2 symlinks not followed). Tip sha 7cddb188…dfc91: MATCH.
Companion manifest: AUDITOR_CORPUS_CRAWL_BATCH09_DEDUPE_MANIFEST_2026-11-09.tsv, sha256 677bc1c220bf201613ad98eaad76dd3997a8f6fa319f8283c9e9d6c28ecba641 (22035 rows + header; columns: sha256, copies, canonical_path, folders, covered_b01_08, also_outside_reports, sidecar_status_canonical). Canonical path = top-level reports/ first, then non-mirror subfolder, then mirror (self-audit/_git_v8/heavy-daily), shortest path.
Note: the manifest, written after the hash pass, is itself not in the counts.

## 1. Totals
| Measure | Count |
|---|---|
| Regular files | 36250 |
| Unique contents | 22035 |
| Duplicate groups (≥2 copies) | 8088 |
| Redundant copies | 14215 (39.2%) |
| .md files / unique .md contents | 12210 / 6866 |
| Unique doc contents (.md/.tex/.txt/.pdf) | 10618 |
| Unique by extension (top) | .md 6762, .sha256 3687, .txt 3178, .json 2574, .py 1412, .log 857, .bin 491, .pdf 456 |

## 2. Duplicates by folder (files / redundant copies / unique contents canonically owned)
| Folder | Files | Redundant | Owned unique |
|---|---|---|---|
| s_family_paths | 8406 | 2513 | 5893 (data: .txt/.json/.bin/.npz) |
| (top-level) | 4511 | 3 | 4508 |
| heavy-daily | 4296 | 989 | 3307 |
| bridges/AUDITOR | 4092 | 3614 | 478 |
| AUDITOR (reports/AUDITOR) | 3140 | 1177 | 1963 |
| bridges/_git_v8_unpushed_clone | 2826 | 2683 | 143 |
| self-audit | 2644 | 1154 | 1490 |
| bridges/BRIDGE_C_35 | 1792 | 54 | 1738 |
| bridges/NONLOCAL_QM_EH11D | 907 | 498 | 409 |
| crypto | 876 | 143 | 733 |
| bridges/PROFESSOR_PROOF | 599 | 515 | 84 |
| evidence | 438 | 74 | 364 |
| bridges/PHYSICIST | 392 | 392 | 0 (pure mirror) |
| papers | 315 | 109 | 206 |
| chronoflux | 295 | 14 | 281 |
| bridges/LOCAL | 160 | 158 | 2 |
| bridges/EIGEN | 58 | 58 | 0 (pure mirror) |
Cross-tree: 2252 uncovered unique doc contents in reports/ also exist outside reports/ (self-audit 1018 — mirrors of oct17-master; top-level 684; heavy-daily 216).

## 3. Coverage by batches 01–08
Method: any full sha256, 8-hex prefix, or exact basename cited in the 12 AUDITOR_*_2026-11-09.md records. Result: 228 unique contents (298 paths; 161 unique .md) covered. Prefix matching is approximate (possible false positives; no collision check beyond 8 hex).

## 4. Existing sidecars (report only; none created or changed)
| Status | Count |
|---|---|
| MATCH | 6346 |
| MISMATCH | 21 |
| Orphan (target absent) | 233 |
| Unparsable | 0 |
MISMATCH paths (relative to reports/):
- Known: papers/RTA_FOUNDATION_BOUND/{NOTES_v14.md, src/front_v14.tex, src/main_v14.tex} (B4-2); papers/RTA_FOUNDATION_BOUND/RTA_FOUNDATION_BOUND_v15.pdf (B4-1); papers/RTA_FOUNDATION_BOUND_v17_DRAFT_2026-11-05_2037CST/{RTA_FOUNDATION_BOUND_v17_DRAFT.pdf, src/front_v14.tex, src/main_v14.tex} (C17-1).
- NEW (B9-1): PAPER_S2_11DM2ETX_EXTENSION_OF_GENERAL_RELATIVITY_INTERPRETATION_2026-11-05.md and its _CITATION_PINS_ twin, each mismatched in 6 locations (top, AUDITOR/, bridges/AUDITOR, bridges/PHYSICIST, bridges/PROFESSOR_PROOF) = 10 paths; EIGEN_ACK_PRIMARY_MESH_LOCAL_NL_AGENT_2026-10-26.md; FINDINGS_AGENT_LOOSEN_CAT_B_11D_TERNARY_MERGER_CALL_9ee0f248_2026-11-05.md; NL_WORKING_THREAD_RPPT_MC_NUCLEAR_SCALE_2026-10-26.md; OWNER_WRITE_SMITH_BRIDGE_C_RR_DICTIONARY_LOCK_2026-10-26.md.
- B9-2: 233 orphan sidecars (target renamed/absent).

## 5. Unique remainder and revised priority
Uncovered unique .md, not mirrored outside reports/, excluding s_family_paths data: 4449 (top-level 1568, AUDITOR 1078, heavy-daily 673, BRIDGE_C_35 460, bridges/AUDITOR 226, NONLOCAL 202, self-audit 112, crypto 48, tubulin 17, papers 11). Of these, 718 carry math-claim markers (Theorem/Lemma/Proof/PROVED/REFUTED/CONDITIONAL): top 345, heavy-daily 79, self-audit 75, BRIDGE_C_35 72, AUDITOR 37, bridges/AUDITOR 31, NONLOCAL 28, crypto 18, tubulin 15, papers 5.
Top-level uncovered by prefix: SOFTSF_PRESS 451, OWNER_WRITE 245, FINDINGS_LOCAL 90, FINDINGS_MR1 71, PR1-FINDINGS 66, FINDINGS_PR2 58, REVIEW_LOCAL 58, MR2-FINDINGS 55, FINDINGS_PP 36, NL_RULE5 25.
Priority:
1. B9-1 custody note: re-verify the 14 new MISMATCH paths (1 batch, report-only).
2. OWNER_WRITE (245; authority/locks) — math-bearing subset first (3 batches).
3. FINDINGS_PP remainder (36) + PP-FINDINGS (1 batch).
4. Top-level math-bearing FINDINGS_LOCAL/MR1/MR2/PR1/PR2/REVIEW_LOCAL (~300 marker hits; 8–10 batches).
5. self-audit (75) + crypto (18) + papers (5) + tubulin (15) math-bearing (3 batches).
6. BRIDGE_C_35 (72) + NONLOCAL (28) + AUDITOR/bridges-AUDITOR (68) (4 batches).
7. heavy-daily (79) (2 batches).
8. Non-math remainder (~3700, incl. SOFTSF_PRESS) by custody sampling (2 batches). s_family_paths data: checksum-only.
Estimate: ~24 batches (10–33), ±5, at ~30 math-bearing files per batch.

## 6. New blockers
- B9-1: 14 new sidecar MISMATCH paths (4 records × mirrors).
- B9-2: 233 orphan sidecars.
- B9-3: reports/AUDITOR (3140 files) is distinct from bridges/AUDITOR; provenance of the two Auditor trees not established.
Other blockers unchanged from 08b.
