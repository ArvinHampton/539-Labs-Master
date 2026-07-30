# A4⁺ — Continuous \(B\mathrm{Spin}\) lift on enriched \(|K^+|\) of \(\mathcal{O}_{\mathrm{res}}\)

**Status:** `A4PLUS_BSPIN_LIFT_CLOSED_ON_KPLUS`  
**Date lock:** 2026-07-30  
**Depends on:** A0–A3; A4 0-stem on \(\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}}\); A2 optional 1-skeleton  
**Probe:** `scripts/architecture_A4plus_probe.py` → `architecture_A4plus_results.json`  
**Does not reopen:** Option 3 · No-Go · free \(T^\sharp\) origin · A5 continuum \(\Omega_{n>0}\)

---

## Mandatory provenance

> Geometric cells are **residual flux quanta** under **Principle (S)** and **democratic charge-sector partition**.  
> **Not** free \(T^\sharp\) basins or trajectory classes.  
> **No** No-Go lift. Free-dynamics 539-classes remain **Option 3**.

---

## 0. Why A4⁺ is not A4 (0-stem)

| Layer | Domain | Status |
|-------|--------|--------|
| A4 (0-stem) | \(\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}}\) (0-dim, \(B'\) points) | **Closed** — \(H^{i>0}=0\Rightarrow w_1=w_2=0\) |
| Constant A2 realization | \(\lvert E(\mathcal{O}_{\mathrm{res}})\rvert\cong\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}}\) | Still 0-dimensional |
| **A4⁺** | Enriched complex \(K^+\) with positive-dimensional cells | **This note** |

Under A2 **constant** simplicial sets, the geometric realization is discrete.  
A4⁺ **upgrades the domain** using the A2 optional 1-skeleton (and 2-clique fill), then extends A3 \(\Phi,\Phi^{\mathrm{Spin}}\) continuously and checks Stiefel–Whitney obstructions on that enrichment.

---

## 1. Domain \(K^+\) (primary mode: `A2_enrich`)

