# FINDINGS — Local Path O5 DERIVE: explicit intertwiner ι: H₊ → H₊⊗ℂ² with ι H = (H⊗1₂) ι (B2 construction A, result 7) — 2026-11-09

- Lane: Local Path. Written Nov 9, 2026 (~3:25 PM CST, America/Chicago) under the Owner decision of 3:11 PM CST, reports/OWNER_WRITE_MAINCHAT_BLUEPRINT_1509_CORRECTED_ADOPTED_2026-11-09_1511.md (sha 5a6e7177…), item O5. Additive new file. No CERT. Tip 7cddb188… untouched. Nothing sent outside. Pure math; small numpy checks only (scratch, not kept).
- **Status note:** the Owner adopted B2 = (B)-M (NL Option M). This file concerns the **not-adopted alternative** (construction A, LD-A4 with a unitary ι). Nothing here changes the adoption.
- Sources: reports/FINDINGS_LOCAL_DERIVE_PREV_CONSTRUCTION_A_DIRECT_SUM_ISOMETRY_2026-11-09.md (sha 4b25d2edf14b887038186ac2d4b580bacb106b3811456fceeea702f08c8a783f; "A-file"), result 7 and LD-A4; NL reports/NL_DERIVED_B2_CLOSURE_A_DIRECT_SUM_NONLOCAL_IOTA_2026-11-09_1315.md (988f1436…) A-3, and …_B_TWO_SECTOR_HxC2_OPTIONS_M_D_2026-11-09_1315.md (5907eaf3…).

## 0. Setting (as in A-file LR-0 and NL)
H₊ = L²(ℝ³)⊗ℂ⁴, H₋ = H₊⊗ℂ² = L²(ℝ³)⊗ℂ⁴⊗ℂ². H = α·p + βm (free Dirac, m ≥ 0), any γ-representation; on H₋ the Hamiltonian is H⊗1₂. A = γ⁰KΠ. A-file result 7: with AHA⁻¹ = −H (Majorana rep), Q_U = [[0, AU*],[UA, 0]] satisfies Q_U H_tot Q_U⁻¹ = −H_tot iff U H U* = H⊗1₂. We need an explicit unitary U =: ι with that property.

## 1. When can such ι exist? (the multiplicity criterion)
1. **PROVED — criterion.** Let H be self-adjoint on a separable space with Hahn–Hellinger data (spectral measure class [μ], multiplicity function n_H: ℝ → {0,1,2,…,∞}). Then H⊗1₂ has the same class [μ] and n_{H⊗1₂} = 2n_H. By Hahn–Hellinger, H ≅ H⊗1₂ (unitarily) **iff n_H(E) = 2n_H(E) μ-a.e., i.e. iff n_H ∈ {0, ∞} μ-a.e.**
2. **REFUTED (by item 1) for any H with a finite-multiplicity spectral part.** In particular: simple spectrum; any H with an isolated eigenvalue of finite multiplicity (e.g. a harmonic-oscillator H diagonal in the Hermite basis — finite-multiplicity eigenvalues — or a Dirac operator with a binding potential such as Coulomb, whose bound states have finite multiplicity). For such H no unitary ι with ιH = (H⊗1₂)ι exists. Proof for an eigenvalue E of multiplicity k < ∞: ι would map ker(H−E) (dim k) unitarily onto ker(H⊗1₂ − E) = ker(H−E)⊗ℂ² (dim 2k), impossible.
3. **PROVED — the free Dirac H satisfies the criterion, so A-file result 7 (existence) is correct, not flawed.** In momentum space H(p) has eigenvalues ±E(p), E = √(p²+m²), each of multiplicity 2 on ℂ⁴. Passing to p = rω (r > 0, ω ∈ S²), E depends on r only, so the angular factor L²(S²) (infinite-dimensional) contributes infinite multiplicity: H is a.c. on (−∞,−m] ∪ [m,∞) with uniform multiplicity ∞ (m = 0: on ℝ). Hence n_H ≡ ∞ on the spectrum. The relevant feature is the **infinite multiplicity from the angular sphere**, not the ± symmetry of the spectrum and not continuity per se (a continuous simple spectrum would still fail by item 1). The Hermite basis is irrelevant for intertwining: A-file LD-A4 and NL A-3 interleavings do not intertwine H (no claim was made that they do).

