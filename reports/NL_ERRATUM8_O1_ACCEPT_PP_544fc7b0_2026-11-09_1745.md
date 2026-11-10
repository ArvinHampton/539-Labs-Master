# NL erratum 8: accepting PP's audit 544fc7b0 of the O1 section (§A) of NL 1736 (additive)
Author: Non Local Path (NL). The derivations below are **NL derived proposals**.
Date: 2026-11-09, CST (America/Chicago). New file only. Nothing is edited, nothing is locked, and no vacuum, source or b is adopted. No CERT. Nothing sent outside. Tip 7cddb188 untouched.
Weekly usage was checked before starting: 39.7%, below the 90% stop.

- **Applies to:** NL_DERIVED_RESOLUTION_O1_MIXED_FACES_ODES_NONLINEAR_M5_2026-11-09_1736.md (13ccd162…), **§A only**.
- **Audit:** FINDINGS_PP_AUDIT_OWNER_PASTED_PARITY_FLIP_ANOMALY_2026-11-09_1745.md (sha 544fc7b0b0183022ad1d201933d28de3db9dc58d2a5a7e0b9103bf8675b6450c, equal to its sidecar).
- **Not touched:** §B–§D of 1736. PP's audit of them is still running.

## Standing premises
- **P-b.** The face Z₂ σ = (r → 2r_b − r) × τ is a symmetry of 11D supergravity, including **both** ∫C∧G∧G and ∫C∧I₈. This forces C₃ → s₁₁σ*C₃ (PP C0). It replaces 1736 A2's "CS term" wording; the conclusion is the same.
- **P-fix (stated explicitly as a premise).** The face is a Z₂ fixed plane, τ = id. It is **not** a consequence of the Israel algebra; see fix 1.

## Fixes
1. **Fixed point not implied by the Israel algebra.** The 1736 claim "[K] = 2K needs the face fixed pointwise" is retracted and is **REFUTED**.
   - Any face isometry τ with τ*h = h and τ*K = K gives the jump K(y) + τ*K(τ⁻¹y) = 2K(y).
   - K depends on the S⁴ only through μ_a², via Δ̃ = Σ X_aμ_a², so the S⁴ antipodal map is an example.
   - P-fix is therefore an explicit premise.
2. **O1 off a fixed plane.** The 1736 claim "if the face is not a fixed plane, O1 has no meaning" is retracted and is **REFUTED**. PD1 gives ε = s₁₁s₄ = −s_x s_Σ for any τ. Two cases are added:
   - **(i)** τ reverses the M5 worldvolume orientation (s_x s_Σ = −1), e.g. an anticonformal involution of Σ combined with φ_i → −φ_i. Then G₄ is **even** and the **net face M5 charge is 0**: the stack's image is an anti-stack.
   - **(ii)** τ preserves it (s_x s_Σ = +1), e.g. the S⁴ antipodal map, acting freely on the face. Then G₄ is **odd** and the net face charge is **2N_flux**.
   - O1 is undefined only when there is no Z₂ at all (two-sided gluing P1/P2).
3. **Brane count with E₈.** "N_b = 2N_flux" is replaced by **N_M5 + n_inst = 2N_flux** whenever the Hořava–Witten E₈ wall sector is present (CONDITIONAL, HW). N_b = 2N_flux ∈ 2ℤ holds only if n_inst = 0.
4. **Linking cycle.** The fibre S⁴ at a single radius does not link a stack on the face. The stack's linking 4-cycle in the transverse (r, S⁴) space is **S⁴(r₊) − S⁴(r₋)**, so the charge is **Φ₊ − Φ₋ = (1 − ε)Φ**. Odd parity gives 2Φ and even gives 0.

