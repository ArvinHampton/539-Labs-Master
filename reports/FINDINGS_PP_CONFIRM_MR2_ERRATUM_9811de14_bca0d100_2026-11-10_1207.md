# FINDINGS — PP confirm of MR2 additive erratum bca0d100 of filing 9811de14 (backreacted near-plane metric; 9760-free δ²)
2026-11-10, written 12:07:54 CST (America/Chicago). Author: **Professor Proof (PP), Soft SF confirm**. Faithfulness confirm of wording, premises and bookkeeping absorbs only (F-1–F-7 and N1–N9 of PP audit 81291f84, plus addendum 7789f89a). Not a first-prove. No new script was written or run, and no existing script was re-run. Additive new file; no existing file edited, moved, renamed or deleted. **Nothing adopted.** No CERT. Nothing sent. Junction **UNSOLVED**. Wording: resonant algebra. Labels: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING.

Confirmed: `MR2_ERRATUM_PP_AUDIT_HW_BACKREACTED_METRIC_CHARGE_9811de14_2026-11-10.md`, sha256 bca0d1003786fd21dd5d9d4f120dd8bb522cc5d0d3feadac760879e0e0979ba1.

## 0. Authority and scope, including the L-GN gate
- **Authority:** PP audit 81291f84 (§8 is the absorb checklist). Its math rulings stand. Addendum 7789f89a supersedes it only on two bookkeeping items: (i) parent E₈ tally **18/2/4/0** (after the row-22 split, e2750e28 / 395bff64), not the stale 17/2/4/0; (ii) tip after-hash 7cddb188…. The rest of 9811de14 is not reopened.
- **L-GN gate.** MR2 erratum 7d8fb406 of f4ee61f2 claims an index-generic proof of L-GN (§2; script 1728d877…, log 20f66fe3…, 21/21 PASS). A separate PP confirm of 7d8fb406 is **in flight and not parent-accepted**. In this file, 7d8fb406 is cited **only as an already-filed, still-unconfirmed erratum**. It is not a proved input. Any in-flight confirm of it is also not used: an evidence directory for that confirm exists on disk; it was not opened and was not used. PP does not re-derive the Gauss–Codazzi–Ricci argument here and does not re-run the L-GN script.
- **Consequence:** GN-G stays **CONDITIONAL** on L-GN in this file. Accepting the F-1 *wording* absorb (scope to the D = 4 instance; name L-GN) does not discharge GN-G.
- **Not adopted and not used as inputs:** 9760, N = 4880, N ≠ 0 (P-N), P-Y₆, P-HWbc, 1a as the physical wall, P-bulk. No backreacted metric is invented. No f4ee61f2 grade is used or changed: 12/3/2/1 as ruled in 976e5621 stands until the other confirm is ruled. No NL or Local grade is used as a premise.

