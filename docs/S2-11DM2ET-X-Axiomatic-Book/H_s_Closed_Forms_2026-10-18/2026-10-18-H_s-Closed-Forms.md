> **Master-copy notation note (added 2026-10-18 at push; report text below is otherwise verbatim).** Labels B1–B8 are this report's own item labels; they are not reused on Master. Prediction PB5 (a rational t^1 term) was refuted (the term is 0). Category convention for Master (rev. 4): Cat A = proved, or exact (including exact finite computation); floating-point-only results = Cat B. Where this report labels a floating result Cat A, read it as Cat B (C12, C13). Theorem names: Theorem G = Lewis–Zagier period theorem (rev. 3 meaning); the g_s asymptotics = Theorem G_s; the zero-set theorem = Theorem D. Erratum: ERRATUM_Consolidated_CrossReview_2026-10-18.md. Consolidated statement: Bridge_C_Consolidated_rev4_2026-10-18/.

# H_s: closed forms in s (q-series, Zwegers parameters, radial coefficients) and the assembly C = −H_s + P_s (2026-10-18, CDT)

Scripts and outputs: `2026-10-18-H_s-Closed-Forms/`. Everything ran locally. Nothing was pushed, posted or emailed.

This continues the Path B work of the interrupted run (`2026-10-18-Paths-A-B-C/B`, copied here). The pre-registration `00_PREREG_B.md` (sha256 in `00_PREREG_B.sha256`, written 11:31 CDT) is unchanged.

**Labels.**
- **Cat A** = exact or proved. Finite-range checks are flagged as such.
- **Cat B** = numerical or conjectural.
- **F1** = the cited 2-D Euler–Maclaurin expansion for cone sums with averaged edge weights. It is the same input as in the ζ-curve and P_s proofs.

No TPC or RH claims are made.

**Definition (Master).**
- H_s = Σ_{v∈Z²} w(v) q^{Q_s(v)}, with Q_s(n,k) = n² + snk + (s/2)k(k+1).
- w = ½(sgn B(c₁,v) − sgn B(c₂,v)), with M = [[2,s],[s,s]], c₁ = (−1,1) and c₂ = (−4,1).
- C := P_s − H_s.

**Notation.**
- g := gcd(24, s−8).
- c₀ := s/(4(s−2)).
- Δ := 7s² − 46s + 64 = (s−2)(7s−32).

## 0. Summary

| # | Result | Cat |
|---|---|---|
| B1 | **q-series closed form** (Theorem G_s style), valid for all s ≥ 5 (§1) | A (case analysis; checked to q⁴⁰⁰ for s = 5..30, 41) |
| B2 | **s-stable two-variable form:** H_s(q) = 𝓗(q, q^s) up to an explicit exponent ≥ 4s+16, for s ≥ 9 (§2) | A (case analysis; first deviation predicted exactly at 37 values of s) |
| B3 | **Zwegers parameters as functions of s** (§3): a, Q(c_i), B(c₁,c₂), the orthogonal vectors, and **4Q(c₁)Q(c₂) = Δ** | A |
| B4 | **Characteristic correction:** H_s = ½q^{c₀}ϑ^{c₁,c₂}_{a,0,hol} + Δ_lines(s), where Δ_lines is a finite sum of unary theta series with explicit s-dependence (§3.2) | A (identity proved; checked to q⁴⁰⁰ for 27 values of s) |
| B5 | **Shadow data in s.** The c₁-part of the completion factors exactly as a weight-3/2 unary theta in Z + s/(2(s−2)) times Σ_{y∈Z+½} q^{(s/2)y²}. The c₂-part is a finite coset sum with explicit forms (§3.3). | A for the algebra; the modular completion itself rests on Zwegers (thesis 2002, Cor. 2.9, cited, not re-checked) |
| B6 | **Radial coefficients at x = 0**, closed in s (§4): H_{−1} = H₀ = H₁ = 0; H_{∓1/2} closed; H₅ ≡ 0 | A modulo F1 (from the interrupted run, re-verified) |
| B7 | **All integer radial orders of H_s vanish at x = 0, to every order** (new; §4.2) | A modulo F1 |
| B8 | **Assembly into C:** C_int = (1+E_s)/2 to all orders at x = 0, C_half = (θ₃ − Θ_hol,s)/2 − H_s; closed forms through t¹ (§5) | A modulo F1 and Hecke |

## 1. q-series closed form (B1)

