# FINDINGS: PP confirm of NL Erratum 28 (a8121c8c), accepting PP audits of the 12:05 gap (debc7d52) and junction (dff93e21) filings and both 12:24 addenda
2026-11-10, written 12:29:40 CST (America/Chicago). Author: **Professor Proof (PP), Soft SF confirm** (absorption check only; no first-prove). Additive new file; no existing file edited, renamed, deleted or chmod-ed. **Nothing adopted.** **Junction UNSOLVED.** No CERT. **D-B3 unclosed.** No metric invented, constructed or ruled out. Wording: resonant algebra. No message sent (no SendToAgent, no SendToUser, no external send); the parent delivers.

## Verdict
**FAITHFUL.** Leftover required fixes: **none.** Residual nits only (section 5).

## 1. Integrity (PP re-hash, all = sidecar)
| object | sha256 | mode | mtime CST |
|---|---|---|---|
| NL Erratum 28 NL_ERRATUM28_ACCEPT_PP_1205_GAP_JUNCTION_2026-11-10_1225.md | a8121c8c1636724af48434c95ddc6c88ed0cd401887a57b880a094431f549c1f | 644 | 12:25:57.757 (header 12:25:57) |
| PP gap audit ..._debc7d52_2026-11-10_1221.md | 087acf470ba1c28bf14b94b106fccff1b5f100a65806849f5383d3b37ac9e6f8 | 444 | 12:21:27 |
| PP gap addendum ..._debc7d52_2026-11-10_1224.md | 3844d94d10f361a5a006764a669141f80597af0b36d8f3b435618e48232a0602 | 444 | 12:24:15 |
| PP junction audit ..._dff93e21_2026-11-10_1221.md | f25a6d552630c1991d4c656ab6ac1c933967d1119642ee9ff232ca2636994a9e | 444 | 12:21:29 |
| PP junction addendum ..._dff93e21_2026-11-10_1224.md | d3e7306e3bbf383177bb575d149d7ac4a6611f8838de7ef95be09d37cba3ccc3 | 444 | 12:24:17 |
| frozen NL 1205 gap | debc7d52665491781a9017a9214fbd81686f8a0f6e256006c88cee07ca65f48f | 644 | 12:05:46.756 |
| frozen gapjx_gap.py | 516a87b7d9244cb05a43cad1c64497972cdd9d6281fe01ed629a1054a77161dc | 444 | 12:02:26.341 |
| frozen gapjx_gap_run.log (21 [PASS] / 0 [FAIL]) | 77895ba29852743273c6c6c964e0a3ca793d5031565834d9d5789545e7d03cc5 | 444 | 12:02:26.685 |
| frozen NL 1205 junction | dff93e2142227c8713bc2c5343141aeb83a2759f6d88763c7a0fe1c1da3a9970 | 644 | 12:05:46.776 |
| frozen gapjx_junction.py | b054521be0b458821afc7d6bf6d44ae48bb1ba41d2181e4f5f2217e6309a0ac9 | 444 | 12:02:26.341 |
| frozen gapjx_junction_run.log (10 [PASS] / 0 [FAIL]) | 6326cf4e2e81e345daedcb657722a9161719ab41dfefc088d0f33d0fb8787e3f | 444 | 12:02:28.213 |
| NL Erratum 27 (hashed only, to confirm unedited; not used) | 9ceaa00f7af6bf51e7f2be7ba78f1cf293f5006c14ecded4617f4c66265a5e51 | 644 | 12:23:15.561 |

All parents, scripts, logs and the four PP audit/addendum files are unedited (hashes, modes and mtimes as recorded at the 12:21 audits). Evidence: /workspace/quantum-comp/reports/evidence_pp_confirm_nl_erratum28_a8121c8c_2026-11-10/ — integrity_hashes.txt (7dae688e240fe0b5e251edf80bfe6ff9b667ecabd7589d5a016fb08271710d37) and absorption_checklist.md (94355db14bfc428e9ec53539cb41c56659ca800beeb78e21951a42eb05578646), each mode 444 with a .sha256 sidecar.

Not used as inputs: Erratum 27 and any PP confirm of it (treated neither as FAITHFUL nor as a proved input); the 12:09 BPS filings 617bc443 / 6ccc9ef4 and their PP audits 9bfa9657 / e7d3a64f; running Local jobs; MR2 files; other agents' directories; the 1130 script/log; 1120 / E26 only as already-ruled citations.

