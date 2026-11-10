# MR2 cross-check of NL O4 KK spectrum + errata to MR2 7824e789. 2026-11-09, ~15:40 CST (America/Chicago)
Agent: MR2. Authority: Owner's own words, t4294u, 15:13 CST (Physicist transcript pos 17862), KK compute go-ahead.
Limits: this is a new additive file and nothing existing was edited. MR2 7824e789… is NOT overwritten; its errata are in §4 below. Tip 7cddb188… untouched (re-hashed). No CERT, no Gemini, nothing sent outside, no agent messaged.
Labels: every item carries exactly one of PROVED, CONDITIONAL (condition stated), OPEN or REFUTED. Steps marked [MR2-calc] are MR2 computations from cited formulas; PP audit is pending.

## Rollup
- NL's file verified. Its script was re-run and gives an identical log.
- The −16/3 instability is confirmed again.
- **Lemma L1 is assessed as follows:**
  - **PROVED** for the coupled-scalar, S⁴-TT and form sectors.
  - **CONDITIONAL** for the spin-2 and vector sectors. It holds there if L1 is read as "the X₇-covariant operators (□, Hodge, Lichnerowicz Δ_L), not AdS harmonic formulas". Under that reading, the AdS₅×H² Weyl tensor is handled explicitly and changes nothing NL tabulated.
  - Not REFUTED anywhere.
- **NL's slip report on MR2 §3 is correct.** Erratum E1 below.
- **NL's (3/2)(L₅/L₇) equals MR2's √(6/d) at d=4.** It is consistent and is not a KK mode.

## 1. Verification of NL's file and scripts (task 1)
- **C1 (PROVED).** sha256(NL_DERIVED_O4_KK_SPECTRUM_ADS5S4SIGMA2_BF_2026-11-09_1526.md) = ceb85ec369bb098c7820be62a41cc9b7077f786e7fa9c33af0dfbebd86804264. This equals the claimed value and the on-disk sidecar.
- **C2 (PROVED).** I copied `/workspace/nl-kk-1513/nl_kk_o4.py` to /tmp and re-ran it. The script writes its log beside itself, so NL's directory was not touched. The output is byte-identical to `nl_kk_o4.log`, exit 0.
- **C3 (PROVED).** NL's route S1(b) (7D SO(5) potential V = (g²/2)(2TrT² − (TrT)²), M²L₇² = −8) is independent of DFGHM and of L1. So the headline instability (14 modes, m²L₅² = −16/3, all N, g, Γ) does not rest on L1.
  - It agrees with MR2 7824e789 S1–S2: the same −16/3, the same threshold λ̂ < 1/3, the same Bolza/KMP values and the same k, L₅, L₇, r, ρ, Area.
- **C4 (PROVED).** NL's table entries were spot-checked against DFGHM (p=7, q=4) × (2/3):
  - coupled scalars: −16/3, 0, 32/3 for ℓ = 2, 3, 4
  - plus branch: 48, 224/3, …
  - spin-2: (2/3)·4ℓ(ℓ+3)
  - 2-forms: (2/3)·4(ℓ+1)(ℓ+2)
  - 3-form: (2/3)(2ℓ)² and (2/3)(2ℓ+6)²
  - vectors at ℓ=1: 0 and 40
  - All arithmetic matches.
  - NL's reconstruction of the garbled printed (5.2) is the one the matrix (5.1) gives, and it reproduces the 10 massless SO(5) vectors. I did not re-derive (5.2) independently, so that item is **CONDITIONAL**.
- **C5 (PROVED). Resolves NL V3, the KR flux convention.**
  - KR's field equations (2) and (4)–(5) give F_mnpq = 6m₀ε_mnpq, R_mn = 12m₀²g and R_μν = −6m₀²g. With q₀ = 6m₀ that is exactly (D): Ric(S⁴) = q₀²/3, Ric(X₇) = −q₀²/6.
  - KR's eq. (14), F̂₄ = 6R₀³Ω₄, differs from their own (4) by a factor of 16 if Ω₄ is the unit-S⁴ volume form. With S⁴ radius R₀/2 and m₀ = 1/R₀, (4) gives (3/8)R₀³Ω₄.
  - So (14) is a misprint or uses a different convention inside KR. It does not affect (D) or any mass.

## 2. Lemma L1: does DFGHM use maximal symmetry of the external AdS_p? (task 2)
DFGHM (hep-th/0105047 §3) fixes gauge only on the **internal** M_q: de Donder-type conditions (3.5)–(3.8) on internal indices. They expand in M_q harmonics and obtain equations covariant in the external space. AdS_p is invoked at the end (BF bound (3.1), and reading eigenvalues as masses). Below, sector by sector, is where external curvature enters. Throughout, X = X₇ = AdS₅×H²/Γ with Ric = Λ_R g and Λ_R = −4k². Each factor is maximally symmetric, and the mixed Riemann components vanish.

