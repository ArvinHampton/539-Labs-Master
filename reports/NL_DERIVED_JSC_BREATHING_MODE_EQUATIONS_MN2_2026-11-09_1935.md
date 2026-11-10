# NL DERIVED: JS-C with the S⁴ breathing mode — field equations, truncation consistency, local face closure (file 1 of 2)
2026-11-09, CST (America/Chicago). **NL derived proposal.** Nothing here is adopted. Junction status: **UNSOLVED** (19a88b19), unchanged.
Authority: OW b0b9ae7f (pursue), OW 90cec14c (S⁴ breathing mode, go, not adoption), OW 8b26c786 (KK Group A scope), OW 36683379 (citations).
Scripts: /workspace/nl-jsc-1905/ (every .py and .log has a .sha256 sidecar). Companion: NL_DERIVED_JSC_BREATHING_MODE_SHOOT_MN2_2026-11-09_*.md.

**Tally: PROVED 6 · CONDITIONAL 2 · OPEN 2 · REFUTED 1 · total 11**

## 0. Scope
- **E0 (PROVED).** The breathing scalar (overall S⁴ scale, constant on Σ, even under the wall ℤ₂) is invariant under Aut⁺(Bolza) (order 48) × wall ℤ₂. It lies in KK Group A (8b26c786) and inside the 49b04146 scope. Reason: it is a function of the transverse coordinate only.

## 1. Truncations that keep the breathing mode
- **E1 (PROVED).** The SO(5)-singlet ansatz
  ds² = e^{2A}dx²₍₁,₃₎ + dy² + e^{2B}ds²(H²) + e^{2C}ds²(S⁴), G₄ = Q vol(S⁴), q := Qe^{−4C}
  is a consistent truncation of 11D supergravity (symmetry principle: it keeps all SO(5)-invariant modes, and H²/Bolza is locally homogeneous). With S := 4A′ + 2B′ + 4C′ and L = 1, the equations are:
  - A″ = q²/6 − A′S
  - B″ = q²/6 − e^{−2B} − B′S
  - C″ = −q²/3 + 3e^{−2C} − C′S
  - constraint: ½(S² − 4A′² − 2B′² − 4C′²) − ½(−2e^{−2B} + 12e^{−2C}) + q²/4 = 0.
  Check: the AdS₅ fixed point A′ = −1, e^{−2B} = 4, e^{−2C} = 8/3, q² = 24 has residuals 0 and constraint 0 (singlet_toy_shoot.log).
- **E2 (PROVED).** This class does not contain MN2. MN2 needs the twist Dφ₁ = dφ₁ + du/v and the squashing X_a = 2^{−3/5} ≠ X_b = 2^{2/5}. Neither is SO(5)-invariant. The fixed point in E1 is the untwisted, round-S⁴ "(D)-type" vacuum.
- **E3 (REFUTED, counterexample).** Claim: "the uniform-breathing ansatz on the MN2 CLP uplift is consistent". The ansatz is: 7D block × D̃^{1/3}e^{2γβ}, S⁴ block × e^{2β}D̃^{−2/3}, squashing fixed at the MN2 values, G₄ r-independent with no r- or x-legs. With that G₄, T_{rχ} = 0 identically, so Einstein needs R_{rχ} = 0. Counterexample (40-digit mpmath, mn2_breathing_consistency_v3.log): at β′ = 0.5, β″ = 0.1 and χ = 0.7, R_{rχ} = −0.4663059673 for every γ ∈ {−1, −2/3, −1/2, −1/3, 0, 1/2, 1}. Control at β = 0: R_{rχ} ≈ 10⁻⁴². So the ansatz is inconsistent for any γ.
- **E4 (CONDITIONAL, on a numerical identification).** R_{rχ} = (3/2) β′ ∂_χ ln D̃ exactly, independent of γ, f, g and β″. The ratio is 1.5000000000 at all 15 sampled points (mn2_breathing_linearity_v3.log). This vanishes only if β′ = 0 or X_a = X_b. The X_a = X_b case agrees with E1. Hence, within this ansatz, **MN2 permits no breathing profile**. The condition is a closed-form proof of the identity, which has not been done.
- **E5 (OPEN).** A consistent MN2 truncation that keeps a breathing mode has not been derived. It would need a χ-dependent breathing β(r,χ), a varying squashing, or G₄ with dr∧dχ legs (to source T_{rχ}). That is a KK/PDE problem. The breathing mode is not in the 7D maximal S⁴ truncation, where the S⁴ volume is fixed by the unimodular SL(5) scalars. The massive breathing truncations (hep-th/9807051, hep-th/0003286) are SO(n)-singlet only, i.e. E1's class. These citations were read for the claim, not re-derived.
- **E6 (OPEN).** Whether the Cassani–Josse–Petrini–Waldram N=2 truncation (arXiv 2011.04775) around MN2 contains an S⁴-volume scalar is unverified. Its math was not checked here, so nothing rests on it.

## 2. Local face closure (λ′ = 0, k_Σ = k_x, k_fib = −2k_x, tension = charge)
- **E7 (PROVED, singlet truncation).** Israel conditions on the IR-kept side, with face data A′ = B′ = a (k_Σ = k_x) and C′ = −2a (k_fib = −2k_x). There is no squashing scalar, so λ ≡ 0 and λ′ = 0 holds trivially. Then tension = charge (σ = q/κ²) gives **a = q/6**, and ρ = 6k_x/κ² with k_x > 0. This confirms task-1 C4 in a consistent truncation.
- **E8 (PROVED).** Substituting E7 into the constraint gives −9a² + q²/4 + e^{−2B_w} − 6e^{−2C_w} = 0. So the wall must satisfy **e^{−2B_w} = 6e^{−2C_w}**. The wall data form a one-parameter family [A′, B, B′, C, C′] = [a, −½ln(6e^{−2C_w}), a, C_w, −2a], with a = Qe^{−4C_w}/6. Constraint residuals are ≤ 6·10⁻¹⁴.
- **E9 (PROVED).** If both Σ and the fibre are flat, the constraint holds identically (the BPS M5 wall). The relation in E8 is the curvature cost of a curved Σ and a curved fibre.
- **E10 (CONDITIONAL on E4).** On MN2, the C4 closure is not realizable in the uniform ansatz. C4 needs β′ = −2f′/(1+2γ) ≠ 0 at the face (since k_x > 0), but E4 forces β′ = 0. The local closure is algebraically consistent, but no consistent bulk carries it off the face.

## 3. Bottom line for file 1
- The breathing-mode face closure is **confirmed** only in the SO(5)-singlet truncation, which does not contain MN2 (E1, E2, E7, E8).
- On MN2, the natural uniform-breathing ansatz is **refuted** (E3). The blocker is E5/E6: a consistent breathing truncation around MN2.

## 4. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 6 | E0, E1, E2, E7, E8, E9 |
| CONDITIONAL | 2 | E4, E10 |
| OPEN | 2 | E5, E6 |
| REFUTED | 1 | E3 |
