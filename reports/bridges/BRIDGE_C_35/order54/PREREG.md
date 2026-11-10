# order54 PREREG (Bridge C, 35-component law vector; RG* labels; CORE_FREEZE; new files only)
## RG45c-1 (source audit, Category A): endpoint convention h(0)
Written sources: order5 PREREG §1.1 "sgn 0 = 0"; §1.3 E(z)=erf(√π z) (odd, E(0)=0); order5 zwegers.py np.sign (sign 0 = 0); order18 a2.py B1b(u)=0 at u∈Z.
Hence h(0) = (E−sgn)(0)·G(0) = 0 = ½(h(0+)+h(0−)) (h odd): the midpoint convention, B̄1(0)=0. Forced, not chosen.
## RG45c-2 (numeric, Category A-numeric): A1(R_j) sawtooth formula
R_j := ½ Σ_{v∈Z²} (E−sgn)(z_j(ν)) f(v) e^{−tQ(ν)}, f = e(B(ν,β)+xQ(ν)) (lib2 phase_ints), ν=α+v, y=t/2π,
z_1 = √10·ν1·√y (wall u1=(0,1), λ=ν1, θ1=α1), z_2 = (ν1+21ν2)√(2y/17) (wall u2=(21,−1), λ=ν1+21ν2, θ2=α1+21α2).
Prediction: √t·R_j → A1_j = √(π/Q(u_j)) · Σ_{r=0}^{P−1} m_r B̄1((r+θ_j)/P), Q(u1)=7/2, Q(u2)=595/2,
m_r = period mean of f on the line through base v=(r,0) in direction u_j (order53 RG45b), P = ℓ-period of m (lcm of line periods, from a2.period along (1,0)), B̄1(0)=0.
(Derivation: Poisson along lines gives √(π/(tQ(u_j)))·m_ℓ·h(√t(ℓ+θ)); EM jump J=h(0+)−h(0−)=−2, ∫h=0, h′ even ⇒ no t^0 jump term; error O(t).)
Direct: line-by-line exact summation (b-range to Gaussian tail < 1e−18, λ range |λ|√t ≤ 9·scale), t ∈ {4e−3, 2e−3, 1e−3}; A1_num = quadratic-in-t Richardson extrapolation of √t·R_j to t=0.
Sample: XS[:6] × all 105 companions × 2 walls (fixed now; runtime-limited, no post-hoc change).
PASS iff max |A1_num − A1_pred| ≤ 1e−6·max(1,|A1_pred|) over the sample, AND the gating control FAILS:
 control = one-sided convention B̄1(0)=−½ (i.e. h(0)=h(0+)), required to miss by >1e−4 on ≥1 case with θ_j+r∈Z and m_r≠0; if no such case exists in the sample, the control is reported VOID and the verdict states the endpoint is untested numerically.
## RG46: runs only if an explicit Ξ_compl / A1−Ξ_compl tied to the v12 shadow Ξ results. A1(R_j) alone is not such an object (it is a t^{−1/2} coefficient, not a shadow); expected SKIP.
## Phase-aware k≠0 bound: not written in sources; not attempted.
