# U1 LEDGER — s = 8 and s = 11 analogues of the s = 7 Q(√35) mechanism; cusp onset — 2026-10-18

Package: `s8_s11_Analogues_2026-10-18/` (report `2026-10-18-s8-s11-Analogues.md`, verbatim, plus key scripts and text outputs).
See also `ERRATUM_s11_Genus_Count_2026-10-18.md` (the genus count for s = 11 is 4, not 2).
Pure copy-and-create. No locks altered. CORE_FREEZE holds. Distinct from HQCC termination claims. No TPC or RH claim. Residual ≠ Resonant.

## Category A (computed / checked; exact or to the stated finite range)
- A1. 2P_s = E_s + 1 + θ₃ − Θ_hol,s exactly as q-series to q^3000 for s = 7, 8, 11. (`series_s.py/.txt`)
- A2. E_s is a multiplicity-1 single-class ray-class generating function for each s: s = 8: Q(√3), order Z[2√3], ε = 2+√3, γ-eigenvalue ε² but no double counting (cone is a fundamental domain for ⟨ε²⟩ = U_{𝔪,1}); s = 11: Q(√11), order Z[3√11], ε = 10+3√11, modulus 𝔭₂(9)∞∞, one class of 48. (`rayclass_s.py`, `minmod_s.py`)
- A3. ζ_E(0), ζ_E(−1): s = 7: 1/10, 29/1200; s = 8: 1/6, 5/36; s = 11: 7/18, 1129/1296 (Shintani cones, 5 decompositions, and PARI Hecke L-functions agree). t^{±1/2} terms of E_s vanish; exact t^{−1}, t^{−1/2}, t^0 coefficients of P_s, E_s, Θ_hol (`asym_s.txt`). Baker obstruction carries over (citing Baker 1966).
- A4. S/T family: S unitary, S² = P, (ST)³ = I for all three s (PSL₂(Z) representation). s = 8: even lattice, all 48 components Eisenstein, cusp part 0. (`family_s.py`, `content_s.py`, `analyze_content.py`)
- A5. s = 11: u_L has a genuine dihedral cusp component (|Eis| = |cusp| = 0.204): 6 Maass forms with λ = 1/4 from 12 non-genus characters of conductor (3) and (9). Cusp function-space rank ≥ 73 of 110; ≥ 90 dihedral newforms (lower bounds). (`cusp_chars_11.py/.txt`, `cusp_dim.py`)
- A6. Herglotz closed form for the Eisenstein part: s = 8 to 3e-13 (5 complex points) and ≤ 3.9e-13 (8 rationals); s = 11 Eisenstein projection to 2.5e-13; ψ_cusp(x) ≠ 0 at 8 rationals for s = 11. So "ψ is purely Eisenstein" (true at s = 7, 8) is not family-wide.
- A7. Genus periodicity: s = 7, 8 genus-periodic (0 varying residues); s = 11 not (20 residues vary).
- A8 (counts; from the g_s package `cusp_onset.py`). h⁺ vs number of genera: equal for s = 3..20, 30 except s = 11 (8 vs 4) and s = 19 (8 vs 4); also s = 25 (12 vs 4), s = 41 (24 vs 8). Cusp onset at s = 11, 19, 25, 41 in the tested range.

## Category B
- Herglotz proof template transferred to s = 8 (inputs I1–I3 hold numerically; not re-audited). For s = 11 it proves only the Eisenstein projection.
- "h⁺ ≠ #genera ⇔ cusp part" as an explanation; predicted cusp parts at s = 19, 25, 41 (no decomposition run).
- Use of Herglotz_Eis on the real line for s = 11.
- Not done: L(0)-value identities for the s = 11 cusp rows.

## Caveats
- Finite ranges (q^3000, primes < 60000, stated norm bounds, ~1e-13 numerics). s = 11 cusp counts are lower bounds (84 of 396 components uncovered).
- Ray-class / L-function / character computations rely on PARI (known quirks handled by hand). The diagnostic `ecusp_8` run is inconclusive, not a failure.
- **Erratum:** the report's table lists genera = 2 for s = 11; correct is 4 (Cl⁺ ≅ Z/4 × Z/2). Conclusion unchanged.

## Normalisation note (ζ(−1))
The single-class ray-class values ζ(−1,𝒦) = 29/60, 5/12, 1129/36 and ζ_E(−1) = 29/1200, 5/36, 1129/1296 differ only by normalisation: N𝔞 = 20Q, 3Q, 36Q respectively, so Σ N𝔞^{−w} = c^{−w} ζ_E(w) and at w = −1 the factor is c (e.g. 29/60 = 20 · 29/1200).

## Files not included (binary / large)
`S_*.npy`, `T_*.npy`, `P_*.npy`, `raw_*.npy` (raw_11.npy 46 MB), all `content_*.pkl` (up to 14.9 MB), `ecusp_*.pkl`, `herg_terms_*.pkl`, `__pycache__/`. All regenerable by the included scripts.
