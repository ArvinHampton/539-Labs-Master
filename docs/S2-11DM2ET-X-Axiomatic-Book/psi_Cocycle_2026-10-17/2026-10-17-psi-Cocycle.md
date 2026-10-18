# ψ, the order-t⁰ S-cocycle of the fundamental-domain E-vector: closed form and analyticity
*2026-10-17, for Arvin Hampton. Box-only work, read-only on the repo. Scripts and outputs: `2026-10-17-psi-cocycle/`.*
*Scope: this is pure q-series and Maass-form analysis. It is separate from HQCC, and it claims nothing about TPC or RH.*

## Verdict: CLOSED FORM (Cat A, with one constant fixed numerically; see the A-audit)

**Main result.** ψ is the Lewis–Zagier **period function** of an explicit vector of weight-0 **Maass forms with eigenvalue λ = 1/4** (spectral parameter s = 1/2). These forms are the Siegel-theta lift of the ray class 𝒦 over the closed geodesic of γ.
- The E-vector is precisely the Lewis–Zagier holomorphic "periodic function" f(z) = Σ_{n>0} A_n n^{s−1/2} e(nz) of these forms. At s = 1/2 the factor n^{s−1/2} is 1.
- For x > 0:

  **ψ(x) = (x / (π√35)) · ( ∫₀^{i∞} [u_R, R_x^{1/2}] − (log ε)/2 ),**  with ε = 6+√35, R_x(w) = Im w / ((w−x)(w̄−x)),

  where [u,v] = u_w v dw + u v_{w̄} dw̄ is the Green 1-form.
- The same formula with a split contour, which is the one used numerically:

  ψ(x) = −(1/π)·[ (x/√35)(log ε/2 − J_R(x)) + J_L(−1/x) ],  J(z) := ∫_i^{i∞}[u, R_z^{1/2}].

**Agreement with the exact values.** The period integral agrees with the exact finite Bernoulli-sum values of ψ (the radial constant terms) on 84 rationals: the 44-point grid that contains the 37 earlier points, plus 40 random rationals with denominators up to 60, of both signs. The maximum deviation is **1.1·10⁻¹³**, the quadrature floor (`psi_all.txt`, `psi_period.txt`). For example, ψ(1) = 0.0068839937604 − 0.0382597122170 i from both routes.

**Consequences.**
- ψ extends **real-analytically to ℝ∖{0}**. In fact it extends holomorphically to Re z > 0, and separately to Re z < 0.
- On x < 0 the correct automorphy factor is **|x|, not x**. This is the (cτ+d)^{1/2}(cτ̄+d)^{1/2} factor of a signature-(1,1) Siegel theta. With it, ψ(−x) = conj ψ(x) (checked to 8·10⁻¹⁴).
- With the holomorphic factor x, the cocycle at negative x is not even bounded: it grows like 1/y (`neg_side.txt`). Our earlier P_s report only tested x > 0.
- So the E-vector **is a vector-valued quantum modular form of weight 1 in Zagier's sense, for the real automorphy factor |cx+d|.** Equivalently it is "weight (1/2,1/2)", the f-function of a λ = 1/4 Maass form. The exceptional set for S is {0}.

**ζ values.** ζ(0,𝒦) = **1/10** and **ζ(−1,𝒦) = 29/60**, both exact rationals, consistent with Siegel–Klingen.

**s = 8 and s = 11.** The same structure carries over. Exact cone-zeta values: ζ_E(0) = 1/6 and ζ_E(−1) = 5/36 for s = 8; ζ_E(0) = 7/18 and ζ_E(−1) = 1129/1296 for s = 11. There are no half-integer powers in either case.

---

## Setup (notation from the P_s report)
- **Lattice and form.** L = Z², Gram A = [[2,7],[7,7]], Q2(ν) = ν₁² + 7ν₁ν₂ + (7/2)ν₂². Also γ = [[−1,−7],[2,13]], ε = 6+√35, a = (7/10, −1/5).
- **Fundamental domain.** F = C₀ ∪ ρ₂C₀ = [e₁, γe₁).
- **E-vector components.** E_{α,β}(τ) = Σ_{ν∈F∩(α+Z²)} e(B(ν,β)) e(τQ2(ν)). Write E_L := E_{a,0} and E_R := Σ_p E_{p,−a}, where p runs over the 35 classes of A⁻¹Z²/Z².
- **Radial expansion.** E(x+iy) = 2I·G(x)/t + κ(x) + O(t), with no t^{−1/2} term.
- **The cocycle.** ψ(x) := κ_L(−1/x) − (x/√35)·Σ_p κ_{p,−a}(x). At rationals this is a finite Shintani-type sum over residue classes mod 4m of B₂, B₁·B₁ and roots of unity (`fastkappa.py`; it reproduces the earlier values exactly). Every ψ(h/m) is therefore algebraic, in Q(ζ_N, √35).

