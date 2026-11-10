# AUDITOR — Full-corpus crawl, Batch 04: packaging (RTA v16/v17) + close-out
Written: 2026-11-09 ~13:05 CST (America/Chicago), by Auditor.
Owner authority: "All haults lifted", 2026-11-09 12:34 CST (pt1864u).

Limits kept:
- This is a new dated file only (exclusive create). No sidecars were created.
- Archives were extracted ONLY into the scratch directory /tmp/aud/b4. Nothing was extracted over live files.
- Tools were read, not run. Tip `7cddb188…` untouched.
- No CERT, no Gemini, no external sends. No verdict was changed.

Paths: P16 = /workspace/quantum-comp/reports/papers/RTA_FOUNDATION_BOUND/, P17 = /workspace/quantum-comp/reports/papers/RTA_FOUNDATION_BOUND_v17_DRAFT_2026-11-05_2037CST/.
All mtimes are 2026-11-06 14:38–14:40 CST (the bulk copy). Archive member timestamps are given separately below.

## 1. Custody table
| # | Artifact | sha256 | Sidecar | mtime vs stated |
|---|---|---|---|---|
| 1 | P16/RTA_FOUNDATION_BOUND_src.zip (45 entries, 41 files) | 1abfae46e981ff4d287f3c9f113fe9f6da9c15489477c0082656e74d3c8915c4 | NONE | 11-06 14:38:50; members dated 2026-10-24 11:41–11:54 CDT |
| 2 | P17/RTA_FOUNDATION_BOUND_v17_DRAFT_src_minimal.tgz (9 files) | 239ded320b33488781477dad96a304a9b45dd112de26e78fb6e3fb4ba5e1ee42 | NONE | 11-06 14:40:44; members dated 2026-11-05 20:38–20:42 CST |
| 3 | P17/qa_pages/ (9 PNG: boundary-139..142, end-154..156, front-001, -002) | per-file in §2 | NONE | 11-06 14:40:45 |
| 4 | P17/qa_pages_fix/ (boundary-140..144, front-001, excerpt.txt) | excerpt.txt 54076c8a9dce23c2b9aff1a701347363bb92e7c042d61d916a59f09a141a0287 | NONE | 11-06 14:40:45 |
| 5 | P16/tools/conv_partI.py | 08ec24f10f99c312dac0e5067a38f0df374c284de16f751e0522376bb83c156e | NONE | 11-06 14:38:50 (= zip copy) |
| 6 | P16/tools/edit_partII.py | 462588cfd1afa63b8554c4f41d649e45415e49bcfc563f034c2fcab35ac1804f | NONE | 11-06 14:38:50 (= zip copy) |
| 7 | P16/RTA_FOUNDATION_BOUND_v15.pdf (142 pp; Created 2026-10-27 19:27:06 CDT) | 9c05e1aecc01f6e20febdc70efcdcc875266e44eb6d55dd4a3df821f36c1362b | **MISMATCH**: sidecar c2d101f5dd98…13e7 | 11-06 14:40:33 |
| 8 | P16/RTA_FOUNDATION_BOUND_v14.pdf (140 pp; Created 2026-10-27 17:00:11 CDT) | ab4673f3d5fe3649a6ac56db67f2fd6b13ee88ea016f794470cc03bde8d8315e | MATCH (.sha256); .sha256.src 6/6 MATCH | 11-06 14:40:33 |
| 9 | P16/RTA_FOUNDATION_BOUND.pdf (unversioned; 119 pp; Created 2026-10-24 11:54:17 CDT) | ffa2873d789df0dac9303acabd34d0734bb1ab544eccfb86cbfe1504f5ca2cfd | NONE | 11-06 14:38:50 |
| 10 | v14 src/NOTES sidecars | see §2.10 | 1 MATCH / 3 MISMATCH | 11-06 14:40 |

