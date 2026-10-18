> **Master-copy notation note (added 2026-10-18 at push; report text below is otherwise verbatim).** W here = the Eisenstein space, dim 3∏(p^e+1)/2 for odd s (Master: V_Eis, d_Eis); V − W = d_cusp. D here = the order discriminant (Master: D_s = 140, 48, 396 at s = 7, 8, 11). Floating SVD ranks and FFT counts are Cat B (C13); exact values: Cusp_Onset_Closure_2026-10-18/. Category convention for Master (rev. 4): Cat A = proved, or exact (including exact finite computation); floating-point-only results = Cat B. Where this report labels a floating result Cat A, read it as Cat B (C12, C13). Theorem names: Theorem G = Lewis–Zagier period theorem (rev. 3 meaning); the g_s asymptotics = Theorem G_s; the zero-set theorem = Theorem D. Erratum: ERRATUM_Consolidated_CrossReview_2026-10-18.md. Consolidated statement: Bridge_C_Consolidated_rev4_2026-10-18/.

# Cusp-onset rule: does a cusp part appear exactly when h⁺ ≠ #genera? (2026-10-18, CDT)

Scripts and outputs: `2026-10-18-Cusp-Onset/`. Everything ran locally on the box. Nothing was pushed, posted or emailed.

This continues the interrupted combined run `2026-10-18-Paths-A-B-C.md` (its Path A folder was copied here and extended). The combined file is superseded where this report differs; see §6.

**Labels.**
- **Cat A** = exact or proved. This includes exact finite computations, which are flagged as such.
- **Cat B** = numerical, empirical or conjectural.

No TPC or RH claims are made.

## 0. Verdict

