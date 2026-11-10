# NL ERRATUM 28: accept PP audits of the two 12:05 filings (debc7d52 gap; dff93e21 junction)
2026-11-10, written 12:25:57 CST (America/Chicago). **NL derived proposal.** Author: Non Local Path (NL). Additive only. No existing file is edited, renamed, deleted or chmod-ed; the two 1205 filings, their sidecars, gapjx_gap.py, gapjx_junction.py, their logs and their sidecars stay frozen, and this erratum records the fixes. Wording: resonant algebra.

Frozen targets (read and hashed only, each sha = its sidecar):
- NL 1205 gap NL_DERIVED_NONBPS_GAP_FIXEDFACE_FLOW_PROFILE_RESOLUTION_2026-11-10_1205.md = debc7d52665491781a9017a9214fbd81686f8a0f6e256006c88cee07ca65f48f (mode 644).
- /workspace/nl-gapjx-t552-1110/gapjx_gap.py = 516a87b7d9244cb05a43cad1c64497972cdd9d6281fe01ed629a1054a77161dc (444).
- /workspace/nl-gapjx-t552-1110/gapjx_gap_run.log = 77895ba29852743273c6c6c964e0a3ca793d5031565834d9d5789545e7d03cc5 (444). Clean run, exit 0, **21/21 PASS**.
- NL 1205 junction NL_DERIVED_JUNCTION_GA9_S4_CX8_BACKREACT_LIMITED_2026-11-10_1205.md = dff93e2142227c8713bc2c5343141aeb83a2759f6d88763c7a0fe1c1da3a9970 (mode 644).
- /workspace/nl-gapjx-t552-1110/gapjx_junction.py = b054521be0b458821afc7d6bf6d44ae48bb1ba41d2181e4f5f2217e6309a0ac9 (444).
- /workspace/nl-gapjx-t552-1110/gapjx_junction_run.log = 6326cf4e2e81e345daedcb657722a9161719ab41dfefc088d0f33d0fb8787e3f (444). Clean run, exit 0, **10/10 PASS**.
- Frozen 1142 (e7312edb), 1120 (79ad0c64), Erratum 26 (a44b18d9), Erratum 27 (9ceaa00f), and the 1130 script/log: not edited.

Inputs, read in full (each sha = its sidecar; all mode 444):
- FINDINGS_PP_AUDIT_NL_NONBPS_GAP_FIXEDFACE_FLOW_PROFILE_debc7d52_2026-11-10_1221.md, sha 087acf470ba1c28bf14b94b106fccff1b5f100a65806849f5383d3b37ac9e6f8, written 12:21:27 CST.
- FINDINGS_PP_ADDENDUM_NL_NONBPS_GAP_FIXEDFACE_FLOW_PROFILE_debc7d52_2026-11-10_1224.md, sha 3844d94d10f361a5a006764a669141f80597af0b36d8f3b435618e48232a0602, written 12:24:15 CST.
- FINDINGS_PP_AUDIT_NL_JUNCTION_GA9_S4_A15_dff93e21_2026-11-10_1221.md, sha f25a6d552630c1991d4c656ab6ac1c933967d1119642ee9ff232ca2636994a9e, written 12:21:29 CST.
- FINDINGS_PP_ADDENDUM_NL_JUNCTION_GA9_S4_A15_dff93e21_2026-11-10_1224.md, sha d3e7306e3bbf383177bb575d149d7ac4a6611f8838de7ef95be09d37cba3ccc3, written 12:24:17 CST.

The parent accepts both 12:21 findings. The 12:24 addenda update 1142 citations only, because 1142 is now ruled by PP e073f0ef (16/6/6/1 = 29, no label-class changes, D-B3 unclosed). Erratum 27 (9ceaa00f) absorbs those 1142 scope relabels and is pending PP FAITHFUL confirm; it is not an input that changes any grade here. The 12:21 findings correctly treated 1142 as unaudited at the time they were written; this erratum follows the addenda for those citations.

PP evidence (read-only) /workspace/quantum-comp/reports/evidence_pp_audit_nl_t552u_gapjx_2026-11-10/: gap re-run byte-identical (21/21); independent checks 23/23 PASS; junction re-run byte-identical (10/10); independent checks 12/12 PASS.

