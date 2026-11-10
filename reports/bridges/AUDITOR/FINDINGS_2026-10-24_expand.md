# AUDITOR — FINDINGS 2026-10-24 (expand pass)
Pass time: 22:09–22:20 CDT (America/Chicago). Read-only on all sources. No PASS/FAIL was altered.
Previous pass: [FINDINGS_2026-10-24_priority.md](FINDINGS_2026-10-24_priority.md). This file lists only this pass's issues, plus the status of the priority items.
Tags: CHAT = agent notes, gate notes or briefs. PAPER = tex/PDF/Lean or the hashed RESULTS corpus.

## A. Re-audit of order58 amend, order59 and order60 (urgent block)

### [resolved] Priority blocker: order58 RG47a PASS
- Path: BRIDGE_C_35/order58/RESULTS.md (amended 22:10:15 CDT).
- Evidence: the RESULTS now reads "RG47a: FAIL under the preregistered relative criterion". The strict statistic is 0.17 against a 1e−6 bar, and the log shows resid_rel_strict = 0.1746. The Cat A alternative branch is explicitly marked not met. The cancellation explanation is labelled a post-hoc Cat B disclosure.
- Conclusion: **no RESULTS file now claims RG47a PASS.** The first version of RESULTS.md, before the amend, did claim it; that version has been superseded.
- RG48 is recorded as "NOT EXECUTED AS PREREGISTERED (no Cat A verdict)". The Milgram enumeration is classed as post-PREREG Cat B. This resolves the priority warning on RG48.
- Hashes: PREREG (75ebf419…), RESULTS and all 13 SHA256SUMS entries verify OK. This resolves the priority warning on the missing hash chain.

### [note] order58: data/rg47a.json still contains "RG47a_PASS": true
- Path: order58/data/rg47a.json and logs/rg47a.log.
- Claim vs evidence: the machine-readable flag says PASS, while RESULTS says FAIL. RESULTS line 2 discloses this and voids the flag.
- Fix: add a sidecar file such as data/VOID_FLAGS.md, or make sure no downstream parser reads the flag. Do not edit the hashed data.

### [note] order59: RG49 and RG50 hashes and verdicts are consistent
- Hashes: PREREG (bec0231d…) OK; all 11 SHA256SUMS entries OK.
- The a_H condition is documented in PAPER: order59/PREREG.md:14–17. I verified it independently:
  - The sha256 values of em.py (5fb526b5…), em_check.py (a41af336…) and closed_forms.py (78f3f8a4…) are byte-identical between heavy-daily/2026-10-17-P_s-structure and _git_v8_unpushed_clone.
  - The git blobs b0f34801, 3c8f9683 and 78ceea29 are present in `git ls-files -s`.
  - The order59 copy of scripts/em.py has the same hash.
- The condition is MET as documented. RG50 PASS matches the RESULTS numbers: |Δ| = 3.9e−31, drift 1.5e−5 < 1e−3, and the K1 and K2 controls fail.

### [note] order59 RG50 has no Category label in RESULTS
- Claim vs evidence: ORDER60_BRIEF.md:6 (CHAT) says "RG50 PASS (a_H wire; Cat B radical pending symbolic)". order59/RESULTS.md:9 (PAPER) gives no Cat label for RG50.
- Fix: add a Cat label line to RESULTS in the next order's addendum. Do not edit the hashed RESULTS.

### [note] order60: verdicts match PREREG and data; PREREG.sha256 uses a repo-relative path
- Path: order60/PREREG.sha256 lists "order60/PREREG.md", so `sha256sum -c` fails when run inside order60/. Run from BRIDGE_C_35 the hash 28905ae9… is OK. All 6 SHA256SUMS entries are OK.
- RG47b: SKIP. This follows the rule in PREREG:10 (i PASS; ii and iii skipped).
- RG47c: PARTIAL. This follows the rule in PREREG:17. The baseline excess is 75 and R_Q1 is 49, a reduction of 26 ≥ 10. The control reduction is 3, and 26 > 3. Neither is closed. The gate (75 / 148 / 150) is reproduced.
- The R_both near-closure (excess 2) is correctly labelled descriptive and not a verdict.
- PREREG mtime 22:09:01, log 22:09:13 CDT: hashed before the run.

