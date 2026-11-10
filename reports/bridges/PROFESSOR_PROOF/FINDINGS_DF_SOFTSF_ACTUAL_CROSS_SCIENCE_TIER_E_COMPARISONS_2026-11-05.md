# FINDINGS — DF Soft SF: ACTUAL cross-science Tier E comparisons (2026-11-05)

Soft SF STARTED under OW `06748ff29e8b5e103833c5dec0712443a255d4e26990ea53acaa8793306fe9e2` (resolution / continue matching) + PRIMARY `bcc3ced0f1dfe15560e0bdb2e45bb35f4b1db26dcfb439e647a98c12fc5bc9a9`.
Soft SF AMEND hygiene `ab3bbbe52e881d9ce2a1d4bb8f086ef9c460c76fa4f631cb4ba3500308f3f49b` STANDS (math-only ≠ empirical; synthetic planted = circular E-FIT; Tier E never proof).
Also cited: Tier E OW 104d8ae9…; D₁/S_eff 96f8d42e…; RTA v16 PDF 1fe7b8a2…. tip LOCK `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` — **tip_touched NO**. invent HOLD STANDS. No CERT. No publish/spend. OW b25d5616… predictions catalog NOT started.

## Soft SF MATCH OWs
- 06748ff2… (continue actual comparisons beyond inventory): MATCH — real spectra/fits computed on on-disk FITS.
- bcc3ced0… (PRIMARY: solve the problem): MATCH.
- ab3bbbe5… hygiene: MATCH — no math-only or synthetic result counted positive.

## Methods (reproducible)
- Script: `reports/df_softsf_virgo_2026-11-05/virgo_analysis.py` run with `/workspace/.venv-df/bin/python` (~20 s). Outputs: `virgo_results.json`, `summary.txt`, `spectrum_{TSI_new,SPM_GREEN,SPM_RED,SPM_BLUE}.npz`, `SHA256SUMS.txt`.
- Data structure (astropy headers):
  - VIRGO_TSI_Minute.fits: PrimaryHDU (3, 14 199 837) float64; cols TAI s, TSI [org WRR], TSI [new SI] W/m²; L2a v8.0, PMOD/WRC; 1996-02-22 → 2023-02-20; cadence 60 s; NaN = missing (7.2 % of rows in used column). No separate quality-flag column; NaN is the only flag. Used col 3 (SI scale).
  - VIRGO-SPM-{RED,GREEN,BLUE}-L2: PrimaryHDU (2, 14 342 400); TAI s, signal ppm; 1996-01-23 → 2023-04-30; 60 s (one 90 s step 1996-03-26/27); duty cycle 94.3 %; header states orbit/degradation/outlier correction, 7-deg polynomial and **2-month high-pass already applied** (selection effect). NaN frac G 5.7 %, R 4.6 %, B 9.5 %.
  - LOI-ALL-PIXELS (1.9 GB): **not analysed** this pass (gap).
- Procedure: split into 16384-min (~11.4 d) segments; keep segments ≥95 % finite (TSI 482/866, G 652/875, R 736/875, B 444/875); linear-interpolate interior gaps; quadratic detrend; 6-h running-mean high-pass; Hann window; average |FFT|² over segments. Resolution 1.017 µHz (≈0.29 s in period at 540 s; Nyquist 120 s). Statistic: max power in the 3 bins nearest target ÷ (median of band 5–60 µHz away / ln2). Null: same statistic at 500 random periods U(450,750) s per channel. Per-segment LSQ sinusoid (sin, cos, const; 3 free params, period fixed) at each target, gaps masked.
- Free params: period fixed by hypothesis (0 fitted); 3 per segment LSQ; analyst choices = segment length, 95 % cut, 6-h high-pass, band width (not tuned; single run).

## VIRGO results (ratio R; null mean ± sd; z vs null)
| channel | null R (mean±sd, p99) | 539 s | 539.9 s | 540 s | 500 | 600 | 700 |
|---|---|---|---|---|---|---|---|
| TSI new | 0.723±0.067 (0.894) | 0.683 (z −0.60) | 0.768 (z +0.67)* | 0.768 (z +0.67)* | −0.04 | −0.28 | −0.32 |
| SPM GREEN | 0.726±0.088 (1.266) | z −0.19 | z −0.34* | z −0.34* | −0.07 | +0.11 | −0.55 |
| SPM RED | 0.721±0.069 (0.992) | z −0.66 | z −0.36* | z −0.36* | −0.34 | +0.07 | −0.45 |
| SPM BLUE | 0.732±0.102 (1.209) | z −0.14 | z −0.09* | z −0.09* | −0.68 | +0.19 | −0.53 |
\*539.9 and 540 s share the same nearest bin (1851.40 µHz, 540.13 s) — **not separable** at this resolution; 539 s is ~3 bins away.
LSQ amplitudes at all targets equal the red-noise continuum level of neighbours (e.g. SPM RED: 539 s 0.450±0.228 ppm, 540 s 0.463±0.241, controls 0.430/0.475/0.536 ppm; TSI ≈0.001 W/m² at all periods) — no target excess.

