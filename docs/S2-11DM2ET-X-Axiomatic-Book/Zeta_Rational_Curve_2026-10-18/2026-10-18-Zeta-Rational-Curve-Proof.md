# ζ_E(0;s) and ζ_E(−1;s) lie on one rational curve in s: proof for every integer s ≥ 3
> *Master copy (2026-10-18): cross-references to unpublished local folders were removed; the mathematics is unchanged.*


**Date:** 2026-10-18, work done 10:07–10:14 CDT. **Box only.** Nothing was pushed or emailed.
**Folder:** `reports/heavy-daily/2026-10-18-Zeta-Rational-Curve-Proof/`
**Scope:** pure mathematics.
**Status:** Cat A for every algebraic step, all done symbolically in s. The only analytic input is two standard published facts, F1 and F2 in §2. They are cited, not re-proved, which is the same convention as Lemma P in the C_third report. **No step rests on an unproved lemma.**

## 1. Theorem
**Setup, for an integer s ≥ 3:**
- Q_s(n,k) = n² + snk + (s/2)k(k+1)
- R = Σ_{n≥0, k≥1} q^{Q_s}, Mm = Σ_{n≤−1, k≤0} q^{Q_s}, E_s = R + Mm (the definition used in `series_s.py`)
- c₀ = s/(4(s−2))

Write E_s = Σ_m e_m q^m and define ζ_E(w;s) = Σ_m e_m (m − c₀)^{−w}. It converges for Re w > 1 and continues meromorphically.

**Theorem.** For every integer s ≥ 3:
- (a) ζ_E(0;s) = (s−4)(s−5) / (12(s−2))
- (b) ζ_E(−1;s) = (2s⁵ − 14s⁴ − 45s³ + 425s² − 632s − 96) / (1440(s−2)²)
- (c) The t^{−1} coefficient of E_s(e^{−t}) e^{c₀t} is arccosh(s−1)/√(s(s−2)). Its t^{−1/2} and t^{1/2} coefficients vanish.

For example: s=7 gives 1/10 and 29/1200; s=8 gives 1/6 and 5/36; s=11 gives 7/18 and 1129/1296. The framework values are three points on this single curve. As a curiosity, ζ_E(0) vanishes at s = 4 and s = 5.

**Validity range: integers s ≥ 3.**
- s ≥ 3 makes δ := 1/(2(s−2)) lie in (0, ½], which is exactly what the proof uses (§3, Steps 1–2).
- For s ≤ 2 the construction breaks: at s = 2 the shift a has a pole, and for s < 2 the form is no longer indefinite in the needed way.
- Non-integer s are not considered, because Q_s must be integer-valued.
- The framework itself uses only s ∈ {7, 8, 11}. Other s belong to the formal family.

## 2. Analytic inputs (cited, standard)
- **F1 (2-D Euler–Maclaurin).** Let Φ be smooth and rapidly decreasing on the closed quadrant, and x ∈ (0,1], y ∈ [0,1). Then as t → 0⁺, Σ_{i,j≥0} Φ(√t(x+i), √t(y+j)) has a full asymptotic expansion in powers t^{j/2}, with no log terms. It is obtained by iterating the 1-D formula Σ_{i≥0} φ(i+x) = ∫₀^∞ φ − Σ_{p≥1} B_p(x)/p!·φ^{(p−1)}(0) + R_N. References:
  - Zagier, *The Mellin transform and related analytic techniques*, 2006, §4;
  - Shintani, J. Fac. Sci. Univ. Tokyo 23 (1976), whose Bernoulli-polynomial formulas for cone zeta values at non-positive integers are equivalent.
- **F2 (Mellin dictionary).** Suppose Z(t) = Σ e^{−tQ(ν)} has the expansion Σ c_j t^{j/2} + Res·t^{−1} and decays exponentially as t → ∞. Then Γ(w)ζ(w) = ∫₀^∞ Z(t)t^{w−1}dt continues meromorphically, and ζ(−k) = (−1)^k k!·c_{2k}. In particular ζ(0) = c₀ and ζ(−1) = −c₂ (Zagier, op. cit.).

Both are used here exactly as in the earlier Lemma P and Shintani-cone computations.

