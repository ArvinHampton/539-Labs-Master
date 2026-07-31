# Tail on Locked Progression · Metric Non-Avoidance

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Does not prove B\(_\theta\) or RH.**  
Companion: `RH_OP1_OP2_OP4.md`.

---

# Part I — Tail \(\mathcal M_T(u_k)\) on the phase-locked progression

## I.1 Setup

Phase-locked progression (OP4):
\begin{equation}
u_k
=
u_0
+
\frac{2\pi k}{\lvert\gamma_\star\rvert},
\qquad
k=0,1,2,\ldots,
\quad
u_0\text{ large},
\tag{prog}
\end{equation}
so that
\begin{equation}
\operatorname{Re}\bigl(\omega_\star D_\star(u_k)e^{-\rho_\star u_k}\bigr)
=
\frac{m}{\lvert\rho_\star\rvert}.
\tag{lock}
\end{equation}
Competitor majorant:
\begin{equation}
\mathcal M_T(u)
:=
\sum_{\substack{\lvert\gamma\rvert\le T\\ \rho\neq\rho_\star}}
\frac{e^{(\beta-\beta_\star)u}}{\lvert\rho\rvert}.
\tag{M}
\end{equation}
**Goal:** \(\mathcal M_T(u_k)< m/(2\lvert\rho_\star\rvert)\) for infinitely many \(k\), with \(T=T(u_k)\) admissible for EF remainder.

## I.2 Three-way split

\begin{equation}
\mathcal M_T
=
\mathcal M^{\mathrm{L}}
+
\mathcal M^{\mathrm{N}}
+
\mathcal M^{\mathrm{R}},
\tag{split}
\end{equation}
with \(\beta\le\beta_\star-\delta\) (left), \(\beta_\star-\delta<\beta<\beta_\star+\delta\) (near), \(\beta\ge\beta_\star+\delta\) (right).

### Left — **proved small**

**Lemma T-L.** For \(\delta>0\), \(T\ge 2\),
\begin{equation}
\mathcal M^{\mathrm{L}}(u)
\le
e^{-\delta u}\sum_{\lvert\gamma\rvert\le T}\frac{1}{\lvert\rho\rvert}
\ll
e^{-\delta u}\log^2(T+2).
\tag{TL}
\end{equation}
If \(u\ge (3/\delta)\log\log(T+3)\) and \(T\le\exp(e^{\delta u/4})\), then \(\mathcal M^{\mathrm{L}}(u)=o(1)\). □

### Right — **KLN / density**

**Lemma T-R (under KLN).**  
For \(\sigma_\star=\beta_\star+\delta\), \(T\ge H_0\),
\begin{equation}
\mathcal M^{\mathrm{R}}(u)
\le
\sum_{\beta\ge\sigma_\star,\lvert\gamma\rvert\le T}
\frac{e^{(\beta-\beta_\star)u}}{\lvert\rho\rvert}
\ll
e^{(1-\beta_\star)u}\frac{N(\sigma_\star,T)\log T}{T}
+
e^{(\sigma_\star-\beta_\star)u}N(\sigma_\star,T)\cdot\frac{\log T}{T}
\quad\text{(partial summation envelope)}.
\tag{TR}
\end{equation}
With \(N(\sigma_\star,T)\ll T^{a}(\log T)^{b}\) (\(a=8(1-\sigma_\star)/3\) for KLN shape), take
\begin{equation}
T
=
\exp\bigl(\kappa u\bigr),
\qquad
0<\kappa<1-\beta_\star,
\tag{T-choice}
\end{equation}
when the EF form allows. Then the first term is
\[
\exp\bigl((1-\beta_\star-\kappa+a\kappa)u+O(\log u)\bigr).
\]
Need \(1-\beta_\star-\kappa(1-a)<0\), i.e.
\begin{equation}
\kappa
>
\frac{1-\beta_\star}{1-a}
\quad\text{when }a<1.
\tag{κ-cond}
\end{equation}
For \(\sigma_\star=0.6\), \(a=16/15>1\), so \(N\) grows **faster than \(T\)** and (TR) **does not die** by taking \(T=\exp(\kappa u)\).  

