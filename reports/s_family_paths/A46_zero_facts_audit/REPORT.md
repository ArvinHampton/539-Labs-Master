# A46: independent audit of the two structural zeros of g_k (from A45 §4.3)

**For:** Arvin Hampton · 2026-10-22 (CDT). Only new files were written, all in `A46_zero_facts_audit/`. Code `check.py` was written from scratch, with no imports from A45. It ran under `nice`, OMP_NUM_THREADS=1, `ulimit -v` 3 GB, in about 12 s. No TPC or RH claims are made.

## 0. Definitions (from A40/A39)
g_k(q) = Σ_{n≥0} q^{n²}/(−q^k;q^k)_n. Write P_n(x) = ∏_{j≤n}(1+x^j)^{-1} = Σ_m φ_n(m)x^m. Then

g_k(d) = Σ_{n: n²≤d, k | d−n²} φ_n((d−n²)/k).   (*)

**Lemma 0 (stabilisation).** P_n ≡ P_∞ (mod x^{n+1}), so φ_n(m) = c_m for m ≤ n. Here P_∞ = Σ c_m x^m with c_0..c_12 = 1, −1, 0, −1, 1, −1, 1, −1, 2, −2, 2, −2, 3 (exact). The two facts used are **c_2 = 0** and **c_6 = 1**. In addition, φ_0(m) = δ_{m,0} and φ_1(m) = (−1)^m.

(*) was checked against a direct, truncated expansion of the full series for every k ≤ 40, at both target exponents: 0 mismatches.

## 1. Claim 1: g_k(k(k+2)) = 0
**Proof (independent).** Take any squarefree k ≥ 2. Let d = k²+2k < (k+1)², so every contributing n has n ≤ k. The condition k | d − n² means k | n², and since k is squarefree this gives k | n. So n ∈ {0, k}.
- n = 0 gives φ_0(k+2) = 0.
- n = k gives m = 2 ≤ k, so the term is φ_k(2) = c_2 = 0.

Hence g_k(d) = 0. ∎

**Scope proved (Category A): every squarefree k ≥ 2, odd or even.** Oddness is not used.

**Sharpness.**
- k = 1 fails: g_1(3) = φ_1(2) = 1. The stabilisation needs n = k ≥ 2. The claim as worded ("every squarefree odd k") is therefore false at k = 1, and needs k ≥ 3 (A45's own proof states k ≥ 3).
- Non-squarefree k: g_k(k(k+2)) ≠ 0 for all 392 non-squarefree k in 4..1001 (numerical; extra n with k | n², k ∤ n contribute). Sample values: k = 4: −1, 8: 1, 9: 2, 12: −2, 18: 6, 25: 6, 27: 8, 45: 40, 49: 29, 75: 263, 121: 1180, 125: 5083, 169: 8904. So squarefreeness is necessary in practice for k ≤ 1001. That it is necessary for all k is **not** proved.

**Certificate.** k = 2..1001: all 608 squarefree k (404 odd ≥ 3, 204 even) give g_k(k(k+2)) = 0 exactly. No non-squarefree k gives 0.

## 2. Claim 2: g_k((k+2)² − 3) = 0
**Proof (independent).** Let d = k²+4k+1 = (k+2)² − 3, so n ≤ k+1. Since d ≡ 1 (mod k), the condition on n is n² ≡ 1 (mod k).

Suppose k = p^a is an odd prime power. Then (n−1)(n+1) ≡ 0, and p cannot divide both factors, so n ≡ ±1 (mod k). Within [0, k+1] this gives n ∈ {1, k−1, k+1}, which are distinct for k ≥ 3. The terms are:
- n = 1: φ_1(k+4) = (−1)^{k+4} = −1, since k is odd.
- n = k−1: m = 6, so for k ≥ 7 the term is φ_{k−1}(6) = c_6 = +1.
- n = k+1: m = 2, so the term is c_2 = 0.

The sum is 0.
- k = 5 by direct computation: terms (n, m, φ) = (1, 9, −1), (4, 6, +1), (6, 2, 0), sum 0.
- k = 3 fails: (1, 7, −1), (2, 6, φ_2(6) = 0), (4, 2, 0), so g_3(22) = −1.

∎

**Scope proved (Category A): every odd prime power k ≥ 5**, i.e. all primes k ≥ 5 together with 9, 25, 27, 49, 81, 121, 125, … The prime case is the original claim, now proved. The prime-power extension is new.

**Sharpness.**
- k = 3 fails (value −1). Even k fail for k ≤ 15: g_2 = 1, g_4 = 2, g_6 = 3, g_8 = −3, g_10 = 2, g_12 = 9, g_14 = 2. In 1..1001, **no even k** gives zero.
- Non-prime-powers: the only zeros among all non-prime-power k ≤ 1001 are **k = 15 and k = 21**.
  - k = 15: (1,19,−1), (4,18,2), (11,11,−2), (14,6,1), (16,2,0).
  - k = 21: (1,25,−1), (8,22,6), (13,17,−6), (20,6,1), (22,2,0).
  - In both, the extra roots cancel in pairs. This is a numerical coincidence; no proof is given.
- Conclusion: "prime" can be weakened to "odd prime power". The zero set in 1..1001 is exactly {odd prime powers ≥ 5} ∪ {15, 21}.

**Certificate.** All 166 primes 5..997 and all odd prime powers 7..1001: zero, with no failures. The zero set over k = 1..1001 is as stated above.

## 3. Comparison with A45 §4.3
- (i) A45's proof matches ours. Minor gaps:
  - It does not state the stabilisation lemma explicitly. The claim c_2 = 0 needs n = k ≥ 2.
  - "odd" is unnecessary, and is a weaker statement than what holds.
  - The task wording "every squarefree odd k" omits k ≥ 3; k = 1 is a counterexample.
  - A45's data claim "0/96 non-squarefree" (odd k ≤ 999) is consistent with our 392/392 (all k ≤ 1001).
- (ii) A45's proof is correct for primes. Points to note:
  - Its root step only uses that n² ≡ 1 has two roots, so it extends verbatim to odd prime powers. A45 did not note this.
  - The k ≥ 7 condition for c_6 and the separate k = 5 check are both handled correctly by A45.
  - A45 does not record that k = 3 fails, or the sporadic zeros at k = 15 and 21. Because of those two, "zero ⇒ prime power" is false. Any L(k)/L*(k) analysis should not use this zero as a primality detector.
- No numerical disagreement with A45.

## Verdicts
| Claim | Verdict | Proved scope (Category A) | Numeric range |
|---|---|---|---|
| 1. g_k(k(k+2)) = 0, squarefree odd k | **VERIFIED (with proof)** for k ≥ 3. **Fails at k = 1.** | all squarefree k ≥ 2 | k ≤ 1001: 608/608 squarefree zero, 0/392 non-squarefree zero |
| 2. g_k((k+2)²−3) = 0, prime k ≥ 5 | **VERIFIED (with proof)** | all odd prime powers k ≥ 5 | k ≤ 1001: all prime powers zero; k = 3 and all even k nonzero; sporadic zeros k = 15, 21 |

## Files
`check.py`, `results.json`, `REPORT.md`, `REPORT.pdf`, `mk_pdf.py`.
