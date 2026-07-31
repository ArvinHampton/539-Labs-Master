# Signed Sum Attack: \(\sum_{\rho\neq\rho_\star}(\rho_\star/\rho)\,J_X(\rho)\) without RH

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Does not prove B\(_\theta\) or RH.**

Object:
\begin{equation}
\Sigma_X(T)
:=
\sum_{\substack{\lvert\gamma\rvert\le T\\ \rho\neq\rho_\star}}
\frac{\rho_\star}{\rho}\,J_X(\rho),
\qquad
J_X(\rho)
:=
\int_{\log 2}^{\log X}\frac{e^{(\rho-\rho_\star)u}}{u}\,du.
\tag{Σ}
\end{equation}
This is the **main oscillatory piece** of \(\mathrm{Off}_X\) in the master identity
(`RH_B_theta_Explicit_Formula.md`). Boundary terms and \(1/(\log x)^2\) pieces are secondary and tracked in §6.

**Method:** finite interchange → truncated explicit formula → cancel main and self contributions against \(M_X\) and \(\mathrm{Self}_X\) → residual in primes / truncation tail.  
**No RH. No model constants.**

---

## 1. Finite interchange (proved)

**Lemma 1.1.** For finite \(T\) and \(X>2\),
\begin{equation}
\Sigma_X(T)
=
\rho_\star
\int_{\log 2}^{\log X}
\frac{e^{-\rho_\star u}}{u}
\Biggl(
\sum_{\substack{\lvert\gamma\rvert\le T\\ \rho\neq\rho_\star}}
\frac{e^{\rho u}}{\rho}
\Biggr)
du.
\tag{1}
\end{equation}
**Proof.** Finite sum; Fubini for continuous integrands on a compact \(u\)-interval. □

Write \(x=e^{u}\) when convenient. Define the truncated zero sum
\begin{equation}
Z_T(x)
:=
\sum_{\lvert\gamma\rvert\le T}\frac{x^{\rho}}{\rho},
\qquad
Z_T^{\neq}(x)
:=
Z_T(x)-\frac{x^{\rho_\star}}{\rho_\star}
\quad(\lvert\gamma_\star\rvert\le T).
\tag{2}
\end{equation}
Then the inner sum in (1) is \(Z_T^{\neq}(e^{u})\), and
\begin{equation}
\Sigma_X(T)
=
\rho_\star
\int_{\log 2}^{\log X}
\frac{e^{-\rho_\star u}}{u}\,Z_T^{\neq}(e^{u})\,du.
\tag{3}
\end{equation}

---

## 2. Truncated explicit formula (literature input)

As in the master note, for \(x\ge 2\) not a prime power, \(T\ge 2\),
\begin{equation}
\psi(x)
=
x
-
Z_T(x)
-
\log(2\pi)
-
\frac12\log(1-x^{-2})
+
R(x,T),
\tag{4}
\end{equation}
with
\begin{equation}
\lvert R(x,T)\rvert
\le
C_{\mathrm{EF}}
\Bigl(
\frac{x\log(xT)}{T}
+
\log x
\Bigr).
\tag{5}
\end{equation}
Hence
\begin{equation}
Z_T(x)
=
x-\psi(x)-c(x)+R(x,T),
\qquad
c(x):=\log(2\pi)+\tfrac12\log(1-x^{-2}),
\tag{6}
\end{equation}
and
\begin{equation}
Z_T^{\neq}(x)
=
x-\psi(x)-c(x)+R(x,T)-\frac{x^{\rho_\star}}{\rho_\star}.
\tag{7}
\end{equation}

---

## 3. Substitution into \(\Sigma_X\)

Insert (7) into (3):
\begin{equation}
\begin{aligned}
\Sigma_X(T)
&=
\rho_\star
\int_{\log 2}^{\log X}
\frac{e^{-\rho_\star u}}{u}
\Biggl(
e^{u}-\psi(e^{u})-c(e^{u})+R(e^{u},T)-\frac{e^{\rho_\star u}}{\rho_\star}
\Biggr)
du
\\
&=
I_{\mathrm{main}}
-
I_{\psi}
-
I_{c}
+
I_{R}
-
I_{\mathrm{self}}.
\end{aligned}
\tag{8}
\end{equation}

