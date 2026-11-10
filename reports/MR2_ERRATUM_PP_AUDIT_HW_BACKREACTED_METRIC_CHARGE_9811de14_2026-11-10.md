# MR2 — Erratum to 9811de14 (backreacted near-plane metric; 9760-free δ²) per PP audit 81291f84 and addendum 7789f89a
2026-11-10, written 12:03:55 CST (America/Chicago), by MR2. This is an additive erratum only. Nothing was edited: not 9811de14, its script 2d8092a7 or its log 7634069f; not f4ee61f2, QC note 66f04088 or the L-GN erratum 7d8fb406; and no frozen script or log. Grades from other filings are cited only, never mixed in. **Nothing adopted.** No CERT. No Gemini. Nothing sent. Junction **UNSOLVED**. Wording: resonant algebra. No new script was run; every check cited below is already on disk.

## 0. Audits accepted (sha = sidecar, re-hashed from reports/)
- **PP audit** FINDINGS_PP_AUDIT_MR2_HW_BACKREACTED_METRIC_CHARGE_9811de14_2026-11-10_1157.md: 81291f843da6d01e4bbba362e370a05436a19b6dd046d4987ea83f3c34b737d8. Written 11:57:23 CST = mtime, mode 444. Its math rulings are accepted in full.
- **PP addendum** FINDINGS_PP_AUDIT_MR2_HW_BACKREACTED_METRIC_CHARGE_9811de14_ADDENDUM_TALLY_CUSTODY_2026-11-10_1201.md: 7789f89a788c011c42891d27e872060708bec71e02e703d590049ac2c80d05fa. Header 12:01:34 CST = mtime 12:01:34.000, mode 444. Accepted.
  - Disclosure, not edited: its sidecar mtime is 12:01:32.33, about 1.7 s **before** the file's mtime. The content matches the sidecar hash.
  - The addendum supersedes 1157 only on two bookkeeping items:
    - (i) The parent E₈ tally is the already-ruled **18/2/4/0** after the row-22 split (e2750e28 / 395bff64), not the stale 17/2/4/0 from eebd7dd7.
    - (ii) The tip after-hash missing from 1157 §10 is now recorded: 7cddb188…, mtime 2026-11-06 14:38:54 CST, mode 644, untouched.
- **Unchanged this write:** 9811de1490a88569860a3a2e3b04a5fe75387fc83eb1ba020221f72395150770, script 2d8092a779b8ed5cf4118d05f054ff9ccf227dbe10fc754a93d645ba10c75d5c, log 7634069fcc9700debd53ab57b7e10aca703cec460c630ca61034196933524dbb, f4ee61f2…, 66f04088…, 7d8fb406….

## 1. Ruled tally (stands; no self-upgrade)
- **PROVED 9:** 1; 2 [D=4 instance]; 3 [D=4 instance]; 4; 5 [incl. D=11, PP P4]; 6 [implication, L-GN named]; 7 [examples, A scoped]; 11 [implication, corrected premises]; 13 [implication, refined premises].
- **CONDITIONAL 4:** GN-G; 6b; 8; 12b.
- **OPEN 1:** 10.
- **REFUTED 2:** 9 [Gauss-scalar scope]; 12 [implication, corrected premises].
- **Total 16, plus 2 bookkeeping:** integrity, and the R14 record answered (scoped-compatible).
- **Grade moves (PP):**
  - (a) The general-D / D=11 rider of rows 2–3 goes PROVED → CONDITIONAL on L-GN, as GN-G.
  - (b) Row 14 changes from a math OPEN row to a record row, answered.
- **Other standing tallies, by citation only:**
  - Parent E₈: **18/2/4/0** (addendum correction).
  - f4ee61f2: as ruled in 976e5621, **12/3/2/1**, until PP confirms 7d8fb406.

## 2. F-1 — L-GN cited; rows 2–3 scoped; GN-G regrade requested
- **Rows 2–3 scope (disclosed).** The J1–J3 instance is D = 4 with:
  - **one background jet**: h0 and h1 are fixed rationals, and only the second y-jet h2 is symbolic;
  - **h independent of t**;
  - evaluation at **one point**, (u, v) = (1/3, 1/5), y = 0.
  
  It is PROVED for that instance only. The general-D / D=11 use is GN-G, CONDITIONAL on L-GN.
- **L-GN (restated).** In g = dy² + h_ab(y,x) with K_ab = ½∂_y h_ab, in any D and signature:
  - Gauss components R_abcd and Codazzi components R_yabc carry at most first y-derivatives of h.
  - ∂_y²h enters Riemann only through R_yayb = −∂_yK_ab + K_acK^c_b.
