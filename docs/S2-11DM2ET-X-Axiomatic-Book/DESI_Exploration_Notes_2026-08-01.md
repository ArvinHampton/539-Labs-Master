# DESI Exploration Notes — 2026-08-01

**Context:** User navigated the public DESI Data Archive (desi.lbl.gov) in search of datasets for R-FFT-539.9 analysis.

## Directory Structure Observed

### Top-level /public/dr1/
- spectro/
- survey/
- target/
- vac/
- LICENSE.md
- README.md

### /public/dr1/vac/ (Value-Added Catalogs)
Key subdirectories identified:

- agngal/
- agnqso/
- bao-cosmo-params/
- cigale/
- civ-absorber/
- desivast/
- dla-cnn-gp/
- dla-toolkit/
- emfit/
- extragalactic-dwarfs/
- fastspecfit/
- full-shape-bao-clustering/
- full-shape-cosmo-params/
- gfinder/
- hetdex/
- lsdr9-photometry/
- lss/
- lya-correlations/
- lya-deltas/
- mgii-absorber/
- mws/
- mws-bhb/
- mws-spdist/
- mws-specdis/
- qmassiron/
- skyspec/
- stellar-mass-emline/
- stellar-reddening/
- strong-lensing/
- zlya/

## Priority Targets for R-FFT-539.9

1. **bao-cosmo-params/** — BAO cosmology parameters and associated power spectra / chains.
2. **full-shape-bao-clustering/** — Full-shape BAO clustering measurements (highest priority for periodicity search).
3. **full-shape-cosmo-params/** — Complementary full-shape cosmology parameters.
4. **lya-deltas/** and **lya-correlations/** — Lyman-alpha forest density field products.

## Analysis Protocol Reminder

- Free spectral estimate first (Kaiser window, zero-padded FFT or equivalent, no 539.9 injected).
- Report free peak period + uncertainty + null significance.
- Only after free estimate is frozen, report secondary compatibility metrics (power_5399, snr_5399).
- See R_FFT_5399_Validation_Protocol.md for binding rules.

## Status

Awaiting user download of specific files from the priority folders so that numerical R-FFT-539.9 can be executed on real DESI data products.
