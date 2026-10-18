# The E_R cancellation, proved: the Herglotz closed form for ψ_Eis, and E_R in closed form

Date: 2026-10-18, 11:49 PM – about 12:30 AM CDT (America/Chicago). Work done on the box only. No Heavy, no Grok, no pushes, no emails. The repo was only read.

Folder: `2026-10-18-ER-cancellation/` (contents in §8).

Labels:
- **Cat A**: proved here, or a finite or high-precision computation with the check stated.
- **Cat B**: relies on a cited theorem not re-proved here, or is only a sketch.

This report makes no HQCC, TPC or RH claims. Residual ≠ Resonant. CORE_FREEZE holds.

## 0. Verdict

**Proved.** The Lambert-series leftover in the ψ_Eis derivation cancels exactly against (z/√35)E_R(z). Hence, for every z with Re z > 0:

  **Ψ(z) = E_L(−1/z) − (z/√35)E_R(z) = (1/8) Σ_{j∈{0,2,4,6}, l∈{0,1}} e(−j/8)·R_{j,l}(z),**
  **R_χ(z) = Σ_{m≥1} a_χ(m) Σ_{s=1}^{140} ρ_s^χ ψ_Γ(s/140 + m/(20z)).**

On H the left side is the q-series; on the rest of Re z > 0 it is its analytic continuation. In particular, ψ(x) = Ψ(x) for x > 0.

The proof also gives **E_R in closed form** (Theorem 2):

  **E_R(z) = (√35/140) Σ_χ w_χ Σ_{n,k≥1} b̂_χ(n)·ǎ_χ(k)·e(nkz/140),  w_χ = e(−j/8)/16,**

with Gauss sums b̂(n) = Σ_{r mod 140} b(r)e(rn/140) and ǎ(k) = Σ_{r mod 20} a(r)e(kr/20). This is the explicit Eisenstein decomposition of E_R, so of u_R as well: each genus piece E_{ψ,ψχ₁₄₀} is replaced by its "Fricke dual" Gauss-sum series at level 140. Numerically it matches the cone-sum coefficients of E_R for all N ≤ 5600 to 4.6·10⁻¹⁴, with the same result at two box sizes.

**Status of the proof.** Every step is written out in §§2–5, with each interchange justified. The new steps are:
- the Mittag-Leffler step;
- convergence and growth of R;
- a two-variable summation-by-parts lemma that justifies swapping the conditionally convergent double sum Σ_m Σ_n a(m)ρ_n/(nz+7m);
- the trivial-character case, which needs a second-order summation by parts because Σa ≠ 0;
- a Liouville argument for the 140-periodic difference.

The proof uses these inputs, all Cat A from earlier reports:

| input | source |
|---|---|
| (I1) genus decomposition E_L = Σ w_χ G_χ(·/20) | Cusp-Part §2, §5; local check recalled in §1 |
| (I2) Maass S-law u_L(−1/w) = u_R(w)/√35 | Conditions-Removed §2, Poisson summation |
| (I3) Green-form lemma (C = −π/2) and the Stokes formula giving Ψ's continuation to Re z > 0 | Conditions-Removed §1, psi-Cocycle A3 |

The Fourier–integral interchange R2 used in (I3) is now written out (§6.1). The sector-uniform Euler–Maclaurin R1 is not needed for the main theorem. It is needed only to identify ψ(x) with the exact Bernoulli/κ values, and §6.2 gives a written proof of it.

**What is not claimed:**
- No direct arithmetic (Gauss-sum or ideal-theoretic) proof of Theorem 2. It is derived analytically, by Liouville, from (I2)–(I3), and checked numerically.
- §6.2 (R1) is a standard estimate, written as a proof but less detailed than §§2–5.

## 1. Setup

**Characters and the two coefficient sequences.** For each of the 8 genus characters χ = χ_{j,l}:
- ψ = ψ_χ mod 20, as in the earlier table;
- a(m) = ψ(m)·1_{(m,10)=1}, with period 20 and a(0) = 0;
- b(k) = ψ(k)χ₁₄₀(k), with period 140 and b(0) = b(140) = 0;
- parities η_a = ψ(−1) and η_b = ψ(−1)χ₁₄₀(−1) = η_a, so **η_aη_b = 1**.

