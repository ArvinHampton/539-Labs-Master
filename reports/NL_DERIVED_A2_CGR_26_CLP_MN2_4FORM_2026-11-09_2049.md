# NL DERIVED: component comparison of CGR (2.6) G₄ against the MN2 (CLP) 4-form
2026-11-09, 20:49 CST (America/Chicago). **NL derived proposal.** Nothing here is adopted. Junction status: **UNSOLVED**, unchanged. The count-gap status is unchanged.

Authority: **OW t4426** OWNER_WRITE_MAINCHAT_t4426_PURSUE_ALL_OPEN_JUNCTION_ROUTES_2026-11-09_1956.md = d5eaeef3f6b53270bd09e30053f6cdbf442d191c58a0a9fda30daff83907ffb3 ("Pursue all open"; χ-smearing is NOT decided; this is item 5, the A2 component comparison queued by E16-A2). **OW t4431** OWNER_WRITE_MAINCHAT_t4431_LIFT_90_PERCENT_STOP_2026-11-09_2020.md = f700141d3ee862c7b077b0f67db5fb03b3adc56808c927ba1dd016c88910b1ec (the 90% stop is lifted; usage is still reported). Also OW 19a88b19 (MN N=2 working vacuum, CONDITIONAL; junction UNSOLVED); OW 36683379 (citations checked, never upgrade alone); OW f1d167d1 (the algebra is not named in this file). E16 1951 (E16-A2 CONDITIONAL, queued); PP confirm E16 6eb2fccd…; 1943 T1 (metric/scalar/radii PROVED; flux sub-part was the queued formula identity); PP gate 384096a8 (Maxwell at λ_CLP=1/8). CGR arXiv 1906.08900 eqs. (2.5), (2.6), (3.1)–(3.3), (6.1); CLP hep-th/9903214 eqs. (4.1)–(4.2).

Limits: additive only. No existing script or report is edited (including 1943, E16, y16.py, map_checks.py, and the PP/MR2 sources). No CERT, no Gemini, nothing sent, no agent messaged. Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 before and after. Usage 82.7% at the start of this write (weekly reset Tue Nov 10 09:49 CST).

χ-smearing is not decided (OW t4426). The comparison is of the exact MN2 IR 4-form, which is the same geometry on both the **χ-smeared** and **χ-uniform** branches; the two branches are not distinguished here.

**Tally: PROVED 2 · CONDITIONAL 0 · OPEN 3 · REFUTED 0 · total 5**

## 1. Question and setup

E16-A2 left T1's G₄ identification as **CONDITIONAL**: "The G₄ (flux) identification of CGR (2.6) with the PP/CLP 4-form used in 384096a8 rests on the formula identity. No component-by-component comparison has been done (queued). T1's metric, scalar and radii identification stays PROVED." This file does that comparison at the CGR §6.1 MN2 vacuum, and checks the flux.

