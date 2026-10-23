# A44: Independent audit of A41 (odd k = 17..25, pairing identity, growth constant, even-k MIX criterion, local-CLT layer)

Date: 2026-10-22 (CDT). Folder: `reports/s_family_paths/A44_oddk_audit/`. Only new files were written here. No existing file was modified and nothing was pushed. All jobs ran under nice, with OMP_NUM_THREADS=1 and `ulimit -v 3000000`. No jobs remain running.

Object, as in A38–A41: g_k(q) = Σ_{n≥0} q^{n²}/(−q^k;q^k)_n. Write a_n(m) = (−1)^m φ_n(m), where Σ_m φ_n(m)x^m = ∏_{j≤n}(1+x^j)^{−1}. For odd k, (−1)^d g_k(d) = E_d − O_d.

Independence rules:
- No A41 code was imported or executed.
- I reused A40's own code: `gcert.c`, `eo_indep.py`, `blocks_indep.py`, and `tails_indep.py` (the last adapted as `tails_A44.py`).
- **The local-CLT layer was rederived and reimplemented from scratch** (`proof/clt_indep.py`). It does not import `clt.py` or `sums.py`. It feeds every block and tail check below.
- The only A41 inputs are numbers under audit: the window parameters (UA, UB, ULO, UHI, A0), the constants α1 and α2 (used only after a safety check), and the zero lists to compare.

## Verdict table

| claim | verdict | notes |
|---|---|---|
| (a) Parity Dominance for k = 17, 19, 21, 23, 25 at N1 = 1500, with η_k = 0.16854 / 0.14240 / 0.11651 / 0.09094 / 0.06515 and D_k = 37 895 709 / 40 987 057 / 42 790 252 / 45 486 986 / 48 035 214 | **VERIFIED** (computer-assisted, Category A) | Blocks recomputed with independent R1 cells: R_k(A44) ≤ R_k(A41) for every k. Tails pass at η_t = 10^−6 with A41's D_k. |
| (a) two-prime certificate to 6·10^7; zero counts 80/89/88/105/76; last zeros 1137/766/2055/837/936 | **VERIFIED** | gcert rerun at D = 6·10^7 with both primes. The double-zero sets equal the exact zero sets (exact run to d ≤ 3·10^5) and A41's lists, element by element. |
| (b) pairing identity g_k(−q) = Σ U_m(1−q^{4m+1}−q^{(2m+1)k}) with U_m ≥ 0, all odd k | **VERIFIED** | Proof checked. Positivity is re-proved directly (see below). Exact check to q^2500 for every odd k ≤ 25. |
| (c) c_exp(k)² = L(z)/k with 1−z = z^{k/2}; c_k < 1 for all k; 1 − c_k ~ √(2 log k/k) | **VERIFIED**, with one minor GAP | GAP: A41 proves only that the *critical value* of F_k equals L(z)/k. That this critical point is the max–min is not proved (A41 §1, "Growth constant"). It agrees numerically with a direct max–min to 20 digits for 13 values of k. The other two statements are proved. |
| (d) even-k MIX criterion | **VERIFIED** | Proof checked. Brute force for all even k ≤ 400: 0 mismatches. |
| shared local-CLT layer `clt.py` / `sums.py` (R1) | **VERIFIED** | Rederived from first principles (below), and independently reimplemented with different minor-arc bounds. The new code gives δ and S_lo on the same cells that are slightly *better* than `clt.py`'s, so `clt.py`'s outputs are consistent with valid bounds. |

No FAIL was found. No bug changes a verdict.

## 1. Local-CLT layer (R1): first-principles derivation

**Model identity.** ∏_{j≤n} 1/(1+(−x)^j) = ∏_{odd j≤n}(1+x^j) · ∏_{n/2<k≤n} 1/(1−x^{2k}).
- Proof: use 1/(1−x^j) = (1+x^j)/(1−x^{2j}) for odd j and 1/(1+x^{2i}) = (1−x^{2i})/(1−x^{4i}). Then ∏_{i≤n/2}(1−x^{2i}) divided by ∏_{l≤n}(1−x^{2l}) leaves ∏_{n/2<l≤n}(1−x^{2l})^{−1}.
- The identity also gives a_n(m) ≥ 0 directly.
- Checked exactly for n ≤ 60, to x^3000 (`proof/check_model.py`).