**Lambert data.**
- G_χ(τ) = Σ_{m,k≥1} a(m)b(k)e(mkτ).
- ρ_n = −b̂(n)/(2πi·140) is 140-periodic, with ρ₀ = 0, ρ_{−n} = η_bρ_n, and Σ_{s=1}^{140} ρ_s = −b(0)/(2πi) = 0.
- β(n) := Σ_{j=1}^n ρ_j (β(0) = 0) is therefore 140-periodic and bounded.
- φ(X) := Σ_{s=1}^{140} ρ_s ψ_Γ(s/140 + X), so R(z) = Σ_{m≥1} a(m)φ(m/(20z)).

**(I1), recalled.** E_L(τ) = Σ_χ w_χ G_χ(τ/20), with w_χ = χ̄(S₊)/16 = e(−j/8)/16.
- Region S₊ is one ray class mod 𝔭₂𝔭₅∞₁∞₂.
- σ(S₊) = S₋ and N∘σ = N, so the theta series of S₊ and S₋ coincide. Averaging them kills every χ with χ(d) = −1 and leaves the 8 genus characters.
- r_χ(n) = Σ_{N𝔞=n} χ(𝔞) = Σ_{d|n} a(d)b(n/d) is a local check:
  - split p: 2ψ(p);
  - inert p: ψ(p)²(1 − 1 + 1);
  - p = 7: χ(𝔭₇) = ψ(7);
  - multiplicativity.
- The region ↔ ideal bijection is elementary and was checked to norm 60 000. All of this is Cat A from the Cusp-Part report.

## 2. The split G_χ(−1/(20z)) = 2R_χ(z) + T_χ(z)  (Cat A)

**Lemma 1 (Mittag-Leffler).** Let B(u) := Σ_{k≥1} b(k)e(ku) for Im u > 0, and let B also denote its meromorphic continuation P(e(u))/(1 − e(140u)), where P(q) = Σ_{r=1}^{139} b(r)q^r. Then for every u ∉ (1/140)Z:

  B(u) = Σ_{n∈Z} ρ_n/(u − n/140), summed symmetrically, = Σ_{s=1}^{140} ρ_s π cot π(u − s/140).

The series Σ_{n≥1} ρ_n/(u ∓ n/140) converge separately.

*Proof.*
- B is 1-periodic, with simple poles at n/140 and residue P(e(n/140))/(−2πi·140) = ρ_n.
- B(u) → 0 as Im u → +∞. As Im u → −∞, B(u) → 0 because deg P ≤ 139.
- The cot sum has the same poles and residues, is 1-periodic, and tends to ∓iπΣρ_s = 0 as Im u → ±∞.
- The difference is entire, 1-periodic and bounded, hence constant (Liouville in e(u)), and that constant is 0.
- Grouping n by s mod 140 gives the cot form.
- The one-sided series converge by Abel summation: β is bounded, and n ↦ 1/(u − n/140) has finite total variation on [1, ∞). ∎

**Lemma 2.** For X ∉ (−∞, −1/140]:

  φ(X) = −140 Σ_{n≥1} ρ_n/(n + 140X).

*Proof.*
- Insert ψ_Γ(w) = −γ + Σ_{k≥0}[1/(k+1) − 1/(k+w)] into the finite s-sum.
- The constants cancel because Σρ_s = 0. What remains is −140 Σ_k Σ_{s=1}^{140} ρ_s/(140k + s + 140X).
- These are the 140-block partial sums of the series on the right, which converges by Lemma 1's Abel argument. ∎

**Lemma 3 (R is holomorphic on Re z > 0, with polynomial growth).** Two facts about φ:
- **Asymptotics.** Uniformly in Re X ≥ 0, φ(X) = β₁/X + O(|X|⁻²) as |X| → ∞, where β₁ = Σ_s ρ_s B₁(s/140). This follows from ψ_Γ(w+h) = log w + Σ_k (−1)^{k+1}B_k(h)/(k w^k) + O(|w|^{−K}), uniformly for |arg w| ≤ π − δ, together with Σρ_s = 0.
- **β₁ = 0 when η_b = +1.** Pair s with 140 − s.

Consequences:
- **Odd case (η_b = −1).** Then η_a = −1, so a has mean zero and its partial sums are bounded.
- **Holomorphy.** For z in a compact K ⊂ {Re z > 0}, X_m = m/(20z) lies in Re X > 0 with |X_m| ≍ m. So
  R(z) = Σ_m a(m)[φ(X_m) − 20zβ₁/m] + 20zβ₁·Σ_m a(m)/m.
  The first sum converges absolutely and uniformly on K. The second is a convergent Dirichlet series value (zero when η_b = +1). So R is holomorphic on Re z > 0.
