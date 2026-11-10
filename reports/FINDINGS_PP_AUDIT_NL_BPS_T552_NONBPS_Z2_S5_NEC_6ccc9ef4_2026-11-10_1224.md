# FINDINGS — PP Soft SF audit of NL t552u non-BPS filing 6ccc9ef4 (NEC necessary condition on (φ, λ, w)-truncation faces: Z2 corner / S2-13, non-BPS Z2, non-BPS S5)
PP, 2026-11-10, written 12:24:48 CST (America/Chicago) (= file mtime). Labels are pure math (PROVED / CONDITIONAL / OPEN / REFUTED / PENDING). Additive only; no existing file edited, moved, renamed, chmod-ed or deleted. Resonant algebra (never RTA). **Nothing adopted. Junction: UNSOLVED. No CERT.** Tip read-only, mode left 644. No messages sent; the parent delivers.

## 0. Authority and scope
- **OW t552u** (eae1b39d635c69966a2b32642d395ae402d3c33fcf64db7f0b77cad2d8c60db2 = sidecar, mtime 11:46:34.255). Verbatim **"Pursue all for resolution."** — **CONFIRMED** by PP against the NL chat transcript (user turn, speaker cu:405590937, exact text). It is pursuit only and adopts nothing; its Interpretation section is not an Owner ruling. **Standing t4436** (32881263…): only PP-audited PROVED/REFUTED results keep or drop branches; COND stays COND.
- Already ruled and not reopened: PP resume b39c7756 (19/3/6/0) and Erratum 25 (01b7141f; PP confirm 5dd9a6cd). There, Z-1 is PROVED, **Z-2 is CONDITIONAL (float)** and Z-3 is OPEN. PP-accepted drops (E5-4, E2-4, E3, BPS S5) are untouched. **Z-2 numerics are not used as grounds here and not regraded.**
- Separation kept: this filing and this audit do not touch the 1205 gap/junction work (D-B3 / A6–A16, GA9, S4; debc7d52 / dff93e21) or its in-flight audit, 1142 (e7312edb), or any MR2 file. The sibling BPS filing 617bc443 is audited in the companion PP file of this time and is not used to prove anything here.
- Premise record: NL lists (h0) = Erratum 24 (h2) and (ii) the D1 HW hypothesis "for the record" and says the NEC items do not use them. **PP verified this:** B1–B3 use only the frozen face formulas, the PP Y15 NEC criterion, the frozen Hamiltonian constraint and the A′ sign branch. No Killing spinor, projection or supercharge enters. S6 appears only as the odd-HW record.

## 1. Integrity (re-hashed by PP; every sidecar MATCH)
| object | sha256 | mode / mtime (CST) |
|---|---|---|
| target `NL_DERIVED_BPS_T552_NONBPS_Z2_S5_NEC_NECESSARY_2026-11-10_1209.md` | 6ccc9ef4fa283436fbc221b422bc65054f2a6cc34e456439172d7b945b5b3539 | 644 / 12:09:21.126 (same mtime as 617bc443; sidecar identical mtime) |
| script `/workspace/nl-bps-t552-1110/z2_nec_necessary_exact_2026-11-10.py` | 5d342df45b11605781d94a19540b8aeb02bb6a938c70b126ef047188359193b2 | 444 / content 12:05:57.912, sidecar 12:06:04.839 |
| log `…/z2_nec_necessary_exact_2026-11-10.log` | 718cc019dfc994e321c1842c7ccbe32c351d64f399cbcbb96a1622e4d26c1efb | 444 / 12:06:06.367, sidecar 12:06:06.415 |
| frozen face defs `/workspace/nl-bps-d6-2057/z2_centre_flow_faces.py` | 21bcbc3f53eadaf74690f052fa37fb541c5b2c8e4f4bd547e841126e1f3ac641 (= sidecar; log 03b2db8b…) | 644 / 2026-11-09 20:57:39 |
| Z2 corner / S5 (2026-11-09) / Erratum 24 / Erratum 25 / PP resume / PP E25 confirm / E1 | 101467fc8993b011… / 3ceb060529a4022b… / 60bbc7183291a92b… / 01b7141f92ac5764… / b39c7756d8cbb9fa… / 5dd9a6cd670115e5… / 2f33b65db0791028… | all = sidecar; full shas in the companion PP file §1 |
| OW t552u / t4436 / 1117 / 1108 / 1130 / t4431 / f825dfff | eae1b39d… / 32881263… / bff79185… / c6375f85… / 945d81bb… / f700141d… / f825dfff… | all = sidecar |
| **tip** | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 at 12:12:14, 12:21:51 and 12:23:48 (before the companion write), and 12:24:48 (same command, immediately before this write): **7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91** | 644 / 2026-11-06 14:38:54, unchanged |
- Freeze/run: sidecar frozen 12:06:04.839; log 12:06:06.367 (≈1.5 s later). The script content (12:05:57.912) predates the freeze and its hash matches. **Clean.**
- **Header nit (no fix to the frozen file):** "1209 CST" vs mtime 12:09:21.126.
- NL's disclosure is accepted as stated: a pre-freeze dry run used simplify(...)==0 in one cross-check, and this was replaced by an expand identity before the freeze. **That dry run supports no claim and PP does not use simplify==0 anywhere.**

