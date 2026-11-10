# CANDIDATE_MAPS: maps between the crypto mathematics and RNT / RTA / g_k / g_s / Bridge C

Frozen with PREREG.md before any test. Each map: domain, codomain, formula, prediction, falsifier. No map has a free parameter chosen after data (all integers come from the sources: k from {7, 11, 17, 67, 68}, 539, the block sizes 3·68 + 5·67).

Notation: T3 as in INVENTORY §1; Sq_k = squares mod k; blk : Z/539 → {0..7}, the block of ρ when [0,539) is cut into consecutive blocks of sizes 68,68,68,67,67,67,67,67 (`crypto/RPP_spec_v1/RESIDUAL_PREDICATE_C.md` l.38; the reduction ρ = u mod 539 is the A2 stand-in, not stated by any source, `RPP_spec_v2_drafts/PI_AMENDMENT_DRAFT.md` l.211).

## M1. Orbit-residue map
- Domain: seeds n ∈ ℕ; codomain [0,1]. Formula: Φ_k(n) = (1/σ(n))·#{0 ≤ i < σ(n) : T3^i(n) mod k ∈ Sq_k}.
- Prediction (new): mean Φ_k > |Sq_k|/k + 0.02 for k = 7, 11, 17, 67, i.e. T3 orbits "see" the squares that carry OccFilt_k(∞).
- Falsifier: PREREG H1.

## M2. Fibre sizes → g_k index
- Domain {67, 68} (block sizes); codomain: zero counts of g_k. Formula: b ↦ Z_b = #{allowed d ≤ 20000 : g_b(d) = 0}.
- Prediction (new): g_67 and g_68 are extreme in zero count among g_60..g_76.
- Falsifier: PREREG H2. Prior honest label: numerology (block sizes are forced by 539 and m = 8, see INVENTORY §5, so there is no mechanism tying them to g_k).

## M3. T3 on fibre blocks
- Domain Z/1617 (n mod 3·539); codomain {0..7}²; formula n ↦ (blk(n mod 539), blk(T3(n) mod 539)).
- Prediction (new): T3 preserves fibre blocks preferentially: D ≥ 1.5·D₀.
- Falsifier: PREREG H3.

## M4. 539 = 7²·11, 18 + 521, 68·7 + 67 vs s = 7 Bridge C / level of ρ_s
- No formula with a testable consequence exists: Bridge C's level 9800 = 2³·5²·7² and dim V = 36 at s = 7 are not functions of 539, and 68·7 + 67 = 543 ≠ 539 (so "68·7+67" is not an identity of the packaging; the true identity is 3·68 + 5·67 = 539). Status: analogy only, not tested. Dropped by the rule "no map without a prediction".

## M5. T3 as an operation of RTA
- Not definable: RTA has no algebraic operation or axiom (A18 §1). T3 is the only map in RTA (manuscript Def 2.1), so "T3 vs RTA axioms" is the identity map on the same definition. Status: not a bridge (same object, no new prediction). Not tested.

## M6. 3-adic measure of T3 vs OccFilt_k
- Domain Z_3 with Haar measure μ. Formula: the extension T3(n) = (n − r)/3 ∘ branch, i.e. n ↦ n/3, (4n+2)/3, (2n−1)/3... on classes r = 0,1,2 (the integer branches 3k ↦ k, 3k+1 ↦ 4k+2, 3k+2 ↦ 2k+1 written in k = (n−r)/3, which extend continuously to Z_3).
- Prediction: none possible for squares mod k with 3 ∤ k, because n mod k is not continuous on Z_3. What can be proved instead is recorded in RESULTS §Proofs (μ is T3-invariant and T3 is measure-isomorphic to the full one-sided 3-shift). This is a Category A fact about the crypto map alone; it is not a bridge.