- **Growth.** For 1 ≤ Re z ≤ 141 and Im z ≤ −1:
  - X_m lies in the closed first quadrant, and |φ(X)| ≤ C(1 + log(1+|X|)) because Re(s/140 + X) ≥ 1/140;
  - splitting at m = 20|z| gives |R(z)| ≤ C|z| log(2+|z|) + C|z| + C|z|²/(20|z|) = O(|z| log|z|). ∎

**Proposition 4.** For z ∈ H:

  G_χ(−1/(20z)) = 2R_χ(z) + T_χ(z),  where T_χ(z) := −lim_{M→∞} Σ_{0<|m|≤M} a(m)φ(m/(20z)),

and the limit exists.

*Proof.*
1. **Termwise expansion.** u_m := −m/(20z) lies in H, and G(−1/(20z)) = Σ_{m≥1} a(m)B(u_m), absolutely convergent. Since u_m − n/140 = −(7m + nz)/(140z), Lemma 1 gives
   B(u_m) = −140z[Σ_{n≥1} ρ_n/(7m + nz) + η_b Σ_{n≥1} ρ_n/(7m − nz)].
2. **Identify the two pieces.** By Lemma 2 these are φ(X_m) and −η_bφ(−X_m), with −X_m ∈ H.
3. **Sum over m.** The sum of a(m)φ(X_m) converges (Lemma 3), so Sing := −η_b Σ_{m≥1} a(m)φ(−X_m) converges as well, and G = R + Sing.
4. **Rewrite Sing − R.** Using η_a = η_b and a(−m) = η_a·a(m):
   Sing − R = −Σ_{m≥1}[a(m)φ(X_m) + a(−m)φ(X_{−m})] = T. ∎

**By (I1)**, E_L(−1/z) = Σ_χ w_χ(2R_χ + T_χ). Hence the theorem is equivalent to

  **(★) Σ_χ w_χ T_χ(z) = (z/√35) E_R(z) on H.**

## 3. T_χ as a Lambert series  (Cat A)

Write F(m,n) := 1/(nz + 7m), for z ∈ H, m ∈ Z, n ≥ 1. Then:
- |nz + 7m| ≥ n·Im z > 0;
- the values nz + 7m run over part of a lattice in C, so **Σ_{m∈Z, n≥1} |nz+7m|⁻³ < ∞**.

By Lemma 2, T(z) = 140z·lim_M Σ_{|m|≤M} a(m)g(m), where g(m) := Σ_{n≥1} ρ_n F(m,n). (The term m = 0 is absent when a(0) = 0.)

**Lemma 5 (two-variable summation by parts).** Suppose a(m) = α(m) − α(m−1) with α bounded, i.e. a has period 20 and mean zero. Then both iterated sums
- lim_M Σ_{|m|≤M} a(m) Σ_{n≥1} ρ_n F(m,n), and
- Σ_{n≥1} ρ_n·lim_M Σ_{|m|≤M} a(m)F(m,n)

exist and both equal the absolutely convergent sum Σ_{m,n} α(m)β(n)·Δ_mΔ_nF(m,n).

*Proof.*
- **Size of the differences.** Δ_nF = −z/(w(w+z)) with w = nz + 7m, and Δ_mΔ_nF = z(14w + 49 + 7z)/(w(w+z)(w+7)(w+7+z)) = O(|w|⁻³).
- **First order (n inside).**
  - Summing by parts in n (β(0) = 0, F(m,N) → 0) gives g(m) = −Σ_n β(n)Δ_nF(m,n), absolutely convergent.
  - |g(m)| ≤ C Σ_n |nz+7m|⁻² ≤ C′/|m| → 0.
  - Summing by parts in m over |m| ≤ M, the boundary terms α(M)g(M) and α(−M−1)g(−M) tend to 0.
  - The bulk is −Σ_m α(m)Δ_m g(m) = Σ_{m,n} α(m)β(n)Δ_mΔ_nF, which is absolutely convergent.
- **Second order (m inside).**
  - Summing by parts in m gives k(n) := Σ_m a(m)F(m,n) = −Σ_m α(m)Δ_mF, absolutely convergent.
  - |k(N)| ≤ C Σ_m |Nz+7m|⁻² ≤ C′/(N·Im z) → 0.
  - Summing by parts in n then gives the same absolutely convergent double sum. ∎