- **L1-a: coupled scalars (3.31)–(3.33) and (4.1)–(4.10). PROVED.**
  - These come from the internal Einstein equations (E3) and the internal form equation (F1). In a product background, δR_αβ involves the external space only through □ₓ acting on scalars; the external Riemann tensor does not enter.
  - The trace H is eliminated with (3.32), which is purely internal.
  - So M²L₇² = 4ℓ(ℓ−3) (minus branch, ℓ≥2) and 4(ℓ+3)(ℓ+6) (plus branch) hold for any Einstein X.
  - Separately, route S1(b) proves the ℓ=2 case without L1.
- **L1-b: S⁴-TT scalars (3.40)/(8.x). PROVED.** The operator is (□ₓ + □_y)δ − 2R_α^γ_β^δ, where the Riemann tensor is internal (S⁴). Only □ₓ on scalars touches X.
- **L1-c: forms (F2), (3.35), (3.41)–(3.42), (7.x). PROVED, for the 7D masses and the 5D reduction.**
  - The operators are Maxwell δd and the Hodge Laplacian on X, which are X-covariant. The CS 3-form equation is first order, *_X d.
  - On a product, the Hodge Laplacian splits exactly: Δ_H(ω_x ∧ η_Σ) = (Δ_H5 ω)∧η + ω∧Δ_HΣ η, and its Σ-eigenvalues are ≥ 0.
  - Examples: a 7D 2-form on harmonic vol_Σ gives a 5D scalar with m² = M², since δ(φ(x)vol_Σ) = 0. A 1-form on Σ gives a shift of μ ≥ 0.
  - So no Weyl tensor enters. 5D m² = (2/3)M²L₇² + (Σ Hodge eigenvalue ≥ 0).
- **L1-d: coupled vectors (3.34)–(3.37), (5.1)–(5.2). CONDITIONAL, on C4's (5.2) reconstruction.**
  - The E2 derivation commutes ∇^ν∇_μ on X, which brings in only Ric(X) = Λ_R g. Max is X-covariant.
  - The structure is X-safe. The only remaining condition is the printed-formula reconstruction, not curvature.
- **L1-e: spin-2 (3.38)–(3.39), (6.x). CONDITIONAL on reading (6.x) as the X-covariant equation (Δ_L^X − 2Λ_R + M²)H = 0, with M² the S⁴ eigenvalue shift. Not REFUTED.**
  - Here external curvature does enter. R⁽¹⁾_μν(H) = ½Δ_L H + …, and Δ_L^X contains Riem(X), including the nonzero Weyl tensor of AdS₅×H².
  - The scalar parts of H_μν decouple using ∇^μ∇_μ∇_νf = ∇_ν(□ + Λ_R)f and Δ_L∇∇f = ∇∇□f. Both hold on any Einstein space.
  - Massive Fierz–Pauli on an Einstein background is consistent.
  - So the 7D masses carry over. But the **5D numbers need Δ_L of AdS₅×H² decomposed explicitly; AdS₇ formulas cannot be used.** [MR2-calc] With mixed Riemann = 0 and K_Σ = Λ_R:
    - (i) AdS₅-block TT with Σ-constant mode: m² = M², so the 5D massless graviton is at M=0. ✓ NL.
    - (ii) Σ-TT (holomorphic quadratic differentials): Δ_L^Σ = 2K = 2Λ_R cancels −2Λ_R, so m² = M² (shift 0). Teichmüller modes are at 0 for M=0. ✓ NL.
    - (iii) Σ-trace piece H_ij = φg_ij, H_μν = aφg_μν + c∇_μ∇_νφ:
      - The Fierz–Pauli trace and transversality constraints solve to a = −2(Λ_R+m²)/(5Λ_R+4m²) and c = 2/(5Λ_R+4m²). This is regular, because 5Λ_R + 4m² = 0 would need M² = −3k² < 0.
      - Δ_L(φg) = −(□φ)g gives m² = M² − 2Λ_R = M² + 8k², i.e. m²L₅² = (2/3)M²L₇² + 8. ✓ NL "+8".
      - At M=0 it is gauge-dependent, but the Σ-breathing value 8 is independently PROVED (7D Einstein–Λ reduction, MR2 script §4 / NL §5).
    - (iv) Mixed h_μi = V_μ ω_i with ω harmonic:
      - (Δ_L h)_μi = −∇²h + 2Λ_R h, with ∇²_Σω = Kω (Weitzenböck).
      - The Proca identity ∇^νF_νμ = (∇² − Λ_R)V gives m² = M² − K − Λ_R = M² + 8k², i.e. +8. ✓ NL.
      - For coexact ω the shift is 8 + 4μ̂ ≥ 8.
    - All shifts are ≥ 0. NL's spin-2-derived entries stand.
  - Conclusion: L1 as literally worded ("DFGHM equations hold with AdS₇ replaced by any Einstein space") is **true for the 7D field equations**. The 5D masses of tensor pieces must be taken from Δ_L on the product, as in (i)–(iv), not from AdS₇ harmonic formulas. NL did exactly this.
  - Remaining condition: a component-by-component re-derivation of DFGHM (3.38)–(3.39) on non-maximally-symmetric X. MR2 did this only at the structural level above.
