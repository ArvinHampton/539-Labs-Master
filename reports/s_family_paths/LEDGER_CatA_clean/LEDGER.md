# Category A ledger: s-family, dimensions, Bridge C, T3 arithmetic, H3 orbit map

**For:** Arvin Hampton · 2026-10-22

Path shorthand: `SF/` = `/workspace/quantum-comp/reports/s_family_paths/`.

## 0. Standing hypotheses

- **(TB)** The manuscript theta lift u has type ρ_s and eigenvalue λ = 1/4. The λ = 1/4 constant-term criterion holds. Arb/python-flint ball arithmetic is correct. The rounding analysis of `SF/A2/scripts/certify_hybrid.py` is correct.
- **(F1–F5)** These are standard facts about Weil representations of finite quadratic modules, including Scheithauer's upper-triangular formula (as listed in `SF/A12_H1H2_odd`).
- **(I1–I5)** These are the local imports listed in `SF/A15_ST_balance` §1. They consist of F1–F5 together with the local models of `SF/A11_induction`.
- **Computer certificates.** "Exact mod-p rank" means the following. The defining equations have coefficients in Z[ζ][1/N], and they are reduced at a prime above p. Under reduction the rank can only drop. So a computed mod-p dimension is an upper bound for the dimension over C. Likewise, an integer bounded by ℓ/2 in absolute value is determined by its residue mod ℓ.

Notation: ρ_s is the s-family Weil representation, W is its γ_s- and (−1)-invariant subspace, E = ρ-span(δ₀) ⊆ W, and C = W ⊖ E is the cusp part. S, T and Z = S² are the standard generators. e(x) = e^{2πix}.

---

## 1. s-family Weil representation ρ_s

1. **Theorem.** For every odd s ≥ 5, tr_C ρ(S) = tr_W ρ(S) = tr_E ρ(S) = 0. Hence dim C⁺ = dim C⁻ = d_cusp/2. Assume TB.
    *Proof.* The matrix entries of ρ(S) lie in Q(ζ_n)·n^{−1/2}. For odd s, a Galois automorphism σ with σ(√n) = −√n fixes the label structure (family_s label matrices) and maps each of the spaces W, E, C to itself. It sends tr ρ(S) to −tr ρ(S). Since S² = Z acts as 1 on W, tr S is an integer combination of ±1, hence rational, so it is fixed by σ. A rational number equal to its own negative is 0. (`SF/A6_certify/REPORT.md`, `SF/galois_review/REVIEW.md` G1.)
2. **Theorem.** The same conclusion holds for s ≡ 4, 6 mod 8.
    *Proof.* For these s, √n ∉ Q(ζ_{n/2}), so the automorphism σ of entry 1 still exists, and the argument applies verbatim. (`SF/galois_review` G1.)
3. **Theorem.** For every even s, tr_W S = 0.
    *Proof.* There is a monomial unitary K_y on W that anticommutes with S and commutes with γ_s and −1. Then tr_W S = tr_W(K_y S K_y^{−1}) = −tr_W S. (`SF/A8c_Spairing_even/REPORT.md`. An exact check for even s = 6..60 is in `pairing_on_W.py`.)
4. **Theorem.** Assume F1–F5. Let s ≡ 0, 2 mod 8 and E = ρ-span(δ₀). Then tr_E S = 0 and tr_C S = 0, so dim C⁺ = dim C⁻.
    *Proof.* By entry 8, tr_E S = ∏_p t_p, where t_p is the local trace on the local δ₀-span. Since s ≡ 0, 2 mod 8, m ≡ 0, 1 mod 4, so 4 | M, and the 2-adic exponent is a ≥ 2. There are two cases.
    - **a odd, or u ≡ 1 mod 4.** Then t₂ = 0. For a ≥ 3 this follows from entry 5 (P-stability) and entry 6 (H2), by the lift lemma of entry 8, down to the base classes. For a = 2 the base classes (2, 1/4) ⊕ (8, −u/16) have trace 0 exactly when u ≡ 1 mod 4 (certificate: `SF/A11_induction/exact_E0.py`, exact arithmetic). This case does not use H2.
    - **a even and u ≡ 3 mod 4.** The odd number u is a product of odd prime powers. Because u ≡ 3 mod 4, some p^e ∥ u satisfies p^e ≡ 3 mod 4. Then t_p = 0 by entry 7.

    So tr_E S = 0. Since E ⊆ W (γ_s commutes with ρ and fixes δ₀), tr_C S = tr_W S − tr_E S = 0 by entry 3. (`SF/A12_H1H2_odd`, `SF/A31_entry7_check/REFEREE.md` §5.)
    **Corollary.** Combining entries 1, 2 and 4: tr_C S = 0 for every s ≥ 5, with E = ρ-span(δ₀) when s ≡ 0, 2 mod 8.
