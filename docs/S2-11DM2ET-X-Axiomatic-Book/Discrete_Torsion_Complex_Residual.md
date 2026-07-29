# Discrete torsion-style complex on residual cores (TTC / RTTC enrichment)

**Direction 2 (primary):** controlled **discrete** enrichment of Temporal Torsion Cohomology / Resonant Temporal Torsion Cohomology.  
**Status:** Residual-only cochain package **assembled and verified**. Continuum Cartan field equations **not** claimed.  
**Provenance (mandatory):** residual flux quanta under Principle **(S)** + democratic charge-sector partition — **not** free \(T^\sharp\). No No-Go lift. Option 3 unchanged.

**Depends on:** `Discrete_Patterns_Residual_Carrier.md` (core linking, \(\delta f\), \(\omega_2\), \(\mu\), \(\beta_\sharp\) fibers).  
**Probe:** `scripts/discrete_torsion_complex_probe.py`.

---

## 0. Scope and non-claims

| In scope (combinatorial) | Out of scope (Cat.\ B continuum / forbidden) |
|--------------------------|-----------------------------------------------|
| Cochains on residual cores and charge \(K_9\) | Continuum Cartan torsion field equations |
| Differentials \(d\) with \(d^2=0\) where defined | Continuum hopfions as free \(T^\sharp\) basins |
| \(\beta_\sharp\)-grading of the core path | Identifying this complex with book continuum \(T=d+(\zeta^t-1)\wedge H_3\) without extra work |
| Arithmetic identities involving \(B'\bmod 8\) | Security reductions; No-Go lift |

**Category label.** The *combinatorial* cochain package is Category A-adjacent discrete mathematics on locked residual data.  
Calling it a “TTC/RTTC enrichment” is **Category B terminology** (model contact). Continuum geometric identification remains **Category B design space**.

---

## 1. Discrete spaces

### 1.1 Charge sector complex

Vertices \(Q_9=\{0,1,\ldots,8\}\) (residual charge-sector indices).  
Simplicial set: complete complex \(K_9\) (all ordered tuples of distinct vertices as nondegenerate simplices, or equivalently the ordered simplex on 9 letters).

### 1.2 Residual core path

Canonical core \(\mathcal{O}_{\mathrm{res}}=\{x_0<\cdots<x_{B'-1}\}\).  
**Path complex** \(P_{B'}\): vertices \(\{0,\ldots,B'-1\}\); 1-simplices \((i,i+1)\).  
Optional **tower clique enrichment** \(P_{B'}^+\): add 2-simplices on each same-tower triple (56 triangles on canonical core 0).

### 1.3 Residual charge density

Monochrome lifts
\[
\rho\colon Q_9\to\mathbb{Z}/9\mathbb{Z},
\qquad
\rho(q)=r_q,
\]
where every label in \(\mathcal{O}_{\mathrm{res}}^{(q)}\) satisfies \(x\equiv r_q\pmod 9\).  
Canonical: \((\rho(0),\ldots,\rho(8))=(3,4,5,6,7,8,0,1,2)\).

---

## 2. Cochain package (assembled torsion source)

### 2.1 On charge \(K_9\)

| Degree | Cochain | Formula | \(d\)-property |
|--------|---------|---------|----------------|
| 0 | \(u(a)=a\) | sector index | — |
| 1 | \(\alpha(a,b)=\mathrm{sgn}(a-b)\) | unit skew | — |
| 1 | \(L_{ab}=B'\alpha(a,b)\) | core linking scale | — |
| 2 | \(\omega_2=d\alpha\) | \(\mathrm{sgn}(b-c)-\mathrm{sgn}(a-c)+\mathrm{sgn}(a-b)\) | **exact**; \(d\omega_2=0\) |
| 2 | \(\mu(a,b,c)=B'\,\mathrm{sgn}(a-b)\mathrm{sgn}(b-c)\) | Massey-style product of links | **\(d\mu=0\)** (2-cocycle) |
| 0 | \(\rho\) | monochrome mod-9 density | **flat** on each core: \(d\rho=0\) along any edge inside one core |

### 2.2 On the core path

| Degree | Cochain | Formula | \(d\)-property |
|--------|---------|---------|----------------|
| 0 | \(f(i)=\tau(x_i)\) | tower label | — |
| 1 | \((\delta f)(i,i+1)=\tau(x_{i+1})-\tau(x_i)\) | tower coboundary | **exact** on \(P_{B'}\); telescopes |

### 2.3 Discrete torsion source (definition)

**Definition (residual discrete torsion package).**  
\[
\mathfrak{T}_{\mathrm{res}}
:=
\bigl(
\rho,\;
\alpha,\;
L,\;
\omega_2,\;
\mu,\;
f,\;
\delta f
\bigr)
\]
with differentials as in §§2.1–2.2.

**Source interpretation (combinatorial only).**  
- \(\rho\): residual **charge density** on sectors.  
- \(\delta f\): discrete **spin/tower transport** along residual order.  
- \(\mu\) and \(\omega_2\): discrete **sector curvature / linking products**.  
- \(L=B'S\): global pairing scale.

No continuum metric or Cartan connection is introduced.

---

## 3. Closure and \(d^2=0\)

### 3.1 Charge complex

**Theorem (Charge closure).**  
On \(K_9\) with the cochains above:

1. \(d\alpha=\omega_2\) and \(d\omega_2=0\).  
2. \(d\mu=0\) on every ordered 4-simplex.  
3. For all \(a<b<c\): \(\omega_2(a,b,c)=-1\) and \(\mu(a,b,c)=B'\).

*Proof.* §12 of `Discrete_Patterns_Residual_Carrier.md` + probe.

### 3.2 Path complex

**Theorem (Path exactness).**  
\(\delta f=df\) on \(P_{B'}\), hence \(d(\delta f)=0\) in the sense that the path has no independent 2-simplices; on any tower triangle \((i,j,k)\) with the same \(\tau\), the alternating sum of edge values of \(\delta f\) along a spanning tree cancels when extended by zero off-path, while the **index** 2-cochain \(\omega_2(i,j,k)=-1\) for \(i<j<k\) is exact as \(d\mathrm{sgn}\) on indices.

**Proposition (Tower triangles).**  
There are **56** same-tower 3-point cliques on canonical core 0. On each ordered triple of indices \(i<j<k\),
\[
\omega_2^{\mathrm{idx}}(i,j,k):=\mathrm{sgn}(j-k)-\mathrm{sgn}(i-k)+\mathrm{sgn}(i-j)=-1,
\]
matching the charge-sector value of \(\omega_2\) on ordered triples.

### 3.3 \(\beta_\sharp\)-grading

**Definition.** Grade core vertices by \(\beta_\sharp(i)=i\bmod 8\).

**Theorem (Homogeneous path edges).**  
Every path edge \((i,i+1)\) raises Bott degree by exactly \(+1\bmod 8\):
\[
\beta_\sharp(i+1)-\beta_\sharp(i)\equiv 1\pmod 8.
\]
Thus \(\delta f\) is a **degree-\(+1\)** cochain in the \(\beta_\sharp\)-grading: it maps the graded piece of vertices of degree \(k\) into edges of type \(k\to k+1\).

**Corollary (Fiber isolation under adjacency).**  
Index-adjacent edges never stay inside a single Bott fiber \(F_k\). Within-fiber structure is **0-dimensional** for the path adjacency; linking among fibers is the separate RNT form of §10 in the patterns note (blocks \(U,V\), cross zero).

**Closure under residual order + \(\beta_\sharp\):**  
the path differential is compatible with residual total order and is homogeneous of degree 1 for \(\beta_\sharp\); charge-complex differentials ignore \(\beta_\sharp\) and close independently (\(d^2=0\)).

---

## 4. Global arithmetic identities (\(B'\equiv 3\pmod 8\))

Let \(B'=\lfloor(N_{\mathrm{flux}}-f_{\max})/9\rfloor\) and write \(B'=8\cdot 67+3\).

| ID | Identity | Value / check |
|----|----------|----------------|
| **I1** | \(B'\equiv 3\pmod 8\) | \(539\equiv 3\) |
| **I2** | Bott block \(\lvert U\rvert=3\equiv B'\pmod 8\) | Same residual **3** as \(B'\bmod 8\) |
| **I3** | \(\lvert V\rvert=5\), \(\lvert U\rvert+\lvert V\rvert=8\) | Full Bott clock |
| **I4** | \(3\cdot 68+5\cdot 67=B'\) | Fiber size partition of the core |
| **I5** | \(\displaystyle\sum_{a<b<c}\mu(a,b,c)=\binom{9}{3}B'=84\,B'\) | \(84\cdot 539=45276\) |
| **I6** | \(\displaystyle\sum_{a<b<c}\omega_2(a,b,c)=-\binom{9}{3}=-84\) | Independent of \(B'\) |
| **I7** | Path edge count \(B'-1=538=8\cdot 67+2\equiv 2\pmod 8\) | \((B'\bmod 8)-1\bmod 8\) |
| **I8** | \(\mathrm{Lk}(F_k,F_m)=0\) across \(U\leftrightarrow V\) | Separates the \(+3\) residual grades \(\{0,1,2\}\) from the bulk \(67\)-block |

**Structural reading (combinatorial).**  
The same integer **3** appears as:

1. \(B'\bmod 8\) (packaging residual after seed clear / charge split);  
2. \(\lvert U\rvert\), the number of Bott grades with fiber size 68 (the “excess” grades in A1);  
3. the scale of cross-fiber **vanishing** between \(U\) and \(V\).

The 2-cocycle \(\mu\) is **homogeneous of weight 1 in \(B'\)**: summing over charge triples multiplies the linking scale by the pure incidence count \(\binom{9}{3}=84\).

**Not claimed:** these identities prove continuum torsion quantization or fix \(G_4=539.9\).

---

## 5. Contact with TTC / RTTC (Category B naming)

| Continuum book language (Cat.\ B as model structure) | Discrete residual analogue (this note) |
|------------------------------------------------------|----------------------------------------|
| Torsion operator / spin density source | Package \(\mathfrak{T}_{\mathrm{res}}\): \(\rho\), \(\delta f\), \(\mu\) |
| Temporal / resonant cohomology | Cochain cohomology of \(K_9\) and \(P_{B'}\) with the listed \(d\) |
| Flux period / cyclotomic coefficients | **Not** reproduced; \(B'\) and \(\beta_\sharp\) only |
| Sub-harmonics \(\{5,15,45\}\,\mathrm{s}\) | **Not** used here |

**Allowed statement:**  
> A residual-only discrete cochain package \(\mathfrak{T}_{\mathrm{res}}\) exists, is closed under the differentials above, is compatible with residual order and \(\beta_\sharp\), and supplies a combinatorial substrate for Category B TTC/RTTC enrichment.

**Forbidden statement:**  
> Continuum Cartan torsion equals \(\mathfrak{T}_{\mathrm{res}}\), or free \(T^\sharp\) dynamics produce this complex as 539 basins.

---

## 6. Optional next deepenings (still residual-only)

| Item | Notes |
|------|--------|
| Total complex \(K_9\times P_{B'}\) with product differential | Couple \(\mu\) to path chains |
| Coefficients in \(\mathbb{Z}/B'\) or \(\mathbb{Z}/8\) | Reduce \(L\) and \(\mu\) mod Bott residual |
| Cohomology dimensions \(H^*(K_9;\mathbb{Z})\) with \(\alpha,\mu\) as products | Pure algebraic topology on \(K_9\) |
| Direction 1 Massey higher products | \(d^{-1}\) products of \(\mu\) with \(\alpha\) |

---

## 7. Verification checklist

`scripts/discrete_torsion_complex_probe.py` asserts:

1. Monochrome \(\rho\) and core sizes \(B'\).  
2. \(L=B'S\), \(\omega_2=d\alpha\), \(d\mu=0\), \(\omega_2\equiv -1\) on ordered triples, \(\mu\equiv B'\) on ordered triples.  
3. Every path edge has \(\Delta\beta_\sharp\equiv 1\pmod 8\).  
4. Identities I1–I8 (arithmetic block).  
5. 56 tower triangles; \(\omega_2^{\mathrm{idx}}=-1\) on each ordered index triple.  
6. Provenance flags.

---

## 8. Bottom line

> **Direction 2 discrete layer:** the package  
> \[
> \mathfrak{T}_{\mathrm{res}}=(\rho,\alpha,L,\omega_2,\mu,f,\delta f)
> \]  
> is a closed residual-only torsion-style cochain complex, homogeneous under \(\beta_\sharp\) on the core path, with global arithmetic tying \(B'\equiv 3\pmod 8\) to the Bott block \(\lvert U\rvert=3\).  
> Continuum TTC/RTTC field equations remain Category B design space. Free \(T^\sharp\) origin and No-Go lifts are not claimed.
