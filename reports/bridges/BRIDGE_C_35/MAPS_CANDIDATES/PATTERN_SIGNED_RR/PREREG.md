# PREREG: PATTERN_SIGNED_RR (Map-PSR1: signed lift mass per 140Q fibre vs MF2)
Lock: written after explore (data/explore.sha256), before scripts/test.py. Explore never read ρ_res.
Written sources: rev8 tex (reports/self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Bridge_C_Consolidated_rev8_2026-10-19/bridge_c_consolidated_rev8.tex):
- l.134: Q;
- l.156–158: c1 = (−1,1), c2 = (−4,1), w(v) = ½(sgn B(c1,v) − sgn B(c2,v)), with H_s = Σ_v w(v) q^{Q(v+a)+7/20};
- l.272: 140 labels and phases e(B(α,β)), β ∈ {0,−a}.

## Rule
For each label (α,β), with ν = α+v:
M_f(α,β) = (2R+1)^{-2} Σ_{|v_i|≤R} w(v)·e(B(ν,β))·[140Q(ν) ≡ f mod 8].
Pool: ρ_mod(f) ∝ Σ_{140 labels} |M_f(α,β)|, normalized to total 1. The normalization removes the 1/R decay.
Density: a centred square box. Test R = 400 (fresh; explore used 150 and 300). A fibre counts as non-zero iff its normalized mass is > 10⁻⁶.

## Prediction
P1: ρ_mod = ρ_res = (1,8,3,0,7,8,5,0)/32.
- PASS iff max_f |ρ_mod − ρ_res| ≤ 10⁻³ (Category B, numerical) and the supports are equal.
- FAIL otherwise.
- VACUOUS if ρ_mod is uniform on the 6 open fibres.
No a-shift↔{3,7} flip transform is registered (no written reason).
