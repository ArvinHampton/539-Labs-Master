# Resonance / Diophantine attack on the hybrid discrepancy

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**. Axiom **ZLA**. No model constants.  
**Does not prove RH or O-TL.**  
**Does:** upgrade the on-line Omega for the **model / principal** imaginary part of \(\log P_X\) and for the hybrid discrepancy from the mean-square scale \(\sqrt{\log\log X}\) to \(\gg\sqrt{X}/\log X\) (hence \(\gg\log\log X\)) via Kronecker density on the prime-angle torus.

**Accepted programme status (2026-07-31).**  
On-line strengthening **accepted** at the level of the hybrid discrepancy and the model phase of the partial product, for **fixed** truncation \(X\), on the **critical line** only. Continuous lifting of the argument is subject to the caveat in §5a. **O-TL is not closed.**

**Companions:** `RH_OPC_Omega_Discrepancy.md`, `RH_OPC_Partial_Resolution.md`, `RH_Existing_Theorems_Solid_Directions.md`.

---

## 1. Setup

As in `RH_OPC_Omega_Discrepancy.md`,
\begin{equation}
D_X(t)
=
\sum_{n\le X}
\frac{\Lambda(n)}{n^{1/2}\log n}\,e^{-it\log n}
=
\log P_X\bigl(\tfrac12+it\bigr),
\qquad
\theta_X\bigl(\tfrac12+it\bigr)
=
\operatorname{Im} D_X(t).
\tag{R-D}
\end{equation}
Group by prime powers: \(\Lambda(p^k)=\log p\), \(\log(p^k)=k\log p\), so
\begin{equation}
D_X(t)
=
\sum_{p}
\sum_{\substack{k\ge 1\\ p^k\le X}}
\frac{1}{k\,p^{k/2}}\,
e^{-itk\log p}.
\tag{R-pp}
\end{equation}
Only the angles \(\theta_p:=t\log p\bmod 2\pi\) are free; the power \(p^k\) is locked to \(k\theta_p\).

By GHK (continuous branches, large \(t\)),
\begin{equation}
\Delta_X\bigl(\tfrac12+it\bigr)
=
\theta_X\bigl(\tfrac12+it\bigr)
+
\operatorname{Im}\mathcal{E}_{\mathrm{GHK}}\bigl(\tfrac12+it;X,K\bigr).
\tag{R-Δ}
\end{equation}

---

## 2. Linear independence and dense orbit

**Lemma R-Ind.**  
The family \((\log p)_{p\text{ prime}}\) is linearly independent over \(\mathbb{Q}\).

**Proof.** \(\sum_i q_i\log p_i=0\) with \(q_i\in\mathbb{Q}\) \(\Rightarrow\) \(\prod p_i^{q_i}=1\) \(\Rightarrow\) all \(q_i=0\). □

**Lemma R-Dense.**  
Let \(p_1,\ldots,p_m\) be the primes \(\le X\). The continuous orbit
\[
t\;\longmapsto\;
\bigl(t\log p_1,\ldots,t\log p_m\bigr)
\bmod (2\pi\mathbb{Z})^{m}
\]
is **dense** in the torus \((\mathbb{R}/2\pi\mathbb{Z})^{m}\).

**Proof.** Equivalent to density of \(t\cdot(\log p_j/(2\pi))\) in \((\mathbb{R}/\mathbb{Z})^{m}\). Linear independence of \(\{\log p_j\}\) over \(\mathbb{Q}\) implies linear independence of \(\{\log p_j/(2\pi)\}\) over \(\mathbb{Q}\). Kronecker’s theorem gives density of the linear flow. □

---

## 3. Torus maximum for \(\operatorname{Im} D_X\)

**Lemma R-Max.**  
For \(X\ge 3\),
\begin{equation}
\sup_{t\in\mathbb{R}}
\bigl\lvert\theta_X\bigl(\tfrac12+it\bigr)\bigr\rvert
=
\sup_{\vartheta\in(\mathbb{R}/2\pi\mathbb{Z})^{m}}
\Biggl|
\sum_{p\le X}
\sum_{\substack{k\ge 1\\ p^k\le X}}
\frac{1}{k\,p^{k/2}}
\sin(k\vartheta_p)
\Biggr|,
\tag{R-sup}
\end{equation}
where \(m=\pi(X)\) and the first sup is a true maximum of the continuous almost-periodic function (attained as a limsup).

