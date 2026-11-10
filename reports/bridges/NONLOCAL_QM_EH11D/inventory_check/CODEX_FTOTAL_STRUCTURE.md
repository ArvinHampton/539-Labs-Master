# CODEX F_total — written structure extract (no numerics, no PREREG)
Source: theorems/periodic-table-codex.txt:44-69 (identical text at zenodo 20709375 txt:46-69). Written formula only.

F_total = F_Coulomb^rel + F_SO + F_torsion + F_flux + F_leak   (T:48,52-53)

| term | written form (T:53-60) | standard symbols | free / unwritten params | Cat B plugs |
|---|---|---|---|---|
| F_Coulomb^rel | −(Z_eff α ħ c / r²)(1 + (α Z_eff)²/n²) Ω₁₁D | α, ħ, c, r, n | Z_eff(Z, orbital) — no screening rule written; Ω₁₁D | — |
| F_SO | (1/(2 m_e² c²))(1/r)(dV/dr)(L·S) Ω₁₁D | m_e, c, L, S | V(r) undefined (circular w/ V_eff "obtained by direct integration", T:66); Ω₁₁D | — |
| F_torsion | γ_LQG S_e ρ_puncture Θ_hyp · g₁₁ Φ ψ · sin(2πt/539.9) Ω₁₁D | γ_LQG (Immirzi; value not stated) | S_e, ρ_puncture, Θ_hyp, g₁₁, Φ, ψ — none given numerically; Ω₁₁D | 539.9 s; "61 punctures" |
| F_flux | g_s X^M(t)(1 + ρ_DM/10) sin(2πt/539.9) ∇Φ Ω₁₁D | — | g_s, X^M(t), ρ_DM (local value/units), ∇Φ; "/10" unexplained constant | 539.9 s; ρ_DM coupling |
| F_leak | κ_dark √δ(t) (1 + δa_μ^{−U} g_{−U}² m_μ²/(8π² M_{−U}²))(1 + β_PBH e^{−M_PBH/k_B T}) Ω₁₁D | m_μ, k_B | κ_dark, δ(t), δa_μ^{−U}, g_{−U}, M_{−U}, M_PBH, T | β_PBH=0.18 (from 18132056), −U sector |

Dimensional note (structure only): F_leak has no r-dependence or force units written; F_SO as written is an energy-operator form, not a force. Terms are not dimensionally homogeneous as written.

## Free parameter count (written, unvalued)
Ω₁₁D (1, global; contradicted as "absorbs all scaling" T:18) + Z_eff rule + V(r) + 6 torsion (S_e, ρ_puncture, Θ_hyp, g₁₁, Φ, ψ) + 4 flux (g_s, X^M, ρ_DM, ∇Φ) + 7 leak (κ_dark, δ, δa_μ^{−U}, g_{−U}, M_{−U}, M_PBH, T) ≈ **≥19 unvalued quantities**, plus γ_LQG convention.
## Cat B plugs: 539.9 s (×2 terms), β_PBH = 0.18, −U/PBH sector, 61-puncture count.

## Prerequisites for a Z=1–118 table test (none present)
1. Numeric Ω₁₁D fixed *before* comparison (not fit). 2. Explicit Z_eff(Z,n,l) rule. 3. Values for all ≥19 params, Z-independent or with written Z-dependence. 4. Defined observable map (F_total → ionization energy / fine structure) — T:66-69 asserts but gives none. 5. Time-average treatment of sin(2πt/539.9) terms. 6. Reference dataset (NIST) + tolerance written in advance.

## ABSENT artifacts
- periodic_table_539labs.json — ABSENT (find over /workspace/quantum-comp, 2026-10-24 22:17 CDT (mtime))
- Numeric Ω₁₁D value; Z_eff rule; any computed Z-table; "539 Labs Raman sideband" data referenced at C:100-101.
