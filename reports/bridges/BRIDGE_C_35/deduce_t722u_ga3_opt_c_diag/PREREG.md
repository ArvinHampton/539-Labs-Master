# deduce_t722u_ga3_opt_c_diag — PREREG (hashed BEFORE any RESULTS / numbers)
Date 2026-10-25 (CDT). Authority: t722u AUTHOR AUTHORIZE (c) (Arvin via Physicist) — GO diagnostics only: R-D3 complex-contour/tail + R-E2 slash regen on t713u regenerated Ξ. Compute authority t712s4471 (class C); R-D3 AUTHOR-ACCEPT t720u; R-E2 under t712s4471; ψ ≡ psi-Cocycle t713s4484 (principal branch stands); path P2 i∞→x per t713s4497 (P2) / t721u.
Posture: CORE_FREEZE; SF-W7-3; Residual-vs-Resonant lock; no nonlocal EH11D/Ω₁₁D/F_total; no order78.

## Scope (binding)
- DIAGNOSTICS-ONLY. NOT Cat A. NOT Bridge-closing. Does NOT fill G-A3; NO ledger fill.
- R-C1 remains BLOCKED (R-PKG1 CONFIRM 1749576a… / RESULTS 7d324d73…).
- Ξ source ONLY: deduce_t713u_ga3_fill/data/Xi_regen_N106.tsv sha 35b186f9df70c2bf247432edcef946e5f66f0ddf1bbca2f4454a30b210707197 (verify before use; abort BLOCKED on mismatch). Ledger Ξ 7dbd63af… NOT used. No χ/ϑ, no X4 identification invented.
- Selectors for slash: FINDINGS 437d4571e0f707460c7ac2a7dd983d0649161dd7975779101907eaedba7d7476 / candidate 3d502756d1a932a35ba0e559cad513674789a7667a0a8fc45007d8950179366f (Written family F=a+bt+ct²+d/(1+t²), t=7x−3, x>0; residual_slash=|7x|^{-1/2}F).
- Baselines cited only: REJECTED fill 4da09dec… / RESULTS c4755206… / CONFIRM a520614b…; menu a05693fb… / CONFIRM 2e1dec49…; schema 8d247feb…; G-A1b CLOSED b34aebe6…; STREAM c6ab7cc2…; inventory a08d0597….

## Methods (fixed in advance)
R-E2 slash regen: solve the 4×4 Written-family system EXACTLY (Fractions) on Object A residual_factor samples 19.801180, 3.160700, 20.665180, 55.302065 at t=−2,0,2,4 (source heavy-daily/a5db06c-U1_LEDGER_P_SLASH_Remark85.md sha dfd2b4b0…; 6-decimal Written values taken as exact rationals). Emit a,b,c,d exactly + 30-digit decimals; residual_slash(x)=|7x|^{-1/2}F(x) evaluated at 30 digits; compare to 4-decimal coeffs used in t713u. Output data/slash_regen.json with sha.
R-D3 contour: h(x) := ψ(x)e^{−iπ/4} − I_N(x+iε), with I_N(z)=Σ_ν −e^{iπ/4} c_ν (2ν)^{−1/2} e(νz) over Ξ_N106 (termwise closed form of P2 integral i∞→x+iε, vertical segment above the real endpoint). W₇ side: h(W₇x) with endpoint W₇x+iε (primary) and W₇(x+iε) (sensitivity). ε ∈ {0.1, 0.05, 0.02, 0.01, 0.005, 0}. Error/tail bounds:
 (B1) truncation tail of the full Written-product series beyond N=106 at height ε: T(ε) ≤ Σ_{ν>106, 4ν∈ℤ} M(ν)(2ν)^{−1/2}e^{−2πνε}, majorant M(ν)=√ν·(2⌊√(ν/35)⌋+2) (n+a≤√ν; ≤ ⌊√(ν/35)⌋+1 m-values per parity class, one n each) — analytic majorant, no coefficient invented.
 (B2) shift defect relative to real endpoint: S(ε)=Σ_{Ξ_N}|c_ν|(2ν)^{−1/2}(1−e^{−2πνε}).
 Defect δ_ε(x)=h_ε(x)−slash(x)h_ε(W₇x); propagated bound E_δ = T(ε)(1+|slash|) (+ ψ quad err ≤2e-9 from t713u).
Samples x∈{1/7,3/7,5/7,1}; tol as t713u (10(1e-12+σ|h(W₇x)|), σ from regen residual).
## Force criteria (pre-stated)
- F1: |δ_ε| ≤ tol at all 4 x for some admissible ε with E_δ ≤ tol? expected FAIL.
- F2: δ≡0 forced? samples never force → NOT forced.
- F3 controlled iff δ_ε has an explicit bound E_δ ≪ |δ_ε| AND the ε→0 limit is stable (|δ_ε| variation across ε≤0.02 within E_δ+S). Otherwise F3 PASS-uncontrolled.
- Bridge YES / δ≡0 / residual-C newly forced: expected NO/NO/NO. Outcome label DIAGNOSTICS COMPLETE or BLOCKED.