5. **Theorem (P-stability).** Assume F1–F5. For every 2-adic exponent a ≥ 2, δ_h lies in the δ₀-span.
    *Proof.* δ_h is obtained from δ₀ by the explicit word S T^{2^a} S. This is evaluated with Scheithauer's formula (F1–F5). (`SF/A12`.) An exact mod-p check (p = 33556993) for a = 2..7 and all 24 classes u mod 8 is in `SF/A13_H1_check/verify_h1.py`.
6. **Theorem (H2).** Assume F1–F5 and a ≥ 3. Then tr S = 0 on (1 − P)E₀.
    *Proof.* The space X = (1 − P)E₀ has a basis indexed by P¹(Z/M). The level is lcm(4, M), which is where a ≥ 3 is needed. In this basis S acts monomially and without fixed points, so every diagonal entry of S vanishes. (`SF/A12`.)
7. **Theorem (odd-prime local factor).** Let p be an odd prime, e ≥ 0, c a unit mod p^e, D_p = (Z/p^e, q(x) = cx²/p^e), and ρ_p its Weil representation. Let E0_p be the SL₂(Z)-span of δ₀ in C[D_p]. Then:
    - (i) E0_p is the space of even functions on D_p, of dimension (p^e + 1)/2.
    - (ii) t_p := tr(S | E0_p) is equal to:
        - 1 if e is even;
        - (2/p) if e is odd and p ≡ 1 mod 4;
        - 0 if e is odd and p ≡ 3 mod 4.

        In particular t_p does not depend on c.
    - (iii) For the global form D = ⊕_p D_p, E0 = ⊗_p E0_p, and tr_E S = ∏_p t_p.

    *Proof.* Write γ(a) = Σ_{x mod p^e} e(ax²/p^e). Take S e_x = ε p^{−e/2} Σ_y e(−2cxy/p^e) e_y with ε = conj γ(c)/|γ(c)|. Then:
    - tr S = conj γ(c) γ(−2c)/p^e and tr SZ = conj γ(c) γ(2c)/p^e.
    - **e even:** γ(a) = p^{e/2} for every unit a, so tr S = tr SZ = 1.
    - **e odd:** γ(a) = p^{(e−1)/2} (a/p) ε_p √p, so tr S = (−2/p) and tr SZ = (2/p).

    By (i), the projection onto E0_p is ½(1 + Z), so t_p = ½(tr S + tr SZ) = (2/p)(1 + (−1/p))/2. This gives (ii). The opposite sign convention for T conjugates every quantity, and t_p is real, so it is unchanged. Part (i) is the odd case of H1/H2 (F1–F5). For (iii): δ₀ = ⊗ δ_{0,p}; SL₂(Z) → ∏_p SL₂(Z/p^{k_p}) is surjective; and ρ = ⊗ρ_p. Hence the span of the pure tensor δ₀ is the tensor product of the local spans. The phases are consistent because the total signature is 0 and every odd local part has even signature. (W and C are not tensor products, and the argument does not use such a decomposition.)
    *Certificate.* `SF/A31_entry7_check/local_odd.py` covers all 53 odd prime powers p^e ≤ 201, each with c a residue and with c a non-residue. It computes t_p exactly in Z[ζ_{p^e}] modulo Φ_{p^e}, and dim E0_p as a rank mod ℓ ≡ 1 mod p^e (lower bound = dim W⁺). It finds (i) and (ii) in all 106 cases.
8. **Theorem (factorisation and lift lemma).** Assume F1–F5. For even s, the original definitions of W, E and C reduce to C[D], with the complex-conjugate convention of `SF/A10`, so vanishing statements transfer between the two. Furthermore, tr_C S = −∏_p t_p, and tr_{P E0_a} S = t_{a−2} (2-adic lift lemma).
    *Proof.* `SF/A11_induction/REPORT.md`. The factorisation is entry 7(iii) combined with entry 3. The lift lemma follows by comparing P E0_a with E0_{a−2} through the isotropic quotient. *Certificate:* the base classes a = 2, 3, 4, including P-stability, are computed exactly in `SF/A11_induction/exact_E0.py`.
