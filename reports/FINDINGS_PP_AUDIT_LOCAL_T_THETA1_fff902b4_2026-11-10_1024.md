# FINDINGS (PP Soft SF audit): Local T-theta1 discharge (fff902b4…). 2026-11-10, written 10:24 CST (America/Chicago)

- **Scope.** Additive. No existing file edited. Nothing written into Local's directories (PP evidence is in `reports/pp_evidence_ttheta1_fff902b4_2026-11-10_1023/`). No CERT. No Gemini. No external send. Nothing adopted. Junction UNSOLVED. "Resonant algebra" (RTA historical alias only).
- **Integrity (checked 10:12 and again 10:23 CST).**
  - Report FINDINGS_LOCAL_t4436_T_THETA1_UNARY_THETA_2026-11-10_1010.md = fff902b4ea0cde17b96b0da60318afe8446f4e209dcc2d24bd26cb78a320dc59 = sidecar. OK.
  - s13_t_theta1_unary_certificate.py = f928f94da38386cf58e02f49830d6195eb01c48392332b30c0246ef205e69c73 = sidecar. OK.
  - s13_t_theta1_unary_certificate.log = d72fbb662da0d097178091661852dc2474f40cf0f26ef9f15c6ce26848ae6186 = sidecar. OK.
  - s1b_oc_branches.py / .log: sidecars OK.
  - Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 MATCH (before and after). 26a7c91e… and ab20f7ca… MATCH their sidecars (unchanged).
- **Running jobs.** Not touched. s1e (932685) and chain (1015729) running throughout. ob_v4_6272_D56 (1045533/1045534) exited on its own between 10:12 and 10:22 CST, and the chain then started s2e_j2_level9800 (1088107/1088109); PP did not signal or touch any of these. Local should read the ob_v4 log for its result.
- **Method.** Local's script copied to PP scratch (`/workspace/pp_scratch_ttheta1_1030/s13_copy.py`, sha identical) and re-run: output identical. Independent PP script `pp_ttheta1_check.py` (1883b9cd…), log `pp_ttheta1_check.log` (cd12facb…). Exact tests only: polynomial remainder mod Φ₇, sympy `expand`/`cancel` on polynomial and rational-function identities, `Fraction` Gaussian-rational arithmetic. Floats appear only in clearly marked illustrations.

## Row being regraded

Exactly one row: 26a7c91e, branch **Oc-3** (O-c), the row tagged **[COND: T-theta1]** (line 68): "u ∈ S_{3/2}(Γ₀(196),χ₂₈) (unary weight-3/2 theta), hence T(p²)u = χ₋₇(p)(1+p)u (computed: −4, −6, 12, −14 at p = 3, 5, 11, 13). An Eisenstein-type system, never 49a1's or Ξ's."

Not touched: the Oc-3 **[REF]** row (single-square-class readings; upheld in PP 2232 b6c246a8 for every squarefree t), the Oc-3 [COND: REC] row, the Oc-3 [OPEN] Ξ_RTA row, the other Oc-3 PROVED rows, and every other REF row. No new proof bears on any REF row. T-theta1 is used by this one row only (5 mentions in 26a7c91e, all naming this row or its discharge; 0 in ab20f7ca), and it does not occur in the Bridge C files.

## Step-by-step ruling

### (1) Jacobi extension of the θ-law, and the derivative law (D): **PROVED**

- Inversion ψ(Wσ,w) = (−2iσ)^{1/2} e(σw²) ψ(σ,2σw): PP re-derived it from F0-5. Poisson with f(x) = e(−x²/(4σ) + xw) and the Gaussian integral gives f̂(ξ) = (−2iσ)^{1/2} e(σ(w−ξ)²). Summing and using ψ(σ,−v) = ψ(σ,v) gives the formula.
- U_n = W∘T^{−n}∘W as Möbius maps: checked.
- Exact sympy checks (rational-function identities, `cancel` = 0):
  - 4ττ₂w₃ + z = 0;
  - τ₂w₃² + 4ττ₂²w₃² − nz²/(4nτ+1) = 0;
  - (−2iτ₂)(−2iτ) − (4nτ+1) = 0;
  - composition: c₂d + c₁ − cd₂ = −c₁(a₂d₂ − b₂c₂ − 1) = 0.