## 3. Proof (every step checked in `prove_zeta.py`; all lines print PASS)
**Step 0: geometry (symbolic).** Put ν = (n,k) + a with a = (s/(2(s−2)), −1/(s−2)) and Q₂ = x² + sxy + (s/2)y². Then:
- Q_s(n,k) = Q₂(ν) + c₀.
- γ = [[−1,−s],[2,2s−1]] has det γ = 1, preserves Q₂, and satisfies γa − a = (0,−1), so γ preserves a+Z².
- With r₁ = (1,0) and r₂ = γr₁ = (−1,2), write ν = S r₁ + T r₂. Then

  **Q₂ = S² + 2(s−1)ST + T²,**

  and S = n + k/2 + ½ + δ, T = (k − 1/(s−2))/2.
- So in the γ-adapted basis the form depends on s **only through A = s−1 = ½ tr γ**.

**Step 1: Lemma E, E_s equals the sum over the half-open cone C = {S > 0, T ≥ 0} of a + Z² (all s ≥ 3, Cat A).**
- Since 0 < 1/(s−2) ≤ 1, T ≥ 0 ⇔ k ≥ 1. So C ∩ (a+Z²) = {k ≥ 1, n + k/2 + ½ + δ > 0}.
- This set contains R = {n ≥ 0, k ≥ 1}. The remainder is C∖R = {n ≤ −1, k ≥ 1, k > −2n − 1 − 2δ}. Because 0 < 2δ ≤ 1, this is exactly {n ≤ −1, k ≥ −2n − 1}, and k ≥ 1 then holds automatically.
- The involution φ(n,k) = (n, −2n−k−1) preserves Q_s. This is a symbolic identity; φ is the reflection of the coset fixing n.
- φ maps Mm = {n ≤ −1, k ≤ 0} bijectively onto {n ≤ −1, k ≥ −2n−1} = C∖R.
- Hence E_s = Σ_{ν∈C∩(a+Z²)} q^{Q₂(ν)+c₀}, so ζ_E(w;s) = Σ_{ν∈C∩(a+Z²)} Q₂(ν)^{−w}.
- A brute-force region check over s = 3..60 found 0 mismatches. The earlier q^3000 checks for s = 7, 8, 11 are consistent with this.

**Step 2: two classes, uniform in s (Cat A).** The (S,T)-lattice of a+Z² is Λ = Z(1,0) + Z(½,½), and [Λ : Z²] = 2. So C ∩ (a+Z²) is the union of two translated quadrants (x+i, y+j), i, j ≥ 0:

| class | from | (x, y) |
|---|---|---|
| 1 | k even | (½ + δ, 1 − δ) |
| 2 | k odd | (δ, ½ − δ) |

For s ≥ 3 these satisfy x ∈ (0,1] and y ∈ [0,1). **There is no case split by parity or any other residue.** The half-integer (s/2)k(k+1) is absorbed by the shift a, whose coordinates are rational in s.

**Step 3: Euler–Maclaurin coefficients (symbolic in s, x, y).**
- The script applies F1 to F = e^{−t(u² + 2Auv + v²)}. It computes the edge integrals ∫₀^∞ ∂^{p−1}F|_{edge} and the corner derivatives ∂_u^{p−1}∂_v^{q−1}F(0,0) with sympy, then collects powers of √t.
- Per class, it obtains:
  - t^{−1/2}: −√π(x+y−1)/2
  - **t⁰: B₁(x)B₁(y) + (A/2)(B₂(x) + B₂(y))**
  - t^{1/2}: −√π s(s−2)(x+y−1)(2x² − 2xy − x + 2y² − y)/12
  - t¹: an explicit polynomial in s, x, y (in `prove_zeta.txt`). It equals −B₄(x)(6A−4A³)/24 − B₄(y)(6A−4A³)/24 − (B₁B₃ + B₃B₁)/3 − A·B₂B₂/2.
- These are re-derived independently of the hand formulas in `shintani_s.py`, and agree with them.