Conventions, all used as written and not upgraded by citation:
- g = 2 (= g_c of the MN2 record). CGR (2.5) and CLP (4.1) use the same g^{-2} fibre factor.
- e^{30φ}=2, e^{10λ}=2, g² L² = 2^{4/3}, l=−1 (H²). "All other 5D fields trivial" (CGR §6.1), but the 7D/11D uplift keeps the topological twist (3.2): A^{ab}_{(1)} = (1/g) ω̄^{ab}.
- T^{ab}=e^{-6λ}=X_a=X_1=2^{-3/5}, T^{αβ}=e^{4λ}=X_b=X_0=X_2=2^{2/5}, det T=1. Δ = T_{ij} μ^i μ^j = D̃.
- Embedding: μ^1+iμ^2 = μ_1 e^{iφ_1} (SO(2) twist plane, CLP X_1), μ^3+iμ^4 = μ_2 e^{iφ_2}, μ^5=μ_0, with μ_0=cos α, μ_1=sin α cos β, μ_2=sin α sin β. Physical S⁴ chart: α∈[0,π], β∈[0,π/2], φ_i∈[0,2π). (β∈[0,π] double-covers: β↦π−β with φ_1↦φ_1+π.)
- Twist: A^{12}=−du/(g v) on Poincaré H² with R_{ab}=−g² h_{ab}, so F^{12}=−du∧dv/(g v²)=−g vol(Σ)_{unwarped}. CLP A^1=du/(g v), a_1=1, a_2=0, F^1=−F^{12}.
- "Our" MN2 4-form is the Hodge dual of CLP (4.2) at this vacuum (dX=0), with λ_CLP=1/(2g²)=1/8 and kap=1, the same coefficient that 384096a8 used for Maxwell. Hodge convention: MR2/PP `hodge_num`, (*Ω)_A = √|g| Ω^B ε_{B A} on sorted combination coefficients (Lorentzian √|det g|).
- CGR (2.6) is specialised at the vacuum: DT=0, S_{(3)}=0, leaving the U-term and the F-term.

Script and logs, new dated directory `/workspace/nl-a2-cgr-2032/`, sidecars:
- cgr_clp_g4_compare_2026-11-09_2041.py = 57c2693ad32e23ce83c3b4492a1a8d093c24b071f19f964e7536482b1c46e5e7, **frozen before execution**. Two earlier compile-failed drafts (2035, 2040) were left unedited and unused.
- cgr_clp_g4_compare_2026-11-09_2041.log = 450ffdc07dd0d6b6c6a598032a9c3145d91d082c0f2fdcb219c6bdfaec6c76d7
- cgr_clp_g4_flux_fund_gauss_2026-11-09_2048.log = 68357b215e223fde66f3b0790010c3ca8aebbb3176b028e4c18f2286b808203b (fundamental-domain and Gauss integrals, importing the frozen 2041 module; the flux block in 2041.log used the double-covering range β∈[0,π] and should not be used for the integral).

11D coordinates (t,x1,x2,x3,z,u,v,α,β,φ1,φ2). Metric: CGR (2.5) / CLP (4.1) with ds_7² = e^{-4φ} ds_5² + e^{6φ} ds²(Σ), ds_5² the AdS_5 of radius L in Poincaré form, ds²(Σ)=(du²+dv²)/(g² v²).

## 2. A2-comp (PROVED). Component match at the MN2 vacuum

At six generic points in the fundamental domain, and at additional checks with α>π/2 or φ_i>π, every nonzero 4-form component of CGR (2.6) equals minus the corresponding component of *_{11}(CLP (4.2)), with max relative error after the sign flip between 9.4×10^{-16} and 3.5×10^{-15}. The two forms have identical support. The overall minus sign is the Lorentzian Hodge / orientation convention (F = −*(*F) in the √|g| convention used here); it is not a physical disagreement.

The supported components, and which term of (2.6) / (4.2) produces them:

| component (names) | origin |
|---|---|
| (α, β, φ1, φ2) | U-term / dual of U_CLP ε_{(7)}: the fibre 4-form |
| (u, α, β, φ2) | same U-term, through Dμ^i = dμ^i + g A^{ij} μ^j, which carries du |
| (u, v, α, φ2), (u, v, β, φ2) | F-term / dual of the (1/(2g²)) X_1^{-2} d(μ_1²)∧(dφ_1+g A^1)∧*̄ F^1 twist term |

There are no AdS_5 legs (no t, x_i, or z). That is the expected support of a purely internal G₄ plus the Σ-twist.

On the overlapping chart β∈(π/2,π) the √|g| Hodge stays positive while the CGR embedding 4-form (1/4!) ε_{i_1…i_5} μ^{i_1} Dμ^{i_2}∧⋯ follows sign(cos β). That is a second cover of the same S⁴, not a second physical flux, and is excluded from the integral in §3.

