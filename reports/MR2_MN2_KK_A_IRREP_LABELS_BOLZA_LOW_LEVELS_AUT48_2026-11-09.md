# MR2 · MN2 · KK Group A — irrep labels of the low Bolza Laplace levels under Aut⁺ (order 48, GL(2,3))
Date: 2026-11-09 (CST). Scope: OW 8b26c786 (Group A = Aut⁺(Bolza) × wall ℤ₂ adopted as KK truncation symmetry; scope choice, not a result). Group B not adopted. Full spectrum OPEN; junction UNSOLVED; count gap unchanged.

Files (frozen before run):
- `MR2_MN2_KK_A_IRREP_LABELS_BOLZA_LOW_LEVELS_AUT48_2026-11-09.py` sha256 ff80054190db1d7ef0ce365cdf9784afe5f21e067f63f74d3e12c2501cd08ea7 (chmod a-w)
- `….log` sha256 6383cd412278cf9976820b6019bded1cf702bedda993243b0939c7b18f8bde90 (runtime 40 s)
- Reuses [G] group data and [T] mesh/assembly of the KK .py sha 88949658…b26c (sha-checked at start of run).

## Premise convention (PP 985d404d residual 1)
One premise only, attached to the headline: **(U) Bolza uniformization** — Σ = ℍ/Γ with Isom(Σ) (order 96) acting simply transitively on the triangles of the (2,3,8) tiling, so Σ/Isom = the (2,3,8) triangle and L²(Σ) = ⊕_π π ⊗ (π-twisted triangle problem). All abstract group-theory statements below are PROVED unconditionally; numerics are labelled separately. "PROVED with a COND premise" is counted as COND.

## Method (smallest settling computation)
- Coxeter triple (r_AB, r_AC, r_BC) of antiholomorphic involutions found in G96 (products of orders 8, 2, 3; generate all 96). Homomorphism Isom → O_h (B3 mirrors), kernel ⟨J⟩, checked well defined.
- 13 real irreps of Isom (dims 1⁴ 2² 3⁴ 4³, Σd² = 96, all ⟨χ,χ⟩ = 1) by splitting constructed reps (1-dim chars, T⊗χ, T⊗T(⊗χ), H¹⊗χ, H¹⊗T⊗χ) with a random symmetric commutant.
- Per irrep π: vector-valued P1 FEM on the triangle, u ∈ V₊(π(r_i)) essential on edge i; multiplicity of an eigenvalue in the π-problem = multiplicity of π in the Laplace eigenspace. n = 60, 120, Richardson. No sweeps.
- Control: 1-dim sectors reproduce the scalar NN/DN/ND/DD values of ecee2668 (only I1 below 25.5: 0, 23.0786). Count check: 24 nonzero eigenvalues (with multiplicity) below 25.5 vs Weyl leading term 25.5.

## Definition of the labels (PROVED, group theory)
GL(2,3) → PGL(2,3) ≅ S₄. **3** := pullback of the standard rotation rep T1 of S₄; character **+1** on order-8 elements. **3⊗sgn** := 3 ⊗ det; character **−1** on order-8 elements. Both order-8 classes of GL(2,3) map to the single 4-cycle class of S₄, so the distinction is well defined; det is the unique nontrivial 1-dim character, so the label is invariant under every automorphism of GL(2,3) (intrinsic).

## Result
| λ (FEM, Richardson) | SU value (mult) | rel diff | Isom irrep | dim | Aut⁺ content |
|---|---|---|---|---|---|
| 3.83889 | 3.838887 (3) | 3.1e-9 | I10 | 3 | **3** |
| 5.35360 | 5.353601 (4) | 3.8e-9 | I12 | 4 | 4 (J-faithful) |
| 8.24955 | 8.249555 (2) | 7.8e-9 | I5 | 2 | 2 (J-trivial) |
| 14.72622 | 14.726217 (4) | 6.7e-9 | I11 | 4 | 4 (J-faithful) |
| 15.04892 | 15.048916 (3) | 1.4e-8 | I8 | 3 | 3⊗sgn |
| 18.65882 | 18.658820 (3) | 2.5e-8 | I10 | 3 | 3 |
| 20.51986 | 20.519860 (4) | 2.0e-9 | I13 | 4 | 2′ ⊕ 2″ (complex pair; real 4-dim) |
| 23.07856 | 23.078558 (1) | 3.9e-8 | I1 | 1 | 1 |

Each level is a single irreducible Isom-rep (no accidental degeneracy below 25.5). Aut⁺ content is the restriction of the Isom irrep; the Aut⁺ invariant level (for Group A, before the wall) below 25.5 is only 0 and 23.0786.

## Claims
1. **Headline — λ₁ = 3.8389 eigenspace is the Aut⁺ irrep 3** (trace +1 on order-8 elements; Isom irrep I10 = T1 ⊗ trivial, χ(r) = +1 on all three reflections). **CONDITIONAL** on (U); the eigenvalue identification is numerical (FEM float, Richardson n=60/120), cross-checked against SU to 3e-9.
2. Irrep decomposition of all levels λ < 25.5 as in the table, including 23.0786 = trivial. **CONDITIONAL** on (U) (same premise, same numerical status; counted once more because it is a separate deliverable).
3. Label definitions 3 vs 3⊗sgn are intrinsic (automorphism-invariant). **PROVED** (group theory).
4. Isom(Bolza) has 13 real irreps (1⁴ 2² 3⁴ 4³), with the Aut⁺-restrictions listed in the log ([C]); I13 restricts to the complex pair 2′⊕2″ (⟨χ,χ⟩₄₈ = 2). **PROVED** (computed exactly from G96 data).
5. Strohmaier–Uski multiplicities (3,4,2,4,3,3,4,1) agree with the FEM multiplicities. **CONDITIONAL** (citation; agreement verified numerically; citation does not upgrade anything).
6. Caveat: the Isom labels I11 vs I12 (both 4-dim, J-faithful) depend on the chosen Coxeter triple up to outer automorphism of Isom; the Aut⁺ labels do not. **PROVED** (remark).
7. Levels above 25.5, rigorous (interval/enclosure) error bounds for the FEM eigenvalues, and the charged S⁴ towers. **OPEN**.

## Tally (COND convention)
PROVED 3 (claims 3, 4, 6) · CONDITIONAL 3 (claims 1, 2, 5) · OPEN 1 (claim 7) · REFUTED 0.

Rules: new dated files only; .py frozen before log and md; no existing file edited; tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` untouched; nothing external; no messages sent.
