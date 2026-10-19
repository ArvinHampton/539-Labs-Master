# ERRATUM — Bridge C Consolidated rev. 5, post-push (2026-10-18)

New file. Pure copy-and-create. The pushed rev. 5 files (`Bridge_C_Consolidated_rev5_2026-10-18/`, `ERRATUM_Consolidated_Rev5_2026-10-18.md`, the U1 ledgers, `Open_Algebraic_2026-10-18/`) are **not** edited, and the rev. 5 PDF is not rebuilt. Read this file together with them.
Convention: Cat A means proved or exact (including exact finite computation); Cat B means floating-point only, numerical, or cited without re-derivation. No TPC/RH claim. Distinct from HQCC termination claims. CORE_FREEZE holds. No lock files altered.
Sources: `Open_Algebraic_Update_2026-10-18/2026-10-18-Open-Algebraic.md` (sections 19:02, 19:16 and 19:37 CDT) and `AtkinLehner_Local_2026-10-18/2026-10-18-AtkinLehner-Local.md`.
Numbering refers to the rev. 5 PDF: Proposition 13.12 = prop:orbit5, 13.13 = prop:psq5, 13.15 = prop:hc5, Theorem 13.16 = thm:s98, §13.8 = sec:rev5misc.

## (a) Proposition 13.13 ("Prime-square sectors", §13.6): old/new pieces are not subrepresentations for odd s

**Diagnosis (Cat A, exact).** For odd s the lattice (Z², A) is odd, so the family's T-action uses q′ = Q + B(·, w_c) (w_c the characteristic vector). The table below counts the order-p elements t of L′/Z²:

| s | p | order-p elements | Q-isotropic | q′-isotropic | B(t, w_c) |
|---|---|---|---|---|---|
| 9 | 3 | 2 | 1 | 0 | 1/3 |
| 11 | 3 | 2 | 1 | 0 | 1/3 |
| 25 | 5 | 4 | 2 | 0 | 1/5, 2/5 |

No order-p subgroup is q′-isotropic, so the translation-averaging projector Π used in `finer.py` (isotropy tested with the untwisted Q in the Δ = L₀′/L₀ model) is **not** ρ-equivariant.

**Replacement wording** (as drafted in the source report):
> The "old/new pieces" in the table are the image and kernel of the translation-averaging projector Π computed in the Δ = L₀′/L₀ orbit model, with isotropy tested for the untwisted form Q. For odd s the lattice is odd and the family's T-action uses q′ = Q + B(·, w_c), for which no order-p isotropic subgroup exists at s = 9, 11, 25 (exact). So **Π is not ρ-equivariant, and the "pieces" are not subrepresentations in general.** At s = 11 the (+,+) sector is irreducible (floating commutant computation), so the 18/72 split is not a decomposition into ρ-pieces. The exact rank statements (every listed subspace has injective lift; the ν₀ coefficient is nonzero on the listed "new" subspaces) remain correct as linear-algebra statements. The phrase "splits each sector into old and new pieces" should read "splits each sector (as a vector space) into the image and kernel of Π", and the open item "irreducibility of the pieces" should be replaced by "irreducibility of the sectors: (+,+) at s = 9 has two irreducible summands (48 + 12); all other sectors at s = 9, 11 are irreducible (floating, Cat B)".

**Status of each part.**
- **Cat A, unchanged:** the exact ranks in the table (9: 12/48/12; 11: 18/72/20; 25: 36/432/132), the injectivity of each listed subspace, and ν₀ ≠ 0 on the listed "new" subspaces and = 0 on the "old" ones. These now hold as linear-algebra statements about im Π and ker Π.
- **Cat B:**
  - At s = 9, the (+,+) sector (dim 60) has commutant 2, i.e. two irreducible summands 48 + 12. The (−,−) sector is irreducible.
  - At s = 11, both (+,+) (dim 90) and (−,−) (dim 20) are irreducible.
  - Evidence: floating commutant and Krylov computations (`commutant_9/11.json`, `krylov_irr_9/11.json`). s = 25 was not completed.
- **Addition to the commentary on Proposition 13.12:** injectivity also follows at s = 11, where the sectors are irreducible (Cat B).
- **s = 98 is unaffected.** For even s the lattice is even and t₀ = (0, 1/m) is genuinely isotropic (Q(t₀) = 1). Theorem 13.16 uses only theta identities, not equivariance of Π.

## (b) Global root numbers at s = 7: modulus 1, but **not** roots of unity (Cat A)

The exact local factors are in Q(ζ₈₄₀). Their product gives each global root number W as an algebraic number with |W| = 1 and a **non-monic** minimal polynomial over Q. Examples:
- 5t⁸ + 6t⁴ + 5 for χ = [3,0,1];
- 90075015625t⁴⁸ − 16784790750t³⁶ + 136399927931t²⁴ − 16784790750t¹² + 90075015625 for χ = [1,0,1].

So W is not a root of unity (`AtkinLehner_Local_2026-10-18/minpolys.json`). The identification with PARI's numerical W is Cat B (60 digits).

**The rev. 5 sentence** (`Bridge_C_Consolidated_rev5_2026-10-18/rev5_sec.tex`, §13.8, line 145) is:
> "The global root numbers are non-real (Category~B, numerical), so the $Z_p$ act by pseudo-eigenvalues of modulus $1$."

