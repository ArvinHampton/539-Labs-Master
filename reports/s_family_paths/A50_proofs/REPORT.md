# A50: proof work on g_k — k = 0 mod 4 MIX classes, and the composite-zero gap

**For:** Arvin Hampton · 2026-10-22 (CDT). All files are new and live in `A50_proofs/`. Every run used `nice`, OMP_NUM_THREADS=1 and `ulimit -v` 3 GB. No TPC or RH claims. Category A below means fully proved; every computer check states its range.

Notation: g_k(q)=Σ q^{n²}/(−q^k;q^k)_n, g_k(d)=[q^d]g_k; φ_n(m)=[x^m]∏_{j≤n}(1+x^j)^{-1}; A_n(m)=|φ_n(m)|=(−1)^mφ_n(m) (distinct odd parts ≤ n times a multiset of even parts 2i, n/2<i≤n); Q(m)=q_odd(m)=#partitions of m into distinct odd parts, c_m=(−1)^mQ(m).

## Summary

| Part | Result | Status |
|---|---|---|
| 1 | The class d≡0 (mod 4) of g_4 is exactly F(q⁴), F(Q)=Σ Q^{n²}/(−Q;Q)_{2n}. Mod 2, F is the Slater-type product 1/((Q;Q²)_∞(Q⁴,Q¹⁶;Q²⁰)_∞). So g_4(d)≠0 whenever that partition count is odd. | Category A |
| 1 | Exact alternating-sum form (−1)^D h(D)=Σ_ℓ(−1)^ℓ A_{2ℓ}(D−ℓ²). The terms are exponentially larger than the result, so no termwise dominance argument can work. | Category A (formula); size claim numerical |
| 1 | No sparse Hecke-type or product form found. The Bailey partner α_n is not a Laurent polynomial. Precise requirement for a proof stated (§1.4). | obstruction |
| 1 | Data for k=4,8,12,16: k=4 has a pure sign law (period 16 in d), no slips to d<8·10⁴. k=8 (c=1) and k=12 (c=0,4) show phase slips at d≈144j² and 324j². | numerical |
| 2 | r=2: A_s(m₁)>A_{k−s}(m₂), hence g_k((k+2)²−3)≠0, is **proved for s odd** in two regimes (u≤t−3, or t≥4 and u≥s+2), for all k not covered by the finite check. About 27% of r=2 values k≤6000. | Category A |
| 2 | Exact formula for A_n(m) for m≤2n+1; Q monotone; u²≥k+4 for the root s. | Category A |
| 2 | Float-certified check: all odd non-prime-power k≤11000: zero set is exactly {15,21}. | computer, range stated |
| 2 | s even, thin band, t≤3, r≥3 in general | not proved |

## 1. Part 1: k=4 (then 8, 12)

### 1.1 Reduction (Category A)

For k=4, n² mod 4 ∈{0,1}. So g_4 has only classes d≡0,1 (mod 4) (class 0 is MIX, class 1 is ONE, as in A44).

*Proof of the split.* Write n=2ℓ (class 0) or n=2ℓ+1 (class 1) and put Q=q⁴:

g_4|_{d≡0} = Σ_ℓ Q^{ℓ²}/(−Q;Q)_{2ℓ} =: F(Q),  g_4|_{d≡1} = q Σ_ℓ Q^{ℓ²+ℓ}/(−Q;Q)_{2ℓ+1}. ∎

F is the sign-free sister of the tenth-order function X(q)=Σ(−1)^n q^{n²}/(−q;q)_{2n}. Write F=Σh(D)Q^D, so g_4(4D)=h(D). Zeros of h (exact, D<20000): D∈{3,5,12,13,15,21,29,35}, i.e. d∈{12,20,48,52,60,84,116,140}, matching A39/A40.

### 1.2 Mod-2 identity (Category A)

**Proposition 1.** h(D) ≡ #{partitions of D into parts that are odd or ≡ ±4 (mod 20)} (mod 2). Hence h(D)≠0 whenever that count is odd.

*Proof.* (−Q;Q)_{2n}≡(Q;Q)_{2n} (mod 2), as power series with integer coefficients. So F≡Σ Q^{n²}/(Q;Q)_{2n}. By the Rogers–Slater mod-20 identity (Slater (79)), Σ Q^{n²}/(Q;Q)_{2n}=1/((Q;Q²)_∞(Q⁴,Q¹⁶;Q²⁰)_∞). ∎

Checked: parity match for all D<20000 (`k4.py`). The odd fraction is 0.4947, so this settles roughly half of all D and cannot give full nonvanishing. This is the only exact modular-type input found.

