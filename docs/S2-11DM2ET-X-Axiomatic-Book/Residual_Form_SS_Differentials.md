# Differentials in the Residual Form SS · Cartan–Eilenberg · Explicit \(D(\alpha\otimes f)\)

**S²-11DM²ET-X Model: Minimal Unification Core**  
**Author:** Arvin B. Hampton (String Weaver)

Three parts, in order. Residual provenance **(S)** only for locked claims. Continuum Cartan–Eilenberg / Einstein–Cartan field SS = **Category B**.

**Companions:** `Residual_Form_Spectral_Sequences.md`, `Residual_Product_Complex.md`, `Residual_Product_Cohomology.md`.  
**Probes:** `scripts/form_ss_probe.py`, `scripts/residual_product_complex_probe.py`, `scripts/form_ss_differentials_probe.py`.

---

## Part I — Differentials in the residual form spectral sequence

### 1.1 Bicomplex differentials (before pages)

On residual tensors \(\varphi\otimes\psi\in C^p(K_9)\otimes C^q(P)\):

\[
\begin{aligned}
d_Q(\varphi\otimes\psi)
&=
(d_Q\varphi)\otimes\psi
&&\text{bidegree }(+1,0),\\[4pt]
d_P(\varphi\otimes\psi)
&=
(-1)^p\,\varphi\otimes(d_P\psi)
&&\text{bidegree }(0,+1),\\[4pt]
D
&=
d_Q+d_P
&&\text{total degree }+1.
\end{aligned}
\]

Relations already locked:
\[
d_Q\alpha=\omega_2,\qquad
d_P f=\delta f,\qquad
d_P(\delta f)=0
\quad\text{(minimal path: no residual 2-cells)}.
\]

### 1.2 Spectral sequence pages (charge filtration)

Filter by charge degree \(p\). Then:

| Page | Differential | Bidegree on \(E_r^{p,q}\) | Residual meaning |
|------|--------------|---------------------------|------------------|
| \(E_0\) | \(d_0=d_P\) | \((0,+1)\) | tower/path coboundary at fixed charge |
| \(E_1\) | \(d_1=d_Q\) | \((+1,0)\) | charge coboundary on path-cohomology |
| \(E_r\) (\(r\ge 2\)) | \(d_r\) | \((r,1-r)\) | higher page maps (thin \(F\Rightarrow\) mostly zero) |

Path filtration swaps roles: \(d_0=d_Q\), \(d_1\sim d_P\).

### 1.3 Low-degree residual generators and which \(d_r\) kills them

```text
q=1     1⊗δf  --d1=dQ-->  α⊗δf  --d1-->  ω₂⊗δf
         |d0               |d0              |d0
q=0      1    --d1=dQ-->   α    --d1-->   ω₂  (μ = -B′ω₂ ordered)
                \_______ α⊗f (total deg 1; mixed height) _______/
                         D(α⊗f) = -η  (see Part III)
```

