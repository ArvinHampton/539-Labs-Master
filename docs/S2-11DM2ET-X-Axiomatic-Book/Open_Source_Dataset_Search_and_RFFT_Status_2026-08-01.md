# Open Source Dataset Search for R-FFT-539.9 and Status Update

**Date:** 2026-08-01  
**Status:** Expanded inventory; free-first analysis limited to staged synthetics in this environment. Category A free peaks on synthetics; Category B for any model interpretation. Residual discrete algebra untouched.

## Have we searched any and all?
No exhaustive search of every open time-series repository is possible or practical. The current Dataset_Registry covers the primary domains relevant to the S²-11DM²ET-X validation programme (GW strain/aux, PTA residuals, EEG, EHT proxies, INTEGRAL maps). An expanded web search on 2026-08-01 identified additional candidates listed below. Bulk import of all is not feasible here due to archive sizes (GBs–TBs), irregular sampling, or high sample rates requiring downsampling.

## Expanded candidate list (status: loader_only or candidate unless staged)
- GWOSC O4a / O4b open data (strain + auxiliary channels; loaders exist; prefer 1 Hz second-trend for G4 searches).
- Additional PTAs: EPTA DR2, PPTA DR3, InPTA DR2, IPTA combinations (public residuals; convert via even-sampling as for NANOGrav; control only).
- PhysioNet / OpenNeuro: Siena Scalp EEG, longer PSG, continuous BCI/EEG sets (decimate for secondary G4 checks; free peaks typically in EEG band).
- Geomagnetic: SuperMAG 1 s, INTERMAGNET, GMAG/CARISMA/IMAGE arrays, IGETS superconducting gravimeter hourly multi-year series.
- Seismic: IRIS continuous or SeisBench datasets (select long even segments).
- Solar / space weather: NOAA NCEI, SDO/HMI time series.
- Other geophysical continuous 1 s series (magnetotelluric storm windows, etc.).

## What has been analyzed free-first
- All staged synthetics (pure_G4, AM_G4, multi_harmonic, G4_plus_noise, off_target_600, pure_noise, coloured_noise): free_T recovers 539.9 s exactly when the tone is injected; recovers injected off-target when present; recovers unrelated short periods in pure noise. Phase-scramble nulls empty the G4 power. Documented in NANOGrav_PTA_and_RFFT_Harmonics_Analysis_2026-08-01.md.
- NANOGrav: protocol and frequency-mismatch control only (no full residual import here).
- One prior CHB-MIT EEG segment noted in registry (free peak ~32 Hz; secondary non-significant).

## Protocol for future imports
1. Confirm even sampling or convert (nanograv_residual_to_even style).
2. Prefer segments with duration >> 540 s and fs >= 0.1–1 Hz for multiple G4 cycles.
3. Free estimator + phase-scramble / scrambled-G4 nulls first.
4. discovery_claim_allowed only for free non-scrambled.
5. Secondary G4 / ladder metrics compatibility only; Category B for model linkage.
6. Record under R-FFT/results/ and update registry.

## Consistency
Primary model signature remains the HQCC-locked G₄ = 539.90 s resonant flux in E_leak(t) and h(t). Hard falsifiers (LIGO O5 QPO, LISA 1.85 mHz line) unchanged. Expanded candidates do not alter residual discrete Category A core.

Engine: docs/S2-11DM2ET-X-Axiomatic-Book/scripts/r_fft_5399.py  
Loaders: R-FFT/loaders/r_fft_public_loaders.py  
Registry: R-FFT/registry/Dataset_Registry.md (to be updated with this inventory).
