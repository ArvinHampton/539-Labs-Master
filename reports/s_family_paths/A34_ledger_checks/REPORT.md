# A34: checks and closures for the clean Category A ledger

**For:** Arvin Hampton · 2026-10-22, America/Chicago (CDT).

**Ground rules.**
- New files only, in `SF/A34_ledger_checks/`.
- CORE_FREEZE is respected: H_s is not redefined, and no certifier code was touched or run.
- The s31 mm sector was not touched.
- All jobs ran under `nice` with OMP_NUM_THREADS=1 and `ulimit -v` ≤ 2.5 GB. Peak resident memory was about 0.7 GB.
- Nothing was pushed or sent. No TPC/RH claims are made.

**Categories.** **Cat A** = proved, or exact relative to named hypotheses. **Cat B** = numerical or interpretive. The two are kept strictly apart.

`SF/` = `/workspace/quantum-comp/reports/s_family_paths/`. Entry numbers refer to `LEDGER_CatA_clean` (v1).

## Summary

| Item | Outcome |
|---|---|
| (1) Entry 14, closed forms for d_cusp | **Fixed.** The odd-s statements are verified. The even-s statements are only conditional, and one step has a gap (§1.1). |
| (1) Entry 17, Gauss-sum vanishing | **Fixed.** The statement had a transcription error: it read "2 ‖ m" where the correct condition is "2 \| m". The full proof is verified, and the exact values of \|G\| were added (§1.2). |
| (1) Entry 23, Hecke commutation | **Verified** under the hypothesis of Γ(N)-invariance (TB4). The proof is written out (§1.3). |
| (1) Entry 24, sector lemma | **Fixed.** The proof needs dim V = dim W, which is proved only for odd s ≤ 51, so the scope is restricted to that range (§1.4). |
| (2) Certificate 10 | **Fixed citation.** The Y-certificate is `SF/A8c_Spairing_even/scripts/pairing_on_W.py`, not `A8_Spairing_even/modp_trace.py`. Re-run for s = 8, 16, 18, 24, 26: identical results. `global_trE.py` was also re-run: identical results. |
| (2) Certificate 56 | **Verified** (`galois_dilation_fast.py`). Re-run at s = 8 and 10: identical results. |
| (2) Certificate 57 | **Fixed.** The script `classgroups_A5.py` uses PARI `quadclassunit`, so I replaced it with an unconditional reduction-cycle computation (`A34/scripts/classno_exact.py`). The values agree. **The claim "the Cl(4n_s) predictor fails at s = 25" was wrong**: the predictor gives 3, and dim S(ρ_25) = 3. The correct exact failures are listed in §2.3. |
| (2) Certificate 58 | **Fixed citation.** The (187, 186, 187) multiplicities came from `scan.py`, which is floating point (Cat B). The entry now has a proof: entry 11 together with an exact dim E = 560 (§2.4). |
| (3) rev1 entry 15, distribution of r | **Closed** (Cat A). The CHECK marks are resolved. The mean upper bound follows from Nair–Tenenbaum (Acta Math. 180 (1998), Theorem 1), whose hypotheses I verified. The lower bound is elementary. The Gaussian refinement is not needed and is not included (§3.1). |
| (3) Friction-coupled PDE | **Closed for its spatially homogeneous reduction.** In that reduction there is no attracting solution of any kind, and the stated function is not a solution. **The full PDE is not well-formed**: the contraction for γF∇Φ is unspecified, so nothing can be proved about it (§3.2). |
| (3) Class-group predictor at s = 27, 29 | **Failed to close.** dim S(ρ_s) ∈ [3, 4] at both s, and the predictor value is 3. Raising the Hecke lower bound with 8 primes leaves it at 3 (§3.3). Only the Cl(K_s) version fails exactly there. |
| (3) E_L ↔ u_L identification | **Not proved; left out.** It is an analytic identification of a cone-sum generating function with a Maass theta lift. None of the ledger entries depends on it (§3.4). |
| Found during checks | Entry 2 (s ≡ 4, 6 mod 8) **failed as stated**. A6 verified the even-s step only for s ≤ 38. It is replaced by an exact certificate for 12 ≤ s ≤ 46 (§2.5). As a result, the corollary "tr_C S = 0 for every s ≥ 5" is narrowed to the proved ranges. |

