# AUDITOR — ADDENDUM 2 to the full since-v17 report: files after the Addendum 1 scan — 2026-11-09

Role: Auditor, the audit-only keeper. Written Mon 2026-11-09 ~18:29 CST (America/Chicago). Additive and created exclusively (noclobber), with a .sha256 sidecar.

Earlier files (not touched):
- Parent report AUDITOR_FULL_REPORT_ALL_ADVANCEMENTS_SINCE_V17_2026-11-09_1816:
  - .md b3933d665226d703c5b46519da65698b3cc142ca6cbcb9724080e158604a5350
  - .pdf 49c573d5d71d35ca5d5fb4d7b032de3f76948ed6afb882b6eea7b5230003b078
- Addendum 1, AUDITOR_ADDENDUM1_FULL_REPORT_SINCE_V17_POST_CUTOFF_2026-11-09.md: 2d5197c1dfe3307a2fda59107e0e856ac5370b9a90a5ada65ebb01766422bf2b

Window covered:
- Files in /workspace/quantum-comp/ and /workspace/539-labs/ that landed after the Addendum 1 scan (~18:26:05 CST).
- Rescanned through **18:28:10 CST**. The Auditor's own files are excluded.

Labels: PROVED / CONDITIONAL / OPEN / REFUTED. Grades are **PP's own**. Hashes only. No CERT, no Gemini, nothing sent outside.

## 1. Supersession notice
- Addendum 1 §3 and §4 say: "PP audit of NL Y16 (7270a6b3) — still NOT FOUND (scratch suggests in progress)".
- **That statement is SUPERSEDED. The PP Y16 audit is now FOUND** (§2a below, mtime 18:25:34 CST). It landed seconds before Addendum 1 was written, after its scan.
- Addendum 1 is not edited. This notice is the correction.

## 2. New files (the only two in the window)
| # | time (mtime, CST) | file (reports/) | sha256 | sidecar |
|---|---|---|---|---|
| a | 18:25:34 | FINDINGS_PP_AUDIT_NL_Y16_TRR2_WALL_STRESS_AND_ERRATUM12_2026-11-09_1826.md | 149be02a794917d92f36c7a2383bbb4eb74623bb4f7b57dd111ad09f73ba7293 | MATCH |
| b | 18:26:39 | FINDINGS_PP_CITATION_SCOPE_REGRADE_OW_36683379_NL_ERRATUM13_MR2_FLAGS_2026-11-09_1832.md | c74b5a2d67c29d262977692dde59e83ee6dcd04af5bb4c4a55006527386f3abc | MATCH |

- Header times "1826" and "1832" do not match mtimes 18:25:34 and 18:26:39. This is the recurring header/mtime lag.
- The rescan through 18:28:10 found **no other files**:
  - no new Owner write after c7795d6e (18:16);
  - no MR2 symbolic/global-curvature .md;
  - nothing in /workspace/539-labs/.

### 2a. PP audit of NL Y16 (7270a6b3) and NL erratum 12 (53d4f945)
- **Integrity (I1–I5, PROVED):**
  - Y16, erratum 12 and NL's y16.py / y16_1812.log equal their sidecars.
  - PP's rerun log is byte-identical to NL's (fa443be5…; PP scratch sidecar MATCH).
  - Tip MATCH.
  - "Y16 first" is Physicist's 18:05 relay, not OW 9bb1858c text (PROVED).
- **Y16 grades:** PP **agrees with NL on every item.**
  - PROVED: Q15 (only the tr R² stress can carry the NEC-violating sign), Q3, Q4a, Q5 (in terms of λ), Q7 (the R² supply is N-independent), **Q11a (the junction verdict does not change at leading order in 1/N, given J1)**, Q12a, Q13.
  - CONDITIONAL: Q0, Q1, Q2, Q4b, Q6, Q10 (with a rounding fix), Q11b, Q12b.
  - OPEN: Q8, Q14.
  - NL's tally 8/8/2/0 = 18: PROVED.
