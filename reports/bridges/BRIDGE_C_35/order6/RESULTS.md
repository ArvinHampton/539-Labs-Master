# order6 results: completing the orthant pieces
PREREG sha256 c19500e3…dfea (unchanged). Script hashes: scripts/SHA256SUMS. Deviations are listed in NOTES.md, and the recorded verdicts stand.

## Category A (derived; proof sketches flagged)
- **Orthant split.** For generic α, the ν-sign orthant weight decomposes as orth_ν = ¼(1+s1)(1+s2) = ½·ODD + ½·EVEN, with ODD = ½(s1+s2) and EVEN = ½(1+s1s2). The difference between the v-sign and ν-sign weights is a finite set of half-lines and points (L_O), plus the full lines U_H.
  - 15 of the 105 companions have α on an axis, where some ν-signs are 0. They are listed in data/slaw.json; see NOTES.
- **Odd pair (c1 = (−1,1), c′ = (−7,2)).**
  - Completion: ½(E(√10·ν1·√y) + E(√35·ν2·√y)).
  - Shadow: weight-3/2 unary thetas. One is Σ n e(5n²τ/2) (n ∈ α1+Z) paired with θ_{7/2}. The other is Σ m e(35m²τ/4) (m ∈ α2+Z) paired with θ_1(ν1+7ν2/2), glued over 2 classes.
- **Axis half-lines (Q = 1, 7/2).** These are positive-definite 1-D pieces. Vignéras' equation has no bounded weight-½ solution other than constants, so they have no completion on H; they are quantum modular (false/partial thetas). Their quantum shadows are Σ n e(n²τ) (n ∈ α1+7α2/2+Z) and Σ n e(7n²τ/2) (n ∈ α1+α2+Z). *Argument sketch.*
- **Even double orthant.** This piece is not of Zwegers form, for two reasons (*argument sketch*):
  - EVEN is even under ν → −ν, while Zwegers' ρ is odd.
  - The natural product candidate ½(1+E1E2) violates Vignéras' equation: its cross term is ∝ B(c1,c′) = −35 ≠ 0.

  The orthant is also not a union of unit-group fundamental cones, because Q(e1) = 1 ≠ Q(e2) = 7/2 (automorph [[−1,−7],[2,13]]). So EVEN is a partial Hecke-type sum.

## Category B (numerical)
Interior S-law tests (120 τ, fixed 35-component law vector S-matrix, Ĥ(−1/τ) = (τ/√35)·M·Ĥ(τ)):

| object | r | verdict |
|---|---|---|
| gating: Ĥ (cone part, completed) | 6.0e−16 | pass (required) |
| gating: holomorphic H_ν | 0.300 | fail (required) |
| **O1: odd orthant pair Ĝ_O** | 6.1e−16 | **pass** |
| **E1: even product candidate Ê = ½(1+E1E2)** | 0.903 | **FAIL** (as predicted) |
| **O3: completed orthant ¼(1+E1)(1+E2)** | 0.451 | **FAIL** (as predicted) |
| **F1: completed full series Ŝ_ν = ½Ê + ½Ĝ_O − Ĥ** | 0.451 | **FAIL** (as predicted) |
| F2: residual(Ŝ) = ½·residual(Ê) | max diff 4.7e−16 | **pass** |

Truncation error (box 40 vs 50) is ≤ 6e−17.

Finite-difference shadow tests (4 τ × 6 companions):
- **O2:** the odd-pair shadow formula matches to 3.4e−9 (**pass**).
- **E2:** the product-rule ∂_τ̄ of Ê matches to 3.3e−9 (**pass**; this is a calculus check). Its ∂_τ̄ carries E-factors, so it is not a sum of unary-theta products.

Radial test R1 (x ∈ {1, ½, ⅓, ⅔}, 6 companions, t_j = 2^{−j}·0.02/(2m)²):
- For the completed Ŝ_ν, the max |c1| is 5.6e−10 and the max |c2| is 1.6e−8. Both are ≤ 1e−6, so **pass 4/4**: the completed A1 and A2 vanish.
- Control: the uncompleted S_ν gives |c1| from 0.48 to 1.13 (> 1e−3, as required).

## Verdicts
- Odd orthant completion: obeys the fixed S-law. **Pass.**
- Even double orthant: the proposed product completion **fails**. The even piece has no weight-1 Zwegers/Vignéras completion of this type.
- Completed full series: **fails** the fixed S-law. The whole failure equals ½ × the failure of the even piece (F2).
- A1/A2: after any smooth completion they vanish identically (R1), so radial "closure" is automatic and does not discriminate. The obstruction is visible only in the interior S-law.
- **Shadow rule (preregistered): the full-series shadow is NOT located.** What is located: the cone part plus the odd orthant, with four weight-3/2 unary thetas (5n²/2, R²/34, 35m²/4 glued to the walls 7/2, 595/2, 1). Not completed: the even double orthant and the axis half-lines.
