# Implications of the 17–19 Oct Bridge-C work for (1) the 5th Order of Unification, (2) Residual Ternary Algebra, (3) Even multi-k, (4) K3 cohomology
Date: 2026-10-19, written 08:48–09:40 CDT. Read-only pass. Nothing was pushed, sent or submitted, and no existing file was edited. The only new files are this report and the folder `2026-10-19-Implications-checks/` (`checks.py`/`checks.json`, `weil5.py`/`weil5.json`, `cvals.py`/`cvals.json`).

**Labels.** **Cat A** means proved, or exact, including exact finite computation and "conditional on a named cited theorem". **Cat B** means numerical only, PSLQ, citation-only identification, interpretation, analogy, or conjecture.

**Scope.** No TPC or RH claims. This is separate from the HQCC termination claims. No lepton, Orch-OR or neuroscience material is used. The new checks are labelled IC-1 … IC-7, which avoids the L-series labels.

**Sources.** The definitions are quoted from the local Master clone `/workspace/quantum-comp/oct17-master` (tip 48684e3, 2026-10-14 21:40 CDT). Below, `BOOK/` means `oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/`. Two other source notes:
- The GitHub tip is now 1ec3baa ("Rev6 (15/15)", 2026-10-18 22:14 CDT). GitHub code search returns no hits for this repo (not indexed), so the definitions were taken from the clone. The Rev6 commits add Bridge-C material and do not touch the definition files cited here.
- `2026-10-19-Bridge-C-Consolidated-rev7/bridge_c_consolidated_rev7.tex` is currently **byte-identical** to rev6 (`diff`: 0 lines), so "rev6" below also covers rev7 as it stands.

---

## 0. Where each term is defined (STEP 1)

| Term | Found? | Exact source(s) |
|---|---|---|
| 5th / Fifth Order (of) Unification | **Yes**, as "fifth-order unification". The exact string "Order of Unification" does **not** occur. | `BOOK/Theorem_Lemma_Chain_9_Maths_Fifth_Order_and_Full_Model_2026-08-26.md` l.7; `BOOK/Discrete_Bridge_E8_to_Fifth_Order_2026-08-24.md`; `BOOK/Executive_Summary_2026-09-17_Needed_Ingredients.md` l.10–12; `BOOK/Master_Glossary_S2-11DM2ET-X_2026-10-02_rev2.md` l.144, 155–156; `oct17-master/PAPERS.md` l.12–14 (portal file name "Final draft__5th Order Unification and Residual Ternary Algebra.docx") |
| Residual Ternary Algebra (RTA) | **Yes** | `BOOK/Residual_Ternary_Algebra_Full_Manuscript_Draft_2026-08-24.md` (full text); `BOOK/Executive_Summary_2026-09-16_Explore_Residual_Ternary_Algebra.md`; `PAPERS.md` l.10–16. The bare token "RTA" is not used in the corpus as an abbreviation. |
| Even multi-k | **Yes**, as "**Pure-even multi-k** families" (Bring–Jerrard / A₅). No other meaning is defined. | `quantum-comp/drive/extracts/pure-even-multi-k.md`; `quantum-comp/drive/ADVANCEMENTS.md` §8 (l.391–420); `BOOK/U1_E2_MONO_Continuous_Necessity_Monodromy_2026-08-18.md` l.9–18; `BOOK/N1_A5_S5_Quintic_Evenness_Necessity_2026-08-16.md` l.7, 19. The `multi_k` hits in `R-FFT/registry` and `run_rfft_observatory.py` are an unrelated dataset key. |
| K3 / K3 cohomology | **Yes**, only as Cat B scaffolding | `BOOK/Ramanujan_Hampton_Saha_Sinha_Bhat_K3_Resonant_Unification.md`; `BOOK/Ramanujan_Mock_Theta_K3_Zenodo_Deposit_Note_2026-08-06.md` (Zenodo 21817875); `drive/extracts/ramanujan-mock-theta-k3.md`; `drive/ADVANCEMENTS.md` §9 (non-canonical 9-Maths list, item 4) |
| Zenodo 21514429 "9 Maths of Unification" | Record metadata read (API) | `https://zenodo.org/api/records/21514429` (Theorem–Lemma Chain for the 9 Maths of Unification, 2026-07-23). The abstract does not use "fifth order", "K3" or "multi-k". |
| Supplement text `artifacts/Ramanujan_Journal_Submission_2026-08-25/Theorem_Lemma_Chain_9_Maths_Residual_Contacts.txt` | **Not found** | Not in the local clone, and GitHub returns "path does not exist". Its contents are therefore not used here. |

---

## 1. The 5th Order of Unification

