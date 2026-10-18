# Independent audit: "The E_R cancellation, proved" (2026-10-18-ER-Cancellation-Proof.md)

Date: Sunday 2026-10-18, about 3:00–3:35 AM CDT (America/Chicago). Auditor: Grok Bot, for Arvin Hampton (539 Labs).
Box only. No Heavy, no Grok prompts, no pushes, no emails. The audited report, its folder, and the earlier reports were only read; none were edited.
Scripts and outputs: `2026-10-18-ER-cancellation-audit/` (listed in §6). The numerical code was written from scratch; the one reuse is flagged in §4.3.

Labels: **Cat A** means proved in the text (as audited) or a finite / high-precision computation with the check stated. **Cat B** means it rests on a cited or standard theorem not re-proved, or is a sketch.
This audit makes no HQCC, TPC or RH claims.

## 0. Verdict: **PASS WITH FIXES**

- **No fatal error found.** Every step of Theorem 1 (the Herglotz closed form on Re z > 0) and Theorem 2 (E_R in closed form) is correct, given the inputs (I1)–(I3).
- There are **3 fixable gaps** and **8 minor issues**. None of them changes a statement; all fixes are written out in §3.
- The independent numerics agree everywhere:
  - The per-character split G = 2R + T holds to ≤ 8·10⁻³⁴ for all 8 characters at 5 points, including one with Re z < 0.
  - Theorem 2 matches the from-scratch lattice coefficients of E_R for all N ≤ 14 000 (627 nonzero coefficients). The maximum deviation is 1.8·10⁻¹⁵, and all 627 coefficients agree exactly as elements A + Bφ of Z[φ].
  - Theorem 1 holds to ≤ 6·10⁻³⁵ at 6 points of H, to ≤ 2.5·10⁻¹⁶ at 8 points of Re z > 0 off H (double-precision period formula), and to ≤ 6·10⁻³⁵ at 8 rationals.
- **What stays conditional.** Theorem 1 and Theorem 2 are complete *given (I1)–(I3)*, which are Cat A inputs from earlier reports. I re-checked (I1) and the (I3) period formula numerically but did not re-audit their proofs. The identification Ψ(x) = κ-value ψ(x) at rationals also needs R1. R1 is correct in outline, but its remainder bookkeeping is a gap; the fix in §3 G3 is a standard argument.

## 1. Step-by-step check

