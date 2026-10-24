## 10. Parity Dominance for odd k = 17..33: the analytic layers

Path shorthand as above. The objects are those of section 7.

101. **Theorem (tail step, odd k = 17..33, computer-assisted).** Let k be odd with 17 ≤ k ≤ 33 and N1 = 1500. Assume the local-CLT bound of entry 91 (the hypothesis H_CLT: for every n ≥ N1 − 33 and every u in the block window, |√(2π)σP(S = m) − e^{−(m−μ)²/(2σ²)}| ≤ δ with the cell constants used there) and the block inequality of entries 79 and 91. Then for every allowed d ≥ D₀(k) the contribution of the terms outside the block window to E_d is at most η_t·O_d with η_t = 10⁻⁶. Here D₀ = ⌈(N1/α₁)²⌉; in particular D₀ = 53 864 548 (k = 31) and 55 887 431 (k = 33). The tail margin T(D₀) ranges from −39.38 (k = 17) to −28.55 (k = 33), and the margin is monotone in d ≥ D₀ (gap γ ≤ −0.0085 against the required −2.5/√D₀).
    *Proof.* 
    - For even n, log A_n(e^{−u/n}) ≤ nΦ₁(u). On the odd j the bound follows from the convexity of log(1 + e^{−x}) (midpoint bound); on the l-sum it follows from the monotonicity of −log(1 − e^{−x}). Hence e_n ≤ exp(√d·F(α,u)) by Chernoff.
    - The function F is convex in α and is evaluated at the endpoints of α-boxes. The central odd term has a certified lower bound C*. The window lemma (α ∈ [α₁, α₂] implies n ≥ N1 and u ∈ [UA, UB]) gives the separation into block and tail.
    - All constants are enclosed in 256-bit ball arithmetic. Every lemma is written with explicit constants in `SF/A60_tail_rederivation/DERIVATION.md`, and the code is independent of `SF/A56_A49_audit`.
    - The same statement is proved in `SF/A61_clt_proofs/PROOFS.md`, items 21–28. The evaluation was implemented a third time without the convexity step (`SF/A61_clt_proofs/code/tail61.py`), and it also closes for all nine k.
    *Supplementary exact checks* (`SF/A60_tail_rederivation/`):
    - (−1)^d g_k(d) = E_d − O_d holds for d ≤ 20 000 and all odd k = 17..33, with 0 mismatches, both against the q-series and against the product formula of entry 74.
    - The exact zero sets for k = 27, 29, 31, 33 agree with entry 92.
    - The two-prime modular certificate up to D_cert = 10⁶·⌈D₀/10⁶⌉ ≥ D₀ has double zeros exactly on Z_k and no single-prime zero.

