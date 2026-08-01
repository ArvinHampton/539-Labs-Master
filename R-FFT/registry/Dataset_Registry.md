# R-FFT-539.9 Dataset Registry
**Date:** 2026-08-01 (updated Observatories edition)  
**Engine:** free-first R-FFT-539.9  
**Change log:** 2026-07-27 initial expanded observatories; 2026-08-01 added INTEGRAL/SPI 511 keV and PhysioNet EEG formal entries; results/ convention noted.

## Binding rule (mandatory)
Every series MUST be run with the free estimator + phase-scramble / scrambled-G4 nulls first.  
discovery_claim_allowed opens only for free, non-scrambled runs.  
Preconditioned lock is secondary, labeled compatibility only.

## Staged datasets (ready now under artifacts/RFFT_datasets/ and mirrored on Drive / 539-Labs-Master)
- synthetic/pure_noise.npz (+ .csv sample)
- synthetic/pure_G4.npz
- synthetic/G4_plus_noise.npz
- synthetic/off_target_600.npz
- synthetic/AM_G4.npz
- synthetic/coloured_noise.npz
- synthetic/multi_harmonic.npz
- internal/multi_k_residual_placeholder.npz (quantum-domain placeholder)

All synthetic series: fs = 1 Hz, duration ≈ 40 × 539.9 s (≈ 21 596 samples).

## Observatories section

### 1. LIGO (Hanford H1 + Livingston L1)
- Best public access: GWOSC (gwosc.org) + GWpy / NDS2 (nds.gwosc.org)
- Recommended for R-FFT: O3 second-trend auxiliary channels (1 Hz RMS)
  Example channels:
  - H1:ISI-GND_STS_ITMY_Z_BLRMS_30M_100M.rms
  - L1:ISI-GND_STS_HAM5_X_BLRMS_100M_300M.rms
  - H1:ISI-GND_BRS_ETMY_RX_BLRMS_30M_100M.rms
- Sampling notes: second-trend data are already 1 Hz; ideal for ~540 s searches. Full set ~61 GB; fetch individual channels.
- Free-first: required. Treat any peak near 539.9 s as Category B interpretation until independent replication.

### 2. Virgo (V1)
- Best public access: GWOSC open data (same portals as LIGO)
- Strain and selected auxiliary / DQ channels available for O3/O4 periods.
- Sampling notes: strain is high-rate (need downsampling to ≤1 Hz for long continuous segments). Auxiliary channels vary.
- Free-first: required. Same discovery gate as LIGO.

### 3. KAGRA (K1)
- Best public access: GWOSC where released for joint observing runs.
- Sampling notes: similar to Virgo/LIGO; prefer low-frequency or trend products if available.
- Free-first: required.

### 4. GEO 600
- Best public access: limited open segments via GWOSC.
- Sampling notes: useful mainly for short comparison segments; not primary long-baseline target.
- Free-first: required.

### 5. NANOGrav (and related PTAs)
- Best public access: nanograv.org/science/data and Zenodo (15-year DOI 10.5281/zenodo.16051178, 12.5-year releases)
- Data products: TOAs, post-fit residuals (ASCII, both full and epoch-averaged, whitened and un-whitened), correlation matrices.
- Sampling notes: residuals are irregularly sampled (cadence typically days). Convert to evenly sampled residual vector (linear interpolation or binning) before R-FFT. Native sensitivity is nanohertz; 539.9 s lies well above the usual PTA band and serves mainly as a control or super-harmonic check.
- Free-first: required. Any claimed short-period feature must be tested against the free estimator + nulls.

### 6. Event Horizon Telescope (EHT / M87*)
- Best public access: CyVerse Data Commons (polarised visibility releases), accompanying papers (2017/2018/2021 epochs).
- Sampling notes: sparse VLBI campaigns (days within a week, years between campaigns). Continuous 1 Hz series do not exist. Possible proxies: published polarisation-fraction or EVPA time series, or multi-year polarity-flip monitoring light curves constructed from the literature.
- Free-first: required. Multi-year polarity changes are interesting for the model’s 539.9-day claims but cannot be treated as continuous 540 s searches without explicit proxy construction and labeling.

### 7. PhysioNet EEG (CHB-MIT and related)
- Best public access: PhysioNet (CHB-MIT Scalp EEG Database and other continuous EEG sets).
- Sampling notes: typically 256 Hz; one-hour segments contain only ~6–7 cycles of 539.9 s. Decimation or longer multi-hour recordings recommended for any secondary G4 check.
- Free-first: required. Free peaks commonly land in the EEG band. Secondary G4 metrics stay compatibility only.
- Status: converter and one live CHB-MIT run already performed (free peak ~32 Hz; secondary non-significant).

### 8. INTEGRAL/SPI 511 keV positron annihilation
- Best public access: A&A papers (Yoneda et al. 2025, Siegert & Yoneda 2026) and INTEGRAL archive.
- Sampling notes: primarily spatial maps; time-binned flux light curves (if constructed) would be required for free-first spectral search. High-latitude hotspots and possible 2–3× higher rate reported.
- Free-first: required if any continuous or evenly sampled time series is available. Spatial features alone are not spectral claims.
- Model link remains Category B (possible outflow / leakage interpretation).

### 9. Other (deferred or secondary)
- DESI voids, Planck residuals, muon g-2 wiggle residuals, JWST monitoring: not continuous high-cadence observatory time series at the required sampling; treat only if a concrete evenly sampled residual vector is published and can be staged.

## Public datasets (loader only – fetch locally)
Use the expanded loaders in loaders/r_fft_public_loaders.py (and the fuller observatory_data loaders in 539-Labs-Master) on the machine that has the R-FFT script and network access. Full bulk archives are not staged here because of size.

## Results convention
All free-first run outputs (JSON preferred) should be placed under RFFT_datasets/results/ (local) and mirrored to the corresponding Drive / GitHub location.

## Free-first reminder
1. Load series  
2. Run free mode + nulls (phase-scramble / scrambled-G4)  
3. Only if discovery_claim_allowed = True examine secondary model metrics (power_5399, μ-style quantities, etc.)