## 1. Proof checks

### 1.1 Entry 14 (closed forms for d_cusp; `SF/A/REPORT.md` §1, `p1_formula_check.py`)

The setting is odd s with n = s(s−2), G(m) = ∏_{q‖m} (q+1)/2, dim V = s(s−1) and d_Eis = 3G(n).

- **Lemma (verified).** For odd m, G(m) ≤ (m+1)/2, with equality iff m = 1 or m is a prime power.
  - *Proof.* If m = q is a prime power, G = (q+1)/2.
  - For coprime odd a, b ≥ 3, we have (a+1)(b+1)/4 < (ab+1)/2. This is equivalent to (a−1)(b−1) > 0.
  - If G(a) ≤ (a+1)/2 and G(b) ≤ (b+1)/2, then G(ab) = G(a)G(b) ≤ (a+1)(b+1)/4 < (ab+1)/2.
  - Induction on the number of prime-power factors gives the lemma, with strict inequality whenever there are two or more factors.
- **Odd s lower bound (verified).**
  - Since gcd(s, s−2) = 1, G(n) = G(s)G(s−2) ≤ (s+1)(s−1)/4.
  - So d_cusp = s(s−1) − 3G(n) ≥ s(s−1) − 3(s²−1)/4 = (s−1)(s−3)/4 > 0 for s ≥ 5.
  - Equality holds iff s and s−2 are both prime powers.
- **Odd s parity (verified).**
  - s(s−1) is even.
  - One of s, s−2 is ≡ 3 mod 4. An integer ≡ 3 mod 4 has a prime-power factor q ∥ it with q ≡ 3 mod 4, because a product of factors ≡ 1 mod 4 is ≡ 1 mod 4.
  - For such q, (q+1)/2 is even, so G(n) is even and d_Eis is even.
- **Even s: d_cusp = 0 ⇔ s ∈ {6, 8, 10}, and parity (NOT verified unconditionally).**
  - The proof assumes d₂(k, v) ≤ 2^{k−1} + 6, which is proved only for k ≤ 6.
  - Step 4 (s = 2m²) bounds the number of extra relations only as "at most about m/2", which is not a proof.
  - Parity at even s needs the d₂ formula for every k.
  - **Status:** odd-s statements are Cat A at formula level. The even-s statements are dropped from the ledger.
- **Scope.** These are statements about closed forms. They equal the true d_cusp where dim V and d_Eis are proved: dim V = s(s−1) for odd s ≤ 51, together with the certified local factors.

### 1.2 Entry 17 (Gauss-sum vanishing; `stage_ps/.../P_s-Structure §A4`, `heavy-daily/2026-10-18-C_third-modularity/theoremG_check.py`)

**Definitions.**
- Q(n,k) = n² + 7nk + 7k(k+1)/2, which is integer-valued.
- For gcd(h,m) = 1, G(h/m) = (2m)^{−2} Σ_{n,k mod 2m} e(hQ(n,k)/m).

The summand is 2m-periodic in each variable, since Q(n+2m,k) − Q(n,k) and Q(n,k+2m) − Q(n,k) are both divisible by m.

**Statement.** G(h/m) = 0 iff 2 | m or 5 | m. Otherwise:
- |G| = 1/m if 7 ∤ m;
- |G| = √7/m if 7 | m.

The v1 ledger had "2 ‖ m". That is a transcription error: the source writes "2\|m", an escaped "|".

