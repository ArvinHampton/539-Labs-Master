# Validation Datasets Draft — 2026-08-01

**Status:** Working draft compiled from conversation and project memory.  
**Purpose:** Identify existing public datasets suitable for R-FFT-539.9 free-first analysis and model compatibility checks.  
**Rule:** Free spectral estimate first (no 539.9 in estimator). Preconditioned mode is secondary compatibility only. See R_FFT_5399_Validation_Protocol.md.

---

## 1. Current Draft List of Validation Datasets

### 1.1 Microgravity Flame Physics (ISS SoFIE-GEL)
- Long-burn spherical flame radius time-series (up to ~336 s)
- Monotonic √t growth + radiative extinction observed
- High-cadence video-derived radius data ideal for isotropic diffusion + resonant ripple tests
- Access: NASA Combustion Integrated Rack / SoFIE project pages; associated papers and supplemental data
- Status: Candidate for free FFT on radius time series

### 1.2 DESI Large-Scale Structure
- DR1 / DR2 / DR3 BAO power spectra and void catalogs
- Full-shape clustering measurements
- Void fraction η_void ≈ 0.15 and BAO wiggles
- Public archive: https://data.desi.lbl.gov/public/dr1/vac/ (and later releases)
- Key subfolders identified in conversation: bao-cosmo-params/, full-shape-bao-clustering/, lya-deltas/, etc.
- Status: Primary candidate for binned power-spectrum / redshift-series periodicity search

### 1.3 M87* Multi-Wavelength Data
- NASA Chandra + Hubble + ALMA sonification waveform (spatial left-to-right scan of composite image)
- EHT polarized images and multi-epoch monitoring
- Multi-wavelength light curves
- Status: Sonification itself is spatial, not temporal; raw monitoring light curves preferred for temporal analysis

### 1.4 Gravitational Wave & Echo Data
- LIGO O4 public strain data (gwosc.org)
- Potential ringdown echoes and stochastic background searches
- Status: High priority for free spectral search of long strain segments

### 1.5 Supporting / Secondary Datasets
- Muon g-2 final result (FNAL)
- GRB power spectra (e.g., GRB 250702B references)
- Atomic clock stability records
- Planck CMB low-ℓ anomalies
- ALMA / Chandra monitoring of M87*

---

## 2. DESI Exploration Notes (Conversation 2026-08-01)

User navigated:
- https://data.desi.lbl.gov/public/dr1/vac/
- Subdirectories: agngal/, agnqso/, bao-cosmo-params/, cigale/, civ-absorber/, desivast/, dla-cnn-gp/, dla-toolkit/, emfit/, extragalactic-dwarfs/, fastspecfit/, full-shape-bao-clustering/, full-shape-cosmo-params/, gfinder/, hetdex/, lsdr9-photometry/, lss/, lya-correlations/, lya-deltas/, mgii-absorber/, mws/, qmassiron/, skyspec/, stellar-mass-emline/, stellar-reddening/, strong-lensing/, zlya/

Most relevant for R-FFT:
- bao-cosmo-params/
- full-shape-bao-clustering/
- full-shape-cosmo-params/
- lya-deltas/ and lya-correlations/

These contain processed BAO power spectra, correlation functions, and cosmology parameter chains that can be converted into time/redshift series for free spectral analysis.

---

## 3. Recommended Immediate Actions

1. Download representative files from bao-cosmo-params/ or full-shape-bao-clustering/.
2. Extract numerical time/redshift-binned series.
3. Run free-first R-FFT-539.9 (precondition=False).
4. Report free peak period, bootstrap CI, and null fraction before any compatibility check against 539.9 s.
5. Only then report secondary power_5399 / snr_5399.

---

## 4. Provenance

- Compiled from conversation screenshots of desi.lbl.gov and prior validation dataset discussions.
- Residual-flux provenance mandatory for any continuum interpretation.
- Category A: discrete residual algebra and packaging remain untouched.
- Category B: any continuum / G4 / leakage interpretation of spectral results.

**Next:** User to supply specific downloaded FITS / table files or extracted time series for numerical execution of the pipeline.