## 2. Findings per artifact
### 2.1 src.zip = the v1 source snapshot behind the unversioned PDF
- Contents: NOTES.md, src/ (main, main_preamble, front, intro, found, appD, partIII, partI/4, partII/27 files) and tools/ (2 scripts). Members are dated Oct 24 11:41–11:54. NOTES.md is dated 11:54, which matches the unversioned PDF's CreationDate of 11:54:17.
- The zip's NOTES.md :3 reads "Output: RTA_FOUNDATION_BOUND.pdf (119 pp)", and the PDF has 119 pages. Consistent.
- Diff against the live P16 tree (scratch only): **36 SAME, 5 DIFF, 0 missing.**
  - NOTES.md: v2/v3 history appended, 2319 → 2754 B.
  - src/appD.tex: 4487 → 5186 B.
  - src/found.tex: 9628 → 9872 B.
  - src/front.tex: +`\clearpage\input{glossary}`, the v2 glossary.
  - src/partIII.tex: 34767 → 35560 B; Open-problem wording expanded.
- So the live base files were edited in place after v1. **The live unversioned base src no longer reproduces the v1 PDF; the zip does.** This is benign: the live versioned files (front_vN, main_vN, …) are the ones that build v2+.
### 2.2 v17 src_minimal.tgz = the PRE-QA-fix snapshot (new evidence for C17-1)
- Contents: NOTES_v17.md, BASELINE_UNTOUCHED_CHECK.txt, DRAFT_MILESTONES.txt, and src/{main_v17, front_v17, glossary_v17, partIII_postv16_ledger_v17, partIII_boundary_rank_v17, appE_withdrawn_v17}.tex. Members are dated 20:38–20:42 CST.
- Diff against live P17: **5 SAME, 4 DIFF.**
  - DRAFT_MILESTONES.txt: 298 → 433 B. The live file adds :11–14, from "20:42:50 … deliverable ready" through "20:47:04 QA-fix delivered".
  - postv16_ledger: 6324 → 5984 B.
  - boundary_rank: 14550 → 15932 B. Changes: H defined on the free F-module F[G] instead of C[G]; the orbit list moved from an align* block to a 2-column table.
  - appE: 1802 → 1820 B.
- Environment census of the tarball's additive chapters: thm 3 / prop 7 / def 9 / rem 7 = **26**. This exactly matches DELIVERY_REPORT.txt:16, the pre-fix count. The live tree has 22 (thm 3 / prop 4 / def 7 / rem 8).
- Conclusion: the tarball was packaged at the ~20:42 first delivery and never refreshed. **It does not match the shipped post-fix PDF (9b407e1b…).**
- Effect on C17-1: there was a packaged pre-fix deliverable state, and the absolute-path v17 sidecar fits that packaging step. But no record ties `ee88d1cd…` to the pre-fix PDF, and that PDF is gone. The xdvipdfmx CreationDate/ID make a byte-exact rebuild impossible. **C17-1 stays UNDETERMINED**, though it is now more strongly consistent with the QA-fix explanation.
### 2.3 / 2.4 qa_pages vs qa_pages_fix
- front-001.png is byte-identical in both folders (db8a07d9…). Boundary pages shift from 139–142 to 140–144, consistent with the 2-column orbit table and the extra text.
- qa_pages_fix/excerpt.txt matches the current v17 PDF text: 125 of 132 long lines are found verbatim, and the remainder is page-break and spacing variance. It includes the post-fix "free F-module" wording. So the qa_pages_fix set corresponds to the shipped PDF.
- PNG hashes:
  - qa_pages: boundary-139 0cc63741…, -140 d3c93b4e…, -141 4a7b9160…, -142 38e646a8…, end-154 64a5d7f0…, -155 085a4929…, -156 20d0b9c8…, front-001 db8a07d9…, front-002 c7a2360e…
  - qa_pages_fix: boundary-140 1a9a5309…, -141 417cd7ee…, -142 6377a87f…, -143 9f0ecc02…, -144 6c702691…, front-001 db8a07d9…