- **New PP-1 (CONDITIONAL; arithmetic checked, anomaly derivation unchecked).**
  - Conrad (hep-th/9708031) and Lü (hep-th/9711014) give η = λ⁶/κ⁴ = (4π)⁵, which is 8× HW's printed value. That gives u = 1, not 2.
  - The R² supply becomes −1 M5 unit (was −2), and the fraction is ≤ 2.5×10⁻⁴. **No verdict changes.**
- **Erratum 12:**
  - all 10 fe0c3d92 fixes applied faithfully (PROVED);
  - tally 7/5/0/2 = 14 correct;
  - revised 1800 tally 13/11/3/2 = 29 correct.
- **NL fixes requested: 4** (both normalizations; Q10 rounding; Q6 per-direction note; header "no outside services" superseded by 36683379).
- **Tally check:** file rollup **PROVED 27 · CONDITIONAL 9 · OPEN 2 · REFUTED 0 = 38**. VERIFIED by counting the named items:
  - PROVED: I1–I5, attribution, Q15, Q3, Q4a, Q5, Q7, Q11a, Q12a, Q13, Y16 tally, E12-1…10, E12-T, E12-1800 = 27.
  - CONDITIONAL: Q0, Q1, Q2, Q4b, Q6, Q10, Q11b, Q12b, PP-1 = 9.
  - OPEN: Q8, Q14 = 2.
- **Status impact:**
  - The Y16 result (tr R² cannot change the leading-order junction no-go) is now **PP-audited: PROVED given J1**.
  - **Junction stays UNSOLVED.** Y14 and Y15 stay OPEN.
  - The HW coefficient is now CONTESTED (PP-1, CONDITIONAL).

### 2b. PP citation-scope regrade under OW 36683379 (NL erratum 13 + MR2 narrowing flags)
- **Integrity:**
  - E13 (b5190ea8…) and MR2 flags (a4084322…) equal their sidecars (A1, A2).
  - The four nl-junction-1817 files MATCH, and PP's reruns are byte-identical (A3).
  - BBBW eqs. 2.12–2.13 are confirmed in the local text (A5).
- **A4 [REFUTED, bookkeeping]:** E13's header pairs its script hashes with the wrong file names. This independently confirms Addendum 1 flag **C-1**. The files themselves are intact.
- **E13 math, PROVED where math-checked:**
  - **B-M4 strengthened:** exactly ℤ∖{±1} is attained for every C₂, with no bound.
  - B-M6 scope fix: Taubes covers only the unweighted problem. On the weighted problem Y6-vanish excludes SD/ASD fields, so Taubes contributes nothing to Y14.
  - B-M8 clarification: the BLS example is reducible, SD on S₊ and ASD on S₋.
  - B-M12: Bolza length 3.0571418390, exact.
- **New B-PP2 (PROVED, elementary):** **non-BPS E₈ Yang–Mills fields exist on the round, unweighted S⁴ for every charge**, using commuting SU(2)₁×SU(2)₂ ⊂ Spin(4) ⊂ SO(16) ⊂ E₈.
  - This upgrades only the round-existence half of 1800 Y12.
  - Stability is not addressed. **Y14 (weighted fibre) stays OPEN.**
  - PP proposes, without adopting, a 16/11/3/2 = 32 split of the 1800 tally.
- **Bolza:**
  - B-M13/M14: the systole and second length are numerically confirmed over reduced words of length ≤ 6 (3.05714, 4.89690). This is not a proof, so CONDITIONAL.
  - B-M16: |Aut⁺| = 48 is math-checked except one textbook lemma (CONDITIONAL).
  - Jenni's global maximality stays math-unchecked (CONDITIONAL).
- **MR2 flags:**
  - C1: bibliographic data verified against public Crossref records (~18:25 CST; read only). PP adds the DOIs MR2 omitted (CMP 145: 10.1007/BF02099143) and the correct follow-on authors (Bourguignon–Lawson, CMP 79).
  - **C2 [REFUTED]:** MR2's Taubes pin (CMP 91, 1983) is the wrong paper. The right one is JDG 17 (1982) 139.
  - C3: Jenni = CMH 59 (1984) 193–203, doi 10.1007/BF02566345.
  - C7: F1–F3 (7/20, β(κ)) are still ABSENT. CONDITIONAL; this is a search outcome.
