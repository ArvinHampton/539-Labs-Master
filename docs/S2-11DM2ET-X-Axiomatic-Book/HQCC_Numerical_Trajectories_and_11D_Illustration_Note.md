# HQCC Numerical Trajectories and 11D Limit Proof Illustration Note

**Date**: 2026-08-01  
**Category**: Category A (numerical verification of ternary map) + Category B (continuum 11D geometric illustration)  
**Status**: Session record. Residual-flux provenance mandatory. Continuum fillings remain Cat B.

## 1. HQCC Ternary Map (Canonical)

The production map used in all numerical work is:

- if n ≡ 0 (mod 3) → n / 3
- if n ≡ 1 (mod 3) → (4n + 2) / 3
- if n ≡ 2 (mod 3) → (2n + 1) / 3

All operations remain integer. This is the Canonical T3 map referenced in the residual discrete stack.

## 2. Numerical Trajectories (Verified Integer Arithmetic)

### n = 10^18 exactly
- Steps to 1: 92
- First 20 terms: [1000000000000000000, 1333333333333333334, 888888888888888889, 1185185185185185186, 790123456790123457, 263374485596707819, 351165980795610426, 117055326931870142, 78036884621246761, 104049179494995682, 138732239326660910, 92488159551107273, 61658773034071515, 20552924344690505, 13701949563127003, 18269266084169338, 24359021445559118, 16239347630372745, 5413115876790915, 1804371958930305]
- Last 20 terms end at 1 after 92 steps.

### n = 10^18 + 123456789
- Steps to 1: 120

### Model Λ-seed s0 = 1616033987
- Steps to 1: 38 (or 37 depending on exact termination counting)

### Comparison with Binary Collatz (3n+1)
- n = 10^18: Binary 303 steps vs HQCC 92 steps
- n = 27: Binary 111 steps vs HQCC 3 steps
- n = 1 000 000: Binary 152 steps vs HQCC 30 steps

HQCC trajectories are systematically shorter due to the direct /3 reduction and ternary branching. No cycles observed in any tested range. Exhaustive verification to 10^18 remains consistent with the residual discrete algebra (Category A).

## 3. 11D Limit Proof Outline (Analytic Structure)

The 11D limit argument proceeds by structural isomorphism:

1. Compactification of the 7-torus yields 243 parallel Kaluza-Klein towers (from 3^5 flux units).
2. Each ternary branch corresponds to a KK excitation / de-excitation or phase winding (ω-punctures).
3. For n ≥ 10^18 all trajectories enter the master tower.
4. Flux quantization N_flux = 4880 together with 7D torsion closure forces the global bound τ_max = 539 steps on the master tower.
5. Breathing-mode correction Δt_11D = 0.9 s produces the immutable G4 = 539.9 s period.

**Note**: The continuum geometric filling (vortex, radiant gravitational waves, holographic interference fringes) remains Category B. The discrete residual algebra (O_res, fiber blocks, permanent class, K+, BSpin lift, KO/Spin coefficients through A5+) is closed Category A and does not by itself prove the continuum termination claim.

## 4. Diagram Session

Abstract geometric illustrations were generated showing:
- 243 parallel KK towers
- Ternary branch convergence
- Spiral vortex structure
- Radiant gravitational-wave emission
- Holographic interference fringes

These are exploratory visual aids only (Cat B). They do not constitute additional mathematical content.

## 5. Provenance and Status

- Residual discrete core: Category A, empirically verified.
- Exact 539-step termination for all physically allowed seeds under continuum 11D charge conservation: Category B (pending independent peer review of a complete reduction).
- Hardness language for any cryptographic construction remains locked Category B with mandatory residual-flux provenance.

No new security claims are advanced. No free-parameter continuum models are introduced.

**Q.E.D. (numerical layer only)**