### (a) What it claims and what it needs (quoted)
- `BOOK/Theorem_Lemma_Chain_9_Maths_…_2026-08-26.md` l.7: "Peer review is invited only for the pure-math manuscript: Residual Ternary Algebra and **fifth-order unification through that algebra**."
- `BOOK/Discrete_Bridge_E8_to_Fifth_Order_2026-08-24.md` §2, steps 1–4. E8 Weyl arithmetic leads to PW(7,11;3⁵), which leads to "Packaging under Principle (S) therefore selects the residual values s ∈ {7,8,11}", which leads to "The series g_s(q) = Σ q^{n²}/(−q^s;q^s)_n recovers the classical shape of Ramanujan's fifth-order mock theta function f0 at the ordinary value s=1, and specialises at the residual values selected by packaging." §3: "[C7's] continuous modular law (exact weight-1/2 slash identity and quantitative continuous Fricke match) remains open and is not required for the discrete bridge."
- `BOOK/Executive_Summary_2026-09-17_Needed_Ingredients.md` l.10–12: "Fifth-order unification is a bundle, not one path. Missing: **a coefficient-emitting map (or retirement of the functor claim), plus a unique completed period and tail for C.**"
- `BOOK/Master_Glossary_…_rev2.md`: l.144 "g_s, g_7. Fifth-order residual series and the s=7 member." l.155–156 "PW. No functor. Contact numerical." "E8 functor. Not locked."

So the "fifth order" of the programme needs three things:
- (N1) a map that emits coefficients, carrying E8/PW data to the series. A functor is currently **not** locked.
- (N2) a unique completed period for C.
- (N3) a tail for C.

### (b) Results that bear on it
1. **(N2) The completed period exists only in vector-valued form; a scalar one is excluded.**
   - Cat A, conditional on Baker and the q-expansion principle for (i): rev6 Theorem E rules out every scalar additive modular, mock (signature (1,1)), unary, partial or false theta law up to o(1/t). Theorem E(ii) rules out every quotient law C·g = F, and E(iii) every scalar W₇ slash law.
   - Cat A, proved and audited once: Theorems F and G (140-label Siegel lift to λ = ¼ Maass forms; Lewis–Zagier period formula, real-analytic on ℝ∖{0}).
   - Cat A, given the inputs I1–I3: Theorems I and J (closed Herglotz form of the cocycle).
   - Net effect: the "completed period for C" required by N2 is supplied **as a 140-component vector cocycle**, not as a scalar period. Whether it is "unique" in the sense of the 09-17 summary is not addressed by any theorem; uniqueness is **open**.
2. **(N3) The tail is supplied exactly at x = 0, x = ½ and x = ⅓ through high order.**
   - Cat A: closed forms through t^{17/2} at x = 0 of the shape √(2πs)[R_e + S_e√Δ], Δ = (s−2)(7s−32) (Analytic-CatB-Push, Round 4, G.1). Also t^{11/2} and t^{13/2} at x = ½ and x = ⅓, the period-72 theorem at x = ⅓, and the general-N periodicity and Gauss evaluation (Theorems 2 and 3 there). The CRT Factorization Proposition (CFP) gives periods 16 and 96, and the six N = 8 classes are pairwise distinct (F.2).
   - This turns RTA's "qualitative residual defect markers" into exact continuous radial targets.
   - The tail is **not** given at all rationals in closed form. t^{19/2} and beyond are not computed.
3. **The special role of s = 7 comes from a frozen choice, not from structure** (Cat A; Algebraic-Round3 §5–§7).
   - 7s − 32 = −2Q(c₂) is a property of the cone edge c₂ = (−4,1), which was locked for s = 7 and then frozen.
   - Within c₁ + ℤe₁, c₂ is forced only at s = 7, and only under two selection conditions. That selection rule is Cat B as motivation.
   - It is **not** unique among all primitive vectors, and it is not forced for s ≠ 7.
   - The axes cone c₂ ∝ (−s,2) gives C_mixed ≡ 0 and closed forms in ℚ(√(2s)).
   - The universal piece R_e does not depend on the wall (proved t^{−1/2} … t^{13/2}).
   - Implication: closed-form evidence does **not** single out the packaging values s ∈ {7,8,11}. The Bridge-C mathematics is uniform in s: the tensor theorem holds for all odd s, the closed forms are rational in s, and Theorem G_s holds for all real s > 0. The values that are structurally special in this work are s = 5 (H₅ ≡ 0, and every c_e(5) = 0) and s = 8 (frozen = axes, Δ = 144 = 12²), not s = 7 or s = 11. This does not refute the discrete bridge, which is a packaging statement. It does mean the Bridge-C results give **no independent support** for the selection step 3 of the discrete bridge (Cat A for the facts; the "no support" reading is Cat B).
