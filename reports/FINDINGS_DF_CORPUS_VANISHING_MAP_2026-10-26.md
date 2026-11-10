# FINDINGS — Dataset Filtration lane: corpus vanishing sweep — 2026-10-26 America/Chicago
**Status: COMPLETE** (DF lane only; inventory/cite only, no new physics). Authority: OWNER VOICE LOCK via Physicist. Soft SF invent HOLD tip fill else. Soft SF F3 CLOSED. No tip fold. **tip_touched NO.**

## Pins
| Pin | Value |
|---|---|
| tip Soft SF LOCK (expected) | `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` |
| tip path hashed | `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` → `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` **MATCH** |
| Sibling (modular P5a rows, not re-inventoried) | MR2-FINDINGS-CORPUS-VANISHING-MAP_2026-10-26.md; grok-batches/LOCAL-VANISHING-MAP_2026-10-26.md |
| Sweep method | read-only; npz keys/shapes/zero-count/NaN-count by numpy; grep zero/null/absent/vanish/κ/k on md/json/csv |

## Key finding up front
**No dataset/filtration file states a vanishing, dim 0, or zero-count at any modular weight κ or k.** κ = ABSENT everywhere in this lane. The only "k" is the label `multi_k` (multi-k style dynamics); no numeric k value is given. The lane's "vanishing" signatures are all empirical: exact zeros in arrays, null/blank fields, absent fields, absent datasets, and near-zero ratios.

