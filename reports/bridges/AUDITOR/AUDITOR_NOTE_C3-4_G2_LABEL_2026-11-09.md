# AUDITOR NOTE — C3-4 — muon g−2 value label in PP review — 2026-11-09

Auditor (executor). Prepared 2026-11-09 ~12:52 CST (America/Chicago). Additive note only: the PP review is NOT edited. Exclusive create. No CERT. No external sends. Tier-E verdict unchanged.

## Subject
R/FINDINGS_PP_OWNER_PDF_1715_MATH_REVIEW_2026-11-05.md (sha256 17ab357b2e88c99296a18f4750ce8360a780bda152d24653831ba98e776f5bc2), line 18:
"Tier E input: a_μ = 11659181×10⁻¹⁰ is the muon g−2 measured value, not an arithmetic constant."
Note: 11659181×10⁻¹⁰ = 116591810×10⁻¹¹ = 0.0011659181 exactly.

## Primary sources (fetched 2026-11-09)
1. Aoyama et al., "The anomalous magnetic moment of the muon in the Standard Model", Phys. Rep. 887 (2020) 1 — https://arxiv.org/abs/2006.04822 — abstract: "a_μ^SM = 116 591 810(43)×10⁻¹¹ … smaller than the Brookhaven measurement by 3.7σ". Table 1: E821 experiment 116 592 089(63)×10⁻¹¹.
2. Muon g−2 Collab. (FNAL Run-1), PRL 126, 141801 (2021) — https://arxiv.org/abs/2104.03281 — a_μ(FNAL) = 116 592 040(54)×10⁻¹¹; experimental average a_μ(Exp) = 116 592 061(41)×10⁻¹¹; quotes a_μ(SM) = 116 591 810(43)×10⁻¹¹ from ref. [13] (= source 1).
3. Muon g−2 Collab. (FNAL Run-2/3), PRL 131, 161802 (2023) — https://arxiv.org/abs/2308.06230 — a_μ(FNAL) = 116 592 055(24)×10⁻¹¹; world average a_μ(exp) = 116 592 059(22)×10⁻¹¹.
Context (later; secondary pages via search, not used for the verdict): PDG 2025 review https://pdg.lbl.gov/2025/reviews/rpp2025-rev-g-2-muon-anom-mag-moment.pdf and WP25 https://muon-gm2-theory.illinois.edu/white-paper-25/ give exp world average 116 592 071.5(14.5)×10⁻¹¹ (after FNAL final, June 2025) and updated SM 116 592 033(62)×10⁻¹¹.

## Finding
- 11659181×10⁻¹⁰ matches the 2020 Theory Initiative **Standard-Model prediction** (116 591 810×10⁻¹¹) to all digits shown.
- It does not match any measured value: E821 116 592 089, FNAL-2021 average 116 592 061, FNAL-2023 world average 116 592 059, 2025 world average 116 592 071.5 (all ×10⁻¹¹). The measured values would read ≈ 11659206–11659207×10⁻¹⁰.
- **Verdict: PP :18 "measured value" is a MISLABEL.** Correct label: "SM prediction (Muon g−2 Theory Initiative 2020, Phys. Rep. 887, arXiv:2006.04822)". It is superseded by WP25 (116 592 033(62)×10⁻¹¹).
- Unchanged: the PP point that a_μ is a Tier-E physical input, not an arithmetic constant, stands. This is a label correction only; no verdict changes. The κ = 1.595361 = √(2/0.7858) remark on the same line is unaffected (Auditor check: √(2/0.7858) = 1.5953610…).

## Suggested erratum text (for the PP lane/Owner; not applied)
"PP review 2026-11-05 :18 — read 'a_μ = 11659181×10⁻¹⁰ is the 2020 Standard-Model prediction (Aoyama et al., Phys. Rep. 887 (2020), arXiv:2006.04822), not a measured value; measured world averages are 116592061(41)×10⁻¹¹ (2021) and 116592059(22)×10⁻¹¹ (2023). Tier-E status unchanged.'"

Tip sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 untouched. C3-4 → RESOLVED (label), pending PP-lane erratum.