4. **The f₀ contact stays at the level of the series shape, not the lattice** (Cat A).
   - g₁ = f₀ by definition (Hickerson–Mortenson eq. (4.5), per `2026-10-17-Residual-Identities-Mock-Theta-Status.md` A2).
   - The Bridge-C lattice M = [[2,s],[s,s]] has det = −s(s−2). That is positive for 0 < s < 2, so at s = 1 the lattice is **definite**, not of signature (1,1), and H_s is Zwegers-admissible only for integer s ≥ 5 (rev6 App. "Closed forms for g_s").
   - So the indefinite-lattice part of the RTA (H_s, C, ℚ(√(s(s−2)))) does **not** specialise to the classical fifth-order Hecke-type structure. That structure lives over ℚ(√5) (Andrews; Zwegers). The fifth-order link is carried only by g_s at s = 1.
5. **Theorem G_s** (Cat A, elementary proof, quick audit in rev3).
   - g_s(e^{−t}) ~ Σ c_k(s)t^k with c_k ∈ ℚ[s] of exact degree k, and with no t^{−1} or half-integer terms, for all real s > 0.
   - g_s ∉ span_ℚ{1, θ₃, R, M_m} (exact rank to q⁴⁰⁰, s = 3..20, 25, 30, 41).
   - This gives the "fifth-order residual series" a proved radial expansion at x = 0 that is uniform in s and agrees with f₀ at s = 1. It does **not** settle quantum modularity of g_s, which the glossary lists as a conjecture.
6. **(N1) The coefficient-emitting map / E8 functor: no bearing.** None of the work touches E8, PW(7,11;3⁵) or any functor. Status unchanged: "No functor", "E8 functor. Not locked."

### (c) What changes
- **Strengthened (A):** N2 and N3 are now answered **in the vector-valued sense**. The scalar part of N2 is settled **negatively** (Theorem E).
- **Needs correction or rewording:**
  - Any statement that the fifth-order bridge needs a scalar "weight-1/2 slash identity" for C. That route is closed (Theorem E(iii)).
  - Any implication that the s = 7 closed forms are intrinsic to s = 7. The (7s−32)-dependence comes from the frozen c₂ choice (Algebraic-Round3 §5(c), §6.2).
- **Not refuted:** the discrete bridge E8 → PW → {7,8,11} → g_s, which is a packaging statement. It also gains no support from this work.

### (d) Open
- N1: a functor or coefficient-emitting map, or its retirement.
- Uniqueness of the vector-valued completed period.
- Radial tails at general rationals in closed form, and t^{19/2} onward.
- Quantum modularity of g_s itself.
- Whether a canonical s-dependent cone, such as the axes cone, should replace the frozen c₂ in the definition. That is a definitional choice for the author, and CORE_FREEZE currently keeps the frozen cone.

---

## 2. Residual Ternary Algebra (Ramanujan Journal v1.0, submitted 2026-08-26, ID c0edfefa-a14d-4b51-b5e3-bf60ee7eca3a)

### (a) What it claims and needs (quoted from `BOOK/Residual_Ternary_Algebra_Full_Manuscript_Draft_2026-08-24.md`)
- Abstract l.15: "The residual law for C — the exact weight-1/2 slash prefactor identity and quantitative continuous Fricke verification against residual samples — remains open; the samples themselves are treated only as qualitative residual defect markers. Classical Zwegers completion applies to the cone series H_s."
- §9 l.166–190: M = [[2,s],[s,s]]; Q_s = n² + snk + (s/2)k(k+1); "Locked residual cones of negative norm (case s = 7) are c1 = (−1,1) and c2 = (−4,1)"; C := P_orth − H_s; "Through degree 100 the coefficients of C take values only in {0,1,1.5}".
- §10 l.202: "chi_nat(s) = (s/(2(s−2)), −1/(s−2))".
- §11 l.214–216: "residual weight-3/2 shadow Ξ … residual disc-35 series"; "A residual period-function candidate of weight 1/2 is the formal residual Eichler integral of … Ξ. Holomorphic projection recovers C by the locked rewrite."
- §12 l.222–226: "Three residual slash-factor candidates … None recovers a quantitative match … Residual constant × residual automorphy therefore fails. The residual identity for the exact weight-1/2 slash prefactor remains the primary open obstruction." Also: "Quantum modularity of g_s and of C is stated as an open residual conjecture."
- `PAPERS.md` l.10: "No acceptance is claimed. Residual law for Bridge Series C remains open."

### (b) Results that bear on it
1. **The residual law as formulated is settled in the negative, in scalar form.**
   - Cat A: rev6 Theorem E; `2026-10-17-Bridge-C-Residual-Law.md` verdict items 2–4.
   - Leading radial term: C(e^{−t}) = I/t + a_C t^{−1/2} + …, with I = log(6+√35)/(2√35) (Theorem C; a_C is a proved closed form modulo F1).
   - Baker gives log(6+√35) ∉ ℚ̄ + πℚ̄. Hence no additive law with algebraic modular, mock or theta pieces exists up to o(1/t) (E(i), conditional on Baker and the q-expansion principle).
   - There is no quotient law (E(ii)).
   - There is no scalar W₇ law (C − λ(7τ)^{−k}C(−1/(7τ)) bounded) for **any** weight k and any constant λ. This is an exact finite computation: 178 of 270 test rationals, including the Master sample x = 5/7 (E(iii)).
   - This is exactly the "exact weight-1/2 slash prefactor identity" of §12, and it cannot exist. RTA §12's own finding, "Residual constant × residual automorphy therefore fails", is confirmed and now **proved**.
