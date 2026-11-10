# FINDINGS — Eigen Cat A foolproof: 539 Corpus §2.1 + Codex MODULE 2 (DRAFT, 2026-11-03)
REPORTS ONLY · No CERT · Video EXCLUDED · No RECS · Soft SF PRESS parent-only

## Hashes
- tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` BEFORE 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 / AFTER identical — tip_touched NO
- OW 8a0325da19ba3802652a654523b681cf74a623d28a4f1a4484999420098a453b
- Corpus 5a8f863093c6eacb57a03b74b8c3906808111fbe43f6ba9677aebae4b8f17f9e
- Codex 0183093491115f3c7928446eaa5d9c15a0b30bd32d09acdd7484a67799c1cc21 (re-hashed, MATCH)
- PROOF_HANKEL_POSITIVITY 663f6c4fefd6e52ee17414b24909187bea1375b2da7aaa83e648d6b7e80c96c1
- PROOF_22_TO_13_AND_WILSON 314b8212e9faceaa1e28541e5c74b87505fd767b10a6190a1de8c832a3de5eb9
- Compute: `eigen-cata-foolproof-2026-11-03/compute.py`, `compute.log`, `SHA256SUMS` (sympy, exact)

## Reconstruction (M=3)
Reading: [k]=x^k in group ring ℤ[ℤ/3] (x^3=1); ρ(h)=3×3 circulant; eigenvalues h(ω^j). Paths = pairs (a,b) of support terms, state a+b mod 3; W = signed sum at a target state, N = Σ|weights|. The corpus does not name the target state; with target [1] the example reproduces exactly. Reading is faithful but target choice is inferred (not written) → MATCH-with-stated-reading.

h1·h2 = 2[0] + 0[1] + 4[2]. Target [1]: paths (0,1) weight +1, (1,0) weight −1 → W=0, N=2.

## Claim table
| Claim | Status | Exact numbers |
|---|---|---|
| det ρ(h1) ≠ 0 | MATCH (ℤ and ℤ/3) | det=2 (≡2 mod 3); eigs 2, 1+ω, 1+ω² |
| det ρ(h2) ≠ 0 | MATCH over ℤ; **FAIL over ℤ/3** | det=36 ≡ 0 mod 3; eigs 3, −3∓√3 i |
| W=0, N=2 | MATCH (target [1]) | other targets: [0] W=2,N=4; [2] W=4,N=4 |
| det≠0 does not prevent cancellation | MATCH (over ℤ) | det 2·36=72≠0, W=0 |
| \|W\| ≤ N ≤ ∏‖h_i‖₁ | MATCH-on-example | 0 ≤ 2 ≤ 10 |
| ∏‖h_i‖₁ = spr(ρ(\|T\|)) | MATCH-on-example (holds generally for nonneg circulants, Perron eigval = coeff sum) | 2·5 = 10 = spr |
| \|W\| ≤ ∏ spr(ρ(h_i)) | MATCH-on-example (trivial, W=0) | ∏spr = 2·2√3 = 6.928; per-target max \|W\|=4 ≤ 6.928 also holds; general statement invent-pending |
| Corpus §1 "odd M ⇒ 1+ω^j≠0 ⇒ det ρ≠0" | TENSION: true over ℂ for h=1+x; mod 3 the h2 layer is singular | — |
| Codex: det(M)≢0 mod 3 ⇒ M⁻¹ mod 3 | MATCH (standard linear algebra) | — |
| Codex: invertibility "prevents information collisions" | FAIL / category error | invertible per-layer maps coexist with W=0 total cancellation (corpus's own §2.1 example); also h2 is not invertible mod 3, so example does not even satisfy the Codex hypothesis on ℤ/3 |
| Codex HQCC Φ/χ map | AMBIGUOUS / invent-pending | Φ well-defined on ℤ₃; "convergence theorem" stated with no proof; not checked |
| Codex Ω=N−\|W\| ≡ 0 (mod 539) hardness | invent-pending | N redefined ("block length") vs §2.1 (path count); W redefined (winding number) → AMBIGUOUS definitions; on §2.1 example Ω=2 ≢0 mod 539; no hardness proof given |
| "multi-layered Hankel" (HQH-539-512) | AMBIGUOUS / ABSENT | no Hankel matrix specified in corpus or Codex |

## Hankel cross-map
PROOF_HANKEL_POSITIVITY (sha above): det(H)≠0 does not eliminate ghosts; PSD Hankel positivity is the correct condition (H=[[1,2],[2,1]], det −3, eigenvalue −1). The corpus "multi-layered Hankel" narrative is NOT that theorem and supplies no Hankel data. The §2.1 example is consistent with that proof's category point and with PROOF_22_TO_13_AND_WILSON: non-vanishing det (invertibility) does not control signs/cancellations; the Codex "no collisions" inference repeats the same category error. No new Hankel theorem asserted.

## Vs eigen-matrix
This is elementary group-ring/circulant arithmetic on ℤ[ℤ/3]; it bears no relation to Eigen ρ̄ mod-ℓ Galois representations / modular N36/Q89 work beyond the shared word "ρ". No eigen-matrix-search or eigen-card1f artifacts were modified or needed; no tip Cat A coefficients, roots, Kr QQ or ν used or invented.
