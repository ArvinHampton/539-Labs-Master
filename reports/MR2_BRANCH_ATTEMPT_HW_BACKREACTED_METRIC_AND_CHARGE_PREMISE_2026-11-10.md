# MR2 — Branch attempt (UNADOPTED): backreacted near-plane metric (construct or rule out) and the covering-space δ² claim without the 9760 value — HW Z₂ plane
2026-11-10, written 11:39:48 CST (America/Chicago), by MR2. This is an additive new file; no existing file was edited. f4ee61f2 and its script and log are untouched. Pursuit only. **Nothing is adopted.** No CERT. No Gemini. Nothing was sent. Junction **UNSOLVED**. Wording: resonant algebra.

## 0. Authority and scope
- **OW 945d81bb…** (OWNER_WRITE_CALL_83d7a0fa_PURSUE_OPEN_ITEMS_UNAUDITED_FILINGS_2026-11-10_1130.md): sha = sidecar, mtime 11:31:15. Disclosure, not edited: its header says "written 11:31 CST", which is minute-level.
  - MR2 parts, verbatim: "bulk regularity up to the Hořava–Witten plane is open once instantons backreact — there is no backreacted metric on disk; construct or rule out one. Also address the non-integrable one-over-epsilon density on the covering space that E-eight instantons do not cancel, including whether the unadopted charge 9760 premise can be replaced by an adopted value."
- The 11:08 directive (c6375f85…) and the 11:17 directive (bff79185…, work backward from the geometry) continue to apply. t4436 stands. t433u does not cover this work.
- **Not used as proved inputs:**
  - MR2 f4ee61f2… (my 11:24 filing) and its grades are unadopted, so every result reused here is re-derived in this filing's frozen script (§4 K).
  - NL_DERIVED_E8_INSTANTON_GEOMETRIC_DELTA_ODD_G4_2026-11-10_1120.md (79ad0c64…, sha = sidecar) is cited only. Its grades are not adopted.
- **Also not adopted:** the pasted tension-to-charge figures (not used), 1a as the physical wall, and B1-c2′ as the KK scope (Group A remains the KK scope). The working assumption is no pure uncharged M5 stack, with instanton backreaction across the flow; the E₈ wall sector is CONDITIONAL.

## 1. Files
| file (reports/) | sha256 | times (CST) |
|---|---|---|
| mr2_hw_backreact_jet_charge_2026-11-10.py | 2d8092a779b8ed5cf4118d05f054ff9ccf227dbe10fc754a93d645ba10c75d5c | content mtime 11:36:54; sidecar + chmod a-w 11:37:27.74 |
| mr2_hw_backreact_jet_charge_2026-11-10.log | 7634069fcc9700debd53ab57b7e10aca703cec460c630ca61034196933524dbb | 11:37:53 (sidecar 11:37:53) |
| this .md | see .md.sha256 | header = mtime |

- **Run record.** The log begins `RUN_START_WALLCLOCK 2026-11-10 11:37:27 CST`, then `SCRIPT_SHA256 2d8092a7…` (= sidecar). It ends with exit 0, `ALL_CHECKS PASS` (20 checks) and `RUN_END 11:37:53`. Originals are in /workspace/mr2-hw-curv-1110/, copied with `cp -p`.
- **Disclosure: freeze vs run start.** The freeze (sidecar written at 11:37:27.74) and the run start fall in the same second. The log stamp has one-second resolution. The two steps ran sequentially in one `&&` chain, freeze first, but the log alone cannot prove sub-second order.
- **Disclosure: pre-freeze scratch runs.**
  - /tmp/scratch_pretest2.py with sha 29674c91… crashed on a leftover placeholder line.
  - A second scratch run, byte-identical to the frozen script (sha 2d8092a7…), ran in /tmp from about 11:36:54 to 11:37:19 with all checks passing.
  - Neither is cited. The cited evidence is only the post-freeze log.
- **Method.** Own curvature code, exact 2-jets. Zero tests use `expand(...)==0` / `Poly.is_zero` on rational polynomials, exact LDL, and rational comparisons. No `simplify`, no floats.

