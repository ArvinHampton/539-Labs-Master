# NOTES: BATCH6_RTA_GEOM
## Sources re-read
- /tmp/repo539/docs/S2-11DM2ET-X-Axiomatic-Book/scripts/residual_p_plus_multiscale_probe.py: lines 60–76 (stokes_chord_zero), 80–112 (core, buckets, the 56 triples, window split), 196–213 (chord-zero A, path-H² proxy). atoms()/tower_of() are imported unchanged.
- /tmp/repo539/docs/S2-11DM2ET-X-Axiomatic-Book/P_plus_Permanent_Class_Survival_Optional_Lock_2026-08-08.md (56 triples: 3 in W = 18, 53 in towers).
- BATCH5 NOTES (survival sources); BATCH3/BATCH4 NOTES (x_j = 21+9j, β♯ = j mod 8).

## Disclosures
- Fibre of a triple = start index mod 8 is an operational convention, fixed in the PREREG.
- The χ₁₄₀ table in the PREREG was miscomputed by hand before hashing. Correct values are in RESULTS. Future preregs should compute data with a hashed script before writing them in.
- The path-H² chord-zero proxy is identically 0 (disjoint consecutive triples), so it cannot discriminate fibres. Like the BATCH5 survival test, it is too coarse.

## Pattern across BATCH3–6 (for Arvin)
Every written residual invariant tested so far (β♯ counts, τ occupancy, permanent-class survival, P⁺ triples, chord-zero H²) is governed by the carrier arithmetic: step 9 vs tower widths 21/20, and B′ ≡ 3 mod 8. The modular data (51/54, χ₁₄₀, theta norms, A2c support) have never predicted a non-vacuous feature. This is consistent with the Residual-vs-Resonant lock: no bridge.

## Sharpest next step
- On the residual side, the cheap written invariants are exhausted. Remaining options:
  - (a) A written invariant that is *not* a function of the carrier arithmetic alone. The candidates are the form spectral sequence pages or the K⁺ (V = 539, E = 594, F = 56) cell structure. A next prereg could predict a K⁺ Betti/torsion count over F_p for p | 140 versus p ∤ 140 from the modular datum.
  - (b) Wait for a written 539-step Π / ±1 grading (C6/C10/C11/E1–E3).
- order21 and the paper were not touched. CORE_FREEZE; new files only; no push, no sends.
