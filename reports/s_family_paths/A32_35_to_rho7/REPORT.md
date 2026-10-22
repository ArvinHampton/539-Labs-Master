# A32: The 35-component Weil representation and ρ_7: exact intertwiners and an explicit map

**For:** Arvin Hampton · 2026-10-22, about 10:25 AM CDT.

**Folder:** `reports/s_family_paths/A32_35_to_rho7/`
- Scripts: `exact_hom.py`, `run.py`, `numeric.py`, `exact_verify.py`, `controls.py`.
- Results: `results.json`, `numeric.json`, `exact_verify.json`, `controls.json`, `X_chi3.npy`.

**Ground rules**
- `A/scripts/weil_family.py` and the RTA_prereg runner were imported read-only. The certifier was not touched (CORE_FREEZE), and H_s was not redefined.
- The cert queue was not touched.
- New files only. Nothing was pushed or sent.
- No TPC or RH claims.
- **Cat A** = proved, or exact relative to named imports. **Cat B** = numerical or interpretive.

## Verdict
1. **Exact: no equivariant map without a twist.** Hom_{SL₂(Z)}(ρ₃₅, ρ_7|W) = 0, and the same holds for the dual ρ₃₅*, in both directions and against ρ_7|W*. This is proved by a mod-p rank certificate at two primes (Cat A, computer certificate). It is **not** explained by disjoint T-spectra: all 12 T-eigenvalues of ρ₃₅ occur in ρ_7|W. The obstruction is the S-matrix.
2. **Exact: an explicit map after the order-4 character twist χ³.**
   - **Twist:** χ is the generator of Hom(SL₂(Z), C^×) ≅ Z/12, with χ(T) = e(1/12) and χ(S) = −i. So χ³(T) = i and χ³(S) = i.
   - **Hom dimension:** dim Hom(ρ₃₅⊗χ³, ρ_7|W) = 1.
   - **The map Φ:** it is explicit and monomial, with rank 6 and image exactly the cusp part C. It is verified exactly in Z[ζ_29400] on S and T (Cat A).
   - **Identification:** **C ≅ (ρ₃₅)_{(−,−)} ⊗ χ³**, where (ρ₃₅)_{(−,−)} = ρ₅⁻ ⊗ ρ₇⁻ is the 6-dimensional part that is odd under both local reflections Z₅ and Z₇.
   - **Uniqueness:** this is the only one of the 12 characters that gives a non-zero Hom, and it does so with multiplicity 1. The other non-zero cases are the dual and adjoint forms of the same statement.
3. **Revised ledger entry 61.** The untwisted statement is upgraded from floating point to **exact Cat A (computer certificate)**. The conclusion "no equivariant map" holds only untwisted. Up to the χ³ twist, C is canonically a sector of the 35-component Weil representation.

## 1. What the objects are (sources: RTA_prereg Amendments 1–2, RTA_implications §2, A18 §4)
- **Lattice.** A_7 = [[2,7],[7,7]], with det −35. It is an **odd** lattice.
  - Amendment 1 (Cat A): there is no even binary lattice of det −35, because b² − 4ac = 35 ≡ 3 mod 4 is impossible.
- **D(A_7) and its form.** D(A_7) = L′/L has order 35. Since 35 is odd, b(μ,ν) = μᵀA⁻¹ν mod 1 has a unique quadratic refinement q(μ) = 2⁻¹·b(μ,μ), with 2⁻¹ = 18 mod 35.
- **The 35-dim representation ρ₃₅** is the Weil representation of (D, q):
  - T e_μ = e(q(μ)) e_μ;
  - S e_μ = (ε/√35) Σ_ν e(−b(μ,ν)) e_ν, with **ε = i**.
  - ε is fixed by the SL₂ relations. It is the unique choice at both primes used below, and numerically it is also unique.
- **Group and level.** ρ₃₅ is a representation of SL₂(Z) (S⁴ = 1, (ST)³ = S²). It needs no metaplectic cover. T has exact order 35, so the representation factors through SL₂(Z/35).
- **The "35-component law" (Residual-Law B3).** Its source marks it "Not attempted". **No B3 law vector exists anywhere in the repo** (Amendment 2; A18 §4). So the representation space is the only exact object available, and this report works with it.
- **ρ_7.** This is the s-family representation on the 140 labels (`family_s.py` / `WFam(7)`), restricted to the 42-dimensional subspace W fixed by γ₇ and −1.
  - It is an SL₂(Z) representation, with T of **exact order 140** on W (computed here exactly; not the "level 70" sometimes quoted).
  - W = E ⊕ C, where E is 36-dimensional and C is 6-dimensional.
  - dim End(ρ_7|W) = 2 exactly, and dim End(ρ₃₅) = 4 exactly.