## 1736 §A, revised
- **A0r (REFUTED, fix 1).** "[K] = 2K needs the face fixed pointwise."
- **A1 (PROVED given P-fix).** τ = id, so s_x = s_Σ = s₄ = +1 and s₁₁ = −1.
- **A2 (PROVED given P-b).** C₃ → s₁₁σ*C₃. There is no C → −C at fixed orientation.
- **A3 (PROVED given P-fix and P-b).** The S⁴ flux and all face-tangent G₄ legs are odd; legs with one dr are even.
- **A4a (PROVED given A3 and Bianchi).** The net face M5 charge is 2N_flux.
- **A4b (CONDITIONAL on HW).** N_M5 + n_inst = 2N_flux.
- **A4c (PROVED, Stokes).** The linking cycle is S⁴(r₊) − S⁴(r₋), and the charge is Φ₊ − Φ₋.
- **A5 (PROVED given Witten quantization).** λ|_{S⁴} = 0, so Φ/(2πℓ_P)³ ∈ ℤ with no half-integer shift.
- **A6 (CONDITIONAL on HW).** A P-fix face needs an E₈ wall sector. Its instantons are brane-like and cannot cure the fibre-NEC deficit.
- **A7 (OPEN).** Anomaly inflow for an M5 stack on an HW wall. The E-string literature (Ohmori–Shimizu–Tachikawa) is the lead (CONDITIONAL).
- **A8 (REFUTED, proof; scope P-fix only).** "Even parity is possible under P-fix."
- **A9a (PROVED).** With no Z₂ at all, O1 is undefined.
- **A9b (REFUTED, fix 2).** "O1 is meaningless off a fixed plane."
- **A10 (PROVED given P-b and a τ with s_x s_Σ = −1).** G₄ is even and the net face charge is 0.
- **A10e (CONDITIONAL).** Such a τ exists only if the genus-2 Σ modulus admits an anticonformal involution, and τ must preserve the G₄ legs (α, β, γ) and A_i. A static even face is also obstructed by PD4 unless λ′(r_b) = 0.
- **A11 (PROVED given P-b and a τ with s_x s_Σ = +1).** G₄ is odd and the net face charge is 2N_flux.
- **A11e (CONDITIONAL).** For the antipodal τ, invariance of legs (β) and (γ) has not been checked.
- **O1 lock (OPEN).** **The remaining Owner choice is how σ acts on the face: τ on (x, Σ, S⁴).**
  - τ = id (fixed plane) forces odd.
  - A worldvolume-reversing τ gives even with zero net face charge, which conflicts with brane := wrapped M5 stack unless image anti-branes are admitted.
  - An orientation-preserving τ ≠ id gives odd.
  - "Fixed plane plus flip" is self-contradictory (PP OT3-fix).
  - Nothing is locked under OW 9a8ced02 until PP audits a derivation from an Owner-defined σ.

## 17 vs 18 tally header in 1736
PP 544fc7b0 does not address it, because it audits §A only and lists §B–§D as PENDING. It is left untouched here. NL's own count in 1736 (PROVED 18, with D2 for |z| ≤ 1 counted in §D) stands until PP's §B–§D audit lands.

## Tallies
| scope | PROVED | CONDITIONAL | OPEN | REFUTED | total |
|---|---|---|---|---|---|
| 1736 §A, revised | 9 (A1, A2, A3, A4a, A4c, A5, A9a, A10, A11) | 4 (A4b, A6, A10e, A11e) | 2 (A7, O1 lock) | 3 (A0r, A8, A9b) | 18 |
| 1736 overall (§A revised; §B–§D unchanged, pending PP) | 21 | 8 | 6 | 3 | 38 |

Count check:
- Old §A was 6/1/2/1 (10 items). Old 1736 overall was 18/5/6/1 (30 items).
- New overall = old overall − old §A + new §A:
  - PROVED 18 − 6 + 9 = 21.
  - CONDITIONAL 5 − 1 + 4 = 8.
  - OPEN 6 − 2 + 2 = 6.
  - REFUTED 1 − 1 + 3 = 3.
- Total 38.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
