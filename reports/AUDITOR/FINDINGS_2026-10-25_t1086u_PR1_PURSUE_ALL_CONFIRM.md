# FINDINGS — t1086u PR1 PURSUE ALL CONFIRM — 2026-10-25 ~20:00 CDT (America/Chicago)
Auditor · CONFIRM-only · invent-ban ON · residual-C LOCKED (read-only, not edited)

## Verdict: MATCH-with-SF

## Input shas (verified)
- Report PR1_PURSUE_ALL_t1086u_2026-10-25.md: ae375df25df11979d66b461cc9fd2d0dd82fe3ec4ba4ac5f5edb70936ece3b86 ✔
- Catalog rev.13 /workspace/obs-data-PR1-HEPP-QM-GR.md: 67ee59e844b9a602c26509fd8e726c816116fa2ab81d9cfda87868ee8c27bb6b ✔
- Item-3 OWNER_WRITE_ITEM3_ER_EPR_star_throat_2026-10-25.md: 5bd5a5e15c287fdb1fd60fb773ad3315304b6924c586c89902322ff3c25eeca7 ✔ (matches its .sha256 sidecar)
- t1078u OWNER_WRITE_NL_Q2_Q4_Q7_Q8_Q10_t1078u_2026-10-25.md: 3cad20f68bd6bf817bf40e2fc3567f650b6e53d4323aafb573d5a64c71815ea3 ✔
- Prior PR1 FINDINGS t1055u: 11445aaa6fd89a14fd04cec315f4f0e9e11fb8a046d20a33a3137aefdbbfdb5b ✔
- residual-C tip: 492fb3ac95c20e9117594639eb5947c90785a09e93da8301d6e83980c490a6fa ✔ untouched

## Baseline
No backup of rev.12 e8058aa9… found. Diffed against the backup that exists, obs-data-PR1-HEPP-QM-GR.pre-lock-retag-da0097d0.md (da0097d0…, rev.11). So the diff covers rev.12 plus rev.13. The rev.12 parts match what t1055u FINDINGS 11445aaa… already CONFIRMED (LOCK pointer, W-D4 annotate, post-LOCK footer).

## Per-expect
1. W3.2 star throat Written-backed — PASS. Item-3 line 16 quote matches the report and catalog §2F(d) word for word (chat 7ca21548). Forcing energy, mechanism and rates are kept not Written.
2. t1078u labels LABEL WRITTEN / mechanisms ABSENT-with-Owner-hold — PASS. t1078u lines 8–9 (gaps 2/3) and line 31 (ABSENT-with-Owner-hold) match §2F(b)/(c).
3. OPEN→constraint map — PASS. Added to §2F with pointers only to existing §2A/§2B/§2D/§2F rows. No numbers.
4. LVK Gaps deepen list only, no new [V] — PASS. Gaps §4 item 7 is prose. The 2 extra "[V" tokens in the diff are prose references ("no new [V] rows", "already [V5]"), not new rows.
5. residual-C 492fb3ac… untouched — PASS.
6. invent-ban ON; Bridge PARTIAL; READY NO; not Cat A — PASS (report header, changelog, footer).

## Measured-row stability
Changed lines are only: header, §1 pointer, §2F annotations, §2F/W4 summary, changelog, Gaps §4.6/§4.7, footer. No measured HEPP/QM/GR row changed.

## Soft flags (clerical)
- SF1: No rev.12 e8058aa9… backup on disk. The baseline is two revisions back (da0097d0…).
- SF2: In the §2F DE-transfer bullet, "Photon→torsion-hole strike dynamics still NEED WRITE" is left as is. This is consistent: only the mechanism is held, and the label is Written. It is wording drift next to the "LABEL WRITTEN" tag.
- SF3: Cites are truncated (a6836958…, d299708f…, bdc1d8b0…). The report's self-sha is left to the parent message. The "primaries not re-fetched" note is fine.
