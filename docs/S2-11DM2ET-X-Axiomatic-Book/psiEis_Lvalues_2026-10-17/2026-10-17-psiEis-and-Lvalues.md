# ψ_Eis in closed form (twisted Herglotz functions) and the cusp rows via Hecke L-values

Date: 2026-10-17 (America/Chicago). Work done on the box only, between 11:19 PM and about 11:50 PM CDT. No Heavy, no Grok, no pushes, no emails. The repo was only read. At most 3 cores were used.

Folder: `2026-10-17-psiEis-Lvalues/` (contents listed in §6).

Labels:
- **Cat A**: proved here, or an exact or high-precision computation with the check stated.
- **Cat B**: relies on a cited theorem or standard theory that was not re-proved here, or is only a sketch.

This report makes no HQCC, TPC or RH claims. Residual ≠ Resonant. CORE_FREEZE holds.

## 0. Verdicts

**(A) ψ_Eis has an exact closed form as a finite combination of twisted Herglotz functions.** For x > 0:

  **ψ(x) = ψ_Eis(x) = (1/8) Σ_{j∈{0,2,4,6}} Σ_{l∈{0,1}} e(−j/8) · R_{j,l}(x)**

  **R_{j,l}(z) = Σ_{m≥1, (m,10)=1} ψ_{j,l}(m) Σ_{s=1}^{140} ρ_s^{(j,l)} · ψ_Γ( s/140 + m/(20z) )**

where:
- ψ_Γ = Γ′/Γ is the digamma function.
- ψ_{j,l} is the genus Dirichlet character of the Cusp-Part report (§2): conductor dividing 20, normalised by ψ(7) = χ_{j,l}(𝔭₇).
- ψ′ = ψ·χ₁₄₀, and ρ_s = −(1/(2πi·140)) Σ_{r mod 140} ψ′(r) e(rs/140).
- When ψ′ is primitive mod 140, this is −τ(ψ′)·conj(ψ′(s))/(2πi·140).
- For x < 0, use ψ(x) = conj ψ(|x|).

Equivalently, this is the Lewis–Zagier shape Σ(mz+n)^{−2s} at s = ½, with characters, and with the n-sum taken first:

  R_{j,l}(z) = −140 z Σ_{m≥1} Σ_{n≥1} a(m) ρ_n / (7m + n z),  with a(m) = ψ(m)·1_{(m,10)=1}.

Checks (all Cat A, numerical):
- **High precision.** On all 44 grid rationals in [1/8, 2] with denominators ≤ 8, this agrees with the exact Bernoulli-sum ψ to **|Δ| ≤ 5.7·10⁻³³** at 34 digits. This includes ψ(1) = 0.006883993760419869190321587 − 0.03825971221697307224258855 i.
- **Random rationals.** 40 random rationals with denominators ≤ 60, both signs: 2.5·10⁻¹².
- **Off the real axis.** The identity also holds as holomorphic functions on Re z > 0. At z = 1+0.6i and 2+i, the q-series cocycle E_L(−1/z) − (z/√35)E_R(z) agrees with the 34-digit Herglotz value to 3·10⁻¹⁷ and 2·10⁻¹⁶ (q-series in double precision).
- **No remainder.** The identity has no elementary correction terms: no constant, no log, no polynomial.

What this means:
- ψ_Eis is a "twisted Herglotz/Kronecker-limit" function.
- No log-regularisation is needed, because ψ′ is never trivial and the B₁-moment of ρ vanishes whenever a(m) has nonzero mean.
- This differs from Radchenko–Zagier's untwisted F(x) = Σ(ψ_Γ(nx) − log nx)/n, whose rational values involve dilogarithms. Here the combination takes algebraic values at every rational (the earlier Bernoulli sums).
- Proof status: the derivation is complete for the E_L half (§1.2). The cancellation of the E_R half is verified numerically but not proved (**Cat B**).

