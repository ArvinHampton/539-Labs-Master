# Target-lemma sketch · literature extracts · L5 numerical plan

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A** only — no model constants.  
**RH:** open; workstream active.  
**Primary object:** \(A_X\) from `RH_L1_Phase_Functional_CatA.md`.

---

# Part I — Target-lemma sketch  
## From Akatsuka’s \(m\log\log x\) term to \(\arg\) / \(A_X\)

### I.1 Setup

Let
\[
Y=\sup\{\operatorname{Re}\rho:\zeta(\rho)=0\}.
\]
Assume for contradiction (or for the intermediate analysis) that \(Y>1/2\). Let \(\rho=\beta+i\gamma\) with \(\beta=Y\), multiplicity \(m\ge 1\).

Write
\[
\log P_x(s)
=
\sum_{p\le x}-\log(1-p^{-s})
=
\sum_{p\le x}\sum_{k\ge 1}\frac{p^{-ks}}{k},
\]
so
\[
\log P_x(s)
=
\sum_{n\le x}\frac{\Lambda(n)}{\log n}\,n^{-s}
\quad\text{(equivalently the prime-power expansion)}.
\]
The continuous argument is
\[
\theta_x(\sigma,t)
=
\arg P_x(\sigma+it)
=
\operatorname{Im}\log P_x(\sigma+it)
\]
along the continuous branch of L1. The smoothed functional is
\[
A_X(\sigma,t)
=
\int
\theta_{e^u}(\sigma,t)\,
\phi\Bigl(\frac{u}{\log X}\Bigr)
\frac{du}{\log X}.
\]

### I.2 What Akatsuka actually supplies (corrected)

**Full line-by-line extract:** `RH_Akatsuka_Theorem_Extract.md`.

Akatsuka [Aka17] does **not** state the off-line schematic (★) as a theorem. The main quoted theorem is a **critical-line** DRH-type equivalence:

- \(\psi(x)=x+o(\sqrt{x}\log x)\)  
  \(\Leftrightarrow\)  
- renormalized limit of \((\log x)^m\zeta_x(\tfrac12+i\tau)\) exists and is nonzero  
  ( \(m=\) order of \(\zeta\) at that point),  
with RH as a consequence of the DRH-scale condition, and an explicit limit involving \(\sqrt{2}\) when \(\tau=0\).

If that limit is a nonzero constant \(C\), then on the line
\begin{equation}
\log\zeta_x\bigl(\tfrac12+i\tau\bigr)
=
-m\log\log x
+
R_{\mathrm{pole}}(x)
+
\log C
+
o(1)
\tag{★\(_\mathrm{line}\)}
\end{equation}
— so the \(m\log\log\) mechanism is a factor \((\log x)^{-m}\) in the **renormalized product on \(\mathrm{Re}=\tfrac12\)**, not an automatic off-line argument bound.

**Off-line** zero \(\Rightarrow\) product pathology is closer to [Aka17, Thm 2] (product asymptotics \(\Leftrightarrow\) zero-free half-plane, per abstract page) and to [Aka24, Prop. 7.1] (\(\Omega_+\) for real weighted prime sums when \(\Theta>\kappa\)). The **target lemma for \(A_X\) at \(Y>1/2\)** remains **open** and is not a direct quote of [Aka17].

### I.3 Real and imaginary parts

Write
\[
\log P_x(\beta+i\gamma)
=
U_x+i\theta_x(\beta,\gamma),
\]
where \(U_x=\log|P_x(\beta+i\gamma)|\) and \(\theta_x=\arg P_x\).

Then (★) splits as
\begin{align}
U_x
&=
\operatorname{Re}\bigl(m\log\log x+C_0+E\bigr)
=
m\log\log x
+
\operatorname{Re} C_0
+
\operatorname{Re} E,
\label{eq:U}
\\
\theta_x(\beta,\gamma)
&=
\operatorname{Im}\bigl(m\log\log x+C_0+E\bigr)
=
\operatorname{Im} C_0
+
\operatorname{Im} E,
\label{eq:theta-naive}
\end{align}
if one treats \(\log\log x\) as **real** (principal \(\log\log x>0\) for \(x>e\)).

