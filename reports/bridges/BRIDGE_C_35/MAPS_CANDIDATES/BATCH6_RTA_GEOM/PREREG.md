# PREREG: BATCH6_RTA_GEOM (Map-C21 to Map-C24): the 56 P⁺ same-tower triples and the chord-zero path-H² proxy over the 8 fibres
Written 2026-10-24 at about 7:10 PM CDT, before any BATCH6 test. Owner: Arvin Hampton. New files only. CORE_FREEZE. All maps are **Category B**. A pass is a survived prediction, not a bridge; a pass flagged vacuous carries no weight. order21 and the paper are not touched. C15–C20 are not reopened. No Π, grading or predicate is invented. Runs: nice, OMP_NUM_THREADS=1, ulimit -v 3000000.

## Written objects (computed by importing the source probe's own functions)
Source: /tmp/repo539/docs/S2-11DM2ET-X-Axiomatic-Book/scripts/residual_p_plus_multiscale_probe.py. Functions atoms() and tower_of() are imported read-only.
- O: the probe's core, O = residual[i] with i % 9 == 0 (this equals 21+9j).
- Triples: all 3-subsets (i,j,k) of core indices in one tower bucket that has ≥ 3 elements (written count 56).
- Window: W = 18. The written split is 3 in the window (k < 18) and 53 in the tower region (i ≥ 17).
- Chord-zero matrix A (56 × 538): row t has a 1 at column i if j = i+1, and a 1 at column j if k = j+1. Proxy = 56 − rank A.
- Gates (else VOID): 56 triples; in-window count 3; in-tower count 53.
- Fibre of a triple: β♯ of its **start index** i, i.e. i mod 8. This is an operational convention fixed here; the sources do not assign triples to fibres.
- Per-fibre proxy: proxy_r = n_r − rank(A restricted to rows with i ≡ r).

Modular data (written): P-odd/P-even symbol split 51/54 (C3_RUN post-hoc); χ₁₄₀(2r+1) for r = 0..7 is [1, 1, 0, 0, 1, 0, 1, 1]; the three unary-theta norms 5/2, 1/34, 35/4 (three distinct thetas).

## Map-C21 (51/54 split → parity of fibres)
Prediction: let E = #triples with even start fibre and Od = # with odd start fibre (E + Od = 56). Then Od < E and E − Od ≤ 3 (mirroring 54 − 51 = 3).
PASS iff both hold.

## Map-C22 (χ₁₄₀ → forbidden fibres)
Prediction: no triple starts in a fibre r with χ₁₄₀(2r+1) = 0, i.e. r ∈ {2, 3, 5}.
PASS iff n_2 = n_3 = n_5 = 0.

## Map-C23 (RG1′ zero-set "iff" structure → chord-zero path H²)
Prediction: proxy_r = 0 for every fibre r, and the global proxy = 0.
**Flagged in advance as possibly vacuous:** if the 56 triples are pairwise disjoint consecutive runs, then A has full row rank by construction, and a pass is vacuous (Category A). The script records disjointness.

## Map-C24 (three unary thetas → the 3 window triples)
Prediction: the 3 in-window triples have pairwise distinct start fibres i mod 8.
PASS iff the three start residues are distinct.

## Still OPEN (blocked): C6, C10, C11, E1–E3.
