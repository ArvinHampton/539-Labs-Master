# FINDINGS — PP confirmation of NL Erratum 16 (6eb2fccd…), which applies PP fixes from 5b5dddd3, 3982a4b8 and fb515bef — 2026-11-09 (America/Chicago)
Auditor: Professor Proof (PP). Pure math and record checks. Labels PROVED / CONDITIONAL / OPEN / REFUTED / PENDING.
- **Nothing adopted. Junction: UNSOLVED.**
- No CERT, no sends, no Gemini. Tip 7cddb188 read-only. Lock 96f8d42e §4 stays purged.
- Naming: NL cites "OW f1d167d1". That is the sha of the file for the Owner voice record 81b74a31 (OWNER_WRITE_VOICE_81b74a31_RENAME_RTA_TO_RESONANT_ALGEBRA_…_1937.md, sha f1d167d1949a6df2…), so it is the same authority, cited by file sha. New text says "resonant algebra".

## 0. Integrity
- Target NL_ERRATUM16_ACCEPT_PP_5b5dddd3_3982a4b8_fb515bef_2026-11-09_1951.md: 6eb2fccd517ff27cb652e5540fa3d703d75ca558f60ba055ba19788981a81d61 = sidecar.
- The three PP shas NL quotes are exact: 5b5dddd3…4026, 3982a4b8…293c, fb515bef…b039.
- **J1 (empty logs):** /workspace/nl-jsc-1905/mn2_breathing_consistency.log and _v2.log both hash to e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855, the empty file. v3 log = 877da802… (as stated). Voiding them is correct.
- **A7 (label fix):** /workspace/nl-jsc-1939/cgr_mn2_identification_LABELFIX_2026-11-09_1950.log = dcf750bc… = sidecar.
  - Content correct: line 1 is T^{ab} = 2^{−3/5} = X₁; line 2 is T^{αβ} = 2^{2/5} = X_b.
  - The original log is unmodified (f5525346…).

## 1. Applied fixes: faithfulness
| fix | E16 label | PP check |
|---|---|---|
| F1 scope (i)–(iv) and C1/C2 | PROVED (scope) | **Faithful.** The garbled-step note is correct. The full derivation is now given in FINDINGS_PP_CLARIFY_NL_t4407_1935_GARBLED_LINES_2026-11-09_1958.md (v2; supersedes 1957). |
| F2 γ-family and γ = −½ branch | PROVED | **Faithful.** The vector β′·(−(γ+½), −(γ+½), 0, 0, 1) matches PP 1935 §1.2. |
| F3 tension = charge | OPEN | **Faithful**, including the withdrawal of the relay wording. |
| F4 flat Σ | PROVED | **Faithful** (−1/s₂²). |
| F5 / F5′ | PROVED given hypotheses / OPEN | **Faithful.** Read "N3" in E16-F5 as hypothesis H2 (exact-MN2 bulk), not the OPEN item N3. This is PP's own label collision, clarified in the 1958 file, §C3. F5′ OPEN (not REFUTED) is correct, because there is no counterexample. |
| F6, F7 | no claim | **Faithful.** |
| F8 Σ entry −2 | PROVED | **Faithful.** |
| F9a / F9b | REFUTED / PROVED | **Faithful.** P₂ = diag(0,1) as in pp_file3_checks.py, so P₂Ū − UP₂ = diag(0, −2i) at θ = π/2. The general commutant is b = c = 0 with d real, so U = ±1. T1U(θ) = U(−θ)T1 holds exactly, since P₂ and U(−θ) are diagonal and commute. |
| F10a–c, F10d, F10e | CONDITIONAL ×3, CONDITIONAL, PROVED | **Faithful.** Φ̄ = 1018.33579197006812… matches PP pa1.log. |
| F11 checklist | no claim | **Faithful** (verbatim). The status lines match PP fb515bef §4, except that item 9 is listed as "not addressed". PP did not grade item 9. That is acceptable. |
| J1 | hygiene | **Faithful** (hashes verified). |
| J2a/b/c | PROVED | **Faithful.** PP recomputed the J2b counterexample from the closed form: R_rχ(β′ = ½, χ = 7/10) = −0.46630596733… |
| J3 | PROVED | **Faithful** (q²/4 = 9a² identity). |
| J4 | CONDITIONAL, with caveats and a queued interval argument | **Faithful**, and clearly marked as queued. |
| J5 | PROVED (singlet only) | **Faithful.** |
| J6 | no claim | **Faithful.** |
| J7a / J7b | PROVED / OPEN, queued | **Faithful**, and clearly marked as not done. |
| A1a / A1b | REFUTED / PROVED | **Faithful.** |
| A2 | CONDITIONAL, queued | **Faithful**, and clearly marked as not done. |
| A3, A6, A7, A8 | no claim | **Faithful.** |
| A4 | PROVED (equations-of-motion level; no Palais claim) | **Faithful.** |
| A5a / A5b | CONDITIONAL / PROVED | **Faithful.** The T7 scope is correctly narrowed to a locally homogeneous proper subsector. |