- **Where it is proved.** L-GN is stated and proved (index-generic Christoffel argument) in the additive erratum MR2_ERRATUM_PP_AUDIT_HW_PLANE_RICCI2_WEYL2_f4ee61f2_2026-11-10.md, sha 7d8fb4067a33c6f3530fd03610e15e981fe46e89c87660614b0d48b7c7ce6554, written 11:59:12 CST, §2.
  - Machine check: frozen script 1728d877918a96c8d91862483ade6b376ce6d91fdd531b1bb6881d138a3d0a50, log 20f66fe318da09fcbaf192a923291fe31e1dbe9ca03de0dac59ffcff32a09177, 21/21 PASS.
  - Coverage: fully general non-diagonal, x-dependent 2-jets in D = 4, 5 and 6. In D = 5, the general-[K] δ² coefficients are checked with κ_tv ≠ 0.
  - That erratum is **pending PP confirmation**. 3G (in 976e5621) and GN-G (here) are **not** treated as regraded.
- **L-GN is named in** rows 6, 6b, 8, 9 and 11 (see §§3–6).
- **Request to PP.** If you accept the L-GN proof already filed in 7d8fb406 §2, please regrade **GN-G from CONDITIONAL to PROVED as implication** of L-GN. If so, the proposed tally is 10/3/1/2 = 16 + 2. Until you confirm, the ruled **9/4/1/2** stands.

## 3. F-2 — rows 11 and 12: corrected premise sets and pointwise scope
- **Row 11 (PROVED as implication, as ruled).**
  - Premises: {P-reg, P-Poinc, P-Israel, P-content including **P-τ** (every charged plane object has τ > 0) and **"each M5 worldvolume ∋ t"**}.
  - **L-GN** is needed for non-diagonal or x-dependent walls. Otherwise the row is restricted to diagonal x-independent walls, the K1–K3 model.
  - No charge value is used.
- **Row 12 (REFUTED as implication, as ruled): "E₈ instantons cancel the density".**
  - Premises: the same set, plus P-Poinc for strict positivity of the δ² coefficient. The null-stress counterexample in 976e5621 P7.5 shows this is needed.
  - Pointwise scope: the refutation holds at points where the **non-gravitational** wall density is nonzero (F ≠ 0, or an M5 density with τ > 0).
  - Points carrying **gravitational density only** are out of scope (row 12b), as are **distributional, point-like** sources (outside P-reg).
  - Cancelling charge between instantons and anti-instantons, or between branes and anti-branes, does not cancel stress: S(k,k) ≥ 0 term by term.

## 4. F-3 — row 13: refined premise set
Row 13 is PROVED as implication of:
- **P-HW**, including that the Z₂ fixes the plane and each S⁴ fibre pointwise.
- **No off-plane sources** (dG = 0 off the plane).
- **P-HWbc**: HW integer normalisation of the Bianchi source. CONDITIONAL premise.
- **P-N**: N ≠ 0. **Unadopted premise.**
- **P-Y₆**: the backreacted plane's internal manifold is the Y₆ of the 1a face (twisted S⁴ bundle over Σ). **Unadopted premise.** Adopted D2 (cc21b272, p₁(TY₆) = 0, under t433u as graded) applies only to that Y₆.
- P-content and P-τ.

D2 supplies the **integrated** n_R = 0, i.e. ⟨p₁(TM|_plane), [S⁴]⟩ = 0. The **pointwise** gravitational density is not excluded and stays in 12b. N = 4880, 9760, N ≠ 0, P-Y₆ and P-HWbc are all not adopted.

## 5. F-4 — row 14 / B-4: withdrawn sentence and scoped reading
- **Withdrawn (incorrect as stated):** "If the t433u reading stands, adopted D3 already gives n_inst + N_M5 = 9760 ≠ 0, and row 13 follows from it directly."
- **Scoped reading (PP 81291f84 §6, accepted):** the records are compatible once scoped.
  - t433u adopted D3 only as an implication identity on the 1a/MN2 face in HW normalisation, together with the in-vacuum N = 4880 (cc21b272 line 46; PP 1948; aeb9ab13).
  - OW 1130's "unadopted" refers to 9760 as a premise, i.e. a physical wall charge for the backreacted face.
  - 1a is not adopted as the physical wall, so adopted D3 does not attach to the backreacted face.
- **Answer to the 11:30 question:**
  - No adopted value attaches to the backreacted face.
  - The integer 9760 is not needed.
  - It is replaced by the weaker unadopted premise N ≠ 0, plus adopted D2 (scoped by the unadopted P-Y₆) and P-HWbc. Together these give S ≢ 0.
  - It is **not** replaced by an adopted value.
- MR2 invents no new Owner ruling.

## 6. F-5, F-6, F-7
- **F-5 (row 7).** Example A treated j as independent of f₁f₂. Under P-HWbc, J ⊃ c·tr F∧F ∝ f₁f₂.
  - A is replaced by **A′**: f₂ = 0 (so tr F∧F = 0 and j = 0 consistently), f₁ = 1, τ = 0, κ² = 1, r = +1.
  - From the logged polynomial (log 7634069f, J6 line), the required H·H/24 = −(3·1 + 8·1)/16 = **−11/16 < 0**. This is exact arithmetic and agrees with PP P7.5.
  - **B is robust:** with j = λf₁f₂, the required value is 1/4 + λ²/16 > 0 (PP P7.3). Satisfiability (B) is what row 9 uses.
