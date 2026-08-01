# R-FFT Open-Source Dataset Search Expansion — 2026-08-01

**Status:** Expansion of the existing Dataset_Registry (2026-07-27 observatories edition) and Validation_Datasets_Draft.  
**Protocol remains binding:** Free-first unrestricted peak search + phase-scramble / scrambled-G4 nulls. Discovery only from free non-scrambled. Secondary G₄ = 539.9 s and ladder {5, 10, 15, 30, 45} s are compatibility only. Three Clocks never mixed. Category A (DSP) / Category B (model interpretation) mandatory.

## 1. Current Coverage (already registered)

- Staged synthetics (pure_noise, pure_G4, G4_plus_noise, off_target_600, AM_G4, coloured_noise, multi_harmonic): free-first analysis complete (exact recovery of 539.9 s when injected; null in noise).
- LIGO / Virgo / KAGRA: loaders for second-trend 1 Hz aux and downsampled strain (GWOSC / NDS2).
- NANOGrav 15-yr residuals: conversion stub + protocol (control only; nHz band).
- EHT / M87* proxies: sparse, literature-based.
- Notes on DESI BAO / voids, SoFIE-GEL flame radius, PhysioNet, INTEGRAL.

## 2. Newly Identified Open-Source Candidates

### Gravitational-wave and PTA
- GWOSC O4a / O4b calibrated strain + aux channels (public; large volume; prefer 1 Hz second-trends or downsampled segments).
- EPTA DR2 residuals and timing solutions (public GitLab / papers).
- PPTA DR3 (CSIRO / GitHub).
- InPTA DR2 (uGMRT dual-band).
- IPTA combined products when released.

### Solar / Space Weather
- NOAA / NCEI space-weather holdings (GOES, DSCOVR, magnetograms, flux).
- SDO / HMI magnetograms and continuum (JSOC public).
- SOHO multi-spectral (machine-learning-ready cubes available).
- SuperMAG geomagnetic indices (1 s).

### Biomedical / PhysioNet
- Siena Scalp EEG Database (open access).
- Other open PhysioNet EEG / polysomnography continuous recordings (Motor Movement/Imagery, CAP Sleep, etc.).
- Longer continuous series preferred for multiple G₄ cycles.

### Other
- INTEGRAL public data results catalog and science windows (511 keV maps / light curves via ISDC / HEASARC).
- Superconducting gravimeter residuals (IGETS network, hourly multi-year).
- SeisBench / IRIS continuous seismic (secondary).

## 3. Import and Analysis Status

- Full bulk download and staging of multi-GB / multi-TB archives (GWOSC O4, full SDO, long EEG) is not performed in this environment (size and network limits).
- Loaders already exist or can be extended for GWpy / NDS2, residual-to-even conversion, and proxy construction.
- Free-first R-FFT can be run locally on any even-sampled continuous segment of sufficient length (≥ several G₄ cycles, preferably ≥ 40).
- Synthetics remain the only fully staged and analyzed set; results stand as Category A free peaks matching construction.

## 4. Recommended Next Actions (local machine)

1. Extend Dataset_Registry.json with the new candidates as "loader_only" or "candidate".
2. Fetch representative short continuous segments (e.g., O3/O4 1 Hz aux of several hours, selected PTA residual series after even sampling, open PhysioNet EEG of multi-hour duration).
3. Run free-first + nulls; report free_T, power at G₄, discovery_claim_allowed.
4. Secondary compatibility only after free stage.
5. Push any new results under the same Cat A/B and residual-flux provenance rules.

## 5. Summary

We have not previously searched every conceivable open time-series archive. The present expansion lists the principal additional public sources relevant to long-baseline spectral search near the G₄ scale. Bulk import of all is deferred to local execution with the existing free-first engine. The residual discrete algebraic core remains Category A and untouched. Continuum interpretations remain Category B.
