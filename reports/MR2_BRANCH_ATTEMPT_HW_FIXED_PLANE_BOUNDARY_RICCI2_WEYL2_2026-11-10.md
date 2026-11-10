# MR2 — Branch attempt (UNADOPTED): HW fixed-plane boundary matching vs Ricci² / Weyl² divergence, reverse-engineered from the geometry
2026-11-10, written 11:24:09 CST (America/Chicago) by MR2 (executor). This is an additive new file; no existing file was edited. It is a labelled pursuit only. **Nothing is adopted.** No CERT. No Gemini. Nothing was sent. Junction **UNSOLVED**. Wording: resonant algebra.

## 0. Authority and scope
- **OW c6375f85…** (OWNER_WRITE_CALL_83d7a0fa_PURSUE_HW_ODD_G4_BRIDGE_C_CLOSING_IMPLICATIONS_2026-11-10_1108.md, sidecar MATCH, mtime 11:08:36). Assigned MR2 sentence, verbatim: "Math Research 2 must ensure the 11D curvature check's boundary terms matching onto the HW fixed plane do not trigger an irreversible divergence in Ricci² or Weyl²."
- **MR2 verbatim check 79710111…** (MR2_NOTE_CALL_83d7a0fa_1108_VERBATIM_INDEPENDENT_CHECK_2026-11-10.md, sidecar MATCH, mtime 11:11:42).
- **OW bff79185…** (OWNER_WRITE_CALL_83d7a0fa_REVERSE_ENGINEER_FROM_GEOMETRY_2026-11-10_1117.md, sha = sidecar, mtime 11:17:26). Method directive: start from the geometric side and work backward to the algebraic structures the geometry demands; report which geometric features force specific algebraic forms.
  - Disclosure, not edited: its header says "~11:17 CST", which is minute-level. Its sidecar records an absolute path rather than a relative name.
- **Scope.**
  - t4436 governs: the math leads, and no unproved option is adopted by fiat. t433u does not cover this work.
  - The caller's pasted figures (tension-to-charge 1.26–1.33 at the AdS end and 5/3 at the UV end) are **not adopted and not used** anywhere below.
  - 1a is not adopted as the physical wall. B1-c2′ is not adopted as the KK scope; Group A remains the KK scope.
  - The E₈ wall sector is treated as CONDITIONAL, gated by instanton backreaction across the flow.
- **Working assumption.** No pure uncharged M5 stack. The general theorems in §3 are source-agnostic and do not use one.
  - The one MN2 instance (E1) uses the filed unbackreacted kink (exact MN2 next to the wall). It is recorded only as branch **U** (unbackreacted, superseded as the working assumption).
  - I do **not** rely on 79795981 / e2750e28 / 1eb4cec4 / 395bff64 (wall Bianchi / J_M5). Their unbackreacted-wall premise conflicts with the new working assumption, so they are cited only as context.

## 1. Inventory (all sha = sidecar, verified this run)
| file | sha256 prefix | current grade used |
|---|---|---|
| MR2_MN2_Z2_WALL_BOUNDARY_CURVATURE_E8_BOLZA_2026-11-09.md | bd47ff5e | per PP aeb9ab13 |
| FINDINGS_PP_AUDIT_MR2_MN2_Z2_WALL_CURVATURE_E8_2026-11-09_1840.md | aeb9ab13 | (ii) Israel δ −6k/0/−8k PROVED; (iii) 1/ε² scaling with coefficients 16, 20, 64, 128/15 PROVED; (i) one-sided limits PROVED at samples, global/near-wall CONDITIONAL; N = 4880 and charge 9760 exact PROVED; thickness grading CONDITIONAL |
| MR2_ERRATUM_…SYSTOLE_LABEL / MR2_ERRATUM2_…PER_PP_aeb9ab13 | 2368ffbd / 5511845e | errata (context) |
| MR2_TWISTED_VACUA_EINSTEIN_SYMBOLIC_AND_GLOBAL_CURVATURE_2026-11-09.md | 78cac4c4 | 11D bulk curvature check (context) |
| FINDINGS_PP_AUDIT_MR2_ERRATUM2_GATE_SYMBOLIC_EINSTEIN_GLOBAL_CURVATURE_2026-11-09_1933.md | 205dbc3f | PP gate audit (context) |
| MR2_ERRATUM2_PER_PP_GATE_AUDIT_FULL11D_2026-11-09.md | 7b9ebdaf | context |
| MR2_CROSSCHECK_NL_BREATHING_MODE_CURVATURE_EFT_2026-11-09.md | b44cd004 | context |
| NL_DERIVED_Y16_HW_TRR2_WALL_STRESS_NEC_2026-11-09_1813.md (+ PP Y16 audit) | 7270a6b3 | −½tr R² is the only NEC-negative listed wall ingredient; magnitude CONDITIONAL (PP-1) |
| FINDINGS_PP_AUDIT_NL_Y14_STAGE2_Y15_FIBRE_ISRAEL_2026-11-09_1953.md | (read) | I2 null positivity PROVED for any YM field; PP corollary k_v ≤ k_x PROVED; Poincaré ⇒ no x-legs |
| OWNER_WRITE_MAINCHAT_t4369_…_1745.md / NL_DERIVED_ODD_HW_WALL_E8_MU_TIME_LOCALIZATION_…_1750.md | f825dfff / 4d9c9951 | citations only (face := Z₂ fixed plane, O1 odd) |
| 79795981 / e2750e28 / 1eb4cec4 / 395bff64 | MATCH | context only, not relied on (see §0) |

