# PREREG order22 — the unit γ acting on the corner term (geometric map RG9) and cone additivity (RG9b)
Written 2026-10-24 (America/Chicago) BEFORE any order22 numerics. CORE_FREEZE. MAPS_CANDIDATES untouched; no Π / ±1 grading / path predicate. Inputs read-only: order18/data/a2_arrays.npz (CO = A2_corner at XS, 216×105).

## Geometric objects (Category A facts, written here)
- γ = [[−1,−7],[2,13]] acting on ν by ν ↦ γν; γᵀAγ = A (checked exactly in the script), unit 6+√35, log unit 2L = log(6+√35).
- Arcs on the negative hyperboloid: the orthant arc z(μ) = cosh μ ĉ′ − sinh μ e1, μ ∈ [0,L], from ĉ′ to −ĉ1, has length L = ½ log(6+√35) (cosh L = √(7/2)), i.e. exactly half the unit arc (length 2L, the arc from a point to its γ-image). In ν-space the orthant arc corresponds to the cone K = cone(e1,e2) (the closed first quadrant, where Q > 0).
- γ⁻¹ = [[13,7],[−2,−1]]; γ⁻¹K = cone(u1,u2) with u1 = γ⁻¹e1 = (13,−2), u2 = γ⁻¹e2 = (7,−1); det(u1,u2) = 1, Q(u1) = 1, Q(u2) = 7/2, B(u1,u2) = 7.
- General corner invariant (iterated Euler–Maclaurin, as paper v6 Thm A2even, for a unimodular cone (u1,u2) with half weights on the boundary rays, ¼ at 0): for ν = a u1 + b u2 on class r mod N with coordinates (ρa, ρb),
  Corner_{(u1,u2)}(α,β;x) := Σ_r f_r [ B̄1(ρa/N)B̄1(ρb/N) + (B(u1,u2)/(4Q(u2)))·B2(ρa/N) + (B(u1,u2)/(4Q(u1)))·B2(ρb/N) ].
  For (e1,e2) this is A2_corner (coefficients ½ and 7/4).
- Transport (Category A): S^E_{γα,γβ} = S^{E∘γ}_{α,β} (substitute ν = γμ), and E∘γ = χ_{γ⁻¹K} + χ_{−γ⁻¹K}. With Γ the monomial matrix of the reduction (γα_j, γβ_j) → e(ph)·companion k (paper rule (iii) + (i),(ii)), the t^0 corner coefficients satisfy (Γ·A2_corner)_j = Corner_{(u1,u2)}(α_j,β_j;x).

## Map RG9 (geometric, residual-internal; NEW prediction)
(Γ·A2_corner)(x) = Corner_{(u1,u2)}(x) at all 216 points × 105 companions, and the corner term is NOT γ-covariant: Γ·A2_corner ≠ A2_corner.
Metrics (absolute): e9 = max |Γ·CO − Corner_{γ⁻¹K}|; non-vacuity ν9 = ‖Γ·CO − CO‖_F / ‖CO‖_F.
PASS iff e9 ≤ 1e−9 AND ν9 ≥ 1e−3. FAIL iff e9 ≥ 1e−6. If e9 ≤ 1e−9 but ν9 < 1e−3: "vacuous" (γ-covariant), not a pass.
## Map RG9b (cone additivity under subdivision by the ray (1,1))
Corner_{(e1,(1,1))} + Corner_{((1,1),e2)} = Corner_{(e1,e2)} = CO (each subcone unimodular). Metric: max abs difference. PASS ≤ 1e−9; FAIL ≥ 1e−6. Non-vacuity: each subcone term has ‖·‖_F ≥ 1e−3‖CO‖_F.
## Controls
- C1: Corner_{(e1,e2)} reproduces CO: max abs ≤ 1e−9 (else void).
- C2: Γ·G = G for the Gauss means (A0/I) from order4b: max abs ≤ 1e−12 (γ-invariance of the 35-component law vector data).
## Predictions
RG9 PASS (non-vacuous); RG9b PASS. A pass is residual-internal geometry, not a Residual↔Resonant bridge; no Resonant object is used. E1–E3 OPEN.
nice, OMP_NUM_THREADS=1, <3 GB; no push/sends; new files only.
