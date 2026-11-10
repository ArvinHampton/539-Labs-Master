# FINDINGS — PP audit: MR2 V2, JOINT table, t4333 EFT-validity re-audit (MN2, MN1, BBBW z=±2, ±3; N=4880, g=2) — 2026-11-09 17:33 CST (America/Chicago)
Auditor: PP (Professor Proof, Soft SF audit). Pure math. Labels: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. Refutation only by proof or counterexample.
Limits: new file only, nothing edited or overwritten. No CERT. No Gemini. Nothing sent to anyone. Outside reads: public arXiv abstract pages only (every citation CONDITIONAL). **Nothing is adopted.** Vacuum-choice HOLD (OW aaadb280) unchanged; routine stays paused.
Tip: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md re-hashed at start and at write time = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — MATCH, untouched. Note only: its mtime reads 2026-11-06 14:38:54 CST while the 10-26 Auditor record says 10:31 CDT; many files carry Nov 6 14:40 stamps (looks like a restore). Content hash is what counts.
Steering folded in: Physicist (gate relayed under OW aaadb280) items (a)–(c); NL ERRATUM6 check; MR2 ADDENDUM_FACE_DEFINED check.

## 1. Files and hashes — PROVED (all MATCH their .sha256 sidecars)
| file | sha256 |
|---|---|
| MR2_TWISTED_SUSY_VACUA_MN2_MN1_BBBW_COMPARE_2026-11-09.md | 98e502c37d42c7dc1dde4e79ce383faac14ce631545f25c50b3b601d0afa524d |
| …_COMPARE_2026-11-09.py (frozen) | 4562c8a1936a460b23999a2e4b0f5942886c53c98fee58ae185ad839b5051d4c |
| …_COMPARE_2026-11-09.log | 986adf547589e17395781d3d288e863c59cf48c7a174655c7958fab4fd26baea |
| …_COMPARE_2026-11-09_V2.py | d6e9b1f10f79b6aefa2c6c3f579f53ffd526db165c0f55149948ad1cdeccbd10 |
| …_COMPARE_2026-11-09_V2.log | c15fa0bde7cdad945610223605dbd7a8ee9c380b82a04c27ddfea3d9da38d5ed |
| JOINT_MR2_NL_TWISTED_VACUA_COMPARE_MN2_MN1_BBBW_N4880_G2_2026-11-09.md | 0b364d6e626f71f80e763eb8ccd504f512ae65f5187c8428d12464619c59f3e4 |
| JOINT_…_ERRATUM_TALLY_2026-11-09.md | dc9dd1a0f27c3afda6d12a64553b92246023ed5db83d628ffd3c370987cd2801 |
| JOINT_…_ADDENDUM_FACE_DEFINED_2026-11-09.md | 97d671e33729071a9bd70dbe2ef55ae2dc129f75937519a57700d1caf65e28d2 |
| OWNER_WRITE_MAINCHAT_t4337_…_2026-11-09_1644.md (OW) | f283cffd365ca7368a9f7b5dfdca7ee177ed54db25a28c1944999a5af755e5b6 |
| NL_DERIVED_…_2026-11-09_1620.md | 418e4e50e4ce791bfb7c00fe4916dcee7082027c38ed7c55fea82659c98838e6 |
| NL_ERRATUM4_…_1640.md | e58cede8c0ab0713f0d4b95d93068191d7ef2cb7adf65b8f3c42aa4a4753eaf8 |
| NL_ERRATUM6_CITATIONS_TWISTED_VACUA_ACCEPT_MR2_2026-11-09_1707.md | 5c012d06211319f3975f74b5a67448b140a134c71dfdf025e4ce2c50b577c019 |
| FINDINGS_PP_AUDIT_TWISTED_SUSY_VACUA_COMPARE_2026-11-09_1638.md (prior PP) | df503cd99df53b222b27f5d6a2dfbb1fb09dd9c7237630d72a7fff36a75ed494 |

PP scratch (box, /workspace/pp_v2_audit, sha256 prefixes): pp_numbers.py baf7c4aabb72fc7a; pp_riemann.py fd1486cdb422cdb2; pp_riemann2.py 444f15ded722df9a (log 5bd87b5dc4e6fb92); pp_precision_test.py c36dad2327912131 (log b2e81babc82b68b2); rerun_V2.log 73178b2c1ff466d8; dbg2.py aeddbe3639a03117 (log 7f0cbc3ddb59d6fb); mr2_core.py 65aaabd1180166a3 (= V2 lines 1–187).

