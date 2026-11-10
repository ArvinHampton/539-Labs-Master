# FINDINGS — PP confirmation of NL_ERRATUM23_ACCEPT_PP_e9ac8a37_f530cbc0_2026-11-09_2241.md
PP, 2026-11-09, CST (America/Chicago). Labels are pure math. No CERT. Nothing sent. Additive. Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 checked at start.

## Integrity
- Target 4bdfb71c…: its sidecar checks OK.
- All 11 sidecars in /workspace/nl-e23-2233/ check OK. The NOTE file is 77ab006c86fde47d….
- /workspace/nl-d6s2-2110/z2_bvp_continuation.log is b4036905372c64f3…, identical to its hash at the PP 2228 audit, so it is unedited. The NOTE file records the hand-typed line and edits nothing.

## Verdict: FAITHFUL
| item | check | result |
|---|---|---|
| E23-1 S2-4 twist lock | all four steps match PP f530cbc0 §3; premises stated; credited to PP; labelled PROVED (implication) | ✓ |
| E23-2 w·w′ ≥ 0 | NL's 2233 w3 log is a Laurent identity against 2G^{ww}∂_wW; zeros {0}; f′(0)=3; this matches PP A3 | ✓ PROVED (exact) |
| S2-7 | the 5 missing premises are listed, plus the S5 escape and S6 as a record premise; stays COND; [χU] and [χS] kept | ✓ |
| S2-12 | the real-print log gives 31 = 30+1; 30L reach for exactly 12 flows (w_m ∈ {−0.05,−0.10}, d6 ≥ +0.05); the ten w_m=−0.3 flows end by 2.01L; no complex artefacts; stays COND | ✓ |
| R6 / E22-δ | PP's independent exact check: d²″ − 4(96A′²+8A′+1) expands to 0 identically, and disc = 64 − 384 = −320 < 0. So d² is strictly convex, and 1.2443057… is the unique global minimum. Its value is a float, so R6 stays COND | ✓ |
| abs(b) | NL 2239 log: 6A′ on 4/4 locked sectors (γ_r = ±1); 2A′ on 4/4 unlocked sectors (γ_r = ±1/3). Agrees with PP B1 | ✓ |
| eta 2233 | the spurious 1/Δ (ω₂ = −2^{14/15}/2, giving 0/4 and 0/4) is disclosed, the file is left unchanged as a record, superseded by 2239, and supports no claim | ✓ |
| z2 log | unedited; the annotation is in the separate NOTE file | ✓ |
| revised D6 S2 tally | 8/2/3/0 = 13, matches PP f530cbc0 | ✓ |
| E22 roll-up | 0/0/0/0 distinct | ✓ |
| branches | [χS], [χU] and [w] kept; nothing adopted; junction UNSOLVED | ✓ |

## Tally
NL's header tally of 2/0/0/0 is accepted as a row count. For any roll-up, the distinct new claims are **0/0/0/0**:
- E23-1 is the S2-4 grade change, already counted in the revised 2216 tally.
- E23-2 is added content of the S2-10 row.
NL §0 says the same in substance. Refutations: none.

## Fixes (bookkeeping only; no grade changes)
- E23-α: credit E23-2 to PP (f530cbc0 A3, pp_d6s2_exact_2026-11-09_2225), re-derived by NL, the same way E23-1 is credited.
- E23-β: state "distinct new claims for roll-up: 0/0/0/0" explicitly next to the 2/0/0/0 header, as was done for E22-β.

Tip at write time: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (unchanged).
