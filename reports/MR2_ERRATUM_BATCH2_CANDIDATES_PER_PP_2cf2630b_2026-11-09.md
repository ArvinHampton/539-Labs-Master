# MR2 — Erratum to batch-2 candidate resolutions, per PP audit 2cf2630b
Date: 2026-11-09, ~20:00–20:15 CST (America/Chicago). Agent: Math Research 2 (executor). Additive; text only; no new computation.
Amends: MR2_CANDIDATE_RESOLUTIONS_BATCH2_DPa_DPb_LAYER2_RC_SEC10_PER_OW_b0b9ae7f_2026-11-09.md (f688c7e38ebf8ab5df38733569a19db8424f1c760818cddbfe5578268081e2ce). That file and the frozen .py (516438eb…) / .log (9f52edb0…) are unchanged.
Audit: FINDINGS_PP_AUDIT_MR2_CANDIDATES_BATCH2_DPa_DPb_LAYER2_RC_SEC10_2026-11-09_1952.md — 2cf2630b6da06bb0eaf2277f65fd052b9869382d4ab2b1a9bbbe7dcfcbe90908 (file = sidecar, MATCH).
Owner records (file = sidecar, Owner's words present):
- OW ed8effba (t4417, ~19:34) OWNER_WRITE_MAINCHAT_t4417_CLARIFY_1631_RELEASED_LAYER2_SEFF_MAPPING_PURGE_2026-11-09_1934.md — ed8effba8799c66cf2bfeeddd1df52d2bf5298fe5aec89fcc82ca8270dea2720. Verbatim: "Yes, my 4:31 instruction released the Layer2 lock, the S_eff lock and the mapping purge."
- OW 81b74a31 naming, OWNER_WRITE_VOICE_81b74a31_RENAME_RTA_TO_RESONANT_ALGEBRA_DROP_RESIDUAL_RESONANT_SPLIT_2026-11-09_1937.md — f1d167d1949a6df231eb908bf3574f0e289e91ce297b4376417ac910f2a037a4. Applied here: RTA is read as **resonant algebra**, with no residual/resonant split. Nomenclature only.
Labels PROVED / COND / OPEN / REF. Nothing adopted; the Owner chooses. PP fix 8 (optional closed forms) skipped. Tip 7cddb188 untouched; no CERT; no Gemini; nothing sent outside; no agent messaged.

## E1 (PP fix 1, A5) — lock scope: ACCEPTED
- §0.1 OPEN → **CLOSED by OW ed8effba**. Released at 4:31 PM: the Layer2 "LOCKED" status (a71f388e), the S_eff lock (96f8d42e) and the mapping purge (a71f388e). All three are neutral and unresolved, and none is adopted.
- Every "if still in force" / "if the purge applies" hedge in §§1.0, 1.1, 1.2, 2.1 and 3.0 is withdrawn.
  - The 10-26 a-I reading (D1-norm ↔ Kerr area) and L2-3 are no longer excluded by a purge. They stay **OPEN** only because no well-typed target or map is on disk (PP-L2-2 typing).
  - The value equality N_flux = 4880 = M5 N, read as a structure map, stays OPEN: it is no longer barred, but it is also not derived.
- **DP-b restated:** DP-b is a *candidate definition of the neutral symbol S_eff*, not "a carrier for the locked S_eff". The DPb-1 precondition ("after the Owner answers §0.1 … meaningless if S_eff is released") is withdrawn as wrong.
  - A field-action reading of S_eff (bd3730eb b-I) is no longer barred, but no such action is on disk (OPEN).
  - b-7 ("no face source") is a property of DP-b's carrier, not of S_eff in general.
- bd3730eb's lock-based *reasons for picking* a-II and b-II are superseded. Its mathematics is unaffected.
- Nomenclature (PP fix 9): DP-b's factors are the **static-cell factor O(p) = {f + kj : 0 ≤ j < R(p)}** and the **counter factor {1, …, W + b}**, not "Residual₅₃₉ × Resonant₅₃₉". The math is unchanged.

## E2 (PP fix 2, A1) — DPa-1 rationale: ACCEPTED
- **REF:** my claim "the normalisation is not a free choice / DPa-1 adds no arbitrary datum beyond DPa-2". Checked counterexample: 2λ = (0,2,2) kills im D¹ = ⟨t_ω, t_ωf − s_αδ⟩ (2·0 = 0; 2 − 2 = 0) and is nonzero on [s_αδ], so it meets every ℚ-linear constraint. Over ℚ nothing forces c = 1.
- **PROVED, replacing it:** D̂₁ = λ is canonical *relative to* the integral lattice F²_ℤ, the orientation convention α(a,b) = sgn(a − b), and (for characterisation (ii)) a chosen generator of H³(G³).
  - Every allowed functional is cλ with c ∈ ℚˣ.
  - λ(F²_ℤ) = ℤ, since gcd(0,1,1) = 1, which forces c = ±1.
  - Positivity on s_αδ then gives c = 1.
  - The norm ‖·‖_{D1} does not depend on the sign.
- DPa-1 therefore adds one datum, the integral structure. a-1..a-4 stay COND (DP-a).

## E3 (PP fix 3, A2) — control self-flag: ACCEPTED; my self-flag was REF
Hand check of the (D) Kehagias–Russo product AdS₅(L) × H²(ρ) × S⁴(r), with G = q·vol(S⁴), R_MN = (1/12)(G·G)_MN − (1/144)g_MN G²:
- On S⁴: (G·G)_ab = 6q² g_ab and G² = 24q², so R_ab = (1/2 − 1/6)q² g_ab = (q²/3) g_ab. The external blocks give R_ab = −(q²/6) g_ab.
- S⁴: 3/r² = q²/3. With r = ½, q² = 36.
- AdS₅: −4/L² = −6, so **L² = F = 2/3**. H²: −1/ρ² = −6, so ρ² = 1/6. These agree with KR's L² = 2R₀²/3, ρ² = R₀²/6, r² = R₀²/4 at R₀ = 1.
- **R(D) = 5(−6) + 2(−6) + 4(12) = −30 − 12 + 48 = 6 = G²/144 = 24·36/144. PROVED (exact, by hand).**

Consequences:
- The frozen script's banner "expect R=6" is the correct value for (D).
- The error is the coded F = 4/9 (L = 2/3) under the label "(D) product". For that coded metric, R = −45 − 12 + 48 = −9 exactly, which the run reproduced. So the routine is still validated.
- My batch-2 self-flag ("copied by mistake; [CMP]'s R = 6 is a different diagnostic, not the Ricci scalar") is **REF** and withdrawn.
- Source of the 4/9: MR2's own MR2_TWISTED_VACUA_ADOPTION_BLOCKERS_RIEMANN_SYSTOLE_FULL_EOM_2026-11-09.md (9ab8f0a6…) line 27, "e^{2f} = 4/9 so that L_AdS5 = 2/3". That describes a non-(D) control. It is flagged here only; the file is not edited.
- No MN2 number changes (PP reran the frozen .py and got a byte-identical log).

## E4 (PP fix 4 + parent note) — row 4b split: ACCEPTED
- **4b-i: Φ = 144R/ℓ² is non-constant on MN2. PROVED (computer-assisted).**
  - Basis: PP's disjoint interval enclosures R(π/4, π/4) ∈ [6.02894…], R(π/2 − 1/100, 1/100) ∈ [11.99653…] and R(1/100, π/4) ∈ [5.29146…].
  - PP's stated caveat: evalf is trusted to 45 digits on the entries.
  - It stays COND on MN2 being an exact solution (OW 19a88b19) and on K1, R = G²/144. I re-derived the trace: R = G²/12 − 11G²/144 = G²/144.
  - My original "PROVED (grid)" was float-only and should have been COND.
- **4b-ii: range Φ ∈ [0.308665516, 0.700009526] ℓ_p⁻², ratio 2.26786. COND** (float grid; global extremes not certified).

## E5 (PP fix 5) — EH lock row 4d: ACCEPTED, strengthened
- **REF, k-independent:** Φ is non-constant (4b-i, PROVED), so **no constant k of any value** satisfies k² = Φ(p)/1728 at every p. The choice k = 1/L₅ plays no role.
- **Separately, Φ-3:** k²/(Φ_max/1728) = ℓ²/L₅² = e^{−2f₀} = 2^{4/5} = 1.7411 ≠ 1. This is COND on R_max = 12 and on k = 1/L₅. L₅ is point-dependent in the warped frame (Δ^{1/6}).
- PP's pointwise-warped variant k(p) = 1/(ℓe^{f₀}Δ^{1/6}) gives ratios in [2.0, 3.6] at the six points, never 1. COND (float), taken from PP and not re-run.
- Under Φ-2 (an averaged Φ) the question stays OPEN.

## E6 (PP fix 6) — Rc-REF: ACCEPTED
- **REF at N = 4880** rests on the direct ratios: L₅/R_c = 23.569, (L₅/2)/R_c = 11.784, ρ/R_c = 16.666, (ℓ/2)/R_c = 15.549, and systole/R_c ≥ 47.5. All are ≥ 11.78, and the warp factor Δ^{1/6} ∈ [0.933, 1.047] cannot close that gap.
- The N^{1/3} argument excludes only an identity that would hold for all N. It is not what refutes the claim at fixed N.
- Crossing values, checked: N = 4880/ratio³ ≈ 0.37 (L₅), 1.05 (ρ), 1.30 (ℓ/2), 2.98 (L₅/2). All are far outside N ≫ 1.

## E7 (PP fix 7, A3) — G₂ item: ACCEPTED
- **M₆ is spin: PROVED.** I checked PP's argument:
  - TM₆ ⊕ ℝ ≅ π*TΣ ⊕ π*(L ⊕ ℝ³).
  - The MN2 twist line bundle L has curvature dx∧dy/y² (a₁ = 1), so deg L = Area(Σ, K = −1)/2π = 4π(g−1)/2π = 2. That is even, so w₂(L) = 0.
  - w₁ = 0, and w₂(TΣ) ≡ χ(Σ) = −2 ≡ 0 (mod 2).
  - Whitney gives w₂(TM₆) = 0. M₇ = ℝ × M₆ is then orientable and spin.
- **A G₂-structure on M₇ exists: COND**, resting on the cited criterion "a 7-manifold admits a G₂-structure iff it is orientable and spin". Sources: Bryant, math/0305124, the passage recorded in MR2 fd191d28 [L7] (L461–478); also Gray (1969) and Lawson–Michelsohn, *Spin Geometry* §IV.10. I have not re-proved it.
- **Torsion-free: OPEN.**
- **Recommendation update:** G2-1 (no G₂-structure) is still recommended, but now as a *choice*: nothing in the MN2 work uses the 1+7+27 split. It is not forced, since a G₂-structure exists (COND). G2-2 now reads "existence COND on the cited criterion only".

## E8 — DP-b arithmetic (parent note, PP A6): ACCEPTED
- **Ω₁ = 8: PROVED (exact).** 4880 − 21 = 4859 = 9·539 + 8, and 8 ≢ 0 (mod 539).
- Also exact: N − 9·539 = 29, and Ω over N = 4880..4888 is [8, 0, 1, …, 7].
- As statements about S_eff these stay COND on adopting DP-b.

## Corrected rollup (batch-2 rows; PP's split and regrades)
| # | Item | Label |
|---|---|---|
| 0.1 | lock-release scope | CLOSED (OW ed8effba) |
| 1a | DP-a/DP-b take no vacuum input | PROVED |
| 1b | N_flux = M5 N as a structure map | OPEN |
| 1c | DPa-1 ⇒ a-1..a-4 | COND |
| 1d | DPb-1 ⇒ DP-b carrier gives no face source | COND |
| 2a | Layer2 = the unbuilt D₁ component | PROVED |
| 2b | L2-3 transfer | OPEN |
| 3a | κ, ratios | PROVED |
| 3b | Rc-REF at N = 4880 | REF |
| 3c | Rc-1 | PROVED / COND |
| 3d | Rc-2 | PROVED / COND |
| 4a | §10 = fd191d28 §10 | COND |
| 4b-i | Φ non-constant | PROVED (interval, PP) |
| 4b-ii | Φ range | COND |
| 4c | Φ_max = 2Φ_(D) | PROVED (arith.); R_max = 12 COND |
| 4d | EH lock, any constant k | REF |
| 4e | Φ-2/W-2 values | OPEN |
| 4f | torsion-free G₂ | OPEN |
| 4g | 61 = punctures/cusps | REF |
| 4h | §10 item 5 | CLOSED (OW 19a88b19) |

**Tally (first label per row):** PROVED 7 · COND 4 · OPEN 4 · REF 3 (+2 CLOSED), 18 labelled rows. This matches PP's count.

Erratum rows: E2 DPa-1 forcing claim REF; E2 relative canonicity PROVED; E3 R(D) = 6 PROVED; E3 my earlier self-flag REF; E7 M₆ spin PROVED; E7 G₂-structure existence COND; E8 Ω₁ = 8 PROVED. **Added: PROVED 4 · COND 1 · REF 2.**

## Recommendations after this erratum (none adopted; the Owner chooses)
- DP-a: **DPa-1** stays, with a new rationale: canonical relative to the integral lattice, the sign and the generator. It is not forced over ℚ.
- DP-b: **DPb-1** (Ω₁ = 8), now with no precondition, as a candidate definition of the neutral S_eff.
- Layer2: **L2-1**, or L2-2 if DPa-1 is adopted. Unchanged.
- R_c: **Rc-3** by default, then Rc-2 over Rc-1. Unchanged.
- §10: **Φ-1, W-1, P-3** unchanged. **G2-1** is kept as a choice, not a forced result.

## Disagreements with PP
None. Every fix was checked and accepted. E5's pointwise-warped variant and PP's interval enclosures are accepted on PP's run; I did not re-run them.
