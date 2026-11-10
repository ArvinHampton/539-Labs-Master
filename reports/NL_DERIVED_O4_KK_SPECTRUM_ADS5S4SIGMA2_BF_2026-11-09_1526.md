# NL DERIVED: O4 — KK spectrum of (D) = AdS₅×S⁴×Σ₂ against the 5D BF bound — 2026-11-09 15:26 CST (America/Chicago)
Agent: Non Local Path (NL). Authority: Owner, 3:13 PM CST, Physicist transcript pos 17862: "Authorize the compute go-ahead for the full Kaluza-Klein spectrum calculation based on the standard flux normalization, N = 4880, and genus g = 2 constraints adopted earlier." Joint with MR2 (literature pass); PP audits.
Limits: new additive file; nothing edited. Tip 7cddb188… checked before and after. No CERT, no Gemini, nothing sent to any agent or service. Public arXiv PDFs read: hep-th/0105047 (DFGHM), hep-th/0003281 (Kehagias–Russo).
Scripts: /workspace/nl-kk-1513/nl_kk_o4.py (sha 65d6a787d96176c872764a09fba9ed30e685976c59fabdba4ab64877ff3f3175), log nl_kk_o4.log (sha 9f581aa66f920990e7b14ba179db96322f4363f4b7d4165d9428feb033feb804).
Inputs: FINDINGS_PP_DERIVE_ADS5S4SIGMA_PARAMETERS_2026-11-09_1357.md (4660b73e), PP p_stab.log, MR2_KK_SPECTRUM_ADS5_S4_SIGMA2_BF_BOUND_2026-11-09.md (7824e789) with its .py/.log.

## Verdict (short)
- (D) is **perturbatively BF-unstable** for every N, every g ≥ 2 and every Σ modulus. The unstable field is the **14 of SO(5)** at S⁴ level ℓ = 2 (the coupled S⁴-metric-trace / S⁴-flux scalar, lower branch), constant on Σ: **m²L₅² = −16/3 < −4**.
- Σ-dependent copies of the same 14 have m²L₅² = −16/3 + 4λ̂ (λ̂ = Laplace eigenvalue on Σ rescaled to curvature −1). They are stable iff λ̂ ≥ 1/3, i.e. λ_phys ≥ 4k²/3.
- Every other bosonic tower is at or above m²L₅² = 0 (CONDITIONAL on Lemma L1 for the massive S⁴ levels).
- PP's √6/2 is a **different object**: the charge/tension ratio of a probe M5 domain wall. It is a genuine non-perturbative (brane-nucleation) channel at probe level and is **not** a truncation artifact. Both instabilities come from the same fact, L₅/L₇ = √(2/3).

## 1. Setup
- **V1 (PROVED, script §1).** With R_MN = (1/12)(G_M…G_N… − (1/12)g G²) and G = q₀vol(S⁴), q₀ = 2√6k: Ric(S⁴) = 8k² = 3/r², Ric(AdS₅) = Ric(Σ) = −4k². So X₇ := AdS₅×Σ is **Einstein** with Ric = −6/L₇², L₇ = √6/(2k) = 2r, and (D) is exactly the Freund–Rubin X₇×S⁴ of AdS₇×S⁴ with AdS₇ replaced by X₇. Radii: L₅ = 1/k, (L₅/L₇)² = 2/3.
- **V2 (PROVED).** The metric ratios L₅/ρ = 2, L₅/r = 2√6/3 match Kehagias–Russo hep-th/0003281 eq. (13) (L² = 2R₀²/3, ρ² = R₀²/6, r² = R₀²/4). This agrees with MR2.
- **V3 (OPEN, immaterial).** KR eq. (14) writes F̂₄ = 6R₀³Ω₄; in our normalization the Einstein equations force q₀ = 6/R₀. I did not reconcile KR's form convention. It does not affect any mass below, because only the Einstein equations fix q₀.
- **Equivalent 7D picture.** (D) is the SO(5)-invariant vacuum of 7D maximal SO(5) gauged sugra (T_ij = δ_ij, A = 0, S₃ = 0) on the 7D Einstein space AdS₅×Σ. The consistent truncation is Nastase–Vaman–van Nieuwenhuizen hep-th/9905075, hep-th/9911238.
- **L1 (CONDITIONAL; PP to audit).** DFGHM's linearized equations (3.16)–(7.12) for AdS_p×M_q stay valid with AdS_p replaced by any Einstein X_p of the same Ricci constant.
  - Sketch: the background flux has no X legs. X enters only through □ₓ on scalars, the Maxwell and Hodge operators, R⁽¹⁾_μν (equivalently Lichnerowicz Δ_L), and commutators ∇^μ∇_(μ∇_ν)f = ∇_ν(□ + Λ′)f. Those involve only Ric(X). Δ_L also commutes with Hessians on any Einstein space.
  - I checked this by inspecting the equations, not component by component.
