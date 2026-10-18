> Copy of a local report. Local-only paths are replaced with repo-relative names. The scripts expect the companion local folders 2026-10-17-cusp-part and 2026-10-17-psi-conditions (fitF.pkl, uvec.py, S/T .npy), which are not included because they are binaries or local-only files.

# S and T spectra on the 72-dim P-invariant subspace (Theorem F, Bridge C rev2)
Script: s_eig.py (output s_eig.txt). Builder reused unchanged: family.py from 2026-10-17-cusp-part (a = (7/10,-1/5) = -(the user's a); same up to u_{-α,-β}=u_{α,β}). The rebuilt S,T match the stored 2026-10-17-psi-conditions/S_matrix.npy, T_matrix.npy exactly (diff 0).

## Checks (Cat A)
- P=S²: |P²−I|=1.4e-15, [P,T]=8.8e-16, dim Fix(P)=72.
- On the 72: S²=I to 9.6e-16, (ST)³=I to 2.2e-15. (On all 140, (ST)³≠P; that only holds on the 72.)
## S spectrum (Cat A)
- Eigenvalues ±1 (max deviation 1.8e-15). **n₊ = 36, n₋ = 36, tr S|₇₂ = 0** (numerically 0 ± 1e-16; an integer since the eigenvalues are ±1, so exact).
- No closed-form Gauss-sum derivation was done. The trace is exactly 0.
## Eisenstein/cusp split: not resolved
- In the 140-label coordinates, neither the column nor the row span of Π=(I+P)/2 restricted to the 116 Eisenstein labels (dim 60) or the 24 cusp labels (dim 12) is S-invariant. Residual 0.2–0.4. The T residual is ≤1.5e-15.
- Traces on those spans: tr = ∓0.2089 (not integers). So the per-block n₊/n₋ values are not meaningful in this basis. A truly S-invariant 60+12 basis (the paper's "coefficientwise" claim) was not found in the cusp-part scripts. Open.
## T spectrum (Cat A)
- Order of T|₇₂ = **140** (|T¹⁴⁰−I|=7.5e-14). The eigenvalues are e(r), with angle residual 5e-13 against the denominator 840. r : multiplicity:
0:1, 3/70:2, 1/14:1, 1/10:1, 19/140:4, 1/7:1, 6/35:2, 13/70:2, 31/140:4, 17/70:2, 1/4:2, 2/7:1, 27/70:2, 11/28:2, 2/5:1, 59/140:4, 33/70:2, 1/2:1, 15/28:2, 19/35:2, 4/7:1, 3/5:1, 9/14:1, 13/20:2, 47/70:2, 24/35:2, 26/35:2, 11/14:1, 111/140:4, 23/28:2, 17/20:2, 31/35:2, 9/10:1, 131/140:4, 34/35:2, 139/140:4  (total 72).

## Rerun in function space (script split_V.py, output split_V.txt)
Method: C = 140 labels × Fourier modes (exact cone sums from cusp-part/uvec.py, constant term included, |Q| ≤ 60, 1495 modes). Since u(w) = C·(mode functions), the span of the values u(w) is V = colspan(C) ⊂ C¹⁴⁰. S and T act on V directly, because u(−1/w) = S u(w). The relations kernel is {x : xᵀC = 0}, and S and T act on it through their transposes. Eis and cusp parts: each label is pure. 24 labels are pure cusp (Eisenstein content ≤ 7.5e-31) and 116 are pure Eisenstein (cusp content ≤ 3.1e-30) (fitF.pkl). So the character projection of C is a restriction to rows.

Results (Cat A):
- **dim V = 42, not 72.** The singular-value gap is 17.1 → 1.8e-13, and the rank is the same at |Q| ≤ 25 and ≤ 60. The relations kernel has dim 98. It is invariant under Sᵀ (4.0e-16) and Tᵀ (7.8e-16). V is invariant under S (3.5e-16) and T (6.5e-16). V ⊂ Fix(P) (8.5e-16).
- **Eis: dim 36.** S-invariance 3.2e-16, T-invariance 8.0e-16, S²=I there. tr S = 0, so **n₊=18, n₋=18**. The T eigenvalues are the 36 distinct values from the 72-dim list above, each once.
- **Cusp: dim 6.** S-invariance 4.5e-16, T-invariance 3.1e-16. tr S = 0, so **n₊=3, n₋=3**. T eigenvalues e(r) for r = 19/140, 31/140, 59/140, 111/140, 131/140, 139/140.
- Eis ⊕ cusp = V (rank 42). Totals are 21/21 on V.

Verdict: the split into Eisenstein and cusp parts is S- and T-invariant, so that qualitative claim holds. The paper's dimensions are wrong. "Rows rank 60/12 in the 72" measures ranks of Π=(I+P)/2 restricted to label rows, which is a coordinate artifact and not invariant (see above). The functions u_{α,β} span only 42 = 36 + 6. The 72-dim Fix(P) is the correct domain of the matrix representation (S²=(ST)³=I there; n±=36/36). However, it is a label-space representation that contains the 42-dim function space V as an invariant subrepresentation. On the 72, the T multiplicities are 1, 2, 4, against 1, 1, 2 on V. So Fix(P) = V ⊕ (a 30-dim T-stable complement with T multiplicities 0, 1, 2) that these Maass functions do not realise. Possibly the complement belongs to the f_{α,β} q-series partners mentioned in family.py; this was not checked. Recommended correction for Theorem F: "the functions span a 42-dim representation = 36 Eis + 6 cusp, inside the 72-dim P-invariant label representation".

## Step 1 follow-ups (scripts cusp_count.py, fpart_rank.py)
- (a) Cusp count (Cat A): 24 non-σ-invariant pure-type ray-class characters occur. They form 12 σ-orbits, and every orbit has size 2. χ and χ∘σ give the same theta series, so there are 12 distinct dihedral Maass cusp forms, and all 12 have nonzero content. The 24×48 label×(character, sign) content matrix has rank 6, both before and after merging σ-pairs. So the 12 forms occur only in 6 fixed linear combinations, which gives dim V_cusp = 6. Corrected statement: the 24 characters give 12 forms, which realise a 6-dim cusp span. The earlier "12-dim cusp part" was wrong. The pairing is not explained by u_{−α,−β}=u_{α,β}; that relation is already built into V. The structure behind the 6 combinations was not identified (open).
- (b) The partners f (Cat A, with f taken to be the positive-frequency part of u): rank C(q>0) = rank C(q<0) = rank C = 42. These partners span the same V, so they do not supply the missing 30 dims of Fix(P). Whether Fix(P)/V is realised by any functions is open.
