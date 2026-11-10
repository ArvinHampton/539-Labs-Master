# order43 RESULTS: exact k = 0 law and exact miss split
PREREG sha256 66dd47276a7ec06b01a7ad2f3ff7e14f8bf4710c053d83c2a95e3e78d223bdeb (hashed before numerics). 12 points × 105 companions; κ̂ and M fixed.
## LD0: D0(−1/x) = (x√35)^{−1}·M_b·D0(x), with M_b = diag(B2(α2))·M·diag(B2(α2))^{−1}: PASS
Max error 2.4e−16 (threshold 1e−12); min|B2(α2)| = 1/150 > 0. Category A: an immediate corollary of the G S-law (Theorem STlaw), as noted in PREREG.
## RG40: exact split R = (a) + (b): PASS (algebraic consolidation, as disclosed)
Max ‖R − R_pred‖/‖R‖ = 4.8e−15.
| x | r(C2b) | ‖R‖ | ‖(a)‖ k = 0 law mismatch | ‖(b)‖ k ≠ 0 remainder | ‖R‖/(‖a‖+‖b‖) |
|---|---|---|---|---|---|
| 1 | 0.1408 | 0.256 | 0.205 | 0.154 | 0.714 |
| 2 | 0.0848 | 0.308 | 1.226 | 1.223 | 0.126 |
| 3 | 0.0639 | 0.348 | 1.874 | 1.874 | 0.093 |
| 4 | 0.0523 | 0.380 | 2.503 | 2.501 | 0.076 |
| 5 | 0.0446 | 0.405 | 3.131 | 3.121 | 0.065 |
| 6 | 0.0393 | 0.428 | 3.756 | 3.745 | 0.057 |
| 7 | 0.0353 | 0.450 | 4.384 | 4.369 | 0.051 |
| 8 | 0.0323 | 0.470 | 5.011 | 5.002 | 0.047 |
| 1/2 | 0.0847 | 0.154 | 0.613 | 0.611 | 0.126 |
| 1/3 | 0.0638 | 0.116 | 0.625 | 0.625 | 0.093 |
| 2/3 | 0.0370 | 0.135 | 0.342 | 0.360 | 0.191 |
| 3/2 | 0.0370 | 0.202 | 0.514 | 0.540 | 0.191 |
## Reading
- The miss of the C2b near-law is the exact difference between an explicit k = 0 law mismatch (a) and the k ≠ 0 L_B remainder (b). They are nearly equal and opposite, with cancellation to 5–13% for x ≥ 2.
- Post-hoc observation (not a test): the cancellation ratio is the same at x and 1/x (2 vs ½: 0.12593; 3 vs ⅓: 0.09298; ⅔ vs 3/2: 0.19144). The norms scale by x between the pair.
## Category, v11
A: LD0 (minor corollary of Theorem STlaw). B: the split numbers. v11: **no**. By the PREREG criterion LD0 alone does not warrant it; a non-trivial statement about the remainder is needed.
order44: not run. The preregistered rule says no law for the remainder can be written without fitting. Ξ: not identified. E1–E3 OPEN.