**Lemma 6 (inner m-sum).** If Σ_{r mod 20} a(r) = 0, then for n ≥ 1:

  Σ_m a(m)/(7m + nz) = −(2πi/140) Σ_{k≥1} ǎ(k) e(nkz/140),  summed symmetrically.

*Proof.* Group m by residue r mod 20. Each symmetric partial sum Σ_{|k|≤K} 1/(r + 20k + nz/7) tends to (π/20)cot(π(r + nz/7)/20); the divergent parts cancel because Σa = 0. Since Im(nz/7) > 0, expand cot πw = −i(1 + 2Σ_{k≥1} e(kw)) and sum over r. ∎

**Proposition 7. For every genus character χ and every z ∈ H:**

  **T_χ(z) = (z/140) Σ_{n,k≥1} b̂(n) ǎ(k) e(nkz/140).**

The right side converges absolutely.

*Proof, ψ nontrivial (7 characters; Σ_r a(r) = 0).*
- Apply Lemma 5 to swap the order.
- Apply Lemma 6 to the inner m-sum.
- Use 140z·(−2πiρ_n/140) = z·b̂(n)/140.

*Proof, ψ trivial* (a = 1_{(·,10)=1}, Σ_r a(r) = 8, b = χ₁₄₀ even). Here the n-outer iterated sum does **not** converge, so a second-order argument is needed.

1. **A second primitive.** b is even, so Σ_{n=1}^{140} β(n) = −Σ_j jρ_j = −70Σ_jρ_j = 0. Hence β(n) = γ(n) − γ(n−1) with γ bounded and periodic; choose γ(−1) = γ(0).
2. **The functional Λ.** Summing by parts twice gives, for f with f(N), Δf(N) → 0 and Σ|D²f| < ∞:
   Σ_{n≥1} ρ_n f(n) = Λ(f) := γ(0)(f(2) − f(1)) + Σ_{n≥1} γ(n) D²f(n),  with D²f(n) = f(n+2) − 2f(n+1) + f(n).
   Λ is defined whenever Σ|D²f| < ∞, and **Λ(constant) = 0**.
3. **Split a.** Write a = a* + 2/5 on m ≠ 0, where a* := a − 2/5 is 20-periodic with mean zero and a*(0) = −2/5.
4. **The a* part.** Lemma 5 applies on all of Z. Lemma 6 gives ǎ*(k) = ǎ(k) − 8·1_{20|k}. Removing the m = 0 term a*(0)g(0) = −(2/5)Σ_n ρ_n/(nz):
   Σ_{m≠0} a*(m)g(m) = −(2πi/140) Σ_{n,k} ρ_n ǎ*(k) q^{nk/140} + (2/5) Σ_n ρ_n/(nz).
5. **The constant part.**
   - g(m) = γ(0)ΔF(m,1) + Σ_n γ(n)D²_nF(m,n) = O(m⁻²), so Σ_{m≠0} g(m) converges absolutely.
   - |D²_nF| = O(|nz+7m|⁻³) is absolutely summable over (m ≠ 0, n), so Fubini gives Σ_{m≠0} g(m) = Λ(h), with h(n) := Σ_{m≠0} F(m,n) = (π/7)cot(πnz/7) − 1/(nz) (symmetric sum).
   - Write h = −πi/7 + h̃, with h̃(n) = −1/(nz) − (2πi/7) Σ_{j≥1} q^{nj/7}.
   - Λ(−πi/7) = 0, and h̃ decays, so Λ(h̃) = Σ_n ρ_n h̃(n).
   - Therefore (2/5)Σ_{m≠0} g(m) = −(2/5)Σ_n ρ_n/(nz) − (2/5)(2πi/7) Σ_{n,j} ρ_n q^{nj/7}.
6. **Combine.** The ±(2/5)Σρ_n/(nz) terms cancel; these are L(1, χ₁₄₀)-type constants, i.e. log ε. Since (2/5)(2πi/7) = (2πi/140)·8 = (2πi/140)·ǎ(20j), the remaining terms recombine into −(2πi/140) Σ_{n,k} ρ_n ǎ(k) q^{nk/140}. Multiplying by 140z gives the stated formula, with no extra terms. ∎

