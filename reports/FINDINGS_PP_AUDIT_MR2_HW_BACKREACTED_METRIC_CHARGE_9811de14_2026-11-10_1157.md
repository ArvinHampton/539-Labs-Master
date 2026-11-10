# FINDINGS — PP audit of MR2 backreacted near-plane metric and 9760-free δ² filing 9811de14
2026-11-10, written 11:57:23 CST (America/Chicago). Author: **Professor Proof (PP), Soft SF audit** (after lane self-prove, not first-prove). Audit only. Additive new file; no existing file edited. **Nothing adopted.** No CERT. Nothing sent. Junction **UNSOLVED**. Wording: resonant algebra. Labels: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING; refutation only by proof or counterexample.

Audited: `MR2_BRANCH_ATTEMPT_HW_BACKREACTED_METRIC_AND_CHARGE_PREMISE_2026-11-10.md` (sha 9811de1490a88569860a3a2e3b04a5fe75387fc83eb1ba020221f72395150770), script 2d8092a7…, log 7634069f….

## 0. Authority and scope (re-hashed this run; sha = sidecar)
| record | sha256 | use |
|---|---|---|
| OW 1130 `OWNER_WRITE_CALL_83d7a0fa_PURSUE_OPEN_ITEMS_UNAUDITED_FILINGS_2026-11-10_1130.md` | 945d81bb447a923fc68c79ea3ce4df1405aa6f5787e27a301898e98042a47b3c | Owner DIRECT (verbatim previously verified by PP against call / cu:405590937 pos 18530). "Construct or rule out" is a pursuit; no metric by fiat; absence is not a resolution; 9760 unadopted. |
| OW 1108 `…PURSUE_HW_ODD_G4_BRIDGE_C_CLOSING_IMPLICATIONS_2026-11-10_1108.md` | c6375f853020e8e994125e1b42acffe830350db0b116b60f0f5f75abbb5f84ca | continues; E₈ wall sector CONDITIONAL; nothing adopted from pasted text |
| OW 1117 `…REVERSE_ENGINEER_FROM_GEOMETRY_2026-11-10_1117.md` | bff79185f361bf461194c8d8c9590a4dc7ad0e520ce2f985f41048453545a2f4 | geometry-first method (§5) |
| t4436 `OWNER_WRITE_MAINCHAT_t4436_LET_MATH_LEAD_ALL_OPEN_PATHS_2026-11-09_2127.md` | 328812635d807f5cb7d1e5e6b5df7f89512060c36c090a2a191526ab7e90fd46 | math leads; nothing by fiat. t433u does not cover this filing. |
| PP citation rule 2030 `FINDINGS_PP_CORRECTION_1949_CITATION_GRADES_edcd9551_2026-11-09_2030.md` | 69d334568f933cbe82969a4eada5de45a1cca74783620d31c5a43061d4f8e844 | a citation never makes a row PROVED by itself |
| PP 976e5621 `FINDINGS_PP_AUDIT_MR2_HW_PLANE_RICCI2_WEYL2_f4ee61f2_2026-11-10_1140.md` | 976e56211308cf68e8ad80df063f99e08826d441e0f4d8a45242ad6fad01031c | already-ruled scopes (L-GN / 3G; row 10/15 corrected premises; 9760 inessential). Applied here for consistency. The filing (11:39:48) predates it (11:40:51); MR2 had not seen it. |

Not adopted and not used as physical inputs: N = 4880, charge 9760 (as a wall charge), 1a as the physical wall, B1-c2′, the tension-to-charge figures, MR2 f4ee61f2 grades, NL 79ad0c64 grades (NL filing PP-audited separately as 5cf92795…; cited here only as literature where MR2 cites GA7a). The parallel PP audit of Local dff4b879 is not used.

