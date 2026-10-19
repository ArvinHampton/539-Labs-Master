> **Master-copy note (added 2026-10-18 at push; report text below is otherwise verbatim).** Local root numbers for the 24 s = 7 cusp characters. Its correction of 'roots of unity' applies to Open_Algebraic_2026-10-18/ section (d). Convention: Cat A = proved or exact (incl. exact finite computation); floating-only/numerical/cited = Cat B. Naming as rev. 5 (W_P = Fix(P); d_Eis; no 'Theorem L' label). See ERRATUM_Rev5_PostPush_2026-10-18.md. No TPC/RH claim; distinct from HQCC termination claims; CORE_FREEZE holds.

# s = 7 cusp characters: local root numbers, product check, Atkin–Lehner / sector-sign comparison
Box time Sun Oct 18 19:26 CDT 2026. Scripts and outputs are in `2026-10-18-AtkinLehner-Local/`. No existing file was edited and nothing was pushed.

## Summary
- **Product check passed for all 24 characters.** ∏_v ε_v (over 𝔭₂, 𝔭₅, 𝔭₇, ∞₁, ∞₂) equals PARI's `lfunrootres` root number to |∏ − W| ≤ 2.7·10⁻⁶³ at 60 digits. It also agrees with `al_s7.json` to its 8 decimals.
  - The local factors are **Cat A**: exact elements of Q(ζ₈₄₀), with |ε_v|² = 1 checked algebraically. The match with W is **Cat B**, because W itself is numerical.
- **Sector signs vs local root numbers: no match (Cat A).**
  - ε_𝔭₅ is never ±1. Its minimal polynomial over Q is not monic (25t¹⁶ − …, 5t⁸ + 6t⁴ + 5), so it is not even a root of unity.
  - ε_𝔭₇ is non-real for 16 of the 24 characters and ±1 for the other 8.
  - ε_p(π_p) = λ_p·ε_𝔭 is never ±1.
  - Every one of these values depends on the character. The sector signs are a constant −1 on the whole sector.
- **What does match, exactly (Cat A on the character side):**
  - Z_p = ψ_𝔭(−1) = ε(ψ_𝔭)·ε(ψ_𝔭⁻¹) = −1 at p = 5, 7, for all 24 characters.
  - Hence S_p² = η_p(−1)·Z_p = ω_{π_p}(−1) = ε_p(π_p)·ε_p(π_p^∨). This gives −1 at 5 and +1 at 7, which is the normalisation-free W² sign.
  - So the sector signs are *products* of local root numbers, not the root numbers themselves.
- **Correction to `2026-10-18-Open-Algebraic.md` (d).** That report calls the global root numbers "non-real roots of unity". They are **not roots of unity**: their minimal polynomials, e.g. 5t⁸ + 6t⁴ + 5, are not monic (exact, Cat A). They do have modulus 1.

## Setup and conventions (cited)
- **Field and characters.**
  - K = Q(√35), O = Z[√35]. 𝔡 = (2√35), with v_𝔭(𝔡) = 2, 1, 1 at 𝔭₂, 𝔭₅, 𝔭₇ (checked in PARI from `nfinit(...).diff`).
  - The characters are the same `bnrinit(bnf,[𝔭₂³𝔭₅𝔭₇,[1,1]],1)` characters as in `al_s7.py` and `cusp_chars.pkl` (from `2026-10-17-cusp-part/`), with cyc = [24,2,2]. The chareval values of (3) reproduce the pickle's.
  - All 24 have conductor 𝔭₂²𝔭₅𝔭₇ and ∞-type [0,0] or [1,1].