| Class / cochain | Killed by | Page / mechanism |
|-----------------|-----------|------------------|
| \(\delta f - d_P f\) | definition | \(E_0\): not a free generator |
| \(\omega_2 - d_Q\alpha\) | definition | \(E_0/E_1\) relation |
| ordered \(\mu+B'\omega_2\) | residual relation | form relation, not a free \(d_r\) |
| \(\eta=\alpha\otimes\delta f-\omega_2\otimes f\) | \(D(\alpha\otimes f)=-\eta\) | total \(D\) ⇒ dies before \(E_\infty\) (boundary) |
| pure \([\alpha]\) in \(H^1(K_9)\) | \(d_Q\alpha=\omega_2\neq 0\) | never a cocycle; no \(E_2^{1,0}\) from free \(\alpha\) |
| \([\alpha\otimes\delta f]\) | no residual \(d_r\) hits it in thin \(F\) | **permanent** \(E_\infty^{1,1}\) |

### 1.4 Collapse

Residual \(F\) has few bidegrees occupied. After \(d_0,d_1\) enforce \(\omega_2=d\alpha\), \(\delta f=d f\), and the primitive \(\alpha\otimes f\) kills \(\eta\), higher \(d_r\) (\(r\ge 2\)) have **no room** to act nontrivially on the remaining generator. Hence:

\[
E_2=E_\infty:
\quad
H^0(F)\cong\mathbb{Q}\cdot[\mathbf{1}],\ 
H^1(F)=0,\ 
H^2(F)\cong\mathbb{Q}\cdot[\alpha\otimes\delta f].
\]

### 1.5 Graph layer is a different SS

Layer (G) uses the **cell filtration** of the 1-skeleton (dimension), not the form bicomplex. Differentials there are graph boundary maps; they produce \(\beta_1=36B'-8\), **not** \(H^2(F)\). Do not identify \(d_r^{\mathrm{form}}\) with graph \(\partial\).

---

## Part II — Cartan–Eilenberg spectral sequences (and “Cartan–Einstein”)

### 2.1 Name hygiene

| Name | What it is | Status here |
|------|------------|-------------|
| **Cartan–Eilenberg SS** | Homological algebra: SS for \(\mathrm{Ext}/\mathrm{Tor}\), hypercohomology, filtered complexes (CE 1956) | Formal template for any bicomplex / filtered complex |
| **Cartan structure equations** | \(\Omega=d\omega+\omega\wedge\omega\), torsion \(\Theta=d\theta+\omega\wedge\theta\) | Continuum geometric; **Category B** if used as residual proof |
| **Einstein–Cartan gravity** | Gravity with torsion; spin ↔ torsion | Continuum field theory; **Category B** |
| “Cartan–Einstein spectral sequence” | **Not** a standard named SS in the literature | At best: CE-style SS applied to an Einstein–Cartan / torsion complex |

So: **Cartan–Eilenberg** = the algebraic machine. **Einstein–Cartan** = a continuum geometric theory one *might* feed into that machine. Residual lock does **not** require the second.

### 2.2 Cartan–Eilenberg machine (what we already use)

For a filtered complex \((K^\bullet,F^\bullet,d)\), CE gives \(E_r\Rightarrow H^\bullet(K)\).  
Our residual form SS **is** an instance:

- filtered object = residual form bicomplex \(F^{\bullet,\bullet}\)  
- \(d=D=d_Q+d_P\)  
- \(E_r\) as in Part I  

No new continuum structure is implied.

### 2.3 Hypothetical Einstein–Cartan / torsion SS (Category B only)

If one **designs** (not locks) a continuum complex with connection \(\omega\), coframe \(\theta\), torsion \(\Theta\), curvature \(\Omega\):

\[
\begin{aligned}
\Theta &= d\theta+\omega\wedge\theta,\\
\Omega &= d\omega+\omega\wedge\omega,
\end{aligned}
\]

a filtered CE SS might be built by form degree, by filtration “connection / coframe / curvature,” or by residual-vs-continuum. **Possible slogans** (all Category B):

| Slogan | Risk |
|--------|------|
| \(d_r\) “transmits” torsion between charge and tower | Metaphor unless a complex is defined |
| Identify \(\alpha\otimes\delta f\) with a torsion class in EC | **Overclaim** — residual discrete ≠ EC field |
| Recover 539 from EC SS | Blocked by Option 3 / No-Go for free dynamics |

**Programme stance:** residual \(E_\infty^{1,1}=[\alpha\otimes\delta f]\) is discrete and locked. Any Einstein–Cartan SS that “lifts” it is **design space**, not foundation.

### 2.4 Safe dictionary (residual ↔ continuum metaphor)

| Residual form SS | Continuum metaphor (Cat B) |
|------------------|----------------------------|
| \(\alpha\) | discrete “connection-like” 1-cochain on sectors |
| \(\omega_2=d\alpha\) | discrete curvature-like 2-cochain |
| \(\delta f\) | tower / path “displacement” |
| \(\alpha\otimes\delta f\) | mixed charge–tower coupling (torsion-flavoured) |
| \(\eta\) | exact “gauge” combination killed by primitive \(\alpha\otimes f\) |

Metaphor ≠ theorem.

---

## Part III — Explicit formula for \(D(\alpha\otimes f)\)

### 3.1 Degrees

\[
\alpha\in C^1(K_9),\qquad
f\in C^0(P_{B'}),\qquad
\alpha\otimes f\in C^{1,0}\subset \mathrm{Tot}^1.
\]

### 3.2 Definition of \(D\)

\[
D(\varphi\otimes\psi)
=
d_Q\varphi\otimes\psi
+
(-1)^{\deg\varphi}\,\varphi\otimes d_P\psi.
\]

### 3.3 Plug in \(\varphi=\alpha\), \(\psi=f\)

\[
\begin{aligned}
D(\alpha\otimes f)
&=
d_Q\alpha\otimes f
+
(-1)^{1}\,\alpha\otimes d_P f
\\[6pt]
&=
\omega_2\otimes f
-
\alpha\otimes\delta f
\\[6pt]
&=
-\bigl(\alpha\otimes\delta f-\omega_2\otimes f\bigr)
\\[6pt]
&=
-\eta.
\end{aligned}
\]

### 3.4 Evaluation form (cells)

On residual product cells:

| Cell | \(\langle D(\alpha\otimes f),\,\mathrm{cell}\rangle\) |
|------|--------------------------------------------------------|
| Triangle \(T(a,b,c;i)\) | \(\omega_2(a,b,c)\,f(i)\) |
| Square \(S(a,b;i)\) | \(-\alpha(a,b)\,\delta f(i)\) |

Compare \(\eta\):

| Cell | \(\langle\eta,\,\mathrm{cell}\rangle\) |
|------|----------------------------------------|
| Triangle \(T(a,b,c;i)\) | \(-\omega_2(a,b,c)\,f(i)\) |
| Square \(S(a,b;i)\) | \(\alpha(a,b)\,\delta f(i)\) |

Hence on every residual triangle and square:
\[
\boxed{
D(\alpha\otimes f)=-\eta
}
\]
as cochains, not only up to coboundaries.

### 3.5 Prism identity (consistency check)

On triangular prism \((a,b,c)\times e_i\), Stokes for \(D^2=0\) and the face formula reduce to
\[
\omega_2(a,b,c)\bigl(f(i)-f(i+1)\bigr)
+
\bigl(\alpha(a,b)+\alpha(b,c)+\alpha(c,a)\bigr)\delta f(i)
=0,
\]
using \(\delta f(i)=f(i+1)-f(i)\) and \(\sum_{\mathrm{cyc}}\alpha=\omega_2\). Verified in `residual_product_complex_probe.py` and `form_ss_differentials_probe.py`.

### 3.6 Consequence for the SS

\[
\eta=-D(\alpha\otimes f)
\quad\Rightarrow\quad
[\eta]=0\in H^2(F),
\]
while
\[
\alpha\otimes\delta f
=
\omega_2\otimes f+\eta
=
\omega_2\otimes f-D(\alpha\otimes f)
\]
shows \(\alpha\otimes\delta f\) and \(\omega_2\otimes f\) differ by a coboundary; in residual \(F\), after pure-charge exactness of \(\omega_2\otimes f\)-type terms is quotiented as in Layer (F), the **permanent** class is
\[
[\alpha\otimes\delta f]\in E_\infty^{1,1}\cong H^2(F).
\]

### 3.7 Compact reference card

\[
\begin{aligned}
D(\alpha\otimes f)
&=
\omega_2\otimes f-\alpha\otimes\delta f
=
-\eta,
\\[4pt]
\eta
&=
\alpha\otimes\delta f-\omega_2\otimes f,
\\[4pt]
d_Q\alpha&=\omega_2,
\quad
d_P f=\delta f,
\\[4pt]
\mu&=-B'\,\omega_2
\quad(a<b<c),
\\[4pt]
H^2(F)&\cong\mathbb{Q}\cdot[\alpha\otimes\delta f].
\end{aligned}
\]

---

## Stack placement

```text
Product complex          D, η, μ̃                 LOCKED
H^• (G)/(F)/(S)          β₁, [α⊗δf]              LOCKED
Form SS                  E∞^{1,1}=[α⊗δf]          LOCKED
SS differentials         d0=dP, d1=dQ, dr≥2~0    THIS NOTE
D(α⊗f)=−η                explicit                THIS NOTE
Cartan–Eilenberg machine formal template         OK as algebra
Einstein–Cartan field SS                         Category B only
```

---

## One-line close

**Residual form SS differentials are \(d_0=d_P\), \(d_1=d_Q\), higher \(d_r\) idle on thin \(F\); Cartan–Eilenberg is the algebraic name for that machine, while Einstein–Cartan lifts stay Category B; and the explicit formula is \(D(\alpha\otimes f)=\omega_2\otimes f-\alpha\otimes\delta f=-\eta\).**

*Per aspera ad astra.*