| step | content | finding |
|---|---|---|
| §1 setup | η_a = ψ(−1), η_b = ψ(−1)χ₁₄₀(−1) | Correct. χ₁₄₀ is the character of the real quadratic field Q(√35), so it is even, and **η_aη_b = +1**. Checked: χ₁₄₀(139) = +1, and η_a = η_b for all 8 characters. |
| §1 | ρ_n = −b̂(n)/(2πi·140), ρ₀ = 0, Σρ_s = 0, ρ₋ₙ = η_bρ_n | Correct. b̂(0) = 0 because ψχ₁₄₀ is a nontrivial character mod 140. Numerically \|Σρ_s\| ≤ 10⁻³⁶ and ρ₀ = 0. |
| §1 (I1) | local check of r_χ | Correct, but "inert p: ψ(p)²(1−1+1)" is shorthand for r_χ(p²); the fact r_χ(p) = 0 for inert p is not stated (**m5**). Coefficientwise check from scratch: E_L = Σ w_χG_χ(·/20) exactly for 20Q ≤ 2000. |
| Lemma 1 | Mittag-Leffler B(u) = Σρ_s π cot π(u − s/140) | Correct. The residue is P(e(n/140))/(−2πi·140) = ρ_n; both sides tend to 0 at ±i∞ (deg P ≤ 139, Σρ = 0); Liouville in e(u) finishes it. Numerically ≤ 5·10⁻²⁹ at 3 points (both half-planes) for χ_{0,0} and χ_{4,1}. |
| Lemma 2 | digamma form φ(X) = −140Σρ_n/(n + 140X) | Correct. The constants cancel by Σρ = 0, and the 140-block partial sums converge. |
| Lemma 3 | holomorphy and growth of R | Correct on Re z > 0. Pairing s ↔ 140 − s gives β₁ = 0 for η_b = +1; numerically β₁ ≤ 4·10⁻³⁷ for the 4 even characters and 0.036–0.081 for the odd ones. **Gap G1:** holomorphy on H ∩ {Re z ≤ 0} is used but not proved. **m3:** the growth step does not say how the β₁/X tail is handled. |
| Prop. 4 | G = 2R + T | Correct. I re-derived steps 1–4: u_m − n/140 = −(7m + nz)/(140z), the two pieces are φ(X_m) and −η_bφ(−X_m), and Sing − R = T uses a(−m) = η_a a(m) and η_a = η_b. |
| Lemma 5 | two-variable summation by parts | Correct. The kernel identities were checked symbolically (sympy, exact 0): Δ_nF = −z/(w(w+z)); Δ_mΔ_nF = z(14w + 49 + 7z)/(w(w+z)(w+7)(w+7+z)); D²_nF = 2z²/(w(w+z)(w+2z)). **O(\|w\|⁻³) holds uniformly** because w + c (c ∈ {z, 7, 7+z, 2z}) is again a point n′z + 7m′ with n′ ≥ 1, so \|w + c\| ≥ max(Im z, \|w\| − \|c\|) ≥ c_z\|w\|. The text leaves this implicit (**m2**). **Boundary terms:** α(M)g(M) → 0 since g(M) = O(1/M), and β(N)k(N) → 0 since k(N) = O(1/(N·Im z)). Both are handled correctly. |
| Lemma 6 | inner m-sum via cot | Correct, including the sign and the 2πi/140. The symmetric limit in m versus the per-residue symmetric limits differ by O(1/M) (**m4**, unstated). |
| Prop. 7, trivial χ | second-order Λ, the ±(2/5)Σρ_n/(nz) cancellation | Correct. Σ_{n=1}^{140}β(n) = −Σjρ_j = 0 for even ρ (numerically 2·10⁻²⁹). Λ(const) = 0, and Fubini applies because D²F = O(\|w\|⁻³) is summable over (m ≠ 0, n ≥ 1). The recombination (2/5)(2πi/7) = (2πi/140)·8 = (2πi/140)[ǎ(20j) − ǎ*(20j)] is right. **The cancelled constant is genuinely nonzero:** (2/5)Σρ_n/(nz) = 0.0036057 + 0.0048075i at z = 0.6 + 0.45i. The "log ε" remark is right: Σρ_n/n = i·log ε/(70π) to 15 digits (h(Q(√35)) = 2 in the class number formula, Cat B standard). The n-outer iterated sum does diverge here: k(n) → −(2/5)πi/7 ≠ 0 while β(n) does not tend to 0. So the second-order argument is genuinely needed. |
| §4(a)–(c) | holomorphy, D = zP, entire 140-periodic extension | Correct. One correction: only Re z > 0 is needed (see G1). |
| §4(d), Lemma 8 | growth of Ψ on S, Cauchy | **Correct, and the geometry is right.** S has width 140 = one period. On S, \|q′\| = e^{2πY/140} ≥ e^{2π/140} and \|z\| ≤ 141 + Y = O(1 + log\|q′\|), so the whole exterior of a fixed circle is covered. I re-derived the constant-term integrand (log ε/2)·z(z+it)^{−3/2}(z−it)^{−1/2}; it is exact. The bounds \|z+it\| ≥ max(1, \|t−Y\|), \|z−it\| ≥ t + Y, \|v\| ≤ 1 and \|v_w̄\| ≤ ¼(\|z\|+t)^{1/2}t^{−1/2} all hold. The branch is fine: Im(t² + z²) = 2xy has constant sign in t, so R_z(it) never meets (−∞, 0]. **Exponent slip (m1):** \|D\| ≤ C(1+\|z\|)² gives \|P\| ≤ C(1 + log\|q′\|), not the square stated; either suffices. **On P = 0:** periodicity plus "no constant term" alone would *not* force P = 0 (e(z/140) is a counterexample). What forces it is the growth bound o(\|q′\|) as Im z → −∞, combined with the Laurent coefficients on C* agreeing with the H-Fourier coefficients, which have N ≥ 1 only. The text uses exactly this, so it is correct. |
| §5 | dictionary ν ↔ θ ∈ 𝔭₂ | Correct. θ = (7u − 2v) + u√35, N(θ) = 14u² − 28uv + 4v² = −140Q, B(ν,a) = (7u − 2v)/10. ε-invariance: Re(εθ) − Re θ = 5(A + 7B) ≡ 0 mod 10 for A ≡ B mod 2. Also observed: every frequency lies in (2/140)Z (**m8**, harmless). |
| §6.1 R2 | Fourier sum / Green integral interchange | Correct conclusion, two slips (**m6**). (i) "O(n²) lattice points with \|Q\| ≤ n" is wrong as stated: there are infinitely many; it is O(n) γ-orbits. The bound \|c_n\| ≤ C(1+\|n\|)² is still true. (ii) The frequencies are not integers (min \|Q\| = 4/140 for u_R, 0.35 for u_L), so the decay factor is e^{−2πn₀(y+s)} with n₀ = min\|Q\|, not e^{−2π(y+s)}. The dominating function stays integrable. |
| §6.2 R1 | sector-uniform Euler–Maclaurin | Correct in outline; **gap G3** (remainder bookkeeping); the dependency on R1 is **m7**. |

