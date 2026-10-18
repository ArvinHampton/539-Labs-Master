# The E_R cancellation, proved (rev 2): the Herglotz closed form for ψ_Eis, and E_R in closed form

**Status: Cat A, audited once (pass with fixes, all fixes applied).**
- Audit: `2026-10-18-ER-Cancellation-Audit.md`.
- Inputs (I1)–(I3), listed in §0, are earlier Cat A results. The audit checked them numerically but did not re-audit them.

Date: 2026-10-18, rev 2 written about 3:31–3:40 AM CDT (America/Chicago). Rev 1 (`2026-10-18-ER-Cancellation-Proof.md`) is unchanged. Work done on the box only. No Heavy, no Grok, no pushes, no emails. The repo was only read.

Folder: `2026-10-18-ER-cancellation/` (rev-1 scripts, plus `em_check2.py` / `em_check_corrected.txt` new in rev 2).

Labels:
- **Cat A**: proved here, or a finite or high-precision computation with the check stated.
- **Cat B**: relies on a cited theorem not re-proved here, or is only a sketch.

This report makes no HQCC, TPC or RH claims. Residual ≠ Resonant. CORE_FREEZE holds.

## Changelog (rev 1 → rev 2)

| audit item | fix | where in rev 2 |
|---|---|---|
| **G1** R holomorphic only on Re z > 0 in rev 1 | Adopted the auditor's fix (a): Lemma 3 is extended to U = H ∪ {Re z > 0} (arg X_m = −arg z ∈ (−π, π/2)), so Prop. 4 holds on all of H. Fix (b), restricting to Re z > 0, would also suffice; §4 only uses Re z > 0. | Lemma 3(i), Prop. 4, §4(a)/(c) |
| **G2** odd-character tail | Abel summation: Σ_{m≥M₀} a(m)/m = O(1/M₀), hence R = O(1+\|z\|) on S | Lemma 3(iii) |
| **G3** R1 remainder bookkeeping | Full order-3 two-variable Euler–Maclaurin, with every remainder bounded. The "t^{±1/2} terms vanish" claim is removed; the cancellation argument is put in its place. **Deviation:** the auditor's 1D remainder sign (−1)^{p+1}B̃_p(u−y)/p! is wrong for odd p. The correct form is (−1)^{p+1}B̃_p(y−u)/p! = −B̃_p(u−y)/p!, verified to 10⁻³¹ for p = 1, 2, 3. Bounds use only \|B̃_p\|, so the argument is unaffected. | §6.2, `em_check2.py` |
| m1 | \|P\| ≤ C(1 + log\|q′\|), not squared | §4(d) |
| m2 | Uniformity of O(\|w\|⁻³) over the lattice | §3, preamble to Lemma 5 |
| m3 | R = O(1+\|z\|), not O(\|z\| log\|z\|) | Lemma 3(iii) |
| m4 | Symmetric m-limit vs per-residue limits differ by O(1/M) | Lemma 6 |
| m5 | Inert p: r_χ(p) = 0 and r_χ(p²) = ψ(p)² | §1 (I1) |
| m6 | R2: O(n) γ-orbits (not lattice points) with \|Q\| ≤ n; decay e^{−2πn₀(y+s)}, n₀ = min\|Q\| > 0 | §6.1 |
| m7 | ψ(x) = κ-value needs R1, stated explicitly | §0, §6.2 "Use" |
| m8 | ν = 0 ∉ F, so E_R has no constant term; frequencies lie in (2/140)Z, with a proof | §4(b), §5 |

## 0. Verdict

**Theorem 1 (Cat A, given I1–I3).** For every z with Re z > 0, and in fact on U = H ∪ {Re z > 0}:

  **Ψ(z) = E_L(−1/z) − (z/√35)E_R(z) = (1/8) Σ_{j∈{0,2,4,6}, l∈{0,1}} e(−j/8)·R_{j,l}(z),**
  **R_χ(z) = Σ_{m≥1} a_χ(m) Σ_{s=1}^{140} ρ_s^χ ψ_Γ(s/140 + m/(20z)).**

On H the left side is the q-series; on the rest of U it is the continuation from (I3).

**Corollary (Cat A, given I1–I3 and R1, §6.2).** For rational x > 0, Ψ(x) equals the exact Bernoulli/κ value ψ(x) = κ_L(−1/x) − (x/√35)Σκ_R(x). So the Herglotz form gives the exact Bernoulli values.

