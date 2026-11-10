# FINDINGS — CONFIRM deduce_t700u_ga1b LOCK (G-A1b Dual-split)
Stamp: 2026-10-25 10:24 CDT (America/Chicago). Auditor: Residual-vs-Resonant. Authority: Arvin t700s4408 (PURSUE Dual-split). Base: BRIDGE_C_35/. Soft-SF only; PASS/FAIL untouched.

## Hash match (live recompute)
| Artifact | Claimed | Live |
|---|---|---|
| deduce_t700u_ga1b/PREREG.md | 07ae9d08b02edd57d9b628082fa722a7de09a82cb7af36ba3ab57068bca4ddad | MATCH |
| deduce_t700u_ga1b/RESULTS.md | 3ce2f550e9103fb2bf2c34e073e431bb13fe123d6bbdfc39d4a3b124d4767abd | MATCH |
| deduce_t700u_ga1b/SHA256SUMS | b1e69bf49e803f1b1052d38163b5749b3b9404dd4d19dc928796161e78ac58e1 | MATCH |
| author_candidates/AUTHOR_CANDIDATE_GA1b_DualSplit_Paired_Scheme_2026-10-25.md | 0504098862367dc0c8d2ea08af4460feb19064c23481701bf85d9e7cf63c5650 | MATCH |
| STREAM_IDLE_LOCAL.md (BRIDGE_C_35 root) | ac41e5b14922dd72341f5af297ec6900a3dc856c38731e0c9b1a285c23b3497f | MATCH |
| inventory_check/SHA256SUMS | 541ae988cf25ceecfbe391dacdf330be8913ec61dbca17d0b65c4c8c3c5c795e | MATCH |
| Baseline FINDINGS t695u | 437d4571e0f707460c7ac2a7dd983d0649161dd7975779101907eaedba7d7476 | MATCH (present, unaltered) |

sha256sum -c: deduce_t700u_ga1b/SHA256SUMS 4/4 OK; inventory_check/SHA256SUMS 51/51 OK.
Order: PREREG mtime 10:22:10 CDT < RESULTS 10:22:35 CDT; RESULTS cites PREREG sha unchanged; pass/fail rule fixed in PREREG. OK.
Note: STREAM and inventory paths are BRIDGE_C_35 root, not inside deduce_t700u_ga1b/ (path ambiguity only, no SF).

## Claims
1. Dual-split NOT DEDUCED-FORCED — CONFIRMED (RESULTS Q3; Q1 DEDUCED out-of-scope of domain-restricted ansatz; Q2 per-point Written ABSENT).
2. Candidate R-DS0/1/2 scheme, no numeric invent, NOT Cat A — CONFIRMED. Numerals present are only W₇ image coordinates (−1, −1/3, …), sample x, and cited Written aggregate (0.14–0.29, ~1e-13); no DS cell supplied. Header labels "NOT Cat A; NOT law".
3. Bridge PARTIAL; READY NO; residual-C OPEN; no δ≡0/RG76d/Bridge YES force — CONFIRMED (RESULTS Q4 + STREAM L23). G-A1b closure cannot force G-A1c uniqueness — CONFIRMED.
4. SF-W7-3 / CORE_FREEZE — CONFIRMED (PREREG header; Closure-named files fenced in Q2).
5. Baseline 437d4571… premises held — CONFIRMED (re-cited and re-verified; not superseded).
6. t700s4408 cited — CONFIRMED (PREREG, RESULTS, candidate, STREAM).

## Soft SF
SF-T700-*: none raised.

## Open set
G-A1b (candidate pending Arvin ACCEPT/reject; R-DS2 needs precedence statement vs weakened S-B1), G-A1c, G-A3 (h_residual^{high} ABSENT), G-R2; X4 coeffs ABSENT; B3 empty. No order78.

Verdict: CONFIRM LOCK deduce_t700u_ga1b. Candidate NOT accepted as Cat A.
