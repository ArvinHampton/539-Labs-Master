# ERRATUM (Local-derived) to FINDINGS_LOCAL_t4436_T_THETA1_UNARY_THETA_2026-11-10_1010.md (fff902b4…), applying PP audit df7b06d0 and tally addendum 6b43adda. 2026-11-10, written 10:27 CST (America/Chicago)

- **Scope.** Additive. The 1010 T-theta1 findings (fff902b4…), the 1024 a-3 erratum (ba558e64…), and the 1025 D=56 file (92853714…) are NOT edited, deleted, renamed or moved. The 1024 a-3 erratum correctly recorded the then-ruled tally 64/16/5/9/2, before this ACCEPT, and is left as written. No CERT. No Gemini. Nothing sent outside. Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, checked before and after writing. "Resonant algebra" (RTA historical alias only). A citation alone never makes a claim PROVED (OW 36683379). **Nothing is adopted.** Junction UNSOLVED.
- **Source audit:** FINDINGS_PP_AUDIT_LOCAL_T_THETA1_fff902b4_2026-11-10_1024.md, sha256 df7b06d07b5c6221b76b33772d131d7aa4cc9402a2c81c2e6d1aed73f432ca55 (verified on disk). Tally addendum FINDINGS_PP_AUDIT_LOCAL_T_THETA1_fff902b4_ADDENDUM_TALLY_2026-11-10_1025.md, sha256 6b43adda7525bdab2270906c14ee8546a1fc80124e6dde0d816481dc53b03aa5 (verified on disk); this addendum supersedes the 1024 audit on the two tallies only. Original findings sha256 fff902b4ea0cde17b96b0da60318afe8446f4e209dcc2d24bd26cb78a320dc59 (verified; not edited).
- **Authority.** Owner t4436. PP ruling: ACCEPT, with fixes F1–F5 (wording and a coordinate normalisation only; no further grade change beyond the already-ruled ACCEPT). Running jobs were not disturbed: s1e (PID 932685), chain_v2 (PID 1015729), s2e (PIDs 1088107/1088109), the ob_v5 waiter (PID 1096505), and pp_ttheta1_check. No heavy PARI job was started.

## F1. Identify the prefactor as j by setting z=0; θ has no zeros

1010 §1, in the U_n case of Claim J, says: "The square-root prefactor is (−2iτ₂)^{1/2}(−2iτ)^{1/2}, whose square is 4nτ+1, and the branch is the one already fixed by PP at z=0."

Replace "branch fixed by PP at z=0" by the following identification. For any word, the derived identity reads

ψ(γτ, z/(cτ+d)) = s_γ(τ) · E_γ(τ,z) · ψ(τ,z),

with E_γ(τ,0) = 1. Setting z = 0 gives s_γ(τ) θ(τ) = θ(γτ), so s_γ = j(γ,τ) identically, because θ = θ₃(2τ) has no zeros on H. This removes any branch ambiguity. The rest of Claim J, and the differentiated law (D), stand.

## F2. §0 claimed u = Σ_k χ(k) U(τ,k/7); the sum is G·u

1010 §0 states: "u(τ) = Σ_{k=1}^{6} χ(k) U(τ, k/7)". That identity is false. For every n, Σ_k χ(k) e(n k/7) equals χ(n)·G, not χ(n), where G = Σ χ₋₇(k) ζ₇^k = i√7. Hence

Ũ(τ) := Σ_{k=1}^{6} χ(k) U(τ, k/7) = G·u(τ).

(PP [B]: S_n − χ(n)G ≡ 0 mod Φ₇ for every n mod 7, and G² = −7. The sign G = +i√7 is the sine argument already in 1010 §6, independently of the typo in F5.)

Because G ≠ 0 is a constant, every step of 1010 §2 applies verbatim to Ũ: the ψ-coefficient (c z/2 − (cτ+d)m/2) expands to 0, with m = 28 k μ, c = 196 μ, z = (k/7)(cτ+d); the total exponent is −μ d k² ∈ ℤ, so e(·) = 1; the even-m shift formulas and the reindexing ℓ ≡ k d (mod 7) with χ(k) = χ(d) χ(ℓ) stand. This yields

