# Bridge Series C: search for a residual law (modular part + controlled remainder, or a weight-1/2 slash)
Date: 2026-10-17, 20:11–20:45 CDT. Master clone `/workspace/quantum-comp/oct17-master`, tip 48684e3 (unchanged).
Read-only throughout. Nothing was pushed, emailed, sent, or run through Grok.
Scripts and outputs are in `2026-10-17-bridge-c-residual-law/`.
Separation notes: no HQCC termination claim is made here. TPC and RH stay unclaimed. Residual ≠ Resonant. CORE_FREEZE holds.

## Verdict (up front)
**OBSTRUCTION, plus an exact reduction. No residual law was found.**

1. **Exact reduction (Cat A, verified to q^3000).** C and C_third have the **same** remainder, the orthant series P_s = Σ_{n,k≥0} q^{n²+7nk+(7/2)k(k+1)}:
   - C = −H_s + P_s (this is the definition);
   - C_third = q^8 f_{2,7,7}(−q^10, −q^14, q) + P_s.

   Everything else in C and C_third is mock/indefinite-theta (Zwegers/HM) or unary theta. The whole "residual law" question is therefore a question about P_s.
2. **Obstruction to "modular + controlled remainder" (Cat A, assuming two standard cited theorems).** As q = e^{−t}, t → 0+:
   - P_s, C and C_third all equal I/t + O(t^{−1/2}), with **I = log(6+√35)/(2√35)**. Here 6+√35 is the fundamental unit of Q(√35).
   - Every weight-1 modular form with algebraic coefficients contributes 2π·(algebraic)/t. Every signature-(1,1) Zwegers holomorphic part contributes 0/t. Every unary, partial or false theta contributes O(t^{−1/2}) or (algebraic)/t.
   - By Baker's theorem, log(6+√35) ∉ Q̄ + πQ̄.
   - So neither C nor C_third equals (any Q̄-combination of those objects) + o(1/t).
   - In particular, **no weight-1/2 residual false theta can absorb the remainder**.
3. **Obstruction to the θ-prefactor / quotient route (Cat A).** C_third·g = F is impossible for any holomorphic modular forms g and F, of any weight, level or multiplier, even with complex coefficients. For C the same holds with Q̄ coefficients (Cat A). With complex coefficients it is Cat B, because the needed t^{−1/2} coefficient of C is only known numerically.
4. **Obstruction to a scalar Fricke/W_7 slash, any weight k and any constant λ (Cat A, finite exact computation).**
   - The leading singularity of C at x ∈ Q is G(x)·I/t, where G is an explicit Gauss mean.
   - G(x) ≠ 0 while G(−1/(7x)) = 0 at 178 of 270 test rationals. The **Master sample point x = 5/7** is one of them, and so are 2/7, 4/7, 6/7 and 2/3. At those points no scalar cocycle C − λ(7τ)^{−k}C(−1/(7τ)) can be bounded.
   - Where both values are nonzero, |G| obeys an exact **weight-1** (not weight-1/2) relation with |λ| = 7^{−1/2}. Its phase varies with x, so no constant λ works.
5. **What the law does give quantitatively (Cat A).** It replaces the four qualitative sample magnitudes with **exact continuous radial targets**:
   - the singular coefficient lim_{t→0} t·C(e^{2πix}e^{−t}) = I·G(x) at every rational x;
   - for example, I = 0.2094198… at x = 1, and |I·G| = I/√7 = 0.079153… at x = 1/7, 3/7, 5/7.

   The published samples are not radial values of C. C(0.995·e^{2πix}) is about 19.5, 18.5, 19.9 and 54.0 in modulus, against the samples' 19.80, 1.82, 9.24 and 20.90.
6. **Left open (Cat B):** a **vector-valued** law over the 35 discriminant-group components, in the Weil representation of the level-70 lattice. It is not excluded and is the only route these obstructions leave.

---