- T^n and −I cases: correct.
- (D) follows by z-differentiation: checked by hand.
- **Branch (fix F1).** The proof is complete once one line is stated. For any word, the derived identity reads ψ(γτ, z/(cτ+d)) = s_γ(τ)·E_γ(τ,z)·ψ(τ,z), with E_γ(τ,0) = 1. Setting z = 0 gives s_γ(τ)θ(τ) = θ(γτ), so s_γ = j(γ,τ) identically (θ = θ₃(2τ) has no zeros on H). This removes any branch ambiguity; "fixed by PP at z = 0" should be replaced by this sentence.

### (2) Law (L) and multiplier χ₂₈(d) j³: **PROVED, after fix F2**

- **Slip (fix F2, does not change the conclusion).** §0 claims u(τ) = Σ_{k=1}^{6} χ(k) U(τ,k/7). This is false. The sum Σ_k χ(k) e(nk/7) equals χ(n)·G for every n, not χ(n), so the sum over k is **G·u**, where G = Σχ₋₇(k)ζ₇^k = i√7.
  - Exact proof: PP [B] checks S_n − χ(n)G ≡ 0 mod Φ₇ for every n mod 7, and G² = −7.
  - FLOAT illustration only: the ratio Ũ/u = 2.64575131106459i = i√7 at 40 digits.
- Because G ≠ 0 is a constant, every step of §2 applies verbatim to Ũ := G·u, and dividing by G gives (L) for u. §0 and §2 must be restated with Ũ = G·u.
- §2 algebra, exact (sympy):
  - the ψ-coefficient (cz/2 − (cτ+d)m/2) expands to 0, with m = 28kμ, c = 196μ, z = (k/7)(cτ+d);
  - the total exponent is −μdk², which lies in ℤ, so e(·) = 1;
  - the shift formulas (m even) and the reindexing ℓ ≡ kd mod 7 with χ(k) = χ(d)χ(ℓ) were checked by hand.
- **κ(γ) = χ₋₄(d), proved exactly and without evaluation.**
  - By Θ4, κ(γ) := j(γ,τ)²/(cτ+d) is a ratio of two cocycles, constant in τ, so it is a homomorphism Γ₀(4) → {±1}.
  - Its values on the generators are κ(T) = 1, κ(U₁) = 1 (j² = 4τ+1) and κ(−I) = 1/(−1) = −1.
  - These match χ₋₄(1) = 1, χ₋₄(1) = 1 and χ₋₄(−1) = −1.
  - d ↦ χ₋₄(d) is a homomorphism on Γ₀(4), since d(γ₁γ₂) = c₁b₂ + d₁d₂ ≡ d₁d₂ (mod 4) because 4 | c₁.
  - Hence κ = χ₋₄(d) on **all** of Γ₀(4), and so on Γ₀(196).
- (−7/·)(−4/·) = (28/·) by complete multiplicativity of the Kronecker symbol in its upper argument. [C] is a consistent range check.
- **(M): u(γτ) = χ₂₈(d) j(γ,τ)³ u(τ) for every γ ∈ Γ₀(196): PROVED.** This is the PARI/PP θ-multiplier convention for M_{3/2}(Γ₀(196),χ₂₈) used in 0f1d3361.

### (3) Certificate [K]: **reproduced, and exact for the reason stated**