It does not say "roots of unity", but it misattributes the pseudo-eigenvalues. It should read:
> "The global root numbers have modulus 1 and are non-real; they are not roots of unity (non-monic minimal polynomials, e.g. 5t⁸+6t⁴+5; Category A for the exact local product, Category B for the match with the numerical W). The Atkin–Lehner operators W_p act by pseudo-eigenvalues of modulus 1; the local reflections Z_p act by ±1 sector signs."

**The pushed `Open_Algebraic_2026-10-18/2026-10-18-Open-Algebraic.md`**, section "(d) s = 7 Atkin–Lehner data", says "Global root numbers … are non-real roots of unity". Read "roots of unity" as wrong: they have modulus 1 but are not roots of unity. `CHANGELOG_rev5.md` and `U1_LEDGER_Open_Algebraic_2026-10-18.md` say only "non-real", which stands.

## (c) Atkin–Lehner (§13.8): "partial/open (blocked)" is replaced by the local computation

| Statement | Status |
|---|---|
| Local root numbers ε_v at 𝔭₂, 𝔭₅, 𝔭₇, ∞ for all 24 cusp characters, exact in Q(ζ₈₄₀) (Tate's local formulas; two additive-character conventions; independent of the auxiliary element c), with \|ε_v\|² = 1 checked algebraically | **A** |
| ∏_v ε_v = global root number W, to ≤ 2.7·10⁻⁶³ against PARI lfunrootres (W is numerical) | **B** |
| ε_𝔭₂ is a 6th root of unity. ε_𝔭₅ is never a root of unity (25t¹⁶ − 30t¹² + 11t⁸ − 30t⁴ + 25, or 5t⁸ + 6t⁴ + 5). ε_𝔭₇ is ±1 for k ≡ 3 mod 6 and otherwise a root of 7t⁶ ± 13t³ + 7. λ₂λ₅λ₇ = 1 | **A** |
| The sector signs are **not** individual local root numbers: ε_𝔭, ε_p(π_p) are never ±1 (ε₇(π₇) = ±i at best) and vary across the sector, whereas the sector sign is constantly −1 | **A** (character side) |
| The sector signs are **products** of local root numbers: Z_p = ψ_𝔭(−1) = ε(ψ_𝔭)ε(ψ_𝔭⁻¹) = −1 at p = 5, 7 for all 24 characters, and S_p² = η_p(−1)Z_p = ω_{π_p}(−1) = ε_p(π_p)ε_p(π_p^∨), which is −1 at 5 and +1 at 7 (the central-character sign) | **A** (character side; that the sector is spanned by these characters is from earlier reports) |
| W_p ↔ S_p holds only up to a fixed unit. Atkin–Li's W_{p²}² = χ_Q(−1)χ̄_{Q′}(Q) gives W₄₉² = −1 ≠ S₇² = +1 and W₂₅² ∈ {e(±1/6), −1}. The normalisation is taken from Atkin–Li and was not re-derived; W_p was not applied to the actual forms | **B** (literature) |
| By-product: [k,0,1] and [k,1,1] have identical finite local factors, so W(partner) = −W exactly via ε_∞ = −1 | **A** (local factors) |

## (d) New Category A results (`Open_Algebraic_Update_2026-10-18/`)

1. **g acts consistently on the old classes for every odd m, including composite m (Cat A).**
   - t₀ = (0, 1/m) ∈ L′ is isotropic of order m. With M_t = Z² + Z·t₀ = Z ⊕ (1/m)Z, we have g·M_t = M_t for all m ≥ 1, by an explicit check on the basis using g and g⁻¹.
   - For composite odd m, t^⊥ = ⟨t₀⟩ in the cyclic m-part. So the span of the g-relations is δ_iso ⊗ X, of dimension m(m−1), for **all odd m**.
   - This removes the hypotheses of Proposition 13.15 ("given g-consistency"; "composite m open").
   - Consequence: dim V(2m²) ≤ (s/2)(s/2+1) − m(m−1) for all odd m.
2. **Extra h-relations at m = 2k²−1: 2, 6, 12 at m = 7, 17, 31 (Cat A, as proved relations, hence upper bounds).**
   - h = (g+I)/(2k) is an isometry with h² = g. M = ∩ h^j M_t:
     - m = 17: ⟨(6,0),(1,1/17)⟩, Gram [[72,216],[216,72]];
     - m = 31: ⟨(8,0),(1,1/31)⟩, Gram [[128,512],[512,128]].
   - The ranks come from exact orbit-sum maps (flint), with h·M = M:

| m | k | s | dim F | rank_g | rank_h | extra | exact upper bound |
|---|---|---|---|---|---|---|---|
| 7 | 2 | 98 | 98 | 56 | 54 | 2 | dim V(98) = 2406 (equality, Thm 13.16) |
| 17 | 3 | 578 | 578 | 306 | 300 | 6 | dim V(578) ≤ 289·290 − 272 − 6 = 83532 |
| 31 | 4 | 1922 | 1922 | 992 | 980 | 12 | dim V(1922) ≤ 961·962 − 930 − 12 = 923540 |

   - m = 7 reproduces the exact Fourier result. Lower bounds (no further relations) at m = 17 and 31 were **not** computed.
   - Rev. 5 said "no number is claimed" for m = 17; this item supersedes that.
3. **Cat B:** the general count extra = k(k−1) at m = 2k²−1 (three data points; tr h = 2k and |det(h∓1)| = 2(k∓1) are exact, but the subquotient C_h needed for a proof was not identified).
