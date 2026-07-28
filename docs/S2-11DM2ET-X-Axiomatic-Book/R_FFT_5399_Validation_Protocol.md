# R-FFT-539.9 Validation Protocol

**Status:** Binding for any public or internal claim that cites R-FFT-539.9,  
`power_5399`, `snr_5399`, or a refined period near \(G_4 = 539.9\,\mathrm{s}\).

**Companion code:** `scripts/r_fft_5399.py`  
**Related:** `Empirical_PhaseLocking_Protocol.md`, `NoGo_Theorem_Canonical.md`,  
`ACE_Status_of_Record.md`, `CLOSED_CONSTANTS.md`

---

## 0. One-line rule

> **Preconditioned lock onto 539.9 is not unsupervised discovery.**  
> Primary period claims must come from a free spectral estimate with **no**  
> \(539.9\) in the estimator, grid, filters, horizon, or templates.

---

## 1. What R-FFT-539.9 is

R-FFT-539.9 is a spectral pipeline that combines:

| Layer | Contents | Uses \(G_4\)? |
|-------|----------|---------------|
| **A — Standard DSP** | Kaiser window (\(\beta=8.6\)), optional ~5 s cosine modulation, zero-padded FFT (`nfft = N×16`), mean-spectrum SNR, 3-bin quadratic peak refinement | Only if the *target bin* is set to \(1/G_4\) |
| **B — Model-tuned** | Resonant preconditioning (G₄-locked phase / \(\beta_{\mathrm{PBH}}\) amplitude structure), target metrics `power_5399` / `snr_5399` | **Yes** |

Layer B is **compatibility / lock analysis**, not free discovery.

Closed ledger constants (do not re-fit as free parameters in a discovery claim):

| Symbol | Value | Role |
|--------|-------|------|
| \(G_4\) | 539.9 s | Clock-III period |
| \(\kappa_{\mathrm{dark}}\) | \(243/539\) | Dark-energy coupling |
| \(\beta_{\mathrm{PBH}}\) | \(11/61\) | PBH friction / sine-mode weight |
| \(\mu\) | 1.55 | Stability target (framework constant) |
| Ladder | \(\{5,10,15,30,45\}\) s | Sub-harmonics |

Attractor (closed form):

\[
\Phi(t)=\Phi_0+0.90\cos(2\pi t/539.9)+(11/61)\sin(2\pi t/539.9).
\]

In HQH-539 crypto materials, \(\Phi(t)\) is **theoretical only** (not per-step state modulation). Do not treat crypto pipeline outputs as empirical proof of \(\Phi(t)\).

---

## 2. Forbidden practices (estimation stage)

The following **void a discovery claim** for period \(G_4\):

1. Setting horizon \(N\), window length, or frequency grid **to privilege** \(1/539.9\).
2. Band-pass / notch / matched filters **centred near** \(1/539.9\) *before* estimating the dominant period.
3. Calling `full_r_fft_analysis(..., precondition=True)` and reporting `refined_period ≈ 539.9` as an unsupervised finding.
4. Inserting 539.9 into the phase observable, residual construction, or bootstrap **re-weighting**.
5. Discarding bootstrap / null replicates by proximity to 539.9.
6. Conflating Clock II (\(\sigma = 539\)) with Clock III (\(G_4 = 539.9\)) or with ACE depth \(N_\star = 14\).

---

## 3. Required reporting order

### Primary (must appear first; no 539.9 in the estimator)

| Item | Specification |
|------|----------------|
| Series definition | Sampling \(\Delta t\), length \(N\), detrend (linear default) |
| Estimator | Free peak of **Kaiser-only** windowed periodogram / zero-padded FFT (no ~5 s cosine modulation; that modulation is model ladder structure) **or** protocol-compliant periodogram from `Empirical_PhaseLocking_Protocol.md` |
| Point estimate | \(\hat T = 1/f_{k^\ast}\), \(k^\ast=\arg\max\) power on the natural grid |
| Uncertainty | Residual / block bootstrap **or** phase-randomisation ensemble; **no** 539.9 |
| Peak significance | Phase-scramble or shuffle nulls; report fraction of nulls exceeding observed peak power |

Code path:

```text
full_r_fft_analysis(series, dt, precondition=False, scrambled_g4_control=False, n_null=B)
→ free_T_hat, free_f_hat, free_peak_power, null_fraction_exceeding
discovery_claim_allowed == True
```

### Secondary (optional; only after primary is frozen)