2. **The correct weight is 1, not ½** (Cat A).
   - Where both Gauss means are nonzero, |G| obeys an exact **weight-1** relation with |λ| = 7^{−1/2} (`2026-10-17-Bridge-C-Residual-Law.md` item 4).
   - The leading 1/t radial profiles obey the S/T law with factor 1/|x| (rev6, profile law proved by Poisson summation in rev3).
   - The vector cocycle is the weight-1 object with automorphy factor |cx+d| (Theorem G).
   - So the "weight 1/2" in §11–§12 is the wrong weight for the law that exists.
3. **What replaces it is an explicit vector-valued law** (Cat A as stated in rev6).
   - P_s, the shared remainder of C and C_third (Theorem A), is, up to theta and mock pieces, one ray-class partial theta series of ℚ(√35) (Theorem B).
   - The 140-label Siegel lift, the 72-dimensional PSL₂(ℤ) label representation, and the 42-dimensional function span V = V_Eis(36) ⊕ V_cusp(6) (Theorem H, exact since rev4).
   - The Lewis–Zagier period function and the Herglotz closed form (Theorems G, I, J).
   - For all odd s, the tensor theorem ρ = ρ_(s) ⊗ ρ_(s−2) ⊗ ρ₂. Sectors with ε_all = −1 vanish, and the odd-parity sectors are cusp (proved lemma plus exact factorisation; Open-Algebraic item 5; Symmetry-Audit rows 1–5 "SOUND").
   - This is the "residual-admissible" positive answer that §12 lacked. It is a law for the **vector of cone sums**, not for scalar C.
4. **The samples have been replaced** (Cat A). The four published samples are not radial values of C: C(0.995·e^{2πix}) has modulus about 19.5, 18.5, 19.9 and 54.0, against 19.80, 1.82, 9.24 and 20.90. They are replaced by the exact radial targets lim t·C(e(x)e^{−t}) = I·G(x) at every rational x (Theorem D).
5. **χ_nat is confirmed as the right characteristic** (Cat A). RTA §10's χ_nat(s) = (s/(2(s−2)), −1/(s−2)) is exactly the a_char of Analytic-CatB-Push Theorem 3: completing the square gives Q₊(ν) = Q₂(ν + a_char) + c₀, with c₀ = s/(4(s−2)). It enters the Gauss evaluation H(c) = 2(aQ₂(u₂)/p)g_p e((a/p)[−g²(c+δ)²/(2(7s−32)) + c₀]).
6. **The cones need a note** (Cat A). §9 locks c₁ and c₂ "case s = 7" but uses s ∈ {7,8,11}.
   - c₁ = (−1,1) is forced by the wall n = 0 (§6.1).
   - c₂ = (−4,1) is forced at s = 7 only within b = 1, and is not forced for s ≠ 7. Edge-class invariance H^{(c₁,c_a)} = H^{(c₁,c_{s−a})} is proved (Algebraic-Round3 §5(b)).
   - rev6 Theorem A(iv): C_mixed vanishes through q²⁹³ but not identically.
7. **Two small factual points in the manuscript text** (Cat A; new exact checks in this pass, `2026-10-19-Implications-checks/`):
   - **IC-1 (coefficient values of C).** With the §9 definitions (s = 7, c₁ = (−1,1), c₂ = (−4,1)), the coefficients of C lie in {0, 1, 3/2} through q¹⁰¹. The first coefficient outside that set is **[q¹⁰²]C = 2**, coming from C_third. Through q⁴¹⁹ the value set is {0, ½, 1, 3/2, 2, 3}, with [q¹⁴⁴]C = 3 and the ½-values from C_mixed (`cvals.json`).
     - The script reproduces rev6 Theorem A(iv) exactly: C_mixed = −½q²⁹⁴ + ½q³⁰¹ − q³³⁰ + q³³⁷ − q³⁶⁸ + q³⁷⁵ …
     - The manuscript's "through degree 100" is literally true, but a reader may take it as structural. A revision should say that it is a finite-range observation and that the value set grows.
   - **IC-2 (two objects named P_s).** §7 defines P_s := (−q^s;q^s)_∞·g_s. §9 uses P_s for the orthant path count Σ_{n,k≥0} q^{Q_s}. At s = 7 these differ first at q¹⁴ (coefficients 1 vs 0; `checks.json`), because of the extra 1/(q^s;q^s)_k. rev6 uses P_s in the §9 sense. A revision should rename one of them.