**Theorem 2 (Cat A, given I1–I3).**

  **E_R(z) = (√35/140) Σ_χ w_χ Σ_{n,k≥1} b̂_χ(n) ǎ_χ(k) e(nkz/140),  w_χ = e(−j/8)/16.**

This is the explicit Eisenstein decomposition of E_R.

**Inputs: earlier Cat A results, checked numerically by the audit but not re-audited.**

| input | content | source | audit's numerical check |
|---|---|---|---|
| (I1) | E_L = Σ_χ w_χ G_χ(·/20) | Cusp-Part §2, §5 | exact for 20Q ≤ 2000 |
| (I2) | Maass S-law u_L(−1/w) = u_R(w)/√35, by Poisson summation | Conditions-Removed §2 | — |
| (I3) | Green-form lemma (C = −π/2) and the Stokes/period formula continuing Ψ to Re z > 0 | Conditions-Removed §1; psi-Cocycle A3 | period formula matches the q-series on H and Herglotz off H to 10⁻¹⁶ |

**Not claimed:** an arithmetic (Gauss-sum or ideal-theoretic) proof of Theorem 2.

**Numerics.**

| check | rev 1 | audit (independent code) |
|---|---|---|
| split G = 2R + T, all 8 characters | 7·10⁻¹⁴ | ≤ 8·10⁻³⁴ |
| Theorem 2 | N ≤ 5600, 4.6·10⁻¹⁴ | N ≤ 14 000, 1.8·10⁻¹⁵, exact in Z[φ] |
| Theorem 1 on H | — | 5.5·10⁻³⁵ |
| Theorem 1 off H | 2·10⁻¹² | 9·10⁻¹⁶ |
| Theorem 1 at rationals | 5.7·10⁻³³ | 5.7·10⁻³⁵ |

## 1. Setup

**Characters and the two coefficient sequences.** For each of the 8 genus characters χ = χ_{j,l}:
- ψ mod 20, as in the Cusp-Part table;
- a(m) = ψ(m)·1_{(m,10)=1}, with period 20 and a(0) = 0;
- b(k) = ψ(k)χ₁₄₀(k), with period 140 and b(0) = b(140) = 0;
- parities η_a = ψ(−1) and η_b = ψ(−1)χ₁₄₀(−1) = η_a, so **η_aη_b = 1**. This holds because χ₁₄₀ is the character of the real field Q(√35), hence even.

**Lambert data.**
- G_χ(τ) = Σ_{m,k≥1} a(m)b(k)e(mkτ).
- ρ_n = −b̂(n)/(2πi·140) is 140-periodic, with ρ₀ = 0 (b̂(0) = 0 since ψχ₁₄₀ is nontrivial mod 140), ρ_{−n} = η_bρ_n, and Σ_{s=1}^{140} ρ_s = −b(0)/(2πi) = 0.
- β(n) := Σ_{j=1}^n ρ_j (β(0) = 0) is therefore 140-periodic and bounded.
- φ(X) := Σ_s ρ_s ψ_Γ(s/140 + X), so R(z) = Σ_{m≥1} a(m)φ(m/(20z)).

**(I1), recalled.** E_L(τ) = Σ_χ w_χ G_χ(τ/20), with w_χ = χ̄(S₊)/16 = e(−j/8)/16.
- S₊ is one ray class mod 𝔭₂𝔭₅∞₁∞₂.
- σ(S₊) = S₋ and N∘σ = N, so averaging the two equal theta series kills every χ with χ(d) = −1.
- r_χ(n) = Σ_{N𝔞=n} χ(𝔞) = Σ_{d|n} a(d)b(n/d) is a local check (m5):
  - split p: r_χ(p) = 2ψ(p);
  - inert p: r_χ(p) = 0 on both sides, since ψ(p)(1 + χ₁₄₀(p)) = 0, and r_χ(p²) = χ((p)) = ψ(p²) = ψ(p)²(1 − 1 + 1);
  - p = 7: χ(𝔭₇) = ψ(7);
  - multiplicativity.

## 2. The split G_χ(−1/(20z)) = 2R_χ(z) + T_χ(z)  (Cat A)

**Lemma 1 (Mittag-Leffler).** Let B(u) := Σ_{k≥1} b(k)e(ku) for Im u > 0, and let B also denote its meromorphic continuation P(e(u))/(1 − e(140u)), where P(q) = Σ_{r=1}^{139} b(r)q^r. Then for every u ∉ (1/140)Z:

  B(u) = Σ_n ρ_n/(u − n/140), summed symmetrically, = Σ_{s=1}^{140} ρ_s π cot π(u − s/140).

