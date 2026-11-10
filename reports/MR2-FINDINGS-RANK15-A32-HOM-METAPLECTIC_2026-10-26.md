# MR2 FINDINGS — Rank 15 ONLY: A32 Hom + metaplectic Hom vanishings (cite-verify)
- **Status:** Cat A cite-verified (Hom table + metaplectic); stub wording PARTIAL MISMATCH on "lattice automorph" (see §4)
- tip Soft SF LOCK start/end: `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` / same · tip_touched Soft SF NO
- Rank 15 only · Soft SF invent HOLD · Soft SF F3 CLOSED · Opt 1 Weil NOT selected · no tip fold · no invent · Bridge PARTIAL READY NO
- Method: read REPORT.md only; no numerics re-run.

## 1. Source sha
`s_family_paths/A32_35_to_rho7/REPORT.md` sha256 `fc92193b6e19e7b2f15fd97bcd0e00fdcdf5992912bce41f335eb19bb77b773e` — matches stub prefix and CI#26: **YES**.

## 2. Hom table (REPORT §2, Cat A computer certificate, mod-p rank at p=29401 and 14729401; dim_C ≤ dim_Fp)
Scope: 96 Hom spaces = {ρ₃₅, ρ₃₅*}⊗χᵏ (k=0..11) → {ρ₇|W, ρ₇|W*}, both directions.
| Variant | dim | Status |
|---|---|---|
| ρ₃₅ ↔ ρ₇\|W | 0 | Cat A |
| ρ₃₅* ↔ ρ₇\|W | 0 | Cat A |
| ρ₃₅, ρ₃₅* → ρ₇\|W* | 0 | Cat A |
| ρ₃₅⊗χᵏ → ρ₇\|W, k≠3 | 0 | Cat A |
| ρ₃₅⊗χ³ ↔ ρ₇\|W | 1 | Cat A (lower bound = explicit Φ, exact in Z[ζ₂₉₄₀₀]) |
| ρ₃₅*⊗χ⁹ ↔ ρ₇\|W* | 1 | complex-conjugate statement |
| all other combinations | 0 | Cat A |
χ: χ(T)=e(1/12), χ(S)=−i. Vanishing untwisted is from S-matrix, not T-spectrum (all 12 T-eigenvalues of ρ₃₅ occur in ρ₇|W). Subspaces: all Hom into E, C vanish except χ³→C (dim 1).

## 3. Exceptions (non-zero pairs)
Only: ρ₃₅⊗χ³ ↔ ρ₇|W (image C ≅ ρ₅⁻⊗ρ₇⁻⊗χ³) and its conjugate ρ₃₅*⊗χ⁹ ↔ ρ₇|W*; REPORT: "other non-zero cases are the dual and adjoint forms of the same statement". Note stub phrase "Hom(ρ₃₅*⊗χᵏ, ρ₇|W*)" — REPORT's exception for ρ₃₅* vs W* is at k=9, not k=3.

## 4. Metaplectic / central −1 (REPORT §2, Cat A "one line")
A genuine Mp₂(Z) character acts by −1 on central S⁴; ρ₃₅ (SL₂(Z), S⁴=1, no metaplectic cover needed) and ρ₇|W are trivial on S⁴ ⇒ all half-integral η-power twist Hom = 0. Integer η^{2k} twists = χᵏ, exhaustive (χ generates the 12 characters).

## 5. Lattice note (REPORT §1)
A₇ = [[2,7],[7,7]], det −35, **odd**; Amendment 1 (Cat A): no even binary lattice of det −35 (b²−4ac=35≡3 mod 4). |D(A₇)|=35 odd ⇒ unique quadratic refinement q=2⁻¹b(μ,μ), 2⁻¹=18 mod 35; ε=i fixed by SL₂ relations.
**MISMATCH/ABSENT:** REPORT contains no "lattice automorphism" argument and no "lattice/central −1 mismatch" mechanism. The central −1 in REPORT is S⁴ (metaplectic vanish, §4); the oddness of A₇ is used only to justify the unique q and no-cover SL₂(Z) action. Separately W is the subspace fixed by γ₇ and −1 (definition, not a mismatch). Correct stub wording: "odd lattice A₇ (no even det −35 lattice) ⇒ honest SL₂(Z) rep trivial on S⁴ ⇒ metaplectic Hom = 0".

## 6. Cat B (not folded as Cat A)
χ³ = η⁶ multiplier (weight-3) reading of C; floating-point controls (other lattices sharing local odd parts give same χ³ hit). B3 law vector: never built (Open); Φ transports nothing.

## Soft SF risks (≤3)
1. Identifying ρ₇|W / C with tip Path C ρ̄ / V₄₂ — NOT done here; would be invent.
2. Reading χ³~η⁶ (Cat B) as Cat A, or as a Weil dictionary (Opt 1 NOT selected).
3. Stub "lattice automorph" wording could be cited as a REPORT mechanism — it is ABSENT.
