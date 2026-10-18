# Is C_third modular, mock modular or quantum modular? — 2026-10-18 (CDT)

Folder: `reports/heavy-daily/2026-10-18-C_third-modularity/` (all scripts and outputs; nothing existing was edited, nothing pushed, no emails).
Inputs used: the Bridge-C-Residual-Law, P_s-Structure, psi-Cocycle, psi-Conditions-Removed (with the §4.2 cusp claim withdrawn), Cusp-Part, psiEis-and-Lvalues, ER-Cancellation-Proof-rev2 and PARI-Free-Certification reports, and `2026-10-18-Bridge-C-Consolidated/bridge_c_consolidated.tex` (skimmed: Thms D, E, F, G, §§ baker / lead / lz / open).

Labels. **Cat A** means proved here or exactly checked here. "Conditional" names the cited input it depends on. **Cat B** means a heuristic, an interpretation, or finite numerics with no proof behind them. Every cited theorem carries its check status.

## 0. Verdict

| Sense | Verdict for C_third | Cat |
|---|---|---|
| Modular (any weight, level, multiplier, in finite-dimensional vector-valued form, with a q^r shift allowed) | **No.** There are three independent reasons: (i) the Baker obstruction (consolidated Thm E(i)); (ii) the multiplicative t^{-1/2} obstruction (Thm E(ii)); (iii) the new Theorem O2 (§3), which needs no Baker. | A. (i) is conditional on Baker and the q-expansion principle. (ii) and (iii) are unconditional. |
| Mock or mixed mock modular, with the holomorphic factor (cτ+d)^k and a cocycle o(1/y) at the rationals | **No.** Theorem O2 covers C_third itself, for any weight and any finite-dimensional ρ. Theorem O1 shows that even the de-shifted part X = ½(ϑ_hol+E_L), the E-series E_L, and the whole E-vector cannot be components of such objects. | A, with the class conditions stated in §3. |
| Strict quantum modular (Zagier: values on Q) | **No values exist.** C_third diverges radially at every tested rational. Each one has a t^{-1} or a t^{-1/2} term; 490 of 490 rationals with m ≤ 40 were tested. | A for the finite scan. "Every rational": B. |
| Strong quantum modular (cocycle real-analytic off γ^{-1}∞) for any automorphy factor | **No** for C_third, by O2 with either factor. With the factor \|cx+d\|, X fails only at order y^{-1/2}, and only because of its Zwegers piece. | A for C_third. B for "no completion of ϑ_hol helps". |
| **Renormalised quantum modular** (integer-order radial data, factor \|cx+d\|, weight 1) | **Yes, after removing the factor q^{7/20} and the theta pieces.** The integer-order radial data of C_third are exactly those of ½(1+E). The E_L part is the (a,0) component of the 72-dimensional weight-1 \|cx+d\| quantum modular vector, i.e. the Lewis–Zagier f-function of a λ=1/4 Maass Eisenstein series. Exact values are in §4. | A for the identities, parity and values. The words "quantum modular form" for the \|·\| factor are terminology (B), as in consolidated Thm G. |
| Remaining obstruction to a single object | **Two independent pieces:** (a) the weight-0 factor e(7τ/20), which is entire but not a modular multiplier (O2); (b) the factor mismatch. X's integer sector needs \|cτ+d\| (O1), and its half-integer sector is a mixed-mock (holomorphic-factor) object whose cocycle is O(y^{-1/2}). | A for the statements. Whether any exotic class unifies them is open (§3.4). |

**In one line.** C_third = ½(1−θ_3) + ½·q^{7/20}·[ϑ_hol + E_L]. This is a theta piece, a mixed-mock Zwegers piece and a Maass-type quantum modular piece, all multiplied by the non-modular entire factor q^{7/20}. No single modular, mock or quantum modular form accounts for C_third. The precise obstructions are O1 (the sign of cx+d) and O2 (the q^{7/20} phase). After renormalisation the E-part is fully quantum modular (weight 1, |cx+d|), and the Zwegers part contributes nothing to the integer-order data.

