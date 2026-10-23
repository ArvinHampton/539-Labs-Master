# A41: Towards a uniform mechanism for Parity Dominance of g_k, odd k

Date: 2026-10-22 (CDT). Folder: `reports/s_family_paths/A41_uniform_oddk/`. Only new files were written. No existing file or certifier code was modified, nothing was pushed, and no TPC or RH claim is made. Preregistration: `prereg/prereg.md`, sha256 `ec7470ad81ee8aebeca45396d883bb4c98a79dd223d40e09213112d65adf57f1`, written 14:58:45 CDT, before any computation for k ≥ 17 (`prereg/prereg.sha256` also hashes `analysis/ck.py` and `analysis/ck.txt`).

Object, as in A38–A40: g_k(q) = Σ_{n≥0} q^{n²}/(−q^k;q^k)_n. Here a_n(m) = (−1)^m φ_n(m) ≥ 0. For odd k, (−1)^d g_k(d) = E_d − O_d, where E_d sums over even n and O_d over odd n. Allowed d means d mod k is a square.

## Verdict

1. **No uniform closed-form identity was found.** Two members of the family are classical:
   - g_1 is Ramanujan's fifth-order mock theta function f_0(q) = Σ q^{n²}/(−q;q)_n.
   - g_2 is Ramanujan's third-order mock theta function φ(q) = Σ q^{n²}/(−q²;q²)_n.

   The k = 4 member is not identified here. For odd k ≥ 3 the evidence is against any theta, eta-quotient, mock theta or Appell–Lerch representation (§1; evidence only, not proof).
2. **A closed form for the growth constant was found.** The saddle-point growth constant of A39 is c_exp(k)² = L(z_k)/k, where L is the Rogers dilogarithm and z_k ∈ (0,1) solves 1 − z = z^{k/2}.
   - This is a rank-one Nahm-type equation with A = k/2.
   - The constant is a rational multiple of π² for k = 1, 2, 4 only, among k ≤ 25 (by PSLQ).
3. **A k-uniform asymptotic mechanism was found, but it is not proved.** The predicted limit is E_d/O_d → c_k = √((1−X_k)/(1+X_k)), with X_k = Y_k^{k/2} and Y_k^k + Y_k² = 1.
   - This comes from a parity bias in the n-ladder, and it is the same mechanism for every odd k.
   - It is algebraically identical to A39's (1 − Y^{k/2})/Y. c_k < 1 for every k (proved), so the mechanism predicts an eventual sign for all odd k.
   - However 1 − c_k ~ √(2 log k / k) → 0, so **no k-uniform η exists even asymptotically**. The correct uniform target is η_k ≍ 1 − c_k.
   - The asymptotic itself is Category B.
4. **Parity Dominance is now proved for k = 17, 19, 21, 23, 25** (Category A, computer-assisted, not independently audited). The block+tail method does not fail at k ≈ 17–19. The failure seen at cutoff N1 = 900 is removed by N1 = 1500. Constants are in the table after this list.

   A two-prime nonvanishing certificate covers allowed d ≤ 6·10^7 > max D_k. Hence **OccFilt_k(∞) = {squares mod k} for every odd k ≤ 25**, and the zero sets are the finite lists in §3.
5. **Mod 4 (proved for every even k).**
   - k ≡ 2 (mod 4): every allowed class is ONE.
   - k ≡ 0 (mod 4): MIX classes always exist, with an explicit 2-adic criterion. The MIX sign groups are the residue chains r and r + k/2.
   - This explains why the parity mechanism is absent for even k and why MIX classes have ratio → 1 (§4).

Parity Dominance constants for k = 17..25 (item 4):

| k | 17 | 19 | 21 | 23 | 25 |
|---|---|---|---|---|---|
| block ratio R_k (N1=1500) | 0.8314560 | 0.8575917 | 0.8834878 | 0.9090546 | 0.9348480 |
| η_k = 1−R_k−10^−6 (truncated) | **0.16854** | **0.14240** | **0.11651** | **0.09094** | **0.06515** |
| D_k | 37 895 709 | 40 987 057 | 42 790 252 | 45 486 986 | 48 035 214 |
| tail T(D_k) (must be ≤ 0) | −15.29 | −15.81 | −10.29 | −7.51 | −7.76 |

