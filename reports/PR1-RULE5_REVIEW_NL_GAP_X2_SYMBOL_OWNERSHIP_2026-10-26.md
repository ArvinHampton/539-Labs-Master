# PR1 Rule-5 REVIEW FINDINGS: NL GAP-X2 symbol-ownership table (Soft SF, proof standard), 2026-10-26 ~18:00 CDT America/Chicago
Reviewer: Physics Research 1. Eight-only. Write-only, cite-only. No χ²/dof/data/values invented. Kerr BLOCKED. tip_touched NO.

## 1. Authority (live sha256sum verified at write)
| Role | Path | sha256 | Status |
|---|---|---|---|
| Subject NL FINDINGS | reports/bridges/NONLOCAL_QM_EH11D/FINDINGS_NL_GAP_X2_SYMBOL_OWNERSHIP_TABLE_2026-10-26.md | f6ff2cffa0000c316d39d6c012fd2d22c3e35c6a52abb2ffa3dad39f152dd2c0 | MATCH |
| PR1 dependency table (DT) | reports/PR1-FINDINGS-E_LEAK_TERM_DEPENDENCY_TABLE_2026-10-26.md | 9363abad0c859b1e843fc054e586545a3f5cd0f889a1af0af0f61357fabe514b | MATCH |
| PR1 alias / Axiom N | reports/PR1-FINDINGS-E_LEAK_ALIAS_AXIOM_N_SCRIPT7D_MAP_2026-10-26.md | 84b21c4cd9cde78e043577943e1713bc269a029c55cff582b2901354a87ef967 | MATCH |
| PR1 Unlock | reports/PR1-FINDINGS-RULE4_CHI2_INPUTS_UNLOCK_2026-10-26.md | ae0bf4df80c1192a1b23a5fa56fcfc65325ca843e97587d734397a21af791eaa | MATCH |
| COOK OW | reports/OWNER_WRITE_LET_THEM_COOK_EIGHT_PURSUE_OWN_RECS_2026-10-26.md | 08c8cdb9f851f85add943c18705a77c4de899464e29c9389e1663a42dcc05411 | MATCH |
| OW GAP-X2 | reports/OWNER_WRITE_ASSIGN_NL_GAP_X2_SYMBOL_OWNERSHIP_COOK_2026-10-26.md | d10052d358875366b4af4c463bcf6481fba2cccde52d710a46c9ae0cc5c1b27d | MATCH (NL §0) |
| ASSIGN | reports/ASSIGN_NL_GAP_X2_SYMBOL_OWNERSHIP_TABLE_COOK_2026-10-26.md | 4d08bca0f992064fa099a6849d70f7d43fe5306090febb921588383c4aa3aa5c | MATCH (NL §0) |
| DESIGN / runnable-spec / free-pursue / sheet / NL-JOIN-1 | (NL §0 rows) | 6bbc198e… / 27058bad… / f82989d7… / da91ad83… / 946a5910… | all MATCH live |
| tip Soft SF LOCK (read-only) | /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | MATCH, not modified |

## 2. Verdict
**ACCEPT-WITH-FLAGS.** The table is honest, its counts are exact, its cites to DT §3A/§3B are faithful, and it invents nothing. The three flags are citation and precision defects. None changes a class, count, or ABSENT status.