8. **RTA §11 "Holomorphic projection recovers C"** (Cat A for the growth argument, using the standard t^{−1/2} radial growth bound for weight-½ harmonic Maass forms, which is cited).
   - Any weight-½ object has leading radial order t^{−1/2}, so it cannot carry C's I/t term.
   - Whatever Ξ and its Eichler integral are, they cannot *be* the residual law for C. At best they describe pieces of C. The sentence should be restated with that qualification.
   - That Ξ is "disc-35" agrees with Theorem B (ℚ(√35)); this is Cat B as an identification, since Ξ is only formally defined in the manuscript.
9. **Unaffected:** §2–§5 (T3, B′ = 539, 3·68 + 5·67, 18 + 521, Λ_B), §6 Prop 6.2 (g₇ residues), §8 (Euler collapse). §13's statement that classical Zwegers completion applies to H_s is consistent with rev6, where H_s is Zwegers-admissible for integer s ≥ 5.

### (c) Does the work settle the "residual law for Bridge Series C"?
**Yes for the scalar question as posed, and the answer is negative (Cat A). In the positive direction it is advanced to an explicit vector-valued law (Cat A as labelled in rev6).** The work does **not** prove the "quantitative continuous Fricke verification against residual samples", because those samples are shown not to be radial values of C. Quantum modularity of scalar C, and of g_s, remains unclaimed. rev6 says explicitly: "We do not claim that C, C_third or P_s is modular, mock modular, or quantum modular as a scalar q-series."

**What a revision would say.** This is draft wording only. Following the standing advice, leave the submitted v1.0 as is and use it only if the journal requests a revision, drawing on rev6/rev7.
- *Abstract*, replacing "remains open":
  > "We show that no scalar residual law exists: C has the radial singularity I/t with I = log(6+√35)/(2√35), and by Baker's theorem no identity with algebraic modular, mock or theta pieces up to o(1/t), no quotient law, and no scalar W₇ slash law of any weight holds. The obstruction is resolved by a vector-valued weight-1 law: the fundamental-domain cone sums form a 140-component cocycle given by a Lewis–Zagier period formula for λ = ¼ Maass forms obtained by a Siegel theta lift over ℚ(√35)."
- §12: replace "primary open obstruction" with a statement of Theorems C and E, plus a pointer to the vector-valued law (Theorems F, G, H). Move the four samples to a remark saying they are not radial values of C.
- §11: reword the "weight 1/2" period candidate per item 8, or drop it.
- §9: apply IC-1, IC-2 and the cone note of item 6.
- Keep, as open: uniqueness of the vector completion; quantum modularity of scalar C and of g_s; and that H_s, C and P_s are not claimed modular as scalar q-series.
- Cite rev6 as the consolidated internal working paper, which is not externally refereed. Do not import the Cat-B items (Theorem K; PSLQ-only items) as theorems.

### (d) Open
- Uniqueness or normalisation of the vector completion.
- The exact rank of the lift relations at m = 17, 31, …: Proposition K1 gives proved upper bounds, and sharpness is open.
- The general-p (C3) statement without citation.
- s = 121 and s = 3481 full runs.
- t^{19/2} and beyond.
- Quantum modularity of g_s.
- Whether the author wants the frozen c₂ kept (CORE_FREEZE) or an s-canonical cone in a revision.

---

## 3. Even multi-k

### (a) What it claims and needs (quoted)
- `drive/extracts/pure-even-multi-k.md` (Drive `1cpRxyTmihGuswwxA0fsi7-N1xt7ogwF_9B6i1i0zPio`), Theorem 3.1: "α(m)=256m² − 3125k⁴/256, β(m)=k·α(m); disc(x⁵+α(m)x+β(m)) = (256α(m)²m)²." The seeds are x⁵−55x+88 (A₅), x⁵−100x+400 (A₅), x⁵+20x+16 (A₅) and x⁵+20x−32 (D₅). "Open: density of A₅ fibres; A₅ vs D₅ criterion; Nielsen-labelled Hurwitz multi-k fusion."
- `BOOK/U1_E2_MONO_Continuous_Necessity_Monodromy_2026-08-18.md` l.9, 13: "Success criterion (locked): an explicit continuous monodromy representation or character variety of multi-k A5 type (5A² 5B², lift −1, braid orbit 12) that forces Necessity without residual evenness import"; "Pure-even multi-k paths are explicit ℚ(t) models of geometric A5-covers of type 5A² 5B² with lift invariant −1 (braid orbit size 12)."
- `BOOK/N1_A5_S5_…_2026-08-16.md` l.19: "the alternating group A5 cannot be forced from the discrete residual core alone … Fibre density and the Necessity theorem remain STILL OPEN."

