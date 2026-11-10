# NL DERIVED: B2 settled — CGR N=2 moment maps, gravitino-shift superpotential, and the BKV sign flip vs the odd HW ℤ₂
2026-11-09_2012 CST (America/Chicago). **NL derived proposal.** Nothing adopted. Junction: **UNSOLVED** (19a88b19), unchanged.
Authority: **OW t4426 d5eaeef3** ("Pursue all open"); follow-up to NL_DERIVED_BPS_CALIBRATED_WALL_MN2_2026-11-09_2007.md (704df3ee…), item B2. Citations per OW 3f160803 + 36683379 (math checked; a citation never makes a claim PROVED). Nomenclature OW f1d167d1 (the resonant algebra is not used here).
Source: CGR arXiv 1906.08900 §5.3 and App. D ((5.15)–(5.26), (D.14)–(D.21)), (2.5)–(2.6), (3.8); text at /workspace/pp-audit-kk/cgr.txt.
Scripts: /workspace/nl-bps-b2-2011/ — n2_moment_maps.py 709543f7… / .log 00165bd9…; bkv_signflip.py f17b40b2… / .log a41b2489…; each with a .sha256 sidecar.
Limits: new files only. No CERT, no Gemini, nothing sent, no agent messaged. Tip 7cddb188… checked before and after.

**Tally: PROVED 4 · CONDITIONAL 3 · OPEN 0 · REFUTED 0 · total 7**

**χ branches:** every item here is a statement about the bulk 5D theory and the ℤ₂ action. It holds identically in **[χU]** (χ-uniform) and **[χS]** (χ-smeared); no item depends on the source profile.

## 1. N=2 data re-checked
- **C1 (PROVED; exact, n2_moment_maps.py).** CGR's N=2 data are internally consistent at z^a = 0:
  - C_IJK h^I h^J h^K = 1 with C₀₁₂ = √3/2 and h^I = (Σ², −Σ⁻¹Ω⁻¹, −Σ⁻¹Ω)/√3.
  - g_xy = 3∂h^I∂h^J a_IJ = diag(6/Σ², 2/Ω²), which reproduces the (5.16) kinetic terms.
  - (D.14) with the moment maps (D.19), N_A N^A of (D.21) (only k₁ = l∂_ξ and k₂ = ∂_ξ act at z = 0, with g_ξξ = e^{4ϕ}) and W^x = 0 reproduces the (5.16) potential **for all (Σ, Ω, ϕ)**, i.e. including the squashing scalar w.
  - (5.16) at w = 0 equals (3.8) at ψ = 0, T = 1, so it is the potential used in B1.
  - The moment-map normalisation of k₂ checks: |dP₂|²_g = ¼|k₂|²_g = e^{4ϕ}/4.
- **C2 (PROVED; exact).** At z = 0 every P⃗_I points along the 3-direction, so P⃗ = ½h^I P⃗_I has a **fixed direction**, with
  - P = −(√3/(12ΩΣ))(Ω²e^{2ϕ} + 2ΩΣ³ + l e^{2ϕ} + 2).
  - **W_B1 = −2√3 g P** identically on the (φ, λ) slice w = 0 (residual 0). So W_B1 = 2√3 g|P| wherever P < 0, which includes MN2 and its neighbourhood.
  - On the full 3-scalar space (Σ, Ω, ϕ) the extension W = −2√3 g P satisfies **V = 2G^{ij}∂_iW∂_jW − (4/3)W²** exactly, with G = diag(6/Σ², 2/Ω², 4).
  - The hypermultiplet part 2G^{ϕϕ}(∂_ϕW)² equals the 8g²N_A N^A term exactly (the moment-map identity). So the hyperino shift is the gradient of the same W.
  - W can change sign where P = 0; this is the sign change seen on branch +1 in 2007 B3. The supersymmetric flows are those of |P| on each side of that locus.

## 2. Is W the supersymmetric superpotential?
- **C3 (CONDITIONAL, only on the general N = 2, D = 5 fermion-shift formulas: gravitino shift ∝ g P^r σ_r, gaugino shift ∝ g P^x, hyperino shift ∝ g N, as in the general theory on which CGR (D.14) rests; not re-derived here).**
  - Since P⃗ has a fixed direction (C2), the gravitino shift has the single eigenvalue magnitude |P|. The flat-domain-wall BPS equations are then A′ ∝ ∓|P| and X′ ∝ G^{-1}∂|P|.
  - Their normalisation is fixed by the Ward identity, which C1–C2 verify: V = 2|∂W|² − (4/3)W² with W = 2√3 g|P|. These are exactly the B1 equations A′ = −W/3, X′ = W_X/30 on the (φ, λ) slice.
  - So **B2 is confirmed, not refuted.** The B1 flows are BPS flows of the N=2 subtruncation, preserving 4 of its 8 supercharges (γ_r ε = ε).