## 1. Task (1): the identity, checked and decomposed

**(1.1) The identity, exactly as stated:**

  2·C_third = q^8 f_{2,7,7}(−q^10, −q^14, q) + 1 + E

It holds to q^3000 and to q^8000 (`series_3000.txt`, `series_8000.txt`, all PASS). The difference 2C_third − q^8f − E has only the constant term 1. **No correction is needed. [Cat A]**

- Proof: I2 (C_third = q^8 f + P_s) combined with A1 of the P_s report (2P_s = E + 1 + θ_3 − Θ_hol) and I3 (Θ_hol = q^8 f + θ_3) gives 2C_third = 2q^8f + E + 1 + θ_3 − Θ_hol = q^8 f + 1 + E. The status of I2, I3 and A1 in their source reports is Cat A (proved, and series-checked).
- E was built three independent ways: the P_s-report definition, the unit-fundamental-cone lattice sum, and an ideal-side ray-class enumeration with norms (N𝔞+7)/20. All three agree (PASS).

**(1.2) Splitting into pieces:**

  C_third = ½(Θ_hol − θ_3) + ½(1+E) = ½(1 − θ_3) + ½ q^{7/20} [ϑ_hol + E_L]

Here:
- Θ_hol = q^{7/20} ϑ_hol, with ϑ_hol = E^{C0}_{−a} − E^{C0}_{a}. These are quadrant cone sums over the cosets ∓a + Z², with a = (7/10, −1/5) and Q(ν) = ν1² + 7ν1ν2 + 3.5ν2².
- E = q^{7/20} E_L, where E_L is the unit-fundamental-cone sum over a + Z² (label #70 = (a,0)).
- Ideal form: E = Σ_{𝔞∈𝒦} q^{(N𝔞+7)/20}, where 𝒦 is one narrow ray class mod 𝔭2𝔭5∞1∞2.

**(1.3) The genus formula for E's coefficients.** Let r_𝒦(N) be the number of ideals 𝔞 ∈ 𝒦 of norm N. Then

  r_𝒦(N) = ½·1_S(N mod 280)·Σ_{d|N} χ_140(d)

with S an explicit residue set and χ_140 the **even** Kronecker character of Q(√35).
- Checked for N ≤ 59 993 with 0 inconsistencies (`genus.txt`). [Cat A as a finite check]
- As an identity for all N: Cat B here. It is equivalent to the Eisenstein (genus) property of u_L, which psiEis proves at the level of σ-invariant characters (cited from that report, not re-proved).

**Analysis of the pieces:**
- **½(1−θ_3):** a weight-½ theta function, modular.
- **ϑ_hol:** the holomorphic part of a signature-(1,1) Zwegers indefinite theta function.
  - Here c1 = (−1/5, 1/5) and c2 = (−1/5, 2/35), with Q(c1) = −1/10, Q(c2) = −1/35 and B(c1,c2) = −1/5 (`obstruction_checks.txt`; Cat A for the conditions).
  - The completion's weight-1 vector-valued transformation is Zwegers, thesis, Cor. 2.9 (local copy used in an earlier report; cited, statement not re-checked today).
  - Via the Hickerson–Mortenson f_{a,b,c} → Appell–Lerch decomposition (arXiv:1208.1421, Thm 1.3; cited, not checked), q^8 f is mixed mock: Appell–Lerch sums times weight-½ thetas.
- **E_L:** the positive-frequency (f-function) part of the λ = 1/4 Maass Eisenstein theta lift u_L. This is consolidated Thms F and G.
  - The S/T law is proved by Poisson summation (Cat A in the source).
  - The Lewis–Zagier period formula and cocycle are Cat A numerically, with written proofs (audited once).
  - The phrase "QMF" for the |·| factor is B.

## 2. Structural lemma: the parity splitting (new; Cat A)

**Lemma P.** At every rational x, expand along q = e(x)e^{−t}, t → 0+:
- (a) e(7τ/20)ϑ_hol, θ_3, and hence q^8 f = Θ_hol − θ_3, contain only half-integer powers t^{−1/2}, t^{1/2}, … (up to exponentially small terms);
- (b) E = q^{7/20}E_L contains only the integer powers t^{−1}, t^0, t^1, …

Consequently, at every order, the integer-power coefficients of C_third are exactly those of ½(1+E), and the half-integer ones are exactly those of ½q^8f.

**Proof.**

(a) Split the coset into classes ν = ν0 + 2m n, with n ∈ Z²_{≥0} and ν0 ∈ (0, 2m)².
- No coset point lies on a wall, since a has non-integral coordinates in both directions.
- 2-D Euler–Maclaurin for the rapidly decaying F(u) = e^{−Q(u)} on the closed quadrant (Q has positive coefficients there) gives the following. The coefficient of t^{(j−2)/2} in a class sum is Σ_{p+q=j} c_{pq}(F)·B_p(ν0,1/2m)B_q(ν0,2/2m), times the class phase e(xQ(ν0)).
- The map ν0 ↦ 2m(1,1) − ν0 is a bijection from the classes of −a+Z² to those of a+Z² inside the box. It preserves the phase: the difference is −2hB((1,1),ν0) + 4mhQ(1,1) ∈ Z, because B((1,1),ν0) ∈ ½Z and Q(1,1) = 23/2. It sends the shift s to 1−s.
- Since B_p(1−s) = (−1)^p B_p(s), the order-j coefficients of E^{C0}_{−a} and E^{C0}_a differ by (−1)^j. So ϑ_hol keeps only odd j, i.e. half-integer powers.
- Multiplying by e(7x/20)e^{−7t/20} preserves this.
- θ_3(x+it/2π) is c·t^{−1/2} plus exponentially small terms, by its modularity.

(b) Write E_L(e(x)e^{−t}) as a Mellin integral of Γ(s)D_x(s), with D_x(s) = Σ_{ν∈(a+Z²)∩F} e(xQ(ν))Q(ν)^{−s}.
- The weight e(xQ(ν)) is invariant under the unit γ, which preserves both Q and the coset. It depends only on ν mod a lattice.
- So D_x is a finite combination of partial zeta functions of totally positive coset classes modulo units, and hence a finite combination of Hecke L-functions of narrow ray class characters.
- These are entire, except for a simple pole at s = 1 (Hecke; standard, cited). So the only terms are t^{−1}, from s = 1, and t^k for k ≥ 0, from the poles of Γ at −k. There is no log t, because D_x is regular at 0.

Cat: A, conditional on the standard 2-D Euler–Maclaurin asymptotics (iterated 1-D EM with remainders; the sector-uniform version R1 is in the consolidated tex) and on Hecke's theorem.

**Numerical corroboration (Cat A, finite):**
- κ_{q8f}(x) := 2c_C − 1 − c_E = 0 to ≤ 1e−15 at 14 rationals (`radial.txt`). Here c_C and c_E were computed from *different* cones.
- A direct least-squares fit of √t·q^8 f at x = 0 gives a t^0 coefficient of 1.7e−8 against neighbours of size O(1) (`parity_fit2.txt`).
- Fits at x ≠ 0 are ill-conditioned (B, not used).

**Consequences (Cat A):**
- C_third has the singular expansion I·G(x)/t + h_C(x)t^{−1/2} + c_C(x) + …
  - The t^{−1} term comes from E alone: the Zwegers part has no 1/t term (consolidated Lemma zw0).
  - The t^{−1/2} term comes from q^8f alone.
- Since h_C ≠ 0 at all 490 rationals with m ≤ 40 (`scan.txt`), there is no finite radial limit there. The "both zero" set is empty.
- Theorem G (G(h/m) = 0 iff 2|m or 5|m) was re-checked on 1102 rationals with m ≤ 60, with 0 mismatches (`theoremG_check.txt`). Its proof is in the consolidated tex (Cat A).

## 3. Task (2): obstructions

### 3.1 (a) Modular — no

Restatement of the Baker obstruction (consolidated Thm E(i); Cat A, conditional on Baker, Mathematika 13 (1966), theorem number not re-checked, and on the q-expansion principle/algebraicity at all cusps, cited):
- There is no identity C_third = F + 𝓔, where F is in the Q̄-span of: holomorphic modular forms with algebraic coefficients (with q^r shifts), signature-(1,1) Zwegers holomorphic parts with rational characteristics, and unary/partial/false thetas; and 𝓔(e^{−t}) = o(1/t).
- Reason: the 1/t coefficient at x = 0 is I = log(6+√35)/(2√35) ∉ πQ̄ + Q̄.
- Thm E(ii), the multiplicative version (unconditional): C_third·g ≠ F for holomorphic modular g ≢ 0 and F, because C_third has a t^{−1/2} term while F/g has only integer-step powers.
- Theorem O2 below excludes modularity again, over C, without Baker.

### 3.2 Theorem O2 — the q^{7/20} phase obstruction (new; Cat A)

**Setup.**
- Γ ⊂ SL2(Z) of finite index; ρ: Γ → GL_d(C) any representation (unitarity is not needed); k ∈ R.
- j(γ,τ) is either (cτ+d)^k or |cτ+d|^k, with any multiplier absorbed into ρ.
- V: H → C^d is holomorphic, with V(γτ) = j(γ,τ)ρ(γ)V(τ) + o(1/y) as τ → x + i0, for every γ ∈ Γ and every rational x ≠ γ^{−1}∞.

**Claim.** C_third ≠ λ·V for every λ ∈ C^d. The same holds for C, P_s and E, which have the same 1/t profile I·G (respectively 2I·G).

This class contains:
- modular forms;
- holomorphic parts of harmonic Maass forms of any weight and shadow (their cocycles are period integrals, analytic off γ^{−1}∞; standard, e.g. the Bringmann–Folsom–Ono–Rolen monograph, cited, not checked);
- mixed mock forms Σ f_j g_j whose modular factors g_j have weight < 1;
- strong quantum modular forms of any weight.

**Proof.**
- Take γ0 = [[1,0],[140N,1]] ∈ Γ (some power of [[1,0],[140,1]] lies in Γ).
- Use x_n = γ0^n(1/3) = 1/(3 + 140Nn).
- Comparing the 1/y coefficients, with Im γτ ≈ y/(cx+d)², gives

  σ_C(x_n)(140Nn/3+1)² = j_n(1/3)·λρ(γ0)^n σ_V(1/3),

  where σ_C(x) = I·G(x) is the 1/t profile.
- Gauss-sum evaluation, for gcd(m,70) = 1:

  G(1/m) = e(7·\overline{20}/m)·(35/m)/m = e(7/(20m))·P(m mod 140)/m.

  This follows by completing the square, Q_s ≡ n'² − (35/4)(k − 5^{−1})² + 7/20 mod m. It is verified for 17 values of m, including m = 143, 283, 423, 563 ≡ 3 mod 140 (`o2_family.txt`; Cat A).
- So the left side is σ_C(1/3)·e(7x_n/20 − 7/60)·(1+140Nn/3).
- Hence g(n) := e(w/(n+u))(n+u)^{1−k} (with w = 7/(20·140N) ≠ 0, u = 3/(140N), and a sign for the |·| case) is, for n ≥ 0, a linear combination of the entries of ρ(γ0)^n. It therefore satisfies a constant-coefficient linear recurrence Σ_{i≤r} a_i g(n+i) = 0.
- The function Σ a_i g(z+i) is analytic near z = ∞ (as z^{1−k} times a function of 1/z) and vanishes at all large integers, so it vanishes identically. Take branch cuts vertically downward from each pole.
- Near z = −u only the i = 0 term has the essential singularity of e(w/(z+u)). So a_0 = 0, and inductively all a_i = 0, a contradiction. ∎
- σ_C(1/3) = I·G(1/3) ≠ 0.
- Numerical illustration of the extra phase on 13 rationals (`obstruction_checks.txt`): G(γ0x)|cx+1|e(−7(γ0x−x)/20)/G(x) = 1 to 1e−14, while e(7(γ0x−x)/20) varies.

**Byproduct.** This explains the "x-dependent W_7 phase" in the residual-law report and consolidated §§ Gauss-means. Over 120 pairs (m < 30), the raw phases of G(x)/(7^{−1/2}(7x)G(W_7x)) take 108 distinct values. After removing e(7(x − W_7x)/20) only 4 remain: ±3/20 and ±7/20 turns (`w7_explain.txt`; Cat A, finite). This complements the consolidated "vector mixing" reading.

**Sharpness.** The o(1/y) hypothesis matters. C_third *is* e(7τ/20) × (|·|-type object) + theta pieces, and e(7τ/20) is entire, hence trivially a weight-0 "quantum modular" function. O2 shows precisely that this factor cannot be absorbed into a modular multiplier.

### 3.3 (b) Mock modular — Theorem O1, the sign obstruction (new; Cat A, conditional on the cited inputs)

**Why Baker alone does not settle mock modularity.** The holomorphic parts of harmonic Maass forms can have transcendental coefficients and constant terms, for example logarithms of algebraic numbers. Examples, cited as context only, not checked: Duke–Li, "Harmonic Maass forms of weight one"; Kudla–Rapoport–Yang; Charollois–Li; Ehlen. So "I is transcendental" does not by itself exclude E being mock. The correct obstruction is the sign of cx+d.

**Input: the singular S-law has |x| (Cat A, exact finite Gauss means).**

  G_{a,0}(−1/x) = Σ_{p∈L'/Z²} G_{p,−a}(x) / (√35·|x|)

- This was checked at 9 points, x = ±1/3, ±1/7, ±3/7, ±1, 1/9. Both sides are zero at ±2/3 and −4/9.
- With the signed factor x the ratio is exactly −1 at every negative x tested (`sign_law_check.txt`).
- Note for the consolidated tex, § "Leading order: radial profiles": the profile law printed there with 1/(√35 x) is correct for x > 0. For x < 0 the factor is |x|, consistent with its Thm G statement "with the factor |x| the same holds for x < 0". This is a minor wording issue; their tests were evidently at x > 0.

**Theorem O1.**
- Hypotheses: V is holomorphic and finite-dimensional on Γ ∋ S, T^N; ρ'(T^N) is diagonalizable with unimodular eigenvalues; V(γτ) = (cτ+d)^k ρ'(γ)V(τ) + o(1/y) at each rational x ≠ γ^{−1}∞.
- Conclusion: none of E_L, X = ½(ϑ_hol+E_L), or the 72-component E-vector is λ·V. The singular level forces k = 1; other k fail by modulus.
- Proof:
  - Put Y = λρ'(S)V. Then E_L(−1/τ) − τY(τ) = o(1/y), which forces σ_Y(x) = x·σ_L(−1/x) = sgn(x)·σ_R(x)/√35, where σ_R = Σ_p G_{p,−a}·(cone measure).
  - T-finiteness gives σ_Y(x + 140Nn) = Σ_j c_j ω_j^n, with |ω_j| = 1.
  - By contrast σ_R(x + 140Nn) = σ_R(x), and σ_R(1/3) ≠ 0.
  - So an exponential polynomial with unimodular bases would equal +A for n ≥ 0 and −A for n < 0, with A ≠ 0. That is impossible, since it is determined by its values on n ≥ 0.
  - X has the same σ, because ϑ_hol has no 1/t term (Lemma zw0). ∎

**Class covered.** Modular forms, harmonic Maass holomorphic parts of weight 1 with any shadow (cuspidal or not; cited as above), and mixed mock Σ f_j g_j with modular factors of weight < 1. In particular:

**Corollary.**
- E (or the E-vector) is not the holomorphic part of a weight-1 harmonic Maass form, nor a component of a vector of such.
- E is not a holomorphic weight-1 modular form. Independently: χ_140 is even, so Σ_{d|N}χ_140(d)-type coefficients belong to Maass, not holomorphic, weight-1 Eisenstein series. Holomorphic E_1^{ψ1,ψ2} needs ψ1ψ2(−1) = −1 (classical, Cat A).
- E is not mixed mock with modular factors of weight < 1.
- The "log ε / growth I/t" heuristic in the task is thereby replaced by a precise statement. The obstruction is not the size I/t, which weight-1 objects can carry. It is the **sgn(cx+d) in the 1/t profile law**, a signature-(1,1) weight-(½,½) phenomenon. The reason, Cat B as an explanation: the Siegel theta of signature (1,1) has the factor (cτ+d)^{1/2}(cτ̄+d)^{1/2}, whose boundary value is |cx+d|.

### 3.4 What O1/O2 do NOT exclude (precise residual gap; open)

Objects whose cocycles are themselves of size ≥ 1/y are not excluded. Example: Σ f_j g_j with g_j holomorphic weight-1 modular and f_j weight-0 holomorphic functions with logarithmic cocycles, of log η / Eichler-integral type, whose boundary cocycles can produce sgn(x) up to the analytic function log|x|. Such a "weight 0 × weight 1" product structure could in principle reproduce |cx+d|. I did not test or construct one. This is not "mock modular" in the Zwegers/Zagier sense; the question is open (B).

### 3.5 (c) Quantum modular — combining Zwegers with the E-vector cocycle

**Factor mismatch, made precise.** By Lemma P the two pieces live in complementary radial sectors:
- **Integer sector** (t^{−1}, t^0, t^1, …): only ½(1+E). E_L's data obey the weight-1 law with |cx+d| (Thm G: cocycle real-analytic off γ^{−1}∞; Cat A numerics/written proofs as cited). They provably cannot obey the holomorphic law (O1).
- **Half-integer sector** (t^{−1/2}, t^{1/2}, …): only ½q^8 f, i.e. ½(Θ_hol − θ_3). This is a mixed-mock, holomorphic-factor object. Its cocycle is O(y^{−1/2}) near rationals, since the shadow involves weight-½ unary thetas, which grow like y^{−1/2}. h_{q8f} ≠ 0 at all 14 test points (Cat A). Cat B: "no other completion makes it bounded".
- Consequently, for γ with cx+d > 0 on an interval (e.g. S on x > 0) the two factors agree there. X then satisfies a one-sided weight-1 law with error O(y^{−1/2}), coming only from the Zwegers shadow.
- For cx+d < 0 the integer sector requires |·| and the half-integer sector requires (cτ+d). No single automorphy factor gives a cocycle o(1/y) and bounded at the y^{−1/2} level (A at order 1/y by O1; B beyond).
- **The combination survives renormalisation.** Keep only integer-order data (the constant term c(x) of the radial expansion). The Zwegers piece contributes exactly 0 at every rational (Lemma P). So the renormalised value function of X is ½e(…)κ_L, which is quantum modular of weight 1 for |cx+d| (Thm G; the "QMF" wording is B).
- Context, not checked: this mirrors Zagier's Maass-form example in "Quantum modular forms" (Clay Math. Proc. 12, 2010), and the Bettin–Conrey treatment of Σ d(n)q^n (Period functions and cotangent sums, Algebra & Number Theory 7 (2013)), where the divisor-sum Eisenstein series is "quantum modular" only after removing the singular terms.

## 4. Task (3): the best positive theorem

**Theorem P (structure of C_third). [Cat A for (i)–(iii) and the formula in (iv), with the stated citations; "QMF" wording B]**

Let I = log ε/(2√35) with ε = 6+√35, let G be the Gauss mean of Q_s, and let G_a(x) = e(−7x/20)G(x). Then:

**(i) Decomposition.**

  C_third = ½(1−θ_3) + ½e(7τ/20)[ϑ_hol + E_L]

with ϑ_hol a signature-(1,1) Zwegers holomorphic part (weight 1, holomorphic factor; Zwegers Cor. 2.9 cited) and E_L the (a,0) component of the 72-dimensional fundamental-domain vector.

**(ii) The E_L component.** E_L is the Lewis–Zagier f-function of the λ = 1/4 Maass Eisenstein theta lift (consolidated Thms F, G). Its cocycle for factor |cx+d| and weight 1 is real-analytic on R∖{γ^{−1}∞}. Only Eisenstein labels occur in the S- and T-rows of (a,0) (`obstruction_checks.txt`; the label-level S is not block-diagonal in general, max |S[cusp,Eis]| = 0.17, but this row is).
- The singular profile G_a is exactly invariant under the Weil kernel: G_a(γx)|cx+1| = G_a(x) for γ = [[1,0],[140,1]].
  - Numerics: 13 points to 1e−14.
  - Proof: for x = 1/m with gcd(m,70) = 1, the closed form of §3.2 gives it.
  - In general: B, as in consolidated §lead.

**(iii) Parity splitting (Lemma P).** At all orders and all rationals, the integer-order radial data of C_third are those of ½(1+E), and the half-integer ones are those of ½q^8 f.

**(iv) Renormalised values.** For rational x = h/m,

  c_C(x) = ½ + ½e(7x/20)·Z_x(0) − (7/20)·I·G(x),

where Z_x(0) = Σ_{𝔞∈𝒦} e(xN𝔞/20)|_{s=0} = κ_L(x) is a value at s = 0 of a combination of ray-class partial zeta functions:

  Z_x(0) = ½ Σ_{d0,e0 mod L} χ_140(d0)·1_S(d0e0)·e(hd0e0/(20m))·(½ − d0/L)(½ − e0/L),   L = lcm(280, 20m).

So c_C(x) = α(x) + β(x)·I, with α ∈ Q(ζ_L) and β = −(7/20)G(x) ∈ Q(ζ_{40m}).
- β = 0 exactly when 2|m or 5|m.
- Otherwise c_C(x) is transcendental: I is transcendental by Lindemann–Weierstrass, and α, β are algebraic with β ≠ 0.

**The remaining obstruction to a single unified object:**
- (1) the factor e(7τ/20) (O2);
- (2) the mixture of the |cx+d| integer sector (E) with the (cτ+d) half-integer sector (Zwegers) (O1 plus §3.5);
- (3) the weight-½ theta term.
Only exotic classes with cocycles of size ≥ 1/y (§3.4) are not excluded.

## 5. Task (4): exact values at rationals (the Shintani L(0) side)

**Radial limits.** At no tested rational does C_third have a finite radial limit (§2). The natural exact invariant is the renormalised value c_C(x), the t^0 coefficient. Its exact formula is Theorem P(iv).

**What enters, and what does not.** The cusp-form L(0) values of the PARI-free certification do **not** enter.
- The weight e(xN𝔞/20) depends only on N𝔞, so only the norm-type (genus) data of 𝒦 survive.
- The resulting values are products of generalized Bernoulli B_1 values: this is the (½−d0/L)(½−e0/L) structure.
- Separately, the S- and T-partners of row (a,0) are all Eisenstein.
- Cat: A as a computation (three independent evaluations agree); B as a general statement (it rests on the genus formula, §1.3).

**Exact values.** `exact_values.py` evaluates the genus formula with exact rationals. Every value matches the independent quadrant-cone Euler–Maclaurin value to ≤ 4e−15. In addition, Z_x(0) was computed three independent ways (lattice κ_L, Shintani cone, genus/Hurwitz), agreeing to ~1e−12 at 14 rationals (`radial.txt`).

| x | c_C(x) = α + β·I | numeric |
|---|---|---|
| 0 | 11/20 − (7/20)I | 0.476703062890 |
| 1/2 | 0 | 0 |
| 1/3 | −3/40 + 31√3 i/120 − (7/120)(1+√3 i)·I | −0.087216 + 0.426287 i |
| 1/4 | 2 + (3/2)i | — |
| 1/5 | ½ + ¼√5 + (i/(20√2))(√(5−√5) + 3√(5+√5)) | 1.059017 + 0.344095 i |
| 1/6 | 3/2 + (3√3/2) i = 3e(1/6) | — |
| 1/7 | α ∈ Q(ζ_7, i) (see file) − (√7 i/20)·I | 1.134143 − 0.029578 i |
| 3/7 | α (file) + (√7 i/20)·I | 0.021306 + 0.669102 i |
| 1/10 | √5/4 − 0.683664… i (radicals in file) | 0.559017 − 0.683664 i |

The 2/5 and 3/10 entries are in `exact_values.txt`.

Other leading terms:
- h_C(0) = −√π(49−2√14)/140.
- At x = 1/2: C_third ~ (√π/4)·t^{−1/2}, with s = c = 0.
- All tests are Cat A as exact finite evaluations, conditional on the genus formula, which is itself confirmed by the two independent routes at these points.

## 6. Cat A / Cat B summary

**Cat A:**
- identity (1) to q^8000;
- the decomposition;
- Lemma P (conditional on 2-D EM and Hecke);
- the finite scans (490 rationals, no finite limits; Theorem G on 1102 rationals);
- Theorem O2 (unconditional, via the Gauss-sum closed form);
- Theorem O1 (conditional on the cited analyticity of harmonic-Maass/mixed cocycles and on the |x| profile law, which was checked exactly at the points needed: x = ±1/3);
- Baker obstruction E(i) (conditional on Baker and the q-expansion principle);
- E(ii);
- Theorem P(i), (iii) and (iv);
- the exact values;
- the W_7-phase explanation (finite).

**Cat B:**
- the genus formula for all N;
- "no finite radial limit at every rational";
- the profile law for all γ and x;
- no completion of ϑ_hol giving a bounded |·|-cocycle;
- the "QMF" terminology for |·|;
- the Siegel-theta explanation of |cx+d|;
- the §3.4 residual class (open);
- the Lewis–Zagier / Bettin–Conrey / Zagier analogies (context).

**Cited, not re-checked today:**
- Zwegers Cor. 2.9;
- HM Thm 1.3;
- Hecke (entire continuation of ray-class L-functions);
- Baker 1966;
- q-expansion principle (Shimura);
- Lewis–Zagier; Zagier QMF (2010); Bettin–Conrey (2013);
- Duke–Li / KRY / Charollois–Li / Ehlen (context only);
- the BFOR monograph (cocycle analyticity);
- consolidated Thms D–G and psiEis, with their own stated statuses.

No claims about HQCC, TPC or RH are made or implied.

## 7. Files (all under `reports/heavy-daily/2026-10-18-C_third-modularity/`)

| File | Contents |
|---|---|
| `series.py`, `series_3000.txt`, `series_8000.txt`, `series.npz` | identity (1); three constructions of E |
| `genus.py`, `genus.txt` | the genus formula for r_𝒦(N), N ≤ 59 993 |
| `radial.py`, `radial.txt` | s, h, c at 14 rationals; three-way Z_x(0); κ_{q8f} = 0 |
| `parity_check.py`, `parity_fit2.py` (+ .txt) | numerical parity fits |
| `scan.py`, `scan.txt` | 490 rationals, no finite radial limit |
| `theoremG_check.py` | Theorem G zero set, m ≤ 60 |
| `sign_law_check.py` | the \|x\| singular S-law (input to O1) |
| `o2_family.py` | Gauss-sum closed form (input to O2) |
| `obstruction_checks.py` | Weil-kernel phase, Eisenstein row, Zwegers conditions |
| `w7_explain.py` | W_7 phase explained by q^{7/20} |
| `exact_values.py`, `exact_values.txt` | exact α, β |

Imported code, read-only: `kappa_all` (psi-conditions folder) and `shintani` (2026-10-18-PARI-free folder).
