# FINDINGS: PP confirm of NL Erratum 27 (9ceaa00f), accepting PP e073f0ef (audit of NL 1142 non-BPS gap e7312edb)
2026-11-10, written 12:28:08 CST (America/Chicago). Author: **Professor Proof (PP), Soft SF confirm** (absorption check only; no first-prove). Additive new file; no existing file edited, renamed, deleted or chmod-ed. **Nothing adopted.** **Junction UNSOLVED.** No CERT. **D-B3 unclosed.** Wording: resonant algebra. No message sent (no SendToAgent, no SendToUser, no external send). No metric invented.

## Verdict
**FAITHFUL.** Erratum 27 absorbs all 7 priority fixes of e073f0ef §8 with the required wording, and all 10 nits (N-8, N-9, N-10 acknowledged as optional or not actionable on frozen files, which is fine). **Leftover required fixes: none.** Residual nits only (§4). Erratum tally **0/0/0/0** confirmed. 1142 ruled tally **16/6/6/1 = 29** confirmed against the restated labels and the 1142 §5 item lists; **no label-class change**.

## 1. Integrity (PP re-hash; each = its sidecar)
| object | sha256 | mode | note |
|---|---|---|---|
| NL Erratum 27 NL_ERRATUM27_ACCEPT_PP_e073f0ef_NONBPS_GAP_1142_2026-11-10_1221.md | 9ceaa00f7af6bf51e7f2be7ba78f1cf293f5006c14ecded4617f4c66265a5e51 | 644 | header "written 12:23:15 CST" = mtime 12:23:15.561 ✓; sidecar content MATCH; sidecar records a **full path** (nit R-2); filename _1221 vs 12:23:15 (nit R-1, do not rename) |
| PP e073f0ef FINDINGS_PP_AUDIT_NL_NONBPS_TENSION_CHARGE_GAP_e7312edb_2026-11-10_1211.md | e073f0ef804d788043a08c0d06d6e5b3a0e288dca3695c9f194fc69d14350bca | 444 | mtime 12:11:36.705; unedited |
| NL 1142 (frozen) | e7312edb8e4b5ad3d104c779688d7842a9e7b5deb3aaafe6176de1bfe94fe4bd | 644 | mtime 11:42:33.784; unedited |
| nonbps_gap.py (frozen) | e483f4b183773da0e3791cacc0ba27d93f56e55cbba8fc4a4208d29af5dbbe12 | 444 | unedited |
| nonbps_gap_run.log (frozen) | bf2484a6718be693dcca5802c8f8bf6791894b9f8213cf738f0adf4f3b7c6402 | 444 | 23 `[PASS]` / 0 `[FAIL]`; unedited |
| OW t4431, OW t552u (extra authorities cited by the erratum) | f700141d3ee862c7b077b0f67db5fb03b3adc56808c927ba1dd016c88910b1ec / eae1b39d635c69966a2b32642d395ae402d3c33fcf64db7f0b77cad2d8c60db2 | — | = sidecar; cited prefixes match |
| PP confirm of Erratum 26 | f2e64d448127af7b90bf7d1a4353b7c5e1342cae927b30f75d544cd53a5b1c0d | — | hashed only; **not an input** here |
| 12:05 filings debc7d52 / dff93e21 | debc7d52665491781a9017a9214fbd81686f8a0f6e256006c88cee07ca65f48f / dff93e2142227c8713bc2c5343141aeb83a2759f6d88763c7a0fe1c1da3a9970 | — | hashed only (unedited); not read for this confirm, not mixed in. Their audits/addenda and NL Erratum 28 were not opened |

Evidence: evidence_pp_confirm_nl_erratum27_9ceaa00f_2026-11-10/ (integrity_hashes.txt 7c9ba24c3e320f3c30c53728a2f6ef7ad14a1cafb1d7dab78b8b789d5f3e94a6; absorption_checklist.md 3780c4ae8477857e489d695aaca9c446fee1fb2d388317ff87dd0e19e44facf0; tip_custody_after_write.txt written after this file). All 444 with 444 sidecars.

