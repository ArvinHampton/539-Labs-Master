# PROOF — Wilson C1 closed form under stated assumption (2026-11-03)
Label: invented pending mathematical proof (assumption is INVENTED, not from corpus/Owner). No physics CERT. REPORTS ONLY.

Written β (PROOF_22_TO_13_AND_WILSON.md, Phase 2): β(C_1) = −(7/20)·(x_11²ℏ²/(R_x²T_c²))·C_1, κ := x_11²ℏ²/(R_x²T_c²).
INVENTED RG ASSUMPTION A1: one-loop truncation, convention β := μ dC_1/dμ, R_x, x_11, T_c μ-independent (κ constant), no operator mixing with O_2,O_3.

## Theorem (PROVED under A1). C_1(μ) = C_1(μ_0)·(μ/μ_0)^{−(7/20)κ}; equivalently C_1(μ_bio) = C_1(μ_0)(μ_0/μ_bio)^{(7/20)κ}.
Proof: d ln C_1/d ln μ = −(7/20)κ constant; integrate from ln μ_0. Uniqueness: linear ODE, Picard–Lindelöf. ∎
Consistency: substitute: μ d/dμ [C_0(μ/μ_0)^{−aκ}] = −aκ C_0(μ/μ_0)^{−aκ} = β(C_1), a=7/20; boundary C_1(μ_0)=C_0. ✓
Corpus/Owner form (1+κ)^{−7/20} is μ-independent, so its μ-derivative is 0 ≠ −(7/20)κC_1 for κ≠0: FALSE under A1. ∎
Small-κ note: (1+κ)^{−7/20} ≈ 1 − (7/20)κ = first-order of (μ/μ_0)^{−(7/20)κ} only if ln(μ/μ_0) = 1 — a coincidence, not a derivation.

## If R_x runs (κ = κ(μ))
C_1(μ) = C_1(μ_0)·exp(−(7/20)∫_{ln μ_0}^{ln μ} κ(μ') d ln μ'). (PROVED, linear ODE.)
(1+κ_*)^{−7/20} is recovered iff ∫ κ d ln μ = ln(1+κ_*) over the flow — e.g. if κ(μ) = dln(1+K(μ))/dlnμ with K going 0→κ_*. That requires a specific R_x(μ) not written anywhere: ABSENT. One-loop truncation also unjustified when κ is not small: invent-pending.
