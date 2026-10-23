# A47: zeros of g_k((k+2)²−3) at composite k

**For:** Arvin Hampton · 2026-10-22 (CDT). All files are new and live in `A47_composite_zeros/`. Every run used `nice`, OMP_NUM_THREADS=1 and `ulimit -v` 3 GB. No TPC or RH claims are made.

Notation follows A46: d = (k+2)²−3 = k²+4k+1, g_k(d) = Σ_{n²≤d, k|d−n²} φ_n((d−n²)/k), and φ_n(m) = c_m for m ≤ n.

## 1. Results

### Category A (proved)

**Lemma 1 (sign).** For every n and m, (−1)^m φ_n(m) ≥ 0.

*Proof.* Use 1/(−q;q)_n = (q;q)_n/(q²;q²)_n and put q = −x. Then
P_n(−x) = ∏_{j≤n}(1−(−x)^j) / ∏_{j≤n}(1−x^{2j}) = ∏_{odd j≤n}(1+x^j) · ∏_{even j≤n}(1−x^j) / ∏_{i≤n}(1−x^{2i}).
Every even factor 1−x^{2i} in the numerator (2i ≤ n) cancels against the denominator. What remains is
P_n(−x) = ∏_{odd j≤n}(1+x^j) / ∏_{n/2<i≤n}(1−x^{2i}),
which has nonnegative coefficients. Write A_n(m) = |φ_n(m)|. Then A_n(m) counts pairs made of (a set of distinct odd parts ≤ n) and (a multiset of even parts 2i with n/2 < i ≤ n), with total size m. Letting n → ∞ gives c_m = (−1)^m·q_odd(m), where q_odd(m) is the number of partitions of m into distinct odd parts. ∎

The lemma was also checked numerically for all n, m ≤ 400 (`sign.py`, no violations).

**Lemma 2 (reduction, odd k ≥ 7).** Let R be the set of roots s of s² ≡ 1 (mod k) with 1 < s < k/2. Then
g_k(d) = Σ_{s∈R} [ φ_s(k+4−t_s) + φ_{k−s}(4+2s−t_s) ],  where t_s = (s²−1)/k.

*Proof.* Since d ≡ 1 (mod k), the contributing n are exactly the roots of n² ≡ 1 in [0, k+1]. These are the roots in (0,k), together with n = k+1. The baseline terms n ∈ {1, k−1, k+1} contribute −1 + c_6 + c_2 = 0, as in A46. The other roots come in pairs (s, k−s). Direct substitution gives m(s) = k+4−t and m(k−s) = 4+2s−t. ∎

**Corollary 3 (pair cancellation is opposite-sign cancellation).** m(s) + m(k−s) = k+8+2s−2t is odd, so by Lemma 1 the two terms of each pair always have opposite signs (or one of them is 0). In particular:
- If k has r = 2 distinct prime factors, then |R| = 1. In that case g_k(d) = 0 **if and only if** A_s(k+4−t) = A_{k−s}(4+2s−t).
- In general, g_k(d) = 0 if and only if the signed pair sums cancel overall.
- Since |R| = 2^{r−1} − 1 ≥ 1 for every non-prime-power odd k, this proves that non-prime-power k can vanish only through such a coincidence.

**Proposition 4 (even k, partial).** If k = 2p^a with k ≥ 10 (p an odd prime), then g_k(d) = 2 ≠ 0.

*Proof.* The roots of n² ≡ 1 mod 2p^a are n ≡ ±1 only, so n ∈ {1, k−1, k+1}. The terms are:
- n = 1: φ_1(k+4) = +1, since k is even.
- n = k−1: m = 6 ≤ k−1, so the term is c_6 = +1.
- n = k+1: m = 2, so the term is c_2 = 0.

The sum is 2. ∎

Checked values: g_10 = g_14 = 2. For general even k, the same baseline +2 appears, plus extra pairs. That case is numerical only.

### Mechanism at k = 15 and k = 21 (exact)

For each k below, the baseline terms n = 1, k−1, k+1 give (−1, +1, 0) and are omitted. Each row is one extra pair: (n, m, φ) for n = s and for n = k−s, then the pair sum.

