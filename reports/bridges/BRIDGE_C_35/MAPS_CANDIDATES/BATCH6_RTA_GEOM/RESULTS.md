# RESULTS: BATCH6_RTA_GEOM
PREREG.md sha256 0f19ed3d0168cee1c670b3e5f955b2003fde17e08333d4d9e823a3a36e2bc49c, hashed before tests. Script scripts/b6.py (imports the source probe's atoms()/tower_of() read-only; hash in scripts/SHA256SUMS); data data/b6.json; log logs/b6.log. Exact (sympy ranks), under 1 s.

Gates: 56 triples, 3 in the window, 53 in the tower region. All OK (the written counts are reproduced).
Triple start fibres (i mod 8), counts r = 0..7: **[13, 0, 1, 14, 13, 1, 1, 13]**. E = 28, Od = 28.
Window triples: (0,1,2), (7,8,9), (14,15,16), with starts mod 8 = 0, 7, 6.
All 56 triples are consecutive runs (i, i+1, i+2) and pairwise disjoint. Chord-zero proxy: global 0, and 0 in every fibre.

| Map | Prediction | Measured | Verdict | Vacuous? |
|---|---|---|---|---|
| C21 (51/54) | Od < E and E − Od ≤ 3 | E = Od = 28 | **FAIL** | — |
| C22 (χ₁₄₀) | n₂ = n₃ = n₅ = 0 | n₂ = 1, n₃ = 14, n₅ = 1 | **FAIL** (see datum error) | — |
| C23 (RG1′ → path H²) | proxy_r = 0 for all r, global 0 | all 0 | PASS | **yes, vacuous** (flagged in the PREREG: disjoint consecutive rows ⇒ full row rank, Category A) |
| C24 (three thetas → window triples) | distinct start fibres | 0, 7, 6 | PASS | **yes, carrier-forced** (see below) |
| C6, C10, C11, E1–E3 | — | blocked | OPEN | — |

**Bridge: NO.** The two passes are vacuous or carrier-forced; the two discriminating maps failed.

## Post-hoc analysis (verdicts unchanged)
- **C24 is carrier-forced (Category A).** The window triples start at i = 0, 7, 14: the core step 9 against tower width 21 puts 3 core points in a tower every 7 indices (63 = 3·21) in the 21-wide region. 7k mod 8 for k = 0, 1, 2 gives 0, 7, 6, which are always distinct. No modular datum enters, so the pass is not evidence.
- **C22 datum error (disclosed).** The PREREG transcribed χ₁₄₀(2r+1) as [1,1,0,0,1,0,1,1]. The correct values (sympy) are **[1, −1, 0, 0, 1, −1, 1, 0]**, so the true zero set is {2, 3, 7}, not {2, 3, 5}. C22 is recorded FAIL under its literal rule. The intended χ-tied map would also fail (n₇ = 13 ≠ 0). No rescue; the hashed PREREG is not edited.
- The fibre profile [13,0,1,14,13,1,1,13] concentrates on r ∈ {0,3,4,7}, because triples are spaced by 7 or 8 on the core. This is carrier arithmetic again.