- **Matrices.**
  - ρ₃₅: S and T as above. The labels are listed in `exact_verify.json` (stored as r = adj(A)·m mod 35, so μ = r/(−35)), with their q values.
  - ρ_7|W: the WFam S_row and T_mono rows restricted to W orbit vectors. All phases lie in e(Z/9800), i.e. are 9800th roots of unity, and the normalisation is 1/√35.

## 2. Exact intertwiner computation
- **Method.** Solve XS₁ = S₂X and XT₁ = T₂X in exact arithmetic over F_p, with p ≡ 1 mod 29 400 (= lcm(9800, 140, 12, 8)), and with ζ ↦ a primitive 29 400th root of unity in F_p.
  - √35 and ε are fixed in F_p by the relations: exactly one root of 35 and one ε satisfy them.
  - Both S's carry the same factor 1/√35, so it cancels.
- **Why the mod-p result is a proof of vanishing.** The equations have coefficients in Z[ζ][1/35]. Reduction mod a prime above p is a ring map, so the rank can only drop, and **dim Hom over C ≤ dim over F_p**. A mod-p nullity of 0 therefore proves Hom = 0 in characteristic 0.
  - Two primes were used, p = 29 401 and 14 729 401, with identical results.
- **Scope of the check.** 96 Hom spaces in total: {ρ₃₅, ρ₃₅*} ⊗ χᵏ (k = 0..11) → {ρ_7|W, ρ_7|W*}, in both directions.
- **T-spectra (exact).**
  - ρ₃₅ has eigenvalues e(t), with multiplicities:

    | t | 0 | 1/7 | 2/7 | 4/7 | 2/5 | 3/5 | 6/35 | 19/35 | 24/35 | 26/35 | 31/35 | 34/35 |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|
    | mult. | 1 | 2 | 2 | 2 | 2 | 2 | 4 | 4 | 4 | 4 | 4 | 4 |

  - ρ_7|W has 36 distinct eigenvalues of order dividing 140; the full list is in `results.json`.
  - **Overlap, untwisted:** all 12 eigenvalues of ρ₃₅ occur in ρ_7|W, each with multiplicity 1 there. So the spectrum allows up to 37 matched unknowns, and the vanishing comes from S.
  - **Overlap after χ³:** the shifted values t + 1/4 all occur too.
- **Results.**

| Variant | dim Hom (exact upper bound, two primes) | Status |
|---|---|---|
| ρ₃₅ → ρ_7\|W, and the reverse direction | 0 | **Cat A, = 0** |
| ρ₃₅* → ρ_7\|W, and the reverse direction | 0 | **Cat A, = 0** |
| ρ₃₅, ρ₃₅* → ρ_7\|W* | 0 | **Cat A, = 0** |
| ρ₃₅⊗χᵏ → ρ_7\|W, for k ≠ 3 | 0 | **Cat A, = 0** |
| **ρ₃₅⊗χ³ ↔ ρ_7\|W** | **1** | **Cat A, = 1** (lower bound by the explicit map in §3) |
| ρ₃₅*⊗χ⁹ ↔ ρ_7\|W* | 1 | the complex-conjugate statement |
| all other combinations | 0 | Cat A |

- **Consequences for subspaces.** For the subspaces E and C, every Hom vanishes except χ³ → C, which has dimension 1. This follows because a Hom into a subrep embeds in the Hom into W, and the image in the χ³ case is C (§3).
- **Metaplectic (half-integral η-power) twists.** A genuine character of Mp₂(Z) acts by −1 on the central element S⁴. Both representations here are trivial on S⁴, so all those Hom spaces are 0 (Cat A, one line).
- **Weight-shift twists by η^{2k}.** These are exactly the χᵏ above, and the list is exhaustive: χ generates all 12 characters of SL₂(Z).

## 3. The explicit map (Cat A)
- **Construction.** Φ: ρ₃₅⊗χ³ → ρ_7|W was found in floating point.
  - Its residual is 1.4·10⁻¹⁶, and the gap to the next singular value is 1.05.
  - All 24 non-zero entries have equal modulus, and their phases are exact multiples of 1/29 400.
- **Exact verification.** Rescaled to unit entries, Y was verified **exactly** in the group ring Z[Z/29400], reduced modulo the cyclotomic polynomial Φ₂₉₄₀₀:
  - Y·S₃₅′ = S_7·Y: **210 of 210 entries agree**;
  - Y·T₃₅′ = T_7·Y: **24 of 24 entries agree**.
  - The check uses the unnormalised orbit basis. All six target orbits have size 4, so the normalisation is a single scalar.
  - Generators suffice, so Φ is an SL₂(Z)-intertwiner.
