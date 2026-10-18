# g_s: closed forms in s, proof, relations to E_s / P_s / H_s / Θ_hol, parity split and cusp onset
> *Master copy (2026-10-18): cross-references to unpublished local folders were removed; the mathematics is unchanged.*


Date: 2026-10-18 (CDT). Box only. Nothing pushed or emailed.
Folder: `2026-10-18-g_s-Closed-Forms/`.
Labels: **Cat A** means proved symbolically, or exact on the stated finite range. **Cat B** means exploratory or interpretive.

## 0. Definition and source

**g_s(q) = Σ_{n≥0} q^{n²} / (−q^s; q^s)_n**

- **Source:** Master contact 23, `docs/S2-11DM2ET-X-Axiomatic-Book/42_Discrete_Contacts.md` l.31 (commit e18ca14; local clone `oct17-master`). The entry reads "sum q^{n^2}/(-q^s;q^s)_n | locked | Mixed scale; s in {7,8,11}". Contact 8 gives the level set {7, 8, 11} ("Levels for series g_s").
- **Also quoted in:** `2026-10-17-Residual-Identities-Mock-Theta-Status.md` §2 (A2, B1) and `2026-10-17-Levers-1-2-Hecke-g7-Cthird.md`. The latter found the Bailey lemma negative for s ≥ 3.
- **Calibrations:** g₁ = f₀ (5th order) and g₂ = φ (3rd order).
- **Prefix check:** the published prefix g₇ = 1, 1, 0, 0, 1, 0, 0, 0, −1, 1, 0, −1, … is reproduced here (`relations.txt`).

## 1. Radial and asymptotic coefficients of g_s(e^{−t}), t → 0+ (items 1 and 3)

**Theorem G (Cat A, elementary proof, valid for every real s > 0).**
g_s(e^{−t}) ~ Σ_{k≥0} c_k(s) t^k as an asymptotic, not convergent, expansion. Each c_k(s) ∈ Q[s] has exact degree k. In particular:

- **t^{−1} coefficient = 0 and t^{−1/2} coefficient = 0** for all s, and every half-integer order vanishes.
- c₀ = 2
- c₁ = 2s − 6 = 2(s − 3)
- c₂ = 5s² − 44s + 75
- c₃ = (55s³ − 930s² + 3918s − 4683)/3
- c₄ = (1073s⁴ − 28864s³ + 214620s² − 593128s + 545835)/12
- c₅ through c₈ are in `prove_gs.txt`.

**Mellin values.** Define M(w) = ∫₀^∞ (g_s(e^{−t}) − 1) t^{w−1} dt, which converges for Re w > 0, and ζ_g(w) := M(w)/Γ(w). Then:

- **ζ_g(0) = 1**
- **ζ_g(−1) = 6 − 2s**
- ζ_g(−2) = 10s² − 88s + 150
- in general ζ_g(−k) = (−1)^k k! c_k(s), and there is no pole at w = 1.

Reading ζ_g as the Dirichlet series Σ a_m m^{−w} of the q-coefficients needs polynomial growth of a_m. That growth is not proved for general s (Cat B). For s = 1 (f₀) the coefficients grow like e^{c√m}.

**Proof** (`prove_gs.py`, sympy, all PASS).
1. Write 1/(−q^s;q^s)_n = 2^{−n} exp Σ_{j≤n} Λ(sjt), where Λ(x) = log(2/(1+e^{−x})) = x/2 − x²/8 + x⁴/192 − x⁶/2880 + …. This is analytic for |x| < π.
2. Expanding exp(−tn² + Σ_m λ_m (st)^m S_m(n)) in t, with S_m the Faulhaber polynomials, makes the t^k coefficient a polynomial in (n, s) of n-degree ≤ 2k and s-degree ≤ k.
3. Sum against 2^{−n} using A_m = Σ n^m 2^{−n} ∈ Q, where A₀ = 2 and A_m = Σ_{i<m} C(m,i) A_i. This gives c_k(s) ∈ Q[s].
4. **Remainder bound.** Split at N = t^{−1/3}.
   - For n ≤ N: the exponent is O(t^{1/3}) uniformly, and the Taylor remainder is ≤ C_K t^{K+1}(1+n)^{4K+4}. Summed against 2^{−n} this is O(t^{K+1}).
   - For n > N with snt ≤ 1: each factor is ≤ 1/(1+e^{−1}), so the term is ≤ 0.7311^n.
   - For snt > 1: the term is ≤ e^{−tn²} ≤ e^{−n/s}.
   - Both tails, and the formal tail Σ_{n>N} 2^{−n}|poly|, are superpolynomially small in t.