## 2. Premises
- **P-HW** (f825dfff, CONDITIONAL premise): a Z₂ fixed plane, codim-1 and timelike, with a Z₂-even metric and odd G₄.
- **P-HWbc**: the HW boundary condition G_t(0⁺) = ½J, where J is the wall 4-form density (M5 + E₈ + gravitational). Cited from HW hep-th/9603142 and consistent with NL GA2 (cited only). CONDITIONAL premise.
- **P-reg / P-Poinc / P-Israel / P-content**: as stated in f4ee61f2, restated here.
  - Gaussian normal coordinates.
  - R^{1,3} Poincaré invariance, so [K] is real-diagonalisable and the normal-leg 3-form H lives on Y₆.
  - Israel junction S = −(1/κ²)([K] − h[K]), and with Z₂, K⁺ − hK⁺ = −(κ²/2)S.
  - Wall content = E₈ YM (positive trace) + M5s with τ ≥ 0, with τ > 0 wherever their density is nonzero. The gravitational −½tr R² stress is excluded unless stated.
- **P-G**: bulk normalisation G_MN = (1/12)(G_MPQR G_N^PQR − (1/8)g_MN G²) at the plane.
- **P-N**: the fibre flux integer N ≠ 0. This is weaker than N = 4880, which stays unadopted.
- **A-D2 (adopted under t433u A.6; listed in the supplement 85b42876 nit 1; PP confirm eebd7dd7 lists D1–D3 and D5 as PROVED):** p₁(TY₆) = 0, so ½tr R∧R is exact on Y₆ and carries no integrated wall charge. This statement is topological and does not change under backreaction of the metric.

## 3. Task 1 — backreacted near-plane metric: construct or rule out
Starting from the geometry: a timelike Z₂ plane in an Einstein–4-form bulk.

**Row 1 — validation [V1–V2] — PROVED.** S² gives R = 2 and S³ gives R = 6.

**Row 2 — the equations split into constraints and evolution [J1a–c] — PROVED (exact; D = 4, Lorentzian, non-diagonal, x-dependent model with a fully symbolic second y-jet).**
- G_yy and G_ya contain no ∂_y²h.
- R_ab = −½∂_y²h_ab + (terms free of ∂_y²h), with unit coefficient. So the second y-jet is solved for algebraically.
- The structure is index-generic (Gauss–Codazzi–Ricci), so it holds in D = 11.

**Row 3 — Gauss and Codazzi constraints [J2–J3] — PROVED (exact).**
- Gauss: 2G_yy = −r[h] + (tr K)² − tr K².
- Codazzi: G_ya = D_bK^b_a − D_aK (the sign fixed by the run is +).

**Row 4 — Z₂–Israel inversion on the 10D plane [J4a–c] — PROVED (exact).**
- K⁺ = −(κ²/2)(S − h trS/9) and tr K⁺ = κ² trS/18.
- **(tr K⁺)² − tr K⁺² = (κ⁴/4)((trS)²/9 − trS²).**

**Row 5 — normal–normal 4-form stress [J5] — PROVED (exact, generic Lorentzian D = 6; the identity is index-generic).**
- With G = G_t + dy∧H: **T_yy = H·H/24 − G_t·G_t/96**.

**Row 6 — forced plane constraint — PROVED as implication of {rows 3–5, P-HW, P-HWbc, P-G, P-Poinc}.**
- At every point of the plane:
  **H·H/24 = −r[h]/2 + (κ⁴/8)((trS)²/9 − trS²) + J·J/384.**
- Under P-Poinc, H lives on Riemannian Y₆, so H·H ≥ 0. A backreacted plane therefore must satisfy the necessary inequality
  **r[h] ≤ (κ⁴/4)((trS)²/9 − trS²) + J·J/192**, with equality iff H = 0 at that point.
- Smeared M5s lower the right-hand side: S = −τh⁽⁶⁾ gives (trS)²/9 − trS² = −2τ².

**Row 6b — Codazzi with sources — CONDITIONAL.**
- −(κ²/2)D_bS^b_a = T_ya(0⁺) = (1/12)H_PQR G_t,a^PQR = (1/24)H_PQR J_a^PQR.
- So the wall stress is conserved where H·J = 0.
- The index algebra was done by hand and is not machine-checked.

**Row 7 — the constraint has content and is satisfiable [J6a–c] — PROVED (exact examples).**
- Data: a Poincaré-invariant magnetic E₈ generator on the fibre, (f₁, f₂) = (1, 1), τ = 0, j = 0, κ² = 1. With these data the required H·H/24 is:
  - −3/4 at r = +1, so that data is ruled out;
  - +1/4 at r = −1, so that data is allowed.
- In general, required H·H/24 = −(3f₁⁴ − 2f₁²f₂² + 3f₂⁴ + 4(f₁² + f₂²)τ + 4τ²)κ⁴/16 + j²/16 − r/2, as printed in the log.
- The content is null-positive (J6c).

