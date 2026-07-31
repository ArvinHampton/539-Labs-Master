# M1.2 — Remainder Bound Strategy and Lemma Form

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Strength:** strategy + **conditional lemma form** with named constants.  
**Not claimed:** a complete unconditional pointwise proof of the bound at off-line zeros, nor RH.

---

## 1. Object

From the GHK hybrid (unconditional),

\[
\zeta(s)=P_X(s)\,Z_X(s)\,(1+\varepsilon_X(s)),
\qquad
\lvert\varepsilon_X(s)\rvert
\le
C_{\varepsilon}\Biggl(
\frac{X^{K+2}}{(|s|\log X)^K}+X^{-\sigma}\log X\Biggr)
\]

for \(\sigma=\operatorname{Re}s\ge 0\), \(\lvert t\rvert\ge 2\), \(X\ge 2\), fixed integer \(K\ge 1\), and fixed smooth weight \(u\) of mass 1 as in GHK.

Write

\[
\log Z_X(s)
= -\sum_{\rho} U\bigl((s-\rho)\log X\bigr),
\qquad
U(z)=\int_0^\infty u(x)\,E_1(z\log x)\,dx.
\]

Near a distinguished zero \(\rho_\star\) of multiplicity \(m\), isolate

\[
\log Z_X(s)
= -m\,U\bigl((s-\rho_\star)\log X\bigr)
- \sum_{\rho\neq\rho_\star} U\bigl((s-\rho)\log X\bigr).
\]

For \(z\to 0\), \(U(z)\sim -\log z + \text{(real regularizer)}\) along a fixed branch (GHK / \(E_1\) asymptotics). Hence

\[
\theta_X(s)
:= \arg P_X(s)
= m\arg(s-\rho_\star)
- \operatorname{Im}\mathcal R_X^{(\mathrm{EP})}(s)
+ \delta_{\mathrm{br}}(s)
+ O\bigl(\lvert\varepsilon_X(s)\rvert\bigr),
\]

where the **Euler–Hadamard remainder** is

\[
\mathcal R_X^{(\mathrm{EP})}(s)
:=
\sum_{\rho\neq\rho_\star} U\bigl((s-\rho)\log X\bigr)
+ \mathcal R_X^{\mathrm{arith}}(s)
+ \mathcal R_X^{\mathrm{pole}}(s),
\]

and \(\delta_{\mathrm{br}}\) tracks branch choices (fixed once a path is chosen — M1.3).

**M1.2 goal:** bound \(\lvert\operatorname{Im}\mathcal R_X^{(\mathrm{EP})}(s_0)\rvert\) at test points \(s_0\).

---

## 2. Parameter regime (critical)

The GHK power error \(X^{K+2}/(|t|\log X)^K\) is **useless** unless

\[
X \ll |t|^{K/(K+2)}\,(\log X)^{O(1)}.
\]

In moment applications GHK take \(X=O((\log T)^{O(1)})\).  
**Diagnostic default:** \(X=(\log(|t|+3))^2\).

| Choice | Effect |
|--------|--------|
| \(X=200\), \(K=4\), \(t\sim 14\) | term3 \(\gg 10^5\) — bound dead |
| \(X=(\log t)^2\sim 7\)–\(20\) | term3 can be \(<1\) — usable sketch |
| \(X\to\infty\) at fixed \(t\) | hybrid error explodes; not the M1.2 regime |

---

## 3. Decomposition

Fix \(s_0=\sigma_0+it_0\), \(\lvert t_0\rvert\ge 2\), \(1/2\le\sigma_0\le 1\), \(X\ge 3\), \(H\ge 1\).