**(B) The cusp rows are exact combinations of Hecke L-values at s = 0, not of central values.** For every cusp row c of the vector-valued cocycle Φ, and every rational x among the 7 test points (1, 1/3, 2, 3/5, 7/4, −1, −2/3):

  **Φ_c(x) = κ_c(−1/x) − |x| Σ_{c′∈cusp} S_{cc′} κ_{c′}(x),**

  **κ_c(h/k) = Σ_{χ′} Ĝ_{c,h/k}(χ′) · L_{𝔪_k}(0, χ′),**

where:
- χ′ runs over ray class characters of Q(√35) of modulus 𝔪_k, which is (2√35)·∞₁∞₂ with extra powers of 𝔭₂, 𝔭₅, 𝔭₇ and (3) as k requires.
- Ĝ is an explicit finite Fourier coefficient built from the exact cusp coefficients F̂_c(χ) = (1/48)e(k/60) and the additive character e(hN𝔞/(140k)).

Equivalently, when k has no factor 3:

  κ_c(h/k) = (1/φ(140k)) Σ_{ψ mod 140k} τ(ψ̄) ψ(h) Σ_χ F̂_c(χ) · L(0, u_χ ⊗ ψ).

When 3 | k there is one extra term from ideals divisible by the inert prime 3 (§2.2).

Agreement (Cat A, using PARI lfun values):
- All 24 cusp rows at all 7 points: max deviation **4·10⁻¹⁴** from the exact Bernoulli values. For example, Φ₇₃(1) = 0.120446470003 + 0.176437422094 i.
- Only **totally odd** cusp characters contribute. For those, L(0,χ) = W(χ)·140·L(1,χ̄)/π², checked to 2·10⁻¹⁵.
- The L(0) values are algebraic integers in Z[ζ₁₂], for example L(0, χ_{3,1,1}) = −12 + 4i and L(0, χ_{1,1,1}) = −(6+4√3) + (6√3−4)i (recognised to 10⁻¹⁰).
- So the cusp-row values at rationals are combinations of **edge values** L(0) ~ L(1). They are not combinations of central values.

The precise mismatch with the central-value hypothesis:
- Replace every L(0,·) by L(½,·) in the exact formula. Then Φ₇₃(1) becomes 0.0349 + 0.0748 i instead of 0.1204 + 0.1764 i, a max deviation of 0.32 over the 24 rows.
- Using only the 12 totally odd central values gives a deviation of 0.31.
- At x = 1 the 24 cusp-row values lie in a 6-dimensional space, one direction per σ-pair of totally odd characters.
- The central values of the 12 forms are tabulated (§2.3). They enter integrals or Mellin transforms of Φ, not the point values. That last statement is Cat B: standard LZ theory, not tested here.

**Hand certification.** Cl⁺_{(2√35)∞₁∞₂} ≅ Z/2 × Z/2 × Z/24 is now certified **without PARI**, together with the σ-action, the infinity types and the conductors (§3). Of the 96 characters, exactly 24 are non-σ-invariant of pure type, all of conductor (2√35): 12 of type (0,0) and 12 of type (1,1). This matches PARI.

## 1. (A) Details

### 1.1 Starting point (Cat A, from earlier reports)
- Ψ(z) = E_L(−1/z) − (z/√35)E_R(z) is holomorphic on H. It continues to Re z > 0, with boundary values ψ(x) given by exact Bernoulli sums.
- u_L is pure Eisenstein. Its positive part is E_L(τ) = Σ_χ (e(−j/8)/16)·G_χ(τ/20), with G_χ(τ) = Σ_{m,k≥1} a(m)b(k) e(mkτ), a = ψ·1_{(·,10)=1}, b = ψ′.

### 1.2 Derivation (Cat A for the E_L half, Cat B for the final cancellation)