5. Hence the expansion holds for every fixed real s > 0. No unproved lemma is used.

**Why the dependence is polynomial, not rational like ζ_E.**
- g_s has no lattice or cone structure. The damping comes from (−q^s;q^s)_n → 2^n, not from a quadratic form.
- So there is no area term, no 1/(s−2) cone geometry, and no Bernoulli evaluation at s-dependent offsets. s enters only through the variable st inside Λ.
- By contrast, ζ_E has the pole at s = 2 because the class offsets δ = 1/(2(s−2)) sit in Bernoulli polynomials.

## 2. Pre-registration, fit and held-out test (item 2)

- **Pre-registration:** `00_PREREGISTRATION_gs.md`, sha256 `8da9d9a6cab2cb1fd16c545e8660803b5eb3d50d81f033d7267cee9df9ac1794`, written at 10:24 CDT before any g_s numerics.
- **Disclosure:** I had already worked out c₀ = 2 and c₁ = 2s − 6 by hand, so those two are not blind.
- **Hypotheses:**
  - H1: no t^{−1} or t^{−1/2} term, and c₀ = 2.
  - H2: c_k ∈ Q[s] with degree ≤ k.
  - H3: ζ_g(−k) polynomial in s.
- **Numerics** (`gs_numeric.py` → `gs_numeric.json`):
  - direct mpmath evaluation at 80 digits;
  - degree-16 and degree-18 polynomial fits in t on st ∈ [3·10⁻⁴, 6·10⁻³];
  - s = 1, 2, 3..20, 25, 30, 41;
  - stability between the two fits is 10⁻¹⁵ to 10⁻⁹ (s = 1 is worst, at 3·10⁻⁵).
- **Fit set:** s = 3..7. **Held-out set:** s = 1, 2, 8..20, 25, 30, 41 (`gs_fit_heldout.txt`).

| k | fitted on s = 3..7 | worst held-out relative deviation |
|---|---|---|
| 0 | 2 | 1.5e−19 |
| 1 | 2s − 6 | 6.6e−16 |
| 2 | 5s² − 44s + 75 | 2.8e−13 |
| 3 | 55s³/3 − 310s² + 1306s − 1561 | 4.1e−11 |
| 4 | 1073s⁴/12 − … + 181945/4 | 3.0e−9 |

- In every row the worst deviation is at s = 1, the numerically weakest point, and it is within that point's fit stability. All other held-out s agree to about 10⁻¹⁵.
- The symbolic c₀..c₄ equal the fitted polynomials exactly. They agree with the numerics for s = 3..20, 25, 30, 41 to 2.2e−15.
- **Result:** H1, H2 and H3 are confirmed, then proved (Theorem G).
- **Recorded failure:** an extra guess I made during the proof (not pre-registered) was that the leading coefficient is lc_k = Li_{−2k}(½)/(4^k k!). It **fails**. In fact lc_k = [u^k] Σ_n Π_{j≤n} 1/(1+e^{−uj}), the s → ∞ limit with st = u fixed.

## 3. P_s and Θ_hol as functions of s through order t¹ (item 4 support)

This generalises the s = 7, 8, 11 table to all s ≥ 3 (`prove_P_Theta.py` → `prove_P_Theta.txt`).

**Status: Cat A algebra, with the same cited input F1 (2-D Euler–Maclaurin) as the ζ-curve proof.**

Method:
- R = Σ_{n≥0,k≥1} q^{Q_s} = e^{−tc₀} Σ_{quadrant} e^{−tQ₂} is a single class with offsets (½ + 1/(s−2), 1 − 1/(s−2)).
- P = R + (1+θ₃)/2.
- Θ_hol = E − 2R, using the proved E_s coefficients.

| object | t^{−1} | t^{−1/2} | t^0 | t^{1/2} | t^1 |
|---|---|---|---|---|---|
| E_s | Res | 0 | ζ_E(0) − c₀Res | 0 | −ζ_E(−1) − c₀ζ_E(0) + c₀²Res/2 |
| P_s | Res/2 | √π(s² − 2√(2s))/(4s(s−2)) | (1 + E₀)/2 | P_{1/2}(s) | E₁/2 |
| Θ_hol | 0 | √π(s²/2 − 2s + √(2s))/(s(s−2)) | 0 | −2P_{1/2}(s) | 0 |
| g_s | 0 | 0 | 2 | 0 | 2s − 6 |