**Proof (verified line by line).**
- **2 | m.** Q(n,k+m) − Q(n,k) = m(7n + 7k + 7(m+1)/2). With m even, the phase change is e(7h(m+1)/2) = −1, because 7h(m+1) is odd. The shift k ↦ k+m is a bijection mod 2m, so G = −G = 0.
- **m odd, 5 | m.** Put a = m/5. Then Q(n−a, k+a) − Q(n,k) = mn + a(7−m)/2. The phase is e(h(7−m)/10). Here (7−m)/2 ≡ 7·2^{−1} ≡ 1 mod 5 and gcd(h,5) = 1, so the phase is ≠ 1, and G = 0.
- **m odd, 5 ∤ m.**
  - Q is m-periodic, so G = m^{−2} Σ_{n,k mod m}.
  - With 2 invertible mod m, the substitution n′ = n + 7·2^{−1}k gives hQ ≡ h(n′² − (35/4)k² + (7/2)k).
  - So G = m^{−2} g₁ g₂ with g₁ = Σ_{n′} e(hn′²/m), and |g₁| = √m.
  - By CRT, g₂ factors over p^e ∥ m.
    - If p ∤ 35, the quadratic coefficient is a unit, and completing the square gives modulus p^{e/2}.
    - If p = 7, the sum is Σ_{k mod 7^e} e(h′(−(5/4)k² + k/2)/7^{e−1}) = 7·Σ_{k mod 7^{e−1}}(…). Its modulus is 7·7^{(e−1)/2} = 7^{(e+1)/2}, because the quadratic coefficient is a unit mod 7.
  - Hence |G| = m^{−2}·√m·√m·(√7 if 7 | m) ≠ 0.

**Cross-check (Cat B, float).** `theoremG_check.py` covers m ≤ 60 (1102 rationals) with 0 mismatches. The source reports m ≤ 105 (3374 pairs) with 0 mismatches.

### 1.3 Entry 23 (Hecke commutation; `SF/A7_s21/REPORT.md` A1)

**Hypotheses.**
- N ≥ 1, and p is prime with p ≡ 1 mod N.
- F is a smooth vector-valued function with F(γz) = ρ(γ)F(z) for γ ∈ SL₂(Z), and F is Γ(N)-invariant (TB4).
- ΔF = λF.

**Definition.** T′_p F(z) = p^{−1/2}[F(pz) + Σ_{j=0}^{p−1} F((z+Nj)/p)].

**Statement.**
- T′_p F is of type ρ with the same λ, and it commutes with every constant matrix commuting with ρ (in particular the P_σ).
- If every component of F has the form Σ_{m∈(1/N)Z} a(m)√y K₀(2π|m|y)e(mx) + c√y, then T′_p F has coefficients b(m) = a(pm) + a(m/p), and constant term 2c.

**Proof (verified).**
1. Let Δ = {M ∈ M₂(Z) : det M = p, M ≡ I mod N}. The p+1 matrices (1, Nj; 0, p) and (p, 0; 0, 1) lie in Δ, because p ≡ 1 mod N. They are inequivalent under left multiplication by Γ(N), and since |Γ(N)\Δ| = p + 1 for p ∤ N, they form a complete system of representatives.
2. For γ ∈ SL₂(Z), γ^{−1}Δγ = Δ, so {γ^{−1}Mγ} is again a system of representatives.
3. Then Σ_M F(Mγz) = Σ_M F(γ·γ^{−1}Mγ·z) = ρ(γ) Σ_{M′} F(M′z). Changing representatives does not change the sum, by Γ(N)-invariance.
4. Δ (the Laplacian) commutes with every z ↦ Mz for M ∈ GL₂⁺(R), so λ is preserved. The operator acts componentwise, so it commutes with constant matrices.
5. **Fourier side.** F(pz) contributes p^{1/2} a(m′/p) at frequency m′.
   - Σ_j e(mNj/p) = p if p | mN and 0 otherwise. Since mN ∈ Z and gcd(p,N) = 1, p | mN iff m/p ∈ (1/N)Z.
   - So Σ_j F((z+Nj)/p) contributes p·a(pm′)√(y/p) at frequency m′.
   - After the factor p^{−1/2} this gives b = a(pm′) + a(m′/p). The √y-terms contribute c + c.

### 1.4 Entry 24 (sector lemma; `SF/A6_certify/REPORT.md` A1)

**Hypotheses.**
- TB2: u has type ρ_s and λ = 1/4. Its constant term is a multiple of c₀ = Π_W δ₀. The λ = 1/4 constant-term criterion holds.
- s is odd with 5 ≤ s ≤ 51, so dim V = dim W = s(s−1) and the components of u on W are linearly independent.
- σ is a P-even local-sign sector other than all-plus, with P_σW ≠ 0.

