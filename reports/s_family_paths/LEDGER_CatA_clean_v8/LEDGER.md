# Category A ledger v8: s-family, dimensions, Bridge C, T3 arithmetic, H3 orbit map, the g_k family, RTA's Bridge Series C

**For:** Arvin Hampton · 2026-10-24

Path shorthand: `SF/` = `/workspace/quantum-comp/reports/s_family_paths/`; paths beginning `reports/` are relative to `/workspace/quantum-comp/`. This ledger contains Category A statements only (proofs, and computer certificates in exact or ball arithmetic). It has 109 numbered entries. Sources of every entry are listed in `INDEX.md`.

## 0. Standing hypotheses

- **(TB3)** S² = P on the label space, i.e. ρ(−I) = P.
- **(TB4)** The components of the theta lift u are invariant under the principal congruence subgroup Γ(N), where N = ord ρ(T).
- **(TB)** The manuscript theta lift u has type ρ_s and eigenvalue λ = 1/4. The λ = 1/4 constant-term criterion holds. Arb/python-flint ball arithmetic is correct. The rounding analysis of `SF/A2/scripts/certify_hybrid.py` is correct.
- **(F1–F5)** These are standard facts about Weil representations of finite quadratic modules, including Scheithauer's upper-triangular formula (as listed in `SF/A12_H1H2_odd`).
- **(TB5)** The theta-lift theorem of TB2 holds for every lattice (Λ_𝔭, Q/p) in the genus of A_s (`SF/A37_dihedral_count/prereg.md`). Used only in entry 103.
- **(I1–I5)** These are the local imports listed in `SF/A15_ST_balance` §1. They consist of F1–F5 together with the local models of `SF/A11_induction`.
- **Computer certificates.** "Exact mod-p rank" means the following. The defining equations have coefficients in Z[ζ][1/N], and they are reduced at a prime above p. Under reduction the rank can only drop. So a computed mod-p dimension is an upper bound for the dimension over C. Likewise, an integer bounded by ℓ/2 in absolute value is determined by its residue mod ℓ.

Writing TB2 for the part of TB concerning the theta lift: u has type ρ_s, eigenvalue λ = 1/4, its constant term is a multiple of c₀ = Π_Wδ₀, and the λ = 1/4 constant-term criterion holds.

Notation: ρ_s is the s-family Weil representation, W is its γ_s- and (−1)-invariant subspace, E = ρ-span(δ₀) ⊆ W, and C = W ⊖ E is the cusp part. S, T and Z = S² are the standard generators. e(x) = e^{2πix}.

---

## 1. s-family Weil representation ρ_s

1. **Theorem.** Assume TB3. For every odd s ≥ 5, tr_C ρ(S) = tr_W ρ(S) = tr_E ρ(S) = 0, hence dim C⁺ = dim C⁻ = d_cusp/2.
    *Proof.* Let n = s(s−2) ≡ 3 mod 4 and Ŝ = √n·S on the label space.
    - **Fields.** For the labels, B(α,β) ∈ (1/2n)Z and Q(α) ∈ (1/4n)Z. So Ŝ has entries in Q(ζ_{2n}), T is monomial with phases in Q(ζ_{4n}), the monomials γ_s and N that cut out W have phases in Q(ζ_{2n}), and c₀ is rational.
    - **T^{2n} is diagonal.** Summing the T-phases over 2n steps gives T^{2n} = D := diag(e(−2nQ(α))), a sign matrix.
    - **The Galois element.** Let σ ∈ Gal(Q(ζ_{4n})/Q) send ζ_{4n} ↦ ζ_{4n}^{2n+1}. Since 2n+1 ≡ 1 mod 2n, σ fixes Ŝ, the W-phases and c₀, and σ(T) = TD = T^{2n+1}. Write √n = k√d with d ≡ 3 mod 4. Since 2n+1 ≡ 1 mod d and ≡ 3 mod 4, quadratic reciprocity gives (d/(2n+1)) = −1, so σ(√n) = −√n and σ(S) = −S.
    - **Invariance.** σ(W) = W. σ(E) is the smallest subspace containing Π_W c₀ that is stable under −S and T^{2n+1}, and T^{2n+1} generates the same group as T, so σ(E) = E. σ commutes with complex conjugation, so σ(C) = C and σ fixes the orthogonal projector P_C.
    - **Conclusion.** t = tr(P_C S) satisfies σ(t) = −t. By TB3, S² = 1 on W, so t is a rational integer, and therefore t = 0. The same argument applies to W and E.
    (`SF/A6_certify/REPORT.md` A4; exact hypothesis checks for s = 5..40 in `SF/A6_certify/scripts/galois_sign.py`.)

2. **Certificate.** Let s ≡ 4, 6 mod 8 with 12 ≤ s ≤ 46, and let E = ρ-span(δ₀) in C[D]. Then tr_E S = 0. Combined with entry 3, tr_C S = 0, so dim C⁺ = dim C⁻.
    *Certificate.* `SF/A31_entry7_check/global_trE.py`, run for s = 12, 14, 20, 22, 28, 30, 36, 38, 44, 46 (log: `SF/A34_ledger_checks/logs/global_trE_rerun_and_4_6mod8.txt`). The script computes the ⟨S,T⟩-span of δ₀ and tr_E S modulo two primes ℓ ≡ 1 mod 8M. On E, S² = 1, so tr_E S is an integer with |tr| ≤ dim E < ℓ/2, and its residue determines it. All ten values are 0.

3. **Theorem.** For every even s, tr_W S = 0.
    *Proof.* There is a monomial unitary K_y on W that anticommutes with S and commutes with γ_s and −1. Then tr_W S = tr_W(K_y S K_y^{−1}) = −tr_W S. (`SF/A8c_Spairing_even/REPORT.md`. An exact check for even s = 6..60 is in `pairing_on_W.py`.)
4. **Theorem.** Assume F1–F5. Let s ≡ 0, 2 mod 8 and E = ρ-span(δ₀). Then tr_E S = 0 and tr_C S = 0, so dim C⁺ = dim C⁻.
    *Proof.* By entry 8, tr_E S = ∏_p t_p, where t_p is the local trace on the local δ₀-span. Since s ≡ 0, 2 mod 8, m ≡ 0, 1 mod 4, so 4 | M, and the 2-adic exponent is a ≥ 2. There are two cases.
    - **a odd, or u ≡ 1 mod 4.** Then t₂ = 0. For a ≥ 3 this follows from entry 5 (P-stability) and entry 6, by the lift lemma of entry 8, down to the base classes. For a = 2 the base classes (2, 1/4) ⊕ (8, −u/16) have trace 0 exactly when u ≡ 1 mod 4 (certificate: `SF/A11_induction/exact_E0.py`, exact arithmetic). This case does not use entry 6.
    - **a even and u ≡ 3 mod 4.** The odd number u is a product of odd prime powers. Because u ≡ 3 mod 4, some p^e ∥ u satisfies p^e ≡ 3 mod 4. Then t_p = 0 by entry 7.

    So tr_E S = 0. Since E ⊆ W (γ_s commutes with ρ and fixes δ₀), tr_C S = tr_W S − tr_E S = 0 by entry 3. (`SF/A12_H1H2_odd`, `SF/A31_entry7_check/REFEREE.md` §5.)
    **Corollary.** tr_C S = 0 for every odd s ≥ 5, for every s ≡ 0, 2 mod 8 (with E = ρ-span(δ₀)), and for every s ≡ 4, 6 mod 8 with 12 ≤ s ≤ 46 (entries 1, 2 and 4).
5. **Theorem (P-stability).** Assume F1–F5. For every 2-adic exponent a ≥ 2, δ_h lies in the δ₀-span.
    *Proof.* δ_h is obtained from δ₀ by the explicit word S T^{2^a} S. This is evaluated with Scheithauer's formula (F1–F5). (`SF/A12`.) An exact mod-p check (p = 33556993) for a = 2..7 and all 24 classes u mod 8 is in `SF/A13_H1_check/verify_h1.py`.
6. **Theorem (trace vanishing off the P-fixed part).** Assume F1–F5 and a ≥ 3. Then tr S = 0 on (1 − P)E₀.
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

    By (i), the projection onto E0_p is ½(1 + Z), so t_p = ½(tr S + tr SZ) = (2/p)(1 + (−1/p))/2. This gives (ii). The opposite sign convention for T conjugates every quantity, and t_p is real, so it is unchanged. Part (i) is the odd-prime case of the span computation of `SF/A12_H1H2_odd` (F1–F5). For (iii): δ₀ = ⊗ δ_{0,p}; SL₂(Z) → ∏_p SL₂(Z/p^{k_p}) is surjective; and ρ = ⊗ρ_p. Hence the span of the pure tensor δ₀ is the tensor product of the local spans. The phases are consistent because the total signature is 0 and every odd local part has even signature. (W and C are not tensor products, and the argument does not use such a decomposition.)
    *Certificate.* `SF/A31_entry7_check/local_odd.py` covers all 53 odd prime powers p^e ≤ 201, each with c a residue and with c a non-residue. It computes t_p exactly in Z[ζ_{p^e}] modulo Φ_{p^e}, and dim E0_p as a rank mod ℓ ≡ 1 mod p^e (lower bound = dim W⁺). It finds (i) and (ii) in all 106 cases.
8. **Theorem (factorisation and lift lemma).** Assume F1–F5. Let s be even, work on C[D] with the complex-conjugate convention of `SF/A10`, and take E := ρ-span(δ₀) ⊆ W and C := W ⊖ E. Then tr_E S = ∏_p t_p, tr_C S = −∏_p t_p, and tr_{P E0_a} S = t_{a−2} (2-adic lift lemma). Every statement in this ledger about E and C for even s refers to this E = ρ-span(δ₀).
    *Proof.* `SF/A11_induction/REPORT.md`. The factorisation is entry 7(iii) combined with entry 3. The lift lemma follows by comparing P E0_a with E0_{a−2} through the isotropic quotient. *Certificate:* the base classes a = 2, 3, 4, including P-stability, are computed exactly in `SF/A11_induction/exact_E0.py`.
9. **Theorem.** On the full space C[D], tr S = tr SZ = 0. The Eisenstein trace factorises as a product of local factors, and the local factor vanishes for every odd p ≡ 3 mod 4 with exponent 1.
    *Proof.* tr S and tr SZ are normalised quadratic Gauss sums of the bilinear form, and they vanish by a one-line Gauss-sum evaluation. The factorisation follows from the tensor decomposition of entry 7(iii). The local vanishing is entry 7(ii) with e = 1. *Certificate:* 2-adic and odd local classes are checked exactly in `SF/A10_uniform_Spairing/exact_local.py`.
10. **Certificate.** Let s ≡ 0, 2 mod 8 with 8 ≤ s ≤ 74. Then tr_E S = 0, where E = ρ-span(δ₀).
    *Certificate:* `SF/A31_entry7_check/global_trE.py`. It works on the full D = A^{−1}Z²/Z². It computes the ⟨S, T⟩-span of δ₀ and tr_E S modulo two primes ℓ ≡ 1 mod 8M. On E, S² = 1, so tr_E S is an integer of absolute value at most dim E < ℓ/2, and its residue determines it. All 18 values of s give 0. For s = 8, 16, 18, 24, 26, 32, 40, 48, 50, 56 and 58, an independent certificate of tr_C S = tr_E S = 0 is given by the invertible operator Y = Z − SZS, which anticommutes with S (exact mod-𝔭 rank of Y|_W on the orbit basis of W; `SF/A8c_Spairing_even/scripts/pairing_on_W.py`). Since Y lies in the image of the group algebra and anticommutes with S on W, invertibility of Y|_W makes Y|_C an isomorphism C⁺ → C⁻. For s = 10, C = 0.
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
14. **Theorem (closed forms for d_cusp, odd s).** For odd m let G(m) = ∏_{q‖m} (q+1)/2, where q runs over the exact prime-power divisors of m. For odd s ≥ 5 let n = s(s−2), dim V = s(s−1), d_Eis = 3G(n) and d_cusp = dim V − d_Eis. Then:
    - (i) G(m) ≤ (m+1)/2 for odd m, with equality iff m = 1 or m is a prime power;
    - (ii) d_cusp ≥ (s−1)(s−3)/4 > 0, with equality iff s and s−2 are both prime powers;
    - (iii) d_cusp is even.

    These are statements about the closed forms. They describe the true d_cusp for odd s ≤ 51, where dim V = s(s−1) and d_Eis = 3G(n) are proved.
    *Proof.* (i) If m = q is a prime power, then G(m) = (q+1)/2. For coprime odd a, b ≥ 3, (a+1)(b+1)/4 < (ab+1)/2 is equivalent to (a−1)(b−1) > 0. By multiplicativity and induction on the number of prime-power factors, G(m) < (m+1)/2 whenever m has at least two of them. (ii) gcd(s, s−2) = 1, so G(n) = G(s)G(s−2) ≤ (s+1)(s−1)/4 by (i). Hence d_cusp ≥ s(s−1) − 3(s²−1)/4 = (s−1)(s−3)/4, with equality iff equality holds in (i) for both s and s−2. (iii) s(s−1) is even. One of s, s−2 is ≡ 3 mod 4, and an integer ≡ 3 mod 4 has an exact prime-power divisor q ≡ 3 mod 4, since a product of factors ≡ 1 mod 4 is ≡ 1 mod 4. Then (q+1)/2 is even, so G(n) and d_Eis are even. (Parity for odd s also follows from entry 1.)

