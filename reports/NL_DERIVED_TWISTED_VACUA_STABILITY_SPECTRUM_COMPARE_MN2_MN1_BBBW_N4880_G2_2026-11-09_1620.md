# NL DERIVED: twisted SUSY vacua — stability and spectrum compare (MN N=2, MN N=1, BBBW) at N = 4880, g = 2 — 2026-11-09 16:20 CST (America/Chicago)
Agent: Non Local Path (NL). Authority: Owner widget 4:09 PM CST, OW record OWNER_WRITE_MAINCHAT_VACUUM_REPLACE_D_TWISTED_SUSY_COMPARE_2026-11-09_1609.md (sha 822cecb27e974268175d5d88d6b0ab032fc7be1d85ea5f10321d9c24da128ca0, verified). **Nothing is adopted.** This file only compares.
Limits: new additive file; nothing edited. Tip 7cddb188… checked before and after. No CERT. Nothing sent to Gemini or any service. Public arXiv PDFs read: hep-th/9903214 (CLP), hep-th/0007018 (MN), 1203.0303 (BBBW).
MR2 geometry file: MR2_TWISTED_SUSY_VACUA_MN2_MN1_BBBW_COMPARE_2026-11-09.md not yet written at 16:20. Only its script exists (….py, sha 6d069d094fd15532198bc14b4afdcb52dd0601cc9f88185a326b505f62dcbe57). Its a_D = (8/81)√6 N³ = 0.241925 N³ and its use of BBBW (3.8) agree with this file. MR2's metrics, susy, a/c and EFT columns are left as placeholders.
Scripts and logs: /workspace/nl-twist-1609/ (each with .sha256)
- core.py c7b534a98906907b7b70df70dd189b9beb45b348e698fd187140bb5a0f5d057c
- nl_twist_main.py a3e12b75854d7085af814fff21770eb12693637792787934e87da4c3d7dbd7b5, log 30b89fb5bbaa991cdbfdb89ef9e52f817c759d07da52a8c5d2c8279b2b1db7a8
- nucl_identity.py 3fd1c5ce0f21c022feb4874a979e549a84615661cbf6ef277f4d42adf37bc58e, log af06bdbfb5aacc5fdc91c99f10925a213766af2d31fa7160d5e15205104ff54a
- downstream.py 2c324cfe8f09dc33decc525b1fcee21de7f755e2e4f865a86bcb6c2518026a33, log 36a307fd7830d24591acfde2d0578fde1333bd71b3d3761ad4a4190e820a3035

## Verdict (short)
- All three candidates (MN N=2, MN N=1, the BBBW |z| ≥ 2 family) remove the (D) instability in the sector computed here. The two SO(5)-14 components that stay neutral under the twist go from m²L₅² = −16/3 in (D) to a lowest value of **exactly −4 (Δ = 2, BF-saturated, stable)** for every z. The full spectrum is stable by the positive-energy theorem (CONDITIONAL); the charged 12 components of the 14 were not computed (OPEN).
- The √6/2 analogue (probe M5 domain wall wrapped on Σ, charge/tension) is **exactly 1** at the admissible homogeneous positions for every candidate. This is BPS saturation: no net force, no probe-level nucleation. It is an exact identity on the whole BBBW family (sympy), CONDITIONAL on the CLP uplift and the probe approximation.
- Both Owner adoptions (P_rev = T1, G = ½T^(EH)) are compatible. G = ½T^(EH) is literally standard 11D sugra, which these vacua solve. P_rev lives on H⊗ℂ²; it has no stated map to the bulk fields, so no conflict can arise yet (CONDITIONAL); the R-symmetry interplay is OPEN.
- Downstream at N = 4880, g = 2: G₅ falls to 0.58 (MN2), 0.79 (MN1), 0.41 (BBBW z=2) and 0.31 (z=3) of (D)'s value. k := 1/L₅ rises by 3–14%. V₇eff and the junction tension move accordingly. The junction itself is OPEN, because the fibre is now warped and twisted.

