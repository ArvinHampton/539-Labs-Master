# order26 RESULTS
PREREG sha256 d0a31ded81d93c64f75496b3c729672a6d1281ace33d16e0e2189c726736a755 (hashed before numerics).
Between-cone B = cone((7,−1),(1,0)), unimodular; the only unimodular piece between γ⁻¹K and K (the unions have det 2 and det 7).
| test | value | verdict (preregistered rule) |
|---|---|---|
| C1 corner(K)=CO | 0.0 | PASS |
| C2 Γ_γ·CO = Cor_{γ⁻¹K} | 1.6e−14 | PASS |
| C3 Y_− = −½D | 7.9e−15 | PASS |
| C4 RG15 abs vs 52.0306 (≤1e−9) | 1.48e−5 | **FAIL by rule** (see note) |
| **I1** D = ±Cor_B + t·vtx | min max-error 72.48 (s=−1); vertex term has no effect; LS fit relative residual 0.597 (a=−1.287) | **FAIL** |
| **RG17** R(Y_−) carried by P_−R(Cor_B) | β = 1.000, r = 1.1e−14, non-vacuity 1.00 | **PASS by rule, but trivial** (see below) |
| RG17′ Cor_B against the weight-1 law | abs 54.406, rel 0.0586 | FAIL |
C4 note: the threshold was set against a 4-decimal rounded constant; that was a preregistration error. Post hoc, against the stored order25 value 52.030585237…, the difference is at floating-point level. The rule verdict stands as FAIL.
## Post-hoc finding (after verdicts were recorded)
Cor_B = Cor_K numerically: 7.6e−15 at x, 2.0e−14 at −1/x. B = hK with h = [[1,7],[0,−1]] = −σ, an improper automorph of A (checked). So RG17 reduces to P_−R(Cor_K) = R(Y_−), which is order25's split itself. It carries no new information, and the non-vacuity check (a norm ratio) did not catch this; that is a lesson for future preregistrations.
A naive exact pair-transport check of Γ_h (same convention as Γ_γ) gives identity on only 3 of 105 entries, so the equality Cor_{hK} = Cor_K is **not** yet explained by an exact argument (a convention or sign symmetry of the corner is suspected). It is Category B only.
## Answers
- RG17: PASS by the letter of the rule, but trivial (between-cone corner = K corner).
- Between-cone identity Cor_K − Cor_{γ⁻¹K} = ±corner(B) (+ vertex terms): **does not hold** (error 72.5).
- Category A: none new. Category B: I1 FAIL, Cor_B = Cor_K to 2e−14, RG17′ FAIL.
- v10: no. Ξ: not identified. E1–E3 OPEN.
