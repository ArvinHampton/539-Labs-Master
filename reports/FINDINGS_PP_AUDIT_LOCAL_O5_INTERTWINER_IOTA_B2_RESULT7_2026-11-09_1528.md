# FINDINGS — PP audit of Local O5: explicit intertwiner ι: H₊ → H₊⊗ℂ² (B2 construction A, result 7) — 2026-11-09 15:28 CST (America/Chicago)
Agent: Professor Proof (Soft SF). Authority: GO (2) under OW 5a6e7177… (verified). Additive; the audited file is unchanged. Tip 7cddb188… untouched. No CERT. Nothing sent outside. No Gemini.
Context kept: **B2 = (B)-M (Majorana pure swap on H⊗ℂ²) is the Owner-adopted closure (OW 68a2b8e1).** Construction A is a non-adopted comparison only (prior PP audit FINDINGS_PP_SOFTSF_AUDIT_LOCAL_B2_CONSTRUCTION_A_ADDENDUM_NL_ERRATUM_2026-11-09_1316.md). Nothing here changes the adoption.
Scripts/logs: /workspace/audit-scratch/pp_local_o3o5o7_1521/o5_addendum_checks.py/.log.

## 0. Hash
FINDINGS_LOCAL_DERIVE_EXPLICIT_INTERTWINER_IOTA_B2_RESULT7_2026-11-09.md: ac1dd4e2d5850fa210d7c1f30ab42c7b3c481f4056d4c99c91dd716b3a98a415 — **MATCH** (sidecar OK).

## 1. Audit
1. **Multiplicity criterion — PROVED, CONFIRM, with a precision note.** Hahn–Hellinger: self-adjoint operators on separable spaces are unitarily equivalent iff they have the same maximal spectral type [μ] and the same multiplicity function n μ-a.e. H⊗1₂ = H⊕H has type [μ] and multiplicity 2n_H (with 2·∞ = ∞). So H ≅ H⊗1₂ ⇔ n_H = 2n_H μ-a.e.
   - **Precision:** n_H ≥ 1 μ-a.e. by definition of the maximal spectral type, so the "0" alternative is vacuous. The exact statement is: **H ≅ H⊗1₂ ⇔ n_H = ∞ μ-a.e. (uniform infinite multiplicity).** Local's "{0,∞}" is not wrong, only redundant. Separability is needed and holds.
2. **REFUTED (existence of ι when n_H < ∞ on a set of positive μ-measure) — CONFIRM** (refuted by proof). The eigenvalue argument (dim k vs 2k) is correct and self-contained. Examples are correct: 3D oscillator, and Dirac–Coulomb bound states, which have finite degeneracy.
3. **Free Dirac H has n_H ≡ ∞ — PROVED, CONFIRM.** H(p) has eigenvalues ±E(p), each of multiplicity 2. E depends only on r = |p|, and the L²(S²) factor gives infinite multiplicity; the spectrum is a.c. on (−∞,−m]∪[m,∞) (ℝ if m = 0). Local is correct that the source of the infinite multiplicity is the angular sphere, not the ± symmetry.
4. **ι unitary — PROVED, CONFIRM.**
   - FW: U* = (E+m − βα·p)/√(2E(E+m)), because (βα·p)* = −βα·p, and (βα·p)² = −p². Hence UU* = ((E+m)²+p²)/(2E(E+m)) = 1.
   - Numerics: U H U* = Eβ to ≤ 5.4×10⁻¹⁵ in both the Dirac and Majorana representations (m ∈ {0,1}, 200 random p each).
   - T₊ (Fourier ∘ U_FW ∘ spherical-harmonic/β-eigenbasis expansion) is unitary onto L²(ℝ₊,r²dr)⊗ℓ²(ℕ₀×{1..4}).
   - Bijections checked: b: ℕ₀×{0,1} → ℕ₀×{0,1}×{0,1}, via M = 2ν+ŝ ↦ (⌊M/4⌋, M mod 2, ⌊(M mod 4)/2⌋), is a bijection (proof: composite of two bijections; also checked to be injective and onto the initial segment for ν < 5×10⁴), and ν ↔ (l,m) is checked for ν < 10⁵. W is a relabelling of an orthonormal coordinate system, hence unitary.
5. **ι intertwines and preserves the energy sign — PROVED, CONFIRM.** W maps the β = +1 pair {1,2} to the β = +1 pair, and the β = −1 pair to the β = −1 pair. It acts trivially in r, so it commutes with σ_s E(r); hence ιHι* = H⊗1₂, with matching domains. The explicit formula for χ̂_t in §2 inverts T₋ correctly.
6. **Q_ι antiunitary, Q² = −1, QH_totQ⁻¹ = −H_tot — PROVED, CONFIRM (Majorana representation).**
   - Q² = diag(Aι*ιA, ιAAι*) = diag(A², ιA²ι*), with A² = γ⁰(γ⁰)*ΠK-commuting = γ⁰γ⁰* = −1 (Majorana; numerically γ⁰γ⁰* = −1 there and +1 in Dirac).
   - Conjugation blocks: (Aι*)(H⊗1₂)(ιA⁻¹) = AHA⁻¹ = −H, and (ιA)H(A⁻¹ι*) = −ιHι* = −H⊗1₂.
   - Checked in momentum space, where A acts as ψ̂(p) ↦ γ⁰·conj(ψ̂(p)): γ⁰ conj(H(p)) γ⁰⁻¹ = −H(p) holds **exactly (error 0) in the Majorana representation**. **It fails in the Dirac representation (error ~11)**, as Local's caveat says: there one must transport A by the Pauli unitary V.
   - Q² = −1 is representation-independent under that transport, since (VAV*)² = VA²V* and A² = ±1 is scalar.
   - This agrees with the earlier B2 fact Q_ι² = η·diag(1, ιι*) with ιι* = 1 for unitary ι.
7. **Non-local, non-canonical; unique up to the commutant — PROVED, CONFIRM.** No unitary L²⊗ℂ⁴ → L²⊗ℂ⁸ intertwines the multiplication algebra, because the fibre dimensions 4 ≠ 8 differ. ι′ι* lies in the commutant of H⊗1₂.
8. Numerical check: evidence only. PP's independent rerun agrees.

**Verdict line ("CONDITIONAL on H free Dirac / n_H = ∞"; "OPEN: Owner's exact H_{+U}") — CONFIRM.**

## 2. PP rollup
Local's rollup **PROVED 6 · CONDITIONAL 1 · OPEN 1 · REFUTED 1 — CONFIRMED.**
- Errors: none.
- Precision notes: criterion is "n_H = ∞ μ-a.e." (the 0 is vacuous); A = γ⁰KΠ anti-commutes with H only in a Majorana representation, as Local states.
- (B)-M remains the adopted B2 closure; this file does not affect it.
Citation tags (CONDITIONAL until pinned): Hahn–Hellinger multiplicity theorem; Pauli's fundamental theorem. FW is verified directly above (no citation needed).
No CERT. Tip untouched.
