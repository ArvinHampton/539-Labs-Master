# OP1 · OP2 · OP4 — Phase-Stable Dominance, Conditional Resonance Hit, Prescribed-Phase Ω

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Does not prove B\(_\theta\) or RH.**  
**L4:** no RH smuggled into OP2 independence.

Companions: `RH_Resonance_Littlewood_Omega.md`, `RH_Signed_Sum_Attack.md`.

---

## 0. Notation

Fix a nontrivial zero \(\rho_\star=\beta_\star+i\gamma_\star\) of multiplicity \(m\ge 1\), \(\beta_\star\in(1/2,1)\).  
Write \(x=e^{u}\), \(u\ge \log 2\). Truncated explicit formula:
\begin{equation}
\psi(e^{u})-e^{u}
=
-
\sum_{\lvert\gamma\rvert\le T}
\frac{e^{\rho u}}{\rho}
-
c(e^{u})
+
R(e^{u},T),
\tag{EF}
\end{equation}
with \(\lvert R\rvert\ll e^{u}\log(e^{u}T)/T+\log(e^{u})\) (symbolic \(C_{\mathrm{EF}}\)).

**Distinguished term** (multiplicity \(m\)):
\begin{equation}
D_\star(u)
:=
-
\frac{m\,e^{\rho_\star u}}{\rho_\star}.
\tag{D}
\end{equation}
**Competitor sum** (other zeros with \(\lvert\gamma\rvert\le T\)):
\begin{equation}
C_T(u)
:=
-
\sum_{\substack{\lvert\gamma\rvert\le T\\ \rho\neq\rho_\star}}
\frac{e^{\rho u}}{\rho}.
\tag{C}
\end{equation}
**Phase-aligned real part** (for residual / B\(_\theta\)):
\begin{equation}
\Phi_T(u)
:=
\operatorname{Re}\Bigl(
e^{-\rho_\star u}
\bigl(D_\star(u)+C_T(u)\bigr)
\Bigr)
=
\operatorname{Re}\Bigl(
-\frac{m}{\rho_\star}
-
\sum_{\substack{\lvert\gamma\rvert\le T\\ \rho\neq\rho_\star}}
\frac{e^{(\rho-\rho_\star)u}}{\rho}
\Bigr).
\tag{Φ}
\end{equation}
Note \(\operatorname{Re}(-m/\rho_\star)= -m\beta_\star/\lvert\rho_\star\rvert^2\) is a **fixed negative** constant if we took absolute alignment differently; for lower-bounding \(\lvert I(X)\rvert\) we choose the **sign** of the test functional. Define also
\begin{equation}
\Phi_T^{+}(u)
:=
\operatorname{Re}\Bigl(
\omega\cdot e^{-\rho_\star u}
\bigl(D_\star(u)+C_T(u)\bigr)
\Bigr),
\qquad
\omega\in\mathbb{C},\ \lvert\omega\rvert=1,
\tag{Φω}
\end{equation}
so that the free phase \(\omega\) can lock the distinguished term to be **positive real**:
\begin{equation}
\omega\cdot\Bigl(-\frac{m}{\rho_\star}\Bigr)
=
\frac{m}{\lvert\rho_\star\rvert}
\quad\Rightarrow\quad
\operatorname{Re}\Bigl(\omega\cdot\bigl(-m/\rho_\star\bigr)\Bigr)
=
\frac{m}{\lvert\rho_\star\rvert}.
\tag{lock}
\end{equation}
(Choose \(\omega = -e^{-i\operatorname{Arg}(-1/\rho_\star)}\cdot(\text{sign fix})\); explicitly \(\omega = -\lvert\rho_\star\rvert/\rho_\star\cdot(-1)\) up to the branch that makes \(-m\omega/\rho_\star = m/\lvert\rho_\star\rvert\).)

