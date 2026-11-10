# PREREG: order7. Three completion candidates for the even double-orthant piece
Written 2026-10-24, about 3:00 PM CDT (America/Chicago), before any order7 computation. Owner: Arvin Hampton.
Parents: `../order5/`, `../order6/` (read-only; order6 lib6.py imported read-only). New files only. CORE_FREEZE. Category A = proof/exact; Category B = numerical. nice, OMP_NUM_THREADS=1, ulimit -v 3000000. No push, no external sends.
Notation as order6: E1 = E(√10ν1√y), E2 = E(√35ν2√y), EVEN = ½(1+s1s2), Ê = Σ ½(1+E1E2) f q^Q. M = fixed 35-component law vector S-matrix (A35 S_rows, 105×105). P = the involution G_{α,β} ↦ G_{−α,−β} on the 105-family (with its phases, via A35 `reduce`).

## 0. Parity lemma (Category A once the finite check passes)
Claim: M² = 35·P exactly. Consequence: if F obeys F(−1/τ) = (τ/√35)·M·F(τ) (fixed weight-1 law), applying it twice gives F = −(M²/35)F = −PF, so F is P-odd. **No nonzero P-even vector can obey the fixed weight-1 S-law.** At weight 0 (F(−1/τ) = ε(1/√35)MF) or weight 2, S² gives F = PF: P-even is allowed. Every ½(1+…) even weight on ν is P-even (ν → −ν), so the even piece can only couple to even weight.
Check: M² − 35P = 0 exactly in Z[e(1/9800)] (computed with exact exponent arithmetic; float check |·| ≤ 1e−9 also reported).

## 1. Candidate 1: non-Vignéras weight-1 object
p_λ = ½(1+E1E2) + λ·G, G = exp(−π(ℓ1²+ℓ2²)) with ℓ1 = √10ν1√y, ℓ2 = √35ν2√y (the Vignéras defect of E1E2 is −(2κ0/π)G with κ0 = B(c1,c′)/√(Q(c1)Q(c′)) = −√14). F_λ = Σ p_λ f q^Q (convergent: Q + 5ν1² + 17.5ν2² positive definite).
Prediction (from §0): FAIL for every λ. Test: λ* = least-squares minimiser of the fixed weight-1 residual over 120 τ (one real/complex parameter); r(λ*) > 1e−4 ⇒ "fails as predicted". Failure mode predicted: residual of the P-even part never below ‖F‖-scale, and r(λ) ≥ r_min > 1e−4.

## 2. Candidate 2: weight-0 Siegel / Hecke–Maass object for Q(√35)
Siegel theta at a negative line z: Θ_z(τ) = y^{1/2} Σ_ν e(Q(ν)x + B(ν,β))·exp(−2πy(Q(ν) − 2Q_z(ν))), Q_z(ν) = B(ν,z)²/(4Q(z)) (< 0). Unit γ = [[−1,−7],[2,13]] (from 6+√35, γᵀAγ = A), γc1 = (−6,11).
Hecke/Maass candidates: Φ_k = ∫_{c1}^{γc1} e^{2πik·μ(z)/μ_tot} Θ_z dμ(z), k = 0 (Hecke/Eisenstein-type) and k = 1 (Grössencharacter mode r = π/log(6+√35)), μ = hyperbolic arclength on the negative cone (Gauss–Legendre, 24 nodes, box |n|,|k| ≤ 30).
Predicted S-action (Category A by Siegel's theorem for each Θ_z): Φ_k(−1/τ) = ε·(1/√35)·M·Φ_k(τ), weight 0, ε ∈ {+1,−1} fixed by the test (both allowed by S²; report which). Pass ≤ 1e−10, fail > 1e−4. Parity check: PΦ_k = Φ_k (pass ≤ 1e−10).
Coupling to the even piece (predicted FAIL): Ê(τ) ∈ colspan over τ of [y^{−1/2}Φ_0, y^{−1/2}Φ_1, y^{1/2}Φ_0, y^{1/2}Φ_1] (420 columns) on 660 τ rows: relative residual ≥ 1e−4 ⇒ "no coupling of this form"; ≤ 1e−10 ⇒ coupling found.

## 3. Candidate 3: enlarged law space W (named "enlarged law space W_420", separate from the 35-component law vector)
W(τ) = span of the 420 columns [Ê, Ĥ, Ĝ_O, Θ_E] (Θ_E = holomorphic ν-sign EVEN series, convergent). Dimension bound: 420. Rows: 660 interior τ (≥ 1.5 × 420), same sampling rule as order5 with a larger count (seed 7).
Law tested: target T(τ) = τ^{−w}·X(−1/τ) ∈ colspan W(τ), for X ∈ {Ê, Θ_E, Ŝ_ν (full completed)} and w ∈ {0, 1}, with an arbitrary (unfixed) mixing matrix. Statistic ε = max over target columns of relative residual. Pass ≤ 1e−10; fail ≥ 1e−4. Positive control: X = Ĥ, w = 1 must pass. Rank of W reported; if rank W ≥ 0.9·660 the test is inconclusive.
Prediction: FAIL for Ê, Θ_E, Ŝ_ν at both weights.

## 4. Shadow FD
Candidate 1 at λ*: ∂_τ̄F_λ by product rule vs finite differences (calculus check, pass ≤ 1e−6). Candidate 2: weight-0 objects have no ξ-shadow in the weight-3/2 sense; not tested.

## 5. Verdict rule for the full series
"Full-series shadow located" iff some candidate yields a completion of the even piece that, added to Ĥ and Ĝ_O, obeys a law (fixed or in W_420). Otherwise: blocked, with the parity lemma as the stated reason.