15. **Theorem (distribution of r, odd s, formula level).** Let r = d_cusp/dim V with the closed forms of entry 14. Write k = ω(s) + ω(s−2) and g(m) = ∏_{q‖m}(1+1/q)/2, so that 1 − r = 3·(s−2)/(s−1)·g(s)g(s−2). All averages below are over odd s ≤ X.
    - (i) mean k = 2 log log X + O(1), and Var k ≪ log log X.
    - (ii) The empirical law of r tends to the point mass at 1. In particular mean r → 1.
    - (iii) For almost all odd s, 1 − r = (log s)^{−2 log 2 + o(1)}.
    - (iv) (log X)^{−2 log 2} ≪ mean g(s)g(s−2) ≪ 1/log X. Consequently the density of {s : r < 1 − ε} is ≪ 1/(ε log X).
    - (v) Y = Σ_{q‖s(s−2)} log(1 + 1/q) has a limit law, and that law is continuous.
    - (vi) The set L of limit points of r satisfies L ⊆ {1} ∪ {1 − 3w : w ∈ W}, where W = {2^{−2−j}∏_{q∈S}(1+1/q)/2 : j ≥ 0, S a finite set of pairwise coprime odd prime powers}. Hence L is countable and closed, and L ⊆ {1/4} ∪ [1/2, 1].

    *Proof.* (i) For an odd prime p ≤ X, the number of odd s ≤ X with p | s(s−2) is X/p + O(1). Mertens' theorem gives mean k = Σ_{3≤p≤X} 2/p + O(1) = 2 log log X + O(1). For p ≠ q both ≤ X^{1/4}, the density of {pq | s(s−2)-type events} is 4/(pq) + O(X^{−1/2}). The primes above X^{1/4} contribute O(1) to k, so the second moment is (mean k)² + O(log log X).
    (ii) By (i) and Chebyshev, k ≥ log log X except on a set of density O(1/log log X). Off that set, 1 − r ≤ 3(2/3)^k → 0.
    (iii) log(1 − r) = −k log 2 + Y + O(1), with 0 ≤ Y ≤ Σ_{p|n} 1/p ≪ log log log s. By (i), k = 2 log log s + O(ψ(s)√(log log s)) for almost all s, for any ψ → ∞.
    (iv) *Lower bound:* g(s)g(s−2) ≥ 2^{−k}, and x ↦ 2^{−x} is convex, so by Jensen the mean is ≥ 2^{−mean k}, and (i) gives ≫ (log X)^{−2 log 2}. *Upper bound:* apply Nair–Tenenbaum (Acta Math. 180 (1998), Theorem 1) with two variables, Q₁(n) = n, Q₂(n) = n − 2 and y = x. Q₁Q₂ has no fixed prime divisor, because Q₁Q₂(1) = −1. F(n₁,n₂) = g(n₁)g(n₂), with g(2^e) := 1, satisfies F(m₁n₁, m₂n₂) ≤ F(n₁,n₂) for coprime pairs, so F ∈ M₂(1,1,ε). The theorem gives Σ_{n≤X} F(n, n−2) ≪ X ∏_{p≤X}(1 − 2/p)·(Σ_{n≤X} g(n)/n)². Since Σ_{n≤X} g(n)/n ≤ ∏_{p≤X}(1 + 1/(2p) + O(p^{−2})) ≪ (log X)^{1/2}, the sum is ≪ X/log X. Restricting to odd n only decreases it, since F ≥ 0. The density statement follows by Markov's inequality.
    (v) *Existence:* truncate Y at primes p ≤ y. By CRT, the truncated variable has the law of Σ_{p≤y} X_p with independent X_p, and E|Y − Y_y| ≤ Σ_{p>y} 2/p² → 0. *Continuity:* each X_p is discrete with largest atom P(X_p = 0) = 1 − 2/p for p ≥ 5, and ∏_p(1 − 2/p) = 0. By Lévy's theorem (Studia Math. 3 (1931)), a convergent series of independent discrete random variables has a continuous law iff the product of the largest atoms is 0.
    (vi) Along a subsequence on which r tends to a limit below 1, k is bounded, since otherwise g → 0. Pass to further subsequences on which k is constant and each prime-power factor is either constant or tends to ∞. A factor tending to ∞ contributes the factor 1/2 in the limit, and since s → ∞, at least one factor of s and one factor of s−2 tend to ∞. This gives the form 1 − 3w. W is countable, and its only accumulation points are again of the same form, which gives the stated inclusions.

16. **Theorem.** Assume Chen's theorem (1973). Let r = d_cusp/dim V for odd s (formula level).
    - Whether r is close to 1/4 depends only on the number k of prime-power factors of s(s−2). If every prime factor grows, then r → 1 − 3/2^k.
    - liminf r = 1/4 is equivalent to the existence of infinitely many pairs (s−2, s) of odd prime powers.
    - liminf r ≤ 5/8.

    *Proof.* The first two statements follow from the multiplicative closed form of r: each factor tends to its limit as the prime grows. The third follows by applying Chen's theorem (p + 2 = prime or a product of two primes) to get k ≤ 3 infinitely often. (`SF/A3_chen/REPORT.md`.)
17. **Theorem (isometry swap).** Let h ∈ SO(A)(Q) with h(S⁺) = S⁻ and Q∘h = Q. Then θ(R⁺) = θ(R⁻). At m = 7 (s = 98) such an h exists, so dim V(98) = 2406. Also, tr(g | Fix N) = 2m.
    *Proof.* h maps the representation-number sets bijectively while preserving Q, so the two theta series agree term by term. (`SF/galois_review/REVIEW.md` G11.)
18. **Theorem (Gauss-sum vanishing).** Let Q(n,k) = n² + 7nk + 7k(k+1)/2 and, for gcd(h,m) = 1, G(h/m) = (2m)^{−2} Σ_{n,k mod 2m} e(hQ(n,k)/m). Then G(h/m) = 0 iff 2 | m or 5 | m. Otherwise |G(h/m)| = 1/m if 7 ∤ m, and |G(h/m)| = √7/m if 7 | m.
    *Proof.* Q is integer-valued. Q(n+2m,k) − Q(n,k) and Q(n,k+2m) − Q(n,k) are divisible by m, so the summand is 2m-periodic and shifts permute the terms.
    - **2 | m.** Q(n,k+m) − Q(n,k) = m(7n + 7k + 7(m+1)/2). The shift k ↦ k+m multiplies every term by e(7h(m+1)/2) = −1, because 7h(m+1) is odd. Hence G = −G = 0.
    - **m odd and 5 | m.** Put a = m/5. Then Q(n−a, k+a) − Q(n,k) = mn + a(7−m)/2. The shift multiplies every term by e(h(7−m)/10) = e(hj/5) with j = (7−m)/2 ≡ 1 mod 5. Since gcd(h,5) = 1, the factor is ≠ 1, so G = 0.
    - **m odd and 5 ∤ m.** Q is m-periodic, so G = m^{−2}Σ_{n,k mod m}. Because 2 is invertible mod m, the substitution n′ = n + 7·2^{−1}k gives hQ ≡ h(n′² − (35/4)k² + (7/2)k). So G = m^{−2}g₁g₂, where g₁ = Σ_{n′} e(hn′²/m) has |g₁| = √m. By the Chinese remainder theorem, g₂ factors over p^e ‖ m. For p ∤ 35, completing the square gives a factor of modulus p^{e/2}. For p = 7, the factor is Σ_{k mod 7^e} e(h′(−(5/4)k² + k/2)/7^{e−1}) = 7·Σ_{k mod 7^{e−1}}(…). Since −5/4 is a unit mod 7, it has modulus 7·7^{(e−1)/2}. Multiplying, |G| = m^{−2}·√m·√m·(√7 if 7 | m). This is non-zero.

## 2. Dimensions of S(ρ_s)

Here S(ρ_s) denotes the space of Maass cusp forms of type ρ_s on W, of weight 0, with λ = 1/4. Every result in this section assumes TB. Upper bounds come from `SF/A2/scripts/certify_hybrid.py` (M = 6, Q = 40; Arb ball arithmetic). Lower bounds come from the sector lemma (entry 25) applied with d_cusp > 0, or from exact Hecke or T-row determinants.

19. **Certificate.** dim S(ρ_s) = 1 for s = 5, 7, 9, 12, 13, 14. (`SF/A/REPORT.md` §3, `SF/A2/REPORT.md`.)
20. **Certificate.** dim S(ρ_s) = 2 for s = 11 and s = 19. At s = 19 there is one form in each of two sectors. (`SF/A2`, `SF/A9_hecke_family/certify_hecke_s.py`.)
21. **Certificate.** Assume in addition Γ(1596)-invariance via Wohlfahrt. Then dim S(ρ_21) = 5. The lower bound comes from the Hecke images T′_p, p = 1597, certified in Arb at 256 bits from exact Fourier coefficients. (`SF/A7_s21/certify_hecke.py`.)
22. **Certificate.** dim S(ρ_23) = 3 (`SF/A6_certify`) and dim S(ρ_25) = 3 (`SF/A9`).
23. **Certificate.**
    - 3 ≤ dim S(ρ_15) ≤ 4.
    - 3 ≤ dim S(ρ_17) ≤ 4.
    - dim S(ρ_s) ≥ 3 for s = 27, 29, 31.

    (`SF/A9_hecke_family`.)
24. **Theorem (Hecke commutation).** Let N ≥ 1 and let p be a prime with p ≡ 1 mod N. Let F be a smooth vector-valued function with F(γz) = ρ(γ)F(z) for all γ ∈ SL₂(Z), invariant under Γ(N), with ΔF = λF. Put T′_pF(z) = p^{−1/2}[F(pz) + Σ_{j=0}^{p−1} F((z+Nj)/p)]. Then:
    - T′_pF is of type ρ, with ΔT′_pF = λT′_pF;
    - T′_p commutes with every constant matrix, in particular with the sector projectors P_σ;
    - if every component of F is Σ_{m∈(1/N)Z} a(m)√y K₀(2π|m|y)e(mx) + c√y, then T′_pF has coefficients b(m) = a(pm) + a(m/p) and constant term 2c.

    *Proof.* Let Δ_p = {M ∈ M₂(Z) : det M = p, M ≡ I mod N}. The p+1 matrices (1, Nj; 0, p) (0 ≤ j < p) and (p, 0; 0, 1) lie in Δ_p, because p ≡ 1 mod N, and they represent the p+1 classes of Γ(N)\Δ_p. For γ ∈ SL₂(Z), γ^{−1}Δ_pγ = Δ_p, so {γ^{−1}Mγ} is again a system of representatives. Therefore Σ_M F(Mγz) = Σ_M F(γ·γ^{−1}Mγ·z) = ρ(γ)Σ_{M′} F(M′z), and the sum does not depend on the choice of representatives by Γ(N)-invariance. The Laplacian commutes with z ↦ Mz for M ∈ GL₂⁺(R), so λ is preserved, and the operator acts componentwise. On the Fourier side, F(pz) contributes p^{1/2}a(m′/p) at frequency m′. For the other terms, Σ_j e(mNj/p) equals p if p | mN and 0 otherwise; since mN ∈ Z and gcd(p,N) = 1, p | mN iff m/p ∈ (1/N)Z. So Σ_j F((z+Nj)/p) contributes p·p^{−1/2}a(pm′) at frequency m′. After the factor p^{−1/2}, b(m′) = a(pm′) + a(m′/p). Each √y-term contributes c√y, which gives 2c.

25. **Theorem (sector lemma).** Assume TB2. Let s be odd with 5 ≤ s ≤ 51, so that dim V = dim W = s(s−1). Let σ be a P-even local-sign sector other than the all-plus sector, with P_σW ≠ 0. Then P_σu is a non-zero cusp form of type ρ_s with λ = 1/4. Forms obtained from distinct sectors are linearly independent.
    *Proof.*
    1. P_σ is a polynomial in the local reflections Z_p, which commute with ρ. So P_σu has type ρ_s and eigenvalue 1/4.
    2. The constant term of u is a multiple of c₀ = Π_Wδ₀ (TB2). E = ρ-span(c₀) lies in the all-plus sector, because c₀ is even in every local component and the Z_p commute with ρ. Hence P_σc₀ = 0, the constant term of P_σu vanishes, and P_σu is cuspidal by the λ = 1/4 constant-term criterion.
    3. Since dim V = dim W, the components of u on W are linearly independent functions. If P_σu = 0, every row of P_σ would be a linear functional on W vanishing on all values of u, which would force P_σ|_W = 0, contrary to hypothesis.
    4. The sector projectors are mutually orthogonal, so forms in distinct sectors are independent.

### Dihedral structure

Throughout this subsection, s is odd, n = s(s−2), K_s = Q(√n), O = Z[√n], ω = (s+√n)/2 and ε = (s−1)+√n. "Dihedral over K_s" means a finite linear combination of theta series θ_ψ attached to finite-order Hecke characters ψ of K_s with ψ ≠ ψ∘σ, where σ is the non-trivial automorphism of K_s. K_s is a real quadratic field (n > 0 is not a square). In addition to TB and TB4, the results assume the classical Hecke–Maass correspondence: a Hecke theta series attached to a finite-order character of a real quadratic field, with no archimedean twist, is a Maass form with λ = 1/4; it is cuspidal iff ψ ≠ ψ∘σ, and it is an Eisenstein series iff ψ = ψ∘σ.


26. **Theorem (the lattice form is a norm form).** Let Q(x) = x₁² + s x₁x₂ + (s/2)x₂². Then Q(x) = N(x₁ + ωx₂), and Λ = Z + Zω is an invertible ideal of O. For s = 9, …, 29, ε is the fundamental unit of O and has norm +1. Consequently every component of the theta lift u is a Hecke theta series of K_s at λ = 1/4. Its cusp part is dihedral over K_s. The sector projectors P_σ and the Hecke operators T′_p (p ≡ 1 mod the T-level) preserve the space of such combinations.
    *Proof.* ω + ω′ = s and ωω′ = (s² − n)/4 = s/2, so N(x₁ + ωx₂) = x₁² + s x₁x₂ + (s/2)x₂². 2Q is primitive of discriminant 4n, so Λ is an invertible O-ideal. The unit statements come from the continued fraction of √n (exact integer arithmetic; `SF/A36_hecke_character/scripts/classdata.py`, `out/classdata.json`). By the coefficient formula of the lift (TB), a_{α,β}(m) = ½ Σ e(B(ν,β)), where the sum is over ν ∈ α + Λ with Q(ν) = m, taken modulo ε². So each component is the theta series of an ε²-invariant function on D⁻¹Λ/Λ with no |ν/ν′|^{it} factor. Expanding this function in characters of G₀ = I_D(O)/{(ν) : ν ≡ 1 mod D, N(ν) > 0} writes the component as a finite combination of θ_ψ(k·), and Hecke–Maass gives λ = 1/4. Terms with ψ = ψ∘σ are Eisenstein, so cusp parts involve only ψ ≠ ψ∘σ. P_σ is a constant matrix, and T′_p acts diagonally on each θ_ψ, so both preserve the space.


27. **Certificate (exact class data).** The data below are computed unconditionally, using Gauss reduction cycles and composition for Cl(O), the continued fraction of √n for ε, exhaustive enumeration of (O/DO)^×, and |G₀| = h·|(O/DO)^×| / |⟨−1, ε⟩ mod D| (`SF/A36_hecke_character/scripts/classdata.py`, `out/classdata.json`; no conditional input).

    | s | D | h⁺(4n) | h(4n) | Cl(O) | ring-class cusp pairs (h − \|Cl[2]\|)/2 | \|(O/DO)^×\| | \|G₀\| |
    |---|---|---|---|---|---|---|---|
    | 9 | 126 | 4 | 2 | Z/2 | 0 | 4536 | 36 |
    | 11 | 198 | 8 | 4 | Z/4 | 1 | 11880 | 120 |
    | 23 | 966 | 8 | 4 | (Z/2)² | 0 | 255024 | 528 |
    | 25 | 1150 | 12 | 6 | Z/6 | 2 | 506000 | 1320 |
    | 27 | 1350 | 12 | 6 | Z/6 | 2 | 486000 | 1080 |
    | 29 | 1566 | 12 | 6 | Z/6 | 2 | 789264 | 1512 |


