# Holographic window investigation

**Script:** `scripts/holographic_window_investigate.py`  
**JSON:** `holographic_window_results.json`  
**Related:** No-Go (canonical), Empirical phase-locking protocol, ACE status of record

---

## 1. What the model means by “holographic window”

From **HQH-539 / S²-11DM²ET-X** materials (spec + KK-tower notes):

| Object | Model value | Role |
|--------|------------:|------|
| Coherent trit window \(W\) | **18** \(=\lfloor e^{3}/\ln 3\rfloor\) | First 18 steps (0–17); **non-circular** from \(e^{3}\) and \(\ln 3\) (`NonCircular_18_plus_521.md`) |
| Body length (ansatz) | **521** \(=4880//9-21\) | So \(18+521=539\); \(-21\) still needs motivation |
| Puncture / screen digit count \(P\) | **61** | \(G_2\) ω-punctures: ternary digits resolved before leakage |
| Seed threshold | \(\sim 10^{18}\) | Magnitude to engage full coherent / screen structure |
| \(3^{18}\) | 387 420 489 | Scale of an 18-trit word |
| \(\log_3(10^{18})\) | ≈ 37.73 | Ternary digit length at the HQCC threshold |

### Spec admissions (important)

1. **Natural** \(T_3\) trajectories on large integers stop in roughly **374–506** steps (mean ≈ **436**), not 539.  
2. **539 forced iterations** are an **explicit engineering / tower-traversal choice** (continue past the fixed point).  
3. The **18 / 521 split** matches \(18+521=539\) with derived 18; production still applies **uniform** \(T_3\) with **no** special op at step 17→18.

So the holographic window is a **model constraint layered on top of** the residue map — exactly the kind of extra structure the No-Go says is needed for a long resonant story, and **not** implied by ACE contraction alone.

### Composition (when 539 is imposed)

\[
18\ (\text{window}) + 1\ (\text{master}) + 520\ (\text{tower pull}) = 539
\]

That arithmetic **inserts fixed counts**; it is not the ACE bridge \(N_\star=14\).

---

## 2. How we investigated (protocol-compliant)

### Model-facing constructions (pre-declared; not 539.9)

1. **`holo_window_W18`** — rolling 18-step residue word \((n_{t-W+1},\ldots,n_t)\bmod 3\) as a base-3 fraction in \([-1/2,1/2]\).  
2. **`holo_screen_P61`** — last 61 ternary digits of \(n_t\) as a base-3 screen coordinate.  
3. **`holo_window_plus_screen`** — \(0.65\cdot(1)+0.35\cdot(2)\).

### Spectral design (no 539.9 in estimator)

| Item | Choice |
|------|--------|
| Map | \(T^\sharp\) (min-defect completion) |
| Horizon | \(N=4096=2^{12}\) |
| Estimator | Periodogram after linear detrend; natural DFT grid |
| Bootstrap | Residual, \(B=250\); same grid |
| 18 / 61 / 539.9 | **Post-hoc compatibility only** |

---

## 3. Results

### Natural stopping times (no forced 539)

| Stat | Value |
|------|------:|
| Median | **52** |
| Mean | ~916 (heavy upper tail; some hit max 2000) |
| q05–q95 | [29, 2000] |
| Fraction \(\ge 539\) | ~0.45 |
| Fraction \(\le 14\) (ACE \(N_\star\)) | ~0.04 |

**Reading:** Free iteration under \(T^\sharp\) does **not** concentrate at 539. Many orbits stop early; a minority run long. Forced 539 remains an **external length constraint**, matching the HQH spec.

### Spectral primary estimates

| Phase construction | \(\hat T\) median | Ensemble median 95% CI (sketch) |
|--------------------|------------------:|----------------------------------|
| holo_window_W18 | **~3.00** | Wide (heavy tail toward \(N\)) |
| holo_screen_P61 | **4096** (\(=\!N\)) | \([N,N]\) — lowest-frequency dominance |
| window + screen | **~3.00** | Wide |

Post-hoc \(|\hat T_{\mathrm{med}}-539.9|\approx 537\) for window-based phases.

**Screen series:** almost always peaks at the **fundamental DFT bin** \(T=N\). That means the 61-trit screen coordinate is **slowly varying / trend-like** after linear detrend residuals, **not** a clean oscillator at period 61 or 539.9.

**Window series:** dominant mass at **short** periods (~3), i.e. residue-scale structure, not a carrier near 18 or 539.9.  
(Wide CIs that *include* 18, 61, and 539.9 reflect **dispersion / low-frequency leakage**, not a sharp resonant detection at those values.)

---

## 4. Interpretation

| Question | Answer from this investigation |
|----------|--------------------------------|
| Is the holographic window in the model? | Yes: **W = 18**, screen **P = 61**, threshold \(\sim 10^{18}\) |
| Is it computational in HQH-539 crypto? | Spec: **theoretical**; uniform \(T_3\), no step-17 boundary op |
| Does it force spectral period 539.9 under \(T^\sharp\)? | **Not observed** in this design |
| Does free dynamics stop at 539? | **No** (median stop ~52; 539 is forced length) |
| Relation to ACE / No-Go | Window + screen + forced count are **extra constraints**; ACE still only gives short mean contraction / \(N_\star=14\) |

### What a holographic window *can* do (model role)

- Bound **information resolution** (18-trit coherent word; 61-digit screen).  
- Mark a **theoretical phase split** (seeding vs master tower) without changing local \(T_3\).  
- Enter **security / hardness** narratives (structured sparsity, full tower traversal).  

### What it does *not* do (this empirical slice)

- Automatically produce a **dominant** spectral peak at **539.9** in window/screen phase series under free \(T^\sharp\) iteration.  
- Replace the need for **forced iteration count** or a **pre-chosen phase-lock** if the model asserts a 539-step resonant ring.

---

## 5. Status relative to the canonical No-Go

The No-Go already listed “holographic window” among constraints **outside** residue + democracy + \(T^\sharp\) contraction.

This investigation **confirms** that reading:

1. Window (**18**) and screen (**61**) are well-defined model integers.  
2. They do **not**, by themselves under protocol spectral analysis, recover **539.9** as the dominant period.  
3. **Forced 539** is still required for the crypto “full path”; natural stopping is a different distribution.  
4. Empirical search for ~539.9 remains a **hypothesis test** (separate protocol), not a derivation from the window definition.

---

## 6. Reproduce

```powershell
python S2-11DM2ET-X-Axiomatic-Book\scripts\holographic_window_investigate.py --N 4096 --seeds 40 --B 250 --map sharp
python S2-11DM2ET-X-Axiomatic-Book\scripts\holographic_window_investigate.py --N 4096 --seeds 40 --B 250 --map T3
```

---

## 7. Bottom line

> **Holographic window** = 18-trit coherent seeding (theoretical phase) + **61**-digit puncture screen + \(\sim 10^{18}\) threshold.  
> **Spec:** uniform map; 539 is **forced** length; natural stops are shorter.  
> **Empirical (this run):** window/screen phases show **short** dominant periods (~3) or **DC/\(N\)** for the screen — **not** a clean 539.9 resonance.  
> **No-Go consistent:** long resonant structure still needs **extra** constraints (fixed count, window narrative, phase-lock hypothesis), not ACE alone.
