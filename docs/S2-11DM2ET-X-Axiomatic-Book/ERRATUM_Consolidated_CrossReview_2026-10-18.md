# ERRATUM (consolidated): internal cross-review C1–C18 of the 2026-10-18 Bridge C work

Source: internal cross-review `Cross_Review_2026-10-18/` (Master copy, redacted to framework scope), with the exact closures in `Tensor_Pattern_Closure_2026-10-18/`, `General_s_Tensor_2026-10-18/`, `Cusp_Onset_Closure_2026-10-18/`, `H_s_Closure_2026-10-18/`, `C_third_Unified_2026-10-18/`, `C_third_Closure_2026-10-18/`. Consolidated statement: `Bridge_C_Consolidated_rev4_2026-10-18/` (rev. 4, Appendix C, items R4.1–R4.12).
Pure copy-and-create: this file is new; **no earlier Master file is edited, renamed or deleted**. The earlier files listed below remain as they are; read them together with this erratum. No locks altered. CORE_FREEZE holds. Distinct from HQCC termination claims. No TPC or RH claim.

## 0. Conventions fixed from now on (C5, C6, C7, C12)
- **Categories.** Cat A = proved, or exact (including an exact finite computation on a stated set; "modulo F1" / "conditional on [cited theorem]" is stated where it applies). Floating-point-only results (SVD ranks, FFT counts, PSLQ, numerical residuals) = **Cat B**, however small the residual. Earlier ledgers that list "Cat A (numerical)" items are relabelled below.
- **Theorem names.** Theorem G = the Lewis–Zagier period theorem of the consolidated paper (rev. 3 meaning, unchanged). The g_s asymptotics = **Theorem G_s**. The zero-set theorem for the Gauss mean (called "Theorem G" in the C_third-Modularity report) = **Theorem D** of the consolidated paper. "Theorem L" is not used (it is the framework's Parity Dominance Theorem); no new label collides with L1–L7; Lemma L keeps its name. Lemma C1 / C2 of C_third-Unified are called **Lemma Prod1 / Prod2** (to avoid a clash with cross-review item C1).
- **Spaces.** W_P := Fix(P), dim 2(s−1)² (72 at s = 7). V := the function span. V_Eis, d_Eis := the Eisenstein (constant-term cyclic) span and its dimension, 3∏(p^e+1)/2 for odd s. d_cusp := dim V − d_Eis. V^⊥ := complement of V in W_P. Several reports wrote "W" for W_P, for V_Eis, or for V^⊥.
- **The three D's at s = 11.** n_s := s(s−2) (99 at s = 11; rev. 3's "D = 99"); D_s := discriminant of the order (396; 140, 48 at s = 7, 8); ℓ_s := coordinate scale X = ℓ_s ν (198; 70, 48 at s = 7, 8).
- **S versus S⁻¹.** S_lab := the label matrix, u(−1/w) = S_lab u(w). On the stored S₇, S₈, S₁₁: S_lab² = P, (S_lab T)³ = I on all labels, (S_lab⁻¹T)³ = S_lab⁻². The SL₂(Z) representation in the standard presentation is **ρ(S) := S_lab⁻¹**, ρ(T) := T. "(ST)³ = I on all of C¹⁴⁰" and "(ST)³ ≠ P on all 140 labels" are both correct for S = S_lab. On W_P, S_lab = S_lab⁻¹.

## 1. Corrections to files already on Master
### 1a. `U1_LEDGER_s8_s11_Analogues_2026-10-18.md` and `s8_s11_Analogues_2026-10-18/`
- **A2, s = 8 unit (C17).** "order Z[2√3], ε = 2+√3" is wrong for the order: 2+√3 ∉ Z[2√3]. The fundamental unit of the order is **7+4√3 = ε_γ**. Statements with 2+√3 are correct for the maximal order only. (Cat A)
- **A5, s = 11 cusp rank (C2).** "Cusp function-space rank ≥ 73 of 110" (and "Eis ≤ 37") is withdrawn. Exact: **dim V = 110, d_Eis = 90, d_cusp = 20** (Cat A; exact rank, local Eisenstein factors certified). The statements that u_L at s = 11 has genuine dihedral cusp content and the 12 non-genus characters stand. "≥ 90 dihedral newforms" is a Cat B count of forms, not a dimension, and is not a lower bound on d_cusp.
- **A8 and Cat B "h⁺ ≠ #genera ⇔ cusp part" (C11).** The h⁺ and genus counts are correct data, but the "cusp onset at s = 11, 19, 25, 41" reading is **refuted**: (i) the family span has a cusp part for every odd s ≥ 5 (d_cusp ≥ (s−1)(s−3)/4 > 0; exact at the certified s); (ii) for the single vector u_L, s = 14, 17, 18, 22, 23 have h⁺ = #genera and cusp content. The u_L criterion is H̄ ≠ 1 (rev. 4, Prop. 11.8).
- **"60 + 12" (C3)** in the s8_s11 report (s = 7 label split "60 Eisenstein-or-zero + 12 cusp"): superseded by W_P = 72, V = 42 = 36 + 6, V^⊥ = 30 (see also `ERRATUM_Theorem_F_Function_Span_42_2026-10-18.md`).
- **Genera at s = 11 (C1):** 4, not 2 — already corrected in `ERRATUM_s11_Genus_Count_2026-10-18.md`; nothing further.
- **D notation (C6):** the report's "D = 70/48/198" is ℓ_s, not a discriminant.
- **Category relabel:** the floating items in A4–A6 (unitarity residuals, |Eis| = |cusp| = 0.204, Herglotz agreement to 1e-13) are Cat B under the convention of §0; the exact q-series identities, ζ-values and ray-class computations stay Cat A.

