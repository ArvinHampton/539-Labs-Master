# FINDINGS: PP audit of the MR2/NL comparison of twisted SUSY vacua (MN N=2, MN N=1, BBBW) at N = 4880, g = 2. 2026-11-09 16:38 CST (America/Chicago)
Agent: Professor Proof (Soft SF). Additive file; nothing edited.
Authority (each sha256 re-hashed and matched to its sidecar):
- OW 822cecb27e974268175d5d88d6b0ab032fc7be1d85ea5f10321d9c24da128ca0 (replace (D) with a twisted SUSY vacuum; compare before adopting)
- OW 2d1e877e (t4315: G = ½T^(EH), P_rev = T1)
- OW 5a6e7177 (blueprint; Λ₀ and R_c := κℓ_P as definitions)
**OW 5f59e33e5b49… (voice 1f7b6901) WITHDRAWS t4327 (ed526f70).** Ξ is UNNAMED; carrier, brane and face are UNDEFINED; R_c's physical role is OPEN; DP-a and Layer2 have no stance. No t4327 consistency check is made here.
Limits: tip 7cddb188 untouched (re-hashed: MATCH). No CERT. Nothing sent outside. No Gemini. LOCK 96f8d42e §4 not used.
Scratch: /workspace/audit-scratch/pp_twist_1632/
- pp_twist_check.py a7e19083… / .log f5505cae…
- re-run copies of NL's scripts
- mr2_twist.rerun 1c93fd49…
Literature: the BBBW (1203.0303) and MN (hep-th/0007018) PDF texts in NL's folder were read. Citations are CONDITIONAL.

## Rollup
PROVED 9 · CONDITIONAL 10 · OPEN 5 · PENDING 4 · REFUTED 0. **Fixes requested: NL 4, MR2 4.**

## 0. Inputs and integrity
- **I1 (PROVED).** NL_DERIVED_TWISTED_VACUA_…_1620.md sha256 418e4e50e4ce791bfb7c00fe4916dcee7082027c38ed7c55fea82659c98838e6 equals its sidecar.
  - NL's script and log hashes all match the values cited in the file (core c7b534a9, nl_twist_main a3e12b75/30b89fb5, nucl_identity 3fd1c5ce/af06bdbf, downstream 2c324cfe/36a307fd).
  - Re-runs of copies: nucl_identity and downstream are byte-identical. nl_twist_main differs only in the absolute script path printed in a numpy RuntimeWarning line (stderr capture); the content is identical.
- **I2 (PENDING).** MR2_TWISTED_SUSY_VACUA_MN2_MN1_BBBW_COMPARE_2026-11-09.py has **no sidecar**, and it changed while I was auditing:
  - 6d069d09 (as cited by NL 16:20) → aa16d54e (PP copy, 16:33) → 4562c8a1 (16:35).
  - PP re-ran aa16d54e (exit 0). Results are in §§1–5.
  - MR2's .md and .log, and any joint MR2/NL table, had **not landed** at 16:38 (reports/ re-checked). They are PENDING.

## 1. Are these 11D (7D gauged-sugra) solutions with an AdS₅×Σ_g twist?
- **S1 (CONDITIONAL, citation; PDF text read).** BBBW §3, eq. (3.8): the AdS₅ fixed points of the U(1)² truncation of 7D SO(5) gauged sugra on Σ_g, with twist fluxes p/(8g−8) and q/(8g−8), p + q = 2g − 2.
  - For **κ = −1 (hyperbolic Σ, g ≥ 2)** BBBW (L645) state that "the metric functions and the scalars are real for all properly quantized values of z".
  - |z| = 1 is MN N=2 and z = 0 is MN N=1 (L647–648; MN hep-th/0007018 also requires g > 1).
  - Uplift to 11D: CLP hep-th/9903214 / Cvetič et al. hep-th/0003286 (CONDITIONAL).
  - Supersymmetry: MN2 has 8 supercharges (4D N=2); MN1 and BBBW |z| ≠ 1 have 4 (4D N=1) (CONDITIONAL, citation).
