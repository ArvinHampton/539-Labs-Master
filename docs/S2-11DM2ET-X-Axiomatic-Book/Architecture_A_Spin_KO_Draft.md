# Architecture A draft — Spin bordism \(\to KO\) \(\to\) Bott

**Status:** Category B. **Retargeted (2026-07)** to carrier \(\mathcal{O}_{\mathrm{res}}\).  
**Active programme:** `Architecture_A_Ores_Programme.md`.  
**Does not claim a completed continuous classifying map into \(B\mathrm{Spin}\).**

---

## Mandatory provenance

> Objects with cardinality 539 in this architecture are **residual flux quanta** in \(\mathcal{O}_{\mathrm{res}}\) (Principle (S) + democratic charge-sector partition).  
> **Not** free \(T^\sharp\) basins or trajectory homotopy classes.  
> **No** No-Go lift. Full block: `Architecture_A_Ores_Programme.md` §0.

Legacy trajectory-space sketches below are retained only as historical notes; **do not** use them as the 539-count source.

---

## 1. Classical interface (fixed)

\[
M\mathrm{Spin} \xrightarrow{\mathrm{ABS}} \mathrm{KO}
\]

Spin bordism classes map to real \(K\)-theory; Bott periodicity acts on \(\mathrm{KO}\).  
On the discrete carrier we first use a **Bott clock** \(\mathbb{Z}/8\) and a discrete product space; continuous \(B\mathrm{Spin}\) is Phase A4+.

---

## 2. Carrier and discrete background

\[
\lvert\mathcal{O}_{\mathrm{res}}\rvert
=
\Bigl\lfloor\frac{N_{\mathrm{flux}}-f_{\max}}{9}\Bigr\rfloor
=
539.
\]

\[
X_{\mathrm{disc}}
=
\mathbb{Z}/9
\times
\mathbb{Z}/N_{\mathrm{tow}}
\times
\mathbb{Z}/8.
\]

Continuous aspirational lift:
\[
X_4
=
B(\mathbb{Z}/9)
\times
B(\mathbb{Z}/N_{\mathrm{tow}})
\times
BO
\quad(B\mathrm{Spin}\text{ preferred when spin data exist}).
\]

| Factor | Role on residual flux quantum \(x\) |
|--------|--------------------------------------|
| \(\mathbb{Z}/9\) | Charge sector of the core / \(x\bmod 9\) (cores monochrome) |
| \(\mathbb{Z}/N_{\mathrm{tow}}\) | Democratic tower block \(\tau(x)\) |
| \(\mathbb{Z}/8\) | Bott degree \(\beta(x)=x\bmod 8\) |

**Deprecated as 539-source:** path packages \(\mathcal{C}_1,\mathcal{C}_2\) with free \(T^\sharp\) (basins \(=2\)).

---

## 3. Classifying map (discrete layer — executed)

\[
f(x)=\bigl(q(x),\,\tau(x),\,\beta(x)\bigr).
\]

**Verified** (`scripts/architecture_A_ores_probe.py`):

- \(f\) injective on canonical \(\mathcal{O}_{\mathrm{res}}\) via \((\tau,\beta)\) (539 distinct pairs).
- \(f\) injective on nine-core union (4851 distinct triples).
- Bott fibers \(\lvert F_k\rvert\in\{67,68\}\) with \(B'=8\cdot 67+3\).

---

## 4. Bott action / grading on the image

1. Grade \(\mathcal{O}_{\mathrm{res}}\) by \(\beta(x)\in\mathbb{Z}/8\).  
2. Record fiber cardinalities (discrete \(KO\)-proxy labels from the real Bott table — **labels only**).  
3. Arithmetic consistency:
   \[
   B' = 8\cdot\lfloor B'/8\rfloor + (B'\bmod 8) = 8\cdot 67 + 3.
   \]
4. **No free \(\mathbb{Z}/8\) action** on the set (\(8\nmid 539\)) — residual structure required.

**Forbidden:** defining the filtration by presupposing 539 trajectory classes and grouping them into 67 groups of 8 by hand.

---

## 5. Consistency with No-Go / ACE

| Statement | Architecture A stance |
|-----------|------------------------|
| \(N_\star=14\) short contraction | Intact; different type from \(\lvert\mathcal{O}_{\mathrm{res}}\rvert\) |
| \(\lambda=\ln 3/539\) | Still not derived from democracy; Bott on carrier does not create that Lipschitz constant |
| Free basins \(=2\) | Intact Category A |
| \(G_4=539.9\,\mathrm{s}\) | Not identified with \(K(\mathbb{Z},4)\) / \(BO\) degree without Clock-III dictionary |
| Empirical 539.9 spectral test | Still hypothesis protocol |

---

## 6. Exit criteria

- [x] Carrier \(\mathcal{O}_{\mathrm{res}}\) fixed with 539-free count  
- [x] Discrete \(X\) and \(f_\sharp\) defined  
- [x] Bott grading \(\beta_\sharp\) seed-independent; O2 residual exhibited  
- [x] Simplicial lift (A2) + continuous \(\Phi\to\mathrm{Gr}_1(V)\hookrightarrow BO\) (A3)  
- [x] Oriented rank-2 spin-aimed model (A3)  
- [x] Spin lift / \(w_1,w_2=0\) on \(\mathcal{O}_{\mathrm{res}}^{\mathrm{disc}}\) (A4)  
- [x] \(KO_0\) / \(\Omega_0^{\mathrm{Spin}}\) residual class \(B'\) (A5)

---

## 7. Bottom line

Architecture A is the standard bridge (spin bordism → \(KO\) → Bott), now **aimed at residual-flux carrier \(\mathcal{O}_{\mathrm{res}}\)** with honest provenance.  
Discrete classifying map, Bott-clock grading, \(B\mathrm{Spin}\) lift (A4), and 0-stem \(KO/\Omega^{\mathrm{Spin}}\) (A5) are closed on residual carrier.  
See `Architecture_A_Ores_Programme.md`, `Architecture_A4_BSpin_Lift.md`, `Architecture_A5_KO_Spin_Bordism.md`.