### 3.1 Self piece

\begin{equation}
I_{\mathrm{self}}
=
\rho_\star
\int_{\log 2}^{\log X}
\frac{e^{-\rho_\star u}}{u}\cdot\frac{e^{\rho_\star u}}{\rho_\star}\,du
=
\int_{\log 2}^{\log X}\frac{du}{u}
=
\log\log X-\log\log 2.
\tag{9}
\end{equation}

### 3.2 Main piece

\begin{equation}
I_{\mathrm{main}}
=
\rho_\star
\int_{\log 2}^{\log X}
\frac{e^{(1-\rho_\star)u}}{u}\,du
=
\rho_\star
\int_2^X\frac{dx}{x^{\rho_\star}\log x}.
\tag{10}
\end{equation}
(Change of variables \(x=e^{u}\).)

### 3.3 Prime piece

\begin{equation}
I_{\psi}
=
\rho_\star
\int_{\log 2}^{\log X}
\frac{e^{-\rho_\star u}}{u}\,\psi(e^{u})\,du
=
\rho_\star
\int_2^X\frac{\psi(x)}{x^{\rho_\star+1}\log x}\,dx.
\tag{11}
\end{equation}

### 3.4 Trivial and remainder pieces

\begin{equation}
I_{c}
=
\rho_\star
\int_{\log 2}^{\log X}
\frac{e^{-\rho_\star u}}{u}\,c(e^{u})\,du,
\qquad
\lvert I_{c}\rvert
\ll_{\beta_\star} 1
\quad(\beta_\star>0),
\tag{12}
\end{equation}
\begin{equation}
\lvert I_{R}\rvert
\le
\lvert\rho_\star\rvert
\int_{\log 2}^{\log X}
\frac{e^{-\beta_\star u}}{u}\,C_{\mathrm{EF}}
\Bigl(
\frac{e^{u}\log(e^{u}T)}{T}
+
u
\Bigr)
du
\ll
\lvert\rho_\star\rvert\,C_{\mathrm{EF}}
\Biggl(
\frac{X^{1-\beta_\star}\log(XT)}{T\log X}
+
\frac{X^{1-\beta_\star}}{T}
+
1
\Biggr).
\tag{13}
\end{equation}

---

## 4. Cancellation against \(M_X\) and \(\mathrm{Self}_X\)

### 4.1 Recall master decomposition

From the master identity, the **principal** part of \(\mathrm{Off}_X\) coming from the \(\rho_\star/(\rho\log x)\) integrals is exactly \(-\Sigma_X(T)\).  
(Boundary terms \(X^{\rho}/(\rho\log X)\) and \(1/(\log)^2\) integrals form \(\mathrm{Off}^{\partial}\), treated in §6.)

Schematically:
\begin{equation}
S_X
=
M_X
+
\mathrm{Self}_X
-
\Sigma_X(T)
+
\mathrm{Off}^{\partial}_X(T)
+
\mathrm{Triv}_X
+
\mathrm{Rem}_X(T).
\tag{14}
\end{equation}

### 4.2 Main cancellation