## 1. Integrity (all re-hashed by PP this run; sha = sidecar unless stated)
| file | sha256 | notes |
|---|---|---|
| filing `MR2_BRANCH_ATTEMPT_HW_BACKREACTED_METRIC_AND_CHARGE_PREMISE_2026-11-10.md` | 9811de1490a88569860a3a2e3b04a5fe75387fc83eb1ba020221f72395150770 | header "written 11:39:48 CST" = mtime 11:39:48.332 CST; sidecar 11:39:48.340; mode 644 (MR2 convention; nit) |
| script `mr2_hw_backreact_jet_charge_2026-11-10.py` (reports/ and /workspace/mr2-hw-curv-1110/) | 2d8092a779b8ed5cf4118d05f054ff9ccf227dbe10fc754a93d645ba10c75d5c | both copies `cmp` identical; mode 444; content mtime 11:36:54.25; sidecar 11:37:27.74 |
| log `mr2_hw_backreact_jet_charge_2026-11-10.log` (both copies) | 7634069fcc9700debd53ab57b7e10aca703cec460c630ca61034196933524dbb | both copies `cmp` identical; mode 444; mtime 11:37:53.28; RUN_START 11:37:27, SCRIPT_SHA256 = 2d8092a7… (= sidecar), 20 PASS lines, ALL_CHECKS PASS, RUN_END 11:37:53 |
| tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | mtime 2026-11-06 14:38:54 CST, mode 644; before and after this write (§11) |
| MR2 f4ee61f2 `MR2_BRANCH_ATTEMPT_HW_FIXED_PLANE_BOUNDARY_RICCI2_WEYL2_2026-11-10.md` | f4ee61f26ad536800792b510f29f714c9c622fd11a8c378e545a8a38976c330d | unedited; mtime 11:24:09 CST |
| PP 976e5621 | 976e56211308cf68e8ad80df063f99e08826d441e0f4d8a45242ad6fad01031c | mode 444 |
| OW t433u (MR2) `OWNER_WRITE_MR2CHAT_t433u_SEND_REPORT_THEN_ADOPT_ALL_PROVED_FROM_PP_2026-11-10.md` | 3df3878860906386276ce33cecac17019124ae1671b5d2d330709cc0058dcf47 | |
| OW t433u coordinator `OWNER_WRITE_COORD_MR2CHAT_t433u_ADOPT_PP_PROVED_VERIFIED_2026-11-10_1035.md` | dd7b747aeda21415cd945a9b0bcfea0800639209353762a0f4e92f5ef04d1c55 | |
| MR2 adoption `MR2_ADOPTION_PP_PROVED_PER_OW_t433u_2026-11-10.md` | f3f6d65c845c3dd076e9287495d4d1891f6ffdc144d46b0449e8dc9f660d4fae | = MR2's citation |
| MR2 supplement `MR2_SUPPLEMENT_ADOPTION_t433u_PER_PP_eebd7dd7_2026-11-10.md` | 85b4287624393815e11d875b162a53eec5caf6d9c49066307b66ec74d3336d8c | = MR2's citation |
| PP confirm `FINDINGS_PP_CONFIRM_MR2_ADOPTION_t433u_2026-11-10_1037.md` | eebd7dd70fd8222260c8a5f6d8bbc8238244993cf45a90c1d129942932558ea8 | |
| MR2 E₈ parent cc21b272 `MR2_BRANCH_ATTEMPT_BATCH1_C2PRIME_E8_BUNDLE_UNDER_1A_R_TILDE_INVARIANCE_2026-11-10.md` | cc21b2728dd74fe6aae8d7da186a5bb40f9b5b4e8d8390226f2fa0e904f08f11 | source of D2, D3 |
| MR2 erratum 55941d82 / PP confirm f2e2e0a6 | 55941d820946de7fd5aec8603cfb711c569a71a42b27fe32b77bd575a192f4fa / f2e2e0a68230f578f9eabd04a1e240eced7e6ae7cb761c99125152c9eaf91f95 | D2/D3 unchanged there |
| PP 1948 dee9410e `FINDINGS_PP_AUDIT_MR2_CANDIDATES_BATCH1_PHI2_HW_WALL_THICKNESS_2026-11-09_1948.md` | dee9410e90bcd6eb3e5df436314a0ba98d791bea938bc53968d5baf388ca059c | |
| PP aeb9ab13 `FINDINGS_PP_AUDIT_MR2_MN2_Z2_WALL_CURVATURE_E8_2026-11-09_1840.md` | aeb9ab130c11ceeebe475b1b1da12e61c6dc294aaf23c4b4fb2166dda5cae128 | |
| OW t4369 (P-HW) `OWNER_WRITE_MAINCHAT_t4369_FACE_Z2_FIXED_PLANE_HW_WALL_G4_ODD_O1_RESOLVED_2026-11-09_1745.md` | f825dfffb8cd17a7f3f57a2b0a70bd0d9c9d73f215febffdbd2ca95b494d7cd1 | = sidecar |
| NL 79ad0c64 `NL_DERIVED_E8_INSTANTON_GEOMETRIC_DELTA_ODD_G4_2026-11-10_1120.md` | 79ad0c6417e825d4fee8d412af62a767688b883a88c39c6a6affd716ce4ffa29 | cited only |

Bookkeeping row (integrity): **PROVED.** Every sha MR2 cites that PP re-hashed matches.