The one-sided series Σ_{n≥1} ρ_n/(u ∓ n/140) converge separately.

*Proof.*
- B is 1-periodic, with simple poles at n/140 and residue P(e(n/140))/(−2πi·140) = ρ_n.
- B → 0 at ±i∞: at −i∞ because deg P ≤ 139.
- The cot sum has the same poles and residues and tends to ∓iπΣρ_s = 0.
- The difference is entire, periodic and bounded, hence 0 by Liouville in e(u).
- The one-sided series converge by Abel summation: β is bounded, and n ↦ 1/(u − n/140) has finite total variation. ∎

**Lemma 2.** For X ∉ (−∞, −1/140]: φ(X) = −140 Σ_{n≥1} ρ_n/(n + 140X).

*Proof.* Insert ψ_Γ(w) = −γ + Σ_{k≥0}[1/(k+1) − 1/(k+w)]. The constants cancel by Σρ_s = 0, and the result is the 140-block partial sums of the convergent series. ∎

**Lemma 3 (R on U; growth on S).** Let β₁ := Σ_s ρ_s B₁(s/140). Then β₁ = 0 when η_b = +1 (pair s with 140 − s). When η_b = −1, also η_a = −1, so a is odd with mean zero and A(N) := Σ_{m≤N} a(m) is bounded.

*Uniform asymptotics.* For every δ > 0, uniformly in |arg X| ≤ π − δ:

  φ(X) = β₁/X + E(X),  |E(X)| ≤ C_δ|X|⁻² for |X| ≥ 1.

This follows from ψ_Γ(w+h) = log w + Σ_{k=1}^{K} (−1)^{k+1}B_k(h)/(k w^k) + O_δ(|w|^{−K−1}) and Σρ_s = 0. For 1 ≤ |X| ≤ X₀, both φ and β₁/X are bounded away from the poles.

**(i) Holomorphy on U (G1).**
- For z ∈ U = H ∪ {Re z > 0}, arg z ∈ (−π/2, π), so arg X_m = −arg z ∈ (−π, π/2). Hence X_m never lies on (−∞, 0], where the poles −s/140 − k of φ are.
- On a compact K ⊂ U: |arg X_m| ≤ π − δ_K and |X_m| = m/(20|z|) ≍_K m.
- So R(z) = Σ_m a(m)[φ(X_m) − 20zβ₁/m] + 20zβ₁·L(1, a). The first sum converges absolutely and uniformly on K, since its terms are O_K(m⁻²). The second term is absent when η_b = +1, and is a convergent Dirichlet series value times z when η_b = −1.
- Hence **R is holomorphic on U**.

**(ii)** The same estimates hold on −U (for −X_m ∈ H) and give convergence of the Sing series in Prop. 4.

**(iii) Growth on S = {1 ≤ Re z ≤ 141, Im z ≤ −1} (G2, m3).** Here X_m lies in the closed first quadrant. Let M₀ := ⌈20|z|⌉, so |X_m| ≥ 1 for m ≥ M₀. Split

  R = Σ_{m<M₀} a(m)φ(X_m) + 20zβ₁ Σ_{m≥M₀} a(m)/m + Σ_{m≥M₀} a(m)E(X_m).

- **First sum: O(|z|).** For |X| ≤ 1 in the first quadrant, Re(s/140 + X) ≥ 1/140, so |φ| ≤ C.
- **Second sum: O(1).** It is nonzero only if η_b = −1. By Abel summation, Σ_{m≥M₀} a(m)/m = −A(M₀−1)/M₀ + Σ_{m≥M₀} A(m)/(m(m+1)) = O(1/M₀) = O(1/|z|).
- **Third sum: O(|z|).** It is ≤ C Σ_{m≥M₀} (20|z|/m)² = O(|z|²/M₀).

**Hence |R(z)| ≤ C(1 + |z|) on S.** The audit observed numerically that max_χ|R_χ|/|z| ≈ 0.50–0.53 for 1.4 ≤ |z| ≤ 1010. ∎

**Proposition 4.** For z ∈ H, with the limit existing:

  G_χ(−1/(20z)) = 2R_χ(z) + T_χ(z),  T_χ(z) := −lim_M Σ_{0<|m|≤M} a(m)φ(m/(20z)).

*Proof.*
1. u_m := −m/(20z) lies in H. G(−1/(20z)) = Σ_{m≥1} a(m)B(u_m) converges absolutely, and u_m − n/140 = −(7m + nz)/(140z).
2. By Lemmas 1 and 2, B(u_m) = φ(X_m) − η_bφ(−X_m).
3. R converges by Lemma 3(i) (z ∈ H ⊂ U), so Sing := −η_b Σ_{m≥1} a(m)φ(−X_m) converges as well, and G = R + Sing.
4. Since η_a = η_b and a(−m) = η_a·a(m), Sing − R = T. ∎