Case analysis of w:
- B(c₁,v) = (s−2)n and B(c₂,v) = (s−8)n − 3sk.
- w = +1 when n ≥ 1 and 3sk > (s−8)n.
- w = −1 on the negatives of those points.
- w = ½·sgn(k) on n = 0.
- w = ½ on the wall 3sk = (s−8)n with n ≥ 1.
- Q_s(−v) = Q_s(v) − sk.

Hence, for every s ≥ 5:

  **H_s(q) = Σ_{n≥1} Σ_{k > (s−8)n/(3s)} ( q^{Q_s(n,k)} − q^{Q_s(n,k) − sk} )
       + ½ Σ_{k≥1} ( q^{sk(k+1)/2} − q^{sk(k−1)/2} )
       + ½ Σ_{n≥1, 3s | (s−8)n} ( q^{Q_s(n,k_n)} − q^{Q_s(n,k_n) − sk_n} ),  k_n = (s−8)n/(3s).**

- The identity is exact, by the case analysis above. It was checked against the brute-force Master definition to q⁴⁰⁰ for s = 5..30 and 41: **27 of 27 PASS** (`H_zwegers.py` → `H_zwegers.txt`).
- The wall sum is non-empty only when (3s/g) | n. Its first term sits at exponent ≥ (3s/g)².
- The leading terms are universal: H_s = −½ − q^{s+1} + q^{2s+1} − q^{2s+4} − q^{3s+1} + q^{3s+4} − …

## 2. s-stable two-variable form (B2)

Define

  𝓗(x, y) = Σ_{n≥1} Σ_{k≥⌈n/3⌉} x^{n²}( y^{nk+k(k+1)/2} − y^{nk+k(k−1)/2} ) + ½ Σ_{k≥1}( y^{k(k+1)/2} − y^{k(k−1)/2} ).

- **Claim.** For s ≥ 9, H_s(q) = 𝓗(q, q^s) + O(q^{e(s)}). Here e(s) is the least exponent of either of the following:
  - a boundary point (n, ⌈n/3⌉−1) that satisfies 3sk > (s−8)n, which needs s(n−3⌈n/3⌉+3) < 8n;
  - a wall point.
- Explicitly, e(s) = 4s+16 for 9 ≤ s ≤ 32 (from n = 4), and e(s) = 15s+49 for 33 ≤ s ≤ 55 (from n = 7). The second formula was checked at s = 33..41 and 50.
- Checked to q³⁰⁰⁰ for s = 9..41, 50, 64, 80, 100: the first deviation equals the predicted e(s) in **37 of 37 cases** (`H_stable.py` → `H_stable.txt`). [A]
- This is the analogue of the s-uniformity in Theorem G_s. There the coefficients are Q[s]-polynomials. Here 𝓗 is s-independent: each term is ±x^{n²}y^m. So below e(s), every coefficient of H_s sits at an exponent of the form n² + ms, and the (n, m) data do not depend on s. Distinct (n, m) can collide at a particular s.

## 3. Zwegers parameters in s (B3–B5)

### 3.1 Parameters (`H_zwegers.txt`, sympy) [A]

| quantity | value |
|---|---|
| M, det M | [[2,s],[s,s]], −s(s−2) |
| characteristic a = M⁻¹(0, s/2) | (s/(2(s−2)), −1/(s−2)); b = 0 |
| Q(a) | −c₀ = −s/(4(s−2)); so q^{Q_s(v)} = q^{c₀}q^{Q(v+a)} |
| Q(c₁), Q(c₂) | −(s−2)/2, −(7s−32)/2. Both are < 0 iff s ≥ 5. |
| B(c₁,c₂) | −4(s−2) < 0, so c₁ and c₂ are in the same component and the pair is admissible for s ≥ 5 |
| B(c₁,a), B(c₂,a) | s/2, s/2 |
| **4Q(c₁)Q(c₂)** | **(s−2)(7s−32) = Δ**, the radicand of the radial coefficients |
| orthogonal vectors | u₁ = (0,1), Q(u₁) = s/2; u₂ = (3s, s−8)/g, Q(u₂) = s(s−2)(7s−32)/(2g²) |
| lattice index of Zc_i ⊕ Zu_i | 1 for c₁; \|7s−32\|/g for c₂ |

### 3.2 Characteristic correction (B4) [A]
Master's weights use B(c,v), but Zwegers' weights use B(c,ν) with ν = v + a. These differ only on finitely many lattice lines:
- c₁: only on n = 0.
- c₂: only on lines L(v) := (s−8)n − 3sk = ℓ with −s/2 ≤ ℓ ≤ 0.

