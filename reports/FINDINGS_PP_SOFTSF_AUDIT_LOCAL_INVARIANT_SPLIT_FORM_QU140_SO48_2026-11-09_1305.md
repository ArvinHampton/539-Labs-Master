# Soft SF FINDINGS: PP audit of Local's invariant split form on ℚ[U(140)] ↪ split SO₄₈(ℚ)

**Files audited.** Both hashes were verified as a MATCH.

- FINDINGS_LOCAL_DERIVE_INVARIANT_SPLIT_FORM_QU140_SO48_2026-11-09.md (sha 0344dc48…)
- ERRATUM_LOCAL_DERIVE_INVARIANT_SPLIT_FORM_QU140_SO48_ITEM1_2026-11-09.md (sha cd62134b…)

**Authority and rules.**

- Authority is OWNER_WRITE_CALL_e9c1dbda (sha 33d25a79…). Physicist relayed the request.
- This is an additive file. Tip 7cddb188 is untouched. No CERT. Nothing was sent outside.

**Method.** Hand derivation, plus an independent Python check. The check rebuilt the 48×48 Gram matrix from U(140) itself (units mod 140) and computed the character-order census.

**Verdict: CONFIRM.** Rollup: PROVED 8, CONDITIONAL 0, OPEN 4, REFUTED 0. LD-1 is a Local-derived definition, so adopting it is the Owner's choice.

| Item | Claim | PP verdict |
|---|---|---|
| 1 (as corrected by the erratum) | B(g,h) = B(1,hg⁻¹). With z = Σ B(1,k)k, B = ε(x z y*). B is symmetric iff z* = z. | **PROVED.** The coefficient of 1 in g z h⁻¹ is z_{hg⁻¹}. Symmetry means z_k = z_{k⁻¹}. The erratum correctly repairs the garbled line 13. For symmetric B the original formula agrees. |
| 2 | B_z(x,x) = (1/48)Σ_χ χ(z)\|χ(x)\|². The signature is (a+2b, 48−a−2b). | **PROVED.** There are 8 real characters, since \|A[2]\| = 8, and 20 conjugate pairs. χ̄(z) = χ(z) is real because z* = z. The Fourier pieces are B-orthogonal, so each real character contributes 1 and each pair contributes 2 with sign sgn χ(z). |
| 3 | The Galois orbit census, and that every sign pattern is realizable over ℚ. | **PROVED.** Computed: d=1 gives 1 orbit, d=2 gives 7, d=3 gives 1, d=4 gives 4, d=6 gives 7 and d=12 gives 4. Character counts are 1, 7, 2, 8, 14 and 16 (total 48). Each d=12 orbit is 2 pairs with values α and α′ in ℚ(√3), so its signs are independent (++ from 1, +− from √3). |
| 4 | z = [−1] gives (ℤ[A],B) ≅ 24H over ℤ, even and unimodular, with signature (24,24). | **PROVED.** −g ≢ g mod 140 for every unit, so the pairing is a perfect matching. Independent rebuild: symmetric, zero diagonal, det = (−1)²⁴ = 1, eigenvalues +1 ×24 and −1 ×24. |
| 5 | det and disc are 1, the Hasse invariant is +1 at every place, and the form is split over ℚ and every ℚ_p. | **PROVED.** The signed disc is (−1)^{1128} = 1. The Hasse invariant comes from 276 pairs (−1,−1)_p, an even number. 24H is hyperbolic, so this is immediate. |
| 6 | A embeds faithfully in SO₄₈(ℚ), split. | **PROVED.** Invariance B(ax,ay) = B(x,y) holds since a* = a⁻¹ and A is abelian; the check returned True for all 48 elements. Every element acts as an even permutation (exponent 12, as in my 12:55 FINDINGS item 8). |
| 7 | The image is unramified (hyperspecial) at 23 and at every p. | **PROVED.** ℤ[A] is even unimodular, so ℤ_p[A] is self-dual and SO is smooth reductive over ℤ_p, including p = 2. Permutations preserve the lattice. |
| 9 | The non-existence alternative fails. | **PROVED** by explicit construction. Labelling note: the rollup says "REFUTED 0" while item 9 says "refuted by counterexample". Both are consistent if no corpus claim asserted non-existence. If one did, it should be counted as REFUTED 1. |
| OPEN ×4 | No π, no Satake datum or ω₂₃, non-uniqueness of z, the relation to Γ₄₈, and the Bridge C operators. | **OPEN.** I agree with all of these. |

**Cross-checks with my earlier audits.**

- The trace form z = 1 gives signature (28,20), which I recomputed here. That matches my 1305 audit item A3.
- So z = [−1] is the right replacement for the plain trace form. Its form Σ a_g a_{−g} is split.
- It is a different ℚ-form from SO(Γ₄₈⊗ℚ), which is compact at ∞. This is consistent with item 7 (REFUTED) of the SO48 v=23 file.

No CERT. REPORTS ONLY.
