# B\(_\theta\): Explicit Formula Identity for \(S_X(\rho_\star)\)

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Strength:** classical bookkeeping toward Conjecture B\(_\theta\).  
**Does not prove B\(_\theta\) or RH.**

Goal: write a **fully rigorous** truncated identity expressing
\[
S_X(\rho_\star)
=
\sum_{n\le X}\frac{\Lambda(n)}{n^{\rho_\star}\log n}
\]
in terms of a **self-term**, an **off-diagonal zero sum**, a **main term**, and an **error**, so that the open problem is isolated as a single estimate.

---

## 1. Stieltjes starting point (proved)

Let \(\psi(x)=\sum_{n\le x}\Lambda(n)\). For \(X>2\) not a prime power and \(\rho_\star=\beta+i\gamma\) with \(\beta\in(0,1)\),
\begin{equation}
S_X(\rho_\star)
=
\int_{2-}^{X}\frac{d\psi(x)}{x^{\rho_\star}\log x}.
\tag{1}
\end{equation}
Integration by parts (Stieltjes) with \(U(x)=\psi(x)\), \(dV=x^{-\rho_\star}(\log x)^{-1}dx\):

Set
\[
f(x)=\frac{1}{x^{\rho_\star}\log x}.
\]
Then for \(2\le a<b\), not prime powers,
\begin{equation}
\int_a^b f\,d\psi
=
\psi(b)f(b)-\psi(a)f(a)
-
\int_a^b\psi(x)f'(x)\,dx.
\tag{2}
\end{equation}
Compute
\begin{equation}
f'(x)
=
-\frac{\rho_\star}{x^{\rho_\star+1}\log x}
-
\frac{1}{x^{\rho_\star+1}(\log x)^2}.
\tag{3}
\end{equation}
Hence with \(a=2\), \(b=X\),
\begin{equation}
\begin{aligned}
S_X(\rho_\star)
&=
\psi(X)f(X)-\psi(2)f(2)
+
\int_2^X\psi(x)\frac{\rho_\star}{x^{\rho_\star+1}\log x}\,dx
\\
&\quad
+
\int_2^X\psi(x)\frac{1}{x^{\rho_\star+1}(\log x)^2}\,dx.
\end{aligned}
\tag{4}
\end{equation}
**Lemma 1.** Identity (4) is unconditional for \(X>2\) not a prime power. □

---

## 2. Truncated explicit formula (literature input)

**Theorem EF (classical, truncated form).**  
There exists an absolute \(C_{\mathrm{EF}}>0\) such that for \(x\ge 2\), \(T\ge 2\),
\begin{equation}
\psi(x)
=
x
-
\sum_{\lvert\operatorname{Im}\rho\rvert\le T}\frac{x^{\rho}}{\rho}
-
\log(2\pi)
-
\frac12\log\bigl(1-x^{-2}\bigr)
+
R(x,T),
\tag{5}
\end{equation}
where the sum runs over nontrivial zeros with multiplicity, and
\begin{equation}
\lvert R(x,T)\rvert
\le
C_{\mathrm{EF}}
\Biggl(
\frac{x\log(xT)}{T}
+
\log x
\Biggr)
\tag{6}
\end{equation}
when \(x\) is not a prime power (standard references: Davenport, *Multiplicative Number Theory*, Ch. 17; explicit constants available in the literature of platform estimates — we keep \(C_{\mathrm{EF}}\) symbolic).

**We treat (5)–(6) as external classical input**, not re-proved here.

---

## 3. Substitution

Insert (5) into (4). Write \(\psi=x-\sum_{\lvert\gamma\rvert\le T}x^{\rho}/\rho-\log(2\pi)-\frac12\log(1-x^{-2})+R\).

### 3.1 Main term \(x\)

\begin{equation}
\begin{aligned}
M_X
&:=
Xf(X)-2f(2)
+
\int_2^X x\cdot\frac{\rho_\star}{x^{\rho_\star+1}\log x}\,dx
+
\int_2^X x\cdot\frac{1}{x^{\rho_\star+1}(\log x)^2}\,dx
\\
&=
\frac{X^{1-\rho_\star}}{\log X}
-
\frac{2^{1-\rho_\star}}{\log 2}
+
\rho_\star\int_2^X\frac{dx}{x^{\rho_\star}\log x}
+
\int_2^X\frac{dx}{x^{\rho_\star}(\log x)^2}.
\end{aligned}
\tag{7}
\end{equation}

### 3.2 Self-term \(\rho=\rho_\star\)

