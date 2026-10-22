# Category A ledger (revision 1): s-family, Bridge C, T3/budget arithmetic, H3 orbit map

**For:** Arvin Hampton · **Compiled:** 2026-10-22, 10:00 AM CDT · **Revision 1:** 2026-10-22, about 10:30 AM CDT.

**Sources:** every report in `reports/s_family_paths/` (A, A2–A32, RTA_implications, RTA_prereg, RNT_prereg, galois_review, loose_ends) and `reports/SUMMARY_2026-10-21/SUMMARY.md`.

**Rules for this ledger**

- This is a read-only consolidation. Nothing here is upgraded beyond the status the source report (including the referee reports A31 and A32) gives it.
- **Category A** means proved, or exact relative to named imports.
- **Category B** items appear only in the appendix.
- No TPC or RH claims.
- New files only. Nothing was pushed or sent.

**Path shorthand:** `SF/` = `/workspace/quantum-comp/reports/s_family_paths/`.

**Status keys**

- **P** — proved, hand proof.
- **P-rel** — proved relative to named imports.
- **CC** — computer certificate: exact arithmetic or ball arithmetic.
- **IC** — independently checked by a separate referee report.

**Standard imports**

- **TB (trust base of `SF/A`, `SF/A6`).** This means:
  - the manuscript theta lift u has type ρ_s and λ = 1/4;
  - the λ = 1/4 constant-term criterion;
  - Arb/python-flint ball arithmetic;
  - the rounding analysis of `A2/scripts/certify_hybrid.py`.
- **F1–F5 (`SF/A12`).** These are standard Weil-representation facts, including Scheithauer's upper-triangular formula.
- **I1–I5 (`SF/A15`).** These are imports from A11/A12.

---

## Corrections in this revision
Entry numbers below refer to the **original** ledger (65 entries) unless marked "new". This revision has 66 entries.

- **Original entry 7 (odd-prime step)** — restated precisely as a local statement about C[D_p]: E0_p = SL2-span of δ₀ = the even functions, dim (p^e+1)/2; t_p = tr(S | E0_p) defined explicitly (1 / (2/p) / 0), independent of c; only E0 = ⊗E0_p factors, not W or C. Status raised from "not independently reviewed" to P-rel F1–F5, IC by A31. Added the CC extension tr_E S = 0 for all s ≡ 0, 2 mod 8, 8 ≤ s ≤ 74. (Still entry 7.)
- **Original entry 4** — added the scope caveat E = ρ-span(δ₀) (equal to the isotropic-span definition only numerically beyond s = 18), and the note that a = 2 rests on the exact base-class certificates, not on H2 (proved only for a ≥ 3). The "odd-prime part not independently reviewed" line now cites A31. (Still entry 4.)
- **Original entry 61 (35 vs ρ7)** — upgraded from floating point to exact Category A (computer certificate): Hom(ρ35, ρ7|W) = 0 untwisted, also for the dual and for all twists χ^k with k ≠ 3. The implication "no equivariant map exists" was removed; the entry now states that only untwisted maps are excluded. (Now entry 62.)
- **New entry 31 (Bridge C)** — Hom(ρ35 ⊗ χ³, ρ7|W) is 1-dimensional; Φ unique up to scale, monomial with entries ±1, ±e(1/5); image exactly C, kernel 29-dim; C ≅ ρ5⁻ ⊗ ρ7⁻ ⊗ χ³. Category A, exact in cyclotomic arithmetic (A32). The never-built law vector and the float-only |det| = 35 controls are placed in Category B (appendix).
- **Renumbering** — original entries 31–65 are now 32–66 (shift +1); internal cross-references updated. Original entries 1–30 keep their numbers.
- **Editorial** — the section "Corrections recorded across the reports" was removed (original entry 51 now states its corrected reading inline); lettered theorem labels were dropped from original entries 14 and 18; open problems 1 and 4 and the Category B appendix were updated to match.

---

## 1. s-family Weil representation ρ_s (W, E, C = cusp part)

1. **The S-pairing holds for every odd s ≥ 5.** For every odd s ≥ 5, tr_C ρ(S) = 0, so dim C⁺ = dim C⁻ = d_cusp/2. The same holds on W and on E.
    - Status: P (Galois-sign argument, σ(√n) = −√n).
    - Imports: TB, family_s label matrices.
    - Source: `SF/A6_certify/REPORT.md`, `SF/galois_review/REVIEW.md` (G1).
