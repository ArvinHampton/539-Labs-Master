# order9 RESULTS (unit-arc test). Prereg: PREREG.md (sha256 in PREREG.sha256, hashed before numerics).
## Coefficient identities (mpmath, 105 companions; data/u.json, logs/u.log)
- Geometry (Cat A): arc length log eps = 2L = log(6+sqrt35) = 2.47789; e1e2 angle = L, so [c1, gamma c1] is two orthant-widths.
- U1  c_HPhi0(N) = c_E(N)+c_gammaE(N): **FAIL** (max |diff| = 2.0, integer miscount on boundary/overlap rays; predicted FAIL). Category B (falsified).
- U2  c_HPhi0(N) = c_{C_arc}(N): **pass** (max 1.74e-9 at dps 30, all 105 rows). Category B (numerical, exact-integer target).
- U3  Hecke/<gamma>-orbit completeness: **pass** (max 0). gamma-invariant companions: 0,12,18,23,29,35,47,53,58,64,70,82,88,93,99.
## Radial (rational x, t-grid; preregistered rule thresholds 1e-5)
- R1 Theta_E, 7 terms/8 pts: x=1 pass (3.7e-7); x=1/3 pass (5.2e-6); x=1/4 **inconclusive** (A2 err 1.2e-4 > 1e-5, by prereg rule; no refit counted).
- R2 Theta_{C_arc} A0 vs prediction: x=1 pass (7.5e-11); x=1/3 pass (9.0e-11). A0(C_arc)=2·A0(E) observed.
- order8 M2 (5 terms/6 pts) is recorded as **FAIL** under its preregistered rule (A2 err to 1.15e-3); m2posthoc refit is descriptive only.
- order8 M2a A0 checks are NOT counted as evidence (they rediscover parent Lemma 2 / 2L = log(6+sqrt35)).
## Parity obstruction M^2 = 35·P — now exact (Category A)
data/cyclo.json: M^2−35P evaluated under all 3360 embeddings of Z[e(1/9800)]; max |entry| = 1.8e-14 < 1/2. Entries are algebraic integers, so all-conjugates <1 ⇒ norm 0 ⇒ identity exact. (Replaces the prior 30-digit-only check.)
## Verdict
Theta_E + gamma(Theta_E) = H(Phi0): **FALSIFIED** as stated (U1). Corrected identification H(Phi0) = Theta_{C_arc} holds (U2, U3); Theta_E = H(Phi) is an identification (not a Residual–Resonant bridge).
Full-series xi-shadow: **NOT located.** H(Phi0) is the holomorphic projection of a weight-0 object; it gives no weight-3/2 unary theta shadow for the even piece. Known shadow pieces remain three distinct unary-theta series (5n²/2 shared), not four.

## Open next step
Compute xi_0 / Laplacian of the weight-0 Siegel lift Phi0 restricted to C_arc boundary rays (e2, gamma e2) to obtain the boundary unary theta terms; test them as the missing weight-3/2 shadow via exact coefficients; explain R1 x=1/4 A2 inconclusive with dps-40 t-grid.