9. **Theorem.** On the full space C[D], tr S = tr SZ = 0. The Eisenstein trace factorises as a product of local factors, and the local factor vanishes for every odd p ≡ 3 mod 4 with exponent 1.
    *Proof.* tr S and tr SZ are normalised quadratic Gauss sums of the bilinear form, and they vanish by a one-line Gauss-sum evaluation. The factorisation follows from the tensor decomposition of entry 7(iii). The local vanishing is entry 7(ii) with e = 1. *Certificate:* 2-adic and odd local classes are checked exactly in `SF/A10_uniform_Spairing/exact_local.py`.
10. **Certificate.** Let s ≡ 0, 2 mod 8 with 8 ≤ s ≤ 74. Then tr_E S = 0, where E = ρ-span(δ₀).
    *Certificate:* `SF/A31_entry7_check/global_trE.py`. It works on the full D = A^{−1}Z²/Z². It computes the ⟨S, T⟩-span of δ₀ and tr_E S modulo two primes ℓ ≡ 1 mod 8M. On E, S² = 1, so tr_E S is an integer of absolute value at most dim E < ℓ/2, and its residue determines it. All 18 values of s give 0. For s = 8, 16, 18, 24, 26, 32, 40, 48, 50, 56 and 58, an independent certificate of tr_C S = tr_E S = 0 is given by the invertible operator Y = Z − SZS, which anticommutes with S (exact mod-p rank; `SF/A8_Spairing_even/modp_trace.py`). For s = 10, C = 0.
11. **Theorem (ST-balance, even s).** Assume I1–I5. Let R = ST, so R³ = I, and let ω = e^{2πi/3}. For every even s ≥ 6:
    - tr_W R = −ω if s ≡ 2 mod 3, and tr_W R = 0 otherwise.
    - tr_E R = −ω exactly when (Exc) holds, and tr_E R = 0 otherwise. Here (Exc) means: 3 | m − 1, a is even, u ≡ 1 mod 4, and v_p(M) is even for every prime p ≡ 2 mod 3.
    - Hence tr_C R ∈ {0, −ω}. The R-eigenvalue multiplicities on C are (k, k, k) or (k+1, k, k+1).
    - Moreover, 3 | d_cusp ⇔ tr_C R = 0 ⇔ (s ≢ 2 mod 3 or (Exc)).

    *Proof.* R splits into local factors because γ_s splits D (entry 13). The local traces r_p are computed in entry 13. The 2-adic base cases are certified exactly (`SF/A15_ST_balance/local_2adic_ab.py`). Since R³ = I, the multiplicities (n₁, n_ω, n_ω̄) satisfy n₁ + n_ω ω + n_ω̄ ω̄ = tr R with n₁ + n_ω + n_ω̄ = dim. Solving gives the stated patterns. (`SF/A15_ST_balance/REPORT.md`.)
12. **Certificate.** For every even s with 6 ≤ s ≤ 400 (198 values), tr_W R equals the Gauss-sum formula of entry 11. The method computes exact phase histograms, evaluates them at 40 digits, and rounds into the lattice Z[ω]. The lattice spacing is far above the error, so the rounding is exact. (`SF/A15_ST_balance/formula_even.py`, `gauss_even.py`.)
13. **Theorem (local formulas for tr_W R).** Assume I5.
    - γ_s splits D, since (1/(m−1))Z² ∩ (1/p^k)Z² = Z².
    - For odd p, r_p = ½ a_p(1 + κ_p). So r_p ≠ 0 iff χ₋₃(p^e) = 1, and r_3 ≠ 0 always.
    - The case analysis mod 3 (3 ∤ M; 3 | m; 3 | m − 1) is exhaustive.
    - Multiplicities of R computed mod p equal the true multiplicities for p ∤ 3, because R³ = I is diagonalisable mod p.

    *Proof.* `SF/A15_ST_balance/REPORT.md` §§2–4. The splitting is the stated lattice intersection. r_p is a local Gauss-sum evaluation. The last point holds because x³ − 1 is separable mod p.