## 0. Definitions used (Master, quoted with file:line)
All paths are under `docs/S2-11DM2ET-X-Axiomatic-Book/`.
- `Residual_Bridge_Series_C_Definition.md`:
  - l.11: M = [[2,s],[s,s]].
  - l.15: Q_s(n,k) = n² + snk + (s/2)k(k+1).
  - l.20: c1 = (−1,1), c2 = (−4,1).
  - l.24: w(v) = ½(sgn B(c1,v) − sgn B(c2,v)).
  - l.29: P_s = Σ_{n,k≥0} q^{Q_s}.
  - l.31: H_s = Σ_{v∈Z²} w(v) q^{Q_s(v)}.
  - l.36: C := P_s − H_s.
  - l.53: exterior w = −1 points contribute +1.
  - l.104–107: the sample table.
- `Pursue_All_C_Closure_Status_2026-08-23.md`:
  - l.41: C_axis = 3/2 + Σ_{n≥1}q^{n²} + Σ_{k≥1}q^{7k(k+1)/2}.
  - l.45–46: C = C_axis + C_third + C_mixed, "C_mixed = 0 through degree 293".
  - l.50: "Fricke samples remain qualitative … (weight 1/2 slash, ρ ≈ 0.995)".
- `Residual_False_Theta_Construction_Attempt_C_2026-08-23.md`:
  - l.24/l.66: C_third = Σ_{n,k≥1} q^{n²+7nk+(7/2)k(k−1)}.
  - l.56: a law for C is equivalent to a law for P_orth.
- `Residual_Fricke_Magnitude_Verification_Slash_C_2026-08-25.md`:
  - l.13: sample points x = 1/7, 3/7, 5/7, 1.
  - l.16: ratios 19.80, 3.15, 20.66, 55.30.
  - l.19: markers −18.2+7.8i, 0.3−1.8i, 2.1−9.0i, 20.7+2.9i.
  - l.21: W_7(x) = −1/(7x).
  - l.24: residual_slash = |7x|^{−1/2}·residual_factor.
- `Residual_Law_for_Bridge_C_Status_Freeze_2026-08-24.md` l.84 defines the "residual law" as the exact weight-1/2 slash prefactor plus a continuous Fricke match.
- In the H_s cone, B(c1,v) = 5n and B(c2,v) = −n−21k, since c^T M = (5,0) and (−1,−21).

---

## Category A (verified)

### A1. Exact series identities, checked with exact rational coefficients through q^3000
Script: `identities.py`. Output: `identities.txt`. The H_s box was enlarged by 30 and the result was identical. Every identity below PASSES.
Notation:
- f is HM Def. 0.2 (arXiv:1208.1421).
- Θ_hol := Σ_{n≥1,k≥0} q^{Q_−} − Σ_{n≤0,k≤−1} q^{Q_−}, with Q_− = n²+7nk+(7/2)k(k−1). This is the Zwegers holomorphic part from the levers-1-2 follow-up.
- R := Σ_{n≥0,k≥1} q^{Q_s}.
- θ_3 = Σ_{n∈Z} q^{n²}.

| # | Identity | Status |
|---|---|---|
| I2 | **C_third = q^8 f_{2,7,7}(−q^10,−q^14,q) + P_s** | exact through q^3000; also an elementary reindexing (shown below) |
| I3 | Θ_hol = q^8 f_{2,7,7}(−q^10,−q^14,q) + θ_3 | exact through q^3000 |
| I4 | C_third = Θ_hol − Σ_{n≥1}q^{n²} + R | exact through q^3000 |
| I5 | **C − C_third = −H_s − q^8 f_{2,7,7}(−q^10,−q^14,q)** | exact through q^3000 |
| I7 | P_s = R + (1+θ_3)/2 | exact through q^3000 |
| I1 | C_mixed := C − C_axis − C_third vanishes through q^293 | confirms the Master claim |
| I1b | **C_mixed ≠ 0**: first terms −½q^294 + ½q^301 − q^330 + q^337 − q^368 + q^375 − … | exact |
| I6 | C_mixed = −H_s − q^8 f − C_axis | exact through q^3000 (it is mock plus unary only) |