## Category A

### A1. The Maass forms (theta lift over the γ-geodesic)
**Definitions.** Integrate the Siegel theta (weight (1/2,1/2)) over the closed geodesic SO(1,1)⁺/⟨γ⟩ and multiply by √y. Unfolding the γ-orbits and using ∫_ℝ e^{−a·cosh 2w} dw = K₀(a), with geodesic length log ε, gives

  u_L(w) = √y Σ_{ν∈(a+Z²)/⟨γ⟩} K₀(2π|Q2(ν)|y) e(Q2(ν)x),

  u_R(w) = √y [ log ε + Σ_{0≠ν∈A⁻¹Z²/⟨γ⟩} e(B(ν,−a)) K₀(2π|Q2(ν)|y) e(Q2(ν)x) ].

- The sums run over all four regions S±, T±, so negative-norm vectors give negative frequencies. The γ-fundamental cones are [e₁, γe₁) and [f, γf) with f = (1,−1), and their negatives.
- Each Fourier term √y·K₀(2π|n|y)e(nx), and √y itself, is a Δ-eigenfunction with λ = 1/4. So u_L and u_R are λ = 1/4 eigenfunctions.

**Modularity.**
- From Borcherds, *Automorphic forms with singularities on Grassmannians*, Invent. Math. 132 (1998), arXiv:alg-geom/9609022, Thm 4.1 (statement checked online). The Siegel theta of a signature-(b⁺,b⁻) lattice transforms with (cτ+d)^{b⁺/2}(cτ̄+d)^{b⁻/2}·ρ_L. Here b⁺ = b⁻ = 1, so the factor is |cτ+d|, and √y·θ is weight 0.
- Integration over the compact cycle commutes with the transformation.
- Numerical check (`maass_lift.txt`):
  - u_L(−1/w) = u_R(w)/√35 to 6·10⁻¹¹ at three points; the residual is truncation.
  - u_L(w+1) = e(13/20)·u_L(w) exactly.

**Positive Fourier coefficients equal 2E.** The automorph −ρ₁ maps S⁺ to S⁻, fixes a mod Z², preserves the phase e(B(ν,−a)), and permutes the classes p. So the S⁺ and S⁻ parts of the positive coefficients coincide, and f_{u_L} = 2E_L, f_{u_R} = 2E_R. Numerical check: identical for all norms ≤ 25, with deviations 0 and 5·10⁻¹⁴.

### A2. Green-form lemma
**Statement.** For z ∈ H, with the integral taken along the vertical ray from z:
- ∫_z^{z+i∞}[√y K₀(2πny)e(nx), R_z^{1/2}] = C·e(nz) for n > 0, with C = −π/2;
- the same integral is 0 for n < 0;
- ∫_z^{z+i∞}[√y, R_z^{1/2}] = 1/2.

**Proof.**
- R_z(w) is holomorphic in z, and ∂_{w̄}R_z = i/(2(w̄−z)²). Along the ray, R_z = (y+s)/(s(2y+s)) > 0.
- The integral is therefore holomorphic in z: the endpoint term vanishes because v_{w̄} ~ (w−z)^{1/2}. It is also translation-covariant, so it equals e(nx)g(y) with g(y) = C·e^{−2πny}.
- For n < 0 the integral is bounded as y → ∞, which forces C = 0.
- The n = 0 integral reduces to (y/2)∫₀^∞ s^{−1/2}(2y+s)^{−3/2} ds = ½·B(½,1)/2 = 1/2.

**Status.** C = −π/2 was obtained by 30-digit quadrature for n = 1, 2, 3 at two values of z: ratio −1.5707963267949, imaginary parts below 10⁻³⁰ (`lemma_c1.txt`). This is the only constant not derived by hand. It is the s = 1/2 case of the Lewis–Zagier construction ("the period function as the integral of a closed 1-form", Lewis–Zagier, *Period functions for Maass wave forms I*, Ann. Math. 153 (2001), arXiv:math/0101270, Ch. II §2; table of contents checked online).