Searches:
- reports/ contains **no backreacted wall metric or ansatz**. A grep for "backreacted metric/ansatz" returns nothing. The blocker is recorded in row 14.
- Cheung–Gauntlett–Rosen is not needed here and is not cited.

## 2. Files of this filing
| file | sha256 | mtime (CST) |
|---|---|---|
| reports/mr2_hw_plane_ricci2_weyl2_2026-11-10.py | cd289c73043595e303fc5f2d5a0c2e7ba0b2fa5b5cdef33489dcf0231a9c695d | 11:21:00 (frozen chmod a-w, sidecar 11:21:00) |
| reports/mr2_hw_plane_ricci2_weyl2_2026-11-10.log | d5396417b7d3c3ad1212bb8748abe90b26910c89a448081334801038e10b6f23 | 11:21:49 (sidecar 11:21:55) |
| this .md | see .md.sha256 | header = mtime |

- **Freeze order.** Freeze at 11:21:00, then run. The log's first line is `RUN_START_WALLCLOCK 2026-11-10 11:21:05 CST` and its second is `SCRIPT_SHA256 cd289c73…` (= sidecar). So freeze ≤ run start. The run ended 11:21:49 with exit 0 and `ALL_CHECKS PASS` (33 checks).
- Originals are in /workspace/mr2-hw-curv-1110/ and were copied with `cp -p` (same sha).
- **Disclosure.** Before freezing I ran one scratch pre-test of an earlier draft as /tmp/scratch_pretest.py (sha 8fccc991…, run 11:20:05–11:20:48, all PASS). It differs from the frozen script only in replacing `simplify(…)==0` zero tests with canonical `expand(…)==0` / direct rational comparisons, plus one comment line. The pre-test is not cited as evidence.
- **Method.**
  - I wrote my own Christoffel, Riemann and Weyl code, evaluated at a point from the exact 2-jet of the metric.
  - Every quantity is a polynomial or rational function with rational coefficients. Zero tests use canonical polynomial forms (`Poly(...).is_zero`, `expand(...)==0`). No floats, no `simplify`.
  - In E1, `nsimplify` is used only to normalise an already-rational polynomial before list equality.
  - Validation V: for normal-coordinate jets, S² gives R = 2 and Riem² = 4; H² gives R = −2; S³ gives R = 6, Ric² = 12, Riem² = 12 and Weyl² = 0.

## 3. Premises (stated; every implication below names its premises)
- **P-HW.** The face is the HW-type Z₂ fixed plane (f825dfff): a codimension-1 timelike 10D hypersurface, with a Z₂-even metric (C⁰, Lipschitz across the plane) and G₄ odd.
- **P-reg.** Gaussian normal coordinates (y, x^a) exist near the plane. The extrinsic curvature K_ab is bounded on each side, with bounded tangential derivatives. A thin-wall smoothing has ∂_yK_ab = [K]_ab φ_ε(y) + bounded, with ∫φ_ε = 1.
- **P-Poinc.** The face is R^{1,3}-Poincaré invariant, as a constant-r face of an AdS₅ solution is. Then [K] = κ_x η ⊕ [K]_{Y₆} with Y₆ Riemannian, so [K]^a_b is real-diagonalisable, and the wall F has no x-legs (PP 1953, N6).
- **P-Israel.** S^a_b = −(1/κ²)([K]^a_b − δ^a_b[K]), the PP/NL convention.
- **P-2der.** Two-derivative 11D supergravity bulk action, plus HW boundary terms (tr F² − ½ tr R²) on the plane.
- **P-content.** Wall stress = E₈ YM (positive-definite trace) + M5s of tension τ ≥ 0, whose 6D worldvolumes lie inside the 10D plane. The −½ tr R² stress is excluded unless stated.
- **P-down.** The HW-native reading. The Z₂ quotient is a manifold with boundary (HW hep-th/9603142, title verified by PP). The wall δ-terms are boundary conditions (Israel / Gibbons–Hawking), and curvature invariants at the plane mean one-sided limits.
- **P-bulk.** The one-sided bulk metric is C² up to the plane, with bounded curvature.
- **P-G.** G₄ is bounded on each side. In branch U, all its components are tangent (filed C2, PROVED).