- Local's run reproduces exactly: index 336, 166 generators, 0 mismatches.
- PP independent run, using Gaussian-rational `Fraction` arithmetic and PP's own word algorithm:
  - on Local's 166-generator set, at two **new** points τ₀ = 3/11 + i/13 and −5/9 + 2i/7: j²/(cτ₀+d) = χ₋₄(d) exactly, 0 mismatches;
  - on an independent Schreier set (DFS coset tree on P¹(ℤ/196), index 336, 115 nontrivial generators), at the same two points: 0 mismatches;
  - the word sign (−1 exactly from −I) equals χ₋₄(d) on both sets.
- **Why a point check is exact here.** It is **not** a test of an identity between modular forms. The quantity tested is a constant. By Θ4, j² is the product ∏(4n_iτ_i + 1) along the word, which equals κ(γ)(cτ+d) as a rational-function identity in τ (the cocycle telescopes). So one exact Gaussian-rational evaluation determines κ(γ) ∈ {±1}, and the second point is a control. In any case, the generator argument in (2) already proves κ = χ₋₄(d) without [K]. [K] is corroboration.

### (4) Cuspidality: **a proof (Hecke's argument), PROVED after fix F3**

Local's bound is correct, and it does yield a proof rather than only a bound. The full argument:

- **Bound on u.** For λ ∈ H, |u(λ)| ≤ 2Σ_{n≥1} n e^{−2πn² Im λ} ≤ 1/(4π Im λ) + 2·max_x x e^{−2πx² Im λ} ≪ 1 + 1/Im λ.
- **Uniformity in x.** Take σ ∈ SL₂(ℤ) with σ∞ = ς ≠ ∞ (so γ ≠ 0). For x in one period [0,w] and y ≥ 1, one has |γτ+δ|² ≍ y² uniformly. So g := (γτ+δ)^{−3/2} u(στ), with any fixed holomorphic branch on H, satisfies sup_x |g(x+iy)| ≪ y^{−1/2} → 0.
- **Quasi-periodicity.** η := σT^wσ^{−1} ∈ ±Γ₀(196). By (M) and the cocycle relation, g(τ+w) = ε(τ)g(τ), where ε is continuous with values in a finite set of roots of unity. Since H is connected, ε is a constant ε = e(r), r ∈ [0,1).
- **Fourier expansion.** Hence g(τ) = Σ_n b_n e((n+r)τ/w), with b_n = (1/w)∫_0^w g(x+iy) e(−(n+r)(x+iy)/w) dx.
- **Vanishing of the non-positive terms.** |b_n| ≤ sup_x|g(·+iy)|·e^{2π(n+r)y/w}. For n + r ≤ 0, this tends to 0 as y → ∞. So b_n = 0 for all n + r ≤ 0.
- **Conclusion.** u is holomorphic and vanishing at every cusp. At ∞ this is direct. u ∈ S_{3/2}(Γ₀(196),χ₂₈): **PROVED.**
- Fix F3: Local's §4 should state the uniform-in-x bound, the constancy of ε, and the coefficient integral explicitly. The "either choice of branch" remark is then justified.

### (5) Sturm identification, coordinates, eigenvalues, and u ∉ K: **PROVED, after fix F4**

