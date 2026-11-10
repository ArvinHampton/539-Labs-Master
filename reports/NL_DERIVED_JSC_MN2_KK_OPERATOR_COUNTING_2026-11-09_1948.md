# NL DERIVED: T7 sector around MN2 — KK operator (partial), IR falloffs, and the wall-vs-IR count
2026-11-09, CST (America/Chicago). **NL derived proposal.** Nothing here is adopted. Junction status: **UNSOLVED** (19a88b19), unchanged.
Authority: OW 90cec14c. Scope: KK Group A, Aut⁺(Bolza) of order 48 × wall ℤ₂ (OW 8b26c786, 49b04146).
Builds on: …MN2_BREATHING_TRUNCATION_STATUS_2026-11-09_1943.md (b103f08f…), items T7 and T8; …SHOOT_MN2_2026-11-09_1936.md (358c4b09…), items S1–S3.
Scripts: /workspace/nl-jsc-1947/ (cgr_level0_masses.py 7bf0412d…, log 5ac90deb…; selfdual_stress_check.py df221f28…, log b91d362c…), all with sidecars.

**Tally: PROVED 4 · CONDITIONAL 2 · OPEN 2 · REFUTED 0 · total 8**

**Assumption, stated up front:** χ-smearing of the wall sources (an M5/instanton density n(χ) on S⁴) is an assumption. No Owner record fixes it. f825dfff fixes only the total, N_M5 + n_inst = 9760.

## 1. KK operator and spectrum
- **K1 (PROVED; my own computation from the CGR potential, arXiv 1906.08900 eq. 3.8).** The H-invariant scalars that come from 7D supergravity (φ, λ; Σ-zero-mode, SO(2)×SO(3) singlets) have masses at MN2 of m²L² = **−4** and **+12**, i.e. **Δ = 2** (at the BF bound) and **Δ = 6**.
  - The gradient vanishes at the vacuum e^{30φ} = e^{10λ} = 2, and g²L² = 2^{4/3}. Both agree with CGR eq. 6.2.
  - These are exact eigenmodes of the T7 linear operator, because the (φ, λ) sector is a consistent truncation. Neither one is a uniform S⁴ breathing mode (1943, T3).
- **K3 (OPEN).** The higher H-invariant spectrum on MN2 (genuine χ-dependent modes of β, X and the G₄ dr∧dχ components) was **not computed**.
  - It requires the gauge-fixed linearization of all H-invariant 11D fields: about 8 metric functions plus 7 G₄ components of (r,χ), with regularity at χ = 0 and π/2. Its eigenproblem is quadratic in the radial exponent.
  - I did not get that to a converged, gauge-checked state, so no numbers are reported.
  - The count in §3 uses only n_rel ≥ 1, which K1 supplies. It does not depend on the rest of the spectrum.

## 2. IR (AdS₅ end) falloffs
- **K2 (PROVED).** Take a mode of dimension Δ about the IR AdS₅, with Poincaré coordinate z and the IR at z → ∞. The linearized radial solutions are z^{4−Δ} and z^{Δ}; at Δ = 2 they are z² and z² ln z.
  - A branch that decays in the IR exists **iff Δ > 4**. At Δ = 4 the branch is constant, i.e. marginal.
  - So the codimension of the IR-regular set is **1 per mode with Δ ≥ 4** and **2 per mode with Δ < 4** (relevant modes).
  - Applied to K1: the Δ = 2 mode gives codimension 2, and the Δ = 6 mode gives 1.
  - This matches the singlet toy, where both modes are irrelevant (S1: m²L² = 8 and 48).

## 3. Wall data under T8, counted against the IR codimension
- **K4 (PROVED).** Pointwise in χ, the C4 face data (K_x = k, K_Σ = k, K_fib = −2k) give an Israel stress with ρ = 6k/κ², P_x = P_Σ = −ρ and P_fib = 0. That is exactly a 5-brane on ℝ^{1,3} × Σ, smeared over S⁴. NEC holds for k > 0 (script). So with the breathing mode, the 6:8:8 NEC obstruction of aeb9ab13 is absent locally.
- **K5 (CONDITIONAL, on the E₈ instantons being (anti-)self-dual along S⁴-fibre 4-planes).** A self-dual field on those 4 directions has zero stress along them (checked numerically to 10⁻¹⁶). It has tension-like stress −¼F² along x and Σ, the same as an M5 on ℝ^{1,3} × Σ, and its Bianchi charge enters G₄ with the same sign. So the **n_inst/N_M5 split does not appear** in the bulk equations or in the Israel conditions, and it is not a free wall parameter.
- **K6 (CONDITIONAL, on χ-smearing being admissible and on genericity).** Count on M retained χ-harmonics with N physical modes; P is the reduced phase space, of dimension 2N.
  - **Wall data** are the field values (N; the squashing modulus X(r_w, χ) is among them), plus the source harmonics of n(χ) (M − 1; harmonic 0 is fixed by 9760).
  - **Conditions on the wall data:**
    - the Hamiltonian constraint, one per harmonic (M); in the toy this is what forced e^{−2B_w} = 6e^{−2C_w};
    - the momentum (rχ) constraint, M − 1 conditions. This is the force-balance (conservation) equation of the smeared branes, so it fixes n(χ) instead of leaving it free.
  - So the wall set has dimension N + (M − 1) − M − (M − 1) = N − M.
  - **The IR-regular set** has dimension N − n_rel (K2).
  - **Expected intersection dimension:** (N − M) + (N − n_rel) − 2N = **−M − n_rel ≤ −(M + 1)**, using n_rel ≥ 1 from K1.
  - Calibration: for M = 1 with no source freedom this gives −1 − n_rel. The singlet toy (n_rel = 0) gives −1, which matches S3/S4.
  - **Outcome:** the χ-smearing freedom is used up by force balance, and the split adds nothing (K5). The problem is overdetermined by at least M + 1. **Solutions are generically not possible, so no 2D boundary-value problem was set up and no shoot was attempted.**
- **K7 (OPEN).** The non-generic loophole. The count assumes the Hamiltonian, momentum and IR conditions are independent. Special structure could make them dependent, e.g. a supersymmetric (calibrated) wall cutting a BPS flow, where first-order equations replace the second-order ones. Whether such a BPS end-of-world wall compatible with the odd HW-type ℤ₂ wall exists on MN2 is open.

## 4. Scope
- **K8 (PROVED).** Every mode used here (the φ, λ zero-modes, the χ-dependent T7 fields and n(χ)) is constant on Σ up to the twist compensator and even under the wall ℤ₂. All of them are in KK Group A.

## 5. Junction impact
- With the breathing mode the face becomes NEC-compatible locally (K4). Globally, though, the T7 counting is overdetermined (K6). The extra freedom T8 listed (the squashing modulus, the split, χ-smearing) does not offset this: the squashing modulus is ordinary wall data, the split drops out (K5), and the smearing function is fixed by force balance.
- The breathing-mode route to the junction is therefore generically closed, up to K7 (a BPS/non-generic wall) and the uncomputed spectrum K3, which cannot reduce the deficit below M + 1.
- **The junction remains UNSOLVED.**

## 6. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 4 | K1, K2, K4, K8 |
| CONDITIONAL | 2 | K5, K6 |
| OPEN | 2 | K3, K7 |
| REFUTED | 0 | — |