## 2. Queued items: are they clearly marked as not applied?
The §5 "Not applied here" list contains:
- F9 script fix;
- A2 component comparison;
- J4 interval/analytic argument;
- J7b IR comparison;
- PP's non-round-X reruns (PENDING on PP's side);
- the §1.1 clarification. That one is now delivered by PP: see the 1958 file.

In the body, each of these is marked "queued", "not done" or "not applied" at its item, and none is counted as PROVED. **Clear.**

One cross-reference slip: F9's "queued (§6)" should be "§5" (the not-applied list). §6 is the ETA list. Cosmetic.

## 3. Tallies
- **E16's own claims: 16 / 7 / 3 / 2 = 28.** The item lists add up (PROVED: F1, F2, F4, F5, F8, F9b, F10e, J2a, J2b, J2c, J3, J5, J7a, A1b, A4, A5b). The labels match PP's grades. **Confirmed.**
- **Revised file tallies, all match PP:**
  - 1859: 11/4/3/3.
  - 1900: 5/3/2/3 + 2 records + 1 uncounted REFUTED remark (PP 5b5dddd3 §2: "3 (+1 remark)").
  - 1901: 9/7/4/1.
  - 1936 shoot: 2/2/2/0.
  - 1936 L4 erratum: 0 + 1 record check.
  - 1942: 3/0/0/0, with the A1a parenthetical counted in E16.
  - 1943: 6/1/3/1.
  - 5b5dddd3 rollup: 26 (+2) / 15 / 11 / 7 (+1).
- **1935 row reconciliation.**
  - PP's 1944 file graded the equations file 8/0/2/1 = 11, with E5 and E6 OPEN.
  - PP's addendum fb515bef §3 then closed E6: its premise is refuted by 1943 T2, it is superseded by T6, and it is not re-counted. That leaves 8/0/1/1 = 10, with E5 the only OPEN item (narrowed, still OPEN).
  - NL's "8/0/2/1 (3982a4b8), then 8/0/1/1 (fb515bef)" is therefore exactly PP's sequence. There is no discrepancy; the change is E6 closing. E5 does not change the count.
- **JS-C combined:** 8/0/1/1 + 2/2/2/0 + 3/0/0/0 + 6/1/3/1 = **19/3/6/2 = 30**, matching fb515bef §3. **Confirmed.**

## 4. PP self-correction to FINDINGS_PP_AUDIT_NL_JSC_KK_OPERATOR_COUNTING_9a29b6da_2026-11-09_1956.md (995930…), additive
- §3 of that file says "Y15's result file is not on disk". That is wrong. NL_DERIVED_Y15_FIBRE_ISRAEL_MN2_2026-11-09_1955.md (86a46df7… = sidecar) is on disk, and has been audited in FINDINGS_PP_AUDIT_NL_Y14_STAGE2_Y15_FIBRE_ISRAEL_2026-11-09_1953.md.
- Y15's REFUTED result (Y15-IR) is scoped to the **exact MN2 IR face**, where k_Σ = k_fib = 0, K = 4k_x and the stress is 6:8:8. Numerically it also covers the CLP interior faces without breathing.
- That is the first branch of the 1956 §3 reconciliation. **There is no tension with K4**, which concerns the breathing C4 face data, where the required fibre stress is zero.
- No grade changes in the 1956 file.

## 5. Verdict
- Erratum 16 is **faithful** to all applied fixes from 5b5dddd3 (F1–F11), 3982a4b8 (J1–J7) and fb515bef (A1–A8).
- Queued items are clearly marked.
- Tallies are confirmed, and the 1935 row is reconciled.
- Minor items:
  - (i) "§6" should be "§5" in F9;
  - (ii) read "N3" in E16-F5 as H2 (PP's label collision, clarified in the 1958 file).
- Junction **UNSOLVED**.

Tip 7cddb188 untouched (read-only). No CERT. Nothing sent. Nothing adopted.