- **Regrade of earlier PP marks (D):**
  - fe0c3d92's and erratum 12's origin-based "unverified" marks are withdrawn. Each is replaced by per-step math-checked / math-unchecked grades.
  - BBBW z ∈ ℤ for g = 2 moves to **PROVED given the BBBW parameterization**.
  - Other PP files from 11-09 had no origin-based marks.
- **Fixes requested:** NL 8 (additive erratum 14), MR2 5.
- **Tally check:** file rollup **PROVED 30 · CONDITIONAL 10 · OPEN 0 · REFUTED 3 = 43**. VERIFIED by counting:
  - PROVED: A1, A2, A3, A5 (4); B-M1, B-M3, B-M4, B-M6, B-M8, B-M10, B-PP2, M11-transfer, B-M12, B-M15, B-M18 (11); list-honesty, E13 tally, 1800-31 tally (3); C1, C3, C4, C5, C6, C8, C9 (7); D-1807, D-E12, D-BBBW, D-scan (4); OW 36683379 sha (1) = 30.
  - CONDITIONAL: B-M2, B-M5, B-M7, B-M9, B-M11, B-M13, B-M14, B-M16, B-M19, C7 = 10.
  - REFUTED: A4, B-M17, C2 = 3.
  - PP also confirms NL's E13 tally 10/9/0/1 = 20 and the 1800 tally 15/11/3/2 = 31.
- **Status impact:**
  - The citation re-check under 36683379 is now **filed and PP-audited**. Addendum 1's "partial, not PP-audited" becomes **PP-audited**, with the headline existence and stability theorems (M2, M5, M9, Jenni) still CONDITIONAL.
  - No result became PROVED by citation alone; the rule was respected.

## 3. Custody flag B-1 (restated)
- **Files:**
  - quantum-comp/reports/evidence_local_bridgeC_resolution_2026-11-09/part3_halfint.py, sha256 857e14f370e035bfa9b7be7e2c54d954b0c582ef18ec8c673faddf6361609602
  - …/part3_halfint.log, sha256 c4b8cf4d87887f98ce185a820d78035da6ca62d0bd0d12a4f3e64ba6d345b006
- **Last seen:** hashed by the Auditor at ~17:37 CST (both mtimes 17:37). The parent report §4.8 quotes the .log.
- **Now:** absent from all of /workspace (`find /workspace -name 'part3_halfint*'` returned 0 at 18:28:10 CST).
- **Removal was not by the Auditor.** No record on disk says who removed them or why. Local FINDINGS 9e34f2dc does not list them, and its item 3a states the same dim-0 fact from part3_search/preimage.
- **Not yet resolved.** It needs Owner or Local attention; recommended next step is a Local note explaining the removal. Nothing in the graded record depends only on these two files.

## 4. Updated NOT FOUND list (supersedes Addendum 1 §3 where they differ)
| item | status |
|---|---|
| PP audit of NL Y16 | **FOUND** (149be02a…) |
| PP audit of the citation re-check (E13, MR2 flags) | **FOUND** (c74b5a2d…) |
| ce4d9e80 fix; Local FINDINGS after 15:20 | FOUND (Addendum 1: c2e9b6fe…, 9e34f2dc…) |
| PP audit of Local A/B (c2e9b6fe, 9e34f2dc) | NOT FOUND |
| NL erratum 14 (PP fixes from 2a and 2b) | NOT FOUND |
| MR2 symbolic/global-curvature .md; MR2 ERRATUM2 to 9ab8f0a6 | NOT FOUND |
| t4371 text | NOT FOUND (relayed only) |
| RTA v18 draft | NOT FOUND (only the safe outline e18d8fea) |

MISMATCH in this window: none.

## 5. Custody
- No existing file was edited, moved or deleted, including the report, its PDF, the sidecars, Addendum 1, v16 and v17.
- Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md`: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91. Verified before writing (18:28:10) and after.
- No CERT. No Gemini. Nothing sent outside.
