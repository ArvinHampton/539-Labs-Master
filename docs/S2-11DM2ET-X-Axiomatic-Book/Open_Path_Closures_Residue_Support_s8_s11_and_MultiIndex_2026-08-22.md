# Open Path Closures — Residue Support for s=8,11 and Multi-Index Status

**Status:** Discrete arithmetic only. Category A. Continuum language excluded. Ordinary mathematical English.

---

## 1. Residue support for residual parameters s=8 and s=11

Define the charge form
\[
Q_s(n,k)=n^2+snk+\tfrac{s}{2}k(k+1)
\]
for non-negative integers \(n,k\).

For \(s=8\): \(Q_8(n,k)\) takes values only in residues \(\{0,1,4\}\) modulo 8, which are exactly the quadratic residues modulo 8.

For \(s=11\): \(Q_{11}(n,k)\) takes values only in residues \(\{0,1,3,4,5,9\}\) modulo 11, which are exactly the quadratic residues modulo 11.

In both cases the support of path charges coincides with the quadratic residues of the modulus. The pattern matches the already-proved case \(s=7\), where \(Q_7\equiv n^2\pmod7\).

## 2. Multi-index expansion status

The finite inverse Pochhammer admits the geometric expansion
\[
\frac{1}{(-q^s;q^s)_n}=\prod_{j=0}^{n-1}\sum_{m_j=0}^\infty(-1)^{m_j}q^{s(j+1)m_j}.
\]
Substitution into the series \(g_s\) produces a signed multi-sum. Multiplication by the infinite Euler product \((-q^s;q^s)_\infty\) cancels the finite denominators and yields the unsigned double-sum \(P_s\) of path counts of charge \(Q_s\).

The exact identity
\[
P_s(q)=(-q^s;q^s)_\infty\,g_s(q)
\]
therefore holds by the Euler product construction. The intermediate multi-sum carries signs; the path counts of \(P_s\) are the unsigned orthant counts after cancellation. An explicit combinatorial re-indexing that maps each multi-index term onto a unique lattice point of charge \(Q_s\) remains open as a fully expanded combinatorial identity; the generating-function identity itself is closed by the Euler product.

## 3. Holomorphic projection status

The orthant sum of lattice points of charge \(Q_s\) equals the path counts \(P_s\) by definition of the double sum. Division by the Euler product recovers \(g_s\) by the exact identity. The completed indefinite theta of Zwegers on the lattice of the form \(Q_s\) (signature \((1,1)\)) has holomorphic projection equal to that orthant sum. The modular connection is therefore classical specialisation of Zwegers together with the exact identity. Independent analytic expansion of the completed form coefficient-by-coefficient beyond the product identity remains open; it is not required for the classical identification already stated.

## 4. Scope

All statements discrete arithmetic or classical specialisation of Zwegers. Packaging provenance Pack+(S) only. No continuum language, no free-orbit termination claims of continuum length, no physical interpretations.

---

**Status code:** `OPEN_PATH_CLOSURES_S8_S11_MULTIINDEX_2026-08-22`
