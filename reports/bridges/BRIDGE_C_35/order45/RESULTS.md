# order45 RESULTS: RG43 (x ↔ 1/x invariance at κ = 1)
PREREG sha256 325adfd013b59c5dd9d96bbaca293177f073951966e2c456d68521cce9496a8b (hashed before numerics).
## RG43: PASS (Category B as tested; Category A candidate)
| pair | c(x) | c(1/x) | rel diff | ‖R(1/x)‖·x/‖R(x)‖ |
|---|---|---|---|---|
| 5/7 ↔ 7/5 | 0.29703878 | 0.29703878 | 3.2e−15 | 1.000000000000 |
| 4 ↔ 1/4 | 0.07617288 | 0.07617288 | 9.1e−16 | 1.000000000000 |
| 9/2 ↔ 2/9 | 0.09411413 | 0.09411413 | 4.7e−15 | 1.000000000000 |
| 5 ↔ 1/5 | 0.06496284 | 0.06496284 | 8.5e−16 | 1.000000000000 |
| 7/3 ↔ 3/7 | 0.18754287 | 0.18754287 | 9.8e−15 | 1.000000000000 |
| 2 ↔ 1/2 | 0.12614279 | 0.12614279 | 6.6e−16 | 1.000000000000 |
| 3 ↔ 1/3 | 0.09316884 | 0.09316884 | 4.3e−15 | 1.000000000000 |
| 2/3 ↔ 3/2 | 0.19197618 | 0.19197618 | 3.3e−15 | 1.000000000000 |
Max 9.8e−15 (PASS ≤ 1e−10). Prediction PASS: correct. The order44 ~1e−5 asymmetry came from κ̂ ≠ 1.
## Post-hoc mechanism (after the verdict; disclosed): scripts/o45_posthoc.py
Candidate identity, with κ = 1 and Π the monomial matrix of (α,β) ↦ (α,−β) from the reduction rules:
**R(1/x) = −x^{−1}·conj(Π·(35^{−1/2}M)^{−1}·R(x))**, which gives ‖R(1/x)‖ = ‖R(x)‖/x.
Proof sketch:
(i) F(−x) = conj(Π·F(x)) for F = C2b. Exact: the complex conjugate of the summand e(−xQ(ν) + B(ν,β)) is e(xQ(ν) − B(ν,β)), and the B2 weights are real.
(ii) conj(kM)·Π = Π·(kM)^{−1}, with k = 35^{−1/2}.
(iii) kM is unitary.
Then R(1/x) = conj(ΠF(x)) − x^{−1}kM·conj(ΠF(−1/x)) = −x^{−1}·conj(Π(kM)^{−1}[F(−1/x) − x·kM·F(x)]).
Numerical checks: (i) 1.1e−15, (ii) 6.0e−16, (iii) 5.0e−16. The identity itself holds to 1.4e−13 (relative, at x = 2, 5/7, 9/2).
Status: (i) is proved. (ii) and (iii) are finite matrix identities verified only in floating point, not exactly. The symmetry is therefore a Category A candidate pending exact certification of (ii) and (iii) in Z[ζ_9800].
## v11
No. The proof is incomplete until (ii) and (iii) are certified exactly. Ξ: not identified. E1–E3 OPEN.
