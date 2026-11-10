# FINDINGS — PP audit of MR2 HW fixed-plane boundary Ricci²/Weyl² filing f4ee61f2 (+ QC note 66f04088)
2026-11-10, written 11:40:51 CST (America/Chicago). Author: **Professor Proof (PP), Soft SF audit.** Audit only. Additive new file; no existing file edited. **Nothing adopted.** No CERT. Nothing sent. Junction **UNSOLVED**. Wording: resonant algebra. Labels: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING; refutation only by proof or counterexample. NL's 79ad0c64 filing is audited separately; no NL grade is used here.

## 0. Authority (re-hashed this run; sha = sidecar)
| record | sha256 | use |
|---|---|---|
| OW 1108 `OWNER_WRITE_CALL_83d7a0fa_PURSUE_HW_ODD_G4_BRIDGE_C_CLOSING_IMPLICATIONS_2026-11-10_1108.md` | c6375f853020e8e994125e1b42acffe830350db0b116b60f0f5f75abbb5f84ca | MR2 item (verbatim): "ensure the 11D curvature check's boundary terms matching onto the HW fixed plane do not trigger an irreversible divergence in Ricci² or Weyl²". Nothing adopted from pasted text; E₈ wall sector CONDITIONAL (backreaction-gated). |
| OW 1117 `…REVERSE_ENGINEER_FROM_GEOMETRY_2026-11-10_1117.md` | bff79185f361bf461194c8d8c9590a4dc7ad0e520ce2f985f41048453545a2f4 | geometry-first method; PP audits as filed, no regrade by fiat. |
| t4436 `OWNER_WRITE_MAINCHAT_t4436_LET_MATH_LEAD_ALL_OPEN_PATHS_2026-11-09_2127.md` | 328812635d807f5cb7d1e5e6b5df7f89512060c36c090a2a191526ab7e90fd46 | math leads; COND stays COND; nothing by fiat. t433u does not cover this filing (MR2 correct). |
| OW 1130 `…PURSUE_OPEN_ITEMS_UNAUDITED_FILINGS_2026-11-10_1130.md` (appeared 11:31, after the filing) | 945d81bb447a923fc68c79ea3ce4df1405aa6f5787e27a301898e98042a47b3c (sidecar records absolute path; hash matches) | context only: PP to prioritise this filing; 9760 unadopted; "construct or rule out" a backreacted metric is a pursuit. Changes no grade here. |

Not adopted, and not used as physical inputs in this audit: N = 4880, charge 9760, tension-to-charge figures, 1a, B1-c2′, E₈ wall sector, MN2 branch U. Wall Bianchi / J_M5 files (79795981 / e2750e28 / 1eb4cec4 / 395bff64) are context only.

