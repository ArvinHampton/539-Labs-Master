> **Master-copy notation note (added 2026-10-18 at push; report text below is otherwise verbatim).** Lemma C1 / Lemma C2 of this report are called Lemma Prod1 / Lemma Prod2 on Master (to avoid clashing with Cross-Review item C1). Category convention for Master (rev. 4): Cat A = proved, or exact (including exact finite computation); floating-point-only results = Cat B. Where this report labels a floating result Cat A, read it as Cat B (C12, C13). Theorem names: Theorem G = Lewis–Zagier period theorem (rev. 3 meaning); the g_s asymptotics = Theorem G_s; the zero-set theorem = Theorem D. Erratum: ERRATUM_Consolidated_CrossReview_2026-10-18.md. Consolidated statement: Bridge_C_Consolidated_rev4_2026-10-18/.

# C_third: is there one object that carries both the E-part and the Zwegers part? (2026-10-18, CDT)

Scripts and outputs: `2026-10-18-C_third-Unified/`. Everything ran locally. Nothing was pushed, posted or emailed.

This continues the Path C work of the interrupted run (its `LEMMAS_C.md` and `candidate_logeta_E1.*` are copied here and kept as §4).

**Labels.**
- **Cat A** = exact or proved. Finite q-range checks are flagged as such.
- **Cat B** = numerical, conjectural, or identification by citation only.

No TPC or RH claims are made.

**Known verdicts, taken as given** (from `2026-10-18-C_third-Modularity.md`):
- C_third is not modular, and not mock or mixed mock (O1, O2).
- Its E-part is renormalised quantum modular (weight 1, factor |cx+d|).
- C_third = ½(1−θ₃) + ½q^{7/20}[ϑ_hol + E_L].

## 0. Verdict

| Question | Answer | Cat |
|---|---|---|
| Is there one **lattice object** carrying both parts? | **Yes.** For every s ≥ 5: 2C_third,s − 1 + θ₃ = q^{c₀}·Σ_{ν∈a+Z²} w(ν) q^{Q(ν)}. This is **one coset, one quadratic form, and one non-negative, degree-0, piecewise-constant cone weight** w = 1_{F′} + 1_{−Q₁}. | A (identity proved; checked to q²⁰⁰⁰ for s = 5..25 and 41, and to q³⁰⁰⁰ at s = 7) |
| How do the two known parts sit inside it? | They are exactly the **odd and even parts of w under ν ↦ −ν**: odd part = Zwegers ϑ_hol (mock, weight 1, holomorphic factor); even part = E_L. The odd part of the unit-cone indicator gives **exactly 0**, so E_L has no holomorphic weight-1 (mixed-type) content. | A (proof via the improper automorph R_s; checked for all listed s) |
| What theory covers each part? | Odd part: Zwegers 2002 indefinite theta. Even part: Zwegers 2012 *mock Maass theta function*, in the degenerate case c₂ = γc₁, where it is an actual λ = 1/4 Maass waveform (the u_L of Theorems F/G). | B (identification by citation; normalisations not re-derived) |
| One **vector-valued or mixed automorphic** object with a single transformation law? | **No.** The parity split is also the radial parity (half-integer vs integer orders) and the automorphy type ((cτ+d) vs \|cτ+d\|). Any vector holding both parts is a direct sum with block factor diag((cτ+d)ρ₁, \|cτ+d\|ρ₂). The q^{c₀} phase adds the O2 obstruction. | A for the parity and dictionary statements (modulo F1 and Hecke); A for the O1/O2 consequences as cited; B for "no exotic kernel exists" (open) |
| Weight-0 log-cocycle × weight-1 holomorphic products (interrupted run) | Cannot carry either sector (Lemma C1). | A (C1); C2 conditional |

## 1. The single-coset identity [A]

**Setting.**
- Q(ν) = ½νᵀMν with M = [[2,s],[s,s]], and ν ∈ a + Z² with a = (s/(2(s−2)), −1/(s−2)).
- Q(ν) + c₀ = Q_s(v), with c₀ = s/(4(s−2)).
- Cones, all open:
  - Q₁ = {ν₁>0, ν₂>0};
  - F = {ν₂>0, 2ν₁+ν₂>0} = [e₁, γe₁), the unit-group fundamental cone with γe₁ = (−1,2);
  - F′ = F∖Q₁ = {ν₁<0, ν₂>0, 2ν₁+ν₂>0}.
- No point of ±a + Z² lies on any of these rays, because ν₂ ∉ Z, ν₁ ∉ Z and 2ν₁+ν₂ ∉ Z for s ≥ 5.
- C_third,s := P_s + Θ_hol,s − θ₃. This is the all-s identity of `2026-10-18-g_s-Closed-Forms.md` §4; at s = 7 it is Master's C_third.

