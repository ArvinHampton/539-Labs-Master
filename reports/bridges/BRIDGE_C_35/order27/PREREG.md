# order27 PREREG (written and hashed before numerics)
## 1. Transport convention (fixed in writing)
For any g ∈ GL₂(Z) with gᵀAg = A, **det g = ±1 alike**, Γ_g is the monomial matrix defined by G_{gα_j, gβ_j} = Σ_k (Γ_g)_{jk} G_{α_k,β_k}. Its entries come from `reduce` applied to the pair (gα_j, gβ_j); this is the same convention as Γ_γ.
The order26 "naive" check computed exactly this matrix for h and found Γ_h ≠ I (3/105 identity rows). That is NOT a contradiction: Γ_h·Cor_K = Cor_{hK} only needs Cor_K to be Γ_h-fixed, not Γ_h = I.
Transport (paper Prop. transport): S^{χ_C}_{gα,gβ} = S^{χ_{g⁻¹C}}_{α,β}. The proof never uses det g, so Γ_g Cor_C = Cor_{g⁻¹C} holds for improper g as well.
## Claimed Category A statement (proof sketch fixed now)
L1 (parity): Cor_{−C} = Cor_C for a unimodular cone C. In the basis (−u1,−u2) the coordinates are (−a,−b). B̄1 is odd and vanishes on Z, B2 is even, and B(u1,u2) and Q(u_i) are unchanged, so the weights agree termwise with the same phases f.
L2: Cor_{hK} = Cor_K for h = −σ, since hK = −(σK); then L1 and Cor_{σK} = Cor_K (v8 Cor. sigma).
L3: Γ_{−I}·Cor_K = Cor_{−K} = Cor_K. Hence Cor_K is fixed by Γ_{−I} and by Γ_h, although neither matrix is I.
## Exact certificates (integer arithmetic: permutation plus exponents mod 9800)
X1 Γ_h = product of Γ_σ = I and Γ_{−I}, in either order (compare perm and exponents exactly). X2 Γ_{−I}² = I, Γ_h² = I. X3 [Γ_h, M] = 0 by exponent multisets. X4 [Γ_h, Γ_γ] exact (report: commute or not).
## Numerical controls
N1 Cor_{hK} = CO and Cor_{−K} = CO (≤1e−12). N2 Γ_h·CO = CO (≤1e−12). N3 order26 values: Cor_B = Cor_K reproduced (blind w.r.t. method, consistent with order26).
## 2. RG18 (group ⟨γ,h⟩)
Fixed object: the orbit O = {Cor_{wK} : w = γ^a h^b, a ∈ {−2,…,2}, b ∈ {0,1}} (10 cones), stacked over x and −1/x on the 216-point grid.
Group projectors: for characters (ε,η) ∈ {±1}², P_{ε,η} = ¼(I+εΓ_γ)(I+ηΓ_h). They are used only if Γ_h and Γ_γ commute (X4); otherwise only the orbit span is used.
Non-vacuity rule (order26 lesson): let W = span{CO, Γ_γCO} (at x and −1/x). r_new = max over the orbit of ‖Cor_{wK} − proj_W Cor_{wK}‖ / ‖CO‖.
If r_new ≤ 1e−10, then every ⟨γ,h⟩ object (average, projector, or orbit combination) is a Γ_γ-image combination of CO, and **RG18 = VACUOUS by rule**. Otherwise test each new direction (orthogonal complement of W in the orbit span) against the weight-1 law: PASS abs ≤ 1e−8; FAIL rel ≥ 1e−3; else inconclusive.
Exact geometric law stated in advance: none is proposed beyond L1–L3.
## Predictions (blind derivation; uses v9/order25 facts Γ_γ² = I)
X1–X3 hold. Orbit collapses to {CO, Γ_γCO} (since Cor_{γK} = Cor_{γ⁻¹K} by Γ_γ² = I and Cor_{hC} invariance), so r_new ≈ 0 ⇒ RG18 VACUOUS.
Rules: no Resonant objects, MAPS_CANDIDATES untouched, no bridge claim, E1–E3 OPEN, Ξ not identified.
