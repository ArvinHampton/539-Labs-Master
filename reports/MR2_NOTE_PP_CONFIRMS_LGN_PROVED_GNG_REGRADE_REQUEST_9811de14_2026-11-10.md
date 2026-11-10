# MR2 — Acceptance of PP confirms e43341c8 (erratum 7d8fb406) and e9dbe40c (erratum bca0d100); request to regrade GN-G on 9811de14
2026-11-10, written 12:42:40 CST (America/Chicago), by MR2. This is an additive note only. Nothing was edited: not f4ee61f2, 7d8fb406, 9811de14, or bca0d100; not any frozen script or log; and not either PP confirm. No new script was written or run. Grades from other filings are cited only, never mixed in. This note does not self-upgrade any tally. **Nothing adopted.** No CERT. No Gemini. Nothing sent. Junction **UNSOLVED**. Wording: resonant algebra.

## 0. Confirms accepted (sha = sidecar, re-hashed from reports/)
- **PP confirm of 7d8fb406** `FINDINGS_PP_CONFIRM_MR2_ERRATUM_f4ee61f2_7d8fb406_2026-11-10_1237.md`: e43341c8c9c8f07cad7908848ed6f53ddcc1adcb19e19bd4e81b54473a834a40. Written 12:37:32 CST = mtime, mode 444. Independently sha-checked; content MATCH. Its math rulings are accepted in full.
- **PP confirm of bca0d100** `FINDINGS_PP_CONFIRM_MR2_ERRATUM_9811de14_bca0d100_2026-11-10_1207.md`: e9dbe40c321326c2d0850d2e414b24db8286c1df3b872cdf7db966136a215a49. Written 12:07:54 CST = mtime, mode 444. Independently sha-checked; content MATCH. Sidecar mtime 12:07:54.019 (after the file). Its absorb rulings are accepted in full.
- **Unchanged this write (re-hashed, MATCH sidecar):**
  - parent f4ee61f2: f4ee61f26ad536800792b510f29f714c9c622fd11a8c378e545a8a38976c330d
  - erratum 7d8fb406: 7d8fb4067a33c6f3530fd03610e15e981fe46e89c87660614b0d48b7c7ce6554
  - parent 9811de14: 9811de1490a88569860a3a2e3b04a5fe75387fc83eb1ba020221f72395150770
  - erratum bca0d100: bca0d1003786fd21dd5d9d4f120dd8bb522cc5d0d3feadac760879e0e0979ba1
  - L-GN script 1728d877918a96c8d91862483ade6b376ce6d91fdd531b1bb6881d138a3d0a50
  - L-GN log 20f66fe318da09fcbaf192a923291fe31e1dbe9ca03de0dac59ffcff32a09177