**f4ee61f2 non-use claim: verified.** The frozen script reads no file other than itself (line 6, self-hash). K1–K6 are recomputed in-script from first principles. f4ee61f2 is cited only for the elementary identity ∫φ_ε² = 1/(3ε), which is not machine-checked in this script (nit N4); PP checked it exactly (P9). No f4ee61f2 grade is used as a premise here, and none is used by PP.

## 2. Evidence: `reports/evidence_pp_audit_mr2_hw_backreact_9811de14_2026-11-10/` (every file mode 444, each with a `.sha256` sidecar)
| file | sha256 | content |
|---|---|---|
| mr2_hw_backreact_jet_charge_2026-11-10.py | 2d8092a779b8ed5cf4118d05f054ff9ccf227dbe10fc754a93d645ba10c75d5c | byte-identical copy (`cmp` equal); not edited |
| pp_rerun.log | d9ba72b63f2311127e0b837af00b8a0fd949592b0cd36a9277461a022efeea54 | re-run 11:50:23–11:50:48 CST |
| pp_rerun.exit / pp_rerun.stderr | d4e49dd8b59469b9ec9b4026c9796f2e272e46b3e0dfe7486db13f05630cfbf9 / e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | `EXIT 0` / empty |
| pp_rerun_vs_mr2_log.diff.txt | 899b0eb976f365d9b323de22606dfb2771e2af58d5c455314cb5e502dce34d4e | only lines 1 and 41 (RUN_START / RUN_END wall clock) differ; lines 2–40 byte-identical, incl. SCRIPT_SHA256, the factored H·H/24 polynomial, examples −3/4 and 1/4, 20 PASS |
| pp_independent_checks.py / .log | dfa5a24e914101a81dd5f2335edc56ca5dad8bda04539a94afdeb3847f938165 / 4d4ede4dee2eee20837ee724485cfa4994136796d21110216472090e4718b7ab | PP's own code (no MR2 routine imported). Sealed run 11:53:36–11:54:13 CST: exit 0, **38 PASS / 0 FAIL**, ALL_CHECKS PASS |
| pp_independent_checks.exit / .stderr | d4e49dd8b59469b9ec9b4026c9796f2e272e46b3e0dfe7486db13f05630cfbf9 / e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | `EXIT 0` / empty |
| pp_mr2_namespace_scan.txt | 63138f707b6448f18d1bc862ebeccce66c23e1714f9a0be4b78c43da45e511af | source scan of MR2 script |

Method: exact SymPy only. Zero tests use `expand(...) == 0`, `Poly(...).is_zero`, Rational equality, and exact LDL pivots. There is no `simplify`, no float and no `allclose`. `sp.solve` (P5.1) is a one-unknown linear solve, and `limit` (P9.2) is an exact limit of tanh. PP's curvature code uses a different route from MR2's: R^a_bcd from Christoffel derivatives, with ∂(g⁻¹) = −g⁻¹∂g g⁻¹. It is validated on stereographic S² (R = 2) and on H² (R = −2), which are coordinates MR2 did not use. Draft disclosure: one scratch run of the same script (sha dfa5a24e…, /workspace/pp_scratch, 11:52:42–11:53:18) also passed 38/38. No buggy draft existed, and the sealed evidence run is the cited one.

**Namespace scan of MR2's script:** no `nsimplify`, no `simplify`, no float/`evalf`/numpy/`allclose`, and no file input. `sp.factor` is used for printing only. K4 `is_positive_definite` runs on an integer matrix, and PP re-checked it by exact LDL (P8.7). J3 accepts either sign by construction (nit N2). The printed sign is +, and PP pins + independently (P1.5).

**Freeze / run disclosure (recorded, not over-weighted).** The sidecar was written at 11:37:27.74 and RUN_START is stamped 11:37:27, so both fall in the same second. MR2 states they ran freeze-first in one `&&` chain, and a one-second stamp cannot prove sub-second order. The log's SCRIPT_SHA256 equals the frozen sha, and PP's post-freeze re-run is byte-identical apart from the wall-clock lines. The cited evidence is therefore clean, and the disclosure has no grade effect. The pre-freeze /tmp scratch runs are disclosed and not cited.

## 3. Task 1 — backreacted metric: item-by-item
**L-GN** is used exactly as defined in 976e5621: in g = dy² + h(y,x), ∂_y²h enters Riemann only through R_yayb, while Gauss and Codazzi carry at most first y-derivatives.

