# A58: independent audit of the cited Chern bound used in A54

**For:** Arvin Hampton (539 Labs) · 2026-10-22 (America/Chicago). All files are new and live in `A58_chern_bound_audit/`; nothing in A54, A46, A47, A50 or A56 was changed (A54's scripts were run read-only, with bytecode writing off, only to compare numbers). Runs used `nice`, OMP_NUM_THREADS=1, under 3 GB. Category A only; no TPC or RH claims. "A\*" means proved except for one cited published bound.

Notation as in A54: Q(n)=#partitions of n into distinct odd parts; for odd k and a root s of s²≡1 (mod k), 1<s<k/2: t=(s²−1)/k, u=k−2s, m₁=k+4−t, m₂=4+2s−t, n₂=k−s, A₁=A_s(m₁), A₂=A_{n₂}(m₂), where A_n(m)=|[x^m]∏_{j≤n}(1+x^j)^{-1}|. Put v(n)=24n−1, x(n)=π√v/12, ψ(n)=√6·e^{x(n)}/v(n)^{3/4}, M(n)=π v^{-1/2} I₁(x(n)).

## Summary (coverage)

| # | Question | Result | Status |
|---|---|---|---|
| 1 | Is the cited bound locatable, and what exactly does it say? | Yes. S. Chern, *Asymptotics for the Fourier coefficients of eta-quotients*, J. Number Theory 199 (2019) 168–191, arXiv:1805.08759 (only one arXiv version, v1, 22 May 2018). The published theorem is **Theorem 1.1** (error only as "≪_{m,δ}", not explicit). The **explicit** error is **eq. (3.10)** in §3.3, announced in **Remark 3** after Theorem 1.1. The journal page could not be fetched (timeout), so all numbering below is the arXiv v1 numbering. | located; text quoted in §1 |
| 2 | Do the hypotheses hold for G=(q²;q²)²/((q;q)(q⁴;q⁴))=ΣQ(n)qⁿ? | Yes, all of them, in exact rational arithmetic: m=(1,2,4), δ=(−1,2,−1), Σδ=0, Δ₁=0≤0, Δ₂=−1, L=4, condition (1.8) holds for ℓ=1,…,4, L_{>0}={1,3,4} (so k≡2 mod 4 never contributes), n≥1>−Δ₂/24. | confirmed (§2) |
| 3 | Does A54's usage match (variables, ranges, constants, strictness, k-dependence)? | Yes. A54's B(n)=E(n)+tail was re-transcribed from the paper text independently and agrees with A54's `chern.py` to 8 digits at 7 test points; the full formula (1.9) was evaluated with Dedekind-sum multipliers and checked against exact Q(n), n≤600 (0 violations; the actual error is at most 2.9·10⁻³ of the E-bound); abs(Q−M)≤B holds for all 3≤n≤8000 and every 5th n up to 35 200 (0 violations). No dependence on k enters Chern's constants (they depend only on m,δ,n); k enters only through the ranges of m₁,m₂ (§3). | confirmed (§3) |
| 4 | Elementary facts A54 used without proof | Proved here: the two-sided Bessel bounds, A_n(m) exact formula (m≤2n+1), monotonicity Q(n)≤Q(n+1) for n≥2, and a rigorous non-increasing majorant of B(n)/ψ(n) (A54 checked monotonicity on a grid only). | closed (§4) |
| 5 | Threshold s≥1200 | Re-derived in interval arithmetic with every constant recomputed. Case 1 (m₁<5s+8): margin ≥0.0965 at s=1200 (A54: 0.095); Case 2: ≥0.976. **Least integer S₀ for which the rigorous margins are positive: 1127** (margin 0.0004); positive at every integer in [1127, 3000] and monotone beyond. So 1200 is valid and not tight. | confirmed (§5) |
| 6 | Finite range below the threshold | Exact-integer certificate (no floating point) for **all 15 616 pairs with 3≤s≤2500**: 15 587 certified, 29 not, the **same 29** as A54's long-double chain, all with s≤32; exact big-integer DP settles them (only (4,15), (8,21) have A₁=A₂). Exact DP for all pairs with s≤300 (995 pairs), and 163 boundary pairs with 1050≤s≤1300, m₁≤3200: min A₁/A₂=2.0527 at (1079,2205). | confirmed (§6) |
| 7 | Reduction g_k((k+2)²−3)=Σ(−1)^{t+1}(A₁−A₂) | Checked against the direct coefficient of g_k for all 144 odd non-prime-power k≤501: 0 mismatches; zero set {15,21}. Numerical check only; the proof of the reduction is A50's, outside this audit. | numerical |
| 8 | Verdict | **The theorem stands as stated** (A\* status unchanged: it still rests on Chern's published explicit bound, which was located, matches the hypotheses, and passes every numerical test; I did not re-prove the circle-method lemmas). No change of hypothesis or threshold is needed. Wording amendments only (§7). The analytic argument is only needed for s≥2501, since the exact certificate reaches s=2500. | stands |

## 1. The cited statement (arXiv:1805.08759v1, text read from the PDF)

Setting: G(q)=∏_{r=1}^R (q^{m_r};q^{m_r})_∞^{δ_r}=Σ g(n)qⁿ, m_r distinct positive integers, δ_r nonzero integers, Σδ_r≥0 (abstract). With (1.5): Δ₁=−½Σδ_r, Δ₂=Σm_rδ_r, Δ₃(k)=−Σδ_r gcd²(m_r,k)/m_r, Δ₄(k)=∏(m_r/gcd(m_r,k))^{−δ_r/2}; ω_{h,k}=exp(−πiΣδ_r s(m_rh/gcd(m_r,k), k/gcd(m_r,k))) (Dedekind sums); L=lcm(m_r); L_{>0}={1≤ℓ≤L: Δ₃(ℓ)>0}, L_{≤0} the rest.

**Theorem 1.1 (verbatim content).** If Δ₁≤0 and
 min_{1≤r≤R} gcd²(m_r,ℓ)/m_r ≥ Δ₃(ℓ)/24 (1.8)
holds for all 1≤ℓ≤L, then for positive integers n>−Δ₂/24,

 g(n)=E(n)+Σ_{ℓ∈L_{>0}} 2π Δ₄(ℓ) ((24n+Δ₂)/Δ₃(ℓ))^{−(Δ₁+1)/2} Σ_{1≤k≤N, k≡ℓ (mod L)} [I_{−Δ₁−1}((π/6k)√(Δ₃(ℓ)(24n+Δ₂)))/k] Σ_{0≤h<k,(h,k)=1} ω_{h,k} e(−nh/k), (1.9)

N=⌊√(2π(n+Δ₂/24))⌋ (1.10), I_s the modified Bessel function, and |E(n)|≪_{m,δ} 1 if Δ₁=0; (n+Δ₂/24)^{1/4} if Δ₁=−½; (n+Δ₂/24)^{1/2}log(n+Δ₂/24) if Δ₁=−1; (n+Δ₂/24)^{−Δ₁−1/2} if Δ₁≤−3/2 (1.11).

**Remark 3** (p. 4): "An explicit bound of E(n) is given in (3.10). It would be necessary if one wants to study the exact sign pattern of g(n)."

**Equation (3.10)** (§3.3, assembled from Lemmas 3.1, 3.3, 3.4; ϱ=1/N², ν=n+Δ₂/24):

 |E(n)| ≤ [2^{−Δ₁}π^{−1}N^{−Δ₁+2}/ν] e^{2πϱν} Σ_{ℓ∈L_{>0}} e^{Δ₃(ℓ)π/3}
  + 2e^{2πϱν} Ξ_{Δ₁}(N) × { Σ_{1≤ℓ≤L} Δ₄(ℓ) exp(πΔ₃(ℓ)/24 + Σ_r |δ_r|e^{−πgcd²(m_r,ℓ)/m_r}/(1−e^{−πgcd²(m_r,ℓ)/m_r})²) − Σ_{ℓ∈L_{>0}} Δ₄(ℓ)e^{πΔ₃(ℓ)/24} },

with Ξ₀(x)=1 (eq. 1.16). All inequalities are non-strict. The theorem as published gives no numerical constant; A54's phrase "Theorem 1.1 with error (3.10)" is therefore accurate only if (3.10) is named as the source of the constant (see §7).

## 2. Hypotheses for Q(n) (exact arithmetic, `chern_iv.py`, log `data/chern_hypotheses.log`)

(q²;q²)²/((q;q)(q⁴;q⁴)) = (−q;q²)_∞ (since (−q;q²)=(q²;q⁴)/(q;q²) and 1/(q;q²)=(q²;q²)/(q;q)).

| ℓ | Δ₃(ℓ) | Δ₄(ℓ) | min gcd²(m,ℓ)/m | ≥Δ₃/24 ? | set |
|---|---|---|---|---|---|
| 1 | 1/4 | 1 | 1/4 | yes (1/96) | L_{>0} |
| 2 | −2 | √2 | 1 | yes (−1/12) | L_{≤0} |
| 3 | 1/4 | 1 | 1/4 | yes | L_{>0} |
| 4 | 1 | 1 | 1 | yes (1/24) | L_{>0} |

Also R=3, m distinct, δ nonzero, Σδ=0≥0, Δ₁=0≤0, Δ₂=−1, L=4. For k=1: 2πΔ₄(1)((24n−1)/Δ₃(1))^{−1/2} I₁(π√(Δ₃(1)(24n−1))/6)·ω_{1,1}=π(24n−1)^{−1/2}I₁(π√(24n−1)/12)=M(n) (ω_{1,1}=1). The k-th term for k odd has size ≤ (π/√v)I₁(x/k), for k≡0 (mod 4) ≤ (2π/√v)I₁(2x/k), using |ω|=1 and φ(k)≤k. So |Q(n)−M(n)| ≤ E(n)+Σ_{3≤k≤N, k≢2 (4)} (those sizes) =: B(n), which is exactly what A54 uses.

## 3. A54's usage against the hypotheses

* **Variables.** Q enters only as Q(n) with n a positive integer; in A54's argument n∈{m₁, m₂, m₁−s−1, s, s+1, 4s, 3s+2, 2s+3}, all ≥566 when s≥1127, so n>−Δ₂/24 and N≥43 always hold. Matches.
* **Constants.** Independent transcription of (3.10) in mpmath interval arithmetic (`chern_iv.py`; written from the paper text, A54's code compared afterwards in `verify_chern_instance.py`): B(n) agrees with A54's `chern.Bbound` to 8 significant digits at n=3,10,100,1000,1800,5000,20000 (ratio 1.0). Sample values: E(n)≈132–138 (constant, as Δ₁=0 predicts), tail dominated by the k=4 term (∼e^{x/2}); B/M=5.8·10⁻² (n=100), 4.5·10⁻⁹ (n=1000), 5.8·10⁻²⁰ (n=5000).
* **Strict vs non-strict.** (3.10) is non-strict; A54's use is non-strict until the final comparison, which has strictly positive margin. Case split m₁<5s+8 / m₁≥5s+8 is exhaustive over integers.
* **Dependence on k.** None in Chern's bound; the k-dependence is carried by u=k−2s with u²≥k+4 (k | u²−4, u²−4>0), which gives √(m₁+1)≤u, 1.5s+4<m₂≤2s+3, t≥1. Re-derived in §5.
* **Validation of the formula itself in this instance** (`verify_chern_instance.py`, log `data/verify_chern_instance.log`): (a) the complete right side of (1.9) (all k≤N, Dedekind multipliers computed exactly, 80-digit arithmetic) minus exact Q(n) satisfies |Q−main|≤E-bound for every n=1..600, with max ratio |Q−main|/E-bound=2.9·10⁻³ and imaginary part ≤4·10⁻⁵⁷; the actual |Q−main| is 0.16, 0.041, 0.030, 0.0031 at n=10, 100, 500, 1000 against E-bound ≈132. (b) |Q(n)−M(n)|≤B(n): 0 violations for all 3≤n≤8000 and every 5th n up to 35 200 (exact integers; max |Q−M|/B=0.46 at n=35 200).

## 4. Elementary facts proved here (A54 used them without proof or by numerical check)

**4.1 Bessel bounds, y>0.** I₁(y)=(y/π)∫_{−1}^{1}√(1−t²)e^{yt}dt. Put t=1−w, √(1−t²)=√(w(2−w)).
(i) √(w(2−w))≤√(2w) gives I₁(y)≤(y/π)e^y√2Γ(3/2)y^{−3/2}=e^y/√(2πy).
(ii) e^{yt}≤e^y and ∫_{−1}^{1}√(1−t²)dt=π/2 give I₁(y)≤ye^y/2.
(iii) √(w(2−w))≥√(2w)(1−w/2) on [0,2]; the right side is negative for w>2, so ∫₀² ≥ ∫₀^∞, and ∫₀^∞√(2w)(1−w/2)e^{−yw}dw=√2Γ(3/2)y^{−3/2}−(√2/2)Γ(5/2)y^{−5/2}. Hence I₁(y)≥(1−3/(4y))e^y/√(2πy). (A54 verified this numerically on 1≤y≤1000.)
Consequences: M(n)≤ψ(n) and M(n)≥(1−3/(4x(n)))ψ(n). Numerical sanity on y∈(0,20000]: no violation (`elementary_checks.py`). Also sup_y min(y/2,1/√(2πy))=½(2/π)^{1/3}<0.4302, so I₁(y)≤0.4302e^y for all y.

**4.2 Exact formula.** ∏_{j≤n}(1+x^j)^{−1}=(x;x²)_∞(−x^{n+1};x)_∞, and [x^a](x;x²)_∞=(−1)^aQ(a). For m≤2n+1 at most one part ≥n+1 can occur (two distinct parts are ≥(n+1)+(n+2)=2n+3>m), so (−1)^m[x^m]∏=Q(m)+Σ_{x=0}^{m−n−1}(−1)^{m+x}Q(x)=A_n(m). Also ∏_{j≤n}(1+x^j)^{−1}=∏_{odd j≤n}(1−x^j)/∏_{n/2<i≤n}(1−x^{2i}), so A_n(m) counts pairs (λ,μ), λ distinct odd parts ≤n, μ multiset of even parts in (n,2n], |λ|+|μ|=m, all with sign (−1)^m. Re-tested with new code (`t_lib.py`): packed-integer series equals plain recurrence for n≤40, m≤3n+10, and for n=7,30,64 to m=900.

**4.3 Q is nondecreasing for n≥2.** Exact table (35 201 values, SHA in `SHA256SUMS`): Q(n)≤Q(n+1) for 2≤n<35 200. For n≥300, dM/dn=π²v^{−1}[I₀−2I₁/x]≥π²v^{−1}(1−2/x)I₁(x) (I₀≥I₁), so M(n+1)−M(n)≥π(1−2/x)(1−3/(4x))ψ(n)√v(n)/v(n+1), while B(n)+B(n+1)≤2B̄(n+1) with B̄ from 4.4. The ratio 2B̄(n+1)/(that lower bound) is 0.42 at n=300, 0.10 at 400, ≤2·10⁻⁴ at 1000, and is non-increasing (the terms C_E v^{5/4}e^{−x} and K v^{5/4}e^{−x/2} decrease for v>365, and (1−2/x)(1−3/(4x)) increases); so Q(n+1)>Q(n) for all n≥300 (`q_monotone.py`). Consequence used: Σ_{x≤y, x≡p (2)} Q(x)≤(y/2+1)Q(y) and |Σ_{x=0}^{y}(−1)^xQ(x)|≤max(Q(y),1) (Q(0)−Q(1)=0; alternating sum of a nondecreasing nonnegative sequence from x=2).

**4.4 A rigorous majorant of B(n)/ψ(n), n≥300.** For n≥300, N≥43, N²/ν≤2π and 2πϱν<(1+1/N)²≤(44/43)², so E(n)≤C_E=138.1955 (interval upper end; both sums in (3.10) evaluated with directed rounding). For the tail: each term has Bessel argument ≤x/2 (odd k≥3: x/k≤x/3; k≡0 mod 4: 2x/k≤x/2), the number of terms is ≤N≤√(2πν)=√(πv/12), prefactor ≤2π/√v, so by 4.1 tail≤K·e^{x/2} with K=2π√(π/12)·0.4302=1.3828. Set B̄(n)=C_E+K e^{x(n)/2} (increasing) and β̄(n)=B̄(n)/ψ(n). ψ is increasing (d ln ψ/dn=π/√v−18/v>0 for v>33), so C_E/ψ decreases; the other term is (K/√6)v^{3/4}e^{−x/2}, and d ln(v^{3/4}e^{−x/2})/dn=18/v−π/(2√v)<0 for v>131. Hence β̄ is non-increasing, and for n≥300: **(1−3/(4x)−β̄(n))ψ(n) ≤ Q(n) ≤ (1+β̄(n))ψ(n)**. Values: β̄(300)=6.6·10⁻³, β̄(600)=1.1·10⁻⁴, β̄(1000)=1.7·10⁻⁶, β̄(1804)=2.5·10⁻⁹, β̄(3000)=1.4·10⁻¹², β̄(6000)=1.1·10⁻¹⁸. (A54 asserted monotonicity of β from "the closed form" and a grid to 10⁷; this replaces that.)

## 5. Re-derivation of the threshold (`threshold.py`, log `data/threshold.log`)

**Geometry** (all pairs, s≥3). k | s²−1, k>2s odd; t≥1; t<s/2 so 1.5s+4<m₂≤2s+3. u=k−2s is odd and ≥3 (u=1 would force k=3), k | u²−4>0 so u²≥k+4=2s+u+4, hence 2s+3≤u²−u−1 and m₁=m₂+u≤u²−1: **u≥√(m₁+1)**. y₂:=m₂−n₂−1=s+3−t−u≤s−1. If m₂≤n₂ then A₂=Q(m₂); in general (m₂≤2n₂+1 because n₂≥s+3) A₂=Q(m₂)+(−1)^{m₂}Σ_{x≤y₂}(−1)^xQ(x)≤Q(m₂)+Q(s).

**Lower bound for A₁.** (a) μ empty: A_s(m)≥Q(m)−Σ_{j odd,j>s}Q(m−j)≥Q(m)−(m/2)Q(m−s−1) (a distinct-odd partition with a part j>s is counted by Q(m−j)). (b) Adding any multiset of even parts from (s,2s] is injective, so A_s(m₁)≥A_s(m″) when D=m₁−m″ is such a sum. The reachable D are exactly: D=0, and even D with j·e_min≤D≤2js for some j (j parts fill every even number in [j·e_min,2js]; e_min=s+1 for odd s, s+2 for even s). For odd s: every even D≥s+1; for even s: every even D≥s+2 **except D=2s+2**.

**Case 1: m₁<5s+8** (so m₁≤5s+7, y₁=m₁−s−1>s/2+3, m₁>1.5s+4). A₁−A₂≥Q(m₁)−(m₁/2)Q(y₁)−Q(m₂)−Q(s). Divide by ψ(m₁), use 4.4 with all arguments ≥1.5s+4 or ≥s/2+3 (n≥300 needs s≥594):
* L=1−3/(4x(n_a))−β̄(n_a), n_a=1.5s+4 (increasing in s).
* T=(1+β̄(n_a))·r₀, r₀=e^{−π/√24}(1−24√(n_a+1)/(24n_a−1))^{−3/4}. Reason: ψ(m₂)/ψ(m₁)=exp(f(u)), f(u)=−(x(m₁)−x(m₁−u))+¾ln(v₁/(v₁−24u)), f′(u)=(−π+18/√v₂)/√v₂<0, so the worst case is u=u₀=√(m₁+1); by concavity x(m₁)−x(m₂)≥u₀π/√v₁>π/√24, and the log term is ≤¾ln(1/(1−24u₀/v₁)), largest at the smallest m₁. Constant 0.5364 at s=1127 (A54: 0.54).
* θ=((5s+7)/2)(1+β̄(s/2+3))e^{−π(s+1)/√(120s+167)}3^{3/4} (from x(m₁)−x(y₁)≥(s+1)π/√(24(5s+7)−1) and v₁/v_{y₁}<3).
* U=(1+β̄(s))e^{−π(s/2+4)/√(120s+167)}((120s+167)/(24s−1))^{3/4}.
θ and U are decreasing for s≥50 (d/ds ln θ=5/(5s+7)−π(60s+107)/(120s+167)^{3/2}<0; d/ds of the exponent in U has numerator −π(30s−156.5)); L increases, T decreases. So margin₁(s)≥L−T−θ−U evaluated at s=S₀ for all s≥S₀.

**Case 2: m₁≥5s+8.** Then k≥5s+5, n₂≥4s+5>m₂, so A₂=Q(m₂)≤Q(2s+3). Pick m″∈{4s,…,4s+3}, m″≡m₁ (mod 2), **and D≠2s+2** (the two parity-compatible choices give D and D−2, so one is always admissible); D≥s+5. Then A₁≥Q(4s)−(1.5s+2)Q(3s+2). Margin: [1−3/(4x(4s))−β̄(4s)]−(1.5s+2)(1+β̄(3s+2))ψ(3s+2)/ψ(4s)−(1+β̄(2s+3))ψ(2s+3)/ψ(4s); each subtracted term is decreasing in s (d/ds of the log of the first is <1/s−0.17/√s+O(s⁻²)<0 for s≥100).

**Numerical values** (Case 1 and Case 2 are `margin_A` and `margin_B` in the code; interval arithmetic, lower ends of the margins; `threshold.py`; monotone pieces re-checked on 46 731 grid points 600…10¹² in `elementary_checks.py`):

| S₀ | Case 1 margin (L, T, θ, U) | Case 2 margin (L, c₁, c₂) |
|---|---|---|
| 1000 | −0.2426 (0.9849, 0.5370, 0.6557, 0.0348) | 0.9544 (0.9908, 0.0364, 8·10⁻¹¹) |
| **1127** | **+0.0004** (0.9858, 0.5364, 0.4226, 0.0263) | 0.9703 (0.9913, 0.0210, 2·10⁻¹¹) |
| **1200** | **0.0965** (0.9862, 0.5361, 0.3310, 0.0226) | 0.9761 (0.9916, 0.0154, 9·10⁻¹²) |
| 1500 | 0.3119 | 0.9877 |
| 2501 | 0.4464 (0.9905, 0.5332, 0.0084, 0.0025) | 0.9940 |
| 10⁴ | 0.4654 | 0.9971 |
| 10⁶ | 0.4726 | 0.9997 |
| →∞ | →1−e^{−π/√24}=0.4734 | →1 |

A54's `analytic_check.py` re-run gives 0.0949 at 1200, −0.044 at 1100, 0.4463 at 2501, 0.9935/0.9460 (Case 2 at 2501/1200): same picture, slightly different constants (A54 uses Q(s+1) and a factor 1.001). **Least S₀ with positive rigorous margins in both cases: 1127; positive at every integer 1127…3000 and, by the monotonicity above, for all s≥1127.** The stated threshold 1200 is valid with margin 0.0965.

**How much does the argument lean on Chern's constant?** Replace β̄ by an arbitrary uniform relative error d (Q∈[(1−3/(4x)−d)ψ,(1+d)ψ]): the margins stay positive for d up to 0.051 at S₀=1200, 0.289 at 2501, 0.302 at 5000 (limit ≈0.31); the actual β̄ is 2.5·10⁻⁹ at n=1804 and 2.5·10⁻¹⁴ at n=3754 (`tolerance.py`). A54's remark "a relative error of 40% would still do" is slightly generous (≈29–31% at s≥2501). In practice the proof uses Chern only through Q(n)=ψ(n)(1+O(10⁻⁸)) for n≥1800, so even a large mis-transcription of the constants in (3.10) would not matter. A direct exact check of this: for 3≤n≤35 200 the exact table gives |Q−M|≤B with B/Q≤10⁻⁸ for n≥1000.

## 6. Finite range below the threshold (exact integers; `pairs_certify.py`, `exact_range.py`, `boundary_scan.py`, `boundary_exact.py`)

Pairs: every (s,k) with k odd, k>2s, k | s²−1, 3≤s≤2500: **15 616** (A54: 15 587 certified + 29 not = 15 616).
* **Certificate** (all arithmetic in Python integers; Q table exact to 35 200; A₂ by 4.2; A₁ lower bound by Case-1-type union bound at an admissible m″, tried in the order m″=m₁, 4s+3…4s, then a scan of (m₂,min(m₁,8s)]): **15 587 pairs have LB>A₂ as integers; 29 do not**, exactly A54's 29 (set equality checked against `chain_2500.json`), all with s≤32. Minimum certified LB/A₂ by block: s∈[3,100] 1.0229 (34,1155); [101,400] 1.9678 (103,221); [401,1000] 2.0257 (404,837); [1001,1300] 2.0527 (1079,2205); [1301,2500] 2.0577 (1376,2805). (This is LB/A₂ for the first admissible m″ found, not the best.)
* **Exact DP** (direct coefficients of ∏_{odd j≤s}(1+x^j)/∏_{even e∈(s,2s]}(1−x^e), independent of any lower-bound lemma): all 563 pairs with 3≤s≤200: only (4,15) (A₁=A₂=2) and (8,21) (A₁=A₂=6) fail A₁>A₂; min A₁/A₂ over the rest 1.7811 at (34,77), as in A54; the lower bound never exceeded the exact A₁ (0 violations over all candidates m″ tried). s=201–300 (432 pairs, `data/exact_range_201_300.log`): none fails; min A₁/A₂=1.99891 at (208,437); 0 lower-bound violations. Together with the chain's exact settlement, exact DP covers all pairs with s≤300.
* **Boundary region.** (i) All 163 pairs with 1050≤s≤1300 and m₁≤3200, exact A₁ and A₂: A₁>A₂ in every case; min A₁/A₂=2.05274 at (s,k,t,u)=(1079,2205,528,47) (k=u²−4, the extremal shape). (ii) Exact A₁ for all pairs with m₁≤24 000 at s=1128, 1199, 1200, 1201 (`data/boundary_exact.log`): e.g. (1199,2995): A₁/A₂=2810.2, (A₁−A₂)/ψ(m₁)=0.9938; (1200,13211): ratio 3.3·10³⁶; (1201,3005): 3007.2. In all cases (A₁−A₂)/ψ(m₁) lies in 0.994–0.998 and LB≤A₁ as required. So the finite computation covers s≤2500, comfortably above 1127/1200 and the analytic range starts inside it (overlap 1127…2500).
* The finite certificate and the analytic range together cover every s≥3; the analytic part is logically needed only for s≥2501.

## 7. Verdict and amendments

**The theorem stands as stated:** for every odd k and root s with 1<s<k/2, A₁>A₂ except (s,k)=(4,15),(8,21); hence for odd k with exactly two distinct prime factors g_k((k+2)²−3)≠0 except k=15,21. Status A\* (one cited published bound), with the following findings.
1. *No gap found in the use of the bound.* Hypotheses hold, the transcription of (3.10) is right, ranges and strictness are consistent, k enters only via u²≥k+4.
2. *Citation wording (amendment).* Write: "Chern, J. Number Theory 199 (2019) 168–191 (arXiv:1805.08759): Theorem 1.1 with the explicit error term (3.10) of §3.3 (cf. Remark 3)". Theorem 1.1 alone states E(n)≪1 without a constant. Numbering is from arXiv v1, the only arXiv version; the journal version was not accessible to me.
3. *Presentational amendments, not mathematical gaps.* (a) Q nondecreasing (n≥2), the lower Bessel bound and the monotonicity of β are now proved (§4); A54 can cite these. (b) In Case 2 for even s the value D=2s+2 is not a sum of even parts from (s,2s]; the recipe "m″∈{4s,…,4s+3}" should say "choose the parity-compatible m″ with D≠2s+2" (always possible). A54's list of admissible D is right. (c) "40%" tolerance should read about 30%. (d) A54's chain for 400<s≤2500 used long doubles with margin 10⁻⁹; the exact-integer version here removes that dependence (same 29 exceptions).
4. *Threshold.* 1200 is valid; the least threshold this derivation gives is 1127. No change needed.

## 8. Limits of this audit

* I did not re-prove Chern's circle-method lemmas (Lemmas 2.1–2.4, 3.1–3.4). I read §§2–3, checked that (3.10) is assembled correctly from Lemmas 3.1, 3.3, 3.4 and that the numerical content (full formula (1.9) and the explicit error bound) is consistent with exact Q(n) for n≤600 and n≤35 200 respectively. A numerical pass is evidence, not a proof; the analytic range still depends on the published result. An independent route (Hagis' Rademacher-type series for distinct odd summands, which A54 suggests) was not evaluated here.
* The journal version of the paper was not retrieved; if it differs in numbering or constants from arXiv v1, (3.10) should be re-checked against it. The argument is insensitive to the constants (§5).
* The reduction g_k→A₁−A₂ (A50) was only checked numerically (k≤501), and r≥3 prime factors, even k, and the F(Q) part of A54 are outside this audit.

## 9. Files (all in `A58_chern_bound_audit/`)

`REPORT.md`, `REPORT.pdf`, `SHA256SUMS`; `src/chern_1805.08759.pdf` (arXiv v1 PDF) and `src/chern.txt` (text extraction); `code/`: `a58lib.py` (packed exact series, pair enumeration; new), `chern_iv.py` (hypotheses, formula (1.9), (3.10) in interval arithmetic; new), `verify_chern_instance.py`, `threshold.py`, `tolerance.py`, `q_monotone.py`, `elementary_checks.py`, `make_Q.py`, `chainlib.py`, `pairs_certify.py`, `exact_range.py`, `boundary_scan.py`, `boundary_exact.py`, `link_check.py`, `t_lib.py`, `mk_pdf.py`; `data/`: logs of each run and `Q_exact_35200.pkl` (exact Q(0..35200); SHA256 of the decimal list 6a2037fb…a78). All code is newly written for this audit; A54's `chern.py` and `analytic_check.py` were only executed read-only for the comparisons in §3 and §5 (the PDF script follows the same markdown→HTML→headless-Chrome pattern as A54's `mk_pdf.py`, rewritten).
