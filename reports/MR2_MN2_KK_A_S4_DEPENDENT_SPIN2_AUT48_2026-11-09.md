# MR2 · MN2 · KK Group A — S⁴-dependent spin-2 modes (stage 1 of OW d5eaeef3)
Date: 2026-11-09, ~20:25 CST. Authority: OW d5eaeef3 ("Pursue all open") under OW 8b26c786 (Group A = Aut⁺(Bolza), order 48, × wall ℤ₂, a scope choice, not a result). B not adopted. Full spectrum OPEN; junction UNSOLVED; count gap unchanged. Usage at start: 72.8%.

| file | sha256 |
|---|---|
| MR2_MN2_KK_A_S4_DEPENDENT_SPIN2_AUT48_2026-11-09.py (chmod a-w, sidecar before run) | 17f821d25491ea072cd574238f052b30d8c7dcc8e5681ae2b44e5e642d5c977a |
| ….log (exit 0, 14 s) | c4fc9660c92edc2c8824e21b2758087c5ff750848aedb4c708fdd771708bccef |

Inputs: the KK .py (sha 88949658… MATCH) supplies the verbatim V2 `cand_metric` block (the source of V2 sha ad134752) and the [T] FEM helpers. MN2 point: X₁ = 2^(−3/5), X₂ = X₀ = 2^(2/5), F₀ = 2^(−4/5), G₀ = 2^(1/5)/4, F₀/G₀ = 2 (all exact).

## Resonant algebra naming
- RA-1: reduction of the Bachas–Estes operator.
- RA-1x: exact shift identity.
- RA-2: S⁴ radial spectrum.
- RA-3: Group A selection.

## RA-1. Reduction
- Write S⁴ ⊂ ℝ³ ⊕ ℝ², with μ⃗ = (m₀, m₂e^{iφ₂}) carrying X₀ = X₂ = s and ν = m₁e^{iφ₁} carrying X₁ = t. Set |μ⃗| = cos θ and |ν| = sin θ.
- The S⁴ block of the V2 metric is c[H dθ² + (cos²θ/s) dΩ₂² + (sin²θ/t) dφ₁²], where c = D^(−2/3)/4, D = s cos²θ + t sin²θ and H = sin²θ/s + cos²θ/t.
- The (u, φ₁) twist cross term only minimally couples ∂_{φ₁}. Block inversion gives g^{uu} = 1/g_uu(bare) and g^{φ₁φ₁} = 1/g_{φ₁φ₁}(bare) + a²/g_uu.
- So for q = 0, the operator on ψ = f(Σ) Θ(θ) Y_j(μ̂) is
  −e^{2A}(1/√g)∂(√g g ∂ψ) = [2(−Δ_Σ) f]·ΘY + f·(L_θ Θ)Y,
  where L_θ is the self-adjoint radial operator in log [RA-1].
- The derivation is exact and written out above. The machine check compares the full 11D operator (all V2 cross terms, a₁ = 7/10) with the reduced one on 5 test functions (j = 0, 1, 2) at 15 random points. Maximum relative difference 1.4e-15. **COND** under the float convention (the check is numerical; the derivation is by hand).

## RA-1x. Exact shift. PROVED (exact sympy, log [RA-1x])
- H·s·t − D ≡ 0, so D^(1/2)H^(−1/2) = √(st) is constant. Also 4F₀st = 2, 4F₀s² = 4 and 4F₀t² = 1, all exact.
- With symbolic j, q and Θ, sympy gives: L_θ(MN2) − [2·L_θ(round unit S⁴) + 2j(j+1) − q²] = 0.
- Hence **μ_{ℓ,j,q} = 2ℓ(ℓ+3) + 2j(j+1) − q², with ℓ = j + |q| + 2n.** The round-S⁴ radial problem is the Jacobi equation, with eigenvalues ℓ(ℓ+3).

## RA-2. Spectrum. PROVED (RA-1x plus the classical round-S⁴ spectrum; reproduced numerically)
- Control: on the round S⁴ (s = t = F₀ = 1), the Galerkin solver reproduces 4ℓ(ℓ+3) exactly (j = 0, 1, 2; values 0, 16, 40, 72, 112, 160, 216).
- At MN2, the q = 0 values for j = 0…5 and n = 0…3 match the closed form to ≤ 2.5e-11, with N = 24 vs 34 agreement ≤ 2.2e-12.
- First values: j = 0: 0, 20, 56, 108. j = 1: 12, 40, 84, 144. j = 2: 32, 68, 120, 188.

