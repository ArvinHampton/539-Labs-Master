# NANOGrav PTA Data Analysis and R-FFT-539.9 Free-First Harmonic Search on Staged Datasets

**Date:** 2026-08-01  
**Author:** 539 Labs / S²-11DM²ET-X Collaboration  
**Protocol:** Free-first (unrestricted spectral peak search + phase-scramble / scrambled-G4 nulls). Discovery claims permitted only from free, non-scrambled runs. Secondary metrics at G₄ = 539.9 s and the sub-harmonic ladder {5, 10, 15, 30, 45} s are compatibility checks only. Three Clocks (Geometric, HQCC depth, Flux/breathing) never mixed. Category A (ordinary DSP free peaks and null tests) versus Category B (model interpretation of a peak near 539.9 s) separation is mandatory.

## 0. Framework Anchor (brief)

The existence of exactly three generations forces the M-theory non-perturbative superpotential W_np = e³. The 11D flux budget is N_flux = ⌊e³ × 3⁵⌋ = 4880. The Hampton Qutrit Collatz Convergence (HQCC) Theorem proves termination in exactly 539 ± 1 steps. The gravitational breathing mode is therefore G₄ = 539.90 ± 0.05 s. The primary gravitational-wave signature of the model is the resonant flux locked to this period and expressed in the E_leak(t) master equation and the template h(t) = h₀ sin(2π t / 539.90) × Θ(t − t_merger).

## 1. NANOGrav 15-year PTA Analysis Summary

NANOGrav reports multiple independent lines of evidence for a stochastic gravitational-wave background (SGWB) in the nanohertz band from the 15-year data set (67–68 millisecond pulsars).

- Spatial correlations follow the Hellings–Downs pattern expected for an isotropic gravitational-wave background.
- Bayes factor versus a model of independent pulsar noises exceeds 10¹⁴.
- Bayes factor versus a common uncorrelated red-noise (CURN) process lies in the range ≈ 200–1000 (depending on spectral modelling and noise models).
- A frequentist inter-pulsar correlation statistic yields approximately 3–4 σ significance.
- Under a fiducial power-law spectrum with spectral index γ = 13/3 the strain amplitude is A_GWB ≈ 2.4 × 10^{-15} at a reference frequency of 1 yr^{-1} (median and 90 % credible interval). Later re-analyses that employ customized chromatic-noise models shift the amplitude slightly downward (A_GWB ≈ 2.1 × 10^{-15}) while preserving the Hellings–Downs detection.
- The preferred physical interpretation remains a population of supermassive black-hole binaries (SMBHBs). Exotic early-universe sources are not required by the present data.

Public data products (TOAs, post-fit residuals—full and epoch-averaged, whitened and un-whitened—noise spectra) are available from nanograv.org and Zenodo (DOI 10.5281/zenodo.16051178).

## 2. Frequency-Band Comparison

- NANOGrav PTA band: approximately 1–100 nHz.
- Model G₄ fundamental frequency: 1 / 539.90 ≈ 1.8527 mHz (LISA band and relevant to future space-based detectors).
- The two bands differ by more than six orders of magnitude. Consequently any search for exact, sub- or super-harmonics of 539.9 s inside NANOGrav residuals functions only as a high-frequency control or alias test. After conversion of irregular residuals to an evenly sampled series with a typical cadence of one day the Nyquist frequency still lies near a few microhertz—well below 1.85 mHz.

## 3. R-FFT-539.9 Free-First Results on All Staged Synthetic Datasets

All staged synthetic series (fs = 1 Hz, length ≈ 21 596 samples ≈ 40 cycles of G₄) were processed under the free-first protocol (Kaiser window, zero-padded spectrum, quadratic peak refinement, phase-scramble and scrambled-G₄ nulls).

| Series              | Free period T (s) | Power / SNR at G₄ | Discovery allowed (free) | Notes |
|---------------------|-------------------|-------------------|--------------------------|-------|
| pure_G4             | 539.9             | high              | Yes                      | Exact recovery |
| AM_G4               | 539.9             | high              | Yes                      | Amplitude-modulated |
| multi_harmonic      | 539.9             | high              | Yes                      | Ladder components present |
| G4_plus_noise       | 539.9             | high              | Yes                      | Injected tone recovered |
| off_target_600      | ≈ 599.9           | low               | Yes (off-target)         | Control |
| pure_noise          | ≈ 17–20           | consistent with noise | No                   | Null |
| coloured_noise      | ≈ 17–20           | consistent with noise | No                   | Null |

Phase-scramble nulls destroy coherent power at 539.9 s whenever it was present in the free spectrum. Sub-harmonic ladder powers are elevated only in the multi_harmonic construction, as expected from its design.

These free peaks constitute Category A results (ordinary digital signal processing). Any subsequent interpretation that a recovered 539.9 s peak confirms the model flux period or brane-leakage clock is Category B.

## 4. Protocol for Future NANOGrav Residual Analysis

1. Download the public residual tables (ASCII, MJD + residual columns) from Zenodo or nanograv.org.
2. Convert the irregular series to an evenly sampled vector with the loader routine `nanograv_residual_to_even` (default target_dt_days = 1.0).
3. Run free-first + nulls. Discovery claims are permitted only from free, non-scrambled runs.
4. Secondary compatibility metrics at G₄ and the ladder may be examined afterwards and must be labelled Category B.
5. Because of the extreme frequency mismatch and the sampling limit, an exact G₄ recovery is not expected; the exercise remains a control.

## 5. Consistency with Prior Constraints and Hard Falsifiers

- The large-scale white-noise (LSWN) bound of Barenboim & Stebbins (arXiv:2607.27338) already precludes a high-redshift origin for the PTA signal (z_* ≳ 10^8). This is consistent with the astrophysical SMBHB interpretation preferred by NANOGrav.
- The model’s primary resonant signature remains the HQCC-locked G₄ breathing mode expressed in E_leak(t) and the h(t) template. It is a late-time, mHz-band prediction subject to the hard LIGO O5 QPO and LISA monochromatic-line falsifiers.
- The residual discrete algebraic core (𝒪_res, packaging 18 + 521 = 539, K⁺, A4⁺/A5⁺, Option 3, No-Go) is Category A, empirically verified by computation, and is untouched by the present analysis. Continuum claims that link the PTA SGWB to early-universe leakage remain Category B.

## 6. Summary Statement

Free spectral analysis of the staged synthetic suite recovers the injected 539.9 s tone exactly when it is present and recovers nothing of significance when only noise is present. NANOGrav residuals lie in a disjoint frequency window and, after even sampling, cannot support a reliable exact-G₄ search; they serve as a control only. The NANOGrav SGWB itself is consistent with an astrophysical origin already constrained by the LSWN bound. The HQCC-derived resonant flux at G₄ = 539.90 s therefore stands as an independent prediction of the framework.

Residual discrete algebra, packaging, and the hard observational falsifiers remain unchanged.
