# PR1 FINDINGS — NL Rule-4 Hybrid MC Numerical Recompute (2026-10-26)

**Verdict: INCONCLUSIVE.** χ²_recomputed = ABSENT. Data set, dof, and the full E_leak coefficients are all ABSENT, so the Doc's 0.79 cannot be recomputed.
**tip_touched: NO.** The tip Soft SF LOCK file `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` was not touched. Live sha `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` matches.

## 1. Authority (live sha256, all MATCH)
| Doc | sha256 |
|---|---|
| ASSIGN pack | 3a6e41d9f9c7227cb1f0c61007c63eeaf2bfb8bddd33526790d078f30d9fefd3 |
| Runnable-spec | 27058bad386fc64dff071324e4f4d248a60113c68349917b42656c93025fe980 |
| OW Rule-4 OPEN | bc42067bf015fb321ac11e45c1b6a74019ed85a6294d21e80a4691442b09d1f8 |
| PASS/READY YES | 7070d2b1ceaedaa148b5a918fb7ab79b48dbbbe2b560a03e5cd3cba3b586cfda |
| Hybrid MC DESIGN | 6bbc198e9a73ef8d80b8d7c1127404b3226faf66f4893272ba0fdaadd465968b |
| RPPT deepen | ce6520ce182a8c26ec1c99b783c8d31a4f0620b99b0cc4da71362dbdec82b070 |
| Sheet params | da91ad83ac35a2f3a897dbd1794b90d102b409284012b889d6b74849e3af5998 |
| Corrected 7D A27 | 4758d180f467a35d139833711029ac4121fa98d79bb3129be1b579d8254250b1 |
| minus-PT A27 | 7302244a8fd5dd641855191e1f2e92dfe638fcb69845af6203b28c72dfcbb65d |
| Prior PR1 pack (context) | e381700d0390dfb6d8246b00b88365c9852b42fae1a8e983bd7d4e818bcf3165 |
| corrected_E_leak.py (REDUCED) | a786538854a27c7b0409c24c8a7d1bfa595db780f05214796fcec9822c9b945a |
| Full_E_leak_and_Higgs_Echo_CatB.md | 506e85b43172417dea8fd2b7705dc9eae5944f658a8b513b76882441d18e0627 |
| E_leak_CuNc_Numerical_Patch.md | 2c75306fa4357901ceea668362b8c4e3f17ce377ca4f8c55459ee69509e41682 |
| Catalog obs-data-PR1-HEPP-QM-GR.md (read-only) | 6c680789ff64a7bb1a83276690e20a1748d8d2a31f19a97b869c13109b77f33d |

## 2. Frozen params (Corrected 7D §3.1 + sheet)
ρ_DM = 0.31 GeV/cm³, β_PBH = 0.18, κ_dark = 0.45, z = 1…118. Join wire g_s X^M is PASSED (cite READY YES 7070d2b1…). **Its numerical value is ABSENT and was not invented.**

## 3. What is Written (Corrected 7D §2.5–§3.1)
- **E_leak(t), §2.5:** E_0 e^{-t/τ} L Ω_11D + κ_dark √δ(t) v_0 f_energy (1+ρ_DM/10)(1+m_φΦ+g_coupling A+h_coupling T+m_ψψ+g_11Φψ+g_s X^M) + ρ_DM∫sin(…)dτ + Σ_{z=1}^{118} E_b(z)(E_z^-−Z_z^-)/(c²τ^-) sin(2πt/(539.9+Δt_11D)) + δΔ A_H-QP(1−τ_echo/t) e^{-(t−τ_echo)²/2σ²} + SħΩe^{-S}(1−E_em/ΔE) + β_PBH ρ_DM e^{-M_PBH/(k_B T_rad)} + δa_μ^{-U}(…) κ_dark sin(2πt/539.9).
- **F_friction(t):** 0.9(γ−1)m_adj v_0²(539.9/1000)e^{-t/(τ+γL_QG N_simplex)}L + Σ_{z=1}^{118} β_z(N_z^-−2Z_z^-)e^{-t/τ^-} + A_H-QP δΔ e^{…} + cos((k1−k2)d−θ)(1+α_alt).
- **§3.1:** "numerical integration of E_leak(t), achieving χ²/dof = 0.79 … Verified against DESI DR2 … ATLAS Open Data". No data points, dof, or residuals are given.
- **Fully-specified terms using frozen + Cited coefficients only: none.** Every term carries at least one ABSENT symbol: E_0, τ, L, Ω_11D, δ(t), v_0, f_energy, Φ, ψ, A, T, the couplings, E_b(z), E_z^-, τ^-, β_z, Δt_11D, A_H-QP, τ_echo, σ_inh, S, Ω, E_em, ΔE, M_PBH, T_rad, g_-U, M_-U, γ, m_adj, k1, k2, d, θ, α_alt. The Doc-full integration was therefore **not run**.