| Item | Specification |
|------|----------------|
| Model target metrics | `power_5399`, `snr_5399` at \(f=1/G_4\) on the **same free-processed** spectrum |
| Compatibility | Is \(\hat T\) consistent with 539.9? (pre-registered \(\delta\), CI coverage, etc.) |
| Preconditioned run | `precondition=True` for lock / attractor diagnostics only — label **“compatibility, not discovery”** |
| Scrambled-G4 control | `scrambled_g4_control=True` or `n_null>0` phase-scramble; compare `power_5399` / `snr_5399` to null |

Code path for side-by-side comparison:

```text
compare_precondition_modes(series, dt, n_null=B)
→ free / preconditioned / scrambled_g4 + summary.warning
```

### Tertiary (framework bookkeeping, not data-driven discovery)

- `echo_amplitude` / `echo_beta` (= \(\beta_{\mathrm{PBH}}=11/61\))
- `mu_stability` (= 1.55 ledger value unless independently re-estimated under a pre-registered metric)
- Sub-harmonic ladder powers

---

## 4. Nulls (scrambled-G4 analogue)

| Null | What it preserves | What it destroys | Role |
|------|-------------------|------------------|------|
| Phase-randomisation | \(|\mathrm{DFT}|\) shape | Coherent phase (incl. G₄ lock) | Peak / `power_5399` significance |
| Random shuffle | Marginal values | Dependence + spectrum shape | Simple absolute null |
| Residual bootstrap | Trend structure | Residual arrangement | Uncertainty on \(\hat T\) |

**Label mapping:** materials may not use the string `scrambled-G4`; the code flag  
`scrambled_g4_control` and `n_null` phase-scramble nulls are the operational form.

A large `power_5399` under `precondition=True` that **collapses** under phase-scramble is evidence of phase-coherent structure *relative to the preconditioner*, not free discovery of \(G_4\).

---

## 5. Decision table

| Observation | Allowed claim |
|-------------|----------------|
| Free \(\hat T \approx 539.9\) with null \(p\) below pre-registered \(\alpha\), CI excludes alternatives of interest | Candidate empirical period consistent with Clock-III hypothesis |
| Free \(\hat T\) far from 539.9; preconditioned `refined_period ≈ 539.9` | **No discovery of \(G_4\)**; at most “preconditioner recovered its own period” |
| Preconditioned SNR ≫ free SNR and ≫ scrambled control | Model-tuned energy concentration — report as **secondary**, not discovery |
| Only `power_5399` reported, no free peak | **Non-compliant** report |

---

## 6. Minimum compliant abstract template

```text
We estimate the dominant period of [series] with a free spectral method
(no reference to 539.9 in the estimator). We obtain T_hat = … with
[bootstrap CI] and phase-scramble null fraction …. Separately, as a
compatibility check against the S²-11DM²ET-X Clock-III value G4 = 539.9 s,
we report power_5399 / snr_5399 = …. Preconditioned R-FFT runs are
presented only as secondary lock diagnostics and are not used as
discovery statistics.
```

---

## 7. Relationship to the empirical phase-locking protocol

`Empirical_PhaseLocking_Protocol.md` remains the **canonical** free-period  
protocol for map trajectories (periodogram on natural DFT grid, bootstrap,  
post-hoc compatibility).

R-FFT-539.9 **extends** that stack with:

- documented Kaiser / zero-pad / quadratic refinement DSP, and  
- optional model-tuned metrics and preconditioning,

without relaxing the free-first rule. Where they differ, **free-first wins**.

---

## 8. Source inventory (full_r_fft_analysis)

See `R_FFT_5399_Source_Inventory.md` for what was found vs. missing when this  
pipeline was redrafted, and where the ready-to-use implementation lives.

## 9. Observatory data (real only)

- **Synthetics dismissed:** `data/RFFT_datasets/SYNTHETIC_DISMISSED.md`  
  (`pure_noise`, `pure_G4`, `multi_k_residual_placeholder`, …).
- **Registry / loaders:** `data/RFFT_datasets/REGISTRY.json`,  
  `scripts/observatory_data/`, CLI `scripts/run_rfft_observatory.py`.
- **Staging status:** `data/RFFT_datasets/REAL_DATA_STATUS.md`.
- **Validation V5 (INTEGRAL/SPI 511 keV):**  
  `data/RFFT_datasets/VALIDATION_V5_INTEGRAL_SPI_511keV.md` — free-first  
  binding; Clock III secondary; numerical run only after light curve staged.

Discovery reports must name a registry observatory id and set `is_real: true`  
in provenance. Fabricated `.npz`/`.csv` test series are out of band.
