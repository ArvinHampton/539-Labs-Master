# Density vs isolation · Maynard–Pratt · Levinson–Ivić

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**. Axiom **ZLA**.  
**No claim** that (Iso_H), Hypothesis F, Mass-with-A, B_θ, or RH is proved.

**Companions:**  
`RH_Iso_H_Classical_Constraints.md`,  
`RH_Finite_Product_Ivic_MassA.md`,  
`RH_ND1_Stability_Resolve.md`,  
`RH_M1_2_Effective_Density.md`.

---

## 0. Purpose

Clarify how **bulk density** and **local isolation** relate to Lip \(A\), Mass-with-A, and (Iso_H). Record Maynard–Pratt half-isolation and Levinson–Ivić horizontal isolation as classical geometry — **different objects** from (Iso_H).

---

## 1. Maynard–Pratt half-isolated zeros

### Definition

A zero \(\rho_0=\beta_0+i\gamma_0\) is **\(Y\)-half-isolated** if every nearby zero (within \((\log\lvert\gamma_0\rvert)^2\)) either

- has real part almost equal to \(\beta_0\) and lies **above** \(\rho_0\), or  
- has real part **substantially smaller** than \(\beta_0\).

It is half-isolated for a suitable range of \(Y\). Roughly: **no nearby zeros below or to the right**.

### Unconditional

There are few half-isolated zeros; those with \(\beta\ge\sigma\) and \(\gamma\in[T,2T]\) number
\[
\ll T^{2(1-\sigma)+o(1)}.
\]

### Conditional

Under **Hypothesis F** (all non-trivial zeros lie on finitely many fixed vertical lines), Maynard–Pratt improve Ingham–Huxley to essentially density-hypothesis strength:
\begin{equation}
N(\sigma,T)
\ll
T^{2(1-\sigma)}
\exp\bigl((\log\log T)^{O(1)}\bigr).
\tag{MP-F}
\end{equation}
Consequences for primes in short intervals follow under the same assumption.

### Logical direction

\[
\text{Hypothesis F}
\quad\Longrightarrow\quad
\text{better density}.
\]
That is the **converse** of what (Iso_H) needs. They do **not** prove finitely many vertical lines or (Iso_H).

**Standing:** classical / literature — **recorded**. No (Iso_H) claim.

---

## 2. Levinson–Ivić horizontal isolation

If zeros with \(\beta>1-\delta\) are isolated in short **horizontal** rectangles of height \(2\delta\) near \(\sigma=1\), the zero-free region improves to
\begin{equation}
\sigma
>
1
-
\frac{C}{\log\log t}.
\tag{Lev-ZF}
\end{equation}

**Ivić Theorem 4:** under the same isolation, large multiplicity forces the zero even further left.

### What this is / is not

| This is | This is not |
|---------|-------------|
| **Horizontal** isolation near the far-right edge of the strip | Isolation on a fixed **vertical** line at arbitrary \(\beta_\star\in(1/2,1)\) |
| A tool for zero-free regions near \(\sigma=1\) | **(Iso_H)** |

**Standing:** classical — **recorded**. Not a substitute for (Iso_H).

---

## 3. Density vs isolation

| | **Density** | **Isolation** |
|---|-------------|----------------|
| **Object** | Bulk count \(N(\sigma,T)\), \(N_{\mathrm{vert}}\), \(N_{\mathrm{line}}\) | Local geometry (gaps, one-sided neighbourhoods, uniqueness) |
| **Answers** | How many zeros in a region up to height \(T\) | How those zeros are arranged relative to each other |
| **Feeds \(A\)** | Yes: \(M(T)\Rightarrow A\ll M\log T\) | Only if isolation is strong enough to force \(M\) small (e.g. Iso_H) |
| **Examples** | Ingham, Huxley, KLN, Bellotti | Point isolation; Levinson horizontal near \(\sigma=1\); Maynard–Pratt half-isolation; (Iso_H) |

### Programme consequence

**Mass-with-A** needs either:

- a **density-type** polylog bound on competitors near \(\beta_\star\), or  
- the stronger isolation **(Iso_H)**.

Half-isolation and Levinson isolation are **different geometric objects**; neither is (Iso_H), and neither currently supplies polylog \(M\) for arbitrary \(\beta_\star>1/2\).

---

## 4. Barrier restated

```text
(RM)
  ├── classical density (strong near σ=1, weak near 1/2)
  ├── Iso_H → A = O(1) → Mass-with-A → B_θ
  ├── Levinson horizontal isolation → better zero-free region (not Iso_H)
  └── Maynard–Pratt half-isolation / Hypothesis F → better density
        (converse direction; does not prove Iso_H)
```

---

## 5. Solid directions (frozen)

| Rank | Direction |
|------|-----------|
| **1** | **Effective density at moderate \(\sigma\)** |
| **2** | **(Iso_H) technology** |
| **3** | **Path continuation from on-line Ω** |
| **4** | **Resonance off the line** |
| **5** | **Mass-with-A under (RM)** |

Density vs isolation distinction in §3 is **locked**.  
**No claim** that (Iso_H), Hypothesis F, or B_θ is proved.

---

## 6. Status

| Item | Status |
|------|--------|
| Density vs isolation distinction | **Frozen** (this note) |
| Maynard–Pratt / Levinson–Ivić role | **Recorded** — not Iso_H |
| Polylog \(A\) / Mass-with-A as theorems | **Open** |
| Unconditional (Iso_H) / B_θ / O-TL | **Open — primary not closed** |
| RH | **Open** |
| Programme label | `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` |

---

## One-liner

**Density counts bulk zeros; isolation arranges them — Mass-with-A needs polylog density near \(\beta_\star\) or Iso_H; Maynard–Pratt half-isolation and Levinson horizontal isolation are different geometries and do not prove Iso_H.**

*Per aspera ad astra.*
