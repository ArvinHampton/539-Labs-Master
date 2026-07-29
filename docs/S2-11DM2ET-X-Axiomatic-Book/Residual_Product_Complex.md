# Residual product complex \(K_9\times P_{B'}\)

**Primary next structure (residual-only).**  
Couples the locked **charge-sector complex** to the **residual core path** by a product simplicial set and product differential.  
**Status:** Defined, mixed closed cochains constructed, \(D^2=0\) / \(D\eta=0\) verified.  
**Provenance (mandatory):** residual flux under Principle **(S)** + democratic charge-sector partition — **not** free \(T^\sharp\). Continuum Cartan, free-\(T^\sharp\) origin, and No-Go lifts are **out of scope**.

**Depends on:** `Discrete_Patterns_Residual_Carrier.md`, `Discrete_Torsion_Complex_Residual.md`.  
**Probe:** `scripts/residual_product_complex_probe.py`.

---

## 1. Product simplicial set

### 1.1 Factors

| Factor | Symbol | 0-cells | 1-cells | Higher |
|--------|--------|---------|---------|--------|
| Charge sectors | \(K_9\) | \(a\in\{0,\ldots,8\}\) | ordered pairs \(a\neq b\) | all ordered \(k\)-tuples of distinct sectors (complete) |
| Residual path | \(P_{B'}\) | \(i\in\{0,\ldots,B'-1\}\) | edges \(e_i=(i\to i+1)\) | none (1-dimensional) |