- **L2 (PROVED).** On X₇ = AdS₅×Σ, the scalar, Hodge and Lichnerowicz operators split as (5D operator) + (Σ operator). Mixed Riemann components vanish, and the Σ eigenvalues are ≥ 0, except Δ_L on TT, handled in S5.
  - So a 7D field of mass M² gives 5D masses m²L₅² = (2/3)M²L₇² + (Σ shift).
  - The Σ shift is 4λ̂ for scalar harmonics, 4μ̂ for Hodge 1-form eigenvalues, and 0 on harmonic forms.

## 2. Sectors (L₇ towers from DFGHM with p = 7, q = 4, D = 11; λ_ℓ = ℓ(ℓ+3)/r²)
Calibration (script §2): the same formulas give AdS₇×S⁴ scalar Δ = 2ℓ (ℓ ≥ 2) and 2ℓ+12 (ℓ ≥ 0, breathing Δ = 12). They give vector masses 4(ℓ²−1) and 4(ℓ+2)(ℓ+4) (ℓ = 1: the 10 massless SO(5) gauge fields, Δ = 5 currents), and AdS₅×S⁵ Δ = ℓ.

**S1 (PROVED). The 14, Σ-constant: m²L₅² = −16/3.** It has three independent routes that agree:
- (a) DFGHM (4.7), lower branch m²₋L₇² = 4ℓ(ℓ−3), at ℓ = 2: −8.
- (b) 7D gauged sugra, without L1. Take L = R − ¼Tr(T⁻¹∂T)² − V with V = (g²/2)(2TrT² − (TrT)²). Then V₀ = −15g²/2, L₇² = 4/g², V′ = 0, and M² = −2g², so M²L₇² = −8 (script §3).
  - By SO(5), the 14 cannot mix linearly with the metric, A, S₃ or the breathing mode. Since □₇ = □₅ + Δ_Σ, the Σ-constant mode has m² = M².
- (c) Δ = 4 is the protected dimension of the 14 in the (2,0) stress-tensor multiplet: Δ(Δ−6) = −8.
- Normalization: a mass is an eigenvalue of the linear wave operator, so field normalization drops out. Only the M²/Λ ratio matters, and routes (a)–(c) fix it identically.
- Radius relation: Ric(X₇) = −6/L₇² = −4k² = Ric(AdS₅) = −4/L₅², so L₅²/L₇² = 2/3.
- So m²L₅² = −8·(2/3) = −16/3 < −4. In L₇ units, the 5D bound is −6 (stricter than the 7D bound −9). Δ = 2 ± 2i/√3.

**S2 (PROVED). The 14 on Σ harmonics: m²L₅² = −16/3 + 4λ̂.** This is BF-stable iff λ̂ ≥ 1/3, i.e. λ_phys ≥ 4k²/3 = 8.10196×10⁻⁴ ℓ_p⁻² at N = 4880.

**S3 (CONDITIONAL on L1). The other coupled scalars.** The lower branch for ℓ ≥ 3 is (8/3)ℓ(ℓ−3) ≥ 0. The upper branch (ℓ ≥ 0) is (8/3)(ℓ+3)(ℓ+6) ≥ 48.

**S4 (PROVED).**
- The upper branch at ℓ = 0 is the S⁴ breathing mode, with m²L₅² = 48.
- The Σ breathing mode (7D Einstein–Λ on Σ, script §5) has m²L₅² = 8.
- Both equal PP's C3 values. PP's 2-modulus truncation is therefore correct for what it contains. It cannot see the 14 because those are SO(5) non-singlets.

