# Symmetry Audit — neg, Z_q, Z_p, γ in the odd-s label family (2026-10-18 21:18 CDT)
Folder: 2026-10-18-Symmetry-Audit/. Nothing was pushed, and no pushed file was edited.
Cat A = exact. Cat B = floating-point/cited.

## 0. Root cause (Cat A, exact)
The 21:16 "retraction" in 2026-10-18-Open-Algebraic.md is itself **wrong**. Cause: a matrix-convention bug in **my** map builders.
- vecfam.map_exp, commutant.py (X[j,i]) and sec_sparse/sec_valid (BFS) build a label map as X[j(i),i] = e(ph_i).
- The correct operator is the transpose, Y[i,j(i)] = e(ph_i). This is Family.Pmatrix's convention.
- Exact check: Y_neg = S² = P (|Y−P| = 1e−15).
- exact_commute.py, exponent arithmetic mod K = 2D², s = 5, 7, 9, 11, 13, 15, 25:
  - in the Y convention, neg, γ, Z_p (p|s) and Z_q (q|s−2) **all commute exactly** with S and T;
  - in the X convention, neg and Z_q fail;
  - γ and Z_p (p|s) pass in both (their phases are trivial).
- So the cause is not q′ versus Q; neg = ρ(−I) = S² is a symmetry on the whole label space.

## 1. Re-run on the correct spaces (sec_fixed.py)
- The sector is built in the Y convention.
- Exact invariance certificate: for sampled labels x, (S E)[x,:] = ζ^{coef x}·(S E)[rep,:], or 0 on killed orbits. Every row at s ≤ 11; 300 rows at s = 25, 49. **0 failures** everywhere.
- Then: mod-ℓ commutant (exactly verified basis) and piece dimensions. Lift to C via ℓ ∤ |Mp2(Z/N)| (lift_check.json).

| s | (+,+) | pieces | commutant | (−,−) | mixed |
|---|---|---|---|---|---|
| 7 | 36 | 36 | 1 | 6 (irr.) | 0, 0 |
| 9 | 60 | 12 + 48 | 2 | 12 (irr.) | 0, 0 |
| 11 | 90 | **18 + 72** | 2 | 20 (irr.) | 0, 0 |
| 25 | 468 | 36 + 432 | 2 | 132 (irr.) | 0, 0 |

- p-local invariants (p_old_fixed.py; p with p² | s(s−2)): F = Fix⟨T_p, S T_p S⁻¹⟩ inside (+,+) has dim **12, 18, 36**, and dim(+,+)/dim F = 5, 5, 13. Inside (−,−) the dim is 0.
- So the 12/18/36 piece is the p-old part (trivial on the p-factor) and the 48/72/432 piece is the p-new part. These match the rev5 Prop psq5 "old/new" columns exactly.
- s=49 (+,+) is running in the correct convention: dim 1800, certificate 0 failures; the commutant was not finished when this report was written.