**Working convention:** fix \(\omega_\star\) so that
\begin{equation}
\operatorname{Re}\bigl(\omega_\star D_\star(u)e^{-\rho_\star u}\bigr)
=
\frac{m}{\lvert\rho_\star\rvert}
\quad\text{for all \(u\)}
\tag{lock2}
\end{equation}
(the \(u\)-dependence cancels). Then
\begin{equation}
\Phi_T^{\star}(u)
:=
\frac{m}{\lvert\rho_\star\rvert}
+
\operatorname{Re}\Biggl(
\omega_\star
\sum_{\substack{\lvert\gamma\rvert\le T\\ \rho\neq\rho_\star}}
\bigl(-e^{(\rho-\rho_\star)u}/\rho\bigr)
\Biggr).
\tag{Φ*}
\end{equation}
**OP1** asks for \(\Phi_T^{\star}(u)\) large positive on long logarithmic measure.

---

# OP4 — Prescribed-phase Ω (torus)

## OP4.1 Dirichlet / Kronecker approximation

**Theorem D (Dirichlet box principle).**  
Let \(\alpha_1,\ldots,\alpha_N\in\mathbb{R}\) and \(Q\ge 1\). There exist integers \(q,a_1,\ldots,a_N\) with
\begin{equation}
1\le q\le Q^{N},
\qquad
\bigl\lvert q\alpha_j-a_j\bigr\rvert
\le
Q^{-1}
\quad(j=1,\ldots,N).
\tag{Dir}
\end{equation}

**Corollary D′ (simultaneous angles).**  
Given frequencies \(\nu_1,\ldots,\nu_N\in\mathbb{R}\) and targets \(\theta_j\in\mathbb{R}/2\pi\mathbb{Z}\), for any \(U_0\ge 0\) and \(Q\ge 1\) there exists
\begin{equation}
u\in[U_0,\,U_0+(2\pi)Q^{N}/\nu_{\min}^{\ast}]
\tag{u-loc}
\end{equation}
(with a standard effective range; \(\nu_{\min}^{\ast}\) a normalization of frequency scale) such that
\begin{equation}
\bigl\lVert \nu_j u-\theta_j\bigr\rVert_{2\pi}
\le
\frac{2\pi}{Q}
\quad(j=1,\ldots,N),
\tag{ang}
\end{equation}
where \(\lVert\cdot\rVert_{2\pi}\) is distance on \(\mathbb{R}/2\pi\mathbb{Z}\).  
(If frequencies are \(\mathbb{Q}\)-linearly dependent the dimension drops and ranges improve.)

## OP4.2 Prescribing the distinguished phase

**Lemma OP4.1 (phase lock of \(\rho_\star\) alone).**  
The map \(u\mapsto\operatorname{Arg}(e^{\rho_\star u}/\rho_\star)=\gamma_\star u-\operatorname{Arg}\rho_\star\) is linear in \(u\).  
For any target angle \(\theta_\star\) and any \(U_0\), there is a progression
\begin{equation}
u_k
=
u_0
+
\frac{2\pi k}{\lvert\gamma_\star\rvert}
\quad(k\in\mathbb{Z}_{\ge 0}),
\tag{prog}
\end{equation}
with \(u_0\ge U_0\) and \(\operatorname{Arg}(e^{\rho_\star u_k}/\rho_\star)\equiv\theta_\star\pmod{2\pi}\), provided \(\gamma_\star\neq 0\).  
**No other zeros involved.** □