14. **Theorem (closed forms for d_cusp).** Let G(m) denote the closed-form count of `SF/A`. Then:
    - For odd m, G(m) ≤ (m+1)/2, with equality iff m = 1 or m is a prime power.
    - For odd s ≥ 5, the closed form satisfies d_cusp ≥ (s−1)(s−3)/4 > 0.
    - d_cusp = 0 ⇔ s ∈ {6, 8, 10}.
    - d_cusp is even for every s ≥ 5.

    These statements concern the closed-form expressions. They equal the true d_cusp wherever the closed forms are proved, namely dim V = s(s−1) for odd s ≤ 51, and d₂(k, v) for k ≤ 6.
    *Proof.* G is multiplicative; a prime power p^e contributes exactly (p^e+1)/2, and for coprime factors the product of the local values is strictly below (m+1)/2. The remaining statements follow by substituting into the closed forms (full proofs in `SF/A/REPORT.md`.) For odd s, the parity also follows from entry 1.
15. **Theorem.** Assume Chen's theorem (1973). Let r = d_cusp/dim V for odd s (formula level).
    - Whether r is close to 1/4 depends only on the number k of prime-power factors of s(s−2). If every prime factor grows, then r → 1 − 3/2^k.
    - liminf r = 1/4 is equivalent to the existence of infinitely many pairs (s−2, s) of odd prime powers.
    - liminf r ≤ 5/8.

    *Proof.* The first two statements follow from the multiplicative closed form of r: each factor tends to its limit as the prime grows. The third follows by applying Chen's theorem (p + 2 = prime or a product of two primes) to get k ≤ 3 infinitely often. (`SF/A3_chen/REPORT.md`.)
16. **Theorem (isometry swap).** Let h ∈ SO(A)(Q) with h(S⁺) = S⁻ and Q∘h = Q. Then θ(R⁺) = θ(R⁻). At m = 7 (s = 98) such an h exists, so dim V(98) = 2406. Also, tr(g | Fix N) = 2m.
    *Proof.* h maps the representation-number sets bijectively while preserving Q, so the two theta series agree term by term. (`SF/galois_review/REVIEW.md` G11.)
17. **Theorem (Gauss-sum vanishing).** |G(h/m)| is given by the factorisation of quadratic Gauss sums, and G(h/m) = 0 iff 2 ‖ m or 5 | m.
    *Proof.* By the Chinese remainder theorem, G factors into local Gauss sums. Each local factor is evaluated in closed form; the factor at 2 vanishes exactly when 2 ‖ m, and the factor at 5 vanishes exactly when 5 | m (full computation in `SF/galois_review/REVIEW.md` G6.)

## 2. Dimensions of S(ρ_s)

Here S(ρ_s) denotes the space of Maass cusp forms of type ρ_s on W, of weight 0, with λ = 1/4. Every result in this section assumes TB. Upper bounds come from `SF/A2/scripts/certify_hybrid.py` (M = 6, Q = 40; Arb ball arithmetic). Lower bounds come from the sector lemma (entry 24) applied with d_cusp > 0, or from exact Hecke or T-row determinants.

18. **Certificate.** dim S(ρ_s) = 1 for s = 5, 7, 9, 12, 13, 14. (`SF/A/REPORT.md` §3, `SF/A2/REPORT.md`.)
19. **Certificate.** dim S(ρ_s) = 2 for s = 11 and s = 19. At s = 19 there is one form in each of two sectors. (`SF/A2`, `SF/A9_hecke_family/certify_hecke_s.py`.)
20. **Certificate.** Assume in addition Γ(1596)-invariance via Wohlfahrt. Then dim S(ρ_21) = 5. The lower bound comes from the Hecke images T′_p, p = 1597, certified in Arb at 256 bits from exact Fourier coefficients. (`SF/A7_s21/certify_hecke.py`.)
21. **Certificate.** dim S(ρ_23) = 3 (`SF/A6_certify`) and dim S(ρ_25) = 3 (`SF/A9`).
22. **Certificate.**
    - 3 ≤ dim S(ρ_15) ≤ 4.
    - 3 ≤ dim S(ρ_17) ≤ 4.
    - dim S(ρ_s) ≥ 3 for s = 27, 29, 31.

    (`SF/A9_hecke_family`.)
23. **Theorem (Hecke commutation).** If F is a cusp form of type ρ with eigenvalue λ, then T′_p F is again of type ρ with eigenvalue λ. T′_p commutes with the sector projectors, and its coefficients are given by the explicit formula of `SF/A7_s21`.
    *Proof.* T′_p is a sum over double-coset representatives, which commute with the Laplacian. The ρ-twist is compatible with the representatives because ρ factors through the level (TB). (`SF/A7_s21`.)