By (I1), E_L(−1/z) = Σ_χ w_χ(2R_χ + T_χ). Hence Theorem 1 is equivalent to

  **(★) Σ_χ w_χ T_χ(z) = (z/√35)E_R(z) on H.**

## 3. T_χ as a Lambert series  (Cat A)

Write F(m,n) := 1/(nz + 7m), for z ∈ H, m ∈ Z, n ≥ 1, and w := nz + 7m.

**Uniform kernel bounds (m2).** The kernel identities (checked symbolically by the audit) are:
- Δ_nF = −z/(w(w+z));
- Δ_mΔ_nF = z(14w + 49 + 7z)/(w(w+z)(w+7)(w+7+z));
- D²_nF = 2z²/(w(w+z)(w+2z)).

Each shifted point w + c, with c ∈ {z, 7, 7+z, 2z}, is again of the form n′z + 7m′ with n′ ≥ 1. So |w + c| ≥ max(Im z, |w| − |c|) ≥ c_z|w|, with c_z > 0 depending only on z. Hence |Δ_mΔ_nF|, |D²_nF| ≤ C_z|w|⁻³ uniformly. Moreover Σ_{m∈Z, n≥1} |nz+7m|⁻³ < ∞, because the values nz + 7m lie in a lattice of C (z ∉ R).

By Lemma 2, T(z) = 140z·lim_M Σ_{|m|≤M} a(m)g(m), where g(m) := Σ_{n≥1} ρ_n F(m,n).

**Lemma 5 (two-variable summation by parts).** Suppose a(m) = α(m) − α(m−1) with α bounded (a 20-periodic with mean zero). Then both iterated sums
- lim_M Σ_{|m|≤M} a(m) Σ_n ρ_n F(m,n), and
- Σ_n ρ_n·lim_M Σ_{|m|≤M} a(m)F(m,n)

exist and equal the absolutely convergent Σ_{m,n} α(m)β(n)Δ_mΔ_nF.

*Proof.*
- **n inside.** Summing by parts in n gives g(m) = −Σ_n β(n)Δ_nF, absolutely convergent, with g(m) = O(1/|m|). Summing by parts in m, the boundary terms α(M)g(M) and α(−M−1)g(−M) tend to 0, and the bulk is the double sum.
- **m inside.** k(n) := Σ_m a(m)F(m,n) = −Σ_m α(m)Δ_mF, with k(N) = O(1/(N·Im z)). Summing by parts in n gives the same double sum. ∎

**Lemma 6 (inner m-sum).** If Σ_{r mod 20} a(r) = 0, then for n ≥ 1:

  lim_M Σ_{|m|≤M} a(m)/(7m + nz) = −(2πi/140) Σ_{k≥1} ǎ(k) e(nkz/140).

*Proof.*
- Take M = 20K + 19 and group m by r ∈ {0, …, 19}. Each residue class contributes Σ_{k=−K−1}^{K} 1/(r + 20k + nz/7) up to one end term.
- (m4) The symmetric limit over |m| ≤ M and the per-residue symmetric limits differ by O(1/M): only O(1) terms of size O(1/M) at the two ends are regrouped. The general M ≠ 20K + 19 differs by O(1/M) as well.
- Each per-residue symmetric sum tends to (π/20)cot(π(r + nz/7)/20). The divergent parts cancel because Σa = 0.
- Since Im(nz/7) > 0, expand cot πw = −i(1 + 2Σ_{k≥1} e(kw)). ∎

**Proposition 7.** For every genus character χ and z ∈ H:

  **T_χ(z) = (z/140) Σ_{n,k≥1} b̂(n) ǎ(k) e(nkz/140),**

absolutely convergent.

*Nontrivial ψ (Σa = 0).* Apply Lemma 5, then Lemma 6, and use 140z·(−2πiρ_n/140) = z·b̂(n)/140.

*Trivial ψ* (a = 1_{(·,10)=1}, Σa = 8, b = χ₁₄₀ even). Here the n-outer iterated sum diverges: k(n) → −(2/5)πi/7 ≠ 0 while β does not tend to 0. So a second-order argument is needed.

