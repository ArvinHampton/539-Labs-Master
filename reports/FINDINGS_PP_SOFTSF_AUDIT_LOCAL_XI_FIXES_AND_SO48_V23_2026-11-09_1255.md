# Soft SF FINDINGS: PP audit of two Local files, 2026-11-09 ~12:55 CST (America/Chicago)

**Authority:** Owner DIRECT, relayed by Physicist at ~12:33 CST.
**Scope:** new dated file only. tip 7cddb188 untouched. No CERT.

**Method:** derived by hand. Exact integer checks were run in Python, and nothing was saved apart from this file.

## (1) FINDINGS_LOCAL_XI_FRICKE_W49_GAMMA0_49_PROOF_LOGIC_PP_FIXES_2026-11-09.md (sha 72222fed…)

**Verdict: CONFIRM.** The rollup 9/3/6/0 stands.

### Fix 1 landed (L6, L25)
- C7 no longer cites E7. It now cites LMFDB 49.2.a.a, Cremona 49a1 and Atkin–Lehner 1970.
- The new C7 argument is valid.
  - W(i/7) = −1/(49·i/7) = i/7, so W has a fixed point.
  - For an involution on a genus-1 curve, #Fix = 2 − tr(W|H¹) = 2 − 2ε.
  - Since #Fix > 0, ε = −1 and #Fix = 4.
  - The root number is w = −ε = +1, which is consistent with rank 0. The j-invariant is −3375, consistent with CM by disc −7.

### Fix 2 landed (L6, L12, L27)
- The Fricke involution is now written W_49^Fricke throughout, and DMZ's operator is written W₄₉^DMZ. C9 is now explicitly distinct from C2.

### C10 forced-carrier wording (L30) is correct
- The unrestricted scalar reading is refuted by C7.
- T:316 stands only as a constraint on the vector-valued carrier V.

### Other checks
- **C4:** the cusp widths 1, 49 and 1×6 sum to 56, as they should.
- **C5:** the h = 1 normalizer criterion holds; there are extras only if 4 | N or 9 | N (Conway–Norton).
- **C3:** the normalized form (0, −1/7; 7, 0) is correct.
- No new issues.

## (2) FINDINGS_LOCAL_SO48_V23_LOCAL_DATUM_MATCH_CHECK_2026-11-09.md (sha 2135adfb…)

**Verdict: CONFIRM.** The rollup is 8 PROVED, 1 CONDITIONAL, 4 OPEN and 2 REFUTED.

### Item 7: REFUTED-by-proof, confirmed
- Γ₄₈ is positive-definite, so G(ℝ) = SO(48) is compact.
- So G is ℝ-anisotropic and therefore not ℚ-split.
- "Split SO₄₈ over ℚ" and "G = SO(Γ₄₈⊗ℚ)" are therefore incompatible.

### Item 6: PROVED, split at every finite place
- At an odd prime p, a unimodular rank-48 lattice with disc 1 gives a form with unit diagonal. Its Hasse invariant is trivial, so it is isometric to H²⁴, which has det (−1)²⁴ = 1.
- At ∞, the definite form has Hasse invariant +1, and H²⁴ has (−1)^{C(24,2)} = (−1)^{276} = +1.
- By the product formula, the Hasse invariants then agree at 2 as well.
- Equal dimension, determinant and Hasse invariant give an isometry over ℚ₂. So the form is split at every finite place, including 23.

### Item 11: #OG(24,48)(F₂₃), PROVED and verified exactly
- |SO⁺₄₈(q)| = q⁵⁵²(q²⁴−1)∏_{i=1}^{23}(q^{2i}−1).
- The Siegel parabolic has order |P| = q⁵⁵²∏_{i=1}^{24}(q^i−1).
- In exact integer arithmetic, the index is ∏_{i=1}^{23}(23^i+1).
- Both families together give 2∏ = ∏_{i=0}^{23}(23^i+1). This number has 377 digits, ≈ 1.436×10³⁷⁶, matching Local's value.
- SO⁺ preserves each family, so the index counts one family.

### Item 3: CONDITIONAL, framed correctly
- Spin is simply connected and absolutely almost simple, and it is isotropic at 23 by item 6. So strong approximation with respect to {23} applies (Kneser, Platonov–Rapinchuk Thm 7.12).
- An automorphic π with π₂₃ trivial is then invariant under the image of Spin(𝔸). So it factors through the abelian (spinor-norm) quotient and is one-dimensional.
- The citation is not re-read, so CONDITIONAL is the right label.

### Other items, all verified
- **1:** ρ(D₂₄) = (23, …, 1, 0). The positive half of the Satake parameters is 23^{23..0}.
- **2:** the trivial representation is non-tempered and non-generic. The L-factor has poles at Re s = ±23, …
- **4:** (35/23) = (12/23) = +1, since 9² ≡ 12. (−7/23) = (16/23) = +1, since 4² ≡ 16.
- **8:** the group has exponent 12, so no element has order 16 or 48, and every regular permutation is even. The form is definite, so it is not split.
- **10:** Lie rank and matrix rank are different notions.
- **13:** REFUTED. 212² + 47·212 = 54908 < 54990.25 = 234.5², so θ₁(212) ≈ 234.32. The bound first holds at κ = 213 (55380).

### Labels
- Item 5 is a corpus-search fact. It is sound as reported; I did not re-run the search.
- The OPEN items (9, 12, 14, 15) are undefined, not refuted. Labels are appropriate.

No CERT. REPORTS ONLY.
