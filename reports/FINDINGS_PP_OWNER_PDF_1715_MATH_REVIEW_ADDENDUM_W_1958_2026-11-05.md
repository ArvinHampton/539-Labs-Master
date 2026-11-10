# Addendum W: bounded math review of the t4134 appended claims (mock modular, 3-adic, Iwasawa)

**Basis.** This review works from Physicist's relay. I did not have the source text of t4134. There was no simulation, no new research, no compiling and no CERT.

**Labels.** FALSE means proved false. ND means not defined, so the statement can't be assessed. UNS means unsupported, a non sequitur. VALID means correct as stated.

## Finite or algebraic claims

1. **B48 rank 36 with ker B = ker S0 ∩ ker(S_M T).** ND as written, because H is missing.
   - The proved fact is rank[S0; S_M R_t H] = 36 for the original weights. The tuned weights give 48 (Addendum V).
   - The original and tuned ranks must be kept distinct.
2. **"Nonzero Gram determinant" together with rank 36: FALSE.**
   - The Gram matrix of 48 vectors spanning a rank-36 space is singular, so det = 0.
   - The two claims contradict each other.
3. **C̃_xy = σ(a_{x⁻¹y}) − a_{w⁻¹} (one constant subtracted from every entry) called a "spectral shift": FALSE.**
   - Subtracting κ from every entry subtracts κJ, a rank-1 change. Here J is the all-ones matrix.
   - It changes only the trivial-character eigenvalue, by −48κ, and leaves the other 47 unchanged.
   - A spectral shift is −κI.
4. **K_B = {p < B : p | 140, (140/p) = −1}: FALSE (the set is empty).**
   - If p | 140 then (140/p) = 0, so no prime qualifies.
   - The constructive fix is p ∤ 140.
5. **"Character table invertible over F = Q(√35)": ND over F.**
   - The table of C2×C4×C6 has entries i and ω, which are not in F.
   - It is invertible over L = Q(√35, i, √3). That is the correct statement.
6. **det B_red = product of regular-representation factors.**
   - VALID for a group-ring element H: det ρ(H) = Π_χ λ(χ).
   - FALSE for B. B is not a group-ring element, and it is singular (rank 36).
7. **Positive weights imply nonzero real parts of eigenvalues: FALSE.**
   - Counterexample: C2 with H = 1 + g has eigenvalues 2 and 0.

## Mock modular claims

8. **M = Σ c(n) qⁿ with c(n) given only as "trace identifiers": ND.**
9. **ψ = Σ_{m ∈ Z¹²∖0} λ0(m) m q^{‖m‖²/280}: FALSE as a "unary weight-3/2" form.**
   - m is a vector, so ψ is vector-valued.
   - A rank-12 theta series with a linear harmonic polynomial has weight 12/2 + 1 = 7, not 3/2.
   - If λ0 is even, the m and −m terms cancel, giving ψ ≡ 0.
   - Constructive: a weight-3/2 unary theta requires rank 1, namely Σ_n χ(n) n q^{n²/N} with χ odd.
10. **Derivative of the completion C.** The completion is C = (i/2)^{1/2} ∫_{−τ̄}^{i∞} ψ̄(−z̄) (z+τ)^{−1/2} dz.
    - The claimed derivative −(i/2) τ^{−1/2} ψ̄(τ) is FALSE. The derivative depends on y = Im τ, not on τ.
    - The later lower-endpoint form is correct: ∂_τ̄ C = (i/2)^{1/2} (2iy)^{−1/2} ψ̄(τ) = (4y)^{−1/2} ψ̄(τ), up to branch.
    - With ξ := 2i y^{1/2} ∂_τ̄ (no conjugation), ξC = i ψ̄(τ). So the claim ξM = ψ̄ is FALSE by a factor of i.
    - Corrected normalization, either one works:
      - define ξ := 2 y^{1/2} ∂_τ̄, which gives ψ̄; or
      - use the standard ξ_{1/2} = 2i y^{1/2} \overline{∂_τ̄}, which gives −i ψ, up to branch.