102. **Theorem (all steps of the local-CLT layer and of the tail step are proved).** Every analytic step used in the computer-assisted proofs of entries 79 (for k = 17..25) and 91 (k = 27..33) at N1 = 1500 is a proved lemma. There are 28 steps, as listed in `SF/A61_clt_proofs/prereg.md`. All constants (δ, R_k, D₀, T) are unchanged. In particular:
    - (i) **Shift bound.** For 0 < p ≤ ½, |y| ≤ t < π and h = pe^{iy}/(1 − p + pe^{iy}): |h(1−h)(1−2h)| ≤ v((1−2p) + p|y|)/cos(y/2)³ ≤ (v(1−2p) + tvp)/cos(t/2)³, with v = p(1−p) and constant 1.
    - (ii) **Abel bound.** For v_j nonincreasing, Σ_{odd j≤n} v_j(1 − cos jθ) ≥ Σ_{odd j ≥ 1/|sin θ| + 1} v_j.
    - (iii) **Upper bound on log A_n.** For even n, log A_n(e^{−u/n}) ≤ nΦ₁(u) + log 2. This is the only parity used, because the e_n are even-n terms.
    - (iv) **Remaining steps.** The main-arc Taylor bound with the exact third cumulant and a fourth-derivative bound, the Gaussian tail via erfc, the five minor-arc regimes, the Riemann-sum enclosures uniform in n ≥ 1467, the block-inequality algebra, the closed form of Φ₁ with dilogarithms, the tiny-α estimate, the monotonicity in D, the central odd term, the window lemma, and the assembly E_d ≤ (R + η_t)O_d.
    *Proof.* `SF/A61_clt_proofs/PROOFS.md`, items 1–28. Two of them are short enough to give here:
    - (i): |1 − p + pe^{iy}|² = 1 − 4v sin²(y/2) ≥ cos²(y/2) and |1 − p − pe^{iy}| ≤ (1 − 2p) + p|y|.
    - (ii): Abel summation against the nonincreasing v_j. The required partial sums of the terms 1 − cos jθ over odd j are nonnegative and monotone, with C(J) ≥ (J + 1 − X)/2 for X = 1/|sin θ| (PROOFS.md item 2).
    *Finite checks* (`SF/A61_clt_proofs/code/`, `out/`), all exact, symbolic or in ball arithmetic:
    - 28 symbolic identities;
    - Φ₁ against quadrature to 10⁻⁵⁷;
    - 2079 containment checks of the cell enclosures, 1512 checks of the point constants and 3200 checks of the tiny-α estimate, all with 0 violations;
    - exact rational contiguity and coverage of the cell lists.
    *Dependencies, stated exactly.*
    - The numerical constants are produced by the code of `SF/A56_A49_audit`. That code was checked against the proved lemmas term by term and by the containment tests above.
    - The local-CLT layer and block inequality were also re-derived and re-implemented independently (`SF/A59_clt_rederivation`). The certified δ is no larger than the first layer's in all 500 cells of width 0.005 on [0.40, 2.90], and the block ratios are R_k = 0.7905, 0.8068, 0.8229, 0.8391 for k = 27, 29, 31, 33 (entry 91, last row).
    - The tail step has three implementations (A56, A60, A61).

## 11. Dimensions of S(ρ_s) at s = 27, 29, 33, 39

103. **Theorem (bounds at s = 27, 29, 33, 39).** Assume TB, TB4 and TB5. TB5 is the theta-lift theorem of TB2 for every lattice (Λ_𝔭, Q/p) in the genus of A_s (`SF/A37_dihedral_count/prereg.md`).
    - (i) **Class data, unconditional.** For s = 27, 29, 33, 39 (n = 675, 783, 1023, 1443): h(4n) = 6, 6, 8, 8; Cl ≅ Z/6, Z/6, Z/2 × Z/4, Z/2 × Z/4; |Cl[2]| = 2, 2, 4, 4; and (s − 1) + √n is a unit of norm +1.
    - (ii) **Lower bounds.** dim S(ρ_27) ≥ 3, dim S(ρ_29) ≥ 3, dim S(ρ_33) ≥ 5 and dim S(ρ_39) ≥ 5. The sector ranks are:
      - s = 27: (3+,5+) 1, (3−,5−) 2;
      - s = 29: (3+,29+) 1, (3−,29−) 2;
      - s = 33: (3+,11+,31+) 1, (3+,11−,31−) 1, (3−,11+,31−) 2, (3−,11−,31+) 1;
      - s = 39: (3+,13+,37+) 1, (3+,13−,37−) 2, (3−,13+,37−) 1, (3−,13−,37+) 1.
      In the sectors with an Eisenstein part, cuspidal combinations are used. The genus lifts over every class of Cl² give no further rank at any of the four s.
    - (iii) **s = 27.** The sectors (3+,5−) and (3−,5+) have label dimension 0, (3+,5+) = 1 and 2 ≤ (3−,5−) ≤ 3. Hence 3 ≤ dim S(ρ_27) ≤ 4.
    - (iv) **s = 29.** 2 ≤ dim(3−,29−) ≤ 4.
    *Proof and certificate.* 
    - (i) comes from Gauss reduction cycles and composition (`SF/A36_hecke_character/scripts/classdata.py`; `SF/A48_s_dims/results_v2/classdata_A48.json`).
    - (ii) uses exact ranks mod ℓ ≈ 10¹² of lifts, Hecke images and genus lifts over the coefficient columns. Fewer vectors can only lower a rank, so each rank is a lower bound (`SF/A48_s_dims/logs/genus_s27.log`, `genus_s33.log`, `genus_s39.log`, `out/genus_s39.json`; `SF/A37_dihedral_count/logs/genus_s29.log`).
    - The upper bounds in (iii) and (iv) are certificates of the frozen certifier, relative to TB:
      - `SF/A48_s_dims/certs/hcert_s27_3p_5p_M3_Q40_Y45-710-35-12.json` gives (3+,5+) ≤ 1;
      - `SF/A9_hecke_family/certs/hcert_s27_3m_5m_M6_Q40.json` and `SF/A48_s_dims/certs/hcert_s27_3m_5m_M3_Q40_Y45-710-35-12.json` give (3−,5−) ≤ 3;
      - `SF/A48_s_dims/certs/hcert_s29_3m_29m_M3_Q40_Y45-710-35-12.json` gives (3−,29−) ≤ 4.
    - The forms counted are K_s-dihedral by entry 26.
    *Scope.* No upper bound on dim S(ρ_29), dim S(ρ_33) or dim S(ρ_39) is proved. The certifier runs at s = 33 and s = 39 are on hold: their exact stage does not fit in the memory available. No statement about them is made here.

