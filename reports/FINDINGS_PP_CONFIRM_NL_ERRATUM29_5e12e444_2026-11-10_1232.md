# FINDINGS: PP confirm of NL Erratum 29 (5e12e444), accepting PP audits of the two 12:09 t552u BPS filings (FX 617bc443 / 9bfa9657; NEC 6ccc9ef4 / e7d3a64f)
2026-11-10, written 12:32:19 CST (America/Chicago). Author: **Professor Proof (PP), Soft SF confirm** (absorption check only; no first-prove). Additive new file; no existing file edited, renamed, deleted or chmod-ed. **Nothing adopted.** **Junction UNSOLVED.** No CERT. **D-B3 unclosed.** No metric invented, constructed or ruled out. MN2 not adopted. Wording: resonant algebra. No message sent (no SendToAgent, no SendToUser, no external send); the parent delivers.

## 0. Verdict
**FAITHFUL.** Leftover required fixes: **none.** Residual nits: R1–R3 (§4). Erratum tally **0/0/0/0** confirmed against the restated labels (body §11–§13), not just the header. FX **8/2/3/0 = 13 with A12 restated**; NEC **3/0/2/0 = 5 with B3 restated**. No label-class moves; A12 and B3 stay PROVED, accepted only as restated (E4-3 precedent).

## 1. Integrity (re-hashed by PP; each = sidecar)
| file | sha256 | mode / mtime CST |
|---|---|---|
| Erratum 29 NL_ERRATUM29_ACCEPT_PP_1209_BPS_NEC_2026-11-10_1227.md | 5e12e444f7549972dd2b46239fc0d4585268216b22f734eea8a70c5ce2e6d23c | 644 / 12:28:25.288 (header "written 12:28:25 CST" = mtime; filename _1227 is a name/time nit, not renamed) |
| PP FX audit FINDINGS_PP_AUDIT_NL_BPS_T552_FX_FIXED_SET_EULER_617bc443_2026-11-10_1223.md | 9bfa9657beee4ed9e8df9e87b6747b6182aa80e9920bdbcbceb729c3a1029e60 | 444 / 12:23:48.000 |
| PP NEC audit FINDINGS_PP_AUDIT_NL_BPS_T552_NONBPS_Z2_S5_NEC_6ccc9ef4_2026-11-10_1224.md | e7d3a64f8a65a66a8609a1c394930208d280a8e23657621ae4743b989ee9aec7 | 444 / 12:24:48.000 |
| NL 1209 FX | 617bc44358f0fb13a8e05d5dc20e102eee9916600bfbc8dd70fa6dcb1f57f297 | 644 / 12:09:21.126 (header "1209" nit, not edited) |
| fx_fixed_set_euler_exact_2026-11-10.py | 3ff3ae939a19e6e6fc8712449ae56f99de5ff2be18d365e32073a64139f66cef | 444 / 12:05:01.852 (line 48 dead code stays frozen) |
| fx_fixed_set_euler_exact_2026-11-10.log | c3b711e3950dde9046672a31846148f7d1983c4c353b98a3aa4f960d6e548cbf | 444 / 12:06:06.043; 40 [PASS] / 0 [FAIL] |
| NL 1209 NEC | 6ccc9ef4fa283436fbc221b422bc65054f2a6cc34e456439172d7b945b5b3539 | 644 / 12:09:21.126 (same nit, not edited) |
| z2_nec_necessary_exact_2026-11-10.py | 5d342df45b11605781d94a19540b8aeb02bb6a938c70b126ef047188359193b2 | 444 / 12:05:57.912 |
| z2_nec_necessary_exact_2026-11-10.log | 718cc019dfc994e321c1842c7ccbe32c351d64f399cbcbb96a1622e4d26c1efb | 444 / 12:06:06.367; 7 [PASS] / 0 [FAIL] |
| frozen face defs z2_centre_flow_faces.py | 21bcbc3f53eadaf74690f052fa37fb541c5b2c8e4f4bd547e841126e1f3ac641 | 644 / 2026-11-09 20:57:39.622 |
| E27 / E28 (hashed only to confirm unedited; contents not used) | 9ceaa00f7af6bf51e7f2be7ba78f1cf293f5006c14ecded4617f4c66265a5e51 / a8121c8c1636724af48434c95ddc6c88ed0cd401887a57b880a094431f549c1f | 644 / 12:23:15.561, 12:25:57.757 |

Evidence: evidence_pp_confirm_nl_erratum29_5e12e444_2026-11-10/ — integrity_hashes.txt ff07b4e4915dd70bd9475fca66e7f8c67ed1eca436a552fced69b07fa23fbeda; absorption_checklist.md 7166d602db2184ed1094bf82b284b63642a278d6c62bc09cda384323ba219d08 (each = sidecar, mode 444).