## 1. Method (NL derived proposal)
- **T0 (PROVED; calibrations in nl_twist_main.log).** The 7D U(1)² truncation of 11D sugra on S⁴ is the CLP Lagrangian (hep-th/9903214 (4.6)–(4.8)) = MN (hep-th/0007018 eq. 89), with m = 1 and g_CLP = √2 m. I reduce it on H²/Γ with ds₇² = e^{2αh}ds₅² + e^{2βh}ds²(unit H²), α = 1/√15, β = −3α/2 (5D Einstein frame, canonical h). This gives a 5D potential V₅(λ₁, λ₂, h) with twist fluxes F^i = s(1±z)/8 vol(unit H²). Masses are m²L₅² = eig(K⁻¹∂²V₅)·(−12/V₀). The same code reproduces:
  - C1: AdS₇, 7D m²L₇² = −8 (twice) for (λ₁, λ₂), which is Δ = 4, the 14.
  - C2: (D) with no flux: m²L₅² = −16/3, −16/3, 8. This is NL O4 S1/S4 exactly.
  - C3: (D): L₅ = 40.567128, Area = 5170.0935 and G₅ = 9.324866×10⁻⁷ (F1), a = 0.241925 N³ (MR2's a_D).
  - C4: the (D) probe-M5 ratio = 1.22474487 = √6/2 (PP C4 / NL O4 Q1).
  - C5: the AdS₇ probe ratio = 1 (BPS).
- **T1 (PROVED, numerical).** With s = √2, the 5D extremum reproduces BBBW (3.8) λ₁ and λ₂ to all printed digits at z = 0, ½, 1, 2, 3, 5, 7. My 7D-frame area of Σ is exactly 2 × BBBW e^{2g₀} (a unit convention). With R_S⁴ = (πN)^{1/3}ℓ_P, L₇ = 2R_S⁴ and G₁₁ = 16π⁷ℓ_P⁹, a = πL₅³/(8G₅) equals BBBW (2.22), a = (g−1)N³(−1+9z²+(1+3z²)^{3/2})/(48z²), to 10⁻¹² at every z. So the flux normalization is the standard (2πℓ_P)³N quantum, and MN1/MN2 = 27/32.
- **T2 (CONDITIONAL; CLP, Cvetič et al. hep-th/0003286, BBBW §3).** The U(1)² truncation is consistent and uplifts to 11D. I cite this; I do not rederive it.
- **T3 (PROVED from BBBW (2.12)–(2.13)).** At g = 2, z = n/(g−1) ∈ ℤ, with (p, q) = (1+z, 1−z). The options are z = 0 (MN1, (1,1)), |z| = 1 (MN2, (2,0)) and |z| ≥ 2 (BBBW, e.g. z = 2 → (3,−1)). No point with 0 < |z| < 1 exists at g = 2; z and −z are mirror images. z = ½ appears below only as a code check.

## 2. Per-candidate results (m²L₅² in the (λ₁, λ₂, h) sector; Δ = 2 + √(4 + m²L₅²); 5D bound −4)

### 2.1 MN N=2 (z = 1)
- **B1 (PROVED within the truncation).** m²L₅² = −4, 0, 12, so Δ = 2, 4, 6. The lowest value saturates BF (Δ = 2), which fits the N=2 stress-tensor multiplet's Δ = 2 scalar.
- Fixed point: X₁ = 2^{−3/5}, X₂ = X₀ (SO(3) invariant; MR2's .py checks the same).
- Numbers: L₅ = 37.653721 ℓ_P (7D frame), Area(Σ) = 8908.32 ℓ_P², G₅ = 5.4118×10⁻⁷ ℓ_P³, a = N³/3 = 3.87381×10¹⁰.
- **Probe M5:** admissible homogeneous positions are the arc μ₁ = 0 (U(1)₂ untwisted). On that arc the ratio is ≡ 1.000000000000 (min = max, 2001 points). This is BPS: a flat Coulomb-branch direction.

### 2.2 MN N=1 (z = 0)
- **B2 (PROVED within the truncation).** m²L₅² = −4, 4−2√7 = −1.2915, 4+2√7 = 9.2915, so Δ = 2, 1+√7, 3+√7 (exact forms identified from the numbers to 10⁻⁸).
- Fixed point: X₁ = X₂, X₁⁵ = 3/4.
- Numbers: L₅ = 39.470162 ℓ_P, Area = 6525.69 ℓ_P², G₅ = 7.3878×10⁻⁷ ℓ_P³, a = (9/32)N³ = 3.26853×10¹⁰.
- **Probe M5:** the only admissible homogeneous position is μ₀ = 1 (both U(1)s twisted, p = q = 1). The ratio there is 1.000000000000.

### 2.3 BBBW family, |z| ≥ 2 at g = 2 (MN points are z = 0, 1 of the same formulas)
- **B3 (PROVED within the truncation).**
  - z = 2: m²L₅² = −4, 0.946364, 13.842533, so Δ = 2, 4.22404, 6.22404.
  - z = 3: −4, 1.431535, 14.753796.
  - z = 5: −4, 1.905079, 15.625226.
  - z = 7: −4, 2.134816, 16.042241.
  - Pattern: the lowest is always −4, and Δ₃ = Δ₂ + 2.
- Numbers:
  - z = 2: L₅ = 36.305054, Area = 12713.77, G₅ = 3.7920×10⁻⁷, a = 4.95558×10¹⁰.
  - z = 3: L₅ = 35.600612, Area = 16700.44, G₅ = 2.8868×10⁻⁷, a = 6.13789×10¹⁰.
  - a grows ~ z (BBBW (4.9)), so G₅ → 0 as |z| grows.
- **Probe M5:** μ₀ = 1, ratio 1.000000000000 at every z tested.

## 3. BF stability: is the (D) −16/3 channel lifted?
- **B4 (PROVED within the truncation).** The (D) unstable mode is the Σ-constant 14. Under the twist SO(5) → U(1)² (or SO(2)×SO(3) for MN2), the U(1)²-neutral part of the 14 is the (λ₁, λ₂) pair. In (D) both sit at −16/3 (C2). In every twisted vacuum the pair moves to {−4, m₂²}, with m₂²L₅² ∈ {0 (MN2), −1.2915 (MN1), +0.946 (z=2), …}. So the −16/3 channel is lifted to the BF bound and no longer violates it.
- **B5 (CONDITIONAL; positive-energy theorem: Breitenlohner–Freedman 1982; Gibbons–Hull–Warner 1983; Townsend 1984).** Each candidate keeps globally defined Killing spinors on compact Σ₂. With the twist the spinors are constant sections. So the full linearized KK spectrum satisfies m²L₅² ≥ −4, and the lowest KK scalar is −4 (attained, B1–B3). I cite this; I did not recompute it.
- **B6 (OPEN).** Not computed:
  - the 12 charged components of the 14, which become sections of the twist bundles over Σ;
  - Σ-harmonic towers;
  - the full KK spectrum on the twisted S⁴ fibration. This needs e.g. ExFT KK spectrometry (Malek–Samtleben 1911.12640, 2009.12051). I found no published full spectrum for these vacua in this pass. B5 bounds all of these at ≥ −4.

## 4. Brane nucleation: the analogue of PP's √6/2
- **N0 (PROVED, calibration).** Probe M5 on ℝ^{1,3}×Σ at a point μ of S⁴, using CLP (4.1) for the metric and the ε₇ term of (4.2) for *G₄:
  - U(μ) = 2g Σ_α(X_α²μ_α² − Δ̃X_α) + gΔ̃X₀, Δ̃ = Σ X_α μ_α².
  - DBI ∝ Δ̃ e^{4r/L₅}; WZ ∝ −U L₅/4 · e^{4r/L₅}. So R(μ) = −U(μ)L₅/(4Δ̃(μ)), normalized so that AdS₇ gives 1.
  - It returns √6/2 for (D) (C4) and 1 for AdS₇ (C5).
- **N1 (CONDITIONAL: static wall homogeneous on Σ).** A wrapped M5 at a Σ-constant μ needs μ_i = 0 for every U(1)_i of nonzero degree. A degree-≠0 circle bundle has no section at fixed φ_i.
  - Admissible loci: MN2, the arc μ₁ = 0; MN1 and BBBW, the point μ₀ = 1.
  - The naive values at charged points (e.g. 1.5 for MN2 at μ₁ = 1) are not admissible probes. They omit the fibration term in the DBI, which only raises the tension. They are not evidence of nucleation.
- **N2 (PROVED, sympy identity, nucl_identity.log).** At μ₀ = 1, R = (2(X₁X₂)²(X₁+X₂) − 1)/2. On BBBW (3.8), (X₁X₂)²(X₁+X₂) = 3/2 identically in z (symbolic residual 0). So **R = 1 exactly** for MN1, MN2 (limits) and all BBBW z. For MN2, R ≡ 1 on the whole arc μ₁ = 0 (numerical, 10⁻¹²).
- **N3 (CONDITIONAL; CLP uplift, probe limit N ≫ 1, worldvolume H₃ = 0, leading order in ℓ_P/L).** Verdict: the ratio is 1, i.e. BPS saturation with no probe-level nucleation, for every candidate. (D) had √6/2 > 1. This matches the BPS expectation; here it is derived, not assumed.
- **N4 (OPEN).** Two things are not studied: walls whose μ varies over Σ (sections through μ_i = 0, with gradient and extra WZ terms), and backreacted bubbles beyond the probe limit. B5's positive-energy argument covers the latter (CONDITIONAL).

## 5. Compatibility with OW 2d1e877e (P_rev = T1; G = ½T^(EH))
- **C1 (PROVED).** G_MN = ½T^(EH)_MN(G_std) is identically the standard 11D Einstein equation (NL carry-forward 1556; F1). The vacua solve standard 11D sugra with the standard quantum (T1: a matches BBBW (2.22)). So nothing needs rescaling.
- **C2 (PROVED).** In the U(1)² truncation the Chern–Simons/odd-dimensional source F¹∧F² vanishes, because both are 2-forms on the 2-dimensional Σ. So S₃ = 0 is consistent and no extra CS term is needed beyond the standard d*G = ½G∧G.
- **C3 (CONDITIONAL).** Supersymmetry uses the standard 11D gravitino variation with the standard G normalization, and ½T^(EH) touches neither. The CS sign convention (NL O4 A2) and the uplift orientation fix which of z and −z is "p ≥ q", with no physical effect.
- **C4 (CONDITIONAL).** P_rev = T1 = (S·P̂)|_{H₋} = P₋ is defined on the 4D Dirac-level space H⊗ℂ². The corpus has no map from the 11D gravitino or the Killing spinors to H⊗ℂ², so no twisted vacuum conflicts with it at the level of definitions.
- **C5 (OPEN).** How P₋ (antiunitary, contains parity) acts on the R-symmetry: SU(2)_R×U(1)_r for MN2, U(1)_R for MN1/BBBW. The twist ties U(1)_R to the Σ spin connection, and an antiunitary map flips R-charge. Whether P₋ must commute with the R-symmetry is undecided until a bulk-to-H⊗ℂ² map is defined.

## 6. Downstream at N = 4880, g = 2 (downstream.log; on hold per OW 822cecb2)
- **D1 (CONDITIONAL on N, g and the convention).** G₅ uses the same convention as F1: G₅ = G₁₁/(Vol S⁴_R · Area₇D(Σ)), with L₅ the 7D-frame AdS₅ radius. In 11D the AdS₅ factor is warped by Δ̃^{1/3}, so G₅ alone is frame-dependent; the invariant is a = πL₅³/(8G₅) (T1).

| vacuum | L₅ [ℓ_P] | k = 1/L₅ | Area(Σ) [ℓ_P²] | G₅ [ℓ_P³] | G₅/G₅(D) | a/N³ |
|---|---|---|---|---|---|---|
| (D) ref | 40.567128 | 0.0246505 | 5170.09 | 9.3249e-7 | 1 | 0.241925 |
| MN2 | 37.653721 | 0.0265578 | 8908.32 | 5.4118e-7 | 0.5804 | 1/3 |
| MN1 | 39.470162 | 0.0253356 | 6525.69 | 7.3878e-7 | 0.7923 | 9/32 |
| BBBW z=2 | 36.305054 | 0.0275444 | 12713.77 | 3.7920e-7 | 0.4067 | 0.426418 |
| BBBW z=3 | 35.600612 | 0.0280894 | 16700.44 | 2.8868e-7 | 0.3096 | 0.528153 |

- **D2 (CONDITIONAL; PP 9dde377d B2).** V₇eff = V̂₆(1 − e^{−2kb})/(2k). Under a consistent truncation, V̂₆ → G₁₁/G₅ (the warp integrates out). With b OPEN, the kb → ∞ values are:
  - V₇eff = 1.0512e12 (D), 1.6811e12 (MN2), 1.2909e12 (MN1), 2.3133e12 (z=2), 2.9798e12 (z=3) ℓ_P⁷.
  - G₄ = G₁₁/V₇eff = 4.597e-8 (D), 2.875e-8, 3.744e-8, 2.089e-8, 1.622e-8 ℓ_P².
- **D3 (OPEN; PP 52acc3d7).** PP's Israel algebra assumes an unwarped fibre with A′ = k, B′ = 0. In the twisted vacua the 4D block is pointwise k_eff(μ) = Δ̃(μ)^{−1/6}/L₅, and the fibre is the twisted S⁴-bundle over Σ. So the face stress is non-uniform over S⁴. PP O1 (the Z₂ parity of C₃) now also involves the G₄ legs on Σ. The reference tension σ₄ = 6k/κ² moves from 1.2178e-7 ((D), equal to PP's value) to 1.3120e-7 (MN2), 1.2516e-7 (MN1), 1.3607e-7 (z=2) and 1.3877e-7 (z=3) ℓ_P⁻¹⁰. The junction stays OPEN until the brane and face are defined (PP: no Owner record defines them).
- **D4 (OPEN).** b, and hence the finite-b V₇eff and G₄.
- **R1 (REFUTED, by computation).** "(D)'s k = 0.0246505 and G₅ = 9.33e-7 carry over to the replacement vacuum." Every candidate differs (table D1).

## 7. Joint comparison table — NL half (MR2 columns are placeholders)
| candidate | susy | BF status / lowest scalar | nucleation ratio | T1/½ compatibility | G₅ [ℓ_P³] | junction / V₇eff effect |
|---|---|---|---|---|---|---|
| (D) ref | none | UNSTABLE: 14 at −16/3 | √6/2 = 1.2247 | ½: yes; T1: n/a | 9.3249e-7 | PP 52acc3d7 / 9dde377d baseline |
| MN N=2 (z=1, (p,q)=(2,0)) | [MR2] | stable; lowest −4 (Δ=2), then 0, 12 (B5 CONDITIONAL for full KK) | 1 (BPS, arc μ₁=0) | ½: PROVED; T1: no conflict (CONDITIONAL), R-sym OPEN | 5.4118e-7 | V₇eff ×1.599, σ₄ ×1.077; junction OPEN (warped/twisted fibre) |
| MN N=1 (z=0, (1,1)) | [MR2] | stable; lowest −4 (Δ=2), then 4−2√7, 4+2√7 | 1 (BPS, μ₀=1) | same | 7.3878e-7 | V₇eff ×1.228, σ₄ ×1.028; junction OPEN |
| BBBW z=2 ((3,−1); z=−2 mirror) | [MR2] | stable; lowest −4, then 0.946, 13.84 | 1 (BPS, μ₀=1) | same | 3.7920e-7 | V₇eff ×2.201, σ₄ ×1.117; junction OPEN |
| BBBW z=3 ((4,−2)) | [MR2] | stable; lowest −4, then 1.432, 14.75 | 1 (BPS, μ₀=1) | same | 2.8868e-7 | V₇eff ×2.835, σ₄ ×1.139; junction OPEN |
MR2 placeholders still to merge: [metric/G₄ uplift] [susy N] [a, c finite-N] [EFT validity] [Φ/W₃₅].

## For the Owner to decide (no NL recommendation is an adoption)
1. Which candidate. On NL's stability criteria all are equal: perturbatively stable at the BF bound and BPS against probe nucleation. They differ in susy (N=2 vs N=1), a, G₅ and the size of Σ.
2. If BBBW: which z (|z| ≥ 2 at g = 2; z and −z equivalent).
3. Whether to authorize the OPEN full KK spectrum (B6) on the chosen vacuum, and a bulk-to-H⊗ℂ² map for C5.
4. The junction and face definition (D3) and b (D4), still on hold.

## Label tally
PROVED 11 (T0, T1, T3, B1, B2, B3, B4, N0, N2, C1, C2) · CONDITIONAL 8 (T2, B5, N1, N3, C3, C4, D1, D2) · OPEN 5 (B6, N4, C5, D3, D4) · REFUTED 1 (R1, by computation).

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
