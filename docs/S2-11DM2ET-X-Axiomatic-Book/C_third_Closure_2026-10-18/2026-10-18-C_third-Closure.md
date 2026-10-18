> **Master-copy notation note (added 2026-10-18 at push; report text below is otherwise verbatim).** The weight-0 identification is by citation of Zwegers 2012 (via a restatement); Cat B on Master. ∫_{Γ_F} Ξ₁ = 0 is numerical (Cat B). Category convention for Master (rev. 4): Cat A = proved, or exact (including exact finite computation); floating-point-only results = Cat B. Where this report labels a floating result Cat A, read it as Cat B (C12, C13). Theorem names: Theorem G = Lewis–Zagier period theorem (rev. 3 meaning); the g_s asymptotics = Theorem G_s; the zero-set theorem = Theorem D. Erratum: ERRATUM_Consolidated_CrossReview_2026-10-18.md. Consolidated statement: Bridge_C_Consolidated_rev4_2026-10-18/.

# C_third — Closure (Path C follow-up)

Date: 2026-10-18 (CDT). Local only; nothing pushed. Builds on `2026-10-18-C_third-Unified.md` and `2026-10-18-C_third-Unified/LEMMAS_C.md`.
Labels: **Cat A** = exact or proved. **Cat B** = numerical, conjectural, or identification by citation only. No TPC/RH claims.

Scripts and outputs: `2026-10-18-C_third-Closure/`
- `unified_theta_check.py`: numerical test of the unified construction.
- `unified_theta_check_s7.txt`, `_s9.txt`, `_s13.txt`: outputs at τ = 0.137 + 0.61i, box R = 30.

## 1. Summary

| Item | Result | Status |
|---|---|---|
| One kernel for both parts | Ξ = Ξ₀ + Ξ₁ on the space of lines c(t) in the signature-(1,1) plane. Ξ₀ is a Siegel theta (weight 0). Ξ₁ is a Kudla–Millson-type insertion 2B(n,c′(t))√y (weight 1). Same coset a+Z², same Q. | A (definitions; the two integral identities below) |
| ∫ Ξ₁ dt equals Zwegers' 2002 completion | Exact, by the fundamental theorem of calculus | A (proof §3); numerical diff ≤ 6e−17 |
| ∫ Ξ₀ dt equals Zwegers' 2012 mock Maass theta Θ_a when c₂ = γc₁ and γa ≡ a | Diff 8e−16 (s = 7), 8e−16 (s = 9), 5e−15 (s = 13) | B (Lemma 2.4 of Zwegers 2012, used via its restatement in BCN; checked numerically) |
| Unit-cone (F) weight-1 piece is zero | ∫_{[c₁,γc₁]} Ξ₁ = 0, numerically about 1e−15 | B (numerical; proof sketch §3.3) |
| Non-γ chain: shadow does not cancel | \|Θ̂ − Θ\| ≈ 0.11–0.13 for (c₁, c(t₂/3)) | B (numerical control) |
| Sign weights vs F-cone counts | max deviation 0 for Q ≤ 30 | A on that finite range |
| One object of a single weight | **No.** Two chains (unit cone F and quadrant Q₁), and two different holomorphic extractions | A for the obstruction as in the prior report; B for "no other kernel exists" |
| Higher depth | Not available for the natural lattice: rank 2 means depth ≤ 1 | B (discussion §5) |

## 2. The construction

Set B(x,y) = xᵀAy with A = [[2,s],[s,s]] and Q(n) = ½B(n,n), giving Q = Q_s on ν = (n,k). Fix a = (s/(2(s−2)), −1/(s−2)) and γ = [[−1,−s],[2,2s−1]].

**Path of lines.** c₁ = (s,−2)/√(s²−2s) has Q(c₁) = 1. Take e₁ ⊥ c₁ with Q(e₁) = −1. Then c(t) = cosh t·c₁ + sinh t·e₁ and c′(t) = c⊥(t). The endpoint is c(t₂) = γc₁ with |t₂ − t₁| = log ε, where ε is the fundamental unit attached to γ. Numerically log ε = 2.477888730288 at s = 7, and the script reproduces |t₂ − t₁| to 12 digits.

**Kernels** (y = Im τ):
- Ξ₀(τ,t) = √y Σ_{n∈a+Z²} q^{Q(n)} e^{−πy B(n,c(t))²}
- Ξ₁(τ,t) = √y Σ_{n∈a+Z²} 2B(n,c′(t)) q^{Q(n)} e^{−πy B(n,c(t))²}

Both converge absolutely. The combined exponent −2πy(Q(n) + ½B(n,c(t))²) is −2πy times the Siegel majorant, which is positive definite. The first version of the script had an OverflowError because it multiplied a huge factor by a tiny one; it now computes the exponent as one quantity.

**The two parts of C_third.** Recall from the prior report:

  2C_third − 1 + θ₃ = q^{c₀}·Σ_{a+Z²} (1_{F′} + 1_{−Q₁}) q^Q,  with 1_K = ¼(ρ_odd + ρ_even).