- **S2 (PROVED, arithmetic).** At g = 2: p + q = 2 and z = (p − q)/(p + q) = p − 1 ∈ ℤ.
  - The admissible points are z = 0 (MN1), |z| = 1 (MN2) and |z| ≥ 2 (BBBW); z and −z are mirror images.
  - BBBW's count of g − 2 fixed points with 0 < z < 1 (L436) is 0 at g = 2. So NL's z = ½ is only a code check, as NL says.
  - Σ must be hyperbolic, and g = 2 is allowed for all three.
- **S3 (PROVED, independent).** From BBBW (3.8) as printed (κ = −1), I computed X₁ = e^{2λ₁} and X₂ = X₁e^{−2(λ₁−λ₂)}. They match MR2's and NL's fixed-point values to 12 digits at z = 2 and 3. MN2 has X₁ = 2^{−3/5}, X₂ = X₀; MN1 has X₁⁵ = 3/4.
- **S4 (PENDING; flag on MR2).** MR2 .py §6 "11D Einstein check R^t_t = −R" **fails on its own terms**:
  - max|R^t_t + R| = 530 (MN1), 237 (MN2), 79 (z=2), 447 (z=3), against R of order 5–500.
  - The negative control (X₁×1.1) gives a residual of the same size (498). So the check is non-discriminating, and either the coded uplift metric or the Ricci routine is wrong.
  - The criterion itself is correct: with G₄ having no AdS₅ legs, R^t_t = −G²/144 = −R.
  - So MR2's 11D curvature numbers (Φ = 144R ranges, ℓ_p²R_max ≈ 0.03–0.22, used for EFT validity) are **not usable**. Existence of the solutions rests on S1 (citation), not on MR2 §6.

## 2. Central charges at N = 4880, g = 2 (pp_twist_check.log; standard (2πℓ_P)³N)
- **A1 (PROVED, arithmetic on BBBW (2.22), κ = −1).** a = c = (g−1)N³(−1 + 9z² + (1+3z²)^{3/2})/(48z²). Values:

| candidate | a/N³ (large N) | a = c (large N) | a/a_(D) |
|---|---|---|---|
| MN1 z=0 (limit) | 9/32 = 0.28125 | 3.2685264×10¹⁰ | 1.162551 |
| MN2 z=1 | 1/3 | 3.8738091×10¹⁰ | 1.377838 |
| BBBW z=2 | 0.4264175343 | 4.9555803×10¹⁰ | 1.762603 |
| BBBW z=3 | 0.5281529477 | 6.1378910×10¹⁰ | 2.183128 |

  - MN1/MN2 = 27/32.
- **A2 (PROVED, arithmetic; formulas CONDITIONAL on GM (2.5) and BBBW (2.20)).** Exact finite N:
  - MN2: a = (8N³ − 3N − 5)/24 = 929714161355/24 and c = (2N³ − N − 1)/6 = 232428539119/6.
  - MN1: a = (9N³ − 3N − 6)/32 = 522964216677/16 and c = (9N³ − 5N − 4)/32 = 261482105899/8.
  - These agree exactly with MR2's a-maximization output and NL's numbers.
- **A3 (CONDITIONAL).** NL's holographic a = πL₅³/(8G₅) equals (2.22) to 10⁻¹² (NL T1), and MR2 §5 reproduces it with J/(8π²/3) = 1. L₅, Area and G₅ are 7D-frame quantities. Only a is frame-invariant, as NL D1 correctly says.

