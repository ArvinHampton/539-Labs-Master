# A55: small-k exceptions of the g_k zero families, and the k = 15, 21 sporadic zeros

**For:** Arvin Hampton · 2026-10-22 (CDT). Only new files, all in `A55_small_k_exceptions/` (A46, A47, A49, A50 were read; A54_proofs2 was looked at read-only and is about k = 4, so it is not used). Every run used `nice`, OMP_NUM_THREADS=1, `ulimit -v` 3 GB; the whole job takes under 10 s of CPU. No TPC or RH claims.

Notation (as in A46/A47/A50). g_k(d) = Σ_{n²≤d, k | d−n²} φ_n((d−n²)/k), where P_n(x) = ∏_{j≤n}(1+x^j)^{-1} = Σ φ_n(m)x^m, and c_m = φ_∞(m) = (−1)^m q(m), with q(m) the number of partitions of m into distinct odd parts (A47 Lemma 1). q(0..14) = 1,1,0,1,1,1,1,1,2,2,2,2,3,3,3. Stabilisation: φ_n(m) = c_m for m ≤ n. A term of g_k(d) is written (n, m, φ). "Odd prime power" means k = p^a, p odd, a ≥ 1.

The three families under study, named so the report has no letter labels:

- **Family 1:** d = (k+2)²−3 = k²+4k+1, zero for all odd prime powers k except k = 3 (§1).
- **Family 2:** d = k²+2k+4, zero for odd prime powers k ≡ 3 (mod 4) except k = 3, 7.
- **Family 3:** d = k²+3k+4, zero for odd prime powers k ≡ 1 (mod 4) except k = 5.

## 0. Summary

1. **The exception sets are not "3, 5, 7 for every family".** They are exact and different (Theorem 1, Category A): Family 1 fails only at k = 3; Family 2 fails only at k = 3 and 7; Family 3 fails only at k = 5. (A49 stated "k ≥ 9" as the range of validity; that is sufficient but not sharp: Family 1 holds from k = 5, Family 2 holds for every prime power ≡ 3 mod 4 except 3 and 7, Family 3 holds for every prime power ≡ 1 mod 4 except 5.) The union of the exceptions is {3, 5, 7}, and k = 5 is *not* an exception of Family 1: the term φ_4(6) equals c_6 although 6 > 4, because the first truncation correction S(1) vanishes (§1.3).
2. **The hypothesis is right for three of the four failures and wrong for one.** Truncation (stabilisation input φ_n(m) = c_m, m ≤ n, broken in the term n = k−b) causes: Family 1 at k = 3 (φ_2(6) = 0 ≠ c_6 = 1), Family 2 at k = 7 (φ_5(6) = 2 ≠ c_6 = 1), Family 3 at k = 5 (φ_3(7) = −2 ≠ c_7 = −1). Family 2 at k = 3 is *not* a truncation failure: there the congruence n² ≡ 4 (mod 3) has an extra solution n = 4 = 2k−2 that is inside n ≤ √d (§1.3). The inputs c_2 = 0, c_6 = 1, c_7 = −1 are used as stated and nothing else breaks. The numbers 3, 5, 7 enter only as "the odd integers below the stabilisation threshold 9", not as primes: 9, 25, 27, 49 are not exceptional.
3. **New proved zero families (Category A, Theorem 2).** For d = k²+jk+b² with b ∈ {1, 2} and every integer j, I classified exactly which (j, b, k mod 4) give g_k(d) = 0 for all large odd prime powers k. There are 16 families with −8 ≤ j ≤ 8 (j = −2, −1, 1, 4 for b = 1; j = −4..3 for b = 2; plus the boundary families j ≤ −5 for b = 2). Examples: g_k(k²+k+1) = 0 for all odd prime powers k ≥ 5; g_k((k−1)²) = 0 and g_k(k²−k+1) = 0 for all odd prime powers k ≥ 3; g_k(k²+4) = 0 for k ≡ 1 mod 4 prime powers k ≥ 9; g_k(k²+k+4) = 0 for k ≡ 3 mod 4 prime powers k ≥ 7; g_k((k−2)²) = 0 for k ≡ 1 mod 4. In every one of these families the exceptions among odd prime powers are subsets of {3, 5, 7}, and always below the threshold K = max(j+3b, 2b+1, −j) (they are the odd prime powers below K that are not rescued by a vanishing correction). No other infinite family exists in the search window (below).
4. **Search (numerical, exact integers, all k ≤ 500; 3025 pairs (j, c), j = −8..16, c = −60..60, which contains j = 0..6, c = −6..8 and every (k+a)²−b with 1 ≤ a ≤ 6, −6 ≤ b ≤ 8):** every pattern "zero for ≥ 90% of the allowed k of an arithmetic class (k ≥ 70)" has c ∈ {0, 1, 4}, i.e. c = b² with b ∈ {0, 1, 2}, and is in Theorem 2 or in the b = 0 case (squarefree k). For c = b² with b ≥ 3 the zero sets are finite clusters that drift to larger k as j grows (e.g. c = 16, j = 8: k = 49, 59, 61; j = 16: k = 131, 139). For non-square c the zero rate among allowed d is ≤ 5% and no residue class is zero.
5. **k = 15, 21: not explained by the {3,5,7} truncation mechanism; explained as small-size coincidences (numerical, with an exact term-level description).** Evidence: (i) the truncation failures live in the terms n = k−b, which are stable for k ≥ 9, while at k = 15, 21 the zeros come from *extra roots* of n² ≡ d (mod k) that exist only for composite k; (ii) at k = 15 and 21 the cancelling pair is a different small-number equality in every family (e.g. c_14 + c_13 = 0 because q(13) = q(14) = 3; or φ_4(18) = 2 = −c_11), all between integers ≤ 9; (iii) the sporadic zero rate of k = 15, 21 equals that of the primes 17, 19, 23 (14% vs 16% in the window j = 0..6, c = −6..8) and falls with k for every k, prime or composite (≤ 7% above k ≈ 29 on the full grid; zero in window j = 0..6, c = −6..8 for all k > 25); (iv) 15 and 21 are the two *smallest odd non-prime-powers*, and 35 = 5·7, 45 = 9·5, 63, 75, 105 = 3·5·7 are not zeros, so a "product of exceptional primes 3, 5, 7" rule is refuted; (v) the pair magnitudes at Family 1 are equal at 15 (2, 2) and 21 (6, 6), then differ by a factor ≥ 2 at 33, 35, 39 and ≥ 1.78 for every non-prime-power k > 21 (minimum at k = 77; A47/A50 range k ≤ 11000). The odd non-prime-power zero sets over all 34 families with j = −8..8, c ∈ {1, 4} and k ≤ 2000 are ⊂ {15, 21} (§3.3). A proof that no zero occurs for non-prime-power k > 21 is still not available for all k (A50 proved a subset; this report adds nothing there).

