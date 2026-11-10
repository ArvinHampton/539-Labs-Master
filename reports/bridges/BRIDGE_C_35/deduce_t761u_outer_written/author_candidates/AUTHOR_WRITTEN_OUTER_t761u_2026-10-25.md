# AUTHOR-WRITTEN outer_even / outer_odd — defs + menu (t761u, 2026-10-25 CDT)
Status: AUTHOR-WRITTEN draft — NOT Cat A until Arvin ACCEPT + Auditor CONFIRM. Inventory #2 of MASTER 544de792….
Basis: AW-α (χ AW-1a-0, ϑ AW-2a, n=1, N_trunc=106; deduce_t761u_accept RESULTS 3aae6f19…; Auditor MATCH pending). NOT AW-X4.

## 1. WRITTEN catalogue (verbatim sources; not invented)
- WRITTEN (HD e60cad9b… L16–18): even sector k=2m, m≥1: q^{outer_even(m)} · partial theta a=7m; outer_even(m) = 35m² + 7m (unit residual coefficients).
- WRITTEN (HD e60cad9b… L20–22): odd sector k=2m+1, m≥0: q^{outer_odd(m)} · partial theta a=7m+7/2; outer_odd(m) = 35m² + 42m + 49/4 (unit residual coefficients).
- WRITTEN (HD 552541cf… L20–22): Ξ_even=Σ_{m≥0} outer_even_coeff(m)·Θ_{3/2}(·;a=7m); Ξ_odd=Σ_{m≥0} outer_odd_coeff(m)·Θ_{3/2}(·;a=7m+7/2); tables "obtained by expanding…" (not tabulated).
- WRITTEN (HD 1bab65c4… L15–17): even (m≥1) 42, 154, 336, 588, 910, 1302, 1764, 2296, …; odd (m≥0) 12.25, 89.25, 236.25, 453.25, 740.25, 1097.25, 1524.25, ….
- DEDUCED (logs/outer_dedcheck.log, scripts/outer_check.py): formula reproduces all 15 listed 1bab65c4 values; |ledger_exp| (xi_written exponent_parity_check.log, k=0..11 under AW-α χ) = outer_{parity(k)}(⌊k/2⌋) for all k≥0. Arithmetic only.

## 2. Gaps needing AUTHOR pick
- G-O1 even m-range: e60cad9b/1bab65c4 say m≥1; 552541cf says m≥0. Under AW-1a-0, k=0 (m=0) included with outer_even(0)=0.
  - O-1a include m=0 (align AW-α) [rec]
  - O-1b exclude m=0 (align e60cad9b)
- G-O2 sign/link: HD product uses q^{+outer}·Θ; ledger under AW-α uses q^{-outer}·ϑ; |ledger_exp| = outer (DEDUCED).
  - O-2a KEEP ledger form only: outer_* tabulated as |ledger exponent| under AW-α χ; NO claim ledger≡HD [rec; soft SF if ≡ claimed]
  - O-2b KEEP HD product form only: q^{+outer} unit; tables from 1bab65c4 values; ledger path separate
  - O-2c AUTHOR-link both via completed-square Q_7 (xi_written G-2); still NOT AW-X4 unless Arvin separately accepts sign resolution
- G-O3 tables:
  - O-3a schema-only EMPTY table `m | outer_even(m) | outer_odd(m) | sector` (formula fills; no new invent) [rec]
  - O-3b fill first N rows from Written formula (unit coeffs; DEDUCED, not invented)
  - O-3c HOLD tables ABSENT (formula cite only)
- G-O4 coeff vs exponent:
  - O-4a identify outer_*_coeff = unit, exponent = outer_* (Written "unit residual coefficients") [rec]
  - O-4b leave coeff symbolic, separate

## 3. MENU for Arvin
- O-α ACCEPT all recommended: O-1a + O-2a + O-3a + O-4a
- O-β ACCEPT subset (list items)
- O-γ REVISE (notes; e.g. O-1b, O-2b, O-3b)
- O-δ REJECT — hold outer_* formula-cite only; tables stay ABSENT
- O-X4 (OPTIONAL, SEPARATE): same as AW-X4 — ACCEPT ledger≡HD; requires resolving G-2; NOT implied by O-α.

## Bans honoured
No AW-X4 / ledger≡HD Cat A; G-A3 not reopened; 4da09dec… not revived; no Ξ Fourier coeffs beyond outer_* formula values; δ≡0/Bridge YES not forced; no nonlocal; no order78.
