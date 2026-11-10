# FINDINGS — PP Soft SF confirmation of MR2 erratum 7d8fb406 (to f4ee61f2, per PP audit 976e5621) + independent verification of lemma L-GN
2026-11-10, written 12:37:32 CST (America/Chicago). Author: **Professor Proof (PP), Soft SF confirm.** Additive new file; no existing file edited, moved, renamed or deleted. **Nothing adopted.** No CERT. Nothing sent. Junction **UNSOLVED**. Wording: resonant algebra. Labels: PROVED / CONDITIONAL / OPEN / REFUTED. This is a confirmation, not a first proof: PP verified MR2's written proof and machine checks; PP did not substitute a proof of its own for MR2's.

## 0. Authority and scope
- **Authority:** PP audit `FINDINGS_PP_AUDIT_MR2_HW_PLANE_RICCI2_WEYL2_f4ee61f2_2026-11-10_1140.md` (976e5621…, mode 444, unedited); its §7 is the absorb checklist and line 65 defines L-GN. The rest of f4ee61f2 is not reopened.
- **Target:** MR2 erratum `MR2_ERRATUM_PP_AUDIT_HW_PLANE_RICCI2_WEYL2_f4ee61f2_2026-11-10.md` (7d8fb406…), plus its new script/log `mr2_lgn_gaussian_normal_lemma_2026-11-10.{py,log}`.
- **Out of scope, not opened, not used:** MR2 filing 9811de14, PP audit 81291f84 of it, and the 9811de14-related files that appeared in reports/ during this pass (an MR2 erratum of 9811de14 at 12:03:55 and a PP confirm of it at 12:07:54). They were seen only as directory-listing names. No grade from them is used or written here.
- Not adopted and not used as inputs: 9760, N = 4880, 1a as the physical wall, P-bulk, MN2 branch U. No backreacted metric invented. No PARI started. No Local job (s1e, chain_v2, s2e, wait_then_ob_v5, any ob_v4) touched. No other agent's directory written.

