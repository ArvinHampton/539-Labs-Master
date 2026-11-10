# FINDINGS — t1049u Author-authority package + residual-C CONFIRM-insert score (2026-10-25 ~18:55 CDT, America/Chicago)

**Scope:** Score OWNER_WRITE_AUTHORITY_OPEN_DEADLOCKS (t1049u) and its residual-C CONFIRM insert. Auditor did not edit residual-C or any Owner Write. Invent-ban; CORE_FREEZE; no order78; Empty #7–#9 HOLD; no 4da09dec revive.
**Invent-ban RESTORED:** VERIFIED. Write's lane map says "Invent-ban: RESTORED after this package, except Owner Zenodo Secure Form action". Draft §1c (line 56) says "Invent-ban restored after this insert (Zenodo Secure Form remains Owner-only)". Header row 16 still reads "ON except Owner-lifted Item (2)", so it does not mention t1049u (soft note N-2).
**residual-C status:** OPEN-conditional. No LOCK (row 14 "None"). P5 tag `[[ to prove / accepted ]]` is still blank. residual_B1 numeric/closed form is still OPEN. Bridge is PARTIAL (row 17). READY is not claimed anywhere, so READY = NO. No false LOCK/READY claim.

## Verified sha256 (box, recomputed)
| Artifact | sha256 | Status |
|---|---|---|
| OWNER_WRITE_AUTHORITY_OPEN_DEADLOCKS_2026-10-25.md | bdc1d8b02b44c81cedd5b2b374766533409336acc86546a4ae06f98a03e0fdbd | MATCH expected |
| residual-c-field-WRITTEN_PREMISES_DRAFT.md (live) | 9adb84fa6540b518b18943a54459d1388d65bfa823d78d08ba750d3eb57be7ab | MATCH expected |
| residual-c-…pre-authority-5bb86c70.md (backup) | 5bb86c70d0cc1b85815abef40490a37d34f9d50974f17967b35d1fcdd506b2af | MATCH prior |
| OWNER_WRITE_ITEM2_residual_factor_B1_2026-10-25.md (live, M6-strike update) | 358f4d050acf9adfcae817d28c97a03e0adafe698aa5f452367f52b2ec8553bd | located; matches prefix 358f4d05 |
| Write inputs: CONFLICT_RESOLUTION_FULL b7ae82ed…; ITEM4 3193335f…; DIGIT_CALL_VERDICT 4e60264c…; RTA_v12 f837aa37… | all recomputed | MATCH as cited |
| Write input: ITEM2 cited 49aba949… | live is now 358f4d05… | this is the pre-strike version (see N-1) |
| Prior FINDINGS f8d2f7e6…, 74bb4e42…, f70af109…, 23bc9d2f… | recomputed | MATCH |

## Verdict: **MATCH-with-SF** (hygiene only; no content SF)

## Per-stamp table
| Claimed stamp | Write | residual-C draft | Status |
|---|---|---|---|
| k = −2 | W-D2 | rows 81, 82, 88, 130; §1c | PRESENT |
| ρ(W₇) form-space +1 | W-D4 | line 106 (FILLED, replaces Arvin-blank); §1c | PRESENT |
| ρ(W₇)² = Id | W-D4 ("ρ(W₇)² = Id_V (P1-R1)") | line 82 (R4 normalisation), line 106 | PRESENT. Checkable: W₇=(0,−1;49,0), W₇² = −49·I, scalar ⇒ identity in PSL₂-style projective class. Stated as a normalisation, not a theorem. |
| M6 STRUCK (84≠168) | W-A1 | line 45, §1c line 63; Item2 live line 50 | PRESENT. Checkable: \|PSL(2,13)\|/13 = 1092/13 = 84. |
| L_coh = 0.0034 ly / 18 fs Written | W-H2 | row 18; §1c line 64 | PRESENT (see supersession analysis) |
| Ω₁₁D unaffected | W-F1 | §1c | PRESENT |
| Item4 G3 closed | W-G3 (cites 3193335f…, verified) | §1c | PRESENT |
| Still OPEN: LOCK, residual_B1, P5 tag | Constraints + STATUS | row 14/18, line 68 | PRESENT as OPEN |

