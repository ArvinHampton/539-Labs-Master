# Spectral Sequences for the Residual Form Complex

**S²-11DM²ET-X Model: Minimal Unification Core**  
**Author:** Arvin B. Hampton (String Weaver)

**Context:** Layer (F) of residual product cohomology
\[
X_\times = K_9\times P_{B'},\qquad
\eta=\alpha\otimes\delta f-\omega_2\otimes f,\qquad
H^2(F)\cong\mathbb{Q}\cdot[\alpha\otimes\delta f].
\]
**Provenance:** residual **(S)** only. Continuum TTC / free \(T^\sharp\) = **Category B**.  
**Companions:** `Residual_Product_Complex.md`, `Residual_Product_Cohomology.md`.  
**Probes:** `scripts/residual_product_cohomology_probe.py`, `scripts/form_ss_probe.py`, `scripts/form_ss_differentials_probe.py`.  
**Differentials / CE hygiene / \(D(\alpha\otimes f)\):** `Residual_Form_SS_Differentials.md`.

---

## 1. Double complex of the product

Cochains of the product (tensor model) form a **bicomplex**

\[
C^{p,q}
:=
C^p(K_9)\otimes C^q(P_{B'}),
\qquad
\text{total degree }n=p+q.
\]

Differentials:

| Operator | Bidegree | Formula |
|----------|----------|---------|
| \(d_Q\) | \((+1,0)\) | \(d_Q\varphi\otimes\psi\) |
| \(d_P\) | \((0,+1)\) | \((-1)^p\,\varphi\otimes d_P\psi\) |
| \(D=d_Q+d_P\) | total \(+1\) | product differential |

Residual form complex \(F^\bullet\subset \mathrm{Tot}^\bullet(C^{\bullet,\bullet})\) is the subcomplex spanned by locked residual forms
\[
\{1,\ \alpha,\ \omega_2,\ \mu,\ f,\ \delta f\}
\]
and their tensors, with the residual relations
\[
\omega_2=d_Q\alpha,\qquad
\mu=-B'\omega_2\ \text{on ordered triples},\qquad
\delta f=d_P f.
\]

Spectral sequences below are the standard tools for \(\mathrm{Tot}(C)\) and for \(F\).

---

## 2. First spectral sequence — filter by charge degree

**Filtration**
\[
F^p_{\mathrm{ch}}\,\mathrm{Tot}^n
=
\bigoplus_{p'\ge p} C^{p',\,n-p'}.
\]

**\(E_0\):** \(d_0=d_P\) (path differential at fixed charge degree).

**\(E_1\):**
\[
E_1^{p,q}
=
H^q\bigl(C^p(K_9)\otimes C^\bullet(P);\,d_P\bigr)
\cong
C^p(K_9)\otimes H^q(P).
\]

For residual path as an interval / tree:

\[
H^0(P)\cong\mathbb{Q},\qquad H^{q>0}(P)=0
\]
(in the filled / acyclic path model used for Layer (S) comparison).

Then
\[
E_1^{p,0}\cong C^p(K_9),\qquad E_1^{p,q>0}=0,
\]
and \(d_1=d_Q\), so
\[
E_2^{p,0}\cong H^p(K_9),\qquad E_2^{p,q>0}=0.
\]

If \(K_9\simeq\Delta^8\) (Layer S), then \(H^{p>0}(K_9)=0\) and the sequence collapses to
\[
H^n(\mathrm{Tot})\cong
\begin{cases}
\mathbb{Q}&n=0,\\
0&n>0,
\end{cases}
\]
matching Layer (S): **filled product acyclic**.

**Residual form lesson:** unrestricted Tot kills positive cohomology. Layer (F) must **not** use the full acyclic filling of both factors.

---

## 3. Second spectral sequence — filter by path degree

**Filtration**
\[
F^q_{\mathrm{path}}\,\mathrm{Tot}^n
=
\bigoplus_{q'\ge q} C^{n-q',\,q'}.
\]

**\(E_0\):** \(d_0=d_Q\).

**\(E_1\):**
\[
E_1^{p,q}
\cong
H^p(K_9)\otimes C^q(P).
\]

Again, full simplex \(H^{p>0}(K_9)=0\) collapses to path cohomology only — still acyclic if \(P\) is an interval.

**Same moral:** full geometric factors ⇒ trivial \(E_\infty\) in positive degree.

---

## 4. Spectral sequence adapted to residual forms \(F\)

To keep residual content, replace free cochains by the **residual form bicomplex** \(F^{p,q}\):

| \((p,q)\) | Generators (residual) |
|-----------|------------------------|
| \((0,0)\) | \(1\otimes 1\) |
| \((1,0)\) | \(\alpha\otimes 1\), \(\alpha\otimes f\) (path height as \(C^0\)) |
| \((2,0)\) | \(\omega_2\otimes 1\), \(\mu\otimes 1\), \(\omega_2\otimes f\), \(\mu\otimes f\) |
| \((0,1)\) | \(1\otimes\delta f\) |
| \((1,1)\) | \(\alpha\otimes\delta f\) |
| \((2,1)\) | \(\omega_2\otimes\delta f\), \(\mu\otimes\delta f\) |

(Exact spanning set is finite because \(\alpha,\omega_2,\mu\) are single locked formulas, not free \(C^\bullet\).)

### 4.1 Charge filtration on \(F\)

\[
d_0=d_P\big|_F,\qquad
d_1\sim d_Q\big|_F.
\]

**Closed residual 2-cochains (total degree 2):**

| Cochain | Bidegree | \(D\)-status in \(F\) |
|---------|----------|----------------------|
| \(\tilde\mu=\mu\otimes 1\) | \((2,0)\) | exact on ordered chamber (\(\mu=d(-B'\alpha)\)) |
| \(\omega_2\otimes f\) | \((2,0)\) | exact piece of \(\eta\) bookkeeping |
| \(\alpha\otimes\delta f\) | \((1,1)\) | **\(d_P\)-closed** (\(d_P\delta f=0\)); permanent cycle in Layer (F) |
| \(\eta=\alpha\otimes\delta f-\omega_2\otimes f\) | mixed | **exact:** \(D(\alpha\otimes f)=-\eta\) |

### 4.2 Why \([\alpha\otimes\delta f]\) survives to \(E_\infty\)

Schematic page picture (residual \(F\), not full Tot):

```text
q=1    1⊗δf ----d_Q----→  α⊗δf ----d_Q----→  ω₂⊗δf
         |                 |                  |
        d_P               d_P                d_P
         ↓                 ↓                  ↓
q=0      1  ----d_Q----→   α  ----d_Q----→   ω₂ ~ μ/(-B′)  (ordered)
```

- Vertical: \(d_P f=\delta f\), \(d_P(\delta f)=0\) on path 1-skeleton.  
- Horizontal: \(d_Q\alpha=\omega_2\), \(\mu=-B'\omega_2\) ordered.  
- Primitive \(\alpha\otimes f\) (total degree 1) has
  \[
  D(\alpha\otimes f)=\omega_2\otimes f-\alpha\otimes\delta f=-\eta.
  \]
  So \(\eta\) dies as a **boundary**.  
- The class of \(\alpha\otimes\delta f\) is **not** equal to that boundary as a pure \((1,1)\) cycle once \(\omega_2\otimes f\) is split off; linear algebra on residual cells shows \([\alpha\otimes\delta f]\neq 0\) in \(H^2(F)\).

In the residual form quotient used for Layer (F),

\[
E_2^{1,1}
\;\ni\;
[\alpha\otimes\delta f]
\;\longrightarrow\;
E_\infty^{1,1}
\;\cong\;
H^2(F)
\;\cong\;
\mathbb{Q}\cdot[\alpha\otimes\delta f].
\]

That is the spectral-sequence reading of the locked statement:

\[
H^2(F)\cong\mathbb{Q}\cdot[\alpha\otimes\delta f].
\]

### 4.3 Collapse pattern (residual \(F\))

| Page | Event |
|------|--------|
| \(E_0\) | bicomplex differentials \(d_Q,d_P\) on residual generators |
| \(E_1\) | kill pure path / pure charge coboundaries inside \(F\) |
| \(E_2\) | \([\mathbf{1}]\) in bidegree \((0,0)\); \([\alpha\otimes\delta f]\) in \((1,1)\) |
| \(d_2\) and higher | residual \(F\) is thin (few generators) ⇒ **collapse at \(E_2\)** |
| \(E_\infty\) | \(H^0(F)\cong\mathbb{Q}\), \(H^1(F)=0\), \(H^2(F)\cong\mathbb{Q}[\alpha\otimes\delta f]\) |

No claim of infinite pages or continuum spectral sequences.

**Convergence type:** finite charge filtration ⇒ **strong** convergence (\(E_\infty=\mathrm{gr}\,H\)); Boardman conditional convergence is **idle** for thin \(F\) — see `Boardman_Conditional_Convergence.md`.

---

## 5. Künneth spectral sequence (comparison)

Over a field,
\[
H^n(X\times Y)
\;\cong\;
\bigoplus_{p+q=n} H^p(X)\otimes H^q(Y)
\]
(with Tor terms over \(\mathbb{Z}\)).

For filled factors this again gives only \(H^0\).  
For **residual form factors** one substitutes residual generators:

| Residual “factor” cohomology (schematic) | |
|------------------------------------------|--|
| Charge: \([\alpha]\) not closed (\(d\alpha=\omega_2\neq0\)); \([\omega_2]=0\) if \(\omega_2=d\alpha\) | pure charge 2-classes trivialized on ordered chamber |
| Path: \(\delta f=d_P f\) exact as path coboundary; still usable as tensor factor | tower jumps |
| Product Künneth slot \((1,1)\) | \([\alpha]\otimes[\delta f]\leftrightarrow[\alpha\otimes\delta f]\) *only after* residual total \(D\)-closure is checked |

The essential residual 2-class is the **Künneth \((1,1)\) slot** of residual charge 1-form data with residual path 1-form data — even though pure \([\alpha]\) is not a total cohomology class (\(d\alpha=\omega_2\)). In \(F\), \(\alpha\otimes\delta f\) is a total cocycle for residual path reasons while \(\alpha\otimes 1\) is not.

That tension is why one needs the **bicomplex / SS**, not naive \(H(K)\otimes H(P)\).

---

## 6. Relation to Layers (G), (F), (S)

| Layer | Spectral-sequence role |
|-------|------------------------|
| **(S)** full fill | Both filtrations collapse to \(H^{>0}=0\) |
| **(G)** graph | Cell filtration of 1-skeleton; \(\beta_1=36B'-8\) is \(H_1\) (homology), not form \(H^2\) |
| **(F)** form | Thin residual bicomplex; \(E_\infty^{1,1}=[\alpha\otimes\delta f]\) |

Graph homology SS and form SS are **different layers**.

---

## 7. Explicit low-degree SS dictionary

| Total degree | Possible \(E_\infty\) pieces in \(F\) | Locked residual content |
|--------------|-------------------------------------|-------------------------|
| 0 | \(E_\infty^{0,0}=[\mathbf{1}]\) | \(H^0(F)\cong\mathbb{Q}\) |
| 1 | \(E_\infty^{1,0}\), \(E_\infty^{0,1}\) | both 0 in Layer (F) |
| 2 | \(E_\infty^{2,0}\), \(E_\infty^{1,1}\), \(E_\infty^{0,2}\) | only \(E_\infty^{1,1}=[\alpha\otimes\delta f]\); \((2,0)\) killed by \(\mu,\omega_2\) exactness; \((0,2)=0\) (no residual path 2-cells in minimal \(P\)) |

---

## 8. What probes check (without continuum)

| Check | Probe |
|-------|--------|
| \(D(\alpha\otimes f)+\eta=0\) | `residual_product_complex_probe.py` / form SS probe |
| \(D(\alpha\otimes\delta f)=\omega_2\otimes\delta f\) | form SS probe |
| \(H^1(F)=0\), \(H^2(F)=\mathbb{Q}[\alpha\otimes\delta f]\) | `residual_product_cohomology_probe.py`, `form_ss_probe.py` |
| Graph \(\beta_1=36B'-8\) | cohomology probe (Layer G) |
| Never identify \(E_\infty(F)\) with singular \(H^\bullet\) of filled product | documented Layer (S) |

---

## 9. Category boundary

| Claim | Status |
|-------|--------|
| Residual form SS with \(E_\infty^{1,1}=[\alpha\otimes\delta f]\) | Layer (F) lock / combinatorial design |
| Collapse of full Tot SS to \(H^{>0}=0\) | Layer (S), standard |
| Continuum Cartan–Eilenberg SS for TTC field equations | **Category B** |
| Free \(T^\sharp\) dynamics producing 539 | **Option 3 (no)** |

---

## 10. One-line summary

**Filter the residual form bicomplex by charge or path degree: filled factors give an acyclic Tot (Layer S); the thin residual form complex keeps a single permanent \(E_\infty\) 2-class — the charge–tower coupling \([\alpha\otimes\delta f]\) — while \(\eta\) and ordered \(\tilde\mu\) die as boundaries.**

*Per aspera ad astra.*