- **Even part (E_L).** This is ¼ρ_even on the unit cone F, whose boundary vectors are c₁ and γc₁. Take Γ_F to be the segment [c₁, γc₁]. Then ∫_{Γ_F} Ξ₀ dt = Θ̂_a, and Θ̂_a = Θ_a is Zwegers' 2012 mock Maass theta, with no shadow. Its Lewis–Zagier / false-indefinite partner ϑ_a = ½Σ(1 − sgn·sgn)q^Q gives E_L = ½ϑ_a. Here Lemma R and a ∉ Z² are used, and the constant term corresponds to log ε. Check (A) confirms the analytic identity.
- **Odd part (Zwegers' 2002 ϑ_hol).** This is −½ρ_odd on the quadrant Q₁, which has two negative-norm c's. On the corresponding chain Γ_{Q₁}, ∫ Ξ₁ dt is exactly Zwegers' completion Σ[E(B(n,c₂)√y) − E(B(n,c₁)√y)]q^Q, with E(z) = erf(√π z). Its holomorphic part is ϑ_hol.
- **The F-cone weight-1 piece ¼ρ_odd^F** gives ∫_{Γ_F} Ξ₁ = 0. Check (B) gives about 1e−15. This is the analytic counterpart of the prior finding that this piece "contributes nothing".

**Net statement.** One kernel Ξ, one coset and one quadratic form produce both parts. The chain is Γ = Γ_F + Γ_{Q₁}. The weight-0 component of Γ_F gives E_L. The weight-1 component of Γ_{Q₁} gives the Zwegers part. The weight-1 component of Γ_F vanishes.

The construction is still not a single modular object. The two outputs come out of different operations:
- holomorphic projection / mock completion at weight 1;
- the Lewis–Zagier period correspondence at weight 0.

They also carry different automorphy factors: (cτ+d) versus |cτ+d|. This matches obstructions O1 and O2 in the prior report.

## 3. Proofs and checks

### 3.1 Weight-1 identity (Cat A)
Normalise Q(c(t)) = 1 and c′ ⊥ c. Then d/dt B(n,c(t)) = B(n,c′(t)), so

  d/dt E(√y B(n,c(t))) = 2√y B(n,c′(t)) e^{−πyB(n,c(t))²}.

Multiply by q^{Q(n)} and sum. The termwise integral is dominated by the Siegel majorant, so sum and integral can be swapped. This gives ∫_{t₁}^{t₂} Ξ₁ dt = Σ[E(√yB(n,c(t₂))) − E(√yB(n,c(t₁)))] q^Q.

Numerically: diff 5.65e−17 (s = 7), 3.27e−17 (s = 9), 1.99e−17 (s = 13) on the non-trivial pair (c₁, c(t₂/3)). The non-trivial pair is used because the γ-pair value is identically 0.

### 3.2 Weight-0 identity (Cat B by citation)
With c₂ = γc₁ and γa ≡ a mod Z², sgn(t₂−t₁)·Θ_a (Zwegers' K₀ sign series plus the c⊥ term for Q < 0 plus the δ-term) equals ∫Ξ₀ dt. The orientation sign was missing from the first comparison: the raw outputs differed by exactly a factor −1, since t₂ − t₁ < 0 at these s. With the sign restored the diffs are at the 1e−15 level.

The identity is Zwegers' result in "Mock Maass theta functions" (Q. J. Math. 2012), as restated (Lemma 2.4 in their numbering) in Bringmann–Craig–Nazaroglu, arXiv:2409.17818, §2.2. The original paper is paywalled and was **not read**; only the restatement was. So the identification stays Cat B. The numerics confirm it at three values of s.

Control: for a non-γ pair, Θ̂ ≠ Θ (difference about 0.1), as expected when φ^{[c₁]} − φ^{[c₂]} does not cancel.

### 3.3 Vanishing of the unit-cone weight-1 piece (Cat B)
Proof sketch: n ↦ γn permutes a+Z², preserves Q, and B(γn, γc₁) = B(n,c₁). So the two halves of the completion sum match term for term.

The halves do not converge separately: Q < 0 terms are undamped once split. A rigorous version must pair the terms inside the absolutely convergent combined sum. That bookkeeping is not written out, so the vanishing is kept as Cat B. Numerically it is 0 to 1e−15 at s = 7, 9, 13.

## 4. What is still open
- Reading Zwegers 2012 directly. It is paywalled; the Cat B identification rests on the BCN restatement plus these numerics.
- A rigorous pairing argument for §3.3.
- A genuinely single-weight object. Every attempt splits into weight 0 and weight 1. Whether some exotic kernel exists is open (Cat B).

## 5. Higher depth
The lattice is rank 2 with signature (1,1). Indefinite theta functions of depth r need cones cut out by r independent negative directions. The constructions of Alexandrov–Banerjee–Manschot–Pioline and of Bringmann–Kaszian–Milas–Nazaroglu need signature (n−r, r) with r ≥ 2, so rank ≥ 3. Here every cone is bounded by two lines, which gives depth ≤ 1: Zwegers 2002 / 2012.

Higher-depth objects could only appear after enlarging the lattice. One option is tensoring with a unary theta: θ₃ already appears in C_third, giving rank 3 with signature (1,2) or (2,1). Whether ½(1−θ₃) + ½q^{c₀}Θ_w can be rewritten as a depth-2 theta on a rank-3 lattice was **not attempted** beyond this observation (Cat B, open).
