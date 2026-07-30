# A5 — \(KO\) / \(\Omega^{\mathrm{Spin}}\) on \(\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}}\) (0-stem)

**Programme phase:** A5 (**0-stem residual closure**).  
**Depends on:** A0–A4 (0-stem).  
**Domain (mandatory):** \(\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}}\) only — residual **0-dimensional** spin / real \(K\)-theory.  
**Status:** **Closed** as 0-stem residual closure — **not** higher continuum \(\Omega_{n>0}\).  
**Status code:** `A5_KO_OMEGA0_SPIN_CLOSED_ON_O_RES`  
**Probe:** `scripts/architecture_A4_A5_probe.py` → `architecture_A4_A5_results.json`.

---

## Mandatory provenance

> Objects counted in \(KO_0\) / \(\Omega_0^{\mathrm{Spin}}\) are **residual flux quanta** under Principle **(S)**.  
> Cardinality \(B'=\lfloor(N_{\mathrm{flux}}-f_{\max})/9\rfloor\) is **derived** (no 539 on the RHS).  
> **Not** free \(T^\sharp\) basins. **No** No-Go lift. Option 3 intact.  
> **Domain:** \(\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}}\) / 0-stem only — do **not** promote to continuum \(\Omega_{n>0}\).

---

## 0. Goal

Compute honest residual invariants in
\[
\Omega_0^{\mathrm{Spin}}
\cong
\mathbb{Z},
\qquad
KO_0(\mathrm{pt})
\cong
\mathbb{Z},
\]
linked by the Atiyah–Bott–Shapiro map, and relate them to the A1 Bott fiber table
\[
B'=8\cdot 67+3
\]
without treating 539 as an input hypothesis.

Higher-dimensional continuum spin bordism of fillings remains **Category B** / open.

---

## 1. Classical groups (0-stem)

\[
\begin{aligned}
\Omega_0^{\mathrm{Spin}}
&\cong
\mathbb{Z}
&&\text{(signed points; spin structure unique on \(\mathrm{pt}\))},
\\
KO_0(\mathrm{pt})
&\cong
\mathbb{Z}
&&\text{(virtual rank)},
\\
\mathrm{ABS}
&\colon
\Omega_0^{\mathrm{Spin}}
\xrightarrow{\;\sim\;}
KO_0(\mathrm{pt}).
\end{aligned}
\]

Bott period-8 table for \(KO^{-k}(\mathrm{pt})\) (labels):

| \(k\bmod 8\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|--------------|---|---|---|---|---|---|---|---|
| \(KO^{-k}(\mathrm{pt})\) | \(\mathbb{Z}\) | \(\mathbb{Z}/2\) | \(\mathbb{Z}/2\) | 0 | \(\mathbb{Z}\) | 0 | 0 | 0 |

---

## 2. Residual 0-class

**Definition.**  
Orient each residual quantum positively. The residual carrier as a closed 0-manifold with (unique) spin structures is
\[
\bigl[\mathcal{O}_{\mathrm{res}}\bigr]
\;\in\;
\Omega_0^{\mathrm{Spin}}
\cong
\mathbb{Z},
\qquad
\bigl[\mathcal{O}_{\mathrm{res}}\bigr]
=
B'
=
\Bigl\lfloor\frac{N_{\mathrm{flux}}-f_{\max}}{9}\Bigr\rfloor.
\]

**Theorem A5.1.**  
\[
\mathrm{ABS}\bigl([\mathcal{O}_{\mathrm{res}}]\bigr)
=
B'
\in
KO_0(\mathrm{pt})
\cong
\mathbb{Z}.
\]

**Proof.**  
ABS is an isomorphism on the 0-stem; the class is \(B'\) positively oriented points.  
\(B'\) is packaging arithmetic under (S), not a free-dynamics count. ∎

**Pushforward reading (A3 geometry).**  
Each \(x\in\mathcal{O}_{\mathrm{res}}\) contributes \([\mathrm{pt}_x]\);  
\[
\sum_{x\in\mathcal{O}_{\mathrm{res}}}
[\mathrm{pt}_x]
=
B'
\]
in both \(\Omega_0^{\mathrm{Spin}}\) and \(KO_0(\mathrm{pt})\).

---

## 3. Bott fiber refinement (A1 structure)

A1 gives
\[
\bigl\lvert\beta_\sharp^{-1}(k)\bigr\rvert
\in
\{68,68,68,67,67,67,67,67\}
\quad(k=0,\ldots,7),
\]
and
\[
B'
=
\sum_{k=0}^{7}
\bigl\lvert\beta_\sharp^{-1}(k)\bigr\rvert
=
8\cdot 67+3.
\]

**Definition (discrete \(KO\)-proxy multiset).**  
Assign fiber size \(\lvert\beta_\sharp^{-1}(k)\rvert\) as the count of residual quanta in Bott clock slot \(k\).  
This is a **grading of the same 0-class**, not a computation of \(\pi_k(O)\) from continuum geometry.

**Theorem A5.2 (compatibility).**  
The A1 fiber table is compatible with the residual 0-class:
\[
\sum_k
\lvert\beta_\sharp^{-1}(k)\rvert
=
B'
=
\mathrm{ABS}([\mathcal{O}_{\mathrm{res}}]),
\]
and the period-8 arithmetic \(B'=8\cdot 67+3\) holds with \(B'\) **derived**.

---

## 4. Relation to \(\Phi\) / \(\widetilde\Phi\)

| Object | A5 reading |
|--------|------------|
| \(\Phi,\widetilde\Phi\) | Geometric labels of residual points in \(BO\)/\(B\mathrm{Spin}\) (A3–A4) |
| \([\mathcal{O}_{\mathrm{res}}]\) | Bordism/\(KO\) count of those points |
| Fiber table | Bott clock decomposition of the same set |

No continuum index theorem is required for the 0-stem residual lock.

---

## 5. What A5 does *not* claim

| Non-claim | |
|-----------|--|
| \(\Omega_n^{\mathrm{Spin}}\) for \(n>0\) of a residual continuum filling | **B / open** |
| Free \(T^\sharp\) 539 classes in \(KO\) | **O** (Option 3) |
| Security hardness from \(KO_0\cong\mathbb{Z}\) | **O** |
| Identification of \(G_4=539.9\,\mathrm{s}\) with a \(KO\)-period | **O** |
| No-Go lift via Bott | **O** |

---

## 6. Status

| Item | Tag |
|------|-----|
| \([\mathcal{O}_{\mathrm{res}}]=B'\) in \(\Omega_0^{\mathrm{Spin}}\) | **A** (0-bordism = cardinality of spin points) |
| \(\mathrm{ABS}\to KO_0=B'\) | **A** |
| Fiber table / \(8\cdot67+3\) compatibility | **A** (A1 grading, not free \(\mathbb{Z}/8\) action) |
| Higher \(\Omega_{n>0}\) continuum fillings | **B** — correctly not claimed |
| Promote 0-stem to continuum bordism | **O** (forbidden) |
| Status code | **`A5_KO_OMEGA0_SPIN_CLOSED_ON_O_RES`** |
| Domain line (freeze) | \(\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}}\) / 0-stem only |

---

## One-line

**A5 closes residual 0-stem spin/\(KO\): \(B'\) positive residual points in \(\Omega_0^{\mathrm{Spin}}\cong\mathbb{Z}\), ABS to \(KO_0=B'\), Bott-refined by A1 fibers \(8\cdot67+3\) — domain \(\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}}\) only; not continuum \(\Omega_{n>0}\), not free \(T^\sharp\).**

*Per aspera ad astra.*