24. **Theorem (sector lemma).** Let σ be a P-even sector other than all-plus, with P_σW ≠ 0. Then P_σu is a non-zero cusp form of type ρ_s with λ = 1/4.
    *Proof.* P_σ commutes with ρ, so P_σu has type ρ_s and the same λ. Cuspidality and non-vanishing follow from the λ = 1/4 constant-term criterion (TB) applied in the sector σ; full proof in the source. (`SF/A6_certify`.)

## 3. Bridge C at s = 7

Here A_7 = [[2,7],[7,7]] and |D| = 35. ρ₃₅ is the Weil representation of the discriminant form D(A_7) (S e_μ = (i/√35) Σ_ν e(−b(μ,ν)) e_ν, T e_μ = e(q(μ)) e_μ). χ is the generator of Hom(SL₂(Z), C^×) ≅ Z/12, with χ(T) = e(1/12) and χ(S) = −i.

25. **Theorem.** At s = 7, ρ_7|W = E ⊕ C with dim E = 36 and dim C = 6. Both E and C are irreducible, and dim C⁺ = dim C⁻ = 3. Hence C has no 1-dimensional ρ-invariant subspace, and any S-eigenvector in C generates all of C as a ρ-module.
    *Proof.* dim End(ρ_7|W) = 2 (exact mod-p upper bound; `SF/A32_35_to_rho7/exact_hom.py`), and E, C ≠ 0 are subrepresentations. So both summands are irreducible and non-isomorphic. The equality of C⁺ and C⁻ is entry 1. (`SF/RTA_implications/REPORT.md`.)
26. **Certificate.** Assume TB. Then dim S(ρ_7) = 1. (`SF/A/scripts/certify_s.py`, `SF/A/REPORT.md` §3.)
27. **Theorem.**
    - Q(√35) has class number 2, and 6 + √35 is a unit of norm +1.
    - [[2,1],[1,−17]] is an odd lattice.
    - There is no even binary lattice of determinant −35.

    *Proof.* 6² − 35 = 1, and the class number is standard. For an even binary form, the discriminant b² − 4ac would equal 35, but 35 ≡ 3 mod 4 is not a square mod 4. (`SF/RTA_prereg/REPORT.md`.)
28. **Theorem.** Let C be any irreducible unitary representation.
    - Every Γ-equivariant map C^{⊗a} ⊗ C̄^{⊗b} → C is Z/3-graded by R-degree.
    - If no T-exponents satisfy a + b + c − d ≡ 0 mod 1, then Hom_Γ(C⊗C⊗C, C) = 0.
    - The products x⟨z, y⟩ and z⟨x, y⟩ are equivariant.

    *Proof.* R³ = I acts on the tensor product, and an intertwiner commutes with R. An intertwiner also commutes with T, so it can only connect T-eigenvectors whose exponents match. ⟨·,·⟩ is Γ-invariant. (`SF/A18_RTA_foundation/REPORT.md`.)
29. **Theorem.** dim Hom_{SL₂(Z)}(ρ₃₅ ⊗ χ³, ρ_7|W) = 1. A generator Φ is monomial: after rescaling, its non-zero entries lie in {±1, ±e(1/5)}. Its image is exactly C, and its kernel has dimension 29. Consequently C ≅ ρ₅⁻ ⊗ ρ₇⁻ ⊗ χ³, where ρ₅⁻ ⊗ ρ₇⁻ is the 6-dimensional subspace of ρ₃₅ that is odd under both local reflections Z₅ and Z₇.
    *Proof and certificate.*
    - **Upper bound.** dim ≤ 1 from an exact mod-p rank computation at p = 29 401 and p = 14 729 401 (p ≡ 1 mod 29 400; `SF/A32_35_to_rho7/exact_hom.py`).
    - **Lower bound.** The explicit 35 × 42 matrix Y with unit entries (`SF/A32_35_to_rho7/X_chi3.npy`) satisfies Y·S₃₅′ = S_7·Y (210 of 210 entries) and Y·T₃₅′ = T_7·Y (24 of 24 entries), exactly in Z[Z/29400] modulo Φ₂₉₄₀₀ (`SF/A32_35_to_rho7/exact_verify.py`). Generators suffice.
    - **Rank and image.** The six image rows have disjoint column supports, so the rank is 6. The image is a 6-dimensional subrepresentation of W = E ⊕ C. By entry 25 it must be C.
    - **Kernel and isomorphism.** The kernel contains the 11 labels with a zero local component and the 18-dimensional complement of the (−,−) sector on the 24 primitive labels, so Φ restricted to ρ₅⁻ ⊗ ρ₇⁻ ⊗ χ³ is an isomorphism onto C.

