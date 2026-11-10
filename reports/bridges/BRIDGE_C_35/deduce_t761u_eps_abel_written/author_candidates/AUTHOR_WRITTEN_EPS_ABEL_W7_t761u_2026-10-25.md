# AUTHOR-WRITTEN ε→0 Abel / Im-shift + W₇ action on x+iε — draft + menu (t761u, 2026-10-25 CDT)
Status: AUTHOR-WRITTEN draft — NOT Cat A until Arvin ACCEPT + Auditor CONFIRM. Inventory #4 of MASTER 544de792…. Convention supply only; G-A3 stays PAUSED (no reopen, no fill, no numbers).
Basis: PB-α ACCEPT LOCK (PREREG ba143e9b… / RESULTS cb662101… / SUMS 8274ab19…) — Auditor CONFIRM MATCH soft SF none c26b5f72c4603acd05623df5d745bfa538c4a14131b222bf92c00537f34f458e (SF-1 RESOLVED). AW-α aac04151…; O-α b467bb54…; Written path 94ac4072…. 4da09dec… REJECTED, ε=0 row cited diagnostically only. Verbatim: logs/written_lines.txt (labels = live sha prefix).
PB-α pin carried, not re-litigated: path i∞→x (1bab65c4 L32); principal branch (ACCEPT-default, NOT Written HD); ψ ≡ psi-Cocycle.

## 1. What is Written vs ABSENT
| Item | Written? | Evidence (live sha) |
|---|---|---|
| 1. ε→0 Abel / Im-shift evaluation of residual integral I | ABSENT for residual h. R-D3 is a Bridge-C AUTHOR-ACCEPT convention row (t718u a05693fb L23: "contour not Written"), not HD. HD flags the radial-limit prescription as missing (c48144bf L83 "Recover or restate the precise weight-1/2 Fricke slash operator and radial limit prescription"); radial limits "unavailable as a theorem" (3a5f7aea L57). Abel summation is Written only for one-sided series convergence in Herglotz/E_R (e7967dde L31) and as Dual_Abel_off kernel N^{-1/2}exp(−2πNε), ε=10^{-4}, "definition occupancy", explicitly not a residual-flux object (13eb50e6 L50; 73e5a1a9 L13). Neither fixes ε→0 for h. |
| 2. W₇ action on Im-shifted point | PARTIALLY WRITTEN (adjacent objects): HD/Consolidated act with W₇ as Möbius on τ=x+iε: "C − λ(7τ)^{−k}C(−1/(7τ))" (f26a6418 L145; 2716a441 L499–501), i.e. W₇(x+iε). Clean-v2/ER-Proof: vertical approach "z = x + iy → x … maps to a curve approaching −1/x non-tangentially" (ca3a6d68 L271; a9c9d066 L93). Residual δh is Written only at real x (1bab65c4 L46). No Written line uses W₇x+iε (t722u primary = PREREG choice 36b663d3 L14). |
| 3. Mixed regularization ψ(real x) vs I(x+iε) | ABSENT as a residual convention. Written: ψ for rational x>0 "is the boundary value of the right-hand side of Theorem I" (e7967dde L65) — a holomorphic (Herglotz) extension exists in Written, so a co-shift has a Written object to evaluate, but no Written line prescribes co-shift for h. |
| 4. Any Written HD/Consolidated fixing all of the above for h_residual^{high} | ABSENT. |
t722u facts (verbatim cite, 9aa52f19 L11–28): W₇(x+iε) vs W₇x+iε differ strongly (x=1, ε=0.05: 4.116 vs 0.0569); |δ_ε| unstable as ε→0; F3 controlled only regularized at fixed ε≥0.02; F1 FAIL. No new numbers here.

## 2. MENUS (all AUTHOR-WRITTEN / ACCEPT-needed)
### EP — W₇ endpoint
- EP-α ACCEPT W₇x+iε (shift after map; t722u primary). Continuity with t722u table; no Written support; not a Möbius image of τ.
- EP-β ACCEPT W₇(x+iε) = −1/(7(x+iε)) (Möbius on τ; δ_ε(τ)=h(τ)−slash·h(W₇τ) on ℍ). Written-aligned: f26a6418 L145, 2716a441 L499, ca3a6d68 L271, a9c9d066 L93. [rec]
- EP-γ HOLD — endpoint stays convention-sensitive; any δ_ε table carries both.
### AB — ε→0 / Abel stance
- AB-α KEEP regularized-only at fixed ε≥ε₀ (ε₀ = t722u's 0.02 floor where E_δ ≪ |δ_ε|); no ε→0 claim; F3 real-x NOT controlled. [rec]
- AB-β ACCEPT Abel limit with stated bound (R-D3 as written in t721u L4). Requires an Abel/radial theorem for h that is Written-ABSENT (3a5f7aea L57) and t722u shows divergence of tail majorant at ε=0 ⇒ would be invented; NOT recommended.
- AB-γ HOLD (no ε stance).
### MX — mixed regularization
- MX-α KEEP S3 as-is (ψ real x, I at x+iε; flagged mixed).
- MX-β AUTHORIZE co-shift: ψ evaluated as the Written Herglotz Theorem-I RHS at τ (whose boundary value is psi-Cocycle ψ, e7967dde L65), so ψ-α (PB-α) is preserved in the limit. Uniform-τ object. [rec; future compute only, nothing evaluated here]
- MX-γ HOLD.
### Combined
- E-α [REC] EP-β + AB-α + MX-β: one holomorphic object on ℍ at τ=x+iε, W₇ as Möbius (Written), regularized-only stance (no invented Abel theorem), ψ co-shift via Written Herglotz extension consistent with PB-α ψ-α.
- E-β EP-α + AB-α + MX-α: pure t722u continuity (status quo, both S2/S3 remain soft flags).
- E-γ EP-β + AB-α + MX-α: Written-aligned endpoint only; S3 remains flagged.
- E-δ EP-β + AB-β + MX-β: includes Abel limit — invent-risk; not recommended.
- E-ε HOLD all (#4 stays ABSENT).
Rationale for E-α: only option where every knob is either Written-anchored (EP-β, MX-β) or a non-claim (AB-α); PB-α path/branch/ψ untouched (i∞→τ endpoint, principal branch for (w−τ)^{−1/2} with τ off-axis, ψ boundary value = psi-Cocycle). Caveat: EP-β values differ O(1–70×) from t722u primary; prior t722u table becomes the EP-α variant column, not invalidated.

## 3. Bans honoured
Not a G-A3 reopen (G-A3 PAUSED; menu supplies conventions only); 4da09dec… not revived; no δ≡0 / Bridge YES / F3 real-x controlled claim; no numeric h/δ; no Ξ coeffs; no Abel theorem invented; branch not re-litigated; CORE_FREEZE, SF-W7-3, Residual-vs-Resonant respected; no nonlocal EH11D; no order78.