28. **Theorem.** For s = 9, 11, 23 and 25, S(ρ_s) is exactly the span of forms built from u (by P_σ and T′_p). Hence every form in S(ρ_s) is dihedral over K_s. The data are:

    | s | K_s | Cl(O) | dim S(ρ_s) | eigensystems, as certified on the 8 sampled split primes |
    |---|---|---|---|---|
    | 9 | Q(√7) | Z/2 | 1 | one ray-class system; sampled ψ(𝔭) of order ≤ 2 |
    | 11 | Q(√11) | Z/4 | 2 | one system with ψ(𝔭) = 1 at every sampled principal 𝔭 (sampled ψ(𝔭) of order ≤ 2; observed order 2); one ray-class system |
    | 23 | Q(√483) | (Z/2)² | 3 | three ray-class systems; sampled ψ(𝔭) of order ≤ 2 |
    | 25 | Q(√23) | Z/6 | 3 | one system with ψ(𝔭) = 1 at every sampled principal 𝔭 (sampled orders 1 and 3); two ray-class systems |

    *Proof.* The certified lower bounds are realised by forms built from u alone. At s = 9 this is u_cusp; at s = 23, P_σu (entry 25); at s = 11 and 25, P_σu and T′_pP_σu (`SF/A9_hecke_family/certs/hecke_lower_s*.json`). These lower bounds equal the certified dimensions (entries 19, 20 and 22). So the span of these forms is all of S(ρ_s), and by entry 26 it is dihedral over K_s. The last column is read off from the eigenvalue certificate (entry 29). Ray-class type (not ring-class) is certified by a value ψ(𝔭) ≠ 1 at a principal 𝔭 in the sample. The sampled orders of ψ(𝔭) are divisors of the true character orders; no order beyond those observed is asserted.
    *Dihedral count.* At s = 25, the genus lifts Θ_𝔭 (lattices 𝔞Λ over every class of Cl(O)², with KR = 16 coefficient columns, exact ranks mod ℓ) lie in the span of P_σu and T′_pP_σu: sector ranks (5+,23+) 1 and (5−,23−) 2, total 3, which equals the proved dim S(ρ_25) = 3 (relative to TB, TB4 and the theta-lift theorem TB2; `SF/A37_dihedral_count/scripts/genus_rank.py`, `out/genus_s25.json`).


29. **Certificate (Hecke eigenvalues).** For each of the 15 eigensystems (sectors and Hecke eigenforms) at s = 9, 11, 23, 25, 27 and 29, the eigenvalue λ_p of T′_p at each of 8 split primes p ≡ 1 mod the T-level satisfies λ_p = ζ + ζ⁻¹ with ζ^E = 1, i.e. a_p = ψ(𝔭) + ψ(𝔭̄). Here E = exp((O/DO)^×)·h.
    *Certificate.* The lift coefficients are reduced exactly modulo a prime ℓ ≈ 10¹² with ℓ ≡ 1 mod lcm(D², phase denominators, E). Rank-1 sectors without an Eisenstein part give λ_p directly. The other sectors are solved with the second-order coefficients a(p₀²m). In the rank-2 sectors at s = 25, 27, 29, the 2 × 2 matrix of T′_{p₀} is verified exactly on two further columns. Membership of each λ_p in {ζ + ζ⁻¹ : ζ^E = 1} is tested exactly mod ℓ, and all 15 × 8 tests pass. Within each s the eigensystems are distinct (`SF/A36_hecke_character/scripts/hecke_modl.py`, `out/hecke_modl_s*.json`, `logs/run_s*.out`).


30. **Theorem.** At s = 9, 11, 23 and 25, the ring-class characters of O alone give 0, 1, 0 and 2 cusp pairs, against dim S(ρ_s) = 1, 2, 3 and 3. So ray-class characters of modulus dividing D are necessary at each of these s. At s = 25, at most one of the two ring-class pairs of Cl(O) occurs in S(ρ_25).
    *Proof.* The number of ring-class cusp pairs is (h − |Cl[2]|)/2 (entry 27), and the dimensions are entries 19, 20 and 22. At s = 25, S(ρ_25) is spanned by three eigenforms with pairwise distinct eigensystems (entries 28 and 29). Two of them are certified ray-class (entry 28). So at most one ring-class pair of Cl(O) ≅ Z/6 occurs.


31. **Theorem.** At s = 27 and s = 29, the three forms spanning the Hecke span of the sector projections of u (P_σu and T′_pP_σu) are dihedral over K_s. Only dim S(ρ_s) ≥ 3 is certified at these s (entry 23).
    *Proof.* By entry 26, every form built from u by P_σ and T′_p is dihedral over K_s. The three linearly independent forms are those certified in `SF/A9_hecke_family/certs/hecke_lower_s27.json` and `hecke_lower_s29.json`.
    *Dihedral count (certificate, relative to TB, TB4, TB2).* With KR = 16 coefficient columns and exact ranks mod ℓ ≈ 10¹², the sector ranks at both s = 27 and s = 29 are (+,+) 1 (with an Eisenstein part, cuspidal combinations used) and (−,−) 2, mixed sectors 0, and adding the genus lifts Θ_𝔭 over every class of Cl(O)² does not raise any rank. So the visible dihedral count is 3 at s = 27 and s = 29. This is a lower bound for dim S(ρ_s); no upper bound is asserted (`SF/A37_dihedral_count/out/genus_s27.json`, `genus_s29.json`, `logs/run_s27.out`, `logs/run_s29.out`).


## 3. Bridge C at s = 7

Here A_7 = [[2,7],[7,7]] and |D| = 35. ρ₃₅ is the Weil representation of the discriminant form D(A_7) (S e_μ = (i/√35) Σ_ν e(−b(μ,ν)) e_ν, T e_μ = e(q(μ)) e_μ). χ is the generator of Hom(SL₂(Z), C^×) ≅ Z/12, with χ(T) = e(1/12) and χ(S) = −i.

**The 35-component law vector.** Let A = A_7, Q(ν) = ½νᵀAν and B(ν,β) = νᵀAβ. For α, β ∈ Q² and x ∈ Q, put G_{α,β}(x) = mean over ν ∈ α + Z² of e(x·Q(ν) + B(ν,β)). This is the mean of a periodic function over a coset, so it is a finite Gauss mean. Let D = A⁻¹Z²/Z², a = (7/10, −1/5) and h_A = ½A⁻¹A* = (1/2, 0), where A* is the diagonal of A. Note that a ≡ h_A mod A⁻¹Z². The four candidate definitions of the 35-component law vector are the vectors indexed by μ ∈ D:
- K1_μ = G_{a+μ, a};
- K2_μ = G_{a+μ, 0};
- K3_μ = G_{μ, a};
- K4_μ = G_{μ, 0}.

V denotes the space of functions on Q spanned by the 105 components of K2, K3 and K4. Z₅ and Z₇ denote the local reflections of D = D₅ ⊕ D₇, which act as −1 on one local part and as the identity on the other.


32. **Theorem.** At s = 7, ρ_7|W = E ⊕ C with dim E = 36 and dim C = 6. Both E and C are irreducible, and dim C⁺ = dim C⁻ = 3. Hence C has no 1-dimensional ρ-invariant subspace, and any S-eigenvector in C generates all of C as a ρ-module.
    *Proof.* dim End(ρ_7|W) = 2 (exact mod-p upper bound; `SF/A32_35_to_rho7/exact_hom.py`), and E, C ≠ 0 are subrepresentations. So both summands are irreducible and non-isomorphic. The equality of C⁺ and C⁻ is entry 1. (`SF/RTA_implications/REPORT.md`.)
33. **Certificate.** Assume TB. Then dim S(ρ_7) = 1. (`SF/A/scripts/certify_s.py`, `SF/A/REPORT.md` §3.)
34. **Theorem.**
    - Q(√35) has class number 2, and 6 + √35 is a unit of norm +1.
    - [[2,1],[1,−17]] is an odd lattice.
    - There is no even binary lattice of determinant −35.

    *Proof.* 6² − 35 = 1, and the class number is standard. For an even binary form, the discriminant b² − 4ac would equal 35, but 35 ≡ 3 mod 4 is not a square mod 4. (`SF/RTA_prereg/REPORT.md`.)
35. **Theorem.** Let C be any irreducible unitary representation.
    - Every Γ-equivariant map C^{⊗a} ⊗ C̄^{⊗b} → C is Z/3-graded by R-degree.
    - If no T-exponents satisfy a + b + c − d ≡ 0 mod 1, then Hom_Γ(C⊗C⊗C, C) = 0.
    - The products x⟨z, y⟩ and z⟨x, y⟩ are equivariant.

    *Proof.* R³ = I acts on the tensor product, and an intertwiner commutes with R. An intertwiner also commutes with T, so it can only connect T-eigenvectors whose exponents match. ⟨·,·⟩ is Γ-invariant. (`SF/A18_RTA_foundation/REPORT.md`.)
36. **Theorem.** dim Hom_{SL₂(Z)}(ρ₃₅ ⊗ χ³, ρ_7|W) = 1. A generator Φ is monomial: after rescaling, its non-zero entries lie in {±1, ±e(1/5)}. Its image is exactly C, and its kernel has dimension 29. Consequently C ≅ ρ₅⁻ ⊗ ρ₇⁻ ⊗ χ³, where ρ₅⁻ ⊗ ρ₇⁻ is the 6-dimensional subspace of ρ₃₅ that is odd under both local reflections Z₅ and Z₇.
    *Proof and certificate.*
    - **Upper bound.** dim ≤ 1 from an exact mod-p rank computation at p = 29 401 and p = 14 729 401 (p ≡ 1 mod 29 400; `SF/A32_35_to_rho7/exact_hom.py`).
    - **Lower bound.** The explicit 35 × 42 matrix Y with unit entries (`SF/A32_35_to_rho7/X_chi3.npy`) satisfies Y·S₃₅′ = S_7·Y (210 of 210 entries) and Y·T₃₅′ = T_7·Y (24 of 24 entries), exactly in Z[Z/29400] modulo Φ₂₉₄₀₀ (`SF/A32_35_to_rho7/exact_verify.py`). Generators suffice.
    - **Rank and image.** The six image rows have disjoint column supports, so the rank is 6. The image is a 6-dimensional subrepresentation of W = E ⊕ C. By entry 32 it must be C.
    - **Kernel and isomorphism.** The kernel contains the 11 labels with a zero local component and the 18-dimensional complement of the (−,−) sector on the 24 primitive labels, so Φ restricted to ρ₅⁻ ⊗ ρ₇⁻ ⊗ χ³ is an isomorphism onto C.

37. **Theorem (elementary rules).** For all α, β ∈ Q² and x ∈ Q:
    - G_{α+n,β} = G_{α,β} for every n ∈ Z²;
    - G_{α,β+λ} = e(B(α,λ))·G_{α,β} whenever Aλ ∈ Z²;
    - G_{gα,gβ} = G_{α,β} for every g ∈ GL₂(Z) with gᵀAg = A.

    *Proof.* The first rule holds because α + n + Z² = α + Z². For the second, write ν = α + n; then B(n,λ) = nᵀAλ ∈ Z, so the factor is e(B(α,λ)). For the third, ν ↦ gν is a bijection of α + Z² onto gα + Z² with Q(gν) = Q(ν) and B(gν,gβ) = B(ν,β), and it preserves means of periodic functions.


38. **Theorem (automorph and the local reflection Z₇).** Let γ = [[−1,−7],[2,13]]. Then:
    - γᵀAγ = A and det γ = 1;
    - γ⁻¹ acts on D as Z₇, i.e. as the identity on D₅ and as −1 on D₇;
    - γ⁻¹a − a = (7, −1) ∈ Z².

    Consequently the vectors K2, K3 and K4 are Z₇-invariant: g_μ = g_{Z₇μ} for every μ ∈ D. So their Z₇-odd parts vanish, and in particular their ρ₅⁻ ⊗ ρ₇⁻ parts vanish. K1 is Z₇-odd, and K1 ≡ 0 (entry 42), so the ρ₅⁻ ⊗ ρ₇⁻ part of each of K1–K4 is 0. Hence the image of each of K1–K4 under the χ³-twisted map Φ of entry 36 is 0.
    *Proof.* The identities for γ are a direct computation in integer and rational arithmetic. By the first and third rules of entry 37, G_{α,β} = G_{γ⁻¹α, γ⁻¹β}. By the first rule, γ⁻¹(a+μ) ≡ a + Z₇μ mod Z², and by the second rule the class of the β-argument can be moved back with an explicit phase. For K2, K3 and K4 these phases equal 1 for all 35 μ; for K1 the phase is ½, i.e. the factor is −1. Φ factors through the projection onto ρ₅⁻ ⊗ ρ₇⁻ (entry 36). *Certificate:* exact rational check of all phases for the 35 values of μ (`SF/A33_law_vector_chi3/exact_z7.py`, output `exact_z7.json`).