## 3. Perturbative stability
- **P1 (CONDITIONAL; representation theory plus Killing spinors).** Each candidate is supersymmetric with globally defined Killing spinors on compact Σ₂ (that is what the twist is for). So every KK mode sits in a unitary representation of SU(2,2|2) or SU(2,2|1), and unitarity forces m²L₅² ≥ −4. **No BF-violating mode can exist** (Breitenlohner–Freedman; Gibbons–Hull–Warner). This is the standard argument and rests on citation. NL's B5 is correct in substance.
- **P2 (CONDITIONAL on the CLP Lagrangian; arithmetic re-run).** The U(1)²-neutral pair inside the old 14 has m²L₅²:
  - MN2: −4, 0, 12. This matches Cheung–Gauntlett–Rosen 1906.08900 §6.1 as cited by MR2 earlier.
  - MN1: −4, 4 ∓ 2√7.
  - z = 2: −4, 0.946, 13.84.
  - The (D) value −16/3 does not occur. It is **absent**: these are different vacua, so the mode is not literally "lifted", but the corresponding neutral modes sit at or above BF.
  - NL labels B1–B4 PROVED "within the truncation". They rest on the cited CLP/MN 7D Lagrangian (NL T2 is CONDITIONAL), so the correct label is **CONDITIONAL** (fix N1 below).
- **P3 (OPEN).** Not computed: the 12 charged components of the 14 (sections of the twist bundles), the Σ-harmonic towers and the full KK spectrum. P1 bounds all of them at ≥ −4 (CONDITIONAL), but no explicit spectrum exists.

## 4. Non-perturbative M5-wall nucleation (the √6/2 analogue)
- **W1 (PROVED, independent).** NL N2's identity (X₁X₂)²(X₁+X₂) = 3/2 holds on the BBBW family. I verified it from my own transcription of BBBW (3.8) (not NL's code): exactly 1.5 at z = ½, 2, 3, 5, 7, 20 (20 digits), and in the limits z → 1 (MN2) and z → 0 (MN1). MR2's independent X values give 1.5 as well. So NL's R = (2I − 1)/2 = 1 at μ₀ = 1.
- **W2 (CONDITIONAL; CLP uplift, probe limit, H₃ = 0, homogeneous wall).** The wall ratio formula R(μ) is NL's derivation, calibrated to √6/2 on (D) and 1 on AdS₇.
  - **Verdict:** the ratio drops from √6/2 > 1 to exactly 1 (BPS saturation, no net force) for every candidate at its admissible homogeneous positions. No probe-level nucleation.
  - NL's admissibility restriction (N1: μ_i = 0 for twisted U(1)s) is correctly argued (no section at fixed φ_i of a degree-≠0 bundle).
- **W3 (OPEN).** Inhomogeneous walls and backreacted bubbles, as NL N4 says. The positive-energy argument (P1) covers them only CONDITIONALLY.

## 5. Owner conventions
- **C1 (PROVED).** G = ½T^(EH) is the standard 11D Einstein equation (PP F1 audit 1530; NL carry-forward 1556). The candidates solve standard 11D sugra (S1), so they are compatible, with no rescaling. A1/A3 confirm the standard flux quantum.
- **C2 (PROVED).** F¹∧F² = 0, since both are 2-forms along the 2-dimensional Σ. So S₃ = 0 is consistent (NL C2).
- **C3 (CONDITIONAL).** P_rev = T1 lives on H⊗ℂ², and no bulk→H⊗ℂ² map is defined, so there is no conflict at the level of definitions (NL C4). The R-symmetry interplay is OPEN (NL C5).
- **C4.** The t4327 items are withdrawn (5f59e33e), and NL D3's "brane/face" stays UNDEFINED. NL's own note NL_NOTE_JUNCTION_EVAL_WITHDRAWN… (1633) is consistent with that. No check is made.
- **C5 (CONDITIONAL).** NL R1 ("(D)'s k and G₅ carry over", REFUTED by computation) is correct: the D1 table values differ. But these are frame-dependent 7D quantities, so it is the downstream items, not physics, that change.

