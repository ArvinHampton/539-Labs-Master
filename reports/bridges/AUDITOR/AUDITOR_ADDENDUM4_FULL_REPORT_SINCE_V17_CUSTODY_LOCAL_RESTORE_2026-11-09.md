# AUDITOR — ADDENDUM 4 to the full since-v17 report: Local custody disclosure and restore, OW t4400, new files — 2026-11-09

Role: Auditor, the audit-only keeper. Written Mon 2026-11-09 ~18:34 CST (America/Chicago). Additive and created exclusively (noclobber), with a .sha256 sidecar.

Chain (all untouched):
- Report .md b3933d665226d703c5b46519da65698b3cc142ca6cbcb9724080e158604a5350, .pdf 49c573d5d71d35ca5d5fb4d7b032de3f76948ed6afb882b6eea7b5230003b078
- Addendum 1: 2d5197c1dfe3307a2fda59107e0e856ac5370b9a90a5ada65ebb01766422bf2b
- Addendum 2: fd77f1f47e9919511729703738e79adac69194e2a76b78b2dc92d98f8bb6882c
- Addendum 3: a7de4ea83b89df5fa1d792150ad386e28972a6618c7a0d2dbcaa433c521a6c46

Window: files in /workspace/quantum-comp/ and /workspace/539-labs/ after the Addendum 3 scan (18:30:13 CST), rescanned through **18:33:22 CST**. The Auditor's own files are excluded.

The Auditor records facts and hash checks only; it makes no judgement beyond them. No CERT, no Gemini, nothing sent outside.

## 1. Custody event 1: part3_halfint deletion (disclosed) and restoration (verified)
- **Disclosure** (Local custody note, and as relayed by Physicist):
  - Local's own worker deleted part3_halfint.py and part3_halfint.log at about 18:19 CST as a "tidy" step, before writing FINDINGS 9e34f2dc.
  - The note says nobody else removed them, and Local accepts that this broke the additive-only rule.
  - This answers custody flag B-1 (Addenda 1–3): the "who" is now **disclosed by Local**. The Auditor has no independent record of the deletion time; the note asserts ~18:19.
- **Custody note:** reports/CUSTODY_NOTE_LOCAL_RESTORE_PART3_HALFINT_EVIDENCE_2026-11-09_1838.md
  - sha256 **d813edfb2e08296860f9f900158eba314a319132623f19e9534324667a77626d**; sidecar **MATCH**.
  - mtime 18:31:59 CST. The header says "~18:38", later than the mtime (the recurring header/mtime lag).
- **Restored files** (new files at the original paths, mtime 18:31:59 CST, each with a new .sha256 sidecar):

| file (evidence_local_bridgeC_resolution_2026-11-09/) | sha256 now | sidecar | vs Auditor hash at ~17:37 CST |
|---|---|---|---|
| part3_halfint.py | 857e14f370e035bfa9b7be7e2c54d954b0c582ef18ec8c673faddf6361609602 | MATCH | **MATCH** (byte-identical) |
| part3_halfint.log | c4b8cf4d87887f98ce185a820d78035da6ca62d0bd0d12a4f3e64ba6d345b006 | MATCH | **MATCH** (byte-identical) |

- Local says it rebuilt the files "from the worker's own session record". The Auditor verifies the result only: content identical to the original hashes.
- mtimes are new (18:31:59), so the files' mtime is not the original 17:37.
- **Custody flag B-1: CLOSED.** Breach disclosed; files restored with hash MATCH.
- Status impact: none. The note says the files were a superseded first attempt: trivial-character space, f-eigenspace dim 0, Kohnen plus dim 0. Item 3a of 9e34f2dc stands on part3_search/preimage/check2.

## 2. Custody event 2: rename and edit of the ce4d9e80 erratum draft (disclosed)
- **Disclosure** (same custody note, and as relayed by Physicist):
  - Local's worker wrote a draft, ERRATUM_LOCAL_RELABEL_ce4d9e80_ROOTNUMBER_VS_FRICKE_SYMBOLS_AND_STS_CONTROL_2026-11-09_**1825**.md, sha256 **bf2cb4ea286eb8d34614f0e2207e35a44f756ecf46f94aa2d69cb63a66b661d6**. It was never cited.
  - The draft was renamed to …_**1819**.md and only its header time was corrected, giving **c2e9b6fe**.
  - The note dates the draft "about 18:19"; Physicist's relay calls it a "~18:25 draft". The Auditor records both and does not resolve the difference.
  - **The 1825 copy was not kept.**