## 1. Integrity (re-hashed by PP this run; all sha = sidecar)
| file | sha256 | notes |
|---|---|---|
| tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | mtime 2026-11-06 14:38:54 CST; before and after this write (custody line) |
| parent `MR2_BRANCH_ATTEMPT_HW_FIXED_PLANE_BOUNDARY_RICCI2_WEYL2_2026-11-10.md` | f4ee61f26ad536800792b510f29f714c9c622fd11a8c378e545a8a38976c330d | header 11:24:09 = mtime 11:24:09; mode 644 (nit) |
| QC note `MR2_NOTE_QC_HW_FIXED_PLANE_BOUNDARY_RICCI2_WEYL2_f4ee61f2_2026-11-10.md` | 66f040887ebe660a6d540963b76f005ccd504e9d3e0f1a96b9b842b50f16e2bc | header 11:25:54 = mtime 11:25:54; mode 644. Observation: file mtime 11:25:54.5495 is 2.7 ms after its sidecar mtime 11:25:54.5468; content matches the sidecar hash, so no content change. Nit: say how the mtime was set. |
| script (reports/ and mr2-hw-curv-1110/) | cd289c73043595e303fc5f2d5a0c2e7ba0b2fa5b5cdef33489dcf0231a9c695d | both copies; `cmp` equal; mode 444; frozen 11:21:00 |
| log (reports/ and mr2-hw-curv-1110/) | d5396417b7d3c3ad1212bb8748abe90b26910c89a448081334801038e10b6f23 | both copies; `cmp` equal; mode 444; RUN_START 11:21:05 ≥ freeze 11:21:00; SCRIPT_SHA256 line = cd289c73…; ALL_CHECKS PASS (33 PASS lines counted) |
| MR2 verbatim check 79710111 | 797101112d65910586ad09a7664045b1d748d94dc9e4e976941fddbe3475338d | |
| MR2 MN2 wall bd47ff5e | bd47ff5e8f62a6226680a93107cacae8c8be573399e1f101a2dc57635f03fbfb | |
| PP aeb9ab13 (`FINDINGS_PP_AUDIT_MR2_MN2_Z2_WALL_CURVATURE_E8_2026-11-09_1840.md`) | aeb9ab130c11ceeebe475b1b1da12e61c6dc294aaf23c4b4fb2166dda5cae128 | read: §4 and §6, see row 10 and N2 |
| MR2 erratum (systole label) 2368ffbd | 2368ffbdc6cd6bbe9482e476a085f5d3193da21ef1ea5e2324d3a4a44bf6f295 | |
| MR2 erratum2 per aeb9ab13 5511845e | 5511845e7c4b6e212bf3aa0b11a8e3b531925dd277a7029c8624c74c78bb15b9 | |
| PP 384096a8 (`FINDINGS_PP_AUDIT_MR2_FULL11D_EOM_RIEMANN_SYSTOLE_GATE_2026-11-09_1805.md`) | 384096a8581c1b29bb59768877f36f7fd6caa10f72a23528ea8d058e1253cc19 | line 96: "MN2: Riem² → 3408.000" (numerical limit) |
| MR2 twisted vacua 78cac4c4 | 78cac4c455785f84e3c643bfaeb70fdfecc2a31fcd5351deec8c607388ffebca | |
| PP gate audit 205dbc3f | 205dbc3f067a31413e803d984010815dcf14c3a4d95835a5300b4dfe07f93eee | |
| MR2 erratum2 full11D 7b9ebdaf | 7b9ebdaf9d7656931e65c361cd1cce740479db91352969da4b54ff72ac84b720 | |
| MR2 crosscheck breathing b44cd004 | b44cd00425b792f12c3772898949fc2ed735a1bab0992f4c276bb253e4c333e3 | |
| NL Y16 7270a6b3 | 7270a6b35c97822a4efe37b7f6e78d94efafd0ae44d298ba70554e926c9d5237 | |
| PP Y16 audit (`FINDINGS_PP_AUDIT_NL_Y16_TRR2_WALL_STRESS_AND_ERRATUM12_2026-11-09_1826.md`) | 149be02a794917d92f36c7a2383bbb4eb74623bb4f7b57dd111ad09f73ba7293 | cited by MR2 as "(+ PP Y16 audit)" with no sha (nit N3b) |
| PP 1953 (`FINDINGS_PP_AUDIT_NL_Y14_STAGE2_Y15_FIBRE_ISRAEL_2026-11-09_1953.md`) | 077e417db7f24ece269d7dcde21bc89e260bbe1102d985c63ab60aa94813c23b | = QC N3 value |
| OW t4369 f825dfff | f825dfffb8cd17a7f3f57a2b0a70bd0d9c9d73f215febffdbd2ca95b494d7cd1 | |
| NL 1750 4d9c9951 | 4d9c9951eedc43b359d63842ad1535084b43bf893eca3125a4c7b06c0014468a | |
| 79795981 / e2750e28 / 1eb4cec4 / 395bff64 | 797959812aea… / e2750e284572… / 1eb4cec4ddf8… / 395bff6489ed… (full = sidecar) | context only |
| `/tmp/scratch_pretest.py` | 8fccc9919e36fb11aac9d951dcf7494404565b38e8f21965b290a8f1c2ce0ffb | exists as disclosed; not evidence |

