# FINDINGS — order76 BRIDGE_C_35 (local modular only) — 2026-10-24 23:24 CDT
Auditor: Residual-vs-Resonant. Soft flags only; PASS/FAIL unaltered; nonlocal untouched.

## Live shas (all match citations)
- PREREG.md e8fe0692a2b9e6758769ad82544fc68b3e34ec8dadce8d22f9e5fecb03d7d998
- PREREG.sha256 669ce68fcc90edf042f227e5468a4400d1359096c4b1268dae87df89331de129 (-c from BRIDGE_C_35/: OK)
- RESULTS.md 49d13fd3693af36b59695c06a5c2540257a14aa1ac788a2e62874cb7c8c2fcb4 (cites PREREG e8fe0692…)
- STREAM (live ../STREAM_IDLE_LOCAL.md = data copy) b4138a1fdf2c56ec14eb3b315808a1b0c93da6ea280ddcbb6c6e8180d2b1a3ed
- STREAM_PRIOR 949647bf45bb562154c1ed9ce4676c3890e6e5c06788d5194711223120977d83 (= order75 STREAM parent)
- verbatim b9a214385ef8c550570a20327e5ef1f74f4608ddd355b8cba78ba6782e303f90 (= pin; cmp byte-identical)
- SHA256SUMS dd8c8d64f73076ccae4ddc7f545d5dbaa9f67904c5ab0e215313d26d72c3cfc3
- sha256sum -c (order76 dir): 12/12 OK. pins SUMS ef3bd922… 10/10 OK.

## Gates (claim → audit)
- RG76a ingest PASS → CONFIRMED (verbatim=pin, cmp identical).
- RG76b Zwegers→H_s, not C → CONFIRMED, consistent with pin wording.
- RG76c residual OPEN → CONFIRMED; no proof authored; no false close.
- RG76d ABSENT → CONFIRMED; data/ holds only 3 .md (verbatim + 2 STREAM); no residual_slash values, scripts, CSV/JSON; consistent with SF-W7-1.
- RG76e G1 OPEN≠ACCEPT; Ξ HOLD; GATE 640da80d binds → CONFIRMED.
- RG76f T1–T4 no new material → CONFIRMED.
- Verdict Bridge PARTIAL; READY NO → CONFIRMED. No Bridge YES anywhere (only hit: pin's "Does not authorize Bridge YES").

## Invent-ban / Cat
Cat A; invent-ban stated in PREREG and honored: no residual_slash closed form or numbers; quote in RESULTS matches pin content.
PREREG-before-RESULTS: PREREG.sha256 + RESULTS citation OK; mtimes 23:20:07.059 vs .063 CDT (same-second, ordering by hash citation only).

## Soft flags
- SF-W7-3 avoid-mix: CLEAR — no reference to Closure / heavy-daily / _git_v8 / self-audit / 2026-08 trees in order76.
- SF-76-1: PREREG.sha256 path is "order76/PREREG.md" (must -c from BRIDGE_C_35/, not order76/). Cosmetic.
- SF-76-2: STREAM_PRIOR (order75) stamped "~23:25 CDT", later than order76 stamp 23:20 CDT. Timestamp hygiene only.
- SF-76-3: order75 SUMS now 14/16 live — ../STREAM_IDLE_LOCAL.md and ../pins/SHA256SUMS FAILED due to expected forward drift (live files superseded by order76 STREAM and pin addition). order75 integrity intact via order76's bound STREAM_PRIOR 949647bf and pinned SUMS ef3bd922. Not a FAIL of order75 results.
- SF-W7-1 carried (no recovery data) — unchanged.

## Open set
residual-C law (δ_W7≡0 ∀x) OPEN; RG76d ABSENT pending written residual_slash data; G1 OPEN≠ACCEPT; Ξ HOLD; T1–T4; W-PO-2 (narrowed), W-PO-3, W-NL-1/2 OPEN (nonlocal untouched).
Blockers: none for Local formal LOCK of order76 as document/extract.
