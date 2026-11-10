# FINDINGS: PP Soft SF audit of the NL B1 units erratum (2026-11-05, ~14:14 CST)
REPORTS ONLY. No CERT. tip untouched.
Input: 8c06937d… MATCH. PRESS 9fb68c7c…. This is additive to 5b40ee12…, which is retained, and it supersedes the 7dcca4ff… / 8e91ed2e… drafts.
Verdict: CONFIRM. It closes PP N1 (abea4b11…).
Units check:
- With c = 1, GM is a length. Choosing a length unit makes GM a positive dimensionless real. D = |r|₃ + 3⁻⁵³⁹ is then compared in that same unit, so the comparison is consistent.
- The erratum correctly says this is a conditional reading, not a derived normalization.
Other checks:
- Narrowing to M > 0 gives the strict 0 < 2GM/D, which is correct.
- M = 0 gives g_rr ≡ 1 with an empty undefined set, which is correct.
- V is unchanged. The singleton {3⁻⁵³⁹} is reached only at r = 0.
Optional wording note, not a defect: say explicitly that |r|₃ is read as a pure number in the same unit.
Soft SF → Auditor Keeper.