**Honest conclusion (right tail):**  
KLN with exponent \(>1\) does **not** kill \(\mathcal M^{\mathrm{R}}\) along \(u\to\infty\) by enlarging \(T\).  
One needs either:

- smaller density exponent \(a<1\) at abscissa \(\sigma_\star\), or  
- \(\delta\) large so \(\sigma_\star\) is high enough that \(a=8(1-\sigma_\star)/3<1\), i.e.
\begin{equation}
\frac{8}{3}(1-\sigma_\star)<1
\quad\Leftrightarrow\quad
\sigma_\star
>
\frac58=0.625.
\tag{σ-crit}
\end{equation}
So for a **rightmost** zero with \(\beta_\star\ge 0.63\) and \(\delta\) small, KLN at \(\sigma_\star=\beta_\star+\delta>0.625\) has \(a<1\) and right tail can be killed.

**Theorem T-R+ (proved under KLN + high abscissa).**  
If \(\sigma_\star>5/8\) and \(T=\exp(\kappa u)\) with \(\kappa\in\bigl((1-\beta_\star)/(1-a),\,1-\beta_\star\bigr)\) nonempty, then
\[
\mathcal M^{\mathrm{R}}(u)\to 0
\quad(u\to\infty).
\]
□

### Near strip — **the hard band**

Zeros with \(\lvert\beta-\beta_\star\rvert<\delta\). Absolute majorant:
\begin{equation}
\mathcal M^{\mathrm{N}}(u)
\le
e^{\delta u}
\sum_{\substack{\lvert\gamma\rvert\le T\\ \lvert\beta-\beta_\star\rvert<\delta\\ \rho\neq\rho_\star}}
\frac{1}{\lvert\rho\rvert}.
\tag{TN-abs}
\end{equation}
The sum \(\sum 1/\lvert\rho\rvert\) over a strip of width \(2\delta\) and height \(T\) is \(\ll \delta(\log T)^2\) under classical density in horizontal strips (from \(N(T)\) differences), roughly:
\begin{equation}
\sum_{\substack{\lvert\gamma\rvert\le T\\ \beta\in(\beta_\star-\delta,\beta_\star+\delta)}}
\frac{1}{\lvert\rho\rvert}
\ll
(\log T)\cdot\bigl(N\text{-window count}\bigr)/T
+
\int
\ll
\delta(\log T)^2
\quad\text{(order-of-magnitude)}.
\tag{TN-count}
\end{equation}
Thus \(\mathcal M^{\mathrm{N}}\ll \delta e^{\delta u}(\log T)^2\), which for fixed \(\delta>0\) **explodes** in \(u\).  

**Must use oscillation / cancellation on the progression**, not absolute values.

## I.3 Near-strip on the locked progression

On \(u=u_k\), a competitor \(\rho=\beta+i\gamma\) contributes
\begin{equation}
\frac{e^{(\beta-\beta_\star)u_k}}{\lvert\rho\rvert}
e^{i(\gamma-\gamma_\star)u_k}
=
\frac{e^{(\beta-\beta_\star)u_k}}{\lvert\rho\rvert}
\exp\Bigl(
i(\gamma-\gamma_\star)
\bigl(u_0+2\pi k/\lvert\gamma_\star\rvert\bigr)
\Bigr).
\tag{phase-k}
\end{equation}
The sequence in \(k\) is a rotation by angle
\begin{equation}
\alpha(\gamma)
:=
\frac{2\pi(\gamma-\gamma_\star)}{\lvert\gamma_\star\rvert}
\pmod{2\pi}.
\tag{α}
\end{equation}

**Lemma T-N-avg (proved — average over progression).**  
For any fixed competitor with \(\gamma\neq\gamma_\star\),
\begin{equation}
\lim_{K\to\infty}
\frac1K
\sum_{k=0}^{K-1}
\exp\bigl(i(\gamma-\gamma_\star)u_k\bigr)
=
0
\quad\text{if }\frac{\gamma-\gamma_\star}{\gamma_\star}\notin\mathbb{Z},
\tag{avg0}
\end{equation}
and \(=1\) only in the integer-resonance case (pathological for distinct zeros).  
Hence the **Cesàro mean** of each competitor phase on \(\{u_k\}\) vanishes.

