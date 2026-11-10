# Note on wall Bianchi / J_M5 filing 79795981: stale lift-status lines, and t433u adoption scope
2026-11-10, written 10:35:22 CST (America/Chicago; this is the write time, matching the file's mtime). Author: MR2. Additive status note only; the Bianchi report is not edited. Nothing in this note is adopted. Junction UNSOLVED. Wording: resonant algebra.

# Note on MR2 wall Bianchi / J_M5 filing 79795981: stale lift-status lines, and later t433u adoption scope

Target: MR2_BRANCH_ATTEMPT_BATCH1_C2PRIME_E8_WALL_BIANCHI_JM5_DENSITY_2026-11-10.md, sha256 797959812aeaafc3e1d3c4d59573bc4f315b03936c74121b1138af5c4f877048 = sidecar, written 10:30:58 CST, header = mtime. Script 2a4339e26c97f3c4ca83db71291418e7e3dd4beaaf9b5c4649bcc1791d0c7336 (source mtime 10:24:37, sidecar 10:24:42, run started 10:24:42, mode 444). Log ef281a27920832a323e0e61bee572b44b73e38284f40be7b2ec5b37c00837a21 (mtime 10:27:09, exit 0). reports/ copies cmp-identical, each with its own sidecar. Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 MATCH at this write.

This note does not change any grade in 79795981. It records two timing facts and two nits for the audit.

## 1. Stale "lifts pending PP" wording

The report says, at lines 8, 72 and 133, that the E-S± and E-T lift restorations were still pending Professor Proof. That was already out of date at the 10:30:58 write:

- E-S± erratum 513fdf49b9d4984e2886688e0cd7a44abcc16eb3e51f649eff9394fe181dd9c4 was confirmed in FINDINGS_PP_CONFIRM_MR2_ERRATUM_513fdf49_2026-11-10_1021.md, sha256 dd5a3a25ecd0feb272f35f7ad4925b498b0927b658b9011f5ed966fb0d34859c, mtime 10:22:17 CST.
- E-T erratum 52ba1eea9f3768100ae922552b509815f634d9dc228aac704a44c331ffe64afb was confirmed in FINDINGS_PP_CONFIRM_MR2_ERRATUM_52ba1eea_2026-11-10_1029.md, sha256 e7bc37a184140dd59178e775414f976e6fe0e422163da4c723d4bb99233ec84d, mtime 10:29:10 CST.

The report itself correctly says it does not depend on the lifts beyond listing the candidates. The stale sentences are status only.

## 2. Owner t433u adoption does not include this file

After the report was written, Owner t433u adopted already-PP-proved Math Research 2 results: OW 3df3878860906386276ce33cecac17019124ae1671b5d2d330709cc0058dcf47 (10:32:04 CST), report 20d9e76ae04e31b33455af9a24235cdffaab908542a753ea53baddd64f54bcc1, adoption f3f6d65c845c3dd076e9287495d4d1891f6ffdc144d46b0449e8dc9f660d4fae (10:33:41 CST). That adoption covers only results Professor Proof had already audited and ruled PROVED. This Bianchi / J_M5 filing is not yet audited, so none of its rows is adopted. 1a and B1-c2′ overall remain unadopted. The junction remains UNSOLVED.

## 3. Nits noticed on QC, already partly self-disclosed in 79795981

- The [U] log checks "X0 = X2" and "X1 = X2/2" used sympy's simplify(...) == 0 in the frozen script. The factored formula U = −p²(4 − s) is algebraic. Grounds for a PROVED grade on those two identities should be the algebra, not simplify == 0.
- The Hodge-dual match in row 1, and the pointwise defects in row 7, are high-precision floating checks (25 digits; ≤ 8.6e-42). They are disclosed in the report. Whether they support PROVED or stay COND is for Professor Proof.
- The self-disclosed nits in 79795981 (name vs mtime, wrapper .exit, V2 prefix log line, [F] artefact, mislabelled ⋆² check, unused U_s, elapsed counters) were verified: the .exit file is 7 bytes, "exit 0", not copied into reports/.

Tip untouched. No CERT.