## Insert fidelity (5bb86c70 → 9adb84fa)
Diff: row 18 status; line 45 (M6 removed and marked STRUCK); new §1c (source Write sha bdc1d8b0… and prior sha 5bb86c70… cited; seven stamps); k fills at lines 81/82/88/130; +1 fill at line 106. Every change maps to a Write section. The draft adds no matrix entries, no residual_B1 value and no P5 tag. W-E1 (Audit A superseded) and W-B3 wording are carried faithfully. **No silent invent.**

## GATING (5) / Audit A clearance (74bb4e42 caveats)
| Conflict | Status |
|---|---|
| Modular weight k (½ / metaplectic vs −2; k-parity inference) | **CLEARED.** k = −2 is Owner Written (W-D2); the half-integer path is CLOSED for Option 2. |
| k = −2 vs EH warp k homonym | **CLEARED.** W-D2 has explicit homonym note (soft C2). |
| ρ(W₇) sign (+1 came from OPTIONS, not derived) | **CLEARED as Owner Written** (W-D4 fills +1). It is still not derived, and is an Owner premise rather than a theorem. |
| outer_* definitions | **NOT in this package. Stays OPEN** for this gate (no outer_* stamp in Write or insert). |
| Audit A d=2 package | Stamped SUPERSEDED (W-E1). Only k = −2 is retained. |

## L_coh supersession analysis (check A)
- t928u (f8d2f7e6…) recorded: Written 17 Theorems v5 prints L_coh ≈ 0.34 ly, and 0.0034 was chat-only and ABSENT from Written.
- DIGIT_CALL_VERDICT (4e60264c…, verified) shows that the Written value 3.2×10¹³ m / 9.4607×10¹⁵ m·ly⁻¹ = 0.00338 ly, so the 0.34 print is a factor-100 error. It also shows that 3×10⁻¹² s × 0.006 = 1.8×10⁻¹⁴ s = 18 fs (the print says "18 as"). Both prints are marked AUTHOR_CORRECTED / SUPERSEDED.
- W-H2 explicitly says "Printed 0.34 ly is a factor-100 error … Written value on box / Author-corrected deposit governs" and does not claim Zenodo is corrected.
- **Finding:** this is an **explicit Owner supersession/correction, not a silent conflict.** The draft never asserts 0.34, so there is no dual assertion and no SF. Consequence: the t928u "safe public: cite 0.34 ly" guidance is now STALE internally. The public Zenodo/17T text still prints 0.34 ly and 18 as until the Owner submits the Secure Form. The Auditor does not judge physics correctness, only that the arithmetic in the verdict checks.

## Check C — M6 / prior SF-1
SF-1 from f70af109… (lane map) and 23bc9d2f… (§1b item 6) is **CLEARED**. Item2 live line 50 reads REJECTED/STRUCK; line 61 reads "M1/M3 … (M6 STRUCK)"; draft line 45 has M6 removed from the vocabulary list.

## Soft SF (check E gates)
- Cat A without ACCEPT: none. Empty KEEP / 4da09dec revive: none. Local/NL mix: none (Bridge PARTIAL; no Local Bridge C claim). Bridge YES / δ≡0 / residual-C closed / LOCK claimed: none. Algebraic invent under geometric label: none (Ω₁₁D stamp is a non-identification only).
- **SF-H1 (hygiene):** sidecars are stale. `residual-c-field-WRITTEN_PREMISES_DRAFT.md.sha256` still records 5bb86c70… (live is 9adb84fa…). `OWNER_WRITE_ITEM2_….md.sha256` still records 49aba949… (live is 358f4d05…). Recommend the Owner/coordinator refresh both.
- **N-1 (note):** the Write's input table cites Item2 49aba949… (pre-strike). The Item2 strike edit (→358f4d05…) post-dates it and is traceable via "t1049u W-A1" in Item2 line 50. Acceptable, but MR1/MR2 should cite 358f4d05… going forward.
- **N-2 (note):** draft header row 16 (Invent-ban) and line 50 do not mention t1049u. They are consistent in substance (ban ON), and §1c states restored.

## What remains OPEN
LOCK; P5 tag; residual_B1 numeric/closed form; full ρ on generators (matrix); cusp in/out rules; P4 pairing blanks; outer_* defs (GATING); public Zenodo L_coh correction (Owner-only). **Bridge PARTIAL. READY NO** (draft does not claim otherwise).

## HASH_INTEGRITY (out-of-band)
Append to HASH_INTEGRITY.md: Write bdc1d8b0…; residual-C 9adb84fa… (prior 5bb86c70… backup present); Item2 358f4d05…; this FINDINGS sha (computed after write, not self-embedded).
