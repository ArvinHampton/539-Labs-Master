# FINDINGS — AUDITOR soft-SF hash-only confirm: 539 Labs corpus + intake (2026-11-03)

Scope: hash-only. No source edits, no physics, no CERT, no recommendations. Video files skipped.

| # | File (under reports/) | sha256 (computed) | vs claimed prefix | vs sidecar |
|---|---|---|---|---|
| 1 | 539labs/539_Labs_Technical_Corpus.md | 5a8f863093c6eacb57a03b74b8c3906808111fbe43f6ba9677aebae4b8f17f9e | MATCH (5a8f8630) | MATCH |
| 2 | 539labs/INTAKE_539LABS_TECHNICAL_CORPUS_2026-11-03.md | d75a0a3a71cbc32d029d6a439fe7714ef37f62f8643a4460f2b53e6deb76081f | MATCH (d75a0a3a) | MATCH |

Sidecars checked: 2 (539labs/539_Labs_Technical_Corpus.md.sha256, 539labs/INTAKE_539LABS_TECHNICAL_CORPUS_2026-11-03.md.sha256). Both MATCH.
Mirrors: none found elsewhere under reports/ (searched by filename and by content hash across all .md files).
Corpus section 4: present (line 48, "### 4. TECHNICAL PRESENTATION & COMMERCIAL OUTLINE"). Presence only; content not reviewed.
Skipped: 539labs/539_Labs_Blueprint_30s.mp4.sha256 (video sidecar, out of scope).

Tip (read-only, not touched): /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md
sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — MATCH vs expected 7cddb188.

Counts: files checked 2; MATCH 2; MISMATCH 0; NO-SIDECAR 0; NOT FOUND 0; sidecars 2/2 MATCH; mirrors 0.