## 6. Per-candidate verdict
| candidate | 11D/7D solution, g=2 | SUSY | a = c (N=4880, large N) | BF (perturbative) | M5 wall ratio | overall |
|---|---|---|---|---|---|---|
| (D) reference | yes (PROVED) | none | 2.8115×10¹⁰ | UNSTABLE (14 at −16/3) | √6/2 > 1 | rejected |
| MN N=2 (z=±1) | yes (CONDITIONAL, citation) | N=2 (8 Q) | 3.8738×10¹⁰ (exact a=929714161355/24) | stable (CONDITIONAL); neutral modes −4, 0, 12 | 1 (BPS) on the arc μ₁=0 | **viable** |
| MN N=1 (z=0) | yes (CONDITIONAL) | N=1 (4 Q) | 3.2685×10¹⁰ (exact a=522964216677/16) | stable (CONDITIONAL); −4, 4∓2√7 | 1 (BPS) at μ₀=1 | viable |
| BBBW z=±2 | yes (CONDITIONAL) | N=1 | 4.9556×10¹⁰ | stable (CONDITIONAL); −4, 0.946, 13.84 | 1 | viable |
| BBBW z=±3 | yes (CONDITIONAL) | N=1 | 6.1379×10¹⁰ | stable (CONDITIONAL); −4, 1.43, 14.75 | 1 | viable |
EFT validity (curvature in ℓ_p units) is **PENDING** for all candidates, because MR2's §6 numbers are unusable (S4).

## 7. Recommendation (mathematical, not an adoption)
**MN N=2 (z = 1)** is the most defensible choice. On the stability criteria all candidates tie, so the recommendation rests on the following:
1. Maximal supersymmetry (8 supercharges) gives the strongest protection. Its spectrum has published independent data: CGR 1906.08900 (truncation masses −4, 0, 12) and Gaiotto–Maldacena.
2. a and c are known in closed form at finite N (GM (2.5)), with no a-maximization subtleties.
3. It has the extra SO(3) isometry, which simplifies any later KK, junction or W₃₅ work.
4. BBBW |z| ≥ 2 is a one-parameter family whose z the Owner would also have to choose, and nothing in the project selects it.
5. MN1 is equally consistent, but it has fewer supercharges and an irrational spectrum (1 + √7).

If the Owner prefers N = 1, MN1 is the natural choice. "No clear winner" applies only if extra criteria (for example a target a/N³) are added.

## 8. Fixes requested
**NL (418e4e50):**
- N1. B1–B4 "PROVED within the truncation" should be CONDITIONAL on the CLP/MN 7D Lagrangian (their own T2). The same applies to T0's reduction (the calibrations are PROVED; the reduction is cited).
- N2. Replace "the −16/3 channel is lifted" with "absent in the twisted vacua (different background); the neutral pair sits at ≥ −4".
- N3. B5: state the unitarity argument explicitly (SU(2,2|N) multiplets ⇒ m²L² ≥ −4), and keep it CONDITIONAL.
- N4. D3/D2: tie the junction and V₇eff items to the t4327 withdrawal (brane/face UNDEFINED); NL's 1633 note does this. Keep D2's G₄ values clearly on hold.

**MR2:**
- M1. Write the .md, the .log and the .sha256 sidecars, and freeze the .py (three hashes in 20 minutes: 6d069d09, aa16d54e, 4562c8a1).
- M2. §6 11D Einstein check: the residual |R^t_t + R| is O(R) for every candidate **and** for the negative control. Fix the uplift transcription or the Ricci routine and re-run. Until then, no Φ = 144R or EFT-validity numbers from §6 may be quoted.
- M3. Label every literature-derived item (BBBW (3.8), (2.20), (2.22), GM (2.5), CLP uplift) CONDITIONAL; arithmetic on them can be PROVED.
- M4. Supply the SUSY count and an EFT-validity column for the joint table, using a corrected §6.

## 9. Open / pending
- PENDING: MR2 .md/.log/sidecars; joint MR2/NL table; corrected MR2 §6 (EFT validity); a stable MR2 .py hash.
- OPEN: full KK spectra (P3); inhomogeneous or backreacted walls (W3); R-symmetry vs P_rev (C3); junction, V₇eff and b (on hold; brane/face undefined per 5f59e33e).

Tip 7cddb188 untouched. No CERT. Nothing sent outside. No Gemini.