### 1.3 Structure of the sign and size

Formula (Category A, from sign lemma and the definition): (−1)^D h(D)=Σ_{ℓ≥0}(−1)^ℓ A_{2ℓ}(D−ℓ²).

Numerical facts (not proved):
1. **Sign law.** For every D<20000 the sign of h(D) is (−1)^{D(D−1)/2} (pattern +,+,−,− with period 4), with no violation. Equivalently the sign of g_4(d), d≡0 (mod 4), has period 16 in d and there are no slips for d<8·10⁴ (`k4.py`, `slips.py`). The twisted series Σ|h(D)|Q^D has no product form: its exponent sequence is not eventually of one sign and grows without pattern.
2. **Growth.** log|h(D)|/√D → ≈0.4967 (values 0.481, 0.486, 0.489 at D=4000, 8000, 16000, with 1/√D correction). This matches π/(2√10), i.e. |h(D)|≈exp(π√(D/40)).
3. **Cancellation.** The largest term max_ℓ A_{2ℓ}(D−ℓ²) exceeds |h(D)| by a factor with log ≈ 0.43√D (D=200,500,1000,2000: logs 4.5, 8.4, 12.8, 19.1; `k4terms.py`). So the alternating sum over ℓ cancels exponentially. The envelope is smooth in ℓ, so this is a theta-type cancellation. No termwise argument (largest term, first term, positivity of blocks) can give dominance.

### 1.4 The obstruction and what identity is needed

* **Bailey route fails.** With β_n=1/(−Q;Q)_{2n} the a=1 inversion gives α_n with denominators (1+Q²), (1+Q⁴), … (computed exactly for n≤7 with `bailey_alpha.py`). It is not a Laurent polynomial, so there is no direct Hecke-type double sum from Bailey's lemma. (The mod-2 collapse to Slater is why the product appears only mod 2.)
* **Hecke-type search.** A search for F(Q)·θ = (Hecke double sum Σ_{sg r=sg s} sg(r)(±1)^{r}(±1)^{s}Q^{ar²+brs+cs²+ur+vs}) over a≤c≤6, b≤12, u,v≤8, shifts ≤3, with 12 theta prefactors, matching the first 70 coefficients, found nothing (for F and for Σ|h|Q^D; `hecke_search.py`, needs the coefficient pickle written by `growth_h.py`).
* **Needed (precise).** One of:
  1. a Hecke-type or Appell–Lerch expression for F(Q) (as Choi gave for X, χ), whose transformation at the cusp Q=±i has a dominant term of exact size e^{π√(D/40)} D^{−a} and an error exponentially smaller; or
  2. directly, a circle-method asymptotic for F at Q→±i with exponentially small relative error. The sign period 4 in D says the two dominant singularities are Q=±i with conjugate contributions and a single exponent. This single exponent is the difference from k=8,12 (§1.5).

  Either would give ε_D h(D)>0 for all D≥36, because the main term then has fixed sign and size ≫ error. Without such an identity the MIX phenomenon cannot be beaten by elementary dominance. This is the structural obstruction.

### 1.5 k=8, 12, 16 (numerical)

Exact series to d<6·10⁴ (k=8,12,16; `slips.py`) and to 2·10⁵ for k=4,8,12 (`phasefit.py`):

| k, class | zeros (all d below) | sign behaviour |
|---|---|---|
| 4, c=0 | 12,20,48,52,60,84,116,140 | pure law, period 16, no slip |
| 8, c=1 (MIX) | 9,17,25,49,57,81,249,289,825,1657 | alternates with d/8, with **phase slips** at d≈841, 2769, 4169, 5849, 7809, 10057, … |
| 12, c=0 (MIX) | 12,24,60,120,156,348,396,408 | alternates, slips at d≈444–540, 1608, 3432, 5940, 9132, … |
| 12, c=4 (MIX) | 16,40,52,100,112,148,196,208,292,340,424,436,472,1564 | alternates, slips similar |
| 16, c=0,1,9 | last zeros 2304, 113, 217 | more irregular |

For k=8, c=1 and k=12, c=0 the slip positions follow √d_j ≈ 12j and ≈ 18j (least-squares fit slope 12.00 and 17.98). So the sign flips are those of cos(γ√d+φ) with γ=π/12=2π/(3k) (k=8) and γ=π/18=2π/(3k) (k=12). All zeros lie below the first few slips; no zero in the slip windows up to 2·10⁵ (k=8,12). Reading: in these MIX classes two contributions with the same exponential size interfere, g_k(d)≈A(d)(±1)^{d}cos(γ√d+φ). Nonvanishing for large d then needs (i) the asymptotic with exponentially small error and (ii) a lower bound |cos|≳d^{−N} at integers, which for a phase of the form (algebraic)√d+constant follows from a Liouville-type estimate. This is a plausible route, not a proof. k=4 shows a single dominant term (γ would give slips near 36j², none seen), which is why k=4 is the easier MIX class.

