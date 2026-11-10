# PREREG: order5. True Zwegers completion of the cone part, its shadow, and a sharpened A2 mixed-law test
Written 2026-10-24, about 2:10 PM CDT (America/Chicago), before any order5 computation. Owner: Arvin Hampton.
Folder `reports/bridges/BRIDGE_C_35/order5/` (new files only). CORE_FREEZE: H_s is not redefined; no certifier code is touched; order2/order3c libraries and A35 `symbols.py` are imported read-only. Category A = proof or exact identity; Category B = floating-point / numerical evidence. No pushes, no external sends. Runs: `nice`, `OMP_NUM_THREADS=1`, `ulimit -v 3000000`.

## 0. Notation (unchanged from order2)
A = [[2,7],[7,7]], det A = −35, Q(ν) = ½νᵀAν = ν1² + 7ν1ν2 + (7/2)ν2², B(u,v) = uᵀAv. Companion (α,β) from the 35-component law vector families K2, K3, K4 (105 pairs, `sym_pair`). ν = α + v, v = (n,k) ∈ Z², f(v) = e(xQ(ν) + B(ν,β)).
S_{α,β} = Σ_v wt(v) e(B(ν,β)) q^{Q(ν)}, wt(v) = 1[n≥0,k≥0] − w(v), w(v) = ½(sgn n + sgn(n+21k)), sgn 0 = 0. So S = P_orth − H with H = Σ w(v)·(…) (the 105 shifted and twisted cone series) and P_orth the closed-orthant series.

## 1. Derivation (Category A, written before numerics)
### 1.1 Indefinite form and cone structure
Q has signature (1,1). With c1 = (−1,1), c2 = (−4,1): A c1 = (5,0), A c2 = (−1,−21), so B(c1,v) = 5n and B(c2,v) = −(n+21k). Hence
  w(v) = ½(sgn B(c1,v) − sgn B(c2,v)) — exactly Zwegers' ρ^{c1,c2}, evaluated at v (not at ν).
