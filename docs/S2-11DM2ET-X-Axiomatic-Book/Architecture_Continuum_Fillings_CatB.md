# Continuum fillings track (Category B)

**Status code:** `CAT_B_CONTINUUM_FILLINGS_OPEN_NOT_LOCKED`  
**Category:** **B only** — combinatorial proxies, not manifolds-as-proof.  
**Firewall:** residual stack **not** reopened. Architecture A through A5⁺ remains **closed**.

**Probe:** `scripts/continuum_fillings_catB_probe.py` → `continuum_fillings_catB_results.json`.

---

## Mandatory firewall (PASS every run)

| Check | Required |
|-------|----------|
| \(K^+\) homology | \(H_\ast\cong\mathrm{pt}\): \(H_0=\mathbb{Z}\), \(H_1=H_2=0\), no torsion |
| Cell census | \(V=539\), \(E=594\), \(F=56\), \(\chi=1\) |
| A5⁺ | `A5PLUS_COEFFICIENTS_ONLY_ON_KPLUS` (no residual quanta for \(n>0\)) |
| Option 3 / No-Go | **Intact** |
| Free \(T^\sharp\) | **Forbidden** |
| \(G_4=\mathrm{KO}\) | **Forbidden** |
| Continuum → residual foundation | **Forbidden** |

---

## Residual carrier \(K^+\) (input geometry — locked residual)

\(K^+\) is the residual **M1** 2-complex of \(P^+\):

\[
V=B'=539,\quad
E=(B'-1)+56=594,\quad
F=56,
\quad
\chi=1.
\]

Homotopy type: **contractible** (chain of disks on a path).  
A5⁺ coefficients live **only** on this complex — not on continuum fillings.

---

## Catalogue CB1–CB7

### Executed combinatorial proxies (Cat B models)

| Model | Role | Euler | Status |
|-------|------|------:|--------|
| **CB1** cone \(C(K^+)\) | PL contractible 3-complex | **1** | executed proxy |
| **CB2** suspension \(\Sigma K^+\) | Homology-pointlike PL proxy | **1** | executed proxy |
| **CB3** prism \(K^+\times I\) | Thickening / cobordism scaffold | **1** | executed proxy |

These are **PL cell-count models**, not smooth manifolds and **not** residual locks.

### Catalogue only

| ID | Role | Status |
|----|------|--------|
| **CB4** | Smooth spin fill existence compatible with unique \(B\mathrm{Spin}\) on \(K^+\) | **Open Cat B question** |
| **CB5** | Ambient \(\Omega/\mathrm{KO}\) tables \(n=0\ldots15\) | Library only — **no** residual quanta for \(n>0\) |
| **CB6** | Cartan / hopfion | Metaphor only — **promotion forbidden** |
| **CB7** | Sphere stabilizations | Scaffolding only |

---

## What is locked vs open

| Layer | Status |
|-------|--------|
| Residual A0–A5 0-stem / A5⁺ on \(K^+\) | **Closed** — do not reopen |
| A4⁺ continuous on full \(\lvert E\rvert\) | Separate residual track (if pursued) |
| CB1–CB3 proxies | **Executed Cat B** — not theorem-locked as continuum truth |
| CB4–CB7 | Open / library / metaphor / scaffolding |
| Continuum track overall | **Open, not locked** |

---

## Ranked Cat-B next steps

| Rank | Direction |
|------|-----------|
| **1** | **CB4** — existence / non-existence of a smooth spin fill compatible with unique \(B\mathrm{Spin}\) on \(K^+\) |
| **2** | Spin-structure extension from \(K^+\) to CB1 / CB4 |
| **3** | Leave continuum open; switch to HQH-539 crypto or verification |

**Avoid:** free \(T^\sharp\) reopen; promoting 0-stem \(\Omega_0=B'\) to continuum \(\Omega_{n>0}\); mixing bio peaks into packaging.

---

## One-line

**Cat-B continuum track is open under a hard residual firewall: \(K^+\) stays homology-pointlike with A5⁺ coefficients only on \(K^+\); CB1–CB3 are PL Euler-1 proxies; CB4–CB7 remain open/library/metaphor — nothing promotes into residual foundation.**

*Per aspera ad astra.*