**Probability model.** Tilt at r = e^{−u/n}. Then S = Σ B_j + Σ G_k, where:
- B_j ∈ {0, j}, with p_j = 1/(1+e^{ju/n});
- G_k = 2k·Geom(w_k), with w_k = e^{−2ku/n}.

So P(S=m) = a_n(m) r^m / A_n(r). This is exactly `clt.py`'s model.

**Inversion.** |P(S=m) − g(m−μ)| ≤ (2π)^{−1}[∫_{|θ|≤θ0}|φ−e^{−σ²θ²/2}| + ∫_{|θ|>θ0}e^{−σ²θ²/2} + ∫_{θ0<|θ|≤π}|φ|]. Multiplying by √(2π)σ gives δ = D1 + D2 + D3.

**D1 (major arc).** Put ψ = log φ (centred). Then |ψ − (−σ²θ²/2)| ≤ K3|θ|³/6 with K3 ≥ sup|ψ'''|.
- Bernoulli part: ψ_j''' = (ij)³ q(1−q)(1−2q), with q = pe^{ix}/D and D = 1−p+pe^{ix}.
- |D|² − cos²(x/2) = (1−cos x)(½ − 2p(1−p)) ≥ 0, so |D| ≥ cos(x/2).
- |1−p−pe^{ix}| ≤ (1−2p) + p|x|.
- So |ψ_j'''| ≤ j³[p(1−p)(1−2p) + j θ0 p²(1−p)]/cos³(τ0/2).
- This matches `k3 = (ΣF3 + τ0 ΣF4)/c3`. The F4 sum correctly carries j⁴ (p = 4).
- Geometric part: |ψ'''| ≤ (2k)³ w(1+w)/(1−w)³. This is `8·G3` (no cosine factor is needed).
- If K3θ0 ≤ 1.5σ² (asserted in interval arithmetic), then |R| ≤ σ²θ²/4. Hence |e^R − 1| ≤ |R|e^{|R|}.
- Using ∫|θ|³e^{−σ²θ²/4} = 16/σ⁴, this gives D1 = 4√(2π)K3/(3πσ³) = 4√(2π)k3/(3π S^{3/2}√n). This is exactly the code's formula.

**D2.** D2 = erfc(σθ0/√2) ≤ e^{−z²}/(z√π), with z = τ0√(S n/2). This is exact as coded. It decreases in n, and S_lo is used.

**D3 (minor arcs).**
- Bernoulli: −log|φ_j| = −½log(1 − 2v(1−cos jθ)) ≥ v_j(1−cos jθ).
- Geometric: −log|φ_G| = ½log(1+λ_k sin²(kθ)), with λ = 4w/(1−w)².
- I checked every step of `minor_terms`:
  - the closed forms Σ_{odd j≤n}cos jθ = sin(2Nθ)/(2 sin θ) and Σ_{k=K1}^n cos 2kθ = [sin((2n+1)θ) − sin((2K1−1)θ)]/(2 sin θ);
  - the parity cases (N/n, L/n, 2Nθ, (2K1−1)θ);
  - n sin θ = τ·sinc(τ/n), with sinc ≥ 1 − z²/6;
  - the chord bound for log(1+λx), and 1−cos x ≥ x²/2 − x⁴/24 and sin²x ≥ x² − x⁴/3;
  - the monotonicity of v and λ in z, and b2 with n sin θ ≥ T(1−T²/6n²);
  - region 3, using cos(j(π−φ)) = −cos(jφ) for odd j;
  - the monotone-in-n conditions (n·b ≥ ½ or 1.5);
  - the prefactor √(2π)σ/π, with S_hi.
- All are correct.