### (b) Results that bear on it
1. **Direct bearing: none.** The Bridge-C work never touches Bring–Jerrard quintics, Hurwitz spaces or Galois groups of quintic fibres.
2. **Name collisions, not identifications** (the corpus itself warns against "name-collision-as-identification", `BOOK/Review_Missed_Variables_After_2026-09-16_Lean_C_GF.md`):
   - "even" in Bridge C means even s, or even parts of Weil representations (−1-eigenspaces); in multi-k it means square discriminant (Gal ⊂ A₅).
   - "k" in Proposition K1 (m = 2k²−1, s = 2m²) is the Chebyshev/Pell index (ε_m = ε_k²). In multi-k it is the slice parameter k ∈ ℚ∖{0}.
   - The "m" values also differ.
   - **If** "even multi-k" was meant to refer to the even-s, all-k family of Proposition K1, the status is as follows. This is my reading, not a corpus definition.
     - Cat A: Proposition K1 is proved for all k ≥ 2. rank_g = m(m+1), rank_h = m(m+1) − k(k−1), dim F = 2m² = s, via Pell self-similarity (h² = g, (N₁,h) ≅ (R_k, ε_k)) and Burnside on R_n/2√d R_n. Also proved: tr τ = 2k, rank τ = 2k², and the extra relations are explicit. Mod-p checks pass at k = 5, 6.
     - Cat A: dim V(98) = 2406 (k = 2).
     - Open: equality of the lattice-level rank_h with the actual theta rank at m = 17, 31, …. K1 gives **upper bounds only**.
3. **One genuine group-theoretic contact with A₅.**
   - Cat A, standard theory: PSL₂(𝔽₅) ≅ A₅. For p = 5 the even Weil part (dim 3) factors projectively through A₅, and the odd part (dim 2) is a faithful representation of SL₂(𝔽₅) = 2·A₅.
   - Cat A, from rev6 Theorems F/H and the tensor theorem: the s = 7 representation has the tensor factor ρ_{2x²/5}. V_Eis = A₃ ⊗ W₅⁺ ⊗ W₇⁺ contains W₅⁺, and V_cusp = B₁ ⊗ W₅⁻ ⊗ W₇⁻ contains W₅⁻.
   - **IC-3**, Cat B support for the standard fact (floating-point group closure, `weil5.json`): the S, T images on W₅⁺ and W₅⁻ generate groups of order 120 with scalar subgroup {±1}. The quotient has order 60 and element orders {1,2,3,5}, consistent with A₅.
   - **Reading (Cat B, speculative):** the cusp sector carries a 2·A₅ (binary icosahedral) factor, which is formally reminiscent of "lift invariant −1" (non-split lift to 2·A₅) in the multi-k language. Nothing here is a monodromy representation of a Hurwitz family, and **it does not meet the locked success criterion**. It does not force Necessity, and it imports nothing into the residual core: residual P stays S₅.
4. **IC-4** (Cat A; exact, sympy/PARI, `checks.json`): Theorem 3.1 holds symbolically. The four seed discriminants are squares, and PARI `polgalois` gives A₅, A₅, A₅ and D₅ as stated. This verifies the catalogue's base facts; it does not address density or Necessity.

### (c) What changes
- Nothing in the multi-k catalogue is strengthened or refuted by the Bridge-C work.
- The only new mathematical observation is the A₅ / 2·A₅ tensor factor at s = 7 (item 3). Its link to multi-k is Cat B and does not satisfy the U1-E2 success criterion.
- Recommendation: keep the two "even/k" vocabularies explicitly separated in any write-up.

### (d) Open
All unchanged:
- density of A₅ fibres;
- A₅ vs D₅ criterion;
- Nielsen-labelled Hurwitz fusion;
- a continuous monodromy representation forcing Necessity.

One question is now testable (Cat B suggestion): does the degree-12 permutation representation of PSL₂(ℤ) on the braid orbit (r = 4 branch points, reduced Hurwitz space) factor through a congruence quotient SL₂(ℤ/N), and if so, does it share constituents with the Weil factors W₅^±? This was not computed.

---

## 4. K3 cohomology

### (a) What it claims and needs (quoted)
- `BOOK/Ramanujan_Hampton_Saha_Sinha_Bhat_K3_Resonant_Unification.md` (Status: "Category B continuum"): "K3 cohomology and its elliptic fibrations are realized through the resonant 3-form H3 = d + (ζt − 1) ∧ H3 with ζ = e2πi/539.9"; "Mock theta non-holomorphic corrections map onto kinematic phase-locking ηZPL"; Cat B list: "mock-theta to ηZPL dictionary, K3 resonant 3-form continuum realization".
- `BOOK/Ramanujan_Mock_Theta_K3_Zenodo_Deposit_Note_2026-08-06.md`: "Resonant 3-form H₃ with ζ = exp(2π i / 539.9) as lift of K3 cohomology"; "Claims of 'all numerical discrepancies close to machine precision' are framework-internal."
- No corpus file states a K3 *lattice*, Picard, Mukai, elliptic-genus or moonshine claim.

