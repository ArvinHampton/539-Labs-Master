# eigen-matrix-search

**Arvin Hampton / 539 Labs. Date: 2026-10-08.**

This folder holds the results of searching Arvin Hampton's Grok project "Quantum Comp" (S²-11DM²ET-X model) chat archive for eigenvalue and matrix work, and for neutrino mass/mixing spectra. The source transcripts in `../grok-chats/` are read-only and were not modified. Quotes in the reports are verbatim with file and line references. Every numeric verdict comes from the scripts in `checks/` and sits next to the quote, never written over it.

## Main reports
- `REPORT.md`: the full eigenvalue/matrix search report across the archive. Classified hits by theme, verbatim quotes, re-computed checks, and a list of chats with no saved text.
- `NEUTRINO-EXTRACT.md`: the neutrino mass/mixing extract for the 17 chats in `../grok-chats/raw-neutrino/`. One section per chat: mass formulas, mixing angles/matrices, eigenvalue triples, Δm², seesaw and sum-of-mass claims. Each item is tagged MODEL / PUBLIC / GROK and has check tables. It ends with one consolidated, source-tagged LaTeX block. Bottom line: no chat holds a matrix whose eigenvalues reproduce a printed neutrino mass triple.

## Data tables
- `hits.tsv`: classified search hits (columns: chat_id, title, file, line, term, class = CORE / RELATED / FP / OTHER, theme, snippet).
- `hits_raw.tsv`: the same hits before classification.
- `uncaptured_candidates.tsv`: project chats that look relevant (tiered strong / possible) but have no saved text yet, with Grok URLs and the reason each was flagged.
- `project-chats-current.tsv`: the project's chat list (title, chat id).
- `grok-search-results.md`: notes from Grok's own in-app search for eigen/matrix terms, filtered to this project.

## Checks (`checks/`)
- `numeric_checks.py` → `numeric_checks.json`: re-runs 48 eigenvalue/matrix/trace claims quoted in `REPORT.md`.
- `kplus_laplacian.py` → `kplus_results.json`: rebuilds the residual K⁺ graph Laplacian and spectrum.
- `nu_extract_checks.py`: neutrino base mass, M_ν phase-matrix eigenvalues/singular values, Set A/B Δm², the PMNS assembly, CKM angles, Ω_ν arithmetic.
- `check_21baa1c1.py`: the W_np = e³ neutrino mass formula and its code, θ₁₂ and Δm²₂₁ formulas, seesaw numbers (needs sympy).
- `check_3110c8b2.py`: the resonant-ring lepton formula m = 539.9·cos(2πn/539.9) MeV, the "7021 identity", and the α⁻¹ formula.
- `check_f231d8ef.py`: the Lopez Giant Arc / Big Ring "third structure" geometry (comoving distances, equilateral vertex) and that chat's arithmetic.

## Scripts
- `scan.py`, `classify.py`, `build_candidates.py`: the archive scanner, the rule classifier, and the candidate-list builder for `REPORT.md`.
- `nu_grep.sh`: the neutrino keyword grep used for `NEUTRINO-EXTRACT.md`.
- `nu_assemble.sh`: rebuilds `NEUTRINO-EXTRACT.md` from `nu_parts/*.md` (header, one part per chat, LaTeX block).
