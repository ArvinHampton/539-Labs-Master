# FINDINGS — PP DERIVE item (3): the 11D metric — 2026-11-09 (America/Chicago)
Agent: Professor Proof (Soft SF). Additive file; nothing edited. Tip 7cddb188… untouched. No CERT. Nothing sent outside except public literature lookups.
Authority: OW 68a2b8e1f14e8722… and OW 33d25a790fb1e0da…. LOCK 96f8d42e… read; no purged mapping is used.
Scripts/logs: /workspace/audit-scratch/pp_derive_1320/item3_metric.py (.log), item3_addendum.py (.log), geom.py. Conventions: mostly-plus signature; T_MN = (1/12)(F_MPQR F_N^PQR − (1/8) g_MN F²); G_MN = T_MN with κ² absorbed into F; Φ ≡ F².

**Erratum to FINDINGS_PP_DERIVE_11D_MAP_2026-11-09_1328.md (9dde377d…).** Its Part B sha for the EH appendix is mistyped (41 hex digits). The correct sha is 08b8541a1b40e16961984833915437aa4a96b680fe1404ad3e722191308ede39. Nothing else in that file changes.

## Rollup
PROVED 8 · CONDITIONAL 2 · OPEN 2 · REFUTED 1.
Verdict: **CONDITIONAL.** No Owner record defines an 11D metric (564 OWNER_WRITE* files searched; Auditor B13 §6 is CONFIRMED). The corpus ansatz EH-ds is internally consistent as geometry. Its flux lock (EH-lock), however, is **REFUTED** as a solution of 11D Einstein–four-form theory. A consistent vacuum that keeps the EH warp and EH's K = 8k² is derived below as a DERIVED PROPOSAL.

## Inputs
- **EH appendix.** nonlocal/Einstein_Hampton_Equation_Rewrite_Appendix_2026-09-28.txt (08b8541a1b40e169…). This is 539 Labs corpus text, not an Owner Write. It contains:
  - EH-ds: ds² = e^{−2A(y)}η + dy² + e^{2B}ĝ₆, with B constant and R̂_ab = κ_int ĝ_ab.
  - The lock: k² = Φ/1728, K = 8k², with "No Λ₁₁".
  - Flux N = 4880 "on equatorial S⁴ of unit S⁶".
- **NL be7382b4…** and the PP audit 6fa76f12… of it: on AdS₅ × K3 × S² with F = q·vol(S²)∧J, the source blocks are (−6, 0, +6)q². The unique solution needs Λ₁₁ = −6k², and there is no Λ₁₁ = 0 solution.
- **PP lemma** (90400213…, l.87): a source isotropic over AdS₅ × (2D factor) forces K_2D = −4k².

## 1. Geometry of EH-ds (PROVED, sympy)
- 5D warped block with A = ky: Ric/g = −4k² on all 5 directions, Γ^y_00/g_00 = k, and Γ^0_y0 = −k. These match L3–L5.
- With an Einstein 6-fibre of Ric = K g: R = 6K − 20k², G_ext/g = 6k² − 3K, G_fib/g = 10k² − 2K. These match L6.
- At K = 8k²: R = 28k², G_ext = −18k², G_fib = −6k². These match.
- The (alg) system solves to k² = Φ/1728, K = Φ/216 = 8k². This matches L7 as algebra.

## 2. The four-form source the lock assumes (PROVED, numeric 11D tensor)
- **Exact stress for F ∝ vol(S⁴), legs on 4 of the 6 fibre directions.** In units of F²/96, T^M_M = −1 on the 5 AdS₅ directions, +1 on the 4 legs, and −1 on the 2 transverse fibre directions.
  - The stress is **not isotropic on the fibre**. Its average over the fibre is +F²/288.
- **What EH used instead.** The second (alg) equation, 4k² + K = Φ/144, is R_fib − R_ext = T_fib − T_ext. It implies T_fib = −Φ/288 (item3_addendum.log).
  - That is the **wrong sign** relative to the true fibre average, quite apart from the anisotropy. With the sign corrected the averaged system gives k² = Φ/576 and K = Φ/144 = 4k².
