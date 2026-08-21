# T3 Integrality, Euler Double-Sum, and \(g_7\) Residue Vanishing — Proved (2026-08-21)

**Status:** Category A arithmetic / q-series. Residual Discrete Algebra (539 COUNT) ≠ Resonant. Residual-flux provenance mandatory. Continuum ARCHIVE.

These are the mathematical advances of the 2026-08-21 Ramanujan Journal review. They do not make the current manuscript submitable by themselves. They replace “verified to degree 20” and “a direct residue analysis shows” with proofs.

Companion: `REFEREE_REPORT_Ramanujan_Journal_Manuscript_2026-08-21.md`.  
Script: `scripts/verify_gs_euler_g7_t3.py`.

---

## 1. The series

For each positive integer \(s\) define
\[
g_s(q)=\sum_{n=0}^\infty \frac{q^{n^2}}{(-q^s;q^s)_n}.
\]
When \(s=1\) this is Ramanujan's fifth-order mock theta function
\[
f_0(q)=\sum_{n=0}^\infty \frac{q^{n^2}}{(-q;q)_n}.
\]
It is not the case that \(g_s(q)=f_0(q^s)\), because
\[
f_0(q^s)=\sum_{n=0}^\infty \frac{q^{s n^2}}{(-q^s;q^s)_n}
\]
has quadratic exponents \(s n^2\). The residual series is a mixed-scale analogue.

---

## 2. Theorem (Euler double-sum)

Let
\[
P_s(q):=(-q^s;q^s)_\infty\, g_s(q).
\]
Then
\[
P_s(q)=\sum_{k=0}^\infty \frac{q^{s k(k+1)/2}}{(q^s;q^s)_k}\sum_{n=0}^\infty q^{n^2+s k n}.
\]

**Proof.** The Pochhammer splitting
\[
(-q^s;q^s)_\infty=(-q^s;q^s)_n\,(-q^{s(n+1)};q^s)_\infty
\]
gives
\[
P_s(q)=\sum_{n=0}^\infty q^{n^2}\,(-q^{s(n+1)};q^s)_\infty.
\]
Euler's identity
\[
(z;q)_\infty=\sum_{k\ge 0}\frac{(-1)^k z^k q^{k(k-1)/2}}{(q;q)_k}
\]
with \(z=-q^{s(n+1)}\) and base \(q^s\) yields
\begin{align*}
(-q^{s(n+1)};q^s)_\infty
&=\sum_{k\ge 0}\frac{(-1)^k (-q^{s(n+1)})^k (q^s)^{k(k-1)/2}}{(q^s;q^s)_k}\\
&=\sum_{k\ge 0}\frac{q^{s k(n+1)}\, q^{s k(k-1)/2}}{(q^s;q^s)_k}\\
&=\sum_{k\ge 0}\frac{q^{s k n + s k(k+1)/2}}{(q^s;q^s)_k}.
\end{align*}
Substitute and rearrange the absolutely convergent double sum in \(|q|<1\). QED.

The manuscript's “verified by direct expansion to degree 20” is therefore unnecessary. The identity is classical Euler, not a new theorem. It must still be written as a proof in any submission.

The associated inner quadratic form in \((n,k)\) is \(n^2 + s k n + s k(k+1)/2\). Completing the square in \(n\) gives \(n^2 + s k n = (n+\tfrac{s k}{2})^2 - (s k/2)^2\). Signature statements about a ternary form after expanding a third Pochhammer are a rewriting of the same identity; they do not by themselves trigger Zwegers.

---

## 3. Theorem (\(\Phi\) collapse)

Define
\[
\Phi(m;q)=\sum_{r\ge 0}\frac{(-1)^r q^{r(r+1)/2+m r}}{(q;q)_r}.
\]
Then \(\Phi(m;q)=(q^{m+1};q)_\infty\).

**Proof.** The exponent identity \(r(r+1)/2+m r = r(r-1)/2+(m+1)r\) rewrites the sum as Euler's generating function with \(w=-q^{m+1}\):
\[
\sum_{r\ge 0}\frac{w^r q^{r(r-1)/2}}{(q;q)_r}=(-w;q)_\infty.
\]
Hence \(\Phi(m;q)=(q^{m+1};q)_\infty\). QED.

This is classical. It confirms consistency of the triple-sum rewriting with the double-sum, and does not prove modularity.

---

## 4. Theorem (residue vanishing)