| Region | Zeros | Tool |
|--------|-------|------|
| Local | \(\lvert s_0-\rho\rvert\le r_{\mathrm{loc}}:=(\log X)^{-1}\) | Absorb into principal \(m\arg\); multiplicity via short-interval zero count |
| Medium | \(r_{\mathrm{loc}}<\lvert s_0-\rho\rvert\le H\) | \(\lvert U(z)\rvert\ll\min(1,\lvert z\rvert^{-1})\) + Stieltjes vs \(N(t)\) |
| Far | \(\lvert s_0-\rho\rvert>H\) | GHK power decay in \(K\) |
| Arithmetic / hybrid error | — | \(O(X^{-\sigma_0}\log X)+O(X^{K+2}/(|t_0|\log X)^K)\) |

---

## 4. Kernel bounds (named)

Assume \(u\) is \(C^\infty\), nonnegative, mass 1, GHK support conventions, and \(U\) as above.

**Hypothesis (K).** There exist absolute constants \(C_U^{(0)},C_U^{(K)}\) depending only on \(u\) and \(K\) such that on the principal sheet,

\[
\lvert\operatorname{Im}U(z)\rvert
\le
C_U^{(0)}\min\Bigl(1,\frac{1}{\lvert z\rvert}\Bigr)
+ C_U^{(K)}\frac{X^{O(1)}}{\lvert z\rvert^K}.
\]

**Working majorants** (not sharp):

\[
C_U^{(0)}\le 2.
\]

---

## 5. Zero-density hypothesis (named)

**Hypothesis (ZD).** There exist \(A(\sigma)\ge 0\) and \(B\ge 0\) such that

\[
N(\sigma,T)
:= \#\{\rho=\beta+i\gamma:\ \beta\ge\sigma,\ 0<\gamma\le T\}
\le C_{\mathrm{ZD}}\, T^{A(\sigma)(1-\sigma)}(\log(T+2))^B
\]

uniformly for \(\sigma\in[1/2,1]\), \(T\ge 2\).

**Classical instantiation (Ingham):**

\[
N(\sigma,T)\ll T^{3(1-\sigma)/(2-\sigma)}(\log T)^5.
\]

**Explicit:** Kadiri–Lumley–Ng (2018). **Log-free:** Bellotti-type bounds.

---

## 6. Lemma form (M1.2)

> **Lemma (M1.2 — conditional form).**  
> Assume (K) and (ZD). Let \(K\ge 2\), \(X\ge 3\), \(s_0=\sigma_0+it_0\) with \(\sigma_0\in[1/2,1]\), \(\lvert t_0\rvert\ge 2\), and
>
> \[
> \frac{X^{K+2}}{(|t_0|\log X)^K}\le 1.
> \]
>
> Choose \(H=(\log X)^{2}\). Exclude a local disk of radius \(r_{\mathrm{loc}}=(\log X)^{-1}\) about each zero (local piece absorbed into principal arg).  
> Then there exist constants \(C_1,C_2,C_3,C_4\) depending only on \(u,K,C_{\mathrm{ZD}},A(\cdot),B\) such that
>
> \[
> \bigl\lvert\operatorname{Im}\mathcal R_X^{(\mathrm{EP})}(s_0)\bigr\rvert
> \le
> R_{\mathrm{bound}}(X,s_0)
> :=
> C_1\frac{\log(\lvert t_0\rvert+2)}{\log X}
> + C_2\,\Sigma_{\mathrm{med}}(s_0,X,H)
> + C_3\frac{X^{K+2}}{(\lvert t_0\rvert\log X)^K}
> + C_4\, X^{-\sigma_0}\log X,
> \]
>
> where
>
> \[
> \Sigma_{\mathrm{med}}(s_0,X,H)
> :=
> \sum_{\substack{\rho\neq\rho_\star\\ r_{\mathrm{loc}}<\lvert s_0-\rho\rvert\le H}}
> \min\Bigl(1,\frac{1}{\lvert s_0-\rho\rvert\log X}\Bigr).
> \]
>
> Moreover, under (ZD) and partial summation,
>
> \[
> \Sigma_{\mathrm{med}}(s_0,X,H)
> \le
> C_\Sigma\Biggl(
> \log\log(\lvert t_0\rvert+3)
> + \frac{N_{\mathrm{box}}}{\log X}
> + 1
> \Biggr).
> \]