## B. Orders 50–55

### [warning] order55: RG45c-2″ PASS comes from a PREREG_b hashed after the RG45c-2′ FAIL and after post-hoc diagnostics
- Path: order55/PREREG_b.md and order55/RESULTS.md:6.
- Evidence (mtimes, CDT):
  - rg45c2p.log, the FAIL run: 21:30:31
  - posthoc_j50.log and posthoc_j50b.log: 21:35:19 and 21:35:37
  - PREREG_b hashed: 21:35:58
  - rg45c2pp.log, the PASS run: 21:48:13
- "Hashed before run" is literally true. However, the change (exact λ=0 detection) was designed after seeing which 4 cases failed. RESULTS does not label RG45c-2″ as a post-failure amendment.
- Fix: in the next addendum, keep RG45c-2′ FAIL as the primary preregistered verdict. Label 2″ as "post-diagnostic re-PREREG (Cat B provenance for the fix choice)".

### [note] order53/order54 SHA256SUMS use bare filenames
- Path: order53/SHA256SUMS (rg45b.py) and order54/SHA256SUMS (rg45c.py). Both fail to open under `-c`.
- The hashes match scripts/rg45b.py (e3f8e622…) and scripts/rg45c.py (10e8b7d4…), so content integrity is OK. The paths are broken.
- Fix: in a future order, regenerate the sums with scripts/ paths.

### [note] Orders 50–55: verdicts match the logs
- All PREREG hashes are OK.
- order50: no test was run (no logs or data). The c_k item is untested, consistent with G4 "no bound written".
- order51: R1a PASS and R1b FAIL.
- order52: RG44 PASS. rg44.json has T1–T5 true.
- order53: RG45b PASS; RG46 SKIP.
- order54: RG45c-2 FAIL. The log worst value is 1.386, and RESULTS gives 1.39.
- order55: RG45c-2′ FAIL (log 0.0155); RG45c-2″ PASS (log 6.8e−9).

## C. RTA Foundation Bound v11/v12 → order47–49

### [warning] order47 SHA256SUMS omits the script and data that v12 Prop 39.22 cites as its proof
- Path: order47/SHA256SUMS hashes only PREREG, RESULTS, NOTES, REPORT.pdf and logs/o47.log, and all of these verify OK. scripts/o47.py and data/o47.json are not hashed.
- Claim: v12 Prop 39.22 (src/partIII_inv_v12.tex:9–15) is labelled "(exact, computer-assisted)" and cites BRIDGE_C_35/order47/scripts/o47.py.
- Fix: hash o47.py and o47.json in a new order or addendum. Until then, the computer-assisted proof has no hash chain for its code.

### [warning] order48 and order49 have no SHA256SUMS
- Claim: v12 Thm 39.23 (xinv), widened to Λ via order49, and Remark 39.25 ("7·10⁻¹³ on 48 pairs", from order48) rest on these runs.
- Evidence: only PREREG.sha256 exists, and it verifies OK. The scripts, data and logs are unhashed. order50 is in the same state, but no test was run there.
- The content matches: o48.log gives a maximum of 6.97e−13 against "7e−13", and o49.log has H1–H3 true.
- Fix: add SHA256SUMS for order48 and order49.

### [note] Claim vs evidence checks for Prop MPi / Thm xinv: OK
- The tex for Prop 39.22 states conj(M)ΠM = 35Π and MM† = 35I, zero on 105² entries, with the controls M² = 35P and the 34I control rejected on 105 entries. This matches order47 RESULTS and o47.log exactly.
- "1052 entries" in the pdftotext output is an extraction artefact of 105² and not an error.
- The v11→v12 diff touches only the hypothesis widening, the H3 sentence and the 48-pair remark, as NOTES_v12 states.
- The Cat B numerics are placed in Remark (Category B) 39.25 and App. D o45, so the Cat labelling is correct.