## 1. Generating function (step 1)

**Category A.**
- g_2 = φ(q), Ramanujan's third-order mock theta function. This holds by definition.
- Watson's identity 2φ(−q) − f(q) = (q;q)_∞/(−q;q)_∞² was checked exactly to q^3000 (`analysis/watson_k2.py`). Here f is the third-order f(q) = Σ q^{n²}/(−q;q)_n².
- g_1 = f_0(q), the fifth-order mock theta function. This also holds by definition; the family extends to k = 1. For k = 1 the exact E/O at d = 10^5 is 0.346028, against the predicted c_1 = 0.346014. The zeros are d = 4, 5, 8.

**Category A (exact algebra and check): pairing identity, valid for every odd k.** With P_n(q) = ∏_{j≤n}(1 + (−q^k)^j),

  g_k(−q) = Σ_{m≥0} U_m(q)·(1 − q^{4m+1} − q^{(2m+1)k}),  where U_m = q^{4m²} / (P_{2m}(q)(1 − q^{(2m+1)k})) ∈ Z_{≥0}[[q]].

*Proof.*
- Write T_n for the n-th term of g_k(−q). Then T_n = (−1)^n q^{n²}/P_n, because (−(−q)^k; (−q)^k)_n = P_n for odd k.
- T_{2m+1} = −T_{2m}·q^{4m+1}/(1 − q^{(2m+1)k}). Adding T_{2m} and T_{2m+1} gives the identity.
- U_m ≥ 0 coefficientwise follows from the positivity lemma of A39 together with 1/(1 − q^e) ≥ 0. ∎

Checked to q^4000 for k = 1, 3, 5, 7, 17, 25 (`analysis/pairing.py`). With Y = q^{2m}, the bracket is 1 − Y² − Y^k. It vanishes exactly on Y^k + Y² = 1, the saddle equation of A39. This is the uniform algebraic origin of y_k.

**Growth constant (Category A as algebra; Category B as an asymptotic).** A39's heuristic functional F_k(a,u) = aK(u)/u + (1−a²)u/(ka), with K(u) = (π²/6 − Li2(e^{−2u}))/4, has interior critical point:
- e^{−2u/k} = Y, with Y^k + Y² = 1;
- max_a min_u F = c with c² = (1/k)·L(Y²), where L(x) = Li2(x) + ½ log x log(1−x).

*Derivation.*
- ∂_a F = 0 gives K = u²(1+a²)/(ka²), so F = 2u/(ka).
- ∂_u F = 0 gives K′(u) = 2u/k, that is 1 − e^{−2u} = e^{−4u/k}.
- Substituting and using L(x) + L(1−x) = π²/6 gives the formula.

This reproduces A39's c_exp for k = 3..15 to all printed digits (`analysis/growth.json`). Empirically log O_d = c√d − ½ log d + O(1) matches c_exp to about 7 digits for k = 1, 3, 7, 25 at d ≤ 4·10^5 (`analysis/growth_check.json`).

**Modularity test (Category B).**
- For weakly holomorphic or mock modular q-series of the usual kind, the leading exponent is 4π√(mn)/c with m rational, so c_exp²/π² ∈ Q.
- Here c_exp²/π² = 1/15 (k=1), 1/24 (k=2) and 1/40 (k=4) exactly: z = 1/φ², 1/2 and 1/φ, with L = π²/15, π²/12 and π²/10.
- For every other k ≤ 25, PSLQ finds no relation c² = (p/q)π² with coefficients ≤ 10^6 at 60 digits.
- This matches Zagier's rank-one list A ∈ {1/2, 1, 2}. g_k is not literally a Nahm sum; only its saddle equation has Nahm form.
- Conclusion (evidence, not proof): for odd k ≥ 3, neither g_k nor g_k(−q) = Σ ±(E_d − O_d)q^d is expected to be a theta function, a Hecke or quadratic-form theta series, an eta quotient, or a mock theta / Appell–Lerch object. Their growth constants are (numerically) not of modular type.