- **Verified on disk:**
  - ERRATUM_…_1819.md: sha256 **c2e9b6fe2cb6b08ec24a7f6dfddc967eb7918adb244050d2d67c703b033d42ec**, sidecar MATCH, mtime **18:19:55 CST**. This is the same hash and mtime the Auditor recorded in Addendum 1 (~18:26). **Its content is unchanged since the Auditor first hashed it.**
  - The _1825 draft (bf2cb4ea…): **NOT FOUND**. `find /workspace -name '*ce4d9e80*1825*'` returned nothing. It is not recoverable, and its hash is Local-asserted only.
- **Note on Addendum 1.** Addendum 1 lists c2e9b6fe with mtime 18:19:55 as an "18:19" record. That file is the product of a rename plus a header edit of an earlier draft. Its time as an 18:19 record is therefore **Local-asserted, not original**. Addendum 1 is not edited; this note qualifies it.
- Status impact: none on the mathematics. A's labels and Addendum 1's summary of A stand.

## 3. OW 91e69b38 (t4400): pursue both Bolza groups
- File: reports/OWNER_WRITE_MAINCHAT_t4400_KK_SCOPE_PURSUE_BOTH_BOLZA_GROUPS_48_AND_96_2026-11-09_1832.md
  - sha256 **91e69b3888eba3975232c028168465017d27e470583a9a757c62084d200e36a3**; sidecar **MATCH**; mtime 18:32:08 CST.
- **Verbatim:** "Pursue both for possible resolutions". This is the answer to the order-48 vs order-96 question in Addendum 3 (a7de4ea8) on OW 49b04146.
- **Recorded decision:**
  - Run the KK truncation of OW 49b04146 under **both** (A) Aut⁺(Bolza), order 48, and (B) the full isometry group including reflections, order 96. Each is combined with the wall ℤ₂.
  - Report what each truncation keeps and where they differ.
  - Per Physicist's relay: MR2 runs it and PP audits it. The OW file itself names neither bot.
- **Not decided:** which group is adopted. That stays an **Owner choice (OPEN)** after the results.
- Status: a scope choice, not a result. **The full KK spectrum stays OPEN.**
- **Addendum 3's ambiguity flag is RESOLVED as "both pursued", not as a choice of group.**

## 4. Other new files (18:30:13 to 18:33:22 CST)
| time (mtime) | file (reports/) | sha256 | sidecar | summary / status impact |
|---|---|---|---|---|
| 18:31:45 | MR2_TWISTED_VACUA_EINSTEIN_SYMBOLIC_AND_GLOBAL_CURVATURE_2026-11-09_GLOBAL_CURVATURE_MN1z0.log | aa28c625eeb0042c9274cc51d980dc8a9548420732c4b6ccbc9785ecf4ebfed6 | MATCH | global curvature scan: max\|eig Q\| = 6.6290/ℓ², ℓ_p²·max = 2.69e-3 |
| 18:31:45 | …_GLOBAL_CURVATURE_BBBWz2.log | 1dae84ade46cea1a64abffba0d2753f3f2d1db242e41fa2e3ce136621d0b3a4f | MATCH | max\|eig Q\| = 18.849/ℓ², ℓ_p²·max = 7.64e-3; at the μ₁ = 1 pole |
| 18:31:45 | …_GLOBAL_CURVATURE_BBBWz3.log | 7d4d44d2ce1fae5ec83deed6f8a237dd08630075afce8b4abd15b7dca4b9706f | MATCH | max\|eig Q\| = 21.890/ℓ², ℓ_p²·max = 8.87e-3; at the μ₁ = 1 pole |
| 18:31:48 | …_GLOBAL_CURVATURE_MN2z1.log | 4893f1d2e40890b2c49cb681c824e9687d9b351befe16bc6e58ee9ceccf68cf2 | MATCH | MN2: max\|eig Q\| = 40/3 (13.333…)/ℓ², ℓ_p²·max = 5.40e-3; at the μ₁ = 1 pole |
| 18:32:30 | **MR2_ERRATUM2_PER_PP_GATE_AUDIT_FULL11D_2026-11-09.md** | 7b9ebdaf9d7656931e65c361cd1cce740479db91352969da4b54ff72ac84b720 | MATCH | MR2's response to PP gate 384096a8 §14 items 1–8 (below) |

