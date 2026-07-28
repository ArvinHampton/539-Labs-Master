# R-FFT-539.9 Source Inventory

**Date of inventory:** 2026-07-27  
**Purpose:** Locate implementations and definitions of `full_r_fft_analysis` /  
R-FFT-539.9; record gaps; point to the ready-to-use redraft.

---

## 1. Ready-to-use implementation (this redraft)

| Path | Role |
|------|------|
| `scripts/r_fft_5399.py` | Canonical code: `full_r_fft_analysis`, `compare_precondition_modes`, Kaiser window, free / preconditioned / scrambled-G4 modes |
| `R_FFT_5399_Validation_Protocol.md` | Binding free-first reporting rules |
| `R_FFT_5399_Source_Inventory.md` | This file |

Public API (implemented here; **not** found pre-existing under that name):

```text
full_r_fft_analysis(series, dt, precondition=False, scrambled_g4_control=False, ...)
→ RFFTResult with:
   power_5399, snr_5399, refined_period, free_T_hat,
   echo_amplitude, echo_beta, mu_stability, kappa_dark,
   subharmonic_power, null_*, discovery_claim_allowed
```

---

## 2. Searched locations

| Location | Result |
|----------|--------|
| `C:\Users\bradl\S2-11DM2ET-X-Axiomatic-Book\` | Protocol + empirical scripts; **no** prior `r_fft_5399` / `full_r_fft_analysis` |
| `C:\Users\bradl\Desktop\539Labs\` | HQH-539 crypto/FPGA; constants and \(\Phi(t)\) theory; **no** R-FFT analysis module |
| `C:\Users\bradl` (workspace greps for `power_5399`, `snr_5399`, `full_r_fft`, `r_fft`) | No local Python definition of those identifiers |
| Public web / independent literature | No third-party primary source for this named pipeline |
| X / @539Labs | Deep-research cited primary post for Step-1 DSP snippet; live keyword fetch at inventory time returned no additional hits |

---

## 3. Supporting sources that *do* exist (constants, protocol, theory)

| Source | Path / ref | What it supplies |
|--------|------------|------------------|
| Closed constants | `CLOSED_CONSTANTS.md` | \(G_4\), \(\kappa_{\mathrm{dark}}\), \(\beta_{\mathrm{PBH}}\), clock split |
| HQH-539 spec | `Desktop\539Labs\docs\HQH539_spec.md` | G4, \(\Phi(t)\), ladder, \(\mu\), crypto note that \(\Phi\) is theoretical only |
| Empirical phase-lock protocol | `Empirical_PhaseLocking_Protocol.md` | Free-first spectral rules; forbidden filters; bootstrap / phase-rand nulls |
| Empirical phase-lock code | `scripts\empirical_phase_lock.py` | Protocol-compliant periodogram + residual bootstrap + phase-rand \(p\)-value |
| No-Go / ACE | `NoGo_Theorem_Canonical.md`, `ACE_Status_of_Record.md` | Limits on selling model structure as free dynamics |
| Theorems ledger | `Downloads\S2_11DM2ETX_Theorems_1-61_Overleaf.tex` | \(\zeta^t\), ladder, \(G_4\) uniqueness claims |
| Resolution note | `Resolution_GW250114_ThreeClocks_ClosedConstants.tex` | Three-clock separation |
| Resonant Path excerpt | `Downloads\Resonant_Path_Problem_Whitepaper_Excerpt.md` | Phase-lock as kinematic / hardness structure, not matched-filter DSP |

---

## 4. Explicit gaps (from deep-research + this inventory)

| Claimed / expected item | Status |
|-------------------------|--------|
| Pre-existing `full_r_fft_analysis` in workspace | **Missing** — supplied by `scripts/r_fft_5399.py` |
| Local `power_5399` / `snr_5399` implementation | **Missing** prior to redraft |
| “Category A/B” labels on FFT stages | **Not found** as FFT categories (used elsewhere for crypto / proprietary claims) |
| Median noise-floor SNR | **Not supported** by cited R-FFT description; redraft uses **mean** \(\lvert X\rvert^2\) |
| Named `scrambled-G4` API in older materials | **Not found**; implemented as `scrambled_g4_control` + `n_null` phase-scramble |
| Complete posted snippet with bound `G4` | Fragment was incomplete; redraft binds `G4 = 539.9` explicitly |
| Independent peer-reviewed DSP paper for R-FFT-539.9 | **Not found** |

---

## 5. How to extend if a missing primary source appears

If an original notebook, gist, or @539Labs post with a fuller `r_fft_5399` body is recovered:

1. Diff against `scripts/r_fft_5399.py` (window formula, SNR definition, refine loop).  
2. Prefer **documented behaviour** from the validation protocol over silent changes.  
3. Keep `discovery_claim_allowed` gating intact unless the protocol is formally revised.  
4. Append the recovered URI and SHA-256 of the file to this inventory.

---

## 6. Smoke-test command

```bash
cd S2-11DM2ET-X-Axiomatic-Book/scripts
python r_fft_5399.py --demo --N 8192 --n-null 32 --json-out ../r_fft_5399_demo_results.json
```

Expect: free / preconditioned / scrambled summary printed;  
`discovery_claim_allowed` True only for the free leg.