**Squares mod k.** The allowed set is forced by n² ≡ d (mod k) in the definition. The content of "OccFilt_k(∞) = squares" is that no allowed class vanishes eventually. No genus-character or quadratic-form structure was found or needed.

## 2. Uniform asymptotic (step 2)

**Category A.**
- c_k := (1 − Y^{k/2})/Y = √((1 − X)/(1 + X)), with X = Y^{k/2} = √(1 − Y²). The two forms agree by direct algebra.
- c_k < 1 for every k ≥ 1. Indeed c_k < 1 ⇔ Y + √(1−Y²) > 1, and (Y + √(1−Y²))² = 1 + 2Y√(1−Y²) > 1 for Y ∈ (0,1).
- As k → ∞, 1 − Y ~ W(k/2)/k, so 1 − c_k ~ √(2 log k / k).

**Mechanism (Category B heuristic, uniform in k).**
- The ladder A_{j}/A_{j−1} is 1/(1 − x^j) for odd j and 1/(1 + x^j) for even j.
- Along a chain step n → n+k (k odd), an even-to-odd step contains (k+1)/2 odd factors and (k−1)/2 even ones. The next step has the reverse counts.
- With x^j ≈ X frozen at the saddle, odd n therefore gain a relative factor √((1+X)/(1−X)) over the smooth interpolant, and even n lose the same factor.
- This gives E/O → c_k exactly.
- The smoothing error over a k-window at n ≍ √d is O(k/√d).
- Prediction: E_d/O_d = c_k + O_k(d^{−1/2}). Hence (−1)^d g_k(d) has eventual sign −1 on allowed d for every odd k.

**Evidence (exact integers).**
- At d ≈ 2·10^6 the exact E/O lies within 2.2·10^−4 (k=17) to 4.8·10^−4 (k=25) of c_k, in every class.
- The gap times √d grows roughly like k^{1.3}.
- The last allowed d with E_d ≥ O_d grows like about k^{3.7} (fit over k = 7..25; `analysis/summary.json`).

**What is not proved.** There is no k-uniform rigorous asymptotic. A proof would need a local limit theorem with error o(1 − c_k), uniform in k. The current R1 error δ ≈ 0.15–0.20 at N1 = 1500 is not of that size, and δ decreases empirically like N1^{−1/2}: 0.193 at N1 = 900 and 0.147 at N1 = 1500 (k = 17). A uniform η is impossible in principle, because 1 − c_k → 0.

## 3. k = 17, 19, 21, 23, 25 (step 3)