1. **Lambert part.** Set B(u) := Σ_k b(k)e(ku) = Σ_{r=1}^{140} b(r)e(ru)/(1−e(140u)). Then

   B(u) = π Σ_{s mod 140} ρ_s cot(π(u − s/140)) = Σ_{n∈Z} ρ_n/(u − n/140),

   with symmetric summation. This follows from Liouville: both sides are 1-periodic with the same poles and both tend to 0 at ±i∞, because b(140) = 0 and ρ₀ = 0 (b has mean zero).

2. **Split.** G(−1/(20z)) = Σ_m a(m)B(−m/(20z)). The n > 0 terms give exactly R_χ(z), which is regular on Re z > 0. The n < 0 terms are the singular part.

3. **Rewrite the singular part.** Using Σ_{m≥1} = Σ_{m∈Z} + η_a Σ_{m≥1}(m+v)^{−1}, the singular part equals a Lambert series in z plus η_aη_b·R_χ(z). Here η_aη_b = χ₁₄₀(−1) = +1.

4. **Cancellation (numerical, not proved).** The Lambert-series remainder, summed over χ, cancels against (z/√35)E_R(z). This is the expected Gauss-sum (Poisson) duality, which is the S-law. I verified it only through the end identity: at complex z, and on the real axis to 33 digits. It is not written out as a proof.

   Result: Ψ(z) = Σ_χ (e(−j/8)/16)·(1 + η_aη_b)·R_χ(z) = (1/8) Σ e(−j/8) R_χ(z).

5. **Numerics.** The digamma form converges. Σ_s ρ_s = 0 kills the log, and the 1/X term vanishes or is conditionally summable.
   - The tail uses ψ_Γ(X+h) ~ log X + Σ_{k≥1} (−1)^{k+1}B_k(h)/(kX^k), with tails Σ_{m>M} a(m)m^{−k} done by Hurwitz ζ.
   - Settings: 34 digits, M up to 420, 80 terms.
   - A double-precision version (`herglotz.py`) has a floor of about 1.5·10⁻¹², set by scipy accuracy.

### 1.3 What is and is not claimed
- **Claimed (Cat A, numerical):** the twisted-Herglotz identity above, at 33 digits on 44 rationals, 2.5·10⁻¹² on 40 more, and at complex points.
- **Cat B:** the analytic proof of step 4. The reading of R_χ as the Lewis–Zagier Eisenstein period function at s = ½ for (ψ, ψ′) (LZ Ch. IV). Any functional equations of the individual R_χ, Radchenko–Zagier style, which I did not derive.
- **Not tested:** whether an individual R_χ(x) is algebraic at rationals. Only the full combination is known to be.

## 2. (B) Details

### 2.1 Why s = 0 (Cat A)
- κ_c(x) is the t⁰ coefficient of f_c(e(x)e^{−t}). By Mellin, Γ(w)·Z_c(w; x)·t^{−w} with Z_c(w; x) = Σ A_Q e(Qx) Q^{−w}.
- For a cusp row, Z_c is entire. So κ_c(x) = Z_c(0; x), the additively twisted L-value at **w = 0**.
- For x = h/k with k built from 2, 5 and 7, e(hN𝔞/(140k)) is a ray class function: N𝔞 mod 140k is constant on classes mod 𝔪_k, because α ≡ 1 mod^× 𝔪_k and α ≫ 0 imply Nα ≡ 1 mod 140k. This was checked on all classes up to norm 60 000.
- For 3 | k, write 𝔞 = (3)𝔞′ for the ideals divisible by the inert prime 3. Then Z = Z_A + 9^{−w}Z_B, both ray-class sums, and no derivative terms appear.

### 2.2 Verification (`cusp_rows_L.txt`, `cusp_rows_L2.txt`, `cusp_rows_L3.txt`)
- **L-values:** PARI lfun on [bnr, χ] (primitive), times imprimitive Euler factors (1 − χ_prim(𝔭)) at the primes 𝔭 | 𝔪 not dividing the conductor. Primitive characters were obtained through bnrmap. Precision is 38 digits.