## RA-3. Group A selection. COND
- **q = 0 modes are functions on Σ ⊗ S⁴ harmonics.** Aut⁺ acts on Σ only. Its canonical lift (KK file ecee2668 §A, CONDITIONAL) is trivial on the q = 0 S⁴ factor. So such a mode is invariant ⇔ f lies in the Aut⁺-trivial part of L²(Σ), i.e. I1 ⊕ I2: λ ∈ {0, 23.07856, 74.927, 116.603, …, 222.371 (I2), …}.
- **SU(2)_R.** SO(3)_R commutes with Aut⁺ and with the wall, so it is not projected. Each spin-j multiplet is kept whole. The modes are integer j only (functions on S⁴); j = 0 are the SU(2)_R singlets.
- **Wall ℤ₂.** It acts on 5D fields only; the spin-2 graviton modes are wall-even (Neumann-type; HW premise). No further removal.

## Result: lowest Group-A-invariant S⁴-dependent spin-2 modes (q = 0)
Formula: m²L₅² = 2λ_Σ + 2ℓ(ℓ+3) + 2j(j+1) and Δ = 2 + √(4 + m²L₅²).

| m²L₅² | Δ | λ_Σ | SU(2)_R j (dim) | ℓ | vs Σ-only 46.157 |
|---|---|---|---|---|---|
| **12** | **6** | 0 | 1 (3) | 1 | below |
| **20** | 2+2√6 = 6.89898 | 0 | **0 (singlet)** | 2 | below |
| 32 | 8 | 0 | 2 (5) | 2 | below |
| 40 | 8.63325 | 0 | 1 (3) | 3 | below |
| 56 | 9.74597 | 0 | 0 (1) | 4 | above |
| 58.157119 | 9.88398 | 23.07856 | 1 (3) | 1 | above |
| 60 | 10 | 0 | 3 (7) | 3 | above |
| 66.157119 | 10.37598 | 23.07856 | 0 (1) | 2 | above |

Disclosure: the log's [RA-3] list also prints the S⁴-*constant* row 46.157119 (λ_Σ = 23.07856, μ = 0) with the tag "above". That row is the Σ-only reference itself, not an S⁴-dependent mode, and the tag is cosmetic (equal, not above). The frozen log is not edited.

- **Headline.** The lowest Group-A-invariant S⁴-dependent spin-2 mode is the SU(2)_R triplet at **m²L₅² = 12 (Δ = 6)**. The lowest SU(2)_R singlet is at **m²L₅² = 20 (Δ = 2+2√6)**. Four S⁴-dependent levels (12, 20, 32, 40) lie **below** the Σ-only invariant level 46.157 (λ = 23.0786). All are exact closed-form values given the operator. **COND**: Bachas–Estes reduction (citation, arXiv:1103.2800, form generalised to AdS₅), MN2 vacuum premise (OW 19a88b19) and RA-1.
- **Controls.**
  - Σ-only invariant levels reproduced with the KK FEM helpers (n = 60/120 Richardson): 23.078559 (KK log 23.078559), 74.926718, 116.602585 → m²L₅² = 46.1571, 149.8534, 233.2052.
  - Uniform-point identity m²L₅² = 2λ (KK [S], exact).
  - These are COND (float FEM).

## Tally (PP convention: float numerics or a citation count as COND; a stated premise is graded as an implication)
| # | claim | label |
|---|---|---|
| 1 | RA-1 reduction to 2(−Δ_Σ) + L_θ | COND (machine check float; hand derivation) |
| 2 | RA-1x exact shift identity, μ = 2ℓ(ℓ+3) + 2j(j+1) − q² | PROVED |
| 3 | RA-2 q = 0 spectrum (closed form; controls) | PROVED |
| 4 | RA-3 selection (q = 0 invariant ⇔ f ∈ I1⊕I2; SU(2)_R unprojected; wall-even) | COND (canonical lift; HW) |
| 5 | headline masses 12 (Δ 6, triplet), 20 (Δ 6.899, singlet), 32, 40 below 46.157 | COND (Bachas–Estes; vacuum; RA-1) |
| 6 | controls: Σ-only levels and m²L₅² = 2λ | COND (float FEM) |
| 7 | q ≠ 0 (U(1)-charged) towers; rigorous Σ bounds | OPEN (q ≠ 0 is stage 2) |

**PROVED 2 · COND 4 · OPEN 1 · REF 0 = 7.**

Rules: new dated files only; .py frozen before its log; no existing file edited; tip 7cddb188 untouched; no CERT, no Gemini, nothing external; no messages sent.