- **Additive character.** ψ_K = ψ_Q ∘ Tr_{K/Q}, so ψ_𝔭 = ψ_p ∘ Tr_{K_𝔭/Q_p} has conductor 𝔡_𝔭⁻¹ (n(ψ_𝔭) = v_𝔭(𝔡)).
  - Convention A: ψ_∞(x) = e(x), ψ_p(x) = e(−{x}_p). This is trivial on Q.
  - Convention B is its complex conjugate.
  - Both were run. Each local factor changes by χ_v(−1), and the product was checked to be identical exactly (as Tate's §3.2 dependence on ψ predicts). Tables below use A.
- **Local formulas** (Tate, *Number theoretic background*, Corvallis 1979, §3.2). Equation numbers are omitted; the formulas used are written out here.
  - Ramified χ_v, conductor exponent a, self-dual dx:
    ε(χ_v|·|^{1/2}, ψ_v, dx) = ∫_{c⁻¹O^×} χ_v⁻¹(x)|x|^{−1/2}ψ_v(x)dx = χ_v(c)·N𝔭^{−a/2}·Σ_{u∈(O/𝔭^a)^×} χ_v⁻¹(u)ψ_v(u/c), with v_𝔭(c) = a + n(ψ_v).
  - Real place: ε(sgn^N, e(x)) = i^N.
  - Unramified v (χ_v and ψ_v both unramified): ε = 1. Only 𝔭₂, 𝔭₅, 𝔭₇ and ∞ contribute.
  - Global: ε(½, χ) = ∏_v ε_v (§3.5), compared with PARI `lfunrootres(lfuncreate([bnr,χ]))[3]`.
- **Explicit generators** (PARI `idealstar`):
  - (O/𝔭₂²)^× = ⟨−√35⟩ ≅ Z/2;
  - (O/𝔭₅)^× = ⟨2⟩ ≅ Z/4;
  - (O/𝔭₇)^× = ⟨3⟩ ≅ Z/6.
  - All elements are enumerated as products of the generators and checked distinct, with count N𝔭^a − N𝔭^{a−1}.
- **Local character values.**
  - χ_𝔭(u) = ψ((α))⁻¹, where α comes from `idealchinese` with α ≡ u mod 𝔭^a, α ≡ 1 mod the other modulus primes, and α ≫ 0. All three conditions are asserted in the script.
  - χ_𝔭(c) = ψ(𝔟)⁻¹, where (c) = 𝔭^{a+d}𝔟, c ≡ 1 elsewhere and c ≫ 0. This follows from the reciprocity ∏_w χ_w(c) = 1.
  - The result was checked independent of the choice of c (two choices, exact equality).
- **Exact arithmetic.** Every value is in Q(ζ₈₄₀). √5 is the quadratic Gauss sum and √7 = −i·g₇. |ε|² = 1 was checked as ε·ε̄ = 1 in Q(ζ₈₄₀).

## Table 1: local factors (convention A); k and k+12 have identical local data (exact)
| χ (k,e,1) | ∞-type | ε_𝔭₂ | ε_𝔭₅ | ε_𝔭₇ | ε_∞₁ε_∞₂ | ∏_v ε_v | W (lfunrootres) | max \|∏−W\| |
|---|---|---|---|---|---|---|---|---|
| (1,0,1) & (13,0,1) | [0,0] | e(2/3) | −0.880622+0.473820i | +0.605464−0.795872i | +1 | +0.933454−0.358698i | +0.933454−0.358698i | 1.8e-64 |
| (1,1,1) & (13,1,1) | [1,1] | e(2/3) | −0.880622+0.473820i | +0.605464−0.795872i | −1 | −0.933454+0.358698i | −0.933454+0.358698i | 2.0e-63 |
| (3,0,1) & (15,0,1) | [0,0] | 1 | −0.850651+0.525731i | −1 | +1 | +0.850651−0.525731i | same | 1.5e-64 |
| (3,1,1) & (15,1,1) | [1,1] | 1 | −0.850651+0.525731i | −1 | −1 | −0.850651+0.525731i | same | 1.3e-63 |
| (5,0,1) & (17,0,1) | [0,0] | e(1/3) | +0.029971−0.999551i | +0.605464+0.795872i | +1 | +0.096624+0.995321i | same | 1.1e-64 |
| (5,1,1) & (17,1,1) | [1,1] | e(1/3) | +0.029971−0.999551i | +0.605464+0.795872i | −1 | −0.096624−0.995321i | same | 2.7e-63 |
| (7,0,1) & (19,0,1) | [0,0] | e(2/3) | −0.029971−0.999551i | −0.605464+0.795872i | +1 | +0.096624−0.995321i | same | 1.1e-64 |
| (7,1,1) & (19,1,1) | [1,1] | e(2/3) | −0.029971−0.999551i | −0.605464+0.795872i | −1 | −0.096624+0.995321i | same | 2.7e-63 |
| (9,0,1) & (21,0,1) | [0,0] | 1 | +0.850651+0.525731i | +1 | +1 | +0.850651+0.525731i | same | 1.5e-64 |
| (9,1,1) & (21,1,1) | [1,1] | 1 | +0.850651+0.525731i | +1 | −1 | −0.850651−0.525731i | same | 1.3e-63 |
| (11,0,1) & (23,0,1) | [0,0] | e(1/3) | +0.880622+0.473820i | −0.605464−0.795872i | +1 | +0.933454+0.358698i | same | 1.8e-64 |
| (11,1,1) & (23,1,1) | [1,1] | e(1/3) | +0.880622+0.473820i | −0.605464−0.795872i | −1 | −0.933454−0.358698i | same | 2.0e-63 |

Notes on Table 1:
- ε_𝔭₂ is always a 6th root of unity.
- ε_𝔭₅ is never a root of unity. Its minimal polynomial is 25t¹⁶ − 30t¹² + 11t⁸ − 30t⁴ + 25, or 5t⁸ + 6t⁴ + 5 for k ≡ 3 mod 6.
- ε_𝔭₇ is ±1 for k ≡ 3 mod 6. Otherwise it is a root of 7t⁶ ± 13t³ + 7, which is not a root of unity.
- Exact values are the polynomials in ζ₈₄₀ stored in `local_eps.json`; minimal polynomials are in `minpolys.json`.
- **By-product (Cat A):** [k,0,1] and [k,1,1] have identical finite local factors. Their global root numbers differ exactly by ε_∞ = i·i = −1, which explains the "W(partner) = −W(ψ)" pattern noted earlier (B).

## Table 2: Q-side at 5, 7 (π_p = Ind ψ_𝔭, the local component of the level-19600 form)
The Langlands λ-factors are λ_p = ε(η_p, ψ_p), computed exactly: λ₂ = −i, λ₅ = −1, λ₇ = −i. Check: λ₂λ₅λ₇ = 1 exactly (λ_∞ = 1).
The factors at p are ε_p(π_p) = λ_p·ε_𝔭 (Tate §3.4, inductivity in degree 0).

| χ class (e = 0,1) | ε₅(π₅) | ε₇(π₇) | ψ_𝔭₅(−1) | ψ_𝔭₇(−1) | ω_{π₅}(−1) | ω_{π₇}(−1) | W₂₅² (Atkin–Li) | W₄₉² (Atkin–Li) |
|---|---|---|---|---|---|---|---|---|
| k = 1, 13 | +0.880622−0.473820i | −0.795872−0.605464i | −1 | −1 | −1 | +1 | e(5/6) | −1 |
| k = 3, 15 | +0.850651−0.525731i | +i | −1 | −1 | −1 | +1 | −1 | −1 |
| k = 5, 17 | −0.029971+0.999551i | +0.795872−0.605464i | −1 | −1 | −1 | +1 | e(1/6) | −1 |
| k = 7, 19 | +0.029971+0.999551i | +0.795872+0.605464i | −1 | −1 | −1 | +1 | e(5/6) | −1 |
| k = 9, 21 | −0.850651−0.525731i | −i | −1 | −1 | −1 | +1 | −1 | −1 |
| k = 11, 23 | −0.880622−0.473820i | −0.795872+0.605464i | −1 | −1 | −1 | +1 | e(1/6) | −1 |

How the columns were obtained and checked:
- ω_{π_p}(−1) = η_p(−1)ψ_𝔭(−1). It was checked equal to the p-part of the Dirichlet nebentypus ω(n) = (140/n)·ψ((n)) at −1 (CRT, level 19600).
- Tate's identity ε(ψ_𝔭)ε(ψ_𝔭⁻¹) = ψ_𝔭(−1) was checked exactly, 72/72 (χ⁻¹ = [24−k, e, 1]).
- ε(π_p)ε(π_p^∨) = ω_{π_p}(−1) was checked exactly.
- ψ∘σ = ψ_{k+12} was checked on split primes up to 83 (finite check). This explains the identical local data: 6 Galois orbits per ∞-type.
- The W_Q² column uses Atkin–Li's formula W_Q² = χ_Q(−1)·χ̄_{Q′}(Q), with χ_{Q′}(Q) computed exactly. The formula is applied as cited and was not re-derived. It depends on Atkin–Li's matrix normalisation of W_Q.

## Comparison and categories
1. **Sector sign vs individual local root number: does not match (Cat A).**
   - The (−,−) cusp sector has Z₅ = Z₇ = −1. The exact ε_𝔭₅, ε_𝔭₇, ε₅(π₅) and ε₇(π₇) are non-real, or not ±1, for every character (ε₇(π₇) = ±i at best).
   - They also vary within the sector.
   - Consistent with this, the Atkin–Lehner operators have pseudo-eigenvalues of modulus 1, not ±1. Under the standard local-newform dictionary, λ_{p²}(f) is ε_p(½, π_p) up to a nebentypus-dependent unit.
   - I did **not** compute W_p on the actual forms. That identification is cited, not verified (B/literature).
2. **Z_p = ψ_𝔭(−1) for p = 5, 7 and all 24 characters: matches (Cat A).**
   - The character side is exact.
   - That the sector is spanned by exactly these characters is taken from the earlier reports, not re-proved here.
   - This is natural, since Z_p is multiplication by u_p ≡ −1 at p. Equivalently, Z_p = ε(ψ_𝔭)ε(ψ_𝔭⁻¹).
3. **S_p² on the sector = η_p(−1)Z_p = ω_{π_p}(−1) = ε_p(π_p)ε_p(π_p^∨): matches (Cat A).**
   - The values are −1 at 5 and +1 at 7.
   - This is the normalisation-free form of "W_p ↔ S_p": the product of the pseudo-eigenvalues of f and its W-partner is the local central-character sign.
   - Literal W_{p²}² in Atkin–Li's normalisation carries the extra unit χ̄_{Q′}(Q). For example W₄₉² = −1 ≠ S₇² = +1, and W₂₅² ∈ {e(±1/6), −1}.
   - So S_p = W_{p²} holds only after rescaling W by a fixed unit. This is consistent with the "up to Gauss sum" in the earlier dictionary.

## Not done / caveats
- W_p was not applied to the actual Maass forms numerically (level 19600). The pseudo-eigenvalue ↔ ε_p(π_p) step is from the literature, with its normalising unit not pinned down.
- The global W comes only from PARI's numerical lfunrootres, so the product check is an exact local product matched numerically (60 digits) against W.

## Files (`2026-10-18-AtkinLehner-Local/`)
- `local_eps.py` → `local_eps.json`, `local_eps.log`: Gauss sums, exact ε_v, product check, conventions A/B.
- `compare.py` → `compare.json`, `compare.log`: λ_p, ε_p(π_p), ω(−1), Tate inverse check, Atkin–Li W².
- `minpolys.py` → `minpolys.json`, `minpolys.log`: minimal polynomials and root-of-unity flags.
- `table.py` → `table.md`.