2. **The Galois-sign argument also covers s ≡ 4, 6 mod 8.** It gives tr S = 0 on C, W and E for these s as well. The exact obstruction at s ≡ 0, 2 mod 8 is √n ∈ Q(ζ_{n/2}).
    - Status: P.
    - Source: `SF/galois_review/REVIEW.md` G1, `SF/A6_certify`.
3. **The S-trace vanishes on W for every even s.** For every even s, tr_W S = 0. The proof uses a monomial unitary K_y that anticommutes with S and commutes with γ_s and −1.
    - Status: P, plus an exact check for even s = 6..60.
    - Source: `SF/A8c_Spairing_even/REPORT.md`.
4. **The S-pairing holds uniformly for every s ≡ 0, 2 mod 8.** For every such s, tr_C S = 0 for the original W, E and C. Hence dim C⁺ = dim C⁻ and tr_E S = 0. This closes 34, 42, the ten A10 gaps and the odd-step cases.
    - Status: P-rel. The imports are F1–F5, plus a CC of the 2-adic base classes a = 2, 3, 4.
    - H1 was confirmed independently by A13 and H2 by A14, both with minor expository fixes only. The odd-prime part (entry 7) was independently checked by A31.
    - **The a = 2 case rests on the exact base-class certificates, not on H2.** H2 is proved only for a ≥ 3 (entry 6). For a = 2 the classes (2, 1/4) ⊕ (8, −u/16) have tr = 0 exactly for u ≡ 1 mod 4 (A11 `logs_exact_E0.txt`).
    - **Scope caveat.** Here E means E = ρ-span(δ₀). Its equality with the isotropic-span definition of E (A10) is known only numerically beyond s = 18 (A11), not proved in general. Beyond s = 18 the statement tr_E S = 0 is therefore about ρ-span(δ₀).
    - Source: `SF/A12_H1H2_odd/REPORT.md`, `SF/A13_H1_check`, `SF/A14_H2_check`, `SF/A31_entry7_check/REFEREE.md`.
    - **Combined with entries 1–2, tr_C S = 0 for every s ≥ 5** (P-rel).

5. **H1 (P-stability) holds for all a ≥ 2.** δ_h lies in the δ₀-span, via the explicit word S T^{2^a} S.
    - Status: P-rel F1–F5, and IC by A13.
    - A13 also ran an exact mod-p check (p = 33556993) for a = 2..7 over all 24 classes u mod 8.
    - Source: `SF/A12`, `SF/A13_H1_check/REPORT.md`.
6. **H2 (zero trace on (1−P)E₀) holds for all a ≥ 3.** There is a basis of X indexed by P¹(Z/M), on which S acts monomially and without fixed points.
    - Status: P-rel F1–F5, and IC by A14.
    - A14 notes that the level is lcm(4, M), which is why a = 2 is excluded.
    - Source: `SF/A12`, `SF/A14_H2_check/REPORT.md`.
7. **Odd-prime local step (a local statement about C[D_p]).** Let p be an odd prime, e ≥ 0, and D_p = (Z/p^e, q(x) = c x²/p^e) with c a unit; let ρ_p be its Weil representation.
    - **Span.** E0_p := SL2(Z)-span of δ₀ in C[D_p] equals the space of even functions {f : f(−x) = f(x)}, of dimension (p^e + 1)/2.
    - **Local trace.** Define t_p := tr(S | E0_p) (= ½(tr S + tr SZ)). Then:
        - t_p = 1 if e is even;
        - t_p = (2/p) if e is odd and p ≡ 1 mod 4;
        - t_p = 0 if e is odd and p ≡ 3 mod 4.
    - So t_p = 0 exactly when p^e ≡ 3 mod 4. t_p does not depend on the unit c.
    - **What factors.** Only E0 factors: E0 = ⊗_p E0_p, hence tr_E S = ∏_p t_p. W and C do **not** factor, and the argument does not need them to; C = W ⊖ E0 and tr_C S = tr_W S − tr_E S with tr_W S = 0 from entry 3.
    - Status: P-rel F1–F5; IC by A31 (hand re-derivation, plus an exact check in Z[ζ_{p^e}] for all 53 odd prime powers p^e ≤ 201, each with c a residue and a non-residue: 0 failures).
    - **Extension (CC, A31).** Computed directly on the full discriminant form, tr_E S = 0 exactly for every s ≡ 0, 2 mod 8 with 8 ≤ s ≤ 74 (18 values; exact integer trace via mod-ℓ at two primes with |tr| ≤ dim E < ℓ/2). This cross-checks the certificates of entry 10 and extends them to s = 64, 66, 72, 74.
    - Source: `SF/A12`, `SF/A31_entry7_check/REFEREE.md`, `SF/A31_entry7_check/logs_local_odd.txt`, `SF/A31_entry7_check/logs_global_trE.txt`.