- **Proof of I2.** Put r = n−1 and s = k−1. With x = −q^10 and y = −q^14 the signs cancel. The (r,s ≥ 0) orthant of q^8 f gives C_third. The (r,s < 0) orthant, after (r,s) = (−1−n, −1−k), has exponent exactly Q_s(n,k) and sign −1. I checked the arithmetic by hand and in the script.
- **Where C_mixed comes from.** At q^294 the point (21,−1) lies on the c2-wall n + 21k = 0, with w = ½, outside the orthant, so it contributes −½. Mixed-quadrant points such as (22,−1) at q^330 and (−22,1) at q^337 lie inside the H_s cones but outside the orthant.
- **Consequence for Master (wording, not a new claim about the objects).** "C = C_axis + C_third" holds only through q^293, not as an identity. It appears at:
  - `Residual_Law_for_Bridge_C_Status_Freeze_2026-08-24.md` l.10;
  - `Discrete_Bridge_E8_to_Fifth_Order_2026-08-24.md` l.9 ("C7 = C_axis + C_third, coefficients restricted to {0,1,1.5}");
  - `42_Discrete_Contacts.md` l.34.

  `Pursue_All…` l.45–46 states it correctly, with C_mixed. The value set {0,1,3/2} is correct through degree 101, as l.48 says (through 80) and the Definition file l.56 says (through 100). The first coefficient 2 is at q^102 (`audit_misc.txt`), and the value set through q^3000 is {0, ½, 1, 3/2, 2, 3}. The residue support {0,1,2,4} mod 7 holds for all terms, because Q_s ≡ n² mod 7.
- **Correction to the levers-1-2 follow-up (F1).** That note calls R "a positive-definite-cone partial sum". Q_s is **indefinite** (disc 35). It is positive only on the closed orthant. So the inclusion–exclusion into full definite lattice thetas proposed in lever 1 is **impossible**: the full-lattice sum Σ_{Z²} q^{Q_s} diverges.

### A2. Radial asymptotics at q = 1 (`asymptotics.py`, `asymptotics.txt`)
- **Lemma 1.** As t → 0+:
  - P_s(e^{−t}) = I/t + a_P t^{−1/2} + O(1);
  - C_third(e^{−t}) = I/t − a_P t^{−1/2} + O(1);

  with I = ∫∫_{x,y≥0} e^{−(x²+7xy+(7/2)y²)} = **log(6+√35)/(2√35) = 0.20941982031471463…** and a_P = (√π/4)(1 + (7/2)^{−1/2}) − (7/2)∫∫ y e^{−Q} = **0.5256172043…**
  - Proof: 2-D Euler–Maclaurin on the quadrant, with the linear term (7/2)k treated perturbatively. For C_third, the cone n,k ≥ 1 is the n,k ≥ 0 cone of Q_− minus its two axes, and that flips the sign of the t^{−1/2} term.
  - The closed form for I comes from ∫_0^∞ du/(2(1+7u+3.5u²)). The roots give the ratio (7+√35)/(7−√35) = 6+√35. It matches numeric quadrature to 40 digits.
  - Numerical fit on t ∈ [0.00125, 0.08]: coefficient of 1/t 0.209419 (I = 0.209420); t^{−1/2} coefficient 0.52569 for P_s and −0.52575 for C_third (predicted ±0.525617).
- **Lemma 2.** The holomorphic part of any signature-(1,1) Zwegers ϑ^{c1,c2}_{a,b} has 1/t coefficient **0**. This needs c1, c2 of negative norm and rational a, b, and covers H_s, Θ_hol and q^8 f.
  - Proof: the weight is +1 on a cone K and −1 on −K (walls are 1-D, so O(t^{−1/2})). The mean of e(B(ν,b)) over the coset is the same on K and on −K. Since Q is even, the integrals over K and −K are equal, so the leading terms cancel.
  - Numerically, t·H_s → 0 (fit −0.0002).
  - **Corollary:** C(e^{−t}) = I/t + O(t^{−1/2}). The fit gives 0.20961.
