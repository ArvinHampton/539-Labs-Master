# NOTE — corrections to the Implications report (2026-10-19)

This note accompanies `2026-10-19-Implications-Unification-RTA-multik-K3.md` in this folder. The report itself is pushed unedited; the corrections below are recorded here only.

1. **K3 scope: N₂ only.** `K3_140_Check_2026-10-19/2026-10-19-K3-140-check.md`, §6, supersedes §4 and IC-6 of the report. The 140-label representation is the Weil representation ρ_{N₂} of N₂ = {x ∈ Z² : x₂ even} (Gram [[2,14],[14,28]]), not ρ_{N₁} for N₁ = (Z², 2A); their T-spectra differ. Every K3 statement of the report applies to N₂ only, not N₁ (and the K3 statements made there for M_t are not carried forward). The report's open alternative "ρ_L or ρ_L*" is resolved: ρ_rev ≅ ρ_{N₂} ≅ ρ_T* (Bridge C rev8, Theorem 16.2 and Corollary 16.6).
2. **Weil₅ entry superseded.** The entries `Weil_Z5_even_dim3` and `Weil_Z5_odd_dim2` in `checks.json` ("order_mod_scalars" 81 and 67) are superseded by `weil5.json` (groups of order 120, scalars {±1}, quotients of order 60 with element orders {1,2,3,5}). Only `weil5.json` is used (IC-3, Category B).
3. **Entropy value.** The entropy of the K3 automorphism induced by γ² is 2 log(6+√35) ≈ 4.9558 (spectral radius 71 + 12√35 ≈ 141.993), not ≈ 4.93 as printed in the K3-140 check, K-8.

Labels: Category A = proved or exact; Category B = numerical/heuristic; kept separate. No TPC or RH claim; distinct from HQCC termination claims. CORE_FREEZE holds.