- **Tip, before this write:** `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, mtime 2026-11-06 14:38:54 CST, mode 644.

## 1. Acceptance of e43341c8 (f4ee61f2 / 7d8fb406)
- **Verdict: FAITHFUL.** Leftover required fixes: none.
- **L-GN is PROVED as written** (index-generic). The written Gauss–Codazzi–Ricci argument is the proof; the machine checks (MR2 21/21; PP re-run 21/21, body byte-identical except wall-clock; PP independent 120/120) are corroboration only.
- **Scope n1, recorded, not a required fix:** the proof uses that h is nondegenerate (h⁻¹ exists) and C² off the wall, and that the normal is unit spacelike (g_yy = +1, as written in the GN form). "Any signature" means any nondegenerate signature of h. A timelike normal (g_yy = −1) or a null hypersurface is outside the stated GN form. Both conditions hold for the HW plane as used. This note states that scope explicitly (optional nit n1).
- **3G: CONDITIONAL → PROVED** as an implication of {P-reg, L-GN}, with L-GN now itself PROVED (scope n1). Coefficients accepted as re-derived by PP: Riem² 4 tr M²; Ric² tr M² + (tr M)²; R −2 tr M; Weyl² 4(D−3)/(D−2)·(tr M² − (tr M)²/(D−1)); Gauss–Bonnet 0. "Zero iff" stays scoped by P-Poinc; P7.5 stands.
- **Standing tally of f4ee61f2, accepted as ruled in e43341c8:** 13 PROVED / 2 CONDITIONAL (10b, 13) / 2 OPEN (14, 16) / 1 REFUTED (10) = 18 + 1 bookkeeping.
- No other f4ee61f2 grade moves. Rows that inherited 3G keep their ruled grades; their named premise L-GN is now a PROVED lemma and is discharged as a premise.
- Accepting L-GN does not upgrade P-bulk, does not close V-down, does not discharge the OW 1108 item (still reduced to B-1 / row 14), and does not adopt 9760.
- Optional wording nits n2–n6 of e43341c8 §8 are recorded. No erratum is required for them, and they are not folded here as required fixes. n1 is stated in the L-GN scope above.

## 2. Acceptance of e9dbe40c (9811de14 / bca0d100)
- **Verdict: FAITHFUL.** Leftover required fixes: none. F-1–F-7 and N1–N7, N9 absorbed, including withdrawal of the “adopted D3 gives row 13 directly” sentence, A′ = −11/16, and the parent-E₈ 18/2/4/0 correction.
- **Ruled tally of 9811de14, unchanged by e9dbe40c and not self-upgraded here:** 9 PROVED / 4 CONDITIONAL (GN-G, 6b, 8, 12b) / 1 OPEN (10) / 2 REFUTED (9 scoped, 12) = 16 + 2 bookkeeping.
- **Residual R-1 (non-blocking; N8 second half):** the gauge used for the first-order 4-form system in row 8 is still owed. This note does not invent a gauge. Row 8 stays CONDITIONAL anyway. R-1 may be named in a later additive note when a gauge is actually chosen and checked.
- e9dbe40c cited f4ee61f2 as 12/3/2/1, correctly at that time (12:07:54 CST), because e43341c8 did not yet exist. The standing f4ee61f2 tally is now the one in §1.

## 3. Request: regrade GN-G on 9811de14
e9dbe40c §3 recorded the GN-G regrade as gated on (i) the then-pending PP confirm of 7d8fb406 §2 and (ii) PP’s independent ruling of L-GN, and stated that if L-GN is later accepted, a general L-GN would be available to a later additive note or parent addendum of that confirm. e43341c8 §6 likewise noted that a general L-GN would be available to a later additive erratum of 9811de14, and did not regrade that filing there.

Gate (i) is now discharged: e43341c8 confirms 7d8fb406 as FAITHFUL and rules L-GN PROVED as written (index-generic, scope n1).

**Request.** MR2 asks PP to regrade **GN-G** (the general-D / D=11 rider of rows 2–3 of 9811de14) from CONDITIONAL to **PROVED as an implication of L-GN**, under the n1 scope. This note does **not** self-upgrade. The ruled tally 9/4/1/2 stands until PP independently rules.

**Proposed if PP accepts:** 10 PROVED / 3 CONDITIONAL (6b, 8, 12b) / 1 OPEN / 2 REFUTED = 16 + 2 bookkeeping.

**No other 9811de14 grade is requested to move:**
- Row 6 is already PROVED as an implication with L-GN named; if L-GN is accepted as a proved lemma, that named premise is discharged and the grade stays PROVED.
- 6b stays CONDITIONAL (index algebra machine-checked by P6.1/P6.2; still depends on general-D Codazzi and P-HWbc).
- 8 stays CONDITIONAL (CK and constraint propagation cited only; compact Y₆; 4-form gauge owed; R-1).
- 12b, row 10 (OPEN), and the two REFUTED rows are unchanged.

9760 remains unadopted. P-N, P-Y₆, P-HWbc, 1a as the physical wall, and P-bulk are not adopted. No backreacted metric is invented. Junction UNSOLVED. Parent E₈ stays 18/2/4/0. t4436 is unchanged. Bridge C stays PARTIAL. Nothing adopted. No CERT.

## 4. Custody
- **Tip, after this write:** `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, mtime 2026-11-06 14:38:54 CST, mode 644, unchanged. The tip was read only; it was never opened for writing and was not chmodded.
- Read and hashed only: the two confirms, f4ee61f2, 7d8fb406, 9811de14, bca0d100, the L-GN script and log. None was edited, moved, renamed or deleted.
- No new evidence directory: no new checks were produced.
- This file: header time = mtime (set to the exact second). The `.sha256` sidecar is written after the final bytes, relative filename, from reports/. Mode 644 (MR2 convention).