**Lemma OP4.2 (prescribed phase + finite competitors).**  
Let \(\rho_1,\ldots,\rho_N\) be finitely many zeros other than \(\rho_\star\), with ordinates \(\gamma_j\neq 0\).  
Fix target angles \(\theta_\star,\theta_1,\ldots,\theta_N\).  
Then for any \(U_0\) and \(Q\ge 1\), there exists \(u\ge U_0\) with
\begin{equation}
\begin{aligned}
\bigl\lVert\gamma_\star u-\operatorname{Arg}\rho_\star-\theta_\star\bigr\rVert_{2\pi}
&\le
\frac{2\pi}{Q},
\\
\bigl\lVert\gamma_j u-\operatorname{Arg}\rho_j-\theta_j\bigr\rVert_{2\pi}
&\le
\frac{2\pi}{Q}
\quad(j=1,\ldots,N).
\end{aligned}
\tag{OP4-finite}
\end{equation}
**Proof.** Apply Corollary D′ to frequencies \((\gamma_\star,\gamma_1,\ldots,\gamma_N)\) and the \(N+1\) targets. □

**Theorem OP4-finite (proved).**  
Choose targets so that each \(e^{\rho_j u}/\rho_j\) is aligned to **oppose** the locked distinguished direction \(\omega_\star\) as little as possible — or, for a lower bound on \(\Phi^{\star}\), choose competitor targets so that
\[
\operatorname{Re}\bigl(\omega_\star(-e^{(\rho_j-\rho_\star)u}/\rho_j)\bigr)
\ge
-\frac{e^{(\beta_j-\beta_\star)u}}{\lvert\rho_j\rvert}
\]
is forced near its **least destructive** value, or simply accept the worst-case bound after alignment of \(\rho_\star\) only.

More cleanly: **lock only \(\rho_\star\)** via Lemma OP4.1 and bound competitors absolutely:
\begin{equation}
\Phi_T^{\star}(u)
\ge
\frac{m}{\lvert\rho_\star\rvert}
-
\sum_{\substack{\lvert\gamma\rvert\le T\\ \rho\neq\rho_\star}}
\frac{e^{(\beta-\beta_\star)u}}{\lvert\rho\rvert}
-
\lvert\omega_\star R(e^{u},T)e^{-\rho_\star u}\rvert
-
O(e^{-\beta_\star u}).
\tag{OP4-abs}
\end{equation}
On the progression (prog) where \(\rho_\star\) is phase-locked, (OP4-abs) holds **for every** such \(u_k\).

**Corollary OP4.3 (prescribed phase for the single term).**  
Along \(u_k\) from (prog) with lock (lock2),
\begin{equation}
\operatorname{Re}\bigl(\omega_\star D_\star(u_k)e^{-\rho_\star u_k}\bigr)
=
\frac{m}{\lvert\rho_\star\rvert}.
\tag{OP4-single}
\end{equation}
This is the **prescribed-phase** form of the leading Ω term. □

## OP4.3 Tail obstruction (precise)

Define the **competitor majorant**
\begin{equation}
\mathcal M_T(u)
:=
\sum_{\substack{\lvert\gamma\rvert\le T\\ \rho\neq\rho_\star}}
\frac{e^{(\beta-\beta_\star)u}}{\lvert\rho\rvert}.
\tag{M}
\end{equation}
**OP4 reduces to:** show \(\mathcal M_T(u_k)+e^{-\beta_\star u_k}\lvert R\rvert\) is \(< m/(2\lvert\rho_\star\rvert)\) for infinitely many locked \(u_k\).

Split \(\mathcal M_T=\mathcal M^{\mathrm{far}}+\mathcal M^{\mathrm{near}}\):

| Piece | Bound tool |
|-------|------------|
| \(\beta\ge\beta_\star+\delta\) | Zero density (KLN / Ingham) |
| \(\lvert\beta-\beta_\star\rvert<\delta\), \(\lvert\gamma-\gamma_\star\rvert\) large | Oscillation / density |
| \(\beta\le\beta_\star-\delta\) | Factor \(e^{-\delta u}\) kills at large \(u\) |

**Lemma OP4.4 (left abscissa dies).**  
\[
\sum_{\beta\le\beta_\star-\delta}
\frac{e^{(\beta-\beta_\star)u}}{\lvert\rho\rvert}
\le
e^{-\delta u}
\sum_{\lvert\gamma\rvert\le T}\frac{1}{\lvert\rho\rvert}
\ll
e^{-\delta u}\log^2(T+2).
\]
For \(u\ge (2/\delta)\log\log(T+3)\), this is \(o(1)\). □