- **Rank and image.** Rank 6: the six image rows have disjoint column supports.
  - The image is spanned by the W-orbit basis vectors with indices 26, 28, 30, 32, 34 and 36.
  - That image is C, because W = E ⊕ C with End = 2, so E and C are the only non-zero proper subreps, and C is the 6-dimensional one.
  - **So C is spanned exactly by six W-orbit vectors.**
- **Kernel (29-dim).** It contains every e_μ with μ in the 5-torsion or the 7-torsion subgroup. These are the 11 labels with q ∈ {0, 1/7, 2/7, 4/7, 2/5, 3/5}, i.e. with a zero local component. The remaining 18 dimensions of the kernel come from the other local-sign sectors on the 24 labels.
- **What Φ does to the 35 components.** The 24 "primitive" labels, those with both local parts non-zero (q ∈ (1/35)Z with denominator 35), map 4-to-1 onto the six C basis vectors. Each row is an orbit {±μ, ±μ′}, where μ′ is μ with one local part negated:

| C row | labels (coefficient) | q |
|---|---|---|
| 26 | [7,23] (+1), [28,12] (+1), [7,33] (−1), [28,2] (−1) | 34/35 |
| 28 | [7,18] (+1), [28,17] (+1), [7,3] (−1), [28,32] (−1) | 24/35 |
| 30 | [7,13] (+1), [28,22] (+1), [7,8] (−1), [28,27] (−1) | 19/35 |
| 32 | [14,11], [21,24] (e(1/5)); [14,31], [21,4] (e(7/10)) | 31/35 |
| 34 | [14,6], [21,29] (e(1/5)); [14,1], [21,34] (e(7/10)) | 26/35 |
| 36 | [14,26], [21,9] (e(1/5)); [14,16], [21,19] (e(7/10)) | 6/35 |

- **Reading the table.** Each row is even under μ ↦ −μ and odd under the local reflection. So the source of Φ is the (Z₅ = −, Z₇ = −) sector ρ₅⁻ ⊗ ρ₇⁻, of dimension 2·3 = 6. This is consistent with A ("for odd s, C lies in the (Z_p = −1)-sectors").
- **Is Φ canonical?** Yes, up to a scalar: Hom is 1-dimensional and both sides are irreducible. It is unique up to scaling once χ³ is fixed.
- **Applying it to the B3 law.** Φ would send any 35-component vector to its (−,−) primitive sector. This **could transport a B3 law vector into C**, but no such vector exists, so nothing is transported here.

## 4. Controls and interpretation (Cat B)
- **Floating-point controls** (`controls.json`, χᵏ for k = 0..11): the same single χ³ hit (or its dual) appears for −[[2,1],[1,18]], the dual of [[2,1],[1,18]], [[5,0],[0,7]], [[3,1],[1,12]] and [[2,1],[1,−17]]. It does **not** appear for ±[[6,1],[1,6]], [[1,0],[0,35]] or [[4,1],[1,9]].
  - **So the map is not specific to A_7.** It exists whenever the local odd parts of the order-35 discriminant form match those of D(A_7) (Cat B: controls in floating point only).
- **Interpretation (Cat B).** χ³ is the multiplier of η⁶ (weight 3). One reading is that C is the doubly-odd sector of the D(A_7) Weil representation, shifted by a weight-3 multiplier. Whether the Residual-Law B3 law, if ever built, lives in this sector is open.

## 5. Status
- **Cat A**
  - The untwisted Hom = 0 results (exact, CC at two primes; one prime suffices).
  - The 12-character exhaustive table.
  - The explicit Φ with its exact Z[ζ] verification, its rank 6 and image C, its kernel, and the component table.
  - C ≅ ρ₅⁻ ⊗ ρ₇⁻ ⊗ χ³.
  - **Inherited imports:**
    - ε = i, from the SL₂ relations (unique mod p; standard Weil-representation theory);
    - WFam's definitions of ρ_7 and W;
    - E being a subrep (RTA_implications), with End = 2 exact by the same mod-p bound plus E, C ≠ 0.
- **Cat B:** the controls, and the physical or "law" reading.
- **Open:** the B3 law vector, which has never been built.
- **Ledger entry 61 (revised):**
  - "Hom(ρ₃₅, ρ_7|W) = Hom(ρ₃₅*, ρ_7|W) = 0" is now **exact (CC)**.
  - **Amendment:** "after the χ³ twist there is a unique (up to scalar) intertwiner Φ, with image C ≅ (ρ₃₅)_{(−,−)} ⊗ χ³, verified exactly". This moves from the negative section to section 3 (Bridge C) as a positive Cat A result.