## 2. V2 rerun, code diff, precision, controls
- **P1 PROVED.** V2.py rerun on the box reproduces V2.log line for line; the only differences are timing fields ("[34s]" etc.) and the log's trailing "exit_code=0" line.
- **P2 PROVED.** The metric, G₄ and curvature code is unchanged across draft aa16d54e → frozen 4562c8a1 → V2 (diff). Only the evaluation grid, precision and the controls differ. Correction to the record: draft aa16d54e is **not** lost. A copy is in PP scratch (/workspace/audit-scratch/pp_twist_1632/mr2_twist.py, sha prefix aa16d54e26dd883f), and that copy was used for this diff.
- **P3 PROVED (at the tested points).** The precision explanation holds. On the aa16d54e grid (1e-3 from the poles), float64 gives max|R^t_t+R| = 530, 237, 79.2 and 447. At the **same points** with mpmath dps 60, the same code gives 1.8e-16 to 3.8e-15, and R returns to its regular value (e.g. MN1: 534.68 → 4.4026). Interior float64 points (≥5 cells from the edge) are already ≤ 3.1e-12. On 40 random points per candidate (dps 60) the residual is ≤ 1.1e-53. So the old residuals are float64 cancellation near the coordinate poles, not a property of the solution.
- **P4 PROVED.** The controls work as claimed. VALID (D) passes (3.53e-25, R = 6 exactly). VALID-NEG fails by the predicted 22.0. NEG-CONTROL (X₁×1.1) fails at 1.36.
- **P5 PROVED (doc fix).** The V2 header comment says "dps 50", but the code sets dps 60.

## 3. Numbers in both tables vs PP — PROVED (independent PP code, pp_numbers.py)
- a(N=4880): MN2 = 929714161355/24 = 3.8738090e10 (GM (2.5) exact); MN1 = 522964216677/16 = 3.2685264e10; BBBW z=±2 = 4.9555803e10; z=±3 = 6.1378909e10. **All match PP's values.** MN1/MN2 = 27/32 exactly (large N). a/c ∈ [½, 3/2] for all four.
- X_i, e^{f₀}, e^{2g₀}, the constraint (X₁X₂)²(X₁+X₂) = 3/2, ratios to a_D (1.1626, 1.3778, 1.7626, 2.1831), L₅ (39.470, 37.654, 36.305, 35.601 ℓ_p), G₅, Area(Σ), Σ/L₅ and the Φ ranges all match the JOINT table and NL 1620 to every quoted digit.
- Twist integrality: 2a_i(g−1) = (1±z)(g−1) ∈ ℤ gives (p,q) = (1,1), (2,0), (3,−1), (4,−2). PROVED.
- JOINT erratum tally recount: 25 / 19 / 15 / 1 unlabeled. PROVED.

## 4. Labels and citations (public arXiv abstract pages; each CONDITIONAL as a citation)
- **REFUTED (attribution).** arXiv:2009.12051 is S. Yoon, "Adjoint Reidemeister torsions of two-bridge knots", not Malek–Samtleben. The correct reference is arXiv:2009.03347, "Kaluza-Klein Spectrometry from Exceptional Field Theory": CONDITIONAL.
- **CONDITIONAL.** hep-th/9903214 (Cvetič, Duff, Hoxha, Liu, Lü, Lu, Martinez-Acosta, Pope, Sati, Tran, "Embedding AdS black holes in ten and eleven dimensions") is the S⁴ U(1)² uplift. MR2's second citation fix is correct.
- **CONDITIONAL (partial).** hep-th/0003286 (CLP, "Consistent Kaluza-Klein sphere reductions") is real, but its explicit U(1)² ansatz is for S³. It is only a partial cite for S⁴.
- **OPEN (MR2).** The ¼ coefficient of the last G₄ term. CLP (9903214 eq. (4.2)) has (1/(2g²)) X_i^{-2} d(μ_i²)∧(dφ_i+gA^i)∧*̄F^i, which is 1/8 at g = 2 with F^i = dA^i. MR2's normalization is gA^i = a_i dx/y, i.e. F^i_MR2 = g·dA^i_CLP, and in it the coefficient becomes 1/16, not ¼ (PP derivation, CONDITIONAL on CLP (4.2)). This does not affect §6, a, or NL.
- NL B1–B4 "PROVED within the truncation" → CONDITIONAL (PP N1). This is applied in the JOINT file. Confirmed.