## 2. Classification
| # | Claim (location) | Operators / space | Verdict |
|---|---|---|---|
| 1 | V = A₃⊗X⁺ ⊕ B₁⊗X⁻ at s=7, negation = ⊗Z_p (rev4 Prop matched, Thm tensorodd) | neg = S² = P; Z_5, Z_7, γ commute exactly (Y convention). Sectors 36 + 6 are invariant (certificate) and irreducible (commutant 1) | **SOUND** |
| 2 | Odd-parity sectors are cusp (prop:oddcusp5) | needs only a ρ-invariant σ; (−,−) is invariant with dims 6/12/20/132 = (s−1)(s−3)/4 | **SOUND** |
| 3 | ε_all = −1 sectors vanish (prop:parity5) | Δ-orbit statement; reproduced (mixed sectors empty at s = 7, 9, 11, 25) | **SOUND** |
| 4 | Corrected orbit lemma, ε_all = +1 leading coefficient (prop:orbit5) | orbit-model coefficient on invariant sectors | **SOUND** |
| 5 | d_cusp ≥ (s−1)(s−3)/4 | B₁ sector invariant | **SOUND** |
| 6 | u_L criterion (sec:rev5uL) | class-group/units, no label operators | **SOUND** (unaffected) |
| 7 | s=7 AL sector signs Z_p = ψ_𝔭(−1), S_p² = η_p(−1)Z_p (erratum (c)) | Z_p commute exactly; character side Cat A as stated; operator identity not re-derived here | **SOUND** (not affected) |
| 8a | Prime-square injectivity and exact ranks (psq5 table, totals 72/110/600 = s(s−1)) | exact flint ranks | **SOUND** |
| 8b | psq5 "Π splits each sector into old and new pieces" | true pieces = p-local invariants and their complement, which are ρ-subreps of dims 12/48, 18/72, 36/432 (Cat A). That they coincide with im Π / ker Π from finer.py is shown only by dimension | **SOUND in substance; NEEDS REWORDING** (define "old" as the p-local invariants) |
| 9a | Erratum (a): "Π not ρ-equivariant, so pieces are not subrepresentations"; "s=11 (+,+) irreducible, so 18/72 is not a ρ-decomposition" | evidence used X-convention maps (commutant_9/11.json max_commutator 0.25, krylov_irr): non-invariant spaces | **WRONG** (s=11 (+,+) = 18 + 72, commutant 2, Cat A). The q′-isotropy table itself is correct but irrelevant: the old piece is p-invariant, not Π-defined |
| 9b | Erratum (a) Cat B: s=9 (+,+) = 48 + 12; s=9 (−,−) irreducible; s=11 (−,−) irreducible | same invalid evidence; conclusions confirmed on certified spaces | **SOUND conclusions, upgrade to Cat A; evidence must be replaced** |
| 10 | Z_p (p|s) and γ wherever used | commute in both conventions (exact) | **SOUND** |
| 11 | Unpushed Open-Algebraic md: 21:16 retraction, sec_valid "valid sector" 105/897 | built on a wrong diagnosis; the Fix(γ)∩Fix(Z_p) data are correct but are not the rev sectors | **WRONG retraction** (to be reversed in a new dated section) |
| 12 | Unpushed 20:xx "Cat A" splits 48+12, 432+36, 1728+72 (sec_sparse/split_modl, X convention) | spaces not invariant; numbers coincide with the correct re-run at s = 9, 25 | **Numbers correct (Cat A via sec_fixed); old evidence invalid**; s=49 pending |

## 3. Draft second erratum (NOT pushed)
> **ERRATUM 2 — Bridge C rev. 5 post-push erratum, item (a).** Item (a) of ERRATUM_Rev5_PostPush_2026-10-18 is withdrawn in part. Its floating evidence (commutant.py, krylov_irr.py) built the label maps neg and Z_q (q | s−2) as the transpose of the correct operators, so the "sectors" it analysed were not ρ-invariant (max |[X,S]| = 0.25 recorded in commutant_9.json). With the correct operators (neg = ρ(−I) = S², exactly), neg, γ, Z_p and Z_q all commute exactly with S and T (exact check at s = 5–25).
> Corrected statements (Cat A, mod-ℓ commutant with exactly verified basis, lifted via ℓ ∤ |Mp2(Z/N)|):
> - at s = 9, 11, 25 the (+,+) sector is a sum of two non-isomorphic irreducibles of dims 12+48, 18+72, 36+432;
> - the smaller one is exactly the subspace fixed by the p-local factor of ρ (p² | s(s−2)) and the larger one its complement;
> - the (−,−) sectors (12, 20, 132) are irreducible;
> - mixed sectors vanish.
> Hence Proposition 13.13's "old/new pieces" **are** subrepresentations once "old" is defined as the p-local invariants. Read "Π splits each sector into old and new pieces" as "each sector splits as (p-local invariants) ⊕ complement, of the listed dimensions". The q′-isotropy table in (a) is correct but does not bear on this. The sentence "at s = 11 the (+,+) sector is irreducible, so the 18/72 split is not a decomposition into ρ-pieces" is wrong.
> Items (b), (c), (d) are unaffected. No other rev. 5 or rev. 4 statement depends on the faulty maps.

## 4. Files
- exact_commute.py, exact_commute.json
- sec_fixed.py, sec_fixed_{7,9,11,25}_*.json (s=9 mixed sectors: empty, logged only)
- p_old_fixed.py, p_old_fixed_{9,11,25}_*.json
- ../2026-10-18-Open-Algebraic/lift_check.json
- s=49: ../2026-10-18-Open-Algebraic/sec_fixed_49.log (running)