8. **Factorisation and lift lemma.** For even s, the original definitions collapse to C[D]; this is the complex conjugate of the A10 convention, so vanishing transfers.
    - Factorisation: tr_C S = −∏_p t_p.
    - Lift lemma: tr_{P E0_a} S = t_{a−2}.
    - Exact base classes a = 2, 3, 4, including P-stability.
    - Status: P, and CC for the base classes.
    - Source: `SF/A11_induction/REPORT.md`.
9. **Full-space traces.** tr S = tr SZ = 0 on the full space (one-line Gauss-sum argument). The Eisenstein trace factorises as a tensor product of local factors. The local factor vanishes for odd p ≡ 3 mod 4 with exponent 1.
    - Status: P. Several 2-adic and odd local classes are CC.
    - Source: `SF/A10_uniform_Spairing/REPORT.md`.
10. **Early per-s certificates.** tr_C S = 0 and tr_E S = 0 are certified for s = 8, 16, 18, 24, 26, 32, 40, 48, 50, 56, 58, using an invertible anticommuting operator Y = Z − SZS. C = 0 at s = 10.
    - Status: CC (exact mod-p rank).
    - These are now subsumed by entry 4.
    - Source: `SF/A8c`, `SF/A8_Spairing_even`.
11. **ST-balance for even s.** Let R = ST, so R³ = I, and write ω = e^{2πi/3}.
    - For every even s ≥ 6, tr_W R ∈ {0, −ω}, determined by s mod 3: it is −ω iff s ≡ 2 mod 3.
    - tr_E R = −ω exactly under (Exc), and 0 otherwise.
    - (Exc) is: 3 | m−1, a even, u ≡ 1 mod 4, and v_p(M) even for every prime p ≡ 2 mod 3 (notation of A15 §1).
    - Hence tr_C R ∈ {0, −ω}, and the R-multiplicities on C are (k, k, k) or (k+1, k, k+1).
    - Equivalently, 3 | d_cusp ⇔ tr_C R = 0 ⇔ (s ≢ 2 mod 3 or (Exc)).
    - **Behaviour under (Exc):** E is unbalanced while C is balanced. At s = 56, E has multiplicities (187, 186, 187) and C has (84, 84, 84), because tr_W R = −ω cancels tr_E R.
    - Status: P-rel I1–I5, plus two small 2-adic base cases that are CC. IC by A16.
    - A16 recommends restricting the scope to even s; odd s is Category B only (see the appendix).
    - Source: `SF/A15_ST_balance/REPORT.md`, `SF/A16_ST_check/REPORT.md`.
12. **The tr_W R formula is exactly confirmed for 198 values of s.** The Gauss-sum formula for tr_W R ∈ Z[ω] equals the exact value for every even s from 6 to 400. The check uses exact phase histograms evaluated at 40 digits and rounded into the lattice Z[ω].
    - Status: CC.
    - Source: `SF/A15`.
13. **Local formulas behind tr_W R.**
    - γ_s splits the discriminant form D. The argument is (1/(m−1))Z² ∩ (1/p^k)Z² = Z², with the wording fixed in A16.
    - Odd p: r_p = ½ a_p(1 + κ_p), so r_p ≠ 0 iff χ₋₃(p^e) = 1, and r_3 is never 0.
    - The mod-3 case analysis (3 ∤ M; 3 | m; 3 | m−1) is complete.
    - The W multiplicity counts mod p equal the true counts, because R³ = I is diagonalisable mod p for p ∤ 3.
    - Status: P-rel I5, IC by A16.
    - Source: `SF/A15`, `SF/A16`.