## 2. Gap (debc7d52): F-1 to F-5, as updated by addendum 3844d94d
| fix | required | erratum | verdict |
|---|---|---|---|
| F-1 | H2: P1 is the pointwise identity itself (PP-verified, PG2), not "1142 P1"; W real-analytic, non-constant, W_min > 0; ε, q in N-1 units | §2; §15 H2 | **Absorbed** |
| F-2 (addendum) | A12-a PROVED for sufficiency/kinematics only; "Δ ≥ 0 is also necessary (1142 A10)" is a citation of scoped 1142 A10 (PROVED as an implication, [u ≥ 1], GA2/P-b CONDITIONAL), outside A12-a's own PROVED content | §1, §3; §15 A12-a | **Absorbed.** A10 is cited, not absorbed into A12-a; no silent upgrade |
| F-3 (addendum) | A6-n: N₋ ≤ Δ_N/2 names the Bogomolny floor e_u ≥ \|n\| with u ≥ 1 (Σ_i(u·e_u,i − n_i) ≥ 0); 1142 A1 PROVED as that implication with named bookkeeping premises | §4 (R5, S1, N, x-tension = energy density, source set, u ≥ 1); §15 A6-n | **Absorbed** |
| F-4 | A9-T label carries unadopted 2808.6, 19520/3, Q = 9760 and U-uniform compactness; optional n* = 173 at u = 2 | §5; §15 A9-T | **Absorbed**; optional n* = 173 recorded as sufficient-not-sharp at u = 2 |
| F-5 (addendum) | A8-R cites 1142 GB3 with ruled scope (constant unbackreacted face, fibre-only legs and dependence, source-free); twisted (Σ-legged, sourced) blocks under Y14 S2-2 CONDITIONAL (PP 077e417d) | §6; §15 A8-R(v) | **Absorbed**; GB3 not applied to twisted blocks |

Gap tally **7/6/4/0 = 17 confirmed** against the restated labels (§15 lists match PP 087acf47 §5 row for row). No grade moves. H6 PROVED as an implication of J1 IR data + H5 stage-2 ansatz premises, SO(3)×U(1) ansatz only, not a bound on general static fields. A9-T stays CONDITIONAL; A9-u OPEN; A9-g PROVED. D-B3 unclosed.

## 3. Junction (dff93e21): F-1 to F-7, as updated by addendum d3e7306e
| fix | required | erratum | verdict |
|---|---|---|---|
| F-1 (priority) | S4-2 CONDITIONAL with P-b, GA2, D-C, fixed unbackreacted face, stated wall δ(0)/curvature prescription; upgrade still needs boundary-term derivation (which G₄ components) and coefficient; not refuted | §1, §7; §15 S4-2 | **Absorbed** |
| F-2 (priority, addendum; load-bearing) | A15-2 CONDITIONAL on the scoped 1142 A1–A3 implications holding on the backreacted face, NOT "pending 1142 audit"; keep "does not transfer" (A9-T dichotomy, κ bound); A5 only n = 0 if carried; no automatic upgrade; 1142 A15 OPEN | §1, §8; §15 A15-2 | **Absorbed, following the addendum.** §8 states the scoped-transfer gate and explicitly rejects the pre-addendum "pending 1142 audit" wording; names x-tension = energy density and the source set as the premises that must hold on the backreacted face; A2 (u < 1 companion), A3 (n = 0, off-shell range) scoped; A5 n = 0 only, n > 0 CONDITIONAL on A4, n < 0 false as written (floor 2u\|n\|); GB2/P1 kept as identity and H2 with its own premises; "does not transfer" kept. Not upgraded |
| F-3 | GA9-1/2 labels name block-averaged source model; O(N) and ≈ 3253 / ≈ 4190 CONDITIONAL (test targets 16266.7 / 12568.6, J1/J5 scaling) | §9; §15 GA9-1/2 | **Absorbed** |
| F-4 | premise J1 vs test ID J1 disambiguated; frozen script not edited | §10 (reading-only J0–J9 → JX0–JX9; "given J1" always the premise) | **Absorbed**; gapjx_junction.py b054521b… unchanged, 444 |
| F-5 | A15-1 / §1: Z₂ Israel convention S = −(2/κ²)(K − hK), staticity K_tj = 0, Poincaré symmetry | §11; §15 A15-1 | **Absorbed**; PJ8 general-e / max-eig(K\|Y₆) ≤ k_t recorded without grade change |
| F-6 (addendum) | GA9 cites 1120 D-D (given J1); 1142 A13 REFUTED only under its stated hypotheses; no D-B3/junction closure; not automatic on a backreacted face | §12; §15 GA9 | **Absorbed** (all six A13 hypotheses listed) |
| F-7 | S4-1: P-b or double cover drops the wall term; degree 4 by hand only | §13; §15 S4-1 | **Absorbed** |

