# ADDENDUM F — Owner 18:06 "all RESOLVED" (same review; bounded exact checks; No CERT)
Source: the attachment path was NOT readable from PP's box. This review works from the claims as Physicist relayed them. The embedded .tex question is document content: no manuscript created.
## Group / graph map
- FALSE (stands): U140 ≅ C2×C4×C6 is not cyclic, and is not a Galois group of order 48 attached to ζ49.
- Repair, PROVED under these hypotheses:
  - Hypotheses: G=U140; S={c·w_i} with each w_i a UNIT mod 140 (otherwise c·w_i ∉ G); a>0.
  - Definition: C_xy=Σ a δ(yx⁻¹ ∈ S) is a weighted directed Cayley graph.
  - L=D−C is symmetric iff S=S⁻¹ and a_s=a_{s⁻¹}.
  - Otherwise use C_sym=(C+Cᵀ)/2. This is a valid positive conductance Laplacian, but it LOSES direction and layer order, so the original matrix is not preserved.
  - Self-loops (s=1) cancel in L.
  - Connected iff S generates G (needs checking for the actual S).
  - Coefficient extraction gives a valid PARTIAL map; it is not the original layered product.
## Normalization
- Φ=L⁺q is mean-zero but ‖Φ‖=‖L⁺q‖ is not automatically 1. Imposing ‖Φ‖=1 rescales q (needs q≠0).
- If q≡0 globally on a connected graph, mean-zero gives Φ=0, which CONTRADICTS norm 1.
- If q=0 only on intermediate layers, E=Σ_boundary Φ_x q_x, which need not vanish (Addendum E path example).
- "E_d=0" is FALSE under the stated hypotheses.
## Degree / cross terms
- For a Cayley graph every vertex has degree Σa (regular), so the degree term is (Σa)‖Φ‖² = Σa. This is a single-layer sum, NOT the layered path product N.
- Cross = Φᵀρ(h)Φ is a quadratic form, not a trace. Example: ρ=I₂, Φ=(1,0) gives ΦᵀρΦ=1 but tr=2.
- What holds: λ_min ≤ Φᵀρ_symΦ ≤ λ_max for unit Φ (Rayleigh).
- Character-table invertibility diagonalizes ρ(h) (Fourier) but does not identify the complex amplitude sum |W|.
- Status: the proof step FAILS; the original N/W identity is OPEN (not refuted).
## Geometry (convention dσ_a=−½ε_abc σ_b∧σ_c now stated: progress)
- Kasner p=(−1/3,2/3,2/3): Σp=1 and Σp²=1, so it is a valid Bianchi I vacuum. But p2=p3, so "all distinct" is FALSE.
- Direct substitution into the quoted R11 = Ḣ1 + H1·ΣH + [a1⁴−(a2²−a3²)²]/(2a1²a2²a3²):
  - Kinematic part: H1=p1/t and ΣH=1/t, so Ḣ1+H1ΣH = −p1/t²+p1/t² = 0.
  - Curvature part: a2=a3 makes the bracket a1⁴=t^{−4/3}, and the denominator is 2t^{−2/3}·t^{4/3}·t^{4/3}=2t².
  - Result: R11 = ½t^{−10/3} ≠ 0.
  - CONFIRMED: the trajectory is NOT an exact vacuum Bianchi IX solution. Kasner epochs are asymptotic approximations only.
- Also: the earlier C1212 formula is still unverified, so it cannot be used.
- Replacement statement: "Vacuum Bianchi IX solutions with all a_i unequal exist and are non-flat (literature: Mixmaster / Ringström), so C≠0 on an open set of times." This is a cited existence result, not derived here.
- Remaining obligations: an exact solution or a constraint-satisfying initial data set; the Weyl components from the stated coframe; the 5D embedding and junction.
## Precise closures this round
1. Symmetric Cayley-Laplacian construction (conditions stated above).
2. Normalization contradiction for q≡0.
3. Quadratic form ≠ trace (explicit example).
4. Degree term = Σa (regular Cayley graph).
5. Kasner trajectory fails R11 exactly.
Everything else is unchanged.

## F.1 Source confirmation (read OWNER_TRANSFER_NORMALIZATION_BIANCHI_1806.txt, 95 lines) and corrections
- Line 6: the "cyclic Galois group of order 48" is FALSE (confirmed in the source).
- Line 8: a_{i,c} ∈ ℤ⁺ for EVERY c ∈ G. If w_i is a unit, then S={c·w_i : c∈G}=G, so the graph is complete: CONNECTED automatically. This corrects F's "check generation" for this restrictive case. But w_i is stated only as an integer (∈ℤ); a nonunit w_i takes c·w_i outside G and is undefined. Unit-ness is still required.
- Line 14: C_xy = a_{i,(yx⁻¹)w_i⁻¹}. It is symmetric iff a_{i,c} = a_{i,c⁻¹w_i⁻²} for all c. This is not stated, so (C+Cᵀ)/2 is required otherwise.
- Line 25: diag Σ_{z∼x}C_xz includes the self-loop C_xx (for c = x·x⁻¹·w_i⁻¹, i.e. c = w_i⁻¹, always present here). With off-diagonal −C_xy, the row sums equal C_xx ≠ 0, so 𝟏 ∉ ker L and line 30's kernel claim fails. CORRECT convention: L_xx = Σ_{z≠x}C_xz (equivalently L = D − C with loops cancelled). Line 47 then gives degree Σ_c a_{i,c} − a_{i,w_i⁻¹}, not Σa.
- Line 30: Φ=L⁺q is unique and mean-zero, but ‖Φ‖=1 is an extra constraint on q. Line 57 sets q≡0 ⇒ Φ=0, which CONTRADICTS line 27 (norm 1). Confirmed.
- Line 52: quadratic form ≠ trace. In G (48 vertices), take ρ([1])=I₄₈ and Φ=(e₁−e₂)/√2 (mean 0, norm 1): ΦᵀρΦ = 1, but tr ρ = 48. The line-52 "trace ⇒ |W|" step is UNSUPPORTED; the original N/W stay OPEN.
- Lines 48–49: N := Σa is a single-layer degree. This is a definition, not the original layered path count.
- Lines 76–80: the Kasner substitution into the quoted R11 (line 75) leaves ½t^{−10/3} ≠ 0: NOT exact IX vacuum (confirmed). Also p₂=p₃, so "distinct" is false.
- Line 82: this C1212 (curvature terms dropped) is derived nowhere, and it is not exact for IX.
- Line 70: "iff Kasner-like trajectory" is unproved.
- Lines 89–92: none of the four rows is RESOLVED. Status: map = partial (with the conditions above); normalization = contradiction; identification = unproved; geometry = not exact.
- Line 96 (.tex offer): document content only. Not executed; no manuscript created.