## 2. Issue list

| # | severity | issue |
|---|---|---|
| G1 | gap (fixable) | §4(a) claims D is holomorphic on U = H ∪ {Re z > 0}, and Prop. 4 step 3 uses Lemma 3 on all of H. Lemma 3 only proves convergence and holomorphy of R on Re z > 0. |
| G2 | gap (fixable) | Lemma 3 growth: the odd-case tail Σ_{m>20\|z\|} a(m)·20zβ₁/m is only conditionally convergent. Its O(1) bound needs Abel summation, which is not stated. The written three-term bound does not show where this term goes. |
| G3 | gap (fixable) | R1: the 2D Euler–Maclaurin remainder is bounded only for the bulk term. The inner-variable remainder, summed over the outer variable, and the edge remainders are not written. "The t^{±1/2} terms vanish as computed earlier" is also invoked without saying which computation or for which classes. |
| m1 | minor | §4(d): the (1 + log\|q′\|)² should be (1 + log\|q′\|); either suffices. Lemma 8's C(1+\|z\|)² is far from sharp: numerically \|Ψ(z)\|/\|z\| → 0.0666 ≈ log ε/(2π√35) on S (growth is linear; observation only, Cat A numerics, not proved). |
| m2 | minor | Lemma 5: the uniformity of O(\|w\|⁻³) over the lattice is not argued (one line, given in §1). |
| m3 | minor | Lemma 3 says "R = O(\|z\| log\|z\|)"; the argument actually gives O(\|z\|) (see G2 fix). Harmless. |
| m4 | minor | Lemma 6: symmetric-in-m limit vs per-residue symmetric limits (an O(1/M) difference) is not mentioned. |
| m5 | minor | §1 (I1) inert-prime shorthand: r_χ(p) = 0 and r_χ(p²) = ψ(p)²(1 − 1 + 1). |
| m6 | minor | R2: the counting justification and the decay rate e^{−2πn₀s}, n₀ = min\|Q\| > 0 (see §1 table). |
| m7 | minor | Dependency labelling. §0's "In particular, ψ(x) = Ψ(x) for x > 0" and §6.2's "this is now a proof" both depend on R1 when ψ means the Bernoulli/κ value. §0 says R1 is not needed for the main theorem, which is true for Theorem 1 itself; the corollary should cite R1 explicitly. |
| m8 | minor | Notational: E_R frequencies lie in (1/70)Z. "No constant term" for E_R holds because ν = 0 is excluded from the half-open cone; this is worth saying explicitly. |

No fatal issues.

## 3. Fixes