Notes on the table:
- Res = arccosh(s−1)/√(s(s−2)) and c₀ = s/(4(s−2)).
- P_{1/2}(s) = √π[s⁶ − 10s⁵ + 36s⁴ − 56s³ + 32s² + √2(s^{9/2} − 4s^{7/2} + 16s^{3/2} − 16√s)]/(48(s−2)⁵).

Checks:
- The P_s t^{−1/2} closed form was guessed in advance and now PASSes symbolically.
- The table agrees with `2026-10-18-s8-s11/asym_s.txt` at s = 7, 8, 11 to about 3e−16.

## 4. Relations as functions of s (item 4)

- **(Cat A) Identities valid for all s ≥ 3:**
  - 2P_s = E_s + 1 + θ₃ − Θ_hol
  - P = R + (1+θ₃)/2
  - C_third = P_s + Θ_hol − θ₃
  - q⁸f = Θ_hol − θ₃
- **(Cat A, exact on the stated range) g_s is not in span_Q{1, θ₃, R, Mm}.** That span contains P_s, E_s, Θ_hol, C_third and q⁸f.
  - Test: exact rational rank to q⁴⁰⁰ for s = 3..20, 25, 30, 41 (`relations.txt`).
  - Result: the rank goes from 4 to 5 every time.
  - Independent radial argument (Cat A): any combination in that span with no t^{−1} and no t^{−1/2} must cancel Res and the √(2s) terms. Its t^0 term is then not the constant 2 with polynomial higher orders in general. Theorem G is the cleaner statement.
- **(Cat A, trivial) Coefficientwise,** g_s = Σ_{n≥0} q^{n²} + O(q^{s+1}) = (1+θ₃)/2 + O(q^{s+1}). This is the q-expansion part of P_s. The radial limits do not commute: g_s(e^{−t}) → 2, while (1+θ₃)/2 ~ √π/(2√t).
- **(Cat A for the algebra, Cat B for the Zwegers framing) H_s.** Master definition: M = [[2,s],[s,s]], c₁ = (−1,1), c₂ = (−4,1) (`Hs_conditions.txt`).
  - Q(c₁) = 1 − s/2 and Q(c₂) = 16 − 7s/2.
  - **H_s is a Zwegers-admissible indefinite theta only for integer s ≥ 5.** At s = 3 and 4, Q(c₂) > 0.
  - B(c₁,c₂) = −4(s−2), which equals −20 at s = 7. I am noting this, not interpreting it.
  - C := P_s − H_s, and H_s t^{−1} = 0 (Lemma 2 of the Bridge-C report, cited). So the t^{−1} coefficient of C is Res/2 = arccosh(s−1)/(2√(s(s−2))) for s ≥ 5.
  - **Not done:** the higher radial coefficients of H_s (and so of C) as functions of s. I did not derive them symbolically, so the full C = −H_s + P_s decomposition in s stays open.
- **Summary of the s-dependence:**
  - E, P, Θ: the coefficients lie in Q(s, √s, √(s−2), π^{1/2}, arccosh(s−1)), with poles only at s = 2.
  - g_s: pure Q[s], no poles, valid for every real s > 0, including the mock-theta calibrations s = 1, 2.
  - The only overlap is at q-coefficient level: g_s and P_s share Σq^{n²} up to q^s.

## 5. Parity split (Lemma P) and cusp onset as functions of s (item 5)

**Parity split, Cat A modulo F1, for all s ≥ 3 at the cusp x = 0.**
- Θ_hol has no integer-order terms through t¹ (t^{−1}, t^0 and t^1 coefficients vanish symbolically).
- So the integer orders of P_s equal those of (1+E_s)/2, and the half-integer orders equal those of (θ₃ − Θ_hol)/2.
- This is Lemma P at x = 0, now as an identity in s rather than at s = 7, 8, 11.
- The other rationals x were not redone for general s.
- g_s sits entirely in the integer-order sector with zero half-integer part, but it is not a member of the (1+E)/2 family: its t^{−1} coefficient is 0.

