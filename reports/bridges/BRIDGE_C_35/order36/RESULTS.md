# order36 RESULTS: RG33 (leakage as a span projection)
PREREG sha256 3b7fc650d363d1d0c904276483a25879c47eb7cff2dff91086c9134d80146f9e (hashed before numerics).
Span = column span of the companion Gauss means G = A0/I (ambient rank 36 = dim V; the 35-component law vector is a separate notion).
## Grid handling (as preregistered)
- P7 (order20 grid) is a trivial control: rank G(P7) = 7, so every column lies in the span. Leftover is 6.4e−16 as expected; non-discriminating.
- Primary grid G48: the 48 lowest-complexity points of XS. rank G(G48) = 36, as required. Results are reported globally and per point.
## Controls
D0 (L_B split reconstructs C2b(−1/x)): 1.9e−14 on G48, PASS.
## RG33: FAIL (Category B)
| quantity (G48) | value |
|---|---|
| r_meas (κ̂ = 0.99971 − 0.0043i) | 0.01899 |
| r_pred = ‖(I−P_G)S_out‖/‖S‖, no fit | 0.3590 |
| relative difference (PASS ≤ 1e−6) | 17.9 |
| ‖(I−P_G)S‖/‖S‖ | 0.3678 |
| ‖(I−P_G)X‖/‖X‖ | 0.3677 |
| ‖(I−P_G)S_in‖/‖S‖ | 0.074 |
| Spearman(per-point r, per-point leftover) | 0.18 |
Per-point r: median 0.0187, range 0.0093 (x = 5/8) to 0.139 (x = 1). The worst points are 1, 2, ½, 3, the smallest denominators; per-point leftover median 0.46. Prediction FAIL (blind): correct.
## Reading
- S and the law direction X have the same out-of-span fraction (0.3678 vs 0.3677). Both live largely outside the span of the plain companion Gauss means, and their outside parts are aligned. That is why the near-law survives while the projection leftover is large.
- The plain-Gauss-mean column span is therefore the wrong reference space for the Bernoulli sum C2b. Leakage "outside the companion Gauss span" does not measure the law miss.
- The near-law quality is strongly grid-dependent: r = 0.0585 on P7, 0.019 on G48 and 0.00305 on the full grid. It improves as larger-denominator points are added, and the miss concentrates at x ∈ {1, 2, ½, 3}.
## Category
A: none new. v11: no. Ξ: not identified. E1–E3 OPEN.