Bookkeeping row (integrity): **PROVED.** Not in this audit: new MR2 files `mr2_hw_backreact_jet_charge_2026-11-10.{py,log}` appeared in /workspace/mr2-hw-curv-1110/ at 11:36–11:37. They were not touched or audited.

## 2. Evidence (`reports/evidence_pp_audit_mr2_hw_ricci2_weyl2_f4ee61f2_2026-11-10/`, every file mode 444 with a `.sha256` sidecar)
| file | sha256 | content |
|---|---|---|
| mr2_hw_plane_ricci2_weyl2_2026-11-10.py | cd289c73043595e303fc5f2d5a0c2e7ba0b2fa5b5cdef33489dcf0231a9c695d | byte-identical copy (`cmp` equal) |
| pp_rerun.log | d36f6735702e6f0488549f43204c0bf01ce3b4b605e99c82502e87d6e76a5a4a | re-run 11:32:31–11:33:13 CST |
| pp_rerun.exit / pp_rerun.stderr | d4e49dd8b59469b9ec9b4026c9796f2e272e46b3e0dfe7486db13f05630cfbf9 / e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | `EXIT 0` / empty |
| pp_rerun_vs_mr2_log.diff.txt | e4087c29d4a7ec91914b0c217fa298ff9a8afa15495e0db9e4c6c9b46f70717c | only lines 1 and 69 differ (RUN_START / RUN_END wall clock). Lines 2–68 are byte-identical, including SCRIPT_SHA256, the long one-sided Riem² rational and the expanded coefficient polynomials. |
| pp_independent_checks.py / .log | 412f3527495e125fd6383e47e5cc8af104e75a754396793b689a37240366f345 / 1cf6297f5aa6f8efe4d827cab0969f497976d1a1d2ae402d4ac8aebff36770a5 | PP's own code, with no MR2 routine imported. Exit 0, 41 PASS, ALL_CHECKS PASS. A first draft had one FAIL (P9.3), caused by a PP index bug that wrongly contracted with η; it was corrected before the logged run and is disclosed here. |
| pp_mr2_namespace_float_check.py / .log | 4d996ee938b64ddd830644e502aae222ee7f00e07bbc816e3190aaa49f54efd0 / a2273ff75985c373997cb5a43232d4b4ba3663b5a147f83478b844b33f7325c2 | source scan plus an in-process run of the evidence copy. Exit 0, ALL_CHECKS PASS. |

How the PP checks were run:
- Exact SymPy throughout. Zero tests use `Poly(...).is_zero`, Integer/Rational equality, or exact determinants. No `simplify`, no floats.
- P2 builds 11D curvature from the full functions A_a(y), using PP's own Christoffel and Riemann code and an explicitly constructed Weyl tensor.
- P2L parses the coefficient polynomials straight from MR2's log text.

**Script claims confirmed (namespace check):**
- No bare `simplify(` call, no numpy, no `allclose`/`evalf`/`N(`/`float(`, and no decimal literals in code.
- `nsimplify` occurs exactly once (E1).
- MR2's `coef`, `eR2` and `cA` objects contain no Float.
- The E1 inputs to `nsimplify` contain no Float, and `nsimplify(x) == x` for each, so it is a no-op and not a hidden float path.
- `sp.factor` is used for printing only, and `sp.solve` (F1) is an exact linear solve.

## 3. Row-by-row verdicts
Abbreviation used below: **L-GN** is the Gaussian-normal structure lemma. In coordinates g = dy² + h(y,x), ∂_y²h enters the Riemann tensor only through R_yayb = −∂_yK_ab + K_acK^c_b. Gauss R_abcd and Codazzi R_yabc carry at most first y-derivatives. The filing checks L-GN only in the 11D diagonal x-independent model (A) and the single 4D instance (B7). It does not state or prove L-GN in general D.