### (b) Mathematically justified connections, and their status
1. **Picard (Néron–Severi) lattice: a justified connection.**
   - The s = 7 form is odd: Q(L) ⊄ ℤ, so (ℤ², A) itself cannot be a K3 lattice. Its natural even versions are N₁ = (ℤ², 2A) = [[4,14],[14,14]] and the even sublattice N₂ = {x₂ even} = [[2,14],[14,28]]. Both have det −140 and are even and hyperbolic of rank 2.
   - **IC-5** (Cat A, exact; PARI `qfbsolve`, `checks.json`): both are anisotropic (140 is not a square) and represent no −2. The same holds for the Proposition K1 lattices M_t = [[2,2m],[2m,2]] at k = 2, 3, 4. For M_t this holds for every k, because x² − (m²−1)y² = −1 is impossible: m²−1 ≡ 0 mod 8.
   - **IC-6** (Cat A, exact): the automorph γ of rev6 Theorem B (eigenvalues 6 ± √35) acts on the discriminant group of N₁ and of N₂ as +1 exactly for even powers, and γ itself is not ±1. On M_t, g is not ±1 but **g² = γ acts as +1**. This is the K3-language reading of Algebraic-Round3 Step 4: ε² ≡ 1 mod 2√d.
   - Consequences, Cat A **conditional on cited theorems** (Morrison 1984, §2: every even hyperbolic lattice of rank ≤ 10 is the Néron–Severi lattice of some projective K3; global Torelli and surjectivity of the period map; Nikulin 1979 gluing). Theorem and corollary numbers were not re-checked.
     - Each of N₁, N₂ and M_t is NS(X) for some projective K3 surface X.
     - X has no smooth rational curves (no −2 classes) and no elliptic fibrations (no isotropic classes). So the ample cone is a full component of the positive cone.
     - The isometry γ² of N₁ or N₂, and γ = g² of M_t, glued with id on T_X, extends to a Hodge isometry of H²(X,ℤ) preserving the ample cone. By Torelli it is induced by an **automorphism of infinite order**. Its spectral radius on H² is (6+√35)² = 71 + 12√35, so its entropy is 2 log(6+√35) = 4√35·I, where I is the Baker constant of rev6 Theorem C.
     - For generic X (Hodge isometries of T_X only ±1), γ itself does **not** extend, because it is not ±1 on the discriminant group.
   - This is the standard "automorphs of binary forms ↔ K3 automorphisms" picture (cf. Galluzzi–Lombardo–Peters on automorphs of indefinite binary forms and K3 surfaces; citation from memory, not re-checked → Cat B as a citation).
   - **Reading (Cat B):** the regulator log(6+√35), which drives the Baker obstruction, is (¼ of) the entropy of a K3 automorphism with NS ≅ N₁. This is an exact numerical coincidence of definitions. I claim no theorem linking C to that K3.
2. **Transcendental lattice: no direct link** (Cat A). T_X has signature (2, 20−ρ). A signature-(1,1) lattice, or its negative, cannot be T_X. The discriminant form of T_X is minus that of NS. So vector-valued modular forms for the Weil representation of A_{N} (dual) are the natural targets for Noether–Lefschetz / Borcherds-type generating series of N-polarized K3 families (Borcherds; Kudla–Millson; Maulik–Pandharipande; cited, Cat B as applied here).
   - Whether rev6's 140-label representation equals the Weil representation of the order-140 discriminant form of N₁ was **not verified**. That is Cat B, a plausible hypothesis given |A_{N₁}| = 140 = number of labels.
3. **Mukai lattice: no content** (Cat A). Every even lattice of signature (1,1) embeds in Λ_K3 ⊂ Ũ = U⁴ ⊕ E₈(−1)² (Nikulin). That is true but says nothing specific about Bridge C.
4. **Mock modularity / K3 elliptic genus / Mathieu moonshine: not supported** (Cat B).
   - The K3 elliptic genus is the weak Jacobi form 2φ_{0,1} (index 1, rank-1 definite theta decomposition).
   - The Mathieu mock form H(τ) = 2q^{−1/8}(−1 + 45q + 231q² + …) has weight ½ and shadow ∝ η³, and has a polar term. So H(e^{−t}) grows exponentially as t → 0 (via τ → −1/τ).
   - C grows like I/t with a real-quadratic regulator (Theorem C), and rev6 Theorem E excludes scalar mock laws of the listed kinds.
   - The only shared feature is generic: weight-½ mock objects with weight-3/2 unary shadows, which is Zwegers' framework for H_s and the RTA's Ξ. No M₂₄ structure, no discriminant-35 / M₂₄ link and no elliptic-genus identity appears anywhere. **Speculative, and I would not assert it.**
