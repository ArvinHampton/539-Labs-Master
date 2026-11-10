# FINDINGS: PP confirmation of MR2 erratum 0f89caea (breathing cross-check b44cd004 + line-27 note 553a8a4a, per PP 4c5641ba)
Auditor: PP (Professor Proof). Written 20:36 CST (America/Chicago). Additive; nothing edited or sent; no CERT; no Gemini; nothing adopted. Tip 7cddb188 unchanged.

**Provenance.** MR2_ERRATUM_CROSSCHECK_BREATHING_AND_LINE27_NOTE_PER_PP_2026_2026-11-09.md has sha 0f89caeae709b7bfe0e5094776513cd671f8da637797238a578103574675d869 (sidecar MATCH, 20:29:50). It is text only, so there is no .py to rerun.

## Fix-by-fix (PP 4c5641ba fixes 1–8)
| PP fix | erratum | verdict |
|---|---|---|
| 1 (note scope; 516438eb codes 4/9; withdraw retraction) | Fix 1 | **FAITHFUL.** PP re-verified 516438eb lines 65–66 (F = Rational(4,9)). Its log prints R = −9.0 at all 6 points, and exactly −45 − 12 + 48 = −9. The unscoped sentences are withdrawn as REF. The citation 90f43897 line 39 is verified verbatim ("The error is the coded F = 4/9 … R = −9 exactly"). **PP 2cf2630b stands**, and its fix 3 stands. |
| 2 (M6 restricted to S⁴-constant) | Fix 2 | **FAITHFUL.** It cites 8ca7b93a (12, 20, 32, 40, COND) and keeps the inputs COND. |
| 3 (PART2 finite differences) | Fix 3 | **FAITHFUL.** h = 1e-12 / 1e-8, matching the PART2 code. |
| 4 (M1 "yy only") | Fix 4 | **FAITHFUL.** The phrase is dropped, the by-construction explanation is added, and the grade stays COND. |
| 5 (tally heading) | Fix 5 | **FAITHFUL.** |
| 6 (OOM dependence) | Fix 6 | **FAITHFUL.** The text matches PP 4c5641ba §2. |
| 7 (M9 input sources) | Fix 7 | **FAITHFUL.** All three citations are verified at the stated lines: f688c7e3 L170 ("R_max = 12 exactly is COND"), bd47ff5e L69 (k-range) and 9ab8f0a6 L43 (3408). R_max and 3408 are carried as COND. |
| 8 (note heading) | Fix 1, "Heading narrowed" | **FAITHFUL.** It now refutes only the 9ab8f0a6 line-27 md slip. |

**Tally: 9/4/2/2 = 17. CONFIRMED.** This equals PP 4c5641ba §5.
- PROVED: M3–M9, M12, M14a. COND: M1, M2, M10, M15. OPEN: M11, M16. REF: M13, M14b.
- Residual note, no fix required: under fix 7, M9's numerical outputs ℓ_p²R_max and ℓ_p²√Riem² are COND through their inputs, while M9 as arithmetic stays PROVED. The erratum says exactly this.

**Verdict: FAITHFUL. All 8 fixes applied; no residual fixes.**