**Numerical check of Proposition 7** (`lemmaA.txt`, `lemmaA_hp.txt`):
- Each of the 8 characters separately, at 4 points z ∈ H: |G(−1/20z) − 2R − T| ≤ 7·10⁻¹⁴ in double precision (trivial χ: 3·10⁻¹¹, the Herglotz floor).
- At 34 digits for the trivial χ and for χ_{4,1}: ≤ 5·10⁻³².

## 4. The Liouville argument: (★) and Theorem 2  (Cat A, given I1–I3)

Set D(z) := Ψ(z) − 2Σ_χ w_χ R_χ(z).

**(a) Holomorphy.** By (I3), Ψ continues holomorphically to Re z > 0 through the period formula Ψ(z) = (z/(π√35))(∫_0^{i∞}[u_R, R_z^{1/2}] − log ε/2). By Lemma 3, R is holomorphic there too. So D is holomorphic on U := H ∪ {Re z > 0}.

**(b) Periodic structure on H.** By §2 and Proposition 7, D(z) = z·P(z) on H, where

  P(z) := Σ_{N≥1} p_N e(Nz/140),  p_N := (1/140) Σ_χ w_χ Σ_{nk=N} b̂(n)ǎ(k) − c_R(N/140)/√35.

E_R has only frequencies N/140, since Q(ν) = −N(θ)/140 for θ ∈ 𝔭₂ (dictionary in §5), and it has no constant term.

**(c) Extension to an entire function.**
- P = D/z is holomorphic on U.
- P(z+140) − P(z) is holomorphic on {Re z > 0} and vanishes on H ∩ {Re z > 0}, so it vanishes identically.
- Hence P extends to an entire 140-periodic function.
- As a function of q′ = e(z/140) it is holomorphic on C*, with Laurent series Σ_{N≥1} p_N q′^N by uniqueness, so it is entire in q′.

**(d) Growth (Lemma 8 below).** On S = {1 ≤ Re z ≤ 141, Im z ≤ −1}, |D(z)| ≤ C(1+|z|)². So |P(q′)| ≤ C(1 + log|q′|)² as |q′| → ∞, and Cauchy's estimates give p_N = 0 for all N ≥ 1.

**Hence P ≡ 0. This proves (★) (Theorem 2) and D ≡ 0 (Theorem 1).** ∎

**Lemma 8 (growth of the continued Ψ).** For z = x − iY with 1 ≤ x ≤ 141 and Y ≥ 1, |∫_0^{i∞}[u_R, R_z^{1/2}]| ≤ C(1+|z|).

*Proof.*
- **The kernel on the path w = it.** R_z = t/(t² + z²) = t/((z+it)(z−it)). Since Im(t² + z²) = −2xY < 0, Im R_z > 0 for all t > 0, so the principal branch of R^{1/2} is continuous. It is the continuation of the H-branch through R_z > 0 on the positive real axis.
- **Bounds.** |z+it| ≥ max(1, |t−Y|) and |z−it| ≥ t + Y. Hence |v| = |R|^{1/2} ≤ 1 and |v_w̄| = ¼|z−it|^{1/2} t^{−1/2} |z+it|^{−3/2} ≤ ¼(|z|+t)^{1/2} t^{−1/2}.
- **On (0,1].** u_R(it) = √35·u_L(i/t). u_L has no constant term (a ∉ Z²), so u_R and ∂_w u_R are O(t^{−A}e^{−c/t}). The contribution is O((1+|z|)^{1/2}).
- **On [1,∞), non-constant part.** It is O(e^{−ct}) with the same v-bounds, so its contribution is O((1+|z|)^{1/2}).
- **On [1,∞), constant term √t·log ε.** The integrand is exactly (log ε/2)·z(z+it)^{−3/2}(z−it)^{−1/2}·dt. Its integral is at most C|z|·Y^{−1/2}·∫ dt/max(1,|t−Y|)^{3/2} ≤ C′|z|.
- **Conclusion.** Together with the prefactor z/(π√35), this gives |Ψ(z)| ≤ C(1+|z|)². With Lemma 3, |D(z)| ≤ C(1+|z|)². ∎

**Numerical check of the continuation off H** (`lowerhalf.txt`). The split-path period formula and the Herglotz form agree to ≤ 2·10⁻¹² (the double-precision floor) at z = 1−0.3i, 0.7−0.6i, 2−i, 3−2.5i, 0.4−0.1i and 1.5+0.4i.

