# MR2 · MN2 · KK Group A — charged S⁴ towers, spin-2 (stage 2 of OW d5eaeef3)
Date: 2026-11-09, ~20:45 CST. Authority: OW d5eaeef3 under OW 8b26c786 (Group A = Aut⁺(48) × wall ℤ₂, a scope choice, not a result). B not adopted. Full spectrum OPEN; junction UNSOLVED; count gap unchanged. Usage before this stage: 74.4% (< 82%, so the stage was started).

| file | sha256 |
|---|---|
| MR2_MN2_KK_A_CHARGED_S4_TOWERS_AUT48_2026-11-09.py (chmod a-w, sidecar before run) | 92fe47d02c3c2295ea81780fc49c0726670116a855350b22244b063afee256fb |
| ….log (exit 0, 13 s) | 5d0d3b76e4ffc171d6f05ecbff28e6eba547cf04f154dbe221991265b6340362 |

Inputs, all sha-checked in log [0]:
- KK .py 88949658… (MATCH), supplying [G], the verbatim V2 `cand_metric` and the [T] FEM;
- stage-1 .py 17f821d2… (MATCH);
- the V2 twist line a1 = (1+z)/2, giving a1 = 1 and a2 = 0 at MN2.

Scope: spin-2 only. Scalars and vectors are **OPEN**, because their mixing with the fluxes is not cheap.

## Resonant algebra naming
- RA-4: charged reduction.
- RA-5: Landau/Maass ladder.
- RA-6: Aut⁺ invariants in H⁰(K^m).
- RA-7: assembled masses.

## RA-4. Charged reduction. COND (float machine check; hand derivation)
- For ψ = F(u,v)·Θ(θ)Y_j(μ̂)e^{iqφ₁}, block inversion of the (u, φ₁) twist block gives (1/g_uu)(∂_u − (a₁/v)∂_{φ₁})² + (1/g_{φ₁φ₁})∂_{φ₁}².
- So the operator is 2·H_q F + μ_{ℓ,j,q}F, with H_q = −v²[(∂_u − iq/v)² + ∂_v²] (magnetic field b = q·a₁ = q) and μ from stage 1, RA-1x (exact, symbolic q).
- Machine check of the full 11D operator vs this form, on 4 charged test modes (q = 1, 2, 1, −3; j = 0, 0, 1, 0) at 3 random points each: maximum relative difference 3.0e-15.
- Disclosure: the log also prints 4 "sign s = −1 does not match" lines. These are the rejected opposite-sign alternative, printed as a control; s = +1 is the matching convention.

## RA-5. Ladder. Identities PROVED (exact sympy); completeness COND
- Exact identities, with Δ_k = −v²(∂_u² + ∂_v²) + ikv∂_u, R_k = iv∂_u + v∂_v + k/2 and L_k = iv∂_u − v∂_v + k/2:
  - H_b = Δ_{2b} + b²;
  - Δ_{k+2}R_k = R_kΔ_k;
  - L_{k+2}R_k = Δ_k + (k/2)(1 + k/2);
  - Δ_k v^{k/2} = (k/2)(1 − k/2)v^{k/2}.
- So raising is injective and eigenvalue-preserving on all eigenvalues that occur, and is Aut⁺-equivariant under the canonical lift.
- Spectrum on K^n (b = n): {n² + m(1−m) : m = 1…n, multiplicity h⁰(K^m)} ∪ {n² + λ : λ > 0 a scalar Laplace eigenvalue}. These are the hyperbolic Landau levels n(2k+1) − k(k+1) with k = n − m, plus the raised scalar levels.
- Completeness of this list is standard Maass raising/lowering theory: a citation, so **COND**.

## RA-6. Aut⁺ invariants in H⁰(K^m). PROVED (computer-assisted, exact group; independent control)
- On y² = x⁵ − x, a basis of H⁰(K^m) is x^a ω^m (a ≤ m) together with y x^b ω^m (b ≤ m − 3), where ω = dx/y. Hence H⁰(K^m) ≅ Sym^m ρ ⊕ det ρ ⊗ Sym^{m−3} ρ, with ρ = H⁰(K).
- The factor det ρ arises because η = dx³/y² transforms by det³/κ = det ρ; this was checked on both generators.
- The dimensions 2m − 1 (and 2 for m = 1) match Riemann–Roch.

| m | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| dim H⁰(K^m)^{Aut⁺} | 0 | 0 | 0 | 0 | 0 | **1** | 0 | **1** |

- Independent control: the (2,3,8) orbifold formula dim S_{2m} = −(2m−1) + ⌊m/2⌋ + ⌊2m/3⌋ + ⌊7m/8⌋ (m ≥ 2) gives the same row. Its math was checked against these values; the citation does not upgrade the grade.
- m = 1, 2 reproduce KK ecee2668 (no LLL invariants for q = ±1, ±2).

