# AUDITOR FINDINGS — t1145u PR1 PURSUE RESOLUTIONS rev.17 CONFIRM
Date: 2026-10-25 ~20:52 CDT (America/Chicago). CONFIRM-only. No physics invented. residual-C not edited. No outbound messages.

## Verdict: MATCH-with-SF

## Artifacts (sha256 re-hashed)
- Catalog `/workspace/obs-data-PR1-HEPP-QM-GR.md` = `906f2d13fe22c3513a818ce91857e4a1e063a69eb08e2a8e32134ec4f64f9421` — MATCH
- Report `/workspace/quantum-comp/reports/PR1_PURSUE_RESOLUTIONS_nudge_2026-10-25.md` = `b5bfcad801caa3ab3a05340817a3bf3059dcbf8616c82e80459cd08a0f7609b8` — MATCH
- Prior: rev.16 CONFIRM FINDINGS `3831b6a5…` / catalog `0a9ef2dc…` (report names backup `.pre-rev17-0a9ef2dc.bak`) — chain consistent.

## Checks
| Expect | Result |
|---|---|
| Tip touched by PR1 | NO. Live residual-C `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` = `0677d02a10f298d0e84f41f6da876fe6ed4b886b92000ed70e9cec3be6173ca3` (mtime 20:47:47 CDT), cited read-only; drift 70c47a4c→0677d02a attributed to other lane (consistent with prior Auditor FINDINGS: MR2 §1k). LOCK_DIGEST `964294cc…` kept. MATCH |
| Bridge PARTIAL / READY NO / NOT Cat A | Present in report, changelog rev.17, footer. MATCH |
| [V] Kostelecký S2/S3/S5 | §2G (L222–226), arXiv:0801.0287, orders of magnitude only. MATCH |
| [V] EHT M87* Paper VII | §2B L72, arXiv:2105.01169, 2017 campaign; 2018 explicitly not fetched. MATCH |
| [V] continuum-fitting spins CONTESTED | L71, arXiv:1312.6698 Table 1.1; status CONTESTED. MATCH |
| OPEN: GP-A Vessot; Lamb; EHT 2018 | Gaps L282/L288/L292 + changelog L309. MATCH |
| Author ABSENT mechanisms | photon→torsion-hole, "exposes electron field", W4 DE coeffs, nuclear rates, BH-reverse rates — ABSENT; nothing invented. MATCH |
| Pursue-resolutions framing | Report title + changelog "corrected framing 'pursue resolutions'". MATCH |

## Soft SF (non-blocking)
- SF-1: Catalog header line 2 rev list stops at rev. 14; revs 15–17 only in changelog.
- SF-2: Report top line cites pre-refresh catalog sha `03a35de6…`; superseded by final `906f2d13…` in the same report (self-corrected, but stale line kept).
- SF-3: Changelog rev.17 placed after footer (L309 after L307) — ordering only.
- SF-4: 5 residual `c7121aa8` mentions remain, all labeled "superseded" history (acceptable per report).

Tip untouched by PR1: Y. No Cat A. Bridge PARTIAL / READY NO.
