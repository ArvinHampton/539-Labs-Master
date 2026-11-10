# deduce_t722u_ga3_opt_c_diag — RESULTS (DIAGNOSTICS-ONLY / NOT Cat A / NOT Bridge-closing)
PREREG 36b663d3015b385114fec80305c1f4d79b6775e469caa6dd40740f7dce4163f5 (hashed 11:18:59 CDT before any number; re-verified OK). Authority t722u AUTHORIZE (c); t712s4471; t720u R-D3; t713s4484 ψ; t713s4497 P2. NO ledger fill; R-C1 BLOCKED (1749576a… / 7d324d73…). Ledger Ξ 7dbd63af… unused; no χ/ϑ/X4.

## RG-0 Input — PASS
Ξ data/Xi_regen_N106.tsv sha 35b186f9df70c2bf247432edcef946e5f66f0ddf1bbca2f4454a30b210707197 verified in-script (9 terms, ν≤106). Selectors 437d4571… / 3d502756… (file sha verified). Object A source dfd2b4b0… L31.

## R-E2 slash regen — DONE (data/slash_regen.json c97ec8d589c8b515b7e481d1931fdee996c60eca108c3ce9f47c9eed4fdd943d)
Exact 4×4 Fraction solve: a=82116863/7680000, b=27/125, c=106053121/38400000, d=−57842687/7680000 (interp residual 0 exactly). residual_slash = 19.80118, 1.82483099582765015388…, 9.24174944945382080768…, 20.9022158540470297191… at x=1/7,3/7,5/7,1. vs t713u 4-dec coeffs: |Δ| ≤ 1.1e-7 (x=1). Slash precision is NOT the source of δ.

## R-D3 contour — DONE (scripts/diag.py 77580b51…; data/diag_out.json 0d637ec9…)
Contour: P2 vertical i∞→x+iε, termwise closed form I_N(z)=Σ −e^{iπ/4}c_ν(2ν)^{-1/2}e(νz); h_ε=ψ(x)e^{−iπ/4}−I_N(x+iε); W₇ side endpoint W₇x+iε (variant W₇(x+iε)). ε∈{0.1,0.05,0.02,0.01,0.005,0}. Tail bound T(ε)=Σ_{ν>106}M(ν)(2ν)^{-1/2}e^{−2πνε}, M=√ν(2⌊√(ν/35)⌋+2); E_δ=T(1+slash)+2e-9. ε=0 reproduces REJECTED fill exactly (62.970/7.082/5.558/35.139) — consistency check.

| ε | abs δ at 1/7, 3/7, 5/7, 1 | tol (t713u σ) | E_δ max | shift S(ε) |
|---|---|---|---|---|
| 0.1 | 0.7708, 0.0193, 0.0418, 0.0616 | 1.4e-4…3.3e-6 | 2.0e-9 | 5.30 |
| 0.05 | 0.7662, 0.0197, 0.0436, 0.0569 | 1.4e-4…3.4e-6 | 2.0e-9 | 5.30 |
| 0.02 | 0.1475, 0.0716, 0.1754, 0.4723 | 2.6e-5…1.0e-4 | 3.2e-3 | 5.27 |
| 0.01 | 4.124, 0.349, 0.675, 2.323 | ≤7.7e-4 | 5.3 | 5.05 |
| 0.005 | 14.97, 1.158, 2.134, 5.544 | ≤2.7e-3 | 330 | 4.41 |
| 0 (REJECTED, cite) | 62.97, 7.082, 5.558, 35.14 | 1.1e-2…1.1e-3 | ∞ | 0 |
W₇(x+iε) variant differs strongly (e.g. x=1, ε=0.05: 4.116 vs 0.0569) → convention-sensitive. Full table: author_candidates/DIAGNOSTIC_TABLE_GA3_contour_N106_2026-10-25.md bd63821f….

## Force criteria
- F1: FAIL — |δ_ε| ≫ tol at all 4 x for every ε (even where E_δ≈2e-9).
- F2: δ≡0 NOT forced (samples never force; samples show δ≠0).
- F3: PASS (nonzero defect) — controlled ONLY as a regularized quantity at fixed ε≥0.02 (E_δ ≪ |δ_ε|, rigorous majorant). NOT controlled for the real-x defect: |δ_ε| not stable as ε→0 (grows ~10–100× from ε=0.05 to 0.005; tail majorant diverges at ε=0; S(ε)≈5 ≫ |δ|), and W₇-endpoint convention changes values by O(1–70×). Per PREREG criterion: F3 controlled = NO.
Verdict: DIAGNOSTICS COMPLETE. G-A3 NOT filled (diagnostic only) | Bridge PARTIAL | READY NO | residual-C OPEN. Bridge YES / δ≡0 / residual-C newly forced: NO/NO/NO. No order78.
Soft: (S1) tol formula retains t713u 4-dec σ; with exact regen σ→0, tol→1e-11 (F1 worse). (S2) W₇ action on Im-shifted endpoint is a convention not fixed by P1–P7 (needs AUTHOR choice). (S3) ψ evaluated on real x (principal branch) while I at x+iε — mixed regularization. (S4) Ξ_N106 only 9 terms; true ε→0 needs full Written series beyond N, outside Ξ-source lock.