### A3. Stokes argument giving the closed form
Let Ψ(z) := E_L(−1/z) − (z/√35)·E_R(z), which is holomorphic on H.
1. **Use A2.** c·f(z) = ∫_z^{i∞}[u, R_z^{1/2}] gives c·2E_L(−1/z) = ∫_{−1/z}^{i∞}[u_L, R_{−1/z}^{1/2}].
2. **Pull back by w ↦ −1/w.** Use u_L(−1/w) = u_R(w)/√35 and R_{−1/z}(−1/w) = z²·R_z(w), together with invariance of the Green form under holomorphic pullback. This turns the integral into (z/√35)∫_z^0[u_R, R_z^{1/2}].
3. **Close the contour.** Subtract (z/√35)·∫_z^{i∞}[u_R, R_z^{1/2}] = (z/√35)(2c·E_R(z) + log ε/2). By closedness the result is (z/√35)·∫_0^{i∞}.
   - The branch point of R_z^{1/2} sits on the path and is integrable.
   - The integral converges at 0 because u_R(it) = √35·u_L(i/t) decays exponentially. It converges at i∞ because the constant-term integrand is O(t⁻²).
   - With c = −π/2 this gives **Ψ(z) = (z/(π√35))(∫_0^{i∞}[u_R, R_z^{1/2}] − log ε/2)**.
4. **Analytic continuation.** The right-hand side is holomorphic wherever z² + t² ≠ 0 along the path, i.e. on ℂ∖iℝ. So Ψ continues across (0,∞).
5. **Boundary values.** The Euler–Maclaurin radial expansions hold non-tangentially. Since Ψ is bounded near x > 0, the 1/t terms cancel, and Ψ(x) = κ_L(−1/x) − (x/√35)Σκ = ψ(x).

**Numerical confirmations.**
- Period formula vs. the exact Bernoulli sums: 84 rationals, max deviation 1.1·10⁻¹³ (`psi_all.txt`, `psi_period.txt`).
- A holomorphic polynomial fitted to Ψ using only points with Im z ≥ 0.01 reproduces the real-axis exact values to 2·10⁻¹² at 169 rationals with denominators up to 47 (`lz_test.txt`).
- Ψ(x+iy) → ψ(x) linearly in y (`lz_K.txt`; K = 1/√35 is the only constant for which the singular parts cancel).

### A4. ℝ∖{0} and the |x| factor
- For x < 0, define ψ₋(x) := κ_L(−1/x) − (|x|/√35)Σκ(x). This is the boundary value of E_L(−1/z) + (z/√35)E_R(z), whose singular parts do cancel there.
- ψ₋ equals the same period formula with |x| in the prefactor, to 1.6·10⁻¹⁴ (`neg_side2.txt`).
- ψ₋(−x) = conj ψ(x) holds to 8·10⁻¹⁴. This is consistent with u_L(−w̄) = conj u_L(w), since u_L has real coefficients.
- With the holomorphic factor x, Ψ(x+iy) blows up like 1/y at x < 0 (`neg_side.txt`).
- **Conclusion:** the S-cocycle is real-analytic on ℝ∖{0} for the factor |cx+d|. Near 0, ψ(x) ≈ −0.0549i·x² + 0.0206·x³ (from x = 0.01 and 0.05), so ψ vanishes to second order. It is not analytic at 0, because the two sides are conjugate.
- **Exceptional set: {0}.** T acts by phases only (trivial cocycle), and S and T generate the group, so every h_γ is real-analytic off γ⁻¹∞.

### A5. ζ(−1,𝒦) (`zeta_values.py`, exact rational arithmetic plus a numerical check)
**Method.**
- Σ_{ν∈F∩(a+Z²)} e^{−tQ2(ν)} = 2I/t + ζ_E(0) − ζ_E(−1)·t + ζ_E(−2)·t²/2 − …, with ζ_E(s) := Σ Q2(ν)^{−s}.
- The full Euler–Maclaurin expansion to order t¹ (the ∫⊗point term with B₄ and the point⊗point terms B₁B₃, B₃B₁, B₂B₂) was computed exactly.
- The t^{−1/2} and t^{1/2} coefficients vanish identically (symbolic).

**Values.** ζ_E(0) = 1/10 and ζ_E(−1) = 29/1200. Since N𝔞 = 20·Q2(ν) (P_s report, A2), **ζ(0,𝒦) = 1/10 and ζ(−1,𝒦) = 20·ζ_E(−1) = 29/60**.

