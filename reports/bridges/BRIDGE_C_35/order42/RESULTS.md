# order42 RESULTS: RG39, L_B at integer x = n
PREREG sha256 503bfca79012e4723cfc02a9adaf1a49c925039bbe1dcea41ca08a80068412c3 (hashed before numerics). Helpers verbatim from order20/35; κ̂ and M fixed.
Control: r_1(C2b) = 0.14075 equals the order37 per-point value at x = 1.
## E0: k = 0 term of L_B (i) = B2(α2)·G_{α,β}(x): PASS (exact to rounding)
max|N²c_0 − B2(α2)| = 6.3e−15; max term error 1.1e−15. Proof: the B2 distribution relation (written in PREREG). Category A, but it is a standard identity applied to L_B. It is too small for v11 on its own.
## RG39: FAIL (Category B)
| n | r(C2b) | r(D0 = k = 0 part) | r(k ≠ 0 remainder) | ‖R(C2b)‖ | ‖R(D0)‖ | rel diff |
|---|---|---|---|---|---|---|
| 1 | 0.1408 | 0.327 | 0.090 | 0.256 | 0.205 | 0.20 |
| 2 | 0.0848 | 3.91 | 0.337 | 0.308 | 1.23 | 2.97 |
| 3 | 0.0639 | 8.98 | 0.344 | 0.348 | 1.87 | 4.38 |
| 4 | 0.0523 | 16.0 | 0.344 | 0.380 | 2.50 | 5.58 |
| 5 | 0.0446 | 22.9 | 0.343 | 0.405 | 3.13 | 6.73 |
| 6 | 0.0393 | 36.0 | 0.343 | 0.428 | 3.76 | 7.77 |
| 7 | 0.0353 | 41.7 | 0.343 | 0.450 | 4.38 | 8.75 |
| 8 | 0.0323 | 64.0 | 0.344 | 0.470 | 5.01 | 9.67 |
Max relative difference 9.67 (PASS ≤ 1e−6). Prediction FAIL (blind): correct.
## Reading
- The k = 0 part B2(α2)·G alone is far off the w = −1 law, with r growing roughly like n². This is consistent with G obeying the weight-one law (factor 1/x) while the C2b law uses the factor x.
- The k ≠ 0 aliasing remainder alone misses by a stable ≈ 0.34 for n ≥ 2.
- Their residuals cancel to leave the small near-law miss of C2b. The near-law is a cancellation between the k = 0 and k ≠ 0 L_B parts, not a property of either.
## Category
A: E0 (minor, standard). B: RG39. v11: no. Ξ: not identified. E1–E3 OPEN.