## 5. NL ERRATUM6 (5c012d06) — PROVED: citation-only
The sidecar MATCHes. Read against NL 1620 (418e4e50), ERRATUM6 changes citations only: it accepts MR2's fixes, replacing 2009.12051 with 2009.03347 and marking hep-th/0003286 as partial for S⁴ in favour of hep-th/9903214. **No number and no label changes versus the 1620 file.**

## 6. MR2 ADDENDUM_FACE_DEFINED (97d671e3) — PROVED: no table, number or label change
- The sidecar MATCHes. The cited OW file f283cffd MATCHes its own sidecar, and the definitions quoted in the addendum (brane = stack of wrapped M5-branes; face = 10D matching hypersurface; Ξ := 49a1 ⊗ χ₁₄₀; the rest neutral) agree with the OW text. One precision point: the Owner's verbatim words are "the face as the 10D matching hypersurface". The extension "where the near-throat M5 geometry meets the asymptotic background" comes from the OW's adopted-text gloss, not the Owner's quote.
- Diff vs JOINT 0b364d6e: the addendum has **no tables at all** (0 table rows) and repeats none of JOINT's numeric cells. It supersedes only the header wording ("brane and face are UNDEFINED"). It states that no cell's number or label changes, that the tallies are unchanged, and that **every junction cell stays OPEN** for (D), MN2, MN1, z=2 and z=3. All of this is consistent with JOINT and the erratum. PP agrees that a defined face is not a solved junction, so the junction stays OPEN.
- Minor note: the header times (JOINT "17:08", addendum "17:10") are later than the files' mtimes (17:04:24 and 17:06:20 CST). This is cosmetic.

## 7. t4333 EFT-validity re-audit (ℓ = 2(πN)^{1/3}ℓ_p = 49.6844 ℓ_p, ℓ² = 2468.54 ℓ_p²)
### 7a. Curvature in Planck units
- **PROVED (reproduced).** ℓ_p²R_max = 2.835e-3 (MN1), 4.861e-3 (MN2), 6.035e-3 (z=2), 6.676e-3 (z=3); (D) 2.431e-3. This confirms the gate's 2.8e-3 to 6.7e-3.
- **R is not the right invariant.** In AdS×(sphere/hyperbolic) the negative AdS curvature and the positive sphere curvature partly cancel in R, so a small R does not bound the curvature. PP computed the full Riemann tensor with its own code (Christoffel → Riemann → orthonormal frame by Cholesky → curvature operator Q on Λ² (55×55); Kretschmann = 4ΣQ²; every sectional curvature satisfies |K| ≤ max|eig Q|).
- Validation on the exact (D) product gives Riem² = 618/ℓ⁴ and eig Q ∈ [−6, 4]/ℓ² at all 60 points, including points 1e-6 from the poles. Q is symmetric to 1e-31.
- A dps artifact was found and excluded in PP's own run. At exactly α = π/2 the simplified lambdified expressions hit 0/0 rounding, and the output changes with dps (dbg2). The grid was shifted off exact π/2 multiples by 1.234e-3, and the pole points at 1e-6 are fine.
- **PROVED at 60 sampled points (45 grid + 15 random), dps 50:**

| candidate | Riem² range [1/ℓ⁴] | ℓ_p²√Riem²_max | max\|eig Q\| [1/ℓ²] | ℓ_p² max\|K_sec\| ≤ | (ℓ_p² max\|K\|)³ (≈ R⁴ relative correction) |
|---|---|---|---|---|---|
| (D) | 618 (exact) | 1.007e-2 | 6 | 2.431e-3 | 1.4e-8 |
| MN1 | [375.8, 910.4] | 1.222e-2 | 6.629 | 2.685e-3 | 1.9e-8 |
| MN2 | [511.8, 3408.0] | 2.365e-2 | 13.333 | 5.401e-3 | 1.6e-7 |
| BBBW z=±2 | [501.1, 5755.4] | 3.073e-2 | 18.849 | 7.636e-3 | 4.5e-7 |
| BBBW z=±3 | [507.3, 7318.5] | 3.466e-2 | 21.890 | 8.868e-3 | 7.0e-7 |

  The maxima sit next to the μ₁ = 1 pole (α ≈ π/2, β ≈ 0), where Δ = X₁ is smallest. For MN2, max|eig| → 40/3 there (13.3333 at the sampled point).
