# A54: proof work on g_k, continuing A50

**For:** Arvin Hampton · 2026-10-22 (America/Chicago). All files are new and live in `A54_proofs2/`; nothing in A46, A47 or A50 was changed. Runs used `nice`, OMP_NUM_THREADS=1, under 3 GB. No TPC or RH claims. "Category A" means fully proved, with every computer check stated by range. "A\*" means proved except for one cited published bound, named explicitly. Everything else is labelled numerical or obstruction.

Notation as in A50: g_k(q)=Σ q^{n²}/(−q^k;q^k)_n; φ_n(m)=[x^m]∏_{j≤n}(1+x^j)^{-1}; A_n(m)=|φ_n(m)| (partitions into distinct odd parts ≤ n, plus a multiset of even parts 2i with n/2<i≤n); Q(m)=#partitions of m into distinct odd parts. For odd k and a root s of s²≡1 (mod k), 1<s<k/2: t=(s²−1)/k, u=k−2s, m₁=k+4−t, m₂=4+2s−t, A₁=A_s(m₁), A₂=A_{k−s}(m₂). The pair {s,k−s} contributes (−1)^{t+1}(A₁−A₂) to g_k((k+2)²−3), and the sum over pairs is g_k((k+2)²−3) (A50).

## Summary

| Part | Result | Status |
|---|---|---|
| 2 | **For every odd k and every root s with 1<s<k/2: A₁>A₂, except (s,k)=(4,15) and (8,21) where A₁=A₂.** Hence for every odd k with exactly two distinct prime factors, g_k((k+2)²−3)≠0 except k=15, 21 (where it is 0). This covers s even, the thin band and every t (t≤3 included), with no case split on t. | **A\*** (finite check s≤2500 is computer; analytic range s≥1200 uses Chern's explicit error bound for η-quotient coefficients) |
| 2 | Exact check, all pairs with s≤400 (1454 pairs, big integers): only (4,15),(8,21) fail. Long-double chain check, s≤2500 (15 616 pairs): the 29 failures of the crude chain are all s≤32 and are settled by the exact check. | computer, ranges stated |
| 2 | r≥3 odd k: float scan A50 (k≤11000) extended to k≤14000: no flags; zero set of g_k((k+2)²−3) over odd non-prime-power k≤14000 is exactly {15,21}. Termwise dominance (largest pair term > sum of the others) holds for 92.5% of the 939 odd k≤8000 with ω≥3, and fails otherwise, so it cannot be the proof. | numerical; obstruction |
| 3 | **All even k with 8∤k: g_k((k+2)²−3)=2+(positive)≥2 (k≥7), never 0.** | Category A |
| 3 | **k=2^a, a≥3: g_k((k+2)²−3)=2−A₁−A₂<0**, never 0 (g₈=−3, g₁₆=−8, g₃₂=−31, g₆₄=−236, g₁₂₈=−5174, g₂₅₆=−530110). | Category A |
| 3 | 8 divides k, k has an odd part: signs of the pair terms vary with s (mod 2^a). Float scan of all 1000 such k≤8000: never zero, min abs(g)/max-term =1.05e-4 at k=1840; g>0 for 397, g<0 for 603. | numerical; not proved |
| 1 | Mod 2: F(Q)≡(Q;Q)_∞·G(Q⁴), G the Rogers–Ramanujan series (pentagonal numbers times RR); same as A50's Slater product, written in a form that shows the structure. | Category A (identity), verified to Q⁴⁰⁰⁰ |
| 1 | No product form of F mod 3, 4, 5, 7, 8 (600 terms); no product-like sub-progression D≡r (mod M), M≤16, for moduli 3,4,5,7,8,9; no always-zero or never-zero residue class mod m≤80 (D<20000). | numerical, negative |
| 1 | No Bailey/Hecke identity: α″ for the sign-free pair is a dense polynomial while X's is sparse. Obstruction pinned to a ₁φ₁ at the wrong sign. Hecke-form search found nothing. | obstruction |

## 1. Part 1: the k=4 class F(Q)=Σ Q^{n²}/(−Q;Q)_{2n}

### 1.1 Mod 2 in a form that shows the structure (Category A)

Mod 2, (−Q;Q)_{2n}≡(Q;Q)_{2n}, so F≡Σ Q^{n²}/(Q;Q)_{2n}=1/((Q;Q²)_∞(Q⁴,Q¹⁶;Q²⁰)_∞) (Slater (79), as in A50). Now 1/(Q;Q²)_∞=(−Q;Q)_∞≡(Q;Q)_∞ (mod 2) and 1/(Q⁴,Q¹⁶;Q²⁰)_∞=G(Q⁴)=Σ Q^{4n²}/(Q⁴;Q⁴)_n by Rogers–Ramanujan, so

  F(Q) ≡ (Q;Q)_∞ · G(Q⁴) ≡ (Σ_{n∈ℤ} Q^{n(3n−1)/2}) · G(Q⁴)  (mod 2).

Checked by direct series to Q⁴⁰⁰⁰ (`par2.py`). Consequence: h(D) is odd, hence nonzero, exactly when the number of pairs (pentagonal number n(3n−1)/2, partition of the rest into parts ≡±1 mod 5 scaled by 4) of total D is odd. The observed density of odd h(D) is 0.528 (D<600). Remark, not proved here: (Q;Q)_∞G(Q⁴) is, up to a power of Q, a generalized η-quotient, so results of Serre and Bellaïche–Nicolas type on odd coefficients of such products would give ≫√X/log X odd values in D≤X; positive density is not known by these methods.

### 1.2 Reductions mod 3, 4, 5, 7, 8 (numerical, negative)

`prodform.py 600 …`: write h≡∏(1−Q^n)^{−a_n} (mod m) and look for periodic a_n. Mod 2 gives a_n=1 for n odd and n≡±4 (mod 20) (the Slater product). For m=3,4,5,7,8 the exponents are irregular (mod 3: 1,1,1,0,1,0,1,2,0,2,2,2,0,1,1,2,…; the first seven are the product-like 1,1,1,0,1,0,1 and the pattern breaks at n=8). `mod4.py`: F·(Q;Q)_∞^{-1}≡1+2U (mod 4) with U of density ≈0.5 and no product form. `sweep.py`: for each of m∈{3,4,5,7,8,9} and each progression D≡r (mod M), M≤16, 200 terms each, the same test finds nothing. `classes.py`: no residue class mod M≤80 on which h(D) is always, or never, 0 mod m, for m∈{2,3,4,5,7,8,9,16}, D<20000. So no sign-pure or zero-pure subseries was found and no new positive-density nonvanishing set beyond the mod-2 odd set.

### 1.3 Why there is no Bailey/Hecke route (obstruction)

X(q)=Σ(−1)^nq^{n²}/(−q;q)_{2n} is the z=−1 member of the family Σ z^n q^{n²}/(−q;q)_{2n}. Its Bailey pair (p=q², a=1, β′_n=(p;p)_n/(p;p)_{2n}) has sparse α′, and this gives Choi's Hecke form J̄_{1,4}X(q)=f_{2,3,2}(−q³,−q³,q²) and the Appell–Lerch form X(q)=m(−q²,q⁵,q)+m(−q²,q⁵,q⁴) (Hickerson–Mortenson). F is the z=+1 member. The same inversion (`bailey2.py`, `alpha_series.py`, exact rational arithmetic) gives α″_n a polynomial in q whose number of terms grows (n=10: about 60 terms, degree 80), with no recognisable sparse pattern; for the other natural pair β=1/((q;p)_n(−p;p)_n) (`bailey3.py`) α is sparse but is not the pair attached to F. The specific obstruction: F corresponds to a ₁φ₁ evaluated at z=+c/a, whereas the summation formula used for X holds at z=−c/a. Conjugate-Bailey variants, and the tenth-order relations between φ, ψ, X, χ, only relate F's sister X, χ to each other and to q→−q, which sends F to a function with (q;−q) denominators, not to X. A broad search for Hecke forms H with H/F or H/F(−q) a periodic-exponent product (discriminants 5, 20, 45, 80, 125, 180, 320; `hecke2.py`) was stopped after about 18 minutes with no hit; it was never validated against X, so treat it as inconclusive. No circle-method route exists: the coefficients are signed sums of terms exponentially larger than the result (A50 §1.2).

**What would close Part 1:** a Hecke-type or mock-theta expression for F itself (Σ z^n q^{n²}/(−q;q)_{2n} at z=+1), or an explicit-error asymptotic for h(D) accurate to relative precision e^{−c√D}, which no available method gives.

## 2. Part 2: composite zeros at (k+2)²−3, odd k

### 2.1 Theorem and consequence

For every odd k and every root s of s²≡1 (mod k) with 1<s<k/2: A_s(m₁)>A_{k−s}(m₂), except (s,k)=(4,15),(8,21) where they are equal (both 2, resp. both 6).

For odd k with exactly two distinct prime factors there is exactly one such pair, so g_k((k+2)²−3)=±(A₁−A₂)≠0 except k=15, 21, where g=0. Prime powers k have no such pair and give g=0 trivially (A47); that is the known part of the zero set, and nothing else is a zero in this family when ω(k)=2.

### 2.2 Ingredients (all Category A)

1. **Exact formula (A50 Lemma 4), re-verified:** for m≤2n+1, A_n(m)=Q(m)+(−1)^m Σ_{x=0}^{m−n−1}(−1)^xQ(x). Checked against direct generating-function coefficients for n<90, all m≤2n+1 (`sanity.py`, 0 mismatches), and A_n(m)=|φ_n(m)| for n≤40, m≤3n+10.
2. **Q monotone:** Q(0)=Q(1)=1, Q(2)=0, Q nondecreasing from 2 on, so Σ_{x≤y, x≡p (2)}Q(x)≤(y/2+1)Q(y) for y≥3.
3. **Root geometry:** k | u²−4 and u²−4>0, so u²≥k+4. Hence 2s+3≤u²−u−1, m₁=m₂+u≤u²−1, and m₂≤2s+3. Also t<s/2 so m₂≥1.5s+4.
4. **Lower bound for A₁ (odd parts only plus union bound):** A_s(m)≥Q(m)−Σ_{x≡m−1 (2), x≤m−s−1}Q(x)≥Q(m)−(m/2)Q(m−s−1) (a partition into distinct odd parts that uses an odd part j>s is counted by Q(m−j)).
5. **Adding even parts:** A_s(m₁)≥A_s(m″) whenever D=m₁−m″ is a sum of allowed even parts (each in (s,2s], smallest s+1 for odd s, s+2 for even s); such D are: all even D with s+2≤D≤2s (or s+1≤D for odd s), all even D in (2s+2,4s], and all even D≥s+5 beyond (checked from j(s+2)≤2(j−1)s+1 for j≥3, s≥4).
6. **Upper bound for A₂:** when m₂≤n₂=k−s, A₂=Q(m₂).
7. **Elementary Bessel bounds:** (1−3/(4x))e^x/√(2πx)≤I₁(x)≤e^x/√(2πx), I₁≤xe^x/2 for x>0 (upper bound: I_ν decreasing in ν and I_{1/2}(x)=√(2/πx) sinh x; lower bound checked numerically on 1≤x≤1000 and standard asymptotics).

### 2.3 Finite range s≤2500 (computer)

* `exact_small.py 400`: all (s,k) with k odd, k|s²−1, k>2s, 3≤s≤400 (1454 pairs), A₁ and A₂ as exact big-integer coefficients: **only (4,15),(8,21) have A₁≤A₂** (equal). Minimum A₁/A₂ over the rest: 1.78 at (34,77).
* `chain.py 2500` (long double, margin 1e-9; A₂ exact by ingredient 1; A₁ from the lower bound with the best admissible m″, exact by ingredient 1 if m″≤2s+1 and by ingredient 4 otherwise): 15 587 pairs certified A₁>A₂(1+1e-9); 29 not certified, all with s≤32, all contained in the exact range above. The ratio A₁/A₂ is ≥1.037 only at (26,135) and ≈1.97–2.07 for s≥100 (it tends to about 2.07). The 2500 range is complete: for each s the list of k is all divisors of s²−1 above 2s.

### 2.4 Analytic range s≥1200 (A\*)

The input is a published explicit bound: for the η-quotient (q²;q²)²/((q;q)(q⁴;q⁴)) (so Σ Q(n)q^n=(−q;q²)_∞) Chern's Theorem 1.1 with error (3.10) (J. Number Theory 2019, arXiv 1805.08759; data m=(1,2,4), δ=(−1,2,−1), Δ₁=0, Δ₂=−1, L=4) gives |Q(n)−M(n)|≤B(n), M(n)=π(24n−1)^{−1/2}I₁(π√(24n−1)/12), with B(n) = (explicit error term E(n)) + Σ_{3≤k≤N, k≢2 (4)} (k-th main-term bound). `chern.py` transcribes B(n). **Check of the transcription against exact Q(n), 3≤n≤8000 (big integers, `chern_check.py`): 0 violations; worst |Q−M|/B=0.46 at n=8000; B/Q is 5.7e-2 at n=100, 4.5e-9 at 1000, 5.8e-20 at 5000.** Put ψ(n)=√6 e^{x(n)}/(24n−1)^{3/4}, x(n)=π√(24n−1)/12, β(n)=B(n)/ψ(n); then Q(n)≤(1+β)ψ(n), Q(n)≥(1−3/(4x)−β)ψ(n).

*Case A: m₁<5s+8.* Use ingredient 4 for A₁ with y₁=m₁−s−1≥s/2, and A₂≤Q(m₂)+Q(s+1). With x(m₁)−x(m₂)≥πu/√(24m₁) and u/√m₁>1 (ingredient 3), ψ(m₂)/ψ(m₁)≤e^{−π/√24}(1−1/√m₁)^{−3/4}≤0.54 (the middle expression is decreasing in w=u/√m₁ on the admissible range, so its maximum is at w=1). The crude term is (m₁/2)Q(y₁)≤(2.5s+4)(1+β)ψ(y₁) with ψ(y₁)/ψ(m₁)≤e^{−π(s+1)/√(24(5s+8))}·3^{3/4}·1.001, and the term Q(s+1) is smaller still. Normalised by ψ(m₁), A₁−A₂ ≥ L−θ−T−U with the values (`analytic_check.py`):

| s | 1200 | 1500 | 2501 | 6000 | 10⁴ | 10⁶ |
|---|---|---|---|---|---|---|
| margin A | 0.095 | 0.311 | 0.446 | 0.463 | 0.465 | 0.473 |

At s=2501: L=0.9905, θ=8.4e-3, T=0.5332, U=2.6e-3. Every term is monotone in s (L increases, θ, U decrease, T decreases to e^{−π/√24}), so the margin is positive for all s≥1200.

*Case B: m₁≥5s+8.* Take m″∈{4s,…,4s+3} with m″≡m₁ (2); then D=m₁−m″≥s+5 is admissible (ingredient 5), and A₁≥Q(4s)−(2s+2)Q(3s+2), A₂=Q(m₂)≤Q(2s+3) (here n₂≥4s>m₂). Margin ≥ 1−3/(4x(4s))−β−(2s+2)(1+β)ψ(3s+2)/ψ(4s)−(1+β)ψ(2s+3)/ψ(4s): 0.8906 at s=1000, 0.9904 at s=2000, 0.9935 at s=2501, →1.

Hence A₁>A₂ for all s≥1200 given the cited bound; finite check covers 3≤s≤2500; the ranges overlap. The only non-elementary inputs are Chern's theorem and the monotonicity of β(n)=B(n)/ψ(n) (visible from the closed form: E(n) is a power of n times a bounded exponential factor, the tail is O(n^{3/2}e^{x/2}); checked on the grid, n up to 10⁷). The margin is wide (≥0.44 at s≥2501; a relative error of 40% in Q would still do), and Hagis' Rademacher series for distinct odd parts gives an independent route to an explicit bound.

### 2.5 r≥3 (numerical; no proof)

For odd k with ω(k)=r≥3 there are 2^{r−1}−1 pairs. A pair's sign is fixed by parity: odd s ⇒ 8|t, contribution −(A₁−A₂); even s ⇒ t odd, contribution +(A₁−A₂). So g_k((k+2)²−3)=Σ(pair terms), positive for the even root below k/2, negative for the even root above. Each term is (0.46…0.5)·Q(m₁) (A₁/A₂≈2), so the largest term is the one with smallest t, but t_j−t_i=(s_j²−s_i²)/k is only forced to be ≥1, and Q(m₁) changes by a factor e^{π/(2√(6k))}≈1 per unit of t, so neighbouring terms of opposite sign can nearly cancel. Data: **`dom.py`: of 939 odd k≤8000 with ω≥3, the largest term exceeds the sum of the others for 869 (92.5%)**; for the other 70 no termwise argument works (first: k=105, roots 29, 34, 41, ratio 1.22). Minimum |total|/max|term| over r≥3: 2.88e-4 at k=7035 (A50). **Scan 11001–14000 (`scan_pairs.py`, 1179 non-prime-power k, A50's float-certified DP): no flags; min log-ratio for r=2 is 0.731 at k=11021; min |total|/max|term|=0.0205 at k=12035.** Together with A50 (≤11000): the zero set of g_k((k+2)²−3) among odd non-prime-power k≤14000 is exactly {15,21} (float-certified, not exact). Obstruction for r≥3: sign-alternating near-cancellations between pairs with comparable t; the proof would need ratio control Q(m−a)/Q(m) to relative precision beyond the termwise size, i.e. a Rademacher expansion good to the cancellation level (2.9e-4 so far), not available in closed form.

