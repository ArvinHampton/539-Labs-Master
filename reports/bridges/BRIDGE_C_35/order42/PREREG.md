# order42 PREREG: RG39, L_B at integer x = n (written and hashed before numerics)
Sources: order20 Prop. L_B (i) C2b(x) = N²Σ_{k mod N} c_k G_{α,β+λ_k}(x), with c_k the DFT weights of B2 (order20 ck, lam, Gmean, copied verbatim via order35), and order19 comps() for direct C2b.
Points: x = n ∈ {1, 2, 3, 4, 5, 6, 7, 8}, at x and −1/x, for all 105 companions.
## E0: exact k = 0 identity (Category A candidate; proof fixed now)
The B2 distribution relation Σ_{j<N} B2((a+j)/N) = N^{−1}B2(a) gives c_0 = N^{−2}B2(α2). Hence the k = 0 term of L_B (i) is N²c_0·G_{α,β}(x) = B2(α2)·G_{α,β}(x), independent of N.
Test: max|N²c_0 − B2(α2)| ≤ 1e−12 over all (x, j) used, and max|k0-term − B2(α2)G_{α,β}(x)| ≤ 1e−10. PASS/FAIL accordingly.
## RG39 (predictive; blind)
Hypothesis H39: at integer x = n, the near-law miss comes entirely from the k = 0 part.
With D0(x) = B2(α2)·G(x) (per companion), define R_n(Y) = Y(−1/n) − κ̂·n·35^{−1/2}·M·Y(n), with κ̂ fixed from order37 and M fixed.
Prediction under H39: ‖R_n(C2b)‖ = ‖R_n(D0)‖ exactly, per point. PASS iff max_n |‖R_n(C2b)‖ − ‖R_n(D0)‖|/‖R_n(C2b)‖ ≤ 1e−6. FAIL iff ≥ 1e−2.
Also reported: r_n(C2b), r_n(D0) and r_n(C2b − D0) (the k ≠ 0 remainder), and the remainder share of ‖R_n(C2b)‖.
Prediction (blind): FAIL. G obeys the weight-one S-law (factor 1/x), and B2(α2) is not M-invariant, so D0 should not reproduce the w = −1 miss.
Category: E0 is A if exact (it is the standard distribution relation applied to L_B; I judge it too small for v11 unless RG39 passes). RG39 is Category B.
Naming: RG* only, no labels L1–L7. MAPS_CANDIDATES untouched; no Resonant objects; no new Bernoulli objects (D0 is the k = 0 term of the written L_B); no bridge claim.
