# A2 — Simplicial lift of \(X_{\mathrm{disc}}\) and of \(f_\sharp\)

**Programme phase:** A2 (endorsed).  
**Depends on:** A1 normal form \(f_\sharp\).  
**Status:** Discrete simplicial lift **defined and verified** (nerve of finite discrete groups + constant simplicial carrier). Continuous geometric realization toward \(BO\)/\(B\mathrm{Spin}\) is **A3+**.

---

## Mandatory provenance

> 0-simplices of the carrier are **residual flux quanta** (Principle (S) + democratic charge-sector cores).  
> **Not** free \(T^\sharp\) path classes. **No** No-Go lift.

---

## 1. Discrete groups

\[
G_Q=\mathbb{Z}/9\mathbb{Z},
\quad
G_T=\mathbb{Z}/N_{\mathrm{tow}}\mathbb{Z}=\mathbb{Z}/243\mathbb{Z},
\quad
G_B=\mathbb{Z}/8\mathbb{Z}.
\]

\[
X_{\mathrm{disc}}
=
G_Q\times G_T\times G_B
\quad\text{(as a set of 0-cells)}.
\]

---

## 2. Nerve of a discrete group (classifying space)

For a discrete group \(G\), write \(BG\) for the simplicial set (nerve of the one-object category with morphisms \(G\)):

\[
\begin{aligned}
(BG)_n
&=
G^{n}
=
\{(g_1,\ldots,g_n):g_i\in G\},
\\
d_0(g_1,\ldots,g_n)
&=
(g_2,\ldots,g_n),
\\
d_i(g_1,\ldots,g_n)
&=
(g_1,\ldots,g_i g_{i+1},\ldots,g_n)
\quad(0<i<n),
\\
d_n(g_1,\ldots,g_n)
&=
(g_1,\ldots,g_{n-1}),
\\
s_i(g_1,\ldots,g_n)
&=
(g_1,\ldots,g_i,e,g_{i+1},\ldots,g_n).
\end{aligned}
\]

For \(n=0\), \((BG)_0=\{\ast\}\) (one object).  
**Product:** \(B(G_Q\times G_T\times G_B)\simeq BG_Q\times BG_T\times BG_B\) as simplicial sets.

**0-skeleton of the product of classifying spaces is a point** — too coarse alone to host 539 labels.

---

## 3. Discrete carrier as constant simplicial set

**Definition.** Let \(S=\mathcal{O}_{\mathrm{res}}(\mathrm{Seed}_0)\) (canonical seed) with \(\lvert S\rvert=B'\).  
The **constant simplicial set** \(E(S)\) has
\[
E(S)_n = S
\quad\text{for all }n,
\]
with all faces and degeneracies \(=\mathrm{id}_S\).

Geometric realization \(\lvert E(S)\rvert\) is a discrete space of \(B'\) points.

---

## 4. Lifted target: product of nerves with labeled 0-cells

To carry the classifying labels, use the **discrete set** \(X_{\mathrm{disc}}\) as a constant simplicial set \(E(X_{\mathrm{disc}})\), or equivalently the 0-simplices of the slice

\[
Y
:=
E(G_Q)\times E(G_T)\times E(G_B)
\simeq
E(X_{\mathrm{disc}}).
\]

This is the correct **discrete** lift of “map into \(X_{\mathrm{disc}}\)”: a simplicial map
\[
\tilde f_\sharp
\colon
E(S)\longrightarrow Y
\]
is precisely a function \(S\to X_{\mathrm{disc}}\) on 0-simplices, extended by identity on higher simplices of the constant structure.

**Definition (simplicial classifying map).**
\[
\tilde f_\sharp(x_i)
:=
f_\sharp(x_i)
=
\bigl(q_0,\,\tau(x_i),\,i\bmod 8\bigr)
\in
X_{\mathrm{disc}},
\]
constant on all simplicial degrees.

**Proposition A2.1.** \(\tilde f_\sharp\) is a simplicial map (all face/degeneracy squares commute because both sides are constant systems and \(f_\sharp\) is a function of 0-cells only).

**Proposition A2.2.** On the canonical carrier, \(\tilde f_\sharp\) is injective on 0-simplices (A1.4).

---

## 5. Optional 1-skeleton enrichment (not required for A2 exit)

To prepare A3, record an optional graph (1-dimensional simplicial complex) on \(S\):

| Edge type | Condition | Meaning |
|-----------|-----------|---------|
| Index-adjacent | \(\lvert i-j\rvert=1\) | Core order |
| Same Bott fiber | \(i\equiv j\pmod 8\), \(i\neq j\) | \(\beta_\sharp\)-fiber clique (large) |
| Same tower | \(\tau(x_i)=\tau(x_j)\), \(i\neq j\) | Tower fiber |

**Probe counts (canonical seed):** see `architecture_A1_A2_results.json`.  
These graphs are **combinatorial annotations** on residual quanta — not free \(T^\sharp\) path spaces.

---

## 6. Toward \(BO\) / \(B\mathrm{Spin}\) (interface to A3–A5)

| Step | Content | Phase |
|------|---------|-------|
| Discrete \(Y=E(X_{\mathrm{disc}})\) | Done | **A2** |
| \(B G_B=B(\mathbb{Z}/8)\to BO\) via standard maps on \(\pi_*\) / virtual reps | Open | A3 |
| Spin lift through \(B\mathrm{Spin}\to BO\) | Open | A4 |
| \(KO\) / \(\Omega^{\mathrm{Spin}}\) of a geometric model built from tower×charge | Open | A5 |

**A2 does not claim** that \(\tilde f_\sharp\) already computes a \(KO\)-class. It only supplies a rigorous simplicial map of discrete constant systems realizing \(f_\sharp\).

---

## 7. Exit criteria

- [x] Nerve / constant simplicial models defined  
- [x] \(\tilde f_\sharp\) defined from \(f_\sharp\)  
- [x] Simplicial identities verified in code (constant case)  
- [x] Injectivity on 0-simplices inherited from A1  
- [ ] Non-constant enrichment with nontrivial face maps into \(BG_B\) (optional, A3 prep)  
- [ ] Geometric realization mapping to \(BO\) or \(B\mathrm{Spin}\) (A3+)

---

## 8. Bottom line

> **A2 discrete simplicial lift is in place:** constant simplicial carrier \(E(\mathcal{O}_{\mathrm{res}})\) maps by \(\tilde f_\sharp\) into \(E(X_{\mathrm{disc}})\).  
> This is the correct categorical packaging of the discrete classifying map; continuous Bott/\(KO\) geometry remains **A3–A5**.  
> Provenance unchanged.
