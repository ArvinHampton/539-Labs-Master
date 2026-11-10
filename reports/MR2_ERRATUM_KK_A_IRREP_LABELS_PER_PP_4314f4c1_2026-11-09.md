# MR2 ERRATUM — KK Group A irrep labels (ed0e5bd6), per PP audit 4314f4c1
Date: 2026-11-09, ~20:10 CST. Additive; ed0e5bd6 and all earlier files unchanged. Scope OW 8b26c786 (Group A = Aut⁺(Bolza) × wall ℤ₂, a scope choice, not a result). B not adopted. Full spectrum OPEN; junction UNSOLVED; count gap unchanged. Tip 7cddb188 MATCH, untouched.

- **Audit read:** FINDINGS_PP_AUDIT_MR2_KK_A_IRREP_LABELS_ed0e5bd6_2026-11-09_1955.md, sha256 4314f4c1d77de9375b6a77dbfbb9378187ba9b6546759a49a8a37f7203606af0, **MATCHES** its sidecar.
- **Tiny computation (frozen before run):** `MR2_ERRATUM_KK_A_IRREP_LABELS_PER_PP_4314f4c1_2026-11-09.py` sha256 e76ce0a06a6e36b4af174f1619111a1c53e1d4e7f2bc1b08df83ead6749d771c; `….log` sha256 b8ec6fa4037b912dd0297ca823e52a5c7eefb3a4bb9c00f8c83d827eeec5df4f (runtime < 1 s). It sha-checks ff800541 (the irrep-labels .py) and reuses its exact multiplication table and irreps; integer/permutation search only, characters compared to 1e-6.

All 8 fixes are ACCEPTED; each was confirmed independently by the log. No disagreements on substance; one grading interpretation is flagged under fix 6.

## Fix 1. Valid proof of claim 3 (labels intrinsic). ACCEPT. PROVED
Retract the ed0e5bd6 reason ("det is the unique nontrivial 1-dim character, so the label is invariant"): it only shows σ preserves the pair {3, 3⊗det}, not that it fixes 3.
**Proof (resonant algebra of the check: characters restricted to the order-8 elements).** Let σ ∈ Aut(GL(2,3)). (i) σ preserves element orders, so it maps the set of order-8 elements onto itself. (ii) χ₃ ≡ +1 and χ₃⊗det ≡ −1 on *every* order-8 element (log [A1]: both order-8 classes, sizes 6, 6). (iii) χ∘σ is an irreducible character of the same degree, and GL(2,3) has exactly two 3-dim irreps. Since χ₃∘σ ≡ +1 on order-8 elements, χ₃∘σ = χ₃; likewise for 3⊗sgn. ∎
Computation (log [A1]): |Aut(GL(2,3))| = 48, Inn 24, **|Out| = 2**; 24 of 48 automorphisms swap the two order-8 classes; both 3-dim characters are fixed by all 48. Agrees with PP B1.

## Fix 2. Dependence on the holomorphic subgroup. ACCEPT. PROVED
Log [A2] (exhaustive search over images of the Coxeter triple, with full homomorphism and bijection check): |Aut(Isom)| = 192, |Z| = 2, |Inn| = 48, **|Out(Isom)| = 4**. Induced permutations of the 13 irreps:
| automorphisms | preserve Aut⁺ | permutation |
|---|---|---|
| 48 | yes | id |
| 48 | yes | (I11 I12) |
| 48 | no | (I2 I4)(I7 I10) |
| 48 | no | (I2 I4)(I7 I10)(I11 I12) |

I10 restricts to 3, I7 to 3⊗sgn. So an automorphism of Isom that does not preserve the holomorphic subgroup swaps 3 ↔ 3⊗sgn. **The headline label is defined only after fixing Aut⁺ = the orientation-preserving (holomorphic) subgroup.** In ed0e5bd6 this is fixed by drawing the Coxeter triple from the antiholomorphic involutions (D J_c = −J_c D on H¹; `inv_anti`), so Aut⁺ is the true holomorphic subgroup and the headline stands. Agrees with PP B2.

## Fix 3. Computation behind claim 6. ACCEPT. PROVED (computed, not a remark)
Same table: the Aut⁺-preserving automorphisms (96 of 192) induce exactly {id, (I11 I12)}. So the I11/I12 tags depend on the chosen triple, and the Aut⁺ labels (both 4 J-faithful) do not.

## Fix 4. Naming. ACCEPT. PROVED
Drop "standard". The usual standard rep of S₄ (permutation rep minus trivial) has χ(4-cycle) = −1; pulled back to GL(2,3) that is MR2's **3⊗sgn**. MR2's **3** is the cube-rotation rep of S₄ (χ(4-cycle) = +1). Definition by character stands: **3** := the 3-dim irrep of GL(2,3) with character +1 on order-8 elements; **3⊗sgn** := character −1 there.

## Fix 5. Labels stay COND. ACCEPT. CONDITIONAL
The headline "λ₁ = 3.8389 eigenspace is Aut⁺ irrep 3" stays **CONDITIONAL**, on (U) Bolza uniformization and on float FEM. Conforming FEM gives only upper bounds. Upgrading needs a rigorous *lower* bound above 3.8389 on the I7/I8 (3⊗sgn) sectors (e.g. Lehmann–Goerisch or Temple). PP's independent Klein-model P2 FEM gives λ₁ = 3.83888725875 in the I10 sector, with the 3⊗sgn sectors starting at 15.0489. That is a second independent discretisation; it does not change the grade.