**Proof outline (not a full write-up):**

1. Split the sum over \(\rho\) into local / medium / far.  
2. Local: removed by definition of \(\mathcal R\) (charged to \(m\arg\)).  
3. Medium: apply \(\lvert\operatorname{Im}U\rvert\le C_U^{(0)}\min(1,\lvert z\rvert^{-1})\); Stieltjes integrate using short-interval \(N(t)\) bounds and (ZD).  
4. Far: \(K\)-decay of \(U\); \(H=(\log X)^2\).  
5. Arithmetic hybrid error: \(\operatorname{Im}\) of GHK \(\varepsilon_X\) for \(\lvert\varepsilon_X\rvert\le 1/2\).

**Status:** standard pattern; **full ε-management and branch control remain to be written line-by-line**. Not a published theorem.

---

## 7. Explicit constants — honesty freeze

| Symbol | Symbolic form | Working majorant | Status |
|--------|---------------|------------------|--------|
| \(C_U^{(0)}\) | \(\operatorname{Im}U\) scale | \(\le 2\) | Effective for fixed \(u\) |
| \(C_1\) | short \(N(t)\) density | \(\le 2/\pi\) classically | Effective under classical zero counting |
| \(C_2\) | \(C_U^{(0)}\) | \(\le 2\) | Effective |
| \(C_3\) | GHK \(K\)-constant | \(O_u(1)\) for each fixed \(K\) | Effective once \(u,K\) fixed; not optimized |
| \(C_4\) | hybrid tail | \(\le 2\) | Effective |
| \(C_\Sigma\) | Stieltjes factor | \(\le 4\) provisional | Needs full write-up |
| \(C_{\mathrm{ZD}}\) | density prefactor | literature-explicit in ranges | Cite Kadiri–Lumley–Ng |

**Honesty freeze:** constants **exist and are finite** once \(u,K\), and a density theorem are fixed. **Invented optimized decimals are inadmissible.**

Crude package majorants for code:

```text
C1 = 1.0
C2 = 2.0
C3 = 1.0
C4 = 2.0
```

---

## 8. Average vs pointwise

| Mode | Bound on \(\Sigma_{\mathrm{med}}\) | Use |
|------|-------------------------------------|-----|
| Average over \(t_0\in[T,2T]\) | \(\ll\log\log T\) typical | Supports Conjecture A means |
| Pointwise near zero clusters | can be \(\gg\log\log T\) | Blocks naive M1.3 on short arcs |
| Under density hypothesis | better wide-window control | Conditional sharpening only |

**Critical remark:** average bounds do **not** give Conjecture B. Pointwise medium sums near clusters are the bottleneck for M1.2 → M1.3.

---

## 9. Implementation sketch (code)

Script: `scripts/rh_M1_2_remainder_sketch.py`

```bash
python scripts/rh_M1_2_remainder_sketch.py          # default X=(log t)^2
python scripts/rh_M1_2_remainder_sketch.py --x 20 --K 4
python scripts/rh_M1_2_remainder_sketch.py --x-mode log3
```

- Known zeros only (incomplete medium sum).  
- Flags `ghk_power_error_useful` when term3 \(<1\).  
- P1 semicircle probe vs \(R_{\mathrm{bound}}\).  
- **No RH claim.**

---

## 10. What M1.2 does **not** do

- Does not prove RH.  
- Does not by itself prove Conjecture B.  
- Does not remove the need for M1.3.  
- Does not license Category B constants.

---

## 11. Next after M1.2

1. Full line-by-line proof under (K)+(ZD).  
2. Optimize \(H,K,u\) for minimal \(R_{\mathrm{bound}}\) at first-zero heights.  
3. Feed into M1.3 path design.  
4. Optional: short-\(H\) using only \(N(t+1)-N(t)\ll\log t\).
