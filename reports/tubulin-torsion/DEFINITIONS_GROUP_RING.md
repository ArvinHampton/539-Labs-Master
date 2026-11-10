# DEFINITIONS — Group-ring reading of Owner claim t58u (Lemma 5 candidate)
Base: DEFINITIONS.md (D1–D4). Every item below not forced by the claim is **invented pending mathematical proof** (as a reading).

GR0. G := ℤ/Mℤ (matches D1; choice invented pending mathematical proof). ℤ[G] = {Σ_g a_g[g]}, [g][g']=[g+g'].
GR1. Regular representation ρ: ℤ[G] → Mat_M(ℤ), ρ(h)e_r = Σ_g a_g e_{r+g}. ρ(h) is the circulant matrix (ρ(h))_{r',r} = a_{r'−r}. Eigenvalues: ĥ(k) = Σ_g a_g ω^{kg}, ω = e^{2πi/M}, k = 0..M−1 (DFT); det ρ(h) = ∏_k ĥ(k). ρ is a ring homomorphism; ρ(h) is normal.
GR2. Layer element (reading (a), adopted): for D3 data (C, w, M) and multiplicities a_{i,c} ∈ ℤ, h_i := Σ_{c∈C} a_{i,c}[c·w_i] ∈ ℤ[G]. Step matrix H := (h_1,…,h_n); transfer T(H) := h_n⋯h_1 ∈ ℤ[G] (commutative), ρ(T) = ρ(h_n)⋯ρ(h_1). "det(ρ(H)) ≠ 0" := det ρ(h_i) ≠ 0 ∀i (⇔ det ρ(T) ≠ 0, multiplicativity).
GR2'. Reading (b): H = block layered adjacency over ℤ[G] on layers 0..n, ρ entrywise → (n+1)M square integer matrix. It is block strictly upper-triangular ⇒ nilpotent ⇒ det ρ(H) = 0 and spectral radius 0 always. Under (b) the hypothesis det ≠ 0 is never satisfied: claim vacuous. (PROVED, one line.)
GR3. "Coefficients in ℤ⁺" := a_{i,c} ∈ ℕ_{>0} for every c ∈ C (positive multiplicity on each allowed step). (Reading; invented pending mathematical proof.) Note ℕ≥0 gives the same no-cancellation results.
GR4. Path weight: a path = (c_1..c_n) ∈ C^n, σ(path) = ∏ a_{i,c_i}, endpoint r_s + Σ c_i w_i mod M. Signed weight W(r_s→r_t) = Σ σ = (ρ(T))_{r_t,r_s}. Unsigned N := same with |a_{i,c}| = (ρ(|T|))_{r_t,r_s}, |T| := |h_n|⋯|h_1|.
GR5. "Total cancellation of path states" := gap Γ := N − |W| ≥ 0 (reading; phrase is ABSENT-as-written, invented pending mathematical proof). Collisions of distinct paths on one residue are NOT cancellation (they add when σ>0).
GR6. "Regular spectral radius" := spr(ρ(h)) = max_k |ĥ(k)| over ℂ; for signed h use |h| := Σ|a_g|[g]; for ρ(T): spr(ρ(|T|)) = ∏ ‖h_i‖_1.
