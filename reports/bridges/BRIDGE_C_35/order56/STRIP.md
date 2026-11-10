# order56 STRIP — Category A write of the H_v → H_ν strip (source derivation only; no test)
Written 2026-10-24 before any order56 computation. Local modular sources only. RG* labels.

## Sources (read-only)
- order2/scripts/lib2.py: C = P_orth − H (PIECES/WALLS); phase e(xQ(α+v)+B(α+v,β)) on INTEGER v; walls get ±½ (sgn 0 = 0).
- order2/PREREG.md §weights: w(v) = ½(sgn B(c1,v) − sgn B(c2,v)) = ½(sgn n + sgn(n+21k)).
- order52 RESULTS RG44: oriented Zwegers pair (−c1,c2) = ((1/5,−1/5),(4,−1)), B = −4; the identity fixes orientation, combined weight is a sum of two sgn terms on the two lines L1 = n, L2 = n+21k.
- order54/55 (rg45c.py direct/pred): completion along the walls uses sgn of ν-forms, λ1 = n+θ1, λ2 = n+21k+θ2, θ1 = α1, θ2 = α1+21α2 (ν = α+v); Ξ_compl := Σ_w A1(R_w), R_w = ½Σ(E(z_w)−sgn z_w)·phase·e^{−tQ(ν)}, A1(R_w) = √(π/Q(u_w))·Σ_{r<P} m_r·B̄1((r+θ_w)/P), B̄1(0)=0 (RG45c-2″ PASS).

## Derivation (forced)
H_v weight w_v(v) = ½Σ_i sgn L_i(v); H_ν weight w_ν(v) = ½Σ_i sgn(L_i(v)+θ_i) (L_i(α) = θ_i, linear).
Δ(v) := w_v − w_ν = Σ_i Δ_i(L_i(v)), Δ_i(ℓ) = ½[sgn ℓ − sgn(ℓ+θ_i)], ℓ ∈ Z.
Δ_i(ℓ) ≠ 0 only for ℓ in the closed interval between 0 and −θ_i: finite set ("strip"). For θ>0: ℓ=0 → −½; −θ<ℓ<0 → −1; ℓ=−θ (if integer) → −½ (mirror for θ<0; θ=0 → empty).
Each level set {L_i = ℓ} ∩ Z² is ONE full primitive lattice line: L1: (ℓ,0)+b·(0,1), Q(u)=7/2; L2: (ℓ,0)+b·(21,−1), Q(u)=595/2.
Full-line t^{−1/2} coefficient = 2 × lib2 ray coefficient (√π/2)·mean/√Q(u), i.e. √π·mean_line/√Q(u) (mean over one exact phase period of the line).
Hence A1(Δ) = Σ_i Σ_ℓ Δ_i(ℓ)·√(π/Q(u_i))·mean_{(ℓ,0)+Zu_i}(f).
Bookkeeping: C = P_orth − H_v = P_orth − H_ν − Δ; Ĥ := H_ν + Σ_w R_w. So
  A1(C) = A1(P_orth) − A1(Ĥ) + Ξ_compl − A1(Δ),
and Â1 := A1(C) − Ξ_compl + A1(Δ) = A1(P_orth − Ĥ) (= order55's "A1 − [strip] − Ξ_compl" with [strip] := −A1(Δ), the strip's contribution to C).
Status: algebra Category A. The input A1(Ĥ) = 0 is only an order5 §1.4 proof sketch (Category B); it is tested, not assumed, in order56 PREREG.
Not derived/assumed: any identification of Â1 with the v12 shadow Ξ (v12 §40.3: Ξ "not written as an explicit series").
