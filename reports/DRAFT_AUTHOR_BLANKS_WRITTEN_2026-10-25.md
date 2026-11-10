# DRAFT FOR ARVIN REVIEW — not written into live residual-C
These are proposed fills only. residual-C stays OPEN and Bridge C stays PARTIAL. residual-c-field-WRITTEN_PREMISES_DRAFT.md was not edited. Prepared 2026-10-25 ~17:20 CDT (America/Chicago).

## Grounding used
- Accepted residual-C constraints, as quoted in reports/DRAFT_AUTHOR_BLANKS_dimV_k_rho_2026-10-25.md. That file cites the live draft at sha ea85cbbc239d2e050e2b639908ae70dc850090270f08081662e26606036a7feb:
  - G = Γ₀(49)⁺ = ⟨Γ₀(49), W₇⟩ (l.9, 30, 46)
  - ρ is direct and ρ(W₇) is non-scalar (l.10, 36)
  - dim V ≥ 2 (l.16, 37)
  - k ∈ ℤ, k < 0; trivial multiplier, no cover, PSL₂-style, ρ(W₇)² = Id (l.39–40, 62)
  - conjugation compatibility (l.63)
- Seven-chat findings: reports/FINDINGS_GROK7_W7_AUTHOR_BLANKS_2026-10-25.md. None of the seven chats supplies a level-49 candidate.
- 9 Maths 904104d2…: per the prior draft, its ρ : G_obs → End(M_osc) is a different representation and supplies no value.
- The EH L1–L7 appendix and EinsteinHamptonCurvature.lean have no representation space and no level-49 content (prior draft l.27, l.43).
- **RTA Zenodo 23644022: ABSENT.** No local file references this ID.
- Not re-read in this pass: 17T 18442276, Local rho e39bf210…, 61-omega e6af75da…, DESI 3d4d9a86…. No value below depends on them.
- The OPTIONS packs (residual-c-p1-remainder-OPTIONS.md, residual-c-p2-w7-action-OPTIONS.md) were used only as recommendations.

**Level flag:** here W₇ means Fricke at level 49, τ↦−1/(49τ), up to the residual-C draft's normalization. Chat 0817c866 uses level-7 Fricke τ↦−1/(7τ) and later level 539. Neither is imported here.

## (1) dim V = 2 — AUTHOR-PROPOSED
- Rationale: d ≥ 2 is DERIVED (draft l.16/37). d = 2 is the smallest dimension that admits a non-scalar involution.
- Missing: any Written source fixing d. The 9-dimensional carrier in chat 0817c866 (l.3515) is weight 1/2, level 539, so it is rejected.

## (2) k = −2 — AUTHOR-PROPOSED
- Rationale: k < 0 is DERIVED. The "trivial χ / no cover" premise forces k to be even, because −I ∈ Γ₀(49) acts by (−1)^k and ρ(−I) = Id. That consistency step is my inference. If "PSL₂-style" is meant to quotient out −I, that argument has to be restated. −2 is the largest even negative integer.
- Distinctness: k = −2 is not the RTA residual_slash weight 1/2. **The EH warp k value was not located. Arvin must confirm that −2 differs from it.**
- Missing: a Written weight.

## (3) ρ on generators (P1) — AUTHOR-PROPOSED
- ρ(γ) = I₂ for every γ in Γ₀(49), so no generator list is needed.
- ρ(W₇) = diag(+1, −1).
- Checks:
  - Γ₀(49) relations hold trivially.
  - ρ(W₇)² = I₂.
  - Conjugation (l.63): ρ(W₇γW₇⁻¹) = I = ρ(W₇) I ρ(W₇)⁻¹, using that W₇ normalizes Γ₀(49).
  - Trivial χ holds.
  - ρ(W₇) is non-scalar.
- Missing: any Written generating set or non-trivial ρ|Γ₀(49). This is the minimal extension and carries no arithmetic content.

## (4) ρ(W₇) split (P2) — AUTHOR-PROPOSED (the splitting itself is DERIVED)
- DERIVED: V = V₊ ⊕ V₋ with both summands nonzero (ρ(W₇)² = Id and ρ(W₇) ≠ ±Id; prior draft §4b).
- AUTHOR-PROPOSED: d₊ = 1, d₋ = 1. The residual sign choice is +1, following the OPTIONS +1 recommendation, so it is not derived.
- Missing: a Written ± choice. No level-49 eigenspace data exists in the seven chats.