- **C4 (CONDITIONAL; group theory, not computed).** In the N=4 parent, take the four gravitini in the 4 of USp(4) ≅ Spin(5), restricted to the SO(2) × SO(3)-invariant sector. Invariance forces the mass matrix to be proportional to the identity on each doublet, and the symplectic-Majorana condition relates the two doublets, so both doublets have |eigenvalue| = W.
  - Consequence: W-flows and a BPS wall would preserve **8** Poincaré supercharges (4D N = 2), as B2 stated.
  - The N=4 shift matrix was not evaluated.

## 3. BKV sign flip, re-derived
- **C5 (PROVED; bkv_signflip.py, exact).** Setup: covering space r ∈ ℝ with the wall at r = 0, the kept side r > 0 on a W-flow (A′ = −W/3), and its mirror image A(r) = A(−r), X(r) = X(−r) on r < 0. The Killing-spinor equations are δψ_r: ε′ + (W̃/6)γ_r ε = 0 and δψ_x: ½A′γ_r ε + (W̃/6)ε = 0, where W̃ is the superpotential function the fermions see on each side.
  - r > 0: γ_r ε = +ε and ε = e^{A/2}ε₀.
  - r < 0 with **no flip** (W̃ = +W): γ_r ε = −ε. The projection is opposite on the two sides, so no nonzero continuous spinor exists and no supersymmetry survives.
  - r < 0 **with the flip** (W̃ = −W = sgn(r)·W extended): γ_r ε = +ε on both sides, ε = e^{A(|r|)/2}ε₀ is continuous, and the ℤ₂ action ε(−r) = γ_r ε(r) is satisfied.
  - The δ-function balance gives W̃′ ⊃ 2W(0)δ(r), so [A′] = −2W/3 = −T/6 and **T = 4W**, matching 2007 B4.
  - **So a ℤ₂-even global Killing spinor exists iff W flips sign across the wall.** This is the BKV condition, derived here rather than cited.
- **C6 (CONDITIONAL, on CGR (2.5)–(2.6) as printed and on the standard 5D ↔ 11D gamma-matrix map Γ_r = γ_r ⊗ 𝟙 on the surviving internal spinors).** The 5D flip is the odd HW ℤ₂:
  - Under g → −g at fixed (gA^{ij}, metric, scalars), (2.5) is even (g⁻² only).
  - (2.6) is odd term by term: the leading term goes as g⁻³; the F-term goes as g⁻³·g·F with F^{ab} = g⁻¹R̄; S₍₃₎ = 0 in this sector. So G₄ → −G₄, with the twist gA^{ab} = ω̄ unchanged.
  - W ∝ g flips.
  - 11D parity r → −r combined with C → −C is a symmetry of 11D supergravity: the C∧G∧G term picks up (−1)³ from C → −C and −1 from orientation reversal, so the total sign is +1. Parity acts on spinors by Γ_r.
  - Hence **odd G₄ (f825dfff) ⇔ W̃ = sgn(r)W**, which is compatible. The surviving spinors at the wall satisfy Γ_r ε = +ε, the HW projection.
  - The S⁴ flux N → −N, a jump of 2N = 9760, consistent with f825dfff.

## 4. Consequence for the 2007 file
- **C7 (PROVED; logic).** 2007 B2's hypothesis is now discharged up to C3, which uses only the general N=2 shift formulas, and C6.
  - B4–B7 therefore stand as statements about **supersymmetric** walls: no BPS ℤ₂ wall with the IR side kept and σ ≥ 0 Poincaré content exists in the level-0 sector on Bolza, in either χ branch.
  - B12 (χ-dependent walls) is unaffected and handled in the companion B12 file.

## 5. Junction / gap impact
- None. **Junction UNSOLVED, count gap unchanged.** Nothing adopted.

## 6. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 4 | C1, C2, C5, C7 |
| CONDITIONAL | 3 | C3, C4, C6 |
| OPEN | 0 | — |
| REFUTED | 0 | — |

Check: 4 + 3 + 0 + 0 = 7.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