Not used as inputs: E27 (9ceaa00f) and its PP confirm 689bca8b; E28 (a8121c8c) and its PP confirm; 1205 filings and audits/addenda; 1142 (e7312edb) and e073f0ef; Local jobs; MR2. E29 correctly states E27/E28 were pending and not grade inputs. (Timing note, parent only: E27 was confirmed FAITHFUL after E29 was filed; no bearing on this confirm.)

## 2. FX (9bfa9657) leftover fixes
- **F-1 (priority) — ABSORBED.** E29 §2 withdraws "A7(i)–(iv) and A10 all have cohomogeneity ≥ 4", citing the E4-6 main case (H_Σ × SO(3)_R × U(1)_R kept, face singular on all of C₄) in A10 and A7(iii) with **cohomogeneity 2**, where an (r, χ) system is exactly what is needed; records the cohomogeneity-3 singular H_Σ ∩ SO(3)_R and T²-type branches and that A7(iv) is not bounded by the count. Restated A12 (PROVED): counting 2/3/3/4/5 with H_Σ (+2 without), plus ≥ 4 with H_Σ (≥ 6 without) on **A7(i) and A7(ii) only**. A13 stays OPEN, widened to A7(iii)/A10 of cohomogeneity 2–3 and A7(iv); "(B) fails by construction" dropped for those branches. Handled as a restatement, not an extra REFUTED row (§12 l.113). P8-2 stays CONDITIONAL.
- **F-2 (priority) — ABSORBED.** E29 §3/§11: A2 and A11 prose now c₂(W^±) = (c₁² ∓ 2χ − 3σ)/4; FX-2d already correct, ±2 unaffected; "as written, the W^− line of A11 is wrong"; A2 PROVED (exact); **A11 stays CONDITIONAL** (not upgraded).
- **F-3 — ABSORBED.** E29 §4: general (a,b) argument (s₃ ↦ −s₃ bijection; coincidences only at a = ±b with value 0); D-1 instance list corroboration only; |a| = |b|, q ≠ 0 via the extremal Γ^J eigenline, J = (generator)/|a| homotopic to the vacuum one under (lin).
- **F-4 (nits) — ABSORBED.** A1 step 2: 2q/w = ±1 forced by ε(p) ≠ 0; A8: Z closed and tame; T1 both lock orientations recorded; script line 48 dead code left frozen; "1209" header not edited.
- **E1-1 scope note — ABSORBED (no regrade).** E29 §6 matches audit: single-section gloss; with (reg) also over −n̂₀ and A5's premises, A5 gives a contradiction; E1-1 PROVED (impl.); E1-3 CONDITIONAL, not needed by A5.
- **Drops A3–A6 (already PP-ruled, t4436) — wording MATCHES audit §4.** Common premises identical: (h0), (h1), (P-a), (ii) D1 HW Γⁿε = ε, (or), (lin), (F-4top) or (F-4) [A6: (F-4) with vacuum twist degree, stated in E29 §4], Σ connected genus 2. A3: U(1)_R kept, (reg-F) on all of C₄ (incl. E2∩E1∩U(1)_R, E1∩H_Σ∩U(1)_R ([w])). A4: SO(2) ⊂ SO(3)_R kept, (reg-F) on F₄(n̂), incl. E5∩¬H_Σ and E1 branches with such a remnant. A5: [w]∩H_Σ for all Killing spinors incl. KK, regularity at one face point over each pole (see nit R1). A6: diagonal circles except |a| = |b| with every Killing spinor neutral, (reg-all) on both pole sections. Recorded as already-ruled drops, not new ones. E5-4, E2-4, E3, BPS S5 not reopened. **A7, A10, A13 not dropped** (kept OPEN, E29 §1).
- **FX tally — CONFIRMED** 8/2/3/0 = 13: PROVED A1–A6, A8, A12 (restated); CONDITIONAL A9, A11; OPEN A7, A10, A13 (widened). As filed: 7 PROVED + A12 not accepted as written. No label-class moves.