**Row 8 — (A) local construction — CONDITIONAL.**
- Take real-analytic plane data (h, F with S = S(F,h), smeared τ, J, H) obeying the Gauss and Codazzi constraints of rows 3, 6, 6b and the 4-form constraints on the plane.
- The Gaussian-normal evolution system of row 2, plus the first-order 4-form equations, then has a unique Z₂-symmetric solution in a slab |y| < δ. It is real-analytic up to the plane on each side, so its curvature (Ricci², Riem², Weyl², one-sided) is bounded on compact sub-slabs.
- The 2-jet is fixed algebraically (row 2, PROVED).
- Convergence rests on Cauchy–Kovalevskaya and on constraint propagation through the contracted Bianchi identity. These are standard theorems, cited, not rederived here. That is why the row is CONDITIONAL.
- **Dependency:** NL GA7a (cited, unadopted) argues that static finite-size self-dual instantons vanish where the warp weight varies. If that holds, smooth BPS instanton data are not available, the content becomes point-like, S is distributional in the plane, and Cauchy–Kovalevskaya does not apply. Smooth data would then have to come from non-BPS fields.
- No metric is invented. The row states which data produce one.

**Row 9 — (B) rule-out by a local algebraic or jet obstruction — REFUTED (exact, row 7).**
- Constraint-satisfying pointwise data exist, and the 2-jet is then determined without contradiction.
- So no rule-out holds at the jet level. The only local content is the necessary inequality of row 6.

**Row 10 — (C) global backreacted solution (plane matched to the flow) — OPEN.** Precise mathematical blockers:
1. The Cauchy problem off a timelike plane is ill-posed (Hadamard) for finite-regularity data. Cauchy–Kovalevskaya gives only local analytic slabs and no control of δ.
2. In the Poincaré-invariant static reduction, the bulk equations are Riemannian-signature on the 7D base (y, Y₆). The Israel condition ∂_yh = −κ²(S(F,h) − h trS/9) is a nonlinear Robin-type boundary condition, coupled to the E₈ YM equations on the plane. **What is missing is the theorem that this Einstein–4-form–Robin problem is elliptic** (Lopatinskii–Shapiro complementing condition in a chosen gauge), together with Fredholm/existence near a background.
3. That background would be the junction solution itself, which is UNSOLVED.
4. Localized M5s make S distributional in the plane, which is outside rows 8–9.

The absence of a file on disk is not used as a resolution anywhere.

## 4. Task 2 — covering-space 1/ε density and the 9760 premise
**Row 11 — value-free restatement [K1–K6, re-derived here] — PROVED as implication of {P-reg, P-Poinc, P-Israel, P-content}.**
- The δ² coefficients are:
  - R_MNR^MN: tr k² + (tr k)², a positive-definite form, zero iff [K] = 0 iff S = 0
  - Riem²: 4 tr k²
  - Weyl²: (32/9) tr k̃², with [K̃] = −κ²S̃
- The null-positivity lemma gives S̃ = 0 ⇒ S = 0 within P-content (exact LDL).
- With ∫φ_ε² = 1/(3ε) from f4ee61f2 (an elementary identity, restated not adopted: d/ds(tanh − tanh³/3) = sech⁴), the result is: **wherever S ≢ 0 on the plane, a non-Gauss–Bonnet square evaluated on the covering space has a non-integrable density, for Ricci², Riem² and Weyl² alike.**
- **No charge value is used.**

**Row 12 — "E₈ instantons cancel it" — REFUTED pointwise, as implication of {P-content}.**
- Suppose the non-gravitational wall charge density is nonzero at a point: tr F∧F ≠ 0 (so F ≠ 0) or M5 density ≠ 0 (so τ > 0).
- Then S(k,k) > 0 for some null k (K6), so S ≠ 0 there. Cancellation would need S = 0, so it is impossible at that point.

**Row 12b — the same question with the −½tr R² stress included — CONDITIONAL.** NL Y16, PP-1.

**Row 13 — replacing 9760 by "N ≠ 0" — PROVED as implication of {P-HW, P-HWbc / HW Bianchi normalisation (CONDITIONAL premise), P-N, A-D2, P-content}.**
- **Stokes.** The S⁴ fibre slices on the two sides of the plane are homologous, and odd G₄ takes ∫G₄ from +N to −N. So the wall carries total fibre charge 2N ≠ 0.
- **Gravitational part.** By adopted D2, ½tr R∧R is exact on Y₆, so its fibre integral is 0.
- **Conclusion.** Therefore n_inst + N_M5 = 2N ≠ 0. The non-gravitational density is nonzero somewhere, so S ≢ 0 by row 12, and row 11 applies.
- The signs of n_inst and N_M5 are not needed, because the stress is sign-blind (positive tension for branes and anti-branes, and |F|² for instantons and anti-instantons).