11. **Γ0(140) weight 1/2 with an unspecified multiplier and group character χ_a(d): ND.**
    - The theta multiplier ν_θ and the character must be specified. The condition 4 | 140 does hold.
12. **"Kernel 12 ⇒ shadow/capacity closed": UNS.** The capacity link remains OPEN.

## 3-adic and Iwasawa claims

13. **3 is inert in Q(√35): VALID.**
    - 35 ≡ 2 (mod 3) is a non-residue, so x² − 35 is irreducible mod 3.
    - 3 ∤ 140, so 3 is unramified.
14. **v3 c(n) ≥ −⌊n/3⌋: ND**, because c(n) is undefined.
15. **∫_U χ dμ ≡ Tr B_red (mod 3^k) for ALL compact open U: FALSE unless Tr B_red = 0.**
    - Split U = U1 ⊔ U2. Additivity of the integral gives 2T ≡ T (mod 3^k) for every k, so T = 0.
    - There is also a domain mismatch: units mod 140·3^k versus Z3^×.
16. **Θ3μ = proj_Λ lim Σ_{j ∈ O_F3/3^k} λ0(j) j: ND.** No lifts or convergence are given, and the isotropic Λ has no specified form.
17. **Ultrametric ⇒ leakage zero / security: UNS.**
18. **"The norm on C3 is discrete": FALSE.**
    - |C3^×| = 3^Q, which is dense.
    - F3 = Q3(√35) is unramified quadratic, so |F3^×| = 3^Z is discrete. That part is TRUE.
19. **v3 det B_red = 0 ⇒ strict contraction: FALSE.**
    - Counterexample: I, which has det 1 and v3 = 0 but is an isometry, not a strict contraction.
    - **Integral inverse:** an integral inverse also needs integral entries. Counterexample: diag(1/3, 3) has det 1 but is not integral.
20. **Γ = 1 + 3Z3 with topological generator 4: VALID**, since v3(4 − 1) = 1.
21. **α_i(k0) = 0: ND**, because the analytic family is undefined.
22. **L_j = −∫ log3 dμ_j / Tr(Frob | ker B_j).**
    - The claim "avoiding 5 and 7 ⇒ the denominator is a 3-adic unit" is FALSE.
    - Counterexample: the identity on a 3-dimensional kernel has trace 3, with v3 = 1. The trace can also be 0.
    - The matrix entries are ND.
23. **Coleman edge integral (vector L·log + geom): ND.** No curve, type or uniformizer is given.
24. **Stability or security under arbitrary deformation: UNS.**

## Status

- Original rank 36 is PROVED, and tuned rank 48 is PROVED (Addenda R, V). Keep them distinct.
- Capacity is OPEN.
- No simulation is warranted until items 8, 11, 14, 16, 21 and 23 are defined.
- No CERT, and the tip is untouched.

## W.1 — errata

- **Item 10 corrected.** Use the standard ξ_{1/2} f = 2i y^{1/2} \overline{∂_τ̄ f}. Only the derivative is conjugated; the leading 2i is not.
  - From ∂_τ̄ C = ψ̄ / (2√y), we get ξ_{1/2} C = 2i y^{1/2} · ψ / (2√y) = +iψ. It is NOT −iψ.
  - ξ is antilinear, so ξ(iC) = −i · ξC = ψ.
  - The alternative normalization ξ := 2 y^{1/2} ∂_τ̄, with no conjugation, gives ψ̄, and that still stands.
- **Item 9 narrowed.** The weight 7 = 12/2 + 1 holds only under the hypotheses of a modular lattice and a harmonic coefficient.
  - An arbitrary λ0 does not guarantee any modular weight at all.
  - The FALSE verdict on the "unary weight 3/2" label stands either way.
