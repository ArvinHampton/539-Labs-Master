# ACE: Proved unrestricted mean · Open charge-preserving estimate

## Required form (lifts the No-Go only if achieved)

\[
\mathbb{E}[\chi] \le -\chi_{\min} < 0
\]

obtained **solely** from residue-class structure + topology of the 243 towers,  
**without** reference to \(539\), \(61\), or \(G_4\).

---

## 1. Unrestricted residue averages — **proved**

Leading ratios of ordinary \(T_3\):

\[
\rho_0=\tfrac13,\quad \rho_1=\tfrac43,\quad \rho_2=\tfrac23.
\]

Under uniform residue measure:

\[
\boxed{
\mathbb{E}_{\mathrm{unres}}[\chi]
= \tfrac13\bigl[\ln\tfrac13+\ln\tfrac43+\ln\tfrac23\bigr]
= \tfrac13\ln\tfrac{8}{27}
\approx -0.4054651081
< 0.
}
\]

Also:

\[
\exp\bigl(\mathbb{E}_{\mathrm{unres}}[\chi]\bigr)
= \bigl(\tfrac{8}{27}\bigr)^{1/3}
= \tfrac23.
\]

| Property | |
|----------|--|
| Strictly negative | Yes |
| Independent of \(539,61,G_4\) | Yes |
| Non-circular | Yes |
| Forces integer \(539\) | **No** |
| Selects unique \(w_j=539+61j\) | **No** |

This is a **crude a priori contraction rate** — the only rigorous a priori contraction statement that currently survives.

---

## 2. Charge preservation — \(k(n)\) distribution (**analyzed**)

Published rule: \(T=(n+1)/3+2\cdot 3^{k}\), preserve \(Q=n\bmod 9\).

| Fact | Result |
|------|--------|
| Distinct corrections mod 9 | only \(k=0,1,\ge 2\) |
| Bound | \(k\in\{0,1,2\}\) or **impossible** — **not** heavy-tailed |
| Period | depends only on \(n\bmod 27\) |
| Feasible | \(n\equiv 14,17,23\pmod{27}\) → \(k=2,0,1\) |
| \(P(\mathrm{feasible})\) | \(1/3\) |
| \(P(\mathrm{impossible})\) | \(2/3\) |
| \(\mathbb{E}[k\mid\mathrm{feas}]\) | \(1\) |
| \(\chi\) on feasible rays | \(\to\ln(1/3)<0\) |

**Revised:** difficulty is **not** arbitrarily large \(k\). It is (i) density-\(2/3\) impossible set, (ii) invariant measure of completed map, (iii) bridge to 539.

Details: `k_n_Distribution_Analysis.md` · `scripts/analyze_k_distribution.py`

---

## 3. Two ingredients — still not a full ACE

| Ingredient | Gives | Still needs |
|------------|-------|-------------|
| Markov on residues / mod 27 | transitions; \(k\) already classified | rule on impossible classes; stationary \(\pi\) |
| Democratic avg over 243 towers | initial seeds 20, 21 | not a bound on path measure of \(\chi\) |

**ACE still open**, but the open problem is **rephrased**: complete the map + compute \(\mathbb{E}_\pi[\chi]\), not control unbounded \(k\).

---

## 4. Open problems

### Open Problem A — Charge-preserving ACE

Prove, without mentioning \(539\), \(61\), or \(G_4\):

\[
\mathbb{E}[\chi_{\mathrm{cp}}] \le -\chi_{\min} < 0
\]

from Markov structure of \(T_3^{\mathrm{cp}}\) + democratic average over 243 towers (seeds 20/21).

Acceptable: closed-form \(\chi_{\min}\), or reduction to \(\frac13\ln(8/27)\) + controlled error from the law of \(k\).

### Open Problem B — Bridge

Even after ACE, need

\[
N_\star = \Psi(\chi_{\min},\, 243,\, \text{seeds }20,21)
\]

to a unique integer orbit length, still without inserting \(539\) into \(\Psi\).

**Both** steps are required before flux democracy can determine the Banach rate or a unique generational dictionary.

---

## 5. Status relative to No-Go

| Statement | Status |
|-----------|--------|
| \(\frac13\ln(8/27)<0\) unrestricted | **Proved** |
| Qualitative a priori contraction | **Proved** (too weak for 539) |
| Charge-preserving ACE | **Open** |
| Bridge \(\Psi\to N_\star\) | **Open** |
| Democracy lifts No-Go | **Blocked** until ACE + bridge |
| \(\lambda=\ln 3/539\) | **Conditional** on \(\sigma=539\) only |
| Empirical Resonant Attractor protocol | **Allowed** (estimate \(T\), do not insert 539) |

---

## 6. Bottom line (your formulation, locked)

> In the absence of the ACE the only rigorous contraction statement that survives is the qualitative observation that a uniform average over the three ordinary residue classes is already negative. That observation is a priori and non-circular, yet it is too weak to force the specific integer 539 or to select a unique set of generational windings.

Formal LaTeX: `ACE_Open_ChargePreserving.tex`  
No-Go chapter: `NoGo_FluxDemocracy_ResonantAttractor.tex` (cross-linked)
