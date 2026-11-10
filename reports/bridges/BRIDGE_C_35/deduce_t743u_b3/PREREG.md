# PREREG — t743u B3 (h_residual^{high} table) — Bridge C local modular only
Date 2026-10-25 (America/Chicago, CDT). Arvin t743u PURSUE B3 (overrides Hold). Invent-ban; CORE_FREEZE; SF-W7-3; Residual-vs-Resonant; no nonlocal EH11D; no order78. G-A3 stays PAUSED (no compute/fill reopen); filled table 4da09dec… stays REJECTED.

## Object
B3 = h_residual^{high}(x), h_residual^{high}(W_7 x) at x∈{1/7,3/7,5/7,1}; W_7 images −1, −1/3, −1/5, −1/7 (7368b855 L44). δ_{W_7}h(x) := h(x) − residual_slash(x)·h(W_7 x). Empty table blocks δ≡0 / Bridge YES via RG76d.

## Methods
- M1 Corpus Written extract: rg over /workspace/quantum-comp for h_residual^{high}/h^{high}/h_residual sample values at the 4 nodes + W_7 images. Exclude order*/closure-tree Pack+(S) fits (SF-W7-3), exclude REJECTED 4da09dec… and G-A3 compute outputs (not Written). Hits → logs/search_hits.txt.
- M2 Re-verify P-B3 schema 5f60d40f… unaltered; t708 schema v2 live sha; confirm G-A3 PAUSED / fill REJECTED in STREAM_IDLE_LOCAL.
- M3 Force check: does Cat A stack (S-B1′/S-B1 + R-DS0 + R-UQ0 + R-NV0) force B3 values or δ≡0? Expected NO.
- M4 If Written ABSENT: AUTHOR-CANDIDATE menu (nothing adopted; no numeric cells).
- M5 STREAM LOCK append.

## Force criteria (pre-stated)
- F-B3a Written h_residual^{high} sample values present at nodes? YES/NO
- F-B3b Cat A stack alone forces values or δ≡0? (expected NO)
- F-B3c Prior REJECTED fill 4da09dec… counts as Written? NO (REJECTED; not Cat A)
- F-B3d AUTHOR-CANDIDATE menu needed? YES iff F-B3a NO

## Baselines (verify live full sha)
437d4571e0f707460c7ac2a7dd983d0649161dd7975779101907eaedba7d7476 t695u FINDINGS; b34aebe65a3f57eff1690dde5fce01efa8e3722331e1098ee5f6efb578c905ac t704u; R-UQ0 3181e59e0cb81668fe008028d35ccdee8536bd25158aed650cb57728d2631c60 + CONFIRM 7e20e84c4508dcff21169c89eb407a914e9f99ff56e478dc71cf406a23b06a24; R-NV0 e3fd1b1127b58fa86fac9c671ac4292fa0a7c72119ae79caab8f890f1906ac13 + CONFIRM 2b959003d46762278c8da36a6562da63cd5b6a30d47f02faed8ed2d23900638b; P-B3 5f60d40f43ad1b4a8fcbcbde0bff019921ba15bd2867e0e2882d821bb2a2d94c; X4 2bb870b47a3c11d5a6466aa6acd335cd9b37e94c5775c6b763bb9e7c4cc11d76 (candidate); REJECTED 4da09dec14b6881583bfd685e1c44eb3563bd649f25d05e6f8e91cd618e49d39.
Expected: Bridge PARTIAL; READY NO; residual-C OPEN.