## 2. Part 2: odd non-prime-power k>21

Setup (from A47): d=(k+2)²−3, roots s of s²≡1 (mod k), 1<s<k/2, t=(s²−1)/k, m₁=k+4−t, m₂=4+2s−t, g_k(d)=Σ_s[φ_s(m₁)+φ_{k−s}(m₂)], and (A47 Cor. 3) for r=2 there is one pair and g_k(d)=0 iff A_s(m₁)=A_{k−s}(m₂). New notation: u=k−2s (odd). Then m₁=m₂+u, n₂=k−s=s+u.

### 2.1 Exact tools (Category A)

**Lemma 1 (u bound).** k | u²−4, so u²≥k+4 (u odd, u≥3).
*Proof.* 4(s²−1)=(k−u)²−4≡u²−4 (mod k), and k odd. Since u²−4>0, u²−4≥k. ∎ (Hence the two pair terms are never "adjacent": m₁−m₂≥√(k+4). Both zeros fit: k=15, u=7; k=21, u=5.)

**Lemma 2 (Q monotone).** Q(n+1)≥Q(n) for n≥2.
*Proof.* Injection on distinct-odd partitions λ of n: if 1∉λ send λ→λ∪{1}; if 1∈λ send λ→(λ∖{1}) with its largest part increased by 2 (n≥4). Images of the two classes are disjoint (contain 1 / do not) and each map is injective. n=2,3 direct. ∎ Strictness: a partition of n+1 with no 1 and top two parts L−2, L is not hit by the second map; such partitions exist for n+1≥40, and Q(x+1)>Q(x) for 26≤x<40 is checked exactly (the last non-strict step is x=25), so Q(x+1)>Q(x) for all x≥26 (checked exactly to 3000).

**Lemma 3 (alternating partial sums).** S(y)=Σ_{x≤y}(−1)^xQ(x) satisfies 0≤(−1)^yS(y)≤Q(y).
*Proof.* Q(0)−Q(1)=0 and Q is nondecreasing on x≥2 (Lemma 2), so (−1)^yS(y)=Q(y)−Q(y−1)+… is an alternating sum of nonincreasing nonnegative terms. ∎ (Checked exactly y≤3000.)

**Lemma 4 (exact formula).** For m≤2n+1,
A_n(m)=Q(m)+(−1)^m Σ_{x=0}^{m−n−1}(−1)^xQ(x)  (the sum is empty for m≤n).
In particular A_n(m)=Q(m)+(−1)^{n+1}ε with 0≤ε≤Q(m−n−1) when n<m≤2n+1.
*Proof.* Two evens >n sum to ≥2n+2>m, so at most one even e∈(n,m]. The odd part j>n occurs at most once (two such sum ≥2n+4). Parts of the remaining distinct odd set have sum ≤m−n−1≤n, so they are automatically ≤n and ≠j. Hence A_n(m)=Q(m)−Σ_{odd j∈(n,m]}Q(m−j)+Σ_{even e∈(n,m]}Q(m−e); put x=m−j or m−e. The second statement is Lemma 3 with y=m−n−1 and (−1)^{m+y}=(−1)^{n+1}. ∎ Checked directly n≤80, all m (first failure m=2n+3).

**Lemma 5 (adding evens).** A_n(m)≥A_n(m−D) whenever D is a sum of allowed even parts. For n odd every even D≥n+1 is such a sum.
*Proof.* Adjoin the parts; this is injective. For n odd the allowed evens are {n+1,n+3,…,2n}; j parts give every even number in [j(n+1),2jn], and consecutive ranges overlap since (j+1)(n+1)≤2jn+2 ⇔ (j−1)(n−1)≥0. ∎

### 2.2 Theorem (r=2, s odd; Category A)

**Theorem 6.** Let k be odd with exactly two prime factors, s its root, s odd, with m₂≥26 (this holds for k>168, since m₂>1.5s+4 and s≥14), and t=(s²−1)/k, u=k−2s. If either
(E) u≤t−3, or (D) t≥4 and u≥s+2,
then A_s(m₁)>A_{k−s}(m₂), so g_k((k+2)²−3)≠0.