- **F-6 (row 9), retitled:** "the plane's Gauss **scalar** constraint does not rule out a backreacted plane pointwise" — REFUTED in that scope only (counterexample B).
  - Simultaneous pointwise satisfiability of the full constraint set is **not exhibited**: Codazzi (6b), the plane 4-form constraints and the E₈ YM equations.
  - "The 2-jet is then determined" in 11D inherits GN-G (L-GN named).
  - Row 9 has no bearing on a global solution (row 10, OPEN).
- **F-7 (§5 item 6).** "Elliptic-type bulk problem" is replaced by: "a Riemannian-signature bulk problem whose ellipticity (Lopatinskii–Shapiro complementing condition, in a chosen gauge, with the nonlinear Robin/Israel condition coupled to E₈ YM) is exactly the missing B-1".

## 7. Rows 5, 6, 6b, 8 (citations and named premises)
- **Row 5 (PROVED)** is pinned at **D = 11** by PP P4.0–P4.2 (330 symbolic components): T_yy = H·H/24 − G_t·G_t/96. MR2's own check was D = 6.
- **Row 6 (PROVED as implication)** of {rows 3–5, P-HW, P-HWbc, P-G, P-Poinc, **L-GN**}. The 10D Gauss constraint is general-D, so it falls under GN-G.
- **Row 6b (CONDITIONAL, not upgraded).** The index algebra is machine-checked by PP P6.1 (D = 5 instance) and P6.2 (D = 11): −(κ²/2)D_bS^b_a = (1/24)H_PQR J_a^PQR. The row stays CONDITIONAL on GN-G / **L-GN** and P-HWbc, plus N1.
- **Row 8 (CONDITIONAL)** rests on:
  - Cauchy–Kovalevskaya and constraint propagation (cited);
  - **L-GN** (GN-G) for the 11D 2-jet algebra;
  - real-analytic plane data (B-2);
  - the 4-form gauge, which **the parent left unspecified**. Naming it is still owed.
  
  A uniform slab width δ over the plane needs **compact Y₆ plus Poincaré homogeneity** (N8). No metric is invented.

## 8. Nits folded
- **N1.** κ² convention: P-G has unit bulk coupling while Israel carries κ². The row-6 formula is correct if κ² = 1 in P-G units; otherwise the H·H and J·J terms carry κ². No sign or grade effect.
- **N2.** The J3 Codazzi sign is pinned to **+**: G_ya = D_bK^b_a − D_aK (log J3; PP P1.5).
- **N3.** J4a does not need the "diagonalisable" label. PP P3.1–P3.3 proved it for a generic 10×10 [K].
- **N4.** ∫φ_ε² = 1/(3ε) was not checked in the 9811de14 script. Cited checks: PP P9.1–P9.3, and MR2 log 20f66fe3, C2a–C2d (∫sech² = 2, ∫sech⁴ = 4/3, the Cauchy–Schwarz cases).
- **N5.** Filing mode 644 (convention). Frozen scripts and logs are 444. Nothing is chmod-ed here.
- **N6.** In the parent, the freeze (sidecar 11:37:27.74) and RUN_START (11:37:27) fall in the same second. This was disclosed there. PP's post-freeze re-run is byte-identical apart from the wall-clock lines. Recorded; no grade effect.
- **N7.** Row 5's D = 11 pin is PP P4 (see §7).
- **N8.** See row 8 in §7 (compact Y₆; 4-form gauge unspecified, still owed).
- **N9.** For B-3, cite PP P6.1/P6.2. Row 6b remains CONDITIONAL.

## 9. Blockers (unchanged in substance)
- **B-1:** Lopatinskii–Shapiro ellipticity and existence for the Poincaré-reduced Einstein–4-form–Robin problem, and a background to perturb from (the junction, UNSOLVED).
- **B-2:** smooth, analytic E₈ plane data. This may need to be non-BPS (NL GA7a, cited only).
- **B-3:** discharged as index algebra by PP P6.1/P6.2. Row 6b stays CONDITIONAL.
- **B-4:** answered (record row, scoped-compatible; §5).

## 10. Folded list
F-1, F-2, F-3, F-4 (sentence withdrawn), F-5 (A′ = −11/16), F-6, F-7; N1–N9; the addendum's parent-E₈ 18/2/4/0 correction and tip after-hash; the addendum's sidecar-first 1.7 s gap (disclosed).

Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 **MATCH** (checked before writing; re-checked after). Nothing adopted. No CERT. Nothing sent. Junction UNSOLVED.
