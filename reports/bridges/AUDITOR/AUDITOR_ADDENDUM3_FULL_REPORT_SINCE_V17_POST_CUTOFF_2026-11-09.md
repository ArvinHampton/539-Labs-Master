# AUDITOR — ADDENDUM 3 to the full since-v17 report: files after the Addendum 2 scan — 2026-11-09

Role: Auditor, the audit-only keeper. Written Mon 2026-11-09 ~18:30 CST (America/Chicago). Additive and created exclusively (noclobber), with a .sha256 sidecar.

Chain (all untouched):
- Parent report .md b3933d665226d703c5b46519da65698b3cc142ca6cbcb9724080e158604a5350, .pdf 49c573d5d71d35ca5d5fb4d7b032de3f76948ed6afb882b6eea7b5230003b078
- Addendum 1: 2d5197c1dfe3307a2fda59107e0e856ac5370b9a90a5ada65ebb01766422bf2b
- Addendum 2: fd77f1f47e9919511729703738e79adac69194e2a76b78b2dc92d98f8bb6882c

Window: files in /workspace/quantum-comp/ and /workspace/539-labs/ after the Addendum 2 scan (18:28:10 CST), rescanned through **18:29:36 CST**. The Auditor's own files are excluded.

Labels: PROVED / CONDITIONAL / OPEN / REFUTED. Owner decisions and scope choices are not proofs. Hashes only. No CERT, no Gemini, nothing sent outside.

## 1. New files (the only two in the window)
| # | time (mtime, CST) | file (reports/) | sha256 | sidecar |
|---|---|---|---|---|
| a | 18:28:38 | MR2_ERRATUM_SOURCE_LIMIT_FLAGS_PER_PP_c74b5a2d_2026-11-09.md | a8ad459a325f411233337712dcb4cc84a78b2419bb3f3a2a762c3923194369b3 | MATCH |
| b | 18:28:56 | OWNER_WRITE_MAINCHAT_t4398_KK_TOWER_SCOPE_BOLZA_Z2_INVARIANT_MODES_2026-11-09_1828.md | 49b041469b7dedd8da1881d12894edfb74e8fd55675e8480b4d968cb69c310c2 | MATCH |

Nothing new in /workspace/539-labs/. No other quantum-comp files. No new PP audit.

### 1a. OW 49b04146 (t4398): KK tower scope
- **Owner's words (verbatim, as recorded):** "As mine: restrict the KK tower analysis to modes invariant under the Bolza symmetries and the wall ℤ₂ (scope choice, not a result). Nothing else from the paste."
- Source: widget answer to t4398s18247, main chat, ~18:28 CST.
- **What it decides.** It is a **SCOPE CHOICE, not a result.** The KK tower analysis on the MN N=2 background is restricted to modes invariant under:
  - (i) the automorphism group of the Bolza surface Γ = Σ (OW 7ff8299d);
  - (ii) the wall ℤ₂ of the HW-type fixed plane (OW f825dfff).
  MN N=2 itself remains CONDITIONAL (OW 19a88b19).
- **Status impact:**
  - **The full KK spectrum stays OPEN**, including the Wilson lines and spin structure. The truncation proves nothing about the full spectrum, and modes it excludes are **not** claimed absent.
  - No status changes anywhere else.
  - For KK statements made under this scope, any result should say it applies to the invariant sector only.
- **Not adopted:** nothing else from the pastes t4396u or t4398u. That covers b, E₈ "acceptance", the "5/3 gradient", joint carrier, R_c, DP-a, Layer2, the bulk-to-H⊗ℂ² map, Φ Q3 and α. All stay as previously recorded.
  - Neutral items: still neutral (5f59e33e / f283cffd).
  - b and J7: OPEN.
  - The count gap stays (1.255, 1.667), CONDITIONAL. There is no "5/3 gradient".
- **Pasted text on disk:** t4396u and t4398u exist **only as referenced inside this OW**; there is no standalone file. They are **relayed only, NOT adopted**.
- **Auditor note (not a grade).** "Bolza symmetries" does not say whether this means the orientation-preserving group Aut⁺ or the full isometry group. These have order 48 and 96. Aut⁺ = 48 is math-checked except one lemma, CONDITIONAL; Isom = 96 is in PP c74b5a2d B-M16. Whoever does the KK analysis should name the group; the Owner may need to confirm it.

