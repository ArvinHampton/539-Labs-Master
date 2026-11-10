# order56 PREREG — RG46 (Residual-vs-Resonant lock). Hashed before any test.
Depends on STRIP.md (sha cd96c9af…3837). 105 companions (35-component law vector × 3 families; dim V = 36 only as rank reference) × 216 XS and S-images −1/x. Inputs read-only: order3/data/parts.npz (A1, S_A1, A0, S_A0), lib2, order54 rg45c.py pred() (exec up to TS=), order18 a2.py lines 1–30.
Objects: Ξ_compl = Σ_{w=1,2} pred(α,β,x,w); A1(Δ) per STRIP.md (exact Fraction θ, exact ℓ, per-line period verified); A1(P_orth) = lib2 PIECES[0] t^{−1/2} part.

## RG46a (Category A-numeric identity; residual test)
Â1 := A1 − Ξ_compl + A1(Δ) vs A1(P_orth), at x and −1/x. PASS iff max|Â1 − A1(P_orth)|/max(1,|A1|) ≤ 1e−9 over all 2×216×105.
Control (must FAIL, else verdict void): wrong strip sign A1 − Ξ_compl − A1(Δ) must deviate > 1e−4 somewhere. Second control: A1(Δ) must be nonzero (>1e−6) somewhere, else vacuous.

## RG46b (Category B; resonant test) — order4a closure criterion
Closed at w iff rank[Â1(x) | diag(|x|^w)Â1(−1/x)] = rank Â1(x), SVD rel thr 1e−9, w ∈ {½,1}. Gating: A0 rank 36 closed at w=1, wrong weight (w=−1) joint > 36. PASS iff closed at some w. Run regardless of RG46a; if RG46a fails, RG46b is reported but marked non-forced.

## Ξ match: SKIPPED by prereg. v12 §40.3: "Neither is written as an explicit series with stated coefficients"; no written target exists. No bridge claim.
## Run order: hash → script + SHA256SUMS → run → RESULTS.md. No push/send.