- **Row 1 (V1–V2) — PROVED.** Re-run identical. PP V1–V2 use independent code and coordinates.
- **Row 2 (J1a–c) — PROVED, scoped to the D = 4 instance.** The general-D / "holds in D = 11" rider is split out as **GN-G, CONDITIONAL on L-GN. Grade move.**
  - What the script proves: one background jet, (h0, h1) fixed rationals at (u, v) = (1/3, 1/5), h independent of t, h2 fully symbolic. G_yy and G_ya are h2-free, and R_ab = −½∂_y²h_ab + (h2-free). That is an exact statement about this instance. It is not a general 4D theorem, and not a general-D theorem.
  - "The structure is index-generic (Gauss–Codazzi–Ricci), so it holds in D = 11" is exactly L-GN, which this filing neither states nor proves. This matches 976e5621 3G.
  - PP P1.1–P1.3 corroborate in an independent **D = 5** instance: non-diagonal, t- and x-dependent, 10 symbolic h2 entries, PP code. That is corroboration only. PP does not first-prove L-GN and upgrades nothing; F-1 asks MR2 for the short derivation, as 976e5621 already did.
- **Row 3 (J2–J3) — PROVED, scoped to the D = 4 instance.** The 10D plane use falls under GN-G (L-GN).
  - Gauss: 2G_yy = −r[h] + (tr K)² − tr K², with K = ½∂_yh. Correct convention.
  - Codazzi sign: **+**, i.e. G_ya = D_bK^b_a − D_aK. PP P1.4–P1.5 confirm both, with sign +, in the D = 5 instance with x-dependent K.
- **Row 4 (J4a–c) — PROVED.** MR2 checks it eigenvalue-wise. PP P3.1–P3.3 prove it for a **generic** 10×10 matrix (100 symbols): K⁺ = −(κ²/2)(S − h trS/9), tr K⁺ = κ²trS/18, and (trK⁺)² − tr K⁺² = (κ⁴/4)((trS)²/9 − trS²). The "diagonalisable premise" in the J4a label is not needed for this algebra (nit N3).
- **Row 5 (J5) — PROVED, including D = 11.**
  - MR2 checked D = 6. PP P4.0–P4.2 pin **D = 11** exactly with 330 symbolic components: G² = G_t·G_t + 4H·H, G_yPQR G_y^PQR = H·H, and T_yy = H·H/24 − G_t·G_t/96.
  - The index count is dimension-free, so the D = 11 use is now pinned rather than asserted.
- **Row 6 — PROVED as implication of {rows 3–5, P-HW, P-HWbc, P-G, P-Poinc}, with L-GN named** (the 10D Gauss constraint is general-D, GN-G). Algebra re-derived:
  - PP P5.1: H·H/24 = −r/2 + (κ⁴/8)((trS)²/9 − trS²) + J·J/384.
  - PP P5.2: (κ⁴/4)(…) + J·J/192 − r ≡ H·H/12. So under P-Poinc (H ∈ Λ³Y₆, Riemannian) the inequality holds, with equality iff H = 0.
  - Smeared M5: (trS)²/9 − trS² = −2τ² (P5.3).
  - Nit N1 (κ convention): P-G has unit bulk coupling while Israel carries κ². The formula is correct if κ² = 1 in P-G units. Otherwise the H·H and J·J terms carry κ². No sign or grade effect.
- **Row 6b — CONDITIONAL (stands). B-3's index algebra is now machine-checked by PP.**
  - LHS, PP P6.1 (exact, D = 5 instance): G_ya(0⁺) = −(κ²/2)D_bS^b_a under K⁺ − hK⁺ = −(κ²/2)S.
  - RHS, PP P6.2 (exact, D = 11): T_ya = (1/12)G_yPQR G_a^PQR = (1/12)H_bcd G_t,a^bcd. Every y-leg drops, and with G_t = J/2 this gives (1/24)H·J_a.
  - So −(κ²/2)D_bS^b_a = (1/24)H_PQR J_a^PQR, sign as filed.
  - The row stays CONDITIONAL on general-D Codazzi (GN-G / L-GN) and P-HWbc, plus nit N1. No upgrade by PP; MR2 may cite P6.1/P6.2 in its erratum.
- **Row 7 — PROVED (exact examples), with a required scope fix (F-5).**
  - PP P7.1 reproduces MR2's logged polynomial with independent YM+M5 stress code. P7.2 reproduces A = −3/4 and B = +1/4.
  - **But** under P-HWbc, J ⊃ c·tr F∧F, which is proportional to f₁f₂ on e^6789. Setting j = 0 with f₁ = f₂ = 1 and τ = 0 therefore treats j as independent of F. That holds only if the gravitational density cancels pointwise, a case P-content excludes from the stress.
  - With j = λf₁f₂: **B is robust**, 1/4 + λ²/16 > 0 (P7.3). **A is not robust**, −3/4 + λ²/16, which is positive for λ² > 12 (P7.4).
  - A consistent content example: A′ with f₂ = 0, so tr F∧F = 0 and j = 0 consistently, gives required H·H/24 = −11/16 < 0 (P7.5).
  - J6c's sign test is valid: every monomial has a nonnegative coefficient and even powers of f₁, f₂ (P7.6).
  - Satisfiability (B) is what row 9 uses, and it is robust.