**Exact integer runs** (`exact/eo_ext.py`, a copy of A40's eo_indep.py with extra outputs; sign checked, signbad = 0). Allowed d ≤ 2·10^6:

| k | #zeros | last zero | last d with E_d ≥ O_d | last d with E_d > 0.8·O_d | E/O at d≈2·10^6 | c_k |
|---|---|---|---|---|---|---|
| 17 | 80 | 1137 | 22 628 | 39 984 | 0.634407 | 0.634192 |
| 19 | 89 | 766 | 30 344 | 53 599 | 0.645232 | 0.644974 |
| 21 | 88 | 2055 | 59 661 | 97 197 | 0.654856–0.654862 | 0.654556 |
| 23 | 105 | 837 | 78 453 | 127 582 | 0.663484–0.663540 | 0.663163 |
| 25 | 76 | 936 | 97 904 | 159 251 | 0.671270–0.671442 | 0.670962 |

**Modular zero certificate** (`cert/gcert.c`, a copy of A40's, run with primes 2^61−1 and 10^18+3).
- For each k, the allowed d ≤ 6·10^7 with g_k(d) ≡ 0 modulo both primes are exactly the exact zero lists above (`analysis/summary.json`, cert_match). The certificate was also run at 2·10^7.
- So every other allowed d ≤ 6·10^7 has g_k(d) ≠ 0 (Category A).
- Full zero lists are in `analysis/summary.json`.

**Parity Dominance proofs** (`proof/`).
- Blocks use `verify_blocks_k.py` and `blocks_k.py`, copies of the A39 files. They use the inherited R1 layer (`clt.py` and `sums.py`, sha256 1f4fa761… and c23705a0…, identical to A38/A39) at N1 = 1500.
- Tails use `tails_indep_A41.py`, a copy of A40's arb tail code with the closed-form Φ1. The only changes are file paths and an N1 parameter. R1 constants come from `r1_oracle_A41.py` (`r1_constants_N1500.json`).
- Outcome by cutoff:
  - At N1 = 900: k = 17 passes, with R = 0.9243798, η_t = 0.05, η = 0.0256 and D = 13 624 933. k = 19 fails, since R = 0.96300 and T > 0 for every admissible η_t ≤ 0.035. k = 21 fails, since R = 1.00222 > 1. This is the failure A39/A40 anticipated.
  - At N1 = 1500: all five pass with η_t = 10^−6, as in the Verdict table.
- Therefore, for k ∈ {17, 19, 21, 23, 25}, E_d ≤ (1 − η_k)O_d for all allowed d ≥ D_k. With the certificate, OccFilt_k(∞) = {squares mod k}.
- Status: computer-assisted, same caveats as A39 (inherited R1 audited once in A38; this k-range and N1 = 1500 are **not independently audited**). A39 code was used for the blocks and A40 code for the tails.

**Category B extrapolation.** At N1 = 1500, R_k rises by about 0.026 per step k → k+2, so the method should close up to about k ≈ 33. Beyond that it needs larger N1, which means D_k ∝ N1² and larger certificates. The method can be extended k by k but is not uniform.

**Preregistration outcome.**

| prediction | outcome |
|---|---|
| P1: all zeros < 2000, none in (2000, D_cert] | **failed for k = 21** (zero at 2055). Otherwise confirmed: no zero in (2055, 6·10^7] for k = 21, none in (2000, 6·10^7] for the others |
| P2: E/O within 3·10^−3 of c_k at top of range | confirmed (≤ 5·10^−4) |
| P3: last E ≥ O < 10^5 | confirmed (k = 25: 97 904, marginal) |
| P4: c²/π² rational only for k ∈ {1,2} among odd/even small k | refined: rational for k ∈ {1, 2, 4}; none for other k ≤ 25 |
| P5: c_k < 1 for all k; 1 − c_k ~ √(2 log k/k) | proved |
| P6: mod-4 classification | proved (§4) |

## 4. Mod 4 (step 4): Category A

**Proposition.** Let k = 2^a k′ with k′ odd and a ≥ 1, and let c be a square mod k. Every root r of r² ≡ c (mod k) has r ≡ c (mod 2). The class c is MIX if and only if a ≥ 2 and both c₂ := c mod 2^a and c₂ + 2^a are squares mod 2^{a+1}.

*Proof.*
- The sign of a term is (−1)^m with m = (d − n²)/k, which depends only on n² mod 2k (A39).
- By CRT, n² mod 2k = (n² mod 2^{a+1}, n² mod k′). The k′-part is fixed by c.
- Given n² ≡ c₂ (mod 2^a), n² mod 2^{a+1} ∈ {c₂, c₂ + 2^a}. Roots mod k combine freely from roots mod 2^a and mod k′.
- Case a = 1: n² mod 4 is determined by the parity of n, which is fixed by c. So the class is ONE.
- Case a ≥ 2: the class is MIX exactly when both lifts occur. ∎

**Corollaries.**
- k ≡ 2 (mod 4): every class is ONE, and the elementary Frobenius argument of A39 applies for every such k.
- k ≡ 0 (mod 4): MIX classes always exist.
  - a = 2: c₂ = 0, because 0 and 4 are both squares mod 8, while 5 is not.
  - a ≥ 3: every c with c₂ ≡ 1 (mod 8), because odd squares mod 2^{a+1} are exactly the residues ≡ 1 (mod 8).
- Brute-force check against the criterion for all even k ≤ 200 (`analysis/mod4.py`): k = 4: {0}; 8: {1}; 12: {0, 4}; 16: {0, 1, 9}; 20: {0, 4, 16}; 24: {1, 9}; …

**Structure of the obstruction.**
- If 4 | k and r is a root, then r + k/2 is a root, since (r + k/2)² − r² = rk + k²/4 ≡ 0 (mod k).
- The two have opposite sign exactly when r + k/4 is odd.
- So the two sign groups of a MIX class are the same smooth n-profile, sampled on two interleaved lattices offset by k/2. Each chain has constant sign, because n → n+k preserves n² mod 2k for even k.
- Their difference is a high-frequency (aliasing) remainder. That gives ratio → 1 and oscillation in √d, as observed in A39 (Category B for the oscillation).
- For odd k, by contrast, n → n+k flips the parity of n and hence the sign. The cancellation then takes place inside one chain and is governed by the systematic parity bias c_k < 1 of §2.
- This is why odd k is "PD", k ≡ 2 (mod 4) is cancellation-free, and k ≡ 0 (mod 4) carries a genuinely different and harder problem.

## 5. Category A summary (proved or exact certificate)

- Pairing identity for g_k(−q) with U_m ≥ 0, for all odd k.
- g_1 = f_0 and g_2 = φ. Watson's identity was checked to q^3000.
- The closed form c² = L(z_k)/k for the critical value of A39's saddle functional; c_k < 1 for all k; asymptotic size of 1 − c_k.
- Parity Dominance for k = 17, 19, 21, 23, 25, with the η_k and D_k above. This is computer-assisted and unaudited for these k.
- OccFilt_k(∞) = squares mod k for all odd k ≤ 25, with complete finite zero sets.
- ONE/MIX classification for every even k.

## 6. Conjectural / numerical (Category B)

- E_d/O_d → c_k for every odd k, with error O_k(d^{−1/2}).
- No modular, mock or theta representation for odd k ≥ 3 (based on irrational-looking growth constants).
- The k^{3.7} growth of the last E ≥ O.
- Extrapolation that the method closes up to k ≈ 33 at N1 = 1500.
- The MIX aliasing picture.
- Whether g_4 is a known mock theta function (its growth constant π²/40 is of modular type) was not settled.

## 7. Open

- An independent audit of the k = 17..25, N1 = 1500 runs.
- A rigorous k-uniform local limit theorem with error ≪ 1 − c_k. This is the missing ingredient for "all odd k".
- The MIX classes: a two-term asymptotic for interleaved chains.
- Identification of g_4.

## Files

- `prereg/`: prereg.md, prereg.sha256.
- `analysis/`: ck.py/txt, growth.py/json, growth_check.py/json, watson_k2.py, pairing.py, mod4.py/json, summarize.py, summary.json.
- `exact/`: eo_indep.py (A40 copy), eo_ext.py, run.sh, run2.sh, exact.log, exact2.log, eo_k*_D*.json. This includes eo_k1_D100000.json for k = 1.
- `cert/`: gcert.c (A40 copy), run.sh, z_k*_p*.txt (2·10^7), and `D6e7/` (6·10^7) with its cert.log.
- `proof/`: clt.py, sums.py, blocks_k.py, verify_blocks_k.py, tails_k.py, run_k.sh (A39 copies); saddle.py (range extended) and saddle.json; tails_indep_A41.py and r1_oracle_A41.py (A40 copies with path and N1 changes); out_k*_N{900,1500}.txt, blocks_k*_N*.json, tails_indep_k*_N*_eta*.json, r1_constants*.json.
- `SHA256SUMS`.

Resources: every job ran with nice, OMP_NUM_THREADS=1 and ulimit −v 3 GB. No jobs remain running.