1. **A second primitive.** b is even, so Σ_{n=1}^{140} β(n) = −Σjρ_j = −70Σρ_j = 0. Hence β = γ(n) − γ(n−1) with γ bounded and periodic; take γ(−1) = γ(0).
2. **The functional Λ.** For f with f(N), Δf(N) → 0 and Σ|D²f| < ∞:
   Σ_{n≥1} ρ_n f(n) = Λ(f) := γ(0)(f(2) − f(1)) + Σ_{n≥1} γ(n)D²f(n).
   Λ is defined whenever Σ|D²f| < ∞, and Λ(const) = 0.
3. **Split a.** a = a* + 2/5 on m ≠ 0, where a* := a − 2/5 has mean zero and a*(0) = −2/5.
4. **The a* part.** Lemma 5 on Z, plus Lemma 6 with ǎ*(k) = ǎ(k) − 8·1_{20|k}, minus the m = 0 term:
   Σ_{m≠0} a*(m)g(m) = −(2πi/140) Σ_{n,k} ρ_n ǎ*(k)q^{nk/140} + (2/5) Σ_n ρ_n/(nz).
5. **The constant part.**
   - g(m) = γ(0)ΔF(m,1) + Σ_n γ(n)D²_nF(m,n) = O(m⁻²).
   - By the uniform bound and Fubini, Σ_{m≠0} g(m) = Λ(h), with h(n) = Σ_{m≠0} F(m,n) = (π/7)cot(πnz/7) − 1/(nz) = −πi/7 + h̃(n), where h̃(n) = −1/(nz) − (2πi/7)Σ_{j≥1} q^{nj/7}.
   - Λ(−πi/7) = 0, and Λ(h̃) = Σρ_n h̃(n).
6. **Combine.** The ±(2/5)Σρ_n/(nz) terms cancel. This constant is genuinely nonzero: the audit found Σρ_n/n = i·log ε/(70π) to 15 digits, which is Cat B context via the class number formula and is not used. Since (2/5)(2πi/7) = (2πi/140)·8, the remainder recombines into the stated formula. ∎

**Numerical check.**
- Rev 1: `lemmaA.txt`, `lemmaA_hp.txt`, ≤ 5·10⁻³² at 34 digits for 2 characters.
- Audit: all 8 characters at 5 points, including Re z < 0, to ≤ 8·10⁻³⁴.

## 4. The Liouville argument  (Cat A, given I1–I3)

Set D(z) := Ψ(z) − 2Σ_χ w_χ R_χ(z).

**(a) Holomorphy.** By (I3), Ψ continues holomorphically from H to Re z > 0 via Ψ(z) = (z/(π√35))(∫_0^{i∞}[u_R, R_z^{1/2}] − log ε/2). By Lemma 3(i), R is holomorphic on U. So D is holomorphic on U. Only Re z > 0 is needed below (G1(b) would suffice).

**(b) Periodic structure on H.** By Prop. 4 and Prop. 7, D(z) = z·P(z) on H, where

  P(z) = Σ_{N≥1} p_N e(Nz/140),  p_N = (1/140)Σ_χ w_χ Σ_{nk=N} b̂ǎ − c_R(N/140)/√35.

(m8) E_R has no constant term because ν = 0 ∉ F (F is the half-open cone [e₁, γe₁) without its vertex). Its frequencies are N/140 with N even (§5).

**(c) Extension.**
- P = D/z is holomorphic on {Re z > 0} and equals the Fourier series on H ∩ {Re z > 0}.
- P(z+140) − P(z) is holomorphic on Re z > 0 and vanishes on the open subset H ∩ {Re z > 0}, so it vanishes identically.
- Extend P to C by periodicity. The result is entire, and as a function of q′ = e(z/140) it is holomorphic on C*.
- By uniqueness of Laurent coefficients on C*, P = Σ_{N≥1} p_N q′^N there. So P is entire in q′ with P(0) = 0.

**(d) Growth (m1).**
- S has width one period, so its image under z ↦ q′ is {|q′| ≥ e^{2π/140}}.
- On S, |z| ≤ 141 + |Im z| = O(1 + log|q′|).
- Lemma 8 and Lemma 3(iii) give |D(z)| ≤ C(1+|z|)², hence **|P| ≤ |D|/|z| ≤ C(1+|z|) ≤ C′(1 + log|q′|)**.
- Cauchy's estimates on |q′| = r → ∞ then give p_N = 0 for all N ≥ 1.
- Periodicity plus "no constant term" alone would not suffice (e(z/140) is a counterexample). The o(|q′|) growth is what forces P = 0.

**Hence P ≡ 0. This proves (★) (Theorem 2) and D ≡ 0 on U (Theorem 1).** ∎