39. **Theorem (T-law and S-law).** For all α, β ∈ Q² and x ∈ Q:
    - **T-law:** G_{α,β}(x+1) = e(−Q(α) − B(α,h_A))·G_{α, β+α+h_A}(x);
    - **S-law:** for x ≠ 0, G_{α,β}(−1/x) = (1/(|x|√35))·e(B(α,β))·Σ_{p∈D} G_{β+p, −α}(x).

    *Proof.* *T-law.* For n ∈ Z², Q(n) = n₁² + 7n₁n₂ + (7/2)n₂² ≡ (7/2)n₂ ≡ B(n,h_A) mod 1, because n₂² ≡ n₂ mod 2. With ν = α + n, this gives Q(ν) ≡ Q(α) + B(n,α) + B(n,h_A) ≡ B(ν, α + h_A) − Q(α) − B(α,h_A) mod 1. Substituting into the mean proves the law.
    *S-law.* Fix y ≠ 0 and t > 0, and put Z = yA + itI. Let f(ν) = exp(πi·νᵀZν + 2πi·B(ν,β)). Poisson summation gives Σ_{ν∈α+Z²} f(ν) = det(−iZ)^{−1/2}·Σ_{w∈Z²} e(wᵀα)·exp(−πi(w − Aβ)ᵀZ⁻¹(w − Aβ)). Substitute w − Aβ = −Aγ', so that γ' runs over β + A⁻¹Z² and e(wᵀα) = e(B(α,β) − B(γ',α)). Now let t → 0.
    - *Left side.* The integrand is periodic, so t·(left side) → G_{α,β}(y), up to an exponentially small error.
    - *Determinant.* A has eigenvalues λ₁ > 0 > λ₂. With principal branches, det(−iZ)^{1/2} → √(|y|λ₁)e^{∓iπ/4}·√(|y||λ₂|)e^{±iπ/4} = |y|√35 for either sign of y.
    - *Exponent.* AZ⁻¹A = A/y − (it/y²)I + O(t²). On the coset β + A⁻¹Z² (density 35), the right side is therefore a periodic phase e(−Q(γ')/y − B(γ',α)) times the Gaussian e^{−πt|γ'|²/y²}, up to O(1). Summing gives 35·(mean)·y²/t. The mean over β + A⁻¹Z² equals (1/35)Σ_{p∈D} G_{β+p,−α}(−1/y).
    - *Conclusion.* Comparing the 1/t terms, G_{α,β}(y) = (|y|/√35)·e(B(α,β))·Σ_p G_{β+p,−α}(−1/y). Putting y = −1/x gives the S-law.

    *Closed forms.* Reducing every term with entry 37, both laws map the 105 symbols K2 ∪ K3 ∪ K4 into their own span. The S-matrix M_S has rows (1/√35)·Σ of 35 terms of the form e(k/9800). The T-matrix M_T is monomial with phases e(k/9800): it is diagonal on K2 and swaps K3_μ ↔ K4_μ. The family K1 is mapped into its own span by both laws. (`SF/A35_lawspace_exact/symbols.py`.)


40. **Theorem.** dim V = 36, and V is closed under S and T, i.e. under x ↦ −1/x with the weight |x|⁻¹ of entry 39, and under x ↦ x + 1.
    *Proof and certificate.*
    - *Upper bound.* By the third rule of entry 37, applied to the 12 automorphs of A found with entries of absolute value ≤ 40 (including ±I and γ), the 105 symbols fall into orbits, 12 in each of K2, K3 and K4. Within an orbit, every symbol is e(k/9800) times the orbit representative. So V is spanned by the 3·12 orbit representatives, and dim V ≤ 36 (`SF/A35_lawspace_exact/orbits.py`).
    - *Lower bound.* The Gauss means of all 105 symbols are evaluated exactly mod p at the 48 rationals h/m with 1 ≤ m ≤ 6 and −2m ≤ h < 2m, for p = 1 764 001 and p = 6 468 001 (both ≡ 1 mod 588 000, with ζ sent to a root of unity of F_p). At both primes the rank equals the number of orbit representatives, 3·12. The values lie in Z[ζ][1/(4m)²], and rank can only drop under reduction, so the rank in characteristic 0 is ≥ 36 (`SF/A35_lawspace_exact/exact_main.py`, `exact_main.json`: `eval_points` 48 and `eval_rank` 36 at both primes).
    - *Closure.* By entry 39, both laws hold for all x and map symbols to combinations of symbols, so V is S- and T-stable. The orbit representatives form a basis.


41. **Theorem.** V ≅ E as SL₂(Z)-representations, with no twist. Moreover, for every k ∈ Z/12: Hom(V ⊗ χᵏ, C) = Hom(C, V ⊗ χᵏ) = 0; Hom(V ⊗ χᵏ, E) = 0 for k ≠ 0; and End(V) is 1-dimensional. In particular no χᵏ-twist of the 35-component law vector maps non-trivially to C, including k = 3.
    *Proof and certificate.*
    - *Hom dimensions.* The intertwining equations are solved over F_p at two primes with ζ mapped into F_p (A32's method). Each mod-p dimension is an upper bound for the dimension in characteristic 0. The results are End(V) = 1, Hom(V,E) = Hom(E,V) = 1, Hom(V⊗χᵏ,C) = Hom(C,V⊗χᵏ) = 0 for all k, and Hom(V⊗χᵏ,E) = 0 for k ≠ 0, identically at both primes (`SF/A35_lawspace_exact/exact_main.py`, `exact_main.json`).
    - *Explicit isomorphism.* Let N = 58 800. On V and on E, T is monomial, and its exact eigenbases P_V and P_E lie over Z[½, ζ_N] (P⁻¹P = I verified exactly). The two spectra coincide, and each eigenvalue occurs with multiplicity 1. Put X = P_E·Π·diag(c)·P_V⁻¹, where Π matches equal eigenvalues and each c_i is a root of unity ζ_N^{e_i}. Then X·T_V = T_E·X by construction. X·S_V = S_E·X was verified exactly modulo Φ₅₈₈₀₀ in all 1296 entries; the common factor 1/√35 cancels. X is invertible as a product of invertible matrices (`SF/A35_lawspace_exact/exact_intertwiner.py`, `exact_intertwiner.json`).


42. **Theorem.** K1 ≡ 0 on Q.
    *Proof.* *x = 0:* G_{α,a}(0) = e(B(α,a))·(mean over n ∈ Z² of e(nᵀAa)). Since Aa = (0, 7/2), this is the mean of (−1)^{n₂}, which is 0. *Closure:* by entry 39, T maps K1 to K1 monomially, and S maps K1 to linear combinations of K1. *Induction on the denominator:* for integers n, K1(n) = M_Tⁿ·K1(0) = 0. For x = h/m in lowest terms with m ≥ 2, write x = n + r/m with 0 < r < m. By the T-law, K1(x) is a monomial image of K1(r/m), and by the S-law K1(r/m) = (r/m)·M_S·K1(−m/r). Here −m/r has the smaller denominator r, so the induction closes.


## 4. T3 and budget arithmetic

T3(n) is defined by:
- T3(n) = n/3 for n ≡ 0 mod 3;
- T3(n) = (4n + 2)/3 for n ≡ 1 mod 3;
- T3(n) = (2n + 1)/3 for n ≡ 2 mod 3 (in the integer form of `SF/A20`).

σ(n) is the number of steps needed to reach 1.

43. **Theorem.** With the integer form, T3 maps positive integers to positive integers. The expression (2n + 1)/3 is not an integer for n ≡ 2 mod 3; for example, (2·2 + 1)/3 = 5/3.
    *Proof.* Check each residue class mod 3. (`SF/A20`, `SF/A25`.)
44. **Theorem.** σ(3ᵏm) = k + σ(m), and σ(3ᵏ) = k.
    *Proof.* T3(3n) = n. Use induction on k. (`SF/A23`, `SF/A24`.)
45. **Theorem.** If σ(n) ≤ 539, then T3^{539}(n) = 1 when σ(n) is odd, and T3^{539}(n) = 2 when σ(n) is even.
    *Proof.* T3 alternates 1 ↦ 2 ↦ 1. After reaching 1 at step σ(n), the remaining 539 − σ(n) steps alternate. (`SF/A23_axiom01_revised/REPORT.md`.)
46. **Theorem.** If σ(n) ≤ 540, then T3^{540}(n) = 1 iff σ(n) is even. In particular T3^{540}(4880) = 1, and among n ≤ 10⁶, exactly 504 899 end at 1 and 495 101 end at 2.
    *Proof.* As in entry 45. The counts are an exact enumeration (`SF/A30_540_thermo/tests540.py`).
47. **Theorem.** For every j ≥ 1, the map n mod 3ʲ ↦ (T3ˢ(n) mod 3)_{0≤s<j} is a bijection from Z/3ʲ onto the words of length j over {0, 1, 2}.
    *Proof.* Induction on j. On each residue class mod 3, T3 is affine with leading coefficient 1/3 or 4/3 or 2/3. So T3(n) mod 3^{j−1} is determined by n mod 3ʲ, and it runs over all classes mod 3^{j−1} as n runs over a fixed class mod 3. Exhaustive check for j ≤ 8: `SF/A29_patterns_all/run_core.py`.
48. **Theorem.** T3 does not induce a map on Z/9 (and more generally on Z/3ʲ).
    *Proof.* By entry 47, T3(n) mod 3ʲ depends on n mod 3^{j+1} and not on n mod 3ʲ.
49. **Theorem.** Each m has an explicit list of T3-preimages. Moreover, T3(n) + 2 ≤ (4/3)(n + 2), with equality iff n ≡ 1 mod 3.
    *Proof.* The preimages are found by inverting each branch. For the inequality: n ≡ 1 gives equality, and the other branches give strictly less. (`SF/A24_threshold_1e18`.)
50. **Theorem.** ⌊(4880 − 21)/9⌋ = 539.
    *Proof.* 4859/9 = 539.89. (`SF/A20`, `SF/A23`.)
51. **Theorem.** ⌊3⁵e³⌋ = 4880 and ⌊35e³⌋ = 702.
    *Proof.* 3⁵e³ = 4880.84 and 35e³ = 702.99, both evaluated with rigorous error bounds. (`SF/A19`, `SF/A25`.)
52. **Theorem.**
    - 540 = 2²·3³·5 = 4860/9.
    - ⌊(4880 − f)/9⌋ = 540 exactly for f = 12, …, 20.
    - 539.9 = 540(1 − 1/5400).
    - 5399 is prime. Hence e^{2πi/539.9} = e^{2πi·10/5399} is a primitive 5399th root of unity, and its 539th power is not 1. Moreover, 539 steps of the phase e^{2πi/539.9} give 5390/5399 of a full turn.
    - The beat period of 540 against 539.9 is 2 915 460.

    *Proof.* Direct computation. Primality of 5399 is checked by trial division up to 73. (`SF/A25`, `SF/A30`.)
53. **Certificate.** Let m₅₃₉ be the smallest n with σ(n) = 539. Then:
    - 10⁷ < m₅₃₉ ≤ 788 638 819 521 764 360 564 859 602 047 870.
    - For every d ≤ 291 there is a seed below 10¹⁸ with σ = d.
    - σ(666 954 248 808 172 552) = 291.

    The method is exact integer iteration (`SF/A24_threshold_1e18/exact_min.py`, `beam.py`).
54. **Certificate (exact counts).**
    - max_{n ≤ 20 000} σ(n) = 53, attained at n = 16261.
    - max_{n ≤ 50 000} σ(n) = 55, attained at n = 36043 and 36592.
    - σ(4880) = 14 and σ(10¹⁸) = σ(10¹⁸ + 1) = 92.
    - σ(3^{539}) = 539.
    - Every n ≤ 10⁷ satisfies σ(n) ≤ 539.
    - σ(3^{540}) = 540, and T3^{539}(3^{540}) = 3.

    The method is exact integer iteration (`SF/A19_9maths_axioms/checks.py`, `SF/A23_axiom01_revised/budget.py`, `SF/A28`).
55. **Theorem.**
    - φ⁷ = (29 + 13√5)/2.
    - 1001 = 7·11·13.
    - 18 + 1 + 520 = 539.
    - 243 − 244 + 55 = 54.
    - 4·8 + 5·12 = 92.
    - 4·122 = 488.

    *Proof.* Direct computation. For φ⁷, use φⁿ = (Lₙ + Fₙ√5)/2 with L₇ = 29 and F₇ = 13.
56. **Theorem.** Consider any lift of T3 in which the integer coordinate evolves by T3 and steps are counted one-to-one. In any such lift, the number of steps to reach 1 is exactly σ(n).
    *Proof.* The projection to the integer coordinate is a step-preserving semiconjugacy. (`SF/A20_T3_bulk_vs_shadow`.)

## 5. The H3 orbit map

Φ(n) = Σ_{s<539} w(r_s(n)) ∈ ⟨c⟩ ≅ Z/N, where r_s(n) = T3ˢ(n) mod 3, and w: {0, 1, 2} → Z/N.

57. **Theorem.** Φ is well defined for every n ≥ 1.
    *Proof.* The sum is finite (539 terms) and every T3ˢ(n) is defined. (`SF/A28_H3_map_construction/REPORT.md`.)
58. **Theorem (cocycle law).** Let S_k(n) = Σ_{s<k} w(r_s(n)). Then S_{k+l}(n) = S_k(n) + S_l(T3ᵏn). Hence w induces a monoid homomorphism {0, 1, 2}* → Z/N.
    *Proof.* Split the sum at s = k.
59. **Theorem (tail formula).** If σ(n) ≤ 539 and L = 539 − σ(n), then Φ(n) = S_σ(n) + ⌈L/2⌉w(1) + ⌊L/2⌋w(2).
    *Proof.* Apply entry 58 at k = σ(n). The tail orbit is 1, 2, 1, 2, …, with residues 1, 2, 1, 2, …. An exact check on 301 seeds × 9 weight choices is in `SF/A28_H3_map_construction/h3map.py`.
60. **Theorem.** Replacing the generator c by another generator multiplies Φ by a unit of Z/N. This preserves the zero set of Φ, its additive order, and τ. The manifolds M_A and M_B, with Z/N coefficients, give identical values.
    *Proof.* Φ depends only on the cyclic group ⟨c⟩ ≅ Z/N.
61. **Theorem.**
    - Tors H³(M_A; Z) = Z/N, and there is no self-linking form on H³ in dimension 7.
    - For M_B = L⁷(N), H³(M_B; Z) = 0 and H³(M_B; Z/N) = Z/N.

    *Proof.* Standard: universal coefficients, and the cellular chain complex of a lens space. A linking form in dimension 7 pairs H³ with H⁴, not H³ with itself. (`SF/A28`.)
62. **Theorem.** Let T = d + (ζ(t) − 1)H₃∧. Then T² = 0 iff dt ∧ H₃ = 0 and dH₃ = 0. A torsion class has no non-zero de Rham representative. On M_A, H₃ is exact, and T = e^{−fB} ∘ d ∘ e^{fB}; hence the T-cohomology is isomorphic to de Rham cohomology.
    *Proof.* Expand T². de Rham cohomology is a real vector space, so torsion maps to 0. If H₃ = dB, conjugate d by the exponential. (`SF/A25`, `SF/A28`.)

## 6. Non-existence and vanishing results

63. **Theorem.** There exist positive integers n with σ(n) > 539. Specifically, σ(3^{540}) = 540.
    *Proof.* Entry 44.
64. **Theorem.** For every k ≥ 38 with k ≠ 539, σ(3ᵏ) = k ≠ 539, and 3ᵏ > 10¹⁸. Hence σ is not constantly equal to 539 on n ≥ 10¹⁸.
    *Proof.* Entry 44, together with 3^{38} > 10¹⁸.
65. **Theorem.**
    - 3·61 + 162 + 223 = 568.
    - 244 − 18 − 1 = 225.
    - The alternating sum of the sequence of Betti numbers recorded in `SF/A25` is −162.
    - A closed oriented 7-manifold has b₃ = b₄. Hence no closed oriented 7-manifold has b₃ = 223 and b₄ = 61.
    - With χ = 0 and rk = 3, χ/2 + rk = 3.
    - 3¹⁸ < 10⁹.

    *Proof.* Direct computation. b₃ = b₄ follows from Poincaré duality. (`SF/A25`.)
66. **Theorem.** 540·{2, 3, 4, 5, 10} = {1080, 1620, 2160, 2700, 5400}. None of these is an integer multiple of 539.9.
    *Proof.* k·540/539.9 = 5400k/5399. Since 5399 is prime and does not divide 5400k for these k, the quotient is not an integer. (`SF/A19`, `SF/A23`.)
67. **Theorem.**
    - 540/(1 + 1/540) = 291600/541 ≈ 539.0018.
    - 540/(1 + 0.01·0.185) ≈ 539.0028.
    - 540(1 − 0.0001) = 539.946.
    - 540/(1 + δ) = 539.9 iff δ = 1/5399.

    *Proof.* Direct computation. (`SF/A30`.)
68. **Theorem.** Let ω > 0 and let A, κ be constants with κ ≠ 0. Consider the ordinary differential equation (★) AΦ″(t) = κ sin(ωt)Φ(t). This is the spatially homogeneous form (Φ = Φ(t), constant coefficients) of the friction-coupled equation ∂_t²Φ + c ∂_t²Φ = κ sin(ωt)Φ + βg ∂_t²Φ, with A = 1 + c − βg.
    - (i) For every Φ₀ and every (a, b) ≠ (0, 0), the function Φ₀ + a cos ωt + b sin ωt is not a solution of (★).
    - (ii) If A ≠ 0, then (★) has no solution that attracts all solutions.
    - (iii) If A = 0, the only solution is Φ ≡ 0.

    *Proof.* (i) The left side has only the frequency ω. The right side equals κΦ₀ sin ωt + (κa/2) sin 2ωt + (κb/2)(1 − cos 2ωt). Equating the coefficients of sin 2ωt and cos 2ωt gives a = b = 0. (ii) Write (★) as x′ = M(t)x with x = (Φ, Φ′) and M = (0, 1; κA^{−1} sin ωt, 0). Since tr M = 0, Liouville's formula shows that the monodromy matrix has determinant 1. Suppose a solution p satisfies |x(t) − p(t)| → 0 for every solution x. The differences x − p run over all solutions, so every solution would tend to 0. Then both Floquet multipliers would have modulus less than 1, which contradicts determinant 1. (iii) If A = 0, then κ sin(ωt)Φ(t) = 0. So Φ vanishes wherever sin ωt ≠ 0, and by continuity everywhere.

69. **Theorem.** Let V ∈ {ρ₃₅, ρ₃₅*}, U ∈ {ρ_7|W, ρ_7|W*} and k ∈ Z/12. Then Hom_{SL₂(Z)}(V ⊗ χᵏ, U) = 0 and Hom_{SL₂(Z)}(U, V ⊗ χᵏ) = 0, except in the two cases (V, k, U) = (ρ₃₅, 3, ρ_7|W) and (ρ₃₅*, 9, ρ_7|W*), where the dimension is 1 (entry 36 and its complex conjugate). In particular there is no non-zero intertwiner ρ₃₅ → ρ_7|W. All 12 T-eigenvalues of ρ₃₅ occur in ρ_7|W, so the vanishing is forced by S, not by the T-spectra.
    *Certificate.* The equations XS₁ = S₂X and XT₁ = T₂X are solved over F_p with ζ ↦ a primitive 29 400th root of unity. This was done at p = 29 401 and p = 14 729 401, with identical results. 96 Hom spaces were computed, and the mod-p nullity is 0 in each case listed. (`SF/A32_35_to_rho7/exact_hom.py`, `run.py`, `results.json`.)
70. **Theorem.** Let s ∈ {8, 10, 16, 18}, let L be the conductor of the label data, and let Ŝ = √|D|·S. There is no triple (a, u, k), with a ∈ (Z/L)^×, u ∈ (Z/D)^× and k ∈ Z, such that σ_a(T) = M_u T^k M_u^{−1} and σ_a(Ŝ) = −M_u Ŝ M_u^{−1}. Here σ_a is the Galois automorphism ζ_L ↦ ζ_L^a, and M_u is the label dilation x ↦ ux.
    *Certificate.* `SF/A8c_Spairing_even/scripts/galois_dilation_fast.py`. For each (a, u), it searches exhaustively for k by testing the T-identity exactly as an identity of monomial matrices with integer phases. For every compatible triple it then tests the Ŝ-identity entrywise modulo one prime 𝔭 | p with p ≡ 1 mod L. An identity in characteristic 0 survives reduction, and the signs +1 and −1 cannot both hold mod 𝔭, because p is odd and Ŝ is invertible. Results: (compatible triples, sign +1, sign −1) = (1024, 128, 0), (4096, 256, 0), (36864, 768, 0), (36864, 768, 0) at s = 8, 10, 16, 18. At s = 12 and 14 there are sign −1 solutions, which exercises the test.
71. **Theorem.** Let h(D) be the wide class number of discriminant D. Let K_s = Q(√(s(s−2))) with discriminant d_K, and let 4n_s = 4s(s−2).
    - (i) h(d_K) = 1 at s = 9, 11, 25, 27 and h(d_K) = 2 at s = 29. In each case dim S(ρ_s) ≠ h(d_K)/2.
    - (ii) h(4n_23) = 4 and dim S(ρ_23) = 3. In particular dim S(ρ_23) ∉ {h/2, h}.

    *Proof.* The class numbers are computed exactly by counting the cycles of reduced primitive indefinite forms under Gauss reduction. Two reduced forms are properly equivalent iff they lie on the same cycle. The wide classes are the orbits of the cycles under (a,b,c) ↦ (−a,b,−c). (Script: `SF/A34_ledger_checks/scripts/classno_exact.py`, output `classno_exact.json`.) The dimensions are those of entries 19, 20, 22 and 23: dim = 1, 2, 3 at s = 9, 11, 25; dim ≥ 3 at s = 27, 29; dim = 3 at s = 23. In (i), the values h/2 are 1/2 at s = 9, 11, 25, 27 and 1 at s = 29, and none of them equals the dimension.

72. **Theorem.** Assume I1–I5. At s = 56, the multiplicities of the eigenvalues (1, ω, ω̄) of R = ST are (187, 186, 187) on E and (84, 84, 84) on C.
    *Proof.* *dim E = 560.* By entry 7(iii), dim E = dim E0_{27}·dim E0_7·dim E0_2. The two odd factors are 14 and 4 (entry 7(i)). The 2-adic factor is the dimension for an order-16 class (2,1/4) ⊕ (8, −u/16). For these classes, `SF/A11_induction/exact_E0.py` certifies that the span is exactly 10-dimensional for u ≡ 1 mod 4 and exactly 9-dimensional for u ≡ 3 mod 4 (`logs_exact_E0.txt`). So dim E ∈ {504, 560}. A mod-ℓ Krylov rank (`SF/A31_entry7_check/global_trE.py`, two primes) gives dim E ≥ 560, so dim E = 560.
    *Multiplicities.* At s = 56, (Exc) holds and s ≡ 2 mod 3, so entry 11 gives tr_E R = tr_W R = −ω. Write (n₁, n_ω, n_ω̄) for the multiplicities on E. Then n₁ + n_ω + n_ω̄ = 560 and n₁ + ωn_ω + ω̄n_ω̄ = −ω. Comparing imaginary parts gives n_ω̄ = n_ω + 1, and comparing real parts gives n₁ = n_ω + 1. Hence 3n_ω + 2 = 560, and the multiplicities are (187, 186, 187). On C, dim C = dim W − dim E = 812 − 560 = 252, where dim W = t(t+1) with t = 28 is an orbit count. Also tr_C R = tr_W R − tr_E R = 0, so the three multiplicities are equal, namely 84.


## 7. The g_k family: parity dominance, OccFilt_k(∞) and zero sets

Path shorthand as above. Throughout, k ≥ 1 is an integer.

73. **Definitions.**
    - g_k(q) = Σ_{n≥0} q^{n²}/(−q^k;q^k)_n = Σ_d g_k(d) q^d. Write P_n(x) = ∏_{j≤n}(1+x^j)^{−1} = Σ_m φ_n(m)x^m. Then g_k(d) = Σ_n φ_n((d−n²)/k), the sum running over n ≥ 0 with n² ≤ d and n² ≡ d mod k.
    - **Allowed d:** d mod k is a square mod k. For every other d, g_k(d) = 0 trivially.
    - **OccFilt_k(∞)** is the set of residues r mod k such that g_k(d) ≠ 0 for every sufficiently large d ≡ r mod k.
    - **Zero set and zero count.** Z_k is the set of allowed d ≥ 0 with g_k(d) = 0, and #Z_k is its cardinality. Every such d is counted, including those at which each individual term vanishes. This is the only zero-count notion used in this ledger.
    - a_n(m) = (−1)^m φ_n(m). For odd k, E_d = Σ_{n even} a_n((d−n²)/k) and O_d = Σ_{n odd} a_n((d−n²)/k), with n ranging as above.

74. **Theorem (positivity and sign split).** For all n, m ≥ 0, a_n(m) = [x^m] ∏_{odd j≤n}(1+x^j)·∏_{n/2<l≤n}(1−x^{2l})^{−1}; in particular a_n(m) ≥ 0. For odd k and every d, (−1)^d g_k(d) = E_d − O_d with E_d, O_d ≥ 0.
    *Proof.* Put y = −x. Then 1/(1+y^j) = (1−y^j)/(1−x^{2j}). The numerator ∏_{j≤n}(1−y^j) equals ∏_{odd j≤n}(1+x^j)·∏_{l≤⌊n/2⌋}(1−x^{2l}), and the second factor cancels the first ⌊n/2⌋ factors of ∏_{l≤n}(1−x^{2l}). What remains has non-negative coefficients. For odd k, km ≡ m mod 2, so with m = (d−n²)/k, (−1)^m = (−1)^{d−n²} = (−1)^{d+n}; hence (−1)^d φ_n(m) = (−1)^n a_n(m), and summing over n gives E_d − O_d. *Check:* exact for n ≤ 60 to x^3000 (`SF/A44_oddk_audit/proof/check_model.py`).

75. **Theorem (pairing identity, odd k).** Let k be odd and P̃_n(q) = ∏_{j≤n}(1 + (−q^k)^j). Then

    g_k(−q) = Σ_{m≥0} U_m(q)·(1 − q^{4m+1} − q^{(2m+1)k}),  U_m = q^{4m²} / (P̃_{2m}(q)(1 − q^{(2m+1)k})),

    and every U_m has non-negative integer coefficients.
    *Proof.* For odd k, (−(−q)^k; (−q)^k)_n = P̃_n and (−q)^{n²} = (−1)^n q^{n²}, so the n-th term of g_k(−q) is T_n = (−1)^n q^{n²}/P̃_n. Since (2m+1)² − (2m)² = 4m+1 and P̃_{2m+1} = P̃_{2m}(1 − q^{(2m+1)k}), T_{2m+1} = −T_{2m}·q^{4m+1}/(1 − q^{(2m+1)k}). Adding T_{2m} and T_{2m+1} gives U_m(1 − q^{4m+1} − q^{(2m+1)k}). Positivity: 1/P̃_{2m}(q) is the series A_{2m}(x) = Σ_m a_{2m}(m)x^m at x = q^k, which is coefficientwise ≥ 0 by entry 74, and 1/(1 − q^e) ≥ 0. *Check:* exact integer check of the identity and of U_m ≥ 0 to q^2500 for every odd k ≤ 25 (`SF/A44_oddk_audit/analysis/pairing_check.py`).

76. **Lemma (stabilisation).** Let P_∞(x) = ∏_{j≥1}(1+x^j)^{−1} = Σ_m c_m x^m. Then φ_n(m) = c_m for all m ≤ n. Moreover c_0, …, c_12 = 1, −1, 0, −1, 1, −1, 1, −1, 2, −2, 2, −2, 3; in particular **c_2 = 0** and **c_6 = 1**. Also φ_0(m) = δ_{m,0} and φ_1(m) = (−1)^m.
    *Proof.* P_n = P_∞·∏_{j>n}(1+x^j), and ∏_{j>n}(1+x^j) ≡ 1 mod x^{n+1}, so P_n ≡ P_∞ mod x^{n+1}. The values c_m follow by expanding ∏_{j≤12}(1+x^j)^{−1} to x^{12} (exact integer arithmetic). P_0 = 1 and P_1 = 1/(1+x) give the last two statements.

77. **Theorem.** For every squarefree k ≥ 2, g_k(k(k+2)) = 0.
    *Proof.* Let d = k² + 2k < (k+1)². Every contributing n satisfies n ≤ k and k | d − n², i.e. k | n². Since k is squarefree, k | n, so n ∈ {0, k}. The term n = 0 is φ_0(k+2) = 0. The term n = k has m = 2 ≤ k, so it is φ_k(2) = c_2 = 0 by entry 76. Hence g_k(d) = 0. ∎
    *Sharpness.* g_1(3) = φ_1(2) = 1, so k ≥ 2 is needed.
    *Check:* exact for k = 2..1001: all 608 squarefree k give 0, and none of the 392 non-squarefree k gives 0 (`SF/A46_zero_facts_audit/check.py`, `results.json`).

78. **Theorem.** For every odd prime power k ≥ 5, g_k((k+2)² − 3) = 0.
    *Proof.* Let d = k² + 4k + 1 = (k+2)² − 3, so contributing n satisfy n ≤ k+1, and since d ≡ 1 mod k, n² ≡ 1 mod k. Write k = p^a with p odd. Then p^a | (n−1)(n+1) and p does not divide both factors, so n ≡ ±1 mod k. In [0, k+1] this gives n ∈ {1, k−1, k+1}, distinct for k ≥ 3. The terms are: n = 1: φ_1(k+4) = (−1)^{k+4} = −1 (k odd); n = k−1: m = 6, and for k ≥ 7, m ≤ k−1, so the term is c_6 = +1; n = k+1: m = 2, so the term is c_2 = 0. The sum is 0. For k = 5 the terms (n, m, φ_n(m)) are (1, 9, −1), (4, 6, +1), (6, 2, 0), with sum 0. ∎
    *Sharpness.* For k = 3 the terms are (1, 7, −1), (2, 6, 0), (4, 2, 0), so g_3(22) = −1 (entry 90).
    *Check:* exact for all odd prime powers 5 ≤ k ≤ 1001 (`SF/A46_zero_facts_audit/check.py`, `results.json`).

79. **Parity Dominance Theorem (computer-assisted).** For each odd k ≤ 25 and every allowed d ≥ D_k, E_d ≤ (1 − η_k)O_d, with the constants below. In particular g_k(d) ≠ 0 for every allowed d ≥ D_k.

    | k | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 | 19 | 21 | 23 | 25 |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|
    | N1 | 900 | 900 | 900 | 900 | 900 | 900 | 900 | 1500 | 1500 | 1500 | 1500 | 1500 |
    | block ratio R_k | 0.6025109 | 0.6703845 | 0.7231290 | 0.7680282 | 0.8092646 | 0.8480780 | 0.8860341 | 0.8314560 | 0.8575917 | 0.8834878 | 0.9090546 | 0.9348480 |
    | tail allowance η_t | 10⁻⁶ | 10⁻⁶ | 10⁻⁶ | 10⁻² | 10⁻² | 10⁻² | 5·10⁻² | 10⁻⁶ | 10⁻⁶ | 10⁻⁶ | 10⁻⁶ | 10⁻⁶ |
    | η_k (truncated) | 0.39748 | 0.32961 | 0.27687 | 0.22197 | 0.18073 | 0.14192 | 0.06396 | 0.16854 | 0.14240 | 0.11651 | 0.09094 | 0.06515 |
    | D_k | 5 988 500 | 7 321 266 | 8 890 003 | 9 791 834 | 11 073 024 | 11 836 583 | 12 789 969 | 37 895 709 | 40 987 057 | 42 790 252 | 45 486 986 | 48 035 214 |

    Here η_k = 1 − R_k − η_t, truncated (not rounded) at the fifth decimal.
    *Proof outline.* Write m = (d−n²)/k, α_n = n/√d. All constants are enclosed in interval or ball arithmetic; floating point is used only to choose free parameters.
    - **Local CLT layer.** At r = e^{−u/n}, a_n(m)r^m/A_n(r) is exactly P(S = m) for S = Σ_{odd j≤n} B_j + Σ_{n/2<l≤n} 2l·Geom(e^{−2lu/n}), with independent Bernoulli B_j ∈ {0, j} (entry 74). The inversion bound |P(S=m) − g(m−μ)| ≤ δ/(√(2π)σ), δ = D1 + D2 + D3 (major-arc Taylor remainder, Gaussian tail, minor-arc integral), holds on u-cells uniformly for n ≥ N1 − k, with moments enclosed by a sum lemma. This layer (`clt.py`, `sums.py`) was re-derived from first principles and independently reimplemented with different minor-arc bounds in `SF/A44_oddk_audit/proof/clt_indep.py`; the independent cells give δ no larger than the original ones.
    - **Blocks.** Every even n is charged against ½(o_{n−k} + o_{n+k}); for odd k these neighbours are odd and in the same square class, and each odd n′ is charged by n′ ± k only, with weight ½ each. Interval evaluation over u-boxes of width 0.0025 bounds every block ratio in the saddle window by R_k, with the odd-side factor bounded away from 0.
    - **Tails.** Two-sided Chernoff bounds for log A_n(e^{−u/n}) in terms of Φ1(u) bound all even terms outside the block window by η_t·(a central odd term) for d ≥ D_k = ⌈(N1/α1)²⌉; the margin T(D_k) ≤ 0 and monotonicity in d are verified in ball arithmetic.
    - **Assembly.** Blocks are disjoint, the weights on each odd term sum to ≤ 1, and the central odd term is ≤ O_d, so E_d ≤ R_k·O_d + η_t·O_d ≤ (1 − η_k)·O_d.

    *Certificates.* k = 3..15: `SF/A39_gk_family/proof/` (verify_blocks_k.py, tails_k.py), independently recomputed in `SF/A40_gk_audit/proof/blocks_indep.py` (python-flint arb; bounds ≤ R_k on boxes of width 0.0005) and `SF/A40_gk_audit/proof/tails_indep.py` (closed-form Φ1(u) = [Li2(−e^{−u}) + π²/12 + Li2(e^{−u}) − Li2(e^{−2u})]/(2u); same D_k, all T(D_k) ≤ 0). k = 17..25: `SF/A41_uniform_oddk/proof/`, independently recomputed in `SF/A44_oddk_audit/proof/` (blocks_indep.py with the independent CLT cells of clt_indep.py: R_k(A44) = 0.8305747, 0.8570024, 0.8826329, 0.9080564, 0.9340278 ≤ R_k; tails_A44.py: T(D_k) = −15.29, −15.81, −10.29, −7.51, −7.76 at η_t = 10⁻⁶).

80. **Certificate (finite range and complete zero sets, odd k ≤ 25).** For odd k ≤ 15, every allowed d ≤ 2·10⁷ outside Z_k has g_k(d) ≠ 0; for k = 17..25 the same holds for allowed d ≤ 6·10⁷. Since 2·10⁷ > D_k (k ≤ 15) and 6·10⁷ > D_k (k ≤ 25), Z_k is the finite set computed exactly:

    | k | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 | 19 | 21 | 23 | 25 |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|
    | #Z_k | 9 | 17 | 24 | 20 | 43 | 54 | 55 | 80 | 89 | 88 | 105 | 76 |
    | max Z_k | 43 | 176 | 247 | 118 | 273 | 545 | 565 | 1137 | 766 | 2055 | 837 | 936 |

    Z_3 = {3, 4, 6, 7, 15, 28, 31, 40, 43}.
    *Certificate.* g_k(d) is computed by an exact recurrence modulo the primes 2⁶¹ − 1 and 10¹⁸ + 3 (`SF/A40_gk_audit/cert/gcert.c`, which uses φ_n directly with no sign substitution; k = 17..25 rerun at 6·10⁷ in `SF/A44_oddk_audit/cert/`). A non-zero residue implies g_k(d) ≠ 0. The allowed d that vanish modulo both primes coincide element by element with the exact zero sets computed with Python integers (`SF/A40_gk_audit/exact/eo_indep.py`, d ≤ 3·10⁵), all of which lie far below the exact range (`SF/A40_gk_audit/cert/compare.json`, `SF/A44_oddk_audit/cert/compare.json`).

81. **Corollary.** For every odd k ≤ 25, OccFilt_k(∞) = {squares mod k}, and g_k(d) ≠ 0 for every allowed d > max Z_k.
    *Proof.* Entries 79 and 80; non-allowed classes have g_k(d) = 0.

82. **Certificate (exact range, k = 7).** For every allowed d with 1127 < d ≤ 3·10⁶, O_d > E_d. The last allowed d with E_d ≥ O_d in each class is 1127 (class 0), 407 (class 1), 247 (class 2) and 60 (class 4).
    *Certificate.* `SF/A38_lemmaL/exact/eo_exact.py` computes E_d and O_d as exact Python integers (A_n by exact division ladders, cross-checked against the direct product for n ≤ 30); the comparison is an exact integer comparison.

83. **Theorem (even k: sign classes).** Let k = 2^a k′ with k′ odd and a ≥ 1, and let c be a square mod k. Call the class c ONE if all terms of g_k(d), d ≡ c mod k, have the same sign, and MIX otherwise. Then every root r of r² ≡ c mod k has r ≡ c mod 2, and the class c is MIX if and only if a ≥ 2 and both c mod 2^a and (c mod 2^a) + 2^a are squares mod 2^{a+1}. In particular every class is ONE for k ≡ 2 mod 4, and MIX classes exist for every k ≡ 0 mod 4.
    *Proof.* For even k, n² ≡ c mod k forces n ≡ c mod 2. The sign of the n-th term is (−1)^m with m = (d − n²)/k, and (−1)^m depends only on n² mod 2k. By CRT, n² mod 2k is determined by (n² mod 2^{a+1}, n² mod k′), and the k′-part is fixed by c. Given n² ≡ c₂ := c mod 2^a, n² mod 2^{a+1} ∈ {c₂, c₂ + 2^a}, and square roots mod 2^{a+1} combine freely with roots mod k′. So the class is MIX iff both lifts are squares mod 2^{a+1}. For a = 1 the two lifts are c₂ and c₂ + 2 mod 4, and 2, 3 are non-squares mod 4, so the class is ONE. For a = 2, c₂ = 0 gives the squares 0 and 4 mod 8; for a ≥ 3, every c₂ ≡ 1 mod 8 lifts to two odd residues ≡ 1 mod 8, both squares. ∎ *Check:* brute force for all even k ≤ 400, 0 mismatches (`SF/A44_oddk_audit/analysis/mod4_check.py`).

84. **Theorem (ONE classes have finitely many zeros).** Let k be even and c a ONE class. Let n₀ be the smallest n ≥ 3 with n² ≡ c mod k, L = ⌊n₀/2⌋ + 1 and B_c = n₀² + k(2L(L−1) + 1). Then g_k(d) ≠ 0 for every d ≡ c mod k with d ≥ B_c.
    *Proof.* All terms have one sign, so it suffices that the n₀-term is non-zero. By entry 74, A_{n₀} contains the even parts 2L and 2L + 2 (since n₀/2 < L < L + 1 ≤ n₀ for n₀ ≥ 3) and the odd part 1. Every integer ≥ L(L−1) is a non-negative combination of L and L+1, so every even m ≥ 2L(L−1) is a sum of parts 2L and 2L+2, and every odd m ≥ 2L(L−1) + 1 adds the part 1. Hence a_{n₀}(m) > 0 for m ≥ 2L(L−1) + 1, which covers d ≥ B_c. ∎

    **Corollary (computer-assisted).** For k = 2, 6, 10, 14, every allowed class is ONE (entry 83), so OccFilt_k(∞) = {squares mod k} and Z_k is finite:
    - Z_2 = {2, 8, 10, 26};
    - Z_6 = {3, 6, 12, 18, 21, 24, 30, 46, 48, 78};
    - #Z_10 = 17, max Z_10 = 120; #Z_14 = 30, max Z_14 = 224.

    The same holds class by class for the ONE classes of k = 4, 8 and 12 (their zeros are those listed in `SF/A39_gk_family/REPORT.md` §5 that lie outside the MIX classes 0 mod 4, 1 mod 8, and 0, 4 mod 12). *Certificate:* max B_c = 1778 (k = 14, c = 0), and below B_c the exact integer run to d ≤ 10⁵ decides (`SF/A39_gk_family/exact/one_classes.py`; independently `SF/A40_gk_audit/exact/eo_indep.py`, `even_check.py`).

85. **Theorem (sign rule and the limit coefficients).** For all n, m ≥ 0, (−1)^m φ_n(m) ≥ 0. Let q_odd(m) be the number of partitions of m into distinct odd parts. Then c_m = (−1)^m q_odd(m). Moreover q_odd(m) ≥ 1 for every m ≠ 2 (and q_odd(2) = 0), and q_odd(m) ≥ 2 for every m ≥ 8.
    *Proof.* The first statement is entry 74: (−1)^m φ_n(m) = a_n(m) ≥ 0, with A_n(x) = ∏_{odd j≤n}(1+x^j) · ∏_{n/2<l≤n}(1−x^{2l})^{−1}. Fix m and take n ≥ m. Every factor 1 − x^{2l} with 2l > n ≥ m is ≡ 1 mod x^{m+1}, and odd parts larger than m cannot occur in degree m. So a_n(m) = [x^m] ∏_{odd j}(1+x^j) = q_odd(m). By entry 76, φ_n(m) = c_m for n ≥ m, hence c_m = (−1)^m q_odd(m). For the bounds: q_odd(0) = 1 (empty partition); an odd m has the partition {m}; an even m ≥ 4 has {m−1, 1}; and q_odd(2) = 0. For odd m ≥ 9 the partitions {m} and {1, 3, m−4} are distinct. For even m ≥ 8 the partitions {m−1, 1} and {m−3, 3} are distinct. ∎

86. **Theorem (pair reduction at d = (k+2)² − 3).** Let k ≥ 7 be any integer, d = k² + 4k + 1 and Ξ_k = {s : 1 < s < k/2, s² ≡ 1 mod k}. For s ∈ Ξ_k put t = (s²−1)/k, m₁ = k + 4 − t, m₂ = 4 + 2s − t, A₁ = |φ_s(m₁)| and A₂ = |φ_{k−s}(m₂)|. Then
    g_k(d) = (−1)^k + 1 + Σ_{s∈Ξ_k} [φ_s(m₁) + φ_{k−s}(m₂)].
    - For odd k the leading constant is 0 and each pair contributes (−1)^{t+1}(A₁ − A₂).
    - For even k the leading constant is 2 and each pair contributes (−1)^t (A₁ + A₂).

    *Proof.* Since d < (k+2)², every contributing n has n ≤ k+1, and d ≡ 1 mod k forces n² ≡ 1 mod k. The roots in [0, k+1] are the roots r ∈ (0, k) of r² ≡ 1 together with n = k+1. If r is a root then so is k − r. The value r = k/2 is not a root, because k/2 divides r² and k/2 ∤ 1 for k > 2. So the roots in (0, k) are 1, k−1 and the pairs {s, k−s} with s ∈ Ξ_k. The term n = 1 has m = k+4 and equals φ_1(k+4) = (−1)^k. The term n = k−1 has m = 6 ≤ k−1, so it equals c_6 = 1. The term n = k+1 has m = 2 ≤ k+1, so it equals c_2 = 0 (entry 76). For n = s and n = k−s, m = (d − n²)/k equals m₁ and m₂ respectively. By entry 85, φ_s(m₁) has the sign (−1)^{m₁} = (−1)^{k−t}, and φ_{k−s}(m₂) has the sign (−1)^{m₂} = (−1)^t. For odd k these signs are opposite, and for even k they are equal. ∎
    *Check:* exact integers, every k = 7..130: 0 mismatches against the direct coefficient of g_k.

87. **Theorem (even k at d = (k+2)² − 3).** Let k ≥ 7 be even.
    - (i) If 8 ∤ k, then g_k(d) ≥ 2. In particular g_k(d) = 2 for k = 2p^a (p an odd prime, a ≥ 1, k ≥ 7), where Ξ_k = ∅.
    - (ii) If k = 2^a with a ≥ 3, then g_k(d) = 2 − A₁ − A₂ for the single pair s = k/2 − 1. For k ≥ 16, A₂ ≥ 3 and so g_k(d) ≤ −1. For k = 8, g_8(97) = −3.

    In particular g_k(d) ≠ 0 for every even k ≥ 7 with 8 ∤ k and for every k = 2^a ≥ 8.
    *Proof.* (i) If 8 ∤ k then v₂(k) ∈ {1, 2}. Every s ∈ Ξ_k is odd, so 8 | s² − 1 = tk, and therefore t is even. By entry 86 every pair contributes (A₁ + A₂) ≥ 0, so g_k(d) ≥ 2. If k = 2p^a, the solutions of s² ≡ 1 mod k are s ≡ ±1 mod k, so Ξ_k = ∅ and g_k(d) = 2. (ii) The solutions of s² ≡ 1 mod 2^a are ±1 and ±1 + 2^{a−1}, so Ξ_k = {k/2 − 1}. Here t = k/4 − 1 is odd, and by entry 86 g_k(d) = 2 − A₁ − A₂. Put n₂ = k − s = k/2 + 1 and m₂ = 3k/4 + 3. By entry 74, A₂ = A_{n₂}(m₂) counts pairs (a set of distinct odd parts ≤ n₂, a multiset of even parts in (n₂, 2n₂]) of total size m₂. For k ≥ 16 and o ∈ {1, 3, 5}, the pair ({o}, {m₂ − o}) qualifies: m₂ − o is even and satisfies n₂ < 3k/4 − 2 ≤ m₂ − o ≤ k + 2 = 2n₂. So A₂ ≥ 3. The value g_8(97) = −3 is a direct evaluation. ∎
    *Check:* exact integers for even k = 7..130: g ≥ 2 whenever 8 ∤ k, g = 2 for k = 2p^a, and g < 0 for k = 8, 16, 32, 64, 128 (values −3, −8, −31, −236, −5174).

88. **Theorem (odd k with two distinct prime factors, at d = (k+2)² − 3).** Assume Chern's explicit bound for the coefficients of (q²;q²)²_∞ /((q;q)_∞(q⁴;q⁴)_∞) = Σ Q(n)qⁿ = (−q;q²)_∞, where Q(n) = q_odd(n): S. Chern, J. Number Theory 199 (2019) 168–191 (arXiv:1805.08759), Theorem 1.1 with the explicit error term (3.10) of §3.3 (see Remark 3 there). Let k be odd and s ∈ Ξ_k, with t, m₁, m₂, A₁, A₂ as in entry 86 and u = k − 2s. Then A₁ > A₂, except for (s, k) = (4, 15) and (8, 21), where A₁ = A₂ (= 2 and 6). Consequently, if k is odd with exactly two distinct prime factors, then g_k((k+2)² − 3) ≠ 0 except for k = 15 and k = 21, where it is 0.
    *Proof.* *Consequence.* If k has exactly two distinct prime factors, s² ≡ 1 mod k has four solutions, so Ξ_k = {s} has one element, and g_k(d) = ±(A₁ − A₂) by entry 86. *Inequality.* The ingredients are as follows.
    - **Exact formula.** For m ≤ 2n+1, A_n(m) = Q(m) + (−1)^m Σ_{x=0}^{m−n−1} (−1)^x Q(x). This follows from ∏_{j≤n}(1+x^j)^{−1} = (x;x²)_∞(−x^{n+1};x)_∞, because at most one part ≥ n+1 can occur in degree ≤ 2n+1. Also Q(0) = Q(1) = 1, Q(2) = 0, and Q is non-decreasing from n = 2 on (exact table to n = 35 200, with an analytic argument beyond it).
    - **Root geometry.** u is odd with u ≥ 3, and k | u² − 4 with u² − 4 > 0, so u² ≥ k + 4. Hence m₁ = m₂ + u ≤ u² − 1, u ≥ √(m₁+1), 1.5s + 4 < m₂ ≤ 2s + 3, and 1 ≤ t < s/2.
    - **Lower bound for A₁.** A_s(m) ≥ Q(m) − (m/2) Q(m−s−1). Moreover A_s(m₁) ≥ A_s(m″) whenever D = m₁ − m″ is a sum of even parts from (s, 2s]. For odd s this holds for every even D ≥ s+1; for even s it holds for every even D ≥ s+2 except D = 2s+2.
    - **Upper bound for A₂.** If m₂ ≤ k − s then A₂ = Q(m₂). In general A₂ ≤ Q(m₂) + Q(s).
    - **Finite range.** For all 15 616 pairs (s, k) with k odd, k > 2s, k | s² − 1 and 3 ≤ s ≤ 2500, a lower bound for A₁ exceeds A₂ in exact integer arithmetic for 15 587 of them. The other 29 (all with s ≤ 32) are settled by exact big-integer coefficient extraction, which shows that only (4, 15) and (8, 21) have A₁ ≤ A₂ (both equalities). The exact computation also covers every pair with s ≤ 300, and the minimum of A₁/A₂ over the remaining pairs is 1.7811, at (s, k) = (34, 77) (`SF/A54_proofs2/exact_small.py`; `SF/A58_chern_bound_audit/code/pairs_certify.py`, `exact_range.py`).
    - **Analytic range s ≥ 1127.** Chern's hypotheses hold for m = (1, 2, 4), δ = (−1, 2, −1), Δ₁ = 0, Δ₂ = −1, L = 4. They were checked in exact rational arithmetic. Put x(n) = π√(24n−1)/12, ψ(n) = √6 e^{x(n)}(24n−1)^{−3/4} and M(n) = π(24n−1)^{−1/2} I₁(x(n)). Chern's formula gives |Q(n) − M(n)| ≤ B(n), where B(n) is the explicit error term (3.10) together with the bounds for the terms of index k ≥ 3, k ≢ 2 mod 4. The transcription of B was verified against exact Q(n) for 3 ≤ n ≤ 8000 (and every fifth n up to 35 200) with 0 violations. The elementary Bessel bounds (1 − 3/(4y))e^y/√(2πy) ≤ I₁(y) ≤ e^y/√(2πy) are proved by integration. The ratio B(n)/ψ(n) has a rigorous non-increasing majorant β̄(n) (β̄(300) = 6.6·10⁻³, β̄(1000) = 1.7·10⁻⁶, β̄(6000) = 1.1·10⁻¹⁸), so for n ≥ 300 we get (1 − 3/(4x(n)) − β̄(n))ψ(n) ≤ Q(n) ≤ (1 + β̄(n))ψ(n). *Case 1: m₁ < 5s+8.* Apply the lower bound for A₁ with the argument m₁ − s − 1, and the upper bound for A₂ with ψ(m₂)/ψ(m₁) ≤ e^{−π/√24}(1 − 24√(n_a+1)/(24n_a−1))^{−3/4}, n_a = 1.5s + 4, which is ≤ 0.5364 at s = 1127 and decreases to e^{−π/√24} = 0.5266. The resulting margin is at least 0.0004 at s = 1127, at least 0.0965 at s = 1200 and at least 0.446 at s = 2501, and each constituent is monotone in s. *Case 2: m₁ ≥ 5s+8.* Choose m″ ∈ {4s, …, 4s+3} with m″ ≡ m₁ mod 2 and D = m₁ − m″ ≠ 2s+2. This is always possible, and D ≥ s+5. Then A₁ ≥ Q(4s) − (1.5s+2) Q(3s+2) and A₂ ≤ Q(2s+3), and the margin is at least 0.97 for s ≥ 1127. So A₁ > A₂ for every s ≥ 1127. The threshold s ≥ 1200 is also valid, and 1127 is the least integer for which the rigorous margins are positive. The argument tolerates a uniform relative error in Q of about 5% at s = 1200 and about 30% at s ≥ 2501. The finite range and the analytic range overlap, and together they cover every s ≥ 3. ∎
    *Dependency.* The statement rests on exactly one cited published bound, Chern's explicit error term. (`SF/A54_proofs2/REPORT.md` §2; `SF/A58_chern_bound_audit/REPORT.md` §§1–7.)
    *Check:* the reduction of entry 86 agrees with the direct coefficient of g_k for every odd non-prime-power k ≤ 501 (A58), and A₁ > A₂ holds for every pair of every odd k = 7..130 except the two equalities.

89. **Theorem (uniform zero families d = k² + jk + b², b ∈ {1, 2}).** Let b ∈ {1, 2}, j ∈ Z, d = k² + jk + b², and K = max(j + 3b, 2b + 1, −j). Let k ≥ K be an odd prime power. Then
    g_k(d) = φ_b(k + j) + [j ≥ −2b]·c_{j+2b} + [j ≥ 2b]·c_{j−2b},
    and g_k(d) = 0 exactly in the following cases.
    - **b = 1:** j ∈ {−2, −1, 1, 4}, for all odd prime powers k. These are d = (k−1)², k² − k + 1, k² + k + 1 and (k+2)² − 3. No other j gives a zero.
    - **b = 2:** for −4 ≤ j ≤ 3, exactly when k lies in the class mod 4 given below; for j ≤ −5, exactly when k lies in the class mod 4 given below; for j ≥ 4, never.

    | j | −4 | −3 | −2 | −1 | 0 | 1 | 2 | 3 | j ≤ −5 | j ≥ 4 |
    |---|---|---|---|---|---|---|---|---|---|---|
    | k mod 4 | 1 | 3 | 1 | 1 | 1 | 3 | 3 | 1 | 1 if j ≡ 1, 2 mod 4; 3 if j ≡ 0, 3 mod 4 | none |

    *Proof.* Write k = p^a with p an odd prime. *Roots.* The congruence n² ≡ b² mod p^a has the solutions n ≡ ±b mod k, because p ∤ 2b means that p cannot divide both n − b and n + b. *Which n occur.* The index n = b occurs, since k + j ≥ 0. The index n = k − b occurs iff d ≥ (k−b)², i.e. iff j ≥ −2b. The index n = k + b occurs iff j ≥ 2b. The index n = 2k − b does not occur, because (2k−b)² − d = k(3k − 4b − j) > 0: for j ≥ 0 use k ≥ j + 3b, and for j < 0 use k ≥ 2b + 1. Also b < k − b, so the indices are distinct. *Values.* The term n = b has m = k + j, with value φ_b(k+j). The term n = k − b has m = j + 2b ≤ k − b, so by entry 76 its value is c_{j+2b}. The term n = k + b has m = j − 2b ≤ k + b, with value c_{j−2b}. This proves the formula. *b = 1.* φ_1(k+j) = (−1)^{j+1} since k is odd. With entry 85, g = (−1)^j [−1 + [j ≥ −2] q_odd(j+2) + [j ≥ 2] q_odd(j−2)]. For j ≤ −3 this is ±1. For j = −2, −1, 1 the bracket is −1 + q_odd(0), −1 + q_odd(1), −1 + q_odd(3), all 0. For j = 0 it is −1 + q_odd(2) = −1. For j = 2, 3 it is −1 + q_odd(j+2) + q_odd(j−2) = 1. For j = 4 it is −1 + q_odd(6) + q_odd(2) = 0. For j ≥ 5 both q_odd(j±2) ≥ 1 by entry 85, so the bracket is ≥ 1. *b = 2.* φ_2(m) = 1, −1, 0, 0 for m ≡ 0, 1, 2, 3 mod 4, because 1/((1+x)(1+x²)) = (1−x)/(1−x⁴). For −4 ≤ j ≤ 3 the zero condition is φ_2(k+j) = −c_{j+4}. This reads: j = −4, c₀ = 1 needs k ≡ 1; j = −3, c₁ = −1 needs k ≡ 3; j = −2, c₂ = 0 needs k − 2 ≡ 2, 3 mod 4, i.e. k ≡ 1 (k odd); j = −1, c₃ = −1 needs k ≡ 1; j = 0, c₄ = 1 needs k ≡ 1; j = 1, c₅ = −1 needs k ≡ 3; j = 2, c₆ = 1 needs k ≡ 3; j = 3, c₇ = −1 needs k ≡ 1. For j ≥ 4, c_{j+4} and c_{j−4} have the same sign and |c_{j+4} + c_{j−4}| ≥ q_odd(j+4) ≥ 2, while |φ_2| ≤ 1. For j ≤ −5 only n = 2 occurs, and φ_2(k+j) = 0 iff k + j ≡ 2, 3 mod 4, which for odd k gives the stated class. ∎
    *Check:* exact integers, every odd prime power 3 ≤ k ≤ 500 with k ≥ K, every j ∈ [−8, 16] and b = 1, 2: 5121 cases, 0 mismatches with the formula (`SF/A55_small_k_exceptions/check_theorem.py`, `check_theorem.out`). The cases j = 2, b = 2 (k ≡ 3 mod 4) and j = 3, b = 2 (k ≡ 1 mod 4) contain the families k² + 2k + 4 and k² + 3k + 4.

90. **Theorem (exact failure sets of three zero families).** Let k be an odd prime power.
    - (i) g_k(k² + 4k + 1) = 0 iff k ≠ 3.
    - (ii) If k ≡ 3 mod 4, then g_k(k² + 2k + 4) = 0 iff k ∉ {3, 7}.
    - (iii) If k ≡ 1 mod 4, then g_k(k² + 3k + 4) = 0 iff k ≠ 5.

    The exceptional values are g_3(22) = −1, g_3(19) = −1, g_7(67) = +1 and g_5(44) = −1. In particular g_k((k+2)² − 3) = 0 for every odd prime power k ≥ 5.
    *Proof.* Entry 89 applies for k ≥ K, where K = 7, 8, 9 for the three families (j, b) = (4, 1), (2, 2), (3, 2). The remaining odd prime powers are k = 3, 5 in (i), k = 3, 7 in (ii) and k = 5 in (iii). Their terms (n, m, φ_n(m)) are exact integer evaluations. (i) k = 3: (1, 7, −1), (2, 6, 0), (4, 2, 0), sum −1. k = 5: (1, 9, −1), (4, 6, +1), (6, 2, 0), sum 0. (ii) k = 3: (1, 6, +1), (2, 5, −1), (4, 1, −1), sum −1; the index n = 4 = 2k − 2 is an additional root of n² ≡ 4 mod 3. k = 7: (2, 9, −1), (5, 6, +2), sum +1. (iii) k = 5: (2, 8, +1), (3, 7, −2), sum −1. ∎
    *Check:* exact integers for all odd prime powers k ≤ 500, and by a two-prime residue test (primes 2⁶¹ − 1 and 10¹⁸ + 3; a non-zero residue proves a non-zero value) for all k ≤ 2000: no other failure (`SF/A55_small_k_exceptions/ext.py`).

91. **Parity Dominance Theorem for k = 27, 29, 31, 33 (computer-assisted).** For each k ∈ {27, 29, 31, 33} and every allowed d ≥ D_k, E_d ≤ (1 − η_k)O_d. In particular (−1)^d g_k(d) = E_d − O_d < 0, so g_k(d) ≠ 0. The constants at N1 = 1500, with tail allowance η_t = 10⁻⁶, are the following.

    | k | 27 | 29 | 31 | 33 |
    |---|---|---|---|---|
    | block ratio R_k | 0.83798 | 0.85970 | 0.88196 | 0.90522 |
    | η_k = 1 − R_k − η_t (truncated) | 0.16202 | 0.14029 | 0.11803 | 0.09478 |
    | largest local-CLT error δ on the blocks used | 0.0553 | 0.0564 | 0.0576 | 0.0590 |
    | D_k | 49 312 289 | 51 557 554 | 53 684 094 | 55 698 896 |
    | tail margin T(D_k) (≤ 0 required) | −27.62 | −26.95 | −26.10 | −25.05 |
    | independent block ratio (re-derived local-CLT layer) | 0.79055 | 0.80677 | 0.82294 | 0.83906 |

    The last row is the block ratio obtained with a local-CLT layer that was derived and implemented independently. It corresponds to 1 − R = 0.2095, 0.1932, 0.1771 and 0.1609, and it confirms the block inequality with more room. With the coarser local-CLT layer of entry 79, the block inequality closes for k = 27 (R = 0.9568) and k = 29 (R = 0.9829), but not for k = 31 and 33 (R = 1.0097 and 1.0377). So the layer of this entry is used for all four values of k.
    *Proof outline.* The structure is that of entry 79, with the following local-CLT layer. For every u-cell of width 0.01 in [0.19, 3.31] (312 cells, per-cell choice of the main-arc cut τ₀) and every n ≥ 1467 = N1 − 33, |√(2π) σ P(S = m) − e^{−(m−μ)²/(2σ²)}| ≤ δ for all integers m, with enclosures of σ²/n³ and μ/n². Here δ = D1 + D2 + D3, a Taylor remainder on the major arc, a Gaussian tail, and a minor-arc integral bounded by Abel summation and Riemann-sum lemmas. All constants are enclosed in 128-bit ball arithmetic. The block ratio is bounded on u-boxes of width 0.0025 in the window [UA, UB] by R_k (for k = 31, 33: UA = 0.52, 0.53 and UB = 2.70, 2.75). The tail step uses a Chernoff bound a_n(m) ≤ A_n(r) r^{−m} and enclosures log A_n(e^{−u/n}) ≥ nΦ₁(u) − ½ log 2 − g(u) and ≤ nΦ₁(u) + log 2 + g(u), with g(u) = −log(1 − e^{−u}). The exponent F(α,u) = αΦ₁(u) + (1−α²)u/(kα) is convex in α, since ∂²F/∂α² = 2u/(kα³) > 0, so its supremum over an α-interval is attained at an endpoint. The central odd term is bounded below by the local CLT at the saddle. The requirement T(D_k) ≤ 0 holds with the values above, together with the monotonicity in d and the bracketing of the saddle u*. Then E_d ≤ (R_k + η_t)O_d for d ≥ D_k. (`SF/A56_A49_audit/proof/`, `SF/A57_gk_31_33/proof/`; independent layer and block step in `SF/A59_clt_rederivation/code/`, `DERIVATION.md`.)
    *Dependencies, stated exactly.*
    - The block step and the local-CLT layer were derived and implemented in `SF/A56_A49_audit`. They were re-derived independently and re-implemented in `SF/A59_clt_rederivation`, which gives the block ratios in the last row of the table.
    - Every analytic step of the local-CLT layer and of the tail step is a proved lemma (entry 102). The tail step has been re-derived and re-implemented independently (entry 101).
    - The finite range d < D_k is the certificate of entry 92.

92. **Certificate (zero sets, k = 27, 29, 31, 33) and corollary.** For every allowed d ≤ 5.4·10⁷ (k = 27, 29) and d ≤ 6·10⁷ (k = 31, 33), a range that exceeds the corresponding D_k of entry 91, g_k(d) is computed by the signed recursion a_n[m] = a_{n−1}[m] − (−1)^n a_n[m−n] modulo two primes (2⁶¹ − 1 together with 10¹⁸ + 3 or with 4 611 686 018 427 387 847). A non-zero residue modulo either prime proves g_k(d) ≠ 0. The d with both residues 0 coincide element by element with the exact zero set computed with GMP integers for d ≤ 2·10⁶, and there is no such d beyond max Z_k. So Z_k is the finite set computed exactly:

    | k | 27 | 29 | 31 | 33 |
    |---|---|---|---|---|
    | #Z_k | 68 | 121 | 127 | 88 |
    | max Z_k | 1375 | 1934 | 1712 | 1587 |

    The exact E/O computation to 2·10⁶ finds no negative a_n(m) (confirming entry 74) and the last allowed d with E_d ≥ O_d is 174 344 (k = 31) and 205 161 (k = 33), far below D_k. (`SF/A49_gk_runs/cert/`, `SF/A56_A49_audit/cert/`, `SF/A57_gk_31_33/cert/`, `exact/`; the zero sets are listed in `SF/A57_gk_31_33/REPORT.md` §5.)
    **Corollary.** For every odd k ≤ 33, OccFilt_k(∞) = {squares mod k}, and g_k(d) ≠ 0 for every allowed d > max Z_k. *Proof.* For k ≤ 25 this is entry 81. For k = 27, 29, 31, 33 combine entries 91 and 92: for d < D_k use the certificate, for d ≥ D_k use Parity Dominance; non-allowed classes have g_k(d) = 0. ∎

## 8. Bridge C at s = 7, exact certificates, and the s-family law spaces

Notation as in section 3. The functions K2, K3, K4 and the space V are those defined there.

93. **Certificate (rank 36 at the 216 rationals).** Let X₂₁₆ be the set of the 216 rationals h/m with 1 ≤ m ≤ 15, 1 ≤ h ≤ 3m and gcd(h, m) = 1 (so |X₂₁₆| = 3·Σ_{m≤15} φ(m)). The 105 × 216 evaluation matrix of the components of K2, K3 and K4 has rank exactly 36 = dim V. In particular the 105 functions are already separated by their values on X₂₁₆.
    *Certificate.* Each G_{α,β}(h/m) is an exact finite mean over a 4m × 4m box with integer phases mod 9800m, so it lies in Z[ζ_{9800m}][1/(4m)²]. Let Lev = lcm_{m≤15}(9800m) = 3 531 528 000. Each value is reduced to F_p with ζ sent to a primitive Lev-th root of unity, for p = 17 657 640 001, 21 189 168 001, 35 315 280 001 and 42 378 336 001 (all ≡ 1 mod Lev). The rank is computed with FLINT nmod_mat and equals 36 at all four primes. Reduction is a ring homomorphism, so the rank in characteristic 0 is ≥ 36. The 12 automorphs of entry 40 give rank ≤ dim V ≤ 36. (`SF/A51_bridgeC_exact/rank216.py`, `rank216.json`.)

94. **Theorem (exact SL₂(Z)-relations on V).** Let M_S and M_T be the matrices of S and T on the basis of the 36 orbit representatives (entries 39 and 40), and let G_S = √35·M_S. Over Q(ζ₉₈₀₀) the following hold exactly: M_T is monomial with unit-root entries; G_S has entries that are sums of e(k/9800); G_S⁴ = 35²·I; (G_S M_T)³ = +√35·G_S²; and G_S²/35 is monomial (a signed permutation). Hence M_S⁴ = I and (M_S M_T)³ = M_S². Since SL₂(Z) = ⟨S, T | S⁴ = 1, (ST)³ = S²⟩, M_S and M_T define an SL₂(Z)-representation on V over Q(ζ₉₈₀₀).
    *Certificate.* All computations are in Z[ζ₉₈₀₀] reduced modulo Φ₉₈₀₀ (degree 3360) with integer coefficients, in all 1296 entries of each identity. Here √35 = −i·Σ_a (a/35) ζ₃₅^a (35 ≡ 3 mod 4); it satisfies (√35)² = 35 exactly and has numerical value +5.91608, so it is the positive root. The identity with −√35 in place of +√35 fails. (`SF/A51_bridgeC_exact/sl2_exact.py`, `sl2_exact.json`.)

95. **Certificate (T-spectra).** spec(T|C) = {19, 31, 59, 111, 131, 139}/140 (mod 1) and spec(T|E) consists of 36 distinct values. The six values of spec(T|C) all lie in spec(T|E), and spec(T|V) = spec(T|E). Hence ρ₇|W has 36 distinct T-eigenvalues, six of them doubled, and T alone does not separate C from E; the separation is by S (entry 32).
    *Certificate.* The exact T-exponents on ρ₇|W (exponents mod 29 400) are read from the construction of `SF/A32_35_to_rho7`. Each 1- or 2-cycle of the monomial T gives the eigenvalues e(s/2) and e(s/2 + ½). (`SF/A51_bridgeC_exact/sl2_exact.json`.)

96. **Certificate (dimension of the law spaces V_s).** For odd s let A_s = [[2, s], [s, s]], n = s(s−2), a_s = (s/(2(s−2)), −1/(s−2)) and D_s = A_s⁻¹Z²/Z² (of order n). Let V_s be the span of the 3n functions K2_μ, K3_μ, K4_μ of section 3, built from A_s and a_s. Let G be as in entry 14. Then dim V_s = 3·G(n) for s ∈ {5, 7, 9, 11, 13, 19, 25}:

    | s | 5 | 7 | 9 | 11 | 13 | 19 | 25 |
    |---|---|---|---|---|---|---|---|
    | n | 15 | 35 | 63 | 99 | 143 | 323 | 575 |
    | 3·G(n) | 18 | 36 | 60 | 90 | 126 | 270 | 468 |
    | evaluation points used | 18 | 54 | 84 | 96 | 138 | 288 | 516 |

    *Certificate.* *Upper bound:* the number of orbit representatives of the symbols under the automorphs of A_s with entries of absolute value ≤ 40 (entries 37 and 40) equals 3·G(n) at each of these s. *Lower bound:* the exact mod-p rank of the evaluation matrix of the orbit representatives at the points x = h/m, m = 1, …, 24 reaches 3·G(n) at two primes ≡ 1 mod L·lcm(1..24), using the number of points listed in the last row. Reduction can only lower a rank, so the rank in characteristic 0 is ≥ 3·G(n). (`SF/A53_RTA_maps/scripts/lib53.py`, `map2.py`; `data/map2_s*.json`.)

97. **Theorem (Hom vanishing and End for V_s, certificate).** Assume that the T-law and S-law of entry 39 hold for A_s (for s = 7 this is entry 39; for the other s, the Poisson-summation proof of entry 39 applies with 35 replaced by n = s(s−2)), so that V_s is stable under S and T. Let W_s, E_s, C_s be the label representation, E_s = ρ_s-span(δ₀) and C_s = W_s ⊖ E_s of entries 1–8, with (dim W_s, dim E_s, dim C_s) = (20, 18, 2), (42, 36, 6), (72, 60, 12), (110, 90, 20), (156, 126, 30), (342, 270, 72), (600, 468, 132) at s = 5, 7, 9, 11, 13, 19, 25. For each of these s and every k ∈ Z/12:
    - Hom_{SL₂(Z)}(V_s ⊗ χᵏ, C_s) = Hom_{SL₂(Z)}(C_s, V_s ⊗ χᵏ) = 0;
    - Hom_{SL₂(Z)}(V_s ⊗ χᵏ, E_s) = 0 for k ≠ 0.

    Moreover dim End_{SL₂(Z)}(V_s) = 1 at s = 5, 7, 13, 19. So at these s, V_s is indecomposable as an SL₂(Z)-module, and it is irreducible whenever it is completely reducible (at s = 7, V ≅ E is irreducible by entries 32 and 41).
    *Certificate.* The equations XS₁ = S₂X and XT₁ = T₂X are solved over F_p with ζ sent to a primitive root of unity of the order of the T-exponents, for a prime p between 10⁸ and 2³¹. The matrices of S and T on the certified basis of V_s are the exact closed forms of the symbol calculus, reduced mod p, and the same square root of n is used for V_s and W_s. Both orientations of the V_s matrices give identical numbers. Each mod-p dimension is an upper bound for the dimension in characteristic 0, so a computed 0 is exact. The computed End(V_s) is 1 at s = 5, 7, 13, 19 and 2 at s = 9, 11, 25, and the identity is an element of End(V_s), so the value 1 is exact. The case s = 7 reproduces entry 41. (`SF/A53_RTA_maps/scripts/hom53.py`, `stagec.py`; `data/map2_s*.json`.)

## 9. T3 and residual packaging

T3 is as in section 4: T3(3k) = k, T3(3k+1) = 4k+2, T3(3k+2) = 2k+1. `BR/` = `reports/bridges/CRYPTO_RNT_RTA/`.

98. **Theorem (equitable 8-partition of 539).** Let 539 = a₁ + … + a₈ with positive integers aᵢ and max aᵢ − min aᵢ ≤ 1. Then the multiset {aᵢ} is {68, 68, 68, 67, 67, 67, 67, 67}. In particular 3·68 + 5·67 = 539, and the block sizes of the equitable fibre partition of the residual core are determined by 539 and the number of blocks 8.
    *Proof.* Let q = min aᵢ. Every aᵢ lies in {q, q+1}. Let b be the number of aᵢ equal to q+1. If b = 8, all parts equal q+1 and 8 | 539, which is false because 539 = 8·67 + 3. So 0 ≤ b ≤ 7 and 539 = 8q + b. By uniqueness of division with remainder, q = 67 and b = 3. ∎
    *Dependency.* None. The same statement appears in the RTA manuscript (Definition 4.1, Propositions 4.2–4.3). The partition is distinct from the window-tower split 18 + 521 (entry 55). (`BR/RESULTS.md`, Proofs P1.)

99. **Theorem (Haar measure is T3-invariant on Z₃).** Extend T3 to the 3-adic integers by T3(3k + r) = k, 4k + 2, 2k + 1 for r = 0, 1, 2 and k ∈ Z₃. Let μ be the Haar probability measure on Z₃. Then:
    - (i) T3 is continuous. Each branch maps r + 3Z₃ bijectively onto Z₃, and μ(T3(A)) = 3μ(A) for every Borel A ⊆ r + 3Z₃.
    - (ii) μ(T3⁻¹(B)) = μ(B) for every Borel B ⊆ Z₃.
    - (iii) The itinerary map ι(n) = (T3ˢ(n) mod 3)_{s≥0} is a homeomorphism Z₃ → {0,1,2}^ℕ with ι∘T3 = shift∘ι. It sends μ to the uniform Bernoulli measure.

    *Proof.* (i) The maps k ↦ k, k ↦ 4k+2 and k ↦ 2k+1 are affine bijections of Z₃ with unit leading coefficient, so they preserve μ. The map k ↦ 3k + r is a bijection Z₃ → r + 3Z₃ that scales μ by 1/3. Composing gives (i); continuity is clear on each clopen class r + 3Z₃.
    (ii) T3⁻¹(B) is the disjoint union, over r, of the branch preimages B_r ⊆ r + 3Z₃. By (i), μ(B_r) = μ(B)/3. Sum over r.
    (iii) Induction on j: the set of n whose itinerary begins with a given word w of length j is one class mod 3ʲ. For j = 1 this is n ≡ w₀ mod 3. For the step, the branch for w₀ is an affine bijection from w₀ + 3Z₃ onto Z₃ that sends classes mod 3ʲ inside w₀ + 3Z₃ to classes mod 3^{j−1}. By induction the remaining prefix of length j−1 fixes T3(n) mod 3^{j−1}, hence fixes n mod 3ʲ. So ι is a bijection that maps each cylinder of length j onto a class mod 3ʲ; both have measure 3^{−j}. Because ι is a continuous bijection between compact Hausdorff spaces, it is a homeomorphism. The identity ι∘T3 = shift∘ι holds by definition. ∎
    *Dependency.* Entry 47 (the finite version mod 3ʲ). This is a statement about T3 alone; it makes no claim about RNT, RTA, g_k or cryptographic security. (`BR/RESULTS.md`, Proofs P2.)

100. **Theorem (equidistribution mod M coprime to 6).** Let M ≥ 1 with gcd(M, 6) = 1, and let L ≥ 1. For n running over Z/3^L M, the residue T3^L(n) mod M is well defined, and it takes each value in Z/M exactly 3^L times.
    *Proof.* First the one-step claim: for N = 3^i M with i ≥ 1, the map n mod N ↦ T3(n) mod N/3 is well defined and exactly 3-to-1. Write n = 3k + r. Replacing n by n + N replaces k by k + N/3, which changes T3(n) by N/3, 4N/3 or 2N/3. Each of these is 0 mod N/3, so the map is well defined. Now fix r. As k runs over Z/(N/3), the maps k ↦ k, 4k + 2, 2k + 1 are bijections of Z/(N/3), because N/3 = 3^{i−1}M is odd and so 2 and 4 are units. So each target value has exactly one preimage for each r. Applying the claim with N = 3^L M, 3^{L−1}M, …, 3M gives a well-defined map Z/3^L M → Z/M that is 3^L-to-1. ∎
    *Remark.* For even M the claim fails at the first step, because 2 is not a unit mod M.
    *Check.* Exact for M = 539 and L = 1, 2, 3 (`BR/scripts/h3.py`, `BR/logs/h3.log`).
    *Dependency.* None. This is a statement about T3 alone. (`BR/RESULTS.md`, Proofs P3.)

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
