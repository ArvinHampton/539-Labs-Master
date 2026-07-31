# Conjecture B — Precise Statement and Reduction

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Strength:** conjecture + pure reductions.  
**Does not prove RH.**

---

## 1. Definitions (from `PROGRAMME_BASELINE.md`)

\[
P_x(s)=\prod_{p\le x}(1-p^{-s})^{-1}
\quad\text{or GHK}\quad
P_X(s)=\exp\sum_{n\le X}\frac{\Lambda(n)}{n^s\log n},
\]
\[
\theta_x(s)=\arg P_x(s)
\quad\text{(continuous in the cutoff)},
\qquad
A_X(\sigma,t)=\int_1^2\theta_{X^v}(\sigma+it)\,\phi(v)\,dv,
\]
with \(\phi\ge 0\) supported on \((1,2)\), \(\int\phi=1\).

For pure statements below, **GHK \(P_X\) and \(\theta_X\)** are the primary objects (M1.2 applies directly).  
The literal Euler product differs by a controlled prime-power discrepancy on compact sets of \(s\) away from the abscissa of absolute convergence issues; that comparison is routine and omitted.

---

## 2. Conjecture B (precise forms)

### Conjecture B (unbounded form)

If \(\rho=\beta+i\gamma\) is a nontrivial zero of \(\zeta\) with \(\beta\neq 1/2\), then
\[
\limsup_{X\to\infty}\bigl\lvert A_X(\beta,\gamma)\bigr\rvert
=\infty.
\]

### Conjecture B′ (quantitative form)

There exist absolute \(c>0\) and a sequence \(X_n\to\infty\) (depending on \(\rho\)) such that
\[
\bigl\lvert A_{X_n}(\beta,\gamma)\bigr\rvert
\ge
c\log\log X_n.
\]

### Conjecture B\(_\theta\) (pre-smoothing)

Same statements with \(A_X\) replaced by \(\theta_X\).

---

## 3. Reductions (proved or conditional)

### Proposition 3.1 (O3 off-line — proved)

Let \(\beta>1/2\) be fixed and \(\gamma\in\mathbb{R}\). Then as \(X\to\infty\),
\[
\sup_{v\in[1,2]}\bigl\lvert\theta_{X^v}(\beta+i\gamma)-\theta_X(\beta+i\gamma)\bigr\rvert
\to 0.
\]
**Proof.** Bound (slow-off) in `RH_M1_3_Bis.md` §1 Mechanism γ: short Euler/GHK sum over \((X,X^2]\) is \(O_\beta(X^{1-\beta}/\log X)\to 0\). □

### Corollary 3.2 (proved)

For zeros with \(\beta>1/2\), Conjecture B \(\Leftrightarrow\) Conjecture B\(_\theta\) (unbounded forms), and B′ \(\Leftrightarrow\) B\(_\theta\) quantitative up to adjusting \(c\).

### Proposition 3.3 (phase identity — conditional on GHK + isolation)

Under GHK, Hypothesis (Iso) at scale \(1/\log X\), and \(\lvert\varepsilon_X\rvert\le 1/2\),
\[
\theta_X(s)=m\arg(s-\rho)-\operatorname{Im}\mathcal R_X^{(\mathrm{EP})}(s)+\delta_{\mathrm{br}}
\]
near \(\rho\) (Lemma 2.2 of `RH_M1_2_Line_By_Line.md`).

### Proposition 3.4 (half-turn — conditional)

If \(\sup_{\Gamma_X}R_{\mathrm{bound}}\le\varepsilon_0<m\pi/4\) on the semicircle \(\Gamma_X\) of radius \(1/\log X\) about \(\rho\), then
\[
\bigl\lvert\Delta_{\Gamma_X}\theta_X\bigr\rvert\ge\tfrac12 m\pi.
\]
**Does not imply B** (no \(X\)-growth; and classical \(R_{\mathrm{bound}}\) is too large — M1.2 bottleneck).

---

## 4. Relation to Conjecture A and RH

### Conjecture A (on-line control — schematic)

For a suitable family \(X=X(t)\), \(\lvert A_X(1/2,t)\rvert\) stays bounded or slowly growing (envelope to be fixed in L1).

### Schematic contrappositive (not a theorem)

If one had:

1. Conjecture B at every off-line zero,  
2. a comparison relating off-line \(A_X\) to on-line behaviour via the functional equation / convexity,  
3. Conjecture A preventing matching growth on the line under the same scales,

then off-line zeros would be impossible.  

**Honesty:** step (2) is **not written as a theorem** in this package. Classical convexity and the functional equation control \(\lvert\zeta\rvert\), not \(\theta_X=\arg P_X\).  
**Do not claim that B alone implies RH.**

### What B alone gives

B is a **pure statement about partial Euler phases at off-line zeros**.  
It is motivated by the failed debt argument’s metaphor, but it is **not** known to be equivalent to RH without further analytic work.

---

## 5. Known classical facts that are *not* B

| Fact | Relation to B |
|------|----------------|
| Conrad–Goldfeld on-line **modulus** asymptotics | Different object (modulus on the line) |
| Akatsuka \(m\log\log x\) on the line | Modulus, not arg; on-line |
| \(S(t)=O(\log t)\) | Arg of \(\zeta\), not of \(P_X\) |
| GHK moments of \(\lvert P_X\rvert\) | Means of modulus |
| Argument principle for \(\zeta\) near off-line zero | Arg of \(\zeta\), not \(P_X\) |

---

## 6. Attack routes (ordered by purity)

| Route | Content | Blocker |
|-------|---------|---------|
| **R1** | Improve M1.2 medium sum to \(o(1)\) + isolation ⇒ T1 half-turn for all large \(X\) | Still no \(X\)-growth (need α-bis) |
| **R2** | Lower bound \(\bigl\lvert\sum_{n\le X}\Lambda(n)n^{-\rho}/\log n\bigr\rvert\) | Dirichlet poly at a zero |
| **R3** | Resonance method at height \(\gamma\) with \(\sigma=\beta\) | Correlation with zero |
| **R4** | Mollifiers optimised for phase (O-Moll) | Open construction |
| **R5** | Assume pair correlation / GUE and derive B | Conditional; L4 circularity risk if input encodes RH |

**Recommended pure order:** finish usable M1.2 under (ZD)+gaps (R1 infrastructure) → attempt R2 with explicit formula expansion of the Dirichlet polynomial → only then R3/R4.

---

## 7. Non-claims

1. Conjecture B is **not proved**.  
2. Conjecture B is **not claimed equivalent to RH** without extra steps.  
3. No Category B constants.  
4. L5 numerics do not support or refute B at finite \(X\).

---

## 8. One-liner

**For \(\beta>1/2\), Conjecture B is equivalent to \(\lvert\theta_X(\beta,\gamma)\rvert\to\infty\); O3 is proved; the growth of \(\theta_X\) at an off-line zero is the open pure problem.**