14. **Closed forms for d_cusp, at formula level.**
    - Lemma: for odd m, G(m) ≤ (m+1)/2, with equality iff m is 1 or a prime power.
    - Odd s ≥ 5: d_cusp ≥ (s−1)(s−3)/4 > 0.
    - d_cusp = 0 ⇔ s ∈ {6, 8, 10}.
    - d_cusp is even for every s ≥ 5. For odd s this is independently re-proved by entry 1.
    - **Scope:** these are statements about the closed forms. They describe the true d_cusp only where the closed forms are themselves proved:
        - dim V = s(s−1) is proved for odd s ≤ 51;
        - d₂(k, v) is proved for k ≤ 6.
    - Status: P (formula level).
    - Source: `SF/A/REPORT.md`.
15. **Distribution of r = d_cusp/dim V (odd s, formula level).** The limit law of r is the point mass at 1. It exists but is not continuous. The bounded part has a continuous limit law. The source also proves an exact typical rate and an unconditional structure of the limit-point set.
    - Status: P. Some mean bounds cite Shiu and Nair–Tenenbaum and are marked CHECK in the source.
    - Source: `SF/A4_dist/REPORT.md`.
16. **Chen-type results cannot give liminf r = 1/4.** This is a structural obstruction. Whether r is near 1/4 depends only on the number k of prime-power factors; if every prime factor grows, r → 1 − 3/2^k. liminf r = 1/4 is equivalent to infinitely many odd prime-power pairs (s−2, s). Given Chen, liminf r ≤ 5/8.
    - Status: P, and P-rel Chen (1973) for the corollary. Theorem numbers are flagged CHECK in the source.
    - Source: `SF/A3_chen/REPORT.md`.
17. **Isometry-swap theta identity.** An isometry h ∈ SO(A)(Q) with h(S⁺) = S⁻ and Q∘h = Q gives θ(R⁺) = θ(R⁻). This closed dim V(98) = 2406. Also tr(g | Fix N) = 2m.
    - Status: P, at m = 7 / s = 98 only.
    - Source: `SF/galois_review/REVIEW.md` G11.
18. **Gauss-sum vanishing.** |G(h/m)| is given by quadratic Gauss-sum factorisation, and G(h/m) = 0 iff 2‖m or 5 | m.
    - Status: P.
    - Source: `SF/galois_review/REVIEW.md` G6.

## 2. dim S(ρ_s): certified values and bounds
**Setting.** S(ρ_s) is the space of Maass cusp forms of type ρ_s on W, weight 0, λ = 1/4.
- Upper bounds come from `A2/scripts/certify_hybrid.py` (M = 6, Q = 40), unchanged under CORE_FREEZE.
- Lower bounds come from d_cusp > 0 with the λ = 1/4 criterion, or from exact Hecke/T-row determinants.
- Status for every entry in this section: CC relative to TB.

19. **dim = 1** at s = 5, 7, 9, 12, 13 and 14. Source: `SF/A/REPORT.md` §3, `SF/A2/REPORT.md`.
20. **dim = 2** at s = 11 and s = 19. At s = 19 there is one form in each of two sectors. Source: `SF/A2`, `SF/A9_hecke_family/REPORT.md`.
21. **dim = 5 at s = 21.** The lower bounds come from Hecke T′_p images certified in Arb at 256 bits from exact Fourier coefficients, with p = 1597.
    - Additional import TB4: Γ(1596)-invariance via Wohlfahrt.
    - A6 had earlier certified only the bound ≤ 5; A7 closed it.
    - Source: `SF/A7_s21/REPORT.md`.
22. **dim = 3 at s = 23** (`SF/A6_certify`, quoted in the preregistrations) and **dim = 3 at s = 25** (`SF/A9`).
23. **Brackets.**
    - s = 15: 3 ≤ dim ≤ 4.
    - s = 17: 3 ≤ dim ≤ 4.
    - s = 27, 29, 31: dim ≥ 3, with no certified upper bound yet.
    - Source: `SF/A9`.
24. **Hecke commutation lemma.** T′_p F is again of type ρ with the same eigenvalue. It commutes with the sector projectors, and the source gives an explicit coefficient formula.
    - Status: P-rel TB.
    - Source: `SF/A7_s21`.
25. **Sector lemma.** For a P-even sector σ other than all-plus with P_σW ≠ 0, P_σu is a non-zero cusp form of type ρ_s with λ = 1/4.
    - Status: P-rel TB.
    - Source: `SF/A6_certify`.