### 2.5 / 2.6 tools (byte-identical to the zip copies)
- conv_partI.py reads s_family_paths/PAPER_gk_v1/PAPER.md and **writes** src/partI/p1_summary, p1_body, p1_appA and p1_appB (:44–45, :61, :66).
- edit_partII.py **rewrites src/partII/s*.tex in place**, plus s00_macros, s01_intro and s26_bib (:5–26).
- **Hazard B4-5:** these are historical build tools. Re-running either one would overwrite live spine sources that v16 and v17 both depend on. Do not run them. They were not run.
### 2.7 v15 PDF: sidecar MISMATCH (pre-existing)
- The sidecar `c2d101f5…` equals the hash recorded at render time in R/FINDINGS_AUDITOR_V15_PDF_RENDERED_2026-10-27.md:4 (~19:30 CDT Oct 27).
- The on-disk PDF is `9c05e1ae…`, with CreationDate 19:27:06 Oct 27.
- The same mismatch was already recorded in INVENTORY_AUDITOR_FULL_CORPUS_2026-10-31.md:49285 and FINDINGS_AUDITOR_SOFTSF_CONFIRM_RUN_ALL_2026-10-31.md:23. It is pre-existing as of ≤ Oct 31 and is not new tampering. Its cause is UNDETERMINED.
- Side finding: the same render record :6 gives "**total_now: 71 (=64+7 Cat A promotions)**" for v15. This **SUPPORTS** the digest's "71 (v15)" reading (batch 02, C2-1): NOTES_v16's 82 = v15 ledger 71 + 11.
- The C2-1 erratum stays correct: the ledger 71 (v15) and v16's 71 printed Theorems are different objects.
### 2.8 v14 PDF
- The .sha256 sidecar MATCHES.
- The .sha256.src manifest (6 lines) has all 6 lines MATCH live: the PDF ab4673f3…, partIII_modlocal_v14 a19a26e4…, partIII_partial_v14 33f6aa97…, front_v14 12370222…, glossary_v14 1812f61d…, main_v14 727f5878….
### 2.9 Unversioned RTA_FOUNDATION_BOUND.pdf
- Its sha `ffa2873d…` is **identical to NO numbered version**. I compared all 15 (v2–v16), and every hash is distinct.
- It is the v1 render: 119 pp, Oct 24 11:54:17 CDT. It predates v2 (11:58:01, 122 pp), and the build line is at zip NOTES.md :3.
- Page and date sequence: v1 119 → v2 122 → v3 123 → v4 128 → v5 130 → v6 131 → v7 132 → v8 133 → v9 134 → v10 134 → v11 135 → v12 135 → v13 137 → v14 140 → v15 142 → v16 148, then v17 DRAFT 156.
### 2.10 v14 src/NOTES sidecars
| Sidecar | Recorded | Live | Result |
|---|---|---|---|
| src/front_v14.tex.sha256 | fc44a675… | 12370222… | **MISMATCH** (the .sha256.src manifest has the live value) |
| src/main_v14.tex.sha256 | 3060b4d5… | 727f5878… | **MISMATCH** (the manifest has the live value) |
| src/partIII_draft_v14.tex.sha256 | 797a1d6f… | 797a1d6f… | MATCH |
| NOTES_v14.md.sha256 | 72885415… | cc44fc43… | **MISMATCH** |
All three mismatches were already recorded on Oct 31 (INVENTORY_AUDITOR_FULL_CORPUS_2026-10-31.md:49284, :49286, :49287). They are pre-existing stale sidecars, and they appear to predate the final v14 render. The v14 PDF manifest is self-consistent.

## 3. Bridge touchpoints (batch 04)
None. Packaging artifacts carry no Residual/Resonant, D1, S_eff, Layer2 or junction claims beyond the spine already mapped in batch 01. The tarball's pre-fix boundary chapter contains the same Thm 43.8–43.10 statements.

## 4. CLOSE-OUT: RTA lock → proof → ships → packaging crawl
**Status: COMPLETE for the RTA v16/v17 set (batches 01–04, 40 artifact slots).**
Findings files:
- BATCH01 30a1021c…
- BATCH02 44a53142…
- BATCH03 9e6a9692…
- BATCH04 (this file)
- ERRATUM C2-1 c808a2f6…