**Proof (verified, with the hypothesis made explicit).**
1. P_σ is a polynomial in the local reflections Z_p, which commute with ρ. So P_σu has type ρ_s and the same λ.
2. E = ρ-span(c₀) lies in the all-plus sector, because c₀ is even in every local component and the Z_p commute with ρ. Hence P_σc₀ = 0. The constant term of P_σu vanishes, so P_σu is cuspidal by the criterion.
3. If P_σu = 0, every row of P_σ would be a linear functional on W killing all values of u. By linear independence this forces P_σ|_W = 0, a contradiction.
4. Forms in distinct sectors are linearly independent, because the projectors are orthogonal.

The v1 hypothesis "P_σW ≠ 0" is equivalent to "P_σC ≠ 0" here, since P_σE = 0. **v1 omitted the range s ≤ 51; it is now explicit.**

## 2. Certificate and citation checks (re-runs in `A34/logs/`)

### 2.1 Certificate 10
- **Y = Z − SZS certificate.**
  - The correct script is `SF/A8c_Spairing_even/scripts/pairing_on_W.py`; `SF/A8_Spairing_even/scripts/modp_trace.py` is not it. The script computes rank_𝔭(Y_λ|_W) exactly mod 𝔭 on the orbit basis of W, for λ = (1) and (1,1), and checks Ŝ² = |det| on W.
  - Re-run (`logs/rerun_pairing_on_W.jsonl`): s = 8, 16, 18, 24, 26 give rank = dim W, identical to the source.
  - Source values: full rank for s = 8, 16, 18, 24, 26, 32, 40, 48, 50, 56, 58. At s = 34 and 42 the rank is dim W − 2, so Y certifies nothing there. At s = 10, C = 0.
- **global_trE.py.** Re-run (`logs/global_trE_rerun_and_4_6mod8.txt`): s = 8, 16, 18 give identical results.

### 2.2 Certificate 56 (`SF/A8c_Spairing_even/scripts/galois_dilation_fast.py`)

**What it computes.** For every a ∈ (Z/L)^×, label dilation M_u and k with σ_a(T) = M_u T^k M_u^{−1} (exact monomial identity), it tests σ_a(Ŝ) = ±M_u Ŝ M_u^{−1} mod one prime 𝔭.

**Why mod 𝔭 suffices.** A char-0 identity survives reduction, and +1 and −1 cannot both hold mod 𝔭.

**Results.**
- Re-run at s = 8 and 10 (`logs/rerun_galois_dilation_8_10.jsonl`): T-compatible (a,u,k) counts 1024 and 4096, ε = +1 counts 128 and 256, ε = −1 count 0. Identical to the source.
- s = 16 and 18 were not re-run; the source log is `galois_dilation_fast_16_18.jsonl`.
- The controls s = 12 and 14 do have ε = −1 solutions, which exercises the code.

### 2.3 Certificate 57 (class-group predictors)

**Predictor.** As stated in `SF/A2/REPORT.md` B2, the predictor for the group X is dim S(ρ_s) = h(X)/2 if Cl(X) is cyclic, and h(X) if Cl(X) ≅ [2,2].

**Exact class numbers.** `scripts/classno_exact.py` counts cycles of reduced primitive indefinite forms. This is unconditional; PARI `quadclassunit` is GRH-conditional. Results are in `classno_exact.json`, and all agree with `SF/A5_classgroup/classgroups_A5.json`.

| s | d_K | h(K_s) | h(4n_s) | certified dim |
|---|---|---|---|---|
| 9 | 28 | 1 | 2 | 1 |
| 11 | 44 | 1 | 4 | 2 |
| 23 | 1932 | 4 | 4 | 3 |
| 25 | 92 | 1 | 6 | 3 |
| 27 | 12 | 1 | 6 | [3, 4] |
| 29 | 348 | 2 | 6 | [3, 4] |

**Exact conclusions (Cat A).**
- **Cl(K_s).** The predicted value is h/2 for cyclic groups. It gives 1/2 at s = 9, 11, 25, 27 and 1 at s = 29, so it fails at all five.
- **Cl(4n_s).**
  - At s = 23, h = 4, so the predicted value is 2 (if cyclic) or 4 (if [2,2]). Either way it is ≠ 3, so the predictor fails exactly at s = 23.
  - At s = 25, Cl(4n_25) has order 6 and is therefore cyclic. The predicted value is 3 = dim S(ρ_25), so the predictor **holds** there. The v1 claim was wrong.
  - At s = 27 and 29 the group is cyclic of order 6. The predicted value is 3, which lies inside the certified bracket, so this case is not decided (§3.3).