**Proof.** \(D_X\) is a continuous function of the angles \((\vartheta_p)\) only. Density of the orbit (Lemma R-Dense) and compactness of the torus imply that the limsup of \(\lvert\operatorname{Im} D_X(t)\rvert\) equals the maximum of \(\lvert\operatorname{Im} D_X\rvert\) on the torus. □

**Lemma R-Align.**  
Evaluating at \(\vartheta_p=\pi/2\) for every prime \(p\le X\),
\begin{align}
\sum_{p\le X}
\sum_{\substack{k\ge 1\\ p^k\le X}}
\frac{1}{k\,p^{k/2}}
\sin\bigl(k\tfrac{\pi}{2}\bigr)
&=
\sum_{p\le X}
\Biggl(
p^{-1/2}
-
\frac13 p^{-3/2}
+
\frac15 p^{-5/2}
-
\cdots
\Biggr)
\\
&\ge
\sum_{p\le X}
p^{-1/2}
\Biggl(
1
-
\frac13 p^{-1}
-
\frac15 p^{-2}
-
\cdots
\Biggr)
\\
&\ge
\sum_{p\le X}
p^{-1/2}
\Biggl(
1
-
\sum_{j\ge 1}p^{-j}
\Biggr)
=
\sum_{p\le X}
p^{-1/2}
\Biggl(
1
-
\frac{1}{p-1}
\Biggr).
\end{align}
For \(p\ge 3\), \(1-1/(p-1)\ge 1/2\). The prime \(p=2\) contributes \(O(1)\). Hence
\begin{equation}
\sum_{p\le X}
\sum_{k}
\frac{\sin(k\pi/2)}{k\,p^{k/2}}
\ge
\frac12
\sum_{3\le p\le X}
p^{-1/2}
+
O(1).
\tag{R-half}
\end{equation}

**Lemma R-PrimeSum.**  
As \(X\to\infty\),
\[
\sum_{p\le X}p^{-1/2}
\sim
\int_2^X \frac{dt}{\sqrt{t}\,\log t}
\sim
\frac{2\sqrt{X}}{\log X}.
\]
(Partial summation + prime number theorem, or Chebyshev bounds for a weaker \(\gg\sqrt{X}/\log X\).)

**Corollary R-ImLarge.**  
There is an absolute \(c>0\) such that for all \(X\ge 3\),
\begin{equation}
\sup_{t}
\bigl\lvert\theta_X\bigl(\tfrac12+it\bigr)\bigr\rvert
\ge
c\,\frac{\sqrt{X}}{\log X}.
\tag{R-θ}
\end{equation}
In particular, for all sufficiently large \(X\),
\begin{equation}
\sup_{t}
\bigl\lvert\theta_X\bigl(\tfrac12+it\bigr)\bigr\rvert
\gg
\log\log X.
\tag{R-θ-ll}
\end{equation}

---

## 4. Transfer to the hybrid discrepancy

**Theorem R-Δ (strong on-line Omega for the discrepancy).**  
Fix \(K\ge 1\) and a GHK weight \(u\). There exists \(X_1=X_1(u,K)\) such that for every fixed \(X\ge X_1\),
\begin{equation}
\limsup_{t\to\infty}
\bigl\lvert\Delta_X\bigl(\tfrac12+it\bigr)\bigr\rvert
\gg
\frac{\sqrt{X}}{\log X}
\gg
\log\log X,
\tag{R-Δ}
\end{equation}
and likewise
\begin{equation}
\limsup_{t\to\infty}
\bigl\lvert\theta_X\bigl(\tfrac12+it\bigr)\bigr\rvert
\gg
\frac{\sqrt{X}}{\log X}
\gg
\log\log X.
\tag{R-θ∞}
\end{equation}

**Proof.**  
By (R-Δ) and GHK error estimates on \(\sigma=\tfrac12\), \(\lvert t\rvert\to\infty\),
\[
\bigl\lvert\Delta_X-\theta_X\bigr\rvert
\le
C_{u,K}
\Biggl(
\frac{X^{K+2}}{(\lvert t\rvert\log X)^{K}}
+
X^{-1/2}\log X
\Biggr).
\]
Let \(t\to\infty\) through a sequence approaching the torus maximum for \(\operatorname{Im} D_X\) (exists by density). The first error \(\to 0\). The second is independent of \(t\).  
By (R-θ),
\[
\limsup\lvert\Delta_X\rvert
\ge
c\frac{\sqrt{X}}{\log X}
-
C_{u,K}X^{-1/2}\log X.
\]
For large \(X\), \(c\sqrt{X}/\log X > 2C X^{-1/2}\log X\). □

