# ERRATUM — Non Local Path — erratum to two-track catalog, entry B1 (units) — 2026-11-05

Lane: Non Local Path (NONLOCAL_QM_EH11D). Internal protocol artifact. Reports only.
Date: 2026-11-05 14:05 CST (America/Chicago).
Category B. **No CERT.** invent HOLD stands. Tip sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 unchanged before and after.

## Scope
This is an additive erratum to entry B1 only. It is a normalization-precision fix: no new model is adopted and no target is invented. The original files are preserved unchanged in reports/ and bridges/NONLOCAL_QM_EH11D/:
- FINDINGS_NL_TWO_TRACK_EXACT_CONSEQUENCES_2026-11-05.md — 5b40ee12c9731d68e06a6b590229de49660c57813a901dcaed26d7ab2f4d2468
- SOFTSF_PRESS_FINDINGS_NL_TWO_TRACK_EXACT_CONSEQUENCES_2026-11-05.md — f3a640ccdac4cbf41356197fb39657f68cc4d3d4f5c8c4db6ece39aa2c42a932

Trigger: PP audit FINDINGS_PP_SOFTSF_AUDIT_NL_TWO_TRACK_5b40ee12_2026-11-05.md (computed sha abea4b1149025f4b8b6f0b4b6bc7482cbf5c7ac0a44725369a69c956d932beea), note N1: "'GM commensurable with 3⁻⁵³⁹' is not a precise hypothesis. State it as 'fix units in which GM ∈ ℝ_{>0} is a dimensionless number'."

## Old wording (FINDINGS line 40, quoted exactly)
> Hypotheses (explicit, not a model choice): G and M are real and finite with G > 0, M ≥ 0, in units where GM is commensurable with the dimensionless 3⁻⁵³⁹. The sources do not fix these units, so the statement is conditional on such a normalization.

(PRESS line 7 says: "B1 (G > 0, M ≥ 0 real; units normalized as stated).")

## Corrected B1 (supersedes the hypotheses and statement of B1 only)
Hypotheses (explicit, not a model choice): Fix units in which GM is a positive dimensionless real number (G > 0, M > 0). This is a conditional reading for evaluating the formula, not a normalization derived from or adopted for the model; the sources do not fix units. Taking M > 0 narrows the original M ≥ 0 to the black-hole case; it is not equivalent to M ≥ 0. The M = 0 case is kept separately below. Read |r|₃ as the real number 3^{−v₃(r)} (with |0|₃ = 0) for r ∈ ℚ₃, and set D(r) := |r|₃ + 3⁻⁵³⁹.
Statement: D(r) ≥ 3⁻⁵³⁹ > 0, hence 0 < 2GM/D ≤ 2GM·3⁵³⁹ < ∞. The formula g_rr = (1 − 2GM/D)⁻¹ is undefined exactly when D(r) = 2GM. This happens for some r iff 2GM ∈ V := {3^{−v} + 3⁻⁵³⁹ : v ∈ ℤ} ∪ {3⁻⁵³⁹}.
Not implied: no physical curvature singularity is inferred from the undefined formula, no real limit or blow-up is inferred from the discrete values, and no curvature bound follows.
Separate trivial case (from the original M ≥ 0): if M = 0, then 2GM/D = 0 and g_rr = 1 everywhere. The undefined set is empty.

## Clean diff (B1 hypothesis sentence)
```
- G and M are real and finite with G > 0, M ≥ 0, in units where GM is commensurable with the dimensionless 3⁻⁵³⁹. The sources do not fix these units, so the statement is conditional on such a normalization.
+ Fix units in which GM is a positive dimensionless real number (G > 0, M > 0). The sources do not fix such units, so B1 is conditional on this normalization. [M = 0: separate trivial case, g_rr = 1.]
- Statement: … hence 0 ≤ 2GM/D ≤ 2GM·3⁵³⁹ < ∞.
+ Statement: … hence 0 < 2GM/D ≤ 2GM·3⁵³⁹ < ∞.
```
All other entries (A1–A4, B2) are unchanged. The curvature conclusions of B1 (no physical singularity inferred, no blow-up from discrete values, no curvature bound) are unchanged.

## Compliance
The original catalog and PRESS are not edited, and their mirrors are unchanged. No CERT, publishing, spending, or messages. Next: PP / Keeper as usual (parent handles the handoff).