## 3. Part 3: even k

For even k, roots n of n²≡1 (mod k) are odd, the contributing indices are n≤k+2, n²≡1 (mod k) (since N=(k+2)²−3≡1), with m=(N−n²)/k. Direct computation: n=1 gives φ₁(k+4)=+1; n=k−1 gives m=6, φ=+Q(6)=+1; n=k+1 gives m=2, φ=Q(2)=0. A root s with 1<s<k/2 and its partner k−s give m₁=k+4−t, m₂=4+2s−t, and both have sign (−1)^{m}=(−1)^t. So

  g_k((k+2)²−3) = 2 + Σ_{pairs} (−1)^t (A₁+A₂).

**Claim 1 (Category A).** If 8∤k, every t is even: s is odd, so 8|s²−1=tk, and v₂(k)≤2 forces 2|t. All pair terms are ≥0, so g≥2 for even k≥6 with 8∤k (k=6: 3, k=10: 2). Verified directly for even k≤400 (`part3.py 400 exact`, exact int64): minimum over 8∤k is 2 (at k=10).

**Claim 2 (Category A).** k=2^a, a≥3: the only pair is s=k/2−1, with t=k/4−1 odd. So g=2−(A₁+A₂). For a≥4, A₂=A_{k/2+1}(3k/4+3)≥#{odd o≤k/4+1}≥3 (take o plus a single even part m₂−o∈(n₂, 2n₂] , all admissible), so g<0; k=8 direct: g=−3.