From \(-\sum x^{\rho}/\rho\), the summand \(\rho=\rho_\star\) contributes
\begin{equation}
\begin{aligned}
\mathrm{Self}_X(T)
&:=
-\frac{X^{\rho_\star}}{\rho_\star}f(X)
+\frac{2^{\rho_\star}}{\rho_\star}f(2)
\\
&\quad
-\int_2^X\frac{x^{\rho_\star}}{\rho_\star}\cdot\frac{\rho_\star}{x^{\rho_\star+1}\log x}\,dx
\\
&\quad
-\int_2^X\frac{x^{\rho_\star}}{\rho_\star}\cdot\frac{1}{x^{\rho_\star+1}(\log x)^2}\,dx
\\
&=
-\frac{1}{\rho_\star\log X}
+\frac{2^{0}}{\rho_\star\log 2}\cdot\frac{2^{\rho_\star}}{2^{\rho_\star}}
\\
&\quad
-
\int_2^X\frac{dx}{x\log x}
-
\frac{1}{\rho_\star}
\int_2^X\frac{dx}{x(\log x)^2}.
\end{aligned}
\tag{8}
\end{equation}
Simplify the middle integral:
\begin{equation}
\int_2^X\frac{dx}{x\log x}
=
\log\log X-\log\log 2.
\tag{9}
\end{equation}
The last integral equals \(1/\log 2-1/\log X\) by \(d(1/\log x)= -dx/(x(\log x)^2)\).  
Hence
\begin{equation}
\boxed{
\mathrm{Self}_X
=
-\bigl(\log\log X-\log\log 2\bigr)
+
O\Bigl(\frac{1}{\lvert\rho_\star\rvert\log X}+\frac{1}{\lvert\rho_\star\rvert}\Bigr).
}
\tag{10}
\end{equation}
**The \(\log\log X\) self-term is unconditional** once EF is inserted and \(\lvert\gamma_\star\rvert\le T\) (so \(\rho_\star\) appears in the sum).

### 3.3 Off-diagonal zeros