## RA-7. Group-A-invariant charged spin-2 masses (each ±q; SU(2)_R multiplet 2j+1; wall-even)
Formula: m²L₅² = 2H_Σ + 2ℓ(ℓ+3) + 2j(j+1) − q², with ℓ = j + |q| + 2n.

| m²L₅² | Δ | \|q\| | j | ℓ | H_Σ (origin) |
|---|---|---|---|---|---|
| **55.15712** | **9.69137** | 1 | 0 | 1 | 24.07856 (raised λ = 23.07856) |
| 70.15712 | 10.61145 | 2 | 0 | 2 | 27.07856 (raised λ) |
| 71.15712 | 10.66932 | 1 | 1 | 2 | 24.07856 |
| 83.15712 | 11.33580 | 1 | 0 | 3 | 24.07856 |
| **84 (exact)** | 11.38083 | **6** | 0 | 6 | 6 (LLL; the invariant 6-differential) |
| 90.15712 | 11.70346 | 2 | 1 | 3 | 27.07856 |
| 91.15712 | 11.75485 | 3 | 0 | 3 | 32.07856 |
| 95.15712 | 11.95777 | 1 | 2 | 3 | 24.07856 |
| 106.15712 | 12.49558 | 2 | 0 | 4 | 27.07856 |
| 107.15712 | 12.54311 | 1 | 1 | 4 | 24.07856 |
| 115.15712 | 12.91591 | 3 | 1 | 4 | 32.07856 |
| 118.15712 (×2) | 13.05247 | 2 / 4 | 2 / 0 | 4 / 4 | 27.07856 / 39.07856 |
| 120 (exact) | 13.13553 | 6 | 1 | 7 | 6 (LLL) |

- **Survival.**
  - All charged modes whose Σ factor is a holomorphic-type (Landau) section are removed for |q| = 1…5 and 7, because there are no invariants.
  - q = ±6 keeps one LLL mode per (ℓ, j), coming from the invariant 6-differential; q = ±8 likewise (first at m²L₅² = 128).
  - Raised-scalar modes survive exactly when λ is Aut⁺-invariant (23.07856, 74.9267, …), for every q.
  - SU(2)_R is not projected. The wall ℤ₂ keeps the spin-2 modes (wall-even, HW premise).
- **Lowest charged invariant: q = ±1, j = 0, at m²L₅² = 55.157 (Δ = 9.691).**
  - This is above the Σ-only level 46.157 and well above the neutral S⁴-dependent modes of stage 1 (12, 20, 32, 40).
  - The lowest Landau-type charged invariant is q = ±6 at exactly 84.
- **Completeness below 120.**
  - |q| ≥ 9 gives m²L₅² ≥ 2|q| + q² + 6|q| ≥ 153.
  - q = 7 gives ≥ 129 (Landau m = 6; raised levels ≥ 235).
  - q = 8 gives ≥ 128 (Landau m = 8).
  - Raised levels for |q| ≥ 5 give ≥ 151.
  - So the table is complete below 120, given RA-5 completeness. The log's completeness line states the q = 7 case; the q = 8 case (128) is added here.
- **Grade: COND** (Bachas–Estes citation; MN2 vacuum OW 19a88b19; RA-4 float; RA-5 completeness; λ from float FEM).
- **Controls:** Σ-only invariant levels 23.078559 and 74.926718 reproduced (KK log 23.078559); uniform-point identity m²L₅² = 2λ gives 46.1571 and 149.8534. COND (float).

## Tally (PP convention)
| # | claim | label |
|---|---|---|
| 1 | RA-4 charged reduction 2H_q + μ | COND |
| 2 | μ_{ℓ,j,q} = 2ℓ(ℓ+3) + 2j(j+1) − q² for q ≠ 0 (stage-1 RA-1x, symbolic q) | PROVED |
| 3 | RA-5 ladder identities (exact) | PROVED |
| 4 | RA-5 completeness of the K^n spectrum (Maass theory) | COND (citation) |
| 5 | RA-6 invariant dims of H⁰(K^m), m ≤ 8 (0,0,0,0,0,1,0,1) | PROVED (computer-assisted; orbifold control) |
| 6 | RA-7 lowest invariant charged spin-2 masses (55.157 for q = ±1; 84 for q = ±6; table complete below 120) | COND |
| 7 | controls (Σ-only levels; m²L₅² = 2λ) | COND (float) |
| 8 | charged scalars and vectors; rigorous FEM bounds; masses above 120 | OPEN |

**PROVED 3 · COND 4 · OPEN 1 · REF 0 = 8.**

Rules: new dated files only; .py frozen before its log; no existing file edited; tip 7cddb188 untouched; no CERT, no Gemini, nothing external; no messages sent.