**S5 (PROVED). Σ components of the massless 7D graviton.** These are exact within the 7D truncation; I derived them in TT gauge from (Δ_L − 2Λ′)h = 0 with Λ′ = −4k².
- 5D graviton tower: 4λ̂ (massless at λ̂ = 0).
- Σ-scalar pieces: 8 + 4λ̂. The λ̂ = 0 value reproduces S4's 8.
- Vectors: 8 on harmonic 1-forms, 8 + 4λ̂ on coexact 1-forms.
- **Teichmüller TT modes (6g−6 = 6 real): m² = 0.** On Σ, TT tensors are exactly the holomorphic quadratic differentials, with Δ_L h = 2K h. This upgrades PP's C2 and MR2's S6 from CONDITIONAL.

**S6 (CONDITIONAL on L1). Coupled vectors (DFGHM 5.2), M²L₇² = 4(ℓ²−1) and 4(ℓ+2)(ℓ+4).**
- In 5D: 0 (the 10 gauge fields, ℓ = 1), then 8, 64/3, ….
- Wilson-line scalars from the gauge fields on harmonic 1-forms: 10 × 2g = 40 modes at m² = 0.

**S7 (CONDITIONAL on L1). Remaining towers, all with m² ≥ 0:**
- S⁴-TT metric scalars φ (DFGHM 8.3): 4ℓ(ℓ+3) for ℓ ≥ 2, giving 5D values ≥ 80/3.
- Massive 7D spin-2: 4ℓ(ℓ+3). Their Σ-TT pieces get no shift, and their Σ-scalar pieces get +8 + 4λ̂.
- 2-forms (7.5): 4(ℓ+1)(ℓ+2), giving ≥ 16.
- 3-forms with the Chern–Simons term (7.9–7.11): first-order masses |m|L₇ = 2ℓ and 2ℓ+6.
  - Taking γ from linearizing d*G = ½G∧G gives 2cγ = c. That value of γ is CONDITIONAL on the sign convention.
  - m_i² ≥ 0 holds for any γ (DFGHM 7.12).
  - The ℓ = 0, m = 0 root is pure gauge. 3-forms give no 5D scalars, since Σ has dimension 2.

**S8 (CONDITIONAL on L1). No bosonic mode other than the 14 (S1, S2) violates m²L₅² ≥ −4.**

**S9 (OPEN). Fermions.** Not computed; they are irrelevant to the BF bound.

Tables (m²L₅², Σ-constant; Σ harmonics add the shifts in L2):

| ℓ [dim] | coupled − | coupled + | spin-2 | S⁴-TT φ | vectors | 2-form | 3-form (m²) |
|---|---|---|---|---|---|---|---|
| 0 [1] | — | 48 | 0 | — | — | — | 24 |
| 1 [5] | — | 224/3 | 32/3 | — | 0, 40 | 16 | 8/3, 128/3 |
| 2 [14] | **−16/3** | 320/3 | 80/3 | 80/3 | 8, 64 | 32 | 32/3, 200/3 |
| 3 [30] | 0 | 144 | 48 | 48 | 64/3, 280/3 | 160/3 | 24, 96 |
| 4 [55] | 32/3 | 560/3 | 224/3 | 224/3 | 40, 128 | 80 | 128/3, 392/3 |
| 5 [91] | 80/3 | 704/3 | 320/3 | 320/3 | 64, 168 | 112 | 200/3, 512/3 |
| 6 [140] | 48 | 288 | 144 | 144 | 280/3, 640/3 | 448/3 | 96, 216 |

Plus the Σ-graviton sector: 0 (Teichmüller), 8 (Σ breathing), 8 (harmonic-1-form vectors).

## 3. BF verdict as a function of λ₁(Σ₂)
Conversion: λ_phys = 4k²·λ̂.
- **B1 (REFUTED, by counterexample S1).** "(D) is perturbatively BF-stable."
- **B2 (PROVED).** The instability holds for every N, g and Γ, including finite-area cusped and orbifold quotients, because the constant mode always exists. No condition on λ₁ restores stability. The moduli condition λ̂₁ ≥ 1/3 only removes the *extra* unstable 14-plets.
- **B3 (CONDITIONAL on the cited λ₁ values, not recomputed).**
  - Bolza λ̂₁ ≈ 3.83889 (Strohmaier–Uski), and the Kravchuk–Mazáč–Pal genus-2 maximum is ≈ 3.83890 (2111.12716).
  - So m²L₅² ≈ +10.022 for the first excited 14-plet.
  - Bolza and its neighbourhood therefore have exactly 14 BF-violating scalars, all Σ-constant.