**Lemma 8 (growth of the continued Ψ).** For z = x − iY with 1 ≤ x ≤ 141 and Y ≥ 1, |∫_0^{i∞}[u_R, R_z^{1/2}]| ≤ C(1+|z|), so |Ψ(z)| ≤ C(1+|z|)².

*Proof.*
- **The kernel.** On w = it, R_z = t/((z+it)(z−it)). Im(t² + z²) = −2xY < 0, so Im R_z > 0 and the principal branch is the continuous continuation of the H-branch.
- **Bounds.** |z+it| ≥ max(1, |t−Y|) and |z−it| ≥ t + Y. Hence |v| ≤ 1 and |v_w̄| = ¼|z−it|^{1/2} t^{−1/2} |z+it|^{−3/2} ≤ ¼(|z|+t)^{1/2} t^{−1/2}.
- **On (0,1].** u_R(it) = √35·u_L(i/t), and u_L has no constant term, so u_R and ∂u_R are O(t^{−A}e^{−c/t}). The contribution is O((1+|z|)^{1/2}).
- **On [1,∞), non-constant part.** It is O(e^{−ct}), so the contribution is O((1+|z|)^{1/2}).
- **On [1,∞), constant term √t·log ε.** The integrand is exactly (log ε/2)·z(z+it)^{−3/2}(z−it)^{−1/2}·dt, so the contribution is ≤ C|z|Y^{−1/2}∫dt/max(1,|t−Y|)^{3/2} ≤ C′|z|. ∎

The audit observed numerically that the growth is in fact linear: |Ψ|/|z| → log ε/(2π√35) ≈ 0.06666 on S. This is not proved and not needed.

## 5. Theorem 2 in arithmetic form

**Dictionary (Cat A).** Put ν ∈ L′ = A⁻¹Z², (u, v) = Aν and θ = (7u − 2v) + u√35. Then:
- ν ↔ θ is a bijection L′ → 𝔭₂ = {A + B√35 : A ≡ B mod 2};
- Q(ν) = −N(θ)/140 and B(ν, a) = Re θ/10;
- the phase e(−Re θ/10) is ε-invariant exactly because A ≡ B mod 2.

**(m8) Frequencies.** N(θ) = A² − 35B² ≡ A² − B² ≡ 0 mod 2 for A ≡ B mod 2. So all frequencies lie in (2/140)Z = (1/70)Z.

**Coefficient form.** c_R(N/140) = (√35/140) Σ_χ w_χ Σ_{nk=N} b̂(n)ǎ(k).
- Rev 1: N ≤ 5600, 4.6·10⁻¹⁴.
- Audit: N ≤ 14 000, 1.8·10⁻¹⁵, all 627 nonzero coefficients identical as A + Bφ ∈ Z[φ].

## 6. The analytic conditions R2 and R1

### 6.1 R2: Fourier sum and Green-form integral commute (Cat A)

Claim: for z ∈ H and u = u_L or u_R, ∫_z^{z+i∞}[u, R_z^{1/2}] = Σ_n c_n F_n(z) + c₀/2.

On the ray w = z + is (s > 0), write u = √y·c₀ + Σ_{Q≠0} c_Q T_Q, where T_Q = √y K₀(2π|Q|y)e(Qx). Then:
- **(m6) Frequencies.** The frequencies Q are not integers. They lie in (1/g)Z with |Q| ≥ n₀ > 0 (n₀ = min|Q|, e.g. 4/140 for u_R and 0.35 for u_L).
- **(m6) Coefficients.** c_Q is a finite sum over γ-orbits of lattice vectors of norm Q. The number of γ-orbits with |Q| ≤ X is O(X), since each orbit meets the fundamental cone, where |Q| ≍ |ν|². So Σ_{|Q|≤X} |c_Q| = O(X).
- **Fourier terms.** For X = 2π|Q|(y+s) ≥ 2πn₀ Im z: |T_Q|, |∂_w T_Q| ≤ C_z(1+|Q|)(y+s)^{1/2}(1+(y+s)⁻¹)e^{−2π|Q|(y+s)}.
- **Kernel.** Along the ray, |v| ≤ C_z(1 + s^{−1/2}) and |v_w̄| ≤ C_z(1+s)^{1/2}.
- **Dominating function.** Σ_Q |c_Q|(|T_Q| + |∂T_Q|)(|v| + |v_w̄|) ≤ C_z (1+s)(1 + s^{−1/2}) e^{−2πn₀ s} Σ_Q |c_Q|(1+|Q|)e^{−2π(|Q|−n₀)y}. The Q-sum is finite by the O(X) count. The result is integrable on (0,∞).