## 5. Theorem 2 in arithmetic form; verification against the data

**Dictionary (Cat A, elementary).** Put ν ∈ L′ = A⁻¹Z², (u, v) = Aν and θ := (7u − 2v) + u√35. Then:
- ν ↔ θ is a bijection L′ → 𝔭₂ = {A + B√35 : A ≡ B mod 2};
- Q(ν) = −N(θ)/140 and B(ν, a) = Re(θ)/10.

So c_R(N/140) = Σ_{θ ∈ 𝔭₂ ∩ cone, −Nθ = N} e(−Re θ/10). The phase is invariant under θ ↦ εθ precisely because θ ∈ 𝔭₂.

**Theorem 2 (coefficient form).**

  c_R(N/140) = (√35/140) Σ_χ w_χ Σ_{nk=N} b̂_χ(n)·ǎ_χ(k).

**Check** (`lemmaB.py` → `lemmaB_Q40.txt`, `lemmaB_run40b.log`):
- All N ≤ 5600 (Q ≤ 40, 267 nonzero coefficients): max deviation 4.6·10⁻¹⁴, identical at box sizes 300 and 400.
- Every coefficient is real; the right-hand side has imaginary parts ≤ 5·10⁻¹⁴. The values are in Z[(1+√5)/2], e.g. c(10/140) = −1, c(26/140) = −0.6180339887, c(34/140) = +1.6180339887.

In words: E_R is the combination, with the same weights w_χ and factor √35/140, of the Gauss-sum-dual Lambert series Σ b̂(n)ǎ(k)q^{nk/140} of the 8 genus Eisenstein pieces. These are the S-images, by Proposition 7, of the pieces G_χ(·/20) that make up E_L. This is the explicit Eisenstein decomposition of E_R. For u_R it follows from f_{u_R} = 2E_R together with real coefficients.

## 6. The remaining analytic conditions R1 and R2

### 6.1 R2: Fourier sum and Green-form integral commute (Cat A, written proof)

Claim: for z ∈ H and u = u_L or u_R, ∫_z^{z+i∞}[u, R_z^{1/2}] = Σ_n c_n F_n(z) + c₀/2.

On the ray w = z + is, write u = √y·c₀ + Σ_{n≠0} c_n T_n. Then:
- **Coefficients.** |c_n| ≤ C(1+|n|)², since there are O(n²) lattice points with |Q| ≤ n.
- **Fourier terms.** |T_n|, |∂_w T_n| ≤ C(1+|n|)·(y+s)^{1/2}·e^{−2π|n|(y+s)}(1 + (y+s)^{−1}), by K₀, K₁ ≤ C e^{−X}(1 + X^{−1/2}) for X ≥ X₀.
- **Kernel.** Along the ray, |v| ≤ C(s^{−1/2} + 1) and |v_w̄| ≤ C(1 + s)^{1/2}, uniformly for fixed z.
- **Dominating function.** Σ_{n≠0} |c_n|(|T_n| + |∂T_n|)(|v| + |v_w̄|) ≤ C e^{−2π(y+s)}(1+s)(1 + s^{−1/2}) Σ_n n³e^{−2π(|n|−1)y} = C_z e^{−2πs}(1+s)(1+s^{−1/2}), which is integrable on (0,∞).

Dominated convergence permits termwise integration. Each term is evaluated by the Green-form lemma (I3). The same bound, uniform for z in compact sets, also gives the holomorphy used in (I3). ∎

### 6.2 R1: sector-uniform Euler–Maclaurin (Cat A, standard estimate; written proof, less detailed)

Claim: for rational x, the cone sum f(e(x)e^{−t}) = Σ_{ν ∈ C∩(α+Z²)} e(B(ν,β))e(Q(ν)x)e^{−tQ(ν)} has the expansion s/t + h·t^{−1/2} + κ + O(|t|^{1/2}), uniformly for |arg t| ≤ π/2 − δ.