- **Sturm identification.** s1b gives rank[C|u] = rank C = 9 on n ≤ 600, using exact PARI linear algebra (computational base, audited in PP 2232). So the truncated series u/2 equals C·x with x = [1,0,0,2,0,0,0,0,−3]. Set F := Σ x_i b_i ∈ S. Then u/2 − F ∈ S vanishes for n ≤ 600 > 42 (half-integral Sturm bound at level 196, 0f1d3361 §2.6). So u/2 = F.
- **Fix F4 (normalisation).** s1b's `unary(psi)` is Σ_{k≥1} ψ(k) k q^{k²}, which is **u/2** in fff902b4's notation (u = Σ_{n∈ℤ}). So [1,0,0,2,0,0,0,0,−3] are the coordinates of **u/2**, and u itself has coordinates [2,0,0,4,0,0,0,0,−6]. §5's "u equals that form" must read "u/2 equals that form". Membership and eigenvalues are unaffected.
- **T(p²) eigenvalues.** At p = 3, 5, 11, 13 the eigenvalues are −4, −6, 12, −14, from exact PARI Hecke matrices (base). **PP strengthening: PROVED for every prime p ∤ 14**, by a hand proof from the standard coefficient formula for weight λ + ½ with λ = 1:
  - b(n) = a(p²n) + χ₂₈(p)(−n/p) a(n) + p·a(n/p²), with χ₂₈(p)(−1/p) = χ₋₇(p).
  - If n = k² with p ∤ k: b = χ(p)p a + χ(p) a.
  - If n = k² with p | k: b = χ(p)p a + 0 + χ(p) a.
  - If n is not a square: all three terms are 0.
  - So T(p²)u = χ₋₇(p)(1+p)u.
  - Exact integer check for all primes 3 ≤ p ≤ 113 (p ≠ 7) on n ≤ 300: True. The values agree with PARI at p = 3, 5, 11, 13, which also confirms the convention.
- **u ∉ K = ker T(9).** T(9)u = −4u and u ≠ 0. Exact.
- **"Never 49a1's or Ξ's".** Unchanged and already PROVED elsewhere (|a_p| ≤ 2√p < p+1).

### §6 inversion formula

Local marks it as not required, and PP does not use it.

- The sign of G (G = +i√7) is correct, by the sine argument.
- The constant in u(−1/(196τ)) is supported by floats only, so it is **COND (float)** and outside the row.
- Fix F5: in §6, "Σ χ₋₇(k) ζ⁷" should read Σ χ₋₇(k) ζ^k.

## Verdict

**ACCEPT, with fixes F1–F5** (wording and normalisation only; none changes a grade).

- Oc-3 [COND: T-theta1] → **[PROVED]**: u ∈ S_{3/2}(Γ₀(196),χ₂₈), u/2 has coordinates [1,0,0,2,0,0,0,0,−3], T(p²)u = χ₋₇(p)(1+p)u for all p ∤ 14, u ∉ K. An Eisenstein-type system.
- **t4436 tally: 96 rows, PROVED 64 · COND 16 · OPEN 5 · REFUTED 9 · PENDING 2** (from 63/17/5/9/2). All REF rows untouched.
- **Bridge C unchanged:** 47/11/5/2/1 + V₈₄ (66 rows).
- Ξ_RTA stays OPEN. Oc-2 stays OPEN. B5 stays PENDING. O-b stays OPEN. Nothing adopted. Junction UNSOLVED.

## Fixes for Local (next additive file; fff902b4 is not to be edited)

- **F1.** State the identification s_γ = j(γ,τ) via z = 0 and the non-vanishing of θ, in place of "branch fixed by PP at z = 0".
- **F2.** §0: Σ_k χ(k) U(τ,k/7) = G·u with G = i√7, not u. Restate §2 with Ũ = G·u and divide by G at the end.
- **F3.** §4: write out the uniform-in-x bound, the constancy of the root of unity ε, and the Fourier coefficient integral.
- **F4.** §5: the coordinates [1,0,0,2,0,0,0,0,−3] are those of u/2. u = [2,0,0,4,0,0,0,0,−6].
- **F5.** §6 typo: ζ⁷ → ζ^k. Optionally add PP's all-p ∤ 14 eigenvalue proof.

## PP evidence

| File | sha256 |
|---|---|
| pp_evidence_ttheta1_fff902b4_2026-11-10_1023/pp_ttheta1_check.py | 1883b9cd7b00c0ba8a12b3a9eaab7d51b5d38bfa29429069a4ab59e2a2a0e7a2 |
| pp_evidence_ttheta1_fff902b4_2026-11-10_1023/pp_ttheta1_check.log | cd12facba3e1ff90aa2cb32dc68aaa31ecec05ae200deaf3c96d844bbc94c852 |

Tip 7cddb188 MATCH. Running jobs untouched. Nothing adopted.
