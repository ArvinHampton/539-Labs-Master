# A56: independent audit of A49 (g_k family: Parity Dominance for k = 27, 29; new proved zeros; preregistration and T-jump)

Date: 2026-10-22 (America/Chicago, CDT). Auditor: Grok Bot, for Arvin Hampton. All paths are under `reports/s_family_paths/A56_A49_audit/` (the audit directory) unless stated. Only files inside the audit directory were created. Nothing in `A49_gk_runs/`, `A41*`, `A44*` or elsewhere was modified.

## 0. Verdicts

| item | claim of A49 | A56 verdict |
|---|---|---|
| 1a | Parity Dominance (PD) for k = 27 at N1 = 1500, η₂₇ = 0.03836, D₂₇ = 49 340 462, #Z₂₇ = 68, max Z₂₇ = 1375 | **VERIFIED** (computer-assisted, Category A in the same sense as A41/A44) |
| 1b | PD for k = 29 at N1 = 1500, η₂₉ = 0.01191, D₂₉ = 51 587 220, #Z₂₉ = 121, max Z₂₉ = 1934 | **VERIFIED WITH CAVEATS** (caveats in §1.7: thin block margin that rests on the local-CLT constants, and the tail "margin" −0.057/−0.119 is a ball-arithmetic artefact; the true tail margin is about −27) |
| 1c | R_k for k = 3..15 as listed | **CONFIRMED** (my R_k are lower by 0.0017–0.0032 for k ≤ 15, so A49's values are valid, slightly conservative upper bounds) |
| 1d | k = 31, 33 "fail" at N1 = 1500 | **CONFIRMED only at the strength of the A41/A44 local-CLT layer** (R = 1.0097/1.0377 in my replication, 1.0155/1.0436 in A49). With my own sharper local-CLT layer the block ratio and the tail inequality **pass** for k = 31, 33 (R = 0.882, 0.905). So "fails" is a limitation of constants, not a property of the method. The finite certificate for k = 31, 33 was not run, so this is not a proof of PD for 31, 33. |
| 2 | g_k(k²+2k+4) = 0 (k ≡ 3 mod 4), g_k(k²+3k+4) = 0 (k ≡ 1 mod 4), odd prime powers k ≥ 9 | **VERIFIED**: proof re-derived, exact test of all 320 odd prime powers 9 ≤ k ≤ 1999 (254 of them ≤ 1501): 0 failures. Fails at k = 3, 5, 7 as predicted; composites: only k = 15 vanishes; opposite class gives ±1. |
| 3a | prereg sha256 and timeline | **VERIFIED** (sha256 equal; prereg mtime 18:00:41 CDT; all code copies 18:00:20; first run output 18:00:49.85). Caveat: file mtimes on one machine are self-attested, with no external timestamp. |
| 3b | L* scoring (prime half 5/5 for k = 61..79 etc.) | **VERIFIED** (primary, recomputed from my own exact runs; secondary re-run for all odd k ≤ 999). One small count discrepancy (k = 21 dropped), §4.4. |
| 3c | T-jump at k = 67 (ρ 23.848 → 27.242, T(67) = 3 331 509) | **VERIFIED**: all ten T(k), k = 61..79 odd, reproduced exactly by two independent programs. |

Discrepancies found (none changes a verdict): §5.

## 1. Item 1: Parity Dominance for k = 27 and k = 29

### 1.1 What is claimed and what I re-derived

For odd k put g_k(d) = Σ_{n≥0, n²≤d, k | d−n²} φ_n((d−n²)/k), φ_n(m) = [x^m] ∏_{i=1}^n 1/(1+x^i), and a_n(m) = (−1)^m φ_n(m). I derived from scratch:

* a_n(m) ≥ 0, with generating function A_n(x) = Σ_m a_n(m)x^m = ∏_{j≤n} 1/(1+(−x)^j) = ∏_{j odd ≤ n}(1+x^j) · ∏_{n/2<l≤n}(1−x^{2l})^{−1}. (Use 1/(1−x^j) = (1+x^j)/(1−x^{2j}) for odd j and 1/(1+x^j) = (1−x^j)/(1−x^{2j}) for even j; the even numerators cancel the first n/2 denominators.) So A_n is the generating function of a sum of independent pieces: Bernoulli j for odd j ≤ n, and 2l·Geometric for n/2 < l ≤ n. This gives a probabilistic model: with tilt r = e^{−u/n}, S = Σ_{j odd} j·B_j + Σ_l 2l·N_l, P(B_j=1) = 1/(1+e^{ju/n}), N_l geometric with ratio w_l = e^{−2lu/n}, and a_n(m) r^m / A_n(r) = P(S = m).
* For odd k and d = n² + km, (−1)^d = (−1)^{n+m}, hence (−1)^d g_k(d) = E_d − O_d, with E_d = Σ_{n even} a_n(m_n), O_d = Σ_{n odd} a_n(m_n) (all terms ≥ 0). Parity Dominance means E_d ≤ (1−η_k)O_d for allowed d ≥ D_k, so E_d < O_d and (−1)^d g_k(d) < 0; in particular g_k(d) ≠ 0.
* Allowed d: d mod k is a square mod k, so that some n has k | d − n².

### 1.2 The three ingredients (own derivations)

**Block step.** For even n ≥ N1 the two odd partners n ± k (odd, because k is odd) lie in the same square class, with m_± = m_n ∓ 2n − k ≥ 0. Writing a_n(m) = A_n(r) r^{−m} P_n(S=m) and choosing the base tilt r = e^{−u/n} with μ_n(r) = m_n, one gets

e_n / ½(o_{n−k} + o_{n+k}) ≤ R := (1+δ) / [ ½ Σ_{±} ρ_i (1 − x_i²/(2σ_i²) − δ) ],  ρ_i = (A_{n_i}/A_n)(r) · r^{(n_i²−n²)/k} · σ_n/σ_i,

where x_i = m_i − μ_i(r), and δ is the local-CLT error (§1.3), used in the form P_n ≤ (1+δ)/(√(2π)σ_n) and P_i ≥ (e^{−x²/2σ²} − δ)/(√(2π)σ_i) ≥ (1 − x²/2σ² − δ)/(√(2π)σ_i). Each odd term is used at most twice with weight ½, so Σ_n ½(o_{n−k}+o_{n+k}) ≤ O_d. All of A_{n_i}/A_n, r-powers, σ ratios and x_i²/σ_i² are enclosed over a box of u of width 0.0025 and over s = 1/n ∈ [0, 1/N1] (my code `proof/blocks56.py`, endpoint interval class `proof/iv56.py` on top of 128-bit python-flint balls). R_k is the maximum over boxes with u ∈ [UA, UB] (windows UA = round(0.5u₀,2), UB = round(2.6u₀,2) with y^k + y² = 1, u₀ = −(k/2) ln y; this is the A39/A41 window rule, used so the same inequalities are audited).

**Tail step.** For even n with α = n/√d ≤ α₁ or ≥ α₂ the terms are bounded by Chernoff, a_n(m) ≤ A_n(r) r^{−m}, with m = (d−n²)/k = n²ρ(α), ρ = (1/α²−1)/k. Upper estimate log A_n(e^{−u/n}) ≤ nΦ₁(u) + log 2 + g(u), g(u) = −log(1−e^{−u}); lower estimate log A_n ≥ nΦ₁(u) − ½ log 2 − g(u), where Φ₁(u) = [Li₂(−e^{−u}) + π²/12 + Li₂(e^{−u}) − Li₂(e^{−2u})]/(2u) (I checked the closed form against quadrature to 1e-25). Both come from comparing the Riemann sums over odd j and over n/2 < l ≤ n with integrals using total variation (each odd j is the midpoint of [j−1, j+1]). Hence log e_n ≤ √d·F(α,u) + log 2 + g(u) for every u > 0, with F(α,u) = αΦ₁(u) + (1−α²)u/(kα). **F is convex in α** (∂²F/∂α² = 2u/(kα³) > 0), so a supremum over an α-interval is attained at an endpoint. The central odd term o* near the saddle (α*, u*) is bounded below by √d·F(α*,u*) − C* with C* from the local CLT at the saddle. The tail requirement is T(D) = log√D + log 2 + max(√D·gap + g) + C* − log η_t ≤ 0, η_t = 1e−6, gap = (tail exponent) − F*, monotone in D when gap ≤ −2.5/√D (tiny-α part, α ≤ 0.005, by 1 − e^{−x} ≥ x e^{−x/2}: gap ≤ −4.5/√D). D_k = ⌈(N1/α₁)²⌉ with α₁ = 1/√(1 + k M_lo(UA)); α₂ from M_hi(UB). Then E_d ≤ (R + η_t)O_d, so η_k = 1 − R_k − η_t.

**Why the A49 tail margin looks marginal.** In ball arithmetic in α, √D·(ball width) is about 7·10³ × 0.004, i.e. a loss of ≈ 27 in T. Since F is convex the exact endpoint evaluation has no such loss. My tight mode gives T(29) = −26.9; a non-rigorous floating-point check of the true Chernoff exponent (`proof/check_tailgap.py`) gives gap(α₁) = −0.00908 and gap(α₂) = −0.0286 (so √D·gap ≈ −65 and −205), and the tail ratio is about e^{−27}·η_t. The inequality is robust; the quoted −0.057/−0.119 are not the true margin.

### 1.3 Local-CLT layer, from first principles (`proof/clt56.py`)

Claim, for every u-cell [ua, ub] of width 0.01 and **every n ≥ n₀ = 1467**: |√(2π)σ P(S=m) − e^{−(m−μ)²/(2σ²)}| ≤ δ for all integers m, and σ²/n³ ∈ [S_lo, S_hi], μ/n² ∈ [M_lo, M_hi].

Proof structure: P(S=m) = (1/2π)∫_{−π}^{π} φ(θ)e^{−iθm}dθ and the Gaussian is the Fourier inverse of e^{−σ²θ²/2}; δ = D1 + D2 + D3.

* D1 (Taylor, |θ| ≤ θ₀ = τ₀/n): log φ(θ) = iμθ − σ²θ²/2 + R(θ), |R| ≤ K₃|θ|³/6 where K₃ ≥ sup|(log φ)'''|. With K₃θ₀ ≤ cσ² one has |e^R − 1| ≤ |R|e^{|R|}, so the integral of |φ e^{−iμθ} − e^{−σ²θ²/2}| is at most K₃/(6a²) with a = σ²(½ − c/6), hence D1 = K₃ / (6√(2π) σ³ (½ − c/6)²). Both K₃ and σ³ are enclosed through Riemann-sum lemmas with arb balls (one bound for all n ≥ n₀ and the whole cell, `sumenc`); K₃ uses third derivatives of log(1−p+pe^{ix}) and log(1−we^{iy}), with a cosine denominator controlling the complex shift. I checked numerically (`proof/check_K3.py`) that the sup of |(log φ)'''| is at θ = 0 and that my bound exceeds it by 1–15 % (for τ₀ ≤ 1).
* D2 (Gaussian tail beyond θ₀): ∫_{|θ|>θ₀} e^{−σ²θ²/2} ≤ erfc bound.
* D3 (θ₀ ≤ |θ| ≤ π), D3 = DA + DB + DC: |φ| bounds from |1−p+pe^{ix}|² = 1 − 2p(1−p)(1−cos x), so log|·| ≤ −v(1−cos x) with v = p(1−p), and |φ_G|² = 1/(1 + λ sin²(lθ)), λ = 4w/(1−w)². Region A, τ = nθ ∈ [τ₀, 1.5]: on small τ-cells, lower bounds of the exponent by its low-order Taylor terms (monotone check that n₀·b ≥ ½), integrated cell by cell; region B, θ ∈ [1.5/n, π − 1.5/n]: Abel summation, Σ_{odd j} v_j(1−cos jθ) ≥ Σ_{odd j ≥ 1/|sin θ|+1} v_j, bounded below by an integral; region C, θ near π: Σ_{odd j} v_j(1+cos jφ) ≥ Σ_{odd j ≤ n/2} v_j, again an integral.

Two modes: `c15` uses the textbook choice K₃θ₀ ≤ (3/2)σ² (τ₀ = min(1, 0.99·1.5·S_lo/κ); cell δ ≈ 0.09–0.14, comparable to A41/A44) and `sharp` optimises τ₀ per cell (δ ≈ 0.03–0.087). 312 cells cover u ∈ [0.19, 3.31].

Numerical sanity checks (not part of the proof; `proof/sanity56_clt.py`, exact distribution of S by FFT of the characteristic function) of true max error against the certified δ:

| n | u | true max error | certified δ (c15) | certified δ (sharp) |
|---|---|---|---|---|
| 1468 | 0.65 | 0.01851 | 0.08746 | 0.02846 |
| 1467 | 0.9 | 0.01957 | 0.09165 | 0.03045 |
| 2000 | 1.0 | 0.01715 | 0.08033 | 0.02594 |
| 1467 | 1.5 | 0.02313 | 0.10976 | 0.03678 |
| 1500 | 2.6 | 0.03104 | 0.11738 | 0.05408 |
| 1501 | 3.2 | 0.03535 | 0.12667 | 0.07115 |

In every case the true error is below the certified δ and σ²/n³, μ/n² lie inside the enclosures. (Six cases completed; a seventh, n = 3000, u = 2.0, was stopped for time. Raw output: `proof/sanity56_clt.out`, which has interleaved lines from parallel jobs.)

### 1.4 Results (own pipeline, N1 = 1500, η_t = 1e−6)

Three variants, all my code: FAITH = my cells with the c15 constants, A41/A44 conventions for the block step (s ≤ 1/(N1−k)) and ball-in-α evaluation of the tails; TIGHT = same cells, exact derivation bounds (s ≤ 1/N1) and endpoint (convex) tails; SHARP = sharp cells, TIGHT conventions. Window parameters, saddle (α*, u*) and constants were recomputed (`proof/params56.py`; k = 29: α* = 0.3229999, u* = 1.016816, F* = 0.2171060).

| k | A49 R | A49 η | R FAITH | η FAITH | T FAITH | R TIGHT | T TIGHT | R SHARP | η SHARP | T SHARP | D₀ (mine) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 0.5696327 | 0.43036 | 0.56788 | 0.43211 | −59.21 | 0.56788 | −69.20 | 0.50778 | 0.49222 | −69.25 | 16 669 607 |
| 5 | 0.6308769 | 0.36912 | 0.62895 | 0.37104 | −42.61 | 0.62893 | −54.12 | 0.56012 | 0.43988 | −54.18 | 20 382 618 |
| 7 | 0.6766216 | 0.32337 | 0.67444 | 0.32556 | −37.53 | 0.67438 | −49.54 | 0.59896 | 0.40104 | −49.60 | 23 916 479 |
| 9 | 0.7141402 | 0.28585 | 0.71171 | 0.28828 | −32.12 | 0.71160 | −47.15 | 0.63113 | 0.36887 | −47.21 | 27 265 747 |
| 11 | 0.7470252 | 0.25297 | 0.74434 | 0.25565 | −31.52 | 0.74415 | −48.60 | 0.66013 | 0.33986 | −48.67 | 30 835 058 |
| 13 | 0.7768933 | 0.2231 | 0.77397 | 0.22603 | −23.91 | 0.77367 | −40.78 | 0.68671 | 0.31328 | −40.85 | 32 963 377 |
| 15 | 0.8049517 | 0.19504 | 0.80177 | 0.19822 | −20.31 | 0.80133 | −38.51 | 0.70985 | 0.29014 | −38.58 | 35 620 105 |
| 17 | n/a | | 0.82802 | 0.17198 | −15.34 | 0.82739 | −35.34 | 0.73164 | 0.26836 | −35.41 | 37 947 145 |
| 19 | n/a | | 0.85389 | 0.14610 | −16.37 | 0.85303 | −36.80 | 0.75292 | 0.24707 | −36.87 | 41 043 238 |
| 21 | n/a | | 0.87951 | 0.12049 | −10.80 | 0.87836 | −32.49 | 0.77408 | 0.22591 | −32.55 | 42 849 645 |
| 23 | n/a | | 0.90479 | 0.09521 | −8.23 | 0.90330 | −32.68 | 0.79500 | 0.20499 | −32.75 | 45 550 651 |
| 25 | n/a | | 0.93028 | 0.06972 | −7.81 | 0.92839 | −32.49 | 0.81608 | 0.18391 | −32.56 | 48 102 974 |
| **27** | 0.9616335 | 0.03836 | **0.95675** | **0.04325** | **−1.57** | 0.95437 | −27.55 | 0.83798 | 0.16202 | −27.62 | 49 312 289 |
| **29** | 0.9880828 | 0.01191 | **0.98287** | **0.01712** | **−0.10** | 0.97993 | −26.87 | 0.85970 | 0.14029 | −26.95 | 51 557 554 |
| 31 | 1.0154648 | none | 1.00966 | none (R4 fails: T = +2.90) | +2.90 | 1.00607 | −26.02 | 0.88196 | 0.11803 | −26.10 | 53 684 094 |
| 33 | 1.0436421 | none | 1.03772 | none (T = +4.57) | +4.57 | 1.03339 | −24.98 | 0.90522 | 0.09478 | −25.05 | 55 698 896 |

(η = 1 − R − 1e−6 truncated at 5 decimals. For k = 31, 33 FAITH and TIGHT have R > 1, so no η exists; SHARP has R < 1. All monotonicity and u*-bracket checks passed in every variant for every k; see `proof/pd56_results.json`.)

**Reading.** My FAITH R_k is below A49's R_k for every k (differences 0.0017–0.0058, growing with k), because A49 takes the maximum of two pipelines (and A41 uses a looser s-bound). So A49's listed η_k (k = 3..15, 27, 29) are valid and mildly conservative; my FAITH η₂₉ = 0.01712 against A49's 0.01191.

**Replication on A49's own cell files** (data only, my block/tail code; `proof/replicate56.py`, `logs/replicate56.log`). Using A49's A41 cells my block code gives A49's R_k to 1e−7 for every k = 5..33 (k = 29: 0.9880828200 vs 0.9880828200, difference 3e−16; k = 3 differs by 4e−5, caused by A49's box edge 0.48750000000000004 being one ulp wide, which pulls in a neighbouring cell). Using A49's A44 cells my R_k is lower by 1e−4 to 2.5e−3, as expected for conservative conventions. My tail code, run at A49's D_k, gives T = −0.1185 (k = 29; A49's independent pipeline −0.1190), −1.586 (k = 27; −1.587), +2.887 (k = 31; A49 independent +2.62), +4.558 (k = 33; +4.557).

### 1.5 Finite certificate and zero sets (`cert/modcert.c`, own code)

For odd k, G[d] = (−1)^d g_k(d) is accumulated for all d ≤ 5.4·10⁷ by the signed recursion a_n[m] = a_{n−1}[m] − (−1)^n a_n[m−n] modulo two primes, p₁ = 2⁶¹ − 1 and p₂ = 4 611 686 018 427 387 847 (both prime; primality is not needed for rigour). A residue ≠ 0 modulo either prime proves g_k(d) ≠ 0; only d with both residues 0 remain ("double zeros") and these are re-evaluated exactly. Results (`cert/compare_cert.json`):

* k = 27: 68 double zeros, max 1375, equal to the exact zero set (GMP integers, `exact/gexact.c`, all d ≤ 300 000). No double zero in (300 000, 5.4·10⁷].
* k = 29: 121 double zeros, max 1934, equal to the exact zero set. No double zero beyond 300 000.
* The certificate range 5.4·10⁷ exceeds D₂₇ = 49 340 462 and D₂₉ = 51 587 220 (A49) and my own D₀ (49.31·10⁶, 51.56·10⁶). The exact E/O program (`exact/eo56.c`) found no negative a_n(m) entry (counter `neg` = 0, confirming a_n(m) ≥ 0 in the whole range) and agrees on zeros; last d with E ≥ O below 3·10⁵ is 120 613 (k = 27) and 146 421 (k = 29), far below D_k, so PD is not contradicted by the data.
* Hence for allowed d > max Z_k: below D_k by the certificate, at or above D_k by PD, g_k(d) ≠ 0.

### 1.6 k = 31 and 33

* At the strength of the A41/A44 CLT layer (δ up to ≈ 0.125–0.17) the block ratio exceeds 1: FAITH 1.00966 and 1.03772, TIGHT 1.00607 and 1.03339, A49 1.0155 and 1.0436. The block inequality cannot hold, so this layer fails for k = 31, 33. Confirmed.
* My SHARP layer (δ ≈ 0.06; checked numerically in §1.3) gives R = 0.88196 and 0.90522 and T < 0, i.e. both inequalities of the PD argument pass for k = 31, 33 at N1 = 1500. I did not run the finite certificate to D ≈ 5.4·10⁷ for k = 31, 33, and the sharp layer has only my own derivation plus the FFT spot checks. So I make no PD claim for k = 31, 33, but A49's sentence "the method does not close at N1 = 1500 for k ≥ 31" should read "does not close with the A41/A44 local-CLT constants".
* I did not test k > 33 (my params file stops at 33).

### 1.7 Rigorous versus numerical (for each of k = 27, 29)

Rigorous mathematics (derived above): the A_n product formula; E−O identity; block lemma algebra; the Chernoff step; convexity of F; the tail-monotonicity criterion; the local-CLT decomposition δ = D1 + D2 + D3; the modular argument for nonvanishing.

Computer-assisted with enclosures: all constants (S_lo, S_hi, M_lo, M_hi, K₃, δ per cell, R over 0.0025-boxes, D₀, α₁, α₂, C*, T(D)) are computed with 128-bit arb balls or endpoint intervals built on arb, with outward rounding when passed through float64 JSON files (cell edges compared as exact floats; I add one ulp outward). The residues modulo p₁, p₂ and the exact GMP zero lists are exact integer arithmetic.

Not rigorous, used only as cross-checks: the FFT sanity (`sanity56_clt.out`), the numeric K₃ check, the float tail-gap check, and the A41-cell replication.

What the proof still depends on: that the local-CLT claim (my derivation, A44's derivation, and A41's) is correct for all n ≥ 1467 at every u in the cell; the numerics support it but do not replace the proof; and that no software bug affects all three independent code bases (mine reproduces A41's blocks to 1e−16 only when fed A41's cells, so the block algebra is shared knowledge, but the CLT layer and the tail evaluation were re-implemented).

Verdicts: **k = 27 VERIFIED**: R = 0.9568 (mine, conservative), margin η ≥ 0.043, tail T = −1.57 (conservative ball mode) or −27.6 (exact), certificate and zero set confirmed. **k = 29 VERIFIED WITH CAVEATS**: R = 0.9829 (conservative) / 0.9799 (tight), η ≥ 0.0171 in my pipeline (A49's 0.01191 is conservative), tail inequality true by a wide margin (T = −26.9 exact; −0.10 in the A41 ball style), certificate and zero set confirmed. The caveat is that the 1.2–1.7 % block margin is smaller than the local-CLT error δ ≈ 0.1 that it has to absorb, so k = 29 is only as strong as the local-CLT lemma (which my sharper layer, with R = 0.860, supports with far more room).

## 2. Item 2: new proved zeros

**Statement.** For an odd prime power k ≥ 9: g_k(k²+2k+4) = 0 if k ≡ 3 mod 4; g_k(k²+3k+4) = 0 if k ≡ 1 mod 4.

**Proof (re-derived).** Let d = k² + 2k + 4 (k ≡ 3) or k² + 3k + 4 (k ≡ 1). Then (k+1)² < d < (k+2)², so only n ≤ k+1 contribute. The class condition k | d − n² with d ≡ 4 mod k gives k | (n−2)(n+2). For k = p^a with p odd, p cannot divide both n−2 and n+2 (their difference 4 is prime to p), so p^a divides one of them: n ≡ ±2 mod k. In [0, k+1] this leaves n = 2 and n = k−2 (n = k+2 > k+1, n = 2k−2 > k+1 for k > 3). Term n = 2: m = (d−4)/k = k+2 or k+3, and φ₂(m) = [x^m](1−x)/(1−x⁴) = +1, −1, 0, 0 for m ≡ 0, 1, 2, 3 mod 4; m = k+2 ≡ 1 mod 4 when k ≡ 3, giving −1; m = k+3 ≡ 0 mod 4 when k ≡ 1, giving +1. Term n = k−2: m = (d−(k−2)²)/k = 6 (k ≡ 3) or 7 (k ≡ 1); since m ≤ n (k ≥ 8, resp. k ≥ 9), φ_n(m) = c_m, the coefficient of ∏_{i≥1}(1+x^i)^{−1}, and c₆ = +1, c₇ = −1 (the coefficients are (−1)^m times the number of partitions of m into distinct odd parts: 5+1; and 7). Sums: −1 + 1 = 0 and +1 − 1 = 0. ∎ The hypothesis "prime power" is used exactly once (n ≡ ±2 mod k), and k ≥ 9 exactly once (m ≤ n).

**Exact tests** (`item2/gk_point.c`, signed 128-bit integer arithmetic, exact for these sizes; `item2/analyze_item2.py`, `item2/item2_results.json`; independent series check `item2/series_check.py`):

* All 320 odd prime powers 9 ≤ k ≤ 1999 (254 of them ≤ 1501): g_k at the stated d is exactly 0. Zero failures.
* k = 3, 5, 7 fail as the proof predicts: values (d = 19, 44, 67): −1, −1, +1.
* Non-prime-powers (677 odd non-prime-powers 15 ≤ k ≤ 2001, all odd k from 3 to 2001 were evaluated): only k = 15 gives 0 at the main d (it has extra n with n² ≡ 4 mod 15); all others nonzero.
* Opposite class (k ≡ 3 mod 4 evaluated at k²+3k+4, k ≡ 1 mod 4 at k²+2k+4): the n = 2 term is 0 (m ≡ 2, resp. 3 mod 4), so the value is exactly c₆ = +1 or c₇ = −1, i.e. ±1 ≠ 0 for every prime power tested. So the congruence condition is sharp.
* The (k+2)²−3 family of the prereg also has no failure among the tested prime powers k ≥ 5.

**Verdict: VERIFIED** (Category A, a finite-term proof plus exact evaluation).

## 3. Item 3: preregistration, scoring, T-jump

### 3.1 Timeline (A49 directory mtimes; `stat`)

| time (CDT, 2026-10-22) | file |
|---|---|
| 18:00:20.84 | code copies (`proof_A41/*.py`, `proof_A44/*.py`, `exact/eo_gmp.c`, `gcert.c`) |
| 18:00:41.41 | `prereg/prereg.md` and `prereg/prereg.sha256` (identical mtime) |
| 18:00:49.13–.18 | compiled binaries `eo_gmp`, `gcert`, `run_exact.sh` |
| 18:00:49.85 | first output (`scan/z_k62_p…`); progress log "done 62 18:00:50" |
| 18:00:55.4–18:01:06.9 | `eo_k61..79.json`, scans, ALLDONE 18:01:06 |

`sha256sum prereg/prereg.md` = c441f9b867882893eb79bf73a2e87bdbe0922e57825d5b01420138c64b764bf4, equal to the value stored in `prereg.sha256` and to the claim in the task; size 3656 bytes. No computation output exists before 18:00:49. **Verified**, with two caveats: (i) the code copies pre-date the prereg by 21 s (copying code is not computing results, but the prereg's own statement "before any A49 computation" is true only in that sense); (ii) all timestamps are filesystem mtimes on one machine and the hash lives next to the file, so nothing here would detect a deliberately back-dated file; the check shows ordering consistent with the logs, not an external proof.

The prereg's disclosure section is accurate: it states that the prime half of the primary set was already known from A45 data (not blind). The Task 2 forecasts R ≈ 0.96, 0.985 for k = 27, 29 are extrapolations of the A41/A44 trend (my R_27 = 0.957–0.962, R_29 = 0.980–0.988), not blind predictions.

### 3.2 L* definition and scoring

I coded L* from the prereg text (forced zeros k(k+2) for squarefree k, and (k+2)²−3 for odd prime powers k ≥ 5, removed; L* = max of the remaining zeros) and ran my own exact program (`exact/gexact.c`, GMP, any k, every d ≤ 5·10⁶; `exact/analyze_item3.py`). For all 19 k = 61..79 my zero counts, forced sets and L* equal A49's `analysis/lstar.json` (0 differences). Primary set results:

| k | 61 | 65 | 67 | 69 | 71 | 73 | 75 | 79 |
|---|---|---|---|---|---|---|---|---|
| L* | 8165 | 9545 | 5838 | 6150 | 9472 | 6625 | 7761 | 7909 |
| k(k+2) | 3843 | 4355 | 4623 | 4899 | 5183 | 5475 | 5775 | 6399 |

No other k in 61..79 (62, 63, 64, 66, 68, 70, 72, 74, 76, 77, 78) has a zero beyond k(k+2). Prime half: 5/5 (61, 67, 71, 73, 79). Composite squarefree with L* > k(k+2): 65 and 69, both divisible by 3 or 5, so 65 and 69 are the only exceptions: **PASS / PASS** (the prime half is not a blind test; the prereg says so). k = 75 is not squarefree and is outside the statement.

Secondary set: I re-ran exact g_k(d), d ≤ 2·10⁶, for **every odd k = 3..999** (`exact/sec/`, `exact/analyze_secondary.py`). All 167 primes 3 ≤ k ≤ 997 have L* > k(k+2) (minimum margin 4, at k = 163); 21 of 236 squarefree composites have L* > k(k+2) (15, 21, 33, 35, 39, 55, 65, 69, 111, 115, 123, 129, 201, 213, 291, 381, 519, 543, 717, 723, 993), all divisible by 3 or 5. For every odd k where A49 has data, zero count and L* agree with A49 exactly. After also removing the new class-4 zero of item 2, 74 of the 164 primes 11 ≤ k ≤ 997 have no zero beyond k(k+2) (A49: 74 of 164, equal). The class-4 zero is in Z_k for every odd prime power 9 ≤ k ≤ 999. The tertiary even set (two-prime scan) was not re-run; my exact runs for even k = 62..78 agree with A49 on L* and zero counts (§ 5, item 4).

### 3.3 T(k) and the jump at k = 67

My `eo56.c` (signed GMP E/O) and `gexact.c` (separate program, direct g_k) agree on the zero list for every odd k = 61..79, and `eo56` reproduces A49's T(k) exactly:

| k | 61 | 63 | 65 | 67 | 69 | 71 | 73 | 75 | 77 | 79 |
|---|---|---|---|---|---|---|---|---|---|---|
| T(k) | 2 032 764 | 2 163 991 | 2 402 920 | **3 331 509** | 3 615 885 | 3 921 828 | 4 230 862 | 4 546 884 | 4 857 055 (censored) | 5 000 000 (censored) |
| ρ(k) = √T/k | 23.373 | 23.350 | 23.848 | **27.242** | 27.559 | 27.892 | 28.177 | 28.431 | 28.622 | 28.305 |
| increment | | −0.023 | +0.498 | **+3.394** | +0.316 | +0.334 | +0.284 | +0.254 | +0.190 | −0.317 |

k = 65: 2 402 920, ρ = 23.848; k = 67: 3 331 509, ρ = 27.242; k = 69: 3 615 885, ρ = 27.559, all to 5·10⁶, all matching. The jump is at k = 67 (increment 3.39 ≥ 1.5); no jump in 69..75; 77 and 79 are censored (T > 0.95·D), so "exactly one jump in 61..79" cannot be decided, as A49 says. Scoring: point prediction 63 FAIL; window {61, 63, 65, 67} PASS (edge); post-jump ρ ∈ [25, 28] PASS (27.242). Verdict **VERIFIED**.

## 4. Process notes and disclosures

* All audit code is new (C: `cert/modcert.c`, `exact/eo56.c`, `exact/gexact.c`, `item2/gk_point.c`; Python: `proof/clt56.py`, `iv56.py`, `blocks56.py`, `tails56.py`, `params56.py`, `make_cells56.py`, `run_pd56.py`, and the scripts named above). I read A41/A44/A49 sources to understand the method. No A41/A44/A49 module is imported by any audit script. `proof/replicate56.py` reads A49's cell and summary JSON files as data only.
* Diagnostic outside the audit directory: while debugging a non-conservative σ-ratio in my block code I ran a throw-away harness in `/tmp/diag/` that imported a **copy** of A41's `blocks_k.py` (and converted A41/A44 cell files to my format in `/tmp/a41cells.json`, `/tmp/a44cells.json`). This was used only to locate my bug; none of its output is in this report, and the final code does not use it. The replication in §1.4 uses my own code.
* Resource limits respected: `ulimit -v` ≤ 2.8 GB, `nice`, `OMP_NUM_THREADS=1`, long jobs in background with logs in `logs/`.

## 5. Discrepancies and caveats (none changes a verdict)

1. A49's k = 29 "tail margin −0.057/−0.119, margin real but small" understates the margin: it is a ball-arithmetic artefact. Exact convex evaluation gives T ≈ −27 (§1.2). The block margin (η = 0.0119 in A49, 0.0171 in my pipeline) is the real thin margin.
2. A49's "k = 31, 33 fail" holds only for the A41/A44 local-CLT strength; my sharper layer passes both block and tail inequalities for k = 31, 33 (R = 0.882, 0.905). Not a proof of PD for those k (no finite certificate run).
3. A49's secondary L* data omit k = 21 (no `eo_k21.json` in the A43 directory, the loop silently skips missing files). With the exact run k = 21 has L* = 2055 > 483 and is divisible by 3: the composite count should read 21 of 236 (A49: 20 of 235), and the divisibility statement still holds. The prime count in the json is 166 (k = 3 is added by hand in the report: 167).
4. Even k = 62..78: my exact `gexact` L* values and zero counts agree with A49's (computed by A49 via two-prime double zeros re-evaluated exactly), including the forced k(k+2) zero for squarefree even k.
5. Block R at k = 3 differs by 4·10⁻⁵ between A49's A41 pipeline and the exact box [0.4875, 0.49]: A49's box edge accumulated to 0.48750000000000004. Conservative direction; harmless.
6. A49 D_k are slightly larger than my D₀ (e.g. k = 29: 51 587 220 vs 51 557 554) because α₁ differs in the 4th digit (A41 0.2090532, A44 0.2088431, mine 0.2089032). Larger D is the safe direction, T is monotone, and the certificate range covers both.
7. The prereg Task 2 forecasts are trend extrapolations; the primary prime half is not blind (prereg discloses it).
8. Timestamps are self-attested mtimes, not an external time-stamp.

## 6. Files

`REPORT.md`, `REPORT.pdf`, `SHA256SUMS`; `cert/` (modular certificate, `compare_cert.json`); `exact/` (E/O and exact g_k programs, outputs, `sec/`, analysis scripts and `item3_results.json`, `secondary_results.json`); `item2/`; `proof/` (CLT, block, tail code; `pd56_results.json`, `replicate56.json`, sanity checks); `logs/`.