26. **There is no Riemann–Roch formula for dim S(ρ_s).** Riemann–Roch and the Selberg trace formula give dimensions of holomorphic weight-k spaces, M_k(ρ) − S_{2−k}(ρ*). For a Maass eigenspace at one fixed λ they give only Weyl-law asymptotics, so no RR formula or rigorous bound for dim S(ρ_s) can be produced that way.
    - Status: P (reading of the code plus standard theory).
    - The coincidences between RR₀ and the certified values at s = 7, 12 and 14 are Category B.
    - Source: `SF/A17_dim_formula/REPORT.md`.

## 3. Bridge C at s = 7
Here A = [[2,7],[7,7]], |D| = 35, level 70.

27. **C at s = 7.** C is a 6-dimensional irreducible ρ-module with dim C⁺ = dim C⁻ = 3. Hence there is no 1-dimensional (scalar) cusp-residual law, and every S-eigenvector spans all of C. The constant term c₀ is Eisenstein, so the S-pairing does not constrain it.
    - Status: P-rel TB, A6 (entry 1) and a cited identification.
    - The E_L ↔ u_L identification is Category B by citation, and the implication inherits that status.
    - Source: `SF/RTA_implications/REPORT.md`.
28. **dim S(ρ_7) = 1.**
    - Status: CC.
    - Source: `SF/A/REPORT.md` §3.
29. **Step 0 arithmetic for the controls.** Q(√35) has class number 2, and 6 + √35 is a unit of norm +1. [[2,1],[1,−17]] is odd, so even indefinite controls with det −35 do not exist.
    - Status: P (exact).
    - Source: `SF/RTA_prereg/REPORT.md`.
30. **Equivariant-product facts.**
    - Every Γ-equivariant product C^{⊗a} ⊗ C̄^{⊗b} → C is automatically Z/3-graded by R-degree.
    - If no T-exponents satisfy a + b + c − d ≡ 0 mod 1, then Hom_Γ(C⊗C⊗C, C) = 0.
    - The products x⟨z,y⟩ and z⟨x,y⟩ exist for every irreducible unitary representation.
    - Status: P (elementary).
    - Source: `SF/A18_RTA_foundation/REPORT.md`.

31. **An explicit intertwiner ρ₃₅ ⊗ χ³ → ρ_7|W.** Here ρ₃₅ is the Weil representation of the order-35 discriminant form D(A_7), and χ³(T) = χ³(S) = i.
    - dim Hom(ρ₃₅ ⊗ χ³, ρ_7|W) = 1. The map Φ is unique up to scale.
    - Φ is monomial, with all non-zero entries (after rescaling) in {±1, ±e(1/5)}.
    - Its image is exactly the 6-dimensional cusp part C; its kernel is 29-dimensional.
    - Hence C ≅ ρ₅⁻ ⊗ ρ₇⁻ ⊗ χ³, where ρ₅⁻ ⊗ ρ₇⁻ is the sector of ρ₃₅ odd under both local reflections.
    - Status: **Category A** — verified exactly in cyclotomic arithmetic (Z[ζ_29400]) on the generators S and T (210/210 and 24/24 entries agree), with the upper bound dim ≤ 1 from the mod-p certificate of entry 62.
    - **Not claimed (Category B, see appendix):** no law vector for the 35-component law has ever been built, so nothing is transported by Φ; the appearance of the same χ³ map for other |det| = 35 lattices is float-only.
    - Source: `SF/A32_35_to_rho7/REPORT.md`, `SF/A32_35_to_rho7/exact_verify.json`.

## 4. T3 and budget arithmetic
T3(n) is n/3 for n ≡ 0, (4n+2)/3 for n ≡ 1, and (2n+1)/3 for n ≡ 2 (mod 3), using the integer form of A20. σ(n) is the number of steps to reach 1.

32. **T3 is integer-valued in its corrected form.** As literally written, (2n+1)/3 at n ≡ 2 is not an integer; for example T3(2) = 5/3. Status: P. Source: `SF/A20`, `SF/A25`.
33. **3-power shift.** σ(3ᵏm) = k + σ(m), and σ(3ᵏ) = k. Status: P. Source: `SF/A23`, `SF/A24`.
34. **End-state parity with budget 539.** If σ(n) ≤ 539, then T3^{539}(n) = 1 when σ(n) is odd and 2 when σ(n) is even. For example, 4880 has σ = 14 and ends at 2.
    - Status: P.
    - Source: `SF/A23_axiom01_revised/REPORT.md`.