## 4. T3 and budget arithmetic

T3(n) is defined by:
- T3(n) = n/3 for n ≡ 0 mod 3;
- T3(n) = (4n + 2)/3 for n ≡ 1 mod 3;
- T3(n) = (2n + 1)/3 for n ≡ 2 mod 3 (in the integer form of `SF/A20`).

σ(n) is the number of steps needed to reach 1.

30. **Theorem.** With the integer form, T3 maps positive integers to positive integers. The expression (2n + 1)/3 is not an integer for n ≡ 2 mod 3; for example, (2·2 + 1)/3 = 5/3.
    *Proof.* Check each residue class mod 3. (`SF/A20`, `SF/A25`.)
31. **Theorem.** σ(3ᵏm) = k + σ(m), and σ(3ᵏ) = k.
    *Proof.* T3(3n) = n. Use induction on k. (`SF/A23`, `SF/A24`.)
32. **Theorem.** If σ(n) ≤ 539, then T3^{539}(n) = 1 when σ(n) is odd, and T3^{539}(n) = 2 when σ(n) is even.
    *Proof.* T3 alternates 1 ↦ 2 ↦ 1. After reaching 1 at step σ(n), the remaining 539 − σ(n) steps alternate. (`SF/A23_axiom01_revised/REPORT.md`.)
33. **Theorem.** If σ(n) ≤ 540, then T3^{540}(n) = 1 iff σ(n) is even. In particular T3^{540}(4880) = 1, and among n ≤ 10⁶, exactly 504 899 end at 1 and 495 101 end at 2.
    *Proof.* As in entry 32. The counts are an exact enumeration (`SF/A30_540_thermo/tests540.py`).
34. **Theorem.** For every j ≥ 1, the map n mod 3ʲ ↦ (T3ˢ(n) mod 3)_{0≤s<j} is a bijection from Z/3ʲ onto the words of length j over {0, 1, 2}.
    *Proof.* Induction on j. On each residue class mod 3, T3 is affine with leading coefficient 1/3 or 4/3 or 2/3. So T3(n) mod 3^{j−1} is determined by n mod 3ʲ, and it runs over all classes mod 3^{j−1} as n runs over a fixed class mod 3. Exhaustive check for j ≤ 8: `SF/A29_patterns_all/run_core.py`.
35. **Theorem.** T3 does not induce a map on Z/9 (and more generally on Z/3ʲ).
    *Proof.* By entry 34, T3(n) mod 3ʲ depends on n mod 3^{j+1} and not on n mod 3ʲ.
36. **Theorem.** Each m has an explicit list of T3-preimages. Moreover, T3(n) + 2 ≤ (4/3)(n + 2), with equality iff n ≡ 1 mod 3.
    *Proof.* The preimages are found by inverting each branch. For the inequality: n ≡ 1 gives equality, and the other branches give strictly less. (`SF/A24_threshold_1e18`.)
37. **Theorem.** ⌊(4880 − 21)/9⌋ = 539.
    *Proof.* 4859/9 = 539.89. (`SF/A20`, `SF/A23`.)
38. **Theorem.** ⌊3⁵e³⌋ = 4880 and ⌊35e³⌋ = 702.
    *Proof.* 3⁵e³ = 4880.84 and 35e³ = 702.99, both evaluated with rigorous error bounds. (`SF/A19`, `SF/A25`.)
39. **Theorem.**
    - 540 = 2²·3³·5 = 4860/9.
    - ⌊(4880 − f)/9⌋ = 540 exactly for f = 12, …, 20.
    - 539.9 = 540(1 − 1/5400).
    - 5399 is prime. Hence e^{2πi/539.9} = e^{2πi·10/5399} is a primitive 5399th root of unity, and its 539th power is not 1. Moreover, 539 steps of the phase e^{2πi/539.9} give 5390/5399 of a full turn.
    - The beat period of 540 against 539.9 is 2 915 460.

    *Proof.* Direct computation. Primality of 5399 is checked by trial division up to 73. (`SF/A25`, `SF/A30`.)