Algebraic cross-check, used only as a record of what the script also saw at every vacuum test point: at MN2 (X_0=X_2=X_b) one has U_CLP = g U_CGR, hence U_CLP = 2 U_CGR at g=2, exactly. The Hodge of U_CLP ε_{(7)} then supplies the remaining Δ and g powers that match the first term of (2.6).

The coefficient λ_CLP=1/8 is the one that makes this match. That is the same value 384096a8 needed for the Maxwell residual to vanish, now also the value that agrees with CGR (2.6).

## 3. A2-flux (PROVED). T1's flux identification at the vacuum

The fibre component is independent of (φ1,φ2) (relative difference 2.16×10^{-15}). Pulling G₄ back to a fibre at fixed 7D coordinates (du=0) and integrating over the fundamental domain gives, in magnitude,

∫_{S⁴} G₄ = 8π² / g³.

Gauss–Legendre in (α,β) times (2π)²:

- 12×12: |∫| / (8π²/g³) = 0.9999893181733572, and CGR + CLP = 0 to the printed digits
- 24×24: 0.9999999999730881
- 36×36: 0.9999999999999989, with 8π²/g³ = 9.8696044010893580 and CGR = −9.8696044010893473

So the CGR (2.6) 4-form and the PP/CLP 4-form used in 384096a8 carry the same S⁴ flux at the MN2 vacuum (opposite Hodge-sign convention, same magnitude). E16-A2's queued "formula identity" is discharged at the vacuum: the flux match is PROVED, not merely cited. T1's metric, scalar and radii identification is untouched and stays PROVED. The 1943 and E16 files are not edited; this file is the additive record that the flux sub-part of T1 / E16-A2 is now PROVED at the exact MN2 IR.

## 4. A2-DT (OPEN). The DT / dX terms were not compared

At the vacuum, λ is constant and T^{αβ}=δ, so DT=0 in (2.6) and dX=0 in (4.2). Both extra terms vanish identically on the configuration that was computed, which is why their vanishing is not evidence that they match off the vacuum. A component-by-component check of CGR's second (DT) term against CLP's (1/(2g)) Σ_α X_α^{-1} *̄ dX_α ∧ d(μ_α²) term, along a CGR (φ,λ) domain wall or a variation of λ, has not been done.

## 5. A2-S (OPEN). The S_{(3)} terms were not compared

CGR (2.6) has two further terms, −T_{ij} *S_{(3)} μ^j and (1/g) S_{(3)}^i ∧ Dμ_i. At the §6.1 vacuum, K_{(2)}, h_{(3)} and χ_{(1)} are trivial, so S_{(3)}=0 by (3.4). CLP (4.2) as used in 384096a8 and in the script has no independent 7D three-form. A comparison of these terms against any completion of the 4-form away from the vacuum (charged or running 5D two- and three-forms) has not been done.

## 6. A2-offvac (OPEN). General CLP U(1)² flow with X_0 ≠ X_2 is outside the CGR (φ,λ) sector

The comparison above is at the exact MN2 vacuum, where X_0=X_2=e^{4λ} and the configuration sits in CGR's (φ,λ) truncation (T^{αβ}∝1). Along a general BBBW / CLP flow X_0 and X_2 are independent, which requires a traceless mode in T^{αβ} and is not a CGR (φ,λ)-only field. That is already T3 in 1943 (the (φ,λ) sector does not contain the generic U(1)² flow). This file does not compare 4-forms off the vacuum, and does not change T3.

## 7. What this does not change

The junction remains **UNSOLVED**. χ-smearing remains undecided. Nothing is adopted. The 1948 KK-counting gap is not affected. Y15 / NEC / tr R² shortfalls are not affected. T1 metric, scalar and radii stay PROVED. E16-A2 is discharged at the MN2 vacuum only (A2-comp, A2-flux); the off-vacuum 4-form (A2-DT, A2-S, A2-offvac) stays OPEN.