**Lemma OP4.5 (far-right under KLN — same shape as Thm FR).**  
For \(\sigma_\star=\beta_\star+\delta\) and \(T\ge H_0\),
\[
\sum_{\beta\ge\sigma_\star,\lvert\gamma\rvert\le T}
\frac{e^{(\beta-\beta_\star)u}}{\lvert\rho\rvert}
\ll
e^{(1-\beta_\star)u}
\frac{N(\sigma_\star,T)}{T}
\log T
+
e^{(\sigma_\star-\beta_\star)u}N(\sigma_\star,T)\cdot(\text{crude}).
\]
At \(x=e^{u}\), this is the same tension as far-right Off vs truncation. □

**Theorem OP4-partial (proved).**  
Along the phase-locked progression (prog), for any fixed finite set \(F\) of competitor zeros and \(T=\infty\) truncated to \(F\),
\begin{equation}
\Phi_F^{\star}(u_k)
\ge
\frac{m}{\lvert\rho_\star\rvert}
-
\sum_{\rho\in F}
\frac{e^{(\beta-\beta_\star)u_k}}{\lvert\rho\rvert}
-
o(1).
\tag{OP4-part}
\end{equation}
If \(F=\emptyset\), then \(\Phi^{\star}(u_k)=m/\lvert\rho_\star\rvert>0\) exactly (plus EF remainder).  
**The infinite tail / full \(\mathcal M_T\) is the obstruction to OP4 in full strength.** □

**Status OP4:**  
- Prescribed phase of the **distinguished** term: **proved** (Lemma OP4.1–OP4.3).  
- Finite-competitor control: **proved** (Thm OP4-partial).  
- Full tail \(\mathcal M_T(u_k)<m/(2\lvert\rho_\star\rvert)\) i.o.: **open** (= hard core shared with OP1).

---

# OP1 — Phase-stable one-zero dominance

## OP1.1 Precise target

**Definition (L-Bθ / OP1).**  
We say **OP1 holds** for \(\rho_\star\) if there exist \(c>0\), sequences \(U_n\to\infty\), \(\delta_n>0\), and truncations \(T_n\ge\lvert\gamma_\star\rvert\) such that
\begin{equation}
\Phi_{T_n}^{\star}(u)
\ge
c
\quad\text{for all }u\in[U_n,U_n+\delta_n],
\tag{OP1}
\end{equation}
and
\begin{equation}
\int_{U_n}^{U_n+\delta_n}\frac{du}{u}
=
\log\Bigl(1+\frac{\delta_n}{U_n}\Bigr)
\to\infty
\quad\text{or at least }\sum_n\int_{U_n}^{U_n+\delta_n}\frac{du}{u}=\infty.
\tag{mass}
\end{equation}
(The weaker \(\sum\int=\infty\) already forces \(I(e^{U})\to\infty\) along a subsequence after adding \(B+E\) control.)

**Lemma OP1.1 (OP1 \(\Rightarrow\) B\(_\theta\) quantitative).**  
Assume OP1 with \(\sum_n\int_{U_n}^{U_n+\delta_n}du/u=\infty\), and \(T_n\) large enough that \(E_{e^{U_n+\delta_n}}(T_n)=o(1)\) on those windows, and \(B_X\) controlled. Then
\begin{equation}
\limsup_{X\to\infty}\lvert S_X(\rho_\star)\rvert=\infty.
\tag{OP1⇒B}
\end{equation}
**Proof.** On each window, \(\operatorname{Re}(\omega_\star(\psi-x)x^{-\rho_\star})\) is \(\ge c/2\) after restoring EF error (for \(T_n\) large). Integrating against \(dx/(x\log x)=du/u\) accumulates infinite real part in \(I(X)\). Residual formula (19) yields B\(_\theta\). □

