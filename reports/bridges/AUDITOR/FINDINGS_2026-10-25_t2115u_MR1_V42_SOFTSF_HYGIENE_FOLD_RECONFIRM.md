# FINDINGS — re-CONFIRM MR1 V₄₂ Soft-SF hygiene fold §1j (t2101u/t2115u)
Date: 2026-10-25 ~21:25 CDT (America/Chicago) · Auditor · CONFIRM-only · no tip edits · no messages

## Verdict: MATCH-with-SF (fold itself MATCH; live tip has drifted past a6bc20f8 — SF-1)

| Check | Expected | Observed | Result |
|---|---|---|---|
| Stamp OWNER_WRITE_MR1_V42_HYGIENE_FOLD_t2101u | 29a1e512… | 29a1e512fc4e0f7e176e99f47f9069a19983836f4d26afb8d585677124c72465 | MATCH |
| Backup pre-mr1-v42-hygiene-fold-d29007f1 | d29007f1… | d29007f1e67a1a002c466914d02d533dda76009677fd6cf3bf04e31a9c92ac24 | MATCH |
| Live tip AFTER | a6bc20f8… | **90bbf5089eddea8b0a52370cbb69b78d714b9bad9230dffe80ca19a8c5ef4882** | DRIFT (SF-1) |
| Sidecar .md.sha256 = tip | = tip | 90bbf508… = 90bbf508… | MATCH (vs live tip) |
| Reconstructed a6bc (backup + only tip lines 152,159 §1j) | a6bc20f8… | a6bc20f82b22f0eba0af853aca04142ba54d9a988e87580c17bf76838b165aed | MATCH — fold was §1j-only |
| Cited FINDINGS t1135u_MR1_V42_BASIS_FOLD_RECONFIRM | 00271a5c… | 00271a5cdb0e1e92a448ac7a12a92c2f8e384ceb6106f234a8e468dd70b94042 | MATCH |
| CLOSED stamp MR1_V42_BASIS_FOLD_CLOSED_t1135u | db71207c… | db71207cdf0c682bc4ffb83886d20c2dd9f7959f215e2a7bbed7e35714c9af4b | MATCH |

## Diff backup d29007f1 → live tip 90bbf508 (4 lines)
- L152 §1j heading: pending → MATCH-with-SF cite 00271a5c… — **in scope**
- L159 §1j Status: await → re-CONFIRM landed, CLOSED db71207c…, READY NO / Bridge PARTIAL / NOT Cat A — **in scope**
- L127 §1g heading + L141 §1g Status: pending/await → MATCH-with-SF cite c570af8f… (FINDINGS_2026-10-25_t1129u_MR2_P_OMEGA_FOLD_RECONFIRM.md; sha verified c570af8fc1197c745dd6775fb755f825bb4b288bc04f9a4bdb9af0d11860db0f MATCH, sidecar MATCH) — **out of this fold's scope; no stamp located for a6bc→90bbf508**
- No W₇/gens/k/ρ/V₄₂ content lines touched. No physics content changed.

## Soft SF
- SF-1: Live tip 90bbf508… ≠ claimed a6bc20f8…. Post-fold hygiene edit to §1g (MR2 lane, cites real c570af8f MATCH) applied without an owner stamp/backup of a6bc20f8. Content benign (status hygiene only) but provenance unstamped → MR2 lane should stamp/back up.
- SF-2: §1h stale-pending not touched (disclosed, MR2 lane).

## Gates
Bridge PARTIAL · READY NO · NOT Cat A (all retained on tip).
