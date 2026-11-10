# deduce_t718u_ga3_revise_menu — PREREG (written before RESULTS; frozen)
Stamp: 2026-10-25 CDT. Scope: Local Bridge C only. CORE_FREEZE; SF-W7-3; Residual-vs-Resonant lock; no nonlocal EH11D/Ω₁₁D/F_total; no order78.

## Authority
- AUTHOR DIRECTIVE t718u (Arvin via Physicist): propose revise options for G-A3 re-run given F1 FAIL soft flags. Menu = AUTHOR-CANDIDATE, NOT Cat A. No re-run until Arvin picks.
- t717u Arvin REJECT of fill deduce_t713u_ga3_fill (PREREG 49bd0b24… / RESULTS c4755206… / filled 4da09dec… / Xi_regen 35b186f9… / CONFIRM a520614b…): NOT Cat A; no obstruction ACCEPT.
- Baseline knobs = t713s4497 (P1–P7) + t713s4484 ψ. Schema 8d247feb…; t712s4471 compute auth (G-A3 only) unused here.

## Inputs (read-only, MATCH-only)
deduce_t713u_ga3_fill/{PREREG,RESULTS,author_candidates,SHA256SUMS}; deduce_t712u_ga3_compute/RESULTS (B-path/B-ψ/B-coeff citations b329c67c, 552541cf, 1bab65c4, be1faa52, 736cfd72, 22959c01, e60cad9b, 7368b855, 1be7f7d1, 7dbd63af).

## Rules
- RM-0: NO compute, NO new h/δ numbers. Only numbers cited from REJECTED fill RESULTS (c4755206…).
- RM-1: each option R-* states: knobs changed vs t713s4497; grounding (sha/path) or AUTHOR-convention; invent status ∈ {Written, AUTHOR-ACCEPT-needed, invent-risk}; qualitative expected effect on F1/F2/F3, justified only from cited fill diagnostics. No claim F1 will pass without evidence.
- RM-2: F2 invariant: samples never force δ≡0 under any option.
- RM-3: coverage: path/branch, ψ/W₇, Ξ form, N_trunc/error bound, coeff/slash precision, bundles.
- RM-4: any non-corpus source (e.g. grok_export) labelled AUTHOR-ACCEPT-needed, never Written.
- Standing: Bridge PARTIAL | READY NO | residual-C OPEN.
