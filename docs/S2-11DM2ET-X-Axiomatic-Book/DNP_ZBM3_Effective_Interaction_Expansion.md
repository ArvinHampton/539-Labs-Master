# S2-11DM2ET-X Model: Expansion on the DNP-ZBM3 Effective Interaction (Addendum, 2026-08-01)

Author: Arvin B. Hampton (String Weaver), with xAI Collaboration

## Overview

DNP-ZBM3 is the effective shell-model interaction constructed for the A~80 region in the Nature Communications study of 84Mo and 86Mo. It combines realistic two-body matrix elements (JUN45 + LNPS/Kahana-Lee-Scott) with phenomenological monopole corrections that emulate the effects of three-nucleon forces. The resulting valence space is the union of the upper three pf orbitals (pseudo-SU(3)) and the lower three sdg orbitals (quasi-SU(3)), truncated to keep quadrupole coherence while remaining computationally tractable.

Within the S2-11DM2ET-X framework DNP-ZBM3 is treated as a concrete nuclear realization of the same ternary dynamical principles that underlie the Hampton Qutrit Collatz Convergence theorem. The monopole adjustments that shrink the N=Z=40 gap and restore the g9/2-d5/2 closure are the nuclear-physics counterpart of the residue-class selection rules and the minimal k_phys lift that enforce 11D flux-charge conservation.

Category status: the interaction and the shell-model calculations that employ it are standard nuclear theory (Category A computational nuclear structure). The identification of those monopole corrections with HQCC residue dynamics and 11D leakage is Category B framing only. The residual discrete algebraic objects (O_res, permanent class, K+, BSpin lift) remain untouched Category A pure mathematics.

## Construction Summary

- Two-body part: JUN45 (pf-g9/2) + selected LNPS matrix elements derived from the Kahana-Lee-Scott G-matrix.
- Monopole part: phenomenological shifts that (i) reduce the harmonic-oscillator N=Z=40 gap and (ii) restore the correct spin-orbit ordering of the g9/2 and d5/2 orbitals. These shifts emulate the known action of three-nucleon forces on shell evolution.
- Effective charges: 1.5e (protons), 0.5e (neutrons), standard for the quasi+pseudo-SU(3) space.
- Methods employed: pure quadrupole SU(3) estimates, projected Hartree-Fock, Discrete Non-Orthogonal Shell Model with variation-after-projection, and exact diagonalization (up to ~10^11 basis states for 86Mo).

## Role in the Observed Transition

Calculations with DNP-ZBM3 reproduce the large B(E2) of 84Mo (dominated by a single highly deformed triaxial 8p-8h minimum) and the reduced B(E2) of 86Mo (extensive mixing across the potential-energy surface). Removal of the 3N-emulating monopoles collapses the collectivity by more than an order of magnitude, confirming that three-nucleon effects are essential for the Island of Inversion.

## Framework Correspondence

The ternary map

T3(n) = n/3          (n ≡ 0 mod 3)
       (4n+2)/3      (n ≡ 1 mod 3)
       (2n+1)/3      (n ≡ 2 mod 3)

(with the physical charge-conserving lift of the ≡ 2 branch) supplies a discrete dynamical skeleton whose residue-class selection rules parallel the monopole-driven shell-gap evolution. The 539-step termination and the democratic distribution of the 4880 flux units across 243 Kaluza-Klein towers remain the global organizing principles; DNP-ZBM3 is a local effective theory living inside that skeleton.

## Implementation Notes for Future Work

- The DNP-ZBM3 monopole matrix can be stored as a sparse correction table for use in residual-flux provenance checks.
- Any future ab-initio derivation of the same monopoles from chiral 3N forces can be compared directly with the HQCC charge-conservation constraint.
- No modification is made to the immutable constants G4 = 539.90 s, N_flux = 4880, or the residual discrete stack.

## Provenance

Source: J. Ha et al., Nature Communications 16, 10631 (2025), Methods section and Table 1.
Model framing prepared under 539 Labs LLC. Residual-flux provenance mandatory for continuum claims.
