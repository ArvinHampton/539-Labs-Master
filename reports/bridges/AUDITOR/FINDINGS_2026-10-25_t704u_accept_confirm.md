# Auditor FINDINGS — deduce_t704u_accept CONFIRM (post-ACCEPT R-DS0 ingest)
Stamp: 2026-10-25 10:30 CDT (America/Chicago). Lock: Residual-vs-Resonant. Auditor recomputed every sha256 independently; executor draft 9367111b… (FINDINGS_DRAFT_for_Auditor_CONFIRM_t704u) NOT used as authority.

## Authority (ACCEPT cite)
t704s4427 AUTHOR ACCEPT (Arvin): R-DS0 scope-exclusion ONLY, candidate AUTHOR_CANDIDATE_GA1b_DualSplit_Paired_Scheme_2026-10-25.md sha256 0504098862367dc0c8d2ea08af4460feb19064c23481701bf85d9e7cf63c5650 (live recompute MATCH). R-DS1/R-DS2 NOT accepted.

## Integrity (recomputed)
| Item | sha256 | Verdict |
|---|---|---|
| BRIDGE_C_35/deduce_t704u_accept/PREREG.md | dc74aab66ab20821251625d1dbc6dc1d023e6389a8710c926fa869f522524470 | MATCH |
| .../RESULTS.md | e5b65693825612866c76c5466e48b6e85abf0935bad12d51664a253048c2790a | MATCH |
| .../SHA256SUMS | 2700f98c510d0d48bb73c59c1135a085ccb3bdafa1619890f5eca95c810a43f3 | MATCH; -c 3/3 OK |
| BRIDGE_C_35/STREAM_IDLE_LOCAL.md | 6b54d64221bdb2ca0744a4b3392b3d641d61ccf14f2613d547b109c1cd9cb35c | MATCH (LOCK line t704u present) |
| BRIDGE_C_35/inventory_check/SHA256SUMS | 59a05632870fe9707a1c1376cb5024e8e2a7e15955687ff692059338f40b97a4 | MATCH; -c 55/55 OK (lists t704u PREREG/RESULTS/SUMS) |
| Candidate 05040988… | 0504098862367dc0c8d2ea08af4460feb19064c23481701bf85d9e7cf63c5650 | MATCH |
| Baseline FINDINGS t695u_local_accept | 437d4571e0f707460c7ac2a7dd983d0649161dd7975779101907eaedba7d7476 | MATCH (unaltered) |
| Pre-ACCEPT FINDINGS t700u_ga1b_dual_split | 914bda3c5830a0fe4efd0d24ff91d337d95a10406dd1bbc3459c18b5f3b44898 | MATCH (unaltered) |

PREREG-before-RESULTS: PREREG.md + PREREG.sha256 mtime 10:26:49 CDT; RESULTS.md/SHA256SUMS 10:27:06 CDT; RESULTS quotes PREREG dc74aab6… "unchanged". PASS.

## Scoping / fences
- R-DS0 only ingested as ACCEPT-sourced Cat A [t704s4427; 05040988…]; R-DS1/R-DS2 NOT accepted, NOT ingested. PASS.
- Dual-split OUT of scope for residual_slash; no Dual-split cells. G-A1b CLOSED. PASS.
- Selectors Cat A baseline 437d4571… (t695s4386; source 3d502756…) STANDS for selectors, unchanged.
- 914bda3c… (pre-ACCEPT, AUTHOR-CANDIDATE hygiene) is draft-only and SUPERSEDED by this CONFIRM.
- CORE_FREEZE; SF-W7-3 Closure fence; no numeric invent; no nonlocal objects; no order78. PASS.
- ACCEPT cite present at every Cat A / AUTHOR-ACCEPT use (PREREG Authority, RESULTS PIN, RG-D1, STREAM LOCK). PASS.
- NL baseline 29ebbdd8… (W-PO-2 CLOSED / W-PO-3 FINISHED) untouched.

## Standing (as RESULTS, unaltered by Auditor)
G-A1b CLOSED (R-DS0) | Uniqueness UNIQUE-in-family / overall PARTIAL (G-A1c OPEN) | δ≡0/RG76d/Bridge YES NOT forced (G-A3 ABSENT) | Bridge PARTIAL | READY NO | residual-C OPEN. Open gaps: G-A1c, G-A3, G-R2; X4 coeffs ABSENT; B3 table empty.

## Soft SF
None. (Note, not SF: executor draft file sits in package dir outside SHA256SUMS; non-authoritative.)

## Verdict
CONFIRM. New Local baseline for G-A1b = this FINDINGS; selectors baseline 437d4571… stands; 914bda3c… superseded.