## 2. Priority fixes (each checked against the restated wording, not NL's "all absorbed" claim)
1. **A5** (Erratum §2, §10): PROVED only for n = 0, any u > 0, any Δ_N ≥ 0 (A3 + Q9 + connectedness; N₋ = 0, N₊ = Q). n > 0 CONDITIONAL on A4 (citation not upgraded; only targets ≥ ε_ex(A₀) proved without A4). n < 0: target ≥ 2u|n|, counterexample u = 2, n = −1, Δ_N = 0 (1 < 4) acknowledged. PROVED kept. **Absorbed.**
2. **GB8** (§3, §10): g = u·e_u − n **+ 2N₋** − Δ_N; filed sign wrong except at N₋ = 0 (R9's form, A9's case); differs by −4N₋. PROVED kept. Checked against 1142 line "g(b) := u·e_u(n,b) − n − 2N₋ − Δ_N(b)" and 1142's own closure ε_ex = Δ_N − 2N₋ − (u−1)n, which agree with the fix. **Absorbed.**
3. **GB3/A7/A11** (§4, §10): constant unbackreacted face, W ∝ Δ̃, fibre-only legs and dependence, source-free D(W⋆₄F) = 0, W analytic non-constant, full HW system GA7b CONDITIONAL; "twisted (Σ-legged, sourced) blocks are not covered"; A11 same scope; GB4 on-shell virial / GB6′ not for twisted blocks. GB3 is **not** applied to twisted blocks anywhere in the erratum. **Absorbed.**
4. **A9** (§5, §10): (xi) strict non-BPS by Y14 S2-2 (CONDITIONAL per 077e417d), not GB3; (vii) branch continuity **assumed** at n ≈ 115; (viii) same-branch UV landing e_u(UV) < 19865/6 at n = 115 (= (19520/3 + 115)/2 ✓); (ix) UV as a limit / continuity of g or finite b₂; (x) Δ_N(b) continuity. A9 CONDITIONAL; A9′ OPEN. 9760, N = 4880, 14043/5 (= 2808.6), 19520/3 only as labelled CONDITIONAL test targets, not adopted. **Absorbed.**
5. **V′** (§6, §10): (a) n = 0 scope; (b) "on constant warped faces, for fibre-only fields obeying the stated equation (GB3); twisted blocks CONDITIONAL (Y14 S2-2)"; round UV face outside GB3. V′ CONDITIONAL. **Absorbed.**
6. **A7** (§7, §10): "only by zero-size (point) instantons" dropped; "not realized by any smooth static fibre-only field in GB3's class; zero-size objects need I (CONDITIONAL)". PROVED (impl.) with GB3 scope, u = 1, N₋ = 0. **Absorbed.**
7. **A1** (§8, §10): premises R5, S1, N, x-tension = energy density, source set {E₈ YM, positive-tension M5/anti-M5}, C∧X₈ OPEN, [u ≥ 1]; u < 1 negative Δ_N kinematically closable (Q1c), only N_req ≥ uQ survives; A2 companion stated. **Absorbed.**

No partial absorption found: no scope dropped, no citation upgraded, nothing adopted, D-B3 not closed, A13 REFUTED only as scoped (does not close D-B3 or the junction).

## 3. Nits N-1 to N-10
N-1 ✓ (Fix 4: "not reached within the computed range n ≤ 160 (e_u)"; e vs e_u stated; (155, 160]). N-2 ✓. N-3 ✓ in substance (see R-3). N-4 ✓. N-5 ✓. N-6 ✓. N-7 ✓. N-8 acknowledged (optional su(2) background not done; fine). N-9 acknowledged (frozen log cannot gain a RUN_START line; fine). N-10 acknowledged, no chmod (fine).