### Consolidated open blockers (01–04)
| ID | Blocker | Needs |
|---|---|---|
| C17-1 | v17 PDF sidecar ee88d1cd… ≠ PDF 9b407e1b…; UNDETERMINED; tarball shows the pre-fix packaging state | Owner: whether to add a new dated sidecar (never overwrite) |
| B4-3 | The v17 src_minimal.tgz is the pre-fix snapshot and does not build the shipped PDF | Owner: whether to make a new dated post-fix tarball |
| E16-1 | Frozen v16 prints "Lemma 39.18" for the Parity Lemma 24.3 (pp. 55, 81, 82, 103), from a duplicate label; fixed in v17 | Owner: errata note / v17+ only |
| B4-1 | v15 PDF sidecar MISMATCH (pre-existing ≤ Oct 31) | Owner: record-only or a new dated sidecar |
| B4-2 | v14 front/main/NOTES sidecars MISMATCH (pre-existing ≤ Oct 31) | same |
| B2-1 / B3-1 | No sidecars on 9 batch-02 artifacts (incl. Addenda Q–X), PP base review 17ab357b…, both archives, tools, and the unversioned PDF | Owner decision on sidecar policy |
| B2-2 | /tmp/q.py and /tmp/v.py (cited computation sources) absent; Auditor's independent recomputation matches | Record only, unless the sources are recovered |
| B2-3 | scope-inventory.json (editorial note :12) not found | Locate or record as missing |
| B3-2 | The PR2 records c531eacc / 17ae811b / 398a39f1 exist only under /workspace/quantum-comp/bridges/ | Owner: which tree is canonical |
| B3-3 | PP base review §3 det K_140 rows not re-derived (source not in scope) | Optional future batch |
| C3-1 / C3-2 | Owner Write 546a61df :15 "82 theorems" and :16 "45 provable candidates" | Owner only (Auditor does not edit Owner Writes) |
| C3-3 / C3-4 | Wording risks: "resonant algebra … proven anchors"; g−2 "measured" label | FYI |
| B4-5 | tools/*.py rewrite live src in place | Do-not-run note |
Closed: C2-1 for report source 1cb3d342 (erratum c808a2f6… filed; digest and Owner Write left unedited). The "71 (v15)" reading is now supported by v15 render record :6.

### Optional next crawl (batch 05: bridge/junction corpus, outside the RTA paper set)
1. R/OWNER_WRITE_LOCK_D1_Seff_Layer2_T3_2026-11-03.md (Lock 96f8d42e)
2. R/OWNER_WRITE_CALL_9ee0f248_LOOSEN_CAT_B_11D_TERNARY_MERGER_AMEND_S2_11DM2ETX_2026-11-05.md (2c341bc7)
3. R/FINDINGS_LOCAL_SOFTSF_LANE_REVIEW_COMPENDIUM_S2_11DM2ET_3ADIC_2026-11-05.md (892964f4)
4. R/FINDINGS_NL_TWO_TRACK_EXACT_CONSEQUENCES_2026-11-05.md (5b40ee12)
5. R/FINDINGS_NL_COMPENDIUM_LANE_REVIEW_2026-11-05.md (c9bf12b4)
6. R/evidence/MR1_APPELL_RC_FORENSIC_2026-11-05/ FINDINGS (46beb56b)
7. R/OWNER_DOCUMENT_ANALYTICAL_REVIEW_AUDIT_RESPONSES_TWELVE_AGENT_COMPENDIUM_GAPS_2026-11-05.md (Doc A d5b1aae5)
8. R/OWNER_DOCUMENT_FORMAL_RESOLUTIONS_STRUCTURAL_CORRECTIONS_COMPENDIUM_2026-11-05.md (Doc B 9c6f83da)
9. R/FINDINGS_LOCAL_SOFTSF_RTA_MATH_PREDICTIONS_CATALOG_2026-11-05.md (4e8720de)
10. R/FINDINGS_LOCAL_SOFTSF_GR_EXTENSION_PREDICTIONS_CATALOG_2026-11-05.md (5fbed443)
These are the primary records for the Residual-vs-Resonant lock, D1/S_eff/Layer2, and the S²-11DM²ET-X junction. PP Addenda A–P remain uncrawled and could follow as batch 06.