Ũ(γτ) = χ₋₇(d) j(γ,τ) (cτ+d) Ũ(τ).

Dividing by G gives the law (L) for u, as 1010 §2 concluded:

u(γτ) = χ₋₇(d) j(γ,τ) (cτ+d) u(τ).

The conclusion of §2 is therefore unchanged. §§0 and 2 are restated with Ũ = G·u, and with the division by G at the end.

## F3. Cuspidality details: uniform-in-x bound, constancy of ε, coefficient integral

1010 §4 gives the bound |u(λ)| ≪ 1 + 1/Im(λ) and the decay of the slashed function as O(y^{−1/2}), and concludes that every Fourier expansion at a cusp has no negative index and vanishing constant term. That bound is correct and does yield a proof, once the following details (from the PP audit) are written out.

- **Bound on u.** For λ ∈ H, |u(λ)| ≤ 2 Σ_{n≥1} n e^{−2π n² Im λ} ≤ 1/(4π Im λ) + 2 · max_x x e^{−2π x² Im λ} ≪ 1 + 1/Im λ.
- **Uniformity in x.** Take σ ∈ SL₂(ℤ) with σ∞ = ς ≠ ∞ (so the lower-left entry γ of σ is nonzero). For x in one period [0,w] and y ≥ 1, one has |γτ+δ|² ≍ y² uniformly in x. So g := (γτ+δ)^{−3/2} u(στ), with any fixed holomorphic branch on H, satisfies sup_x |g(x+iy)| ≪ y^{−1/2} → 0 as y → +∞.
- **Quasi-periodicity, and why ε is constant.** Let η := σ T^w σ^{−1} ∈ ±Γ₀(196). By the law (M) and the cocycle relation, g(τ+w) = ε(τ) g(τ), where ε is continuous and takes values in a finite set of roots of unity. Since H is connected, ε is a constant ε = e(r) with r ∈ [0,1).
- **Coefficient integral.** Hence g(τ) = Σ_n b_n e((n+r)τ/w), with b_n = (1/w) ∫_0^w g(x+iy) e(−(n+r)(x+iy)/w) dx.
- **Vanishing of the non-positive terms.** |b_n| ≤ sup_x |g(·+iy)| · e^{2π(n+r)y/w}. For n+r ≤ 0 this tends to 0 as y → ∞, so b_n = 0 for all n+r ≤ 0.

Thus u is holomorphic and vanishing at every cusp (at ∞ this is direct from the series). The "either choice of branch" remark in 1010 §4 is then justified. Therefore u ∈ S_{3/2}(Γ₀(196), χ₂₈) is **PROVED**.

## F4. Coordinates [1,0,0,2,0,0,0,0,−3] are those of u/2

1010 §5 states: "the coefficients of u for n ≤ 600 > 42 agree with the unique form in this 9-dimensional space with coordinates [1,0,0,2,0,0,0,0,−3] in PARI's mfbasis, and that this form is not in K (rank 4→5). Therefore u equals that form."

s1b's series `unary(psi)` is Σ_{k≥1} ψ(k) k q^{k²}, which is **u/2** in the notation of 1010 (u = Σ_{n∈ℤ} χ(n) n e(n²τ) = 2 Σ_{k≥1} χ(k) k q^{k²}, as already written in 1010 §0). So [1,0,0,2,0,0,0,0,−3] are the coordinates of **u/2**, and u itself has coordinates [2,0,0,4,0,0,0,0,−6]. The sentence in §5 must read "**u/2** equals that form."

The Sturm identification is otherwise unchanged: s1b gives rank[C | u/2] = rank C = 9 on n ≤ 600, by exact PARI linear algebra (computational base, audited in PP 2232). So the truncated series u/2 equals C·x with x = [1,0,0,2,0,0,0,0,−3]. Setting F := Σ x_i b_i ∈ S, one has u/2 − F ∈ S vanishing for n ≤ 600 > 42 (half-integral Sturm bound at level 196, 0f1d3361 §2.6), hence u/2 = F. Membership of u in S, the Hecke eigenvalues, and u ∉ K are unaffected (the factor 2 is a nonzero scalar).

