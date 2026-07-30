# A4 — \(w_1,w_2\) and \(B\mathrm{Spin}\) lift on \(\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}}\)

**Programme phase:** A4 (**0-stem residual closure**).  
**Depends on:** A0–A3 (`Architecture_A3_Geometric_BO_BSpin.md`).  
**Domain (mandatory):** \(\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}}\) only — **0-dimensional** discrete residual carrier (\(B'\) points).  
**Status:** **Closed** as 0-stem residual closure — **not** continuum bordism, **not** full continuous A4 on \(|E(\mathcal{O}_{\mathrm{res}})|\).  
**Status code:** `A4_BSPIN_LIFT_CLOSED_ON_O_RES_DISC`  
**Open continuation:** **A4⁺** — \(w_1,w_2\) / \(B\mathrm{Spin}\) on full \(|E(\mathcal{O}_{\mathrm{res}})|\) (A2 cells beyond points).  
**Probe:** `scripts/architecture_A4_A5_probe.py` → `architecture_A4_A5_results.json`.

---

## Mandatory provenance

> Geometric 0-cells are **residual flux quanta** under **Principle (S)** and **democratic charge-sector partition**.  
> **Not** free \(T^\sharp\) basins. **No** No-Go lift. Option 3 intact.  
> **Domain:** \(\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}}\) / 0-stem only.  
> Cite: `Architecture_A_Ores_Programme.md` §0, A1–A3 notes.

---

## 0. Goal

Given the A3 maps
\[
\Phi
\colon
\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}}
\longrightarrow
\mathrm{Gr}_1(V)
\hookrightarrow
BO,
\qquad
\Phi^{\mathrm{Spin}}
\colon
\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}}
\longrightarrow
\widetilde{\mathrm{Gr}}_2^+(W)
\to
BSO
\subset
BO,
\]
decide the Stiefel–Whitney obstructions \(w_1,w_2\) and whether lifts through
\[
B\mathrm{Spin}
\longrightarrow
BSO
\longrightarrow
BO
\]
exist.

---

## 1. Domain cohomology (decisive)

**Lemma A4.1 (discrete domain).**  
The geometric realization \(\lvert E(\mathcal{O}_{\mathrm{res}})\rvert\cong\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}}\) is a **0-dimensional** CW complex with \(B'\) points.  
Hence for all \(i\ge 1\),
\[
H^i\bigl(\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}};\,\mathbb{Z}/2\bigr)
=
0.
\]

**Proof.**  
A discrete finite set is a disjoint union of points; reduced cohomology in positive degrees vanishes. ∎

---

## 2. Obstruction theory

The fibration \(B\mathrm{Spin}\to BO\) has fiber \(B(\ker(\mathrm{Spin}\to O))\); primary obstructions to lifting a map \(f\colon X\to BO\) live in cohomology of \(X\) with coefficients in the homotopy of the fiber (classically packaged by \(w_1,w_2\) for the associated bundle).

**Theorem A4.2 (vanishing of \(w_1,w_2\)).**  
For \(f\in\{\Phi,\,\Phi^{\mathrm{Spin}}\}\),
\[
f^*w_1
=
0
\in
H^1(\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}};\mathbb{Z}/2),
\qquad
f^*w_2
=
0
\in
H^2(\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}};\mathbb{Z}/2).
\]

**Proof.**  
Both groups vanish by Lemma A4.1.  
Additionally: real line bundles have \(w_2=0\) for rank reasons; \(\Phi^{\mathrm{Spin}}\) lands in oriented planes so \(w_1=0\) even before domain vanishing. ∎

**Theorem A4.3 (\(B\mathrm{Spin}\) lift).**  
There exist continuous lifts
\[
\widetilde\Phi,\;
\widetilde\Phi^{\mathrm{Spin}}
\colon
\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}}
\longrightarrow
B\mathrm{Spin}
\]
with
\[
B\mathrm{Spin}\to BO
\]
composing to \(\Phi\) and \(\Phi^{\mathrm{Spin}}\) (after the A3 inclusions).  
On a 0-dimensional domain, primary obstructions vanish, so such lifts exist; with vanishing higher cohomology they are unique up to homotopy of lifts.

**Corollary A4.4 (\(BSO\)).**  
\(\Phi^{\mathrm{Spin}}\) already factors through \(BSO\) by construction (oriented rank-2 planes); \(\Phi\) lifts through \(BSO\) because \(w_1=0\).

---

## 3. Geometric reading (pointwise)

Each residual quantum \(x_i\) contributes:

| Model | Fiber | Spin |
|-------|-------|------|
| \(\Phi(x_i)\) | line \(\mathrm{span}\{e_{\tau,\beta}\}\) | trivial spin structure on a 1D Euclidean space after stabilize/orient |
| \(\Phi^{\mathrm{Spin}}(x_i)\) | oriented 2-plane \(\cong\mathbb{C}\) | standard spin structure on \(\mathbb{R}^2\) |

There are \(B'\) pointwise spin structures, one per residual quantum — **not** free trajectory classes.

---

## 4. Stabilization

Choose \(N=\dim V=N_{\mathrm{tow}}\cdot 8=1944\) for the rank-1 model (A3).  
Stabilization \(\mathrm{Gr}_1(V)\hookrightarrow BO(N)\hookrightarrow BO\) does not create positive-degree cohomology on the discrete domain; Theorems A4.2–A4.3 remain.

---

## 5. What A4 does *not* claim

| Non-claim | |
|-----------|--|
| Lift theorem for continuous \(\Phi\colon|E(\mathcal{O}_{\mathrm{res}})|\to BO\) on positive-dim cells | **Open as A4⁺** |
| Spin structure on a continuum 4-manifold filling | **O / B** |
| Free \(T^\sharp\) paths are spin | **Forbidden** |
| Continuum \(w_2\) of EC/TTC bundles | **B** |
| Security reduction | **O** |
| Reopening A4 on the same 0-dim domain | **Forbidden** (already closed) |

---

## 6. Status

| Item | Tag |
|------|-----|
| \(H^{>0}(\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}};\mathbb{Z}/2)=0\) | **A** |
| \(w_1=w_2=0\) for \(\Phi,\Phi^{\mathrm{Spin}}\) on that domain | **A** |
| \(B\mathrm{Spin}\) lift on **0-skeleton** | **A** (closed A4) |
| Continuous A4 on full \(\lvert E(\mathcal{O}_{\mathrm{res}})\rvert\) | **Open A4⁺** |
| Continuum spin manifold theorems | **B** |

**Status code:** `A4_BSPIN_LIFT_CLOSED_ON_O_RES_DISC`  
**Domain line (freeze):** \(\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}}\) / 0-stem only.

---

## One-line

**On \(\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}}\) only, positive SW cohomology vanishes so \(\Phi,\Phi^{\mathrm{Spin}}\) lift through \(B\mathrm{Spin}\); this is 0-stem residual closure — A4⁺ on full \(|E|\) remains open; no continuum fillings or free \(T^\sharp\).**

*Per aspera ad astra.*