- **L1-f: low/special harmonics (ℓ = 0, 1; Killing and conformal Killing modes) and Σ-exact pieces. CONDITIONAL.** These are gauge or Stückelberg parts. DFGHM handle the internal special cases, and those are internal-only (S⁴). The X-side exact pieces combine into massive 5D vectors and spin-2. Not checked component by component.
- **L1-g: completeness. CONDITIONAL on L1-d,e,f.** No bosonic 5D mode other than the 14-plets (λ̂ < 1/3) violates BF. This agrees with NL S8. Fermions remain **OPEN** and are irrelevant to BF.

## 3. PP's √6/2 (task 4)
- **P1 (PROVED).** (3/2)(L₅/L₇) = (3/2)√(2/3) = √(3/2) = √6/2. MR2 7824e789 §5 gives charge/tension = q₀L_{d+1}/d = √(6/d) for AdS_{d+1}×H^{6−d}×S⁴; at d=4 that is NL's expression. The two forms are consistent.
- **P2 (PROVED).** It is a probe-M5 domain-wall WZ/DBI ratio, not a KK mode. MR2 §5 and NL Q1–Q2 agree.
- **P3 (CONDITIONAL; probe limit, no backreaction).** It describes a brane-nucleation channel. Both files say this.

## 4. Errata to MR2 7824e789 (7824e789316a169dc11eae4d684465e96b4b305cff02e568c43066fea106e8b8). The original is not modified.
- **E1 (task 3). The original statement is REFUTED; the corrected statement is PROVED.**
  - MR2 §3 says: "…at most one nonzero eigenvalue is ≤ 1/4 for g=2, which gives m²L² ≥ −13/3 for that one". That is wrong. For λ̂ ≤ 1/4, m²L² = −16/3 + 4λ̂ ≤ −13/3. NL M2 is correct.
  - Corrected text: "By Otal–Rosas (λ̂₂ > 1/4; cited, not fetched), at most one nonzero eigenvalue is ≤ 1/4 for g=2. If λ̂₁ ≤ 1/4, that 14-plet has −16/3 ≤ m²L² ≤ −13/3 (BF-violating). Every later 14-plet has m²L² > −13/3, and violates BF iff λ̂_j < 1/3."
  - The verdict is unchanged.
- **E2 (PROVED, via NL S5 and §2 L1-e(ii) here). The Teichmüller row S6 in MR2 §2 is upgraded from CONDITIONAL to PROVED**, with m² = 0, six real modes, at linear order.
- **E3. MR2 S11 (vectors, forms, S⁴-TT, Σ-components of massive fields): OPEN → CONDITIONAL, as in §2 here.** S⁴-TT and forms are PROVED (L1-b, L1-c); vectors, spin-2 and special modes are CONDITIONAL (L1-d, L1-e, L1-f). Fermions (S12) stay OPEN.
- **E4 (bookkeeping).** MR2's headline tally ("PROVED 9 · CONDITIONAL 7 · OPEN 6") was not reconciled line by line with its tables. The status table in MR2 §6, as amended by E1–E3, is authoritative.
- **E5 (PROVED).** MR2 §1 [P1] says DFGHM's scalar equations "involve the external space only through □ₓ and its Einstein constant". That is now checked: L1-a. No change is needed.

## 5. Status
| item | label |
|---|---|
| NL file sha ceb85ec3…; script re-run identical | PROVED |
| 14-plet m²L₅² = −16/3 (independent of L1) | PROVED |
| L1, scalar / S⁴-TT / form sectors | PROVED |
| L1, vectors (printed (5.2) reconstruction) | CONDITIONAL |
| L1, spin-2 (X-covariant Δ_L reading; 5D pieces 0, 0, +8, +8 derived here) | CONDITIONAL |
| L1, special and exact modes; completeness S8 | CONDITIONAL |
| L1 refuted anywhere | none found; not REFUTED |
| KR (14) factor-16 mismatch vs KR (4) | PROVED (immaterial) |
| √6/2 = (3/2)L₅/L₇ = √(6/d)|_{d=4}, probe not KK | PROVED |
| E1: original "≥ −13/3" | REFUTED; corrected statement PROVED |
| fermions; count of eigenvalues in (1/4, 1/3); nonlinear endpoint | OPEN |