| Question | Answer | Cat |
|---|---|---|
| Rule at the level of the **function span** of the lift family | **False.** Cuspidal functions occur for every odd s tested (5..25, 41) and for every even s tested except 6, 8, 10. This is independent of h⁺ vs genera. The controls s = 5, 7, 9, 13, 15 have h⁺ = genera and cusp dimension 2, 6, 12, 30, 84. | B (floating SVD ranks, gap- and Q_max-stable). The s = 7 value 36 + 6 matches the independent V42 result. |
| Rule at the level of **u_L / E_s** (the object the s = 11 result was about) | **False as an "exactly when".** h⁺ ≠ genera ⇒ cusp holds at all 5 tested s (11, 19, 21, 25, 41). The converse fails at **s = 14, 17, 18, 22, 23**, where h⁺ = genera but u_L has non-genus (dihedral cusp) content. | A for the finite exact ray-class computation (conditions in §2.3). The extension to all norms is B. |
| What decides it | The exact criterion: the σ-symmetrised class set of E_s in the narrow ray class group G = Cl⁺_m is (1−σ)G-invariant. h⁺/genera = \|Cl⁺(O)²\| only bounds this. | A (criterion: Tate's theorem plus the content dictionary); A on the computed range |

## 1. Function-span method (lift labels to forms, count Eis vs cusp)

### 1.1 Method
`funcspan.py` (from the interrupted run, unchanged; driver `run_funcspan.py`):
- C is the exact Fourier-coefficient matrix (labels × modes) of the S/T theta-lift family u_{α,β} of A_s = [[2,s],[s,s]]. It is built from cone sums over γ-fundamental domains, as in the s = 7 V42 work.
- V = the column span of C, i.e. the span of the values of u.
- W = the SL₂(Z)-cyclic span of the constant-term vector.

**Exactness of the count (new remark; Cat A given the λ = 1/4 constant-term criterion).** Every function in the span has the form λ·u.
- λ·u is cuspidal ⇔ its constant terms vanish at all cusps ⇔ λ ⊥ ρ(g)c for all g ⇔ λ ⊥ W.
- Hence V_Eis := (values of u_Eis) = W.
- Since W ⊂ V, the space of genuinely **cuspidal functions in the span** has dimension **exactly dim V − dim W**, and the Eisenstein projection has rank exactly dim W.
- The interrupted run called V − W a "lower bound". It is a lower bound only for the rank of the cusp *projection*, which can exceed V − W when V_Eis ∩ V_cusp ≠ 0. That is what happens for u_L at s = 11.

### 1.2 Results (`funcspan_table.txt`; all stable under Q_max 25 → 40)

| s | h⁺ | genera | labels | dim V | dim W (Eis) | **cusp = V − W** | h⁺ ≠ gen? |
|---|---|---|---|---|---|---|---|
| 5 | 4 | 4 | 60 | 20 | 18 | **2** | no |
| 6 | 2 | 2 | 24 | 12 | 12 | 0 | no |
| 7 | 4 | 4 | 140 | 42 | 36 | **6** | no |
| 8 | 2 | 2 | 48 | 18 | 18 | 0 | no |
| 9 | 4 | 4 | 252 | 72 | 60 | **12** | no |
| 10 | 2 | 2 | 80 | 30 | 30 | 0 | no |
| 11 | 8 | 4 | 396 | 110 | 90 | **20** | yes |
| 12 | 4 | 4 | 120 | 42 | 36 | **6** | no |
| 13 | 4 | 4 | 572 | 156 | 126 | **30** | no |
| 14 | 4 | 4 | 168 | 56 | 48 | **8** | no |
| 15 | 8 | 8 | 780 | 210 | 126 | **84** | no |
| 16 | 4 | 4 | 224 | 72 | 48 | **24** | no |
| 17 | 8 | 8 | 1020 | 272 | 162 | **110** | no |
| 18 | 4 | 4 | 288 | 84 | 60 | **24** | no |
| 19 | 8 | 4 | 1292 | 342 | 270 | **72** | yes |
| 20 | 4 | 4 | 360 | 110 | 90 | **20** | no |
| 21 | 16 | 8 | 1596 | 420 | 240 | **180** | yes |
| 22 | 4 | 4 | 440 | 132 | 108 | **24** | no |
| 23 | 8 | 8 | 1932 | 506 | 288 | **218** | no |
| 24 | 4 | 4 | 528 | 156 | 120 | **36** | no |
| 25 | 12 | 4 | 2300 | 600 | 468 | **132** | yes |
| 41 | 24 | 8 | 6396 | 1640 | 882 | **758** | yes |

(h⁺ and genera are from `classgroup.py`, i.e. reduced-form cycles. The interrupted run cross-checked them against PARI.)

**Empirical closed forms for odd s (Cat B; 12 of 12 odd s fit, `funcspan_table.txt`):**
- dim V = s(s−1)
- dim W = 3·∏_{p^e ∥ s(s−2)} (p^e+1)/2

For s = 7 this is the local tensor pattern 3·3·4 of the Tensor-Pattern report (A₃ ⊗ W₅⁺ ⊗ W₇⁺), so the formula reads as "Eisenstein = A₃ ⊗ (⊗_p even Weil half)".

If both formulas hold, superadditivity of (q+1)/2 gives dim W ≤ 3(s²−1)/4, with equality iff s and s−2 are prime powers. Then cusp ≥ (s−1)(s−3)/4 > 0 for every odd s ≥ 5. That inequality is elementary given the formulas, but the formulas themselves are Cat B.

Even s: dim V = (s/2)(s/2+1) except at s = 8 and 18 (s/2 a square). The cusp part is 0 only at s = 6, 8, 10 among the tested even s. No even-s formula is claimed.

**Answer at family level:** the rule fails. Cusp functions are generic and appear with h⁺ = genera (5, 7, 9, 12–18, 20, 22–24). [B]

## 2. u_L level: exact ray-class genus test (new, PARI)

### 2.1 Method (`uL_rayclass_exact.py`)
This replaces the prime-periodicity statistics of the interrupted run with exact finite-group computations.

1. **Setup.** E_s = q^{c₀}E_L is the sum over ν ∈ F∩(a+Z²), with F = [e₁, γe₁). Each ν gives an ideal 𝔞(ν) = (β)/𝔡′ in K = Q(√(s²−2s)), where β = (2X₁+sX₂) + cX₂√D₀ and X = dν. Take the modulus 𝔪 = M∞₁∞₂ with M = 2dc, d = 2(s−2) and s²−2s = c²D₀. Split 𝔞 = 𝔠·𝔞′, where 𝔞′ is coprime to M. For each M-part 𝔠, f_𝔠 is the indicator of the set of classes [𝔞′] in G = Cl⁺_𝔪.
2. **Union-of-classes check (exact).** For every n ≤ N_max: #{ν : N𝔞 = n} = μ·Σ_{(𝔠,g) hit} #{𝔟 ∈ g : N𝔟 = n/N𝔠}. This is checked against PARI's ideal list. A part is "complete" when every class of G contains an ideal of norm ≤ N_max/N𝔠. In that case, dev = 0 forces the E-set (to that norm) to be exactly the union of the hit classes.
3. **Genus test.**
   - Genus characters are the σ-invariant characters, i.e. those trivial on H = (1−σ)G. This uses Tate: ker N = C_K^{1−σ} for cyclic K/Q.
   - u_L is Eisenstein ⇔ f̃_𝔠 = f_𝔠 + f_𝔠∘σ, restricted to pure infinity types (the projection with j = [(M−1)]), is H-invariant for every 𝔠.
   - The non-genus pure characters with nonzero content are counted by an FFT on G. Each σ-orbit has size 2 and gives one dihedral Maass cusp form with λ = 1/4.
4. **Bug found and fixed during this run.** A first version used K_N = ker(N mod M) instead of H. That misses genus characters ψ∘N of conductor ∤ M (e.g. χ₋₃∘N at s = 15) and gave a false "cusp" verdict at s = 15. That output is kept as `SUPERSEDED_buggy_KN_genus_test_uL_rayclass_run1.json`. All numbers below use H.

**Validation (`uL_rayclass_validate_7_8_11.txt`):**
- s = 7: Eis
- s = 8: Eis (both 𝔠-parts complete)
- s = 11: CUSP, with exactly **12 non-genus pure characters of orders 4 and 12**, i.e. 6 dihedral Maass forms. This is the same as the independent s8-s11 report.

### 2.2 Results (`uL_rayclass_main.txt`, `uL_rayclass_18_20_25.txt`; N_max = 20000, or 80000 for s = 18, 20, 25)

| s | h⁺ | gen | \|Cl⁺²\| | M | \|G\| | \|H\| | u_L | non-genus pure chars (→ forms) | rule predicts | agrees |
|---|---|---|---|---|---|---|---|---|---|---|
| 5 | 4 | 4 | 1 | 12 | 16 | 2 | Eis | 0 | Eis | ✓ |
| 6 | 2 | 2 | 1 | 32 | 64 | 2 | Eis | 0 | Eis | ✓ |
| 7 | 4 | 4 | 1 | 20 | 32 | 2 | Eis | 0 | Eis | ✓ |
| 8 | 2 | 2 | 1 | 96 | 128 | 4 | Eis | 0 | Eis | ✓ |
| 9 | 4 | 4 | 1 | 84 | 96 | 4 | Eis* | 0 | Eis | ✓ |
| 10 | 2 | 2 | 1 | 128 | 128 | 2 | Eis | 0 | Eis | ✓ |
| 11 | 8 | 4 | 2 | 108 | 288 | 4 | **CUSP** | 12 (6) | cusp | ✓ |
| 12 | 4 | 4 | 1 | 80 | 256 | 4 | Eis | 0 | Eis | ✓ |
| 13 | 4 | 4 | 1 | 44 | 80 | 2 | Eis | 0 | Eis | ✓ |
| 14 | 4 | 4 | 1 | 96 | 256 | 4 | **CUSP** | 8 (4) | Eis | **✗** |
| 15 | 8 | 8 | 1 | 52 | 192 | 2 | Eis | 0 | Eis | ✓ |
| 16 | 4 | 4 | 1 | 224 | 768 | 8 | Eis* | 0 | Eis | ✓ |
| 17 | 8 | 8 | 1 | 60 | 128 | 4 | **CUSP** | 16 (8) | Eis | **✗** |
| 18 | 4 | 4 | 1 | 768 | 2048 | 8 | **CUSP** | 16 (8) | Eis | **✗** |
| 19 | 8 | 4 | 2 | 68 | 256 | 4 | **CUSP** | 32 (16) | cusp | ✓ |
| 20 | 4 | 4 | 1 | 432 | 1152 | 4 | Eis | 0 | Eis | ✓ |
| 21 | 16 | 8 | 2 | 76 | 576 | 4 | **CUSP** | 72 (36) | cusp | ✓ |
| 22 | 4 | 4 | 1 | 160 | 512 | 4 | **CUSP** | 16 (8) | Eis | **✗** |
| 23 | 8 | 8 | 1 | 84 | 192 | 4 | **CUSP** | 24 (12) | Eis | **✗** |
| 24 | 4 | 4 | 1 | 352 | 640 | 4 | Eis* | 0 | Eis | ✓ |
| 25 | 12 | 4 | 3 | 460 | 2112 | 12 | **CUSP** | 88 (44) | cusp | ✓ |
| 41 | 24 | 8 | 3 | 156 | 1152 | 12 | **CUSP** | 240 (120) | cusp | ✓ |

Notes on the table:
- **Eis\*** means Eisenstein on the coprime part and on every complete 𝔠-part. Some deep 𝔠-parts were not complete within N_max: 3-power parts at s = 9, the 𝔭₂ part at s = 16, and 2-power parts at s = 24. They are **unresolved**, not shown Eisenstein.
- **Every CUSP verdict comes from a complete part**, so CUSP needs no extra range.
- **Stability under M → 2M** (`uL_rayclass_M2_stability.txt`):
  - same verdicts at s = 7, 14, 15;
  - same counts at s = 11 (12) and s = 19 (32), complete at N_max = 80000;
  - s = 41 reaches 4595 of 4608 classes at 2M with the same count (240).
- **Correction to the interrupted run:** s = 21 has **72** non-genus pure characters (36 forms). The 108 in its partial output came from the K_N bug.
- The u_L verdicts agree with the interrupted run's prime-periodicity verdicts at every s. The five counterexamples are therefore confirmed by an independent exact method.

### 2.3 Status
- **Cat A (exact, finite).** For each listed s:
  - the class-group data;
  - the union-of-classes property up to N_max;
  - H-invariance or its failure on the complete parts;
  - the resulting verdicts, given two inputs:
    - (i) the dictionary "u_L's Maass content = pure-type character content of E's class sets", as used in the s8-s11 and psiEis reports;
    - (ii) Tate's ker N = C_K^{1−σ}.
- **Cat B:**
  - That M = 2dc is a sufficient modulus for all norms. It is stable under 2M wherever checked, but not proved.
  - The character counts, which come from floating FFT with a threshold. They are integers, stable, and match s = 11 independently.
- **Proved direction (from the interrupted run; A modulo the dictionary).** |Cl⁺²| ≥ 5 ⇒ u_L has cusp content. None of the tested s reaches 5 (the maximum is 3 at s = 25 and 41). So at the user's s = 19, 25, 41 the cusp content rests on the exact finite computation above, not on that lemma.

## 3. Answer to Task A
- **"Cusp part ⇔ h⁺ ≠ #genera" is false** at both levels.
  - At u_L level, the forward direction (h⁺ ≠ genera ⇒ cusp) held in 5 of 5 cases: 11, 19, 21, 25, 41. Proved only when |Cl⁺²| ≥ 5.
  - The reverse direction fails at 14, 17, 18, 22, 23.
- **The correct invariant** is whether the σ-symmetrised E-class set is a union of (1−σ)Cl⁺_𝔪-cosets.
  - (1−σ)Cl⁺_𝔪 surjects onto Cl⁺(O)², which is why h⁺ ≠ genera usually forces cusp content.
  - But it also contains the ray part (O/𝔪)^×/units, which is non-trivial at 14, 17, 18, 22, 23.
  - |H| alone does not decide: |H| = 4 occurs for both Eis (s = 8, 9, 12, 20, 24) and cusp (s = 14, 17, 22, 23).

## 4. Open
- An arithmetic closed criterion in s for the H-invariance. One is not found; the observed u_L-cusp set in 5..25 is {11, 14, 17, 18, 19, 21, 22, 23, 25}.
- Proofs of the odd-s dimension formulas for V and W, and an even-s formula.
- The deep 𝔠-parts at s = 9, 16, 24.
- Exact (rational/cyclotomic) certification of the SVD ranks.
- A proof that M = 2dc suffices.

## 5. Files (`2026-10-18-Cusp-Onset/`)
- **Function span:** funcspan.py, run_funcspan.py, family_s.py, funcspan_*.json/txt, funcspan_table.txt
- **Exact u_L test:** uL_rayclass_exact.py, summarize_rc.py, uL_rayclass_validate_7_8_11.txt, uL_rayclass_main.txt, uL_rayclass_18_20_25.txt, uL_rayclass_M2_stability.txt, the *.json outputs and logs, and SUPERSEDED_buggy_KN_genus_test_uL_rayclass_run1.json (kept for the record)
- **From the interrupted run:** classgroup.py/txt, uL_periodicity*.py/txt, uL_modulus_check.*, uL_rule_table.txt

## 6. Differences from the interrupted combined report
- **S41 placeholders filled:** V = 1640, W = 882, cusp = 758.
- **"cusp ≥" corrected:** V − W is the *exact* dimension of the cuspidal functions in the span.
- **s = 21 count corrected** to 72 characters (36 forms).
- **Counterexamples upgraded** from prime statistics (B-strong) to the exact finite computation (A, conditional as stated).
- **New controls:** s = 5, 6 and 14–24 for the function span.
