# Discrete combinatorial patterns on the residual carrier

**Primary pattern-research direction (highest priority, lowest risk).**  
**Status:** First closed combinatorial structures **executed and verified**.  
**Provenance (mandatory):** All objects are residual flux quanta under Principle **(S)** and democratic charge-sector partition — **not** free \(T^\sharp\). No free-dynamics 539-basins; No-Go untouched.

**Companions:** `PROGRAMME_BASELINE.md`, `Object539_NonCircular_Construction.md`, `Architecture_A1_Seed_Equivariance.md`, `Nine_Maths_Pattern_Exploration.md` (RNT / TTC contacts).  
**Probe:** `scripts/discrete_patterns_residual_probe.py`.

---

## 0. Locked data only

\[
\begin{aligned}
B'&=\Bigl\lfloor\frac{N_{\mathrm{flux}}-f_{\max}}{9}\Bigr\rfloor,\\
\mathcal{O}_{\mathrm{res}}^{(q)}
&=\mathrm{core}(C_q),\quad q\in\{0,\ldots,8\},
\quad
\lvert\mathcal{O}_{\mathrm{res}}^{(q)}\rvert=B',\\
\mathcal{O}_{\mathrm{res}}
&=\mathcal{O}_{\mathrm{res}}^{(0)}
\quad\text{(canonical single core)}.
\end{aligned}
\]