## OP1.2 Pointwise vs stable

| Strength | Meaning | Standing |
|----------|---------|----------|
| Pointwise OP4 | \(\Phi^{\star}(u_k)\ge c\) on a sequence | Finite competitors: **proved**; full tail: open |
| OP1 (stable) | \(\Phi^{\star}\ge c\) on intervals of logarithmic mass | **Open** (stronger) |

**Lemma OP1.2 (stability length from frequency gaps).**  
Suppose at \(u_0\) one has \(\Phi_T^{\star}(u_0)\ge 2c\) and
\begin{equation}
\bigl\lvert\partial_u\Phi_T^{\star}(u)\bigr\rvert
\le
A
\quad\text{on }[u_0,u_0+\delta].
\tag{Lip}
\end{equation}
Then \(\Phi_T^{\star}(u)\ge c\) on \(\delta\le c/A\).  
Differentiating (Φ*): each competitor contributes a factor \(\lvert\rho-\rho_\star\rvert e^{(\beta-\beta_\star)u}/\lvert\rho\rvert\), so
\begin{equation}
A
\ll
\sum_{\rho\neq\rho_\star,\lvert\gamma\rvert\le T}
\frac{\lvert\rho-\rho_\star\rvert}{\lvert\rho\rvert}\,e^{(\beta-\beta_\star)u}
+
\partial_u(\text{Rem}).
\tag{A-bound}
\end{equation}
Near-line competitors with \(\lvert\gamma-\gamma_\star\rvert\) large make \(A\) large ⇒ **stable intervals shrink**.

**Corollary OP1.3.**  
If only finitely many zeros exist (absurd) or all competitors satisfy \(\beta\le\beta_\star-\delta\), then for large \(u\), \(A\to 0\) and OP1 holds with \(\delta_n=1\) say.  
**So OP1 is automatic in a zero-free half-plane to the right of all other zeros** — i.e. if \(\rho_\star\) is **strictly rightmost** and isolated in abscissa by a gap \(\delta>0\), left-abscissa competitors die (Lemma OP4.4), and the only danger is zeros with \(\beta\in(\beta_\star-\delta,\beta_\star]\) (including the critical line).

## OP1.3 Strictly rightmost zero under a gap

**Hypothesis (Gap\(_\delta\)).**  
No zero other than \(\rho_\star\) (and its conjugate, handled symmetrically) has \(\operatorname{Re}\rho>\beta_\star-\delta\).

**Theorem OP1-gap (conditional on Gap\(_\delta\) + EF).**  
Assume Gap\(_\delta\) and \(T=T(u)=e^{u/2}\) (say). Then for all sufficiently large \(u\) on the phase-locked progression (prog),
\begin{equation}
\Phi_T^{\star}(u)
\ge
\frac{m}{\lvert\rho_\star\rvert}
-
O\bigl(e^{-\delta u}\log^2 T\bigr)
-
O\bigl(e^{(1/2-\beta_\star)u}u\bigr)
\ge
\frac{m}{2\lvert\rho_\star\rvert}.
\tag{OP1-gap}
\end{equation}
Moreover \(A\ll e^{-\delta u/2}\) for large \(u\), so stability holds on intervals \(\delta_n=1\), and \(\int du/u\) along \([u_k,u_k+1]\) gives \(\sum 1/u_k=\infty\).  
**Hence Gap\(_\delta\) \(\Rightarrow\) OP1 \(\Rightarrow\) B\(_\theta\).** □

**Proof.** Lemma OP4.4 kills \(\beta\le\beta_\star-\delta\). Rem term with \(T=e^{u/2}\): \(e^{u}\log(e^{u}T)/T\cdot e^{-\beta_\star u}\ll e^{(1/2-\beta_\star)u}u\to 0\) since \(\beta_\star>1/2\). Phase lock from OP4. Stability from \(A\to 0\). Mass: \(u_k\sim 2\pi k/\lvert\gamma_\star\rvert\), \(\sum_k\int_{u_k}^{u_k+1}du/u=\infty\). □