**Sum lemma (`sums.py`).**
- Odd j are midpoints of [j−1, j+1], which tile [0, 2N] with 2N ∈ {n, n+1}. This gives |Σ − ½∫_0^n f| ≤ TV_{[0,n+1]} + ½ sup.
- For the integer sum: K1 − ½ − n/2 ∈ {0, ½}, which gives TV + sup.
- Scaling x = ny gives error (TV_y + c·sup_y)/n ≤ (…)/n1, since the y-integrand does not depend on n.
- Derivatives F′ for Fv, Fp, F3, F4, Gh, G3, Gm were all rechecked symbolically.
- `oddsum` and `intsum` are conservative versions of the same tiling argument.
- **Verdict: correct.**

**Independent implementation** (`proof/clt_indep.py`, python-flint arb):
- It uses the same D1/D2 lemmas.
- Its sum lemma has its own code, with Q = 1000.
- D3 uses *different* bounds:
  - Small τ: a Taylor bound driven by the variance sums themselves, together with a λ-uniform chord.
  - τ ≥ 1, the bulk arc and region 3: a new Abel-summation lemma, Σ_{odd j} v_j(1−cos jθ) ≥ Σ_{odd j ≥ 1/|sin θ|+1} v_j. It holds because v_j is nonincreasing and the partial sums C_i ≥ max(0, i − 1/(2|sin θ|)). It is then followed by ≥ ½∫_Y^1 v(u_h y)dy, with Y = 1/(n sin θ) + 3/n.
- Cells of width 0.01 on u ∈ [0.40, 2.60], valid for all n ≥ 1475 (≤ N1 − k for every k ≤ 25): every cell has mono_ok, max δ = 0.1634, max D3 = 1.2·10^−12, max D2 = 1.3·10^−15.
- Comparison with A41's `clt.py` cells (k = 17, n ≥ 1483; `proof/cmp_cells.py`):

| u-cell | 0.41 | 0.91 | 1.41 | 1.91 | 2.16 |
|---|---|---|---|---|---|
| δ, clt.py | 0.08806 | 0.09388 | 0.10875 | 0.13102 | 0.14314 |
| δ, A44 | 0.08725 | 0.09292 | 0.10752 | 0.12932 | 0.14116 |

- Non-rigorous sanity check (`proof/sanity_clt.py`, FFT of the exact distribution): at n = 1475, u = 0.875 the true relative error is 0.0194, against a certified δ of 0.0923. σ²/n³ and μ/n² lie inside the certified [S_lo, S_hi] and [M_lo, M_hi]. At a second point, n = 1500 and u = 2.2, the true error is 0.0280 against a certified δ of 0.1420, and again σ²/n³ and μ/n² lie inside the certified intervals.

**CLT-layer verdict: VERIFIED.** The R1 layer is now audited from first principles, and its role in A39–A41 no longer rests on inheritance.

## 2. Claim (a): Parity Dominance, k = 17..25

**Blocks.** A40's `blocks_indep.py` was run unchanged with A44's own cells (`proof/cells_k*.json`), at H = 0.0025 and N1 = 1500.

| k | 17 | 19 | 21 | 23 | 25 |
|---|---|---|---|---|---|
| R_k, A41 | 0.8314560 | 0.8575917 | 0.8834878 | 0.9090546 | 0.9348480 |
| R_k, A44 (independent R1) | 0.8305747 | 0.8570024 | 0.8826329 | 0.9080564 | 0.9340278 |
| min odd-side factor (> 0) | 0.8245 | 0.8178 | 0.8100 | 0.8036 | 0.7962 |

**Tails.** `proof/tails_A44.py` is A40's tails code with N1 = 1500, A44 R1 constants, A44 cells, and S_hi from 35 sub-cells.
- Mode `a41` uses A41's α1 and α2. It first asserts that they are safe: α1(A41) ≥ α1(own) and α2(A41) ≤ α2(own). This holds because A44's M_lo(UA) is larger and its M_hi(UB) smaller.
- Mode `own` uses A44's own α1 and α2.

| k | 17 | 19 | 21 | 23 | 25 |
|---|---|---|---|---|---|
| D0 (a41 mode) = A41 D_k | 37 895 709 | 40 987 057 | 42 790 252 | 45 486 986 | 48 035 214 |
| T(D0), η_t = 10^−6, a41 mode | −15.29 | −15.81 | −10.29 | −7.51 | −7.76 |
| D0 (own mode) | 37 967 772 | 41 065 767 | 42 873 463 | 45 576 183 | 48 130 147 |
| T(D0), own mode | −15.35 | −16.38 | −10.82 | −8.52 | −7.82 |