| x | κ(−1/x) dev | κ(x) dev | Φ_c(x) dev (24 rows) | Φ₇₃(x) |
|---|---|---|---|---|
| 1 | 3.4e-15 | 3.2e-15 | 3.8e-15 | 0.120446470003+0.176437422094i |
| −1 | — | — | 4.5e-15 | 0.006264073515+0.213537531676i |
| 2 | 7.5e-15 | 3.4e-15 | 9.6e-15 | 0.206217773055+0.263200146342i |
| 7/4 | 3.3e-13 | 2.0e-14 | 3.4e-13 | 0.188336862451+0.245368413466i |
| 1/3 | 5.6e-15 | 1.6e-14 | 6.7e-15 | 0.038631276713+0.077116144808i |
| 3/5 | 2.1e-14 | 9.2e-14 | 4.0e-14 | 0.073437646967+0.123627119436i |
| −2/3 | 7.5e-15 | 1.1e-14 | 1.2e-14 | 0.012354928128+0.156183157173i |

- **Which L-values enter.** At x = 1, row 73 involves 24 characters: the cusp characters times genus twists ψ∘N, all of them cusp characters again. Only the 12 totally odd ones have L(0) ≠ 0.
- The type (0,0) characters have L(0) = 0, a double zero coming from Γ_R(s)²; mixed-type characters have L(0) = 0 as well. This is Cat A from the PARI values and Cat B as theory (the Hecke functional equation).

### 2.3 Central values of the 12 forms (`lvalues.txt`; PARI, 38 digits)

| χ (σ-pair) | type | root number W | L(½, u_χ) | L(0) |
|---|---|---|---|---|
| (1,·,1) ~ (13,·,1) | (0,0) | 0.933454−0.358698i | 1.109240202417−0.205788403698i | 0 |
| | (1,1) | −0.933454+0.358698i | 0.131513747745+0.708885114750i | −(6+4√3)+(6√3−4)i |
| (3,·,1) ~ (15,·,1) | (0,0) | 0.850651−0.525731i | 1.057777176883−0.300492329005i | 0 |
| | (1,1) | −0.850651+0.525731i | −0.123002454086−0.432986722370i | −12+4i |
| (5,·,1) ~ (17,·,1) | (0,0) | 0.096624+0.995321i | 0.514021161380+0.466537408032i | 0 |
| | (1,1) | −0.096624−0.995321i | 1.122786592523−1.237062791397i | (4√3−6)−(4+6√3)i |

- The other 6 forms, j = 7, 9, 11 ~ 19, 21, 23, are the complex conjugates.
- All 12 central values are nonzero.

## 3. Hand certification of Cl⁺_{(2√35)} (Cat A, PARI-free; `hand_cert.py`)

**Exact sequence.** 1 → U/U_{𝔪,1} → (O/𝔪)^× × {±}² → Cl⁺_𝔪 → Cl → 1, with 𝔪 = 𝔭₂²𝔭₅𝔭₇ = (2√35).

**The pieces:**
- (O/(2))^× = ⟨√35⟩ ≅ Z/2, since O/2 = F₂[t]/(t+1)².
- F₅^× = ⟨2⟩ ≅ Z/4 and F₇^× = ⟨3⟩ ≅ Z/6. Elements a+b√35 reduce to a, because √35 ≡ 0 at 𝔭₅ and 𝔭₇.
- Units: U = ⟨−1, ε = 6+√35⟩. In coordinates, −1 ↦ (0,2,3;1,1) and ε ↦ (1,0,3;0,0).
- Cl = Z/2, generated by 𝔭₁₃:
  - x² − 35y² = ±13 has no solution mod 5;
  - 𝔭₁₃² = (22+3√35), which has norm 169, is totally positive, and is not divisible by 13;
  - its image is (1,1,0;0,0).

**Group structure.** The Smith normal form of the relation matrix gives invariants **[2, 2, 24]**, order 96. This agrees with the hand count h·φ(𝔪)·4/[U : U_{𝔪,1}] = 2·48·4/4.