40. **Certificate.** Let m₅₃₉ be the smallest n with σ(n) = 539. Then:
    - 10⁷ < m₅₃₉ ≤ 788 638 819 521 764 360 564 859 602 047 870.
    - For every d ≤ 291 there is a seed below 10¹⁸ with σ = d.
    - σ(666 954 248 808 172 552) = 291.

    The method is exact integer iteration (`SF/A24_threshold_1e18/exact_min.py`, `beam.py`).
41. **Certificate (exact counts).**
    - max_{n ≤ 20 000} σ(n) = 53, attained at n = 16261.
    - max_{n ≤ 50 000} σ(n) = 55, attained at n = 36043 and 36592.
    - σ(4880) = 14 and σ(10¹⁸) = σ(10¹⁸ + 1) = 92.
    - σ(3^{539}) = 539.
    - Every n ≤ 10⁷ satisfies σ(n) ≤ 539.
    - σ(3^{540}) = 540, and T3^{539}(3^{540}) = 3.

    The method is exact integer iteration (`SF/A19_9maths_axioms/checks.py`, `SF/A23_axiom01_revised/budget.py`, `SF/A28`).
42. **Theorem.**
    - φ⁷ = (29 + 13√5)/2.
    - 1001 = 7·11·13.
    - 18 + 1 + 520 = 539.
    - 243 − 244 + 55 = 54.
    - 4·8 + 5·12 = 92.
    - 4·122 = 488.

    *Proof.* Direct computation. For φ⁷, use φⁿ = (Lₙ + Fₙ√5)/2 with L₇ = 29 and F₇ = 13.
43. **Theorem.** Consider any lift of T3 in which the integer coordinate evolves by T3 and steps are counted one-to-one. In any such lift, the number of steps to reach 1 is exactly σ(n).
    *Proof.* The projection to the integer coordinate is a step-preserving semiconjugacy. (`SF/A20_T3_bulk_vs_shadow`.)

## 5. The H3 orbit map

Φ(n) = Σ_{s<539} w(r_s(n)) ∈ ⟨c⟩ ≅ Z/N, where r_s(n) = T3ˢ(n) mod 3, and w: {0, 1, 2} → Z/N.

44. **Theorem.** Φ is well defined for every n ≥ 1.
    *Proof.* The sum is finite (539 terms) and every T3ˢ(n) is defined. (`SF/A28_H3_map_construction/REPORT.md`.)
45. **Theorem (cocycle law).** Let S_k(n) = Σ_{s<k} w(r_s(n)). Then S_{k+l}(n) = S_k(n) + S_l(T3ᵏn). Hence w induces a monoid homomorphism {0, 1, 2}* → Z/N.
    *Proof.* Split the sum at s = k.
46. **Theorem (tail formula).** If σ(n) ≤ 539 and L = 539 − σ(n), then Φ(n) = S_σ(n) + ⌈L/2⌉w(1) + ⌊L/2⌋w(2).
    *Proof.* Apply entry 45 at k = σ(n). The tail orbit is 1, 2, 1, 2, …, with residues 1, 2, 1, 2, …. An exact check on 301 seeds × 9 weight choices is in `SF/A28_H3_map_construction/h3map.py`.
47. **Theorem.** Replacing the generator c by another generator multiplies Φ by a unit of Z/N. This preserves the zero set of Φ, its additive order, and τ. The manifolds M_A and M_B, with Z/N coefficients, give identical values.
    *Proof.* Φ depends only on the cyclic group ⟨c⟩ ≅ Z/N.
48. **Theorem.**
    - Tors H³(M_A; Z) = Z/N, and there is no self-linking form on H³ in dimension 7.
    - For M_B = L⁷(N), H³(M_B; Z) = 0 and H³(M_B; Z/N) = Z/N.

    *Proof.* Standard: universal coefficients, and the cellular chain complex of a lens space. A linking form in dimension 7 pairs H³ with H⁴, not H³ with itself. (`SF/A28`.)