## F5. §6 typo ζ⁷ → ζ^k, and the all-p ∤ 14 eigenvalue proof

1010 §6 writes: "G := Σ_{k=1}^{6} χ_{-7}(k) ζ⁷". This should read G := Σ_{k=1}^{6} χ_{-7}(k) ζ^k. The rest of Certificate [G] (G = 1+2ζ+2ζ²+2ζ⁴ in the basis, G² = −7, and the sine-sign giving G = +i√7) is unchanged. As in the 1024 audit, the inversion formula of §6 is not required for the row; the constant in u(−1/(196τ)) remains a float illustration, COND (float), and outside the row.

**T(p²) eigenvalues for every prime p ∤ 14** (PP's hand proof, from the standard coefficient formula for weight λ+½ with λ=1). Write a(n) for the coefficients of u, and b(n) for those of T(p²)u:

b(n) = a(p² n) + χ₂₈(p) (−n/p) a(n) + p · a(n/p²),

with χ₂₈(p)(−1/p) = χ₋₇(p). Then:

- if n = k² with p ∤ k: b = χ₋₇(p) p a + χ₋₇(p) a;
- if n = k² with p | k: b = χ₋₇(p) p a + 0 + χ₋₇(p) a;
- if n is not a square: all three terms are 0.

Hence T(p²)u = χ₋₇(p)(1+p) u for every prime p ∤ 14. (Exact integer check for all primes 3 ≤ p ≤ 113, p ≠ 7, on n ≤ 300: True. These values agree with the exact PARI Hecke matrices at p = 3, 5, 11, 13, namely −4, −6, 12, −14, which also confirms the convention.) In particular T(9)u = −4u and u ≠ 0, so u ∉ K = ker T(9). "Never 49a1's or Ξ's" is unchanged and already PROVED elsewhere (|a_p| ≤ 2√p < p+1).

## Grades and tallies (PP-ruled; 1025 addendum)

Fixes F1–F5 are wording and a coordinate normalisation only; none of them changes a grade beyond the already-ruled ACCEPT.

- **Oc-3 [COND: T-theta1]** (26a7c91e, line 68: "u ∈ S_{3/2}(Γ₀(196),χ₂₈) (unary weight-3/2 theta), hence T(p²)u = χ₋₇(p)(1+p)u (computed: −4, −6, 12, −14 at p = 3, 5, 11, 13). An Eisenstein-type system, never 49a1's or Ξ's.") → **PROVED**: u ∈ S_{3/2}(Γ₀(196), χ₂₈), u/2 has coordinates [1,0,0,2,0,0,0,0,−3], T(p²)u = χ₋₇(p)(1+p)u for all p ∤ 14, and u ∉ K.
- No other row is regraded. The Oc-3 [REF] row, the Oc-3 [COND: REC] row, the Oc-3 [OPEN] Ξ_RTA row, and every other REF row are untouched. Ξ, Oc-2 and O-b stay OPEN. B5 stays PENDING.
- **t4436 (PP-ruled, per the 1025 addendum):** 96 rows: **65 PROVED / 15 CONDITIONAL / 5 OPEN / 9 REFUTED / 2 PENDING.** This is the previously ruled 64/16/5/9/2 (a-3 already PROVED in f66e0b90, as recorded in the unedited 1024 a-3 erratum) plus this one COND → PROVED. It is **not** 64/16.
- **Bridge C unchanged, at the split count:** **49 PROVED / 10 CONDITIONAL / 5 OPEN / 2 REFUTED / 1 PENDING + V₈₄ (67 rows).** T-theta1 is not a Bridge C row. The 47/11/5/2/1 + V₈₄ (66 rows) figure in 1010 §7, and in the 1024 audit before the addendum, is stale.

Nothing is adopted. Junction UNSOLVED. Local-derived. Erratum only.
