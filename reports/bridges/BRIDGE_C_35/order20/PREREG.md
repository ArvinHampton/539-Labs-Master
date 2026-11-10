# PREREG order20 — corrected RG6′; the Bernoulli-weighted S-law; Map RG7
Written 2026-10-24 (America/Chicago) BEFORE any order20 numerics. CORE_FREEZE. Inputs read-only: order19/data/rg5_arrays.npz (C11, C2a, C2b at XS and −1/x), order4b/data/A2.npz (A0).
Notation: for a companion (α,β) and rational x, N = N(x) is the period used for C2b in order19 (lcm of the phase periods along (1,0),(0,1)); f_r the phase on class r of α+Z² mod N; ρ2 = α2 + j. G_{α,β}(x) = N^{−2} Σ_r f_r (Gauss mean; independent of the period chosen). k := 35^{−1/2}.

## 1. RG6′ corrected (Category B)
X := C2b − (1/6)·Σ_r f_r, with the SAME N and the SAME classes r as C2b (so (1/6)Σ_r f_r = (N²/6)·G_{α,β}). Law: X(−1/x) = κ·x·kM X(x), κ one complex scalar fitted over all 216 points.
Absolute metric primary: ‖R‖_F with R the residual at the fitted κ. "No law" (RG6′ PASS) if ‖R‖_F ≥ 1e−3·‖X(−1/x)‖_F and ≥ 1e−4 absolute; RG6′ FAIL (law holds) if ‖R‖_F ≤ 1e−9; else inconclusive. Prediction: RG6′ PASS (no law).

## 2. Bernoulli-weighted S-law (Category A statement; numerical check Category B)
**Proposition L_B.** For every (α,β) ∈ Q² and x ∈ Q^×, with λ_k = A^{−1}(0, k/N)ᵀ and DFT weights c_k = N^{−1} Σ_{j<N} B2((α2+j)/N) e(−k(α2+j)/N) (equivalently c_k = Σ_{n≡k (N), n≠0} e((n−k)α2/N)/(2π²n²), the aliased 1/k² Fourier weights of B2):
  (i) C2b(x) = N² Σ_{k mod N} c_k G_{α,β+λ_k}(x);
  (ii) C2b(−1/x) = N′² Σ_{k mod N′} c′_k · e(B(α,β+λ′_k)) /(|x|√35) · Σ_{p∈A^{−1}Z²/Z²} G_{β+λ′_k+p, −α}(x),
with N′, c′_k, λ′_k formed at −1/x.
Proof. (i): DFT inversion on the coset α2+Z mod N gives B2(ρ2/N) = Σ_k c_k e(kρ2/N), and e(kν2/N) = e(B(ν,λ_k)) since Aλ_k = (0,k/N). Insert into Σ_r f_r B2(ρ2/N); the twisted sum over the N² classes is N² G_{α,β+λ_k}. The period N still works for β+λ_k because B(u, λ_k) ∈ N^{−1}Z. (ii): apply (i) at −1/x and the paper's S-law (Theorem STlaw, valid for all α,β ∈ Q²) to each G_{α,β+λ′_k}(−1/x). ∎
So the Bernoulli-weighted sums DO obey an exact S-law, but into Gauss means with characteristics β+λ′_k+p outside the 105 companions. This is why no fixed-M law holds.
**Check B1 (Category B):** evaluate both sides of (ii) by direct Gauss means (exact integer phases) at x ∈ {1, 1/2, 2, 1/3, 3, 2/3, 3/2} for companions j ∈ {0,17,35,52,70,87,104}. Absolute metric: max |LHS − RHS|. PASS ≤ 1e−9; FAIL ≥ 1e−6. Also check (i) at x (same metric). LHS of (ii) is taken from order19 SC[2]. Prediction: PASS.

## 3. Map RG7 (residual-geometric, NEW)
"The S-image of the Bernoulli-weighted sum leaves the span of the 35-component law vector": rank[G(x) | x·C2b(−1/x)] > rank G(x) = 36 over the 216 points (G(x) = A0(x)/I, SVD threshold 1e−9 relative), and likewise for C11 and C2a. RG7 PASS if all three joint ranks exceed 36; FAIL if any equals 36. Prediction: PASS.
No Resonant-side object is used or invented; E1–E3 OPEN; no bridge claim.
nice, OMP_NUM_THREADS=1, <3 GB; no push/sends; new files only.