### 1b. `U1_LEDGER_g_s_Closed_Forms_2026-10-18.md`
- **Label note (C7).** It says Theorem G of the consolidated paper is the "zero set of the Gauss mean". Wrong: **Theorem G is the Lewis–Zagier period theorem; the zero set is Theorem D.** The renaming of the g_s result to Theorem G_s stands.
- **Cusp onset** (Cat A bullet and Cat B bullet): the counts stand; the onset interpretation is refuted as in 1a.
- **"Higher radial coefficients of H_s … not computed (open)":** now computed — H_s at x = 0 has no integer-order terms, and closed forms are known at t^{−1/2}, t^{1/2}, t^{3/2}, t^{5/2} for all s ≥ 5 (Cat A modulo F1); see `U1_LEDGER_H_s_Closed_Forms_2026-10-18.md`.

### 1c. `U1_LEDGER_C_third_Modularity_2026-10-18.md`
- **A6 (C7):** "Theorem G zero set re-checked" → **Theorem D** zero set.
- **A4 / Cat B "the profile law for all γ, x":** the |x| profile law is now **proved** (Audit Theorem 5.1 = rev. 4 Theorem 5.1; Cat A), so Theorem O1 no longer depends on it.
- **C8 (no error):** B(c₁,c₂) = −1/5 there refers to the quadrant cone; B(c₁,c₂) = −4(s−2) refers to the H_s cone. The cones share only the ν₁ = 0 wall.

### 1d. `ERRATUM_Theorem_F_Function_Span_42_2026-10-18.md` and `U1_LEDGER_S_Spectrum_2026-10-18.md`
- dim V = 42 = 36 + 6 is now **exact** (V = Fix(N) ∩ Fix(γ), Fourier-matrix rank mod ℓ = 29401; Cat A), not only numerical (C15).
- The "Open" items are **answered**: V^⊥ (30) = B₁⊗X⁺ (12) ⊕ A₃⊗X⁻ (18) is killed exactly by the γ phase flip; the 6 cusp combinations are V_cusp = B₁⊗X⁻ (X^± = W₅^± ⊗ W₇^±).
- The S multiplicities (36/36 on W_P; 18/18, 3/3 on V_Eis, V_cusp) are now exact via the local Gauss sums; the ledger's "no closed Gauss-sum proof is given" is superseded. Floating residuals listed there are Cat B evidence.

## 2. Corrections to the rev. 3 consolidated paper (local only; never pushed) — fixed in rev. 4
- **C2** s = 11 "cusp ≥ 73" → 20 (R4.1). **C11** onset rule withdrawn (R4.2). **C10** stale open item on s = 8, 11 removed (R4.3). **C9** a_H, a_C and the H_s constant term are closed forms (Cat A mod F1), not PSLQ / "30 digits" (R4.4). **C14** the rev. 3 "Weil erratum" is partly reversed: the old 36-component claim was wrong, but the label representation is exactly Weil(2x²/5) ⊗ Weil(x²/7) ⊗ (4-dim 2-adic factor) (R4.5). **C15** dim V = 42 exact; E_{−a} = E_a proved for all s ≥ 5 by Lemma R (R4.6). **C17** (R4.7).

## 3. Corrections to reports pushed with this erratum
- **C4 (V42-Structure):** local forms x²/5, 3x²/7 (raw residues) → **2x²/5, x²/7** (x₄ ≡ 3a mod 4, x₅ ≡ 2a mod 5, x₇ ≡ 6a mod 7). 2 is a non-square mod 5 and 3 is a non-square mod 7, so the old forms are not isometric to the true ones.
- **C18 (V42-Structure §5):** the Cat B hypothesis "V^⊥ realised by weight-1 lifts" is retired: weight-1 vectors are P-odd (ρ(S)²f = (−1)^k f), so they cannot lie in W_P ⊃ V^⊥.
- **C13 (Cusp-Onset):** floating SVD ranks and FFT character counts are Cat B; the exact values are in `Cusp_Onset_Closure_2026-10-18/` (exact ranks s = 5..51, 72).
- **Cusp-Onset-Closure:** the verbal formula W₂(k,u) means d₂(k,v) with v the odd part of 2t(t−1) (s = 2t); `cert_W_5_6_7_8.json` does not certify d_Eis at s = 5, 7, 8 and is not used.
- **General-s-Tensor:** dim Fix(P) = 2(s−1)²; 3∏(p^e+1)/2 is d_Eis, not dim W_P.
- **H_s-Closure:** the x ≠ 0 fits at x = 1/2 (s = 7, 9, 10) and x = 1/3 (s = 7, 10) are unstable and not quoted. **H_s-Closed-Forms** pre-registered prediction PB5 (rational t¹ term) was refuted (the term is 0).

## 4. What stands
Theorems A–K of the consolidated paper with their rev. 4 statuses (Theorem K is Cat B since rev. 4: floating L(0) identities); O1, O2; Lemma P; the profile law; the S-law and T-law; the s = 8 even-lattice result (all components Eisenstein); the genus counts as corrected.
