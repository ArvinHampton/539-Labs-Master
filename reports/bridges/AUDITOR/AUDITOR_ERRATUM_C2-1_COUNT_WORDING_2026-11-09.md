# AUDITOR ERRATUM C2-1 — count wording in Auditor report source 1cb3d342
Written: 2026-11-09 ~13:00 CST (America/Chicago), by Auditor.
Owner authority: "All haults lifted", 2026-11-09 12:34 CST (pt1864u).
Additive erratum. The corrected file is NOT edited.

## Corrected record
- File: /workspace/quantum-comp/reports/bridges/AUDITOR/AUDITOR_PQC_ADVANCEMENT_REPORT_OWNER_1629_V16BASELINE_FOUNDATIONAL_PHRASE_2026-11-05.md
- sha256: 1cb3d34281522d8ec7d402eec12f890a1de91d190a827a5882963b1f4a12cd1b
- Status: preserved unchanged; re-hashed 2026-11-09, MATCH.

## Corrections
- **Line :16** reads "theorem count **total_now = 82 (= 71 + 11 new Category A)**". Correct reading:
  - 82 counts **mixed numbered statements**: 71 + 11 Category A numbered statements, per NOTES_v16.md:8 (".../NOTES_v16.md", sha 061eac86…).
  - It is not a count of Theorems.
  - The 11 v16 additions are a Theorem / Proposition / Definition mix (NOTES_v16.md:10–20).
- **Line :18** reads "the same PDF sha and **82-theorem label**". Correct reading: "the same PDF sha and the 82-numbered-statement label (mixed statements, not theorems)".

## The distinct count
- The v16 PDF (sha 1fe7b8a2…, 148 pp) prints **71 Theorems**: 60 `\begin{theorem}` environments plus 11 hard-coded Part I Theorems.
- Source: Auditor batch-01 census, AUDITOR_CORPUS_CRAWL_BATCH01_RTA_v16_v17_2026-11-09.md §(c). This agrees with the v17 theorem audit AUDIT_SUMMARY.md, which gives v16 60 + 11.
- This 71 is a **different count** from the "71" summand in NOTES_v16.md:8. The match is a numerical coincidence; the two must not be equated.
- For reference, v17 DRAFT prints 74 Theorems.

## Scope
- This erratum corrects only 1cb3d342 lines :16 and :18.
- The since-v16 digest (FINDINGS_AUDITOR_DIGEST_SINCE_RTA_V16_2026-11-05.md, sha d485dcc2…, lines :15 and :77) is left unedited. Its same wording is noted in batch 02, C2-1.
- The Owner Write 546a61df… line :15 ("82 theorems") is left unedited. It is noted in batch 03, C3-1.
- No verdict changes. Tip 7cddb188… untouched. No CERT.
