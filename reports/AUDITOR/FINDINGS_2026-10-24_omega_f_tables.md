# FINDINGS — Ω/F factor tables pin (Arvin t614u, chat lock)
**Stamp:** 2026-10-24 23:13 CDT (rev. 23:14 CDT — folds NL t614u ingest) · Auditor (soft flags only; PASS/FAIL untouched; LOCAL/NONLOCAL maps kept separate)

## Hashes (live)
- pins/OMEGA_F_FACTOR_TABLES_2026-10-24.md: c9c3b30df6576fd58cd65cec1d2072c12d8db7f222d781d1cb8c8904be048df2 — MATCH cited
- NONLOCAL inventory_check/OMEGA_F_FACTOR_TABLES_2026-10-24.md: c9c3b30d…8df2 — MATCH (identical mirror)
- pins/SHA256SUMS: 45e696ff9d896bf8f2d5ae1765d3db92ed4721c1cfdc9159953e6b4c8313f31a — MATCH; `sha256sum -c` **8/8 OK**
- Parents unchanged: CONSOLIDATED_PIN_LEDGER ffc93ae4…bb6c OK; G1_REOPEN_AND_S_B1_WRITINGS 6c66dbc0…2ab2 OK; a6dfcec4…bf32 = **P_orth_Omega_F_total_2026-10-24.md** OK
- NONLOCAL inventory_check/SHA256SUMS (live, 23:13:02 CDT): fe7843cb4366b58947c07258cb9b0ca380c36cc4f7389b22f71e8489c5fb47e5 — MATCH; `sha256sum -c` **11/11 OK** (supersedes first-pass c0c40e0f… 10/10).
- inventory_check/FINDINGS_OMEGA_F_TABLES_T614U_CAT_B.md: a04c98caad2b708cf02e60a66e34805cdec632e96594dd6a7f3165eaba37440b — MATCH, listed in SUMS OK.
- inventory_check/STREAM_IDLE_WRITTEN.md: 6a9fd41c0e3c5114d147831bf9a377e722c87510212eee103dbb92757c5213ff — MATCH (supersedes a74994ec…; prepended t614u section, history retained).
- Hunt W_PO2_OMEGA_F_TABLES_HUNT ff5ff7f0…693b OK.
- NL1 PREREG untouched: PREREG.md 495c7944…de52e and result.log 85bd2f63…dabb match PREREG.sha256/RESULTS.sha256 (mtime 22:53 CDT). Prior audit FINDINGS_wpo2_hunt c23861c5…53a9 unchanged.

## Written vs ABSENT
- **Written:** Ω₁₁D packaging Ω₀·f_warp(k)·f_curv(K)·f_b(b)·Φ_flux(Φ); Ω channel table (4 rows: warp, curvature, residual b, flux Φ); F_total component table (5 rows: Coulomb^rel, SO, Torsion, Flux, Leak) with explicit forms, each "Scales by Ω₁₁D".
- **Still ABSENT / placeholder:** f_warp(k), f_curv(K) — "Functional form pending explicit compactification"; f_b(b) given only as "Residual packaging scale" (no form); Φ_flux only "Locked to 539.9 s period" (no form); Ω₀ numeric — pin: "Do not invent Ω₀ or f_* numerics beyond what is written here."
- So the *table bodies* now exist (filling the structural ABSENT from hunt ff5ff7f0…), but the Ω channel cells remain placeholders.

## Cat A/B · invent-ban · provenance
- Cat: "Continuum remains Category B" (stated twice). No Cat A elevation found. CLEAN.
- Invent-ban: Auditor added no physics. Pin forms are author-written; no numerics invented. CLEAN (no audit judgment on physical validity).
- Provenance: chat-lock only (t614u). No Drive/paper hash cited. Pin itself: "Drive/paper original required to clear W-PO-2/3 chat≠paper hygiene (W-PO-3 absolute until attach)."
- Local claims: "No local Bridge / G1 / Ξ / residual-C claims from this pin." No order74 touch → W-74-1 not re-audited.

## NL ingest claim checks (a04c98ca…)
- Cat B chat-lock ingest only: VERIFIED ("Label: Cat B continuum (chat lock). Not paper Cat A."). No Cat A elevation.
- W-PO-3 OPEN: VERIFIED (ingest + STREAM both say OPEN until Drive/paper).
- No invent: VERIFIED — ingest quotes channel table as written, marks f_warp/f_curv "pending", refers F_total forms to pin sha rather than recopying; no Ω₀/f_* numerics.
- No NL2: VERIFIED ("No NL2 Z=1–118 fit (periodic_table_539labs.json still ABSENT)"); no NL2 prereg dir exists.
- NL1 PREREG untouched: VERIFIED by hash (above).
- Maps separate: VERIFIED ("no local G1 / Ξ / P̂_orth / residual-C claims").

## Dispositions
- **W-PO-2: OPEN (narrowed), under chat≠paper.** Table-body ABSENT gap is filled (Written, hashed c9c3b30d…), Cat A/B hygiene clean. Remains open because (a) Ω channel cells f_warp/f_curv/f_b/Φ_flux and Ω₀ are still placeholders, and (b) the pin's own text says Drive/paper is required to clear W-PO-2 chat≠paper hygiene. Narrowed scope: {f_* functional forms + Ω₀} + paper attach.
- **W-PO-3: OPEN** (no Drive/paper hashed evidence; pin agrees).

## Soft flags
- N-OMF-1: F_total table header says "locked Codex" while provenance is chat t614u — mixed-provenance label; clarify which is source of record.
- N-OMF-2: Pin ties W-PO-2 closure to paper attach; coordinator framed W-PO-2 as auditor's call. Followed the pin text (stricter); not reconciled further.
- N-OMF-3: Φ_flux "locked to 539.9 s period" — period stated, functional form not; treat as placeholder.
- N-PIN-CONF-1, N-T604U-2 carried (still extend W-PO-2).

- N-OMF-4: ingest posture "W-PO-2 table-body gap addressed by author write (chat)" — accurate for bodies only; not a closure. Consistent with this disposition.
- N-OMF-5: STREAM history retains older "NL1 OPEN" lines under "Standing posture" while header says NL1_STRUCTURAL_ACCEPT — history-section staleness only; no verdict change.

## Open set
W-NL-1, W-NL-2, W-PO-2 (narrowed), W-PO-3, W-PIN-3 (watch), S-B-1 (+N-SB1-1). Closed: W-PO-1, W-74-1. G1/S-B-1/W-NL-*/W-PIN-3 verdicts untouched.