- **Lemma 3 (any rational x = h/m).** t·S(e^{2πix}e^{−t}) → I·G(x) for S ∈ {P_s, C, C_third}. Here G(x) = (2m)^{−2} Σ_{(n,k) mod 2m} e(xQ_s(n,k)) is exact. H_s still contributes 0, because Q_s(−v) = Q_−(v) and Q_− has the same residue mean.
  - Checked numerically to t = 6.25·10^{−4}: `roots_of_unity.txt`.
  - For x = h/7, G = (h/7)_Legendre · i/√7, since Q_s ≡ n² mod 7.
  - For gcd(m, 70) = 1 and m > 1, |G(h/m)| = 1/m. G(h/m) = 0 when 2 | m or 5 | m. See `fricke_profile.txt`.

### A3. Theorem (additive obstruction)
Let 𝓜 be the Q̄-span of the following:
- (i) q^r·f, with r ∈ Q and f a holomorphic weight-1 modular form on some Γ(N) with Q̄ Fourier coefficients;
- (ii) q^r·f with f of half-integral weight, and f of integral weight k ≥ 2 without a q^r shift (the q-expansion as given);
- (iii) q^r times the holomorphic part of any signature-(1,1) Zwegers indefinite theta with negative-norm c's and rational characteristics;
- (iv) unary theta, partial theta and false theta series Σ_{n≥n0} ψ(n) n^ε q^{an²+bn}, with ψ periodic and Q̄-valued, ε ∈ {0,1}, a > 0.

**Statement:** there is no identity C_third = F + E or C = F + E with F ∈ 𝓜 and E(e^{−t}) = o(1/t).

**Proof.** Multiply by t and let t → 0+. The pieces behave as follows:
- (i) gives 2πβ with β ∈ Q̄, because f|S has algebraic q-expansion;
- (ii) gives 0, since its powers are t^{−k+j} with k ∉ {1} or no shift;
- (iii) gives 0 by Lemma 2;
- (iv) gives either 0 or mean(ψ)/(2a) ∈ Q̄.

So I = 2πβ + γ, with β, γ ∈ Q̄. That is log(6+√35) + 4√35 iβ·log(−1) − 2√35γ = 0, a nontrivial Q̄-linear relation among 1, log(6+√35) and log(−1). But log(6+√35) (real, nonzero) and log(−1) = iπ are Q-linearly independent. **Baker's theorem** (A. Baker, *Linear forms in the logarithms of algebraic numbers I*, Mathematika 13 (1966)) says that 1, log α_1, log α_2 are then Q̄-linearly independent. Contradiction. ∎

**Dependencies (stated honestly).**
- (a) Baker's theorem.
- (b) The standard fact that a modular form on Γ(N) with Q̄ coefficients has Q̄·(fixed algebraic factor) expansions at every cusp: Shimura's Q(ζ_N)-rationality / the q-expansion principle. I did not re-check a theorem number in this pass.
- (c) Lemmas 1–2: elementary and proved above, with numerics agreeing to 4–5 digits.

**Reading.** The remainder of C is "weight-1-sized" at q → 1, with a **regulator** (log of the fundamental unit) as its coefficient. Weight-1/2 false thetas are O(t^{−1/2}) and cannot carry it. That rules out the "residual false theta of weight 1/2" called for in `Pursue_All…` l.26 and l.125, in the strong sense of the theorem.

### A4. Theorem (multiplicative / θ-prefactor obstruction)
Let g and F be holomorphic modular forms of any weights, levels and multipliers, with g ≢ 0, and allow any q^r factor. Then **C_third·g ≠ F**.
- **Proof.** Along q = e^{−t}, F/g = c·t^{−j}e^{−α/t}(1 + O(e^{−β/t}))·(power series in t from q^r), so only integer-step powers t^{−j}, t^{−j+1}, … can appear. By Lemma 1, C_third has a nonzero t^{−1/2} term, −a_P t^{−1/2}. ∎
- With Q̄ coefficients the Baker argument gives the same for C, since c ∈ 2π·Q̄ is forced.
- This covers every space in lever 3 (k ∈ {½, 1, 3/2, 2}, N | 140 or 280, any χ) and all others, so I ran no Sturm-bound search. It would be strictly weaker.

