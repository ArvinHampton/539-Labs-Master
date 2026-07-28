# Empirical investigation of a period near 539.9

**Date:** 2026-07-26  
**Protocol:** `Empirical_PhaseLocking_Protocol.md`  
**Script:** `scripts/empirical_phase_lock.py`  
**Status of record:** ACE / No-Go unchanged (`ACE_Status_of_Record.md`)

---

## Design (pre-registered style; no 539.9 in estimator)

| Item | Choice |
|------|--------|
| Maps | \(T^\sharp\) (min-defect) and unrestricted \(T_3\) (separate runs) |
| Horizon \(N\) | \(4096 = 2^{12}\) (power of two; not a multiple of 539) |
| Seeds | 54 (fixed 20, 21, 243, 4880, … + random in \([10^6,10^{12}]\)) |
| Phase \(\Phi_t\) | \(\log_3 n + 0.35\bigl((n \bmod 27)/27 - 1/2\bigr)\) |
| Estimator | Ordinary periodogram after **linear detrend**; natural DFT grid \(f_k = k/N\) |
| Bootstrap | Residual bootstrap, \(B=400\) (publication default 2000); same grid |
| Null | Phase-randomisation, \(B_{\mathrm{null}}=100\) |
| 539.9 | **Only** in post-estimation compatibility |

---

## Primary results (no use of 539.9)

### Map \(T^\sharp\)

| Quantity | Value |
|----------|------:|
| \(\hat T\) median (across seeds) | **2.00** |
| \(\hat T\) mean | 2.48 |
| Ensemble median 95% CI | **[2.00, 3.00]** |
| Per-seed quantiles (q05–q95) | 2.00 … 3.00 |
| Median peak \(p\)-value (phase-rand) | ≈ 0.50 |

### Map \(T_3\) (unrestricted)

| Quantity | Value |
|----------|------:|
| \(\hat T\) median | **2.00** |
| \(\hat T\) mean | ~836 (heavy upper tail on a few seeds) |
| Ensemble median 95% CI | **[2.00, 2.00]** |
| Median peak \(p\)-value | ≈ 0.50 |

JSON: `empirical_phase_lock_results.json`, `empirical_phase_lock_results_T3.json`

---

## Compatibility (post-estimation only)

| Test | \(T^\sharp\) | \(T_3\) |
|------|:------------:|:------:|
| Claimed period | 539.9 | 539.9 |
| \(\lvert\hat T_{\mathrm{med}} - 539.9\rvert\) | **537.9** | **537.9** |
| Claimed inside ensemble 95% CI? | **No** | **No** |
| Fraction of seed CIs covering 539.9 | **0** | **0** |

**Conclusion of the hypothesis check:** under this phase observable, horizon, and maps, the data **do not** support a dominant period near **539.9**. Dominant spectral mass sits at **short** periods (order **2–3** steps), consistent with residue / mod-27 structure and with the ACE short depth scale (\(N_\star=14\)), not with a 539-step resonant carrier in \(\Phi_t\).

Phase-randomisation \(p\approx 0.5\) indicates that even the short-period peak is not strongly distinguished from a spectrum-preserving null for this observable.

---

## Interpretation (aligned with No-Go)

| Claim | Supported by this run? |
|-------|-------------------------|
| Strict short-scale structure in \(\Phi_t\) | Yes (periods ~2–3) |
| Dominant period ≈ 539.9 under \(T^\sharp\) / \(T_3\) + this \(\Phi\) | **No** |
| ACE / No-Go: 539 not forced by residue+towers+democracy | **Consistent** (empirical non-detection of 539.9 as dominant) |
| Need extra structure (fixed count, holographic window, phase-lock design) for long resonance | **Still required** if the model asserts 539.9 |

The long resonant claim is **not refuted for all observables** (a different pre-declared \(\Phi\) or holographic projection might be tested later), but it is **not recovered** by the protocol-default construction above.

---

## Reproduce

```powershell
# Publication-grade bootstrap
python S2-11DM2ET-X-Axiomatic-Book\scripts\empirical_phase_lock.py --N 4096 --seeds 64 --B 2000 --B-null 500 --map sharp

# Comparison map
python S2-11DM2ET-X-Axiomatic-Book\scripts\empirical_phase_lock.py --N 4096 --seeds 64 --B 2000 --map T3
```

---

## Bottom line

> Empirical investigation (protocol-compliant): **dominant period estimates cluster near 2–3, not 539.9.**  
> Compatibility with 539.9 **fails** for this design.  
> That is consistent with the canonical No-Go: pure residue + tower + \(T^\sharp\) dynamics yield short contraction structure; a period near 539.9 remains an **external hypothesis**, not a spectral fact of the raw completed map under the declared phase observable.