## Inventory
| ID | Claim | Space / object | κ | k | Status | Path (sha256) | Backwards: what filtered-out absence produces it |
|---|---|---|---|---|---|---|---|
| DF-1 | t[0]=0 in each npz (1 zero/array) | `t` arrays of all 8 time-series npz (21596 or 2700 samples) | ABSENT | ABSENT | zero-count=1 (trivial) | datasets/*.npz e.g. pure_G4 `d9ecffec9ff64f451247faf13e995f202ac09ba306affbf636cb05f001c99ade` | Time origin at 0; this is the start of the time axis, not a physical vanishing |
| DF-2 | signal has exactly 1 zero | `pure_G4.signal = 0.5 sin(2πt/539.9)` | ABSENT | ABSENT | zero-count=1 | pure_G4.npz `d9ecffec9ff64f451247faf13e995f202ac09ba306affbf636cb05f001c99ade`; INDEX `b70e6a64e49d685e44f2ec92163a8e7b01d9fbb8242c54986b75f5d648298a1b` | No noise term → sin(0)=0 at t=0 exactly. Other series have noise/AM so the exact zero goes away (zero-count 0) |
| DF-3 | No 539.9/540 peak | `pure_noise`, `coloured_noise` (dominant ~148 s) | ABSENT | ABSENT | null (by design) | INDEX `b70e6a64…`; pure_noise `45a0d09c970827b554e20c334658394de9552dbf0bd9a974281e5791f177edf4`; coloured `299633f2939a19f8fcc4ef4ca9c0003eccb86fe07b3610973dfbcc8bc0f0fe0e` | No G4 tone was put in → the G4 bin is empty. These are null controls under the free-first rule |
| DF-4 | 539.9/540 bins weak | `off_target_600` | ABSENT | ABSENT | near-null control | off_target_600 `32593a6d22dba1d005d6a3abb5fa9203b7bf05d0b9b14ccfbc4e1692babd3732` | Tone is at 600 s, so 539.9 is missing → that bin has almost no power |
| DF-5 | 539.9 and 540 fall in the same FFT bin (bin 40) | G4 suite, N=21596, fs=1 | ABSENT | ABSENT | degenerate (no FFT separation) | INDEX `b70e6a64…` | Window = 40×539.9 is too short to separate 1/540 from 1/539.9 → the difference can't be seen by FFT; only the LSQ fit breaks the tie |
| DF-6 | Not a clean tone; "Not a real experimental residual" | `multi_k_residual_placeholder` (fs 0.5, N 2700, 5399 s) | ABSENT | "multi-k" (no numeric k) | PLACEHOLDER / OPEN | npz `9b4ea0eac43f72ea82c8f624a3b62f46705fc6d7c63b219f616e3b8db9e9d815`; manifest_multi_k `9b03a2fe9f590a70107a61d23994adbccad8fc59947b0684145ee6b63d2b6dd2` | The real T3/multi-k residual has not been extracted ("Replace with real … once extracted") → the slot holds placeholder data. Any null result here does not count as a k-vanishing |
| DF-7 | No period / 539.9 / 540 field | `Periodic_Table_Full_Results` (Z, IE_model, IE_exp; 118 rows; zero-count 0, NaN 0) | ABSENT | ABSENT | ABSENT field | `7ee15235db7dfdb06497821552e4f3ff74524970ae6ba27d18839074cf8b94d1` | Only ionization-energy columns were exported → there is no period field |
| DF-8 | T3 14-step, max 55, r=(61/1001)², HQH 18+521 not in registry | Dataset_Registry vs 2026-08-16 freeze | ABSENT | ABSENT | ABSENT (and CONFLICT for no-free-539 / 540 s) | INDEX `b70e6a64…`; Registry.md `b19dcfc81516d422e9489ada064d3e66dc0634c4373c874abdba9663b2deb215`; .json `e9c6b34178d145d04dc516aee381a944125104bf27f0a204e28df200f9922753` | Registry is the pre-freeze (2026-07-27) catalog of observatories/R-FFT → freeze items were never written into it |
| DF-9 | Discovery claim gated | All R-FFT series | ABSENT | ABSENT | null-first (gate) | Registry.md `b19dcfc8…` | Free estimator + scrambled-G4 nulls run first; when the null is not beaten, the discovery claim is not allowed |
| DF-10 | Continuous 1 Hz series do not exist (EHT); DESI/Planck/g-2/JWST deferred | Observatory catalog | ABSENT | ABSENT | ABSENT data | Registry.md `b19dcfc8…` | Sparse VLBI cadence, plus no evenly sampled residual published → there is no input series |
| DF-11 | SOHO/VIRGO FITS staged; "Residual discrete algebra is untouched"; 539.9 stays Cat B | soho-virgo/ (5 FITS, DOWNLOAD_STATUS=COMPLETE) | ABSENT | ABSENT | OPEN (not analyzed) | MANIFEST.md `b0f5910fb7eab068c56f7a6d3db296195299af667e95ed96274c81af5d1a63e6` | No R-FFT run on the FITS (not opened in this sweep, multi-GB) → there is no result, not a null |
| DF-12 | "Separate public data repositories (raw experimental entanglement datasets): 0 found"; RTA relation NONE | Entanglement datasets catalog | ABSENT | ABSENT | zero-count=0 / ABSENT | catalog `af2539b05b24b48559c43a95ac00848650d0c3f19c20674bb24c3ab338a7b99c`; LOCK_SUPERSEDE `8c3cde92dc6686b433880b268193c06c54ffdeee302beb141428e74b38e3ac1e` | Catalog only, invent-ban, and no raw data repository on the box → zero entries. Zenodo 18489291 is pointer-only and its entanglement content is UNVERIFIED |
| DF-13 | `nonzero_ROI` filter: mouse01 7693/7843 nonzero, mouse07 3013/4337 | RIKEN Ca²⁺ ROIs | ABSENT | ABSENT | zero-count: 150 and 1324 all-zero ROIs filtered out | ABC_FINDINGS `21ee4a9e73b7bcd1f37f96794ddaec0ebf0df1db2938b278cd926cdeb983c13d`; paper/manuscript.md | Silent/empty ROIs are dropped by `nonzero_ROI` → network uses only active cells. The dropped cells are what was absent |
| DF-14 | Raw top-1% NREM/wake ratio inflated by "near-silent wake cells" | per-neuron slow-wave ratio | ABSENT | ABSENT | near-zero denominator | ABC_FINDINGS `21ee4a9e…` | Wake power ≈0 → the ratio blows up; the robust cut (wake ≥5% of median) removes these cells |
| DF-15 | REM Ca band ratios near zero: mid_low 0.029/0.060, near_nyquist 0.0077/0.0064 vs wake | spectral_bandpower_summary (mouse01, example_1k) | ABSENT | ABSENT | near-zero (not exact) | csv `8a4e1ea3c589b352fd6a5afc683e5276dd17762241b78b7781c4cf79759aa459` | REM = one 549-frame bout (shorter than the 1500-frame window) plus near-Nyquist power at 7.65 Hz → the high band almost disappears; caveat 3 says not to trust REM |
| DF-16 | Blank (null) vs_wake / EEG columns | spectral_bandpower_summary rows | ABSENT | ABSENT | null fields | csv `8a4e1ea3…` | Wake is the reference (ratio to itself is left blank); Ca rows have no EEG and EEG rows have no Ca |
| DF-17 | Prior REM-delta 1.54× "hit" was not real | EEG, FrameTrigger | ABSENT | ABSENT | retracted (finding gone) | ABC_FINDINGS `21ee4a9e…` | Correct alignment (drop 150 pulses) removes a misalignment artifact → aligned REM δ is 0.63 |
| DF-18 | Classical delta not resolvable on Ca | Ca 7.65 Hz, Nyquist 3.825 | ABSENT | ABSENT | ABSENT band (truncated) | findings_summary `f16e0fef06a0efd6cee1c25e4d46f992c5c9b6542698ef920a69901430a63c64` | Sampling filters out >3.825 Hz → delta is cut to 0.5–3.775 |
| DF-19 | Zenodo 10.5281/zenodo.17667863 HTTP 403 | neural source | ABSENT | ABSENT | ABSENT (blocked) | findings_summary `f16e0fef…` | Network block → that source is missing from the analysis (RIKEN copy used instead) |

## Summary by κ / k
| κ | k | DF-lane vanishings |
|---|---|---|
| any | any | **None.** No dataset/filtration file gives κ, a numeric k, dim, or a modular vanishing |
| ABSENT | "multi-k" label | DF-6 placeholder only, OPEN |

## Backwards summary
1. **By design (null controls):** DF-3, DF-4, DF-9. The tone was left out, so the bin is empty.
2. **Resolution/sampling filters:** DF-5, DF-15, DF-18. Window length or Nyquist removes or merges a feature.
3. **Explicit data-quality filters:** DF-13, DF-14, DF-17. Zero ROIs, near-zero denominators, and a misalignment are removed.
4. **Never-written / never-staged:** DF-6, DF-7, DF-8, DF-10, DF-11, DF-12, DF-19. Here a missing source shows up as ABSENT, which is different from a measured zero.
5. **Trivial exact zeros:** DF-1, DF-2 (t=0, sin 0).

None of these is evidence for or against a modular vanishing at κ/k. They should not be mapped onto R1–R6.

## Gaps
- SOHO/VIRGO FITS not opened or analyzed here (≈2.9 GB). No zero/NaN counts for them.
- RIKEN `.mat` raw arrays were not re-counted in this sweep. The nonzero counts are cited from ABC_FINDINGS/manuscript.
- `regions/`, `network/`, `eeg_aligned/` json/csv were listed but only spot-checked through ABC_FINDINGS. No separate zero/null hits were recorded from them.
- Real multi-k residual is not extracted (DF-6), so there is no k-indexed dataset to sweep.
- No Drive re-pull in this sweep. Only box copies were used.

## Standing unchanged
Soft SF invent HOLD · F3 CLOSED · Bridge PARTIAL · READY NO · tip_touched NO