## 1. Task 1: exact failure of the three families

### 1.1 Tools (Category A unless noted)

**Lemma 1 (closed forms).** φ_0(m) = δ_{m,0}; φ_1(m) = (−1)^m; φ_2(m) = 1, −1, 0, 0 for m ≡ 0, 1, 2, 3 (mod 4), because 1/((1+x)(1+x²)) = (1−x)/(1−x⁴). ∎

**Lemma 2 (exact truncation correction, A50 Lemma 4).** For n < m ≤ 2n+1: φ_n(m) = c_m + S(m−n−1), where S(y) = Σ_{x=0}^{y} (−1)^x Q(x), Q = q. For m ≤ n the correction is zero (stabilisation). S(0..12) = 1, 0, 0, −1, 0, −1, 0, −1, 1, −1, 1, −1, 2. (Proved in A50; re-checked here for all n ≤ 150 and all m ≤ min(2n+1, 300): 0 violations.) Consequently a term with m = n+2 equals its stable value c_m (S(1) = 0), and m = n+1, n+4, n+6, … do not (S(0) = 1, S(3) = −1, S(5) = −1).

**Lemma 3 (q ≥ 1).** q(m) ≥ 1 for all m ≠ 2, and q(m) ≥ 2 for m ≥ 8. *Proof.* m = 0: empty partition; m odd: {m}; m even ≥ 4: {m−1, 1}. For m ≥ 8, q is nondecreasing (A50 Lemma 2) and q(8) = 2. ∎

### 1.2 Theorem 1 (exact failure sets; Category A)

Let k be an odd prime power.
1. g_k(k²+4k+1) = 0 if and only if k ≠ 3. (g_3(22) = −1.)
2. If k ≡ 3 (mod 4): g_k(k²+2k+4) = 0 if and only if k ∉ {3, 7}. (g_3(19) = −1, g_7(67) = +1.)
3. If k ≡ 1 (mod 4): g_k(k²+3k+4) = 0 if and only if k ≠ 5. (g_5(44) = −1.)

*Proof.* Theorem 2 below proves vanishing for all k ≥ K, with K = 7, 8, 9 for the three families (K = max(j+3b, 2b+1, −j); j, b = 4, 1; 2, 2; 3, 2). The remaining odd prime powers are k = 3, 5 (Family 1), k = 3, 5, 7 (Family 2, k ≡ 3 mod 4 leaves 3, 7), k = 3, 5, 7 (Family 3, k ≡ 1 mod 4 leaves 5). Their terms are listed exactly in the table of §1.5 (computed from exact integer φ_n(m)). Family 1: k = 3 gives −1, k = 5 gives 0. Family 2: k = 3 gives −1, k = 7 gives +1. Family 3: k = 5 gives −1. ∎ (Verification range for the "only if" direction beyond K: all odd prime powers k ≤ 500 evaluated exactly, none other fails; all k ≤ 2000 by a two-prime residue test.)

### 1.3 Where each input of the generic proof breaks

The generic proof for a family with d = k²+jk+b² uses, for k odd prime power: the root list n ∈ {b, k−b, k+b}; closed forms for n = b; and stabilisation for n = k−b (m = j+2b) and n = k+b (m = j−2b). Its inputs, per family:

| family | j, b | terms | inputs used | stabilisation needs | breaks at | what exactly breaks |
|---|---|---|---|---|---|---|
| 1 | 4, 1 | n=1 (m=k+4), n=k−1 (m=6), n=k+1 (m=2) | φ_1 = (−1)^m; c_6 = 1; c_2 = 0 | k−1 ≥ 6 (k ≥ 7); k+1 ≥ 2 | k = 3 only | φ_2(6) = 0 ≠ c_6 = 1 (correction −1). At k = 5: m = 6 = n+2, S(1) = 0, so φ_4(6) = c_6 and nothing breaks. c_2 = 0 never breaks (m = 2 ≤ k+1 for every k ≥ 1) |
| 2 | 2, 2 | n=2 (m=k+2), n=k−2 (m=6) | φ_2; c_6 = 1 | k−2 ≥ 6 (k ≥ 8) | k = 7 (truncation), k = 3 (extra root) | k = 7: m = 6 = n+1, S(0) = 1, φ_5(6) = 2 ≠ 1. k = 3: roots are 1, 2, 4, and n = 4 = 2k−2 is inside n ≤ √19; the extra term φ_4(1) = −1 spoils the sum |
| 3 | 3, 2 | n=2 (m=k+3), n=k−2 (m=7) | φ_2; c_7 = −1 | k−2 ≥ 7 (k ≥ 9) | k = 5 only | m = 7 = n+4, S(3) = −1, φ_3(7) = −2 ≠ −1. (k = 7 ≡ 3 mod 4 is not in this family's class; there φ_5(7) = c_7 since S(1) = 0) |

So: the stabilisation threshold k ≥ j+3b is *sufficient*; the true failure set is {k < j+3b : the correction S(j+3b−k−1) ≠ 0, or an extra root appears}. For the odd prime powers the threshold set is {3,5} (Family 1), {3,5,7} (Family 2), {3,5,7} (Family 3), and the class condition mod 4 plus the zero of S(1) cut these to {3}, {3,7}, {5}.

### 1.4 Why the union is {3, 5, 7}

All odd integers ≥ 3 below 9 are 3, 5, 7. Families 1–3 have thresholds 7, 8, 9, so the exception candidates are the odd prime powers below 9 = {3, 5, 7} (9 itself is the first generic one). The primes 3, 5, 7 play no role beyond being the odd numbers below the threshold: the prime powers 9, 25, 27, 49, 81, … built from the same primes are not exceptional in any family (checked exactly for all odd prime powers ≤ 500, all 16 families in §2).

### 1.5 Exact terms for k = 3, 5, 7, 9, 11, 13, 15, 21, 25, 27, 33, 35 (all three families, whether or not k is in the class)

Legend: each term is ROLE(n, m, phi_n(m)) with m=(d-n^2)/k. Roles: B = n=b (exact closed form, no stabilisation needed), L = n=k-b, U = n=k+b (both rely on stabilisation phi_n(m)=c_m, m<=n), X = any other root of n^2=d mod k. `[Δ=x]` marks a term with m>n whose value differs from the stable value c_m by x (stabilisation input broken); `[m>n, Δ=0]` marks m>n with phi_n(m)=c_m anyway (a free extension).

**k = 3** (prime power; k mod 4 = 3)

| family | d | class | terms (n,m,φ) | g_k(d) |
|---|---|---|---|---|
| Family 1 | 22 | all odd k | B(1,7,-1) L(2,6,0)[Δ=-1] U(4,2,0) | **-1** |
| Family 2 | 19 | yes | L(1,6,+1)[m>n, Δ=0] B(2,5,-1) X(4,1,-1) | **-1** |
| Family 3 | 22 | no (k mod 4 ≠ 1) | L(1,7,-1)[m>n, Δ=0] B(2,6,0) X(4,2,0) | **-1** |

**k = 5** (prime power; k mod 4 = 1)

| family | d | class | terms (n,m,φ) | g_k(d) |
|---|---|---|---|---|
| Family 1 | 46 | all odd k | B(1,9,-1) L(4,6,+1)[m>n, Δ=0] U(6,2,0) | **0** |
| Family 2 | 39 | no (k mod 4 ≠ 3) | B(2,7,0) L(3,6,+1)[m>n, Δ=0] | **1** |
| Family 3 | 44 | yes | B(2,8,+1) L(3,7,-2)[Δ=-1] | **-1** |

**k = 7** (prime power; k mod 4 = 3)

| family | d | class | terms (n,m,φ) | g_k(d) |
|---|---|---|---|---|
| Family 1 | 78 | all odd k | B(1,11,-1) L(6,6,+1) U(8,2,0) | **0** |
| Family 2 | 67 | yes | B(2,9,-1) L(5,6,+2)[Δ=+1] | **1** |
| Family 3 | 74 | no (k mod 4 ≠ 1) | B(2,10,0) L(5,7,-1)[m>n, Δ=0] | **-1** |

**k = 9** (prime power; k mod 4 = 1)

| family | d | class | terms (n,m,φ) | g_k(d) |
|---|---|---|---|---|
| Family 1 | 118 | all odd k | B(1,13,-1) L(8,6,+1) U(10,2,0) | **0** |
| Family 2 | 103 | no (k mod 4 ≠ 3) | B(2,11,0) L(7,6,+1) | **1** |
| Family 3 | 112 | yes | B(2,12,+1) L(7,7,-1) | **0** |

**k = 11** (prime power; k mod 4 = 3)

| family | d | class | terms (n,m,φ) | g_k(d) |
|---|---|---|---|---|
| Family 1 | 166 | all odd k | B(1,15,-1) L(10,6,+1) U(12,2,0) | **0** |
| Family 2 | 147 | yes | B(2,13,-1) L(9,6,+1) | **0** |
| Family 3 | 158 | no (k mod 4 ≠ 1) | B(2,14,0) L(9,7,-1) | **-1** |

**k = 13** (prime power; k mod 4 = 1)

| family | d | class | terms (n,m,φ) | g_k(d) |
|---|---|---|---|---|
| Family 1 | 222 | all odd k | B(1,17,-1) L(12,6,+1) U(14,2,0) | **0** |
| Family 2 | 199 | no (k mod 4 ≠ 3) | B(2,15,0) L(11,6,+1) | **1** |
| Family 3 | 212 | yes | B(2,16,+1) L(11,7,-1) | **0** |

**k = 15** (NOT a prime power; k mod 4 = 3)

| family | d | class | terms (n,m,φ) | g_k(d) |
|---|---|---|---|---|
| Family 1 | 286 | all odd k | B(1,19,-1) X(4,18,+2)[Δ=-3] X(11,11,-2) L(14,6,+1) U(16,2,0) | **0** |
| Family 2 | 259 | yes | B(2,17,-1) X(7,14,+3)[m>n, Δ=0] X(8,13,-3)[m>n, Δ=0] L(13,6,+1) | **0** |
| Family 3 | 274 | no (k mod 4 ≠ 1) | B(2,18,0) X(7,15,-5)[Δ=-1] X(8,14,+2)[Δ=-1] L(13,7,-1) | **-4** |

**k = 21** (NOT a prime power; k mod 4 = 1)

| family | d | class | terms (n,m,φ) | g_k(d) |
|---|---|---|---|---|
| Family 1 | 526 | all odd k | B(1,25,-1) X(8,22,+6)[Δ=-2] X(13,17,-6)[Δ=-1] L(20,6,+1) U(22,2,0) | **0** |
| Family 2 | 487 | no (k mod 4 ≠ 3) | B(2,23,0) X(5,22,+7)[Δ=-1] X(16,11,-2) L(19,6,+1) | **6** |
| Family 3 | 508 | yes | B(2,24,+1) X(5,23,-7)[Δ=+2] X(16,12,+3) L(19,7,-1) | **-4** |

**k = 25** (prime power; k mod 4 = 1)

| family | d | class | terms (n,m,φ) | g_k(d) |
|---|---|---|---|---|
| Family 1 | 726 | all odd k | B(1,29,-1) L(24,6,+1) U(26,2,0) | **0** |
| Family 2 | 679 | no (k mod 4 ≠ 3) | B(2,27,0) L(23,6,+1) | **1** |
| Family 3 | 704 | yes | B(2,28,+1) L(23,7,-1) | **0** |

**k = 27** (prime power; k mod 4 = 3)

| family | d | class | terms (n,m,φ) | g_k(d) |
|---|---|---|---|---|
| Family 1 | 838 | all odd k | B(1,31,-1) L(26,6,+1) U(28,2,0) | **0** |
| Family 2 | 787 | yes | B(2,29,-1) L(25,6,+1) | **0** |
| Family 3 | 814 | no (k mod 4 ≠ 1) | B(2,30,0) L(25,7,-1) | **-1** |

**k = 33** (NOT a prime power; k mod 4 = 1)

| family | d | class | terms (n,m,φ) | g_k(d) |
|---|---|---|---|---|
| Family 1 | 1222 | all odd k | B(1,37,-1) X(10,34,+16)[Δ=-10] X(23,21,-8) L(32,6,+1) U(34,2,0) | **8** |
| Family 2 | 1159 | no (k mod 4 ≠ 3) | B(2,35,0) X(13,30,+21)[Δ=+3] X(20,23,-9)[m>n, Δ=0] L(31,6,+1) | **13** |
| Family 3 | 1192 | yes | B(2,36,+1) X(13,31,-21)[Δ=-1] X(20,24,+10)[Δ=-1] L(31,7,-1) | **-11** |

**k = 35** (NOT a prime power; k mod 4 = 3)

| family | d | class | terms (n,m,φ) | g_k(d) |
|---|---|---|---|---|
| Family 1 | 1366 | all odd k | B(1,39,-1) X(6,38,+9)[Δ=-28] X(29,15,-4) L(34,6,+1) U(36,2,0) | **5** |
| Family 2 | 1299 | yes | B(2,37,-1) X(12,33,-20)[Δ=+5] X(23,22,+8) L(33,6,+1) | **-12** |
| Family 3 | 1334 | no (k mod 4 ≠ 1) | B(2,38,0) X(12,34,+19)[Δ=-7] X(23,23,-9) L(33,7,-1) | **9** |


Reading the table: for odd prime powers k ≥ 9 each family in its class has the two (or three) terms B, L (U) all stable, e.g. k = 9: Family 3 gives (2,12,+1) + (7,7,−1) = 0. The family value at a *wrong* class is non-zero (Family 2 at k ≡ 1 mod 4 gives +1, Family 3 at k ≡ 3 mod 4 gives −1), as the formulas predict. Composite k (15, 21, 33, …) have extra roots X, which is the subject of §3.

## 2. Task 2: structured d with zero families

### 2.1 Theorem 2 (classification of uniform zero families; Category A)

Let b ∈ {1, 2}, j ∈ ℤ, d = k²+jk+b², and K = max(j+3b, 2b+1, −j). Let k ≥ K be an odd prime power. Then g_k(d) = φ_b(k+j) + [j ≥ −2b]·c_{j+2b} + [j ≥ 2b]·c_{j−2b}, and g_k(d) = 0 exactly in these cases:

- **b = 1:** j ∈ {−2, −1, 1, 4}, all odd prime powers k. (d = (k−1)², k²−k+1, k²+k+1, (k+2)²−3.) No other j.
- **b = 2:** the class of k mod 4 below, for −4 ≤ j ≤ 3, and for every j ≤ −5 one class; no zero for j ≥ 4.

| j | −4 | −3 | −2 | −1 | 0 | 1 | 2 | 3 | j ≤ −5 | j ≥ 4 |
|---|---|---|---|---|---|---|---|---|---|---|
| k mod 4 | 1 | 3 | 1 | 1 | 1 | 3 | 3 | 1 | 1 if j ≡ 1, 2 (mod 4); 3 if j ≡ 0, 3 (mod 4) | none |

*Proof.*
1. *Roots.* n² ≡ b² (mod p^a) with p odd, p ∤ b: p cannot divide both n−b and n+b (it would divide 2b), so n ≡ ±b (mod k).
2. *Which n ≤ √d.* For k ≥ K: n = b occurs (k+j ≥ 0 means d ≥ b²); n = k−b occurs iff j ≥ −2b (d ≥ (k−b)² ⇔ (j+2b)k ≥ 0); n = k+b occurs iff j ≥ 2b; n = 2k−b does not occur (d < (2k−b)² ⇔ j < 3k−4b; for j ≥ 0, k ≥ j+3b gives j ≤ k−3b < 3k−4b, and for j < 0, k ≥ 2b+1 gives 3k−4b ≥ 2b+3 > j); and b < k−b, so the three values are distinct. Any n ≡ ±b is b, k−b, k+b, 2k−b, … so these are all.
3. *Values.* The term n = b has m = k+j, value φ_b(k+j) by Lemma 1. The term n = k−b has m = j+2b ≤ k−b = n, so by stabilisation it is c_{j+2b}. The term n = k+b has m = j−2b ≤ n, value c_{j−2b}.
4. *b = 1.* φ_1(k+j) = (−1)^{j+1} (k odd) and c_m = (−1)^m q(m), so g = (−1)^j[−1 + [j ≥ −2] q(j+2) + [j ≥ 2] q(j−2)]. For j ≤ −3 this is ±1. For j = −2, −1, 1 the bracket is −1+q(0), −1+q(1), −1+q(3) = 0. For j = 0: −1+q(2) = −1. For j = 2, 3: −1+q(j+2)+q(j−2) = 1. For j = 4: −1+q(6)+q(2) = 0. For j ≥ 5 both q(j+2), q(j−2) ≥ 1 (Lemma 3), so the bracket is ≥ 1.
5. *b = 2.* For −4 ≤ j ≤ 3 the value is φ_2(k+j) + c_{j+4} + [j ≥ 4]c_{j−4}, and the zero condition is φ_2(k+j) = −c_{j+4}: j = −4: c_0 = 1, need φ_2 = −1, i.e. k+j ≡ 1, k ≡ 1; j = −3: c_1 = −1, need k−3 ≡ 0, k ≡ 3; j = −2: c_2 = 0, need φ_2(k−2) = 0, i.e. k−2 ≡ 2, 3, k odd gives k ≡ 1; j = −1: c_3 = −1, need k−1 ≡ 0, k ≡ 1; j = 0: c_4 = 1, need k ≡ 1; j = 1: c_5 = −1, need k+1 ≡ 0, k ≡ 3; j = 2: c_6 = 1, need k+2 ≡ 1, k ≡ 3; j = 3: c_7 = −1, need k+3 ≡ 0, k ≡ 1. For j ≥ 4, c_{j+4} and c_{j−4} have the same sign, so |c_{j+4}+c_{j−4}| = q(j+4)+q(j−4) ≥ 2 (Lemma 3), while |φ_2| ≤ 1: no zero. For j ≤ −5 only n = 2 contributes, and φ_2(k+j) = 0 iff k+j ≡ 2, 3 (mod 4), which for odd k selects the class stated. ∎

**Checks.** The formula in the first line of the theorem was compared with the exact scan for every odd prime power 3 ≤ k ≤ 500 with k ≥ K and every j ∈ [−8, 16], b = 1, 2: 5121 cases, 0 mismatches (`check_theorem.py`, `check_theorem.out`). The scan itself (`scan.py`) was checked against an independent direct q-series expansion of Σ q^{n²}/(−q^k;q^k)_n for k ≤ 40 and k = 47, 61, 63, 77 over the whole (j, c) grid: 125 130 values compared, 0 mismatches (`verify_scan.py`).

### 2.2 The 16 families with j ∈ [−8, 8] (b = 1: j = −2, −1, 1, 4; b = 2: j = −8..3) and their exceptional prime powers

Exceptions are the in-class odd prime powers k < K (the only ones not covered by the proof) whose actual g_k(d) is nonzero, computed exactly; "g = 0" lists in-class odd prime powers below K that vanish anyway.

| j | c | d | zero for odd prime powers k ≡ | threshold K=max(j+3b, 2b+1, −j) | in-class odd prime powers k<K, d≥0, with g≠0 | in-class odd prime powers k<K with g=0 |
|---|---|---|---|---|---|---|
| -2 | 1 | k^2-2k+1 | all odd | 3 | — | — |
| -1 | 1 | k^2-k+1 | all odd | 3 | — | — |
| 1 | 1 | k^2+k+1 | all odd | 4 | [3] | — |
| 4 | 1 | k^2+4k+1 | all odd | 7 | [3] | [5] |
| -8 | 4 | k^2-8k+4 | 3 mod 4 | 8 | — (d<0 or no root: [3, 7]) | — |
| -7 | 4 | k^2-7k+4 | 1 mod 4 | 7 | — (d<0 or no root: [5]) | — |
| -6 | 4 | k^2-6k+4 | 1 mod 4 | 6 | — (d<0 or no root: [5]) | — |
| -5 | 4 | k^2-5k+4 | 3 mod 4 | 5 | — (d<0 or no root: [3]) | — |
| -4 | 4 | k^2-4k+4 | 1 mod 4 | 5 | — | — |
| -3 | 4 | k^2-3k+4 | 3 mod 4 | 5 | — | [3] |
| -2 | 4 | k^2-2k+4 | 1 mod 4 | 5 | — | — |
| -1 | 4 | k^2-k+4 | 1 mod 4 | 5 | — | — |
| 0 | 4 | k^2+4 | 1 mod 4 | 6 | [5] | — |
| 1 | 4 | k^2+k+4 | 3 mod 4 | 7 | [3] | — |
| 2 | 4 | k^2+2k+4 | 3 mod 4 | 8 | [3, 7] | — |
| 3 | 4 | k^2+3k+4 | 1 mod 4 | 9 | [5] | — |

Facts read off this table:
- Every exception lies in {3, 5, 7}. Every exception is below K. Thresholds are j+3b: 4, 7 (b = 1) and 5, 5, 5, 5, 6, 7, 8, 9 (b = 2, j = −4..3, with the extra constraint k ≥ −j and k ≥ 2b+1).
- Not every odd prime power below K fails: Family 1 at k = 5 and the family d = k²−3k+4 at k = 3 are rescued by S(1) = 0 or by small coincidences.
- Boundary families (j < −2b, i.e. d < (k−b)², only the term n = b survives) for b = 2: g = φ_2(k+j), which is exactly zero in one class mod 4 for each j ≤ −5. They are "trivial" in the sense that no cancellation occurs; they are the reason the scan reports a zero at j = −8, c = 4 etc.
- For j ≥ 5 (b = 1) and j ≥ 4 (b = 2) no zero exists for k ≥ K, at any fixed j.
- Translation to (k+a)²−b: j = 2a, c = a²−b. The zero families of this shape are: (k−1)² [c = 1, a = −1], (k+2)²−3 [c = 1, a = 2], (k−4)²−12 [c = 4, k ≡ 3 mod 4], (k−3)²−5 [k ≡ 1], (k−2)² [k ≡ 1], (k−1)²+3 [k ≡ 1], k²+4 [k ≡ 1], (k+1)²+3 [k ≡ 3]. Odd j (k²+k+1, k²−k+1, k²−3k+4 [k ≡ 3], k²−k+4, k²+k+4, k²+3k+4) are not of the form (k+a)²−b with integer a.

### 2.3 Even k, the b = 0 case, and b ≥ 3

**Proposition 3 (k = 2p^a, p odd prime; Category A for k ≥ K).** The roots of n² ≡ b² (mod 2p^a) for b = 1 (n odd) and b = 2 (n even) are again n ≡ ±b (mod k), so the proof of Theorem 2 applies with k even (k ≡ 2 mod 4).
- b = 1: g = (−1)^j[1 + q(j+2)[j ≥ −2] + q(j−2)[j ≥ 2]] for j ≥ −2, and ±1 for j ≤ −3. Never zero. (A47 Proposition 4 is the case j = 4.)
- b = 2: for −4 ≤ j ≤ 3 the needed values of φ_2(k+j) (−1, +1, 0, +1, −1, +1, −1, +1 for j = −4..3) never match the actual value, because k+j ≡ j+2 (mod 4) gives (0, 0, 1, −1, 0, 0, 1, −1). For j ≥ 4 no zero as before. For j ≤ −5 the single term φ_2(k+j) = 0 iff j ≡ 0, 1 (mod 4).
- Check: all k = 2p^a, 10 ≤ k ≤ 500, j = −8..16: b = 1 zeros 0/1500; b = 2, j = −4..16 zeros 0/1260; b = 2, j = −8..−5 zero exactly when j ≡ 0, 1 mod 4 (240/240 agree).

**b = 0 (c = 0, d = k(k+j)).** For squarefree k, k | n² forces k | n. If j < 0 (and k > −j) only n = 0 is possible, φ_0(k+j) = 0, so g = 0 for all squarefree k: trivial boundary zeros (d < k²). If j ≥ 0 and k ≥ j: g = φ_k(j) = c_j, which vanishes iff j = 2 (c_j = 0 only at j = 2, since q(j) ≥ 1 otherwise; Lemma 3). That is A46's Claim 1. In the scan the b = 0 patterns are exactly j = 2 and j < 0, on squarefree k only.

**b ≥ 3 (finiteness; sketch, not Category A).** For fixed j, b ≥ 3 the zero condition is φ_b(k+j) = −(c_{j+2b} + [j ≥ 2b]c_{j−2b}), a fixed number, while A_b(m) = |φ_b(m)| grows like m^{⌈b/2⌉−1}·(positive constant) (the denominator ∏_{b/2<i≤b}(1−x^{2i}) of P_b(−x) has a pole of order ⌈b/2⌉ ≥ 2 at x = 1, and every other pole has smaller order). So each fixed (j, b ≥ 3) has finitely many zeros k. This is the reason no infinite family exists beyond b ≤ 2, but the argument is ineffective. Data: all zeros of c ∈ {9, 16, 25, 36, 49}, j = −8..16, k ≤ 500 (odd and even) are clusters; the largest zero k per b are 47 (b = 3, j = 15), 139 (b = 4, j = 16), 16 (b = 5), 36 (b = 6), 15 (b = 7); b = 4 with j = 8 (d = (k+4)²) has odd prime power zeros exactly at k = 49, 59, 61, where |φ_4(k+8)| = A_4(57), A_4(67), A_4(69) = 6 = c_16 + 1 in absolute value, and j = 16 has k = 131, 139. The cluster position moves right as j grows, consistent with "φ_b(k+j) equals a fixed number only for k+j in a short window".

### 2.4 The search

- **Grid:** k = 2..500 (all k, even too), j = −8..16, c = −60..60 (3025 pairs per k). Exact integers (`scan.py`): φ_n(m) built by φ_n(m) = φ_{n−1}(m) − φ_n(m−n); g_k(d) accumulated over all n ≤ √d with k | d−n². "Allowed" means some n exists; non-allowed d (sum empty) are excluded. entries per (k, j, c): 1 002 402 not allowed or d < 0, 504 128 allowed with g ≠ 0, 8 995 allowed with g = 0.
- **Pattern rule** (`analyze.py`): for each (j, c) and each type (odd prime power, odd non-prime-power, even), each modulus M ∈ {1, 2, 3, 4, 5, 6, 8, 12, 16, 24} and residue r, require ≥ 8 allowed and ≥ 8 zero k with k ≥ 70 and zero fraction ≥ 90%.
- **Result:** 61 minimal patterns, all in these groups:
  1. odd prime powers, c = 1: j = −2, −1, 1, 4, 84/84 zeros for k ≥ 70;
  2. odd prime powers, c = 4: j = −8..3, one class mod 4 each, 42/42 zeros;
  3. c = 0 patterns: odd prime powers j = 2, −8..−1 on prime k (76/84, non-squarefree k excluded), odd composites and even k on classes mod 3 / mod 12, 24 that reflect squarefreeness (zero fractions 27/30 etc., the non-zeros are the non-squarefree k: 175, 325, 475, 245, 275, 425, 250, 490, 350).
- **No other pattern.** Among all non-known (j, c) with ≥ 10 allowed k ≥ 70, the best zero fraction among odd prime powers is 4/84 (4.8%, c = 16, j = 12, 15), for odd non-prime-powers 1/29, for even k 1/54 (`analyze2.py`). The 8 zeros with k ≥ 100 in all non-known families are: (j, c) = (15, 16): k = 101, 103, 107; (16, 16): 131, 139; (−8, −16): 100; (1, 28), (2, 28): 108. These are the b = 4 clusters and isolated sporadic hits.
- **Extended range for the 34 uniform families** (b = 1, 2, j = −8..8; k = 3..2000; two-prime residues mod 2⁶¹−1 and 10¹⁸+3, `ext.py`; nonzero residue certifies nonzero exactly): the zero set among odd prime powers is exactly the predicted one for every family; there are no other odd zeros than the non-prime-power zeros k = 15, 21 listed in §3.3.

## 3. Task 3 and the 15 / 21 question

### 3.1 Terms at k = 15 and k = 21 in every vanishing family (exact)

Roles: B = n = b, L = n = k−b, U = n = k+b, X = extra root of n² ≡ d (mod k). `[Δ=x]` = φ_n(m) − c_m for m > n.

| k | family (j,c) | terms ROLE(n,m,φ), Δ vs c_m | g |
|---|---|---|---|
| 15 | (-8,1) | B(1,7,-1) X(4,6,+1)[Δ=0] | 0 |
| 15 | (-1,1) | B(1,14,+1) X(4,13,-1)[Δ=+2] X(11,6,+1) L(14,1,-1) | 0 |
| 15 | (1,1) | B(1,16,+1) X(4,15,-2)[Δ=+2] X(11,8,+2) L(14,3,-1) | 0 |
| 15 | (4,1) | B(1,19,-1) X(4,18,+2)[Δ=-3] X(11,11,-2) L(14,6,+1) U(16,2,0) | 0 |
| 15 | (-8,4) | B(2,7,0) X(7,4,+1) X(8,3,-1) | 0 |
| 15 | (-5,4) | B(2,10,0) X(7,7,-1) X(8,6,+1) | 0 |
| 15 | (-3,4) | B(2,12,+1) X(7,9,-2)[Δ=0] X(8,8,+2) L(13,1,-1) | 0 |
| 15 | (-2,4) | B(2,13,-1) X(7,10,+2)[Δ=0] X(8,9,-1)[Δ=+1] L(13,2,0) | 0 |
| 15 | (2,4) | B(2,17,-1) X(7,14,+3)[Δ=0] X(8,13,-3)[Δ=0] L(13,6,+1) | 0 |
| 21 | (-8,1) | B(1,13,-1) X(8,10,+2)[Δ=0] X(13,5,-1) | 0 |
| 21 | (-7,1) | B(1,14,+1) X(8,11,-2)[Δ=0] X(13,6,+1) | 0 |
| 21 | (-6,1) | B(1,15,-1) X(8,12,+2)[Δ=-1] X(13,7,-1) | 0 |
| 21 | (-5,1) | B(1,16,+1) X(8,13,-3)[Δ=0] X(13,8,+2) | 0 |
| 21 | (0,1) | B(1,21,-1) X(8,18,+4)[Δ=-1] X(13,13,-3) L(20,2,0) | 0 |
| 21 | (1,1) | B(1,22,+1) X(8,19,-4)[Δ=+2] X(13,14,+4)[Δ=+1] L(20,3,-1) | 0 |
| 21 | (4,1) | B(1,25,-1) X(8,22,+6)[Δ=-2] X(13,17,-6)[Δ=-1] L(20,6,+1) U(22,2,0) | 0 |
| 21 | (8,1) | B(1,29,-1) X(8,26,+7)[Δ=-5] X(13,21,-9)[Δ=-1] L(20,10,+2) U(22,6,+1) | 0 |

Observations:
- In every row the X terms, which exist only because k is composite, cancel the remainder of B + L + U (in Family 1 the baseline B + L + U is −1 + 1 + 0 = 0, so the X pair cancels by itself, as in A47; in the boundary rows such as (−8, 1) at k = 15, a single X term cancels B).
- The coincidences are different in each family. Family 2 at k = 15: X(7,14,+3) + X(8,13,−3) with Δ = 0 on both; this is c_14 + c_13 = 3 − 3 = 0, i.e. **q(13) = q(14) = 3** (a plateau of q; by A50 Lemma 2 q is strictly increasing from 26 on). Family 1 at k = 15: φ_4(18) = 2 is a heavily truncated value (stable value c_18 = 5, Δ = −3) that happens to equal |c_11| = 2. Family 1 at k = 21: φ_8(22) = 6 (Δ = −2) = |φ_13(17)| = 6 (Δ = −1). All the numbers involved are ≤ 9.
- So for composite k the stabilisation threshold is not what fails (n = k−b ≥ 14 ≫ 6, 7): the extra roots s, k−s have m's that are small enough for q-plateaus or truncated counts to coincide.

### 3.2 Family 1 pair magnitudes for odd non-prime-powers k ≤ 105 (exact; each pair contributes A_{k−s} − A_s with the sign of A47 Corollary 3)

| k | factorisation | extra pairs (s,k−s): (A_s(m1), A_{k−s}(m2)) | extra-pair sum | g_k((k+2)^2−3) |
|---|---|---|---|---|
| 15 | 3·5 | (4,11): (2,2) | 0 | 0 |
| 21 | 3·7 | (8,13): (6,6) | 0 | 0 |
| 33 | 3·11 | (10,23): (16,8) | 8 | 8 |
| 35 | 5·7 | (6,29): (9,4) | 5 | 5 |
| 39 | 3·13 | (14,25): (29,14) | 15 | 15 |
| 45 | 3^2·5 | (19,26): (52,25) | -27 | -27 |
| 51 | 3·17 | (16,35): (77,20) | 57 | 57 |
| 55 | 5·11 | (21,34): (115,36) | -79 | -79 |
| 57 | 3·19 | (20,37): (115,35) | 80 | 80 |
| 63 | 3^2·7 | (8,55): (57,6) | 51 | 51 |
| 65 | 5·13 | (14,51): (179,17) | 162 | 162 |
| 69 | 3·23 | (22,47): (269,49) | 220 | 220 |
| 75 | 3·5^2 | (26,49): (370,78) | 292 | 292 |
| 77 | 7·11 | (34,43): (301,169) | 132 | 132 |
| 85 | 5·17 | (16,69): (612,25) | 587 | 587 |
| 87 | 3·29 | (28,59): (795,107) | 688 | 688 |
| 91 | 7·13 | (27,64): (1248,98) | -1150 | -1150 |
| 93 | 3·31 | (32,61): (1049,168) | 881 | 881 |
| 95 | 5·19 | (39,56): (968,311) | -657 | -657 |
| 99 | 3^2·11 | (10,89): (374,9) | 365 | 365 |
| 105 | 3·5·7 | (29,76): (2811,133); (34,71): (2117,223); (41,64): (1771,407) | -2148 | -2148 |

The magnitudes are equal at 15 and 21; the ratio A_s / A_{k−s} is 2, 2.25, 2.07 at 33, 35, 39, 2.08 at 45, 3.85 at 51, 9.5 at 63 and 1.78 at 77 (not monotone, but never near 1 again). A47 reports min log ratio 0.577 at k = 77 for all r = 2, k > 21, k ≤ 1001, and A50 extends to 11000.

### 3.3 Zeros at non-prime-power k in all 34 uniform families

### Zeros at k not an odd prime power (k ≤ 2000, two-prime residue test; exact re-evaluation for k ≤ 500 in the scan)

| family (j,c) | zero k that are odd non-prime-powers | zero k that are even |
|---|---|---|
| (-8,1) | [15, 21] | [] |
| (-7,1) | [21] | [8] |
| (-6,1) | [21] | [8] |
| (-5,1) | [21] | [8] |
| (-4,1) | — | [] |
| (-3,1) | — | [] |
| (-2,1) | — | [8] |
| (-1,1) | [15] | [8] |
| (0,1) | [21] | [] |
| (1,1) | [15, 21] | [] |
| (2,1) | — | [8] |
| (3,1) | — | [] |
| (4,1) | [15, 21] | [] |
| (5,1) | — | [] |
| (6,1) | — | [] |
| (7,1) | — | [] |
| (8,1) | [21] | [] |
| (-8,4) | [15] | [10, 12, 14, 18, 22, 26, 34, 38, 46, 50, 54, 58, 62, 74]…(184 total) |
| (-7,4) | — | [10, 14, 18, 22, 26, 34, 38, 46, 50, 54, 58, 62, 74, 82]…(183 total) |
| (-6,4) | — | [8] |
| (-5,4) | [15] | [8] |
| (-4,4) | — | [12] |
| (-3,4) | [15] | [12] |
| (-2,4) | [15] | [4, 8] |
| (-1,4) | — | [] |
| (0,4) | — | [4, 12] |
| (1,4) | — | [6] |
| (2,4) | [15] | [] |
| (3,4) | — | [8] |
| (4,4) | — | [12] |
| (5,4) | — | [12] |
| (6,4) | — | [] |
| (7,4) | — | [4] |
| (8,4) | — | [4] |

Over all 34 families (b = 1, 2; j = −8..8) and all k ≤ 2000, the odd non-prime-power zeros are only k = 15 and 21 (nine and eight families respectively, see §3.1). The even-k zeros listed are the boundary families (k = 2p^a, j ≤ −5) and tiny k.

### 3.4 Sporadic zero rate versus k (is 15, 21 special?)

For every non-uniform family in three families of grids, the share of allowed d at a given k with g_k(d) = 0 ("sporadic zero rate"). Window A: j = 0..6, c = −6..8 (98 pairs, excluding the 7 uniform ones). Window B: (k+a)²−b, a = 1..6, b = −6..8. Full grid: j = −8..16, c = −60..60, c ≠ 0, excluding uniform families (c ≥ 9 makes small k unrepresentative, so read the full grid as a trend only).

| k | factorisation | window A: zeros/allowed | window B: zeros/allowed | full grid: zeros/allowed |
|---|---|---|---|---|
| 9 | 3^2 | 7/35 (20%) | 1/36 (3%) | 217/1205 (18%) |
| 11 | 11 (prime) | 5/42 (12%) | 3/43 (7%) | 347/1578 (22%) |
| 13 | 13 (prime) | 3/42 (7%) | 3/45 (7%) | 314/1530 (21%) |
| 15 | 3·5 | 4/35 (11%) | 3/33 (9%) | 263/1184 (22%) |
| 17 | 17 (prime) | 9/49 (18%) | 6/44 (14%) | 307/1584 (19%) |
| 19 | 19 (prime) | 8/49 (16%) | 5/43 (12%) | 277/1559 (18%) |
| 21 | 3·7 | 7/42 (17%) | 4/33 (12%) | 191/1109 (17%) |
| 23 | 23 (prime) | 7/49 (14%) | 3/43 (7%) | 202/1534 (13%) |
| 25 | 5^2 | 2/42 (5%) | 1/36 (3%) | 114/1284 (9%) |
| 27 | 3^3 | 0/35 (0%) | 0/34 (0%) | 61/1184 (5%) |
| 29 | 29 (prime) | 0/63 (0%) | 2/46 (4%) | 112/1534 (7%) |
| 31 | 31 (prime) | 0/56 (0%) | 0/48 (0%) | 72/1509 (5%) |
| 33 | 3·11 | 0/35 (0%) | 0/30 (0%) | 21/1034 (2%) |
| 35 | 5·7 | 0/28 (0%) | 0/27 (0%) | 19/1009 (2%) |
| 37 | 37 (prime) | 0/49 (0%) | 0/45 (0%) | 63/1434 (4%) |
| 39 | 3·13 | 0/28 (0%) | 0/31 (0%) | 26/1009 (3%) |
| 41 | 41 (prime) | 0/63 (0%) | 0/46 (0%) | 63/1484 (4%) |
| 43 | 43 (prime) | 0/42 (0%) | 0/43 (0%) | 48/1509 (3%) |
| 45 | 3^2·5 | 0/21 (0%) | 0/21 (0%) | 0/784 (0%) |

Aggregates (zeros/allowed):
- Window A: composites {15, 21}: 11/77 = 14.3%; primes {17, 19, 23}: 24/147 = 16.3%.
- Window B: {15, 21}: 7/66 = 10.6%; {17, 19, 23}: 14/130 = 10.8%.
- Full grid: {15, 21}: 454/2293 = 19.8%; {17, 19, 23}: 786/4677 = 16.8%.
- Beyond k = 25 there are no sporadic zeros at all in window A up to k = 500; window B has six entries beyond 25, at k = 29 (two), 36, 49, 59, 61 (the last three are the b = 4, j = 8 cluster).

The composite numbers 15 and 21 behave exactly like the primes of the same size. The sporadic zero rate depends on the size of k (values of q and truncated counts are small), not on whether k is prime. Conversely the next odd non-prime-powers, 33 = 3·11, 35 = 5·7, 39 = 3·13, have rates ≤ 3%, like the primes of that size, so the data do not support "3·5 and 3·7 because 3, 5, 7 are exceptional".

### 3.5 What is proved, what is numerical, what is explained

**Proved (Category A).**
- Theorem 1: exact failure sets of the three families among odd prime powers (Family 1: {3}; Family 2: {3, 7}; Family 3: {5}), with the term-level reason for each failure (§1.3): truncation correction at k = 3 (Family 1), k = 7 (Family 2), k = 5 (Family 3); extra root n = 2k−2 at k = 3 (Family 2).
- Theorem 2: the complete classification of zero families d = k²+jk+b², b ∈ {1, 2}, over odd prime powers k ≥ K = max(j+3b, 2b+1, −j), for every integer j, including all new families listed in §0 item 3, and the exact exception sets below K for −8 ≤ j ≤ 8 (finite exact evaluations).
- Proposition 3 (k = 2p^a) and the b = 0 case.
- Verification ranges: exact integer scan, all k ≤ 500, all 3025 (j, c); residue test for 34 families to k = 2000; Lemma 2 for n ≤ 150, m ≤ 300; 5121 comparisons of the formula against exact data, 0 mismatches.

**Numerical pattern (not proved).**
- No infinite zero family for c not in {0, 1, 4} in the window (zero rate ≤ 5% for non-square c; finite clusters for b ≥ 3; finiteness for b ≥ 3 has only an ineffective sketch).
- Odd non-prime-power zeros of the 34 families are exactly {15, 21} for k ≤ 2000 (not proved for all k; A47 and A50 give the Family 1 evidence to 5000 / 11000 and a proof for a subset of k).
- Even k: no zeros in the uniform families except the boundary families and k < 15.
- The decay of the sporadic zero rate with k.

**Is the 15 / 21 link to {3, 5, 7} explained?**
- The prime-power exceptions {3, 5, 7} are explained exactly by one mechanism (truncation correction S ≠ 0 below the stabilisation threshold, plus one extra-root accident at k = 3). That is a proof.
- k = 15, 21 are *not* explained by that mechanism: the threshold terms are stable there, and the zeros come from the extra roots that exist only for composite k.
- They are explained at the level of terms as small-number coincidences between an X pair (different in each family, §3.1) and they behave like primes of the same size in the sporadic-zero statistics (§3.4). 15 and 21 are the two smallest odd non-prime-powers; the "product of 3 with 5 and 7" description is a restatement of "smallest", not a mechanism (35, 45, 63, 75, 105 are not zeros, and 9, 27, 81 behave generically).
- Verdict: the two phenomena share only the *size* effect (both occur below ≈ 25), not a common cause. A proof that no further non-prime-power k vanishes is not available; the numerical evidence (min pair ratio ≥ 1.78 for k > 21, k ≤ 11000; no zeros in 34 families for k ≤ 2000) supports "coincidence".

## 4. Files (all in `A55_small_k_exceptions/`)

`lib.py` (exact φ_n(m), g_k(d)), `scan.py` + `scan_status_500.npy` (grid), `verify_scan.py` (independent series check), `analyze.py`, `analyze2.py`, `analyze3.py`, `rates.py` (+ `patterns.json`, `patterns_raw.json`, `composite_zeros_all.json`, `rates.json`), `ext.py` + `ext_zeros_2000.json` (k ≤ 2000), `check_theorem.py` + `check_theorem.out` + `theoremU_check.json`, `gen_tables*.py` and the generated `tables_*.md`, `template.md`, `build.py`, `mk_pdf.py`, `REPORT.md`, `REPORT.pdf`.