| k | n = s: (n, m, φ) | n = k−s: (n, m, φ) | pair sum |
|---|---|---|---|
| **15** | (4, 18, **+2**) | (11, 11, **−2**) | **0** |
| **21** | (8, 22, **+6**) | (13, 17, **−6**) | **0** |
| 33 | (10, 34, 16) | (23, 21, −8) | 8 |
| 35 | (6, 38, 9) | (29, 15, −4) | 5 |
| 39 | (14, 38, 29) | (25, 27, −14) | 15 |
| 45 | (19, 41, −52) | (26, 34, 25) | −27 |
| 63 | (8, 66, 57) | (55, 19, −6) | 51 |
| 105 | (29,101,−2811)/(34,98,2117)/(41,93,−1771) | (76,54,133)/(71,61,−223)/(64,70,407) | total −2148 |

How the two zeros arise:
- **k = 15:** the right-hand term is untruncated (m = 11 ≤ 11), so it equals c_11 = −q_odd(11) = −2 ({11}, {1,3,7}). The truncated term A_4(18) also equals 2. With n = 4, it counts {odd parts ⊂ {1,3}} together with even parts from {6, 8}: these are 6+6+6 and 8+6+3+1.
- **k = 21:** the term φ_13(17) = −6 has m = 17 > 13, so it is slightly truncated: q_odd(17) = 5, plus one extra from 13 < 2i ≤ 17. On the other side, A_8(22) = 6. Small-number equality again.

So both zeros come from Corollary 3's opposite-sign pair whose two magnitudes happen to be equal at small size. Nothing deeper is visible.

### Numerical (not proved)
- **Full scan, k = 1..5000, all k (odd and even):** the zero set is exactly {odd prime powers ≥ 5} ∪ {15, 21}.
  - Method: `big.py`, which evaluates g_k(d) modulo two primes near 2^31.
  - A nonzero residue certifies g_k(d) ≠ 0 exactly.
  - The residue-zero k are exactly the proved odd prime powers plus 15 and 21, which are exact zeros (`pairs.py` / A46).
  - In particular, no even k ≤ 5000 gives a zero.
- **Exact pair data, odd non-prime-power k ≤ 1001** (`pairs.py`, `pairs_1001.json`):
  - Only two pairs vanish, (k, s) = (15, 4) and (21, 8).
  - For r = 2 and k > 21, the magnitude ratio of the two pair terms satisfies |log(A_s/A_{k−s})| ≥ 0.577 (minimum at k = 77). So the two terms always differ by a factor ≥ 1.78, with no near-misses.
  - For r ≥ 3, no partial pair sums cancel to give a total of 0.

## 2. What is not proved, and the obstruction
A complete characterisation would need one of the following:
- **For r = 2:** A_s(k+4−t) ≠ A_{k−s}(4+2s−t) for all k > 21.
- **For r ≥ 3:** non-cancellation of a signed sum of 2^{r−1}−1 pairs.

The difficulty is that the two sides live in different regimes:
- A_{k−s}(m₂) is essentially q_odd(m₂), which grows like exp(π√(m₂/3)).
- A_s(m₁) is a heavily truncated count. Its parts are restricted to odd parts ≤ s and even parts in (s, 2s]. Its growth depends on both s and m₁/s.

Which side dominates changes with s/k (the table shows both signs). A proof would therefore need uniform two-sided asymptotics for A_n(m) across the whole range m/n ∈ [1, ~k/s], plus an argument that no exact equality occurs. The numerics suggest the gap grows (ratios move away from 1). Rigorous effective bounds of this kind were not obtained here. For even k, the extra roots modulo 8 and modulo several primes create the same obstruction on top of the baseline +2.

## 3. Files
`run.py` (exact terms, k ≤ 300), `sign.py` (Lemma 1 check), `pairs.py` and `pairs_1001.json` (exact pair data), `big.py`, `scan_5000.json` and `scan5000.log` (k ≤ 5000 scan, about 9 min), `REPORT.md`, `REPORT.pdf`.
