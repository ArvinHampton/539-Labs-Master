# FINDINGS 2026-10-24 — order67 audit (Auditor, Residual-vs-Resonant)
Time: 2026-10-24 ~22:30 CDT. Read-only audit. No PASS/FAIL altered. No Ξ coeffs adopted (G1 REJECT binds).

## Hashes (verified on disk)
- order67/PREREG.md c41f9e7fd6b2…dc88 = PREREG.sha256 ✔ (mtime 22:22:16 CDT, before RESULTS 22:25:58)
- order67/RESULTS.md 523ccb8dbb856e82c79de4e7595b7b5f58ce527b1978ed2983e85a52dfd2c459. This is the post-fold sha. The coordinator's earlier figure, 965d44c7…, was the pre-fold sha and is superseded; the coordinator confirmed 523ccb8d is the sha to audit.
- SHA256SUMS: `sha256sum -c` passes for all 5 entries (PREREG, RESULTS, logs/search.log, data/DEEP_HUNT_WRITTEN, data/DEEP_HUNT_BROAD_TRIAGE).
- data/DEEP_HUNT_WRITTEN 555bd1c5… = reports/ copy ✔; data/DEEP_HUNT_BROAD_TRIAGE 1afbb051… = reports/ copy ✔.
- X1 source Continue_Resolution_Residual_Shadow_Xi_2026-08-23.md 552541cf… matches the sha quoted in RESULTS ✔.

## Checks
- PREREG before hunt: PASS (mtime order; RESULTS cites the PREREG sha, and PREREG was not rewritten).
- A(2)=[[4,14],[14,14]] is labelled a search-target label and explicitly NOT a Clean_v2 Gram (RESULTS "Gram hygiene"). OK.
- Verdicts: READY NO; RG47f-bis/g/h SKIP; Δ is a definition only (Cat A), and its law is ABSENT. CONFIRMED, consistent with PREREG §(A) ABSENT branch. Nothing invented.
- BROAD_TRIAGE fold: PRESENT in the audited RESULTS (523ccb8d) as the "Addendum BROAD_TRIAGE" section: X1 Ξ series form FOUND, with coefficients flagged as placeholders and never tabulated; G1 REJECT binds; X2 is a kernel; Ξ_compl ABSENT; Map-C6/M_S ABSENT; the nonlocal Ω₁₁D section is kept out of the local claim. So the coordinator's "Local MISSED" applies only to the pre-fold version 965d44c7. **Miss NOT confirmed against 523ccb8d.**

## Notes / warnings
- N-67-1 (NOTE, PAPER-vs-CHAT): the main RESULTS body, under "Residual triage", still says Ξ hits are "None is a target object" and lists only Clean_v2 and theorems/ Ξ. X1 appears only in the addendum. The two sections are consistent, but a reader of the main body would miss X1. Fix: in order68, add a one-line cross-ref from "Residual triage" to the Addendum. Not a warning.
- N-67-2 (NOTE): the "Coverage" section still says "broad patterns were not all hand-read". BROAD_TRIAGE §method says the narrowed hits were all read, but the un-narrowed hits (Ξ 1853, flux 58384) were not. That residual risk is honestly stated.
- W-67-1 (WARNING, low): RESULTS was rewritten after its first hash (965d44c7 → 523ccb8d). There is no in-file note recording the pre-fold sha. Fix: add "supersedes 965d44c7…" to the Addendum header or HASH log. This is a provenance hygiene issue only, and verdicts are unchanged.
- DEEP_HUNT_WRITTEN quotes vs RESULTS: Clean_v2 :698-699, :2606, P_orth :35, PREREG:16 lines agree with RESULTS. OK (spot-check).
- The X1 lines :16/:20/:22/:28 quoted in the addendum match the BROAD_TRIAGE quotes. Not re-read against the source beyond the sha match.

## order68
Not on disk at audit time. Pending: the ask was to fold BROAD_TRIAGE, which is already in order67, so order68 should only add the N-67-1 cross-ref and the W-67-1 supersede note.

## NL
- W-NL-3: CLOSED per prior status (milestone e:3 tag); not regressed.
- W-NL-4 OPEN (CJS/GC1/RICCIBLOCK result.log unhashed).
- W-NL-5 OPEN, widened (~22:30/~22:40 stamps). Not re-scanned this pass.
- No new NL landing verified this pass.

## Local hygiene
W-65-1, W-66-1, W-64, W-C3/C10 stay CLOSED per FINDINGS_2026-10-24_hygiene_closes.md. Those files were not re-hashed this pass.

New: Blockers 0 / Warnings 1 (W-67-1) / Notes 2.
