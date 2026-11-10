# NOTES: BATCH7_RTA_GEOM
## Sources
- K⁺ complex: /tmp/repo539/docs/S2-11DM2ET-X-Axiomatic-Book/scripts/architecture_A4plus_probe.py (build_complex mode "A2_enrich", atoms, core_q0; imported read-only). Docs: Architecture_A4plus_Continuous_BSpin.md, Architecture_A4_BSpin_Lift.md, architecture_A4plus_results.json (same folder). Counts V = 539, E = 594, F = 56 and β = (1,0,0) over F₂: grok-chats/13-t3-vs-hqcc.md line 45.
- Form SS: /tmp/repo539/docs/S2-11DM2ET-X-Axiomatic-Book/Residual_Form_Spectral_Sequences.md (E₁/E₂ over Q; collapse at E₂, lines 205–207) and Thin_Complex_Formality.md §1.

## Process fix (as required)
All modular numbers in the PREREG come from scripts/modular_table.py → data/modular_table.json, both hashed in the PREREG. Nothing was typed by hand.

## Remarks
- The K⁺ boundary orientation is the standard simplicial one (sorted vertices). Over F₂ it agrees with the probe's GF(2) incidence, and it reproduces the written β over F₂.
- Pattern: K⁺, P⁺, the permanent-class survival test and the fibre counts are all either contractible/acyclic or carrier-forced. The residual topology carries no prime-dependent or character-dependent signal for the 35-component law vector data to hit.

## Sharpest next step
- The residual-internal levers are now exhausted in an honest sense: the written residual complexes are acyclic over every tested prime, and the cheap invariants are carrier-forced.
- The only remaining non-vacuous route is the **Resonant side**, which needs a written object: a 539-step Π word, a ±1 grading on O_res, or a path predicate (C6/C10/C11/E1–E3).
- Alternative: written F_p differentials for the thin form complex (unblocks C27).
- Recommend pausing new residual-side maps until one of these is written by Arvin.
- order21 and the paper were not touched. CORE_FREEZE; new files only; no push, no sends.