**Step 4: summing the two classes (symbolic).**
- x+y−1 equals +½ for class 1 and −½ for class 2, so both half-integer coefficients cancel. This gives the vanishing part of (c).
- The t⁰ sum simplifies to (s−4)(s−5)/(12(s−2)), which is (a) by F2.
- The negative of the t¹ sum simplifies to the quintic over 1440(s−2)², which is (b) by F2.
- The area term is 2 · ½∫₀^∞ dm/(m² + 2Am + 1) = arccosh(s−1)/√(s(s−2)). The antiderivative was checked symbolically. This gives (c). ∎

## 4. Cross-checks
- **Exact earlier values:** the closed forms equal all 42 exact (s, cone) values from the independent cone code. That covers s = 3..20, 25, 30, 41 on two cones each. The cone r = (1,1) uses a *different* decomposition, with 3s+2 classes. **No mismatches.**
- **Numerical asymptotics** (`numeric_asymptotic_check.py`). For s = 3, 5, 13, 30, direct sums satisfy (Z(t) − Res/t − ζ(0) + ζ(−1)t)/t² → constant as t → 0, taking t ∝ 1/(s−1)². This supports the analytic input F1/F2.
- **Framework values:** for s = 7, 8, 11 the curve reproduces the values that were earlier confirmed by PARI Hecke L-functions.

## 5. Why the dependence on s is rational (structure)
- **One cone, two classes.** In the γ-adapted basis (r₁, γr₁), the residual series for every s is a sum over **one** Shintani cone with exactly **two** lattice classes. In Zagier's language, the reduced cycle has the same length for all s.
- **Where s enters.** The form is S² + 2AST + T² with A = s−1, the half-trace of γ. The class representatives are affine in δ = 1/(2(s−2)), which comes from the fixed-point shift a of the affine symmetry.
- **What the zeta values are made of.** Shintani/Euler–Maclaurin expresses ζ(0) and ζ(−1) of a cone as Bernoulli polynomials in the class coordinates, multiplied by Taylor coefficients of e^{−Q} at the corner and edge moments ∫v^m e^{−v²}. The coefficients are polynomials in A, and the Bernoulli factors are polynomials in δ. So every value at a non-positive integer is a polynomial in s and 1/(s−2), with rational coefficients.
- **Where the transcendental parts go.** √D and log ε enter only the area term, the residue arccosh(s−1)/√(s(s−2)) at t^{−1}. The half-integer terms carry √π but cancel between the two classes.
- **Denominators.** Degree-4 Bernoulli polynomials in δ would allow denominators up to (s−2)⁴. The symmetric two-class sum cancels them down to (s−2)¹ for ζ(0) and (s−2)² for ζ(−1).
- **Not a coincidence.** The framework values 1/10, 1/6, 7/18 and 29/1200, 5/36, 1129/1296 are samples of these two rational functions, which follow from this uniform cone structure.

## 6. Cat A / Cat B summary
| item | status |
|---|---|
| Q_s = Q₂(ν)+c₀; γ-invariance; cone form S²+2(s−1)ST+T² | Cat A (symbolic) |
| Lemma E: E_s = cone sum, all s ≥ 3 (via φ(n,k) = (n,−2n−k−1)) | Cat A (symbolic identity plus elementary integer inequality) |
| Two classes (½+δ, 1−δ), (δ, ½−δ), no case split | Cat A |
| Euler–Maclaurin coefficient algebra and the two-class sums (a), (b), (c) | Cat A (symbolic) |
| The analytic passage from expansion to ζ-values (F1 2-D EM, F2 Mellin) | cited standard theorems (Zagier 2006; Shintani 1976), not re-proved here |
| Relevance to the framework | only s = 7, 8, 11 are framework scales; the theorem is about the formal s-family |

## 7. Files (`2026-10-18-Zeta-Rational-Curve-Proof/`)
- `prove_zeta.py` → `prove_zeta.txt`: all symbolic steps with PASS lines, plus the per-class coefficient table.
- `numeric_asymptotic_check.py` → `numeric_asymptotic_check.txt`
- `shintani_numeric.py` → `shintani_s3_s4.txt`: exact cone values for s = 3, 4. These complete the cross-check together with the s = 5..41 exact cone-value files, which are held in a separate local folder and not included here.