- **Row 8 — CONDITIONAL (stands).**
  - It rests on Cauchy–Kovalevskaya and constraint propagation, which are cited, not re-derived (rule 2030). It also rests on GN-G (the 11D 2-jet algebra), an unspecified gauge for the first-order 4-form system, and real-analytic plane data (B-2).
  - The NL GA7a dependence is a scope, not an adoption.
  - Nit N8: a uniform slab width δ over the plane needs compact Y₆ plus Poincaré homogeneity; say so.
  - No metric is invented: the row states which data would produce one.
- **Row 9 — REFUTED, scoped (F-6).**
  - What it fairly refutes: "the plane's Gauss scalar constraint rules out every backreacted plane pointwise". Counterexample B is exact and robust to the J coupling (P7.3).
  - What it does not establish: that no jet-level obstruction exists at all. Simultaneous pointwise and 1-jet satisfiability of Codazzi (6b), the plane 4-form constraints and the E₈ YM equations is asserted, not exhibited. "The 2-jet is then determined" in 11D inherits GN-G.
  - It has no bearing on a global solution (row 10). It is a fair jet-level REFUTED only in this scalar-constraint scope.
- **Row 10 — OPEN (stands).** The blockers are real:
  1. The Cauchy problem off a timelike plane is ill-posed (Hadamard) outside analytic data.
  2. Ellipticity of the Poincaré-reduced Einstein–4-form system under a nonlinear Robin (Israel) condition coupled to E₈ YM is missing: Lopatinskii–Shapiro in a chosen gauge, plus Fredholm/existence. Under rule 2030 it is OPEN, not cited-PROVED.
  3. The background to perturb from is the junction, which is UNSOLVED and not treated as a constructed background.
  4. Localized M5s make S distributional.
  The filing does not use the absence of a file as a resolution, and PP invents no metric.

## 4. Task 2 — 1/ε without 9760: item-by-item
- **Row 11 — PROVED as implication, under a corrected premise set (premise fix F-2): {P-reg, P-Poinc, P-Israel, P-content incl. P-τ and "M5 worldvolume ∋ t"}, with L-GN named for non-diagonal or x-dependent walls (or restricted to diagonal walls).**
  - K1–K3 are computed on an **11D diagonal, x-independent** thin-wall jet. PP P8.1–P8.6 confirm them with independent code and an explicit Weyl tensor:
    - Riem²: 4 tr k²
    - Ric²: tr k² + (tr k)²
    - R²: 4(tr k)²
    - Weyl²: (32/9)(tr k² − (tr k)²/10)
    - Gauss–Bonnet: 0
    - degree in δ: ≤ 2
  - Further checks: K4 by exact LDL (P8.7); K5 generically (P3.4–P3.5); K6 pivots 16 (×9) and 4 (×36) (P8.8), matching 976e5621 P9.1; M5 S(k,k) = τ for transverse k and 0 for worldvolume k (P8.9); ∫φ_ε = 1 and ∫φ_ε² = 1/(3ε) exactly (P9.1–P9.3).
  - Under P-Poinc a point-wise eigenframe exists. Extending the coefficients to x-dependent or non-diagonal walls is L-GN, consistent with 976e5621 rows 2/3G/15. **No charge value is used (verified).**
