# order53 RESULTS
PREREG sha256 07e07423…b591 (PREREG.sha256), hashed before tests.
## RG45b: PASS, Category A (finite exact checks; data/rg45b.json)
The sources determine the wall data uniquely: order5 §1.4(ii), the order5 completion constants (Z PASS r=6e−16), and the order18 lines() decomposition.
- Lines parallel to c_j^⊥: u1=(0,1) (Q=7/2) and u2=(21,−1) (Q=595/2). T1 checks the orthogonality and T2 checks that each family of lines covers Z² exactly once.
- Offsets: θ1 = α_1 and θ2 = α_1+21α_2. Here α is the companion's own shift label from order2 lib2. These are not new symbols.
- Character: f(ν) = e(B(ν,β)) (the lib2 phase_ints phase).
- Multiplicity: m_ℓ = mean of f over one period along line ℓ. It is periodic in ℓ (T3, max dev 0) and does not depend on the base point (T4, 2.2e−16). Tested on all 105 companions × 216 XS.
- The E-arguments are fixed by order5: κ1 = √10·√y and κ2 = √(2y/17).
Limitation: the closed-form A1(R_j) = γ_j·√(π/Q(u_j))·J·Σ_r m_r·B̄1-type sawtooth is not proved here. The Euler–Maclaurin endpoint and sign convention at ℓ+θ ∈ Z (the h(0) value) is not fixed by any written source, and no numeric check of it was preregistered. It stays a sketch.
## RG46: SKIPPED. RG45b gives the wall data, not an explicit Ξ_compl or A1−Ξ_compl object. The v12 shadow Ξ is still unidentified with any of these.
Ξ: unidentified. Bridge: NO.
Open next: (a) prereg a numerical check of the A1(R_j) sawtooth formula, with the endpoint convention fixed, against direct Ĥ−H radial asymptotics. (b) Then attempt to match Σ_j A1(R_j) to the v12 Ξ, and run RG46 only if an explicit object results. (c) Phase-aware k≠0 residual bound: not written, left open.