- **CONDITIONAL.** That the sampled maxima are the global sup. The fields are smooth on a compact internal space and the maximum is attained near the pole, so the global value is expected within O(10⁻³) relative, but this is not proved by sampling.
- Large N: all invariants scale as ℓ_p²|K| ∝ N^{-2/3}, so they shrink as N grows. PROVED (scaling).
- **MR2 E1 correction (PROVED).** The R⁴ correction relative to the two-derivative terms is ~(ℓ_p²|Riem|)³ ≈ 2e-8 to 7e-7, not (ℓ_p/ℓ)⁶ ≈ 1e-10. It is still negligible.

### 7b. Size of Σ vs the AdS radius; systole of Σ₂
- **PROVED (fact, not a failure).** Σ radius ℓe^{g₀} = 22.79, 26.63, 31.81, 36.46 ℓ_p vs L₅ = 39.47, 37.65, 36.31, 35.60 ℓ_p, so Σ/L₅ = 0.577, 0.707, 0.876, 1.024. Area(Σ) = 6525.7, 8908.3, 12713.8, 16700.4 ℓ_p². There is no scale separation. The object is the 11D solution, so this does not undermine 11D-sugra validity; it affects only a lower-dimensional EFT reading.
- **PROVED (bound).** The internal metric's Σ block is ℓ²e^{2g₀}Δ^{1/3}ds²(H²/Γ) plus PSD fibre terms, and min X ≤ Δ ≤ max X. So the 11D length of the shortest non-contractible loop from Σ satisfies ℓe^{g₀}(min X)^{1/6}·sys_hyp ≤ sys₁₁ ≤ ℓe^{g₀}X₀^{1/6}·sys_hyp (the upper bound uses the loop at μ₀ = 1, where Δ = X₀):
  - MN1: [22.57, 23.68] × sys_hyp ℓ_p
  - MN2: [24.84, 27.88] × sys_hyp ℓ_p
  - z=2: [29.05, 33.52] × sys_hyp ℓ_p
  - z=3: [32.97, 38.54] × sys_hyp ℓ_p
- **CONDITIONAL.** sys_hyp ≤ 2 arccosh(1+√2) = 3.0571 (the Bolza maximum for genus 2, Jenni). So sys₁₁ ≤ 72.4, 85.2, 102.5, 117.8 ℓ_p.
- A sufficient condition for sys₁₁ ≥ 2πℓ_p is sys_hyp ≥ 0.278 (MN1), 0.253 (MN2), 0.216 (z=2), 0.191 (z=3). PROVED (arithmetic).
- **OPEN.** The absolute systole. The genus-2 complex-structure modulus is not fixed by the solution, and sys_hyp → 0 at the boundary of moduli space. If a loop shrinks below ~ℓ_p, M2-branes wrapped on it become light and the description changes (11D → IIA with a shrinking circle). This holds for every candidate equally, so it does not discriminate. The condition is to pick Σ with sys_hyp ≳ 0.3. This is not a choice PP makes.

### 7c. String coupling, poles, singular loci
- **PROVED (given the metric).** 11D has no dilaton, so there is no g_s in the 11D description. A g_s would appear only after reducing on a small circle, and the only circles that degenerate are the φ_i circles at the μ_i = 0 poles, which shrink smoothly. Near a pole the radial and angular coefficients both tend to 1/X_i with φ period 2π, so there is no conical defect. Δ ≥ min X > 0 everywhere, so there are no singular loci and the warp factors are bounded. The curvature at the poles is the maximum in §7a (≤ 8.9e-3 in Planck units).

