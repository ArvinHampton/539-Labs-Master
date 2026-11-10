# FINDINGS — MR1 — T-E ρ̄|cusp6 local-factor route: classical generators CITE-CHECK
Date: 2026-10-26 · Author: Math Research 1 · Mode: Soft SF invent HOLD · FINDINGS only

## 1. Authority / locks
- OW Card 1D: `/workspace/quantum-comp/reports/OWNER_WRITE_TE_RHOBAR_LOCAL_FACTOR_CARD1D_2026-10-26.md` sha256 `ab8a4937eb4087a8c63b1c9addeb5e9a5c085c3428f963bcb10d3fe468e4595a` (re-verified). Order 2 permits MR1 cite-check under invent HOLD.
- Eigen ABSENT-BLOCKER: `/workspace/grok-batches/EIGEN-TE-RHOBAR-CUSP6-Q18-BASIS_2026-10-26.md` sha256 `e90ef2263cb77626ab7d0ce740e670f1fb4af35d850c0dbe447edb379a7331ca` (re-verified).
- Float T-spectra hint (NOT a Written ID): ρ̄|cusp6 ≈ (1-dim mod 4) ⊗ (2-dim mod 5, exps {1,4}/5) ⊗ (3-dim mod 7, exps {3,5,6}/7). FLOAT HINT ONLY.
- Tip Soft SF LOCK `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` — tip_touched NO; invent HOLD; no tip fold. Factorization ρ̄|cusp6 ≅ ρ₄⊗ρ₅⊗ρ₇ is NOT claimed proved here (Eigen's exact-intertwiner job).
- No Fourier coefficients are given or invented in this file.

Verification legend: [V] = located/confirmed via web this session; [S] = standard reference cited from known bibliography, not URL-fetched this session (parent/Auditor should confirm before any Written use).

## 2. Candidate families and citable sources

### 2a. General framework (vvmf for SL₂(ℤ), irreps, tensor/induction)
- [V] T. Gannon, "The theory of vector-valued modular forms for the modular group", arXiv:1310.4458 (doi:10.48550/arXiv.1310.4458); publ. Contrib. Math. Comput. Sci. 8 (2014) 247–286, doi:10.1007/978-3-662-43831-2_9. Proves: free-module structure of holomorphic vvmf over ℂ[E₄,E₆] for arbitrary multiplier, dimension formula, Serre duality. Relevant to Card 1D step (3) (module over ℂ[E₄,E₆]).
- [V] P. Bantay, T. Gannon, arXiv:0705.2467 — vvmf and hypergeometric equation; dimension counts.
- [V] C. Franc, G. Mason, "Hypergeometric series, modular linear differential equations and vector-valued modular forms", Ramanujan J. (2016), doi:10.1007/s11139-014-9644-x — explicit vvmf for low-dim irreps (dim 2, 3) via ₂F₁/₃F₂ in the Hauptmodul.
- [V via ref list] C. Marks, "Irreducible vector-valued modular forms of dimension less than six", Illinois J. Math. 55(4) (2011) 1267–1297, doi:10.1215/ijm/1373636684 — explicit structure for irreducible ρ with dim<6 (covers 1-,2-,3-dim factors individually).
- [V via ref list] C. Marks, G. Mason, J. London Math. Soc. 82 (2010) 32–48, doi:10.1112/jlms/jdq020 — module structure.
- [V via ref list] I. Tuba, H. Wenzl, arXiv:math/9912013 — classification of irreps of B₃/SL₂(ℤ) of dim ≤5 (determined up to iso by T-eigenvalues + det in generic cases). Relevant: T-spectrum alone determines low-dim irreducible factor only under their genericity conditions; does NOT give intertwiner for a tensor product.
- [V] arXiv:2202.06676, "On the computation of general vector-valued modular forms" — algorithm for Fourier expansions of vvmf beyond Weil reps/Dirichlet inductions. Possible exact-compute route for step (3).
- [S] A. Nobs, J. Wolfart, classification of irreps of SL₂(ℤ/p^λ) (Comment. Math. Helv. 1976) — irreps of SL₂(ℤ/5), SL₂(ℤ/7) needed for ρ₅, ρ₇ identification; CRT: SL₂(ℤ/140) = SL₂(ℤ/4)×SL₂(ℤ/5)×SL₂(ℤ/7) ⇒ irreps factor as tensor products (standard group theory — supports *shape* of Card 1D(1), not the specific ρ̄ decomposition).

### 2b. ρ₄ (1-dim, mod 4) — Dedekind η powers
- [S] H. Rademacher, Topics in Analytic Number Theory (Springer 1973), and Rademacher–Grosswald, Dedekind Sums (Carus Monogr. 16, MAA 1972): η transformation law with Dedekind-sum multiplier; η²⁴=Δ. Proves: χ_η of SL₂(ℤ) has order 24, η^{2k} multiplier character of order 12/gcd. A character of order 4 (T ↦ i^{±1}) is realized by η⁶ (T-exponent 6/24=1/4) / η¹⁸ — standard consequence, Eigen must check exact sign/eigenvalue match vs ρ̄.
- [S] G. Köhler, Eta Products and Theta Series Identities, Springer Monogr. Math. (2011), doi:10.1007/978-3-642-16152-0 — tables of η-products, levels, multipliers.
- [S] Ligozat criterion (in Köhler; Ono, The Web of Modularity, CBMS 102, AMS 2004, Thm 1.64) — modularity of η-quotients on Γ₀(N).
- Status: SOLID public cite for transformation law. Mod-4 character match to ρ₄: requires exact check (not literature).

### 2c. ρ₅ (2-dim, mod 5, T-exps {1,4}/5) — Rogers–Ramanujan
- [S] W. Duke, "Continued fractions and modular functions", Bull. AMS 42 (2005) 137–162 — proves (G,H) Rogers–Ramanujan functions with q^{-1/60}G, q^{11/60}H form a vector-valued modular function for SL₂(ℤ) with explicit S,T matrices (2-dim rep factoring through SL₂(ℤ/5)·(η-type character)), and RR continued fraction is a Hauptmodul for Γ(5).
- [S] B. Berndt et al., Ramanujan's Lost Notebook / standard RR refs; Kubert–Lang below for Klein-form/Siegel-function realization at level 5.
- Note: G,H themselves carry exponents −1/60, 11/60 (level 60), so matching ρ₅ with exps {1,4}/5 requires twisting by an η-power character (e.g. η^k with appropriate k) — the twist and resulting exact S-matrix must be computed by Eigen; Duke's S-matrix is in terms of sin(2π/5), sin(4π/5) ∈ ℚ(ζ₅)⁺ — consistent with CF(140) ⊃ ℚ(ζ₅) but not yet a match.
- Status: SOLID cite for transformation law of the RR pair. ρ₅ match: OPEN (exact check required).

### 2d. ρ₇ (3-dim, mod 7, T-exps {3,5,6}/7) — Klein level 7
- [S] D. S. Kubert, S. Lang, Modular Units, Grundlehren 244, Springer 1981 — Klein forms / Siegel functions, exact transformation under SL₂(ℤ), level-N units.
- [S] N. D. Elkies, "The Klein quartic in number theory", in The Eightfold Way, MSRI Publ. 35 (1999) — Klein's 3-dim rep of PSL₂(𝔽₇) on weight-? forms for Γ(7): x,y,z (theta-type / η-quotient forms, e.g. q^{4/7}, q^{2/7}, q^{1/7} leading exps) satisfying x³y+y³z+z³x=0; X(7) = Klein quartic. Exponents {1,2,4}/7 vs conjugate rep {3,5,6}/7 (= −{1,2,4}/7 mod 1): the hint matches the *dual/complex-conjugate* of Klein's 3-dim triple — Eigen must verify which of the two 3-dim irreps of PSL₂(𝔽₇) and multiplier twist.
- [S] Fricke/Klein classical; Γ₀(49) Fricke involution via Atkin–Lehner (Atkin–Lehner, Math. Ann. 185 (1970)) — standard for newforms on Γ₀(49), not directly the ρ₇ intertwiner.
- Status: SOLID cite for Klein triple transformation law (Elkies, Kubert–Lang). Dual-rep / twist match: OPEN.

### 2e. Tensor product ρ₄⊗ρ₅⊗ρ₇ (dim 6) realized by products of classical generators
- ABSENT: no public cite found asserting a specific 6-dim vvmf of the form (η-power)·(RR pair)·(Klein triple) matches a cusp-component of an induced rep on Γ₀(49) at weight 4. Literature gives each factor individually; product construction is standard (products of vvmf are vvmf for tensor rep) but the identification with ρ̄|cusp6 is NOT literature-supported → Eigen exact work.

## 3. Exact checks Eigen still must do (literature cite ≠ Written ID)
1. Exact intertwiner over CyclotomicField(140): ρ̄|cusp6(S), ρ̄|cusp6(T) ≅ ρ₄⊗ρ₅⊗ρ₇ with exact matrices (not float T-spectra).
2. For each factor, exact S,T of the chosen classical generator (incl. η-twist) equal ρᵢ up to explicit conjugation; dual-vs-Klein 3-dim choice resolved.
3. Weight bookkeeping: total weight of product generators + ℂ[E₄,E₆] module grading → weight 4 component, cusp condition.
4. Module rank/dim through q^18 vs dim 89 (Card 1D(3)); dim-89 MATCH cannot be inferred from literature.

## 4. ABSENT flags
- ABSENT: public cite for the specific identification ρ̄|cusp6 ≅ ρ₄⊗ρ₅⊗ρ₇ (expected — it is project-specific).
- ABSENT: public cite for the 6-dim product generator matching cusp6 / dim 89.
- No family in 2b–2d lacks a solid cite for its own transformation law.
- [S]-tagged items not URL-verified this session; recommend Auditor confirm before Written use.

## 5. Non-claims
No coefficients invented. No tip edit. No dim-89 MATCH claimed. No factorization claimed proved.

## 6. STATUS
STATUS: CITECHECK PARTIAL — framework cites [V]; per-factor transformation-law cites present [S] (solid standard refs, not all URL-fetched); tensor-product identification ABSENT (Eigen exact job).
Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` sha256 re-verified `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` — tip_touched NO.
