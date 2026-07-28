# A1 — Seed equivariance and normal form for β-fibers

**Programme phase:** A1 (endorsed).  
**Carrier:** \(\mathcal{O}_{\mathrm{res}}\) only.  
**Status:** **Closed for the normal-form theorem**; ambient β remains seed-dependent (documented).

---

## Mandatory provenance

> Objects are **residual flux quanta** under **Principle (S)** and **democratic charge-sector partition**.  
> **Not** free \(T^\sharp\) basins. **No** No-Go lift.  
> Cite: `Object539_NonCircular_Construction.md`, `Architecture_A_Ores_Programme.md` §0.

---

## 0. Problem

For a seed \(\mathrm{Seed}\subset\Omega\) with \(\lvert\mathrm{Seed}\rvert=f_{\max}\), write \(\mathcal{O}_{\mathrm{res}}(\mathrm{Seed})\) for the \(q=0\) guaranteed core after equitable residual partition.

**Ambient Bott degree** \(\beta(x)=x\bmod 8\) yields fiber sizes that **vary** with \(\mathrm{Seed}\) (probe: minima from 61 to 67 in 100 trials).  
The tidy canonical-seed table (67/68 split with min 67) is **not** seed-invariant.

**Goal.** A seed-independent normal form of the Bott clock on the carrier, plus equivariance/injectivity statements for the discrete classifying map.

---

## 1. Canonical ordering of a core

**Definition.** For any seed, let
\[
\mathcal{O}_{\mathrm{res}}(\mathrm{Seed})
=
\{x_0<x_1<\cdots<x_{B'-1}\}
\]
be the sorted core (\(B'=\lfloor(N_{\mathrm{flux}}-f_{\max})/9\rfloor\)).

The **core index** of \(x_i\) is \(i\in\{0,\ldots,B'-1\}\).

---

## 2. Index normal form \(\beta_\sharp\)

**Definition (normal Bott degree).**
\[
\beta_\sharp(x_i)
:=
i \bmod 8
\in
\mathbb{Z}/8.
\]

**Theorem A1.1 (Seed-independent fibers).**  
For every seed of size \(f_{\max}\), the fibers
\[
F_k^\sharp
=
\{x_i\in\mathcal{O}_{\mathrm{res}}(\mathrm{Seed}):\beta_\sharp(x_i)=k\}
\]
satisfy
\[
\lvert F_k^\sharp\rvert
=
\begin{cases}
68 & k\in\{0,1,2\},\\
67 & k\in\{3,4,5,6,7\},
\end{cases}
\]
equivalently
\[
\bigl(\lvert F_0^\sharp\rvert,\ldots,\lvert F_7^\sharp\rvert\bigr)
=
(68,68,68,67,67,67,67,67).
\]
In particular \(\min_k\lvert F_k^\sharp\rvert=\lfloor B'/8\rfloor=67\) and
\[
B'=8\cdot 67+3
\]
is realized as three excess slots on degrees \(\{0,1,2\}\).

**Proof.**  
\(\lvert\mathcal{O}_{\mathrm{res}}(\mathrm{Seed})\rvert=B'\) for every seed (equitable residual partition).  
Among indices \(\{0,\ldots,B'-1\}\) with \(B'=8\cdot 67+3\), the residue \(k\bmod 8\) occurs \(68\) times for \(k=0,1,2\) and \(67\) times for \(k=3,\ldots,7\).  
This depends only on \(B'\), not on the labels \(x_i\) or the seed. ∎

**Verification:** 100 random seeds → unique fiber table \((68,68,68,67,67,67,67,67)\) (`scripts/architecture_A1_A2_probe.py`).

---

## 3. Ambient β (not normal)

**Proposition A1.2.**  
Ambient fibers of \(\beta(x)=x\bmod 8\) are **not** seed-invariant.  
In a 100-seed sample, \(\min_k\lvert F_k^{\mathrm{amb}}\rvert\) ranged in \(\{61,\ldots,67\}\).

**Proposition A1.3.**  
There is no pair \((a,b)\) with \(a\) odd (unit in \(\mathbb{Z}/8\)) such that
\[
x\mapsto (ax+b)\bmod 8
\]
reproduces the index fiber table for all tested seeds (0/30 seeds admitted any such affine match in sample).  
Thus ambient β is not related to \(\beta_\sharp\) by a **seed-independent** affine reparametrization on labels.

**Use of ambient β:** optional diagnostic; **not** the Bott clock of the programme after A1.

---

## 4. Normal classifying map

**Definition.**
\[
f_\sharp(x_i)
:=
\bigl(q,\;\tau(x_i),\;\beta_\sharp(x_i)\bigr)
=
\bigl(q,\;\tau(x_i),\;i\bmod 8\bigr)
\in
X_{\mathrm{disc}}.
\]

**Theorem A1.4 (Injectivity, sampled + canonical).**  
On the canonical seed and on 100 random seeds of size \(f_{\max}\),
\[
\bigl(\tau(x_i),\,i\bmod 8\bigr)
\]
is injective on the \(q=0\) core (100/100 and canonical).  
The same holds for ambient pairs \((\tau(x),x\bmod 8)\) in those trials — injectivity is robust; **fiber normality** is what requires \(\beta_\sharp\).

**Remark (tower multiset).**  
The multiset \(\{\tau(x):x\in\mathcal{O}_{\mathrm{res}}(\mathrm{Seed})\}\) **does** depend on the seed (50/50 distinct types in sample).  
So \(f_\sharp\) is not seed-invariant as a map of labeled sets, but:
- cardinality of the carrier is invariant;
- \(\beta_\sharp\)-fiber profile is invariant;
- injectivity of \(f_\sharp\) held in all tested seeds.

**Equivariance in the weak sense used here:**  
invariants of the Bott grading are unchanged under seed change once \(\beta_\sharp\) is adopted; strong equivariance (a natural isomorphism relating \(f_\sharp\) for different seeds via a seed-category) is **not** claimed.

---

## 5. Locked choice after A1

| Object | After A1 |
|--------|----------|
| Bott degree on carrier | \(\beta_\sharp(x_i)=i\bmod 8\) (**normal form**) |
| Fiber theorem | A1.1 — seed-independent |
| Classifying map | \(f_\sharp=(q,\tau,\beta_\sharp)\) |
| Ambient \(x\bmod 8\) | Deprecated for fiber claims |
| Free \(T^\sharp\) | Still Option 3; not used |

---

## 6. Bottom line

> **A1 complete:** the β-fiber variation under random seeds is resolved by passing to the **core-index Bott clock** \(\beta_\sharp\).  
> Fibers are always \((68^3,67^5)\) and realize \(B'=8\cdot 67+3\) without seed dependence.  
> Provenance unchanged: residual flux quanta under (S) + democratic partition.