Let \(s\) be a positive integer. Every monomial in the \(n\)th summand of \(g_s\) has exponent congruent to \(n^2\) modulo \(s\). Consequently the coefficient of \(q^m\) in \(g_s\) vanishes unless \(m\) is a square modulo \(s\).

In particular, for \(s=7\) the squares modulo 7 are \(\{0,1,2,4\}\), so coefficients on classes 3, 5, 6 vanish.

**Proof.** One has
\[
(-q^s;q^s)_n=\prod_{j=1}^n(1+q^{s j}).
\]
The reciprocal \(1/(-q^s;q^s)_n\) is a power series in \(q^s\). Multiplying by \(q^{n^2}\) produces only exponents \(\equiv n^2\pmod{s}\). Summing over \(n\) preserves the constraint. QED.

Computational check (script below): coefficients of \(g_7\) through degree 80 have no terms on classes 3, 5, 6 modulo 7. Nonzero residues that appear: 0, 1, 2, 4.

This does not use 539, N_flux, or packaging.

---

## 5. \(T_3\) integrality

### 5.1 The manuscript formula is not exact-integral

The Ramanujan manuscript writes
\[
T_3(n)=\frac{n}{3}\ (n\equiv 0),\quad \frac{4n+2}{3}\ (n\equiv 1),\quad \frac{2n+1}{3}\ (n\equiv 2),
\]
and claims the map is integral. Exact division fails on the third branch: if \(n=3k+2\) then \(2n+1=6k+5\equiv 2\pmod{3}\). Failures in \(\{0,\ldots,49\}\): sixteen values, all with \(n\equiv 2\pmod{3}\), starting \(n=2,5,8,11,\ldots\).

### 5.2 Corpus canonical map is floor division

`scripts/hqcc_ternary_map_sympy.py` uses integer division
\[
n\mapsto n//3,\quad (4n+2)//3,\quad (2n+1)//3
\]
by residue. That map is integral by construction. It has fixed point 0 and 2-cycle \(\{1,2\}\).

### 5.3 Exact-integer form equivalent to the canonical floor map

On \(n=3k+2\),
\[
\left\lfloor\frac{2n+1}{3}\right\rfloor=\left\lfloor\frac{6k+5}{3}\right\rfloor=2k+1=\frac{2n-1}{3}.
\]
On \(n=3k+1\), \((4n+2)/3=4k+2\) is already an integer. On \(n=3k\), \(n/3=k\) is an integer.

**Canonical exact-integer write-up** (use this in any number-theory text):
\[
T_3(n)=\begin{cases}
n/3 & n\equiv 0\pmod{3},\\
(4n+2)/3 & n\equiv 1\pmod{3},\\
(2n-1)/3 & n\equiv 2\pmod{3}.
\end{cases}
\]
This agrees with the corpus floor map on all nonnegative integers. It does not agree with the manuscript's exact reading of \((2n+1)/3\).

\(T_3\) is unused in the \(g_s\) identities and should be omitted from a Ramanujan Journal note.

---

## 6. What these proofs do not give

- They do not prove that \(g_s\) is the holomorphic part of a harmonic Maass form.
- They do not prove quantum modularity.
- They do not justify \(s\in\{7,8,11\}\) as a distinguished set, except that \(s=7\) is an instance of the residue theorem and \(7,11\) divide 539. The value 8 is not a factor of 539.
- They do not legitimise \(N_{\mathrm{flux}}=4880\) or \(B'=\lfloor(N_{\mathrm{flux}}-f_{\max})/9\rfloor\) as q-series input.

Packaging identities \(539=7^2\cdot 11\), \(3\cdot 68+5\cdot 67=539\), \(18+521=539\) remain elementary arithmetic. Provenance of 539 as a COUNT in residual discrete algebra is unchanged and is not a modular-form theorem.

---

## 7. Computational record (2026-08-21)

- Non-integral exact \((2n+1)/3\) among \(n=0..49\): 16 values, all \(n\equiv 2\pmod{3}\).
- Exact \((2n-1)/3\) on those \(n\): integral, and equal to canonical floor \(T_3\).
- \(g_7\) through degree 80: vanishing violations = none; nonzero residues mod 7 = \(\{0,1,2,4\}\).
- \(539=7^2\cdot 11=3\cdot 68+5\cdot 67=18+521\): true.
- \(\lfloor e^3\cdot 3^5\rfloor=4880\). Back-solving \(B'=539=\lfloor(4880-f_{\max})/9\rfloor\) forces \(f_{\max}\in[21,29]\). That parameter is extra input, not q-series.

---

*End of corrections note. 2026-08-21.*