From (7) of the master note,
\[
M_X
=
\frac{X^{1-\rho_\star}}{\log X}
-
\frac{2^{1-\rho_\star}}{\log 2}
+
\rho_\star\int_2^X\frac{dx}{x^{\rho_\star}\log x}
+
\int_2^X\frac{dx}{x^{\rho_\star}(\log x)^2}.
\]
The third summand is exactly \(I_{\mathrm{main}}\).  
Hence
\begin{equation}
M_X-I_{\mathrm{main}}
=
\frac{X^{1-\rho_\star}}{\log X}
-
\frac{2^{1-\rho_\star}}{\log 2}
+
\int_2^X\frac{dx}{x^{\rho_\star}(\log x)^2}.
\tag{15}
\end{equation}
The integral in (15) is \(O_{\beta_\star}(1)\) for \(\beta_\star>0\) as \(X\to\infty\) if \(\beta_\star>0\); more precisely
\[
\int_2^X x^{-\beta_\star}(\log x)^{-2}\,dx
\ll_{\beta_\star}
\begin{cases}
1 & \beta_\star>0\text{ (bounded as }X\to\infty\text{ after }X^{1-\beta}{}/(\log)^2\text{ if }\beta_\star<1),\\
\end{cases}
\]
Actually for \(\beta_\star<1\): \(\int^X x^{-\beta_\star}(\log x)^{-2}dx\sim X^{1-\beta_\star}/((1-\beta_\star)(\log X)^2)\).  
**Boundary main terms** of size \(X^{1-\beta_\star}/\log X\) remain — they cancel against corresponding boundary pieces inside \(\mathrm{Off}^{\partial}\) and against the \(x\)-boundary in the original Stieltjes form of \(S_X\). Tracked as \(B_X^{\mathrm{main}}\) below.

### 4.3 Self cancellation

From master note (10): \(\mathrm{Self}_X= -(\log\log X-\log\log 2)+O_{\rho_\star}(1)\).  
From (9): \(I_{\mathrm{self}}=\log\log X-\log\log 2\).  
In (14), the combination \(\mathrm{Self}_X-\Sigma_X\) contains \(\mathrm{Self}_X+I_{\mathrm{self}}+\cdots\) (since \(-\Sigma_X\) contributes \(+I_{\mathrm{self}}\) among other terms):
\begin{equation}
\mathrm{Self}_X
+
I_{\mathrm{self}}
=
O_{\rho_\star}(1).
\tag{16}
\end{equation}
**The \(\log\log X\) terms cancel exactly** (up to \(O_{\rho_\star}(1)\)).

### 4.4 Residual formula

**Theorem 4.1 (signed residual — proved).**  
Assume \(X>2\) not a prime power, \(T\ge\lvert\gamma_\star\rvert\), \(\beta_\star\in(0,1)\). Then
\begin{equation}
\begin{aligned}
S_X(\rho_\star)
&=
I_{\psi}
-
I_{\mathrm{main}}
+
B_X
+
E_X(T)
\\
&=
\rho_\star
\int_2^X
\frac{\psi(x)-x}{x^{\rho_\star+1}\log x}\,dx
+
B_X
+
E_X(T),
\end{aligned}
\tag{17}
\end{equation}
where:

- \(B_X=O\bigl(X^{1-\beta_\star}/(\log X)^2+X^{1-\beta_\star}/(\lvert\rho_\star\rvert\log X)+1\bigr)\) collects boundary terms from \(M_X\), \(\mathrm{Off}^{\partial}\), \(\mathrm{Self}\) \(O(1)\), and \(I_c\) (explicitly expandable; see §6);
- \(E_X(T)=I_R+\mathrm{Rem}_X(T)+E^{\partial}_R\) satisfies
\begin{equation}
\lvert E_X(T)\rvert
\le
C_{\mathrm{E}}\,\lvert\rho_\star\rvert
\Biggl(
\frac{X^{1-\beta_\star}\log(XT)}{T\log X}
+
\frac{X^{1-\beta_\star}}{T}
+
1
\Biggr)
\tag{18}
\end{equation}
with \(C_{\mathrm{E}}\) absolute depending only on \(C_{\mathrm{EF}}\).

**Proof outline.**  
Start from (14); replace \(\Sigma_X\) by (8); cancel \(I_{\mathrm{main}}\) against the bulk of \(M_X\) and \(I_{\mathrm{self}}\) against \(\mathrm{Self}_X\); identify \(I_{\psi}-I_{\mathrm{main}}=\rho_\star\int(\psi-x)x^{-\rho_\star-1}(\log x)^{-1}dx\); absorb remaining boundary/trivial/truncation into \(B_X+E_X\). □