**Identity.**

  **2C_third,s − 1 + θ₃ = q^{c₀}[E^{F}_a + E^{−Q₁}_a − E^{Q₁}_a] = q^{c₀}[E^{F′}_a + E^{−Q₁}_a].**

Here E^X_μ := Σ_{ν∈μ+Z², ν∈X} q^{Q(ν)}.

Proof:
- Θ_hol = q^{c₀}(E^{−Q₁}_a − E^{Q₁}_a), because Q_s(−v) = Q_−(v) and the index sets translate as n ≥ 0 ⇔ ν₁ > 0 and k ≥ 1 ⇔ ν₂ > 0.
- E_s = q^{c₀}E^F_a.
- 2P_s = E_s + 1 + θ₃ − Θ_hol.
- Q₁ ⊂ F.

Checks (`single_coset.py` → `single_coset.txt`; `single_coset_s.py` → `single_coset_s.txt`): s = 7 to q³⁰⁰⁰, and s = 5..25 and 41 to q²⁰⁰⁰, all PASS.

So **C_third = ½(1−θ₃) + ½q^{c₀}·Θ_w(a)**, where Θ_w(a) is a sum over two disjoint cones (F′ and −Q₁) with coefficient 1. The theta piece ½(1−θ₃) is the only other ingredient.

## 2. Parity decomposition [A]