**G1 (holomorphy of R on U).** Either fix works.
- **(a) Extend Lemma 3 to U.** For z ∈ U, arg z ∈ (−π/2, π), so arg X_m = −arg z ∈ (−π, π/2), and X_m stays off (−∞, 0]. On a compact K ⊂ U, |arg X_m| ≤ π − δ_K and |X_m| ≍_K m. The uniform digamma asymptotics, and hence the decomposition R = Σ a(m)[φ(X_m) − 20zβ₁/m] + 20zβ₁Σa(m)/m, then hold on K exactly as in Lemma 3. So R is holomorphic on U, and Prop. 4 holds on all of H. Numerically, the split holds at z = −0.4 + 0.7i to ≤ 2·10⁻³⁵ (except 4·10⁻³⁴ for trivial χ), and Theorem 1 itself holds at z = −0.5 + 0.8i to 3·10⁻³⁵.
- **(b) Restrict.** Set U := {Re z > 0} throughout §4. Step (c) then reads: P := D/z is holomorphic on Re z > 0 and equals the H-Fourier series on H ∩ {Re z > 0}. P(z+140) − P(z) vanishes there, hence on Re z > 0. Extend by periodicity. Nothing else changes.

**G2 (tail in the growth bound).** For z ∈ S, X_m lies in the closed first quadrant, and |X_m| ≥ 1 for m ≥ M₀ := ⌈20|z|⌉. Write φ(X) = β₁/X + E(X) with |E(X)| ≤ C|X|⁻² there. Then:
- R = Σ_{m<M₀} a(m)φ(X_m) + 20zβ₁ Σ_{m≥M₀} a(m)/m + Σ_{m≥M₀} a(m)E(X_m).
- **First sum.** |φ| ≤ C on |X| ≤ 1 with Re(s/140 + X) ≥ 1/140, so it is O(|z|).
- **Second sum.** If β₁ ≠ 0 then η_b = −1, so η_a = −1 and a is odd. Then A(N) = Σ_{m≤N}a(m) is bounded, and Abel summation gives Σ_{m≥M₀} a(m)/m = O(1/M₀) = O(1/|z|). The term is O(1).
- **Third sum.** It is ≤ C Σ_{m≥M₀} (20|z|/m)² = O(|z|).
- Hence |R(z)| ≤ C(1 + |z|) on S. Numerically, max_χ |R_χ|/|z| stays at 0.50–0.53 for |z| from 1.4 to 1010 (`growth.txt`).

**G3 (R1 remainder bookkeeping).** Fix one residue class with u ∈ (0,1]×[0,1). Let g(y) := e^{−t q(y)}, where q(y) = Q((u+y)V)·M′² is positive definite on the closed quadrant: q(y) ≥ c|y|². Then |g| ≤ e^{−c sin δ·|t||y|²} for |arg t| ≤ π/2 − δ.

Use the 1D formula, valid for 0 < u ≤ 1 and order p:
  Σ_{k≥0} f(k+u) = ∫₀^∞ f − Σ_{j=1}^p (B_j(u)/j!) f^{(j−1)}(0) + ((−1)^{p+1}/p!) ∫₀^∞ B̃_p(u − y) f^{(p)}(y) dy.
Apply it in y₂ for each fixed k₁, and then sum over k₁, applying the same formula in y₁ to each resulting function of y₁. Homogeneity (∂^α g(y) = t^{|α|/2}(∂^αG)(√t·y), G = e^{−q}) gives:
- **Main term.** ∫∫g = t⁻¹∫∫G, valid for Re t > 0 by analytic continuation of the real-t identity.
- **Edge terms.** ∫₀^∞ ∂₂^{j−1}g(y₁,0) dy₁ ∝ t^{(j−2)/2}.
- **Corner terms.** ∂₁^{i−1}∂₂^{j−1}g(0) is a polynomial in t whose only t⁰ part is the term i = j = 1.
- **Remainders.** Bound them with |∂^α g(y)| ≤ C Σ_{l≤|α|} |t|^l |y|^{2l−|α|} e^{−c′|t||y|²}:
  - the double remainder is O(|t|^{p/2−1});
  - the edge remainders are O(|t|^{(p−1)/2});
  - the inner-variable remainder summed over k₁ is ≤ Σ_{k₁} ∫|∂₂^p g(u₁+k₁, y₂)| dy₂ ≤ C(|t|^{−1/2} + 1)|t|^{(p−1)/2}, by comparing the k₁-sum with an integral plus a sup.
