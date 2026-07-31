# O1 — Exact Akatsuka expansion package + M1 remainder

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A** only — no model constants.  
**Role:** analytic **O1** from the target-lemma sketch: pin what [Aka17] gives exactly, and how it plugs into the named M1 remainder \(\mathcal{R}_x^{\mathrm{EP}}\).

**Companions:**  
`RH_Akatsuka_Theorem_Extract.md`, `RH_M1_Explicit_Formula_Remainder.md`, `RH_L1_Phase_Functional_CatA.md`.

---

## 0. What O1 is

| Deliverable | Content |
|-------------|---------|
| **O1a** | Exact critical-line expansion from Akatsuka (renormalized \(\zeta_x\)) |
| **O1b** | Exact identification of Akatsuka’s pole renormalizer with a piece of M1 |
| **O1c** | Exact structural identity for \(\log P_x\) near a zero via M1 |
| **O1d** | Open bounds still required for the target lemma (not claimed here) |

O1 does **not** prove the target lemma. It freezes the **correct expansion** so later M1.2–M1.4 bounds have a single target.

---

## 1. Notation (aligned with L1 / M1)

\[
\zeta_x(s)=P_x(s)=\prod_{p\le x}(1-p^{-s})^{-1},
\qquad
\log P_x(s)=\sum_{p\le x}\sum_{k\ge 1}\frac{p^{-ks}}{k}.
\]
\[
L_x^{\Lambda}(s)=\sum_{n\le x}\frac{\Lambda(n)}{n^{s}\log n},
\qquad
E_x^{\mathrm{pow}}(s)=\log P_x(s)-L_x^{\Lambda}(s).
\]
Nontrivial zeros \(\rho\); pole at \(s=1\).

**M1-EP identity** (`RH_M1_Explicit_Formula_Remainder.md`):
\begin{equation}
\log\zeta(s)
=
\log P_x(s)
+
\mathcal{R}_x^{\mathrm{EP}}(s),
\tag{M1-EP}
\end{equation}
where \(\mathcal{R}_x^{\mathrm{EP}}\) is built from the **Ingham–von Mangoldt** kernel \(R_{\mathrm{IvM}}(s;x,T)\).

---

## 2. O1a — Exact Akatsuka critical-line package

### 2.1 Theorem ([Aka17], as quoted in KKK/KK)

Define \(\zeta_x(s)\) as above. The following are equivalent:

**(Aκ-1)** \(\displaystyle\psi(x)=x+o\bigl(\sqrt{x}\log x\bigr)\) as \(x\to\infty\).

**(Aκ-2)** There exists \(\tau\in\mathbb{R}\) such that, with \(s_0=\tfrac12+i\tau\) and \(m=\mathrm{ord}_{s=s_0}\zeta(s)\),
\begin{equation}
\lim_{x\to\infty}
\frac
{(\log x)^{m}\,\zeta_x(s_0)}
{\displaystyle
\exp\!\Biggl(
\lim_{\varepsilon\downarrow 0}
\Biggl(
\int_{1+\varepsilon}^{x}
\frac{du}{u^{s_0}\log u}
-
\log\frac{1}{\varepsilon}
\Biggr)
\Biggr)
}
\tag{Aκ-lim}
\end{equation}
exists and is a **nonzero** complex number.

**(Aκ-3)** The same limit exists and is nonzero for **every** \(\tau\in\mathbb{R}\).

**Consequence (Aκ-C):** if (Aκ-1)–(Aκ-3) hold, then RH holds, and the limit equals
\[
\frac{(s_0-1)\,\zeta^{(m)}(s_0)}{e^{(m-1)\gamma}\,m!}
\times
\begin{cases}
\sqrt{2} & \tau=0,\\
1 & \tau\neq 0,
\end{cases}
\]
(\(\gamma=\) Euler–Mascheroni; form as in Kaneko–Koyama–Kurokawa, arXiv:2206.02612, Thm 3.2).

**Citations.**  
Akatsuka, Kodai Math. J. **40** (2017), 79–101, DOI 10.2996/kmj/1490083225;  
restated: arXiv:2206.02612v3 Thm 3.2; arXiv:2203.12791 §1.

### 2.2 Exact expansion when the limit exists

Assume (Aκ-2) at \(s_0=\tfrac12+i\tau\) with limit \(C\neq 0\). Then, as \(x\to\infty\),
\begin{equation}
\boxed{
\zeta_x(s_0)
=
C\cdot
\frac
{e^{R_{\mathrm{pole}}(x;s_0)}}
{(\log x)^{m}}
\cdot\bigl(1+o(1)\bigr)
}
\tag{O1-A}
\end{equation}
where the **pole renormalizer** is the continuous determination of
\begin{equation}
R_{\mathrm{pole}}(x;s_0)
:=
\lim_{\varepsilon\downarrow 0}
\Biggl(
\int_{1+\varepsilon}^{x}
\frac{du}{u^{s_0}\log u}
-
\log\frac{1}{\varepsilon}
\Biggr).
\tag{O1-pole}
\end{equation}