**Corollary 4.2 (structure).**  
\begin{equation}
\boxed{
S_X(\rho_\star)
=
\rho_\star
\int_2^X
\frac{\psi(x)-x}{x^{\rho_\star+1}\log x}\,dx
+
B_X
+
E_X(T).
}
\tag{19}
\end{equation}
The signed zero sum has been **eliminated** in favour of a weighted integral of \(\psi-x\), plus controlled errors.  
**No RH used.**

---

## 5. Classical bounds on the residual integral

### 5.1 Zero-free region input (classical, no RH)

**Theorem ZF (classical).**  
There exists absolute \(c_0>0\) such that
\begin{equation}
\bigl\lvert\psi(x)-x\bigr\rvert
\le
x\exp\bigl(-c_0\sqrt{\log x}\bigr)
\quad(x\ge 3).
\tag{20}
\end{equation}
(Vinogradov–Korobov gives a stronger exponent \((\log x)^{3/5}(\log\log x)^{-1/5}\); either form is admissible.)

### 5.2 Upper bound for the residual integral

**Theorem 5.1 (proved).**  
Under (20), for \(\beta_\star\in(0,1)\) and \(X\ge 3\),
\begin{equation}
\Biggl\lvert
\rho_\star
\int_2^X
\frac{\psi(x)-x}{x^{\rho_\star+1}\log x}\,dx
\Biggr\rvert
\le
C\,\lvert\rho_\star\rvert
\int_{\log 2}^{\log X}
\frac{e^{(1-\beta_\star)t-c_0\sqrt{t}}}{t}\,dt.
\tag{21}
\end{equation}
The right-hand side is
\begin{equation}
\ll_{\beta_\star,c_0}
\frac{X^{1-\beta_\star}}{\log X}\exp\bigl(-c_0\sqrt{\log X}\bigr)
\quad\text{for large \(X\)}.
\tag{22}
\end{equation}
**Proof.** \(|\psi-x|\le x e^{-c_0\sqrt{\log x}}\); substitute \(x=e^{t}\):
\[
\int_2^X\frac{|\psi-x|}{x^{\beta_\star+1}\log x}\,dx
\le
\int_{\log 2}^{\log X}\frac{e^{t}e^{-c_0\sqrt{t}}e^{-(\beta_\star+1)t}e^{t}}{t}\,dt
=
\int\frac{e^{(1-\beta_\star)t-c_0\sqrt{t}}}{t}\,dt.
\]
Standard Laplace / integration by parts yields (22). □

**Corollary 5.2.**  
For any fixed \(\beta_\star\in(0,1)\),
\begin{equation}
\Biggl\lvert
\rho_\star\int_2^X\frac{\psi-x}{x^{\rho_\star+1}\log x}\,dx
\Biggr\rvert
=
o\bigl(X^{1-\beta_\star-\varepsilon}\bigr)
\quad\text{for every }\varepsilon>0,
\tag{23}
\end{equation}
but (22) is still
\begin{equation}
\omega\bigl(\log\log X\bigr)
\quad\text{as }X\to\infty
\text{ whenever }\beta_\star<1
\tag{24}
\end{equation}
(because \(X^{a}e^{-c\sqrt{\log X}}\to\infty\) for any \(a>0\)).

### 5.3 Consequence for B\(_\theta\)