## 4. Results (exact; log section in brackets)
**Row 1 — routine validation [V] — PROVED.**

**Row 2 — δ² structure, 11D diagonal Gaussian-normal wall, generic point [A0–A6] — PROVED (exact).**
- Riem² = 4Σ(A″+A′²)² + 2Σ_{a≠b}(A′_aA′_b)², as an exact polynomial identity. Its degree in 1/ε is ≤ 2.
- With A″_a = −k_a/ε + r_a, the 1/ε² coefficients are, for every A′ and r:
  - Riem² (R_MNPQR^MNPQ): **4 tr k²**
  - Ricci-tensor square R_MNR^MN: **tr k² + (tr k)²**
  - R²: **4(tr k)²**
  - Weyl²: **(32/9)(tr k² − (tr k)²/10) = (32/9) tr k̃²**, where k̃ is traceless on the 10D plane
  - Gauss–Bonnet Riem² − 4Ric² + R²: **0 identically**

**Row 3 — generic [K] (non-diagonal, Lorentzian, x-dependent) [B1–B5] — PROVED (exact D = 4 model); general D as implication of P-reg + P-Poinc.**
- Only R_{yayb} carries 1/ε (B7). The coefficients are 4 tr M², tr M² + (tr M)², 4(tr M)², and (4(D−3)/(D−2))·tr M̃² for Weyl², with M = h⁻¹κ. Gauss–Bonnet gives 0.
- The general-D statement follows because the δ² coefficient is an invariant quadratic form in [K]. Under P-Poinc, [K] is diagonalisable, and the form is fixed by row 2.

**Row 4 — HW boundary terms on the plane [B6, B′1–B′3] — PROVED (exact model + index argument).**
- The pulled-back curvature 2-form R_{ab}{}^{MN} (both form legs tangent) has no 1/ε part. Its Gauss block R_abcd is Z₂-even (equal one-sided limits) and its Codazzi block R_yabc is Z₂-odd (opposite limits, nonzero).
- tr R∧R|_plane contains only Gauss·Gauss and Codazzi·Codazzi, so it is even, single-valued and δ-free. The same holds for tr F∧F.
- The one-sided limits of Riem², Ric², R and Weyl² are equal.
- **So the HW boundary terms themselves trigger no divergence.**

**Row 5 — δ² is non-integrable [C1–C2] — PROVED.**
- For φ_ε = sech²(y/ε)/(2ε): ∫φ_ε = 1 and ∫φ_ε² = 1/(3ε) exactly.
- For any mollifier supported in [−Lε, Lε], Cauchy–Schwarz gives ∫φ_ε² ≥ 1/(2Lε).
- So ∫Q√g dy ≥ Q_δ²/(c ε) − O(1) → ∞ whenever the δ² coefficient Q_δ² ≠ 0 (P-reg).

**Row 6 — not removable by coordinates; not a chart degeneracy — PROVED.**
- Q_δ² is a function of [K]^a_b only: tr[K]², (tr[K])², tr[K̃]². [K] is a geometric invariant of the hypersurface.
- This differs from chart zeros such as sin α·μ₁μ₂ = 0, which are not irreversible.

**Row 7 — Israel map [D1–D4] — PROVED (exact, given P-Israel, n = 10).**
- [K̃] = −κ²S̃ and tr[K] = (κ²/9) tr S.
- Weyl² δ² = (32/9)κ⁴ tr S̃², which is zero iff S ∝ h.
- Ric² δ² = tr[K]² + (tr[K])² is positive-definite on diagonalisable [K], so it is zero iff [K] = 0 iff S = 0. The same holds for Riem².

**Row 8 — uniqueness [F1] — PROVED.**
- αRiem² + βRic² + γR² is free of δ² for every wall iff (α, β, γ) ∝ (1, −4, 1), i.e. Gauss–Bonnet.