**Critical observation.**  
A purely real main term \(m\log\log x\) contributes only to the **modulus** \(\lvert P_x\rvert\), not to the **argument** \(\theta_x\). Therefore:

\[
\boxed{
\text{Akatsuka’s }m\log\log x\text{ term does }\textbf{not}\text{ by itself force }
\lvert\theta_x\rvert\gg m\log\log x.
}
\]

Conjecture B and the target lemma are about \(\lvert A_X\rvert\) (argument), not about \(\lvert P_x\rvert\). The lift must use one of the following mechanisms.

### I.4 Three lift mechanisms (from modulus growth to argument)

#### Mechanism M1 — Complex phase of the Hadamard factor

Near a zero \(\rho\), the Hadamard product contributes a local factor \((s-\rho)^m\). Evaluated at \(s=\rho\) the product vanishes, but the **partial** Euler product is related to \(\zeta\) by
\[
\zeta(s)
=
P_x(s)
\cdot
R_x(s),
\]
where \(R_x\) is the reciprocal of the tail (or an approximate formula linking primes \(>x\) and zeros). Standard approximate formulae give, schematically,
\[
\log\zeta(s)
=
\log P_x(s)
+
\sum_{\rho}
E_\rho(s,x)
+
\cdots
\]
with zero contributions involving incomplete integrals of \(x^{s-\rho}/(s-\rho)\).

At \(s=\beta+i\gamma=\rho\) the full \(\zeta\) vanishes, so \(\log\zeta\) has a **logarithmic singularity** of type \(m\log(s-\rho)\). The partial product remains finite and non-zero; the singularity is carried by the remainder. Differentiating in a small imaginary or real shift \(\delta\) and then taking \(\delta\to 0\) along a path that keeps \(\operatorname{Re}s=\beta\) produces a continuous argument whose **total variation** grows like \(m\log\log x\) when the explicit formula’s zero-sum is truncated at height \(\asymp x\) (Weil explicit formula / Riemann–von Mangoldt bookkeeping).

**Sketch step:**

1. Work at \(s_x=\beta+i\gamma+i\delta_x\) or \(s_x=\beta-\varepsilon_x+i\gamma\) with \(\varepsilon_x,\delta_x\to 0\) slowly.  
2. Use \(\zeta(s_x)\sim c(s_x-\rho)^m\).  
3. Write \(\log P_x(s_x)=\log\zeta(s_x)-\log R_x(s_x)\).  
4. Choose \(x\) so that \(\log R_x\) is controlled (prime number theorem + zero-density in a box).  
5. Then \(\arg P_x(s_x)\) tracks \(\arg(s_x-\rho)^m=m\arg(s_x-\rho)\) plus controlled error.  
6. Sending \(s_x\to\rho\) after \(x\to\infty\) along a discrete sequence yields
   \[
   \lvert\theta_{x_n}(\beta,\gamma)\rvert
   \ge
   c\,m\log\log x_n
   \]
   **if** the path of approach makes \(\arg(s_x-\rho)\) wind or accumulate like \(\log\log x\) — which must be justified by the zero’s contribution in the explicit formula, not by fiat.

This is the standard “zero forces argument growth in truncated objects” idea; making it precise for **exactly** \(A_X(\beta,\gamma)\) is the open core of the target lemma.

#### Mechanism M2 — Use \(\lvert P_x\rvert\) growth + harmonic conjugate / Hilbert transform

If (★) holds with \(U_x\sim m\log\log x\), then \(\log P_x\) has large real part. On horizontal or vertical lines, the imaginary part \(\theta_x\) is essentially the **harmonic conjugate** of \(U_x\) (Cauchy–Riemann for the analytic function \(\log P_x(s)\) in \(s\), for fixed \(x\)).

