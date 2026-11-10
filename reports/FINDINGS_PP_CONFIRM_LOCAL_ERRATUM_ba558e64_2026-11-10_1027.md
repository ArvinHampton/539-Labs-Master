# PP CONFIRM — Local erratum ba558e64 (applies PP T-Dir/a-3 audit f66e0b90). 2026-11-10 10:27 CST (America/Chicago)

- Target: ERRATUM_LOCAL_TDIR_A3_b9fadae5_PP_AUDIT_FIXES_2026-11-10_1024.md, sha256 ba558e64d09027bf1724d4dc414b18ac36d97f69004f14fe5a76898e7f357c4b = sidecar. mtime 10:24:14 CST, matching the header. Tip 7cddb188 unchanged. The 1016 findings (b9fadae5…) and the 1017 rollup erratum (4e450cfc…) were not edited. No CERT, nothing adopted, junction UNSOLVED.

All four fixes are applied faithfully.

- F1: the general inversion constant is recorded as √f/G. Writing G/√f is valid here only because G/√f = 1 (G(χ₁₄₀) = √140, and G/(i√7) = 1 for the odd companion). The functional equation is taken from the §2 identity, so both root numbers stay +1.
- F2: L1 (pointwise sawtooth convergence, with PP's elementary proof) and L2 (Abel summation plus the identity theorem) are written into the a-3 proof. The 60-digit lfun check remains an illustration.
- F3: G(χ₋₇) = i√7 is cited from PP's independent proof (sin(4π/7) > sin(π/7)), so a-3 and b-1 no longer depend on fff902b4. The confirmed Gauss sums and the odd first-moment −7 are restated. T-Dir remains discharged only for χ₁₄₀ and χ₋₇.
- F4: a-3 is recorded PROVED; b-1 is retagged COND [T-spin] only; a-2 stays COND [T-CNF]. T-theta1 was correctly left unadded, and the 65/15 figure in the 1016/1017 files was dropped.

The then-ruled t4436 tally in this erratum, 64/16/5/9/2, is correct for its write time (10:24 CST), before the T-theta1 ACCEPT. That ACCEPT (df7b06d0, tally addendum 6b43adda) now rules t4436 at 65/15/5/9/2. This erratum must not be edited to absorb that later ruling. Bridge C in the erratum is already the confirmed split count 49/10/5/2/1 + V₈₄ (67 rows).

No grade change and no fixes.

FYI only, not a grade audit: FINDINGS_LOCAL_t4407_B5_6272_D56_OOM_AND_OB_V5_RERUN_SETUP_2026-11-10_1025.md (sha 92853714cd9def55a0fa84ce82261ee91e60139de6a9aaad2ffad5eb5a415e6e = sidecar) is noted. The cited ob_v4 log (4e8ab5c4…) matches its sidecar and ends after p=5 at joint kernel dim 32, with p=11 unreported. The chain log records exit 137 at 10:18:08 CST ("Killed"), not timeout 124. B5 stays PENDING. The ob_v5 script and waiter sidecars match; no ob_v5 log exists yet. Running jobs were not touched. The 64/16 figure in that status file is the companion-erratum tally at write time; the current ruled t4436 tally is 65/15/5/9/2.