**Row 9 — null-positivity forces anisotropy [G1] — PROVED as implication of P-content.**
- On R^{1,9}, Σ_{k = t ± e_i}|F(k,·)|² is positive-definite in the 45 components of F (exact LDL; pivots {4, 16}).
- Proof that S ∝ h forces S = 0:
  - S ∝ h gives S(k,k) = 0 for every null k.
  - Both the E₈ part and the M5 part are ≥ 0 on null k, so each vanishes.
  - Then F = 0, and τ = 0 (take k = t + a direction transverse to the 6D worldvolume).
- So **S̃ = 0 ⇒ S = 0** within P-content.

**Row 10 — "E₈/instantons cancel the δ² under odd G₄" — REFUTED as implication of P-content + P-Israel + P-G + Bianchi charge 2N = 9760 (PP exact).**
- Odd G₄ with G bounded gives a bounded, Z₂-even G² and no δ in the Einstein equations. The δ-part of Ricci is exactly the Israel stress.
- A charge of 9760 needs n_inst ≠ 0 (so tr F∧F ≠ 0 and F ≠ 0) or M5s with τ > 0, so S ≠ 0.
- By row 9, S̃ ≠ 0 as well. So the Ricci², Riem² **and** Weyl² δ² coefficients are all strictly positive. E₈ fields add to them; they do not cancel them.

**Row 10b — same question with the −½ tr R² wall stress included — CONDITIONAL.**
- This is the only NEC-negative listed ingredient (Y16, PP Q15).
- Its integrated size is about 10³ too small (Y16 / Y15-R2, CONDITIONAL; PP-1 normalisation). A per-direction check is owed.

**Row 11 — instances [E1–E3] — PROVED (exact).**
- MN2 kink (branch U): coefficients 16, 20, 64 and 128/15 (Riem², Ric², R², Weyl², in a²). This reproduces PP aeb9ab13 §4.
- Umbilic wall: Weyl² δ² = 0 and Riem² = 40a², matching filed V1.
- BPS-type 1:1:0 stress: Weyl² δ² = (128/15)κ⁴τ² ≠ 0.

**Row 12 — verdict V-down — PROVED as implication of {P-HW, P-reg, P-Israel, P-2der, P-down, P-bulk, P-G}.**
- The 11D curvature check's boundary terms (Israel/GHY δ-weights, linear in [K], e.g. ∫R = 16k; HW tr F², tr R² terms) are finite and well-defined.
- Ricci² (both R_MNPQR^MNPQ and R_MNR^MN) and Weyl² at the plane are single-valued finite one-sided limits.
- **No irreversible divergence.**

**Row 13 — P-bulk discharged in branch U (exact MN2 next to the wall) — CONDITIONAL.**
- Bounded one-sided values are filed (Riem² sup 3408 per PP 384096a8; Ric² and Weyl² maxima from dense scans).
- The exact-MN2-near-wall premise is now superseded as the working assumption.

**Row 14 — P-bulk under the new working assumption (instanton backreaction across the flow, charged sources, non-supersymmetric face) — OPEN.**
- Exact blocker: there is no in-repo backreacted metric. Regularity of the backreacted bulk up to the plane has to be proved:
  - (a) For smooth finite-size instantons, S is smooth. Boundedness then needs C² regularity of the Einstein–Israel boundary-value problem, which is not proved here.
  - (b) For zero-size instantons or M5s localized on the plane (codim-5 point sources in 11D), near-source curvature depends on the extremality of the backreacted source. That is cited physics only (CONDITIONAL); no tension-to-charge figure is used or adopted.
- I did not invent a backreacted metric.

**Row 15 — verdict V-up — PROVED (yes, irreversible) as implication of {P-HW, P-reg, P-Poinc, P-Israel, P-content, P-G, charge 9760}.**
- If the check, or any effective action, evaluates a non-Gauss–Bonnet square (Riem², R_MNR^MN, R² or Weyl²) on the orbifold covering space across the δ-localized plane, the result is a non-integrable ∝1/(3ε) density.
- That density cannot be removed by coordinates (row 6) or cancelled by E₈ fields (row 10). It vanishes only for Gauss–Bonnet (row 8).

**Row 16 — ℓ_p⁶ R⁴ terms across a thin plane; finite thickness ε_y ≳ ℓ_p — OPEN.**
- t₈t₈R⁴ is not of Lovelock type. Lovelock quasi-linearity (at most one R_{yayb} factor per term) is cited, not computed here.
- Thickness is a physics premise (PP aeb9ab13 §4).

Junction: **UNSOLVED** (carried, not counted).