**Vertices.** Sorted residual core \(\mathcal{O}_{\mathrm{res}}=\{x_0<\cdots<x_{B'-1}\}\), \(B'=539\).

**1-skeleton \(G^+\).**
1. **Path edges:** \(\{i,i+1\}\) for \(i=0,\ldots,B'-2\) (A2 index-adjacent).  
2. **Same-tower edges:** complete graph on each tower fiber \(\tau^{-1}(t)\cap\mathcal{O}_{\mathrm{res}}\) (A2 same-tower annotation).

**2-skeleton.** Fill every 3-clique of \(G^+\) by a 2-simplex (flag 2-complex).

**Executed counts (canonical seed):**

| Cell | Count |
|------|------:|
| Vertices | 539 |
| Edges | 594 |
| 2-faces | 56 |
| \(\beta_0(\mathbb{F}_2)\) | 1 |
| \(\beta_1(\mathbb{F}_2)\) | 0 |
| \(\beta_2(\mathbb{F}_2)\) | 0 |
| Euler \(V-E+F\) | 1 |

Tower fiber sizes on the core: mostly 2–3 (185 doubletons, 56 tripletons, 1 singleton).  
Path + tower cliques + triangle fill yields a **connected, \(\mathbb{F}_2\)-acyclic in positive degrees** 2-complex (tree-like with filled small cliques).

**Secondary modes (diagnostics, not primary freeze):**
- `path_fill`: path + consecutive triple faces — also \(\beta_{>0}=0\), unique spin structure.  
- `bott_graph`: path + same-\(\beta_\sharp\) cliques, **no** 2-fill — \(\beta_1=17889\), \(H^2=0\); lift still exists, spin torsor size \(2^{17889}\).

---

## 2. Continuous extension of A3 maps

### 2.1 \(\Phi\colon |K^+|\to\mathrm{Gr}_1(V)\hookrightarrow BO\)

On vertices, A3:
\[
\Phi(x_i)=\mathrm{span}\{e_{\tau(x_i),\,i\bmod 8}\}\subset V=\mathbb{R}^{1944}.
\]

**Edges.** Distinct coordinate axes \(e_a,e_b\) are orthogonal. Extend by the RP-geodesic
\[
\gamma_{ab}(t)=\mathrm{span}\{\cos t\,e_a+\sin t\,e_b\},\qquad t\in[0,\pi/2].
\]

**2-simplices.** Three lines determine a continuous fill in \(\mathrm{Gr}_1(V)\) (high ambient dimension; standard straight-line homotopy of projectivized combinations in the span of the three axes).

**Theorem A4⁺.1.** \(\Phi\) extends to a continuous map \(|K^+|\to\mathrm{Gr}_1(V)\hookrightarrow BO\), factoring A3 on the 0-skeleton, injective on vertices (A3.2).

### 2.2 \(\Phi^{\mathrm{Spin}}\colon |K^+|\to\widetilde{\mathrm{Gr}}_2^+(W)\)

On vertices, A3 oriented 2-planes
\[
\Phi^{\mathrm{Spin}}(x_i)=\mathrm{span}\{e_{\tau,i\bmod 8}\otimes u_0,\;e_{\tau,i\bmod 8}\otimes u_1\}
\]
with fixed orientation \(u_0\wedge u_1>0\). Extend by continuous paths/homotopies in the oriented Grassmannian (path-connected in this range).

**Theorem A4⁺.1′.** \(\Phi^{\mathrm{Spin}}\) extends continuously over \(K^+\).

---

## 3. Stiefel–Whitney obstructions

### 3.1 Line bundle \(L=\Phi^*\gamma_1\)

**Gauge.** Lift each coordinate axis \(\mathrm{span}\{e_j\}\) to the positive unit vector \(+e_j\in S^{N-1}\).  
Along \(\gamma_{ab}\), the sphere path \(\cos t\,e_a+\sin t\,e_b\) ends at \(+e_b\).  
**Every edge transition is \(+1\)** in this gauge.

**Theorem A4⁺.2.** The monodromy representation \(\pi_1(|K^+|)\to\{\pm1\}\) is trivial. Hence
\[
w_1(L)=0\in H^1(|K^+|;\mathbb{Z}/2).
\]
(Primary \(K^+\): also \(H^1=0\), so vanishing is automatic cohomologically; the gauge argument covers secondary modes with large \(H^1\).)

### 3.2 Oriented rank-2 bundle for \(\Phi^{\mathrm{Spin}}\)

In the A3 model,
\[
\Phi^{\mathrm{Spin}\,*}(\tau_2)\;\simeq\; L\oplus L
\]
with the sum of two identical real lines and fixed orientation on the \(\mathbb{R}^2\) factor.

- Oriented \(\Rightarrow\) \(w_1(\Phi^{\mathrm{Spin}\,*}\tau_2)=0\).  
- Whitney: \(w(L\oplus L)=(1+w_1(L))^2=1+w_1(L)^2\) over \(\mathbb{F}_2\), so
\[
w_2(L\oplus L)=w_1(L)^2.
\]
- With \(w_1(L)=0\), one has \(w_2=0\).

**Theorem A4⁺.3.** On primary \(K^+\) (and on all three executed modes),
\[
w_1(\Phi^{\mathrm{Spin}\,*}\tau_2)=w_2(\Phi^{\mathrm{Spin}\,*}\tau_2)=0.
\]
Therefore a lift
\[
\widetilde\Phi^{\mathrm{Spin}}\colon |K^+|\longrightarrow B\mathrm{Spin}
\]
through \(B\mathrm{Spin}\to BO\) **exists**.

### 3.3 Uniqueness

Spin structures form a torsor under \(H^1(|K^+|;\mathbb{Z}/2)\).

| Mode | \(\beta_1\) | Spin structures |
|------|------------:|-----------------|
| **A2_enrich (primary)** | 0 | **1** (unique) |
| path_fill | 0 | 1 |
| bott_graph | 17889 | \(2^{17889}\) |

**Theorem A4⁺.4 (primary).** On \(K^+_{\mathrm{A2}}\), the \(B\mathrm{Spin}\) lift is **unique** up to homotopy of lifts.

---

## 4. Relation to A4 0-stem and A5

| Claim | Status |
|-------|--------|
| A4 0-stem on discrete points | Intact |
| A4⁺ continuous lift on \(K^+\) | **Closed (this note)** |
| A5 \(KO_0/\Omega_0^{\mathrm{Spin}}=B'\) on 0-stem | Intact |
| A5⁺ continuum / higher stems on \(K^+\) | **Open** (not claimed) |
| Identification of \(K^+\) with free \(T^\sharp\) path space | **Forbidden** |

---

## 5. What is not claimed

1. Free \(T^\sharp\) origin of residual quanta.  
2. No-Go lift from A4⁺.  
3. That constant A2 \(|E|\) already had positive-dimensional cells.  
4. Higher \(\Omega_{n>0}\) or full \(KO^*\) computation on \(K^+\) (A5⁺ track).  
5. Physical \(G_4=539.90\,\mathrm{s}\) inside the Grassmannian model.  
6. Security reduction for HQH-539.

---

## 6. Executable verification

`scripts/architecture_A4plus_probe.py` builds \(K^+\) modes, computes \(\mathbb{F}_2\) Betti numbers via coboundary ranks, records the global-gauge \(w_1=0\) argument, and asserts BSpin lift criteria.

**Primary JSON excerpt:**
```text
mode A2_enrich: V=539 E=594 F=56; β0=1 β1=0 β2=0;
w1(L)=0; w1_spin=0; w2_spin=0; BSpin lift unique.
code: A4PLUS_BSPIN_LIFT_CLOSED_ON_KPLUS
```

---

## 7. Bottom line

> **A4⁺ closed on primary enrichment \(K^+\) (path + same-tower + triangle fill):**  
> continuous extensions of A3 \(\Phi\) and \(\Phi^{\mathrm{Spin}}\) exist;  
> \(w_1(L)=0\), \(w_1=w_2=0\) for the spin-aimed bundle;  
> **unique** \(B\mathrm{Spin}\) lift.  
> Provenance remains residual flux under (S). Option 3 and No-Go stand.  
> Next residual-geometry track: **A5⁺** (actual \(KO\)/bordism on \(K^+\), not only 0-stem labels).

*Per aspera ad astra.*