*Proof.* n₂=k−s is even. Since m₂≤2n₂+1 (because 4s≤2k−2≤2k−3+t), Lemma 4 gives A_{k−s}(m₂)=Q(m₂)−ε₂≤Q(m₂).
(E): m₁≤2s+1, so by Lemma 4 with n=s odd, A_s(m₁)≥Q(m₁)>Q(m₂) (Lemma 2, m₁−m₂=u≥3).
(D): put D=the least even integer ≥max(s+1,u+3−t). Then s+1≤D≤u−1 (needs u≥s+2, t≥4). Lemma 5: A_s(m₁)≥A_s(m₁−D). With m′=m₁−D we have m₂<m′≤2s+1, so Lemma 4 (n=s odd) gives A_s(m′)≥Q(m′)>Q(m₂)≥A_{k−s}(m₂). ∎

The case m₂<26 means k≤168, covered by the exact check below. The proof chain A₁≥Q(m′)≥Q(m₂)≥A₂ was also verified numerically for all 264 qualifying k≤4000 with no violation (`chain_check.py`).

**Coverage** (`cover.py`, odd k≤6000, r=2, 1529 values): (s odd, E)=105, (s odd, D)=307, i.e. 412 (26.9%) proved; the rest are s even (954), or s odd in the narrow band 2.41s≲k≲3s, or t≤3.

### 2.3 What is not proved

* **s even.** Then A₁=Q(m₁)−ε₁ and A₂=Q(m₂)+ε₂ (regime E), so the needed inequality is Q(m₂+u)>Q(m₂)+Q(y₁)+Q(y₂), y₁=m₁−s−1, y₂=m₂−n₂−1. With u²≥k+4 and the classical asymptotic Q(m)~e^{π√(m/6)}/(2·24^{1/4}m^{3/4}) this holds for large k (ratio ≥≈1.8, error terms exponentially smaller), but I did not get an effective error bound, so this is not Category A. Regime D for s even lacks the injection (Lemma 5 needs n odd and the sign of Lemma 4 goes the wrong way).
* **Thin band** u∈[t−2,s+1] and t≤3 (k=s²−1, (s²−1)/2, (s²−1)/3): m₁ lies just above 2s+1 or far above; Lemma 4 no longer applies.
* **r≥3.** The pair signs are (−1)^{t+1}; cancellation between pairs is not excluded by Theorem 6. Numerics: min |total|/max|term|=3·10⁻⁴ (k=7035), no near-misses.
* **Even k** with >1 odd prime or 8|k: nothing new beyond A47 (k=2p^a, g=2); not attempted analytically.

### 2.4 Computer check (stated range)

`scan_pairs.py`: for every odd non-prime-power k, 15≤k≤11000, evaluate each pair term A_s(m₁), A_{k−s}(m₂) with float64 DP. All recurrences are sums of nonnegative terms, so the relative rounding error is ≤≈10⁻¹¹. Results:
* The only k with total 0 are 15 and 21 (exact pairs 2,2 and 6,6).
* For r=2 and k>21: min log(A₁/A₂)=0.577 (k=77) over k≤1001, 0.715 (k=1517) for 1002–6000, 0.728 (k=6557) for 6001–11000, so A₁>1.78·A₂ throughout.
* For r≥3: min |total|/max|pair term| = 1.5·10⁻³ (k=693), 1.8·10⁻³ (k=2093), 2.9·10⁻⁴ (k=7035). All ≫ rounding.
Hence g_k((k+2)²−3)≠0 for all odd non-prime-power k in (21,11000]. Also, a grid over all (s,t) with s≤258 and every odd k=(s²−1)/t>2s (k≤66563, not only k≤11000): inequality fails only for (s,t)=(4,1),(8,3) (`grid.py`).

## 3. Files

`k4.py`, `k4_20000.json` (reduction, mod-2 match, zeros, sign law, D<20000); `k4terms.py`/`.json` (cancellation); `mixscan.py`, `mixsign.py`, `slips.py`, `slips.json`, `phasefit.py`, `k8seq.py`, `mix_k{4,8,12,16}.json` (MIX data); `formula_check.py` (Lemma 4); `bailey_alpha.py`, `hecke_search.py`, `growth_h.py` (Part 1 obstruction and growth); `chain_check.py` (Theorem 6 chain, Lemma 3); `cover.py`, `cover_6000.json`; `scan_pairs.py`, `scan_pairs_*.json`, `scan_*.log`; `grid.py`, `grid2.py`; `REPORT.md`, `REPORT.pdf`.
