# Resonance Methods and Littlewood Ω — Toward Phase-Aligned Lower Bounds

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Does not prove B\(_\theta\) or RH.**

**Goal.** Map classical tools onto the residual problem from `RH_Signed_Sum_Attack.md`:
\begin{equation}
S_X(\rho_\star)
=
\rho_\star\int_2^X\frac{\psi(x)-x}{x^{\rho_\star+1}\log x}\,dx
+B_X+E_X(T),
\tag{R}
\end{equation}
i.e. produce a **lower** bound for \(S_X(\rho_\star)\) or for a phase-aligned form of \(\psi-x\) at frequency \(\gamma_\star\).

---

## 0. Two classical engines

| Engine | What it does | Output type |
|--------|----------------|-------------|
| **Littlewood Ω (1914+)** | Forces \(\psi(x)-x\) (or \(\pi-\mathrm{li}\)) to be large **both ways** infinitely often | Pointwise-in-\(x\) Ω-results |
| **Resonance (HL ideas → Soundararajan 2008)** | Forces large values of Dirichlet polynomials / \(\zeta(1/2+it)\) on a **positive-measure** set of \(t\) | Measure-theoretic large values |

Neither is, as stated, a lower bound for \(S_X\) **at a fixed zero ordinate**. The rest of this note records exact statements, mechanisms, and the precise gap to B\(_\theta\).

---

# Part A — Littlewood’s Ω-results

## A.1 Classical statements

**Theorem L1 (Littlewood, 1914).**  
\begin{equation}
\pi(x)-\operatorname{li}(x)
=
\Omega_\pm\Biggl(
\frac{\sqrt{x}\,\log\log\log x}{\log x}
\Biggr).
\tag{L1}
\end{equation}
In particular \(\pi(x)-\operatorname{li}(x)\) changes sign infinitely often.  
(Equivalent formulations for \(\psi(x)-x\) and \(\theta(x)-x\) differ by smooth translation factors.)

**Theorem L2 (size under RH / on-line zeros).**  
If all zeros with \(\lvert\gamma\rvert\le T\) lie on \(\operatorname{Re}=\tfrac12\), Dirichlet approximation produces \(x\) at which many terms \(x^{\rho}/\rho\) **align in argument**, yielding the \(\sqrt{x}\,\log\log\log x\) scale in (L1).

**Theorem L3 (zero of large real part ⇒ larger Ω).**  
If \(\zeta(\beta+i\gamma)=0\) with \(\beta>1/2\), then
\begin{equation}
\psi(x)-x
=
\Omega\bigl(x^{\beta}\bigr)
\tag{L3}
\end{equation}
in the sense that
\begin{equation}
\limsup_{x\to\infty}\frac{\lvert\psi(x)-x\rvert}{x^{\beta}}
>0
\tag{L3b}
\end{equation}
(standard consequence of the explicit formula / Landau–Ingham theory; constants depend on \(\rho=\beta+i\gamma\) and on whether other zeros sit at the same abscissa).  
More precisely, one may take
\begin{equation}
\limsup_{x\to\infty}
\frac{\lvert\psi(x)-x\rvert}{x^{\beta}/\lvert\rho\rvert}
\ge 1
-
\varepsilon_{\mathrm{other}},
\tag{L3c}
\end{equation}
where \(\varepsilon_{\mathrm{other}}\) accounts for possible cancellation by other zeros of real part \(\ge\beta\) (if \(\rho_\star\) is a rightmost zero of multiplicity \(m\), the leading coefficient is \(m/\rho_\star\)).

**References (literature, not re-proved here).**  
Littlewood, *Sur la distribution des nombres premiers*, C. R. Acad. Sci. 1914;  
Ingham, *The Distribution of Prime Numbers*;  
Titchmarsh, Ch. IX–X;  
modern surveys on Ω-results (Pintz, etc.).

## A.2 Mechanism: phase alignment of **zeros** at a chosen \(x\)

Littlewood’s argument (schematic):

1. Explicit formula: \(\psi(x)-x \approx -\sum_{\rho} x^{\rho}/\rho\).  
2. Fix a long finite list of zeros \(\rho_n=\beta_n+i\gamma_n\).  
3. Seek \(x=\exp(u)\) so that the angles
   \[
   \gamma_n u - \operatorname{Arg}\rho_n
   \]
   are **simultaneously near \(0\) or \(\pi\)** (Dirichlet’s approximation theorem on the torus \(\mathbb{R}^{N}/\mathbb{Z}^{N}\) for the frequencies \(\gamma_n/(2\pi)\)).  