**Check.** Direct sums minus 2I/t + 1/10 − (29/1200)t, divided by t², converge as t → 0 (0.1593, 0.1624, 0.1640 at t = 0.02, 0.01, 0.005). So the t¹ coefficient is confirmed, and there is no t^{3/2} term.

**Siegel–Klingen** (partial zeta values of ray classes of totally real fields at negative integers are rational) is satisfied. We did not compare against an independent Shintani cone decomposition.

### A6. s = 8, 11 (exact pieces)
For Q_s = n² + snk + (s/2)k(k+1), Q2 = x² + sxy + (s/2)y², a_s = (s/(2(s−2)), −1/(s−2)):
- **Shared structure.** For every s:
  - Q_s = Q2(ν) + s/(4(s−2));
  - ρ₁ and ρ₂ are automorphs and swap a and −a;
  - γ_s = [[−1,−s],[2,2s−1]] has trace 2s−2;
  - F = C₀ ∪ ρ₂C₀ is a γ_s fundamental domain in S⁺.
  So 2P_s = E_s + 1 + θ₃ − Θ_hol,s holds as the same cone bookkeeping (no new series check was run).
- **Residues.** s = 8: D = 48, 2I = log(7+4√3)/(4√3), field Q(√3). s = 11: D = 99, 2I = log(10+3√11)/(3√11), field Q(√11).
- **Exact values.** ζ_E(0) = 1/6, ζ_E(−1) = 5/36 for s = 8; ζ_E(0) = 7/18, ζ_E(−1) = 1129/1296 for s = 11. The t^{±1/2} coefficients are 0 in both cases, and the numerical remainders are O(t²).
- **Baker obstruction.** It transfers verbatim: the log-unit term is irrational over the algebraic coefficients.

## Category B (sketch, not verified)
- **B1. ψ machinery for s = 8, 11.** The same theta-lift argument should give λ = 1/4 Maass forms and real-analytic ψ_s. We did not compute this. For s = 8 the eigenvalue of γ₈ is (2+√3)², the square of the totally positive unit. So E₈ may cover each ideal of its class twice, or else the coset is not preserved by the automorph of 2+√3. The ray-class identification for s = 8 and 11 (conductor, signs) was not done; we only have the cone-zeta values.
- **B2. Other rows.** Only the (a,0) row of the S-cocycle was computed. The lift argument applies to every row of the 36-component vector, but we did not check the others numerically.
- **B3. Structure of u_R.** u_R (a mix of ray-class characters) presumably decomposes into λ = 1/4 Eisenstein and dihedral cusp forms, as in Maass's 1949 construction. We did not decompose it.

## Self-audit
- The κ code (`fastkappa.py`, vectorized, exact integer phases) reproduces the earlier `psi_grid.txt` and `evector2.txt` values digit for digit.
- The period integral is computed independently: Bessel series on y ≥ 1 with Gauss–Legendre quadrature. Changing the quadrature moves the result by ≤ 3·10⁻¹⁶.
- **Inputs not re-derived:**
  - the constant C = −π/2 (numerical only, 30 digits);
  - Borcherds Thm 4.1 applied to our coset/character components. The resulting S-law was checked numerically to 10⁻¹¹ but not derived symbolically;
  - non-tangential validity of the Euler–Maclaurin expansion. This is standard, and the numerical fits are consistent with it.
- **Not used as proof:** Bruggeman–Lewis–Zagier, Mem. AMS 237 (2015) no. 1118, which covers general cofinite groups and non-cuspidal forms. It is cited for context only, and its scope was checked online.

## Files (`2026-10-17-psi-cocycle/`)
- Cocycle evaluation and continuation: `fastkappa.py`, `lz_continuation.py` (`lz_K.txt`), `lz_test.py` (`lz_test.txt`)
- Maass lift and the lemma: `maass_lift.py` (`maass_lift.txt`), `lemma_c1.py` (`lemma_c1.txt`)
- Period-integral checks: `psi_period.py` (`psi_period.txt`), `psi_all.py` (`psi_all.txt`)
- Negative axis: `neg_side.py` (`neg_side.txt`), `neg_side2.py` (`neg_side2.txt`)
- Zeta values: `zeta_values.py` (`zeta_values.txt`)
- Copies from the P_s report: `weil_test.py`, `evector.py`