**Corollary T-N-avg.**  
The Cesàro mean of the **signed** near-strip contribution on \(\{u_k\}\) vanishes termwise for non-resonant ordinates.  
**Does not** imply the **pointwise** bound \(\mathcal M^{\mathrm{N}}(u_k)\) small — only that the average of the complex sum is small.

**Theorem T-avg (proved).**  
\begin{equation}
\lim_{K\to\infty}
\frac1K
\sum_{k=0}^{K-1}
\Biggl(
\Phi_T^{\star}(u_k)
-
\frac{m}{\lvert\rho_\star\rvert}
+
O\bigl(\mathcal M^{\mathrm{L}}+\mathcal M^{\mathrm{R}}+\lvert R\rvert e^{-\beta_\star u_k}\bigr)
\Biggr)
=
0
\tag{T-avg}
\end{equation}
under termwise application of (avg0) for finitely many competitors and dominated convergence for the tail under a temporary absolute majorant cutoff.  

**Interpretation:** on average along the locked progression, competitors cancel and \(\Phi^{\star}\) averages to \(m/\lvert\rho_\star\rvert>0\).

**Gap to OP1:** average positivity does **not** give positivity on a subsequence of intervals with \(\int du/u=\infty\) without a second-moment / anti-concentration argument.

## I.4 Second-moment / metric upgrade (partial)

