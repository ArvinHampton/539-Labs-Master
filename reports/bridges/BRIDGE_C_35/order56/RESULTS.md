# order56 RESULTS (local modular only; RG* labels; CORE_FREEZE: new files in order56/ only)
STRIP.md sha cd96c9af…3837, PREREG.md sha 1fb0ada6…255f, both hashed before running anything. Script hash is in SHA256SUMS. Data: data/rg46.json, data/rg46_raw.npy. Log: logs/rg46.log.
## Audit (Category A, sources)
v12 §40.3 "Where the shadow Ξ enters": Ξ is described only in words and is "not written as an explicit series". v12 "What is not achieved" (2) says "The shadow Ξ is not identified". v12 Open problem 1 describes A1 − Ξcompl as a task, not as a written object. v12 Remark 36.1 and order4a say the sawtooth candidate Ξ_ε does not close. order5 located only the shadow of the cone part H (unary thetas 5n²/2 and R²/34).
## RG46a: PASS (Category A-numeric). The identity Â1 = A1 − Ξ_compl + A1(Δ) = A1(P_orth) holds.
- Max relative deviation: 1.1e−15 at x and 1.8e−15 at −1/x, over 216×105 each.
- Control (wrong strip sign) fails as required, with deviation 3.25.
- The test is not vacuous: max|A1(Δ)| = 3.22.
- This confirms A1(Ĥ) = 0 on the sample. That was order5's §1.4 proof sketch, until now only Category B.
## RG46b: FAIL (Category B). Â1 is not S-closed.
- The gate passed: A0 has rank 36 and closes at w = 1; at the wrong weight the joint rank is 72.
- Â1 has rank 75. Joint rank is 148 at w = ½ and 150 at w = 1.
- Reading: once the strip and the completion are removed, the whole t^{−1/2} obstruction is the orthant piece A1(P_orth). This agrees with order5.
## Ξ match: SKIPPED by the prereg. No written target exists (v12 §40.3).
Ξ: not identified. Bridge: NO.
## Open next
Derive a written completion of the orthant piece P_orth (the axis false thetas Q = 1 and 7/2, plus the double-orthant corner). Then preregister an S-law test for A1(P_orth − P̂_orth).