## 2. Explicit formula (Local-derived LD-O5)
Fix any γ-representation; β = γ⁰, α_k = γ⁰γ^k. Fix an orthonormal eigenbasis b₁,b₂ (β = +1), b₃,b₄ (β = −1) of β on ℂ⁴; σ₁ = σ₂ = +1, σ₃ = σ₄ = −1. Let 𝓕 be the Fourier transform, Y_{lm} the orthonormal spherical harmonics, and index them by **ν = l² + l + m ∈ ℕ₀** (inverse: l = ⌊√ν⌋, m = ν − l² − l; a bijection ℕ₀ ↔ {(l,m): |m| ≤ l}).

**Step 1 (Foldy–Wouthuysen, unitary, fibrewise in p).** U_FW(p) := (E + m + β α·p)/√(2E(E+m)). Then U_FW(p) H(p) U_FW(p)* = E(p) β (uses only the Clifford relations, so valid in every representation; p ≠ 0 when m = 0).

**Step 2 (coordinates).** For ψ ∈ H₊ put φ(p) := U_FW(p) ψ̂(p) and
  c_{ν,s}(r) := ∫_{S²} conj(Y_ν(ω)) ⟨b_s, φ(rω)⟩ dω,  s = 1..4.
The map T₊: ψ ↦ (c_{ν,s})_{ν,s} is unitary H₊ → L²(ℝ₊, r²dr) ⊗ ℓ²(ℕ₀ × {1,2,3,4}), and T₊ H T₊⁻¹ = multiplication by σ_s E(r). Likewise T₋ := T₊ ⊗ 1₂ is unitary H₋ → L²(ℝ₊, r²dr) ⊗ ℓ²(ℕ₀ × {1..4} × {1,2}) with T₋ (H⊗1₂) T₋⁻¹ = σ_s E(r).

**Step 3 (index bijection preserving the energy sign).** For the positive pair s ∈ {1,2} write s = 1+ŝ (ŝ ∈ {0,1}); for the negative pair s ∈ {3,4}, s = 3+ŝ. Define b: ℕ₀ × {0,1} → ℕ₀ × {0,1} × {0,1},
  M := 2ν + ŝ;  b(ν, ŝ) := (ν′, ŝ′, t′) with ν′ = ⌊M/4⌋, ŝ′ = (M mod 4) mod 2, t′ = ⌊(M mod 4)/2⌋.
b is a bijection (composite of ℕ₀×{0,1} → ℕ₀, (ν,ŝ) ↦ 2ν+ŝ, and ℕ₀ → ℕ₀×{0,1}×{0,1}, M ↦ (⌊M/4⌋, M mod 4 split in binary)). Let W be the unitary permutation of coordinates: (W c)_{ν′, s′, t′}(r) := c_{ν, s}(r) where (ν′,ŝ′,t′) = b(ν,ŝ) and s′ lies in the **same** sign pair as s (s′ = 1+ŝ′ if s ∈ {1,2}; s′ = 3+ŝ′ if s ∈ {3,4}); t′+1 labels the ℂ² factor.

**Definition LD-O5 (Local-derived).** **ι := T₋⁻¹ ∘ W ∘ T₊ : H₊ → H₋.** Explicitly, (ιψ) = Σ_{t=1,2} χ_t ⊗ f_t with
  χ̂_t(rω) = U_FW(rω)* Σ_{s′=1}^{4} Σ_{ν′} c_{b⁻¹(ν′, s′, t)}(r) Y_{ν′}(ω) b_{s′},