In every run: u* bracket ok, monotone ok, δ_central ≤ 0.1005 < 0.2, n* ≥ N1.

**Conclusion (Category A, computer-assisted).** For k ∈ {17, 19, 21, 23, 25} and every allowed d ≥ D_k, E_d ≤ (1 − η_k)O_d, with η_k = 1 − R_k(A41) − 10^−6 truncated = 0.16854, 0.14240, 0.11651, 0.09094, 0.06515. All five truncations were checked. The bound holds a fortiori, because R_k(A44) ≤ R_k(A41).

**Finite range.**
- gcert (A40 copy) at D = 6·10^7 > max D_k, primes 2^61−1 and 10^18+3.
- The allowed d with g_k(d) ≡ 0 modulo both primes are exactly the exact zero sets from `exact/eo_indep.py` (d ≤ 3·10^5, signbad = 0). They also equal A41's lists element by element (`cert/compare.json`).
- Counts 80/89/88/105/76; last zeros 1137/766/2055/837/936.
- So OccFilt_k(∞) = {squares mod k} for k = 17..25, and the zero sets are complete.

The exact side checks also reproduce A41's last d with E_d ≥ O_d: 22 628, 30 344, 59 661, 78 453, 97 904.

## 3. Claim (b): pairing identity

- For odd k, (−(−q)^k; (−q)^k)_n = ∏_{i≤n}(1+(−q^k)^i) = P_n, and (−q)^{n²} = (−1)^n q^{n²}.
- T_{2m+1}/T_{2m} = −q^{4m+1}/(1 − q^{(2m+1)k}). Adding T_{2m} and T_{2m+1} gives U_m(1 − q^{4m+1} − q^{(2m+1)k}). Correct.
- Positivity: 1/P_{2m}(q) = A_{2m}(q^k), and the model identity of §1 writes A_n as ∏(1+x^j)·∏(1−x^{2k})^{−1}. This is coefficientwise ≥ 0, which is a self-contained proof that does not need A39's lemma.
- Exact integer check of the identity and of U_m ≥ 0 to q^2500 for all odd k ≤ 25 (`analysis/pairing_check.py`).
- Remark: the link "the bracket vanishes on Y^k + Y² = 1" is heuristic (Category B), as A41 presents it.

## 4. Claim (c): growth constant

