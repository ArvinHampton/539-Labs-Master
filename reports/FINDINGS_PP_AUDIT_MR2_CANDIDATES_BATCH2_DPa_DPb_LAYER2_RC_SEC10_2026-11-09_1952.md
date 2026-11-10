# FINDINGS — PP Soft SF audit of MR2 candidate resolutions, batch 2 (DP-a / DP-b, Layer2, R_c, §10), per OW b0b9ae7f
Date: 2026-11-09, ~19:52 CST (America/Chicago). Auditor: Professor Proof (PP), executor run. Owner: Arvin.
Authority: OW b0b9ae7f (t4407, "Pursue all for resolutions": lanes propose and recommend, PP audits and grades, **nothing is adopted**). Lock-scope answer: OW ed8effba (t4417). Naming: OW 81b74a31 ("resonant algebra"; no residual/resonant split; nomenclature only, no grade changes).
Labels: PROVED / CONDITIONAL (COND) / OPEN / REFUTED (REF) / PENDING. Refutation only by proof or counterexample. Float-only numerics = COND. A citation alone never makes a result PROVED (OW 3f160803 as amended by 36683379).

## 0. Custody (sha256 re-hashed live; every file = its .sha256 sidecar)
| File | sha256 | sidecar |
|---|---|---|
| MR2_CANDIDATE_RESOLUTIONS_BATCH2_DPa_DPb_LAYER2_RC_SEC10_PER_OW_b0b9ae7f_2026-11-09.md | f688c7e38ebf8ab5df38733569a19db8424f1c760818cddbfe5578268081e2ce | MATCH |
| MR2_BATCH2_SEC10_PHI_ON_MN2_RICCI_SCALAR_CHECK_2026-11-09.py (frozen) | 516438eb837def5e9e0addf57c5ea533a59105aea4d6b6b9802f25d58e6c7197 | MATCH |
| MR2_BATCH2_SEC10_PHI_ON_MN2_RICCI_SCALAR_CHECK_2026-11-09.log | 9f52edb0ce2fd0489378796d9eca98d1b929fcf32a7d292ab9a296672d52eebe | MATCH |
| OWNER_WRITE_VOICE_1f7b6901_WITHDRAW_t4327_ALL_ITEMS_NEUTRAL_UNRESOLVED_2026-11-09_1631.md (OW 5f59e33e) | 5f59e33e5b49ed7f7a89b06f0ceff0b7bc7dc034c83d5c65a72bea176aa3a234 | MATCH |
| OWNER_WRITE_MAINCHAT_t4417_CLARIFY_1631_RELEASED_LAYER2_SEFF_MAPPING_PURGE_2026-11-09_1934.md (OW ed8effba) | ed8effba8799c66cf2bfeeddd1df52d2bf5298fe5aec89fcc82ca8270dea2720 | MATCH |
| FINDINGS_PP_DERIVED_DEFS_D1_LAYER2_SEFF_T3_2026-11-09_1309.md (PP bd3730eb) | bd3730eb57a929a40eaed6547daac212b3f7baf468ce8b08b0bbe902d75a565b | MATCH |
| OWNER_WRITE_VOICE_81b74a31_RENAME_RTA_TO_RESONANT_ALGEBRA_DROP_RESIDUAL_RESONANT_SPLIT_2026-11-09_1937.md | f1d167d1949a6df231eb908bf3574f0e289e91ce297b4376417ac910f2a037a4 | MATCH |
| MR2_11D_ADS5_S4_SIGMA2_TO_PHI_V35_MAP_PROPOSAL_2026-11-09.md ([MAP], §10 source) | fd191d28fb1aa40f974bb2f6df5ff3150984f88803907d534668d7b771ff733f | MATCH |
| PAPER_RESIDUAL_TERNARY_ALGEBRA_BRIDGE_C_2026-11-03.md ([P]; read as resonant algebra paper) | 23931ee8f0336d8e187c3913c0b13c9fb55d690e41f91cce01c142d0cd3e4d7b | (re-hashed = MR2's pin) |
Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188…dfc91, untouched (re-hashed). No CERT. No Gemini. Nothing sent outside. No existing file edited.

PP scratch (box, not in reports/): /workspace/pp_audit_b2/ — rerun of a copy of the frozen .py (rerun.log), independent Ricci code (indep.py, ctrl.log, mn2.log), 17×17 scan (scan.py, scan.log), interval enclosures (ivcheck.py, iv.log), integer/arithmetic checks (arith.py).

## 1. Answer to MR2's open question (§0.1): what OW 5f59e33e released — from disk
**5f59e33e verbatim (the only release clause):** "Layer2: UNRESOLVED, no stance. The "Layer2 LOCKED" status (attach a71f388e) is no longer treated as a lock; whether Layer2 holds is an open question." Its preamble also quotes the Owner: "do not lock anything at all ... Treat every item as fully unresolved and neutral ... Just clean unresolved state across the board." The bullet list names neither the S_eff lock (96f8d42e §2) nor the §4 / attach §3 mapping purge. So, read alone, 5f59e33e was **ambiguous** on S_eff and the purge; MR2's "OPEN (Owner)" at 19:33 was a fair reading.
**Resolved by OW ed8effba (t4417, ~19:34 CST), Owner verbatim:** "Yes, my 4:31 instruction released the Layer2 lock, the S_eff lock and the mapping purge." The record lists: Layer2 "LOCKED" status (a71f388e): RELEASED; S_eff lock (96f8d42e): RELEASED; mapping purge (a71f388e): RELEASED; "All three items are now neutral and unresolved. Nothing is adopted." It states that 5f59e33e is left unchanged.
**Answer:** all three (Layer2 LOCKED, the S_eff lock 96f8d42e, and the Lock 96f8d42e §4 / attach mapping purge) were released at 4:31 PM, per ed8effba. Released means neutral and unresolved. It does not mean adopted, and no purged physical map is restored or adopted by it.
**PP bd3730eb (13:09):** it was written before 5f59e33e, and it treats all three as in force: "D₁ / S_eff LOCK (respected, not altered)"; "Pick: b-II. Reasons: the symbol S_eff is Owner-locked (96f8d42e §2)"; "No physical, Kerr, four-forces, SU(3), Kronecker or continuum map is restored (Lock §4)". That assumption is **SUPERSEDED** by 5f59e33e as clarified by ed8effba. bd3730eb's mathematics is unaffected: the a-/b- results are graded on their definitions, not on lock status. Its lock-based *reasons for picking* (a-II over a-I, b-II over b-I) no longer hold as reasons. The options are open again; nothing is decided.
Per the parent's instruction, DP-b and Layer2 are graded below on their math alone, with no lock blocking them.

## 2. Reruns and independent checks
- **Rerun:** a copy of the frozen .py (sha 516438eb… verified before running) gives a log **byte-identical** to 9f52edb0….
- **Independent Ricci code (PP indep.py):** hand-coded metric in mpmath, derivatives by mpmath numerical differentiation (no sympy differentiation, 60 digits), different (r, y) base points. MN2: R(1/3, 2/7) = 5.551455102913087315404, R(1.5, 0.2) = 11.28019223538077716828, R(0.7, 1.1) = 5.514660718209008996342. These agree with MR2 to ≥ 21 digits. Pole limits: μ₁ = 1 pole, 12 − 1.733·10⁻⁵ (ε = 10⁻³) and 12 − 1.733·10⁻⁷ (ε = 10⁻⁴), i.e. 12 − 17.33ε². μ₀ = 1 pole, 5.2913381619 (10⁻³) and 5.2913368531 (10⁻⁴).
- **Control, exact:** the coded product (X = 1, a = 0, F = 4/9, Gs = 1/6) gives −20/(4/9) − 2/(1/6) + 12/(1/4) = −45 − 12 + 48 = **−9**. Both codes reproduce it. **However, that product is not the (D) Kehagias–Russo product.** [MAP] S1 gives L² = 2R₀²/3, ρ² = R₀²/6, r² = R₀²/4. With S⁴ radius ½ (R₀ = 1), (D) has F = L² = **2/3**, not 4/9, and its exact Ricci scalar is −30 − 12 + 48 = **6**. PP's code with F = 2/3 returns R = 6.0. So the banner "expect R=6" is the correct value for (D). The error is the coded F = 4/9 together with the "(D) product" label. MR2's self-flag explanation ("[CMP]'s 'R = 6' in its table is a different diagnostic, not the Ricci scalar") is wrong: [CMP] L30 states "validated on the (D) product, where R = 6". The control still validates the routine, because −9 is the exact value for what was coded. No MN2 number changes.
- **Interval enclosures (PP ivcheck.py):** exact sympy derivatives evaluated at exact points with evalf to 60 digits, each entry padded by ±10⁻⁴⁵, then the Christoffel/Ricci assembly done entirely in mpmath interval arithmetic. MN2:
  R(π/4, π/4) ∈ [6.0289437934363809182929178, +1.2·10⁻⁴⁰ width];
  R(π/2 − 1/100, 1/100) ∈ [11.996534652866469709203581, width 3·10⁻³⁵];
  R(1/100, π/4) ∈ [5.2914603043466870965228779, width 1·10⁻³³].
  The enclosures are pairwise disjoint, so **R (hence Φ = 144R/ℓ²) is non-constant on MN2: PROVED (computer-assisted, interval; the residual caveat is that sympy evalf is trusted to 45 digits on the entries).**
- **Scan:** PP ran a 17×17 grid on [10⁻⁴, π/2 − 10⁻⁴]² and checked the α → π − α reflection at a point (equal to 20 digits). Min 5.291336839894 at the μ₀ = 1 pole, max → 12 at the μ₁ = 1 pole, no interior extremum beyond these. This matches MR2's 9×9 grid. Float numerics: COND.
- **Closed forms (PP observation, COND, numerical identification):** R_max = 12 and **R_min = (10/3)·2^{2/3} = 5.291336839893998** (grid min 5.291336839894; agreement to 12 digits). Hence Φ_max/Φ_min = 3.6·2^{−2/3} = 2.2678578898, which reproduces MR2's 2.26785788981. Not proved symbolically.

## 3. Per-item grade table (MR2 rollup rows; PP grade; note)
| # | Item | MR2 | PP | PP note |
|---|---|---|---|---|
| 0.1 | Scope of the 5f59e33e release | OPEN (Owner) | **CLOSED (Owner record ed8effba)** | All three released; see §1. Not a math grade. |
| 1a | DP-a, DP-b take no vacuum input | PROVED | PROVED | By inspection of the definitions in bd3730eb a.2 / b.2: integer tuples and a ℚ-linear functional only. |
| 1b | N_flux = 4880 = M5 N: value equality; as a structure map | OPEN | OPEN | ⌊243e³⌋ = 4880 (243e³ = 4880.78547…, margin 0.21 from both integers): PROVED. The structure map is OPEN. The purge no longer bars it (ed8effba), but nothing on disk derives it. |
| 1c | DPa-1 consequences a-1..a-4 | COND (DP-a) | COND (DP-a) | Re-checked: im D¹ = span(t_ω, t_ωf − s_αδ); λ = (0,1,1) kills it and λ(s_αδ) = 1. See A1 for the "forcing" claim. |
| 1d | DPb-1 ⇒ S_eff gives no face source (b-7) | COND (DP-b) | COND (DP-b) | Correct under DP-b. After the release this is a property of DP-b's carrier, not of S_eff in general (see A5). Junction stays **UNSOLVED**. |
| 2a | Layer2 on disk = the unbuilt component implementing D₁ | PROVED (record text) | PROVED (record text) | [P] L237 verified verbatim: "Layer 2, the component that would implement D₁, has not yet been constructed from this definition. No result here depends on it." |
| 2b | L2-3 transfer to a Kerr/MN2 quantity | OPEN | OPEN | No longer excluded by the purge. It still has no well-typed target (PP-L2-2 typing). No map H²(F) ≅ ℚ → MN2 quantity is on disk. |
| 3a | κ, ℓ_p/R_c, MN2 length ratios | PROVED (arith.) | PROVED (arith.; inputs [CMP] K2) | Recomputed: Λ₀ = 0.783577217617, κ = 1.597622240065, ℓ = 49.68438219, L₅ = 37.65372059, ρ = 26.62520117, ℓ/2 = 24.8421911. Ratios 23.5686 / 11.7843 / 16.6655 / 15.5495; systole band/R_c ∈ [47.539, 53.361]. 5a6e7177's ℓ_P is the 11D Planck length (its O3 uses (2πℓ_P)³N), so the units are consistent. |
| 3b | Rc-REF: R_c = an MN2 length | REF | **REF** (genuine counterexample at N = 4880) | At the adopted N, every ratio is ≥ 11.78. The warp factor Δ^{1/6} ∈ [0.933, 1.047] cannot close that gap. The N^{1/3} argument is right but proves less than it looks: it excludes only an *N-independent* identity. A fixed-N equality would need N ≈ 0.37 (L₅), 1.05 (ρ), 1.30 (ℓ/2) or 2.98 (L₅/2), all far outside sugra validity (N ≫ 1). The REF at N = 4880 rests on the direct ratios, not on the scaling. |
| 3c | Rc-1: thickness premise met by definition; control | PROVED (arith.) / COND | PROVED (arith.) / COND | (kℓ_p)(ℓ_p/ε)^m = 1.662e-2, 1.041e-2, 1.597e-3 (m = 1, 2, 6) reproduced. k = 1/L₅ is an identification (OPEN). In the warped frame L₅ is point-dependent. |
| 3d | Rc-2: cutoff below 1/ℓ_p; first Σ-KK level 8.5× below | PROVED / COND | PROVED / COND | κ > 1 ⇒ 1/R_c < 1/ℓ_p. m₁ = 0.073588 ℓ_p⁻¹ and (1/R_c)/m₁ = 8.5058 reproduced. λ₁ = 3.8388872589 is independently confirmed by PP's Klein-model P2 FEM (see the separate ed0e5bd6 audit): COND (float, unwarped). |
| 4a | §10 = fd191d28 §10 | COND (reading) | COND (reading) | "t4394" occurs on disk only inside OW b0b9ae7f and MR2's file; the source list t4394s18232 is not on disk. |
| 4b-i | Φ = 144R non-constant on MN2 | PROVED (grid) | **PROVED (computer-assisted, interval enclosures §2)** | MR2's grid was float-only, so as delivered it was COND. PP's interval enclosures upgrade it. COND on MN2 being an exact solution (OW 19a88b19) and on K1 (R = G²/144; PP re-derived the trace: R = (1/12)(G² − (11/12)G²) = G²/144). |
| 4b-ii | Range Φ ∈ [0.308665516, 0.700009526] ℓ_p⁻², ratio 2.26786 | PROVED (grid); global COND | **COND** | Float values; global extremes on a grid. PP's 17×17 scan and independent code agree. Closed-form candidates are in §2. |
| 4c | Φ_max = 2Φ_(D) | arith. PROVED; R_max = 12 COND | Same | 144·12/ℓ² = 432(πN)^{−2/3} = 2·216(πN)^{−2/3}: exact. Numerically 0.7000095264 = 2 × 0.3500047632. |
| 4d | EH lock k² = Φ/1728 on MN2 | REF (sampled points) | **REF (under Φ-1; genuine counterexample)** | The argument is stronger than MR2 states. Φ is non-constant (4b-i, PROVED), so **no constant k of any value** satisfies k² = Φ(p)/1728 at every p. This does not depend on k = 1/L₅. Under Φ-3, k²/(Φ_max/1728) = ℓ²/L₅² = e^{−2f₀} = 2^{4/5} = 1.741101127 ≠ 1, COND on R_max = 12 and on k = 1/L₅. PP added a check with a pointwise warped k(p) = 1/(ℓe^{f₀}Δ^{1/6}): the ratio is 12·2^{4/5}/(RΔ^{1/3}) ∈ {3.490, 3.505, 2.097, 3.600, 2.000, 3.600} at MR2's six points, never 1 (COND, float). Under Φ-2 (averaged Φ): OPEN. |
| 4e | Φ-2 / W-2 integrated values | OPEN | OPEN | Not computed. |
| 4f | Torsion-free G₂ on MN2 M₇ | OPEN | OPEN | See A3: G₂-structure *existence* moves from "COND on M₆ spin (OPEN)" to COND on a cited theorem only. |
| 4g | 61 = class-S punctures / cusps under the adopted vacuum | REF | REF | Bolza Σ is compact, genus 2, so it has no cusps (P-2 is a genuine counterexample). P-1 contradicts the adopted unsourced MN2 on compact Σ. |
| 4h | §10 item 5 | CLOSED (OW 19a88b19) | CLOSED | — |

### PP-added rows
| # | Item | PP | Note |
|---|---|---|---|
| A1a | DPa-1 normalisation is canonical **relative to the integral lattice F²_ℤ and the orientation α(a,b) = sgn(a − b)** | PROVED | Every Thm-41.10 functional is cλ, c ∈ ℚˣ (PP-L2-1). λ(F²_ℤ) = ℤ (gcd of (0,1,1) is 1), so c = ±1, and positivity on s_αδ gives c = 1. Characterisation (ii) (connecting map) is taken from bd3730eb a-L1 and not re-derived here. It also needs a chosen generator of H³(G³). |
| A1b | MR2's rationale "the normalisation is not a free choice… DPa-1 adds no arbitrary datum beyond DPa-2" (unqualified, over ℚ) | **REF** (counterexample) | 2λ kills im D¹ (2·0 = 0, 2·1 − 2·1 = 0) and is nonzero on [s_αδ], so it meets every ℚ-linear constraint DPa-2 imposes. The three characterisations agree, but each imports a datum: (i) the unit value D̂₁(s_αδ) = 1, which is circular as a "forcing" argument; (ii) the lattice F²_ℤ plus a sign; (iii) a generator of H³(G³). The datum DPa-1 adds is that integral structure. The norm ‖·‖_{D1} is sign-independent, so the orientation enters only D̂₁. |
| A2 | Control in the frozen .py: the coded "(D) product" is not (D); (D) has R = 6 exactly | PROVED (exact + numeric cross-check) | MR2's self-flag explanation is REF (see §2). The routine's validity is unaffected. |
| A3 | M₆ (S⁴-bundle over Bolza, MN2 twist a₁ = 1, a₂ = 0) is spin | PROVED | TM₆ ≅ π*TΣ ⊕ V with V ⊕ ℝ ≅ π*E₅ and E₅ = L ⊕ ℝ³. deg L = (1/2π)∫ d(dx/y) = ±Area/2π = ±4π(g−1)/2π = ±2, which is even, so w₂(L) = 0. w₂(TΣ) = χ mod 2 = 0, and w₁ = 0. By Whitney, w₂(TM₆) = 0. So M₇ = ℝ × M₆ is orientable and spin. G₂-structure existence then follows from the classical criterion (orientable + spin 7-manifold; Gray / Lawson–Michelsohn): COND, citation, not re-proved. Torsion-free stays OPEN. |
| A4 | Closed forms R_max = 12, R_min = (10/3)·2^{2/3} | COND (numerical identification, 12 digits) | — |
| A5 | After ed8effba, DP-b is a candidate definition of the neutral symbol S_eff, not "a carrier for the locked S_eff" | PROVED (record reading) | MR2's precondition text ("DP-b … is meaningless if S_eff is released") is wrong. Release makes S_eff unresolved, not undefined-forbidden. A field-action reading of S_eff (bd3730eb b-I) is no longer barred, but no such action is on disk (ABSENT/OPEN). |
| A6 | DP-b arithmetic | PROVED (exact) | (4880 − 21) = 4859 = 9·539 + 8, so Ω₁ = 8 and 8 ≢ 0 (mod 539). Ω over N = 4880..4888 is [8,0,1,…,7]. N − 9·539 = 29. R(4889,21,9) = 540. L(4880) = 14 with the stated orbit; T3^{539}(4880) = 2. As statements about S_eff they stay COND on adopting DP-b. |

### Rollup
- **MR2 (its rule, 18 labelled rows):** PROVED 7 · COND 3 · OPEN 5 · REF 3 (+1 CLOSED). PP re-counted MR2's own table and the arithmetic is right.
- **PP, on MR2's rows** (4b split into 4b-i/4b-ii; 0.1 moved to CLOSED by ed8effba): **PROVED 7 · COND 4 · OPEN 4 · REF 3 (+2 CLOSED)**, 18 labelled rows.
  - Net changes: 0.1 OPEN → CLOSED. 4b split into PROVED (non-constancy, now interval-certified) and COND (range values, float). 4d REF kept, with a stronger argument (any constant k).
- **PP-added rows:** PROVED 4 (A1a, A2, A3, A5, counting A6's arithmetic within A6 below) · REF 1 (A1b) · COND 1 (A4) · plus A6 PROVED (exact arithmetic) → added total PROVED 5 · COND 1 · REF 1.
- **Recommendations (not adopted; PP grades only):**
  - DPa-1's math holds; its "forced / no free datum" rationale is REF as stated and holds only relative to the integral structure (A1).
  - DPb-1's math holds; the lock precondition is moot after ed8effba (A5).
  - L2-1 is fully on disk; L2-2 ⇔ DPa-1.
  - Rc-3 as default is consistent; Rc-REF is confirmed.
  - §10 picks Φ-1, W-1, G2-1 and P-3 are consistent with the vacuum. G2-1 is a choice, not forced: a G₂-structure exists (A3, COND).
  - The Owner chooses in his own words.

## 4. Fixes for MR2 (numbered)
1. **§0.1 / §1.2 / §2.1:** cite OW ed8effba. Layer2 LOCKED, the S_eff lock 96f8d42e and the mapping purge are all RELEASED (neutral, unresolved, nothing adopted). Drop the "if still in force" hedges and the DPb-1 precondition. Restate DP-b as a candidate definition of the neutral S_eff, not "a carrier for the locked S_eff" (A5). Note that bd3730eb's lock-based picking reasons are superseded.
2. **DPa-1 rationale:** replace "the normalisation is not a free choice / adds no arbitrary datum" with "canonical relative to the integral lattice F²_ℤ, the orientation convention and a generator of H³(G³)". State that 2λ satisfies every ℚ-linear constraint (A1b).
3. **Control self-flag:** correct the explanation. R = 6 *is* the Ricci scalar of the (D) KR product (F = L² = 2/3, Gs = 1/6, S⁴ radius ½). The frozen script codes F = 4/9, which is not (D), so the banner's "(D) product" label is the error, and "expect R=6" is right for (D). Record this in an additive erratum; leave the frozen .py unchanged.
4. **Row 4b:** split it. Non-constancy is PROVED only with exact or interval evidence (PP has supplied interval enclosures; cite them, or re-run your own). The grid range [0.308665516, 0.700009526] is float-only, so COND, not "PROVED (computer-assisted)".
5. **Row 4d:** state the stronger, k-independent form: Φ non-constant ⇒ no constant k at all satisfies k² = Φ/1728 pointwise. Separate the Φ-3 statement, which depends on k = 1/L₅ and R_max = 12. Note that L₅ is point-dependent in the warped frame (Δ^{1/6}); the pointwise-k variant also fails (A, COND).
6. **Rc-REF:** say that the N^{1/3} argument excludes only an N-independent identity. The fixed-N refutation at N = 4880 rests on the direct ratios (≥ 11.78). Optionally record the crossing values N ≈ 0.37–2.98, outside N ≫ 1.
7. **G2-2:** update "existence COND on M₆ spin (OPEN)". M₆ is spin (A3: deg L = 2, w₂ = 0), so existence is COND only on the cited G₂ criterion. G2-1 remains a choice, not a forced result.
8. **Optional:** record the numerical closed forms R_max = 12 and R_min = (10/3)·2^{2/3} (COND) and attempt a symbolic proof. That would upgrade 4c's R_max = 12 and Φ-3.
9. **Nomenclature (OW 81b74a31):** in new files use "resonant algebra" for RTA, and do not name the two DP-b product factors "Residual₅₃₉/Resonant₅₃₉" as a split. Call them the static-cell factor O(p) and the counter factor {1..W+b}. The math is unchanged.

Status unchanged: junction **UNSOLVED**; nothing adopted; Group A scope (OW 8b26c786) is a choice, not a result; Lock 96f8d42e §4 purge is RELEASED per ed8effba (neutral, not adopted; no physical map restored here). Tip 7cddb188 untouched. No CERT. No Gemini. Nothing sent outside.
