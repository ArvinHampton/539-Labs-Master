# order5 REPORT (descriptive notes; verdicts as in RESULTS.md)
PREREG sha256 5c40ee5b…fe49 (unchanged since hashing at about 2:10 PM CDT). Script hashes: scripts/SHA256SUMS. Process deviations are in NOTES.md. All verdicts below are the preregistered ones.

## Category A (exact or derived; proof sketches flagged)
- **Cone structure (finite algebra).** w(v) = ½(sgn B(c1,v) − sgn B(c2,v)) with c1 = (−1,1), c2 = (−4,1); Q(c1) = −5/2, Q(c2) = −17/2, B(c1,c2) = −20. The wall directions c1^⊥ = (0,1) (Q = 7/2) and c2^⊥ = (21,−1) (Q = 595/2) are the order3 labels. The orthant's odd part is the Zwegers pair (c1, c′ = (−7,2)), with Q(c′) = −35 and c′^⊥ = (1,0) (Q = 1), plus the axis false thetas F. The double orthant (the even part) is not of Zwegers type.
- **v-signs versus ν-signs (finite algebra).** H_ν − H = U_H and ρ_O(ν)-series − ½(sgn n + sgn k)-series = U_O. Both are finite sums of full unary theta lines (PREREG §1.2).
- **Completion constants (derived; Zwegers' theorem cited).** The completion is
  Ĥ = Σ_ν ½[E(√10·ν1·√y) + E((ν1+21ν2)·√(2y/17))]·e(Q(ν)τ + B(ν,β)),
  and for the orthant pair the term E((ν1+21ν2)·√(2y/17)) is replaced by E(√35·ν2·√y). Here E(z) = erf(√π z), and at the radial point y = t/(2π).
- **Shadow (calculus).** The shadow is
  ∂_τ̄Ĥ = −(i/(2√y)) Σ_j σ_j √|Q(c_j)| Σ_ν w_j e(Q(u_j)s_j²τ + B(ν,β)) · conj(e(|Q(c_j)|w_j²τ)).
  Its weight-3/2 parts are the unary thetas Σ n e(5n²τ/2) with n ∈ α1+Z (c1, unimodular split, paired with θ_{7/2}) and Σ R e(R²τ/34) with R ∈ α1+21α2+Z (c2, glued over 17 classes with θ_{35/34}, i.e. the wall Q = 595/2).
- **Radial consequences, proof sketch only (PREREG §1.4).** Ĥ has no t^{−1/2} and no t^0 term. A2(H) ≡ 0. A2(S_odd) = A2(F). The E-argument constants do not enter A1 or A2. **These are listed as proof sketches, not as completed proofs. Their status rests on the Category B checks P1 and P2 below.**

## Category B (numerical)
### Task (a)
| test | statistic | threshold | verdict |
|---|---|---|---|
| Z controls: holomorphic H_ν; E-args × 1.25 | r = 0.300; 0.109 (Ĥ), 0.112 (Ĝ_O) | must be > 1e−4 | **controls fail, as required** |
| **Z: Ĥ obeys the fixed 35-component law vector S-law, weight 1**, Ĥ(−1/τ) = (τ/√35)·M·Ĥ(τ), 120 interior τ | r = 6.0e−16 (truncation 1.1e−16) | ≤ 1e−10 | **pass** |
| Z: Ĝ_O (orthant odd pair) | r = 6.1e−16 | ≤ 1e−10 | **pass** |
| P3: finite-difference ∂_τ̄Ĥ vs the shadow formula (24 cases) | max rel. err 4.5e−9 | ≤ 1e−6 | **pass** |
| P1: max \|A2(H)\| over 105 × 216 × {x, −1/x} (mp, dps 30) | 1.1e−30 (\|A2\| up to 18.4) | ≤ 1e−11 | **pass** |
| P2: max \|A2(S_odd) − A2(F)\| | 6.8e−15 | ≤ 1e−11 | **pass** |
| check: A2 of the full lines U_H, U_O | 4.4e−30 | (should be 0) | consistent |
| sign control (A0, XS216) | rank 36, closed at w=1; joint 72 at w=−1; fixed-matrix residual 7.7e−16 | gating | **passed** |

Completed-law tests on XS216 (SVD threshold 1e−9). The fixed-matrix residual is not defined for the odd combinations (NOTES item 4).
| object | rank | joint (w) | fixed-matrix residual | closed |
|---|---|---|---|---|
| A1 (reference) | 105 | 210 (½), 210 (1) | 1.82, 4.79 | no |
| A1^c = A1(orth) + A1(U_H) | 105 | 210 (½), 210 (1) | 1.53, 4.27 | **no** |
| A1^c_odd = A1(−U_O + 2U_H + F) | 103 | 206 (½), 206 (1) | – | **no** |
| A2^c = A2(orth) (= A2, by P1) | 73 | 146 (0), 146 (½) | 0.69, 0.82 | **no** |
| A2^c_odd = A2(F) | 99 | 190 (0), 190 (½) | – | **no** |

All four "not closed" predictions hold.

**Shadow verdict (preregistered rule):**
- **The shadow of the cone part H is located (Category B confirmation of the Category A derivation).** Z passes with both controls failing, P1 passes, and P3 passes. It is the pair of weight-3/2 unary thetas of §1.5, attached to the walls Q = 7/2 and 595/2.
- **The shadow of the full C is not located.** The completed A1^c and A2^c do not satisfy the fixed S-law. The remaining obstruction sits in the orthant piece: the axis false thetas F (Q = 1, 7/2) and the uncompleted double-orthant part.

### Task (b): sharpened A2 mixed law
- Points XSb: 359.
- B = [A2, |x|^{½}A1, |x|A0]: numerical rank 214 at dps 30, with a gap of 1.4e27 at the cut (last pivot 7.6e−3, first rejected 5.4e−30). Rows/unknowns = 1.68, which meets the ≥ 1.5 requirement.
- Positive control |x|²A0(−1/x): ε = 2.4e−31 (≤ 1e−20, passes). Negative control A0(−1/x): ε ≥ 0.53 (passes). **Valid.**
- **ε = max residual of A2(−1/x) = 0.389 (min 0.276) ≥ 1e−6 → mixed law FALSIFIED (Category B), decisively.**
- Cross-check of the mp entries against float lib3c: see the bcross line below. t-grid anchors (brute force, t_j = 2^{−j}·0.5/(297.5(2m)²)): x = 1/8 gives err 1.5e−7 and x = 3/8 gives err 2.5e−7. **Pass, 2/2.**
- bcross: max relative difference between the mp entries and float lib3c over all 359 × 105 × 6 entries = 3.7e−13 (≤ 1e−12, **pass**).

## Status summary
- **Category A, unchanged:** the bridge through order t^0. A1 = D + R + W[1] + W[7/2] + W[595/2].
- **Category A, new:** the identities of PREREG §1.1–1.2 and the shadow formula §1.5. Ĥ's fixed S-law, by citation of Zwegers' theorem.
- **Proof sketches, not upgraded to Category A:** A2(H) ≡ 0 and A2(S_odd) = A2(F).
- **Category B:** everything numerical above.
