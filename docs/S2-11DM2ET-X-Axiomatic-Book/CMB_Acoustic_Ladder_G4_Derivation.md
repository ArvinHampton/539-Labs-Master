# CMB acoustic ladder from G4

S²-11DM²ET-X · Category B continuum mapping · 2026-09-20

Pack+(S). Residual-flux provenance mandatory. RESIDUAL_CORE_FREEZE holds.
Twin Prime and RH unclaimed. Continuum G4 mappings stay Category B.
This note replaces ΛCDM for TT peak *positions*. It does not subtract a Planck spectrum.

Canonical constants: `CLOSED_CONSTANTS.md`.
G4 = 539.9 s. D = 11. Cubic +U measure = 3^3 = 27.


## 1. Retired claim

Retired: CMB dip at ℓ = 539.9.

Planck 2018 TT peak 2 is ℓ = 538.1 ± 1.3, amplitude 2586 ± 23 μK².
That is a local maximum of C_ℓ (first rarefaction). A dip is a local minimum.
Nearest Planck troughs: 416.3 and 675.5. The large-scale dip is ℓ ~ 20-27.

The model does not usurp ΛCDM by painting a hole on ΛCDM. It generates the ladder.


## 2. Derivation

Leakage kernel already in the model:

    sin(2 π t / G4)
    cos(2 π t / (G4 h_j (1 ± δ(t)/G4) k_seg))

On the last-scattering 2-sphere this is an angular harmonic in h_j.

Peak 1 is first compression, not a completed 2π of the kernel, so it carries the bulk-to-3-volume ratio:

    ℓ_1 = G4 · D / 3^3 = 539.9 · 11/27 = 219.959...

Peak 2 is the first completed flux period (first rarefaction):

    ℓ_2 = G4 · 1 = 539.9

Peak 3 is the model half-integer overtone h_j = 3/2:

    ℓ_3 = G4 · 3/2 = 809.85

Peak 4 is the first binary subdivision of the second unit, 2 + 1/8 = 17/8:

    ℓ_4 = G4 · 17/8 = 1147.2875

Trough 2 is 5/4:

    ℓ_T2 = G4 · 5/4 = 674.875

Do not generate these from ΛCDM ℓ_A = π/θ_*.
Optional dictionary only:

    ℓ_A^(model) = G4 (μ - 1) = 539.9 · 0.55 = 296.945

That shadow is worse than the direct G4 harmonics and is not the ladder generator.


## 3. Planck 2018 TT comparison (positions only)

| extremum | Planck | model | fraction | residual | status |
|----------|--------|-------|----------|----------|--------|
| peak 1 | 220.6 ± 0.6 | 219.96 | 11/27 | -0.29% | CLOSED |
| trough 1 | 416.3 ± 1.1 | 417.20 | 17/22 | +0.22% | open |
| peak 2 | 538.1 ± 1.3 | 539.9 | 1 | +0.33% | CLOSED |
| trough 2 | 675.5 ± 1.2 | 674.88 | 5/4 | -0.09% | CLOSED |
| peak 3 | 809.8 ± 1.0 | 809.85 | 3/2 | +0.006% | CLOSED |
| trough 3 | 1001.1 ± 1.8 | 1002.67 | 13/7 | +0.16% | open |
| peak 4 | 1147.8 ± 2.3 | 1147.29 | 17/8 | -0.04% | CLOSED |
| trough 5 | 1623.8 ± 2.1 | 1619.7 | 3 | -0.25% | open |

CLOSED set = {G4, 11, 27} union h_j in {1, 3/2} and the first half-integer / eighth.
Heights are not in this note. They belong to kappa_dark = 243/539 and the z-sum.


## 4. Spectrum without a ΛCDM prior

    C_ℓ = A_{H-QP} Σ_n H_n(κ_dark, ρ_DM, N_z^-) P(ℓ - ℓ_n[G4, 11])
         + δC_ℓ^{-U} sin(2 π ℓ / G4 + φ_11)

H_n is loading. P is a peak kernel. δC_ℓ^{-U} rides on the model peaks.


## 5. Still open (do not promote)

- EE extrema (must sit halfway between TT if the oscillator phase is π/2)
- Silk damping tail
- BAO: r_s from D2-brane leakage versus DESI DR2, no hand insertion of 147.09 Mpc
- odd/even height ratios from κ_dark and Σ_z β_z (N_z^- - 2 Z_z^-)

Front-facing copy: https://github.com/ArvinHampton/S2-11DM2ET-X
Validator: scripts/cmb_g4_ladder.py