Junction tally **5/7/3/0 = 15 confirmed** against the restated labels (§15 lists match PP f25a6d55 §5 row for row). The two moves (S4-2, A15-2: PROVED → CONDITIONAL) are accepted as already ruled by PP f25a6d55 and reaffirmed by d3e7306e; no new moves are created. GA9, S4-4 and A15 stay OPEN. No backreacted metric constructed or ruled out. Junction UNSOLVED.

## 4. Erratum tally
**0/0/0/0 confirmed.** Header (L27) = body §17. Every §15 relabel keeps its ruled label class; the only class changes on record are the two already-ruled junction moves, counted against the 1205 junction tally, not here. Watch list clear: 2808.6 / 19520/3 / 9760 not adopted; GB3 not applied to twisted blocks; A15-2 not auto-upgraded; D-B3 and junction not closed; no metric invented; no frozen script edited; E27 cited only as pending and not grade-changing; 12:09 BPS audits not mixed in.

## 5. Residual nits (no fix required)
1. Filename says _1225; header and mtime are 12:25:57. Name/time only; do not rename.
2. §15 tally-line relabels for A12-a and A6-n abbreviate the 1142 scopes ("scoped 1142 A10"; "1142 A1, as that implication"); the full premises ([u ≥ 1], GA2/P-b; R5, S1, N, x-tension = energy density, source set) are in §3 and §4 of the erratum body. Acceptable.
3. S4-3's filed phrase "1142 A1's sign bound survives" (flagged in f25a6d55 as citing an then-unaudited item, not a leftover fix) is not re-scoped in the erratum. It may now be read as citing scoped 1142 A1 (implication); S4-3 stays CONDITIONAL; no grade effect.
4. Stale "E26 pending PP confirm" headers in both frozen 1205 filings stay nits; frozen headers not edited (correct).
5. Gap freeze/run same-second timing (12:02:26.341 / 12:02:26.685) stays a disclosed nit; byte-identical re-run.
6. Erratum and its sidecar are mode 644 (NL convention); no chmod requested.
7. The erratum lists E27 as "pending confirm". That remains NL's statement as of its write; this confirm takes no position on E27 and did not use it.

## 6. Custody
Written (additive only): this file, its .sha256 sidecar, and the evidence directory above (all 444). Nothing else created, edited, renamed, deleted or chmod-ed.

Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md: re-hashed at start, immediately before this write, and after this write: **7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91**, mode 644, mtime 2026-11-06 14:38:54 CST. Unchanged. Never opened for writing.

## 7. Draft message to Non Local Path (id c42a467b-1920-48b8-9956-ff5de411c227), priority: false (held FYI; not sent by PP worker)
"PP confirm of NL Erratum 28 (a8121c8c): FAITHFUL. All five gap fixes (F-1 to F-5) and all seven junction fixes (F-1 to F-7) are absorbed as updated by the 12:24 addenda 3844d94d and d3e7306e. A15-2 follows the addendum: CONDITIONAL on the scoped 1142 A1–A3 implications holding on the backreacted face, not on a pending audit; A5 n = 0 only; the A9-T / κ non-transfer remark is kept; no upgrade. Tallies confirmed: erratum 0/0/0/0; gap 7/6/4/0 = 17; junction 5/7/3/0 = 15 (S4-2 and A15-2 moves accepted as already ruled). No leftover required fixes. Nits only: _1225 filename vs 12:25:57; §15 relabels for A12-a and A6-n abbreviate the scopes given in full in §3–§4; S4-3's '1142 A1 sign bound survives' may now be read as citing scoped A1, no grade effect. Frozen 1205 filings, scripts and logs unedited (21/21, 10/10 PASS stand). E27 not used. Tip 7cddb188 unchanged. Nothing adopted. D-B3 unclosed. Junction UNSOLVED. No CERT. Resonant algebra."

Nothing adopted. Junction UNSOLVED. No CERT. D-B3 unclosed. No metric invented. Resonant algebra. PP findings.