This gives

  **H_s = ½ q^{c₀} Σ_{ν∈a+Z²}(sgn B(c₁,ν) − sgn B(c₂,ν)) q^{Q(ν)}
     − ½Σ_{k∈Z} q^{sk(k+1)/2} + Σ_{−s/2<ℓ<0} Θ_ℓ + ½(Θ₀ + Θ_{−s/2}),**

where Θ_ℓ = Σ_{L(v)=ℓ} q^{Q_s(v)} (ℓ ∈ gZ) is a full positive-definite unary theta series along u₂.
- Checked to q⁴⁰⁰ for 27 values of s, all PASS (`H_zwegers.txt`).
- So H_s is a Zwegers holomorphic part *plus* weight-½ unary thetas, all with explicit s-dependence.

### 3.3 Shadow data (B5)
**c₁-part.** Write ν = x c₁ + y u₁. Then x = −(n + a₁) ∈ −(Z + s/(2(s−2))) and y = k + n + a₁ + a₂ ∈ Z + ½, because **a₁ + a₂ = ½ for every s**. The lattice therefore splits as a product, and the c₁-completion term factors exactly [A]:

  (non-holomorphic weight-½ error-function series of −(s−2)x²/2 over x ∈ Z + s/(2(s−2))) × Σ_{y∈Z+½} q^{(s/2)y²}.

Its shadow is ∝ ḡ₁·θ₁, where:
- g₁(τ) = Σ_{m∈Z+s/(2(s−2))} m q^{(s−2)m²/2} (weight 3/2);
- θ₁ = Σ_{y∈Z+½} q^{(s/2)y²} (weight ½).

**c₂-part.** ℓ = B(c₂,ν) ∈ gZ + s/2, with exponent ℓ²/(2(7s−32)). The orthogonal unary theta is in the variable j ∈ Z + β(ℓ), with form Q(u₂)j². This is a sum over |7s−32|/g cosets.

The transformation law of the completed function is Zwegers Cor. 2.9 (cited; not re-checked here), so the vector-valued modular statement is conditional on that citation.

**s = 5 (Cat A).** Here Q(c₁) = Q(c₂) = −3/2. The involution (n,k) ↦ (n+5k, −k) swaps the two cone walls, and **H₅ ≡ 0** (checked to q²⁰⁰⁰ in the interrupted run, and to q⁴⁰⁰ again here).

## 4. Radial coefficients at x = 0 (B6, B7)

### 4.1 Closed forms through t¹ (`H_closed.txt`, `H_closed_simplified.txt`) [A modulo F1]
- **H_{−1} = H₀ = H₁ = 0.**
- **H_{−1/2} = ½√(2πs)·[ 1/√((s−2)(7s−32)) − 1/(s−2) ]** = ½√(2πs)/(−2Q(c₁))·[√(Q(c₁)/Q(c₂)) − 1]. It does not depend on g.
- **H_{1/2} = √(2πs)/(48(s−2)²)·[ −(s−4)(3s−2) + (s³ − 44s² + 192s + 2g²(s−2))·√(s−2)/(7s−32)^{3/2} ].** It depends on s mod 24 only through g², and vanishes at s = 5.

Checks:
- exact per-s Bernoulli sums at s = 5..60, 99, 100, 151, 223, 300 (0 mismatches);
- direct small-t numerics at s = 5..13, 20, 25, 41, where (H − prediction)/t^{3/2} tends to a constant;
- the simplified forms reproduce the stored values (e.g. s = 7: −0.303525413 and −0.395940835).

Example values (all of them are in `C_assemble.txt`):

| s | g | H_{−1/2} | H_{1/2} |
|---|---|---|---|
| 7 | 1 | −0.303525413 | −0.395940835 |
| 11 | 3 | −0.255311940 | −0.500530945 |
| 19 | 1 | −0.189515705 | −0.666897291 |
| 25 | 1 | −0.163190334 | −0.766397760 |
| 41 | 3 | −0.125299598 | −0.983043817 |

**PB5 of the pre-registration is refuted.** The predicted rational t¹ term is identically 0, because the Dedekind–Rademacher sums cancel under j → m − j.