## Fix 6. Earlier tallies restated under PP's ruling. ACCEPT
Ruling applied: a claim that states its premise is graded as an implication (PROVED if the implication is proved). "PROVED with a COND premise counts as COND" applies only to premises used but not stated. Kept separate, per OW 3f160803: a premise that is a citation, or float numerics, still makes the claim COND. **Flag for PP:** I read the ruling as not overriding that rule; confirm.
- **b0c6e848 (9 rows), as filed:** PROVED 4 (rows 1, 2, 3, 5) · CONDITIONAL 2 (row 6: stated premise (U), but it also used the float k = 3 root of ac257bf7 §3a; row 7: Strohmaier–Uski multiplicity citation) · REFUTED 1 (row 4) · OPEN 2 (rows 8, 9) = 9. **Live, after 69a10b84 fix 4 replaced the root by the closed form:** PROVED 5 (row 6 becomes the proved implication (U) ⇒ locus = {trivial}) · COND 1 · REF 1 · OPEN 2 = 9.
- **00b1a96a (8 rows), as filed:** PROVED 7 (rows 1–6; row 7 as the implication (a) ∧ (b) ⇒ …) · CONDITIONAL 1 (row 8: premise (c) is a float root) = 8. The retracted lemma stays 1 REFUTED, separately. **Live, after 69a10b84 fixes 4 and 5:** PROVED 8.
- **69a10b84 (9 rows):** PROVED 7 (rows 1, 3, 4, 5, 6; row 2 as the implication from the kernel premise; row 8 headline as the implication (U) ⇒ invariant SU(2)_R locus = {trivial}) · CONDITIONAL 1 (row 7: citation) · OPEN 1 (row 9) · REFUTED 0 = 9. Its row 9 (3 vs 3⊗sgn; levels 2–5) is superseded by ed0e5bd6 plus this erratum: now CONDITIONAL.
- **ed0e5bd6 under the same ruling:** unchanged at PROVED 3 · CONDITIONAL 3 · OPEN 1 · REFUTED 0. Claims 1 and 2 rest on float FEM besides (U), so they stay COND. Claims 3 and 6 are now PROVED by MR2's own computation (fixes 1 and 3).

## Fix 7. [F4] erratum for 69a10b84 (PP 985d404d residual 2). ACCEPT. PROVED
The 69a10b84 log printed `+-` followed by a signed value, which gave garbled `+--` for k = 5, 6, 7. The defective lines were:
```
     k=5: cos psi = +--0.441885 -> psi = 1.113098 rad (real)
     k=6: cos psi = +--0.816497 -> psi = 0.615480 rad (real)
     k=7: cos psi = +--1.066804 -> no real psi (|cos psi|>1 would need a complex angle): no SO(3) rep
```
The corrected lines (log [F4']) read:
```
     k=5: cos psi = ±0.441885 -> psi = 1.113098 rad (real)
     k=6: cos psi = ±0.816497 -> psi = 0.615480 rad (real)
     k=7: cos psi = ±1.066804 -> no real psi (|cos psi| > 1): no SO(3) rep
```
k = 4 now prints as `cos psi = 0`. The values and conclusions are unchanged.

## Fix 8. Weyl wording. ACCEPT
The 24-vs-25.5 Weyl comparison in ed0e5bd6 is a **heuristic** count check, not evidence of completeness. Completeness below 25.5 rests on each sector's FEM having computed eigenvalues past 25.5, which it did (still float, so COND).

## Still OPEN
Levels above 25.5; rigorous lower bounds (I7/I8 sectors first); the charged S⁴ towers (deferred, about 3–4 h).

## Tally (this erratum, 9 rows)
| # | item | label |
|---|---|---|
| 1 | claim 3 valid proof; Out(GL(2,3)) = ℤ₂ fixes both 3-dim characters | PROVED |
| 2 | Out(Isom) order 4; non-Aut⁺-preserving automorphisms swap I7 ↔ I10 (3⊗sgn ↔ 3); antiholomorphic triple fixes the label | PROVED |
| 3 | claim 6 computed: Aut⁺-preserving automorphisms induce {id, (I11 I12)} | PROVED |
| 4 | naming: drop "standard"; usual standard = 3⊗sgn | PROVED |
| 5 | headline λ₁ = 3 (and table) stays COND pending lower bounds | CONDITIONAL |
| 6 | tallies restated (bookkeeping verified on disk) | PROVED |
| 7 | [F4] sign lines corrected | PROVED |
| 8 | Weyl comparison is a heuristic | PROVED (wording) |
| 9 | levels above 25.5, rigorous bounds, charged towers | OPEN |

**PROVED 7 · CONDITIONAL 1 · OPEN 1 · REFUTED 0 = 9.**

Rules: new dated files only; .py frozen before its log and this md; no existing file edited; tip untouched; no CERT, no Gemini, nothing external; no messages sent.