- **B4 (CONDITIONAL; Schoen–Wolpert–Yau/Buser).** Near the boundary of moduli space λ̂₁ → 0, which adds one more unstable 14-plet per eigenvalue below 1/3.
- **B5 (OPEN).** How many genus-2 eigenvalues lie in (0, 1/3) as the moduli vary. Otal–Rosas λ̂₂ > 1/4 (cited by MR2, not fetched) leaves the window (1/4, 1/3) undecided.
- **B6 (OPEN).** The nonlinear endpoint of the 14 instability, i.e. which direction of T_ij the vacuum rolls along, and whether another vacuum exists.

## 4. PP's "probe instability √6/2 > 1"
- **Q1 (PROVED). What it is.** It is the ratio of WZ charge to DBI tension of a **probe M5 brane** on ℝ^{1,3}×Σ at a point of S⁴ and fixed y: a domain wall in AdS₅ across which N changes by one.
  - With dC₆ = *G, C₆ = (q₀/4k)e^{−4ky}d⁴x∧vol_Σ, so charge/tension = q₀/(4k) = (3/2)(L₅/L₇) = √6/2.
  - Calibration: the same computation on AdS₇×S⁴ gives 1 (BPS, no force).
- **Q2 (PROVED). Not a KK mode and not a truncation artifact.** It is a property of an extended object, independent of any truncation of the supergravity fields. The 2-modulus truncation's masses (48, 8) are correct (S4). What the truncation missed is the perturbative 14 (S1), which is a separate instability.
- **Q3 (CONDITIONAL; probe level).** Charge > tension makes the wall energy ∝ (1 − √6/2)e^{−4ky}·Area(Σ) unbounded below toward the boundary. That is a non-perturbative brane-nucleation channel (Brown–Teitelboim / Maldacena–Michelson–Strominger hep-th/9812073 / Seiberg–Witten hep-th/9903224 / brane-jet 2003.02851).
  - The conditions are: probe limit (N ≫ 1), the T₅ calibration, and leading order in ℓ_p/ρ ((ℓ_p/ρ)² = 2.4×10⁻³), with backreaction not computed.
  - This is non-perturbative for the vacuum, distinct from the perturbative BF tachyon in S1.
- **Q4 (PROVED). How the two relate.** Both are AdS₇×S⁴ data rescaled by L₅/L₇ = √(2/3):
  - BF side: −8 → −8·(2/3) = −16/3 < −4.
  - Wall side: 1 → 1·√(3/2) > 1.
  - Either one alone makes (D) unstable. S1 is the stronger statement, because it is perturbative and needs no probe approximation.

## 5. Numbers at N = 4880, g = 2 (standard (2πℓ_p)³N). CONDITIONAL on the Owner's chosen inputs.
- k = 0.0246505002 ℓ_p⁻¹, L₅ = 40.5671282, L₇ = 49.6843822, r = 24.8421911 = (πN)^{1/3}, ρ = 20.2835641 (all in ℓ_p). Area(Σ₂) = 5170.09355 ℓ_p².
- All m²L₅² values are pure numbers, independent of N.
- Lowest value per sector:
  - coupled scalars: −16/3 (UNSTABLE)
  - Σ-graviton scalars: 0 (Teichmüller)
  - Wilson lines: 0
  - S⁴-TT: 80/3
  - Σ breathing: 8
  - S⁴ breathing: 48
- The threshold is λ_phys ≥ 8.10196×10⁻⁴ ℓ_p⁻²; Bolza has λ_phys = 9.33076×10⁻³ ℓ_p⁻².

