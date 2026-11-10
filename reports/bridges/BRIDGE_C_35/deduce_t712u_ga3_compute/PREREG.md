# deduce_t712u_ga3_compute — PREREG (written before RESULTS; frozen)
Stamp: 2026-10-25 CDT. Scope: Local Bridge C only (local modular). CORE_FREEZE; SF-W7-3; Residual-vs-Resonant lock; no nonlocal EH11D/Ω₁₁D/F_total; no order78.

## Authority
- t712s4471 AUTHOR AUTHORIZE (Arvin via Physicist): G-A3-only compute. Lifts "new table" ban for THIS h-table only (schema 8d247feb4f1b644dfbaf1d28237eaddfe9ba45c82d40464a2290d4721b0f8051). Source class (C) AUTHORIZED compute. Invent-ban holds everywhere else. Filled values NOT Cat A until Arvin ACCEPT.

## Baselines (not reopened)
Draft CONFIRM 62283038…; t708u PREREG 5c65afec… / RESULTS 1c0e12ca… / SUMS 483cd14e…; STREAM-pre 67e4b8311905f9375ba0485892817f754b397bccaadd69a06e24b0c623705057; inventory-pre d9f692de8e11c84790c30575f1a70a8858a064d24f9cead30856707adf26e27c (60/60). Selectors Cat A FINDINGS 437d4571… / RESULTS f36beeea… (candidate 3d502756…). G-A1b CLOSED FINDINGS b34aebe6… / RESULTS e5b65693… (candidate 05040988…). P-B3 5f60d40f….

## Sample set
x ∈ {1/7, 3/7, 5/7, 1}; W_7x ∈ {−1, −1/3, −1/5, −1/7} (7368b855 L44).

## Compute plan (corpus inputs only; no invented coeffs/trunc/path/ψ)
- h^{high}(x) = ψ(x)/√i − ∫_path Ξ_N(w)(w−x)^{−1/2} dw (be1faa52 L43; 3957bc4 §3).
- Ξ_N: locked Ξ coefficient table (be1faa52 §1 / 5a9b1cf8 = 736cfd72 / 3957bc4 §2), deg ≤ 106 as listed; N_trunc = highest listed degree unless corpus fixes otherwise. Coefficient-table sha recorded.
- Path & branch: as written in corpus (must be unambiguous); branch of (w−x)^{−1/2} principal unless corpus fixes otherwise — recorded.
- ψ(x): corpus definition sha required.
- residual_slash(x) = |7x|^{−1/2}·residual_factor(x), coefficients 7368b855 §2 (in-family, S-B1′/S-B1 437d4571…).
- Error bound vs N_trunc via tail estimate; script/data sha recorded; exact commands logged.

## Pre-registered rules
- RG-C0 Input gate: if ψ(x) definition, unambiguous path, or coefficient semantics are absent/conflicting in corpus ⇒ STOP, report BLOCKED with paths; no cells filled (no invent).
- RG-C1 If gate passes: compute table, fill author_candidates/ table with per-cell provenance, label NOT Cat A.
- RG-C2 Evaluate F1–F3 of schema. Samples alone never force δ≡0 (F2).
- Standing until ACCEPT: Bridge PARTIAL; READY NO; residual-C OPEN unless F-criteria force otherwise.
Pass/Fail fixed now: any numeric cell using an invented ψ, path, truncation, or coefficient = FAIL.
