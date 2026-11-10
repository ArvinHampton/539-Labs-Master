# order13 RESULTS
Prereg: PREREG.md, sha256 52a98cac…31ee, written before numerics. A scratch float probe of (S̃T)³ was run before writing it, as disclosed in the prereg header. Script hashes are in scripts/SHA256SUMS.

## 1. Route A: closed for every h (Category A)
- **W1 exact certificate.** (MT)³ = s·P with s = +35√35. Over all 3360 embeddings of Z[e(1/9800)]: off-diagonal ≤ 1.4e−13, diagonal spread ≤ 2.4e−13, |s² − 35³| ≤ 1.2e−10, all < ½. **pass** (data/w1.json). With S̃² = P (order9), this gives (S̃T)³ = P exactly.
- **Lemma W (Category A).** A nonzero vector obeying the standard T-law and the law F|S = χS̃F must have χ = 1, and is therefore P-odd.
  - Θ_E obeys the standard T-law, so Θ_E + h for any h (Weil genus mates included) can never satisfy a χ = ±i law.
  - Route A is dead. This is a sharper obstruction than order12's basis-limited FAIL, and it makes a genus-mate basis unnecessary.
  - Consistent with Milgram: a rank-2 positive-definite lattice cannot share the discriminant form, because that would need sig ≡ 0 mod 8.

## 2. P-even sector = 𝓗 of a single arc Siegel lift
| Check | Result | Category |
|---|---|---|
| W2a: P-even part of the ν-sign full weight is ½·EVEN | 0 mismatches (105 companions × 25² ν) | A (exact rational) |
| P_even(full_hol) = ½Θ_E = ½𝓗(Φ_orth) | — | identification (order8 M1, 8.7e−10); Φ_orth obeys the weight-0 law (Siegel, each z) |
| W2c: (Δ₀ − ¼)Φ_orth = (π/2)y^{3/2}[B(end) − B(start)] on the orthant arc [ĉ′, ĉ1], 15 companions, \|N\| ≤ 8, 3 y | max 1.1e−31 | **pass** (B) |
| W2d: glued factorisation at ĉ′ | relative 203.9 | **FAIL by rule** |

**W2d explained (post-hoc, descriptive).** The FAIL is a metric artefact: the target B(ĉ′) is identically 0, and its numerical value is about 1e−32. The cprime_all run normalised by Σ|terms| over all 105 companions gives |B(ĉ′)| ≤ 2.0e−31 and direct = glued to 1.2e−14. So **the ray-e1 (35m²/4) end contributes nothing.**

**Closed form of the P-even defect (Category A derivation; Category B confirmation W2c; ĉ′ vanishing is post-hoc Category B):**
  (Δ₀ − ¼)·P_even-lift = ½(Δ₀ − ¼)Φ_orth = ±(π/4)·√140·y^{3/2}·ϑ⁺_{7/2}(τ)·conj(ϑ⁻_{5/2}(τ)),
with ϑ⁺_{7/2} = Σ_{m∈α1+α2+Z} m e(7m²τ/2 + 7(b0+b1)m) and ϑ⁻_{5/2} = Σ_{u∈α1+Z} u e(5u²τ/2 + 5b0u). The overall sign comes from the measured orientation (−1,−1); the product ss′ is invariant under the endpoint flip.

## 3. Shadow verdict
- **By the preregistered rule, the hybrid verdict is NOT formally triggered**, because W2d FAILed by rule. The post-hoc evidence says the failure is an artefact.
- Substantively, subject to that caveat:
  - **P-odd sector:** ξ₁-shadow from the three distinct unary thetas (5n²/2 shared, R²/34, 35m²/4) with weight-½ partners (order5/6).
  - **P-even sector:** no ξ₁-shadow can exist under any scalar-χ weight-1 law (Lemma O + Lemma W, Category A). Its defect is a single Laplacian term, the 5n²/2 series conjugated, times the weight-3/2 Σm e(7m²τ/2), at the ray e2 only.
  - Under these caveats, the full-series shadow is located as a **hybrid**: the P-odd ξ₁-images plus the P-even Laplacian defect. **No new unary theta** appears; the 5n²/2 series is the common link between the two sectors.
- **Descriptive framing (Arvin's opinion, not a theorem):** the P-odd sector is local, hybrid mock-modular; the P-even sector is non-local, hybrid quantum modular.

## 4. Map E1 (RTA-internal, preregistered in PREREG §3)
| x | \|x\| law | signed law | Verdict |
|---|---|---|---|
| −1/5 | 1.6e−19 | 2.0 | |x| law pass, signed law FAIL as predicted |
| −3/4 | 1.5e−19 | 2.0 | |x| law pass, signed law FAIL as predicted |
| −2/3 | — | — | FAIL by the relative metric; K2_0(−1/x) ≈ 8.5e−20 is 0, so both sides vanish and the point is non-discriminating |

- So RTA's C leading profile extends Theorem 3 to x < 0 with the sign-blind |x|⁻¹ law (Category B, 2 of 3 points).
- This is not a Residual↔Resonant bridge. The **Resonant half stays OPEN**. Next measurement: the leading radial profile of a concrete T3/O_res/Π object at rational x < 0, compared against (|x|√35)⁻¹ M (|x| law) and the signed law.

## New candidate maps (statement only, not preregistered)
- **Map E2.** The P-parity eigenvalue of an RTA/Resonant object predicts its law type: P-odd means a holomorphic-type law with χ = 1 (mock); P-even means a |x|-type (quantum/Maass) law. Prediction: any Resonant object pairing with C's leading term A0 (which is P-even) has a sign-blind law.
- **Map E3.** The 5n²/2 unary series is the unique shadow shared by both sectors. Prediction: if T3/O_res carries a weight-3/2 theta, it is the 5n²/2 series at characteristic α1.

## Disclosures
- A float scratch probe of (S̃T)³ ran before the prereg and is disclosed. W1 is the preregistered exact certificate.
- Lemma W assumes h obeys the standard T-law. An h with another T-law would leave Θ_E + h with no T-law at all, so it could not be modular either.
- W2d and E1(−2/3) FAIL by rule because the targets are zero. The post-hoc runs (w2d_posthoc, cprime_all) are descriptive only.
- The v-vs-ν line corrections (U_H, L_O) are not included in P_even(full_hol). Their parity was not computed, and this is the main open gap for "the full series".
- The arc direction (ĉ′ → −ĉ1) was measured. Constants with a ± are fixed only up to that orientation.
- Arvin's local/non-local framing is used descriptively only.

## Open next step
1. Rerun W2d preregistered with an absolute/Σ|terms| metric, and prove B(ĉ′) ≡ 0 in Category A (likely via the improper automorph σ = [[1,7],[0,−1]], which fixes e1).
2. Add the parity of the U_H/L_O line corrections, to close "full series" rather than the "ν-sign full_hol".