- With p = 3, every remainder is O(|t|^{1/2}) uniformly in the sector. This gives s/t + h·t^{−1/2} + κ + O(|t|^{1/2}) with the real-t coefficients.

Two consequences for "Use":
- **No vanishing claim is needed.** Theorem 1 gives Ψ bounded near x > 0. With z = x + iy, the L-side has 1/t_L = xz/(2πy) = x²/(2πy) + ix/(2π), and the R-side has 1/t_R = 1/(2πy) with the prefactor z = x + iy. The y⁻¹ and y^{−1/2} coefficients must then cancel separately. The resulting constants cancel too: (i/2π)(x s_L − s_R/√35) = 0 given the y⁻¹ cancellation. So Ψ(x) = κ_L(−1/x) − (x/√35)Σκ_R(x).
- **The x-uniformity is per rational x**, which is all that is needed.

With this fix R1 is a complete standard argument (Cat A as written proof; Cat B only in the sense of being the textbook Euler–Maclaurin estimate).

**m1–m8.** Replace the exponent in §4(d); add the one-line lattice remark (§1 table) to Lemma 5; state the O(1/M) block-difference in Lemma 6; spell out r_χ(p) = 0 for inert p; in R2, use #{γ-orbits with |Q| ≤ n} = O(n) and the decay e^{−2πn₀s}; cite R1 in §0's "in particular" sentence; note ν = 0 ∉ F.

## 4. Independent numerics (Cat A, finite / high-precision computations)

All code is from scratch: characters, Gauss sums, ρ, R via digamma plus a Hurwitz-ζ asymptotic tail, Lambert series G and T, lattice enumeration of E_L and E_R, and the period integral with u_L, u_R built over all four regions. The only input taken from earlier reports is the (j,l) → ψ table of the Cusp-Part report (I1), and it is tested by the I1 check.

### 4.1 Step-3 split, all 8 characters (`check_split.py` → `check_split.txt`, mpmath at 36 digits)
- Check: |G_χ(−1/(20z)) − 2R_χ(z) − T_χ(z)| at z = 0.6+0.45i, 1+0.9i, 0.25+0.3i, −0.4+0.7i, 2+0.5i.
- Result: **≤ 2·10⁻³⁵ for the 7 nontrivial characters and ≤ 8·10⁻³⁴ for trivial χ, at every point.**
- Tail stability: changing the explicit cutoff from |X_M| = 30 to 40 moves R by ≤ 2·10⁻³⁴.
- For comparison, |T| is 0.07–3.0, so this is a 33-digit identity. The audited report had double precision for all 8 characters and 32 digits for 2.

### 4.2 Theorem 2 vs E_R from scratch (`check_thm2.py` → `check_thm2.txt`)
- **Lattice side.** E_R coefficients by direct enumeration of ν = A⁻¹m ∈ F = [e₁, γe₁) with phase e(−(7m₁ − 2m₂)/10), for 140Q ≤ 14 000 (Q ≤ 100).
- **Result.** The maximum deviation from (√35/140)Σ_χ w_χ Σ_{nk=N} b̂ǎ is **1.84·10⁻¹⁵** over all N ≤ 14 000. There are 627 nonzero coefficients, and |Im| ≤ 7·10⁻¹⁶ on both sides.
- **All 627 coefficients are recognised as A + Bφ with identical integers (A,B) on both sides**; the first few are −1, −φ⁻¹, φ, 1, … (that is −1, −0.618…, 1.618…, 1, …). No odd N carries a nonzero coefficient.
- **I1 check.** The lattice E_L coefficients (ν ∈ F ∩ (a+Z²), 20Q ≤ 2000) equal Σ w_χ(a∗b)(n), with deviation 0.

