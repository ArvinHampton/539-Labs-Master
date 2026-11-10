# WRITE NL — Self-prove G8 repair — 2026-10-27
Written: 2026-10-27 ~15:25 CDT (America/Chicago) · Author: NL · tip_touched NO · Kerr BLOCKED, untouched · No RECS · No new data
Inputs: WRITE_NL_SELF_PROVE_FIVE_INPUTS_INVENTS_2026-10-27.md 8e9b8dae7268b3fa57182389a454ae049e3a7dc9e1f9830b31d8850b86130339 (Item 5); WRITE_NL_GAP_X1_G8_OWNER_WRITE_ABSENT_PACK_2026-10-27.md f23f9a830c205dd75e8d5c69430a2861b640164fff73f16ea32da4519269e8c9 (§2). tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 MATCH before.

## §0 Corpus definition of D (checked)
D appears only in f23f9a83… H2: Q,P ∈ even lattice Λ_s (Q²,P² ∈ 2ℤ, Q·P ∈ ℤ), D(Q,P) = Q²P² − (Q·P)² (Gram determinant). Not in the tip (grep: no Q·P / D(Q,P) in tip). H2 itself is invented pending mathematical proof.

## §1 (a) Corrected hypothesis H2* — invented pending mathematical proof
**H2*:** H2 and Q·P ∈ 2ℤ. Equivalent form, under H2: D ≡ 0 (mod 4).
**Theorem 1.** Under H2: n = D/4 ∈ ℤ ⇔ Q·P ∈ 2ℤ ⇔ D ≡ 0 (mod 4).
*Proof.* Q² = 2a, P² = 2b ⇒ Q²P² = 4ab, so D ≡ −(Q·P)² (mod 4). If Q·P = 2m, D = 4(ab − m²) ∈ 4ℤ. If Q·P is odd, (Q·P)² ≡ 1 (mod 8), so D ≡ 3 (mod 4) and D/4 ∉ ℤ. ∎ (Sharp: Q=(1,2), P=(1,3) in U gives Q·P=5, D=−1.)
**Supplement H+ (needed by §2 step 2):** D > 0. Neither H2 nor H2* gives it. In U, Q=(1,1), P=(1,−1) gives Q²=2, P²=−2, Q·P=0, so H2* holds but D=−4 and n=−1, and √n is not real. H+ is invented pending mathematical proof.

## §2 (b) SL₂(ℤ) invariance of H2* (and H+)
(Q,P) ↦ (Q',P') = (aQ+bP, cQ+dP) with ad−bc=1.
- Evenness: Q'² = a²Q² + 2ab Q·P + b²P² ∈ 2ℤ; likewise P'². Q'·P' ∈ ℤ.
- Parity: Q'·P' = ac Q² + (ad+bc) Q·P + bd P². ac Q², bd P² ∈ 2ℤ, and ad+bc = 1+2bc is odd, so Q'·P' ≡ Q·P (mod 2). ∎
- Cross-check: G' = MGMᵀ ⇒ D' = D, so D ≡ 0 (mod 4) and D > 0 are invariant too. ∎
Machine check: all Q,P ∈ {−3..3}² in U, with T, S and (2,3;1,2). 0 failures for Theorem 1 and parity/D invariance.

## §3 (c) Re-run of f23f9a83… §2 under H1, H2*, H3 (+H+ where stated)
| Step | Claim | Status | Reason |
|---|---|---|---|
| 1 | n = D/4 ∈ ℤ, invariant | **PROVED** (given H2*) | Theorem 1 gives integrality. §2 gives invariance. The original step under H2 alone is FALSE (counterexample). |
| 2 | β_s√n = 4π√Δ_s·√(D/4) = 2π√(Δ_s D) | **PARTIAL** | The algebra is valid for D ≥ 0. It needs H+ (otherwise D=−4 is a counterexample, with √n not real). β_s = 4π√Δ_s rests on H1 (R-c conditional). Δ_s branch {1, 1/s} NF. |
| 3 | L_ĝs invariant | **PROVED** (given H1, H2*, H3, H+) | D' = D and Δ_s depends only on s. |
| G8 overall | conditional statement | **PARTIAL** | Proved conditionally on H1, H2*, H3, H+. H1/H2*/H3/H+ themselves NF from Written premises. Index identification n ↔ ĝ_s NF. G8 Owner-cite stays ABSENT/OPEN. |

## §4 (d) Corpus support
Not supported. The tip has no charge lattice, no Q·P and no D(Q,P). The only corpus occurrences of Q·P ∈ 2ℤ are NL/PR1 working files. PR1 (PR1-FINDINGS-INVENT_THEN_PROVE_COOK_CHI2_MIXED_GAPX1, sha 1aa43909…) labels it "[INVENTED sublattice condition]". **H2* and H+: invented pending mathematical proof.** All G8 labels are KEPT.

## §5 Non-claims
No numeric β_s, D or n values are asserted as data. Not Cat A. No Kerr / Bekenstein π√D reading (BLOCKED). No RECS. tip READ-ONLY.

## Audit request to Professor Proof (accumulates under PP pause)
Please audit and return PASS/FAIL per item: (1) Theorem 1, both directions incl. mod-8 step; (2) parity invariance via ad+bc odd; (3) the H+ counterexample Q=(1,1), P=(1,−1) in U; (4) the step table §3 (1 PROVED, 2 PARTIAL, 3 PROVED-conditional, G8 PARTIAL); (5) the §4 finding that H2*/H+ are invented. This request queues while the PP pause holds. It goes to the Auditor Keeper after audit.