- **R1 (REFUTED).** EH-lock is not a solution of 11D Einstein–four-form theory with T(G₄) as the only bulk source. A fibre with Ric = K ĝ has an isotropic Einstein tensor on the fibre, while the exact stress has eigenvalues +F²/96 and −F²/96 there. Equality forces F = 0, and then k = K = 0.
  - The EH note's own Appendix D flags this check ("T_μν/g = −G²/96 vs T_ab/g = −G²/288").
- **OPEN.** Whether the undefined extra bulk sources T(M2), T(−) and T(PBH) could compensate. They are undefined, so this stays OPEN.

## 3. Consistent replacement (PROVED, sympy + numeric; standard in the literature)
Split the fibre into the 4-cycle carrying the flux and a 2D factor: M₁₁ = AdS₅ × S⁴ × N₂, with F = q·vol(S⁴) and Λ₁₁ = 0.
- **Trace-reversed equations.** In units of f = F²/96 = q²/4: R^M_M = −2f/3 on AdS₅, +4f/3 on S⁴, and −2f/3 on N₂.
- **Solution (all sign branches):** q = 2√6 k, r_S⁴ = √6/(4k), and ρ_N₂ = 1/(2k).
  - Ric(S⁴) = 3/r² = 8k². This **is EH's K = 8k²**, now carried by the S⁴ factor only.
  - Ric(N₂) = −1/ρ² = −4k², so N₂ = H², or a compact Σ_g of genus ≥ 2.
- **Field equations.** dF = 0 holds. d*F = 0 holds, because *F ∝ vol(AdS₅)∧vol(N₂) is closed. F∧F = 0, so the Chern–Simons term does not source anything.
- **Literature.** This is the AdS_{7−N} × H^N × S⁴ family with N = 2: Kehagias–Russo hep-th/0003281, also listed in hep-th/0502031. It is non-supersymmetric.
- **Agreement with prior PP/NL results (PROVED).**
  - K_N₂ = −4k² is exactly the PP isotropy lemma, since N₂ and AdS₅ see the same source.
  - A round S² is excluded at Λ₁₁ = 0, which agrees with NL's no-Λ₁₁ = 0 result for K3 × S².
  - K3 cannot carry the flux, because the flux 4-cycle needs Ric = +8k² while K3 is Ricci-flat.
- **Flux quantization** ∫_{S⁴}F = (2πℓ_p)³N, with N = 4880 as an inserted input:
  - r_S⁴ = (πN)^{1/3} ℓ_p = 24.8422 ℓ_p. The check 8π²r³ = (2π)³N agrees to 1 part in 10¹⁵.
  - k = 0.0246505 ℓ_p⁻¹, L_AdS = 40.567 ℓ_p, ρ = 20.284 ℓ_p.
  - EH's (EH-k) gives k = 0.02531377 under its own normalization, which differs (OPEN which normalization the Owner intends).

## 4. DERIVED PROPOSAL DP-metric (not Owner-adopted)
ds²₁₁ = e^{−2k|y|} η_μν dx^μ dx^ν + dy² + r²dΩ₄² + ρ² ds²(Σ_g), with F₄ = (3/r) vol(S⁴_r), r = √6/(4k), ρ = 1/(2k), and Λ₁₁ = 0. The y-direction is the Poincaré radial coordinate of AdS₅, so the faces are at y = 0 (+U) and y = b (−U).
Everything built on DP-metric is **CONDITIONAL** until the Owner adopts it: item (1) DP-Rc, item (2) B3, and item (4) faces.

## Owner decisions needed
- **D-Met-1.** Adopt DP-metric (AdS₅ × S⁴ × Σ_g) in place of EH-lock (Einstein 6-fibre), or define T(M2), T(−) and T(PBH) so that EH-lock could close.
- **D-Met-2.** Fix the flux normalization: standard (2πℓ_p)³N, or EH's 16πG₁₁ = (2π)⁸ℓ⁹ with its k = 0.02531377.
- **D-Met-3.** Fix N, which stays inserted (4880), and the genus g.
