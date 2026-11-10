# NOTES: BATCH3_RTA_GEOM
## Task 1: search for a written Π / grading / fibre labelling / predicate
Searched (rg, case-insensitive) /workspace/quantum-comp/** and /tmp/repo539/** for: "539-step (word|path|trajectory|sequence)", "Π =|\Pi =|resonant path problem", "grading on O_res|±1 grading|sign grading|Z/2 grading", "block label|fibre block [0-9]|block index", "residual predicate|path predicate". Hits read:
- reports/crypto/RPP_formal_statement/RPP_formal_statement.md: Π is defined as the fixed 539-step T3 body of HQH-539 on u₀ = SHA3-512(m‖s), with "optional residual constraints" that are never specified.
- reports/crypto/RPP_spec_v1/RESIDUAL_T3_predicate_sources.md (2026-10-23): explicit finding that **no source defines a map from a path or T3 value to O_res, a fibre or the permanent class**. It also quotes Architecture_A_Ores_Programme §6, which bars carrier functions on T♯-orbits.
- reports/crypto/RPP_spec_v1/scripts/n_residual_filter.py: a *candidate* fibre map (u mod 539 → interval blocks), labelled as a candidate, not sourced.
- U1_LEDGER_PPT_R_Obstruction_Written_Data_2026-09-14.md (both trees): PR9, "A count is not a clock."
**Found:** written definitions of the fibre labelling β♯(x_j) = j mod 8 (residue classes of the sorted index, NOT intervals), the canonical core x_j = 21+9j and towers τ. **Not found:** any 539-step Π word, any ±1 grading on O_res, any path predicate. C6, C10, C11 and E1–E3 stay OPEN and were not re-hashed.

## Correction to batch 1
MAPS_CANDIDATES Map-C4 used consecutive interval blocks. The written fibres are j mod 8. C4's FAIL stands for the interpretation it preregistered, but that interpretation does not match the source. A source-faithful C4 would need a new prereg.

## Other notes
- 67/68 were not used as targets.
- Order19 was not touched. C15 is written so that order19's final k can be plugged in.
- **Sharpest next lever:** the charge-class obstruction (x ≡ 3 mod 9) shows that any modular→O_res map through quadratic-form representation must respect the mod-9 charge. The next well-posed candidate should use a written carrier function that is mod-9-blind: β♯, τ, or the permanent class on K_9 × P_{B′}. Example: RG1′-type reflections acting on the product complex K_9 × P_{B′}, predicting the sign of α(a,b) = sgn(a−b) under σ. This is written and Category A on the residual side.
- CORE_FREEZE; new files only; no push, no sends.