### 4.3 Theorem 1 (`check_thm1.py` → `check_thm1.txt`; Herglotz side at 36 digits)

| region | points | comparison | max \|diff\| |
|---|---|---|---|
| H | 1+0.6i, 0.5+0.4i, 2+i, 0.8+1.5i, 1.3+0.25i, −0.5+0.8i | from-scratch q-series E_L(−1/z) − (z/√35)E_R(z), 36 digits | **5.5·10⁻³⁵** |
| Re z > 0, off H | 1−0.3i, 2−i, 0.5−0.2i, 5−3i, √2 | from-scratch split-path period formula (I3), double | 2.5·10⁻¹⁶ |
| same, `growth.py` | 3−3i, 10−10i, 20−40i | period formula vs Herglotz (double) | 9.2·10⁻¹⁶ |
| rationals | 1, 1/3, 2, 3/5, 7/4, 5/2, 13/8, 11/7 | exact Bernoulli/κ value (34–36 digits) | **5.7·10⁻³⁵** |
| rationals | same | from-scratch period formula, double | 5.7·10⁻¹⁷ |

- **Caveat on the rational κ reference.** It is computed with `hp_check.psi_exact` from the audited folder, imported read-only with bytecode writing disabled. It is therefore **not independent code**. The from-scratch period formula gives the independent cross-check, at double precision.
- **The period formula on H.** My period-formula implementation reproduces the q-series on H to ~10⁻¹⁶ (e.g. z = 1+0.6i), so its off-H values really are the continuation.
- **Growth.** On S, |Ψ|/|z| = 0.053–0.0667 for |z| from 1.4 to 1010, approaching log ε/(2π√35) = 0.066660 (`growth.txt`). This is consistent with Lemma 8, which proves the weaker C(1+|z|)².

### 4.4 Lemmas (`check_lemmas.py` → `check_lemmas.txt`)
- The three finite-difference kernel identities: exact (sympy).
- Lemma 1: ≤ 5·10⁻²⁹.
- β is 140-periodic and Σ_{1}^{140}β = 0 for trivial χ: ~10⁻²⁹.
- Σρ_n/n = i·log ε/(70π): 15 digits.

## 5. Cat A / Cat B summary
- **Cat A (audited, correct with the fixes above):**
  - Lemmas 1, 2, 5, 6 and Props. 4 and 7, including the trivial character;
  - Lemma 3 with G1 and G2;
  - Lemma 8 and the Liouville/Cauchy step;
  - Theorems 1 and 2 *given (I1)–(I3)*;
  - R2 with m6.
- **Cat A with written fix:** R1, with G3 (a standard Euler–Maclaurin estimate).
- **Inputs not re-audited here:** (I1), (I2), (I3) from the 2026-10-17 reports. They are numerically consistent: the I1 coefficient check is exact, and the (I3) period formula agrees with the q-series on H and with Herglotz off H.
- **Cat B:** the class number formula used to interpret Σρ_n/n as log ε (context only; not used in the proof).
- **Not claimed:** any arithmetic (Gauss-sum) proof of Theorem 2; anything beyond these two theorems.

## 6. Files (`2026-10-18-ER-cancellation-audit/`)
- `common.py`: from-scratch characters, Gauss sums, ρ, β_k, φ, R (mpmath), G and T series, and lattice coefficients of E_L and E_R.
- `check_split.py` → `check_split.txt` (and `.log`): §4.1.
- `check_thm2.py` → `check_thm2.txt`: §4.2 and the I1 check.
- `period.py`: from-scratch u_L and u_R Fourier data (4 regions) and the split-path period formula (double precision).
- `check_thm1.py` → `check_thm1.txt` (and `.log`): §4.3.
- `growth.py` → `growth.txt` (and `.log`): growth on S, plus the period formula vs Herglotz at larger |z|.
- `check_lemmas.py` → `check_lemmas.txt`: §4.4.