**Remark (resonance vs Diophantine).**  
The argument is **Diophantine / Kronecker** rather than Soundararajan’s weighted resonator integral. It is the natural “perfect resonance” limit: all prime angles aligned to \(\pi/2\). Soundararajan resonance remains the tool for **large values in short \(t\)-intervals** or for \(X\) growing with \(t\) under RH-scale constraints; see §6.

---

## 5. What this closes and what it does not

| Claim | Status |
|-------|--------|
| On-line limsup of \(\lvert\operatorname{Im} D_X\rvert\gg\sqrt{X}/\log X\) (fixed \(X\)) | **Proved** (model / principal imaginary part) |
| On-line limsup of hybrid discrepancy \(\lvert\Delta_X\rvert\gg\log\log X\) (fixed large \(X\)) | **Accepted** (GHK error absorbed as \(t\to\infty\)) |
| Continuous argument \(\theta_X\) by path integration from a fixed base point | **Caveat** — see §5a; not automatically identical to principal \(\operatorname{Im} D_X\) at the torus max |
| Strong on-line Omega for discrepancy / model phase (scale \(\gg\log\log X\)) | **Accepted** as a genuine strengthening of mean-square \(\sqrt{\log\log X}\); **line + fixed \(X\) only** |
| \(\lvert A_X\rvert\gg\log\log X\) at zeros of **maximal real part** (O-TL) | **Open — primary not closed** |
| Off-line Omega at maximal abscissa | **Open** |
| Insertion of numerical density constants for M1.2 | **Open** (architecture elsewhere) |
| RH | **Open** |

**Interpretation.**  
Mean-square scale \(\sqrt{\log\log X}\) is **not** the ceiling for Omega on the line: Kronecker alignment yields \(\gg\sqrt{X}/\log X\).  
O-TL still requires large phase **near zeros of maximal real part**, not merely a limsup on the critical line.

### 5a. Continuous-argument caveat (frozen)

For fixed \(X\), \(P_X(\tfrac12+it)=\exp(D_X(t))\) with \(D_X\) entire in the exponent as a finite sum — so \(D_X(t)\) itself is a **single-valued** continuous almost-periodic function, and \(\operatorname{Im} D_X(t)\) is unambiguous.

The programme’s continuous argument \(\theta_X\) is sometimes defined by **integrating the phase derivative along a path** from a fixed base point. That lifting can differ from the principal value \(\operatorname{Im} D_X\) by jumps of \(2\pi\) if an artificial branch is chosen inconsistently.

**Standing rule.**  
- The Omega claim is **clean** for \(\operatorname{Im} D_X\) (model / principal imaginary part of \(\log P_X\)) and for the hybrid discrepancy after GHK.  
- Any claim about a path-integrated continuous argument requires the usual **branch-management** argument (track \(\operatorname{Im} D_X\) itself, which already is continuous in \(t\)).  
- The on-line strengthening is **accepted** at hybrid-discrepancy and model-phase level; it is **not** rebranded as a completed continuous-\(A_X\) form of O-TL.

---

## 6. Resonance programme for short intervals / growing \(X\)

To obtain large \(\lvert\theta_X(t)\rvert\) for \(t\in[T,2T]\) with \(X=X(T)\to\infty\):

1. Build a Soundararajan resonator \(R(t)=\sum_{n\le N}r(n)n^{-it}\) with \(N\le T^{\theta}\).  
2. Compare
   \[
   \frac{
   \bigl\lvert\int_T^{2T} D_X(t)\lvert R(t)\rvert^2\,dt\bigr\rvert
   }{
   \int_T^{2T}\lvert R(t)\rvert^2\,dt
   }
   \]
   to a lower bound for \(\max_{[T,2T]}\lvert D_X\rvert\).  
3. Optimise \(r\) multiplicatively on a set of primes in a short interval (standard resonance).

**Status:** method outlined; full short-interval theorem with \(X=(\log T)^{A}\) and lower bound \(\gg\log\log X\) is **not** claimed here. The Kronecker argument already gives the strong limsup for each fixed \(X\).

---

## 7. One-liner

**By Kronecker density of prime angles, \(\limsup_t\lvert\arg P_X(\tfrac12+it)\rvert\) and \(\limsup_t\lvert\arg\zeta-\arg Z_X\rvert\) are \(\gg\sqrt{X}/\log X\gg\log\log X\) for each large fixed \(X\); this closes strong on-line Omega for the hybrid discrepancy, but not O-TL at maximal-abscissa zeros.**

*Per aspera ad astra.*