## 4. What was run
1. sha256 verification: all 14 docs MATCH, plus the tip LOCK.
2. **minus-PT inventory parse:** 118 elements, Z = 1…118, unique and complete. All 118 have numeric atomic mass. With N = round(A) − Z (the standard +U mass, as minus-PT states):
   - Σ(N−2Z) = 3247 (dimensionless)
   - (N−2Z) < 0 for 1 element
   - **Caveat:** this is structural only. The minus-PT does not Write N_z^- or Z_z^- as distinct "reverse-parity" values, nor β_z, τ^-, E_b(z) or E_z^-. The F_friction / E_leak Σ_z terms therefore cannot be evaluated.
3. **REDUCED-FORM E_leak (corrected_E_leak.py, NOT Doc-full, units unspecified in source):**

| t (s) | E_leak |
|---|---|
| 0 | 45.2777 |
| 1e-15 | 45.2773 |
| 7e-14 | 45.2582 |
| 1e-6 | 45.2467 |
| 1 | 45.2469 |
| 100 | 45.2614 |
| 539.9 | 45.2426 |
| 3600 | 45.2360 |
| 86400 | 45.2524 |

   - Grid: t ∈ [0, 5399] s, 200001 uniform points, trapezoid rule.
   - ∫E_leak dt = 2.44285e5 (unit·s); time-mean = 45.2464; range [45.2297, 45.2777].
   - The known term5 issue reproduces: term5 = S·100·e^{-S}(1+η) ≈ 45.25 dominates, and E_leak(0) ≈ 45.28 versus the historical target 6.07e-12 (flagged in the file comments, not altered).
   - CHI2_DOF = 0.79 in the script is a hard-coded constant, not computed.

## 5. Corpus search (step 3)
- (a) E_b(z) / E_z^- / Z_z^- / N_z^- / β_z / τ^- table: **ABSENT.** The only hits are formula restatements: the inventory_check attachment "Corrected 7D Torsion Geometry and.txt" (lines 33/81/96) and related Drive-unpack docs. None contains a table.
- (b) χ² data set / dof / DESI DR2 / ATLAS points behind 0.79: **ABSENT.** 0.79 appears only as a quoted constant (drive/ADVANCEMENTS.md:463, drive/extracts/academic-definitions.md:30, corrected_E_leak.py, NL bridge docs marked "reference only").
- (c) Integration scripts beyond corrected_E_leak.py:
  - grok-files/S211DM2ETX_Unification_Model_corrected.py (same model class family).
  - oct17-master/.../scripts/{model_lagrangian_hamiltonian_sympy.py, apply_closed_constants.py, observatory_data/loaders.py, r_fft_5399.py}, plus clones under reports/bridges/_git_v8_unpushed_clone and reports/self-audit/repo.
  - Matched "E_leak|friction" by grep. None provides a χ² fit against a Written data set with dof. Not used for numerics.

## 6. ABSENT inventory
- g_s X^M numerical value
- E_b(z), E_z^-, Z_z^- / N_z^- (reverse-parity), β_z, τ^-
- E_0, τ, L, Ω_11D, v_0, f_energy, field amplitudes and couplings
- A_H-QP, τ_echo, σ_inh, Δt_11D, M_PBH, T_rad, g_-U, M_-U
- γ, m_adj, k1, k2, d, θ, α_alt
- Observational data set (DESI DR2 / ATLAS points), dof, model predictions, residuals
- χ²_recomputed

## 7. Verdict vs Doc 0.79
**INCONCLUSIVE.** There is no Written data set, dof, or full coefficient set. No χ² was fabricated.

## 8. Hard excludes
- Tip Soft SF LOCK: tip_touched NO (sha unchanged).
- No Zwegers/Path4 package numerics. C1 = 0.10 is named only and gated on the Local Written asymptotic.
- No Eigen, CRT, or new physics params invented.

## 9. Optional flag
Rank-20 δ_W₇ (sha 85c9c5cf…): SAMPLE ONLY. It is not a proof obligation and is NOT FORCED. Not used here.

## 10. Delivery
Ships to NL Rule 5 as a PR1 Rule-4 recompute record. Status INCONCLUSIVE, pending a Written data set, dof and coefficients.
