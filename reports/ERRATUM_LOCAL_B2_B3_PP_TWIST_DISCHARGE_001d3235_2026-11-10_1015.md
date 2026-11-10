# ERRATUM (Local-derived) to ADDENDUM_LOCAL_t4407_OA_OB_4A_25PARTS_2026-11-09_2143.md (cda63ef5…) and subsequent Local rollups, applying PP discharge 001d3235. 2026-11-10, written 10:15 CST (America/Chicago)

- **Scope.** Additive. Edits nothing: cda63ef5, Local erratum 2159 (f1dcc954…), ERRATUM2 2207 (076a0782…), ERRATUM 0054 (db96af7f…), and FINDINGS_PP_DISCHARGE_B2_B3_2026-11-10_1012.md (001d3235…) are untouched and are corrected or recorded here by reference. No CERT. No Gemini. Nothing sent outside. Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, checked before and after writing. Jobs s1e (932685), ob_v4_6272_D56 (1045533/1045534), and chain (1015729) were not touched.
- **Source discharge:** FINDINGS_PP_DISCHARGE_B2_B3_2026-11-10_1012.md, sha256 001d3235fb2b5ebc750d372407b58d3d40ee99a3fee71e80e11e26be3aff700d (verified on disk; matches its sidecar).
- **Rule:** OW 3f160803 as amended by 36683379 (a citation alone never makes a claim PROVED). "Resonant algebra" (RTA historical alias only).
- **Attribution.** Local is recording PP's discharge of B2 and B3. Local does not claim an independent Local proof of Theorem TW(r). Shimura 1973 Lemma 3.6 is not used as a proof in this file.
- Nothing is adopted. Bridge C stays PARTIAL. O-b stays OPEN.

## Current Local wording being superseded (quoted, not edited)

From ADDENDUM_LOCAL_t4407_OA_OB_4A_25PARTS_2026-11-09_2143.md (cda63ef5…), §2 items 7–8:

> 7. **B2 is split.**
>    - B2 lemma: CONDITIONAL on twist modularity (Shimura 1973, Lemma 3.6).
>    - B2′ consequence: Ξ's eigensystem is not a twist of K. **PROVED** (5bf1e1dc). CM step: a_p(f) = 0 at inert p (from θ_ψ, PROVED in 5bf1e1dc), so ψ² ∈ {χ₋₂₀, χ₁₄₀} on split primes, and both are non-squares by B1.
> 8. **B3:** CONDITIONAL on the same twist lemma. "Reduces to" means a sufficient reduction only.

From the same file, §4 table: "B2, B3 | CONDITIONAL | twist lemma (Shimura 1973 Lemma 3.6)". B2′ is already listed among the PROVED rows.

From ERRATUM2 2207 §4, still the last Bridge C rollup after ERRATUM 0054 and PP confirm 0058: **47 PROVED / 11 CONDITIONAL / 5 OPEN / 2 REFUTED / 1 PENDING + V₈₄ (66 rows)**, with CONDITIONAL (11) = E9, E11a, 3b-i, 3b-ii(b), N1, 3d, N2, O-a, A4, B2, B3.

Those B2 and B3 grades, the Lemma 3.6 tag, and that 66-row rollup are superseded here. The earlier files are not edited.

## Fix 1. Retag and split B2

Retag B2 from "Shimura 1973 Lemma 3.6" to PP Theorem TW(r) (PP 2026-11-10, 001d3235). Use PP's split, not the unsplit alternative.

**Theorem TW(r) (PP), recorded not re-proved.** For 2 ≤ r ≤ 30: if F ∈ M_{k/2}(Γ₀(4N), χ) with k odd and ψ a primitive Dirichlet character mod r, then F⊗ψ ∈ M_{k/2}(Γ₀(4Nr²), χψ²); cusp forms go to cusp forms. For p ∤ 4Nr and T(p²)F = λ_p F, one has T(p²)(F⊗ψ) = ψ(p)² λ_p (F⊗ψ). That T(p²) algebra was already PP-verified and is not reopened. TW(r) covers primitive ψ only; imprimitive ψ is not covered. The range r = 2…30 was certified on every Schreier generator of Γ₀(4r²) and every unit u (largest: r = 30, 3960 generators). A wrong pairing u′ = ud (in place of ud²) fails at r = 5, so the certificate is not vacuous. (r = 2 has no primitive character and is a check only.) General r stays uncertified except for that finite identity.

Split:

- **B2** (2 ≤ r ≤ 30): **PROVED**, by TW(r) together with the already PP-verified T(p²) eigenvalue algebra. This covers the only instance any Bridge C row uses, which is r = 5 (B3).
- **B2-general** (arbitrary r): **CONDITIONAL [T-twist-general]**. This is not a citation of Lemma 3.6; it is the same argument with the finite certificate uncertified for r > 30.
- **B2′:** **PROVED**, unchanged, and needs no modularity. Not reopened.

## Fix 2. B3, citing TW(5); sufficient reduction only

**B3 is PROVED as a sufficient reduction only.** Cite TW(5). If such a G exists at level 4M — that is, if G ∈ S_{3/2}(Γ₀(4M), χ_D) satisfies T(p²)G = χ₋₄(p) a_p(f) G for p ∤ 4M — then H = G ⊗ ψ₅ lies at level 100M, in S_{3/2}(Γ₀(100M), χ_D χ₅), with the Ξ eigenvalues T(p²)H = a_p(f_Ξ) H for p ∤ 20M. Existence of G is not claimed, and the converse is not claimed. **O-b stays OPEN.**

(Here ψ₅ is either character of order 4 mod 5; it is primitive, and ψ₅² = χ₅. The arithmetic that identifies the eigenvalues with those of Ξ is as in e28e0fbd, recorded by PP: conductor of f⊗χ₋₄ is 784, and with M = 784 one has 100M = 78400.)

## Fix 3. Rollup (PP's split)

- **Before (0054 / PP 0058):** 47 PROVED / 11 CONDITIONAL / 5 OPEN / 2 REFUTED / 1 PENDING + V₈₄ (66 rows).
- **Now, with B2 split into two rows:** **49 PROVED / 10 CONDITIONAL / 5 OPEN / 2 REFUTED / 1 PENDING + V₈₄ (67 rows).**
  - B3 CONDITIONAL → PROVED.
  - New row B2 (2 ≤ r ≤ 30) PROVED.
  - B2-general stays CONDITIONAL [T-twist-general].
- **CONDITIONAL (10):** E9, E11a, 3b-i, 3b-ii(b), N1, 3d, N2, O-a, A4, B2-general.
- **OPEN (5):** O-b, O-c, H₊U, Λ₀, P11.
- **REFUTED (2):** 3b-ii, 2f.
- **PENDING (1):** B5. (The 6272 D=28 joint kernel 0 remains a PROVED sub-result inside that PENDING row, as recorded in 0054; D=56 is still running.)

The unsplit alternative (48/10/5/2/1 + V₈₄, 66 rows) is not used.

## Not regraded

- **T-theta1** (FINDINGS_LOCAL_t4436_T_THETA1_UNARY_THETA_2026-11-10_1010.md, sha256 fff902b4ea0cde17b96b0da60318afe8446f4e209dcc2d24bd26cb78a320dc59), filed 10:10 CST, is still awaiting PP audit. It is not regraded here.
- **t4436 branch tally** stays **63/17/5/9/2**. No later PP file confirms T-theta1 (checked through PP 001d3235 and the other 2026-11-10 PP files on disk).

Local-derived. Erratum only; nothing adopted is implied.