**Cusp onset** (`cusp_onset.py`; Cat A for the counts on the finite range; Cat B that "h⁺ ≠ #genera ⇔ cusp part").
- h⁺ = number of cycles of reduced primitive forms of D(s), with D = 4s(s−2) for odd s and s(s−2) for even s.
- Genera = cosets of the principal-form values in (Z/D)^×.
- Cross-check: PARI's wide class number and unit norm (`pari_crosscheck.txt`) give h⁺ = 2h in every case except D = 8 (h⁺ = h = 1, unit norm −1). This agrees with my h⁺ in every case.

| s | D | h⁺ | genera | cusp part expected |
|---|---|---|---|---|
| 3 | 12 | 2 | 2 | no |
| 4 | 8 | 1 | 1 | no |
| 5 | 60 | 4 | 4 | no |
| 6 | 24 | 2 | 2 | no |
| 7 | 140 | 4 | 4 | no |
| 8 | 48 | 2 | 2 | no |
| 9 | 252 | 4 | 4 | no |
| 10 | 80 | 2 | 2 | no |
| **11** | 396 | 8 | **4** | **yes** |
| 12 | 120 | 4 | 4 | no |
| 13 | 572 | 4 | 4 | no |
| 14 | 168 | 4 | 4 | no |
| 15 | 780 | 8 | 8 | no |
| 16 | 224 | 4 | 4 | no |
| 17 | 1020 | 8 | 8 | no |
| 18 | 288 | 4 | 4 | no |
| **19** | 1292 | 8 | 4 | **yes** |
| 20 | 360 | 4 | 4 | no |
| **25** | 2300 | 12 | 4 | **yes** |
| 30 | 840 | 8 | 8 | no |
| **41** | 6396 | 24 | 8 | **yes** |

- **Correction to `2026-10-18-s8-s11-Analogues.md`.** That report listed s = 11 as "h⁺ = 8, genera = 2". The number of genera for D = 396 is **4**. This follows from the coset computation and from Gauss's count 2^{μ−1} with μ = 3 (characters at 3, 11 and the 2-adic δ). So Cl⁺ ≅ Z/4 × Z/2, not Z/8. The conclusion "h⁺ > genera, so a cusp part" is unchanged.
- **Below 21, the cusp onset happens at s = 11 and s = 19.** s = 25 and 41 also qualify. s = 19, 25 and 41 are predictions only (Cat B): no Maass/cusp decomposition was run for them.
- **Where the onset shows up as a function of s:** nowhere in the cusp-0 radial data.
  - ζ_E(0), ζ_E(−1), Res, all P/Θ coefficients in §3 and all c_k(s) of g_s are smooth (rational or polynomial) in s. They are blind to the class group.
  - This is Cat A for the statement that these coefficients are given by s-uniform formulas.
  - The onset lives only in the arithmetic decomposition: ray-class weights, the Eisenstein vs non-genus characters at other cusps or rationals.
  - g_s, having no lattice structure at all, carries no class-group information in its radial data.

## 6. Category summary

- **Cat A:**
  - Theorem G: all c_k(s) ∈ Q[s]; zero t^{−1} and t^{−1/2} terms; ζ_g(0) = 1, ζ_g(−1) = 6 − 2s; c₀..c₈ explicit; valid for all real s > 0.
  - The held-out confirmation.
  - The P_s and Θ_hol coefficients through t¹ for all s ≥ 3, and the parity split at x = 0 (modulo the cited F1, as in the ζ-curve proof).
  - The non-membership of g_s in the span (to q⁴⁰⁰, on the stated s range).
  - The H_s admissibility (s ≥ 5).
  - The h⁺ and genera counts.
- **Cat B:**
  - h⁺ ≠ genera ⇔ cusp part, as an explanation, and the predicted cusp parts at s = 19, 25, 41.
  - The Dirichlet-series reading of ζ_g.
  - The H_s / C higher coefficients in s (not computed).

## 7. Files (in `2026-10-18-g_s-Closed-Forms/`)

- Pre-registration: `00_PREREGISTRATION_gs.md` (held locally, not included; its sha256 is given in §2)
- Numerics: `gs_numeric.py` → `gs_numeric.json`
- Fit and held-out test: `gs_fit_heldout.py` → `.txt`
- g_s proof: `prove_gs.py` → `prove_gs.txt`, `gs_coeffs.pkl`
- P_s / Θ_hol: `prove_P_Theta.py` → `prove_P_Theta.txt`, `PTh_coeffs.pkl`
- Relations: `relations.py` → `.txt`, `.json`
- H_s conditions: `Hs_conditions.py` → `.txt`
- Cusp onset: `cusp_onset.py` → `.txt`, `.json`; `pari_crosscheck.txt`