## 6. Cross-check of MR2 (7824e789… and its .py/.log)
- **M1 (PROVED). MR2's −16/3 is confirmed** by an independent script and an independent route (S1b, 7D potential), with the same field (the 14, coupled trace/flux, lower branch ℓ = 2), the same radius relation (L₅² = (2/3)L₇², L₇ = 2r) and the same shift (+4λ̂). Threshold λ̂ < 1/3 and the Bolza values (+10.0222157, KMP +10.0222573) agree to all printed digits. So do k, L₅, L₇, r, ρ and the area.
- **M2 (REFUTED, by counterexample).** MR2 §3: "Otal–Rosas … gives m²L² ≥ −13/3 for that one". For λ̂₁ ≤ 1/4, m²L₅² = −16/3 + 4λ̂₁ ≤ −13/3; for example λ̂₁ → 0 gives −16/3. The correct statement is: the first excited 14-plet has m² ≤ −13/3 if λ̂₁ ≤ 1/4, and all later ones have m² > −13/3. This does not affect MR2's verdict.
- **M3.** MR2's S11 (vectors, forms, S⁴-TT, Σ components of massive fields, OPEN there) is filled here as S6–S7, CONDITIONAL on L1. MR2's S6 (Teichmüller, CONDITIONAL) is PROVED here as S5.
- **M4.** I agree with MR2 that (D) = KR (vi) untwisted product, and that Maldacena–Núñez, Gaiotto–Maldacena and BBBW results are comparison only; none is used here.

## 7. For MR2 / PP cross-check: assumptions and literature formulas
- A1. Σ₂ is a compact hyperbolic surface with K = −4k², so λ₀ = 0 is simple, λ_j ≥ 0, and λ₁ > 0 depends on the moduli.
- A2. Two-derivative 11D sugra, with R_MN = (1/12)(GG − (1/12)gG²) and d*G = ½G∧G (CS sign convention).
- A3. Lemma L1 (DFGHM on Einstein X₇): CONDITIONAL, sketch in §1.
- A4. Sphere spectra used:
  - S⁴ scalars ℓ(ℓ+3); coexact 1-forms κ = (ℓ+1)(ℓ+2); coexact 2-forms (ℓ+1)(ℓ+2); TT tensors ℓ(ℓ+3) − 2 (ℓ ≥ 2) (standard; Rubin–Ordóñez).
  - On Σ: TT tensors = holomorphic quadratic differentials (dim 6g−6), with Δ_L = 2K on them.
- Literature formulas:
  - DFGHM hep-th/0105047: eqs. (4.3)/(4.7) scalars, (5.1)/(5.2) vectors, (6.3) spin-2, (7.5) forms, (7.9)–(7.12) CS 3-forms, (8.1)/(8.3) internal TT, (3.1) BF.
  - (5.2) as printed is garbled in the PDF text. I used the form derived from matrix (5.1): m²L² = ((p−1)²/(q−1)²)[κ + ((q−1)²/(p−1))(1 ± √(1 + 2(p−1)(D−2)κ/(q−1)³))], which gives 0 for Killing modes.
  - 7D SO(5) gauged sugra scalar sector: V = (g²/2)(2TrT² − (TrT)²), kinetic −¼Tr(T⁻¹∂T)² (Pernici–Pilch–van Nieuwenhuizen; Nastase–Vaman–van Nieuwenhuizen hep-th/9905075, hep-th/9911238). The normalization is cross-checked against the protected Δ = 4.
  - Kehagias–Russo hep-th/0003281 eqs. (13)–(14). Their p.3–4 says stability "needs a case-by-case study"; S1 answers that: unstable.
  - λ₁ anchors: Strohmaier–Uski 1110.2150 (Bolza 3.8388872588); Kravchuk–Mazáč–Pal 2111.12716 (≤ 3.8388976481); Otal–Rosas (Duke 2009); Schoen–Wolpert–Yau / Buser (small eigenvalues). All are as cited by MR2/parent and not re-fetched by NL.
  - Probe: PP 4660b73e C4; hep-th/9812073, hep-th/9903224, 2003.02851.

## Label tally
PROVED 12 (V1, V2, L2, S1, S2, S4, S5, B2, Q1, Q2, Q4, M1) · CONDITIONAL 9 (L1, S3, S6, S7, S8, B3, B4, Q3, §5 numerics) · OPEN 4 (V3, S9, B5, B6) · REFUTED 2 (B1, by counterexample S1; M2, by counterexample).

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after writing).