## 1. Integrity (re-hashed by PP this pass; all sha = sidecar where a sidecar exists)
| record | sha256 | notes |
|---|---|---|
| MR2 erratum (target) | 7d8fb4067a33c6f3530fd03610e15e981fe46e89c87660614b0d48b7c7ce6554 | = sidecar. Header "written 11:59:12 CST" = mtime 11:59:12.674968514; sidecar mtime 11:59:12.682968457; mode 644 (MR2 convention). |
| L-GN script `mr2_lgn_gaussian_normal_lemma_2026-11-10.py` | 1728d877918a96c8d91862483ade6b376ce6d91fdd531b1bb6881d138a3d0a50 | = sidecar; mode 444; content and sidecar mtime 11:57:34.719646170 (freeze). `cmp` identical to /workspace/mr2-hw-curv-1110/ copy. |
| L-GN log `mr2_lgn_gaussian_normal_lemma_2026-11-10.log` | 20f66fe318da09fcbaf192a923291fe31e1dbe9ca03de0dac59ffcff32a09177 | = sidecar; mode 444; mtime 11:57:44.271580967 (sidecar 11:57:44.387). `cmp` identical to the mr2-hw-curv-1110 copy. RUN_START 11:57:36 CST, 2 s after the freeze (clean, not same-second). SCRIPT_SHA256 line = 1728d877…. RUN_END 11:57:44. 21 PASS lines, 0 FAIL, then ALL_CHECKS PASS (not counted as a PASS). |
| parent f4ee61f2 `MR2_BRANCH_ATTEMPT_HW_FIXED_PLANE_BOUNDARY_RICCI2_WEYL2_2026-11-10.md` | f4ee61f26ad536800792b510f29f714c9c622fd11a8c378e545a8a38976c330d | = sidecar; mtime 11:24:09.339; mode 644; unedited. |
| QC note 66f04088 | 66f040887ebe660a6d540963b76f005ccd504e9d3e0f1a96b9b842b50f16e2bc | = sidecar; mtime 11:25:54.549 (sidecar 11:25:54.546); mode 644; unedited. |
| parent frozen script `mr2_hw_plane_ricci2_weyl2_2026-11-10.py` | cd289c73043595e303fc5f2d5a0c2e7ba0b2fa5b5cdef33489dcf0231a9c695d | = sidecar; reports/ and mr2-hw-curv-1110/ copies `cmp` equal; mode 444; unedited. |
| parent frozen log `mr2_hw_plane_ricci2_weyl2_2026-11-10.log` | d5396417b7d3c3ad1212bb8748abe90b26910c89a448081334801038e10b6f23 | = sidecar; both copies `cmp` equal; mode 444; unedited. |
| PP audit 976e5621 | 976e56211308cf68e8ad80df063f99e08826d441e0f4d8a45242ad6fad01031c | = sidecar; mode 444; written 11:40:51 = mtime; unedited. |
| PP 1953 (N3) `FINDINGS_PP_AUDIT_NL_Y14_STAGE2_Y15_FIBRE_ISRAEL_2026-11-09_1953.md` | 077e417db7f24ece269d7dcde21bc89e260bbe1102d985c63ab60aa94813c23b | = sidecar = the value MR2 cites. |
| PP Y16 audit (N3b) `FINDINGS_PP_AUDIT_NL_Y16_TRR2_WALL_STRESS_AND_ERRATUM12_2026-11-09_1826.md` | 149be02a794917d92f36c7a2383bbb4eb74623bb4f7b57dd111ad09f73ba7293 | = sidecar = the value MR2 cites. |
| tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` (before) | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | 12:03:48 CST, before any PP write; mtime 2026-11-06 14:38:54.160403807 CST; mode 644. |
| tip (after) | see §10 | re-hashed after all evidence writes; result recorded in §10. |

Bookkeeping (integrity of the target set): **PROVED.**

## 2. Evidence (`reports/evidence_pp_confirm_mr2_erratum_f4ee61f2_7d8fb406_2026-11-10/`; every file mode 444 with a `.sha256` sidecar; `sha256sum -c` passes on all 13 sidecars)
| file | sha256 | content |
|---|---|---|
| mr2_lgn_gaussian_normal_lemma_2026-11-10.py | 1728d877918a96c8d91862483ade6b376ce6d91fdd531b1bb6881d138a3d0a50 | byte-identical copy of the frozen script (`cmp` equal); the frozen originals were not modified. |
| pp_rerun.log | ad655761ef911f5482cdab91b3a9d3210189ab48f4e2062cef0199c08fe12724 | re-run 12:05:45–12:05:53 CST (7.8 s). 21 PASS, 0 FAIL, ALL_CHECKS PASS. |
| pp_rerun.exit / pp_rerun.stderr | d4e49dd8b59469b9ec9b4026c9796f2e272e46b3e0dfe7486db13f05630cfbf9 / e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | `EXIT 0` / empty. |
| pp_rerun_vs_mr2_log.diff.txt | 3ba4d64fb4b17264adb2a2ed4e79868ea590bf78571ac5613f96ca5024402dc8 | only line 1 (RUN_START) and line 36 (RUN_END) differ, both wall clock. Lines 2–35 byte-identical, including SCRIPT_SHA256 and all 21 PASS lines. |
| pp_namespace_scan.py / .log | a025811b1d27752cdb46ee2d7309d2d675c1d8904376ce11724ce2099f6c34b4 / dada3fc06594ac734b8f4c5e954e265b2bbc138fe97e87ffacee4f3347305b01 | source + AST scan of the MR2 script. ALL_CHECKS PASS. |
| pp_independent_checks.py | 1b8cd3c676c655b9a0aca183fd3fcdfe7d016ec25a88dadb25ed51f8c769b90f | PP's own code; no MR2 routine imported. Frozen (444 + sidecar) 12:22:23.9; run started 12:22:25 (2 s later). |
| pp_independent_checks.log | 66b8ecb53186f843ce0e208d23ee170271f0bac96c83914ddfb65b2df6b45eee | 12:22:25–12:34:18 CST. SCRIPT_SHA256 line = 1b8cd3c6…. **120 PASS, 0 FAIL**, ALL_CHECKS PASS (not counted). |
| pp_independent_checks.exit / .stderr | d4e49dd8b59469b9ec9b4026c9796f2e272e46b3e0dfe7486db13f05630cfbf9 / e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | `EXIT 0` / empty. |
| pp_own_script_scan.py / .log | f6036c15bf007e51fe8bf072963e98215e00743c720bc43e4bebbda3f85715df / bd666a33157817992c8547279d7ff42120ebf594964f9efc165c01bd297afdce | scan of PP's own script: no nsimplify/simplify/numpy/allclose/evalf/float/Float/mpmath, no float literals, no MR2 import or MR2 routine name. ALL_CHECKS PASS. |

**Namespace scan of the MR2 script (pp_namespace_scan.log):**
- Zero code hits for `nsimplify`, bare `simplify(`, `numpy`, `np.`, `allclose`, `evalf`, `float(`, `Float`, `N(`, `mpmath`, `random`, `trigsimp`, `solve(`. No float literals in the AST. Imports are stdlib + SymPy only.
- Zero tests: `Poly(...).is_zero`, `expand(...) == 0`, `sp.diff(...) == 0` on expanded polynomials, Rational equality. `sp.integrate` and `sp.cancel` appear only in C2c/C2d (exact symbolic, positive symbols).
- MR2's disclosure that `nsimplify` was replaced by `cancel` in C2d before freeze is consistent: the frozen file has no `nsimplify`. The pre-freeze scratch files (/tmp/scratch_pretest3*.py) are disclosed as not cited; PP did not use them.

**PP first-draft disclosure.** Draft 1 of pp_independent_checks.py crashed (Python `AttributeError: 'int' object has no attribute 'subs'` in the L-GN(d') step, because zero components were stored as Python ints). It was a crash, not a false PASS. It was fixed with `sp.S(...)`. Draft 2 ran 120 PASS / 0 FAIL. Before freezing, one label (B4) was reworded to state exactly what is computed (R^y_ayb, which equals R_yayb because g_yy = 1, g^ya = 0); the logic did not change. Only the frozen final version (1b8cd3c6…) and its log are cited. The drafts are in /tmp and are not evidence.

## 3. Item-by-item absorb of 976e5621 §7
| item | verdict | basis |
|---|---|---|
| **F-1** state and prove L-GN | **ABSORBED** | Stated in erratum §2 (a)–(d). The written proof is verified in §4 below: correct and complete for the stated scope, with non-blocking wording nits (n1–n3). |
| **F-2** rows 10/15 premise sets | **ABSORBED** | Row 10 now lists P-content, P-Israel, P-G/P-2der, **P-Poinc**, **P-τ**, **n_R = 0** (−½ tr R² out of the charge as well as the stress; n_R ≠ 0 moved to 10b), **L-GN**, and **Q_plane ≠ 0**, with 9760 described as "an in-repo stated premise (PP aeb9ab13, MN2 branch-U normalisation) and is not adopted". Row 15 lists {P-HW, P-reg, P-Poinc, P-Israel, P-content, P-τ, n_R = 0, P-G, L-GN, Q_plane ≠ 0}. Row 10b absorbs n_R ≠ 0. Grades are as ruled. |
| **F-3** row 7 D3 | **ABSORBED** | Both "zero iff" statements are scoped to real-diagonalisable [K] (P-Poinc), and the P7.5 null counterexample is quoted. PP re-checked P7.5 exactly (D10). |
| **F-4** row 12 / §5 bullet 1 | **ABSORBED** | The lead now opens "as an implication, gated by P-bulk, which is OPEN under the working assumption". "F bounded on the plane" was added to row 12's premises. P-reg is stated to exclude zero-size instantons and plane-localized M5s (row 14(b)). The OW 1108 item is "reduced to B-1 (row 14), not discharged". P-bulk is not upgraded. |
| **F-5** §6 items 5, 6 | **ABSORBED** | Item 5 is an implication of {P-content, P-Israel, P-Poinc, P-τ, Q_plane ≠ 0}, and row 9 alone gives only S̃ = 0 ⇒ S = 0. Item 6 says "forces only the form", 9760 is an in-repo stated premise not adopted, and "(filed, exact)" is withdrawn (QC N2 folded). |
| N1 author line | **ABSORBED** | "by MR2", identified in §7 as Math Research 2. The parent's title wording is left unedited, as required. |
| N3 citations | **ABSORBED** | 077e417d… and 149be02a… cited in full. PP re-hashed both: each = sidecar (§1). |
| Row 3 disclosure | **ABSORBED** | One background jet (h0, h1, h2 at u = ½), 5-parameter κ with κ_tv = 0. The D = 4 instance stays PROVED in that scope. |
| Row 9 premise | **ABSORBED** | "each M5 worldvolume contains the time direction t" is named. |
| C2 | **ABSORBED with nit (n5)** | I2 and the box/bump values are now computed, not hard-coded. But C2a is tautological, and the Cauchy–Schwarz *bound* is checked only on two instances (the equality case and one bump), not as a general inequality. The general inequality was already PP-PROVED (976e5621 P5). PP's E1–E4 check the antiderivatives and values properly. No grade depends on this. |
| Modes | **ABSORBED** | Parent and QC .md are mode 644 by convention; frozen script/log are 444; nothing was chmod-ed. |
| QC mtime 2.7 ms | **ABSORBED (as disclosure)** | MR2 states it cannot tell from its session how the mtime was set, and notes that the content matches the 66f04088 sidecar. That is an honest answer. The observation stays a recorded nit, not a required fix. |

**Confirm verdict: FAITHFUL.** Every §7 item is absorbed. There is no self-upgrade: the erratum keeps the ruled 12/3/2/1 and only *proposes* 13/2/2/1. Parent, QC note, parent script/log and 976e5621 are byte-unchanged. No 9811de14 content is mixed in. The erratum's only reference to it is a non-action sentence in §3, which PP has not checked against that filing.

## 4. L-GN verification (load-bearing)
**Statement verified.** In g = dy² + h_ab(y, x) dx^a dx^b with K_ab := ½∂_y h_ab:
- (a) R_abcd has at most first y-derivatives of h.
- (b) R_yabc has at most first y-derivatives of h (mixed ∂_x∂_y h allowed).
- (c) R_yayb = −∂_yK_ab + K_acK^c_b.
- (d) ∂_y²h enters Riemann only through (c).

PP's convention: R^ρ_σμν = ∂_μΓ^ρ_νσ − ∂_νΓ^ρ_μσ + Γ^ρ_μλΓ^λ_νσ − Γ^ρ_νλΓ^λ_μσ, with R_ρσμν = g_ρα R^α_σμν. It is the same as MR2's, and sphere-positive.

**Step-by-step check of MR2 §2:**
1. **Christoffels — CONFIRMED.** g^yy = 1 and g^ya = 0 exactly, so g⁻¹ is block-diagonal.
   - Γ^y_ab = ½(−∂_y h_ab) = −K_ab.
   - Γ^a_yb = ½h^ac ∂_y h_cb = K^a_b.
   - Γ^a_bc = ½h^ad(∂_b h_dc + ∂_c h_db − ∂_d h_bc) = γ^a_bc[h], which involves only tangent derivatives of h.
   - Γ^y_yy = Γ^y_ya = Γ^a_yy = 0, because every term contains a derivative of g_yy = 1 or of g_ya = 0.
   - Exact checks: A1–A4 (values and all first derivatives at a point) on fully general 2-jets in five cases, and B1 with arbitrary functions h_ab(y, x) in D = 3, 4.
2. **"Every Γ has at most first derivatives; y-derivatives only through K" — CONFIRMED.** The second clause, read with step 3, needs one remark that MR2 leaves implicit (n2): ∂_yγ[h] contains ∂_y h⁻¹ = −2h⁻¹Kh⁻¹ and ∂_y∂_x h = 2∂_xK, so it carries only K and ∂_xK, never ∂_y²h. Exact check A3g.
3. **"∂_y²h only from ∂_y acting on K, which requires μ = y or ν = y" — CONFIRMED.** The ΓΓ terms carry at most first derivatives. The ∂Γ terms carry ∂_y²h only when the derivative index is y and Γ ∈ {Γ^y_ab, Γ^a_yb}.
4. **(a) Gauss — CONFIRMED.** With μ, ν tangent, R^a_bcd and R^y_bcd see only ∂_x. Lowering with h (g_ay = 0) adds no derivative. Exact: L-GN(a) in all five jet cases, and B2 (functional, y-derivative order ≤ 1) in D = 3, 4.
5. **(b) Codazzi — CONFIRMED, including the mixed placements.** R^y_abc = ∂_bΓ^y_ca − ∂_cΓ^y_ba + ΓΓ has only ∂_xK. PP checked:
   - all-lowered R_yabc;
   - R^y_abc;
   - R^a_ybc (μ, ν tangent ⇒ only ∂_x);
   - R^a_byc and R^a_bcy (here ∂_y hits Γ^a_cb = γ[h], giving only ∂_y∂_x h and ∂_y h⁻¹; the ∂_c Γ^a_yb term is ∂_xK).

   Exact: L-GN(b) (all four placements plus lowered) in all jet cases, and B3 functional in D = 3, 4. MR2's own machine check covers only the all-lowered R_yabc; PP covers the rest.
6. **(c) Ricci equation — CONFIRMED, including sign and lowering.**
   - R^y_ayb = ∂_yΓ^y_ba − ∂_bΓ^y_ya + Γ^y_yλΓ^λ_ba − Γ^y_bλΓ^λ_ya.
   - The terms are −∂_yK_ab, 0, 0, and −(−K_bc)(K^c_a) respectively (the λ = y term of the last product vanishes).
   - Hence R^y_ayb = −∂_yK_ab + K_acK^c_b.
   - Lowering: R_yayb = g_yy R^y_ayb + g_yc R^c_ayb = R^y_ayb.
   - Sign: unit S² in GN form, g = dy² + sin²y dθ², gives R_yθyθ = sin²y > 0, and −∂_yK + KK^c = −(cos²y − sin²y) + cos²y = sin²y (C1). Unit S³ with x-dependent h gives sectional curvature +1 and Codazzi = 0 (C2).
   - Exact: L-GN(c), L-GN(c′) in all jet cases, and B4 functional in D = 3, 4 (numerator of `together` expands to 0).
7. **(d) — CONFIRMED.** MR2 asserts this step; PP checked it. Classify all-lowered components by the number of y indices:
   - 0 y: Gauss (a).
   - 1 y: R_yabc, and R_aybc, R_abyc, R_abcy, which equal ∓R_yabc, R_ycab and −R_ycab by antisymmetry and pair symmetry. All Codazzi (b).
   - 2 y in the same pair: 0.
   - 2 y in different pairs: R_yayb, R_yaby = −R_yayb, R_ayyb = −R_yayb, R_ayby = R_yayb. All (c).
   - 3 or 4 y: some pair is (y, y), so 0.

   Raised placements are g⁻¹-images, and g⁻¹ is block-diagonal and undifferentiated, so they add no derivatives. The list is complete. Exact check L-GN(d)/(d′): on fully general jets, for **every one** of the D⁴ lowered components and every one of the D⁴ first-index-raised components, the part depending on the ∂_y²h jet equals exactly the (c) pattern transported by these symmetries (resp. its g⁻¹-image), and is 0 elsewhere (D = 4: 256 + 256; D = 5: 625 + 625 in each of three signatures; D = 6: 1296 + 1296).
8. **"No step uses D, the signature or the form of h" — CONFIRMED,** within the scope in n1. No diagonality and no x-independence is used anywhere. PP's checks use non-diagonal, x-dependent h of Euclidean, Lorentzian and split (2,2) signature (SIG lines use exact LDL pivots), while MR2's checks use h(0) = η only. Two independent routes (Γ-route vs. metric-jet formula, A5) agree on every component.

**Gap?** None that affects the claim. Non-blocking wording nits (n1–n3, not required fixes):
- **n1 (scope implicit):** h is nondegenerate (h⁻¹ exists) and C² off the wall, and the normal is unit spacelike (g_yy = +1, as written in the GN form). "Any signature" means any nondegenerate signature of h. A timelike normal (g_yy = −1) or a null hypersurface is outside the stated GN form. Both conditions hold for the HW plane as used.
- **n2:** step 2's "y-derivatives appear only through K" should mention ∂_y h⁻¹ and ∂_y∂_x h in ∂_yγ[h] (both are K-type). Implicit and correct.
- **n3:** step 7 is asserted, not written out; the enumeration above is routine. The final remark "sign conventions K → −K leave (a)–(d) unchanged" is true but not needed.

**Instance corroboration vs. general proof.** MR2's D = 4, 5, 6 and GK0–GK5 checks, and PP's own A/B/C/D checks, are **corroboration**. The general PROVED rests on the verified index-generic written proof (steps 1–7). PP did not upgrade on machine checks alone.

**MR2 machine-check scope notes (nits, not required fixes):**
- **n4:** "fully general 2-jets" is true up to the normalisation h(0) = η. That normalisation fixes the Lorentzian signature in MR2's checks.
- **n4b:** GK0–GK5 use a restricted jet with no ∂_x∂_y h and no ∂_x²h, h(0) = η. PP D1/D1b redo affine-in-w and the w-coefficient pattern on a fully general D = 5 jet with non-diagonal h0.
- **n6:** the GK4 log label reads "(8/3)(trM^2 - trM^2/4)"; it should read (tr M)²/4. The code (`t1**2/4`) is correct.

**L-GN verdict: PROVED as written** (index-generic; scope n1). It is a lemma, not a premise.

## 5. Coefficient extraction for 3G (re-derived by PP)
**By hand, any D.** Under P-reg, h and K are continuous and bounded across the smoothed wall, and ∂_yK_ab = [K]_ab φ_ε + bounded. By L-GN the only 1/ε part of Riemann is R1_yayb = −[K]_ab and its three symmetry images (yaby, ayyb: +; ayby: −). Let M := h⁻¹[K] (mixed).
- Riem² δ²-coefficient: four placements, each [K]_ab[K]^ab, giving **4 tr M²**.
- Ricci: Ric_ab ⊃ g^yy R1_yayb = −[K]_ab; Ric_yy ⊃ h^ab R1_ayby = −tr M; Ric_ya has no 1/ε. So Ric² gives **tr M² + (tr M)²**, R gives **−2 tr M**, and R² gives 4(tr M)².
- Weyl²: by |W|² = |Riem|² − 4/(D−2)|Ric|² + 2/((D−1)(D−2))R² (valid for any algebraic curvature tensor, applied to R1) the coefficient is **4(D−3)/(D−2)·(tr M² − (tr M)²/(D−1))**. This is PP P3D.1 and is re-checked symbolically in D (D8).
- Gauss–Bonnet: 4t₂ − 4(t₂ + t₁²) + 4t₁² = **0** (D9).

**Exact checks:**
- D1/D1b (D = 5 full jet): affine in w; w-part = R1 pattern, κ-only.
- D2–D7 in D = 3, 4, 5, 6, 7 and **11**, each with non-diagonal h0 and all κ entries symbolic, κ_tv included: Riem², Ric², R, explicit-Weyl², GB, and Weyl tracelessness.
- D8–D9: symbolic D.

These match MR2's GK1–GK5 (D = 5), and 976e5621 had already accepted this step given L-GN.

## 6. 3G verdict
- **3G: CONDITIONAL → PROVED as implication of {P-reg, L-GN}, with L-GN now itself PROVED** (scope n1: GN form with spacelike unit normal, nondegenerate h). Both conditions of the regrade rule hold: (i) the index-generic written proof is correct and complete (§4); (ii) the general-D coefficient extraction is re-derived by PP (§5) and is already covered by P3D.1.
- **"Zero iff" stays scoped by P-Poinc** (real-diagonalisable [K]); the P7.5 null counterexample stands (D10).
- **No other grade moves.** Rows that inherited 3G (4-general, 6, 7-composite, 8-general, 10, 15, §6.1) keep their ruled grades. Their named premise L-GN is now a PROVED lemma, so it is discharged as a premise and no longer open. Row 4 stays "PROVED, scoped" as ruled; PP does not regrade it here.
- **Accepting L-GN does not:**
  - upgrade P-bulk (OPEN under the working assumption);
  - close V-down;
  - discharge the OW 1108 MR2 item, which stays reduced to B-1 (row 14);
  - adopt 9760, which stays an inessential in-repo stated premise (Q_plane ≠ 0 suffices).

Row 13 stays CONDITIONAL, and rows 14 and 16 stay OPEN.
- Non-action note: a general L-GN, if accepted, would be available to a later additive erratum of 9811de14. PP does not regrade that filing here.

## 7. Grades / tally
- **f4ee61f2, ruled by 976e5621 (before this confirm):** 12 PROVED / 3 CONDITIONAL (10b, 13, 3G) / 2 OPEN (14, 16) / 1 REFUTED (10) = 18 + 1 bookkeeping.
- **MR2 proposed:** 13 / 2 / 2 / 1 = 18 + 1.
- **PP ruling in this confirm:** **13 PROVED** (1, 2, 3 [D = 4 instance], **3G [impl. of P-reg; L-GN PROVED]**, 4 [scoped], 5, 6, 7, 8, 9 [impl.], 11, 12 [impl.], 15 [impl., corrected premises]) / **2 CONDITIONAL** (10b, 13) / **2 OPEN** (14, 16) / **1 REFUTED** (10, impl., corrected premises) **= 18 + 1 bookkeeping.** PP agrees with MR2's proposal. This becomes the standing tally only when the parent accepts this confirm.
- Parent E₈ already-ruled tally unchanged: **18/2/4/0 = 24 + 1 bookkeeping** (after the accepted row-22 split, e2750e28 / 395bff64).
- t4436 is unchanged and Bridge C stays **PARTIAL**. The E₈ wall sector stays CONDITIONAL. Nothing adopted. Junction UNSOLVED, carried and not counted. No CERT.

## 8. Leftover required fixes
**None.** The confirm is FAITHFUL and L-GN is accepted. Optional wording nits for any future MR2 filing (no erratum required):
- n1: state the nondegenerate-h / spacelike-unit-normal / C² scope of L-GN explicitly.
- n2: mention ∂_y h⁻¹ and ∂_y∂_x h in ∂_yγ[h].
- n3: write out the step-7 enumeration.
- n4: MR2's machine checks fix h(0) = η (Lorentzian); n4b: GK uses a restricted jet.
- n5: C2a is tautological, and C2c/C2d are instances of the CS bound, not the inequality.
- n6: GK4 label typo, (tr M)²/4.

## 9. Observations
- The GK0 "κ_tv = 0 scope closed" claim holds for the D = 5 coefficient identities. The ruled D = 4 row-3 instance (one jet, κ_tv = 0) is unchanged as an instance and is superseded in scope by 3G.
- MR2's erratum §3 contains a sentence about the 9760 adoption-record conflict in 9811de14. It is non-action, and PP has not checked it against that filing.

## 10. Custody
- Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md`:
  - **before** (12:03:48 CST, before any PP write): 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, mtime 2026-11-06 14:38:54.160403807 CST, mode 644.
  - **after** (re-hashed at 12:37:29 CST, after all evidence writes and immediately before this file was written; this file's write does not touch the tip): 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, mtime 2026-11-06 14:38:54.160403807 CST, mode 644. **UNCHANGED (sha, mtime, mode match before).**
  - Never written or chmod-ed.
- MR2 erratum, L-GN script/log and sidecars, parent f4ee61f2, QC note 66f04088, parent frozen script/log (reports/ and /workspace/mr2-hw-curv-1110/), and PP 976e5621 were read and hashed only. Their hashes are unchanged at 12:35:34 CST.
- 9811de14, PP 81291f84 and later 9811de14-related files were not opened. No Local job, PARI, or other agent's directory was touched.
- **This file's mtime** was set with `touch -d` to exactly the header time (.000000000) after its content was written, and before the sidecar was hashed. The `.sha256` sidecar (relative filename) hashes the final bytes. Both files are chmod 444. The markdown is not edited after hashing.
- No message sent. Nothing adopted. No backreacted metric invented. Junction **UNSOLVED**. No CERT.