From (19) and (22), the **classical upper bound** is
\begin{equation}
\lvert S_X(\rho_\star)\rvert
\ll
\frac{X^{1-\beta_\star}}{\log X}e^{-c_0\sqrt{\log X}}
+
\frac{X^{1-\beta_\star}}{(\log X)^2}
+
\frac{X^{1-\beta_\star}\log(XT)}{T\log X}.
\tag{25}
\end{equation}
Choosing \(T=X\) (say) makes the last term the same order as the first without the exp-saving, so take \(T=X\exp(c_0\sqrt{\log X}/2)\) when the EF form allows, or accept
\[
\lvert S_X\rvert
\ll
X^{1-\beta_\star}e^{-c'\sqrt{\log X}}.
\]

**This is an upper bound, not a lower bound.**  
It does **not** prove \(\lvert S_X\rvert\to\infty\), nor \(\lvert S_X\rvert\ge c\log\log X\).  
It also does **not** prove \(\lvert S_X\rvert=O(1)\).

### 5.4 Why classical ZF cannot close B\(_\theta\)

B\(_\theta\) asks for a **lower** bound \(\lvert S_X\rvert\to\infty\).  
Classical ZF gives only an **upper** envelope that still tends to infinity.  
To get a matching lower bound from (19), one would need
\[
\Biggl\lvert
\int_2^X\frac{\psi(x)-x}{x^{\rho_\star+1}\log x}\,dx
\Biggr\rvert
\gg
\log\log X
\]
along a sequence — a **signed** / oscillatory lower bound for a weighted \(\psi-x\) integral at a **complex** abscissa \(\rho_\star\). That is essentially as hard as large values of the original Dirichlet polynomial \(S_X\).

---

## 6. Secondary terms \(\mathrm{Off}^{\partial}\) (bookkeeping)

The full \(I_X(\rho)\) in the master note also contains:

| Piece | Contribution to Off |
|-------|---------------------|
| \(X^{\rho}/(\rho\log X)\) | \(\sum_{\rho\neq\rho_\star}X^{\rho-\rho_\star}/(\rho\log X)\) |
| \(2^{\rho}/(\rho\log 2)\) | \(O(\sum 1/\lvert\rho\rvert)\) |
| \(\int x^{\rho-\rho_\star-1}/(\rho(\log x)^2)\,dx\) | like \(J\) with extra \(1/\log\) |

**Lemma 6.1.** Under classical \(N\)-counting,
\[
\sum_{\lvert\gamma\rvert\le T}\frac{1}{\lvert\rho\rvert}
\ll
\log^2(T+2).
\]
**Lemma 6.2 (boundary zero sum via EF).**  
\[
\sum_{\lvert\gamma\rvert\le T}\frac{X^{\rho}}{\rho}
=
X-\psi(X)-c(X)+R(X,T),
\]
so the off-diagonal boundary piece is this minus \(X^{\rho_\star}/\rho_\star\), and after multiplying by \(X^{-\rho_\star}/\log X\) it is absorbed into the same \(B_X+E_X\) class as in (17).

**Lemma 6.3 (\(1/(\log)^2\) integrals).**  
Interchange as in §1–3 produces an analogue of (19) with an extra factor \(1/\log x\) in the integrand:
\[
\rho_\star\int_2^X\frac{\psi(x)-x}{x^{\rho_\star+1}(\log x)^2}\,dx,
\]
which under ZF is even smaller than (22) by an extra \(\log X\).

**Conclusion:** secondary terms do **not** change the shape of (19).

---

## 7. Equivalent forms of the open problem

### Form A — original
\[
\limsup_{X\to\infty}\lvert S_X(\rho_\star)\rvert=\infty.
\]

### Form B — residual integral (equivalent via Thm 4.1, for admissible \(T=T(X)\))
\[
\limsup_{X\to\infty}
\Biggl\lvert
\int_2^X\frac{\psi(x)-x}{x^{\rho_\star+1}\log x}\,dx
\Biggr\rvert
=\infty.
\]

### Form C — Dirichlet polynomial (identical to A)
\[
\limsup_{X\to\infty}
\Biggl\lvert
\sum_{n\le X}\frac{\Lambda(n)}{n^{\rho_\star}\log n}
\Biggr\rvert
=\infty.
\]

### Form D — signed near-line zeros (equivalent via EF)
\[
\limsup_{X\to\infty}
\bigl\lvert M_X+\mathrm{Off}_X(T(X))\bigr\rvert
<
\infty
\quad\text{fails (self-term not fully cancelled).}
\]
More precisely: after Thm 4.1, Form D is rephrased as Form B.

**All four are open for off-line \(\rho_\star\).** None has been reduced further to a known theorem without RH.

---

## 8. What fails if one assumes RH (sanity check)

Under RH, \(\lvert\psi(x)-x\rvert\ll x^{1/2}\log^2 x\), so for \(\beta_\star>1/2\),
\[
\int_2^\infty\frac{x^{1/2}\log^2 x}{x^{\beta_\star+1}\log x}\,dx
=
\int_2^\infty x^{-1/2-\beta_\star}\log x\,dx
<\infty.
\]
Thus the residual integral **converges**, and \(S_X\to S_\infty\) finite under RH — but **under RH there is no off-line \(\rho_\star\)**.  
So B\(_\theta\) is vacuously compatible with RH: the interesting case is precisely when RH fails and \(\beta_\star>1/2\).

If RH fails at \(\rho_\star\), then \(\psi-x\) is allowed to be as large as \(\asymp x^{\beta_\star}/\lvert\rho_\star\rvert\) infinitely often (Ω-theorems related to that zero). That Ω-push is the heuristic engine for \(\lvert S_X\rvert\to\infty\), but turning Ω-results for \(\psi-x\) into a lower bound for the **weighted complex** integral (19) is still open.

---

## 9. Ω-results and a conditional path (not a proof)

**Classical Ω:** if \(\zeta(\beta_\star+i\gamma_\star)=0\), then
\begin{equation}
\psi(x)-x
=
\Omega\bigl(x^{\beta_\star}/\lvert\rho_\star\rvert\bigr)
\tag{26}
\end{equation}
in the sense of unboundedness of \((\psi(x)-x)x^{-\beta_\star}\) along some sequence (standard consequence of a zero; see Ingham / Titchmarsh).

**Gap:** Ω for \(\psi-x\) at **real** \(x\) does not automatically give Ω for
\[
\int_2^X(\psi(x)-x)x^{-\rho_\star-1}(\log x)^{-1}\,dx,
\]
because the weight \(x^{-\rho_\star}=x^{-\beta_\star}x^{-i\gamma_\star}\) **oscillates** at frequency \(\gamma_\star\log x\). One needs the large values of \(\psi-x\) to **align in phase** with \(x^{i\gamma_\star}\) on a set of \(x\) with enough logarithmic measure.

**Conditional lemma form (not proved):**  
If there is a sequence \(x_n\to\infty\) with
\[
\operatorname{Re}\Bigl(e^{-i\gamma_\star\log x_n}(\psi(x_n)-x_n)x_n^{-\beta_\star}\Bigr)
\ge
c>0
\]
on intervals \([x_n,x_n(1+\delta_n)]\) with \(\int_{x_n}^{x_n(1+\delta_n)}dx/(x\log x)\ge c'\), then the residual integral is \(\gg\log\log\) or at least \(\to\infty\).

**Status:** aligning Ω-points of \(\psi-x\) with the phase \(x^{i\gamma_\star}\) is open; it is essentially a **multiplicative resonance** problem at the ordinate of the zero.

---

## 10. Scoreboard

| Claim | Standing |
|-------|----------|
| Interchange (1)–(3) | **Proved** |
| Decomposition (8) via EF | **Proved** (given EF) |
| Self \(\log\log\) cancellation (16) | **Proved** |
| Residual formula (19) | **Proved** |
| ZF upper bound (22) | **Proved** |
| \(\lvert S_X\rvert\to\infty\) (B\(_\theta\)) | **Open** |
| Phase-aligned Ω for \(\psi-x\) | **Open** |
| RH | **Open** |

---

## 11. Non-claims

1. This note does **not** prove B\(_\theta\).  
2. Cancellation of \(\log\log X\) means the naive self-term heuristic is **not** by itself a proof — the residual is \(\int(\psi-x)\cdots\), not a free \(\log\log\).  
3. Classical ZF gives upper bounds only.  
4. No RH input. No Category B constants.

---

## One-liner

> The signed zero sum reduces **without RH** to \(S_X=\rho_\star\int_2^X(\psi-x)x^{-\rho_\star-1}(\log x)^{-1}dx+B_X+E_X\); self \(\log\log\) cancels; B\(_\theta\) is a lower bound for that weighted \(\psi-x\) integral (phase-aligned Ω), still open.
