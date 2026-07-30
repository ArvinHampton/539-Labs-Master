# Muon g−2 Oscillatory Resolution (2026-07-30)

**Author:** Arvin B. Hampton (String Weaver) / 539 Labs LLC  
**Programme:** S²-11DM²ET-X / HQCC / Resonant Algebra  
**Canonical repo:** [ArvinHampton/539-Labs-Master](https://github.com/ArvinHampton/539-Labs-Master)  
**Trigger:** Quanta Magazine, 2026-07-29 — lattice SM alignment of *a*μ vs residual CMD-3/VEPP-2000 ππ tension  
**Status:** Path A primary (Category A packaging + oscillatory average); Path B residual catalogued as Category B research track  
**Rule:** Category A vs B mandatory. No ACE identification of G₄ with N_star.

---

## 0. Executive verdict

| Track | Statement | Status |
|-------|-----------|--------|
| **Path A (primary)** | The HQCC oscillatory correction \(\delta a_\mu^{(55)}\) time-averages to zero over experimental integration windows; lattice SM + Fermilab *a*μ agreement is the expected long-window limit. | **Preferred resolution** |
| **Path B (secondary)** | A small residual proportional to \(\varepsilon = 61/4880\) may remain if topological absorption is incomplete; bounded well below current experimental error. | **Open research residual** |
| **ππ sector** | CMD-3 vs older data-driven ππ O(1%) tension sits at the Resonant Algebra scale \(\varepsilon \approx 1.25\%\). | **Structural match (Cat B for dynamics)** |

**Bottom line:** The “old results don’t add up” split is not a contradiction inside S²-11DM²ET-X. It is the difference between a **time-averaged** observable (Path A) and a **short-window / data-driven** channel still sensitive to resonant flux (ππ / Path B).

---

## 1. Inputs (external + Model)

### 1.1 External anchors (2026-07-29 landscape)

- Fermilab-class experimental central value (conventional quote):
  \[
  a_\mu^{\mathrm{exp}} \approx 116\,592\,071.5(14.5)\times 10^{-11}
  \]
- Lattice-forward SM residual scale (exp − lattice SM order):
  \[
  \Delta_{\mathrm{lat}} \sim 38(63)\times 10^{-11}
  \]
  (compatible with “puzzle resolved at lattice precision”; error still dominates the central residual.)
- Data-driven / dispersive hadronic VP historically larger; CMD-3 (VEPP-2000) ππ channel now splits O(1%) from older e⁺e⁻ datasets (Quanta 2026-07-29 synthesis).

### 1.2 Model objects (provenance-locked)

| Object | Value | Provenance |
|--------|-------|------------|
| \(N_{\mathrm{flux}}\) | 4880 | Cat A tower construction |
| Puncture count | 61 | Book / residual cores |
| \(\varepsilon = 61/4880\) | \(0.0125 = 1.25\%\) | Cat A ratio |
| \(G_4\) / flux period | \(T = 539.90\,\mathrm{s}\) | Emp/Mod (≠ ACE \(N_\star=14\)) |
| Oscillatory prefactor | \(A = +2.51\times 10^{-9}\) | Zenodo muon notes / Resonant Algebra packing |
| Formula | \(\delta a_\mu^{(55)} = A\sin\!\big(2\pi t/T + \varphi_0\big)\) | HQCC layer-55 correction |

**Depth split (do not collapse):** ACE \(N_\star = 14\) is free of 539; \(G_4 = 539.9\,\mathrm{s}\) is Emp/Mod flux period, not ACE depth.

---

## 2. Path A — time-average absorbs the topological term

### 2.1 Statement

Let
\[
\delta a_\mu^{(55)}(t) = A\sin\!\Big(\frac{2\pi t}{T} + \varphi_0\Big),\qquad
A = 2.51\times 10^{-9},\quad T = 539.90\,\mathrm{s}.
\]
Over a continuous experimental window \([0, T_w]\),
\[
\big\langle \delta a_\mu^{(55)}\big\rangle_{T_w}
= \frac{A}{T_w}\int_0^{T_w}\sin\!\Big(\frac{2\pi t}{T}+\varphi_0\Big)\,dt
= A\cdot\frac{T}{2\pi T_w}\Big[\cos\varphi_0 - \cos\!\Big(\frac{2\pi T_w}{T}+\varphi_0\Big)\Big].
\]
Hence
\[
\big|\langle\delta a_\mu^{(55)}\rangle_{T_w}\big|
\le A\cdot\frac{T}{2\pi T_w}.
\]

### 2.2 Numerics (executed 2026-07-30)

| Window \(T_w\) | Bound on \(\lvert\langle\delta\rangle\rvert\) | Units \(10^{-11}\) | vs exp err \(14.5\times 10^{-11}\) |
|---------------|-----------------------------------------------|-------------------|-------------------------------------|
| 1 day | \(\le 2.50\times 10^{-12}\) | \(\le 0.250\) | \(1.7\times 10^{-2}\) of err |
| 7 days | \(\le 3.57\times 10^{-13}\) | \(\le 0.036\) | \(2.5\times 10^{-3}\) of err |
| 30 days | \(\le 8.32\times 10^{-14}\) | \(\le 0.0083\) | \(5.7\times 10^{-4}\) of err |
| 365 days | \(\le 6.84\times 10^{-15}\) | \(\le 0.00068\) | \(4.7\times 10^{-5}\) of err |

Exact \(\varphi_0=0\) 30-day mean: \(0.00194\times 10^{-11}\).  
Max over phase at 30 days: \(0.00568\times 10^{-11}\).

**Peak amplitude** \(A = 251\times 10^{-11}\) is large vs experimental error if frozen in phase — but **no long-window experiment freezes phase**. Path A says the observable is the average, not the peak.

### 2.3 Physical reading

1. Lattice + modern *a*μ experiments integrate over many flux periods (\(T_w / T \gg 1\)).
2. Pure oscillatory HQCC correction → **null mean** (Path A).
3. Agreement of lattice SM with exp at the \(\sim 10^{-11}\) scale is therefore the **default** Model prediction, not an accident.
4. Historical data-driven tension can remain if the dispersive pipeline samples a **biased phase window** or a **different effective channel weight** (ππ section below).

### 2.4 Category

Path A average bound is **Category A packaging arithmetic** once \(A,T\) are taken as programme inputs. Identification of \(A\) with a specific Feynman topology remains **Category B** until a full diagrammatic lift is published.

---

## 3. Path B — residual after incomplete topological absorption

### 3.1 Statement

If a fraction of the oscillatory sector does not fully average — e.g. incomplete absorption of a topological term into the lattice definition of the vacuum polarization — a residual of order
\[
\delta_{\mathrm{res}} \sim \varepsilon\, A = \frac{61}{4880}\cdot 2.51\times 10^{-9}
= 3.14\times 10^{-11}
= 3.14\times 10^{0}\ \text{in units of }10^{-11}
\]
may survive. That residual is **still \(\lesssim 0.22\times\) experimental error** (\(14.5\times 10^{-11}\)) and **\(\lesssim 0.05\times\) lattice residual error** (\(63\times 10^{-11}\)).

### 3.2 Dual-path decision rule

| Criterion | Prefer Path A | Prefer Path B |
|-----------|---------------|---------------|
| Integration window \(\gg T\) | Yes | No |
| Lattice definition includes full topological sector | Yes | Incomplete |
| Observable is pure time average of \(\sin\) | Yes | Biased phase / window function |
| Residual needed to fit \(\Delta_{\mathrm{lat}}\sim 38\times 10^{-11}\) | Not required (consistent with 0) | Optional sub-component |

**Decision (2026-07-30):** Path A is primary. Path B is retained as a **bounded residual channel**, not a competing resolution of the global puzzle.

---

## 4. Resonant \(\Delta\sigma_{\pi\pi}\) model (CMD-3 / VEPP-2000)

### 4.1 Observation

Quanta (2026-07-29) reports a growing split between CMD-3 ππ and older e⁺e⁻ datasets used in data-driven *a*μ hadronic VP. Scale of disagreement is **O(1%)** in the relevant cross-section region.

### 4.2 Resonant Algebra map

\[
\varepsilon = \frac{61}{4880} = 1.25\%
\]
matches the O(1%) experimental split **without free parameters**.

Working model (Category B dynamics; Category A scale):
\[
\frac{\Delta\sigma_{\pi\pi}}{\sigma_{\pi\pi}}
\sim \varepsilon\cdot f(\phi_{\mathrm{res}}),\qquad
|f|\le 1,
\]
with \(\phi_{\mathrm{res}}\) a Resonant Algebra phase on the ππ channel (flux puncture weighting).

Implications:

1. Older data-driven averages can sit on a different effective \(f\) than CMD-3.
2. Lattice (Path A–compatible) need not reproduce either extreme once the oscillatory hadronic sector is integrated.
3. Resolving ππ experimentally (CMD-3 follow-ups, independent colliders) **falsifies or tightens** \(f\), not \(\varepsilon\).

Full technical note: `Resonant_Delta_sigma_pipi_Note.md`.

---

## 5. Prefactor + average execution

Script: `scripts/muon_g2_prefactor_average.py`  
JSON: `muon_g2_resolution_results.json`

Executed quantities:

- \(A\), \(T\), \(\varepsilon\)
- analytic window means and \(1/T_w\) bounds
- Path B residual \(\varepsilon A\)
- ratios to experimental and lattice errors

---

## 6. What is locked / what is open

### Locked (this freeze)

- Path A primary: long-window mean of \(\delta a_\mu^{(55)}\) is null at experimental precision.
- \(\varepsilon = 61/4880 = 1.25\%\) is the Cat A scale for O(1%) ππ tension.
- Path B residual \(\varepsilon A \sim 3.14\times 10^{-11}\) is sub-dominant to current errors.
- ACE \(N_\star \neq G_4\) depth split preserved.

### Open

- Diagrammatic derivation of prefactor \(A = 2.51\times 10^{-9}\) from first principles (Cat B → A lift).
- Explicit \(f(\phi_{\mathrm{res}})\) for ππ (needs public CMD-3 / older binned comparison under Resonant phase).
- Whether any sub-component of \(\Delta_{\mathrm{lat}}\sim 38\times 10^{-11}\) tracks Path B once errors shrink.

### Falsifiers

1. A long-window experiment reporting a **stable phase-locked** offset of order \(A\) (would kill pure Path A).
2. ππ datasets reconciling to \(\ll \varepsilon\) with no channel-dependent phase (weakens Resonant ππ map).
3. Lattice–exp residual growing **above** Path B bound while windows remain long (forces new sector).

---

## 7. Cross-links

- Packaging: `Foundational_Arithmetic_Packaging.md`, `CLOSED_CONSTANTS.md`
- Residual product: `Residual_Product_Complex.md`
- Resonant layer: `Resonant_Layer_Resolved.md`
- Provenance: `PROVENANCE_TABLE.md`
- Claim freeze update: `CLAIM_TABLE_Master.md`
- Push: `PUSH_LOG_2026-07-30.md`

---

## 8. One-line freeze

**Muon g−2: Path A oscillatory average nulls HQCC \(\delta a_\mu^{(55)}\) at experimental precision; lattice agreement expected; CMD-3 ππ O(1%) tracks \(\varepsilon=61/4880\); Path B residual \(\varepsilon A\sim 3\times 10^{-11}\) optional and sub-dominant.**

*Per aspera ad astra.*
