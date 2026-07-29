# Residual Product Cohomology \(H^\bullet(X_\times)\)

**Status:** Advanced and locked (combinatorial residual).  
**Date:** 2026-07-29  
**Depends on:** `Residual_Product_Complex.md`, `scripts/residual_product_complex_probe.py`  
**Probe:** `scripts/residual_product_cohomology_probe.py`  
**Results:** `residual_product_cohomology_results.json`  
**Provenance:** residual flux under Principle **(S)** only. Not free \(T^\sharp\). No continuum Cartan / No-Go lift.

---

## 0. Setup

\[
X_\times = K_9 \times P_{B'},\qquad B' = 539,
\]
\[
D(\varphi\otimes\psi)=d_Q\varphi\otimes\psi+(-1)^{\deg\varphi}\varphi\otimes d_P\psi.
\]
Locked cochains: \(\alpha,\omega_2,\mu,f,\delta f,\eta=\alpha\otimes\delta f-\omega_2\otimes f,\tilde\mu=\mu\otimes 1\).

---

## 1. Identity: \(\mu=-B'\,\omega_2\) on ordered triples

On ordered charge triples \(a<b<c\):

\[
\omega_2(a,b,c)=-1,\qquad \mu(a,b,c)=B'\,,
\]
hence
\[
\boxed{\mu(a,b,c)=-B'\,\omega_2(a,b,c)}\quad\text{on all }a<b<c.
\]

**Verified** in probe (84 ordered triples).  

The cup formula \(\mu=B'\,\mathrm{sgn}(a-b)\mathrm{sgn}(b-c)\) equals this alternating value on the ordered chamber; the fully alternating extension \(\mu_{\mathrm{alt}}:=-B'\omega_2\) is \(d_Q\)-closed on all 4-tuples.

---

## 2. Three levels

### 2.1 Graph (1-skeleton)

Cartesian product of undirected graphs \(K_9\,\square\,P_{B'}\):

| Object | \(V\) | \(E\) | \(b_0\) | \(b_1\) |
|--------|------:|------:|--------:|--------:|
| \(K_9\) | 9 | 36 | 1 | 28 |
| \(P_{B'}\) | 539 | 538 | 1 | 0 |
| Product 1-skeleton | \(9\cdot 539=4851\) | \(36\cdot539+538\cdot9=24246\) | 1 | **19396** |

\[
b_1 = E-V+1 = 19396
\]
for the connected product graph. This is **nontrivial combinatorial \(H_1\)** of the residual product 1-skeleton (not the geometric simplex product).

### 2.2 Form complex (tensor + locked forms)

| Fact | Status |
|------|--------|
| \(\eta=-D(\alpha\otimes f)\) | **True** (full tensor calculus) |
| \([\eta]=0\) in unrestricted \(H^2(C^\bullet\otimes C^\bullet)\) | **Yes** |
| \([\tilde\mu]=0\) when \(K_9\simeq\Delta^8\) | **Yes** (contractible) |
| \(\eta\) still **nontrivial as cochain** (squares/triangles) | **Yes** (probe) |
| Coupling witness | exact primitive \(\alpha\otimes f\) carries residual \(f,\delta f\) |

So unrestricted form cohomology in positive degree is trivial; residual content sits in **structure of primitives and arithmetic**, not in a free \([\eta]\neq 0\) class over \(\mathbb{Q}\).

### 2.3 Full simplex (geometric / Künneth)

| Factor | Type | \(H^{>0}\) |
|--------|------|------------|
| \(K_9\) as \(\Delta^8\) | contractible | 0 |
| \(P_{B'}\) as interval | contractible | 0 |
| Product | contractible | 0 |

\[
H^0(X_\times;\mathbb{Q})\cong\mathbb{Q},\qquad H^{n>0}(X_\times;\mathbb{Q})=0.
\]

---

## 3. Where residual nontrivial \(H^\bullet\) lives

| Location | Nontrivial data | Locked value |
|----------|-----------------|--------------|
| Graph \(H_1\) | product 1-skeleton | \(b_1=19396\) |
| Residual arithmetic (combinatorial \(H^0\)-type) | \(\sum\mu\) | \(84B'=45276\) |
| Bott-type mod 8 | \(B'\bmod 8\) | 3 |
| Path | edges \(\bmod 8\) | 2 |
| Unit block | \(\lvert U\rvert\) | 3 |
| Mixed coupling | \(\eta=-D(\alpha\otimes f)\) | exact witness, nonzero cochain |
| Ordered 2-form | \(\mu=-B'\omega_2\) | verified |

**Lock statement:**  
Geometric \(H^{n>0}(X_\times;\mathbb{Q})=0\). Nontrivial residual combinatorial structure is locked as graph \(b_1=19396\), mass \(\sum\mu=84B'=45276\), \(B'\equiv 3\pmod 8\), and \(\mu=-B'\omega_2\) on ordered triples, with \(\eta\) an exact mixed coupling witness under Principle (S).

---

## 4. What this does *not* claim

- Continuum Cartan / hopfion  
- Free \(T^\sharp\to 539\) basins (Option 3)  
- Nonzero singular \([\eta]\) over \(\mathbb{Q}\)  
- Biological 18/521 peak detection  

---

## 5. Verification checklist

1. `residual_product_complex_probe.py` — \(D\eta=0\), factor locks  
2. `residual_product_cohomology_probe.py` — three-level \(H^\bullet\), \(\mu=-B'\omega_2\) ordered  
3. JSON results written beside probes  

---

## 6. Bottom line

> Advance residual \(H^\bullet(X_\times)\): geometric cohomology is trivial in positive degree; **nontrivial residual combinatorial \(H\)** is locked at **graph**, **form-arithmetic**, and **mod-8** levels under residual provenance — consistent with the product complex lock and Option 3.

*Per aspera ad astra.*