where c_{b⁻¹(ν′,s′,t)} denotes c_{ν,s} with (ν,ŝ) = b⁻¹(ν′, ŝ′, t−1) and s in the sign pair of s′.

## 3. Results on LD-O5
4. **PROVED — ι is unitary.** T₊, T₋ are unitary (Fourier, the unitary matrix field U_FW(p), the ONB {Y_ν ⊗ b_s} of L²(S²)⊗ℂ⁴ fibred over r); W is a bijective relabelling of an orthonormal coordinate system at each r, hence unitary.
5. **PROVED — ι intertwines.** W acts trivially in r and maps sign pair to sign pair, so it commutes with multiplication by σ_s E(r); hence ι H ι⁻¹ = T₋⁻¹ (σE(r)) T₋ = H⊗1₂, with ι D(H) = D(H⊗1₂) (ι commutes with all bounded Borel functions of the multiplication operator, so domains match).
6. **PROVED — consequence for construction A.** With ι = LD-O5 in the Majorana representation (where AHA⁻¹ = −H, A-file result 3 / NL Option M), Q_ι := [[0, Aι*],[ιA, 0]] is antiunitary on H₊⊕H₋, swaps the sectors, Q_ι² = γ⁰γ⁰* = −1, and Q_ι H_tot Q_ι⁻¹ = −H_tot. (Check: H₊-block (Aι*)(H⊗1₂)(ιA⁻¹) = AHA⁻¹ = −H; H₋-block ιA H A⁻¹ ι* = −ιHι* = −H⊗1₂.) In another representation use ι_rep = LD-O5 built with that rep's β (Step 1 is representation-independent), or conjugate by the Pauli-theorem unitary V between reps.
7. **PROVED — ι is non-local and non-canonical** (consistent with A-file result 6 and NL A-2/A-5): U_FW and the angular relabelling mix positions (no unitary H₊ → H₋ commutes with all M_f). Choices: the frame b_s, the ordering ν, the bijection b. Any two intertwiners differ by a unitary in the commutant of H⊗1₂ (decomposable over E with fibres of dimension ∞), so ι is unique only up to that commutant.
8. **Numerical check (numpy, scratch):** Dirac and a Majorana representation (found by search over Pauli products, all γ^μ imaginary), m ∈ {0, 1}, 200 random p each: ‖U_FW U_FW* − 1‖, ‖U_FW H U_FW* − Eβ‖ ≤ 9×10⁻¹⁵; in the b-basis U_FW H U_FW* = diag(E,E,−E,−E); γ⁰γ⁰* = +1 (Dirac), −1 (Majorana). Bijection b checked on ν < 2×10⁵ (injective, onto the initial segment); ν ↔ (l,m) checked for ν < 10⁵.

## 4. Verdict
- The brief's worry is resolved: "simple spectrum ⇒ no intertwiner" is correct (item 2), but the free Dirac H does **not** have simple spectrum; it has uniform infinite multiplicity (item 3). A-file result 7 (existence) stands; this file supplies the explicit ι (LD-O5).
- **CONDITIONAL:** the construction (and existence at all) is conditional on H being the free Dirac operator, or more generally on n_H ∈ {0,∞} a.e. If the Owner's H_{+U} has any finite-multiplicity spectrum (bound states, 35-component structure with simple pieces), the unitary-ι route is REFUTED by item 2. The Owner's exact H_{+U} remains OPEN (A-file).
- B2 itself is the Owner's: adopted (B)-M. This (A) alternative is recorded only for comparison.

## 5. Rollup
PROVED 6 (items 1, 3, 4, 5, 6, 7) · CONDITIONAL 1 (applicability: H free Dirac / n_H ∈ {0,∞}) · OPEN 1 (Owner's exact H_{+U}) · REFUTED 1 (item 2: intertwiner for any H with finite-multiplicity spectrum, incl. simple spectrum). Numerical check (item 8) is evidence only. No CERT. Tip untouched.
