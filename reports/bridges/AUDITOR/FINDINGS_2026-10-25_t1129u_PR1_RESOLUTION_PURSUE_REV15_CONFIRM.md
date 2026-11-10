# FINDINGS — PR1 catalog rev.15 + Resolution pursue (t1129u) — CONFIRM
Date: 2026-10-25 ~20:35 CDT (America/Chicago). Auditor scope: CONFIRM-only. No physics added. No measured-row PASS/FAIL altered. residual-C not edited.

## Verdict: MATCH-with-SF

## Hashes verified
- Catalog `/workspace/obs-data-PR1-HEPP-QM-GR.md` rev.15: `29cf7c98d3ef0ea670acae4580eeeee7fb21d4c4eeb80b0a4520d28f29090b87` — MATCH
- Prior rev.14 backup `obs-data-PR1-HEPP-QM-GR.rev14.bak.md`: `586dcf94986c33414ebcf5dcf0ee9eebed3181cb4a03dac3c2182d5ff9e7daec` — MATCH (diff taken against it)
- Report `PR1_RESOLUTION_PURSUE_t2030_2026-10-25.md`: `b7ac8c173bdf69cc267f5b2b58f417806267af2203fb321d09f748d25d84c346` — MATCH
- Stamps: t1118u `c1d59d58d391e03340eb2b79391d519fa4eac6f7259239d16a4599ff387ee014`, t1129u `425bb2ab12093b43848c07ea01ee5d918964e962c5fa1fe043ca8ac39269975e` — MATCH
- Prior FINDINGS rev.14: `18b9cc77a61105fd82010075b8785bd55d1ff7519efe6e89d1453d5e8d942e9c` — MATCH
- residual-C (`residual-c-field-WRITTEN_PREMISES_DRAFT.md`) tip before/after: `492fb3ac95c20e9117594639eb5947c90785a09e93da8301d6e83980c490a6fa` — untouched

## Checks
1. SF1 (§4.7 stale rev.13 text + `):**` fragment) — FIXED. Replaced by a rev.15 note and a short historical line.
2. SF2 (t_Mf vs t_M) — FIXED in substance: every unit now reads t_Mf. See Soft SF-A on the glyph.
3. SF3 (duplicate [V rev.14]/[HARD]) — FIXED. Tags merged to "[V rev. 14, HARD; …]".
4. GWTC-4.0 m_g ≤ 1.92×10⁻²³ eV/c² (90%) — PRESENT in the §2B catalog bullet (paper II) and in report line 19. Report and catalog agree. The PN 1.2–5.5× and 98.6%→92.2% figures also agree. Not re-fetched by the Auditor; this is a consistency check only.
5. JUNO (arXiv:2511.14593) — FOLDED as claimed: a §2D row with sin²θ₁₂ = 0.3092 ± 0.0087 and Δm²₂₁ = (7.50 ± 0.12)×10⁻⁵ eV². The §4 open item now reads FOLDED. The row agrees with the report.
6. Table VII spot-check (local `uploads/2112.06861.txt`, GWTC-3 43-event row): Ā₀ 1.88/0.89/86, Ā₁ 1.16/0.32/96, Ā₃ 0.66/2.33/2 and Ā₄ 0.30/0.74/15 all MATCH. The caption says "<" = A_α>0 and ">" = A_α<0, which matches the catalog's A>0/A<0 order. GWTC-2 m_g 3.09 MATCH. Values were read from interleaved pdftotext output (GWTC-2 pair, then GWTC-3 pair, per α), and the Q_GR columns line up.
7. The rev.14 1.31× misattribution fix (Solar System 3.16, not GWTC-2) is consistent with the catalog's own correction text. The 7.3/7.5×10⁻⁴ discrepancy is noted as the paper's own. Auditor did not re-verify against the PDF beyond Table VII.
8. Measured-row delta: rev.14→rev.15 diff touches §2B (GW250114 notation; GWTC-3 wording; 3 new [V] sub-bullets: Table VI/VII, 2509.08099, GWTC-4.0), §2D (+JUNO row), §2F header text, §4 items 2/7 and the changelog. No PASS/FAIL token changed. No unauthorized flips.
9. Status flags: Bridge PARTIAL / READY NO; not Cat A (report line 2). No Zenodo Secure Form blocker citation in the catalog delta or the report — PASS.

## Soft SF
- SF-A (clerical): the rev.15 start-time symbol renders as "t>" (4 occurrences: GW250114 bullet and the 2509.08099 bullet) where rev.14 had "t₀". This looks like a subscript glyph lost in pdftotext. The changelog repeats it ("t> … t_Mf"). Suggest restoring "t₀". No numeric impact.
- SF-B (clerical): the Table VII line says "Full table (α = 0…4)". The paper has α ∈ {0, 0.5, 1, 1.5, 2.5, 3, 3.5, 4}; the catalog quotes the subset 0/1/3/4. Suggest stating the subset explicitly.