### A5. Scalar W_7 slash obstruction (`fricke_profile.py` and `.txt`, `w7_phase.py` and `.txt`)
Take τ = x + iε. A singularity ~ G(x)I/(2πε) at x maps under W_7 to ~ |7x|²G(−1/(7x))I/(2πε). So the cocycle h = C − λ(7τ)^{−k}C(−1/(7τ)) has bounded radial limits only if G(x) = λ(7x)^{−k}|7x|²G(−1/(7x)) for all x.
- **Zero-pattern mismatch.** There are 178 of 270 rationals with denominator < 30 where exactly one of G(x) and G(W_7x) vanishes. Examples are **5/7** (a Master sample point, whose image is −1/5 with G = 0), 2/7, 4/7, 6/7, 2/3 and 4/9. At these points h is unbounded for **every** k and λ.
- **On the common support (60 pairs).** The relation holds with |·| exactly for **k = 1, |λ| = 7^{−1/2}**, with log residual 0.0000. The phase arg(G(x)/(7^{−1/2}(7x)G(W_7x))) varies with x: π/2 at 1/7 and at 1, −π/6 at 1/3 and at 3/7, and other values elsewhere. So **no constant λ** works.
- **W_35, W_70, W_140.** There are zero pairs with both values nonzero. Fully obstructed.
- **Level of the lattice.** A = [[2,7],[7,7]] has A^{−1} = [[−1/5, 1/5],[1/5, −2/35]] and discriminant group of order 35. Its level is **N = 70**, the least N with N·A^{−1} even integral (`audit_misc.txt`). τ ↦ −1/(7τ) does not normalize Γ_0(70): conjugation sends lower-left c to −7b, which needs 10 | b.
- **Consequence for Master's residual_slash.** The |7x|^{−1/2} automorphy factor has the wrong weight for the leading singularity of C. The natural exponent is |7x|^{−1}·7^{−1/2} on the support, and even that fails off it.

### A6. Audit of the "machine-precision recovery" (`audit_misc.txt`)
residual_factor = a + bt + ct² + d/(1+t²) has 4 parameters fitted to 4 ratios, with interpolation determinant 36.14118 ≠ 0. Reproducing the ratios is therefore automatic and is not a test.

This agrees with Master's own ledger, `U1_LEDGER_P_SLASH_Remark85_Interp_Prod_Obstruction_2026-09-01.md` l.36–37 ("interpolation uniqueness … not uniqueness of residual_slash"). The 4 ratios do reproduce from the complex markers: 19.801, 3.161, 20.665, 55.302.

---

## Category B (exploratory)
- **B1. Samples vs the law.**

  | x | G·I/t at ρ = 0.995 (t = 0.0050125) | C(ρe(x)) direct | Master sample |
  |---|---|---|---|
  | 1/7 | 15.79 | 4.58 + 18.92i | −18.2 + 7.8i |
  | 3/7 | 15.79 | 3.40 − 18.24i | 0.3 − 1.8i |
  | 5/7 | 15.79 | 4.27 − 19.46i | 2.1 − 9.0i |
  | 1 | 41.78 | 54.01 | 20.7 + 2.9i |

  - The direct values are consistent with Lemma 3 plus O(t^{−1/2}) corrections. The samples are not radial values of C, C_third or P_s. Their prescription is still unrecovered, as Master itself says (`Expand_Recover_Residual_Shadow_Slash_2026-08-23.md` §3).
  - |sample(1)| = 20.90 ≈ I/(2t) = 20.89 is noted only as a **numerical coincidence**. It is not evidence.
  - The samples cannot be "continuous targets" at all: the true radial values at ρ → 1 diverge like 1/t. The finite, ρ-independent targets the law yields are the singular coefficients I·G(x) (A2, Lemma 3).