\begin{equation}
\begin{aligned}
\mathrm{Off}_X(T)
&:=
-
\sum_{\substack{\lvert\gamma\rvert\le T\\ \rho\neq\rho_\star}}
\Biggl[
\frac{X^{\rho}}{\rho}f(X)
-
\frac{2^{\rho}}{\rho}f(2)
+
\int_2^X\frac{x^{\rho}}{\rho}\bigl(-f'(x)\bigr)\,dx
\Biggr].
\end{aligned}
\tag{11}
\end{equation}
Using \(-f'(x)=\rho_\star x^{-\rho_\star-1}(\log x)^{-1}+x^{-\rho_\star-1}(\log x)^{-2}\),
\begin{equation}
\int_2^X\frac{x^{\rho}}{\rho}\cdot\frac{\rho_\star}{x^{\rho_\star+1}\log x}\,dx
=
\frac{\rho_\star}{\rho}
\int_2^X\frac{x^{\rho-\rho_\star-1}}{\log x}\,dx.
\tag{12}
\end{equation}

### 3.4 Smooth / trivial / remainder pieces

Let \(\mathrm{Triv}_X\) collect the \(-\log(2\pi)-\frac12\log(1-x^{-2})\) insertions (absolutely \(O_\beta(1)\) after integration against \(f'\) for \(\beta>0\)).  
Let \(\mathrm{Rem}_X(T)\) collect \(R(x,T)\) insertions; by (6) and \(\int_2^X x^{-1-\beta}(\log x)^{-1}dx\ll_\beta 1\),
\begin{equation}
\lvert\mathrm{Rem}_X(T)\rvert
\le
C_{\mathrm{EF}}'
\Biggl(
\frac{X^{1-\beta}\log(XT)}{T\log X}
+
\frac{\log X}{T}X^{1-\beta}
+
1
\Biggr)
\tag{13}
\end{equation}
for an absolute \(C_{\mathrm{EF}}'\) depending only on the shape of (6) (symbolic).

---

## 4. Master identity

**Proposition 4.1 (master identity — classical).**  
Let \(X>2\) not a prime power, \(T\ge\lvert\gamma_\star\rvert\), \(\beta\in(0,1)\). Then
\begin{equation}
S_X(\rho_\star)
=
M_X
+
\mathrm{Self}_X
+
\mathrm{Off}_X(T)
+
\mathrm{Triv}_X
+
\mathrm{Rem}_X(T),
\tag{14}
\end{equation}
with \(\mathrm{Self}_X=-\log\log X+O_{\rho_\star}(1)\) as in (10), \(M_X\) as in (7), and errors (13).

**Corollary 4.2.**  
\begin{equation}
S_X(\rho_\star)
+
\log\log X
=
M_X
+
\mathrm{Off}_X(T)
+
O_{\rho_\star}(1)
+
O\bigl(\mathrm{Rem}_X(T)\bigr).
\tag{15}
\end{equation}

---

## 5. Choosing \(T\) to kill the remainder

For fixed \(\beta>1/2\) and \(X\to\infty\), pick e.g.
\[
T=X^{1-\beta+\varepsilon}
\quad(\varepsilon>0\text{ small}).
\]
Then (13) gives \(\mathrm{Rem}_X(T)\to 0\) (or \(O(1)\)).  
Other standard choices: \(T=X/\log^2 X\), etc., depending on \(\beta\).

---

## 6. The open estimate (isolated)

**Conjecture / Target (Off-diagonal).**  
There exist \(c>0\) and a sequence \(X_n\to\infty\) with admissible \(T_n\ge\lvert\gamma_\star\rvert\) such that
\begin{equation}
\bigl\lvert M_{X_n}+\mathrm{Off}_{X_n}(T_n)\bigr\rvert
\le
(1-c)\log\log X_n.
\tag{16}
\end{equation}
Under (16) and (15),
\[
\lvert S_{X_n}(\rho_\star)\rvert
\ge
c\log\log X_n+O(1),
\]
which is Conjecture B\(_\theta\) quantitative.

### What can be said about \(M_X\) for \(\beta>1/2\)

For \(\beta>1\), \(M_X\to M_\infty\) finite.  
For \(1/2<\beta\le 1\),
\[
\int_2^X\frac{dx}{x^{\beta}\log x}
\]
grows at most like a slow iterated logarithm / truncated \(\mathrm{li}\)-type integral — **not** as fast as \(\log\log X\) when \(\beta\) is bounded away from \(1/2\)?  

Actually for \(\beta=1\), \(\int_2^X dx/(x\log x)=\log\log X\).  
For \(\beta<1\), set \(u=\log x\):
\[
\int_{\log 2}^{\log X}e^{(1-\beta)u}/u\,du
\sim
\frac{X^{1-\beta}}{(1-\beta)\log X},
\]
which **dominates** \(\log\log X\) if one only looks at size — but this is the **main term from \(\psi\sim x\)**, which is precisely cancelled in the prime number theorem story by the full zero sum when \(\rho_\star\) is **not** a zero of \(\zeta\).  

At a zero, the self-term is the piece that **breaks** the full cancellation that would make \(S_X\to\log\zeta(\rho_\star)=-\infty\) along a path.  
The correct comparison is:
\[
M_X+\sum_{\text{all }\rho\text{ including }\rho_\star}(\text{zero contributions})
\sim
\log\zeta(\rho_\star)
\quad\text{(divergent)},
\]
while partial sums stay finite.  
So \(M_X+\mathrm{Self}_X+\mathrm{Off}_X\) together encode the incomplete cancellation.

**Refined open problem:** bound \(\lvert M_X+\mathrm{Off}_X(T)\rvert\) so that it cannot cancel more than \((1-c)\log\log X\) of the self-term for a sequence of \(X\).

---

## 7. Density-conditional sketch (not completed)

Under (ZD) / KLN, zeros with \(\beta\ge\sigma_\star>1/2\) are sparse.  
Split \(\mathrm{Off}=\mathrm{Off}_{\mathrm{near}}+\mathrm{Off}_{\mathrm{far}}\).  
Far-right contributions may be estimated by (KLN) and integral bounds on \(\int_2^X x^{\beta-\beta_\star-1}/(\log x)\,dx\).  
Near-line off-diagonal terms are the main analytic difficulty (almost on the scale of Montgomery pair correlation).

**Status:** full density-conditional bound **not claimed** in this note.

---

## 8. Non-claims

1. Identity (14)–(15) is classical bookkeeping — **not** a proof of B.  
2. Target (16) is **open**.  
3. No RH.  
4. No Category B constants.  
5. \(C_{\mathrm{EF}}\) left symbolic pending a fixed published explicit version.

---

## One-liner

> \(S_X(\rho_\star)+\log\log X=M_X+\mathrm{Off}_X+O(1)+\mathrm{Rem}\); B\(_\theta\) is exactly the statement that \(M+\mathrm{Off}\) cannot cancel the whole self-term along a sequence \(X\to\infty\).