## 4. Residual nits (non-blocking)
- R-1. Filename _1221 vs written/mtime 12:23:15 CST. Name/time nit only; do not rename.
- R-2. Erratum sidecar records the full path (/workspace/quantum-comp/reports/…) rather than a basename; content MATCH.
- R-3. N-3 is absorbed by reference ("under the trace/orientation convention of the filing") rather than naming it (e.g. the sign of tr and the S⁴ orientation fixing ⋆ under which n_inst = (1/16π²)∫tr F∧F ≥ 0 ↔ SD). Optional.
- R-4. Erratum §11 reprints other tallies (1120 22/16/5/2 "and Erratum 26", 1711, 1800, Y14, "E24–E26 0/0/0/0 each"). These are references, not inputs to the fixes, and were not re-verified by this confirm. Erratum 26 / f2e64d44 is not an input to the absorption.
- R-5. Optional §4 audit remarks not in §8 (GB5 explicit hypotheses; GB7 twisted-functional remark) are not restated; GB7 is kept "as filed". Not required by §8.

## 5. Tally
- Erratum 27: **PROVED 0 · CONDITIONAL 0 · OPEN 0 · REFUTED 0 = 0** (bookkeeping, scope relabels, premise restatements only). Header = §12 body ✓.
- 1142 as ruled: **PROVED 16** (GB0, GB2, GB3, GB4, GB5, GB6, GB7, GB8, GB9, A1, A2, A3, A5, A7, A10, A11) · **CONDITIONAL 6** (GB1, GB6′, A4, A9, A14, V′) · **OPEN 6** (A6, A8, A9′, A12, A15, A16) · **REFUTED 1** (A13) = **29**. The erratum's lists equal 1142 §5 row for row, and every restated label in §2–§10 keeps its class. Other standing tallies unchanged by this file. E₈ wall sector stays CONDITIONAL (O5).

## 6. Custody
- Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md: sha **7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91**, mode 644, mtime 2026-11-06 14:38:54 CST. Hashed at 12:25 CST (start), at 12:27:43 CST (immediately before this write: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91), and after this write (recorded in evidence_pp_confirm_nl_erratum27_9ceaa00f_2026-11-10/tip_custody_after_write.txt; expected and required value 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91). Never opened for writing; not chmod-ed.
- Erratum 27, e073f0ef, 1142, nonbps_gap.py, nonbps_gap_run.log and sidecars: read and hashed only. Running Local jobs (s1e, chain_v2, s2e, wait_then_ob_v5, ob_v4), other agents' directories, MR2 files, the 12:05 and 12:09 filings and their audits/addenda, Erratum 26 and NL Erratum 28: untouched.
- New files: this file, its sidecar, and the evidence directory above.

## 7. Draft reply to Non Local Path (c42a467b-1920-48b8-9956-ff5de411c227), **unsent**; priority: false (held FYI)
> PP confirm of NL Erratum 27 (9ceaa00f): FAITHFUL to PP e073f0ef §8. All 7 priority fixes (A5 n=0 / n>0 COND on A4 / n<0 floor 2u|n|; GB8 +2N₋; GB3/A7/A11 constant unbackreacted face, fibre-only, source-free, twisted blocks not covered; A9 gates vii–xi with S2-2 COND not GB3; V′ scopes; A7 wording; A1 premises and u<1 companion) and N-1–N-10 absorbed. No leftover required fixes. Residual nits only: filename _1221 vs 12:23:15 (do not rename); sidecar uses a full path; N-3 convention given by reference, not spelled out. Erratum 0/0/0/0; 1142 stays 16/6/6/1 = 29, no class change. Frozen 1142 / nonbps_gap.py / log unedited (23/23). Tip 7cddb188 untouched. Nothing adopted. D-B3 unclosed. Junction UNSOLVED. No CERT. 12:05 package not mixed in. Findings: /workspace/quantum-comp/reports/FINDINGS_PP_CONFIRM_NL_ERRATUM27_9ceaa00f_2026-11-10_1228.md.

Nothing adopted. Tip 7cddb188 untouched. Junction UNSOLVED. No CERT. D-B3 is not closed. Resonant algebra.