### 7d. BF and unitarity
- **CONDITIONAL.** In every row the lowest neutral mass is m²L₅² = −4, which is BF-saturated (NL, on the CLP truncation). SUSY plus unitarity gives m²L² ≥ −4 for the supermultiplet scalars (CONDITIONAL on the literature). (D) is BF-violating (−16/3, PROVED earlier), and that mode is absent in the twisted vacua.
- **OPEN.** The full KK spectrum (charged modes, higher KK levels). For the SUSY vacua, stability is expected from SUSY (CONDITIONAL), but it is not computed.

### 7e. Per-candidate EFT verdicts
| candidate | verdict | reason |
|---|---|---|
| MN2 (z=±1) | **CONDITIONAL** | Curvature ≤ 5.4e-3 ℓ_p⁻² at sampled points, smooth, no singular loci, SUSY. Conditions: CLP/MN/GM citations, the global sup of the sampled curvature, sys_hyp ≳ 0.25, and full KK stability OPEN. CFT dual known. |
| MN1 (z=0) | **CONDITIONAL** | Lowest curvature (≤ 2.7e-3), otherwise the same conditions (sys_hyp ≳ 0.28). CFT dual known. |
| BBBW z=±2 | **CONDITIONAL** | Curvature ≤ 7.6e-3; same conditions (sys_hyp ≳ 0.22). CFT dual unknown (OPEN). |
| BBBW z=±3 | **CONDITIONAL** | Curvature ≤ 8.9e-3; same conditions (sys_hyp ≳ 0.19). CFT dual unknown (OPEN). |

No candidate is REFUTED: all are ≥ 110× inside the sugra regime by max sectional curvature. None is PROVED, because of the citation, sampling, modulus and KK-spectrum conditions.

### 7f. Recommendation (mathematical; adopt nothing)
- The MN2 recommendation (PP df503cd9 §7) **still stands**. EFT validity does not discriminate: all four pass by the same margin type.
- MN1 has about 2× smaller curvature, but MN2 keeps its advantages: 4D N=2 with SU(2)_R × U(1)_r, an exact GM closed form for a and c, and a known CFT dual.
- BBBW |z| ≥ 2 has the largest curvature and an unknown dual.
- The choice is the Owner's. The vacuum-choice HOLD (OW aaadb280) stands.

## 8. Fixes needed
**MR2:**
1. The G₄ last-term coefficient: ¼ → 1/16 in MR2's normalization F^i = a_i dx∧dy/y² (or 1/8 with CLP's F = dA). Re-derive from CLP (4.2) and state the normalization.
2. E1: replace the R⁴ estimate (ℓ_p/ℓ)⁶ ~ 1e-10 with (ℓ_p²|Riem|)³ ≈ 2e-8 to 7e-7.
3. E1 / M5 column: "PROVED (grid)" → "PROVED at sampled points; global sup CONDITIONAL". Report Riem² and max sectional curvature (§7a table) alongside R, since R alone understates the curvature.
4. Add the systole bounds of §7b and state that the absolute systole is OPEN, depending on the unfixed genus-2 modulus.
5. Fix the V2 header comment from "dps 50" to "dps 60".
6. Disclose that draft aa16d54e is not lost (a PP scratch copy exists, sha prefix aa16d54e26dd883f).
7. Optional cosmetic: header times vs file mtimes (JOINT, ADDENDUM).

**NL:**
- None beyond ERRATUM6, which PP verified as citation-only. The "lifted −16/3" wording is already handled (ERRATUM4 / JOINT note 4).

## 9. Rollup (items in this file)
- PROVED 21: §1 hashes; tip; P1–P5; a-values; other table numbers; twist integrality; erratum tally; ERRATUM6; ADDENDUM; ℓ_p²R; sampled Riem²/K_sec; E1 correction; systole two-sided bound; poles/no singular loci/g_s; Σ vs L₅ fact.
- CONDITIONAL 9: 2009.03347; hep-th/9903214; hep-th/0003286 (partial); global curvature sup; BF ≥ −4 by SUSY/unitarity; the four EFT verdicts.
- OPEN 4: G₄ ¼ coefficient; absolute systole (modulus); full KK spectrum; BBBW |z| ≥ 2 CFT dual.
- REFUTED 1: the 2009.12051 attribution.
- PENDING 0.
- **Total 35.**
No CERT. Nothing adopted. Nothing sent.