**Elementary identity.** Let K = {B(c,ν) > 0 > B(c′,ν)}, with c and c′ in the same negative component. Put:
- ρ_odd = sgn B(c,ν) − sgn B(c′,ν) (Zwegers' 2002 weight);
- ρ_even = 1 − sgn B(c,ν)·sgn B(c′,ν) (Zwegers' 2012 weight).

Then **1_K = ¼(ρ_odd + ρ_even)**. Both weights are ±2 on K ∪ −K and 0 elsewhere; ρ_odd is odd and ρ_even is even in ν.

**Applied to w** (since 1_{−Q₁} − 1_{Q₁} = −½ρ_odd^{Q₁}):

  Θ_w(a) = Σ_{a+Z²} [¼ρ_even^F + ¼ρ_odd^F − ½ρ_odd^{Q₁}] q^Q = E^F_a·(even part) + ½(E^F_a − E^F_{−a}) + ϑ_hol,

where ϑ_hol = E^{Q₁}_{−a} − E^{Q₁}_a.

**Lemma R (odd part of the unit cone vanishes).** E^F_a = E^F_{−a} for every s ≥ 5. [A]

Proof (symbolic checks in `R_symmetry_check.txt`):
1. R_s = [[1,s],[0,−1]] satisfies R_sᵀMR_s = M and R_s a = −a.
2. γa − a = (0,−1) ∈ Z², so γ stabilises a + Z², and hence −a + Z² too.
3. R_s e₁ = e₁ and R_sγe₁ = (2s−1, −2) = γ⁻¹e₁. So R_sF is the cone between γ⁻¹e₁ and e₁, which is again a fundamental cone for ⟨γ⟩ on the positive component containing e₁.
4. Hence E^F_a = E^{R_sF}_{−a} = E^{F}_{−a}, using γ-invariance of −a + Z² and of Q, and the fact that no coset point lies on a ray.

Numerical confirmation: identically zero to q³⁰⁰⁰ at s = 7, and to q²⁰⁰⁰ for s = 5..25 and 41.

**Consequence.** Θ_w(a) = E_L + ϑ_hol. The known split is therefore exactly the decomposition of the single cone weight w into its ν ↦ −ν even and odd parts.
- Odd part: −½ρ_odd^{Q₁}, the quadrant, two negative-norm c's. This is Zwegers' ϑ_hol.
- Even part: ¼ρ_even^F, the unit cone, c′ = γc. This is E_L.
- The would-be holomorphic weight-1 Hecke-theta piece ¼ρ_odd^F, which is a mixed-sign-character theta and completable by Zwegers with c′ = γc, contributes **nothing**.

**Radial dictionary [A modulo F1 and Hecke's theorem; Lemma P of the C_third report, extended to all s as in the H_s report §4.2].** At x = 0:
- the odd-weight part has only half-integer orders;
- the even unit-cone part has only integer orders.

So the following three splits coincide:
- parity of the cone weight;
- radial parity;
- type of automorphy factor ((cτ+d) for the Zwegers completion vs |cx+d| for the renormalised E-part).

## 3. Identification and the "single object" question

**(B, by citation.) Two Zwegers lifts of one cone datum.**
- The odd weight is the holomorphic part of Zwegers' indefinite theta ϑ^{c₁,c₂}_{a,0}: weight 1, completed by error functions. Source: thesis 2002, Cor. 2.9 (cited, not re-checked).
- The even weight (1 − sgn·sgn) is the weight of Zwegers' **mock Maass theta function** Φ^{c₁,c₂}_{a,b}. Source: S. Zwegers, "Mock Maass theta functions", Q. J. Math. 63 (2012) 753–770; zbMATH 1254.11045. The abstract and review were read; the paper itself was not checked.
  - Φ is a weight-0, λ = 1/4 eigenfunction built with √y·K₀(2π|Q|y)e(Qx).
  - Its completion is modular with shadow in S_{3/2}⊗S̄_{3/2}.
  - In special cases, which the review describes as those where completion and function coincide (the Cohen σ example), it is an actual Maass waveform.
  - Our even part has c′ = γc, the Hecke/Maass case. Its positive-frequency coefficient series is E_L, the f-function of u_L.

So the natural unified object is the **cone datum (Q, a + Z², w)** together with the two Zwegers kernels:
- the holomorphic kernel e(Q(ν)τ) on the odd part;
- the Maass kernel √y·K₀(2πQ(ν)y)e(Q(ν)x) on the even part.

Equivalently, any one-sided signature-(1,1) cone sum is ¼(a mock-modular theta) + ¼(the q-series of a mock-Maass theta). [identity A; theory B]

**No single automorphic law [A for the listed reasons, as cited].**
- The two parts are lifts of different weight (1 with holomorphic factor, vs 0 Maass, which gives |cx+d| after the f-function normalisation). Consolidated Thm G and O1 show the integer sector cannot satisfy a holomorphic-factor law, and §2 shows the half-integer sector is the Zwegers piece.
- The common factor q^{c₀} = e(c₀τ) is not a multiplier (O2).
- The vector of components Θ_w(μ), μ ∈ L′/L, is the natural vector-valued home. On it, the best available transformation behaviour is the direct sum of the Zwegers 2002 (weight 1) and Zwegers 2012 (weight 0) laws. That is a formal packaging, **not** a new automorphic class. [B, as an interpretation]

**Not excluded (open, B).**
- A single theta-integral kernel (Vignéras / Kudla–Millson type) that produces both parity parts at once. "Mock Maass forms revisited", Q. J. Math. 2025 (DOI 10.1093/qmath/haaf006; abstract only), builds Zwegers' mock Maass forms from theta integrals and might be a starting point. Not tested.
- Higher-depth (non-logarithmic) cocycle classes.

## 4. Product class from the interrupted run (kept)
- **Lemma C1 [A]** (`LEMMAS_C.md`). A finite sum of products f·g, with f of weight 0 holomorphic with logarithmic cocycle and g holomorphic of weight 1, has radial expansions with only t^{−2}, t^{−1}log t and t^{−1} terms at every rational, up to exponentially small error. Jordan blocks add only t^{−m}(log t)^j with m ≥ 1. Such a product can carry neither the half-integer sector nor the t⁰, t¹ sector.
  - Numerics: the candidate log η·E_{1,χ₋₃} at x = 0, 1/3, 1/2, 1/7 has t^{−1/2..1} coefficients equal to 0 within fit precision, 1e-8 to 1e-17 (`candidate_logeta_E1.txt`). These fits are B.
- **Lemma C2 [conditional, same inputs as O1].** Within that class, the |cx+d| factor of the E-part cannot be reproduced either.

## 5. Status summary
- **A:**
  - the single-coset identity, all s ≥ 5 (proved; finite q-checks);
  - the 1_K = ¼(ρ_odd + ρ_even) identity;
  - Lemma R and its consequence Θ_w = E_L + ϑ_hol;
  - the parity ↔ radial-order dictionary (modulo F1 and Hecke);
  - Lemma C1;
  - the "no single law" conclusion as a consequence of the cited O1/O2.
- **B:**
  - the identification of the even part with Zwegers' 2012 mock Maass theta functions (by citation);
  - the vector-valued "direct sum" reading;
  - the numerics of the log η·E₁ fit.
- **Open:**
  - a single theta-integral kernel producing both parts;
  - higher-depth classes;
  - the same analysis at x ≠ 0 for general s.

## 6. Files (`2026-10-18-C_third-Unified/`)
- single_coset.py / .txt / .npz (s = 7, q³⁰⁰⁰)
- single_coset_s.py / .txt (s = 5..25 and 41, q²⁰⁰⁰)
- R_symmetry_check.txt (symbolic: γa − a, R_s a + a, R_sᵀMR_s − M, R_sγe₁ = γ⁻¹e₁)
- LEMMAS_C.md, candidate_logeta_E1.py / .txt (from the interrupted run)