35. **End-state parity with budget 540.** If σ(n) ≤ 540, then T3^{540}(n) = 1 iff σ(n) is even. 4880 ends at 1. Over n ≤ 10⁶, 504 899 seeds end at 1 and 495 101 at 2.
    - Status: P, with a direct check for n ≤ 20 000.
    - Source: `SF/A30_540_thermo`.
36. **Residue words are 3-adic digits.** For every j ≥ 1, the map n mod 3ʲ ↦ (T3ˢ(n) mod 3)_{s<j} is a bijection from Z/3ʲ onto the words of length j over {0, 1, 2}.
    - Status: P (induction), exhaustive for j ≤ 8.
    - Source: `SF/A29_patterns_all/REPORT.md`.
37. **No map on Z/9 is induced** by T3 on residue classes. This is a direct consequence of entry 36, since the next residue depends on n mod 3ʲ⁺¹. Status: P. Source: `SF/A29`.
38. **Inverse branches and growth bound.** The source lists the T3 preimages of each m (case check). It also proves T3(n) + 2 ≤ (4/3)(n + 2), with equality iff n ≡ 1 mod 3. Status: P. Source: `SF/A24_threshold_1e18`.
39. **The packaging identity for the budget B′ = 539.** B′ = ⌊(N_flux − f_max)/9⌋ = ⌊(4880 − 21)/9⌋ = 539. This is a budget, consistent with T3's short orbits, not a termination time.
    - Status: P.
    - Source: `SF/A20`, `SF/A23`.
40. **N_flux = ⌊3⁵e³⌋ = 4880.** Note that ⌊35e³⌋ = 702. Status: P. Source: `SF/A19`, `SF/A25`.
41. **540 and its 539.9 identities.**
    - 540 = 2²·3³·5 = 4860/9.
    - ⌊(4880 − f)/9⌋ = 540 exactly for f = 12..20.
    - The super-harmonics are 540·{2, 3, 4, 5, 10}.
    - 539.9 = 540(1 − 1/5400).
    - **5399 is prime**, so e^{2πi/539.9} = e^{2πi·10/5399} is a primitive 5399th root of unity, and its 539th power is not 1.
    - The beat period of 540 against 539.9 is 2 915 460.
    - Status: P.
    - Source: `SF/A25`, `SF/A30`.
42. **Smallest seed with σ = 539.** Write m₅₃₉ for the smallest n with σ(n) = 539.
    - Bounds: 10⁷ < m₅₃₉ ≤ 788 638 819 521 764 360 564 859 602 047 870 ≈ 7.886×10³². The upper bound is a witness whose σ = 539 was verified.
    - Every depth d ≤ 291 has a seed below 10¹⁸. X₂₉₁ = 666 954 248 808 172 552 has σ = 291.
    - Status: CC.
    - Source: `SF/A24`.
43. **Exact counts.**
    - max σ on [1, 20 000] is 53, at n = 16261. The "54" in RTA Remark 2.6 is σ + 1, a count of states.
    - max σ on [1, 50 000] is 55, at n = 36043 and 36592.
    - σ(4880) = 14, σ(10¹⁸) = σ(10¹⁸ + 1) = 92, σ(3^539) = 539.
    - Every n ≤ 10⁷ resolves within 539 steps. 3^540 does not, and T3^{539}(3^540) = 3.
    - Status: CC (exact).
    - Source: `SF/A19`, `SF/A20`, `SF/A23`, `SF/A28`.
44. **Exact identities checked in the chats.**
    - φ⁷ = (29 + 13√5)/2.
    - 1001 = 7·11·13.
    - 18 + 1 + 520 = 539.
    - 243 − 244 + 55 = 54.
    - 4·8 + 5·12 = 92.
    - 4·122 = 488.
    - Status: P.
    - Source: `SF/A25`.
45. **Lifting T3 cannot change the step count.** Any lift in which the integer coordinate evolves by T3, with steps counted one-to-one, has exactly the shadow step count.
    - Status: P.
    - Source: `SF/A20_T3_bulk_vs_shadow`.

## 5. The H3 orbit map
Φ(n) = Σ_{s<539} w(r_s(n)) ∈ ⟨c⟩ ≅ Z/N.

