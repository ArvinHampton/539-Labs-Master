# RESULTS — t761u inventory #5 G-A3 reopen path (catalogue only)
PREREG sha in logs/PREREG.sha256. Basis live shas in logs/verify_basis.txt.

## 1. Why PAUSED; what "non-rejected reopen" means
- t713u fill (PREREG 49bd0b24… / RESULTS c4755206… / table 4da09dec…) LOCKed; Auditor a520614b… MATCH on LOCK only.
- t717u: Arvin REJECT filled G-A3 (AUDIT_STATUS L408) — values not Cat A; soft SF if treated as accepted.
- t718u revise menu a05693fb… (Auditor 2e1dec49…); t721u R-PKG1 BLOCKED, χ/ϑ absent (PREREG 9e0c3705… / RESULTS 7d324d73… / Auditor 1749576a…); t722u opt-(c) diag RESULTS 9aa52f19… / Auditor 4ad006b7… (F1 FAIL; F3 regularized only).
- t725u PAUSE (AUDIT_STATUS L422): no new G-A3 fill watch; next gap prefer X4.
- "Non-rejected reopen" = a NEW, separately PREREG'd run under the current stacked Cat A (AW+O+PB+E), schema v2 8d247feb…, with zero reuse of 4da09dec cells/data (t713u data/ files likewise excluded). Requires explicit Arvin ACCEPT of a menu option. Not executed here.

## 2. Blocker ledger (t718 R-PKG1 components)
| Blocker | Status now | Source |
|---|---|---|
| Ξ defs χ/ϑ (t721u BLOCK cause) | CLEARED (defs only, no numeric cells) | AW-α aac04151… |
| outer_even/odd form | CLEARED (defs/schema; tables EMPTY) | O-α b467bb54… |
| path pick / branch / ψ (R-B0, path) | CLEARED (i∞→x; principal = ACCEPT-default NOT Written HD — soft flag) | PB-α c26b5f72… |
| contour / ε (R-D3) | CLEARED regularized-only ε≥0.02; no Abel thm; F3 real-x NOT controlled | E-α 82d6976d…/72b9cfb4…; Written c85448e8…; Auditor CONFIRM pending |
| slash (R-E2) | scoped: R-NV0 exact Fraction fit c97ec8d5… (not Written law) | t740u |
| ledger HOLD / ledger≡HD (G-2) | REMAINS — AW-X4/O-X4 NOT accepted | t761u accept LOCKs |
| X4 | REMAINS ABSENT | 2bb870b4… |
| R-C1 wall | REMAINS (stands) | STREAM LOCKs t740u–t761u |
| B3 | KEEP empty table (no data to feed) | b96ff7bd… |
| residual-C | OPEN | all LOCKs |
Net: definitional/contour blockers cleared; the substantive walls (R-C1, X4, ledger≡HD G-2) still block any fill that could be Cat A. A diagnostics-only reopen is technically possible; a fill is not supportable without inventing numbers.

## 3. Menu: see author_candidates/AUTHOR_WRITTEN_GA3_REOPEN_MENU_t761u_2026-10-25.md (rec G-α; G-β acceptable alternative). Nothing adopted.

## Falsifiers
F-nothing-CatA YES · F-G-A3-reopen NO (this package) · F-δ≡0 NO · F-Bridge-YES NO · F-4da09dec-revived NO · F-numeric-cells NO · F3 real-x NOT claimed.
Bridge PARTIAL; READY NO; residual-C OPEN; R-C1 stands; no order78. E-α Auditor CONFIRM had not landed at build time.