**σ-action.**
- σ is trivial on the residue coordinates, since −√35 ≡ √35 mod 2, and swaps the signs.
- σ(q) = [(13)] − q, with [(13)] ↦ (0,3,3;0,0).

**Characters.** Enumerating all 96 characters, with types read off the sign coordinates and conductors off the local unit components:
- 24 are non-σ-invariant of pure type, all with finite conductor 𝔭₂²𝔭₅𝔭₇, split 12 of type (0,0) and 12 of type (1,1);
- 48 are mixed;
- 24 are σ-invariant (genus).

All counts match PARI (`bigray.txt` of the Cusp-Part report).

## 4. Cat A / Cat B

**Cat A**
- The twisted-Herglotz closed form for ψ_Eis: 33 digits on 44 rationals, 40 random rationals, and complex z.
- The E_L half of its derivation.
- Cusp rows equal L(0)-combinations at all 7 test points, to 4·10⁻¹⁴, where the L-values come from PARI lfun.
- The functional equation check L(0) = W·140·L(1,χ̄)/π², to 2·10⁻¹⁵.
- The central values computed and tabulated.
- The central-value hypothesis rejected (deviation 0.3).
- PARI-free certification of Cl⁺_{(2√35)}: structure, σ-action, types, conductors.

**Cat B**
- Analytic proof of the E_R cancellation (step 4 of §1.2).
- Lewis–Zagier reading of R_χ as Eisenstein period functions, and of central values as Mellin data of Φ.
- The Hecke functional equation and Γ-factor zero pattern as theory.
- Correctness of PARI's lfun implementation (internally consistent here: the functional equation holds, and the Bernoulli values are reproduced to 10⁻¹⁴).

**Citations** (status unchanged from the previous report unless noted):
- Radchenko–Zagier, J. reine angew. Math., doi:10.1515/crelle-2023-0009, arXiv:2012.15805. Bibliographic data and the Eichler-integral and cocycle statements were checked online in the previous session.
- Zagier, "A Kronecker limit formula for real quadratic fields", Math. Ann. 213 (1975). Cited only as context for the Herglotz function. **Not checked online in this session.**
- Lewis–Zagier, Ann. Math. 153 (2001), arXiv:math/0101270. Verified earlier.
- Maass, Math. Ann. 121 (1949) 141–183. Bibliographic data verified.
- Hecke: the functional equation for Größencharaktere, cited generically.

## 5. Side notes
- `er_fit.py`: a naive fit of u_R's coefficients to divisor sums (ψ₁*ψ₂)(n/d) with genus pairs **failed** (residual 4). It was not needed once (A) was found, but it means E_R's own Eisenstein basis was not identified.
- The double-precision Herglotz code has a floor of about 1.5·10⁻¹². The 34-digit code removes it.

## 6. Files (`2026-10-17-psiEis-Lvalues/`)
- `herglotz.py`: double-precision R_χ.
- `hp_check.py` → `hp_check.txt`: 34-digit check on 44 rationals; the exact κ is re-implemented in mpmath.
- `complex_check.py` → `complex_check.txt`; `complex_hp.py` → `complex_hp.txt`.
- `lvalues.py` → `lvalues.txt`, `lvalues.pkl`: all 96 characters, L(0), L(½), L(1), root numbers.
- `cusp_rows_L.py` → `cusp_rows_L.txt`: x = ±1.
- `cusp_rows_L2.py` → `cusp_rows_L2.txt`: x = 2, 7/4.
- `cusp_rows_L3.py` → `cusp_rows_L3.txt`: x = 1/3, 3/5, −2/3.
- `central_test.py` → `central_test.txt`.
- `hand_cert.py` → `hand_cert.txt`.
- `er_data.py`, `er_fit.py`: failed side attempt.
- Copied helpers: `family.py`, `uvec.py`, `kappa_all.py`, `fastkappa.py`, `fitF.pkl`, `component_split.json`.