| row | MR2 | PP | basis |
|---|---|---|---|
| 1 V | PROVED | **PROVED** | S², H², S³ normal-coordinate jets; re-run identical |
| 2 δ² structure, 11D diagonal GN | PROVED | **PROVED** | PP P2.2–P2.9 with independent code: Riem² 4 tr k², Ric² tr k²+(tr k)², R² 4(tr k)², Weyl² (32/9)(tr k² − (tr k)²/10), GB 0, degree ≤ 2. P2L.2: the logged 16(9Σk² − 2Σ_{i<j}k_ik_j)/45 ≡ (32/9) tr k̃², exact. P2L.3: it equals PP's explicit-Weyl coefficient. |
| 3 generic [K] | PROVED (D=4 exact); general D as implication | **PROVED, scoped to the D = 4 instance.** **General-D / general-[K] rider (3G): CONDITIONAL on L-GN. Grade move.** | B1–B5 are exact for symbolic κ, but on one background jet (h0, h1, h2 at u = ½) and a 5-parameter κ with κ_tv = 0. That is an instance, not a general 4D theorem. The invariant-form step is **motivated, not proved**: "the δ² coefficient is a function of [K] only" is exactly L-GN, which is not proved in-file. *Given* L-GN, O(h)-invariance + P-Poinc diagonalisability + the row-2 diagonal values would fix the form; PP accepts that second step. The Weyl coefficient algebra 4(D−3)/(D−2)(t₂ − t₁²/(D−1)) is PROVED (P3D.1) *given* the Riem/Ric/R coefficients. PP has not first-proved L-GN and does not use it to keep any grade. |
| 4 HW boundary terms | PROVED (model + index) | **PROVED, scoped** | Proved parts: B6, B′1–B′3 exact in the 4D instance; the index argument (tr R∧R\|_plane pairs Gauss·Gauss + Codazzi·Codazzi, so it is Z₂-even), which is general and elementary. Not proved in general: "no 1/ε in the pulled-back 2-form" in general D is L-GN (3G); equal one-sided limits are shown only in the instance (in general they would follow from the Z₂ isometry, which is not written). Under P-down neither is load-bearing, since only one side exists. Row 4 supports the OW sentence only together with P-down + P-bulk + bounded F on the plane (row 12). |
| 5 non-integrable δ² | PROVED | **PROVED** | P5.1–P5.4: ∫φ_ε = 1, ∫φ_ε² = 1/(3ε) exactly; the Cauchy–Schwarz equality case gives 1/(2Lε). The normalisation [K] = −2k (script k = centre value) gives ∫ = c([K])/(3ε). Nits: the script hard-codes I2 = 2 and prints the CS bound without checking it. |
| 6 not coordinate-removable | PROVED | **PROVED** | Scalars and [K] are geometric. "A function of [K] only" for non-diagonal walls inherits 3G. |
| 7 Israel map | PROVED | **PROVED (algebra); composite scoped** | P7.1–P7.3 hold for a *generic* non-diagonal 10×10 mixed [K]: [K̃] = −κ²S̃, tr[K] = (κ²/9) tr S, tr[K̃]² = κ⁴ tr S̃². The composite "Weyl² δ² = (32/9)κ⁴ tr S̃²" for general walls inherits 3G. **"Zero iff S ∝ h" (D3) needs real diagonalisability (P-Poinc).** Counterexample P7.5: a null stress M = σk^ak_b ≠ 0 has tr M = tr M² = 0, so every δ² coefficient vanishes. D4 states diagonalisability; D3 omits it. |
| 8 uniqueness | PROVED | **PROVED** | P8.1–P8.2 (t₂ and t₁² independent; unique (1,−4,1)). The statement is within span{Riem², Ric², R²}; general walls via 3G. |
| 9 null-positivity | PROVED as impl. of P-content | **PROVED as implication** | P9.1 exact: Σ_{k=t±e_i}\|F(k,·)\|² = 16Σ_j F_tj² + 4Σ_{i<j}F_ij², diagonal with 9 pivots of 16 and 36 of 4. This matches MR2's {4, 16}. P9.3: F(k,·) annihilates k, so each term is ≥ 0 (PP 1953 I2). P9.4–P9.5: the M5 term gives S(k,k) = τ for k = t + transverse and 0 for k = t + worldvolume, so the transverse choice MR2 states is required. The E₈ Lie-algebra trace is component-wise, so all F^A = 0. Implicit premise to name: each M5 worldvolume contains the time direction. |
| 10 "E₈ cancels δ² under odd G₄" | REFUTED as impl. of P-content+P-Israel+P-G+9760 | **REFUTED as implication, of a corrected premise set (grade stands; premise list must be enlarged)** | See §4. The filed premise list is **insufficient**. It needs: **P-Poinc** (strict positivity; P7.5); **P-τ**, i.e. every charged plane object has τ > 0 (P-content allows τ ≥ 0, a "charge without stress" loophole); **n_R = 0**, i.e. −½ tr R² excluded from the Bianchi charge as well as the stress, otherwise the charge could sit in tr R∧R while its stress is excluded by premise, and that case belongs in 10b; and **L-GN** for non-diagonal walls (or restrict to row-2 walls). **9760 is inessential.** The chain uses only Q_plane ≠ 0, so 9760 is a named in-repo premise, never a load-bearing integer. Cancelling instanton/anti-instanton content adds T(k,k) ≥ 0 and cannot cancel. |
| 10b with −½ tr R² stress | CONDITIONAL | **CONDITIONAL** | per Y16 / PP Q15 / PP-1. It now also absorbs the n_R ≠ 0 charge case. A per-direction check is still owed. |
| 11 instances | PROVED | **PROVED (instances)** | P11.1–P11.3: MN2 (a⁴, 0⁶) gives 16, 20, 128/15, 0, 64 (a²). This matches PP aeb9ab13 §4 (Riem² 16a², Ric² 20a², R → 8a, Weyl² 128/15 a²). Umbilic: Weyl² 0, Riem² 40a². BPS 1:1:0: (128/15)κ⁴τ². Branch U only; an instance supports no general claim. |
| 12 V-down | PROVED as impl. of {P-HW,P-reg,P-Israel,P-2der,P-down,P-bulk,P-G} | **PROVED as implication (scoped)** | See §4. It is almost immediate from P-bulk. It does **not** discharge P-bulk, and it does **not** discharge the OW 1108 MR2 item, which is reduced to blocker B-1. Missing premise: F bounded on the plane, needed for HW tr F². P-reg (bounded K) excludes zero-size instantons and plane-localized M5s, so V-down does not cover them (row 14(b)). |
| 13 P-bulk in branch U | CONDITIONAL | **CONDITIONAL** | 384096a8 gives Riem² → 3408 as a numerical limit; the Ric²/Weyl² maxima come from scans. Numerics cannot prove, and the branch-U premise is superseded. |
| 14 P-bulk, backreacted | OPEN | **OPEN** | PP grep of reports/*.md and *.py found no backreacted wall metric or ansatz. Only MR2 itself and OW 1130 mention its absence, and NL 1750 lists one as needed. The blocker is real. Absence is not a resolution (OW 1130), and PP has invented no metric. |
| 15 V-up | PROVED as impl. of {P-HW,P-reg,P-Poinc,P-Israel,P-content,P-G,9760} | **PROVED as implication (premise list corrected as in row 10: + P-τ, n_R = 0, L-GN; 9760 → Q_plane ≠ 0)** | "Irreversible" means → ∞ as ε → 0 at fixed profile shape. Finite thickness ε_y ≳ ℓ_p is row 16. It is a conditional reading: *if* squares are evaluated on the covering space. |
| 16 R⁴ / thickness | OPEN | **OPEN** | Lovelock quasi-linearity is cited, not computed. |
| bookkeeping | PROVED | **PROVED** | §1 |

## 4. Priority audits in detail
**P1 — Row 12 / V-down vs the P-bulk gate.**
- Under P-down the quotient is a manifold with boundary. "At the plane" means the one-sided limit, and P-bulk makes every one-sided curvature component bounded. Riem², R_MNR^MN, R² and Weyl² are therefore bounded, and no divergence can arise.
- The boundary terms are finite under the following premises:
  - Israel/GHY: linear in K, bounded by P-reg.
  - HW tr R²: one-sided pulled-back curvature, bounded by P-bulk.
  - HW tr F²: needs F bounded on the plane. This is **not** in the filed premise list; add it explicitly. (PP notes only that it may follow from P-content + bounded S via the P9.1 form. That is not used for any grade.)
- So row 12 is a correct implication. **Almost all of its content is P-bulk.** Row 4's Z₂ parity results are not load-bearing for it.
- The headline is correctly gated in the relayed summary and in §5 bullet 3. But §5 bullet 1 opens with an unconditional "triggers **no irreversible divergence**", and the "as implication … P-bulk (OPEN)" qualifier comes only two sub-bullets later. **Priority fix:** the lead sentence must carry "as implication, gated by P-bulk, which is OPEN under the working assumption".
- **The OW 1108 MR2 item is not discharged.** It is reduced to B-1 (row 14). P-bulk is not upgraded.

**P2 — Row 10 and row 15's use of it.**
- Chain check:
  - Odd, bounded G₄ ⇒ G² is Z₂-even and bounded, so there is no δ in Einstein (P-G, P-2der). Accepted.
  - The δ-part of Ricci is the Israel stress (P-Israel). Accepted.
  - Q_plane ≠ 0 ⇒ (n_inst ≠ 0 ⇒ F ≠ 0 ⇒ T_YM ≠ 0 by P9.1) or (N_M5 ≠ 0 ⇒ τ > 0). The second branch **needs P-τ**.
  - S ≠ 0 ⇒ S̃ ≠ 0 (row 9). Accepted.
  - S̃ ≠ 0 ⇒ strictly positive Weyl² coefficient. This **needs P-Poinc** (P7.5).
- Loopholes checked:
  - (i) Cancelling instantons: closed, by positivity per null direction.
  - (ii) Charge without stress: open unless P-τ and n_R = 0 are named.
  - (iii) −½ tr R² stress: correctly parked in 10b, which must also take n_R ≠ 0.
- **What aeb9ab13 actually proved.** PP aeb9ab13 §6 graded "N = 4880 exactly, charge 9760" PROVED as an **in-vacuum normalisation result**. It was computed inside the then-adopted MN2 working vacuum: a CLP-Ω flux integral by 40×40 Gauss–Legendre quadrature, π² to 2.4e-15, plus the cohomology/AdS₇×S⁴ normalisation, plus matching to the f825dfff / NL E1 relation N_M5 + n_inst = 2N. Its "E₈ identification" was CONDITIONAL there. It is not a physical theorem about the backreacted face, and it is not an adoption. Under OW 1108 and OW 1130, 9760 is a premise / labelled test target.
- Since row 10 needs only Q_plane ≠ 0, the erratum should state that. This is relevant to OW 1130's question, but it is not a resolution of it.

**P3 — Row 9.** Independently re-derived (P9.1–P9.5): the form is exactly diagonal, with pivots 16 (×9 electric) and 4 (×36 magnetic). The M5 argument is correct with k = t + a transverse direction. PROVED as implication of P-content; −½ tr R² stays excluded.

**P4 — Row 3 general D.** See the table. The 4D model does not carry a general-D PROVED. Split out 3G as CONDITIONAL on L-GN until the erratum proves L-GN, which is a short Gauss–Codazzi–Ricci derivation for MR2 to supply, not PP. The rows that inherit 3G for non-diagonal walls (4-general, 6, 7-composite, 8-general, 10, 15, §6.1) keep their grades **as implications with L-GN named** (or restricted to row-2 walls).

**P5 — Exact identities (rows 2, 5, 7, 8, 11).** All re-checked independently and exactly (§2). No identity failed. The only finding is the D3 diagonalisability omission (P7.5).

**P6 — §6.**
- Item 1 needs L-GN in general D.
- Item 5, "the geometry forces a non-umbilic, anisotropic plane", is an implication of {P-content, P-Israel, P-Poinc, P-τ, Q_plane ≠ 0}. Row 9 alone gives only S̃ = 0 ⇒ S = 0. **Rewrite it as an implication.**
- Item 6: QC N2 is fair. Also replace "(filed, exact)" by "in-repo stated premise (PP aeb9ab13, MN2 branch-U normalisation), not adopted". Odd G₄ forces only the form [G] = 2G and the form of the balance.
- Item 7: the junction is carried, UNSOLVED. Correct.
- Item 4 is P-Poinc restated. Correct.

**P7 — Rows 13, 14, 10b, 16.** Scopes are kept as filed (see table).

## 5. QC note N1–N3
- **N1: fair, cosmetic.** The author is Math Research 2.
- **N2: fair and load-bearing for wording.** PP adds that 9760 is not load-bearing anywhere; Q_plane ≠ 0 suffices.
- **N3: fair.** 077e417d… = sidecar, verified by PP. The same applies to the PP Y16 audit cited without a sha (149be02a…).
- Require N1–N3 in an additive MR2 erratum. Do not edit f4ee61f2.

## 6. Tally
- MR2 filed: 12 / 2 / 2 / 1 = 17 + 1 bookkeeping.
- **PP ruled: PROVED 12** (rows 1, 2, 3 [D=4 instance], 4 [scoped], 5, 6, 7, 8, 9 [impl.], 11, 12 [impl.], 15 [impl., corrected premises]) · **CONDITIONAL 3** (10b, 13, **3G**) · **OPEN 2** (14, 16) · **REFUTED 1** (10, impl., corrected premises) **= 18 + 1 bookkeeping.**
- Grade move: the general-D rider of row 3, PROVED-as-implication → CONDITIONAL (L-GN). No other grade moves; there are premise-list scope fixes on rows 7, 9, 10, 12, 15 and §6.
- Junction UNSOLVED, carried and not counted.
- **No effect on other standing tallies.** t4436, Bridge C, parent E₈, aeb9ab13 and NL 79ad0c64 are not rewritten. The E₈ wall sector stays CONDITIONAL.

## 7. Fixes for an additive MR2 erratum (do not edit f4ee61f2, the QC note, or the frozen script/log)
**Priority:**
- F-1: state and prove L-GN (or carry it as a named premise). Until then, row 3's general-D statement is CONDITIONAL (3G).
- F-2: rows 10/15 premise sets. Add P-Poinc (row 10), P-τ, n_R = 0 (−½ tr R² excluded from the charge too, with the n_R ≠ 0 case moved to 10b), and L-GN. Replace "charge 9760" by "Q_plane ≠ 0 (9760 an in-repo stated premise, PP aeb9ab13; not adopted)".
- F-3: row 7 D3. "Zero iff S ∝ h" requires real-diagonalisable [K] (P-Poinc); null counterexample P7.5.
- F-4: row 12 / §5 bullet 1. Put "as implication, gated by P-bulk (OPEN under the working assumption)" in the lead sentence. Add "F bounded on the plane" to the premises. State that P-reg excludes zero-size instantons and plane-localized M5s. State that the OW 1108 item is reduced to B-1, not discharged.
- F-5: §6 items 5 and 6 as implications with premises named (N2).

**Non-priority:**
- N1 (author line).
- N3 (077e417d…; also 149be02a… for the PP Y16 audit).
- Row 3: disclose the single background jet and κ_tv = 0.
- Row 9: name "M5 worldvolume ∋ t".
- C2: I2 hard-coded; the CS bound is printed, not checked.
- Parent and QC mode 644 (convention).
- QC note mtime 2.7 ms after its sidecar: say how it was set.

## 8. Custody
- Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, mtime 2026-11-06 14:38:54 CST, hashed before and after this write; **untouched**.
- MR2's parent, QC note, script, log, sidecars and the frozen originals in /workspace/mr2-hw-curv-1110/ were read and hashed only. No Local job, NL evidence, or other agent directory was touched.
- No message was sent. Nothing adopted. No backreacted metric invented. Junction **UNSOLVED**. No CERT.