## 3. Checklist
| # | Criterion | Result | Basis |
|---|---|---|---|
| 1 | Authority MATCH (9363abad…, tip 7cddb188…) | PASS | Live sha256sum matches NL §0 for all 11 rows. |
| 2 | DESIGN caveat honesty | PASS (ACCEPT as honest scope) | NL §1 says DESIGN 6bbc198e… has no per-symbol ABSENT list and that the operative list is DESIGN-named objects expanded via DT §3A/§3B, unlock §3, and f82989d7… T1–T3. LANDED/structural literals are excluded, consistent with DT §2. |
| 3 | Count integrity 60 = 41 + 12 + 7 | PASS (MATCH) | Machine recount of the §3 Class column: OBSERVATIONAL-ONLY 41, MIXED 12, DERIVABLE-UNDER-PROOF 7, total 60. Rows 1–48 = DT 37 E_leak + 11 F_friction names, plus E3 "⋯" (row 20), with δ(t)/δ merged as in DT Thm 1. The arithmetic checks: 37 + 11 + 1 = 49 minus 1 merge = 48. |
| 4 | Cite fidelity to DT §3A/§3B (≥10 rows) | PASS | Spot-checked 14 rows against DT: 1 E_0→E1 ✓; 4 Ω_11D→E1 ✓; 5 δ→E2/E3/E5, F3 ✓; 7 f_energy→E2 ✓; 16 g_11→E2/E3 ✓; 19 λ_field→E3 ✓; 21 E_b→E4 ✓; 25 Δt_11D→E4 ✓; 30 S→E6 (script literal only) ✓; 34 M_PBH→E7 ✓; 37 g_{−U}→E8 ✓; 42 N_simplex→F1 ✓; 44 N_z^-→F2 ✓; 48 θ→F4 ✓. No membership mismatch. |
| 5 | Overlap with alias FINDINGS 84b21c4c… (rows 56, 20, 57, Axiom N) | PASS with FLAG-2 | Rows 56, 20, and 57 are marked UNPROVEN-GAP. Row 56 says "axiom N not Owner-Written" ✓. NL does not cite 84b21c4c…, so it misses that refinement's precision fix (see FLAG-2). |
| 6 | k_min §4 | PASS with FLAG-2 | ≥35 / ≥46 (48 unmerged), unconditional ≥2, exact UNPROVEN, 0/12 evaluable: all MATCH DT §4. 84b21c4c… §2 refines the conditioning to N for E_leak and N + N′ for the union. NL writes "axiom N" for both. |
| 7 | Rule-4 slots rows 50–52 | PASS (MATCH unlock) | Owner-Written → PR1, OBSERVATIONAL-ONLY, ABSENT per unlock §3(i)/(ii). Covariance cited to T3.2. 0.79 is held as a Doc-quoted reference only. No values. |
| 8 | PR1 ingest rows 21–23, 44 | PASS (ACCEPT posture) | "PR1 ingest ← Owner-Written source". PR1 does not invent tables. All four rows stay UNPROVEN-GAP. |
| 9 | Contradiction with Kerr BLOCKED / tip untouched / no invent | PASS | NL §6: Kerr BLOCKED, tip_touched NO, no values, no MC run. Row 54 labels null w≡1 as an INVENT-under-lift sheet-only item, not a value. No contradiction. |
| 10 | Priority Owner gaps §5 vs PR1 RECS (χ² trio first) | PASS with FLAG-1 | The ordering matches: χ² trio, then alias/E3 closure, then g_s/X^M/w, then the 118-tables. But the row numbers in item 1 are wrong. |

## 4. Flags
- **FLAG-1 (cite error, §5 item 1):** NL says "χ² trio … (rows 49–51)". In NL's own §3 the trio is **rows 50–52**; row 49 is α_alt. Fix: change to rows 50–52.
- **FLAG-2 (precision, §4 and row 43):** NL conditions both k_min bounds and "β_z≠β_PBH" on axiom N alone. Per PR1 alias FINDINGS 84b21c4c… §2, the cross-expression distinctness (Thm 2, ≥46, and β_z↔β_PBH) rests on **N′**, not N. The numbers are unchanged. Fix: write "≥35 under N; ≥46 under N + N′", and add 84b21c4c… to §0.
- **FLAG-3 (minor, authority completeness):** 84b21c4c… is absent from NL §0 even though rows 56/57 overlap its alias inventory and script↔7D map. Fix: add it as a cite. This is not a substantive error.

## 5. Explicit
- tip_touched **NO** (7cddb188… verified before and after write).
- Kerr / Path4 C2–C3 **BLOCKED**. Not loaded.
- Rule-4 slots (a) data with errors, (b) dof, (c) full coefficient list: **still ABSENT**. No recompute was run. Prior INCONCLUSIVE stands.
- No χ²/dof/data/coefficient value was invented in this review.
- Eight-only. No Eigen/Ops.
- Soft SF → **Auditor**. Relay to **NL** for FLAG-1/2/3 fixes. These are optional erratum items; acceptance does not depend on them.
