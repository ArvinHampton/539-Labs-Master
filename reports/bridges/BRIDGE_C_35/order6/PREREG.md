# PREREG: order6. Completing the orthant pieces of q^{-7/20}·C
Written 2026-10-24, about 2:50 PM CDT (America/Chicago), before any order6 computation. Owner: Arvin Hampton.
Parent: `../order5/` (PREREG 5c40ee5b…, RESULTS). New files only; CORE_FREEZE (H_s not redefined, no certifier code touched; order2 lib2 / A35 symbols.py read-only). Category A = proof/exact; Category B = numerical. nice, OMP_NUM_THREADS=1, ulimit -v 3000000. No push, no external sends.

## 0. Notation (as order5)
ν = α+v, v = (n,k). s1 = sgn ν1 = sgn B(c1,ν)/…, s2 = sgn ν2, s3 = sgn(ν1+21ν2); sgn 0 = 0. E(z) = erf(√π z).
Derived E-arguments (order5 §1.3, unchanged): E1 = E(√10·ν1·√y) (c1 = (−1,1), Q = −5/2), E2 = E(√35·ν2·√y) (c′ = (−7,2), Q = −35, B(c′,ν) = −35ν2, so sgn B(c′,ν) = −s2), E3 = E((ν1+21ν2)·√(2y/17)) (c2 = (−4,1), Q = −17/2).

## 1. Orthant decomposition (Category A, finite algebra)
For α with α1, α2 ∉ Z (all K2/K3/K4 representatives are checked in the script; any exception is listed), no ν lies on an axis, so in ν-signs
  orth_ν = ¼(1+s1)(1+s2) = ½·ODD + ½·EVEN, ODD = ½(s1 + s2) = ½(sgn B(c1,ν) − sgn B(c′,ν)), EVEN = ½(1 + s1 s2) (= 1 on ±orthant, 0 elsewhere).
v-signs versus ν-signs: 1[n≥0]1[k≥0] − ¼(1+sgn(n+α1))(1+sgn(k+α2)) is supported on finitely many half-lines (rays along e2 from (n0,0), along e1 from (n,k0)) and isolated points: partial (half-line) unary thetas, the "axis false-theta" type of order5 (order5 F). Denote them L_O. Full lines U_H as in order5.
So S = S_ν + L_O + U_H, with S_ν = Σ_ν [¼(1+s1)(1+s2) − ½(s1 + s3)] f q^{Q(ν)}.