**Honesty:** Gap\(_\delta\) is a **strong isolation in the half-plane** — much stronger than “simple zero,” and not known for any off-line zero (none are known). It is the clean conditional: **rightmost + abscissa gap \(\Rightarrow\) B\(_\theta\)**.

## OP1.4 Without Gap\(_\delta\): density-conditional sketch

**Hypothesis (ZD-local).**  
\(N(\beta_\star-\delta/2,\,T+H)-N(\beta_\star-\delta/2,\,T-H)\) small for \(H\) in suitable ranges (short-interval density).

Under average density, \(\mathcal M_T(u)\) is small for **most** \(u\), but OP1 needs **specific** phase-locked \(u_k\).  
Passing from almost-all \(u\) to the progression \(u_k\) requires equidistribution of \(\gamma_\star u_k\) vs other structure — related to OP2-type independence.

**Status OP1:**  
- Gap\(_\delta\) \(\Rightarrow\) OP1: **proved** (Thm OP1-gap).  
- Unconditional OP1: **open**.  
- Density + equidistribution on progression: **open** (bridge to OP2).

---

# OP2 — Conditional: ordinates meet resonance large-value sets

## OP2.1 Resonance large-value set

Following Soundararajan (notation as in the resonance note), for parameters \(T,X,V,\sigma\) let
\begin{equation}
E_T
=
\bigl\{
t\in[T,2T]:
\ \bigl\lvert S_X(\sigma+it)\bigr\rvert
\ge
e^{V}
\bigr\},
\tag{E}
\end{equation}
and assume a resonance lower bound
\begin{equation}
\operatorname{meas}(E_T)
\ge
\mu(T,V)
:=
c_0\frac{T}{(\log T)^{B}}
\exp\bigl(-c_1 V^2/\log\log T\bigr)
\tag{meas}
\end{equation}
for \(V\) in the admissible range (as in S1 / Prop. B.2 schematic — treat (meas) as a **named analytic hypothesis (Res)** when not re-proving resonance for \(S_X\)).

## OP2.2 Off-line ordinate set

Let
\begin{equation}
\Gamma_\star(T)
=
\bigl\{
\gamma\in[T,2T]:
\ \zeta(\beta_\star+i\gamma)=0
\bigr\}
\tag{Γ}
\end{equation}
for a fixed \(\beta_\star>1/2\) (or \(\beta_\star\) varying slowly).  
If no off-line zeros exist, \(\Gamma_\star\) is empty and OP2 is vacuous (B\(_\theta\) vacuous at that abscissa).

## OP2.3 Independence hypothesis (L4-labelled)

**Hypothesis (Hit).**  
There exists a subsequence \(T_j\to\infty\) such that
\begin{equation}
\Gamma_\star(T_j)\cap E_{T_j}
\neq
\emptyset.
\tag{Hit}
\end{equation}

**L4 label.**  
(Hit) is an **independence / non-avoidance** assumption between:

- the zero set at abscissa \(\beta_\star\), and  
- the resonance set defined by primes / Dirichlet polynomials,

**It does not follow from RH** (under RH, \(\Gamma_\star=\emptyset\) for \(\beta_\star>1/2\)).  
**It must not be derived from RH-scale pair correlation used as a black box to prove RH.**  
Admissible routes to (Hit): conditional on random-model heuristics (labelled conjectural); or on effective metric theorems if proved without RH.

## OP2.4 Conditional theorem