## 2. Evidence (shared directory `/workspace/quantum-comp/reports/evidence_pp_audit_nl_t552u_bps_1209_2026-11-10/`, all files mode 444 with .sha256 sidecars)
| file | sha256 | content |
|---|---|---|
| rerun_z2_nec_necessary_exact_COPY.py | 5d342df45b11605781d94a19540b8aeb02bb6a938c70b126ef047188359193b2 | byte copy of the frozen script |
| rerun_z2.log | 718cc019dfc994e321c1842c7ccbe32c351d64f399cbcbb96a1622e4d26c1efb | **byte-identical** to NL's log (cmp; no wall-clock lines); exit 0 |
| pp_indep_exact_t552u_bps_2026-11-10.py / .log | 17750c237928852aa2e226ce7631f0291aeb0addc7b0b79caffed55242c911e8 / 0181fc276fc804a7fcf1f22df5c5f890985c1fd87c17e1091265594c53d150ff | PP's own exact checks; sidecar frozen 12:21:05.145 before the run; **47 [PASS] / 0 [FAIL]**, exit 0; rows D1–D9 (11 rows) bear on this filing |
| integrity_cmp_scan.txt | 3d814e9de39b4c949ccd1262bb0e05b31b39f4aba09b04cd0f70bb432ae019c3 | cmp, PASS counts, namespace scan |
- **PASS-line count (exact `^\[PASS\]`, SUMMARY not counted):** 7 PASS / 0 FAIL, agrees with 7/7.
- **Namespace scan, NL script:** imports only `sys, sympy`. No nsimplify, no simplify, no float, no numpy, no allclose, no lambdify. Tests are `expand(...)==0`, exact `Rational` equality and exact zero checks. Z-N4b applies `powsimp(combine='exp')` before `expand`: a canonicalising rewrite, not simplify, and acceptable. **Z-N5 is arithmetic only** (12 − 30/4 = 9/2). The inequality chain itself is not machine-checked by NL; PP D4 checks it.
- **PP independent rows (own derivation, exact):**
  - D1 (μ = e₁, e₃, e₅): own normal chart μ = e_i√(1−|y|²) + Σy_j e_j, with T_aa = t_a(r) generic functions, K = ½g⁻¹ġ at y = 0, then (ln t_a)′ = τ_a for the frozen T. The shape operator is diagonal and all 12 margins equal (2φ′ − A′) + NL's closed forms (rational normal form, numerator `expand==0`). This route is independent of NL's direct log-derivative formula and of its (χ, θ, ψ) chart.
  - D2: Z-N3 re-derived, m(e₁;e₂) + 2m(e₃;e₄) + 2m(e₅;e₁) = 5(2φ′ − A′), with weights (1, 2, 2) ≥ 0. D3: the Σ margin is 5φ′ − A′.
  - D4: on the frozen constraint, −V − [(9/2)A′² − 30λ′² − (3/2)w′²] = −30(φ′ − A′/2)(φ′ + A′/2) exactly.
  - D5 (premise necessity): A′ ≤ 0 is needed. (A′, φ′) = (1, 0) satisfies 2φ′ ≤ A′, but (φ′ − A′/2)(φ′ + A′/2) = −1/4.
  - D6: the |V| wording is not implied when V > 0. At (A′, φ′, λ′, w′) = (−1, −1, 0, 0) every axis and Σ margin is ≤ 0 (values −1, −4), yet V = 18 > (3/8)·12A′² = 9/2. The −V form holds.
  - D7: Z-N6, comb = −5A′ at zero scalar velocity.
  - D8: frozen V at the MN2 point, exactly −3·2^{2/3} < 0, so A′(MN2) = −2^{−2/3} ≠ 0.
  - D9: NL's re-typed eps, k_x, k_S, K = ½eps·g⁻¹ġ, T, constraint (G = diag(60, 60, 3)) and the A′ = −√(…) branch occur verbatim in frozen 21bcbc3f. The frozen grid excludes the axis points (χ, θ ∈ [0.05, π/2 − 0.05]), so B1–B3 add points the Z-2 numerics never sampled. That is legitimate because the NEC criterion is pointwise everywhere on S⁴.