*Proof.*
1. **Reduce to finitely many sublattices.** Write ν = (r + Mk)V/M′ with k ∈ Z²_{≥0}, over finitely many residues r. The phase is constant on each class, because Q(ν)x mod 1 and B(ν,β) mod 1 are periodic mod MZ². C is a half-open simplicial cone with generators e₁, γe₁, and Q(e₁) = Q(γe₁) = 1. Half-open cones are closed cones minus a ray, and a ray is a 1-dimensional case of the same argument.
2. **Positivity on the cone.** Q is positive definite on the closed cone: Q(yV) ≥ c|y|² for y ∈ R²_{≥0}.
3. **Expand each sum.** Apply the 2-variable Euler–Maclaurin formula of order p to h(y) = e^{−tQ(yV)} on (r/M + R_{≥0})².
   - **Main terms.** They are ∫∫h = c₂/t, edge integrals c₁ t^{−1/2}, and corner terms polynomial in t. These are identities for t > 0 that continue analytically to Re t > 0.
   - **Remainders.** They are ∫ B̃·∂^p h. Here ∂^p h = Σ_j P_j(y)t^j e^{−tQ}, with deg P_j ≤ 2j − p, and |e^{−tQ}| ≤ e^{−c sin δ·|t||y|²}. Scaling y ↦ |t|^{−1/2}y bounds them by C_{p,δ}|t|^{(p−2)/2}, uniformly in the sector.
4. **Conclusion.** Taking p = 4 gives the expansion with an O(|t|) remainder, uniformly in the sector. The coefficients are the same as for real t, and the t^{±1/2} terms vanish as computed earlier. ∎

**Use.** With R1, the vertical approach z = x + iy → x, which maps to a curve approaching −1/x non-tangentially, gives Ψ(x) = κ_L(−1/x) − (x/√35)Σκ_R(x). So the Herglotz values at rationals equal the exact Bernoulli sums. Combined with Theorem 1, this is now a proof, not only the earlier 33-digit numerics.

**Citation.** Shintani, "On evaluation of zeta functions of totally real algebraic number fields at non-positive integers", J. Fac. Sci. Univ. Tokyo Sect. IA 23 (1976) 393–417, MR0427231. This is the cone-decomposition context; the bibliographic data were verified online this session. The proof above does not depend on it.

## 7. Cat A / Cat B

**Cat A (written proofs here):**
- Lemmas 1–3 and 5–6 and Lemma 8; Propositions 4 and 7, including the trivial character.
- The Liouville argument, giving Theorem 1 (Herglotz closed form on Re z > 0) and Theorem 2 (E_R closed form).
- R2.
- R1 (standard estimate, written in less detail).

**Cat A inputs from earlier reports:**
- (I1) genus decomposition of E_L;
- (I2) S-law;
- (I3) Green-form lemma and Stokes continuation formula.
- These in turn rest on hand proofs, plus the region ↔ ideal bijection, which is elementary and was checked to 60 000.

**Cat A numerics:**

| check | file | agreement |
|---|---|---|
| Proposition 7 per character | `lemmaA*.txt` | 34 digits for 2 characters; double precision for all 8 |
| Theorem 2 coefficients, N ≤ 5600 | `lemmaB*` | 4.6·10⁻¹⁴ |
| continuation off H | `lowerhalf.txt` | 2·10⁻¹² |
| earlier: 44 rationals | — | 5.7·10⁻³³ |

**Cat B / not done:**
- A purely arithmetic proof of Theorem 2, via Gauss sums over 𝔭₂ / ray classes, avoiding the analytic Liouville step.
- Simplifying b̂ and ǎ to primitive Gauss sums times characters. Several ψ′ and a are imprimitive, so this was left in finite-sum form.
- Lewis–Zagier interpretation (context only; arXiv:math/0101270, verified earlier).

**Remaining lemma:** none for Theorem 1. The proof is complete given (I1)–(I3).

No HQCC, TPC or RH claims.

## 8. Files (`2026-10-18-ER-cancellation/`)
- `lemmaA.py` → `lemmaA.txt`: Proposition 7, double precision, all 8 characters.
- `lemmaA_hp.py` → `lemmaA_hp.txt`: 34 digits, trivial χ and χ_{4,1}.
- `lemmaB.py` → `lemmaB_Q8.txt`, `lemmaB_Q40.txt`, `lemmaB_run40.log` (box 300), `lemmaB_run40b.log` (box 400): Theorem 2.
- `lowerhalf.py` → `lowerhalf.txt`: period formula vs Herglotz in Im z < 0.
- Helpers copied unchanged: `herglotz.py`, `hp_check.py`, `uvec.py`, `family.py`, `complex_check.py`, `fastkappa.py`. `lowerhalf.py` imports `../2026-10-17-psi-cocycle/psi_period.py` read-only.
