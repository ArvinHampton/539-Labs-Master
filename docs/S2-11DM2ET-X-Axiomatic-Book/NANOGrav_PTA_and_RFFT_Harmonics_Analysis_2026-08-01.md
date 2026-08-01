# NANOGrav PTA Data Analysis and R-FFT-539.9 Free-First Harmonic Search on Staged Datasets

**Date:** 2026-08-01  
**Author:** S²-11DM²ET-X / 539 Labs Collaboration  
**Status:** Category A free spectral results on synthetics; Category B continuum / model interpretation for PTA linkage  
**Protocol:** Free-first Resonant FFT (R-FFT-539.9). Discovery claim allowed only from unrestricted free peak + phase-scramble / scrambled-G4 nulls. Secondary power/SNR at G₄ = 539.9 s and sub-harmonic ladder {5, 10, 15, 30, 45} s reported as compatibility checks only. Three Clocks never mixed. Residual discrete algebraic core (𝒪_res, packaging 18+521=539, K⁺, A4⁺/A5⁺, Option 3, No-Go) remains Category A and untouched.

## Brief ledger reminder
Exactly three generations of Standard-Model fermions force the M-theory non-perturbative superpotential W_np = e³. The 11D flux budget is N_flux = ⌊e³ × 3⁵⌋ = 4880. The Hampton Qutrit Collatz Convergence (HQCC) Theorem terminates in exactly 539 ± 1 steps. The gravitational breathing mode is G₄ = 539.90 ± 0.05 s. The primary resonant gravitational-wave signature appears in the master equations E_leak(t) and the template h(t) = h₀ sin(2π t / 539.90) × Θ(t − t_merger).

## 1. NANOGrav 15-year PTA analysis summary
The NANOGrav 15-year data set provides multiple lines of evidence for a stochastic gravitational-wave background (SGWB) in the nanohertz band:
- Hellings–Downs (HD) spatial correlations across 67 pulsars.
- Bayes factors > 10¹⁴ against independent pulsar noise models; 200–1000 against an uncorrelated common red-noise (CURN) process.
- Frequentist correlation statistics at approximately 3–4 σ.
- Characteristic strain amplitude A_GWB ≈ 2.4 × 10^{-15} at reference frequency 1 yr^{-1} under the fiducial spectral index γ = 13/3. Later chromatic-noise-model (CNM) re-analyses shift the amplitude slightly to ≈ 2.1 × 10^{-15} while preserving the HD detection.
- Preferred physical interpretation is a population of supermassive black-hole binaries (SMBHB). Early-universe exotic sources are not required by the data.

Public data products (timing residuals, full and epoch-averaged, whitened and un-whitened) are available via Zenodo DOI 10.5281/zenodo.16051178 and nanograv.org. Residuals are irregularly sampled with typical cadence of days.

## 2. Frequency-band comparison
- NANOGrav / PTA sensitivity window: approximately 1–100 nHz.
- Model G₄ fundamental frequency: 1/539.90 ≈ 1.8527 mHz (LISA band and the hard-falsification target for LIGO O5 QPO searches).
- The two bands are separated by more than six orders of magnitude. An exact, sub- or super-harmonic search for the 539.9 s period inside PTA residuals is therefore a high-frequency control test only. After conversion to even sampling at 1-day cadence the Nyquist frequency remains in the microhertz range, precluding reliable recovery of a 1.85 mHz tone.

## 3. R-FFT-539.9 free-first results on staged synthetic datasets
All staged series (fs = 1 Hz, length ≈ 21 596 samples ≈ 40 cycles of G₄) were processed with the free-first protocol: Kaiser window, zero-padded FFT, quadratic peak refinement, and phase-scramble null diagnostics. Preconditioned and scrambled-G4 modes were run only for secondary comparison.

| Series              | free_T (s)   | free_f (Hz)     | power_G4     | SNR_G4   | discovery_claim_allowed | Notes |
|---------------------|--------------|-----------------|--------------|----------|-------------------------|-------|
| pure_G4             | 539.9        | 0.00185219      | high         | ~6270    | True                    | Exact recovery |
| AM_G4               | 539.9        | 0.00185219      | high         | ~3610    | True                    | Exact recovery |
| multi_harmonic      | 539.9        | 0.00185219      | high         | ~1920    | True                    | Exact + elevated ladder |
| G4_plus_noise       | 539.9        | 0.00185219      | high         | ~1040    | True                    | Exact recovery |
| off_target_600      | ≈599.9       | ≈0.001667       | low          | ~2.6     | True                    | Recovers injected 600 s |
| pure_noise          | ≈20.3        | ≈0.0493         | noise-floor  | ~4.0     | True                    | No G₄ peak |
| coloured_noise      | ≈17.7        | ≈0.0565         | noise-floor  | ~0.06    | True                    | No G₄ peak |

Sub-harmonic ladder powers are elevated only in constructions that intentionally contain them (multi_harmonic). Phase-scramble nulls destroy coherent power at 1/G₄, confirming that elevated secondary scores require phase coherence.

These free peaks constitute Category A digital-signal-processing results. Any interpretation that a free period near 539.9 s confirms the S²-11DM²ET-X flux period, holographic enforcement, or brane-leakage clock remains Category B.

## 4. Protocol for future NANOGrav residual analysis
1. Download residual tables from Zenodo 10.5281/zenodo.16051178 or nanograv.org.
2. Parse MJD and residual columns.
3. Convert to evenly sampled series with `nanograv_residual_to_even(t_mjd, residual_us, target_dt_days=1.0)`.
4. Run free-first R-FFT-539.9 (unrestricted peak + nulls).
5. Only after free discovery stage examine secondary G₄ / ladder compatibility scores.
6. Label any secondary score Category B; sampling precludes reliable exact recovery of the 1.85 mHz tone.

## 5. Consistency with prior constraints and hard falsifiers
The large-scale white-noise (LSWN) bound of Barenboim & Stebbins (arXiv:2607.27338) already limits high-redshift stochastic gravitational-wave power that could redshift into the PTA band (z_*^{2} Ω_GW^{0} < 5 × 10⁷ (f*/nHz)^{3/2}). The NANOGrav SGWB is therefore consistent with a late-time astrophysical (SMBHB) origin.

The model’s primary resonant signature—the G₄ = 539.90 s breathing mode locked by the HQCC theorem and expressed in E_leak(t) and the h(t) template—remains an independent late-time prediction subject to the hard falsifiers:
- LIGO O5 (2026–2028): >5σ QPO at 539.90 ± 0.15 s,
- LISA: monochromatic line at 1.8527 ± 0.0009 mHz.

Residual discrete algebraic structure is untouched. Continuum claims linking the PTA signal to early-universe D2-brane leakage or PBH phase shifts remain Category B.

## Files and engine reference
- Canonical engine: docs/S2-11DM2ET-X-Axiomatic-Book/scripts/r_fft_5399.py (functions full_r_fft_analysis, scrambled_g4_control, …).
- Loaders: R-FFT/loaders/r_fft_public_loaders.py (includes nanograv_residual_to_even).
- Registry: R-FFT/registry/Dataset_Registry.md (Observatories section updated with NANOGrav free-first status).
- Results convention: free-first JSON outputs under R-FFT/results/ (or mirrored artifacts/RFFT_datasets/results/).

All integrals, sums and the three-generation axiom remain exact. No free parameters are introduced.