Authority: OW t552u (eae1b39d…; Owner verbatim "Pursue all for resolution.", transcript-verified), OW 1130 (945d81bb…), OW 1117 (bff79185…), OW 1108 (c6375f85…), standing OW t4436 (32881263…), OW t4431 (f700141d…). Each re-hashed = sidecar. The t552u Interpretation section is not a new Owner ruling.

Not adopted: N = 4880, charge 9760, Δ_N(IR) = 2808.6 = 14043/5, Δ_N(UV) = 19520/3, and the M5-unit figures remain labelled CONDITIONAL test targets. 1a and B1-c2′ are not adopted. The E₈ wall sector stays CONDITIONAL, gated by backreaction (O5). Nothing adopted by fiat. **Junction: UNSOLVED.** D-B3 stays unclosed. No backreacted metric is constructed or ruled out (MR2's 1130 lane). No CERT, no Gemini, nothing sent at write. Tip 7cddb188… checked before and after the write.

**Tally: PROVED 0 · CONDITIONAL 0 · OPEN 0 · REFUTED 0 · total 0.**
This erratum contains **only bookkeeping, scope relabels, and acceptance of two PP grade moves of already-filed junction rows**. Distinct new claims (for any roll-up): **0/0/0/0**. The two grade moves are recorded against the 1205 junction tally, not as new items here.

## 1. Accepted ruling
- **Gap (debc7d52): grades stand, 7/6/4/0 = 17.** No grade moves. H6 is PROVED as an implication of the J1 IR data and the H5 stage-2 ansatz premises (SO(3)×U(1) ansatz only; κ_IR = 1/20 exact). A9-T stays CONDITIONAL. A12-a is PROVED for sufficiency/kinematics only. D-B3 stays unclosed.
- **Junction (dff93e21): ruled tally is 5/7/3/0 = 15** (NL claimed 7/5/3/0). Two grade moves, both accepted:
  - **S4-2: PROVED → CONDITIONAL.** The boundary term is only a sketch ("∝"), with no coefficient and no test, and it depends on the δ(0)/wall-curvature prescription that S4-4 lists as OPEN. Split-invariance needs D-C (CONDITIONAL) and a fixed unbackreacted face, neither named in the filed label. Not refuted.
  - **A15-2: PROVED → CONDITIONAL.** Acceptance of the 1142 audit does not automatically upgrade this row. 1142 A1–A3 are now PROVED on their stated domain, but transfer "verbatim" to a backreacted face still requires those bookkeeping premises (in particular x-tension = energy density, and the source set) to hold there. 1142 A15 remains OPEN. If the row is also read as carrying A5, that is PROVED only for n = 0.
- Integrity: all hashes match; gap 21/21 PASS, re-run byte-identical, independent checks 23/23; junction 10/10 PASS, re-run byte-identical, independent checks 12/12.
- GA9, S4-4 and A15 stay OPEN. No backreacted metric was constructed or ruled out. Junction UNSOLVED.
- Other standing tallies are unchanged: 1120's ruled 22/16/5/2, 1142's ruled 16/6/6/1, Bridge C PARTIAL, t4436, parent E₈. The 12:09 BPS/NEC filings are not regraded here.

## 2. Gap Fix F-1 — H2 premises
H2 stays **PROVED** as an implication. List **P1 as the pointwise identity itself** (ε ≥ |q|/2, verified exactly in this audit, PG2), not as "1142 P1" and not on 1142's authority. Premises of strictness: **W real-analytic, non-constant, W ≥ W_min > 0**. Units: ε, q in the N-1 instanton convention. Strictness follows without needing self-duality: equality forces ε = 0 off the null set {W = W_min}.

## 3. Gap Fix F-2 — A12-a scope
A12-a stays **PROVED for sufficiency / kinematics only** (exact identities, x-block only; force balance is not addressed). The sentence "Δ ≥ 0 is also necessary (1142 A10)" is a **citation of 1142 A10**, now ruled PROVED as an implication with **[u ≥ 1] and GA2/P-b** (CONDITIONAL) in the label. That citation is absorbed here as a scoped citation; it remains **outside A12-a's own PROVED content**.

## 4. Gap Fix F-3 — A6-n floor
A6-n stays **CONDITIONAL**. The clause "N₋ ≤ Δ_N/2" needs the Bogomolny floor **e_u ≥ |n| with u ≥ 1**, i.e. Σ_i(u·e_u,i − n_i) ≥ 0. 1142 A1 is now PROVED as that implication of the named bookkeeping premises (R5, S1, N, x-tension = energy density), the source set, and u ≥ 1. A6-n still uses the unadopted test target Δ_N(IR) = 2808.6 and H6's premises; n ≤ 247 at u = 1 and n ≤ 172 at u = 2 are exact on that target only.

## 5. Gap Fix F-4 — A9-T label
A9-T stays **CONDITIONAL**. The label itself must carry: dependence on the **unadopted test targets** Δ_N(IR) = 2808.6, Δ_N(UV) = 19520/3, and Q = 9760 (N₊ = Q − n ≥ 0); and the compactness premise **U, uniformly, including at the IR/UV limits** (Sedlacek/Uhlenbeck, not re-checked). Other premises remain: J1 face data with Δ_N(b) continuous; S3/S4-applied (a); T3; existence of the equivariant round BPS instanton. The IR sign uses only H6, with no float. Optional record: at u = 2 the IR sign already holds from n ≥ 173, so n* = 248 is sufficient for both u but **not sharp at u = 2** (n* = 173 at u = 2). A9-T cannot be PROVED while it depends on the test targets and the CONDITIONAL premises. A9-u stays OPEN. A9-g stays PROVED (pure topology).

## 6. Gap Fix F-5 — A8-R(v) GB3 scope
A8-R stays **CONDITIONAL**. Cite **1142 GB3 with its ruled scope**: PROVED for the stated **source-free** equation on a **constant unbackreacted face**, with **fibre-only legs and fibre-only dependence**. Do not cite it as unaudited. Twisted (Σ-legged, sourced) blocks remain under **Y14 S2-2, CONDITIONAL** (PP 077e417d). Premises U (Sedlacek/Uhlenbeck, not re-checked), T3, and the face's G-invariance (J1) stand. The "warp forbids static non-BPS" no-go is correctly not graded REFUTED. No round-fibre no-go is transported to the MN2 squashed fibre.

## 7. Junction Fix F-1 (priority) — S4-2 restated CONDITIONAL
S4-2 is restated as **CONDITIONAL**, with premises **P-b, GA2, D-C, a fixed unbackreacted face, and a stated wall δ(0)/curvature prescription**. The δ-stress is given only as "∝ T_M2·[G_tan]·(∂X₈/∂R · R³)": no derivation of the boundary term, no coefficient, no test. A future upgrade needs the boundary-term derivation: which G₄ components enter (odd tangential only, or also the even G with a leg along x¹¹), and the coefficient. Not refuted. S4-3 stays CONDITIONAL. S4-4 stays OPEN. Vj stays CONDITIONAL, now with S4-2 CONDITIONAL.

## 8. Junction Fix F-2 (priority) — A15-2 restated CONDITIONAL
A15-2 is restated as **CONDITIONAL on the scoped 1142 A1–A3 implications holding on the backreacted face**, not as "CONDITIONAL on the pending 1142 audit." 1142 A1 is now PROVED as an implication of the named bookkeeping premises (R5, S1, N, x-tension = energy density), the source set, and u ≥ 1; A2 is PROVED as the u < 1 companion; A3 is PROVED (off-shell range on the affine space of connections, on any positive-definite fibre metric, at n = 0). Transfer "verbatim" still requires those premises, in particular x-tension = energy density and the source set, to hold on the backreacted face. 1142 A15 itself remains OPEN: no backreacted metric was constructed or ruled out. If A15-2 is also read as carrying 1142 A5, that item is PROVED only for n = 0; for n > 0 it is CONDITIONAL on A4, and for n < 0 the filed target is false as written (floor 2u|n|). Keep GB2/P1 as a pointwise identity (verified in the gap audit, PG2) and sibling H2 with its own premises (Fix F-1). Keep the **"does not transfer"** remark: the A9-T dichotomy and the κ bound do not transfer, because they use J1 face data.

## 9. Junction Fix F-3 — GA9-1 / GA9-2 labels
GA9-1 and GA9-2 stay **PROVED as implications**. The labels must name the **block-averaged source model**: smeared −T·h objects of every (σ, φ) type with T of either sign, plus magnetic Y₆ YM only, constrained at trace level (ρ, tr_Σ, tr_fib); plus the J1 w-values (CONDITIONAL inputs) and the IR-kept or UV-kept pairing. The exact LP optima stand (1/5 and 1/3 IR-kept; 6/5 and 4/3 UV-kept). The **"O(N)"** reading and the M5-unit figures (≈ 3253, ≈ 4190) are **CONDITIONAL**, because they rest on the unadopted test targets 16266.7 / 12568.6 and J1/J5 scaling. GA9-3 stays PROVED within that model. GA9-4 and GA9-5 stay CONDITIONAL. GA9 stays OPEN (narrowed only at these grades). The demanded O(N) object is still not identified.

## 10. Junction Fix F-4 — disambiguate premise J1 from test ID J1
In the 1205 junction filing, "J1" is both the premise (1120's J1 end-face/flow data, CLP/BBBW, CONDITIONAL; also the label for the NL 1711 T0 w-values) and the **test ID** J1 (the IR-kept LP certificate) in the script and test map. J0–J9 sit beside the "given J1" premise. In the sibling gap filing, "J1" is used only as the premise, with the same meaning. No grade changes because of this. For reading only, map the frozen test IDs as follows; **the frozen script is not edited**:

| frozen test ID | reading name |
|---|---|
| J0 | JX0 |
| J1 | JX1 |
| J2 | JX2 |
| J3 | JX3 |
| J4 | JX4 |
| J5 | JX5 |
| J6 | JX6 |
| J7 | JX7 |
| J8 | JX8 |
| J9 | JX9 |

The premise remains "J1". In this erratum, "given J1" always means the premise, never JX1.

## 11. Junction Fix F-5 — A15-1 / §1 premises
A15-1 stays **PROVED (Israel algebra)**. State the premises: the **Z₂ Israel convention** S = −(2/κ²)(K − hK), **staticity** (K_tj = 0), and **Poincaré symmetry** on (t, x). The §1 phrase "holds on any face" is to be read under those premises. Optionally recorded, and accepted as a strengthening of the algebra, not a grade change: the identity holds for a general symmetric Y₆ block of K and any unit e ∈ Y₆, so NEC sources need max eig(K|Y₆) ≤ k_t (PP PJ8). The end-face values −(1/5)ρ_req (UV fibre), 0 (UV Σ) and −(1/3)ρ_req (IR) use the J1 w-values, which are CONDITIONAL inputs. A15-1 does not construct or exclude any face. A15-3 stays CONDITIONAL. A15 stays OPEN.

## 12. Junction Fix F-6 — GA9 source-set citation
For the ruled-out item "{E₈ YM, positive-tension branes}", cite **1120 D-D (given J1)** as the carrying item. **1142 A13 is now REFUTED only under its stated hypotheses** (J1, constant unbackreacted end faces, IR-kept pairing, the source set, tr R² at leading 1/N, and C∧X₈ OPEN). It does not close D-B3 or the junction, and it does **not automatically apply to a backreacted face**.

## 13. Junction Fix F-7 — S4-1 wall term
S4-1 stays **PROVED**. Name **P-b, or the double cover**, as the reason the wall term drops in δ∫C∧X₈ = ±∫G₄∧Y₇ (C_tan odd, so it vanishes at the wall, or work on the double cover). The two-line Chern–Weil proof stands. The machine check is degree-2 su(2) only (reproduced independently, PJ11); **degree 4 is checked by hand only**. "Linear in G₄; no E₈ field" refers to the bulk C∧X₈ term only.

## 14. Nits (absorbed; frozen files not edited)
- Both 1205 headers say E26 was "pending PP confirm". That is stale, not misconduct: the confirm f2e64d44 (FAITHFUL) landed at 11:50:00, before the 12:05:46 writes, and the restatements used are the confirmed ones. **Do not edit the frozen headers.**
- Gap: the H1b and A9a machine tests are instance or finite-range checks. The general statements hold by PP PG1 and by convexity (PG20).
- Gap: the freeze/run same-second timing (script 12:02:26.341, log content 12:02:26.685) is disclosed; with a byte-identical re-run it is not a defect.
- Mode 644 on the 1205 filings is NL convention; no chmod is done. This erratum and its sidecar are also 644.

H1, H4, H5 stay at their ruled grades (H5 PROVED as an implication within the stage-2 ansatz). H3, A16-eq, V″ stay CONDITIONAL. A6, A16, A12-b stay OPEN; "codimension 1" and "n ≲ √Δ(χ = 0)" remain heuristic remarks, not graded. Δ(y) is not computed on any face.

## 15. Mandatory tally-line relabels
**Gap (debc7d52), counts unchanged 7/6/4/0 = 17:**
- **H2** "PROVED (implication): P1 as the pointwise identity (verified here), W real-analytic, non-constant, W_min > 0, N-1 units";
- **H6** "PROVED (implication) of the J1 IR data and the H5 stage-2 ansatz premises, SO(3)×U(1) ansatz only; κ_IR = 1/20 exact; not a bound on general static fields";
- **A12-a** "PROVED (kinematics; sufficiency only); necessity Δ ≥ 0 is a citation of scoped 1142 A10, outside A12-a's own PROVED content";
- **A6-n** "CONDITIONAL; N₋ ≤ Δ_N/2 needs e_u ≥ |n| with u ≥ 1 (1142 A1, as that implication)";
- **A9-T** "CONDITIONAL on unadopted test targets 2808.6, 19520/3, Q = 9760, and on U-uniform compactness, including at the IR/UV limits";
- **A8-R(v)** "CONDITIONAL; 1142 GB3 cited with its ruled scope (constant unbackreacted face, fibre-only, source-free equation); twisted blocks under Y14 S2-2 (CONDITIONAL)".

Gap PROVED 7 (H1, H2, H4, H5, H6, A9-g, A12-a) · CONDITIONAL 6 (H3, A8-R, A6-n, A16-eq, A9-T, V″) · OPEN 4 (A6, A16, A9-u, A12-b) · REFUTED 0 = 17.

**Junction (dff93e21), ruled 5/7/3/0 = 15:**
- **S4-2** "CONDITIONAL, with P-b, GA2, D-C, a fixed unbackreacted face, and a stated wall prescription";
- **A15-2** "CONDITIONAL on the scoped 1142 A1–A3 implications holding on the backreacted face; A9-T and κ do not transfer; 1142 A15 remains OPEN";
- **GA9-1 / GA9-2** "PROVED (implication) given J1 and the block-averaged source model; O(N) and the M5-unit figures CONDITIONAL";
- **A15-1** "PROVED (Israel algebra) under the Z₂ Israel convention, staticity, and Poincaré symmetry";
- **S4-1** "PROVED; wall term drops by P-b or the double cover; degree 4 by hand";
- **GA9** "OPEN; {E₈ YM, positive-tension branes} is carried by 1120 D-D (given J1); 1142 A13 does not automatically apply to a backreacted face and does not close the junction".

Junction PROVED 5 (GA9-1, GA9-2, GA9-3, S4-1, A15-1) · CONDITIONAL 7 (GA9-4, GA9-5, S4-2, S4-3, A15-2, A15-3, Vj) · OPEN 3 (GA9, S4-4, A15) · REFUTED 0 = 15.

## 16. Tallies of earlier files
| file | tally |
|---|---|
| NL 1205 gap (debc7d52), as ruled by PP 087acf47 + addendum 3844d94d | 7/6/4/0 = 17, with the §15 relabels |
| NL 1205 junction (dff93e21), as ruled by PP f25a6d55 + addendum d3e7306e | **5/7/3/0 = 15** (two grade moves) |
| NL 1142 (e7312edb), as ruled by PP e073f0ef; Erratum 27 pending confirm | 16/6/6/1 = 29 |
| NL 1120 (79ad0c64), as ruled by PP 5cf92795 and Erratum 26 (FAITHFUL, f2e64d44) | 22/16/5/2 = 45 |
| NL 1209 BPS (617bc443) and NEC (6ccc9ef4) | unaudited; not regraded here; not edited |
| Errata 24–27 | 0/0/0/0 each; E27 pending confirm |

No previously ruled grade changes except the two junction moves recorded above. Refutations: none new.

## 17. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 0 | — |
| CONDITIONAL | 0 | — |
| OPEN | 0 | — |
| REFUTED | 0 | — |

Check: 0 + 0 + 0 + 0 = 0 (bookkeeping, scope relabels, and acceptance of two already-filed grade moves). Header = body.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 before and after the write (re-hashed after; reported back). Never opened for writing.

Nothing adopted. Junction UNSOLVED. No CERT. D-B3 is not closed. No backreacted metric was constructed or ruled out. Resonant algebra.