- **B2. Structural reading.** P_s is a cone-restricted norm-form theta of the real quadratic field Q(√35). Its Mellin transform Γ(s)·Σ_{(n,k)≥0, ≠0} Q_s(n,k)^{−s} is a Shintani-type cone zeta whose residue at s = 1 is I = log ε/(2√35), which resembles the class-number formula. This is the classical reason unsigned real-quadratic norm-form thetas are not holomorphic modular: weight-1 Eisenstein series need odd characters, while ζ_K = ζ·L(χ_35) is even. A natural candidate "law" is therefore a Shintani/Hecke cone decomposition rather than a false theta. I did not check whether the orthant is a union of unit-group fundamental domains. The automorph [[−1,−7],[2,13]] sends (1,0) to (−1,2), not to (0,1).
- **B3. Vector-valued escape.** Over the 35 characteristic components (Zwegers Cor. 2.9(5) shape), the leading profiles G_μ(x) should transform by the weight-1 Weil representation. A **vector-valued** leading-order law is therefore expected to exist, but only for the singular parts. The cone sums themselves stay non-modular by A3. Not attempted.
- **B4.** The C t^{−1/2} coefficient is about 0.8174 from the fit, needed for A4 over C with complex coefficients. It is not derived analytically, because H_s's walls are not axis-aligned.

## Self-audit
1. **Definitions.** They are taken verbatim from Master (§0). The H_s weights were computed from c^T M, and the first C_third exponents (8, 18, 22, 30, 39, 43, 44, 58, 60, 67, 71, 78, 79, 93) match Master l.46.
2. **Series identities.** They are exact (Fractions), and box stability for H_s was checked. The q^3000 checks took about 32 s.
3. **Lemma 1 constants.** I is in closed form, confirmed to 40 digits. a_P is from quadrature, confirmed by a fit (4–5 digits). The error terms are standard Euler–Maclaurin; I did not write a formal remainder bound.
4. **Lemma 2.** This is a symmetry argument. The 1-D wall contributions are O(t^{−1/2}) by 1-D counting. Null-vector cones (Q(c) = 0) are excluded from the theorem.
5. **Baker application.** The coefficient of log(6+√35) is 1, so the relation is nontrivial. Real and imaginary parts give Q-independence. The fact about cusp expansions is cited, not re-derived.
6. **G values.** These are finite exponential sums in floating point. Nonzero values are ≥ 0.034 and zero values are < 1e−9, so zero vs nonzero is unambiguous at the tested denominators. The general formula |G| = 1/m (gcd(m,70) = 1) is observed for m < 30 and not proved.
7. **Not claimed.** I do not claim that C or C_third is quantum modular. I do not claim that no vector-valued law exists, or that the samples are wrong; their prescription is unknown. Nothing here bears on HQCC, TPC or RH.

## Files (`2026-10-17-bridge-c-residual-law/`)
- `identities.py` → `identities.txt`: A1, through q^3000.
- `diag.py`: first C_mixed point, (21,−1) at q^294.
- `asymptotics.py` → `asymptotics.txt`: A2 Lemmas 1–2.
- `roots_of_unity.py` → `roots_of_unity.txt`: Lemma 3 and the B1 table.
- `fricke_profile.py` → `fricke_profile.txt`: A5 (about 8.5 min).
- `w7_phase.py` → `w7_phase.txt`: A5 phases and zero mismatches.
- `audit_misc.py` → `audit_misc.txt`: A6, level 70, first coefficient 2 at q^102.

## Next steps (if pursued)
(a) Prove |G(h/m)| and the zero pattern in general via Gauss-sum multiplicativity (mod 2, 5, 7 and coprime parts).
(b) Build the 35-component vector of cone sums P_s^{(μ)} and test the weight-1 Weil-representation law on the singular parts (B3).
(c) Derive the t^{−1/2} coefficient of H_s analytically, to upgrade A4 for C over C.
(d) Shintani cone decomposition of the orthant relative to the automorph group of Q_s (B2).
