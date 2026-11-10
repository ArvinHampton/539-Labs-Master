# order51 RESULTS: R1 tail bound and R2 H7 completion data
PREREG sha256 12898051d9283d562357b88225aaeac9a3081c8fea76d31f7c872703c7092393 (hashed before numerics). Runtime ~3 s.
## R1: derived and tested
Bound: ‖R‖ ≤ B2 = ‖(a)‖ + ‖N′²Σ_{k≠0}|c′_k|‖ + x‖N²Σ_{k≠0}|c_k|‖ ≤ B1 (crude tail (N²−1)/6). This is rigorous from L_B, |G| ≤ 1 and the unitarity of kM.
- R1a validity: PASS, ‖R‖ ≤ B2 ≤ B1 at all 12 points.
- **R1b non-vacuity: FAIL, as predicted.** B2/‖S‖ ranges from 3.37 (x = 1) to 29.8 (x = 8), while ‖R‖/‖S‖ is 0.03–0.14.
Where it stalls: the triangle inequality discards the (a) ≈ −(b) cancellation that is the smallness. The tail term grows like x·N²/6 while ‖S‖ grows like x. No bound that treats the k ≠ 0 terms in absolute value can explain the near-law. Explaining it needs a phase-aware evaluation of Σ_{k≠0}c_k G_{β+λ_k}, which is the order46 obstruction.
## R2: derived data, one preregistered check FAILs as written
| | exact |
|---|---|
| c1 = A^{−1}(1,0)ᵀ (form ν1, ray (0,1)) | (−1/5, 1/5), Q(c1) = −1/10 |
| c2 = A^{−1}(1,21)ᵀ (form ν1+21ν2, ray (21,−1)) | (4, −1), Q(c2) = −17/2 |
| B(c1,c2) | **+4** (PREREG expected −4: hand-arithmetic sign error in c1) |
Both walls are negative vectors, and the completion constants are √(1/−Q(c)) = √10 and √(2/17). But with the orientation fixed in PREREG, B(c1,c2) > 0, so the Zwegers same-component hypothesis FAILS as preregistered. With −c1 (form −ν1) it would hold (B = −4). Whether H7's sign function uses ν1 or −ν1 with c2 is fixed by H7's definition (the sign combination in the K± terms). That was not derived here, so I make no claim.
Stalled: forming A1 − Ξ_compl requires the order-t^{−1/2} coefficient of the erf-completion terms at rational x. That is not derivable from written sources here. No S-law test was run.
## Status
Category A: R1 inequality (valid but vacuous); exact c1, c2, Q values. Category B: none. v13: no. Ξ: not identified. E1–E3 OPEN.
Open next: (1) read off the sign orientation of the K± walls in H7 from the Part II definition and settle the Zwegers hypothesis; (2) derive the t^{−1/2} asymptotic of Σ(E(s_c√y) − sgn s_c)·phase at rational x, then preregister the A1 − Ξ_compl S-law test; (3) for smallness, a phase-aware (not absolute) treatment of the k ≠ 0 L_B terms.
