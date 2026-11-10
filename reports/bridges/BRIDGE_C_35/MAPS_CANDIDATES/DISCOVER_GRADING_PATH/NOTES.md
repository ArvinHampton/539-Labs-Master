# NOTES: DISCOVER_GRADING_PATH
## Pivot
On Arvin's correction ("It will need to be computationally discovered") I stopped the written-source hunt. It had produced only rg file lists: no INVENTORY was written, no HUNT_GRADING_PATH folder was created, and no written grading or predicate was confirmed. Earlier negative findings stand: reports/crypto/RPP_spec_v1/RESIDUAL_T3_predicate_sources.md and RPP_formal_statement.md.

## Method
1. Exploration (scripts/explore.py, hashed before the PREREG): T3 mod 27 → mod 9 determinism; charge-transition matrix; 200 exploration seeds b"explore-s"; tower-parity grading fibre sums [10, 12, 12, −13, −13, −11, −13, 13] (g total −3).
2. PREREG of D1–D5 with exact definitions; holdout seeds b"holdout-s", s < 1000.
3. Tests; then a post-hoc diagnosis of the D3 FAIL, which led to Lemma V.

## Disclosures
- The source rule (Architecture_A_Ores_Programme §6, quoted in RESIDUAL_T3_predicate_sources.md §3) bars carrier functions on T♯ orbits unless they are labelled a free-dynamics probe. P_res and β̂ are so labelled (Option 3). They are **not** residual-carrier definitions and **not** Arvin-written.
- The D5 parenthetical bound was wrong; disclosed in RESULTS.
- The post-hoc mod-8 log reused holdout seeds 0–299; it is diagnostic only.

## What still blocks C6/C10/C11/E1–E3
- C6/C10 need a specific 539-step Π word. Discovery gives a predicate family on all T3 paths, not a unique Π. To unblock, Arvin must accept (or reject) P_res/β̂ as "the residual constraint on Π".
- C11 needs a ±1 grading. g = (−1)^τ is now an exact candidate; C11's prediction (68-block sums 0, 67-block defect ±1) can be tested **only after** Arvin accepts g, with a new prereg.
- E1–E3 also need the T3 q-series, which is not discovered here.

## Sharpest next step
- New PREREG: an exact Markov chain for T3 on residues u mod (4·9·8 = 288), or deeper, computed by a hashed script, predicting the 8 β̂ hit frequencies. Test on fresh seeds (b"fresh-s").
- A pass would make the path → fibre map β̂ quantitatively predictable from first principles. It is still residual-internal and still no bridge, but it is the first exact path predicate with content.
- Separately, ask Arvin whether g = (−1)^τ and P_res are acceptable as the grading and predicate before re-running C11/C10.
- order27 and the paper were not touched. CORE_FREEZE; new files only; no push, no sends.