4. When phases align, the sum \(\sum x^{\rho_n}/\rho_n\) has size \(\asymp \sum x^{\beta_n}/\lvert\rho_n\rvert\).  
5. On RH, \(\beta_n=1/2\), and one optimizes \(N\sim\log\log\log x\) frequencies to get (L1).

**Key structural point for our programme:**

> Littlewood aligns **many zeros’ phases at one \(x\)**.  
> B\(_\theta\) needs **one fixed frequency \(\gamma_\star\)** (from a single zero) to align with **primes** (through \(\psi-x\)), integrated against \(x^{-\rho_\star}/(x\log x)\).

These are **dual** alignment problems:

| | Littlewood | B\(_\theta\) residual |
|--|------------|----------------------|
| Free variable | \(x\) (or \(u=\log x\)) | \(X\) (upper limit) / integrand in \(x\) |
| Objects aligned | zero angles \(\gamma_n u\) | prime angles via \(\psi\), vs fixed \(\gamma_\star u\) |
| Goal | large \(\lvert\sum x^{\rho}/\rho\rvert\) | large \(\bigl\lvert\int(\psi-x)x^{-\rho_\star-1}(\log x)^{-1}dx\bigr\rvert\) |

## A.3 What L3 gives for the residual integral

From (R), a lower bound on \(S_X\) would follow if
\begin{equation}
I(X)
:=
\int_2^X\frac{\psi(x)-x}{x^{\rho_\star+1}\log x}\,dx
\tag{I}
\end{equation}
is large.

**Lemma A.1 (absolute vs phase).**  
L3 says there is a sequence \(x_k\to\infty\) with
\[
\bigl\lvert\psi(x_k)-x_k\bigr\rvert
\ge
c\,x_k^{\beta_\star}.
\]
If these spikes are **too narrow** or **randomly phased** relative to \(x^{-i\gamma_\star}\), their contribution to \(I(X)\) may cancel.  
A single spike of width \(w_k\) at \(x_k\) contributes to \(I\) at most
\begin{equation}
\ll
\frac{\lvert\psi-x\rvert}{x_k^{\beta_\star+1}\log x_k}\cdot w_k
\ll
\frac{c\,w_k}{x_k\log x_k}.
\tag{spike}
\end{equation}
To accumulate \(\gg\log\log X\) one needs either:

- many aligned spikes with \(\sum w_k/(x_k\log x_k)\gg\log\log X\), or  
- long intervals where \(\operatorname{Re}\bigl(e^{-i\gamma_\star\log x}(\psi-x)x^{-\beta_\star}\bigr)\) stays positive.

**Lemma A.2 (one-zero dominance heuristic — not a theorem).**  
If \(\rho_\star\) is a **rightmost** zero and no other zero has \(\beta\ge\beta_\star\), then for \(u\) near a point where \(\operatorname{Arg}(e^{\rho_\star u}/\rho_\star)\approx\pi\) (so \(-x^{\rho_\star}/\rho_\star\) is large positive in a fixed direction),
\[
\psi(e^u)-e^u
\sim
-\frac{e^{\rho_\star u}}{\rho_\star}
+
\text{(smaller)},
\]
hence
\[
(\psi-x)\,x^{-\rho_\star}
\sim
-\frac{1}{\rho_\star}
+
o(1)
\]
on a positive-density set of \(u\)-scales if lower zeros are negligible. Integrating against \(du/u\) would then give
\[
I(e^{U})
\sim
-\frac{1}{\rho_\star}\log U
=
-\frac{1}{\rho_\star}\log\log X,
\]
i.e. B\(_\theta\) quantitative.

**Status of the heuristic.**  
The error “lower zeros negligible uniformly on long \(u\)-intervals” is **not proved**. It is essentially as strong as controlling the sum of all other \(x^{\rho}/\rho\) against a single term — the same difficulty as zero-density / zero-repulsion problems in the half-plane \(\operatorname{Re}s\ge\beta_\star-\delta\).

**Honesty freeze:** L3 alone does **not** imply B\(_\theta\). The gap is **phase-stable one-zero dominance on logarithmic measure**.

## A.4 Littlewood’s method as a template for phase-stable dominance

Littlewood shows that **Dirichlet approximation can force simultaneous alignment**.  
A B\(_\theta\)-oriented variant would be:

**Target L-Bθ (open).**  
Assume \(\zeta(\rho_\star)=0\), \(\beta_\star>1/2\), and \(\rho_\star\) rightmost (or isolated at its abscissa).  
Prove there exist \(U_n\to\infty\) and \(\delta_n>0\) such that for all \(u\in[U_n,U_n+\delta_n]\),
\begin{equation}
\operatorname{Re}\Biggl(
-\frac{e^{(\rho_\star)u}}{\rho_\star}
-
\sum_{\rho\neq\rho_\star,\lvert\gamma\rvert\le T(u)}
\frac{e^{\rho u}}{\rho}
\Biggr)
\ge
\frac{c\,e^{\beta_\star u}}{\lvert\rho_\star\rvert},
\tag{L-Bθ}
\end{equation}
with \(\delta_n\ge c'/\log U_n\) (enough mass for \(\int du/u\gg c''\)).

This is a **Littlewood-type alignment with a distinguished term protected**.  
Unconditional technology does not currently deliver (L-Bθ).

---

# Part B — Resonance methods

## B.1 Hardy–Littlewood background

Hardy–Littlewood developed:

- approximate functional equation for \(\zeta\);
- moment estimates (e.g. second moment \(\int_0^T\lvert\zeta(1/2+it)\rvert^2\,dt\sim T\log T\));
- large-value technology for Dirichlet polynomials via mean values.

These are the **ancestors** of modern resonance: compare a Dirichlet polynomial to \(\zeta\) in mean square and extract large values.

## B.2 Soundararajan resonance (2008) — precise shape

**Source.** K. Soundararajan, *Extreme values of zeta and \(L\)-functions*, Math. Ann. (2008); arXiv:0708.3990.

**Resonator.** A Dirichlet polynomial
\begin{equation}
R(t)=\sum_{n\le N}r(n)\,n^{-it},
\qquad N\le T^{1-\varepsilon}.
\tag{res}
\end{equation}
**Moments.**
\begin{equation}
M_1=\int\lvert R(t)\rvert^2\Phi(t/T)\,dt,
\qquad
M_2=\int\zeta(1/2+it)\lvert R(t)\rvert^2\Phi(t/T)\,dt.
\tag{mom}
\end{equation}
**Extraction.**
\begin{equation}
\max_{T\le t\le 2T}\lvert\zeta(1/2+it)\rvert
\ge
\frac{\lvert M_2\rvert}{M_1}.
\tag{extract}
\end{equation}

**Theorem S1 (Soundararajan).** For large \(T\), some \(t\in[T,2T]\) has
\begin{equation}
\lvert\zeta(1/2+it)\rvert
\ge
\exp\Biggl((1+o(1))\frac{\sqrt{\log T}}{\sqrt{\log\log T}}\Biggr).
\tag{S1}
\end{equation}
Moreover a lower bound on the **measure** of such \(t\) is given for \(V\) up to \(\asymp\sqrt{\log T/\log\log T}\).

**Coefficient choice (schematic).** Multiplicative \(r(p)\approx L/(\sqrt{p}\log p)\) on a prime range optimized so that \(R\) correlates with the partial Euler product / Dirichlet series of \(\zeta\).

## B.3 Resonance for \(S_X(\sigma+it)\) — what transfers

Define the partial sum as a function of height:
\begin{equation}
S_X(\sigma+it)
=
\sum_{n\le X}\frac{\Lambda(n)}{n^{\sigma+it}\log n}.
\tag{SXt}
\end{equation}
This is a Dirichlet polynomial (weighted) of length \(X\).

**Proposition B.1 (resonance template — classical pattern).**  
For a resonator \(R(t)=\sum_{n\le N}r(n)n^{-it}\) with \(N\) small vs the \(t\)-window,
\begin{equation}
\max_{t\in[T,2T]}\bigl\lvert S_X(\sigma+it)\bigr\rvert
\ge
\frac{
\bigl\lvert\int S_X(\sigma+it)\lvert R(t)\rvert^2\Phi(t/T)\,dt\bigr\rvert
}{
\int\lvert R(t)\rvert^2\Phi(t/T)\,dt
},
\tag{res-S}
\end{equation}
provided the integrals exist (smooth \(\Phi\)). Expanding,
\[
\int S_X\lvert R\rvert^2
=
\sum_{n\le X}\frac{\Lambda(n)}{n^{\sigma}\log n}
\sum_{m,k\le N}r(m)\overline{r(k)}
\int\Bigl(\frac{k}{mn}\Bigr)^{it}\Phi
\]
and the \(t\)-integral detects \(mn\approx k\) (diagonal / near-diagonal).

**Proposition B.2 (achievable conclusion — schematic).**  
By optimizing \(r\) as in Soundararajan, for fixed \(\sigma\in[1/2,1)\) and \(X=T^{\theta}\) in a suitable range, one expects
\begin{equation}
\max_{t\in[T,2T]}\bigl\lvert S_X(\sigma+it)\bigr\rvert
\gg
\exp\bigl(c\sqrt{\log T}/\sqrt{\log\log T}\bigr)
\quad\text{or at least }\gg (\log\log T)^{c},
\tag{res-large}
\end{equation}
on a positive-measure set of \(t\) — **by the same method**, subject to writing error terms carefully for the \(\Lambda/\log\) weights (routine compared to \(\zeta\)).

**Status:** (res-large) at **generic** \(t\) is in reach of published resonance technology.  
**It is not B\(_\theta\).** B\(_\theta\) needs \(t=\gamma_\star\) **exactly** (or \(t\) in a tiny window about \(\gamma_\star\) of width \(o(1/\log X)\)).

## B.4 The measure problem (hard obstruction)

Resonance produces a set \(E_T\subset[T,2T]\) with
\begin{equation}
\operatorname{meas}(E_T)
\gg
\frac{T}{(\log T)^{O(1)}}
\exp\bigl(-c V^2/\log\log T\bigr)
\tag{meas}
\end{equation}
for height \(\ge e^{V}\) of \(\lvert\zeta\rvert\) or \(\lvert S_X\rvert\).

Zero ordinates in \([T,2T]\) number \(\asymp T\log T\).  
The probability a **fixed** ordinate \(\gamma_\star\) lands in \(E_T\) is not controlled: \(E_T\) is defined by a continuous average, not forced to contain arithmetic special points.

**Lemma B.3 (measure vs points).**  
Even if \(\operatorname{meas}(E_T)/T\to 1\), a specific sequence \(\gamma_n\) of zero ordinates need not meet \(E_{|\gamma_n|}\) infinitely often without an independent equidistribution / independence statement between zeros and the resonance set.

**L4 firewall.**  
Assuming “zeros are independent of the resonator maximum set” is a heuristic (GUE + random model). Using it to prove B\(_\theta\) to feed RH would be circular if the independence encodes RH-scale spacing. Conditional theorems are fine if labelled.

## B.5 Resonance **at a zero** — blocked shapes

| Attempt | Blocker |
|---------|---------|
| Put \(t=\gamma_\star\) into (extract) | Resonance only lower-bounds a **max on an interval**, not a prescribed point |
| Shorten window to \([\gamma_\star-h,\gamma_\star+h]\) with \(h\to 0\) | Measure of \(E\) may be \(\gg T/\mathrm{polylog}\) but still \(o(h)\) if \(h\) tiny; method collapses |
| Resonator built from primes to match \(n^{-i\gamma_\star}\) | That is just trying to lower-bound \(\lvert S_X(\rho_\star)\rvert\) **directly** — circular unless a new inequality appears |
| Use \(\zeta(\rho_\star)=0\) inside \(M_2\) | \(\zeta(\rho_\star)=0\) kills the object; \(S_X\) is not \(\log\zeta\) |

---

# Part C — Synthesis: what is usable for B\(_\theta\)

## C.1 Usable unconditional facts

| Fact | Use for residual (R) |
|------|----------------------|
| L3: \(\psi-x=\Omega(x^{\beta_\star})\) if zero at \(\beta_\star\) | Spike size exists; need width + phase |
| Explicit formula | Express \(\psi-x\) as \(-\sum x^{\rho}/\rho+\cdots\) |
| Dirichlet approximation (Littlewood engine) | Align **zeros** at chosen \(x\); dual to our need |
| Resonance (Soundararajan) | Large \(S_X(\sigma+it)\) for **many** \(t\); not fixed \(\gamma_\star\) |
| Residual formula (19) | Identity: B\(_\theta\) \(\Leftrightarrow\) large \(I(X)\) |

## C.2 Non-usable as proofs of B\(_\theta\)

| Claim | Why it fails |
|-------|----------------|
| “Littlewood Ω \(\Rightarrow\) B\(_\theta\)” | Spikes may miss phase / logarithmic measure |
| “Resonance \(\Rightarrow\) B\(_\theta\)” | Wrong variable: \(t\) free, \(\gamma_\star\) fixed |
| “Self \(\log\log\Rightarrow\) B\(_\theta\)” | Cancelled (signed-sum note) |
| “One zero dominates for all large \(x\)” | Not proved; other zeros interfere |

## C.3 Sharp open problems (pure, ordered)

### OP1 — Phase-stable one-zero dominance (Littlewood dual)
Prove (L-Bθ) for a rightmost zero, or a weaker version with \(\int_{U}^{U+\delta}\operatorname{Re}(\cdots)\,du/u\gg c\).

### OP2 — Sparse resonance hitting zeros
Prove that the resonance large-value set \(E_T\) meets \(\{\gamma:\zeta(\beta_\star+i\gamma)=0\}\) under a density hypothesis on off-line zeros (conditional B\(_\theta\) under “zeros not avoiding \(E_T\)”).

### OP3 — Direct Ω for \(S_X(\rho_\star)\)
By Landau–type theorems for Dirichlet series: if \(F(s)=\sum\Lambda(n)/(n^{s}\log n)\) has a singularity at \(\rho_\star\) in some sense… but \(F\) is entire of a sort as a finite sum for each \(X\), and the limit \(X\to\infty\) is \(\log\zeta\) with a log singularity at zeros.  
**Partial idea:** for \(s\to\rho_\star\), \(\log\zeta(s)\sim\log(s-\rho_\star)\), while partial sums \(S_X(s)\) approximate \(\log\zeta(s)\) for \(\operatorname{Re}s>1\) and via analytic continuation in regions free of zeros. Near \(\rho_\star\), the rate at which \(S_X(\rho_\star)\) can stay bounded as \(X\to\infty\) is constrained by how well truncated Euler products approximate \(\zeta\) — related to GHK / hybrid products.  
**Status:** this loops to M1.2/GHK, not a free win.

### OP4 — Effective Ω with explicit phase
Refine L3 to
\begin{equation}
\limsup_{x\to\infty}
\operatorname{Re}\Bigl(
e^{-i\varphi}
(\psi(x)-x)\,x^{-\rho_\star}
\Bigr)
\ge c>0
\tag{OP4}
\end{equation}
for a **prescribed** phase \(\varphi\) (e.g. \(\varphi=0\)).  
Littlewood’s method gives some phase (the aligned direction); **prescribing** the phase while keeping size \(x^{\beta_\star}\) is the content of Dirichlet approximation with a linear constraint — still possible on the torus if enough free frequencies remain.  
**Lemma C.1 (phase prescription — classical torus).**  
Given frequencies \(\gamma_1,\ldots,\gamma_N\) and target angles, Dirichlet approximation still works for \(N-1\) free conditions after fixing one linear form (the phase of the \(\rho_\star\) term).  
So **prescribing the phase of the \(\rho_\star\) term** is fine; the obstruction is controlling the **tail** of zeros not in the finite approximating set — same as Littlewood’s original truncation problem, harder off the line.

## C.4 Conditional theorem form (honest)

**Proposition C.2 (conditional — not proved end-to-end).**  
Assume \(\rho_\star\) is a simple rightmost zero and
\begin{equation}
\sum_{\rho\neq\rho_\star}
\frac{x^{\beta-\beta_\star}}{\lvert\rho\rvert}
\le
\tfrac12\frac{1}{\lvert\rho_\star\rvert}
\quad\text{for all \(x\) in a sequence of intervals with }\int\frac{dx}{x\log x}=\infty.
\tag{dom}
\end{equation}
Then \(I(X)\to\infty\) along a subsequence and B\(_\theta\) holds for \(\rho_\star\).

**Status of (dom):** open; stronger than standard density bounds in short intervals.

---

# Part D — Scoreboard and non-claims

| Item | Standing |
|------|----------|
| Littlewood L1–L3 (literature) | **Theorems** |
| Resonance S1 (literature) | **Theorem** |
| Residual formula (R) | **Proved** (prior note) |
| L3 \(\Rightarrow\) B\(_\theta\) | **False as implication** without phase/measure |
| Resonance \(\Rightarrow\) B\(_\theta\) | **False as implication** (wrong variable) |
| Phase-stable dominance (L-Bθ) | **Open** |
| B\(_\theta\) | **Open** |
| RH | **Open** |

**Non-claims.**  
No proof of B\(_\theta\). No RH. No Category B.  
Literature theorems are cited, not re-proved in full.

---

## One-liner

> Littlewood gives Ω for \(\psi-x\) by aligning **zeros** at a chosen \(x\); resonance gives large \(S_X\) at **many** \(t\); B\(_\theta\) needs phase-stable **one-zero** dominance at frequency \(\gamma_\star\) (or a zero hitting a resonance set) — both open, dual to classical methods but not implied by them.