## 1. Integrity (re-hashed by PP this run; sha = sidecar = expected)
| record | file | sha256 | status | mtime | mode |
|---|---|---|---|---|---|
| erratum (target) | `MR2_ERRATUM_PP_AUDIT_HW_BACKREACTED_METRIC_CHARGE_9811de14_2026-11-10.md` | bca0d1003786fd21dd5d9d4f120dd8bb522cc5d0d3feadac760879e0e0979ba1 | MATCH (sidecar and expected) | 2026-11-10 12:03:55.456 CST | 644 |
| parent 9811de14 (not edited) | `MR2_BRANCH_ATTEMPT_HW_BACKREACTED_METRIC_AND_CHARGE_PREMISE_2026-11-10.md` | 9811de1490a88569860a3a2e3b04a5fe75387fc83eb1ba020221f72395150770 | MATCH (sidecar and expected) | 2026-11-10 11:39:48.332 CST | 644 |
| script 2d8092a7 | `mr2_hw_backreact_jet_charge_2026-11-10.py` | 2d8092a779b8ed5cf4118d05f054ff9ccf227dbe10fc754a93d645ba10c75d5c | MATCH (sidecar and expected) | 2026-11-10 11:36:54.253 CST | 444 |
| log 7634069f | `mr2_hw_backreact_jet_charge_2026-11-10.log` | 7634069fcc9700debd53ab57b7e10aca703cec460c630ca61034196933524dbb | MATCH (sidecar and expected) | 2026-11-10 11:37:53.281 CST | 444 |
| PP audit 81291f84 | `FINDINGS_PP_AUDIT_MR2_HW_BACKREACTED_METRIC_CHARGE_9811de14_2026-11-10_1157.md` | 81291f843da6d01e4bbba362e370a05436a19b6dd046d4987ea83f3c34b737d8 | MATCH (sidecar and expected) | 2026-11-10 11:57:23.551 CST | 444 |
| PP addendum 7789f89a | `FINDINGS_PP_AUDIT_MR2_HW_BACKREACTED_METRIC_CHARGE_9811de14_ADDENDUM_TALLY_CUSTODY_2026-11-10_1201.md` | 7789f89a788c011c42891d27e872060708bec71e02e703d590049ac2c80d05fa | MATCH (sidecar and expected) | 2026-11-10 12:01:34.000 CST | 444 |
| MR2 erratum 7d8fb406 of f4ee61f2 (CITED, PENDING PP confirm; not an input) | `MR2_ERRATUM_PP_AUDIT_HW_PLANE_RICCI2_WEYL2_f4ee61f2_2026-11-10.md` | 7d8fb4067a33c6f3530fd03610e15e981fe46e89c87660614b0d48b7c7ce6554 | MATCH (sidecar and expected) | 2026-11-10 11:59:12.674 CST | 644 |
| L-GN script 1728d877 (cited only) | `mr2_lgn_gaussian_normal_lemma_2026-11-10.py` | 1728d877918a96c8d91862483ade6b376ce6d91fdd531b1bb6881d138a3d0a50 | MATCH (sidecar and expected) | 2026-11-10 11:57:34.719 CST | 444 |
| L-GN log 20f66fe3 (cited only) | `mr2_lgn_gaussian_normal_lemma_2026-11-10.log` | 20f66fe318da09fcbaf192a923291fe31e1dbe9ca03de0dac59ffcff32a09177 | MATCH (sidecar and expected) | 2026-11-10 11:57:44.271 CST | 444 |
| f4ee61f2 (not used) | `MR2_BRANCH_ATTEMPT_HW_FIXED_PLANE_BOUNDARY_RICCI2_WEYL2_2026-11-10.md` | f4ee61f26ad536800792b510f29f714c9c622fd11a8c378e545a8a38976c330d | MATCH (sidecar and expected) | 2026-11-10 11:24:09.339 CST | 644 |
| QC note 66f04088 (not used) | `MR2_NOTE_QC_HW_FIXED_PLANE_BOUNDARY_RICCI2_WEYL2_f4ee61f2_2026-11-10.md` | 66f040887ebe660a6d540963b76f005ccd504e9d3e0f1a96b9b842b50f16e2bc | MATCH (sidecar and expected) | 2026-11-10 11:25:54.549 CST | 644 |
| PP 976e5621 (cited for scope only) | `FINDINGS_PP_AUDIT_MR2_HW_PLANE_RICCI2_WEYL2_f4ee61f2_2026-11-10_1140.md` | 976e56211308cf68e8ad80df063f99e08826d441e0f4d8a45242ad6fad01031c | MATCH (sidecar and expected) | 2026-11-10 11:40:51.800 CST | 444 |
| tip, before (start of this run, 12:05:45 CST) | `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | MATCH | 2026-11-06 14:38:54.160 CST | 644 |

Notes:
- **Erratum:** header "written 12:03:55 CST" = mtime 12:03:55.457 CST. Sidecar mtime 12:03:55.461 (after the file). Mode 644 (MR2 convention, N5). Sound.
- **Script and log copies:** both are `cmp`-identical to the copies in /workspace/mr2-hw-curv-1110/.
- **Addendum 7789f89a:** the sidecar-first gap (sidecar mtime 12:01:32.33, about 1.7 s before the file's 12:01:34.000) is already disclosed and the content matches. MR2 restates the disclosure in §0 and §10. No effect.
- **Other files:** parent 9811de14, script, log, 81291f84 and 7789f89a carry the same sha, mtime and mode as recorded in the authority files, so they are unedited.

Bookkeeping (integrity): **PROVED.**

## 2. Item-by-item absorb (81291f84 §8)
**Priority**
- **F-1 (rows 2–3): ABSORBED.**
  - Erratum §2 scopes J1–J3 to the D = 4 instance and discloses the one background jet (h0, h1 fixed rationals; only h2 symbolic), t-independence, and the single point (u, v) = (1/3, 1/5), y = 0. This matches the log J1–J3 header.
  - The general-D / D = 11 rider is carried as **GN-G, CONDITIONAL on L-GN**.
  - L-GN is restated consistently with 81291f84 §3 and 976e5621. It is **named, not proved**, in:
    - row 6 (§7: premise list includes L-GN; "falls under GN-G");
    - row 6b (§7: CONDITIONAL on GN-G / L-GN);
    - row 8 (§7: L-GN (GN-G) for the 11D 2-jet algebra);
    - row 9 (§6 F-6: "inherits GN-G (L-GN named)");
    - row 11 (§3: L-GN for non-diagonal or x-dependent walls).
  - 7d8fb406 is cited as "pending PP confirmation", and §2 states that 3G and GN-G are not treated as regraded. The GN-G regrade is made a *request*, not a self-upgrade (§1, §2). This is faithful.
- **F-2 (rows 11–12): ABSORBED.**
  - Row 11 premises are exactly {P-reg, P-Poinc, P-Israel, P-content incl. P-τ and "each M5 worldvolume ∋ t"}, with L-GN for non-diagonal or x-dependent walls, or else restriction to the diagonal x-independent K1–K3 model. No charge value is used.
  - Row 12's pointwise scope is stated precisely: non-gravitational density ≠ 0 (F ≠ 0, or an M5 density with τ > 0). Gravitational-only points (12b) and distributional point-like sources (outside P-reg) are excluded. Charge cancellation ≠ stress cancellation.
  - Nit (wording only, not required): row 12 says "the same set, plus P-Poinc", but P-Poinc is already in the set. The redundancy is harmless. It correctly records 976e5621 P7.5 as the reason P-Poinc is needed for strict positivity.
- **F-3 (row 13): ABSORBED.**
  - Erratum §4 premises: P-HW including the Z₂ fixing the plane and each S⁴ fibre pointwise; no off-plane sources (dG = 0 off the plane); P-HWbc (CONDITIONAL premise); P-N (**unadopted**); P-Y₆ (**unadopted**), with adopted D2 (cc21b272, under t433u as graded) applying only to that Y₆; P-content and P-τ.
  - D2 supplies the **integrated** n_R = 0, and the pointwise gravitational density stays in 12b.
  - N = 4880, 9760, N ≠ 0, P-Y₆ and P-HWbc are listed as not adopted. This is faithful to 81291f84 §4.
- **F-4 (row 14 / B-4): ABSORBED.**
  - The sentence "If the t433u reading stands, adopted D3 already gives n_inst + N_M5 = 9760 ≠ 0, and row 13 follows from it directly" is **withdrawn**, verbatim as in parent line 126.
  - The scoped reading of 81291f84 §6 is used. The records are compatible once scoped. D3 is adopted only as an implication identity on the 1a/MN2 face in HW normalisation, with the in-vacuum N = 4880. OW 1130's "unadopted" refers to 9760 as a physical wall charge premise. 1a is not adopted as the physical wall.
  - Answer: no adopted value attaches to the backreacted face, and 9760 is not needed. It is replaced by the weaker unadopted premise P-N, plus adopted D2 scoped by unadopted P-Y₆, plus P-HWbc, giving S ≢ 0. It is **not** replaced by an adopted value.
  - D2 (adopted, scoped) is distinguished from D3 (adopted only on the 1a face). No new Owner ruling is invented.
- **F-5 (row 7): ABSORBED.**
  - A is replaced by A′: f₂ = 0 (so tr F∧F = 0 and j = 0 consistently), f₁ = 1, τ = 0, κ² = 1, r = +1.
  - PP arithmetic check of the logged J6 polynomial (log 7634069f): −(3·1 + 8·1)/16 = **−11/16**. This agrees with 81291f84 P7.5. It is exact substitution, not a new claim.
  - B is robust: 1/4 + λ²/16 > 0 (P7.3), and B is what row 9 uses.
- **F-6 (row 9): ABSORBED.** Row 9 is retitled to the Gauss **scalar** constraint scope (REFUTED there only, via B). It states that simultaneous pointwise satisfiability of Codazzi (6b), the plane 4-form constraints and E₈ YM is **not exhibited**, and that row 9 has no bearing on row 10.
- **F-7 (§5 item 6): ABSORBED.** "Elliptic-type" is replaced by "Riemannian-signature bulk problem whose ellipticity (Lopatinskii–Shapiro …) is exactly the missing B-1".

**Nits**
- **N1: ABSORBED.** κ² convention (P-G unit coupling versus Israel κ²). No sign or grade effect.
- **N2: ABSORBED.** The Codazzi sign is pinned to + (log J3 "Codazzi sign found: +"; PP P1.5).
- **N3: ABSORBED.** The "diagonalisable" label is not needed (PP P3.1–P3.3, generic 10×10).
- **N4: ABSORBED.**
  - Primary cite: PP P9.1–P9.3 (exact), as required.
  - Secondary cite: MR2 log 20f66fe3 C2a–C2d (∫sech² = 2, ∫sech⁴ = 4/3 and the Cauchy–Schwarz cases are present in that log). Observation: these are elementary profile integrals from the log of a script whose parent erratum is still pending. They count as corroboration only; PP P9 is the ground. No grade depends on them.
- **N5: ABSORBED.** Filing mode 644 (convention). Frozen scripts and logs are 444. Nothing chmodded.
- **N6: ABSORBED.** The freeze/run same-second disclosure is recorded with no grade effect (not over-weighted).
- **N7: ABSORBED.** Row 5 is pinned at D = 11 by PP P4.0–P4.2 (330 symbolic components). MR2's own check was D = 6.
- **N8: PARTIALLY ABSORBED (non-blocking).** "Compact Y₆ plus Poincaré homogeneity" for uniform δ is stated. The 4-form gauge is **not named**; the erratum discloses that naming it is "still owed". This is honest disclosure, not a misstatement. Row 8 is CONDITIONAL in any case, and the gauge is one of its listed dependencies, so there is no grade effect. Carried as residual R-1 (§5).
- **N9: ABSORBED.** B-3 cites PP P6.1/P6.2, and row 6b stays CONDITIONAL on GN-G / L-GN and P-HWbc, plus N1.

**Addendum 7789f89a bookkeeping**
- **(i) USED.** Parent E₈ **18/2/4/0** appears in erratum §0 and §1, by citation only. The stale 17/2/4/0 is named only as the superseded figure.
- **(ii) USED.** Tip after-hash 7cddb188…, mtime 2026-11-06 14:38:54 CST, mode 644, as recorded in §0. The sidecar-first 1.7 s gap is disclosed.

**Other checks**
- Parent 9811de14, its script and log, f4ee61f2, QC note 66f04088 and 7d8fb406 are claimed unedited. PP re-hash agrees (§1).
- The claim "no new script" is consistent with disk: no new MR2 script or log is cited by this erratum.
- No self-upgrade anywhere.
- Blockers §9 are unchanged in substance. B-3 is discharged only as index algebra, B-4 is answered as a record row, and row 10 is not resolved by the absence of a file.

**Verdict: FAITHFUL.** All priority items F-1–F-7 are absorbed. N1–N7 and N9 are absorbed. N8 is partially absorbed, with the 4-form gauge disclosed as owed (non-blocking). Both addendum bookkeeping items are used.

## 3. GN-G: left CONDITIONAL; regrade request recorded as gated
- **GN-G** (the general-D / D = 11 rider of rows 2–3): **CONDITIONAL on L-GN.** It is not regraded here.
- **MR2's request** is to regrade GN-G to PROVED as an implication of L-GN if PP accepts 7d8fb406 §2 (proposed 10/3/1/2). It is **recorded as gated** on two steps: first the separate, still-pending PP confirm of 7d8fb406 §2, and then the parent's independent ruling on L-GN.
- **If L-GN is later accepted,** a general L-GN would be available to a later additive note or parent addendum of *this* confirm. This file does not write that regrade.
- 3G (976e5621) is untouched by this file.

## 4. Grades and tally of 9811de14 (ruled; unchanged by this confirm)
- **PROVED 9:**
  - 1
  - 2 [D = 4 instance]
  - 3 [D = 4 instance]
  - 4
  - 5 [incl. D = 11, PP P4]
  - 6 [implication, L-GN named]
  - 7 [examples; A scoped → A′ = −11/16]
  - 11 [implication, corrected premises]
  - 13 [implication, refined premises]
- **CONDITIONAL 4:**
  - GN-G (L-GN)
  - 6b (index algebra machine-checked by P6.1/P6.2; still depends on general-D Codazzi and P-HWbc)
  - 8 (CK and constraint propagation cited only; GN-G; compact Y₆; 4-form gauge owed)
  - 12b
- **OPEN 1:** 10 (the blockers are real; the absence of a file is not a resolution; no metric is invented).
- **REFUTED 2:**
  - 9 [Gauss-scalar scope]
  - 12 [implication, corrected premises]
- **= 16, plus 2 bookkeeping:** integrity PROVED; row-14 record answered (scoped-compatible).
- **Ruled tally: 9 PROVED / 4 CONDITIONAL / 1 OPEN / 2 REFUTED.** The proposed 10/3/1/2 is **not** ruled. It is gated as in §3.
- **Other standing tallies, by citation only and unchanged:**
  - parent E₈ **18/2/4/0**;
  - f4ee61f2 **12/3/2/1** (976e5621);
  - t4436 unchanged;
  - Bridge C PARTIAL;
  - E₈ wall sector CONDITIONAL.
- 9760 remains unadopted. Junction UNSOLVED (carried, not counted). No CERT.

## 5. Leftover required fixes
- **Required fixes: none.** The absorb is faithful.
- **Residual R-1 (non-blocking; nit N8, second half):** name the gauge used for the first-order 4-form system in row 8. It may go in a later additive note. No grade effect while row 8 is CONDITIONAL.
- **Optional wording nit:** row 12's "plus P-Poinc" duplicates a premise already in the set (§2 F-2). No change is needed.

## 6. What PP did not do
- PP did not first-prove or re-derive L-GN, did not re-run the L-GN script or the 9811de14 script, and wrote no new script.
- PP did not use 7d8fb406, or any in-flight confirm of it, as a proved input. PP did not open that confirm's evidence directory.
- PP regraded no row. GN-G stays CONDITIONAL.
- PP invented no backreacted metric. PP did not adopt 9760, N = 4880, N ≠ 0, P-Y₆, P-HWbc, 1a as the physical wall, or P-bulk.
- PP used no f4ee61f2, NL or Local grade as a premise, and changed none.

## 7. Custody
- **Tip** `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md`:
  - Before: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 at 12:05:45 CST.
  - **After all reads and hashing, re-hashed by the write step at 12:07:54 CST, immediately before this file's bytes were written:** 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, mtime 2026-11-06 14:38:54.160 CST, mode 644. **Unchanged.**
  - The tip is read only. It was never opened for writing and was not chmodded, and this write cannot alter it. The parent's independent post-write re-hash is the final custody check.
- **Read and hashed only:** 9811de14, its script and log (both copies), 81291f84, 7789f89a, 7d8fb406, the L-GN script and log, f4ee61f2, QC note 66f04088 and 976e5621. None was edited, moved, renamed or deleted.
- **Directories:** nothing was written in evidence_pp_audit_mr2_hw_backreact_9811de14_2026-11-10/, in evidence_pp_confirm_mr2_erratum_f4ee61f2_7d8fb406_2026-11-10/, or in any other agent's directory. No new evidence directory was created, because no new checks were produced.
- **Local jobs:** no running Local job was touched (s1e, chain_v2, s2e, wait_then_ob_v5, ob_v4).
- **Messages:** none sent. The parent delivers.
- **This file:** header time = mtime (set to the exact second, .000000000). The `.sha256` sidecar was written after the final bytes, and both files are chmod 444.

PP confirm only. Nothing adopted. GN-G CONDITIONAL. Ruled 9/4/1/2. Tip 7cddb188 untouched. Junction UNSOLVED. No CERT. Resonant algebra.