### [note] Thm xinv's coverage of A2^lines rests on a code audit
- Path: order49 H1 ("β and x enter lines() only through ph() and period()") and H4.
- Evidence: the log records H4 as "follows from H2, H3b…", which is a derivation and not a check, yet it is listed as "PASS".
- The Cat A extension to A2^lines depends on the code audit being faithful to the written definition of lines().
- Fix: label H4 as "derived" rather than PASS. State in v13 that coverage of lines() is certified by a code audit.

## D. MAPS deep pass (ledger in [MAPS_LEDGER.md](MAPS_LEDGER.md))

### [warning] C10 status: is "FAIL (closed)" conditional on a CHAT-accepted Π?
- Paths:
  - BATCH2–7 RESULTS and C11_GRADING_ACCEPT/NOTES.md:9 (20:48) say OPEN.
  - DISCOVER_PI_RULE/RESULTS.md:9 (20:57) gives FAIL, Cat A, on Π*_max.
  - PI_MAX_PURSUE (21:01) says "C10 FAIL (closed)".
- Claim vs evidence: the C10 FAIL is an exact computation (539 segments, tests.json T2_segments = 539). But Π*_max is "a free extremal choice" (DISCOVER_PI_RULE PREREG:13). It was accepted only by an Arvin message (CHAT), which has no file in the corpus.
- Fix: record it as "C10 FAIL (Cat A computation) | Π provenance Cat B / CHAT-accepted". Add a superseding status row to MAPS RESULTS; the older OPEN rows are stale. This upgrades the priority note on C10/C11 staleness.

### [note] Π*_max, g and P_res: values verified; acceptance is CHAT only
- sha256(bytes([0,1]*269+[0])) recomputes to c2c26fda…8d87. This matches DISCOVER_PI_RULE/data/tests.json and PI_MAX_PURSUE PM1.
- C11: the S values [10, 12, 12, −13, −13, −11, −13, 13] in RESULTS match data/test.json. The block sizes are 68×3 and 67×5. Σg = −3 (268 +1 and 271 −1).
- The PREREG hashes of C11_GRADING_ACCEPT, DISCOVER_PI_RULE, PI_MAX_PURSUE and BATCH8 are OK.
- The acceptances ("Arvin 2026-10-24") are quoted in NOTES/PREREG, but no message file exists. Tag them CHAT.

### [note] E1–E3 have no definition in the MAPS corpus
- They are carried only as "OPEN", tracing to v12 Open problem 1 and order50. The "(E1)" in the v12 PDF is an unrelated cosine inequality in §8.
- The ledger records them as OPEN with the definition source absent. Fix: cite the defining file.

### [note] Vacuous, VOID and non-discriminating outcomes are labelled correctly
- C13 VOID (gate 297 ≠ 353), C19 PASS non-discriminating, C23 PASS vacuous, C24 PASS carrier-forced: these are labelled as such.
- C22 has a disclosed datum error (χ₁₄₀ transcription), and its FAIL is kept under the literal rule.

## E. Coordinator gates (CHAT vs PAPER)

### [warning] The G1 rejection and the G2–G4 acceptance exist only in CHAT/briefs; the hashed WRITTEN_CANDIDATES still lists G1 as "FOUND"
- Paths:
  - order57/WRITTEN_CANDIDATES.md:13 and :37 say "Explicit Ξ series — FOUND". The sha verifies OK.
  - The rejection appears only in ORDER60_BRIEF.md:7, order58 RESULTS addendum and order60 PREREG:9 / RESULTS:7, which are briefs or gate echoes.
- The G2–G4 citations to v12 were confirmed present in the PDF text: Thm 35.6 (13 hits), Thm 39.3, Thm 39.4, Prop 39.5 and §39.1 c_k.
- G1 itself carries caveats (a)–(e), including the BK 09-02 term-by-term identification FAIL.
- Fix: write a hashed GATES_2026-10-24.md listing G1 REJECT and G2–G4 ACCEPT written-only, with the rationale and the deciders. Do not edit the hashed WRITTEN_CANDIDATES.

## Counts (this pass, new)
Blockers 0 / Warnings 5 / Notes 12. Resolved from the priority pass: 1 blocker and 2 warnings (all order58).