- **Row 12 — REFUTED as implication of a corrected premise set (grade stands; the premise list must be enlarged, F-2), matching 976e5621 row 10.**
  - Chain:
    - non-gravitational density ≠ 0 at p ⇒ F(p) ≠ 0, or an M5 density with τ > 0 (P-τ, restated in this filing's P-content);
    - ⇒ S(k,k) > 0 for some null k (K6 / P8.8–P8.9; needs "worldvolume ∋ t");
    - ⇒ S(p) ≠ 0 ⇒ [K](p) ≠ 0 (P-Israel).
  - The strictly positive δ² coefficient then needs **P-Poinc** (the null-stress counterexample in 976e5621 P7.5), plus P-reg and L-GN or a diagonal wall. The filed "{P-content}" alone is insufficient.
  - "Pointwise" means: at points where the non-gravitational density is nonzero. It does not cover points carrying only gravitational density (12b) or distributional, point-like sources (outside P-reg).
  - Instanton / anti-instanton or brane / anti-brane cancellation of **charge** does not cancel **stress**: S(k,k) ≥ 0 term by term.
- **Row 12b — CONDITIONAL (stands)**, per NL Y16 / PP-1, cited only. Not regraded.
- **Row 13 — PROVED as implication of a refined premise set (premise fix F-3). It does replace the specific value 9760 by N ≠ 0 plus adopted D2, but by a weaker unadopted premise, not by an adopted value.**
  - **Stokes:**
    - Under P-HW, the Z₂ fixes the plane, and so each S⁴ fibre of Y₆, pointwise. Odd G₄ then gives ∫_{S⁴(−y)}G = −∫_{S⁴(+y)}G = −N.
    - The slices are homologous through S⁴ × [−y, y].
    - With dG = 0 off the plane (no off-plane sources, part of P-content), the HW Bianchi identity gives ∫_{S⁴}J = 2N.
    - This is the same argument PP ruled PROVED in dee9410e §2 (2c), lines 78–81.
  - **D2 (adopted, scoped):**
    - cc21b272 line 43, "**D2. p₁(TY₆) = 0. PROVED.**", for the specific Y₆ = twisted S⁴ bundle over Σ of the 1a face (line 36). It is adopted under t433u as graded (eebd7dd7 line 38: "D1–D3 and D5 are correctly listed as PROVED").
    - It is topological, so it applies to a backreacted plane **iff that plane's internal manifold is this Y₆**. Name this as premise **P-Y₆**; it is not adopted.
    - The needed class is ⟨p₁(TM₁₁|_plane), [S⁴]⟩ = ⟨p₁(TY₆), [S⁴]⟩. The TR^{1,3} and normal-line summands are trivial, and with D1 (∫ over the fibre, torsion-free) D2 makes it zero. This is not the same statement as p₁(TS⁴) = 0, and PP does not conflate them. Any Chern–Weil representative, including the one-sided 11D Levi-Civita form, then integrates to 0 over the fibre.
    - D2 thereby supplies the *integrated* n_R = 0 that 976e5621 F-2 asked to be named. The pointwise gravitational density is not excluded (cc21b272 line 45, "pointwise nonzero"), and that part stays in 12b.
  - **Conclusion:** n_inst + N_M5 = 2N ≠ 0, with HW integer normalisation (P-HWbc, CONDITIONAL premise). So some fibre carries nonzero non-gravitational density, and S ≢ 0 by row 12's first half (P-content, P-τ; P-Poinc is not needed for S ≢ 0). Row 11 then applies, with row 11's premise set. Sign-blindness is correct.
  - **Not adopted:** N ≠ 0 (P-N), N = 4880, 9760, P-Y₆, P-HWbc.
- **Row 14 / B-4 — see §6.** It is reclassified from a math OPEN row to a **record row, answered (scoped-compatible)**.

## 5. §5 geometry ⇒ algebra (restatements, not extra PROVED items)
| item | PP reading |
|---|---|
| 1 | Rows 2–3: needs L-GN in general D (GN-G) |
| 2 | Row 4: correct (generic, P3) |
| 3 | Rows 5–6: correct; nit N1 (κ convention) |
| 4 | Row 6: correct, under P-Poinc, with L-GN named |
| 5 | Row 6b: CONDITIONAL (index algebra now pinned by P6.1/P6.2) |
| 6 | "⇒ an elliptic-type bulk problem" overstates (F-7). Read it as: a Riemannian-signature bulk problem whose ellipticity (Lopatinskii–Shapiro) is exactly the missing B-1. |
| 7 | Row 13 as an implication with the refined premises (P-Y₆, P-HWbc, P-N) |

Blockers:
- **B-1:** real; OPEN.
- **B-2:** real. GA7a is cited, unadopted (NL 79ad0c64 is PP-audited separately; not used).
- **B-3:** the index algebra is discharged by PP's exact checks P6.1/P6.2, but row 6b stays CONDITIONAL on GN-G and P-HWbc.
- **B-4:** answered in §6.

## 6. B-4 / Row 14 — 9760 adoption record (quoted from re-hashed files; nothing adopted)
1. **Owner t433u** (3df38788…, line 6), verbatim: "Send report. Then adopt all proved from Professor Proof." Interpretation, line 16: "This does not adopt B1-c2′ overall (it stays COND) or 1a as the physical wall (that remains OPEN). Proved facts about those branches are adopted as facts." Coordinator dd7b747a…, line 20: "every MR2 result already audited by Professor Proof and ruled PROVED is adopted, under the scopes, premises, and accepted errata of the cited audits"; line 22: "1a is not adopted as the physical wall."
2. **MR2 adoption f3f6d65c…**
   - §A.6, line 27: "The remaining parent-tally PROVED rows in cc21b272 as amended … including the definitional 1a face match, the charge 9760, and the D1–D3 and D5 statements as graded there."
   - §C.19, line 58: "Batch-1 facts already PP-audited: definitional 1a face match and charge 9760 PROVED".
   - Line 60: "1a itself is not adopted".
3. **Supplement 85b42876…**, nit 1, line 12: "In that file the 9760 statement is D3 (9760 = n_inst + N_M5) … (D3 is the 9760 charge identity)."
4. **PP confirm eebd7dd7…**, line 29: "1a is not adopted as the physical wall. The definitional face match and the charge 9760 are adopted only as already-PROVED facts." Line 38: "D1–D3 and D5 are correctly listed as PROVED; D4 is not."
5. **What "as graded there" is.**
   - cc21b272, line 46: "**D3. 9760 = n_inst + N_M5. PROVED as an implication of the HW normalisation (f825dfff).**" Line 36 places it on "the 1a wall … the W-fixed constant-r face of the doubled MN2", "in HW normalisation c (f825dfff; HW citation COND)".
   - PP 1948 dee9410e, line 32, under "(1a) HW wall at the radial face": "N = 4880 and charge 9760: PROVED (carried from ERRATUM2)."
   - PP aeb9ab13, lines 71–74: "PROVED: N = 4880 exactly" (CLP-Ω flux in the MN2 working vacuum); "The wall charge 2N = 9760 is exact. It matches the f825dfff / NL E1 relation N_M5 + n_inst = 2N_flux"; "CONDITIONAL: E₈ identification".
   - PP 976e5621, line 110: an "in-vacuum normalisation result … not a physical theorem about the backreacted face, and it is not an adoption."
6. **OW 1108** c6375f85…: line 14 names "2N at N = 4880, total topological charge 9,760" inside a pursuit item; line 10 says "Nothing is adopted from the pasted text."
7. **OW 1130** 945d81bb…
   - Line 5 (coordinator standing summary, not Owner verbatim): "Already-adopted PP-PROVED results under the scoped t692u (Local) and t433u (MR2) instructions stay as adopted; … N = 4880 and total charge 9760 remain unadopted."
   - Line 11 (directive, verbatim substance): "including whether the unadopted charge 9760 premise can be replaced by an adopted value."
   - Line 16: "Charge 9760 remains unadopted. The assigned question is whether that premise can be replaced by an adopted value, not to adopt 9760."

**PP conclusion: the records are compatible once scoped, and no genuine conflict of Owner words remains.**
- (i) What t433u adopted is D3 (and the 1948 / aeb9ab13 facts) **as graded**. That is an implication identity, "n_inst + N_M5 = 2N_flux in HW normalisation (CONDITIONAL citation)", together with the in-vacuum MN2 normalisation N = 4880 on the 1a *definitional* face.
- (ii) What OW 1130 calls unadopted is 9760 as a **premise / physical wall charge** for the backreacted plane, which is f4ee61f2's rows 10/15 premise. Because 1a is not adopted as the physical wall (t433u line 16; eebd7dd7 line 29; OW 1130 line 5), adopted D3 does not attach to the backreacted face.
- OW 1130 line 5 itself asserts both sentences side by side, so the record treats them as compatible.
- PP invents no new Owner ruling. If the Owner meant otherwise, that is for the Owner; PP does not ping from this audit.

**Correction to the filing (F-4).** "If the t433u reading stands, adopted D3 already gives n_inst + N_M5 = 9760 ≠ 0, and row 13 follows from it directly" is **incorrect as stated**. Even under t433u, D3 is adopted only as an implication on the 1a/MN2 face with HW normalisation. It supplies no adopted value for the backreacted face.

**Answer to OW 1130's question:**
- No adopted value attaches to the backreacted face.
- The specific integer 9760 is **not needed**. Rows 11–13 need only S ≢ 0, which follows from N ≠ 0 plus adopted D2 (scoped by P-Y₆) and P-HWbc.
- 9760 is therefore replaced by a weaker, unadopted premise (P-N), not by an adopted value.

## 7. Tally
- MR2 filed: 9 / 3 / 2 / 2 = 16 + 1 bookkeeping.
- **PP ruled:**
  - **PROVED 9:** 1; 2 [D = 4 instance]; 3 [D = 4 instance]; 4; 5 [incl. D = 11, P4]; 6 [implication, L-GN named]; 7 [examples, A scoped]; 11 [implication, corrected premises]; 13 [implication, refined premises].
  - **CONDITIONAL 4:** **GN-G** (general-D rider of rows 2–3, L-GN); 6b; 8; 12b.
  - **OPEN 1:** 10.
  - **REFUTED 2:** 9 [Gauss-scalar scope]; 12 [implication, corrected premises].
  - **= 16, plus 2 bookkeeping** (integrity PROVED; R14 record answered, scoped-compatible).
- **Grade moves:**
  - (a) The general-D / D = 11 rider of rows 2–3 moves PROVED → CONDITIONAL (GN-G, L-GN), consistent with 976e5621 3G.
  - (b) Row 14 moves from OPEN (math) to a record row, answered. This is a record reading, not a math grade and not an Owner ruling.
  - Scope and premise fixes, with no grade change: rows 6, 7, 9, 11, 12, 13 and §5.
- **Other standing tallies unchanged:** t4436, Bridge C (PARTIAL), parent E₈ (17/2/4/0), f4ee61f2 as ruled in 976e5621 (12/3/2/1), NL 79ad0c64 (PP 5cf92795…), aeb9ab13, and the t433u adoption list. The E₈ wall sector stays CONDITIONAL. Junction UNSOLVED, carried, not counted.

## 8. Fixes for an additive MR2 erratum (do not edit 9811de14, its script or its log)
**Priority**
- **F-1 (rows 2–3):** scope to the D = 4 instance, and disclose the single background jet, t-independence and the one point. Carry the general-D rider as GN-G, CONDITIONAL on L-GN, until L-GN is proved in-file (976e5621 F-1). Name L-GN in rows 6, 6b, 8, 9 and 11.
- **F-2 (rows 11–12):** premise set {P-reg, P-Poinc, P-Israel, P-content incl. P-τ and "M5 worldvolume ∋ t"}, with L-GN for non-diagonal or x-dependent walls. State the "pointwise" scope precisely: non-gravitational density ≠ 0; gravitational-only and distributional sources are out of scope.
- **F-3 (row 13):** add P-Y₆ (D2 adopted only for that Y₆), the Z₂ fixing the fibre (in P-HW), no off-plane sources, and the HW integer normalisation (P-HWbc, CONDITIONAL). State that P-N is an unadopted premise. Note that D2 supplies the integrated n_R = 0.
- **F-4 (row 14 / §4):** withdraw "adopted D3 already gives … row 13 follows directly". Use the scoped reading of §6.
- **F-5 (row 7):** example A treats j as independent of f₁f₂. Replace it with f₂ = 0 (A′ = −11/16), or state the gravitational cancellation. B is robust.
- **F-6 (row 9):** retitle to the Gauss scalar-constraint scope. The full constraint set at a point is not exhibited.
- **F-7 (§5 item 6):** "elliptic-type" becomes "Riemannian-signature; ellipticity is B-1".

**Nits**
- N1: κ² convention, P-G versus Israel.
- N2: J3 accepts either sign; pin +.
- N3: J4a does not need the "diagonalisable" label.
- N4: ∫φ² = 1/(3ε) is not checked in-script; cite PP P9 or add a check.
- N5: filing mode 644.
- N6: the freeze/run same-second disclosure is fine as is.
- N7: row 5 is pinned at D = 11 by P4; cite it.
- N8: row 8 uniform δ needs compact Y₆; name the 4-form gauge.
- N9: B-3 may cite PP P6.1/P6.2.

## 9. What PP did not do
- PP did not first-prove L-GN and upgraded no row with it. P1 is corroboration only.
- PP did not construct or posit any metric.
- PP did not adopt 9760, N = 4880, N ≠ 0, P-Y₆ or P-HWbc.
- PP did not use any f4ee61f2 or NL grade as a premise, and did not wait on or mix in the Local dff4b879 audit.

## 10. Custody
- Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md`: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, mtime 2026-11-06 14:38:54 CST, mode 644. Hashed before this write (11:44:32 and 11:54:21 CST) and after (custody check below). **Untouched**, not chmodded.
- 9811de14, its script and log, both copies in /workspace/mr2-hw-curv-1110/, f4ee61f2, its QC note, script and log, 976e5621 and every quoted record were read and hashed only.
- No Local job (s1e, chain_v2, s2e, wait_then_ob_v5) or other agent directory was touched.
- No message was sent. Nothing adopted. No backreacted metric invented. Junction **UNSOLVED**. No CERT. Resonant algebra.
