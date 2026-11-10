# order44 PREREG: RG41, RG42 (written and hashed before numerics)
Fixed: κ̂, M (order37); b_l = B2(α2_l); M_b = diag(b)·M·diag(b)^{−1}; D0 = b·G; Rem = C2b − D0.
(a) = (x√35)^{−1}M_b D0(x) − κ̂x35^{−1/2}M D0(x); (b) = Rem(−1/x) − κ̂x35^{−1/2}M Rem(x); R = (a) + (b) (order43).
## RG41: the k ≠ 0 remainder from data at x only (no fit)
By L_B (ii), C2b(−1/x) = N′²Σ_k c′_k e(B(α,β+λ′_k))(x√35)^{−1}Σ_p G_{β+λ′_k+p,−α}(x). This is the S-law of the shifted characteristics β+λ′_k, evaluated by Gauss means AT x.
With LD0 for D0(−1/x), the prediction is
(b)_pred = [L_B(ii)-RHS(x)] − (x√35)^{−1}M_b D0(x) − κ̂x35^{−1/2}M Rem(x),
which uses only quantities at x.
PASS iff max ‖(b)_pred − (b)‖/‖(b)‖ ≤ 1e−10. FAIL iff ≥ 1e−6. Points: x ∈ {2, 3, 4, 1/2, 2/3, 3/2}.
Disclosure: given L_B (Category A, v7) and LD0 (order43), RG41 is a consistency identity. It expresses (b) entirely at x but is not a new theorem.
Explanation of (b) ≈ −(a), to be tested as stated: (a) + (b) = C2b(−1/x) − κ̂x35^{−1/2}M·C2b(x). So the near-cancellation is exactly the statement that C2b itself nearly obeys the law; no independent mechanism exists in this split.
Descriptive (reported, no verdict): q(x) = ‖C2b(x)‖/‖D0(x)‖ (internal cancellation between k = 0 and k ≠ 0 at x).
## RG42 (blind): x ↔ 1/x invariance of c(x) = ‖R‖/(‖a‖+‖b‖)
New pairs: (5/7, 7/5), (4, 1/4), (9/2, 2/9), (5, 1/5), (7/3, 3/7).
PASS iff all 5 pairs satisfy |c(x) − c(1/x)|/c(x) ≤ 1e−8. FAIL iff any pair ≥ 1e−4. Else inconclusive.
Prediction: PASS (the order43 pairs agreed to ≥ 6 digits).
Category: B unless proved.
## Follow-up rule (fixed)
If RG42 PASS: order45 = an attempted proof of the x ↔ 1/x invariance (written argument plus exact check of the implied identity). If FAIL: no order45.
v11 only for a non-trivial proved statement.
Naming: RG* only, no labels L1–L7; "36" only as dim V. MAPS_CANDIDATES untouched; no Resonant objects; no new Bernoulli objects; no bridge claim.
