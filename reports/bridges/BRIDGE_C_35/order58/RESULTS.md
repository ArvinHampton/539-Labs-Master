# AMENDMENT (2026-10-24, America/Chicago): Auditor blocker, directed by the Physicist
The verdicts below replace the earlier RG47a "PASS on Category A identity branch" and the RG48 "Category A no-go" wording. Those earlier verdicts are superseded. PREREG.md and PREREG.sha256 are unchanged. The data, scripts and logs are unchanged. Note: data/rg47a.json still contains `"RG47a_PASS": true`. The script set that flag using the non-preregistered scale max(|A1|,1), so it is void. The formal verdict is the one in this file.

# order58 RESULTS (local modular only; RG* labels; CORE_FREEZE; new files in order58/ only)
PREREG.md sha 75ebf419…050a, hashed before any test. Scripts: scripts/rg47a.py, rg48.py, rg48b.py. Data: data/rg47a.json, rg47a_raw.npy, rg48.json, rg48b.json. Logs: logs/.

## RG47a: FAIL under the preregistered relative criterion
- PREREG: PASS iff max |A1−Σpieces|/max(|A1|,1e−300) ≤ 1e−6 over the sample. The alternative branch, an exact Cat A identity cited from order6 text, is not met, because order6 §1 does not write the term-by-term split.
- Verified strict statistic, from data/rg47a.json `resid_rel_strict`: **0.17462226357609986 (≈0.1746) ≫ 1e−6 → FAIL.**
- Deviations from PREREG: scripts/rg47a.py scaled by max(|A1|,1), which is not preregistered. The filter |A1| ≥ 1e−9 was added post hoc and is also not in PREREG. Neither can produce a PASS.
- Post-hoc Cat B disclosures (explicitly NOT a PASS):
  - max absolute residual 2.3e−16;
  - residual scaled by max(1,|A1|): 2.3e−16;
  - relative residual where |A1| ≥ 1e−9: 3.9e−14;
  - the strict failure is concentrated in 548 entries with |A1| < 1e−9, where the axis pieces cancel to about 1e−11. Attributing this to float cancellation is a post-hoc interpretation, not a verdict.
- Split used, for the record: the lib2 PIECES[0] t^{-1/2} formula, read as written.
  - axis Q=1: −(√π/2)·w2/√p;
  - axis Q=7/2: −(√π/2)·w1/√r;
  - corner/EVEN: −mf·(l1·Ja + l2·Jb).
  - Reading each sawtooth term as a half-line piece is my interpretation. No new identity is claimed.
- Wrong-sign control (disclosure): relative residual 2.0, above 1e−4.
- Dominance table (disclosure):
  - axis Q=1 is largest in 83.5% of entries, median |piece|/|A1| = 1.0;
  - axis Q=7/2 is largest in 11.9%, median ratio 0.27;
  - corner/EVEN is largest in 7.0%, median ratio about 1e−15, and exactly 0 in 52% of entries.
- Cat B observation, not a verdict: the axis Q=1 piece dominates A1(P_orth).

## RG47b: SKIP (obstruction)
order6 RESULTS writes the shadows Σ n e(n²τ) and Σ n e(7n²τ/2) only as an "argument sketch". It gives no operational match statistic: no Eichler-integral normalisation, no constants, no rational-point evaluation. Per PREREG, the test is skipped rather than run against an invented statistic.

## RG48: NOT EXECUTED AS PREREGISTERED (no Cat A verdict)
- PREREG asked whether the P-even target lies in the span of the χ=±i Weil eigenvectors over the FULL basis. That span test was not run.
- What did run, in rg48.py and rg48b.py, was a Milgram / definite genus-mate enumeration. It is classed here as post-PREREG Cat B exploration, or as material for a separate order. It is **not** a Cat A no-go under RG48's Weil χ=±i criterion.
- Cat B disclosure of what the enumeration found:
  - the companion Q = ν1² + 7ν1ν2 + 7ν2²/2 is odd;
  - its even rescaling A(2) = [[4,14],[14,14]] has det −140, signature (1,1), and Milgram sum 1.000;
  - all 30 reduced positive-definite even binary Grams of det 140 have Milgram sum i;
  - none matches the q-value multiset of A(2) or −A(2).
- rg48.py ran on the odd Gram A (|Gauss| = 0.169) and is invalid; rg48b.py supersedes it.
- P̂_orth is not adopted.

## Next brief (order59)
1. Write an explicit Eichler-integral normalisation for the axis Q=1 false theta at rationals, citing it as the order6 shadow formula. Then preregister RG47b with that statistic.
2. Test whether the axis-Q=1 piece alone carries the RG46b rank excess (rank of A1 − axis_Q1 piece, closure at w = ½ and w = 1).
3. Route A can only continue with vector-valued or indefinite-signature constructions, e.g. a (1,1) mate or Δ-type laws. Excluding definite mates is a Cat B indication only, pending a preregistered test.

## Addendum (gate update, 10:05 PM CDT, received after the PREREG hash)
- G3 A1^ray (v12 Thm 35.6) was accepted as a radial target, A1^ray = √π/(2√Q(u))·mean(f) for Q ∈ {1, 7/2}. It is not in the hashed PREREG. Using it here would make the RG47b verdict post-hoc, so RG47b stays SKIP for order58.
- The axis pieces in RG47a are sawtooth-weighted means, (√π/2)·Σ f·B̄1/N/√Q, not plain mean(f). Matching them to A1^ray needs a written ray-to-sawtooth map, which should be preregistered in order59. The match is an asymptotic statement, not a QM cocycle, and it is not a P̂_orth completion.
- G1: book Ξ was not used anywhere in order58.

## Proposal only: order61 (not created)
If a hashed Cat A-numeric PASS path for the RG47a split identity is wanted, preregister either an absolute-residual criterion or a relative criterion restricted to |A1| ≥ ε, with ε fixed before running. Separately, preregister the RG48 Weil χ=±i full-basis span test and/or the Milgram genus argument as its own order.