Labels on a sorted core \(\{x_0<\cdots<x_{B'-1}\}\):
\[
\bigl(q,\;\tau(x_i),\;\beta_\sharp(x_i)=i\bmod 8\bigr).
\]

Arithmetic identity (A1):
\[
B'=8\cdot 67+3,
\quad
\beta_\sharp\text{-fibers }(68,68,68,67,67,67,67,67).
\]

No continuum hopfions; no Cartan field equations in this document (those stay Category B design space — direction 2).

---

## 1. Line linking number (combinatorial)

**Definition.** For finite \(A,B\subset\mathbb{Z}\),
\[
\mathrm{Lk}(A,B)
:=
\sum_{a\in A}\sum_{b\in B}
\mathrm{sgn}(a-b),
\qquad
\mathrm{sgn}(0)=0,\;
\mathrm{sgn}(+)=+1,\;
\mathrm{sgn}(-)=-1.
\]

**Properties (elementary).**  
\(\mathrm{Lk}(A,A)=0\); \(\mathrm{Lk}(B,A)=-\mathrm{Lk}(A,B)\); integer-valued.

**Interpretation.** Discrete ordered linking / inversion count on the line (RNT-style integer pairing). Not continuum Gauss linking.

---

## 2. Theorem — Core linking form

**Setup.** Canonical residual pool \(R=\Omega\setminus\mathrm{Seed}\) with \(\mathrm{Seed}=\{0,\ldots,f_{\max}-1\}\), sorted; equitable round-robin classes \(C_q\), cores \(\mathcal{O}_{\mathrm{res}}^{(q)}\) of size \(B'\).

**Theorem (Core linking).**  
For all \(a,b\in\{0,\ldots,8\}\),
\[
\mathrm{Lk}\bigl(\mathcal{O}_{\mathrm{res}}^{(a)},\mathcal{O}_{\mathrm{res}}^{(b)}\bigr)
=
B'\,\mathrm{sgn}(a-b).
\]
In matrix form,
\[
L_{ab}
=
B'\,S_{ab},
\qquad
S_{ab}=\mathrm{sgn}(a-b),
\]
i.e.\ \(L=B'S\) with \(S\) the standard skew sign matrix on nine ordered charge sectors:
\[
S
=
\begin{pmatrix}
0 & -1 & -1 & \cdots & -1 \\
+1 & 0 & -1 & \cdots & -1 \\
\vdots &  & \ddots &  & \vdots \\
+1 & \cdots & +1 & 0
\end{pmatrix}.
\]

**Corollary.**  
- \(\mathrm{rk}_{\mathbb{R}}(L)=\mathrm{rk}(S)=8\) (one-dimensional kernel: constant vectors).  
- Every off-diagonal entry has absolute value \(B'\).  
- \(\gcd\bigl\{\lvert L_{ab}\rvert:a\neq b\bigr\}=B'\).

**Proof sketch.**  
Round-robin assignment of a totally ordered residual list of length \(N'=9B'+r\) (\(r=N'\bmod 9\)) places the first \(B'\) elements of each residue class of the index into the cores. For \(a\neq b\), the two arithmetic progressions of indices are strictly interlaced with constant order type: every element of the higher sector index is larger (as residual label) than the corresponding count forces \(\mathrm{Lk}= \pm B'\) with sign \(\mathrm{sgn}(a-b)\). Diagonal vanishes by antisymmetry of \(\mathrm{sgn}\) on \(A=A\). Full verification: exhaustive \(9\times 9\) matrix in the probe (all entries match \(B'\mathrm{sgn}(a-b)\)).

**RNT reading.**  
The nine cores carry a canonical integer pairing scaled exactly by the residual cardinality \(B'\). This is a **Resonant Number Theory** structure using only locked residual data.

---

## 3. Bott-fiber linking on a single core

On \(\mathcal{O}_{\mathrm{res}}=\mathcal{O}_{\mathrm{res}}^{(0)}\), let
\[
F_k=\{\,x_i\in\mathcal{O}_{\mathrm{res}}:\beta_\sharp(x_i)=k\,\},
\quad k\in\mathbb{Z}/8.
\]

**Definition.** Fiber linking matrix
\[
M_{km}=\mathrm{Lk}(F_k,F_m).
\]

**Executed facts (canonical core).**  
- \(M\) is skew; \(M_{kk}=0\).  
- Sample: \(M_{0,1}=-68\), \(M_{0,3}=0\), etc. (see JSON).  
- \(\gcd\) of off-diagonal \(|M_{km}|\) can be \(1\) (no forced global scale \(B'\) on fibers).  

Fiber linking is a finer RNT invariant of the \(\beta_\sharp\)-grading; it is **not** as rigid as the core form \(L=B'S\).

---

## 4. Discrete torsion-style cochains (combinatorial)

### 4.1 Tower coboundary on the core path

Order \(\mathcal{O}_{\mathrm{res}}=\{x_0<\cdots<x_{B'-1}\}\).  
**0-cochain** \(f(i)=\tau(x_i)\in\mathbb{Z}\) (tower label).  
**1-cochain** (path edges)
\[
(\delta f)(i,i+1)
:=
\tau(x_{i+1})-\tau(x_i)\in\mathbb{Z}.
\]

**Proposition.**  
\[
\sum_{i=0}^{B'-2}(\delta f)(i,i+1)
=
\tau(x_{B'-1})-\tau(x_0)
\]
(telescoping). On the canonical core this equals **241** (verified).

This is a discrete **exact** 1-cochain (coboundary) — the combinatorial analogue of a pure-gauge torsion contribution along the core order.

### 4.2 Charge monochromicity as a flat sector cocycle

**Proposition.**  
Each core \(\mathcal{O}_{\mathrm{res}}^{(q)}\) is monochromatic mod 9: all ambient labels satisfy \(x\equiv r_q\pmod 9\) for a fixed \(r_q\).  
Thus the assignment
\[
c_q(x)=r_q\in\mathbb{Z}/9
\]
is constant on the core (a **flat** 0-cochain under any graph with vertices in one core).

**Category B note (direction 2, not claimed here).**  
Promoting \((c_q,\delta f)\) to a source term for a discrete Cartan-type torsion operator on a complex built from cores is **TTC/RTTC enrichment** and must be labeled Category B when continuum language is used. The cochains themselves are pure combinatorics.

### 4.3 Normalized core cocycle on the charge 1-skeleton

View charge sectors \(\{0,\ldots,8\}\) as vertices of \(K_9\).  
**1-cochain**
\[
\alpha(a,b)=\mathrm{sgn}(a-b)\in\{-1,0,+1\}.
\]
Then \(L_{ab}=B'\alpha(a,b)\).  
\(\alpha=\delta u\) up to scale is related to the 0-cochain \(u(a)=a\) via \(\delta u(a,b)=b-a\), not identical to \(\mathrm{sgn}\), but \(\alpha\) is the **sign reduction** of the ordered sector structure.  
It records discrete orientation data for residual charge sectors.

---

## 5. Integer dictionary (RNT substrate)

| Symbol | Value / formula | Role |
|--------|-----------------|------|
| \(B'\) | \(\lfloor(N_{\mathrm{flux}}-f_{\max})/9\rfloor\) | Core size / linking scale |
| \(L_{ab}\) | \(B'\mathrm{sgn}(a-b)\) | Core pairing |
| \(S\) | \(\mathrm{sgn}(a-b)\) | Unit skew form on 9 sectors |
| \(\mathrm{rk}(L)\) | 8 | Corank-1 pairing |
| \(\beta_\sharp\) fibers | \((68^3,67^5)\) | Bott grading sizes |
| \(B'\bmod 8\) | 3 | Residual Bott arithmetic |
| \(\sum\delta f\) | \(\tau_{\mathrm{last}}-\tau_{\mathrm{first}}\) | Tower telescoping |
| Same-tower pairs in core | \(N_{\mathrm{pair}}=353\) (canonical core 0) | Tower clustering |
| Fiber linking \(M_{km}\) | §10 closed form | Bott-grade pairing |
| Same-tower adjacency spectrum | §11 | Incidence algebra |
| 2-cochain \(\omega_2,\mu\) | §12 | Exact / Massey-style on charge \(K_9\) |

All entries use only locked residual data.

---

## 6. What this strengthens

| Direction | Relation |
|-----------|----------|
| **1 (this doc)** | Discrete linking + cochains + RNT pairings **delivered**; fiber / incidence / 2-cochain extensions **§10–12** |
| **2 TTC/RTTC** | Flat charge + \(\delta f\) + \(\omega_2=d\alpha\) prepare a discrete torsion **source substrate** without continuum claims |
| **3 BMMT/HMT** | Nine cores as atomic supports of a discrete measure (mass \(B'\) each) — measure limit still Cat.\ B |
| **4 A4–A5** | Independent geometric stream |
| **5 Secondary** | Untouched; not mixed into provenance |

---

## 7. Forbidden claims

- Free \(T^\sharp\) origin of cores or of \(L_{ab}\).  
- Continuum hopfions produce 539 free basins.  
- \(\mathrm{Lk}\) is continuum Gauss linking of physical loops.  
- Core linking lifts the No-Go.  
- Security reduction from \(L=B'S\).

---

## 8. Verification

`scripts/discrete_patterns_residual_probe.py` asserts:

1. \(\lvert\mathcal{O}_{\mathrm{res}}^{(q)}\rvert=B'\) for all \(q\);  
2. \(L_{ab}=B'\mathrm{sgn}(a-b)\) for all \(a,b\);  
3. skew-symmetry and zero diagonal;  
4. monochromicity mod 9 per core;  
5. telescoping identity for \(\delta f\);  
6. \(\beta_\sharp\) fiber table on core 0;  
7. fiber-linking closed form §10;  
8. same-tower incidence spectrum §11;  
9. 2-cochain identities §12;  
10. provenance flags in JSON output.

---

## 9. Bottom line

> On the locked residual carrier, the nine cores carry the integer pairing  
> \[
> \mathrm{Lk}\bigl(\mathcal{O}_{\mathrm{res}}^{(a)},\mathcal{O}_{\mathrm{res}}^{(b)}\bigr)=B'\,\mathrm{sgn}(a-b),
> \]  
> a clean **RNT** structure scaled by residual cardinality.  
> Tower coboundaries and flat mod-9 cochains supply **discrete torsion-style** data without continuum geometry.  
> Fiber linking, same-tower incidence algebra, and charge 2-cochains (§10–12) complete the next layer of dir.\ 1.  
> This is the recommended primary pattern substrate for later Category B TTC/RTTC enrichment.

---

## 10. Fiber-linking closed forms

On a single sorted core \(\mathcal{O}_{\mathrm{res}}=\{x_0<\cdots<x_{B'-1}\}\) set
\[
F_k=\{x_i:i\equiv k\pmod 8\},\qquad n_k=\lvert F_k\rvert.
\]
Canonical sizes: \(n_k=68\) for \(k\in\{0,1,2\}\) and \(n_k=67\) for \(k\in\{3,4,5,6,7\}\).

Because ambient order coincides with index order on a sorted core, \(\mathrm{Lk}(F_k,F_m)\) equals the line linking of the index progressions \(\{k,k+8,\ldots\}\) and \(\{m,m+8,\ldots\}\).

**Theorem (Fiber linking).**  
For \(k,m\in\{0,\ldots,7\}\),
\[
\mathrm{Lk}(F_k,F_m)
=
\begin{cases}
n_k\,\mathrm{sgn}(k-m) & \text{if }n_k=n_m,\\[4pt]
0 & \text{if }n_k\neq n_m.
\end{cases}
\]
Equivalently, with blocks
\[
U=\{0,1,2\}\ (n=68),\qquad V=\{3,4,5,6,7\}\ (n=67):
\]
- within \(U\): \(M|_{U\times U}=68\,S_U\) (sign matrix on 3 letters);  
- within \(V\): \(M|_{V\times V}=67\,S_V\) (sign matrix on 5 letters);  
- cross terms \(U\leftrightarrow V\): **identically zero**.

**Proof sketch.**  
Index arithmetic progressions with common difference 8. For equal cardinalities \(n_k=n_m=n\) and \(k<m\), the sign count reduces to \(N_{j>i}-N_{j=i}-N_{j<i}=-n\). For \((n_k,n_m)=(68,67)\), the same count cancels to \(0\). Full \(8\times 8\) matrix verified by probe.

**RNT reading.** Bott grading splits the core into two rigid linking blocks scaled by fiber size, with **no** cross-linking between the size-68 and size-67 grades — compatible with \(B'=8\cdot67+3=5\cdot67+3\cdot68\).

---

## 11. Same-tower incidence algebra

**Definition.** On core indices \(\{0,\ldots,B'-1\}\),
\[
Z_{ij}
=
\begin{cases}
1 & \tau(x_i)=\tau(x_j),\\
0 & \text{otherwise},
\end{cases}
\qquad
A=Z-I
\]
(\(Z\): same-tower reflexive incidence; \(A\): adjacency of the disjoint union of cliques, one per tower).

**Partition type (canonical core 0, verified).**  
Tower fibers on the core have size multiset
\[
\{\,1^{1},\;2^{185},\;3^{56}\,\}
\]
(242 towers touched; \(1\cdot1+2\cdot185+3\cdot56=539=B'\)).  
Edges in \(A\): \(N_{\mathrm{pair}}=353\).

**Proposition (Spectrum of \(A\)).**  
\(A\) is block-diagonal with one clique block per tower fiber of size \(n\):
- eigenvalue \(n-1\) with multiplicity 1;  
- eigenvalue \(-1\) with multiplicity \(n-1\).  

Hence the multiset of eigenvalues of \(A\) on the canonical core is
\[
\{\,2^{56},\;1^{185},\;0^{1},\;(-1)^{297}\,\}.
\]
Trace zero; \(\mathrm{rk}(Z)=\#\{\text{towers touched}\}=242\).

**Incidence algebra.**  
\(Z\) is the zeta matrix of the discrete partition of the core by \(\tau\). It is a projector up to scaling on each block (\(Z|_{B_t}=J_{n_t}\), the all-ones matrix). The Möbius matrix of that partition is block-diagonal with
\[
\mu|_{B_t}=I-\frac{1}{n_t}J
\quad(n_t\ge 1)
\]
on non-singleton blocks (standard partition lattice on a flat partition into cliques).

**RNT reading.** Same-tower structure is a partition incidence algebra scaled by democratic tower loads restricted to residual quanta — pure discrete residual data.

---

## 12. Discrete 2-cochains on charge triples

Charge sectors \(\{0,\ldots,8\}\) form the complete complex \(K_9\).  
Recall \(\alpha(a,b)=\mathrm{sgn}(a-b)\) and \(L_{ab}=B'\alpha(a,b)\).

### 12.1 Exact 2-cochain \(\omega_2=d\alpha\)

**Definition.**
\[
\omega_2(a,b,c)
:=
\alpha(b,c)-\alpha(a,c)+\alpha(a,b)
=
\mathrm{sgn}(b-c)-\mathrm{sgn}(a-c)+\mathrm{sgn}(a-b).
\]
Scaled form: \(\Omega_2=B'\omega_2\).

**Proposition.**  
\(\omega_2=d\alpha\) is an **exact** simplicial 2-cochain on \(K_9\), hence a **cocycle**: \(d\omega_2=0\) on every 4-tuple.  
For every ordered triple \(a<b<c\), \(\omega_2(a,b,c)=-1\) (verified on all \(\binom{9}{3}=84\) triples).

**Interpretation.** Discrete torsion-style curvature of the sign 1-form on residual charge sectors — **exact** (pure gauge of the ordered sector coordinate), matching the “exact tower coboundary” theme of §4.1.

### 12.2 Massey-style product cochain \(\mu\)

**Definition.**
\[
\mu(a,b,c)
:=
B'\,\mathrm{sgn}(a-b)\,\mathrm{sgn}(b-c)
=
\frac{L_{ab}\,L_{bc}}{B'}.
\]

**Proposition.**  
For all ordered 4-sets \(0\le a<b<c<d\le 8\),
\[
(d\mu)(a,b,c,d)
=
\mu(b,c,d)-\mu(a,c,d)+\mu(a,b,d)-\mu(a,b,c)
=
0
\]
(126/126 vanishing in probe). Thus \(\mu\) is a **2-cocycle** on the ordered charge complex in this discrete model.

**Proposition.**  
For \(a<b<c\), \(\mathrm{sgn}(a-b)\mathrm{sgn}(b-c)\mathrm{sgn}(c-a)=+1\) (triple sign product always \(+1\) on ordered triples).

**RNT reading.** Products of core linkings renormalized by \(B'\) yield integer 2-cochains with vanishing coboundary on charge 4-simplices — a discrete Massey-type pattern scaled by residual cardinality.

---

## 13. Extended status (dir.\ 1)

| Target | Status |
|--------|--------|
| Core linking \(L=B'S\) | **Theorem** (§2) |
| Fiber linking closed form | **Theorem** (§10) |
| Same-tower incidence spectrum | **Proposition** (§11) |
| Exact \(\omega_2=d\alpha\); cocycle \(\mu\) | **Proposition** (§12) |
| Continuum torsion / hopfion claims | Still Cat.\ B, out of scope |