5. **Bernoulli numerators 691, 3617, 43867** (Cat A for the occurrence and the mechanism; Cat B as a pattern).
   - They are the numerators of B₁₂, B₁₆ and B₁₈. They enter the top g-coefficients of S_e through Euler–Maclaurin (the r = e+1 Bernoulli term of the u₂-edge; Analytic-CatB-Push G.2/G.3).
   - B₁₄ = 7/6 at e = 13 has numerator 7 and is consistent with the same pattern.
   - The mechanism is generic to Euler–Maclaurin. It is **not** evidence for Δ = η²⁴, E₁₂, Yau–Zaslow 1/Δ or any K3 count. Any such reading is Cat B and unsupported.
6. **The corpus K3 "3-form" claim needs correction** (Cat A, standard topology). H³(K3; ℤ) = 0, since the cohomology of a K3 surface is concentrated in degrees 0, 2 and 4 (ranks 1, 22, 1). A 3-form class "as lift of K3 cohomology" therefore cannot be a class on K3 itself. It could only live on a product such as K3 × (3-manifold) inside the 11D setting, which the note would have to specify. This is a correction to Cat B notes, not to any Cat A lock.
   - Side note, **IC-7** (Cat A): as printed, 539.9 = 5399/10 with 5399 prime (PARI `isprime`), so ζ = e^{2πi/539.9} = e^{2πi·10/5399} *is* a root of unity. 2cos(2π/539.9) is then algebraic of degree 2699.
   - This contradicts `reports/heavy-daily/POLYNOMIAL_ROOTS_TARGETS_2026-08-17.md` ("ξ=2cos(2π/539.9) is not algebraic as printed").
   - If 539.9 is meant as a rounded measured value (539.90 ± 0.05), then ζ is not exactly defined, and either way it is unrelated to K3 cohomology.

### (c) What changes
- **New and justified (A, conditional on cited theorems):** the Bridge-C lattices (even versions of the s = 7 form, and the M_t of Proposition K1) are realizable as Picard lattices of K3 surfaces with no −2 curves and no elliptic fibrations. The Pell automorph (squared at s = 7, or γ = g² on M_t) is induced by an infinite-order K3 automorphism of entropy 2 log(6+√35) at s = 7.
- **Needs correction:** the "resonant 3-form as lift of K3 cohomology" wording (H³(K3) = 0), and the "not algebraic" remark on 2cos(2π/539.9).
- **Not supported:** any mock-theta / elliptic-genus / Mathieu-moonshine link to C or g_s, and any Δ/691 reading of the S_e Bernoulli pattern.

### (d) Open
- Whether the 140-label representation equals the Weil representation of A_{N₁} or A_{N₂}. This is a cheap, exact check (not run).
- Whether the λ = ¼ Maass forms or the Lewis–Zagier cocycle have any interpretation on N-polarized K3 moduli. No theorem is known to me, so this is Cat B.
- If wanted: an explicit K3 model, such as a quartic or double plane with NS ≅ N₁, which would make the automorphism concrete (not attempted).

---

## 5. One-line verdicts
| Topic | Definition found | Main implication | Category |
|---|---|---|---|
| 5th Order of Unification | Yes ("fifth-order unification"; the exact phrase "Order of Unification" is absent) | The period/tail needs are met only in vector-valued form; scalar is excluded. s = 7's special role comes from the frozen c₂. The f₀ link stays at the g_s shape (the s = 1 lattice is definite). Functor/E8: no bearing. | A (facts), B (readings) |
| Residual Ternary Algebra | Yes | The open "residual law" is **settled negatively in scalar form** (Theorem E) and **advanced to an explicit vector-valued weight-1 law** (Theorems F–J). Revision notes: weight ½ → 1; samples are not radial values; IC-1 value set; IC-2 P_s collision; cone note. Leave v1.0 as is; use rev6/rev7 if a revision is requested. | A (as labelled in rev6) |
| Even multi-k | Yes ("pure-even multi-k", Bring–Jerrard/A₅) | No direct bearing. Name collisions with even s and K1's k. An A₅ ≅ PSL₂(𝔽₅) / 2·A₅ tensor factor at s = 7 is a formal contact only and does not meet the U1-E2 criterion. Catalogue base facts re-verified (IC-4). | A (facts), B (link) |
| K3 cohomology | Yes (Cat B scaffolding only) | Justified: Bridge-C lattices occur as K3 Picard lattices; the Pell automorph gives an infinite-order K3 automorphism with entropy 2 log(6+√35) (conditional on cited theorems). Corrections: H³(K3) = 0; ζ is a root of unity as printed. Mock/elliptic-genus/moonshine links are unsupported. | A-conditional; B for links |
