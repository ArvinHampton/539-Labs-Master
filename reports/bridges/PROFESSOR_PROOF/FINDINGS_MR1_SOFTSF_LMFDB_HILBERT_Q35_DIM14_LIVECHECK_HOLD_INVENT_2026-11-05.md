# Soft SF FINDINGS — Q(√35) Hilbert dimension livecheck

REPORTS ONLY. invent HOLD STANDS. No invented proofs; No CERT; No publish/spend.
OW context b25d5616… / PRIMARY bcc3ced0… retained, not revalidated here.
Observation: 2026-11-05 13:35 CST (America/Chicago).

## Result: MATCH
MATCH vs RTA v16 Thm 41.7 dimension 14, scoped to field 2.2.140.1 (Q(√35), discriminant 140), level-1 parallel weight [2,2] cuspidal newspace. The named prior live-parsing gap is closed at database-read-off level, not by an independent dimension computation or new proof.

## Exact URLs and quoted displayed cells
1. https://www.lmfdb.org/ModularForm/GL2/TotallyReal/?field_label=2.2.140.1&level_norm=1&weight=2
Quote: “The results below are complete, since the LMFDB contains all Hilbert modular forms over 2.2.140.1 of level norm at most 23”.
Quote: “Results (4 matches)”.
Table headers: “Label | Base field | Level | Dimension”. Rows (math markup normalized):
“1.1-a | Q(√35) | [1, 1, 1] | 2”
“1.1-b | Q(√35) | [1, 1, 1] | 2”
“1.1-c | Q(√35) | [1, 1, 1] | 2”
“1.1-d | Q(√35) | [1, 1, 1] | 8”.
These are constituent dimensions, not an explicit newspace total on the listing. Sum 2+2+2+8=14 is only a cross-check.

2. https://www.lmfdb.org/ModularForm/GL2/TotallyReal/2.2.140.1/holomorphic/2.2.140.1-1.1-a
Title: “Hilbert cusp form 2.2.140.1-1.1-a”.
Properties cells: “Weight | [2, 2]”; “Level norm | 1”; “Level | [1, 1, 1]”; “Dimension | 2”.
Form cells: “Weight: | [2, 2]”; “Level: | [1, 1, 1]”; “Dimension: | 2”; **“Newspace dimension: | 14”**.
Base-field sentence (math markup normalized): “Generator w, with minimal polynomial x^2 - 35; narrow class number 4 and class number 2.”
Quote: “This form has no Atkin-Lehner eigenvalues since the level is (1).”

3. https://www.lmfdb.org/ModularForm/GL2/TotallyReal/2.2.140.1/holomorphic/2.2.140.1-1.1-d
Title: “Hilbert cusp form 2.2.140.1-1.1-d”.
Properties cells: “Weight | [2, 2]”; “Level norm | 1”; “Level | [1, 1, 1]”; “Dimension | 8”.
Form cells: “Weight: | [2, 2]”; “Level: | [1, 1, 1]”; “Dimension: | 8”; **“Newspace dimension: | 14”**.

All three WebFetch calls returned readable page content; no fetch failures. No separate raw HTTP headers/status capture. WebFetch may return cached content per tool semantics. Individual b/c pages and separate dimension tables were unnecessary and not fetched: a/d directly state the requested newspace total.

## Written-source comparison
Re-read PDF via pdftotext:
/workspace/quantum-comp/reports/papers/RTA_FOUNDATION_BOUND/RTA_FOUNDATION_BOUND_v16.pdf
sha256 1fe7b8a2e245e90009c41726db13518b4c752e99ba4e08b4ffd006d8a73c3297.
Thm 41.7 (notation normalized): “One has dim V₃₅^Hilb = 14, with the split (41.3) verified against the LMFDB newform pages for 2.2.140.1 at parallel weight [2, 2] and level 1.”
Its proof records dimensions 2,2,2,8 and their sum 14. Numerical assertions MATCH the live read-off. No independent proof of the theorem's narrow-component assertion is supplied. Remark 41.8 declines identification with 36-dimensional V₃₅; this check supplies none.

Prior catalog rehashed:
FINDINGS_MR1_RESONANT_MATH_PREDICTIONS_NT_MODULAR_HECKE_HOLD_INVENT_2026-11-05.md
sha256 7a0be1d521c7e60d1aaee148af4cb6321785218ba70e9a72e1097d406713001a.
E9 parsing gap only is closed. Literature/framework PRESENT is not project-link PRESENT: O1–O4 remain open/project-object ABSENT as scoped by that catalog; no new literature search or invented resolution.

## Hygiene
Initial local PDF path /workspace/quantum-comp/papers/... was absent; located under reports/papers and successfully extracted. Not a web fetch failure. Initial write command used unavailable `python`; it exited before any writes, then python3 was used.
Locked tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md pre/post SHA256:
7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91.
Post-write and post-mirror rehash confirmed unchanged: tip_touched NO.
FINDINGS and PRESS plus .sha256 mirrored to bridges/{AUDITOR,PHYSICIST,PROFESSOR_PROOF,LOCAL}/ and reports/bridges/{same}/. No tip edits. HOLD invent STANDS. Soft SF only.