- PP first-draft disclosure: see the companion PP file §2 (draft-1 format crash before row A1; draft-2 dead-loop removal; both pre-freeze in /tmp; no draft output used).

## 3. Item-by-item (NL claim → PP ruling, premises named)
Named premises: **(Z-u)** the (φ, λ, w) truncation with the CGR-uplift face data exactly as frozen in 21bcbc3f (eps = Δ^{−1/6}e^{2φ} > 0; k_x, k_S; fibre K = ½eps·g⁻¹ġ with g = Δ^{−2/3}T^{−1}dμdμ; T = diag(e^{−6λ}, e^{−6λ}, e^{4λ+w}, e^{4λ+w}, e^{4λ−2w})); **(Y15)** an NEC face for the required wall stress ⟺ k_v − k_x ≤ 0 for every unit internal v at every face point (PP Y15, cited as the program's criterion); **(HC)** the frozen Hamiltonian constraint 12A′² = 30φ′² + 30λ′² + (3/2)w′² − V; **(A−)** the frozen branch A′ = −√(…) ≤ 0 (with the frozen r and normal conventions). These are statements about that one truncation, **not about an arbitrary 3-scalar truncation**.

| id | NL | PP | reason |
|---|---|---|---|
| B1 axis-point margins | PROVED (exact) | **PROVED (impl. of (Z-u); exact)** | NL Z-N1/Z-N2/Z-N4 re-run byte-identically; PP D1/D3 confirm all margins by an independent chart. Pointwise and algebraic in (φ′, λ′, w′, A′), so valid at every face of every flow of this truncation (BPS or not, any IR). Not an instance check. |
| B2 NEC ⇒ 2φ′ ≤ A′ | PROVED (exact) | **PROVED (impl. of B1, (Y15), eps > 0)** | The nonnegative combination (1, 2, 2) gives 5(2φ′ − A′) ≤ 0 (NL Z-N3, PP D2). The conclusion 2φ′ ≤ A′ needs no sign of A′. The attached clauses "(< 0)" and "5φ′ − A′ ≤ (3/2)A′ ≤ 0" need (A−), which is unlisted (Fix F-1). The polygon statement is correct. |
| B3 NEC faces are kinetic-dominated | PROVED (exact) | **PROVED as restated (impl. of B2, (HC), (A−)); as filed not accepted as written** | Restated: **−V ≤ (9/2)A′² − 30λ′² − (3/2)w′²** on every NEC face (PP D4, using (A−): 2φ′ ≤ A′ ≤ 0 ⇒ φ′² ≥ A′²/4). (A−) is necessary (PP D5). The filed form "\|V\| ≤ (3/8)·12A′²" holds only where V ≤ 0, and is not implied where V > 0 (PP D6). **MN2 corollary, implication:** if a flow approaches the MN2 point with scalar velocities → 0, then near it comb → −5A′(MN2) = 5·2^{−2/3} > 0 (PP D7, D8), so no NEC face exists there. This is an implication of (A−), (HC), the exact V(MN2) < 0 and continuity. It is not an adoption of MN2 as the physical wall. "Anywhere the potential dominates" is likewise valid where V ≤ 0 and −V > (9/2)A′². |
| B4 Z2 corner / S2-13, non-BPS Z2 walls | OPEN | **OPEN** | Only three axis points and Σ are used; the full S⁴ NEC and the flow monotonicity are not done. Z-2 is not used. |
| B5 non-BPS S5 outside the truncation | OPEN | **OPEN** | B3 covers only the truncation. |

## 4. Branch effect (t4436; nothing adopted; no drop)
No branch is dropped by this filing; NL proposes none. **Narrowing recorded (PP-audited PROVED implications):** within the (φ, λ, w) truncation under (Z-u), (Y15), (HC) and (A−), any NEC face must satisfy 2φ′ ≤ A′, −V ≤ (9/2)A′² − 30λ′² − (3/2)w′², and the B2 polygon bound on (λ′, w′). In particular there is no NEC face near the MN2 IR on flows approaching it with vanishing velocities. **[w]/Z2 non-BPS (B4) and non-BPS S5 (B5) stay kept and OPEN.** [χS], [χU] stay kept. S6 is a record premise, not a math escape. Z-2 stays CONDITIONAL (float) as ruled at 1048.

## 5. Grade moves vs NL
No label moves (3/0/2/0). B3 is accepted only as restated (the −V form; (A−) listed), in the E4-3 precedent (PP 1048). As filed, the "\|V\|" wording is not accepted for V > 0. No prior PP grade changes.

## 6. Ruled tally
**PROVED 3 · CONDITIONAL 0 · OPEN 2 · REFUTED 0 = 5**, agreeing with NL's 3/0/2/0 **with B3 restated (Fix F-1)**. As filed: 2 PROVED + B3 not accepted as written. Standing tallies are unchanged: D6 resume 19/3/6/0 (Z2 corner 1/1/1/0 inside it); t4436 / 1120 / Bridge C / parent E₈ untouched. 1205 and 1142 grades are not used.

## 7. Leftover required fixes (next additive NL file; do not edit 6ccc9ef4)
- **F-1 (priority)** List (A−) A′ = −√(…) ≤ 0 (frozen branch and orientation) as a premise of B2's "(< 0)" and Σ clause, of B3 and of Z-N6. Restate B3 as −V ≤ (9/2)A′² − 30λ′² − (3/2)w′². "\|V\| ≤ (3/8)·12A′²" holds only where V ≤ 0; note the exact V(MN2) = −3·2^{2/3}.
- **F-2 (priority)** Scope the title and B3: "any 3-scalar truncation flow" → "any flow of the (φ, λ, w) truncation with the frozen CGR-uplift face data of 21bcbc3f", with (Y15) named as the NEC criterion.
- F-3: State the MN2 corollary as an implication: flows approaching MN2 with scalar velocities → 0, plus continuity and (A−).
- F-4 (nits): Z-N5 is arithmetic, so state the inequality chain as an identity (PP D4) in the next file. Header "1209" vs mtime 12:09:21.

## 8. Custody
- PP wrote only: the shared evidence directory (new; every file mode 444 with sidecar), the companion findings file `FINDINGS_PP_AUDIT_NL_BPS_T552_FX_FIXED_SET_EULER_617bc443_2026-11-10_1223.md` (sha256 9bfa9657beee4ed9e8df9e87b6747b6182aa80e9920bdbcbceb729c3a1029e60, written 12:23:48 = mtime, mode 444, sidecar MATCH), and this file plus its sidecar. No existing file was edited, moved, renamed or deleted. Frozen parents, the 2057/1110 scripts and logs, /workspace/nl-bps-t552-1110/, the 1205 filings, 1142, MR2 files and other agents' directories were read only or not opened. No Local job was touched: no process named s1e / chain_v2 / s2e / wait_then_ob_v5 / ob_v4 was visible to `ps` at 12:13, and PP signalled nothing.
- **Tip after all PP writes up to this file (including the companion findings):** /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = **7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91** (re-hashed at 12:24:48 CST, immediately before writing this file), mode 644, mtime 2026-11-06 14:38:54. Unchanged. No CERT. Nothing adopted. Junction UNSOLVED.