Taking the continuous logarithm along \(x\uparrow\infty\) (principal branch of the limit, then continuous in \(x\)),
\begin{equation}
\boxed{
\log\zeta_x(s_0)
=
-m\log\log x
+
R_{\mathrm{pole}}(x;s_0)
+
\log C
+
o(1)
}
\tag{O1-A-log}
\end{equation}

**This is the exact \(m\log\log\) mechanism in [Aka17]:** a factor \((\log x)^{-m}\) in the **renormalized critical-line** product — **not** an off-line argument bound.

### 2.3 Companion product \(E_2\) ([Aka17, Cor. 4.4] via Aka24 Rem. 1.1)

\[
E_2(X)
=
\frac{\zeta_X(1/2)}{\exp\bigl(\mathrm{li}(X^{1/2})\bigr)}.
\]
Then \(E_2(X)\to -\sqrt{2}\,\zeta(1/2)\) is equivalent to \(\psi(X)=X+o(\sqrt{X}\log X)\).

---

## 3. O1b — Pole renormalizer inside M1

### 3.1 Archimedean / pole term in (IvM)

The truncated formula contains the summand
\[
\frac{x^{1-s}}{1-s}
\]
and, after path integration from a base \(s_\star\) with \(\operatorname{Re}s_\star>1\), a contribution
\[
\int_{\Gamma}\frac{x^{1-w}}{1-w}\,dw
\]
inside \(\mathcal{R}_{x,T}^{\mathrm{IvM}}\) (`RH_M1_Explicit_Formula_Remainder.md` (M1-rem)).

### 3.2 Identification (structural)

The integral defining \(R_{\mathrm{pole}}(x;s_0)\) is the logarithmic integral of \(u^{-s_0}\) against \(du/\log u\), i.e. the **Dirichlet density** of the prime contribution at the pole of \(\zeta\) as seen from the Mellin side.

**O1b claim (structural, not a new theorem):**  
On the critical line, Akatsuka’s factor \(\exp(R_{\mathrm{pole}}(x;s_0))\) is the **closed-form packaging** of the same pole/archimedean compensation that appears when one writes
\[
\log\zeta_x(s_0)
=
\log\zeta(s_0)
-
\mathcal{R}_x^{\mathrm{EP}}(s_0)
\]
and isolates the contribution of the pole \(s=1\) in \(\mathcal{R}_x^{\mathrm{EP}}\) (via \(\int x^{1-w}/(1-w)\,dw\) and the base-point normalization).  

At a **zero** \(s_0\) of \(\zeta\), \(\log\zeta(s_0)\) is singular, so one must approach along a path \(s\to s_0\) as in M1 §4; Akatsuka’s formulation avoids the singularity by multiplying by \((\log x)^{m}\) and renormalizing **before** taking the limit of the partial product alone.

**Dictionary:**

| Akatsuka | M1 |
|----------|-----|
| \(\zeta_x=P_x\) | \(\log P_x\) |
| \((\log x)^{m}\) | compensates \(m\log(s-s_0)\) as \(s\to s_0\) |
| \(e^{R_{\mathrm{pole}}}\) | pole piece of \(\mathcal{R}_{x,T}^{\mathrm{IvM}}\) / archimedean integral |
| limit \(C\neq 0\) | \(\mathcal{R}_x^{\mathrm{EP}}+m\log(s-s_0)-R_{\mathrm{pole}}\) stays controlled |

---

## 4. O1c — M1 structure at a general zero (on or off line)