### 2.4 Certificate 58 (R-multiplicities on E at s = 56)
- The cited `exact_E0_R.py` certifies local classes only. The global (187, 186, 187) numbers come from `scan.py` (`logs_scan_s56.jsonl`), which is float64 SVD (Cat B).
- **Replacement proof (Cat A, assuming I1–I5).**
  - **dim E ≥ 560.** This is a mod-ℓ Krylov rank, so a lower bound, from `SF/A31_entry7_check/global_trE.py` at two primes.
  - **dim E is 504 or 560.** By the tensor factorisation (ledger entry 7(iii)), dim E = dim E0_{27}·dim E0_7·dim E0_2. The odd factors are 14 and 4 (entry 7(i)). For the 2-adic classes (2,1/4) ⊕ (8, −u/16) of order 16, `SF/A11_induction/exact_E0.py` (`logs_exact_E0.txt`, exact_span_certified) gives dim 10 for u ≡ 1 mod 4 and 9 for u ≡ 3 mod 4.
  - **So dim E = 560.**
  - **Multiplicities.** At s = 56, (Exc) holds and s ≡ 2 mod 3. So by entry 11, tr_E R = −ω and tr_W R = −ω. Solving n₁ + n_ω + n_ω̄ = 560 and n₁ + ωn_ω + ω̄n_ω̄ = −ω gives (187, 186, 187).
  - **On C.** dim W = 812 = t(t+1) with t = 28 (orbit count). Then dim C = 252 and tr_C R = 0, so the multiplicities on C are (84, 84, 84).
  - **Caveat.** This argument assumes the 2-adic component at s = 56 is one of the order-16 classes (2,1/4) ⊕ (8, −u/16) in A11's coverage list. The bound dim E ≥ 560 then excludes the dim-9 case.

### 2.5 Entry 2 (s ≡ 4, 6 mod 8): failed as stated, replaced
- `SF/A6_certify/REPORT.md` says the even-s analogue of step 2 (T^{2n} diagonal) "is computer-verified, not written for all s", for s = 6, 12, 14, 20, 22, 28, 30, 36, 38. So "for all s ≡ 4, 6 mod 8" is not proved.
- **New certificate.** `global_trE.py` was run for s = 12, 14, 20, 22, 28, 30, 36, 38, 44, 46. tr_E S = 0 at two primes each, an exact integer since |tr| ≤ dim E < ℓ/2.
- With tr_W S = 0 (entry 3), this gives tr_C S = 0 for every s ≡ 4, 6 mod 8 with 12 ≤ s ≤ 46. Here E = ρ-span(δ₀) in C[D], identified with the original E by entry 8.

## 3. Closure attempts

### 3.1 rev1 entry 15: distribution of r (odd s, formula level). **Closed.**

**Notation.**
- n = s(s−2) and k = ω(s) + ω(s−2).
- g(m) = ∏_{q‖m} (1+1/q)/2.
- 1 − r = 3·(s−2)/(s−1)·g(s)g(s−2).

All averages are over odd s ≤ X.

- **(a) Mean of k (elementary).**
  - For odd p ≤ X, the number of odd s ≤ X with p | s(s−2) is X/p + O(1).
  - Summing over p ≤ X: mean k = Σ_{3≤p≤X} 2/p + O(1/log X) = 2 log log X + O(1), by Mertens.
  - For the second moment, pairs p ≠ q contribute density 4/(pq) + O(1/X). Truncating at p, q ≤ X^{1/4} and bounding the tail by O(1) gives Var k ≪ log log X (Turán–Kubilius).
- **(b) The limit law of r is δ₁ (elementary).**
  - By Chebyshev and (a), k ≥ log log X for all but O(X/log log X) odd s ≤ X.
  - For those s, 1 − r ≤ 3(2/3)^k → 0.
  - Since r ≤ 1, the empirical law of r converges to δ₁, and mean r → 1.