For fixed \(x\), \(s\mapsto\log P_x(s)\) is holomorphic and non-vanishing in \(\operatorname{Re}s>0\). Thus \(\theta_x(\sigma,t)\) and \(U_x(\sigma,t)\) are conjugate. If \(U_x(\beta,\cdot)\) has a large mean or a large monotone trend in a \(t\)-window, conjugate-function inequalities (Privalov, Kolmogorov, etc.) give
\[
\bigl\|\theta_x(\beta,\cdot)\bigr\|_{L^p}
\gg
\bigl\|U_x(\beta,\cdot)-c\bigr\|_{L^p}
\]
on suitable intervals — but the target lemma is **pointwise** at \(t=\gamma\), not \(L^p\).

**Pointwise conjugate bounds are harder.** M2 is a viable **average** route (almost-all \(t\)) but not yet a pointwise target lemma.

#### Mechanism M3 — Extract \(\operatorname{Im}\) from complex \(m\log\log\) with complex log

If the expansion is more accurately
\[
\log P_x(\rho)
\sim
m\log\bigl(\log x\cdot e^{i\psi_x}\bigr)
=
m\log\log x
+
im\psi_x
\]
with a slowly varying phase \(\psi_x\not\equiv 0\pmod{2\pi}\), then
\[
\theta_x(\rho)\sim m\psi_x.
\]
Unless \(\lvert\psi_x\rvert\gg\log\log x\), this still fails to give the target bound. So M3 alone is insufficient unless the literature expansion produces a **large imaginary main term**.

**Conclusion for the sketch:** the viable pure-math route is **M1** (explicit formula / Hadamard remainder) with Akatsuka’s (★) controlling the **size** of the partial product so that the remainder must absorb the zero and force argument growth; M2 is secondary (average); M3 needs extra phase.

### I.5 From \(\theta_x\) to \(A_X\)

Assume a sequence \(x_n\to\infty\) with
\begin{equation}
\label{eq:theta-lower}
\bigl\lvert\theta_{x_n}(\beta,\gamma)\bigr\rvert
\ge
c_0\,m\log\log x_n.
\end{equation}
The smoother \(A_X\) averages \(\theta_{e^u}\) against \(\phi(u/\log X)/\log X\) on \(u\in[\log X,2\log X]\).

**Lemma (smoothing preserves lower bounds along a subsequence) — elementary.**  
Suppose \(\theta_x\) varies slowly on dyadic scales in the sense that for \(x\in[X,X^2]\),
\[
\bigl\lvert\theta_x-\theta_X\bigr\rvert
\le
\tfrac12 c_0\,m\log\log X
\quad\text{(or a weaker o-term)}.
\]
Then for \(X=x_n\),
\[
\bigl\lvert A_X(\beta,\gamma)\bigr\rvert
\ge
\tfrac12 c_0\,m\log\log X.
\]

**Proof idea.** \(A_X\) is a convex combination (probability measure) of values \(\theta_{e^u}\) for \(e^u\in[X,X^2]\). If all those values stay within \(c_0 m\log\log X/2\) of \(\theta_X\), the average stays large.

**Open analytic task:** prove the slow-variation (or find a subsequence where the average is still large even if \(\theta_x\) oscillates). Oscillation of \(\theta_x\) is the main enemy of the lift from (★) to \(A_X\).

### I.6 Target lemma — restated with proof obligations

**Target lemma.**  
If \(Y>1/2\) and \(\rho=\beta+i\gamma\) is a zero of multiplicity \(m\) with \(\beta=Y\), then \(\exists\,X_n\to\infty\) with
\[
\bigl\lvert A_{X_n}(\beta,\gamma)\bigr\rvert
\ge
c\,m\log\log X_n.
\]

