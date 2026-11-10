# PREREG: order8. Linking the P-even weight-1 even piece to weight-0 Siegel objects
Written 2026-10-24, about 3:35 PM CDT (America/Chicago), before any order8 computation. Owner: Arvin Hampton.
Parents: order5–order7 (read-only; order6 lib6, order5 lib5mp, order2 lib2, A35 symbols imported read-only; order7 data/W_E.npz, W_ThE.npz read-only). New files only. CORE_FREEZE. Category A = proof/exact; B = numerical. nice, OMP_NUM_THREADS=1, ulimit -v 3000000. No push, no external sends. No interior float span test is used as evidence.

## 0. Objects
Θ_E,j(τ) = Σ_{ν∈α+Z²} EVEN(ν) e(Q(ν)τ + B(ν,β)), EVEN = ½(1+s1s2) (ν-signs; ½ on axes). Holomorphic, P-even, convergent (±orthant ⊂ positive cone).
Unit-normalised negative lines ĉ1 = c1/√(5/2), ĉ′ = c′/√35; B(ĉ1,ĉ′) = −35/√87.5, L := arccosh(−B(ĉ1,ĉ′)/2) = arccosh(7/(2√3.5)) (= hyperbolic angle of the orthant between e1 and e2; prediction: L = ½·log(6+√35)). Geodesic ẑ(μ) = [sinh(L−μ)ĉ1 + sinh(μ)ĉ′]/sinh L, μ ∈ [0,L].
**Orthant Siegel object** Φ_orth(τ) = ∫_0^L Θ_{ẑ(μ)}(τ) dμ, Θ_z(τ) = y^{1/2} Σ_ν e(Q(ν)x + B(ν,β)) exp(−2πy(Q(ν) + B(ν,ẑ)²/2)). Weight 0, P-even, obeys the fixed weight-0 law Φ(−1/τ) = (1/√35)·M·Φ(τ) (order7; Siegel).

## 1. Map M1 (fixed now): renormalised holomorphic projection 𝓗 = D^{1/2}∘(y→∞ projection)
For N > 0 let a_N(y) be the e(Nx)-Fourier coefficient of Φ_orth. Define 𝓗(Φ)(τ) := Σ_N [lim_{y→∞} 2√N·e^{2πNy}·a_N(y)] q^N.
**Claim M1:** Θ_E = 𝓗(Φ_orth) coefficient by coefficient, for all 105 companions.
Derivation (Category A, Laplace sketch): a_N(y) = Σ_{Q(ν)=N} e(B(ν,β))·y^{1/2}e^{−2πNy}∫_0^L e^{−πyB(ν,ẑ)²}dμ, and B(ν,ẑ)² = 4N sinh²(μ−μ_ν) with μ_ν the position of ν^⊥ on the geodesic; Laplace gives weight 1 if μ_ν ∈ (0,L) (⇔ ν ∈ ±orth interior), ½ on the boundary (ν on an axis), 0 outside.
Test (Category B, mpmath dps 25): per-ν weights w_ν(y) = 2√(Ny)∫_0^L e^{−πyB(ν,ẑ(μ))²}dμ at y = 1e4 and 2e4, linear extrapolation in 1/y; c_Φ(N) := Σ w_ν·e(B(ν,β)); compare with exact c_E(N) for all N ≤ 8 (all ν in box |n|,|k| ≤ 60 with 0 < Q ≤ 8). Pass: max |c_Φ − c_E| ≤ 1e−7 over all N, j. Fail: > 1e−4.
**Meaning if M1 holds:** the even piece is the image of a modular weight-0 object under a fixed but non-equivariant map 𝓗 (mixed, non-modular link). It is NOT a ξ-shadow statement.

## 2. Map M2: radial-limit prediction at rational points
Poisson (Category A): Θ_z is a positive-definite Gaussian sum, so t^{1/2}Φ_orth(x+it/2π) = (2π)^{−1/2}(2π/√35)·L·mean_N(f) + O(t^∞). Θ_E: t·Θ_E = A0_E + A1_E t^{1/2} + A2_E t + O(t^{3/2}).
**Predictions:** (M2a) A0_E(x) = √(2/π)·lim t^{1/2}Φ_orth (equivalently A0_E = mean f·2L/√35); (M2b) Φ_orth has no t^0 and t^{1/2} radial terms; (M2c) A1_E, A2_E are NOT determined by Φ_orth: they equal the order2/order3c formula applied to the two shifted orthant pieces (ν1>0,ν2>0 and ν1<0,ν2<0 as v-cones with offsets), i.e. pure boundary (edge Q = 1, 7/2 and corner) terms.
Test: brute force Θ_E at x ∈ {1, 1/2, 1/3}, 4 companions with α1, α2 ∉ Z (first four in K2 order), t_j = 2^{−j}·0.02/(2m)², j = 0..5, fit {t^{-1}, t^{-1/2}, 1, t^{1/2}, t}; pass |measured − predicted| ≤ 1e−5·max(1,|pred|) for A0, A1, A2. Φ_orth measured at x = 1, 1/2 (2 companions, t = 2e−3, 1e−3, 5e−4, 24 GL nodes): t^{1/2}Φ constant to 1e−8 and equal to the M2a constant (pass ≤ 1e−8 relative).

## 3. Map M3: character-twisted S-law (changes the effective parity; level/T-orbit candidate)
SL2(Z) characters χ_r with χ_r(S)² = χ_r(−I) = −1 for odd r (the η^{2r} characters). Under ρ = ρ_L ⊗ χ_r the weight-1 law reads F(−1/τ) = χ(S)·(τ/√35)·M·F(τ), χ(S) = ±i, and S² then FORCES F = PF (P-even) — the natural P-altering candidate (Category A algebra, same as order7 §0).
Test (fixed-matrix residual with one free scalar, discriminating as in order5 Z): on order7's 660 τ (data/W_E.npz, W_ThE.npz), c* = argmin ‖W − c(τ/√35)MV‖; pass iff r(c*) ≤ 1e−10 and |c* ∓ i| ≤ 1e−8; fail if r(c*) > 1e−4. Objects: Θ_E (holomorphic) and Ê (order6 product completion). Prediction: both FAIL (Θ_E is a partial Hecke-type sum, Ê is not Vignéras). Control: Ĥ with c free must give c* = 1, r ≤ 1e−10.

## 4. Order of maps and verdict rule
M1 → M2 → M3. If a map fails, record Category B and continue. Full-series shadow "located (ξ-sense)" iff M3 passes for some completed even object. If M1 and M2 hold but M3 fails: "even piece identified as 𝓗(Φ_orth) (non-modular link); ξ-shadow of the full series not located".