Q(c1) = −5/2, Q(c2) = −17/2 (both negative), B(c1,c2) = −20 < 0: same component of the negative cone, so Zwegers' convergence condition holds.
Orthogonal (wall) directions: c1^⊥ = (0,1), Q = 7/2; c2^⊥ = (21,−1), Q = 595/2. These are exactly the order3 wall labels 7/2 and 595/2.
Orthant: B(c',v) = −35k for c' = (−7,2) (A c' = (0,−35)), Q(c') = −35, B(c1,c') = −35 < 0, B(c2,c') = −35 < 0; c'^⊥ = (1,0), Q = 1 (the order3 label 1). In the v-variables:
  orth(v) − orth(−v) = ½(sgn B(c1,v) − sgn B(c',v)) + F(v),  F(v) = ½ sgn(n)·[k=0] + ½ sgn(k)·[n=0]
(F = axis false-theta weights). orth(v) + orth(−v) (the double orthant) is NOT of Zwegers type; it is not completed here.

### 1.2 v-signs versus ν-signs (exact line corrections)
Zwegers' completion uses ν. Let ρ_H(ν) = ½(sgn ν1 + sgn(ν1+21ν2)) and ρ_O(ν) = ½(sgn ν1 + sgn ν2). Then, exactly,
  ρ_H(ν) − w(v) = Δ_H(v) = ½[sgn(n+α1) − sgn n] + ½[sgn(m+s) − sgn m],  m = n+21k, s = α1+21α2,
  ρ_O(ν) − ½(sgn n + sgn k) = Δ_O(v) = ½[sgn(n+α1) − sgn n] + ½[sgn(k+α2) − sgn k].
Each is constant on finitely many FULL lattice lines: n = const (direction (0,1)), m = const (direction (21,−1)), k = const (direction (1,0)). Write U_H = Σ_v Δ_H f q^Q, U_O = Σ_v Δ_O f q^Q (finite sums of full unary theta series, holomorphic, weight ½).

### 1.3 Completion constants (the derived prediction)
Ĥ_{α,β}(τ) = Σ_{ν∈α+Z²} ρ̂_H(ν;y) e(Q(ν)τ + B(ν,β)), y = Im τ, with E(z) = 2∫_0^z e^{−πu²}du = erf(√π z) and
  ρ̂_H = ½[ E(B(c1,ν)√y/√(−Q(c1))) − E(B(c2,ν)√y/√(−Q(c2))) ] = ½[ E(√10·ν1·√y) + E((ν1+21ν2)·√(2y/17)) ].
Orthant odd pair: ρ̂_O = ½[E(√10·ν1√y) + E(√35·ν2√y)] (c' term: B(c',ν)/√35 = −√35ν2).
Radial point: τ = x + i t/(2π), so y = t/(2π) and the E-arguments are functions of √t·ν only.
**Prediction Z (fixed S-law, Zwegers Cor. 2.9 specialised):** for every companion j,
  Ĥ_j(−1/τ) = (τ/√35) Σ_k M_jk Ĥ_k(τ),
with M the fixed 35-component law vector S-matrix of A35 `symbols.S_rows` (the same matrix as the A0 law G(−1/x) = (|x|√35)^{-1}·M·G(x)). Same for Ĝ_O := Σ ρ̂_O(…).

### 1.4 Radial expansion of the completed series (Category A, proof sketch fixed now)
(i) Φ(u) = ρ̂_H(u; 1/(2π)) e^{−Q(u)} is smooth and Gaussian-decaying with derivatives (Zwegers). Σ_v f(v)Φ(√t ν) with f N-periodic (N = 2m): Poisson summation gives t^{−1}·mean(f)·∫Φ + O(t^∞). Hence **Ĥ has no t^{−1/2} and no t^0 term** at any rational x.
(ii) R := Ĥ_ν − H_ν = Σ_j γ_j Σ_ν (E_j − sgn_j)(…) f q^Q (γ = ±½). Summing first along lines parallel to c_j^⊥ (full lines, Poisson, O(t^∞) errors) leaves a 1-D sum Σ_ℓ m_ℓ h(√t(ℓ+θ)) with h(σ) = (E − sgn)(κσ)·G(σ), G even. 1-D Euler–Maclaurin: the t^{−1/2} coefficient of R is a pure jump-sawtooth sum (jump 2√(π/Q(u_j))), ∫h = 0 (h odd), and the next coefficient is ∝ jump of h′ at 0 = 2G′(0) = 0. So A2(R) = 0, and the E-argument constants do not enter A1 or A2 (they enter only the S-law, test Z).
(iii) Full lines: Σ_b g(b) e^{−tQ(p0+bu)} = √(π/(tQ(u)))·mean(g)·e^{−tK} + O(t^∞): A1 contribution √π Q(u)^{−1/2}·mean(g), A2 contribution 0.
**Consequences (exact):**
- **P1.** A2(H) ≡ 0 for all 105 companions and all rational x (H = cone pieces + half-weight walls of order2 lib2, i.e. everything except the orthant piece).
- **P2.** Odd combinations: S_odd := S_{α,β} − S_{−α,−β} = Σ_v (wt(v) − wt(−v)) f q^{Q(ν)} (exact, by v → −v), and A2(S_odd) = A2(F), with F the axis false thetas (ray constants of order3c), because S_odd = [Zwegers part in ν] − U_O + 2U_H + F.
- **Completed objects.** Ĉ := C − R_H = P_orth − Ĥ + U_H, so A1^c = A1(orth piece) + A1(U_H), A2^c = A2(orth piece). Odd completion Ŝ_odd = Ĝ_odd + (−U_O + 2U_H + F) with Ĝ_odd = Ĝ_O − 2Ĥ: A1^c_odd = A1(−U_O + 2U_H) + A1(F), A2^c_odd = A2(F).

### 1.5 Predicted shadow (weight-3/2 unary theta series)
∂_τ̄ E(a√y) = (i a/(2√y)) e^{−πa²y}, and e^{−πa²y}e(Q(ν)τ) = e(Q(u_j)s_j²τ)·conj(e(|Q(c_j)|w_j²τ)) with ν = s_j u_j + w_j c_j. Hence
  ∂_τ̄ Ĥ_{α,β} = −(i/(2√y)) Σ_{j=1,2} σ_j √|Q(c_j)| Σ_ν w_j e(Q(u_j)s_j²τ + B(ν,β)) · conj(e(|Q(c_j)| w_j² τ)), σ = (+1,−1),
- c1: s = ν1+ν2, w = −ν1 (unimodular, splits exactly): θ_{7/2}(s ∈ α1+α2+Z) × conj g_{5/2}(n ∈ α1+Z), g_{Q}(τ) = Σ n e(Qn²τ) (weight 3/2, form (5/2)n² = (5n)²/10);
- c2: s = (ν1+4ν2)/17, w = (ν1+21ν2)/17: θ_{35/34}(P = ν1+4ν2) × conj g(R = ν1+21ν2) with weight-3/2 theta Σ R e(R²τ/34), glued over 17 classes (index 17);
- orthant pair c': s = ν1 + 7ν2/2, w = ν2/2: θ_{1} × conj Σ ν2 e((35/4)ν2²τ), glued over 2 classes.
Predicted shadow of the cone part: the weight-3/2 unary thetas Σ n e(5n²τ/2) (n ∈ α1+Z) and Σ R e(R²τ/34) (R ∈ α1+21α2+Z), each paired with the weight-½ unary theta of its wall direction (Q = 7/2, 595/2).
**P3 (identity check).** Finite-difference ∂_τ̄Ĥ agrees with the shadow double sum above.

## 2. Tests for task (a)
- **Z (Category B, decisive for the constants).** 120 interior points τ (fixed by script: x ∈ [−0.45,0.45], y ∈ [0.55,1.3], |τ| ∈ [0.8,1.25], deterministic grid with seed 5), box |n|,|k| ≤ 40 (truncation checked against 50). Statistic r = max over τ,j of |Ĥ_j(−1/τ) − (τ/√35)(MĤ(τ))_j| / max(1, max|Ĥ(−1/τ)|). Pass r ≤ 1e−10; fail r > 1e−4; else inconclusive. Same for Ĝ_O.
  Controls (gating, both must FAIL the law, r > 1e−4): (i) holomorphic H_ν (E→sgn); (ii) E-arguments scaled by 1.25. If a control passes, Z is void.
- **P1, P2 (Category B check of a Category A statement).** Max |A2(H)| and max |A2(S_odd) − A2(F)| over 105 × 216 × {x, −1/x}: pass ≤ 1e−11, fail > 1e−6.
- **P3.** 4 τ × 6 companions, central differences h = 1e−5: pass rel. err ≤ 1e−6.
- **C (completed S-law, Category B).** On XS216, SVD threshold 1e−9, closure iff rank[F | diag(|x|^w)F(−1/x)] = rank F; plus the fixed-matrix residual F(−1/x) vs |x|^{−w}(1/√35)M F(x). Objects: A1^c (w = ½, 1), A1^c_odd (w = ½, 1), A2^c (w = 0, ½), A2^c_odd (w = 0, ½). Predictions: none of the four closes (the orthant carries uncompleted false-theta / double-orthant structure). Sign control: A0 closed at w = 1, not at w = −1.
- **Shadow verdict rule.** "Shadow of the cone part H located (form §1.5)" iff Z passes with controls failing, P1 passes and P3 passes. "Shadow of the full C located" would additionally require A1^c and A2^c to close; otherwise reported as "not located for the orthant part".

## 3. Task (b): sharpened A2 mixed law (Category B)
Law tested (as order4b T1): A2(−1/x) ∈ colspan[A2(x), |x|^{1/2}A1(x), |x|A0(x)] (105 columns each).
Points: XSb = {h/m : 1 ≤ h, m ≤ 24, gcd = 1} (359 points; −1/x has denominator ≤ 24). Entries A0, A1, A2 from the order3c formula re-implemented in mpmath at dps = 30 (exact integer-weighted cyclotomic sums; K-integrals by mp.quad), cross-checked against float lib3c (≤ 1e−12 at all rows).
t-grid anchor (scaled with the denominator): brute-force S_{a,0} at x = 1/8 and 3/8 on t_j = 2^{−j}·0.5/(297.5(2m)²), j = 0..7, fit as order3c Map N; pass err ≤ 1e−3.
Linear algebra in mpmath (dps 30): r_B = numerical rank of B = [A2, |x|^{½}A1, |x|A0] (singular values > 1e−20 σ_max; a gap ≥ 1e8 at the cut required, else inconclusive). Unknowns = r_B; require rows ≥ 1.5·r_B, else inconclusive. Statistic ε = max over the 105 target columns of ‖T − P_B T‖/‖T‖, T = A2(−1/x).
- **Pass (law holds):** ε ≤ 1e−20. **Fail (law falsified):** ε ≥ 1e−6. Between: inconclusive.
- Controls (gating): positive target |x|²A0(−1/x) must give ε ≤ 1e−20; negative target A0(−1/x) must give ε ≥ 1e−6.

## 4. Declared open
Completion of the double-orthant (even) part and of the axis false thetas; proof that the residual S-defects are smooth; any T3/539/g_k link. The derivation §1.4 is a proof sketch; the Schwartz property of Φ is cited from Zwegers (thesis, Ch. 2), not re-proved.

## 5. Order
Hash PREREG → scripts + SHA256SUMS → controls → Z, P1–P3, C → (b) anchor, entries, rank test → RESULTS/NOTES/REPORT. Deviations go to NOTES.md with times; recorded verdicts stand.