## 5. Verdict (plain)
- **Boundary matching formulated the HW-native way** (wall δ-terms treated as Israel/boundary conditions): the matching onto the HW fixed plane triggers **no irreversible divergence** in Ricci² (either R_MNPQR^MNPQ or R_MNR^MN) or Weyl².
  - The boundary terms are linear in [K]. The HW tr F² and tr R² densities are δ-free and single-valued.
  - Every curvature square takes a finite one-sided value at the plane.
  - This is PROVED as an implication of the premises in row 12. Its last premise, a bulk regular up to the plane, is the gate. It holds only conditionally in the superseded unbackreacted branch U, and it is **OPEN** for the backreacted, charged, non-supersymmetric working assumption, because no backreacted metric exists in-repo.
- **Squares evaluated on the covering space across a thin plane**: an irreversible divergence **is** triggered, PROVED as an implication.
  - The density is non-integrable, ∝ tr[K]² + (tr[K])² for the Ricci-tensor square and ∝ tr[K̃]² for Weyl².
  - Odd-G₄ E₈ instantons cannot cancel it. The only δ²-free quadratic combination is Gauss–Bonnet.
- **Effect of dropping the uncharged-M5 assumption:**
  - Rows 2–10 and 15 do not depend on it. Any positive-tension charged content only strengthens S ≠ 0 and S̃ ≠ 0.
  - What changes is P-bulk: the exact-MN2 bound is no longer the working input, and the bulk regularity question becomes OPEN.

## 6. Reverse-engineered from the geometry (per OW bff79185): geometric feature ⇒ forced algebraic form
1. **Thin codim-1 Z₂ plane** (Lipschitz metric) ⇒ the distributional curvature is rank-one in the normal direction, R_{yayb} = −[K]_ab δ.
   - So the only quadratic curvature form with a distributional meaning across the plane is **Gauss–Bonnet (1, −4, 1)**, unique (rows 3, 8). Lovelock forms are the cited higher-order analogue (row 16, OPEN).
2. **Z₂ parity of the fixed plane** ⇒ Gauss block even, Codazzi block odd (row 4).
   - So the HW boundary characteristic density tr R∧R|_plane must be built from Gauss² + Codazzi² pairings. It is forced to be single-valued and δ-free.
3. **Israel matching onto the plane** ⇒ the linear map [K̃] = −κ²S̃, tr[K] = (κ²/9) tr S (n = 10).
   - Weyl² sees only the traceless wall stress; the Ricci-tensor square sees all of it (row 7).
4. **R^{1,3} Poincaré invariance of the face** ⇒ the block form [K] = κ_x η ⊕ [K]_{Y₆}, real-diagonalisable. The wall F has no x-legs (P-Poinc; PP N6).
5. **Brane configuration** (E₈ YM on the plane + M5 6D worldvolumes inside it) ⇒ the null-positive quadratic form Σ_k|F(k,·)|² (PD, pivots {4, 16}). So the wall stress is never pure trace unless it vanishes: **the geometry forces a non-umbilic, anisotropic plane**, and Weyl² δ² > 0 (BPS 1:1:0 gives (128/15)κ⁴τ²) (rows 9, 11).
6. **Odd G₄ with tangent legs** ⇒ [G] = 2G and the charge balance N_M5 + n_inst = 2N = 9760 (filed, exact).
   - That forces S ≠ 0. G² is Z₂-even and bounded, so it contributes no δ (row 10).
7. **Junction (UNSOLVED geometric feature, not treated as solved)** ⇒ for NEC-respecting content, the pointwise inequality k_v ≤ k_x on every Σ and fibre direction (PP 1953 corollary, carried). The MN2 IR face violates it with margin k. Nothing here solves the junction.

## 7. Tally (this file; rows 1–16 including 10b; junction carried; one bookkeeping row for integrity)
- **PROVED 12:** rows 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12 (as implication), 15 (as implication).
- **CONDITIONAL 2:** rows 10b, 13.
- **OPEN 2:** rows 14, 16.
- **REFUTED 1:** row 10.
- **Total: 12 / 2 / 2 / 1 = 17 + 1 bookkeeping** (integrity: all cited shas = sidecars; script and log = sidecars; freeze ≤ run start). Junction UNSOLVED.

## 8. Blockers / next
- B-1 (row 14): a backreacted near-plane metric, or a regularity theorem for the Einstein–Israel boundary-value problem with smooth E₈ instanton data. Joint with NL's assigned E₈ stress-tensor pursuit.
- B-2 (row 10b): a per-direction −½ tr R² stress check.
- B-3 (row 16): an R⁴ / thickness analysis, beyond two-derivative supergravity.

Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 **MATCH** (checked before writing; re-checked after). Nothing adopted. No CERT. Nothing sent. Junction UNSOLVED.