- Φ1 = K/u, since Li2(x) + Li2(−x) = ½Li2(x²). So A41's F_k is A40's tail functional.
- ∂_aF = 0 gives K = u²(1+a²)/(ka²), and then F = 2u/(ka).
- ∂_uF = 0 then gives K′ = 2u/k, and K′ = −½log(1−e^{−2u}). So 1 − e^{−2u} = e^{−4u/k}, that is Y^k + Y² = 1 with Y = e^{−2u/k}.
- c² = 4(K − u²/k)/k, and 4K − 4u²/k = L(1−e^{−2u}) by L(x) + L(1−x) = π²/6. With z = Y² = 1 − e^{−2u} this gives 1 − z = z^{k/2} and c² = L(z)/k. Correct.
- c_k < 1 for all k: correct. The root Y ∈ (0,1) is unique, and (Y + √(1−Y²))² = 1 + 2Y√(1−Y²) > 1.
- 1 − c_k ~ X = √(1−Y²) ~ √(2W(k/2)/k) ~ √(2 log k/k): correct. The ratio converges slowly: 0.706, 0.833, 0.880, 0.947 at k = 10², 10⁴, 10⁶, 10^18 (`analysis/growth_asym.json`).
- The closed form equals a direct numerical max_a min_u F to 20 digits for k = 1, 2, 3, 4, 5, 7, 9, 15, 17, 19, 21, 23, 25 (`analysis/growth_check.txt`).
- c²/π² = 1/15, 1/24, 1/40 for k = 1, 2, 4.
- c_k(17..25) = 0.634192, 0.644974, 0.654556, 0.663163, 0.670962, matching A41.
- **GAP (minor, location: A41 §1 "Growth constant", the sentence "max_a min_u F = c").** Only the critical-point value is derived. That it is the max–min (and equals A39's c_exp) is supported numerically, not proved. The Category A label should be limited to "critical value of F_k".

## 5. Claim (d): even-k MIX criterion

- The sign (−1)^{(d−n²)/k} depends only on n² mod 2k.
- By CRT, n² mod 2k is determined by n² mod 2^{a+1} and n² mod k′, and the k′-part is fixed by c.
- The two possible lifts are c₂ and c₂ + 2^a mod 2^{a+1}. Square roots mod 2^{a+1} combine freely with roots mod k′.
- So the class is MIX iff both lifts are squares mod 2^{a+1}. The condition "a ≥ 2" is automatic: for a = 1, 2 and 3 are non-squares mod 4.
- r ≡ c (mod 2) is correct.
- Corollaries:
  - a = 2 gives c₂ = 0; for a ≥ 3, every c₂ ≡ 1 (mod 8) is MIX.
  - r + k/2 is again a root, with the opposite sign iff r + k/4 is odd, because (r + k/2)² − r² = k(r + k/4).
  - Chains n → n + k have constant sign: 2nk + k² ≡ 0 (mod 2k).
- Brute force for even k ≤ 400 against the criterion: 0 mismatches. k ≡ 2 (mod 4) has no MIX class, and k ≡ 0 (mod 4) always has one. The listed examples (4: {0}, 8: {1}, 12: {0,4}, 16: {0,1,9}, 20: {0,4,16}, 24: {1,9}) are reproduced (`analysis/mod4_check.json`).
- **VERIFIED.**

## 6. Bugs and defects (none changes a verdict)

- **C1 (claim scope, A41 §1).** The "max_a min_u F = c" identification is not proved; see §4.
- **C2 (stale doc, inherited).** The `verify_blocks_k.py` docstring says "for n ≥ N1−7", but the code uses N1−K, which is correct.
- **C3 (cosmetic, clt.py).** The arguments `P` in `constants` and `delta_bound` are unused. `S_hi` over a wide u-window is a single interval evaluation (valid but loose). A44's 35-sub-cell S_hi is smaller: 0.9742 vs 0.9829 for k = 17.
- **C4 (status line, A41 Verdict 4 and §5).** "Not independently audited" is now superseded for k = 17..25 at N1 = 1500 and for the R1 layer.
- **C5 (not audited here).** The N1 = 900 runs (the k = 17 pass with D = 13 624 933, and the k = 19, 21 failures) and the E/O values at d ≈ 2·10^6 were not re-run. Exact runs here went to d ≤ 3·10^5. None of these enters a proved claim.

## Category A (proved) after this audit

- R1 local-CLT layer: rederived and independently reimplemented.
- PD for k = 17, 19, 21, 23, 25 with the η_k and D_k above (computer-assisted). Complete finite zero sets; OccFilt_k(∞) = squares mod k.
- The pairing identity with U_m ≥ 0, for all odd k.
- The critical value of F_k equals L(z)/k. c_k < 1 for all k, and 1 − c_k ~ √(2 log k/k).
- The ONE/MIX criterion for all even k.

The following remain Category B, as A41 itself marks them: E/O → c_k, the max–min identification (numerical), the modularity heuristics, the k^{3.7} growth, and the k ≈ 33 extrapolation.

## Files

- `proof/`: clt_indep.py, check_model.py, cmp_cells.py, make_cells.py, cells_k*.json, r1_constants_A44.json, shi.py, S_hi_fine.json, blocks_indep.py (A40 copy), run_blocks.sh, blocks_k*.log, blocks_indep_k*.json, tails_A44.py, tails_k*_{a41,own}_eta1e-6.json, sanity_clt.py, sanity.log.
- `cert/`: gcert.c (A40 copy), run.sh, cert.log, z_k*_p*.txt, compare.py, compare.json.
- `exact/`: eo_indep.py (A40 copy), run.sh, exact.log, eo_k*_D300000.json.
- `analysis/`: pairing_check.py/json, mod4_check.py/json, growth_check.py/txt, growth_asym.json.
- `mk_pdf.py`, `REPORT.md`, `REPORT.pdf`.