Dominated convergence gives termwise integration. Each term is evaluated by the Green-form lemma (I3). The same bounds, uniform on compacta, give the holomorphy used in (I3). ∎

### 6.2 R1: sector-uniform Euler–Maclaurin, with all remainders (Cat A, written proof; G3)

**Claim.** Fix rational x, a cone sum f, and δ ∈ (0, π/2). Then uniformly for |arg t| ≤ π/2 − δ, |t| ≤ 1:

  f(e(x)e^{−t}) = s/t + h·t^{−1/2} + κ + O(|t|^{1/2}),

with the same coefficients s, h, κ as for real t.

**Reduction.**
- Write the half-open cone [e₁, γe₁) as {y₁v₁ + y₂v₂ : y₁ > 0, y₂ ≥ 0}, with v₁ = e₁ and v₂ = γe₁ (or the analogous description), and pass to a common denominator M′.
- Q(ν)x mod 1 and B(ν, β) mod 1 are periodic in ν mod MZ² for suitable M. Splitting into finitely many residue classes, each class has constant phase and is of the form

  Σ_{k∈Z²_{≥0}} g(u + k),  u ∈ [0,1]²,

  where g(y) := e^{−t q(y)} and q(y) := Q((y₁v₁ + y₂v₂)M/M′) is a positive definite quadratic form on R²_{≥0}: q(y) ≥ c|y|². (Q(v₁) = Q(v₂) = 1 > 0 and Q > 0 on the closed cone.)
- The excluded edge or vertex corresponds to u_i = 0 boundary conventions. A ray sum is the 1-dimensional case of the same argument.
- **Homogeneity.** With G := e^{−q}, g(y) = G(√t·y) (principal root), so ∂^α g(y) = t^{|α|/2}(∂^α G)(√t·y). Here ∂^α G = P_α·G, where P_α is a polynomial whose degrees d ≡ |α| mod 2 range over 0 ≤ d ≤ |α|. Since Re t ≥ sin δ·|t|:

  (★★) |∂^α g(y)| ≤ C_α Σ_{d≤|α|} |t|^{(|α|+d)/2} |y|^d e^{−c sin δ·|t||y|²}.

**1D Euler–Maclaurin formula (corrected sign; see changelog).** For u ∈ [0,1], p ≥ 1, and f with f^{(j)} integrable and decaying:

  Σ_{k≥0} f(k+u) = ∫_0^∞ f − Σ_{j=1}^p (B_j(u)/j!) f^{(j−1)}(0) + ((−1)^{p+1}/p!) ∫_0^∞ B̃_p(y−u) f^{(p)}(y) dy.

This was verified for p = 1, 2, 3, u ∈ {0, 0.37, 1} and complex t, to 10⁻³¹ (`em_check2.py` → `em_check_corrected.txt`). The audit's version with B̃_p(u−y) fails for odd p (`em_check_auditor_sign.txt`).

**Iteration with p = 3.** First apply the formula in y₂, for each fixed k₁ (with y₁ = u₁ + k₁). Then sum over k₁ and apply it in y₁. This produces the following terms:

| term | value | size |
|---|---|---|
| (A) ∫∫ g | t⁻¹∫∫G | gives s/t (analytic continuation from t > 0) |
| (B) edge terms −(B_j(u₂)/j!)∫_0^∞ ∂₂^{j−1}g(y₁,0)dy₁ and −(B_i(u₁)/i!)∫_0^∞ ∂₁^{i−1}g(0,y₂)dy₂, i, j ≤ 3 | c·t^{(j−2)/2} | j = 1 gives t^{−1/2} (h); j = 2 gives t⁰ (part of κ); j = 3 gives O(\|t\|^{1/2}) |
| (C) corner terms (B_i(u₁)B_j(u₂)/(i!j!))∂₁^{i−1}∂₂^{j−1}g(0) | t^{(i+j−2)/2}∂^αG(0) | zero for odd i+j (G even); only i = j = 1 gives t⁰ (part of κ); the rest are O(\|t\|) |
| (R1) 2D remainder from the y₁-step on ∫g dy₂: ∫∫ B̃₃ ∂₁³g | by (★★) and scaling y ↦ \|t\|^{−1/2}y: C Σ_d \|t\|^{(3+d)/2}\|t\|^{−(d+2)/2} | **O(\|t\|^{1/2})** |
| (R2) edge remainders ∫_0^∞ B̃₃·∂₁³∂₂^{j−1}g(y₁,0)dy₁ (and the mirror case) | 1D scaling: C Σ_d \|t\|^{(3+j−1+d)/2}\|t\|^{−(d+1)/2} = C\|t\|^{(j+1)/2} | **O(\|t\|)** |
| (R3) inner remainders Σ_{k₁} ∫_0^∞ B̃₃·∂₂³g(u₁+k₁, y₂)dy₂, see below | C(\|t\|^{1/2} + \|t\|) | **O(\|t\|^{1/2})** |