- **(c) Typical rate (elementary).** For almost all odd s:
  - log(1−r) = −k log 2 + Y + O(1), where 0 ≤ Y ≤ Σ_{p|n} 1/p ≪ log log log s;
  - and k = 2 log log s + O(ψ(s)√(log log s)) for any ψ → ∞.
  - Hence 1 − r = (log s)^{−2 log 2 + o(1)}.
- **(d) Mean of g(s)g(s−2).**
  - **Lower bound (elementary).** g ≥ 2^{−ω}, and x ↦ 2^{−x} is convex, so by Jensen the mean is ≥ 2^{−mean k}. That is ≫ (log X)^{−2 log 2}.
  - **Upper bound ≪ 1/log X.** Use Nair–Tenenbaum, Acta Math. 180 (1998) 119–144, Theorem 1, with k = 2, Q₁(n) = n, Q₂(n) = n−2, and y = x.
    - Q = n(n−2) has no fixed prime divisor, since Q(1) = −1.
    - F(n₁,n₂) = g(n₁)g(n₂), extended with g(2^e) = 1, satisfies F(m₁n₁, m₂n₂) = g(m₁)g(m₂)F(n₁,n₂) ≤ F(n₁,n₂). So F ∈ M₂(1, 1, ε).
    - The bound gives Σ_{n≤X} F ≪ X ∏_{p≤X}(1 − 2/p)(Σ_{n≤X} g(n)/n)².
    - Σ_{n≤X} g(n)/n ≤ ∏_{p≤X}(1 + 1/(2p) + O(p^{−2})) ≍ (log X)^{1/2}.
    - So the sum is ≪ X/log X. Restricting to odd n only decreases the sum, since F ≥ 0.
  - **Consequence.** Mean(1−r) ≍ mean g between (log X)^{−1.386} and (log X)^{−1}. By Markov, the density of {r < 1−ε} is ≪ 1/(ε log X).
- **(e) Y has a continuous limit law.**
  - *Existence.* Truncate at p ≤ y. By CRT, the truncated law is the law of Σ_{p≤y} X_p with independent X_p. The tail satisfies E|Y − Y_y| ≤ Σ_{p>y} 2/p² → 0.
  - *Continuity.* Each X_p is discrete with largest atom P(X_p = 0) = 1 − 2/p for p ≥ 5, and ∏_p(1 − 2/p) = 0. By Lévy's theorem (P. Lévy, Studia Math. 3 (1931); see also Elliott, *Probabilistic Number Theory I*, Ch. 1), a convergent series of independent discrete variables has a continuous law iff the product of its largest atoms is 0.
  - **Note.** This uses one classical cited theorem, stated with its hypothesis verified.
- **(f) Limit-point structure (elementary; source A5).** The set L of limit points of r satisfies L ⊆ {1} ∪ {1 − 3w : w ∈ W}, where W = {2^{−2−j}∏_{q∈S}(1+1/q)/2}.
  - Along a subsequence with limit < 1, k is bounded. Pass to subsequences on which each prime-power factor is either constant or tends to ∞; each factor tending to ∞ contributes 1/2.
  - So L is countable and closed, and L ⊆ {1/4} ∪ [1/2, 1].
- **Not included.**
  - The Gaussian refinement (Halberstam) and the Chen-type disjunctions of A4 A6 are not needed.
  - The Euler-product asymptotic B1 is Cat B.

### 3.2 Friction-coupled PDE (`SF/../maths/theorem-lemma-chain-9-maths.txt` Lemma 5 / Def. 1.1; `SF/A19_9maths_axioms` §1.6)

**The source equation.**

∂_t²Φ + γ_LQG F_friction(t)∇Φ + ρ_snap Θ_hyp(ρ_snap − ρ_DM) ∂_t²Φ = κ_dark sin(2πt/539.9) Φ + β_PBH ∂_t(e^{−M/k_BT} Φ̇).

- The full equation is **not well-formed**. γF∇Φ is a vector added to scalars, with no contraction specified, and F_friction is never defined. So "no periodic attractor" cannot be stated or proved for it. **Failed (not provable).**
- **Self-contained reduction (Cat A).** Take Φ = Φ(t), so ∇Φ = 0, and freeze c = ρ_snapΘ_hyp and g = e^{−M/k_BT} as constants. With ω = 2π/539.9 and A = 1 + c − βg, the equation becomes
  - (★) AΦ″ = κ sin(ωt) Φ.
