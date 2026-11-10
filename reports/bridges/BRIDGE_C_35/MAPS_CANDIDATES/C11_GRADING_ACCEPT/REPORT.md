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
# RESULTS: C11_GRADING_ACCEPT
PREREG.md sha256 eeb29cc9304cdc95a47103c4285d45f67cd654862c50c3688d4eb56a0d71c61b, hashed before scripts/test.py ran. Grading g = (−1)^τ, accepted by Arvin on 2026-10-24 (message accepting g and P_res).

| fibre r | block size | predicted S_r | measured S_r | holds? |
|---|---|---|---|---|
| 0 | 68 | 0 | 10 | no |
| 1 | 68 | 0 | 12 | no |
| 2 | 68 | 0 | 12 | no |
| 3 | 67 | ±1 | −13 | no |
| 4 | 67 | ±1 | −13 | no |
| 5 | 67 | ±1 | −11 | no |
| 6 | 67 | ±1 | −13 | no |
| 7 | 67 | ±1 | 13 | no |

g is non-constant (268 values of +1, 271 of −1), so the test is non-vacuous. Total Σg = −3; prefix-18 sum −2, body-521 sum −1 (descriptive).

**Verdict: C11 FAIL, Category A** (exact finite computation; the outcome was disclosed as expected in the PREREG, i.e. not blind). **Bridge: NO.** Map-C11 (P-even A₁ = 0 → fibre-block balance) is refuted under the accepted grading.

Mechanism (post-hoc, descriptive): towers span 21 or 20 integers, i.e. about 2.2–2.3 consecutive j. Over j, g is a square wave of period ≈ 4.5. Sampling it at stride 8 (one fibre) gives a slow beat, not cancellation, so the |S_r| ≈ 10–13 are coherent sums, not ±1 defects. All 8 conditions fail, not just a few.
# NOTES: C11_GRADING_ACCEPT
- Acceptance cited: Arvin's message of 2026-10-24 accepting g = (−1)^τ and P_res. Before that, both were Option-3 / candidate objects (DISCOVER_GRADING_PATH, DISCOVER_MARKOV_288, DISCOVER_HIT_SIGN).
- Order: explore.py (only τ-source agreement and the O_res check; hashed in data/explore.sha256), then PREREG hashed, then test.py run once. Under 1 s; nice, OMP=1.
- C11 sources read: BATCH2/PREREG.md (verbatim statement), BATCH2–7 status rows, DISCOVER_GRADING_PATH/NOTES.md, RPP_spec_v1/PREREG.md (τ definition). (The "C11" in heavy-daily/Cross-Review is an unrelated rev3 cusp item.)
- Not blind: the sums were already in DISCOVER_GRADING_PATH's exploration. This is disclosed in the PREREG.

## Implications
- **C11:** closed, as FAIL (Category A) under the accepted g. A different grading would be a new candidate needing new acceptance; none is proposed here.
- **C6 / C10 (OPEN): the constraint P_res places on a 539-step Π.** If Π is a T3 orbit word of 539 steps, P_res imposes only consequences that every T3 orbit already satisfies:
  - (a) no two consecutive hits (D1, Category A);
  - (b) no hit in fibres β̂ ∈ {3,7} after the initial pure-division prefix (Lemma V, Category A);
  - (c) asymptotic hit rate 1/9, fibre law ρ = (1,8,3,0,7,8,5,0)/32, and the lag-1 kernel DM2 with independence from lag 2 on (DM1–DM3; lifted chain, numerically confirmed).

  So P_res is a **necessary-condition filter that does not select a Π**: it narrows nothing among T3 orbits. Pinning down a Π for C6/C10 still needs a written seed or word, or an added positional rule (e.g. required hit positions), and that would be invention. **No Π word was constructed.** C10's prediction (4 maximal branch-type segments) cannot be tested without one.
- **E1–E3 (OPEN):** these also need the T3 q-series / α1, which is still unwritten (HUNT_ALPHA1). Unaffected.
- Next step: Arvin chooses either (i) a written/accepted seed rule that fixes Π (for example, Π = the T3 orbit of a specified seed), after which C6/C10 can be preregistered, or (ii) to retire C6/C10/C11 as modular→residual maps refuted or untestable. E1–E3 wait on α1 either way.
- No L1–L7 names. order*/ and the v12 paper were untouched. CORE_FREEZE: this folder only. No push, no send.