### 4.2 All integer orders vanish (B7) [A modulo F1]
By B4, H_s = ½q^{c₀}ϑ_hol + Δ_lines. Each piece contributes only half-integer orders:
- **Δ_lines.** Every term is a full unary theta. At x = 0 it equals c·t^{−1/2}·e^{−κt} plus an exponentially small term, so it carries only half-integer orders.
- **ϑ_hol.** ϑ_hol = 2(E^K_a − E^K_{−a}), with wall points weighted ½.
  - ν ↦ −ν maps the cone classes of −a + Z² to those of a + Z², sending the offsets (x₀, y₀) to (1−x₀, 1−y₀). Edge offsets go to themselves, with the averaged weights.
  - Since B_p(1−x) = (−1)^p B_p(x), the order-j Euler–Maclaurin coefficients of the two sums differ by (−1)^j. So only odd j survive, i.e. only half-integer powers of t. This is the argument of Lemma P(a) of the C_third report.
  - Multiplying by q^{c₀} = e^{−c₀t} preserves the parity.

This extends H_{−1} = H₀ = H₁ = 0 (computed independently, symbolically) to all orders. It was not done at x ≠ 0.

## 5. How H_s combines with P_s into C (B8)

**q-series:**
- C = ½ + ½θ₃ + Σ_{n≥0,k≥1} q^{Q_s(n,k)} − H_s.
- R := Σ_{n≥0,k≥1} q^{Q_s} equals q^{c₀}E^{Q₁}_a, the open-quadrant sum on the same coset a + Z².
- H_s is given by B1, or by B4.
- So **C is the coset a + Z² of the single form Q with cone weight 1_{Q₁} − ½(1_K − 1_{−K}), plus ½ + ½θ₃ minus unary thetas.** [A]

**Radial parity at x = 0, to all orders [A modulo F1 and Hecke's theorem]:**
- integer orders of C = integer orders of P_s = (1+E_s)/2 (from 2P_s = E_s + 1 + θ₃ − Θ_hol, Θ_hol odd, and §4.2);
- half-integer orders of C = those of (θ₃ − Θ_hol,s)/2 − H_s.

**Closed forms through t¹ (`C_assemble.txt`):**
- C_{−1} = arccosh(s−1)/(2√(s(s−2))) = Res/2.
- C₀ = (1+E₀)/2.
- C₁ = E₁/2.
- C_{∓1/2} = P_{∓1/2} − H_{∓1/2}, given explicitly in the file. For example, **C_{−1/2}(7) = 0.829142617**. This replaces the earlier fitted value ≈ 0.8174 of Bridge-C B4.

| s | C_{−1} | C_{−1/2} | C₀ | C_{1/2} | C₁ |
|---|---|---|---|---|---|
| 7 | 0.209419820 | 0.829142617 | 0.476703063 | 0.662805795 | −0.016756369 |
| 11 | 0.150415107 | 0.754907457 | 0.648484273 | 0.914457001 | −0.487962875 |
| 19 | 0.099674672 | 0.667846634 | 0.986855606 | 1.375323367 | −3.696693063 |
| 25 | 0.080711065 | 0.633937018 | 1.238937211 | 1.695897272 | −9.136449802 |
| 41 | 0.054790504 | 0.586117987 | 1.908676855 | 2.502486522 | −43.686717151 |

## 6. Comparison with Theorem G_s
| | g_s (Theorem G_s) | H_s (this report) |
|---|---|---|
| q-series | Σ q^{n²}/(−q^s;q^s)_n | B1 (cone double sum) and B2 (𝓗(q, q^s)) |
| radial coefficients | c_k(s) ∈ Q[s], integer orders only | half-integer orders only (B7); coefficients in √π·Q(s, √s, √(s−2), √(7s−32)) with g-dependence from t^{1/2} |
| validity | every real s > 0 | integer s ≥ 5 (Zwegers admissibility) |
| modular structure | none known for s ≥ 3 | Zwegers holomorphic part plus unary thetas (B4/B5) |

## 7. Open
- Radial coefficients at orders t^{3/2} and beyond, in closed form. They would need Pm > 4 in `H_em.py`, which has not been run.
- The radial expansion at x ≠ 0 for general s.
- A full proof of F1 in the sector-uniform form used here. It is cited, as in earlier reports.
- The explicit vector-valued transformation matrices of the completed ½q^{c₀}ϑ̂ in s. Only the parameters are given; the transformation law is by citation.

## 8. Files (`2026-10-18-H_s-Closed-Forms/`)
- **Pre-registration:** 00_PREREG_B.md, 00_PREREG_B.sha256
- **Radial coefficients:** H_em.py, H_generic.pkl, H_closed.py/txt/pkl, H_closed_simplified.txt, H_values.py/txt, H_numeric.py/txt, H_numeric_small_t.py/txt
- **Assembly of C:** C_assemble.py/txt, C_closed.pkl
- **New this run:** H_zwegers.py/txt (B1, B3, B4 and the parameter table) and H_stable.py/txt (B2)