## 2. Completion constants per piece (the prediction)
- **Odd pair (c1, c′)**: Zwegers. ODD → ½(E1 + E2). Shadow: ∂_τ̄ = −(i/(2√y))·½Σ_j σ_j√|Q_j| Σ_ν w_j e(Q(u_j)s_j²τ + B(ν,β))·conj(e(|Q_j|w_j²τ)) with (σ,|Q|,w,s,Q(u)) = (+1, 5/2, −ν1, ν1+ν2, 7/2) and (−1, 35, ν2/2, ν1 + 7ν2/2, 1). Weight-3/2 unary thetas: Σ n e(5n²τ/2) (n ∈ α1+Z) ⊗ θ_{7/2}, and Σ m e(35m²τ/4) (m ∈ α2+Z) ⊗ θ_{1}(ν1+7ν2/2), glued over 2 classes. Prediction O1: obeys the fixed 35-component law vector S-law at weight 1 (reproduces order5 Z_O). O2: finite-difference ∂_τ̄ matches.
- **Axis half-line pieces L_O / false thetas**: positive-definite 1-D lattices (Q(e1) = 1, Q(e2) = 7/2). Vignéras' equation in one positive variable has only the bounded solution "constant" and the unbounded erfi-type solution, so there is **no bounded weight-½ completion on H**. They are weight-½ quantum modular (false/partial thetas); their quantum "shadow" is the weight-3/2 unary theta Σ_{n∈δ+Z} n e(Q n² τ) with (Q, δ) = (1, α1 + 7α2/2) and (7/2, α1 + α2) (Eichler integral on the lower half-plane). Not completed; no S-law prediction beyond "not closed".
- **Even piece EVEN = ½(1 + s1 s2)**: NOT of Zwegers form. Reason (sketch, Category A-level argument): Zwegers' ρ are odd under ν → −ν; EVEN is even. A bounded solution p of the Vignéras equation (λ = 0) equal asymptotically to EVEN would be needed; the natural candidate p_E = ½(1 + E1E2) fails it, since D(E1E2) = E1·DE2 + E2·DE1 − (1/2π)·∇E1·A^{-1}∇E2 and the cross term is ∝ B(c1,c′) = −35 ≠ 0. Unit group check: the automorph γ = [[−1,−7],[2,13]] (from 6+√35) preserves Q, and Q(e1) = 1 ≠ Q(e2) = 7/2, so the orthant is not a union of unit-group fundamental cones (it is a strict sub-cone of cone(e1, γe1)): EVEN is a partial Hecke-type sum, not a Hecke theta. **Alternative proposed and tested:** the product completion p_E (convergent, by the positive-definiteness of 6ν1²+7ν1ν2+3.5ν2² and ν1²+7ν1ν2+21ν2²). **Prediction E1: p_E FAILS the fixed S-law** (r > 1e−4).
- **Full completed candidate**: Ŝ_ν = Σ[¼(1+E1)(1+E2) − ½(E1 + E3)] f q^Q = ½Ê + ½Ĝ_O − Ĥ. **Prediction F1: fails the S-law**, and its residual equals ½ × the residual of Ê (identity check, F2: |r(Ŝ) − ½r(Ê)|-vector difference ≤ 1e−10).

## 3. Tests
- **S-law at interior τ (Category B)**: same 120 τ, same fixed matrix M (A35 S_rows), same statistic r as order5 Z: pass ≤ 1e−10, fail > 1e−4. Objects: Ĝ_O (O1), Ê (E1), ¼(1+E1)(1+E2) = completed orthant (O3, predicted FAIL), Ŝ_ν (F1), Ĥ (reproduction, must pass: gating control), holomorphic H_ν (must fail: gating control).
- **Shadow FD (Category B)**: 4 τ × 6 companions, h = 1e−5: O2 shadow formula for Ĝ_O (pass ≤ 1e−6); and E2: the product-rule formula ∂_τ̄Ê = ½[(∂_τ̄E1)E2 + E1(∂_τ̄E2)]·(…) (calculus check, pass ≤ 1e−6), with a descriptive check that y^{1/2}·∂_τ̄Ê is not antiholomorphic (∂_τ of it nonzero) — i.e. no unary-theta shadow.
- **Radial A1/A2 (Category B)**: for Ŝ_ν (smooth Schwartz weight), Poisson predicts t·Ŝ_ν(x+it/2π) = A0 + O(t^∞): **R1: completed A1 = completed A2 = 0** at x ∈ {1, 1/2, 1/3, 2/3}, 6 companions, t_j = 2^{−j}·0.02/(2m)², j = 0..5, fit c0 + c1√t + c2t: pass |c1|,|c2| ≤ 1e−6·max(1,|c0|). Control: same fit for the uncompleted S_ν (sgn) must give |c1| > 1e−3 at ≥ 1 point. Consequence declared now: radial closure after completion is automatic for any smooth completion (modular or not), so A1/A2 "closure" cannot discriminate; the obstruction for the full series is measured only by the interior S-law (F1).
- **Shadow verdict rule**: full-series shadow "located" iff F1 passes. Otherwise: "cone + odd-orthant shadow located (four weight-3/2 unary thetas), even double-orthant and axis half-lines not completed".

## 4. Order
Hash → scripts + SHA256SUMS → controls → O1, E1, O3, F1/F2 → FD → radial R1 → RESULTS/NOTES/REPORT.