**Bound for (R3).**
- For fixed y₂ and each d, the majorant m_d(y₁) := |y|^d e^{−c′|t||y|²} is unimodal in y₁ ≥ 0. So Σ_{k₁≥0} m_d(u₁+k₁) ≤ ∫_0^∞ m_d dy₁ + 2·sup_{y₁} m_d.
- Integrating over y₂ and using (★★) with |α| = 3:
  |R3| ≤ C Σ_d |t|^{(3+d)/2}[|t|^{−(d+2)/2} + |t|^{−(d+1)/2}] = C(|t|^{1/2} + |t|).

All constants depend only on δ, q and the class. So every remainder is O(|t|^{1/2}) uniformly in the sector. The t^{−1}, t^{−1/2} and t⁰ coefficients are the same analytic expressions as for real t. ∎

**Use (m7; the rev-1 "t^{±1/2} terms vanish" claim is removed).** Take z = x + iy with y ↓ 0.
- **Right side.** E_R(z) = f_R(e(x)e^{−t_R}) with t_R = 2πy.
- **Left side.** −1/z = −1/x + iy/(xz), so E_L(−1/z) = f_L(e(−1/x)e^{−t_L}) with t_L = 2πy/(xz). Since arg t_L = −arg z → 0, t_L stays in the sector.
- **Expand.**
  - 1/t_L = x²/(2πy) + ix/(2π);
  - t_L^{−1/2} = x(2πy)^{−1/2}(1 + iy/x)^{1/2} = x(2πy)^{−1/2} + O(y^{1/2}).
- **Collect terms in Ψ = f_L − ((x+iy)/√35)f_R.**
  - y⁻¹: (x² s_L − x s_R/√35)/(2π);
  - y^{−1/2}: x(h_L − h_R/√35)/√(2π);
  - y⁰: κ_L − (x/√35)κ_R + (i/2π)(x s_L − s_R/√35);
  - everything else is o(1).
- **Conclude.** By Theorem 1, Ψ is continuous at x, so the y⁻¹ and y^{−1/2} coefficients vanish. The y⁻¹ cancellation gives x s_L = s_R/√35, which kills the extra constant. Hence

  **Ψ(x) = κ_L(−1/x) − (x/√35)Σκ_R(x),**

  the exact Bernoulli value. This is the Corollary in §0. It needs R1 and holds for each rational x separately, which is all that is needed.

**Citation (context only, verified bibliographically).** Shintani, J. Fac. Sci. Univ. Tokyo Sect. IA 23 (1976) 393–417, MR0427231.

## 7. Cat A / Cat B

**Cat A (written proofs here, audited once, fixes applied):**
- Lemmas 1–3 (with G1, G2), 5, 6 and 8.
- Propositions 4 and 7, including the trivial character.
- The Liouville step, giving Theorems 1 and 2 (given I1–I3).
- R2 (with m6).
- R1 (with G3, corrected sign), and the Corollary (given R1).

**Earlier Cat A inputs:** (I1), (I2), (I3), from the 2026-10-17 reports. The audit checked them numerically but did not re-audit their proofs.

**Cat B:**
- The class number interpretation Σρ_n/n = i·log ε/(70π). Context only; not used.
- Lewis–Zagier context.

**Not done:**
- An arithmetic proof of Theorem 2.
- Simplifying the imprimitive Gauss sums.

No HQCC, TPC or RH claims.

## 8. Files
- Rev 1 folder `2026-10-18-ER-cancellation/` (unchanged files):
  - `lemmaA*.py/txt`, `lemmaB*.py/txt/log`, `lowerhalf.py/txt`;
  - helpers.
- New in rev 2:
  - `em_check2.py` → `em_check_corrected.txt`: the corrected EM remainder sign, verified;
  - `em_check.py` → `em_check_auditor_sign.txt`: shows the audit's sign failing for odd p.
- Audit: `2026-10-18-ER-Cancellation-Audit.md` and `2026-10-18-ER-cancellation-audit/`, read only.
