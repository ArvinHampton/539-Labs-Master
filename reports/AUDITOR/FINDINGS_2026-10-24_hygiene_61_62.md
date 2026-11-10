# FINDINGS 2026-10-24 — Hygiene verify + order61/62 cross-ref + order63 (Auditor, read-only)
Pass 22:15–22:17 CDT (America/Chicago). No verdict altered. No physics added. Source files were read only.

## A) Hygiene verification of the expand warnings
| Expand warning | Evidence | Result |
|---|---|---|
| order55 RG45c-2″ labelling | RESULTS.md:20 has an additive note: primary = RG45c-2′ FAIL (PREREG.md); 2″ PASS is post-diagnostic only (PREREG_b hashed after the FAIL); no numbers changed. SHA256SUMS_2026-10-24.md: 14/14 OK, RESULTS = 29a9957f…. The historical SHA256SUMS entry for RESULTS.md now FAILS, which is expected because the file was amended and the older SUMS was kept. | **RESOLVED** [PAPER] |
| order47 SUMS omits o47.py and o47.json | SHA256SUMS_2026-10-24.md covers scripts/o47.py, data/o47.json, the log, PREREG, RESULTS, NOTES, REPORT.pdf and the historical SUMS files: all 11/11 OK. The historical SHA256SUMS, data/SHA256SUMS and scripts/SHA256SUMS are also OK. | **RESOLVED** [PAPER] |
| order48/49 have no SUMS | Each now has a SHA256SUMS (22:14:00) covering script, data, log, PREREG, PREREG.sha256, RESULTS, NOTES and REPORT.pdf. order48: 8/8 OK; order49: 8/8 OK. Every file in both trees is covered. | **RESOLVED** [PAPER] |
| G1–G4 exist only in CHAT; WRITTEN_CANDIDATES still says G1 "FOUND" | order57/GATE_DECISIONS.md records G1 REJECT, which explicitly supersedes the "FOUND" wording for adoption. It records G2 and G3 as accepted with written-only or labelled scope and G4 as input only. GATE_DECISIONS.sha256 is OK (re-hashed at 22:15:34 after the order63 addendum). | **RESOLVED.** The record is now a hashed local record [PAPER-record of a CHAT-origin decision]. |

Hygiene notes:
- N-H1 (note), order55/SHA256SUMS: RESULTS.md now FAILS against the historical file. This is expected and superseded by the dated file. Fix: optionally add a one-line pointer in the old SUMS, or leave it as is.
- N-H2 (note), order55/SHA256SUMS_2026-10-24.md: the last line uses `order55/RESULTS.md`, a parent-relative path. It only resolves from BRIDGE_C_35/. Fix: drop it or make it relative; cosmetic.
- N-H3 (note), the GATE_DECISIONS.md header says the gates were "relayed via Auditor". The Auditor only audits and makes no gate decisions. Fix: change the attribution to "relayed via coordinator".

## B) order61 and order62
The full audit is already in FINDINGS_2026-10-24_order61.md. I re-ran a quick check: order61 SUMS 9/9 OK and PREREG OK; order62 SUMS 5/5 OK and PREREG OK. Verdicts match: RG47a-bis PASS, RG47d FAIL (34/2), RG47e FAIL (excess_proj 2 at w=1), RG48-Weil SKIP (ABSENT). order58 RG47a stays **FAIL** under its literal PREREG; the -bis result does not relabel it.

## C) order63 (BRIDGE_C_35/order63/), status: COMPLETE and VERIFIED
- Hashes: PREREG.sha256 OK (f8f4bbd7…593). SHA256SUMS 5/5 OK.
- mtime order: PREREG and its sha at 22:15:19, then RESULTS, data, log and SUMS at 22:15:34. Step 0 was non-numeric, scripts/ is empty, and no statistic was computed. This is consistent with the ABSENT branch.
- **RG47f: SKIP (ABSENT), consistent with the PREREG.** No written corner↔ρ_lab or Δ-type pairing was found. The search log lists s11_family.tex, order60–62, order7, order13 and MAPS BATCH4. The den 5,7 → ρ5/ρ7 link is explicitly NOT asserted. data/rg47f.json has numeric_test_run=false.
- N-63-1 (note): the PREREG scope includes `partII/*.tex` and "order55–62", but the log records only s11_family.tex and order60–62. Fix: append the grep hits (or zero-hit lines) for the other partII/*.tex files and order55–59 to the search log.
- N-63-2 (note), RG48 disposition:
  - order13 RESULTS.md and NOTES.md (PAPER) do contain "Route A: closed for every h (Category A)" and Lemma W. The W1 exact certificate passed (data/w1.json); order13 PREREG.sha256 is OK.
  - order13 predates RG48 and does not mention it. The equation **RG48 ≡ Route A Weil χ=±i track** is the Physicist's disposition, which is CHAT-origin.
  - That disposition is now recorded locally and hashed in order63 RESULTS.md (in SUMS) and in the GATE_DECISIONS.md addendum (sha OK). It no longer depends on CHAT alone.
  - Tag: the lemma is Cat A [PAPER]; the RG48 mapping is a gate decision [CHAT→hashed record]. Milgram stays Cat B.
- No blockers or warnings for order63.

## Counts this pass
Blockers 0 / Warnings 0 / Notes 5 (N-H1, N-H2, N-H3, N-63-1, N-63-2).
Expand warnings: **4 RESOLVED** (order55 2″, order47 SUMS, order48/49 SUMS, G1–G4). **Still OPEN: 1** (C10 OPEN-vs-FAIL under the CHAT-accepted Π*_max, MAPS).