46. **Well-definedness.** Φ is well defined for every n ≥ 1, including unresolved seeds such as 3^540. Status: P. Source: `SF/A28_H3_map_construction/REPORT.md`.
47. **Cocycle law.** S_{k+l}(n) = S_k(n) + S_l(T3ᵏn). So w induces a monoid homomorphism {0,1,2}* → Z/N. Status: P. Source: `SF/A28`.
48. **Tail formula.** If σ(n) ≤ 539 and L = 539 − σ, then Φ(n) = S_σ(n) + ⌈L/2⌉w(1) + ⌊L/2⌋w(2).
    - Status: P, and exact on 301 seeds × 9 arms.
    - Source: `SF/A28`.
49. **Φ depends only on N.** Changing the generator multiplies Φ by a unit, which preserves Φ = 0, τ and the order. M_A and M_B (with Z/N coefficients) give identical values. No geometry beyond the order N enters.
    - Status: P.
    - Source: `SF/A28`.
50. **Topology of the two candidate manifolds.**
    - On M_A, Tors H³(M_A; Z) = Z/N, and there is no self-linking on H³ in dimension 7.
    - On M_B = L⁷(N), H³(M_B; Z) = 0 and H³(M_B; Z/N) = Z/N.
    - Status: P (standard).
    - Source: `SF/A28`.
51. **Twisted-operator conditions.** Let T = d + (ζ(t) − 1)H₃∧. Then T² = 0 ⇔ dt∧H₃ = 0 and dH₃ = 0.
    - A torsion class has no non-zero de Rham representative.
    - On M_A, H₃ is exact and T = e^{−fB} ∘ d ∘ e^{fB}. So the twisted cohomology is isomorphic to de Rham cohomology: the operator is conjugate to d.
    - Status: P.
    - Source: `SF/A25`, `SF/A28`.

## 6. Negative Category A results (refuted claims, with exact counterexamples)
- These are kept because they are exact. They refute claims; they do not establish any framework content.
- Unless noted, the status is P or CC as stated.

52. **"C3 = T3 terminates in exactly 539 steps" is refuted.**
    - For n ≤ 20 000, orbits finish in ≤ 53 steps, and 4880 takes 14.
    - Read instead as a 539-round budget (T3^{539}(n)), the axiom is a consistent definition and σ = 539 does occur (e.g. 3^539, entry 43); only "terminates in exactly 539" is refuted.
    - Source: `SF/A19`, `SF/A23`.
53. **"Every seed terminates within 539 rounds" is false.** The counterexample is 3^540, which has σ = 540. Source: `SF/A23`.
54. **The threshold reading "σ(n) = 539 for all n ≥ 10¹⁸" is false.** Every 3ᵏ with 38 ≤ k ≠ 539 is a counterexample, and none of the 102 000+ seeds tested has σ = 539. Source: `SF/A24`.
55. **"N_flux = ⌊35e³⌋ = 4880" is false.** ⌊35e³⌋ = 702. Source: `SF/A19`.
56. **The chat arithmetic claims are false.**
    - 3·61 + 162 + 223 = 568, not 539.
    - 244 − 18 − 1 = 225, not 520.
    - The alternating sum of the claimed Betti numbers is −162, not −160.
    - That table violates Poincaré duality for a closed oriented 7-manifold, since b₃ = 223 ≠ b₄ = 61.
    - χ/2 + rk with χ = 0 and rk = 3 gives 3, not 6.
    - 3¹⁸ ≪ 10¹⁸.
    - Source: `SF/A25`.
57. **The harmonics are not HQCC-locked to 539.9.** They are exact multiples of 540, not of 539.9. Source: `SF/A19`, `SF/A23`.
58. **The friction-coupled PDE has no claimed periodic attractor when κ_dark ≠ 0.** Source: `SF/A19` (1.6).
59. **The thermodynamic formula does not give 539.9.** T_eff = 540/(1 + 1/540) = 291600/541 = 539.0018.
    - 540/(1 + 0.01·0.185) = 539.0028.
    - 540(1 − 0.0001) = 539.946.
    - Reaching 539.9 needs δ = 540/5399.
    - Source: `SF/A30`.