- **Theorem.** Assume κ ≠ 0.
  - (i) For any Φ₀ and any (a,b) ≠ (0,0), the function Φ₀ + a cos ωt + b sin ωt does not solve (★). In particular the source's Φ₀ + 0.90 cos ωt + 0.18 sin ωt does not.
  - (ii) If A ≠ 0, (★) has no solution that attracts all solutions.
  - (iii) If A = 0, the only solution is Φ ≡ 0.
- **Proof.**
  - (i) The left side contains only the frequency ω. The right side contains (κa/2) sin 2ωt − (κb/2) cos 2ωt. Both must vanish, so a = b = 0.
  - (ii) (★) is the linear system x′ = M(t)x with x = (Φ, Φ′), where tr M = 0. By Liouville, the monodromy matrix has determinant 1.
    - Suppose a solution p attracts every solution, meaning |x(t) − p(t)| → 0 for all x. Since x − p ranges over all solutions, every solution tends to 0.
    - Then both Floquet multipliers have modulus < 1, contradicting det = 1.
  - (iii) If A = 0, then κ sin(ωt)Φ = 0, so Φ = 0 wherever sin ωt ≠ 0, and by continuity Φ ≡ 0.
- The `checks.py` harmonic balance (sympy) agrees with (i).

### 3.3 Class-group predictor at s = 27 and 29. **Failed to close.**
- **Upper bounds.** s = 27 (3−,5−) ≤ 3 is certified (`SF/A9_hecke_family/certs/hcert_s27_3m_5m_M6_Q40.json`, re-read, not re-run). The (+,+) sector certificates for s = 27 and 29, and the s = 29 (−,−) certificate, never completed: OOM or box restart (`SF/A9/logs/queue_rerun.out`). I did not re-run them, because each needs hours of certifier time near the 3 GB limit.
- **Why upper bounds would not settle it anyway.** The Cl(4n) predictor value is 3. Refuting it needs **dim = 4, i.e. a lower bound of 4**, not an upper bound.
- **Attempt.** I copied `certify_hecke_s.py` to `A34/scripts` (unchanged) and ran it with 8 Hecke primes instead of 3 (`logs/hecke_27_29_NP8.out`, `certs/hecke_lower_s{27,29}.json`; 4 min each, < 0.7 GB).
  - The rank of {P_σu, T′_p P_σu} stays at 2 in (−,−) and 1 in (+,+), at both s.
  - So the Hecke span of the lift is exhausted. A third (−,−) form would need a different construction, such as a theta lift from another genus class.
- **Result.** dim S(ρ_s) ∈ [3, 4] at s = 27 and 29 (the upper bound 4 at s = 27 is not certified either, since (+,+) did not finish). Whether the Cl(4n) predictor fails there is undecided. The Cl(K_s) predictor fails exactly at both (§2.3).

### 3.4 E_L ↔ u_L (`SF/RTA_implications` §2). **Not proved; left out.**
- The claim identifies the ν ↦ −ν even part of the cone-sum series C_third,s with the λ = 1/4 Maass theta lift. It is Cat B by citation in its source (C_third-Unified).
- A proof would need the analytic comparison of the two generating functions: the indefinite theta integral against the cone sums, including the wall terms. That cannot be done within this check.
- No ledger entry uses it. Entry 25 (irreducibility of C at s = 7) is independent of it.

## 4. Other notes
- **Entry 1.** The proof is now the full A6 argument. It needs TB3 (S² = P on the label space, i.e. ρ(−I) = P), which is added as a standing hypothesis.
- **Cat B kept out of the ledger.** All float scans, the A5 dims, and `theoremG_check.py` (float).

## Files (all new)
- REPORT.md, REPORT.html, REPORT.pdf
- `scripts/classno_exact.py`, `classno_exact.json`
- `scripts/certify_hecke_s.py`, `coeffsS.py`, `liftS.py` (copies of A9's, unchanged); `certs/hecke_lower_s27.json`, `hecke_lower_s29.json`
- `logs/`: hecke_27_29_NP8.out, rerun_galois_dilation_8_10.jsonl, rerun_pairing_on_W.jsonl, global_trE_rerun_and_4_6mod8.txt