49. **Theorem.** Let T = d + (ζ(t) − 1)H₃∧. Then T² = 0 iff dt ∧ H₃ = 0 and dH₃ = 0. A torsion class has no non-zero de Rham representative. On M_A, H₃ is exact, and T = e^{−fB} ∘ d ∘ e^{fB}; hence the T-cohomology is isomorphic to de Rham cohomology.
    *Proof.* Expand T². de Rham cohomology is a real vector space, so torsion maps to 0. If H₃ = dB, conjugate d by the exponential. (`SF/A25`, `SF/A28`.)

## 6. Non-existence and vanishing results

50. **Theorem.** There exist positive integers n with σ(n) > 539. Specifically, σ(3^{540}) = 540.
    *Proof.* Entry 31.
51. **Theorem.** For every k ≥ 38 with k ≠ 539, σ(3ᵏ) = k ≠ 539, and 3ᵏ > 10¹⁸. Hence σ is not constantly equal to 539 on n ≥ 10¹⁸.
    *Proof.* Entry 31, together with 3^{38} > 10¹⁸.
52. **Theorem.**
    - 3·61 + 162 + 223 = 568.
    - 244 − 18 − 1 = 225.
    - The alternating sum of the sequence of Betti numbers recorded in `SF/A25` is −162.
    - A closed oriented 7-manifold has b₃ = b₄. Hence no closed oriented 7-manifold has b₃ = 223 and b₄ = 61.
    - With χ = 0 and rk = 3, χ/2 + rk = 3.
    - 3¹⁸ < 10⁹.

    *Proof.* Direct computation. b₃ = b₄ follows from Poincaré duality. (`SF/A25`.)
53. **Theorem.** 540·{2, 3, 4, 5, 10} = {1080, 1620, 2160, 2700, 5400}. None of these is an integer multiple of 539.9.
    *Proof.* k·540/539.9 = 5400k/5399. Since 5399 is prime and does not divide 5400k for these k, the quotient is not an integer. (`SF/A19`, `SF/A23`.)
54. **Theorem.**
    - 540/(1 + 1/540) = 291600/541 ≈ 539.0018.
    - 540/(1 + 0.01·0.185) ≈ 539.0028.
    - 540(1 − 0.0001) = 539.946.
    - 540/(1 + δ) = 539.9 iff δ = 1/5399.

    *Proof.* Direct computation. (`SF/A30`.)
55. **Theorem.** Let V ∈ {ρ₃₅, ρ₃₅*}, U ∈ {ρ_7|W, ρ_7|W*} and k ∈ Z/12. Then Hom_{SL₂(Z)}(V ⊗ χᵏ, U) = 0 and Hom_{SL₂(Z)}(U, V ⊗ χᵏ) = 0, except in the two cases (V, k, U) = (ρ₃₅, 3, ρ_7|W) and (ρ₃₅*, 9, ρ_7|W*), where the dimension is 1 (entry 29 and its complex conjugate). In particular there is no non-zero intertwiner ρ₃₅ → ρ_7|W. All 12 T-eigenvalues of ρ₃₅ occur in ρ_7|W, so the vanishing is forced by S, not by the T-spectra.
    *Certificate.* The equations XS₁ = S₂X and XT₁ = T₂X are solved over F_p with ζ ↦ a primitive 29 400th root of unity. This was done at p = 29 401 and p = 14 729 401, with identical results. 96 Hom spaces were computed, and the mod-p nullity is 0 in each case listed. (`SF/A32_35_to_rho7/exact_hom.py`, `run.py`, `results.json`.)
56. **Theorem.** For s = 8, 10, 16 and 18, no label-dilation Galois automorphism acts on ρ_s(S) with sign −1.
    *Certificate.* Exact enumeration of dilations (`SF/A8c_Spairing_even/galois_dilation_fast.py`).
57. **Theorem.** The class-number predictor Cl(K_s) of `SF/A5_classgroup` differs from dim S(ρ_s) at s = 9 and s = 11. The predictor Cl(4n_s) differs from it at s = 23 and 25.
    *Proof.* The class numbers are exact (`SF/A5_classgroup/classgroups_A5.py`), and they are compared with the certified values of entries 18–22.
58. **Theorem.** At s = 56, the multiplicities of R = ST on E are (187, 186, 187), so E is not R-balanced. On C they are (84, 84, 84).
    *Proof.* Entry 11: at s = 56, (Exc) holds and s ≡ 2 mod 3. The dimensions are dim E = 560 and d_cusp = 252, computed exactly (`SF/A15_ST_balance/exact_E0_R.py`).