## 3. NEC (e7d3a64f) leftover fixes
- **F-1 (priority) — ABSORBED.** E29 §7: **(A−)** A′ = −√(…) ≤ 0 listed as a premise of B2's "(< 0)" and Σ clause, of B3, and of Z-N6; 2φ′ ≤ A′ itself needs no sign. B3 restated: **−V ≤ (9/2)A′² − 30λ′² − (3/2)w′²** (implication of B2, (HC), (A−)); (A−) necessary via (A′, φ′) = (1, 0); filed "|V| ≤ (3/8)·12A′²" held only where V ≤ 0, not in force for V > 0; counterexample (−1, −1, 0, 0), V = 18 > 9/2 recorded. B3 PROVED as restated, not REFUTED. PP spot re-check (sympy, exact): HC gives V(−1,−1,0,0) = 18.
- **F-2 (priority) — ABSORBED.** E29 §1/§8/§11: title and B3 scope → any flow of the (φ, λ, w) truncation with frozen CGR-uplift face data of 21bcbc3f; premises (Z-u), (Y15) PP NEC criterion, (HC) frozen Hamiltonian constraint, (A−) frozen branch; explicitly not an arbitrary 3-scalar truncation; (h0) and (ii) unused by B1–B3. B5 OPEN.
- **F-3 — ABSORBED.** E29 §9: MN2 corollary as implication only (flows approaching MN2 with scalar velocities → 0, continuity, (A−); comb → −5A′(MN2) = 5·2^{−2/3} > 0); exact V(MN2) = −3·2^{2/3} < 0; **MN2 not adopted** (also E29 l.24). PP re-check: at zero velocities A′(MN2) = −2^{−2/3}.
- **F-4 (nits) — ABSORBED.** E29 §10: Z-N5 arithmetic (12 − 30/4 = 9/2); identity −V − [(9/2)A′² − 30λ′² − (3/2)w′²] = −30(φ′ − A′/2)(φ′ + A′/2) (PP D4; PP re-expanded to 0 exactly); header nit not edited.
- **NEC tally — CONFIRMED** 3/0/2/0 = 5: PROVED B1, B2, B3 (restated); OPEN B4, B5. As filed: 2 PROVED + B3 not accepted as written. No drops. Z-2 stays CONDITIONAL; numerics not used.

## 4. Residual nits (no required fix; no grade effect)
- **R1.** E29 §1 A5 drop gives the branch as "[w]∩H_Σ for all Killing spinors"; audit §4 item 3 reads "E1∩H_Σ with an SO(2)_ξ ⊂ SO(3)_R remnant commuting with the twisted SL(2,ℝ)", with (tw) among A5's premises (audit A5 row; 617bc443 T552-A5). E29's phrase is the audit's own parenthetical, the [w] branch keeps the (μ₃,μ₄) rotation, and E29 says each drop holds only under its PP-audited premises, so the ruled scope is unchanged. Any later roll-up should quote the full audit §4 item 3 wording and (tw).
- **R2.** E29 filename _1227 vs header/mtime 12:28:25 — name/time nit only; not renamed.
- **R3.** Frozen 1209 headers "1209 CST" vs mtime 12:09:21 and stale mode 644 — nits, not edited.

## 5. Standing
Nothing adopted (N = 4880, charge 9760, 1a, B1-c2′, MN2 as a physical wall: not adopted). E₈ wall sector CONDITIONAL. No prior PP grade changes. Already-accepted drops E5-4, E2-4, E3, BPS S5 not reopened. S2-7, E1-3, P8-2, Z-2 stay CONDITIONAL. D-B3 unclosed. **Junction UNSOLVED.** No CERT. No metric invented.

Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md: **7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91**, mode 644, mtime 2026-11-06 14:38:54 CST; hashed at 12:30:37 (start), 12:30:49 (after evidence writes) and 12:31:59 CST (immediately before this write). Unchanged. Never opened for writing.

## 6. Draft message to Non Local Path (c42a467b-1920-48b8-9956-ff5de411c227) — priority: false; hold as FYI (not sent by PP)
> PP confirm of NL Erratum 29 (5e12e444): FAITHFUL. All leftover fixes from FX 9bfa9657 (F-1–F-4, E1-1 note) and NEC e7d3a64f (F-1–F-4) are absorbed: A12 restated with the cohomogeneity sentence withdrawn (E4-6 counterexample, coh 2), ≥ 4 on A7(i)/(ii) only, A13 widened; c₂(W^±) = (c₁² ∓ 2χ − 3σ)/4, A11 CONDITIONAL; B3 restated as −V ≤ (9/2)A′² − 30λ′² − (3/2)w′² with (A−) listed and scoped to the (φ, λ, w) truncation of 21bcbc3f; MN2 corollary as implication only. A3–A6 drop wording matches the audit. Tallies confirmed: E29 0/0/0/0; FX 8/2/3/0 = 13 (A12 restated); NEC 3/0/2/0 = 5 (B3 restated). No leftover required fixes. Nit only: in any later roll-up quote A5's drop branch in full (E1∩H_Σ with an SO(2)_ξ ⊂ SO(3)_R remnant commuting with the twisted SL(2,ℝ); (tw)). Filename _1227 nit, no rename. Nothing adopted. Junction UNSOLVED. No CERT. Tip 7cddb188 unchanged.
