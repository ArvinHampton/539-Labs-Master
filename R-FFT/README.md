# R-FFT — Free-First Resonant FFT Observatory Package

**Date:** 2026-08-01  
**Project:** S²-11DM²ET-X / 539 Labs  
**Status:** Active

This directory contains the binding instructions, dataset registry, public loaders, staged synthetic series manifests, and results convention for the dedicated R-FFT Grok Agent.

## Contents

- `instructions/R-FFT_Grok_Agent_Instructions.md` — Binding agent protocol (free-first, Three Clocks, Category A/B)
- `registry/Dataset_Registry.md` — Human-readable observatory and staged-dataset registry
- `registry/Dataset_Registry.json` — Machine-readable registry
- `loaders/r_fft_public_loaders.py` — Synthetic + LIGO/Virgo/KAGRA/NANOGrav/EHT helper loaders
- `loaders/run_synthetics_free_first.py` — Example free-first runner stub for staged synthetics
- `synthetic/manifest.json` — Manifest of staged synthetic series (pure_noise, pure_G4, …)
- `internal/manifest.json` — Internal quantum-domain placeholder
- `results/` — Destination for free-first run JSON outputs

## Engine location

Canonical analysis engine:  
`docs/S2-11DM2ET-X-Axiomatic-Book/scripts/r_fft_5399.py`  
(functions `full_r_fft_analysis`, `scrambled_g4_control`, etc.)

Observatory runner and fuller loaders live under the same scripts tree.

## Protocol reminder

1. Free estimator + phase-scramble / scrambled-G4 nulls first.  
2. discovery_claim_allowed opens only for free, non-scrambled runs.  
3. Secondary G4 / ladder metrics are compatibility checks only.  
4. Three Clocks never mixed. Category A / B always explicit.  
5. Plain Text English responses.

Staged .npz / .csv binary data remain local / Drive-mirrored; this GitHub tree carries the text control plane and manifests.