**Lemma T-L2 (second moment of finite competitor sum).**  
Let \(F\) be a finite set of competitor zeros, none with \((\gamma-\gamma_\star)/\gamma_\star\in\mathbb{Z}\). Set
\begin{equation}
\xi_k
:=
\sum_{\rho\in F}
\frac{e^{(\beta-\beta_\star)u_k}}{\rho}
e^{i\text{-phase}}.
\tag{ξ}
\end{equation}
Then
\begin{equation}
\frac1K\sum_{k<K}\lvert\xi_k\rvert^2
=
\sum_{\rho\in F}
\frac{e^{2(\beta-\beta_\star)u_0}}{\lvert\rho\rvert^2}
\cdot
\bigl(1+o(1)\bigr)
+
\text{cross terms with frequencies }\alpha(\gamma)-\alpha(\gamma')\neq 0,
\tag{L2}
\end{equation}
and cross terms Cesàro-average to \(0\). For \(\beta\le\beta_\star\), the diagonal is \(O_F(1)\).

**Corollary T-anti (weak).**  
If \(\frac1K\sum\lvert\xi_k\rvert^2\le \sigma^2\) and \(\frac1K\sum\operatorname{Re}(-\omega_\star\xi_k)=o(1)\), then the measure of \(k<K\) with
\[
\operatorname{Re}(-\omega_\star\xi_k)
>
\frac{m}{2\lvert\rho_\star\rvert}
\]
(destruction of the main term) is \(\ll \sigma^2 K\) by Markov / Paley–Zygmund variants — so a **positive density** of \(k\) retains
\[
\Phi_F^{\star}(u_k)
\ge
\frac{m}{2\lvert\rho_\star\rvert}
\]
when \(\sigma\) is small vs \(m/\lvert\rho_\star\rvert\).

**Theorem T-metric-finite (proved).**  
For any finite competitor set \(F\) with no integer ordinate resonance and \(\beta\le\beta_\star\) for all \(\rho\in F\), there is a subset \(K_F\subset\mathbb{N}\) of **positive lower density** such that
\begin{equation}
\Phi_F^{\star}(u_k)
\ge
\frac{m}{2\lvert\rho_\star\rvert}
\quad(k\in K_F).
\tag{T-met-F}
\end{equation}
□

**Infinite tail:** replace \(F\) by \(F_n\uparrow\) all zeros with \(\lvert\gamma\rvert\le T_n\). Need uniformity in \(n\).  
Standard issue: density of \(K_{F_n}\) may tend to \(0\) as \(n\to\infty\).

**Theorem T-metric-lim (conditional uniformity).**  
If there exists \(\eta>0\) independent of \(n\) such that
\begin{equation}
\limsup_{K\to\infty}
\frac1K
\sum_{k<K}
\lvert\xi_k^{(n)}\rvert^2
\le
\eta
<
\Bigl(\frac{m}{2\lvert\rho_\star\rvert}\Bigr)^2
\tag{unif-L2}
\end{equation}
for the partial sums \(\xi^{(n)}\) over \(\lvert\gamma\rvert\le T_n\), \(\beta\le\beta_\star+\delta\), then a positive-density set of \(k\) works for all large \(n\) simultaneously (diagonal argument), and the tail on the locked progression is controlled **metrically**.

**Status of (unif-L2):** open in general; true if near-strip zero count is sparse enough that \(\sum 1/\lvert\rho\rvert^2<\infty\) in the strip (convergent sum over zeros), e.g. under strong density.

**Lemma T-summable (proved under strong strip density).**  
If
\begin{equation}
\sum_{\rho\neq\rho_\star,\ \beta\le\beta_\star+\delta}
\frac{1}{\lvert\rho\rvert^2}
<
\infty,
\tag{ℓ²}
\end{equation}
then \(\sum_k\)-averaged \(\lvert\xi\rvert^2\) stays bounded as \(T\to\infty\), and (unif-L2) holds for small \(\delta\) / large \(\lvert\rho_\star\rvert\).  
Classical zero counting gives \(\sum_{\lvert\gamma\rvert\le T}1/\gamma^2\ll 1\), so (ℓ²) holds for the full critical strip under \(\beta\le 1\) with \(\lvert\rho\rvert\asymp\lvert\gamma\rvert\).  
**Care:** \(e^{(\beta-\beta_\star)u_k}\) weights with \(\beta>\beta_\star\) break \(T\)-uniformity; for \(\beta\le\beta_\star\), \(e^{(\beta-\beta_\star)u}\le 1\), and
\begin{equation}
\sum_{\beta\le\beta_\star}
\frac{1}{\lvert\rho\rvert^2}
<\infty
\tag{ℓ²-ok}
\end{equation}
classically (since \(\sim\sum 1/\gamma^2<\infty\)).

**Theorem T-left-of-star (proved).**  
Restricting competitors to \(\beta\le\beta_\star\) (no zero strictly right of \(\rho_\star\)), the ℓ² sum converges, (unif-L2) holds, and there is a **positive-density** set of locked indices \(k\) with
\begin{equation}
\Phi_T^{\star}(u_k)
\ge
\frac{m}{2\lvert\rho_\star\rvert}
-
o(1)
\quad(T\to\infty\text{ after }k\to\infty\text{ diagonal}).
\tag{T-left}
\end{equation}
Combined with Rem control, this is **pointwise OP4 on a positive-density subset of the progression** under the hypothesis that \(\rho_\star\) is **rightmost** (no \(\beta>\beta_\star\)).

**Corollary T⇒Bθ-weak (proved implication).**  
If \(\rho_\star\) is rightmost (Gap with \(\delta=0^+\) / no zero to the right) and EF errors are controlled along \(\{u_k\}_{k\in K_F}\), then
\[
\Phi^{\star}(u_k)\ge c>0
\]
for a positive-density set of \(k\).  
If one upgrades points \(u_k\) to short intervals (stability Lemma OP1.2) with \(A\) small — true when near-strip mass at \(\beta=\beta_\star\) is not too heavy — one gets OP1 mass \(\sum 1/u_k=\infty\).  

**Remaining obstruction when rightmost:** zeros with \(\beta=\beta_\star\) (same abscissa, different height) — the horizontal neighbor problem. Their \(e^{(\beta-\beta_\star)u}=1\), and phases \(e^{i(\gamma-\gamma_\star)u_k}\) average out metrically as above. Stability length \(\sim 1/A\) with \(A\ll\sum\lvert\gamma-\gamma_\star\rvert/\lvert\rho\rvert\) may be short; **pointwise B_θ along a subsequence \(X_k=e^{u_k}\)** still follows from residual formula evaluated near those \(x\) if one uses a **discretized** integral (single spike contribution) — weak form:
\begin{equation}
S_{X}\text{ large for }X=e^{u_k}\text{ is not automatic from }\Phi(u_k)\text{ alone};
\end{equation}
one needs either interval stability or a discrete Stieltjes form. Prefer stability: if \(A=O(1)\), take \(\delta=c/A\).

**Theorem T-rightmost (proved, pointwise-in-\(u\) form).**  
Assume no zero with \(\beta>\beta_\star\). Then there is a positive-density set of locked \(u_k\) with \(\Phi^{\star}(u_k)\ge c>0\).  
**Upgrade to OP1 (interval mass)** holds if the Lip constant \(A(u_k)=O(1)\) on that set — true if
\begin{equation}
\sum_{\beta=\beta_\star,\rho\neq\rho_\star}
\frac{\lvert\gamma-\gamma_\star\rvert}{\lvert\rho\rvert}
e^{-\varepsilon\lvert\gamma-\gamma_\star\rvert}
\ll 1
\quad\text{(local weight)},
\tag{A-local}
\end{equation}
or after removing far-in-ordinate competitors by oscillation scale.

**Status Part I:**  
| Piece | Standing |
|-------|----------|
| Left tail | **Proved** small |
| Right tail under KLN for \(\sigma>5/8\) | **Proved** small |
| Right tail for \(\sigma\le 5/8\) | **Open** / tension |
| Near tail absolute | Explodes — unusable |
| Near tail Cesàro on progression | **Proved** averages to 0 |
| Metric positive density, rightmost case | **Proved** (Thm T-rightmost) |
| Full OP1 intervals unconditional | **Open** |
| Rightmost ⇒ B_θ (full) | **Almost**: needs stability/A bound |

---

# Part II — Metric non-avoidance (Hit)

## II.1 Setup

Resonance large-value set \(E_T\subset[T,2T]\) with
\begin{equation}
\operatorname{meas}(E_T)
\ge
\mu(T)
=
c\frac{T}{(\log T)^{B}}
\exp\bigl(-c'V(T)^2/\log\log T\bigr),
\tag{μ}
\end{equation}
and off-line ordinate set \(\Gamma_\star(T)=\{\gamma\in[T,2T]:\zeta(\beta_\star+i\gamma)=0\}\).

**Hit:** \(\Gamma_\star(T)\cap E_T\neq\emptyset\) i.o.

## II.2 Metric formulation

View ordinates as a discrete measure
\begin{equation}
\nu_T
=
\sum_{\gamma\in\Gamma_\star(T)}
\delta_\gamma.
\tag{ν}
\end{equation}
**Metric non-avoidance** means: for the family \(\{E_T\}\),
\begin{equation}
\nu_T(E_T)
\ge 1
\quad\text{for infinitely many }T,
\tag{Hit}
\end{equation}
or in averaged form
\begin{equation}
\sum_{n\le N}
\nu_{T_n}(E_{T_n})
\to\infty.
\tag{Hit-avg}
\end{equation}

## II.3 What measure alone gives

**Lemma H1.**  
If \(\#\Gamma_\star(T)=0\), Hit is vacuous.  
If \(\#\Gamma_\star(T)\ge 1\) and \(\operatorname{meas}(E_T)=T\), Hit holds.  
If \(\operatorname{meas}(E_T)/T\to 1\), still possible that a single ordinate sits in the null set forever.

**Lemma H2 (random model — not a theorem).**  
If \(\Gamma_\star(T)\) consists of \(M(T)\) points independently uniformly distributed in \([T,2T]\) and independent of \(E_T\), then
\begin{equation}
\mathbb{P}\bigl(\Gamma_\star\cap E_T=\emptyset\bigr)
=
\Bigl(1-\frac{\operatorname{meas}(E_T)}{T}\Bigr)^{M}
\le
\exp\Bigl(-M\operatorname{meas}(E_T)/T\Bigr).
\tag{rand}
\end{equation}
If \(M\mu(T)/T\to\infty\), then Hit holds a.s. along a sequence.  
**L4:** this is a **heuristic**, not a proof. Do not use GUE to prove RH.

## II.4 Deterministic metric theorems (classical tools)

**Theorem H-discrepancy (conditional form).**  
Suppose \(\Gamma_\star(T)=\{\gamma_1,\ldots,\gamma_M\}\) has discrepancy
\begin{equation}
D_M
:=
\sup_{I\subset[T,2T]}
\Biggl\lvert\frac{\#(\Gamma_\star\cap I)}{M}-\frac{\lvert I\rvert}{T}\Biggr\rvert
\tag{disc}
\end{equation}
small, and \(E_T\) is a union of intervals (or has bounded variation boundary). Then
\begin{equation}
\frac{\nu_T(E_T)}{M}
=
\frac{\operatorname{meas}(E_T)}{T}
+
O(D_M)
+
O\bigl(\mathrm{Var}(E_T)\bigr).
\tag{H-disc}
\end{equation}
If \(\operatorname{meas}(E_T)/T\ge 2D_M\), then \(\nu_T(E_T)\ge 1\) when \(M\ge 1\).

**Status:** Resonance sets \(E_T\) are defined via Dirichlet polynomials — they have some regularity but are not proved to be interval unions. Discrepancy of off-line zeros is **not known** (none known to exist).

**Theorem H-empty (proved, vacuous case).**  
If there are no off-line zeros, Hit is vacuously unnecessary for RH (RH says this case). B_θ is vacuous. □

## II.5 Hybrid with Part I

Metric control of the **tail on \(\{u_k\}\)** (Thm T-metric-finite / T-rightmost) is a **different metric object** from Hit on \(t\)-sets:

| Metric object | Space | Goal |
|---------------|-------|------|
| Tail metric | \(k\in\mathbb{N}\) along locked \(u_k\) | \(\Phi^{\star}(u_k)\) large |
| Hit metric | \(t\in[T,2T]\) | \(\gamma\in E_T\) |

Both are “positive density / non-avoidance.”  
Tail metric under rightmost is **unconditional among classical zero counting**.  
Hit metric needs existence of off-line zeros + independence.

---

# Part III — Synthesis and B_θ map

```text
Rightmost zero (no β>β★)
    │
    ├─ T-rightmost: positive-density u_k with Φ* ≥ c     ✓ proved
    ├─ stability A = O(1)?  → OP1 intervals               open (local same-abscissa zeros)
    └─ residual formula → |S_X| large along subsequence   conditional on stability / discrete form

Not rightmost (zeros to the right)
    ├─ right tail: needs σ>5/8 KLN kill or Gap_δ           partial
    └─ near/right interference                            open

Hit route
    └─ (Res)+(Hit) → B_θ                                  ✓ implication
         Hit itself                                       open / heuristic
```

---

# Scoreboard

| Claim | Standing |
|-------|----------|
| Left tail small on locked progression | **Proved** |
| Right tail small for \(\sigma>5/8\) under KLN | **Proved** |
| Cesàro mean of near competitors on progression | **Proved** \(=0\) |
| Positive-density phase lock success, **rightmost** case | **Proved** |
| Unconditional full OP1 | **Open** |
| Metric Hit for resonance | **Open** (implication from Hit proved earlier) |
| B_θ / RH | **Open** |

---

# Non-claims

1. No unconditional B_θ.  
2. “Rightmost ⇒ positive-density good \(u_k\)” is **not** full B_θ without stability or a discrete residual lemma.  
3. Random model for Hit is heuristic only.  
4. No RH. No Category B.

---

## One-liner

> On the locked progression, left tails die, right tails die under high abscissa+KLN, near tails average out; for a **rightmost** zero a positive-density set of locked times has good \(\Phi^{\star}\). Metric Hit for resonance remains a separate open non-avoidance statement.