**Row 14 — is the charge 9760 itself adopted? — OPEN (record conflict, flagged for the Owner and PP; not resolved by MR2).**
- The t433u listing f3f6d65c says it is: §C.19 "definitional 1a face match and charge 9760 PROVED", from PP 1948 dee9410e… "N = 4880 and charge 9760: PROVED (carried from ERRATUM2)"; and §A.6 with supplement nit 1 lists D3 "9760 = n_inst + N_M5, PROVED as an implication of the HW normalisation (f825dfff)".
- PP confirm eebd7dd7 line 29 reads: "the charge 9760 [is] adopted only as already-PROVED facts".
- OW 945d81bb states: "N = 4880 and total charge 9760 remain unadopted."
- **Answer to the Owner's question.** If the t433u reading stands, adopted D3 already gives n_inst + N_M5 = 9760 ≠ 0, and row 13 follows from it directly. If the 1130 reading stands, no adopted statement supplies a nonzero value. The claim then rests on the stated premise P-N (N ≠ 0), or on the most general hypothesis "S ≢ 0 on the plane" (row 11).
- **In either case the specific value 9760 is not needed.**

## 5. Geometry ⇒ forced algebraic forms (new in this filing; per OW bff79185)
1. **Timelike Z₂ plane in an Einstein bulk** ⇒ a constraint/evolution split. Two constraints (Gauss, Codazzi) live on the plane, and ∂_y²h is algebraic (rows 2–3).
2. **Z₂ doubling + Israel** ⇒ the quadratic wall-stress form (trS)²/9 − trS² enters the plane's scalar constraint (row 4).
3. **Odd G₄ + HW boundary condition** ⇒ the boundary value G_t = J/2, so the wall charge density enters as J·J/384 (rows 5–6).
4. **R^{1,3} Poincaré invariance** ⇒ H is confined to Y₆, so H·H ≥ 0 and the scalar constraint becomes the **inequality r[h] ≤ (κ⁴/4)((trS)²/9 − trS²) + J·J/192** (row 6).
5. **Codazzi on the plane** ⇒ wall-stress conservation, with the source H·J (row 6b, CONDITIONAL).
6. **Static Poincaré reduction** ⇒ an elliptic-type bulk problem with a nonlinear Robin (Israel) boundary condition. The missing algebraic/analytic structure is its complementing condition (row 10).
7. **p₁(TY₆) = 0 (adopted D2)** ⇒ the gravitational charge integrates to zero, so any nonzero flux N forces non-gravitational wall charge, which forces S ≢ 0 (row 13).

## 6. Tally (rows 1–14 incl. 6b and 12b; junction carried; one bookkeeping row for integrity)
- **PROVED 9:** rows 1, 2, 3, 4, 5, 6 (as implication), 7, 11 (as implication), 13 (as implication).
- **CONDITIONAL 3:** rows 6b, 8, 12b.
- **OPEN 2:** rows 10, 14.
- **REFUTED 2:** row 9 (the jet-level rule-out) and row 12 (E₈ cancellation, pointwise, as implication).
- **Total: 9 / 3 / 2 / 2 = 16 + 1 bookkeeping.**
  - Integrity: all cited shas = sidecars, including OW 945d81bb, t433u f3f6d65c / 85b42876 / eebd7dd7, NL 79ad0c64 and PP 1948 dee9410e. Script and log = sidecars. Disclosures are in §1.
- Junction UNSOLVED.

## 7. Blockers
- **B-1 (row 10):** an ellipticity (Lopatinskii–Shapiro) and existence theorem for the Poincaré-reduced Einstein–4-form problem with the Israel Robin condition coupled to E₈ YM on the plane, and a background to perturb from (the junction, UNSOLVED).
- **B-2 (row 8):** smooth, analytic E₈ plane data. If NL GA7a's zero-size result is confirmed, smooth data must be non-BPS.
- **B-3 (row 6b):** a machine check of the Codazzi source identity.
- **B-4 (row 14):** an Owner/PP ruling on the 9760 adoption-record conflict.

Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 **MATCH** (checked before writing; re-checked after). Nothing adopted. No CERT. Nothing sent. Junction UNSOLVED.