**Summary of MR2 erratum 2 (7b9ebdaf):**
1. (D) prose corrected to e^{2f} = 2/3 (PROVED, arithmetic).
2. The curvature maximum is relocated to the μ₁ = 1 pole for MN2 and BBBW, and the whole μ₀ = 0 circle for MN1, which confirms PP. MN2 limits: K = 3408, Ric² = 3312, Weyl² = 1939.2, max\|eig Q\| = 40/3. Values PROVED at the evaluated points and limits; **global sup CONDITIONAL**.
3. "Warping lengthens the systole" is **withdrawn (OPEN)**. A two-sided bound is given (PROVED given the metric). Warp-safe thresholds are 0.19–0.28. The Bolza value is used.
4. BBBW z=2 per-point rows supplied.
5. A dG₄ control that can fail was added and run.
6. Frame-normalized Einstein residuals added.
7. Symbolic "all points" Einstein is deferred to a new symbolic/global .md. Until a full symbolic zero is shown, it stays **CONDITIONAL**.
8. Cosmetics corrected.

Status impact:
- MN N=2 stays **CONDITIONAL**, with no change to the vacuum adoption.
- PP's MR2 gate fixes are now answered, pending a PP check.
- No PROVED upgrade of the all-points or global statements.

**Header/mtime note:** the erratum's header says "written at 18:28 CST"; its mtime is 18:32:30, and the file itself says the mtime is authoritative.

- The symbolic/global **.md** that erratum 2 refers to, MR2_TWISTED_VACUA_EINSTEIN_SYMBOLIC_AND_GLOBAL_CURVATURE_2026-11-09.md, is **NOT FOUND** on disk at 18:33:22. It is a forward reference; only the .py and .log files exist.
- Nothing new in /workspace/539-labs/.

## 5. Updated known-pending (KP) and NOT FOUND list (supersedes Addendum 3 §2 where they differ)
| item | status |
|---|---|
| Custody flag B-1 (part3_halfint) | **CLOSED**: disclosed (d813edfb…) and restored, hashes MATCH the 17:37 originals |
| Local draft ERRATUM_…_1825.md (bf2cb4ea…) | **NOT FOUND** (renamed and edited into c2e9b6fe; not kept; not recoverable) |
| MR2 ERRATUM2 for the gate file 9ab8f0a6 | **FOUND**: 7b9ebdaf… |
| Addendum 3 Bolza-group ambiguity | **RESOLVED as "both pursued"** (OW 91e69b38); the group choice stays OPEN (Owner) |
| MR2 symbolic/global-curvature .md | NOT FOUND (logs only; erratum 2 forward-references it) |
| KK truncation results under 48 and 96 | NOT FOUND (newly ordered) |
| PP check of MR2 a8ad459a and 7b9ebdaf | NOT FOUND |
| PP audit of Local A/B (c2e9b6fe, 9e34f2dc) | NOT FOUND |
| NL erratum 14 | NOT FOUND |
| Y14, Y15 results | NOT FOUND (OPEN) |
| t4371, t4396u, t4398u texts | NOT FOUND (relayed or referenced only; not adopted) |
| RTA v18 draft | NOT FOUND (only the safe outline e18d8fea) |

MISMATCH in this window: none.

## 6. Custody
- No existing file was edited, moved or deleted by the Auditor, including the report, PDF, sidecars, Addenda 1–3, v16 and v17.
- Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md`: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, verified before writing (18:33:22) and after.
- No CERT. No Gemini. Nothing sent outside.
