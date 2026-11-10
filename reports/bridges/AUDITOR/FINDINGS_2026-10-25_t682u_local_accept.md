# FINDINGS — t682u Local deduce_t682u_accept LOCK CONFIRM (post AUTHOR ACCEPT)
Stamp: 2026-10-25 10:03 CDT (America/Chicago). Auditor: Residual-vs-Resonant. Soft-SF only; PASS/FAIL unaltered. NL not touched (separate sibling). No order78.
Authority: AUTHOR ACCEPT Arvin widget t686s4344 via Physicist.

## Hash match (live recompute)
| File | Claimed | Live | |
|---|---|---|---|
| deduce_t682u_accept/PREREG.md | 8de2d410…290be | 8de2d4103a3375665275701fe89aa56c85f2909496029cdfbf0e52c8144290be | MATCH |
| deduce_t682u_accept/RESULTS.md | dea821d5…611e4 | dea821d5524ff090987c5bed426c25567a2f787d7189248db800f7eb3a1611e4 | MATCH |
| deduce_t682u_accept/SHA256SUMS | bcc2ddbb…e7d22 | bcc2ddbba5b7ab4b72369d5d0d5d9cdac9e1f5c7f36e456240843e2b1c2e7d22 | MATCH |
| BRIDGE_C_35/STREAM_IDLE_LOCAL.md | 91aafa60…bb45f0 | 91aafa60d9c6def5789cdb5da866fe5fb2027a2be14c7fd0a2851a813bbb45f0 | MATCH |
| P-B1 AUTHOR_CANDIDATE_B1 (S-B1∧S-B1′) | fdc79a11…4868 | OK via deduce_t682u/SHA256SUMS | MATCH |
| P-X4 AUTHOR_CANDIDATE_X4 sketch | 156ea029…320a | OK via deduce_t682u/SHA256SUMS | MATCH |
| P-B3 AUTHOR_CANDIDATE_B3 schema | 5f60d40f…c94c | OK via deduce_t682u/SHA256SUMS | MATCH |

SUMS: deduce_t682u_accept 3/3 OK; deduce_t682u 6/6 OK (incl. 3 premise files). inventory_check/SHA256SUMS mtime 2026-10-25 00:30 CDT — NOT updated for accept package (no t682u entries).
Order: PREREG mtime 10:00:28 CDT < RESULTS 10:00:50 CDT; RESULTS cites PREREG sha unchanged. PREREG-before-RESULTS OK.

## Claims
- ACCEPT cite: PREREG §Authority and RESULTS header cite t686s4344 for all three Cat A premises with shas. CONFIRMED (no uncited Cat A).
- RG-A1 PARTIAL — CONFIRMED, scope: Written fit re-evaluated by auditor (19.80118, 3.16070, 20.66518, 55.30206) reproduces Object A. D1: S-B1′ bounded ⇒ b=c=0 (deg-3 also excluded). D2: reduced a+d/(1+t²) even in t; t=∓2 samples 19.801180≠20.665180 ⇒ family EMPTY under S-B1′∧Object A. Exact algebra, no numeric invent. Family EXCLUDED, NOT unique. Dual-split NOT FORCED (only aggregate stats; G-A1b) — not upgraded.
- PARTIAL + G-A1a conflict scoping: correctly scoped as a tension between ACCEPT premise P-B1 and the Written residual_slash ansatz, routed to author; not a FAIL, no force. See SF-T682LA-2 on wording.
- RG-A2 X4 ingested as shape only; folding/coeffs ABSENT (G-A2). CONFIRMED.
- RG-A3 B3 schema ACCEPT; values empty ABSENT (G-A3). CONFIRMED.
- RG-A4 δ≡0 / RG76d / Bridge YES NOT newly forced. CONFIRMED.
- Standing: G1 ACCEPT; residual-C OPEN; Bridge PARTIAL; READY NO; no order78; SF-W7-3 stated; CORE_FREEZE stated; no numeric invent. CONFIRMED.

## Soft SF (non-blocking)
- SF-T682LA-1: D3 uses residual_slash ∝ |7x|^{-1/2}·F; that normalization is not restated in PREREG/RESULTS with a Written cite. D3 is corroborative only (D1+D2 suffice); auditor did not independently source it.
- SF-T682LA-2: G-A1a wording "no Written residual_factor satisfying S-B1∧S-B1′∧Object A" should be scoped to "Written 4-param family + deg-3"; Dual-split remains undecided (G-A1b), so a universal phrasing over-reaches.
- SF-T682LA-3: Brief label omits deg-3 exclusion that RESULTS/STREAM include — harmless, note for consistency.
- SF-T682LA-4: inventory_check/SHA256SUMS not updated for deduce_t682u_accept.

## Open set
G-A1a, G-A1b, G-A1c, G-A2, G-A3; residual-C OPEN; author decision on P-B1 vs Written slash (revise S-B1′ / ACCEPT out-of-family residual_factor / supply Dual-split W_7-paired values); T1–T4.
Blockers: none for LOCK. Bridge PARTIAL; READY NO.