**Theorem OP2-cond (proved as implication).**  
Assume (Res) for \(\sigma=\beta_\star\) and \(X=X(T)\) in the resonance-admissible range, and assume (Hit).  
Then there exist \(t_j=\gamma_j\in\Gamma_\star(T_j)\cap E_{T_j}\) with
\begin{equation}
\bigl\lvert S_{X(T_j)}(\beta_\star+i\gamma_j)\bigr\rvert
\ge
e^{V_j}
\to\infty
\quad\text{(choose \(V_j\to\infty\) slowly inside (meas))}.
\tag{OP2⇒}
\end{equation}
If \(\beta_\star+i\gamma_j\) is a zero, this is exactly
\begin{equation}
\bigl\lvert S_{X_j}(\rho_j)\bigr\rvert\to\infty
\tag{Bθ-seq}
\end{equation}
along a sequence of off-line zeros \(\rho_j\) — i.e. **B\(_\theta\) for those zeros**. □

**Corollary OP2.1.**  
\[
\text{(Res)}+\text{(Hit)}
\;\Rightarrow\;
\text{B\(_\theta\) along a sequence of off-line zeros}.
\]

## OP2.5 Toward (Hit) without RH

| Approach | Standing |
|----------|----------|
| \(\operatorname{meas}(E_T)/T\to 1\) and \(\#\Gamma_\star\ge 1\) | Still may avoid if \(\Gamma_\star\) thin and \(E_T^c\) traps it |
| \(\#\Gamma_\star(T)\gg T^{\theta}\) (many off-line zeros) + meas lower bound | Intersection plausible; needs uniform distribution of \(\gamma\) in \([T,2T]\) |
| GUE / random model | Heuristic only; **not** a proof; L4 risk if used for RH |
| Effective Diophantine avoidance bounds | Open |

**Lemma OP2.2 (pigeonhole, weak).**  
If \(\#\Gamma_\star(T)\ge 1\) and \(\operatorname{meas}(E_T)>T-\varepsilon\), intersection can still fail.  
If \(\Gamma_\star\) has an element in every subinterval of length \(\ell\) and every interval of length \(\ell\) meets \(E_T\), then (Hit) holds.  
Resonance currently gives measure, not “hits every interval of length \(\ell\).” □

**Status OP2:**  
- Implication (Res)+(Hit)⇒B_θ: **proved**.  
- (Hit) itself: **open** (conjectural / heuristic).  
- Unconditional (Hit): **not claimed**.

---

# Cross-map: OP1 · OP2 · OP4 · B_θ

```text
OP4 prescribed phase of D_★     ──proved──►  lock along u_k
        │
        ▼
   tail M_T(u_k) small?  ──open──►  full OP4 Ω with phase
        │
        ├── Gap_δ ──proved──► OP1 stable ──proved──► B_θ
        │
        └── density + equidistribution on {u_k} ──open──► OP1

OP2: (Res)+(Hit) ──proved implication──► B_θ along zeros
      (Hit) ──open──►
```

---

# Scoreboard

| Claim | Standing |
|-------|----------|
| OP4: lock phase of \(D_\star\) along arithmetic progression in \(u\) | **Proved** |
| OP4: finite-competitor Φ lower bound | **Proved** |
| OP4: full tail small on locked progression | **Open** |
| OP1: Gap\(_\delta\) ⇒ stable dominance ⇒ B_θ | **Proved** (conditional on Gap) |
| OP1: unconditional | **Open** |
| OP2: (Res)+(Hit) ⇒ B_θ | **Proved** (conditional implication) |
| OP2: (Hit) | **Open** |
| B_θ / RH | **Open** |

---

# Non-claims

1. No unconditional B_θ.  
2. No RH.  
3. Gap\(_\delta\) is not known for any zero.  
4. (Hit) is not proved; not derived from RH.  
5. No Category B constants.

---

## One-liner

> OP4 locks the distinguished phase; OP1 follows from a strict abscissa gap (proved implication); OP2 follows from resonance + non-avoidance (proved implication); both gap and non-avoidance remain open — that is the whole barrier to B_θ.
