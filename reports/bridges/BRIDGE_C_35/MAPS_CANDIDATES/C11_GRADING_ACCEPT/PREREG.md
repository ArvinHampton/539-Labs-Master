# PREREG: C11_GRADING_ACCEPT: re-test of Map-C11 under the accepted grading g = (−1)^τ
Written 2026-10-24 at about 9:15 PM CDT. Owner: Arvin Hampton.
**Acceptance:** in his message of 2026-10-24, Arvin accepted both g = (−1)^τ (the ±1 grading on O_res) and P_res (u ≡ 3 mod 9, the path predicate). Bridge claims still need a non-vacuous PASS.

## Source statement (verbatim, BATCH2/PREREG.md, Map-C11)
"Prediction: under a written ±1 grading of O_res elements, every one of the 8 fibre blocks has signed sum 0 for the 68-blocks, with an odd defect ±1 for the 67-blocks." (Motivation: P-even A₁ = 0, modular → residual.)

## Objects (written; checked pre-test in scripts/explore.py: the two τ sources agree, and O is exactly 21+9j)
- O_res = {x_j = 21 + 9j : j = 0..538}.
- Fibre β♯(x_j) = j mod 8. Blocks: fibres 0, 1, 2 have 68 elements; fibres 3..7 have 67 (539 = 8·67 + 3).
- τ(x) = ⌊x/21⌋ for x < 420, else 20 + ⌊(x − 420)/20⌋ (RPP_spec_v1/PREREG.md; identical to architecture_A4plus_probe.tower_of).
- g(x_j) = (−1)^{τ(x_j)} (accepted).

## Prediction C11 (exact)
S_r := Σ_{j ≡ r (8)} g(x_j). C11 holds iff S_0 = S_1 = S_2 = 0 and S_r ∈ {−1, +1} for r = 3..7.
Verdict: PASS iff all 8 conditions hold. FAIL otherwise. The computation is exact, so the verdict is **Category A** either way.
Non-vacuity: parity alone forces S_r to be even on the 68-blocks and odd on the 67-blocks, so only the magnitudes (0 and ±1) carry content. The test is non-vacuous iff g is non-constant (checked).

## Disclosure (pre-test)
The DISCOVER_GRADING_PATH exploration (logs/explore.log there) already printed tower-parity fibre sums [10, 12, 12, −13, −13, −11, −13, 13] for this τ formula, before g was accepted. So this test is **not blind**. It is the formal, hashed adjudication of C11 under the accepted g. The expected outcome is FAIL, and it is recorded here before the run.
Secondary (descriptive, no verdict): the total Σ g, and the sums over the 18-prefix / 521-body index split.