60. **Phase closure fails.** The phase e^{2πi/539.9} does not close after 539 steps; 539 steps give 5390/5399 of a turn. Source: `SF/A25`, `SF/A28`.
61. **"61 × (539/61) = 539" computes nothing.** It is the identity x·(539/x) = 539, which holds for every x ≠ 0. Source: `SF/A20`.
62. **No untwisted intertwiner between ρ₃₅ and ρ_7|W.** Hom_{SL₂(Z)}(ρ₃₅, ρ_7|W) = 0, in both directions; the same holds for the dual ρ₃₅* and against ρ_7|W*, and for every character twist ρ₃₅ ⊗ χᵏ with k ≠ 3 (χ the generator of Hom(SL₂(Z), C^×) ≅ Z/12).
    - Status: **Category A, CC** — exact mod-p rank certificate at two primes (p = 29 401 and 14 729 401); a mod-p nullity of 0 proves Hom = 0 in characteristic 0.
    - The vanishing is not explained by T-spectra (all 12 T-eigenvalues of ρ₃₅ occur in ρ_7|W); the obstruction is S.
    - **Scope.** This refutes only an *untwisted* map. After the twist χ³ a map does exist (entry 31).
    - Source: `SF/A32_35_to_rho7/REPORT.md`, `SF/A32_35_to_rho7/results.json`.

63. **The label-dilation Galois-sign route gives no sign −1** at s = 8, 10, 16 or 18. Source: `SF/A8c`.
64. **The class-group predictors fail.**
    - The Cl(K_s) predictor fails at s = 9 and 11.
    - The Cl(4n_s) predictor fails at s = 23, 25, 27 and 29.
    - Because the certified dimensions contradict it, the refutation is exact at the certified s.
    - Source: `SF/A5_classgroup`.
65. **E_s is not always exactly balanced under R.** The counterexample is s = 56, where E has multiplicities (187, 186, 187). Source: `SF/A15`.
66. **RTA has no ternary or grading axioms.** It has no arity-3 operation and no identity of associative, Jacobi or Filippov type, so it is not an algebra in the axiomatic sense.
    - Status: P (reading of the sources).
    - Source: `SF/A18`.

---

## Appendix (strictly separate from the ledger above)

### Category B items: numerical or interpretive, not claimed
- **Odd-s ST-balance.** Numerical only; stated as a conjecture.
- **Candidate formula** tr_C(ST) ∈ {0, −ω} beyond what is proved. Also the conjectural closed forms for local factors in A10.
- **Float-scan dimensions:** s = 15: 4, s = 17: 4, s = 27: 4, s = 29: 4, s = 31: 3. Also the RR₀ coincidences and the predictions for s = 16, 18, 20.
- **Bridge C.** The E_L ↔ u_L identification; the 35-component (B3) law vector, which has never been built, and any reading of Φ (entry 31) as transporting a law; the float-only controls in which the same χ³ map appears for other |det| = 35 lattices (A32 `controls.json`); the weight-3 (η⁶) interpretation of χ³; the floating-point S-pairing checks at s = 5, 7, 9, 13; the deferred Hejhal 3+3 prediction.
- **RTA-1 and RNT-1 preregistered tests.** All negative or generic; none survives Holm.
- **A29 patterns.** The modulus leads, all of which are multiples of 3, and a broadband spectral excess at periods ≈ 7–8.6 and ≈ 4.5.
- **A30 tests.** No 540-specific signal.
- **A28.** The H3 map shows no emergence of 539 in any of the 9 arms.
- **A24.** "σ = 539 ⇒ n ≥ 10¹⁸" is supported, but unproved.
- **Physics.** All physical premises: G₄ = 539.9 s, the thermodynamic δ, the 11D bulk/shadow reading, Time, the Two-Time postulate.
- **Mod-ℓ checks.** The rank lower bounds in loose_ends, where agreement at two random primes ℓ is not a proof.

### Open problems
1. Hand proofs of the 2-adic base classes a = 2, 3, 4. Prove E = ρ-span(δ₀) equals the isotropic-span E beyond s = 18.
2. Close dim S(ρ_s) at s = 15 and 17. Obtain upper bounds for s = 27, 29 and 31 (the queue is running). Raise the lower bounds.
3. Find a closed form for Σβ_T on C. Find any rigorous handle on dim S(ρ_s) beyond certificates.
4. Build the B3 law vector, and decide whether it lies in the χ³-twisted sector mapped onto C by entry 31. Prove the other |det| = 35 control cases exactly.
5. Prove or refute ST-balance for odd s.
6. Whether σ > 539 occurs below 10¹⁸. Close the gap 10⁷ < m₅₃₉ ≤ 7.886×10³².
7. A defined bulk rule for C3, if any. None exists in the corpus.
8. Arvin's own 2025-09-19 calculation behind 539 / 539.9, which is not found on the box.
9. Extending the formula-level d_cusp results beyond odd s ≤ 51 and d₂ with k ≤ 6.