| Obligation | Content |
|------------|---------|
| **O1** | Import precise form of Akatsuka expansion at \(s=\beta+i\gamma\) (or nearby) |
| **O2** | Pass from \(\log P_x\) / \(\zeta\)-remainder to continuous \(\theta_x\) via M1 (explicit formula) |
| **O3** | Control oscillation so smoothing to \(A_X\) preserves \(\gg m\log\log X\) |
| **O4** | No model constants; no RH as hypothesis (may use zero-density, FE, zero-free regions near \(\mathrm{Re}=1\)) |

### I.7 How RH would follow (strategy only)

1. Target lemma \(\Rightarrow\) Conjecture B at maximal-abscissa zeros.  
2. FE \(\Rightarrow\) zeros symmetric about \(\mathrm{Re}=1/2\).  
3. Classical zero-free region \(\Rightarrow\) \(Y<1\).  
4. If every configuration with \(Y>1/2\) contradicts controlled behaviour of \(A_X\) or product asymptotics on the line (Conrad–Goldfeld philosophy inverted), conclude \(Y=1/2\).

Step 4 still needs a clean global package; the **load-bearing local step** is O1–O3.

---

# Part II — Literature extracts with exact citations

### II.1 Conrad (2005) — partial Euler products on the critical line

**Citation.**  
Keith Conrad, *Partial Euler products on the critical line*, Canadian Journal of Mathematics **57** (2005), no. 2, 267–297.  
DOI: [10.4153/CJM-2005-012-8](https://doi.org/10.4153/CJM-2005-012-8) (Cambridge Core).  
Author PDF: [https://kconrad.math.uconn.edu/articles/eulerprod.pdf](https://kconrad.math.uconn.edu/articles/eulerprod.pdf).  
MathSciNet / Zbl: see Conrad’s page; widely cited (~40+).

**Content (usable).**  
- Extends Goldfeld’s theorem on partial Euler products for elliptic-curve \(L\)-functions at the centre to **typical** \(L\)-functions **along the critical line**.  
- If a partial Euler product admits an asymptotic
  \[
  \prod_{Np\le x}(\cdots)
  \sim
  \frac{C_t}{(\log x)^{r_t}}
  \]
  at a critical-line point \(1/2+it\), then (under second-moment hypotheses) one obtains **RH for that \(L\)-function** and an identification of \(C_t\) involving a \(\sqrt{2}\) factor governed by second moments (Theorem 1.1–1.2 in Conrad’s numbering for the elliptic / general cases).  
- Shows that the product asymptotic is, in a precise sense, **deeper than RH**: equivalent to a Chebyshev-function estimate \(\psi_E(x)=o(x\log x)\) vs RH \(\Leftrightarrow\psi_E(x)=O(x(\log x)^2)\) (Theorem 1.3 for elliptic curves).

**Use for our track.**  
Supports Conjecture A–type philosophy: **controlled product asymptotics on the line are strong**. We do **not** assume those asymptotics; we aim at argument growth **off** the line.

---

### II.2 Goldfeld (1982) — product asymptotics \(\Rightarrow\) RH (elliptic)

**Citation.**  
Dorian Goldfeld, *Sur les produits partiels eulériens attachés aux courbes elliptiques*, Comptes Rendus de l’Académie des Sciences, Série I **294** (1982), 471–474.  
(English exposition and generalization: Conrad [Con05] above; also cited as Goldfeld’s theorem on BSD product form \(\Rightarrow\) RH for \(L(E,s)\).)

**Content (usable).**  
If
\[
\operatorname{Prod}(E,x)\sim\frac{C}{(\log x)^r},
\]
then \(L(E,s)\) satisfies RH, \(r=\operatorname{ord}_{s=1}L(E,s)\), and \(C\) is identified with a multiple of the leading Taylor coefficient involving \(\sqrt{2}\,e^{-\gamma r/2}\) (see Conrad, Theorem 1.1).

**Use for our track.**  
Historical root of “partial Euler product asymptotics control zeros.” For \(\zeta\), analogous statements motivate why product/argument control is a legitimate RH route.

---

### II.3 Akatsuka (2017) — partial Euler product of \(\zeta\) in the strip

**Citation.**  
Hirotaka Akatsuka, *The Euler product for the Riemann zeta-function in the critical strip*, Kodai Mathematical Journal **40** (2017), no. 1, 79–101.  
DOI: [10.2996/kmj/1490083225](https://doi.org/10.2996/kmj/1490083225).  
MathSciNet: MR3626575. zbMATH: 06732079.  
Author list: [https://www.otaru-uc.ac.jp/~akatsuka/paper_en.html](https://www.otaru-uc.ac.jp/~akatsuka/paper_en.html).

**Abstract (published).**  
Pointwise asymptotic behaviour of the partial Euler product for the Riemann zeta-function on the **right half of the critical strip**; relations among partial Euler products, primes, and nontrivial zeros.

**Content (usable for target lemma).**  
- Works **pointwise** (not only in mean) for \(\zeta\)’s partial product when \(\operatorname{Re}s\) is in the right half of the strip.  
- Connects product behaviour to zero distribution — the classical place to locate an \(m\log\log x\)-type main term associated with a zero of multiplicity \(m\) at abscissa \(\sigma_0\ge Y\) issues.  
- **Primary literature input for O1** in Part I.

**Use for our track.**  
Read [Aka17] for the **exact** expansion at or near a zero of maximal real part; translate into (★) with explicit error \(E(x)\); then run M1–M3.

---

### II.4 LeClair / França–LeClair — random walks (heuristic)

**Citations.**  
- André LeClair, *Riemann Hypothesis and Random Walks: the Zeta case*, arXiv:1601.00914 (2016); related published version in *Symmetry* **13** (2021), 2014, DOI [10.3390/sym13112014](https://doi.org/10.3390/sym13112014).  
- Guilherme França and André LeClair, *On the validity of the Euler product inside the critical strip*, arXiv:1410.3520; related: *Some Riemann Hypotheses from Random Walks over Primes*, arXiv:1509.03643.

**Content (usable with caution).**  
- Models prime trigonometric sums \(\sum_p\cos(t\log p)\,p^{-\sigma}\) as random walks.  
- Heuristic: for \(\sigma>1/2\) the walk converges / product is meaningful, suggesting zeros on the critical line **if** the random-walk hypothesis is granted.  
- **Not a proof**; treat as heuristic only (MathOverflow discussions also flag trust issues for some online expositions — stick to arXiv versions carefully).

**Use for our track.**  
Motivation for Conjecture B only. **No** random-walk hypothesis inside the target lemma.

---

### II.5 Classical background (standard references)

| Topic | Standard reference |
|-------|-------------------|
| Explicit formula | Davenport, *Multiplicative Number Theory*; Ivić, *The Riemann Zeta-Function* |
| \(S(t)=\frac1\pi\arg\zeta(1/2+it)\) | Titchmarsh, *The Theory of the Riemann Zeta-Function* |
| Zero-density estimates | Montgomery; Huxley; recent surveys |
| Zero-free region near \(\mathrm{Re}=1\) | Vinogradov–Korobov |
| Hadamard product | Titchmarsh Ch. II |

---

# Part III — L5 numerical plan only

**Purpose:** diagnostic stress test of \(\theta_x\) and \(A_X\). **Cannot prove RH.**  
**No** model constants in the implementation of \(A_X\).

### III.1 Objects to compute

1. Continuous \(\theta_x(\sigma,t)=\arg P_x(\sigma+it)\) along primes (running sum of \(\Delta\arg(1-p^{-s})^{-1}\)).  
2. Smoothed \(A_X(\sigma,t)\) with fixed \(\phi\) (e.g. \(C^\infty\) bump on \([1,2]\), integral 1).  
3. Optional companion: \(U_x=\log|P_x|\) to test (★)-type modulus growth separately from argument.

### III.2 On-line battery (critical line)

| Parameter | Choice |
|-----------|--------|
| Heights \(t\) | First \(N_z\) known ordinate of zeros on \(\mathrm{Re}=1/2\) (e.g. Odlyzko tables), \(N_z\in\{10,50,100\}\) |
| \(\sigma\) | \(1/2\) |
| \(x\) or \(X\) range | \(e^{5}\) up to \(\min(e^{20}, t^{A})\) with \(A\in\{1,2\}\) as feasible |
| Record | \(\theta_x(1/2,t)\), \(A_X(1/2,t)\), \(\max\lvert A_X\rvert/\log\log X\) |

**Expectation if Conjecture A is true:** \(\lvert A_X(1/2,t)\rvert\) grows at most like \(C\log\log t\) in the tested range (finite check only).

### III.3 Off-line battery (artificial points)

| Parameter | Choice |
|-----------|--------|
| Base height | Same \(t\) as a known zero ordinate \(\gamma\) |
| \(\sigma\) | \(1/2+\delta\) and \(1/2-\delta\) for \(\delta\in\{0.01,0.05,0.1\}\) (where \(\zeta\neq 0\)) |
| Selection | Prefer points where \(\lvert\zeta(\sigma+it)\rvert\) is **small** but non-zero (local minima of \(\lvert\zeta\rvert\)) |
| Record | Same as on-line; compare growth rates of \(\lvert A_X\rvert\) vs \(\lvert A_X(1/2,t)\rvert\) |

**Expectation if Conjecture B mechanism is real:** larger growth of \(\lvert A_X\rvert\) or of \(U_x\) near small \(\lvert\zeta\rvert\) off the line — **suggestive only**.

### III.4 Maximal-abscissa proxy (cannot access true \(Y\) if \(Y=1/2\))

If RH is true, no off-line zero exists. Numerics cannot exhibit the target lemma’s hypothesis \(Y>1/2\).  
**Proxy:** study \(A_X(\sigma,t)\) as \(\sigma\downarrow 1/2\) at fixed large \(t\), or at Gram points / Lehmer pairs where \(\zeta\) is small on the line (pathology of \(S(t)\)).

### III.5 Implementation checklist

```text
[ ] primes up to x_max (segmented sieve)
[ ] complex log increment: Im Log(1/(1-p^{-s})) with continuous branch
[ ] store θ at log-grid for smoothing
[ ] φ bump; integrate A_X
[ ] mpmath/arb high precision for large t
[ ] output JSON: {sigma,t,X,theta,A,U,zeta_abs}
[ ] never claim RH from plots
```

### III.6 Pass/fail for the diagnostic (not for RH)

| Observation | Interpretation |
|-------------|----------------|
| On-line \(\lvert A_X\rvert\) stays mild | Consistent with Conjecture A (finite) |
| Off-line small-\(\lvert\zeta\rvert\) shows larger \(\lvert A_X\rvert\) or \(U_x\) | Consistent with growth mechanism (finite) |
| No difference | Inconclusive; ranges may be too small |
| Code discontinuity in \(\theta_x\) | Branch bug — fix before science |

---

# Part IV — Immediate pure-math next steps

1. **Extract from [Aka17]** the precise theorem that yields (★) or the closest expansion at a zero in the right half-strip.  
2. **Write M1 in full** with an explicit formula remainder estimate (Titchmarsh/Davenport form).  
3. **Prove the smoothing lemma** under a mild Lipschitz/slow-variation hypothesis on \(\theta_x\).  
4. **L5 code** (optional parallel diagnostic).

---

## One-liner

**Akatsuka’s \(m\log\log x\) term drives \(\lvert P_x\rvert\), not automatically \(\arg P_x\); the target lemma needs an explicit-formula lift (M1) from that modulus growth to continuous \(\theta_x\), then a smoothing step to \(A_X\) — Conrad–Goldfeld show product asymptotics are a legitimate RH-strength path; L5 only diagnoses.**

*Per aspera ad astra.*
