# HALO_SIM_WRITTEN_LINKS — simulated physics / dark-halo bulk: written falsifiable predictions (2026-10-24)
Paths relative to /workspace/quantum-comp/reports/self-audit/zenodo/txt/. Cat B inserted matches excluded (ρ_DM 0.31, 539.9 s, plugged g11/gs, β_PBH, η_ZPL).

| ID | Source path:line | Quote | Verdict | Why |
|---|---|---|---|---|
| HW1 | 17822998_…Dark_Matter_Halo.txt:60-67 | "⟨J_{-U}⟩ = (ρ_DM/m_p) Γ_β⁻ ⟨N_z⁻−2Z_z⁻⟩ … Numerical solution (xAI Grok-4 cluster, run ID G4-20251205-0312…) … T_MilkyWay = 539.900 ± 0.003 s" | FAIL (Cat B) | 539.9 s inserted then "solved for"; ρ_DM plugged; ⟨N⁻−2Z⁻⟩ not computed from any written −table; run not reproducible/absent. Only written halo↔−PT formula, but no values. |
| HW2 | 17822998:80-87 | "δT/T = (1/2)(δρ_DM/ρ_DM) − (3/4)δβ_PBH + (1/3)δ⟨N⁻−2Z⁻⟩ → σ_T ≈ 1.8 s"; M31 541.1–541.5 s; Cen A 537.6 s | FAIL (retune escape) | Galaxy-local variation clause makes the 539.9 s claim adjustable; inputs (δβ_PBH, δ⟨N⁻−2Z⁻⟩) unwritten. |
| HW3 | 17822998:96-102 | "Explicit Null Predictions: CMB-S4 ΔC_ℓ = 0 at ℓ≈540; LISA Ω_GW(f=1.851 mHz) < 10⁻¹⁴; Extragalactic surveys: no universal 539.9 s signal. Violation of any null prediction falsifies the model outright." | CLOSEST written null — FAIL for gate | Genuinely written nulls with thresholds. Fail: (a) all keyed to 539.9 s / ℓ≈540 (Cat B); (b) they predict ABSENCE of signal = coincide with standard physics → non-discriminating (vacuous as evidence for model); (c) **contradicted** by 17812891:124-125 (LISA peak h_c = 8×10⁻²² at 1.851 mHz) and 18132056:116 (CMB "dip at l=539.9"); (d) no EH/nonlocal link; future external data. |
| HW4 | 17812891_Galactic_Dynamics….txt:122-130 | SKA flat >100 kpc "<0.5 % sinusoidal residuals at exactly 539.9 s"; LISA peak 1.851 mHz h_c=8×10⁻²²; Gaia 539.9 s periodicity; Euclid "null test at ℓ = 540 ± 5"; LSST dwarf σ periodic 539.9 s | FAIL (Cat B + physically vacuous) | 539.9 s modulation of rotation curves/proper motions is unobservable on those cadences/timescales (dynamical times ~10⁸ yr); keyed to Cat B; contradicts HW3. |
| HW5 | 17812891:70-72, :80-81 | v_c² = GM_b/r + 4πGρ_DM r0²[1+0.15 sin(2πt/539.9)](1−e^{−r/r0}); "M_b = A v_flat⁴ (A = 48±2)" | FAIL (inserted) | BTFR normalisation is the empirical McGaugh value; 0.15 amplitude plugged; ρ_DM, r0 free. |
| HW6 | 17812891:117-119 | "σ_8 = 0.810 ± 0.003 (Planck 2018 …) … observed σ_8 = 0.72–0.76 … without tension" | FAIL (retrodiction; conflicts PTW2 S8 0.75/0.83) | Observed values restated. |
| HW7 | 17812891:23 | "v_flat = 229.5 ± 0.3 km s⁻¹" | FAIL | Observed MW value inserted. |
| HW8 | 18111709_Rebuttal_CDM.txt:100-107 | ρ(r)=ρ0(1+r/r_c)^{-2}exp(−δΔA/σ_inh (1−τ_echo/t)); "χ²/dof = 0.75 vs CDM 1.2" | FAIL | Free ρ0, r_c, σ_inh; fit claim, no dataset/null. |
| HW9 | 18425770_Three-Body….txt:190 | "Falsification: If LISA (2027+) detects three-body GW without 539.9 s precursors, adjust δ(t)…" | FAIL (retune) | Explicit adjust-not-falsify, same pattern as SP1. |
| HW10 | 18132056_Light_duality….txt:115-116 | "LIGO O5: … falsify if no signal at χ²/dof>1"; "Simons Observatory CMB: Confirm dip at l=539.9 (0.1% anisotropy)" | FAIL | Cat B period; ℓ is an integer (539.9 ill-defined); contradicts HW3 ΔC_ℓ=0. |
| HW11 | 17990940_Master_List….txt:9-11 (and all clauses) | "If τ_echo deviates >10% from 539.9 s sub-harmonics … adjust δΔ by 0.1 meV" | FAIL (retune) | Already SP1. |
| HW12 | 17822998:92 | "Voyager 1 & 2 PWS archive 540.0 ± 0.1 s plasma density oscillation (confirmed)" | FAIL (unsourced post-hoc) | No archive reference/analysis written; "confirmed" claim, not prediction. Not a repo test. |

## Result
Cat A candidates fully written: **0**. Best-written null set is HW3, but it is Cat B-keyed, non-discriminating (predicts standard-physics null), and contradicted by sibling papers (HW4, HW10).

## Internal contradictions found (written, falsifiable-in-text only)
- LISA 1.851 mHz: null Ω_GW<10⁻¹⁴ (17822998:99) vs peak h_c=8×10⁻²² (17812891:124-125).
- CMB ℓ≈540: ΔC_ℓ=0 (17822998:98) vs "dip … 0.1% anisotropy" (18132056:116); Euclid "null test" (17812891:129) ambiguous.
- Universal vs local: "no universal 539.9 s signal" (17822998:100) vs SKA/Gaia/LSST galaxy-wide 539.9 s (17812891) and SN/LIGO precursors (20709375, 18132056).
(These are corpus-consistency facts; they are not a gate test of physics and involve Cat B quantities.)

## ABSENT (needed for a non-vacuous halo/sim link test)
1. A halo observable derived from EH/L7 quantities without 539.9 s, ρ_DM 0.31, β_PBH, g11/g_s inserted.
2. Written ⟨N⁻−2Z⁻⟩ value from a −element table (table entries copied from +U; no N⁻/Z⁻ distribution written).
3. Reproducible sim artifacts (run G4-20251205-0312, 10⁶ mock galaxies) — absent.
4. A null that discriminates model vs ΛCDM/MOND with stated threshold and dataset available now.