## 12. RTA's Bridge Series C and the 35-component law vector: leading order

Notation as in sections 3 and 8. Q_7(n,k) = n² + 7nk + (7/2)k(k+1). RTA's orthant series is P_orth = Σ_{n,k≥0} q^{Q_7(n,k)}. With c1 = (−1,1) and c2 = (−4,1) the cone weight is w(v) = ½(sgn B(c1,v) − sgn B(c2,v)) = ½(sgn n + sgn(n+21k)), and H_7 = Σ_{v∈Z²} w(v)q^{Q_7(v)}. RTA's Bridge Series is C = P_orth − H_7. For x = h/m let G(x) = (2m)^{−2} Σ_{(n,k) mod 2m} e(xQ_7(n,k)), and let I = log(6+√35)/(2√35). Radial limits are taken along q = e(x)e^{−t}, t → 0+.

104. **Theorem (the leading profile of RTA's C and the space V).** G(x) = e(7x/20)·K2_0(x), where K2_0 = G_{a,0}, and G ∉ V. Hence the leading profile I·G of C is not in the span of the 35-component law vector. The leading profile of q^{−7/20}·C is I·K2_0. This is a nonzero element of V and a cyclic vector of V.
    *Proof.* 
    - **The identity.** Aa = (0, 7/2), so B(ν,a) = (7/2)ν₂ and Q_7(ν) = Q(ν) + B(ν,a) = Q(ν+a) − Q(a), with Q(a) = ½aᵀAa = −7/20. Translation ν ↦ ν + a maps Z² onto a + Z², so G(x) = e(7x/20)·mean_{ν∈a+Z²} e(xQ(ν)) = e(7x/20)K2_0(x).
    - **Non-membership.** If G ∈ V, then on X₂₁₆ the column of G would lie in the span of the 105 component columns, and the 216 × 106 matrix would have rank ≤ dim V = 36 (entry 40) over Q(ζ). The values lie in Z[ζ_L][1/(4m)²] with L = 3 531 528 000. Reduction at a prime p ≡ 1 mod L is a ring homomorphism, so it cannot raise the rank. The rank mod p is 37 at p = 17 657 640 001, 21 189 168 001, 35 315 280 001 and 42 378 336 001. Every run also verifies G = e(7x/20)K2_0 exactly mod p at all 216 points (`reports/bridges/BRIDGE_C_35/scripts/testA.py`, `data/testA.json`).
    - **Cyclic vector.** K2_0(1) ≠ 0 by entry 18. V is stable under S and T (entry 40) and dim End(V) = 1 (entry 97 at s = 7). Since V ≅ E is irreducible (entries 32 and 41), the S,T-orbit of K2_0 spans V. ∎

105. **Theorem (radial asymptotics of P_orth, H_7 and C at every rational).** For x = h/m and t → 0+:
    - t·P_orth(e(x)e^{−t}) = I·G(x) + O(t^{1/2});
    - t·H_7(e(x)e^{−t}) = O(t^{1/2});
    - t·C(e(x)e^{−t}) = I·G(x) + O(t^{1/2}).
    *Proof.* 
    - **Sum–integral lemma.** Let K ⊂ R² be a closed sector. Let Q be a quadratic form with Q ≥ c|v|² (c > 0) on a closed sector containing K∖{0} in its interior. Let ℓ be linear and f: Z² → C be N-periodic. Fix a residue r and tile R² by the cells r + Nu + [0,N)². For a cell inside K, |φ_t(p) − N^{−2}∫_cell φ_t| ≤ √2N·sup_cell|∇φ_t|, where φ_t = e^{−tQ} and p is the base point. On the cell, |∇φ_t| ≤ Ct(|p|+1)e^{−tc|p|²/2} for t ≤ 1. Summed over p this is O(t^{−1/2}). There are O(R) boundary cells with |p| ≤ R, and they contribute O(Σ_R e^{−tcR²/2}) = O(t^{−1/2}). Since ∫_Kφ_t = t^{−1}∫_K e^{−Q}, summing over residues gives Σ_{v∈K∩Z²} f(v)e^{−tQ(v)} = mean(f)·t^{−1}∫_K e^{−Q} + O(t^{−1/2}). Replacing Q by Q + ℓ, or changing the weights on the two boundary rays, changes the sum by O(t^{−1/2}).
    - **Orthant.** On [0,∞)², Q(n,k) ≥ n² + (7/2)k². Q_7 = Q + (7/2)k is integer valued, and e(xQ_7) is 2m-periodic, with mean G(x). With z = ρ(1,λ), ∫_{[0,∞)²} e^{−Q} = ∫_0^∞ dλ/(2Q(1,λ)). The roots of Q(1,λ) = (7/2)λ² + 7λ + 1 are (−7 ± √35)/7, so the integral is (2√35)^{−1}·log((7+√35)/(7−√35)) = log(6+√35)/(2√35) = I.
    - **Cone.** B(c1,v) = 5n and B(c2,v) = −n − 21k. So w = +1 on the interior of K₊ = {n ≥ 0, n + 21k ≥ 0}, w = −1 on the interior of K₋ = −K₊, w = ±½ on the boundary rays, and w = 0 elsewhere. K₊ is spanned by (21,−1) and (0,1), and Q(a(21,−1) + b(0,1)) = (595/2)a² + 140ab + (7/2)b² is positive definite for a, b ≥ 0. Apply the lemma to K₊, and to K₋ through v = −u. The mean of u ↦ e(xQ_7(−u)) over Z²/2mZ² equals G(x), because negation permutes residues. So the two leading terms cancel. ∎

106. **Theorem (vector-valued S-law of RTA's C at leading order).** Let Λ_C(y) = lim_{t→0+} t·C(e(y)e^{−t}). For every rational x > 0,
    Λ_C(−1/x) = I·e(−7/(20x))·(x√35)^{−1}·Σ_{p∈D} e(−B(p,2a))·K3_p(x).
    Thus the leading profile of q^{−7/20}C, together with its images under x ↦ x + 1 and x ↦ −1/x (the latter with weight |x|^{−1}), spans exactly V, and S and T act on it by the matrices of entry 94.
    *Proof.* 
    - By entries 104 and 105, Λ_C(y) = I·e(7y/20)·K2_0(y).
    - The S-law of entry 39 with α = a and β = 0 gives K2_0(−1/x) = (x√35)^{−1}·Σ_p G_{p,−a}(x).
    - Since A(2a) = (0,7) ∈ Z², the second rule of entry 37 gives G_{p,−a} = e(−B(p,2a))·G_{p,a} = e(−B(p,2a))·K3_p.
    - The spanning statement follows from entry 104.
    *Certificate (consistency).* The identity, with Λ_C replaced by I·G, holds exactly at all 216 points of X₂₁₆, modulo two primes ≡ 1 mod a level containing every root of unity involved, with √35 = −i·Σ_k (k/35)ζ₃₅^k. There are 0 mismatches (`reports/bridges/BRIDGE_C_35/data/testB_exact.json`). ∎

## 13. RTA's Bridge Series C: order t^{−1/2}

Notation as in section 12. For each of the 105 pairs (α,β) of section 3, with μ the representatives in [0,1)² of `SF/A35_lawspace_exact/symbols.py`, the companion series is
S_{α,β}(τ) = Σ_{v∈Z²} wt(v)·e(B(α+v,β))·e(τQ(α+v)), where wt(v) = 1[n ≥ 0, k ≥ 0] − w(v).
For (α,β) = (a,0) one has Q(a+v) = Q_7(v) − 7/20, so S_{a,0} = q^{−7/20}·C. B1(y) = y − ½.

107. **Theorem (order-2 expansion).** Fix (α,β), a rational x = h/m and N = 2m. A piece is given by a sign ε, an offset c ∈ Z² and an integer basis U = (u1,u2). For it put:
    - p = Q(u1), r = Q(u2), q = B(u1,u2), Q̃(z) = Q(Uz), l_i = B(α+c, u_i);
    - f(z) = e(xQ(α+c+Uz) + B(α+c+Uz, β));
    - mean(f) = N^{−2}Σ_{z mod N} f(z) and W_i = N^{−1}Σ_{z mod N} f(z)B1(z_i/N), with z_i ∈ {0, …, N−1};
    - Ar = log((q+√Δ)/(q−√Δ))/(2√Δ), with Δ = q² − 4pr;
    - J_a = (√π/4)·(2/(4pr−q²))·(2√r − q/√p) and J_b = (√π/4)·(2/(4pr−q²))·(2√p − q/√r).
    Then, as t → 0+,
    t·Σ_{z∈Z²_{≥0}} f(z)e^{−tQ(α+c+Uz)} = mean(f)·Ar + t^{1/2}·[−mean(f)(l1J_a + l2J_b) − (√π/2)(r^{−1/2}W_1 + p^{−1/2}W_2)] + O(t).
    For a ray {c + bu : b ≥ 0}, t·Σ_{b≥0} f(c+bu)e^{−tQ(α+c+bu)} = t^{1/2}(√π/2)Q(u)^{−1/2}·mean_{b mod N} f(c+bu) + O(t).
    S_{α,β} is the following signed sum of pieces and rays:
    - the closed orthant (U = I, c = 0), with sign +1;
    - the 21 pieces r·e1 + N·(21,−1) + N·(0,1) of K₊ (r = 0..20), with sign −1;
    - the 21 pieces −r·e1 + N·(−21,1) + N·(0,−1) of K₋, with sign +1;
    - the rays N(0,1) and N(21,−1), with weight +½;
    - the rays N(0,−1) and N(−21,1), with weight −½.
    Consequently t·S_{α,β}(e(x)e^{−t}) = A0(x) + A1(x)t^{1/2} + O(t), with A0 = I·G_{α,β}(x) and A1 given by the sum of the terms above.
    *Proof.*
    - **(a) Periodicity.** Shifting w = α + c + Uz by Nu (u ∈ Z²) changes the phase by x(N·B(w,u) + N²Q(u)) + N·B(u,β). Aα lies in Z² or in (0, 7/2) + Z², so B(w,u) ∈ ½Z and x·N·B(w,u) ∈ Z. Next, x·N²Q(u) ∈ 2mhZ. Finally, β ∈ {0, a} and B(u,a) = (7/2)u₂ give N·B(u,β) ∈ Z.
    - **(b) Decomposition.** Write n = 21j + r with 0 ≤ r < 21. Then n + 21k ≥ 0 iff k ≥ −j, and (n,k) = r e1 + j(21,−1) + (k+j)(0,1). This gives K₊ ∩ Z² as the disjoint union of the 21 pieces. The rays n = 0 and n + 21k = 0 lie in the r = 0 piece, and the origin receives weight 0.
    - **(c) Bounds.** In every piece q ≥ 0 and p, r > 0 (orthant: 1, 7, 7/2; other pieces: 595/2, 140, 7/2). So Q̃ ≥ κ|z|² on z ≥ 0 with κ = min(p,r). For F_t = e^{−tQ(α+c+Uz)} and t ≤ 1 there is a constant K such that:
      - F_t ≤ Ke^{−tκ|z|²/2};
      - |∇F_t| ≤ Kt(|z|+1)e^{−tκ|z|²/2};
      - |∇²F_t| ≤ K(t + t²(|z|+1)²)e^{−tκ|z|²/2}.
    - **(d) One-dimensional lemma.** Let g ∈ C²[0,∞) with g, g′, g″ integrable, and let 0 ≤ α′ < N be an integer. Then Σ_{j≥0} g(α′+Nj) = N^{−1}∫_0^∞ g − B1(α′/N)g(0) + R, with |R| ≤ C_N(sup_{[0,N]}|g′| + ∫|g″|). To see this, apply second-order Euler–Maclaurin to h(s) = g(α′+Ns), with |P₂| ≤ 1/12. Then use ∫_0^∞ h = N^{−1}∫_0^∞ g − N^{−1}∫_0^{α′} g and ½ − α′/N = −B1(α′/N).
    - **(e) Two dimensions.** Apply (d) in z1 for each fixed z2 ≡ β′.
      - By (c), the remainders summed over z2 are O(1).
      - Apply (d) again in z2 to N^{−1}∫_0^∞F_t(s,z2)ds. Its first derivative is O(1) on [0,N], and its second derivative has integral O(1).
      - The boundary term B1(α′/N)Σ_{z2≡β′}F_t(0,z2) equals B1(α′/N)N^{−1}∫_0^∞F_t(0,b)db + O(1).
      - Hence Σ_{z≡(α′,β′), z≥0} F_t = N^{−2}∫∫F_t − N^{−1}B1(β′/N)∫_0^∞F_t(s,0)ds − N^{−1}B1(α′/N)∫_0^∞F_t(0,b)db + O(1).
      - Multiply by f(α′,β′) and sum over residues.
    - **(f) Integrals.**
      - Substituting z = u/√t gives ∫∫F_t = t^{−1}(Ar − √t(l1J_a + l2J_b)) + O(1).
      - ∫_0^∞F_t(s,0)ds = ½√(π/(tp)) + O(1) and ∫_0^∞F_t(0,b)db = ½√(π/(tr)) + O(1).
      - The ray statement is (d) at order 0.
    - **(g) Closed forms.** With z = ρ(1,λ), Ar = ∫_0^∞ dλ/(2Q̃(1,λ)) and J_a = (√π/4)∫_0^∞ Q̃(1,λ)^{−3/2}dλ. The antiderivative of (rλ² + qλ + p)^{−3/2} is 2(2rλ+q)/((4pr−q²)√(rλ²+qλ+p)). J_b follows by symmetry, and A0 = I·G_{α,β} follows as in entry 105. ∎
    *Check.* For the orthant alone at x = 0 with (α,β) = (a,0), the formula gives (√π/4)(1 + (7/2)^{−1/2}) − (7/2)J_b = 0.5256172043….

108. **Corollary (algebraicity at order 2).** For every companion S_{α,β} and every rational x, A1(x)/√π is an algebraic number.
    *Proof.* By entry 107, A1/√π is a finite sum of products of:
    - roots of unity (the values of f);
    - rationals (B1 weights, l_i, signs);
    - the numbers 2/(4pr−q²), √p, √r, 1/√p and 1/√r with p, q, r rational. ∎

109. **Certificate (order 2 on the leading-order zero set).** Let Z0 = {x ∈ X₂₁₆ : 2 | m or 5 | m} (105 points). At every x ∈ Z0 and at x = −1/5, the order-2 coefficient A1(x) of q^{−7/20}C = S_{a,0} is nonzero. Since A0(x) = I·G(x) = 0 there (entry 18), t·|q^{−7/20}C(e(x)e^{−t})| = |A1(x)|·t^{1/2} + O(t) at these points. The smallest value is min |A1| = 0.12292…, and |A1(−1/5)| = 0.42858….
    *Certificate.*
    - The formula of entry 107 is evaluated as follows. The weights for each phase are exact rational histograms. Cosines, sines, square roots and √π are taken in mpmath interval arithmetic at 60 digits.
    - At all 106 points the interval for |A1|² excludes 0, with interval width at most 6·10⁻⁵⁹ (`reports/bridges/BRIDGE_C_35/order2/scripts/map2_interval.py`, `data/map2_interval.json`). ∎