Here \(B'=\lfloor(N_{\mathrm{flux}}-f_{\max})/9\rfloor\) and the path indexes the sorted residual core order (canonical core 0 supplies tower labels for \(\delta f\)).

### 1.2 Product

\[
X_{\times}
:=
K_9\times P_{B'}.
\]

**0-cells:** pairs \((a,i)\).  
**1-cells:**  
- *Horizontal* \(H(a,b;i)\): charge edge \(a\to b\) at fixed residual index \(i\);  
- *Vertical* \(V(a;i)\): path edge \(i\to i+1\) at fixed sector \(a\).  

**2-cells:**  
- *Triangles* \(T(a,b,c;i)\): charge 2-simplex at fixed \(i\);  
- *Squares* \(S(a,b;i)\): product of charge edge \(a\to b\) with path edge \(e_i\) (prism wall).  

**3-cells (for \(D\) checks):**  
- *Tetrahedra* \(\times\) vertex (pure charge);  
- *Triangular prisms* \(T(a,b,c;i)\times e_i\) (mixed).

Optional tower enrichment \(P_{B'}^+\) adds residual index triangles on same-tower triples; the minimal product uses plain \(P_{B'}\).

---

## 2. Product cochain differential

Identify cochains with the **tensor product** of cochain complexes
\[
C^\bullet(X_{\times})
\;\supset\;
C^\bullet(K_9)\otimes C^\bullet(P_{B'}),
\]
total degree \(=\) sum of degrees, differential
\[
D(\varphi\otimes\psi)
=
d_Q\varphi\otimes\psi
+
(-1)^{\deg\varphi}\,
\varphi\otimes d_P\psi.
\]
Since \(d_Q^2=0\) and \(d_P^2=0\) on the locked factors, **\(D^2=0\)** on the tensor product (graded Leibniz).

Path has no 2-simplices, so \(d_P\) vanishes on 1-cochains of \(P_{B'}\) in the sense that there is no free path 2-coboundary; for the 0-cochain \(f\) one has \(d_P f=\delta f\) along edges, and \(d_P(\delta f)=0\).

---

## 3. Locked factor cochains (recall)

| Cochain | Place | Property |
|---------|-------|----------|
| \(\alpha(a,b)=\mathrm{sgn}(a-b)\) | \(C^1(K_9)\) | unit skew |
| \(\omega_2=d_Q\alpha\) | \(C^2(K_9)\) | exact; \(\omega_2\equiv -1\) on \(a<b<c\) |
| \(\mu=B'\alpha\smallsmile\alpha\) (form \(B'\mathrm{sgn}(a-b)\mathrm{sgn}(b-c)\)) | \(C^2(K_9)\) | \(d_Q\mu=0\) |
| \(f(i)=\tau(x_i)\) | \(C^0(P_{B'})\) | tower labels on core 0 |
| \(\delta f=d_P f\) | \(C^1(P_{B'})\) | tower coboundary |

Identity used below (all distinct triples):
\[
\omega_2(a,b,c)
=
\mathrm{sgn}(a-b)+\mathrm{sgn}(b-c)+\mathrm{sgn}(c-a).
\]

---

## 4. Mixed closed cochains

### 4.1 Pure charge pullback (recovers \(\mu\))

\[
\tilde\mu
:=
\mu\otimes 1
\in
C^2(K_9)\otimes C^0(P_{B'}).
\]
Evaluates on triangles \(T(a,b,c;i)\) as \(\mu(a,b,c)\) (independent of \(i\)).

**Proposition.** \(D\tilde\mu=0\) because \(d_Q\mu=0\).  
**Restriction to pure charge:** \(\tilde\mu\mapsto\mu\).

### 4.2 Nontrivial mixed class \(\eta\) (primary coupling)

**Definition.**
\[
\eta
:=
\alpha\otimes \delta f
-
\omega_2\otimes f
\in
\bigl(C^1(K_9)\otimes C^1(P_{B'})\bigr)
\oplus
\bigl(C^2(K_9)\otimes C^0(P_{B'})\bigr)
\]
(total degree 2).

**Evaluation.**  
- On **square** \(S(a,b;i)\): \(\eta=\alpha(a,b)\,\delta f(i)\).  
- On **triangle** \(T(a,b,c;i)\): \(\eta=-\omega_2(a,b,c)\,f(i)\).

**Theorem (Mixed closure).** \(D\eta=0\).

*Proof.*  
\[
D(\alpha\otimes\delta f)
=
d_Q\alpha\otimes\delta f
+
(-1)^1\alpha\otimes d_P(\delta f)
=
\omega_2\otimes\delta f,
\]
\[
D(\omega_2\otimes f)
=
d_Q\omega_2\otimes f
+
\omega_2\otimes d_P f
=
\omega_2\otimes\delta f.
\]
Hence \(D\eta=0\). ∎

**Prism check (geometric).** On a triangular prism \((a,b,c)\times e_i\), the boundary formula reduces to
\[
\omega_2(a,b,c)\bigl(f(i)-f(i+1)\bigr)
+
\bigl(\alpha(a,b)+\alpha(b,c)+\alpha(c,a)\bigr)\delta f(i)
=
0,
\]
using \(f(i+1)-f(i)=\delta f(i)\) and \(\alpha(a,b)+\alpha(b,c)+\alpha(c,a)=\omega_2(a,b,c)\). Verified for all ordered triples and all path edges in the probe.

### 4.3 Restrictions (target: recover locked forms)

| Restriction | Result |
|-------------|--------|
| Pure charge triangle at level \(i\) | \(\eta\big|_{T(\cdot;i)}=-\omega_2\,f(i)\) — recovers \(\omega_2\) up to the tower height \(f(i)\) |
| Pure charge with \(f\) normalized / relative | ratios \(\eta(T;i)/\eta(T;j)=f(i)/f(j)\) when \(\omega_2\neq 0\) |
| Square walls | \(\eta\big|_{S(a,b;i)}=\alpha(a,b)\,\delta f(i)\) — product of **unit core linking sign** and **tower jump** |
| \(\tilde\mu\) on triangles | recovers \(\mu=B'\mathrm{sgn}(a-b)\mathrm{sgn}(b-c)\) exactly |

Thus the product complex carries **both** a pure residual charge 2-cocycle \(\tilde\mu\) and a **coupled** residual 2-cocycle \(\eta\) mixing sector orientation with residual path transport.

---

## 5. Global arithmetic (residual 3)

| ID | Identity | Role in product |
|----|----------|-----------------|
| **I1** | \(B'\equiv 3\pmod 8\) | Linking scale mod Bott period |
| **I2** | \(\lvert U\rvert=3\equiv B'\pmod 8\) | Bott excess block vs packaging residual |
| **P1** | \(\displaystyle\sum_{a<b<c}\mu(a,b,c)=84\,B'\) | Mass of \(\tilde\mu\) on ordered charge triples (per path vertex) |
| **P2** | \(\displaystyle\sum_{a<b}\sum_{i=0}^{B'-2}\eta\bigl(S(a,b;i)\bigr)=0\) | Skew \(\alpha\) sums to 0 against any \(\delta f\) |
| **P3** | Path length \(B'-1\equiv 2\pmod 8\) | Vertical edge count mod 8 |
| **P4** | Number of square types per edge \(i\): \(9\cdot 8=72\) oriented charge pairs | Product 1-skeleton width |

**P2 proof:** \(\sum_{a\neq b}\alpha(a,b)=0\) by skew-symmetry, so \(\sum_{a,b,i}\alpha(a,b)\delta f(i)=0\).

No new continuum claim: these are integer counts on residual cells.

---

## 6. Optional tower enrichment

Replace \(P_{B'}\) by \(P_{B'}^+\) (add 56 same-tower residual triangles).  
Then \(d_P\) may act nontrivially on path 1-cochains into those triangles; \(\omega_2^{\mathrm{idx}}\equiv -1\) on ordered index triples remains exact.  
The tensor identity \(D\eta=0\) still holds on the charge\(\otimes\)path summand; additional path 2-cells require checking \(d_P(\delta f)\) extensions (default: set \(\delta f=0\) off the path 1-skeleton). **Minimal lock uses plain \(P_{B'}\).**

---

## 7. What this closes / leaves open

| Gap | Status |
|-----|--------|
| No coupling between \(K_9\) and residual path | **Closed** by \(X_{\times}\) and \(\eta\) |
| \(D^2=0\) / \(D\eta=0\) on residual data | **Verified** |
| Recovers \(\mu\), \(\omega_2\), \(\alpha\,\delta f\) by restriction | **Yes** |
| Continuum Cartan / hopfion / free \(T^\sharp\) | **Still out of scope** |
| Architecture A4 \(B\mathrm{Spin}\) | Independent stream |

---

## 8. Verification

`scripts/residual_product_complex_probe.py` asserts:

1. Factor identities for \(\alpha,\omega_2,\mu,\delta f\).  
2. Algebraic identity \(\sum_{\mathrm{cyc}}\alpha=\omega_2\) on all triples.  
3. Prism cancellation for \(\eta\) on all \((a,b,c)\) and all path edges (using core-0 \(f,\delta f\)).  
4. \(\tilde\mu\) matches \(\mu\); square values match \(\alpha\,\delta f\).  
5. Arithmetic I1–I2, P1–P3.  
6. Provenance flags.

---

## 9. Bottom line

> The residual product complex  
> \[
> X_{\times}=K_9\times P_{B'}
> \]  
> with  
> \[
> \eta=\alpha\otimes\delta f-\omega_2\otimes f,
> \qquad
> \tilde\mu=\mu\otimes 1
> \]  
> couples charge sectors to the residual path by a **closed** mixed 2-cochain \(\eta\) and a pure charge pullback \(\tilde\mu\).  
> Everything remains residual-only under Principle (S). Continuum TTC field equations are not claimed.
