# PP CONFIRM — MR2 erratum 1eb4cec4 (applies PP e2750e28, wall Bianchi / J_M5 audit of 79795981). 2026-11-10, written 11:02:13 CST (America/Chicago)

Labels are pure math (PROVED / CONDITIONAL / OPEN / REFUTED / PENDING). This is a faithfulness confirm only: no new mathematics, no grade change, nothing adopted (t433u does not adopt these grades), no CERT. **Junction: UNSOLVED.** Wording: resonant algebra. Additive; no existing file edited; nothing written into /workspace/mr2-c2e8-1010/ or any MR2 directory; frozen scripts and PP evidence untouched.

## 0. Integrity
- Target erratum: MR2_ERRATUM_C2PRIME_E8_WALL_BIANCHI_JM5_79795981_PER_PP_e2750e28_2026-11-10.md, sha256 1eb4cec4ddf8fb0c80b4aa45611211425485b0dbc9fb115eb994ab7629643714 = sidecar = claimed. mtime 11:00:38.716 CST, mode 644 (sidecar 644, consistent with MR2's series; nit only). Header "written 11:00:38 CST" = mtime to the second ✓.
- Input audit: FINDINGS_PP_AUDIT_MR2_WALL_BIANCHI_JM5_79795981_2026-11-10_1057.md, still e2750e28457254d661757acb6ebef857f6999153f605db24fd625837a60a8b5f = sidecar, mode 444, mtime 10:57:57.509 CST (unchanged).
- PP evidence dir pp_evidence_bianchi_jm5_79795981_2026-11-10/: all 10 files = their sidecars, mode 444; shas cited in the erratum (pp_exact_checks.py 74991650… / log 00bd3bea…; pp_exact_gb_verify.py f412ff84… / log d9228c09…) match the live files.
- Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, mtime 2026-11-06 14:38:54 CST, checked before this write. Not touched.

## 1. Frozen originals: untouched
| file | sha256 (= sidecar) | mtime CST | mode |
|---|---|---|---|
| report 79795981 | 797959812aeaafc3e1d3c4d59573bc4f315b03936c74121b1138af5c4f877048 | 10:30:58.828 | 644 (as at audit) |
| note 27c61e09 | 27c61e0984c30ba0d2ecfc74f6f764e1da59986088ef6d4419f3aecabd6d8cd4 | 10:35:22.599 | 644 (as at audit) |
| script /workspace/mr2-c2e8-1010/c2p_wall_bianchi_jm5_2026-11-10_1030.py | 2a4339e26c97f3c4ca83db71291418e7e3dd4beaaf9b5c4649bcc1791d0c7336 | 10:24:37.413 | 444 |
| log /workspace/mr2-c2e8-1010/c2p_wall_bianchi_jm5_2026-11-10_1030.log | ef281a27920832a323e0e61bee572b44b73e38284f40be7b2ec5b37c00837a21 | 10:27:09.825 | 444 |
| reports/ copy of script | 2a4339e2… (identical) | 10:29:48.257 | 444 |
| reports/ copy of log | ef281a27… (identical) | 10:29:48.257 | 444 |
| wrapper .exit | "exit 0", no sidecar | 10:27:09.993 | 644 (unchanged; not frozen, as noted in e2750e28 §1) |

All match e2750e28 §1. **The erratum is additive.**

## 2. The 12 fixes (e2750e28 §8) compared with the erratum
| fix | e2750e28 requirement | erratum | verdict |
|---|---|---|---|
| 1 (priority) | State Or₊ (Or + Or orientation of Σ has ∫_{S⁴}J = +2N); rows 3, 8, 9, 10, 13 and 22a depend on it | "Fix 1": Or₊ stated verbatim with the M5/MN flux-sign gloss; lists rows 3, 8, 9, 10, 13 and parent 22a as implications of Or₊; weaker than BPS, not proved | faithful |
| 2 (priority) | Row 1: withdraw simplify==0 and 25-digit Hodge match; cite X₁⁵ = 1/8, U by expand, block Hodge argument, C1–C5; "nowhere zero" for the density vs vol_fib | "Fix 2": both withdrawn (corroboration only); C1–C5 cited item by item; density J_fib/vol_fib = ±κUD^{−7/6} nowhere zero; coordinate component vanishes only at sin α·μ₁μ₂ = 0 | faithful |
| 3 (priority) | Row 7: exact invariant-polynomial identity (C7) replaces 8.6e-42; GL integrals not grounds | "Fix 3": as required, incl. ⋆² = +1 exact; GL integrals (2, ±4, 0) float, not grounds | faithful |
| 4 (priority) | Row 2: ∫G₄_fib = −π² exactly (C6) instead of 2.7e-11 | "Fix 4": as required, independent of 5511845e; 2N = 9760 in-repo (bd47ff5e / 5511845e) | faithful |
| 5 (priority) | Row 10: exact j* = 8784√2/5 ≈ 2484.490386377 on μ₁ = 1; j ≤ 2484; COND → PROVED as implication with index-normalisation premise; E₈ index facts stay in row 11 | "Fix 5": all items present; premise Q_gauge,fib = −(j/4)p₁(Λ²±)_fib, tr = Tr₂₄₈/30 written out; overshoot ≈ 9.9e-7 recorded; row 11 COND | faithful |
| 6 (priority) | Row 13: COND → PROVED as implication; exact adverse min 1 − 5√2/17568; drop or prove float favourable min | "Fix 6": regrade with premises (HW, unbackreacted wall, Or₊, index-1 normalisation); exact min on μ₁ = 1; favourable 1 + R_j > 1 as in e2750e28 row 13; float 1.00001423041894 dropped | faithful |
| 7 | Row 4: name dG₄ = 0 for MN2 uplift as premise | "Fix 7": as required; V2 numerical dG check not grounds | faithful |
| 8 | Row 14: no conflict with cc21b272 row 18; M-loc with localized backreaction OPEN | "Fix 8": both stated; M-s survives | faithful |
| 9 | Tally 12/2/3/0 = 17 + 1 bookkeeping | "Fix 9": 12/2/3/0 = 17 + 1; PROVED rows 1–10, 13, 14; COND 11, 12; OPEN 15–17 | faithful |
| 10 | Row-22 split: 22a PROVED as implication of Or₊ etc., 22b OPEN; parent 18/2/4/0 = 24 + 1; none adopted | "Fix 10": 22a/22b as in e2750e28 §7 incl. witnesses; COND rows D4 and row 8; OPEN 16, 19, 22b, 23; row 23 OPEN; 12′ scoped; 22a not adopted | faithful |
| 11 | Carry stale lift-status correction from 27c61e09 (lines 8, 72, 133) | "Fix 11": lines 8, 72, 133 named; dd5a3a25 10:22:17 and e7bc37a1 10:29:10 cited; no grade effect. PP checked those three report lines: all are "lift … pending PP" status text (line 72 names only the E-T lift; the erratum's quoted gloss is a paraphrase of the three lines together) | faithful (paraphrase nit) |
| 12 | Process: wall-clock stamp + script sha at log start; freeze/sidecar .exit or stop writing it | "Fix 12": accepted for future runs; records that the 79795981 log has no wall-clock stamps and that PP's timing inference is consistent, not proof; re-run identical modulo timers | faithful |

All 12 fixes are folded. No misses, no misstatements. Exact values cross-checked numerically (no new mathematics): 8784√2/5 = 2484.4903863770…, 1 − 5√2/17568 = 0.9995975029706…, both as in e2750e28.

## 3. Grades and tallies — no unexpected change
- Only grade changes: rows 10 and 13, COND → PROVED as implication, exactly as ruled in e2750e28.
- Rows 1, 2, 7 stay PROVED (grounds replaced); rows 3–6, 8, 9, 14 PROVED (implication where ruled); rows 11–12 COND; 15–17 OPEN. Filing tally 12/2/3/0 = 17 + 1 bookkeeping.
- Parent cc21b272: 22a PROVED as implication (Or₊), 22b OPEN; 18/2/4/0 = 24 + 1 bookkeeping. Unadopted.
- Branch status: B1-c2′ COND overall, not adopted; 8399be55 COND; physical 1a datum OPEN; 1a not adopted; Group A the KK scope; literal c2 REFUTED (scoped); t4436 unchanged. Nothing adopted under t433u.
- Erratum states tip 7cddb188 MATCH, Junction UNSOLVED, no CERT ✓.

## 4. Nits (no grade effect; no erratum required)
- N1. Title line duplicated (line 1 and line 4 identical).
- N2. Erratum and sidecar left at mode 644 (consistent with MR2's series).
- N3. Fix 11 quotes a single gloss ("E-S± and E-T lift restorations still pending PP") for three lines whose wording differs; substance correct.
- N4. Authority paragraph says B1-c2′ "is not the KK scope" — consistent with e2750e28 (Group A is the chosen KK scope); wording only.

## 5. Verdict
**FAITHFUL with nits.** No required fixes. No grade changed by this confirm. Nothing adopted. Tip 7cddb188 untouched. **Junction UNSOLVED. No CERT.**

Sha of this findings file: see its .sha256 sidecar (written after header time was confirmed equal to the mtime).