**Claim 3 (computer, not proved).** 8|k with an odd part: t has either parity, pair terms alternate in sign. Exact (k≤400, int64): g<0 for all 8|k≤232 and first positive at k=240 (g=80694). Float scan (`part3.py 8000 float8`, relative error ≈1e-11): all 1000 such k≤8000 have g≠0, min |g|/max|term|=1.05e-4 at k=1840; 397 positive, 603 negative. For 8|k there is no dominance and no proof.

## 4. Files (all in `A54_proofs2/`)

`chern.py`, `chern_mp.py`, `chern_check.py` (Chern bound, transcription check); `analytic_check.py` (margins A/B); `chain.py`, `chain_600.json`, `chain_2500.json/.log` (certified chain, s≤2500); `exact_small.py`, `exact_400.log`, `sanity.py` (exact checks); `dom.py`, `scan_pairs_11001_14000.json`, `scan_11001_14000.log` (r≥3); `part3.py`, `part3_8k.json` (even k); `par2.py`, `prodform.py`, `prodlib.py`, `sweep.py`, `classes.py`, `mod4.py`, `common.py`, `bailey2.py`, `bailey3.py`, `bailey_try.py`, `alpha_series.py`, `hecke2.py` (Part 1); `qtab.py`, `Q_20000.npy`, `Qexact_2000.pkl` (tables).