### 1b. MR2 a8ad459a: erratum to the source-limit flags (a4084322), per PP c74b5a2d
- **What it says.** It applies PP's five MR2 fixes:
  - **Fix 1:** Taubes CMP 91 (1983) is **REFUTED as the Y12 pin**. The replacement is Taubes, JDG 17 (1982) 139–170, doi 10.4310/jdg/1214436701.
  - **Fix 2:** Jenni = Comment. Math. Helv. 59 (1984) 193–203, doi 10.1007/BF02566345. The primary PDF was not obtainable (a challenge page, not a PDF).
  - **Fix 3:** adds the Sadun–Segert CMP 145 DOI 10.1007/BF02099143, and names Bourguignon–Lawson (not BLS) for CMP 79 (1981) 189–230, doi 10.1007/BF01942061.
  - **Fix 4:** states that MR2's Sadun–Segert sign convention (n₋²−n₊²)/8 is the reverse of NL's (orientation only), and that (1,3) is the excluded n± = 1 case.
  - **Fix 5:** the step checks for SSU, Sadun–Segert and BLS are superseded by NL E13 (b5190ea8…) where E13 checked the math.
- Bibliographic data were read from public Crossref records with curl (~18:27–18:28 CST; read only).
- Integrity: it cites PP c74b5a2d…, flags a4084322…, E13 b5190ea8…, OW 36683379… and tip 7cddb188…. All agree with disk.
- **Status impact (bibliographic only; no math upgrade):**
  - Taubes CMP 91 as the Y12 pin: REFUTED.
  - Taubes gluing (M7): **CONDITIONAL**.
  - Jenni global maximality (M13): **CONDITIONAL, pending**.
  - M2, M5, M9: **CONDITIONAL**.
  - Nothing became PROVED by citation alone; the rule was respected.
  - PP's MR2 fix list from c74b5a2d is **fully addressed**, pending a PP check of this erratum (NOT FOUND yet).
- Tally: the file has no PROVED/OPEN rollup. Its "Net" table lists 5 fixes, and all 5 appear in the body. Consistent.

## 2. Known-pending (KP) and NOT FOUND list (supersedes Addendum 2 §4 where they differ)
| item | status |
|---|---|
| PP audit of NL Y16 | FOUND (149be02a…, Addendum 2) |
| PP citation regrade | FOUND (c74b5a2d…, Addendum 2) |
| MR2 fixes for c74b5a2d | **FOUND**: a8ad459a… (this addendum) |
| ce4d9e80 fix; Local FINDINGS after 15:20 | FOUND (c2e9b6fe…, 9e34f2dc…, Addendum 1) |
| PP check of MR2 a8ad459a | NOT FOUND |
| PP audit of Local A/B (c2e9b6fe, 9e34f2dc) | NOT FOUND |
| NL erratum 14 (PP fixes from 149be02a and c74b5a2d, incl. the E13 hash-label swap) | NOT FOUND |
| KK tower analysis under OW 49b04146 scope | NOT FOUND (newly scoped; KK spectrum OPEN) |
| MR2 symbolic/global-curvature .md; MR2 ERRATUM2 to 9ab8f0a6 | NOT FOUND |
| Y14, Y15 results | NOT FOUND (OPEN, in progress) |
| t4371 text | NOT FOUND (relayed only) |
| t4396u / t4398u standalone text | NOT FOUND (referenced only in 49b04146; NOT adopted) |
| RTA v18 draft | NOT FOUND (only the safe outline e18d8fea) |
| Custody flag B-1: part3_halfint.py (857e14f370e035bfa9b7be7e2c54d954b0c582ef18ec8c673faddf6361609602) and .log (c4b8cf4d87887f98ce185a820d78035da6ca62d0bd0d12a4f3e64ba6d345b006) | still ABSENT from /workspace (checked 18:29:36 CST). Last seen ~17:37 CST. Not removed by the Auditor; no record of who removed them. OPEN for the Owner or Local |

MISMATCH in this window: none.

## 3. Net effect on the parent report
- Vacuum: MN N=2, CONDITIONAL, unchanged. The KK analysis is now scoped to the Bolza × wall-ℤ₂ invariant sector. **The full KK spectrum stays OPEN.**
- Junction: UNSOLVED, unchanged.
- Citation re-check: the MR2 side is closed bibliographically. The math of the headline theorems stays CONDITIONAL.
- v18 blockers (parent §7): unchanged.

## 4. Custody
- No existing file was edited, moved or deleted, including the report, PDF, sidecars, Addenda 1–2, v16 and v17.
- Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md`: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, verified before writing and re-verified after.
- No CERT. No Gemini. Nothing sent outside.
