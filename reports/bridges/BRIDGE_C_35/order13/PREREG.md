# PREREG: order13. Weil-representation χ = ±i route, P-even sector as 𝓗 of arc lifts, Map E1
Written 2026-10-24, about 5:10 PM CDT, before order13 numerics. One disclosed exception: a 1-line float probe of (S̃T)³ (scratch file /tmp/probe.py, not a test) gave (S̃T)³ ≈ P to 1.6e−15, and that probe motivated §1.
Parents order5–order12 and REVIEW_PARALLEL are read-only. New files only. CORE_FREEZE. Category A = proof or exact; Category B = numerical. Runs use nice, OMP_NUM_THREADS=1, ulimit -v 3000000. No push, no sends.
Notation: S̃ = M/√35; T = exact T-matrix from symbols.T_rows. F_{α,β}(τ+1) = e(−Q(α)−B(α,hA))·F_{α,β+α+hA}(τ) holds for every ν-weighted series whose weight depends on ν only (this includes Θ_E, Ĥ, Ĝ_O and Θ_{A'}-type sums with the same A). Category A, by the computation in NOTES.

## 1. Route A done properly: the Weil-representation constraint (replaces the genus-mate basis)
**Lemma W (Category A, conditional on the exact identities E1–E2 below).** Suppose F is any nonzero 105-vector of functions, holomorphic or not, with F|₁T = T·F and F|₁S = χ·S̃·F (χ a scalar). Since (ST)³ = S² = −I in SL₂(Z) and F|₁(−I) = −F:
  χ³(S̃T)³F = −F and χ²S̃²F = −F.
With **E1: S̃² = P** (exact, order9) and **E2: (S̃T)³ = P** (to be certified exactly), this gives χ³PF = χ²PF, so **χ = 1**, and then PF = −F.
Consequences:
- No vector obeying the standard T-law obeys a χ = ±i S-law, whatever the basis for h (Weil genus mates included).
- Θ_E obeys the standard T-law, so any h with Θ_E + h modular must obey it too.
- **Route A is closed for every h (Category A).**
The genus-mate basis is therefore not needed. A Milgram remark, for context: a signature-2 lattice with the same discriminant form would need sig ≡ 0 mod 8, which is impossible in rank 2.
**Certificate test W1 (exact):** let Y = (M·T)³ and check Y = s·P with s² = 35³, i.e. the off-diagonal part of Y·P⁻¹ vanishes, its diagonal is constant, and s² − 35³ = 0. Method: all 3360 Galois embeddings of Z[e(1/9800)], max |·| < ½ (as order9 cyclo). s = +35√35 in the identity embedding. **Predicted pass.** **FAIL rule:** if any embedding gives ≥ ½, Lemma W is void and Route A reopens.

## 2. P-even part of the full series as 𝓗 of an arc Siegel lift
- **2a (Category A, algebra).** The ν-sign full weight p_full = ¼(1+s1)(1+s2) − ½(s1+s3) has P-even part ¼(1+s1s2) = ½·EVEN. So P_even(full_hol) = ½Θ_E. Check W2a: exact rational check over the box |ν| ≤ 12 for all 105 α. Disclosure: the v-vs-ν line corrections U_H, L_O (finite unary lines) are not included, and their parity is reported if cheap.
- **2b (identification, order8 M1, pass 8.7e−10).** Θ_E = 𝓗(Φ_orth), with Φ_orth = ∫ over the orthant arc [ĉ′, ĉ1] (length L = ½log(6+√35)). Φ_orth obeys the weight-0 law (Siegel, for each z). So **P_even(full_hol) = ½𝓗(Φ_orth)**, a single arc lift, not a combination.
- **2c: closed-form Laplacian defect (Category A by the order10 computation, applied to the arc [ĉ′, ĉ1]):**
  (Δ₀ − ¼)Φ_orth = (π/2)y^{3/2}[B(ĉ1) − σ·B(ĉ′)], with the orientation fixed numerically.
  - At ĉ1 (ray e2): B = √140·ϑ⁺_{7/2}·conj(ϑ⁻_{5/2}), as in order10.
  - At ĉ′ = (7,−2)/√35 (ray e1): s = √35·ν2 and s′ = ±(2ν1+7ν2), so s²/4 = 35ν2²/4 and s′²/4 = w² with w = ν1 + 7ν2/2. This gives B(ĉ′) = ±2√35·Σ_{ν2∈α2+Z} Σ_{w∈α1+7ν2/2+Z} w·ν2·e(w²τ)·conj(e(35ν2²τ/4)) × twist, glued over 2 classes (ν2 mod 2 fixes w mod ½).
  - So the P-even defect carries exactly the 5n²/2 and 35m²/4 unary series, the same two that form the ξ₁-shadow of the odd pair Ĝ_O, here with weight-3/2 partners ϑ⁺_{7/2} and Σw e(w²τ).
- **Tests (mpmath dps 30, 15 companions, |N| ≤ 8, y ∈ {½, 1, 2}):**
  - W2c: the per-Fourier-mode identity. Pass ≤ 1e−15 relative; FAIL > 1e−6.
  - W2d: the glued factorisation at ĉ′ at 3 τ. Pass ≤ 1e−20.
- **Hybrid verdict rule:** if W1, W2a, W2c and W2d pass, then **the full-series shadow is located as a hybrid**:
  - P-odd sector: the ξ₁-images (three distinct unary thetas).
  - P-even sector: ½ × the Laplacian defect of Φ_orth (2c), with no new unary theta.
  - By Lemma W, no single weight-1 ξ₁-shadow exists (Category A).

## 3. Map E1 (preregistered here, RTA-internal)
**Statement:** RTA's C leading profile Λ_C(y) = I·e(7y/20)·K2_0(y) (parent Lemma 2) obeys at y = x < 0 the sign-blind law Λ_C(−1/x) = I·e(−7/(20x))·(|x|√35)⁻¹·Σ_p e(−B(p,2a))K3_p(x), and the signed (x√35)⁻¹ version fails.
**Test E1:** g-components j = 0 (K2_0) and K3 via the b3x method at x ∈ {−1/5, −2/3, −3/4}, comparing (S̃g)_0 under the |x| law against the signed law. Pass ≤ 1e−15; the signed law is predicted to FAIL (residual ≈ 2).
**Scope:** this is a prediction about RTA's C at negative rationals (Theorem 3 covered x > 0 only). It is NOT a Residual↔Resonant bridge. The Resonant-side (T3/O_res/Π) half stays OPEN: no concrete Resonant profile is available in the tree.