**Result:** no peak at 539, 539.9 or 540 s in any of 4 channels; every target is within ±0.7 σ of the random-period null and indistinguishable from controls. Max |z| = 0.68 (a control).

## Tier E table
| dataset | structure tested | Tier E | math | empirical (pred / meas / tol / free) | physical gaps |
|---|---|---|---|---|---|
| VIRGO TSI+SPM ×3 | 539 s (packaging integer 539 read as seconds — **hypothesis / Cat B**, not Cat A) | **E-UNTESTED** (no written Cat A seconds prediction) — data null-consistent | Prop 41.11/42.6 integer 539 (math only) | 539 s / no peak, z −0.66…−0.14 / ±1 bin (±0.3 s) / 0 fitted period, 3 LSQ | no derivation seconds↔cell capacity |
| VIRGO TSI+SPM ×3 | 539.9 s continuum (prior narrative, Cat B) | **E-TENSION** | none Cat A | 539.9 s / no peak, z −0.36…+0.67 / ±0.3 s / 0 | narrative claim not reproduced; 2-month HP on SPM is irrelevant at mHz |
| VIRGO TSI+SPM ×3 | 540 s freeze claim | **E-TENSION** | none Cat A | 540 s / no peak (same bin as 539.9) / ±0.3 s / 0 | 539.9 vs 540 unresolvable with 11.4 d segments |
| VIRGO | Residual₅₃₉ discrete leftover-cell algebra | **ABSENT** (not computed; no extraction defined) | — | — | no operational definition of Residual₅₃₉ on time series |
| VIRGO LOI 1.9 GB | any | **E-UNTESTED** (not opened this pass) | — | — | gap |
| s-family partB (195 072 trials) | Q1–Q5 vs 16 observables | **E-UNTESTED** for RTA attach; result **null-consistent (chance)** | Cat A number theory (Part A) | non-degenerate (excl. T15/T16): 67 matches vs N4 jitter null 69.2±6.1 (p=0.67); none of T1–T5 within 1σ (e.g. √n₁₃₈=136.996 vs α⁻¹ 137.036, 1.9×10⁶σ; 1/I₃₇=16.830 vs m_τ/m_μ 16.817, 12σ; d_cusp/dimV/2 @s=41 = 0.2311 vs sin²θ_W 0.23129, 5σ) / tol max(σ,10⁻³|y|) / 6 ops × s choice (look-elsewhere 195 072) | T15 (10 067 hits) & T16 (496 hits) degenerate windows; global p flips 1.0↔1e-4 across nulls |
| Periodic_Table npz | IE_model vs IE_exp (118 Z) | **E-UNTESTED** for RTA (no packaging theorem attaches) — numbers CONFIRMED poor | none | MAE 280.3 eV, RMSE 319.7 eV, MAPE 3934 %, Pearson r = −0.54, 0/118 within 10 % | no theorem; model anticorrelates with data |
| synthetic G4 | — | not re-opened (prior: circular E-FIT) | — | — | — |
| muon-g2 / CMB papers | — | not used: no written predicted-vs-measured RTA number located without invention | — | — | gap |

Tier E counts (this pass): E-MATCH 0 · E-PARTIAL 0 · E-FIT 0 · E-TENSION 2 · E-UNTESTED 4 (539 s, LOI, partB-attach, Periodic) · ABSENT 1 (Residual₅₃₉).

## Positive empirical association count: **0**
Missing tests ≠ support; null results are not support.

## Soft SF RESOLVED
1. VIRGO FITS structure/cadence/units/NaN handling documented (TSI + 3 SPM).
2. Actual periodogram + LSQ tests at 539/539.9/540 s with controls and random-period null: no signal (4 channels).
3. 539.9 s / 540 s claims → E-TENSION (not reproduced in public VIRGO L2).
4. partB non-degenerate hits quantified vs nulls → chance.
5. Periodic_Table numbers confirmed poor; E-UNTESTED for RTA.

## Soft SF remaining gaps
- LOI-ALL-PIXELS not analysed (could subset by pixel).
- 539.9 vs 540 s unresolvable with 11.4 d segments; longer coherent segments would need gap-tolerant LS over months.
- No Cat A derivation linking packaging integer 539 to seconds; no operational Residual₅₃₉ extraction.
- No concrete RTA predicted-vs-measured numbers in g-2/CMB papers extracted.
- Analyst choices (segment, high-pass) single-run; not a pre-registration.