Let \(\rho_0=\beta+i\gamma\) be a zero of multiplicity \(m\ge 1\). From M1:
\begin{equation}
\log P_x(s)
=
m\log(s-\rho_0)
+
H_{\rho_0}(s)
-
\mathcal{R}_x^{\mathrm{EP}}(s),
\tag{O1-M1}
\end{equation}
with \(H_{\rho_0}\) holomorphic and non-vanishing at \(\rho_0\), and
\begin{equation}
\mathcal{R}_x^{\mathrm{EP}}(s)
=
\mathcal{R}_{x,T}^{\mathrm{IvM}}(s)
-
E_x^{\mathrm{pow}}(s)
+
O(x^{-\sigma}),
\end{equation}
\begin{equation}
\frac{\zeta'}{\zeta}(s)
=
-
\sum_{n<x}\frac{\Lambda(n)}{n^{s}}
+
\frac{x^{1-s}}{1-s}
-
\sum_{\lvert\Im\rho\rvert\le T}
\frac{x^{\rho-s}}{\rho-s}
+
R_{\mathrm{IvM}}(s;x,T).
\tag{IvM}
\end{equation}

**Argument form:**
\begin{equation}
\theta_x(s)
=
m\arg(s-\rho_0)
+
\operatorname{Im} H_{\rho_0}(s)
-
\operatorname{Im}\mathcal{R}_x^{\mathrm{EP}}(s).
\tag{O1-arg}
\end{equation}

**On the critical line**, if Akatsuka’s limit exists, (O1-A-log) is the special case of controlling
\[
\log P_x(s_0)
=
\log\zeta_x(s_0)
\]
after renormalization — consistent with (O1-M1) taken along a path \(s\to s_0=\rho_0\).

**Off the line** (\(\beta>1/2\)), there is **no** Akatsuka theorem of the form (O1-A). The working expansion remains (O1-M1)/(O1-arg) with bounds on \(\operatorname{Im}\mathcal{R}_x^{\mathrm{EP}}\) still to prove (M1.2).

---

## 5. O1d — What is closed vs open

| Item | Status |
|------|--------|
| Exact (Aκ-1)–(Aκ-3) and (O1-A), (O1-A-log) | **Closed as literature package** |
| Name \(R_{\mathrm{pole}}\), link to M1 pole integral | **Closed structurally (O1b)** |
| Identity (O1-M1), (O1-arg) | **Closed (M1)** |
| Bound \(\lvert\operatorname{Im}\mathcal{R}_x^{\mathrm{EP}}\rvert\) near off-line zeros | **Open (M1.2)** |
| Path with \(\lvert m\arg(s-\rho_0)\rvert\gg m\log\log x\) | **Open (M1.3)** |
| Smoothing to \(A_X\) | **Open (M1.4)** |
| Target lemma | **Open** |
| RH | **Open** |

---

## 6. Precise next analytic lemmas (after O1)

### Lemma O1.1 (on-line, conditional on Akatsuka limit)

Assume (Aκ-2) at \(s_0=\tfrac12+i\tau\) with limit \(C\neq 0\). Then
\[
\log P_x(s_0)
=
-m\log\log x
+
R_{\mathrm{pole}}(x;s_0)
+
\log C
+
o(1)
\quad(x\to\infty).
\]
In particular
\[
\operatorname{Re}\log P_x(s_0)
=
-m\log\log x
+
\operatorname{Re} R_{\mathrm{pole}}(x;s_0)
+
\operatorname{Re}\log C
+
o(1),
\]
and
\[
\theta_x(s_0)
=
\operatorname{Im} R_{\mathrm{pole}}(x;s_0)
+
\operatorname{Im}\log C
+
o(1).
\]

**Note:** on the line under Akatsuka’s limit, \(\theta_x(s_0)\) stays **bounded + slowly varying Im pole term**, not \(\gg m\log\log x\). The \(m\log\log\) mass is in the **modulus**. This matches the earlier warning that real \(m\log\log\) does not automatically give argument growth.

### Lemma O1.2 (off-line — open)

If \(\rho_0=\beta+i\gamma\) has \(\beta=Y>1/2\) and order \(m\), prove existence of \(x_n\to\infty\) and paths \(s_n\to\rho_0\) with
\[
\bigl\lvert\operatorname{Im}\mathcal{R}_{x_n}^{\mathrm{EP}}(s_n)\bigr\rvert
\le
\tfrac14 c\,m\log\log x_n
\quad\text{and}\quad
\bigl\lvert m\arg(s_n-\rho_0)\bigr\rvert
\ge
c\,m\log\log x_n.
\]

### Lemma O1.3 (smoothing — open)

Under slow variation of \(\theta_x\) on \([X,X^2]\), pass O1.2 to \(\lvert A_X(\beta,\gamma)\rvert\ge \tfrac12 c\,m\log\log X\).

---

## 7. Firewall

No \(G_4\), \(\mu\), \(E_{\mathrm{leak}}\), 539.9. Resonant Algebra and residual Architecture A are unrelated as RH lemmas.

---

## One-liner

**O1 freezes the exact Akatsuka critical-line expansion \(\zeta_x(s_0)=C\,e^{R_{\mathrm{pole}}}/(\log x)^{m}\) and the M1 split \(\log\zeta=\log P_x+\mathcal{R}_x^{\mathrm{EP}}\) with named \(R_{\mathrm{IvM}}\); on the line the \(m\log\log\) mass sits in the modulus, so off-line argument growth for the target lemma still needs M1.2–M1.4.**

*Per aspera ad astra.*
