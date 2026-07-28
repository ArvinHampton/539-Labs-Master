# Execution Summary — Closed Constants, Three Clocks, GW250114

**Status:** Complete  
**Date:** 2026-07-26 (session)

## What was executed

### 1. Formal resolution (already in book; extended)

| Asset | Path |
|-------|------|
| Resolution chapter | `Resolution_GW250114_ThreeClocks_ClosedConstants.tex` |
| Authoritative prose | `Resolved_BH_negPBH_GW250114_Statement.md` |
| Constants SSOT | `CLOSED_CONSTANTS.md` |
| Patcher script | `scripts/apply_closed_constants.py` |
| Machine log | `EXECUTION_LOG_closed_constants.json` |
| Book wiring | `\input` in `S2-11DM2ET-X_Axiomatic_Book.tex` after individuality |

### 2. Closed ratios (live everywhere canonical)

| Quantity | Exact |
|----------|-------|
| \(\kappa_{\mathrm{dark}}\) | \(243/539\) |
| \(f_{\mathrm{snap}}\) | \(243/4880\) |
| \(\beta_{\mathrm{PBH}}\) | \(11/61\) |
| Ring coeff | \(243/4880\) |

### 3. Corpus patch pass

- **Text** (tex/md): axiomatic book resolution, HQH539_spec, related docs  
- **DOCX:** 34 model drafts (pass 1) + 13 (pass 2) + 6 (pass 3) + residual cleanups under OneDrive Imports  
- **Theorems 1–61 Overleaf:** Global Lemma Core gains closed-ratio + three-clock lemmas  
- **Axiomatic HMT:** \(\rho_{\mathrm{snap}}=(243/4880)\rho_{\mathrm{DM}}\)  
- **FCPDE waveform:** \(\sin\) amplitude \(=\beta_{\mathrm{PBH}}=11/61\)  
- **HQH-539 spec table:** `KAPPA_DARK`, `BETA_PBH`, `F_SNAP` closed  
- **Left intentionally:** non-β uses of `0.18` (e.g. event duration \(t_E\) 0.18–0.55 s, fringe \(\Delta\mu\pm0.18\))  

### 4. Null-orbit lemma

Added `Lemma (Null-Orbit Reduction Sketch)` in the Resolution chapter: exterior Kerr photon sphere + snap-controlled fractional broadening \(\Rightarrow\) coefficient \(f_{\mathrm{snap}}=243/4880\). Full spin-dependent numerics deferred; no new free modulus.

### 5. Claim ladder (enforced)

1. **Definition** — BH as leakage portal  
2. **Consistency** — GW250114 = Kerr exterior on Clock I  
3. **Prediction** — Clock-III \(G_4\) modulation with \(\beta_{\mathrm{PBH}}=11/61\); ngEHT ring \(243/4880\)

## Explicitly not done / out of scope

- Regenerating all **PDFs** in Downloads (binary; source DOCX/tex updated where available)  
- Full Kerr geodesic **numerical** integration for every spin (lemma sketch only)  
- Publishing to Zenodo (requires your account / upload)  
- FPGA bitstreams or crypto golden vectors re-derived from new floats (spec table updated; re-run golden suite if needed)

## Re-run patcher

```powershell
python C:\Users\bradl\S2-11DM2ET-X-Axiomatic-Book\scripts\apply_closed_constants.py
```

## Public one-liner

> GW250114 confirms the Kerr exterior limit on geometric time; HQCC depth, \(G_4\), and negPBH are not measured by that event; \(\kappa_{\mathrm{dark}}\), \(f_{\mathrm{snap}}\), and \(\beta_{\mathrm{PBH}}\) are the closed ratios \(243/539\), \(243/4880\), \(11/61\).
