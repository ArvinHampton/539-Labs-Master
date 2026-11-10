# FINDINGS: PP audit of O4 KK/BF on (D) = AdS₅×S⁴×Σ₂: MR2 7824e789, NL ceb85ec3 and MR2 cross-check/errata 3d943367. 2026-11-09 16:02 CST (America/Chicago)
Agent: Professor Proof (Soft SF), audit under GO (2). Authority: OW 5a6e7177 (blueprint, verified) and the Owner KK compute go-ahead (t4294u, 15:13 CST, as recorded by MR2/NL; record OWNER_WRITE_MAINCHAT_t4294_SIDECAR_KK_OPS_VERIF_P5a_2026-11-09_1515.md).
Limits: additive new file; nothing edited. Tip 7cddb188 untouched (re-hashed 16:02: MATCH). No CERT. Nothing sent outside (public arXiv PDF hep-th/0105047 read, sha256 777e6e75…). No Gemini. LOCK 96f8d42e §4 (four-force projection) not used.
Written under time pressure (Owner live call); unfinished items are marked PENDING or OPEN.
Scratch: /workspace/audit-scratch/pp_mr2_kk_bf_1528/
- mr2_kk.py: re-run copy of MR2's script; its log is in the same folder
- nlrun/: re-run copy of NL's script
- pp_kk_direct3.py (5442921…), cond.pkl (1bdfb7fe…), pp_kk_solve.py (a108e526…), pp_kk_solve.log (df747ae6…)
Companion: FINDINGS_PP_AUDIT_MR2_ADS5S4SIGMA2_PHI_V35_MAP_2026-11-09_1530.md (2b0a4125…), O1.

## Verdict (one line)
**(D) is perturbatively unstable for every N, every genus g ≥ 2 and every finite-area Γ.** The cause is the 14 of SO(5) at S⁴ level ℓ = 2, constant on Σ, with m²L₅² = −16/3 < −4 (the BF bound). There is also an independent non-perturbative channel: a probe M5 wall with charge/tension √6/2 > 1.

## Rollup
PROVED 11 · CONDITIONAL 9 · OPEN 4 · PENDING 2 · REFUTED 2.

## 0. Integrity
- **H1 (PROVED).** Each sha256 below was recomputed and equals its sidecar:
  - MR2 .md 7824e789316a169dc11eae4d684465e96b4b305cff02e568c43066fea106e8b8
  - MR2 .py ee8b8c90075367aa0028c1220c96b6bf8dfce5f7a073ed69d01f389889b83abf
  - MR2 .log 19ca28bae4635fea0f67909f8eddcaad1a13cfe635ab934a9dd3f7cf87cec882
  - NL ceb85ec369bb098c7820be62a41cc9b7077f786e7fa9c33af0dfbebd86804264
  - MR2 cross-check 3d94336786ad76ea3785b437917e6894dd14f9cb1cf9f833e183d981800bd741
- **H2 (PROVED).** Both scripts were re-run as copies in PP scratch, since each writes its log next to itself; no project file was touched.
  - MR2's re-run log is byte-identical to the original (19ca28ba…).
  - NL's /workspace/nl-kk-1513/nl_kk_o4.py (65d6a787…) re-run log is byte-identical to nl_kk_o4.log (9f581aa6…).
  - So MR2's claim C2 ("NL re-run identical") is confirmed.

## 1. The unstable 14 (S⁴ level ℓ = 2)
- **K1 (PROVED, arithmetic).**
  - Ric(AdS₅) = Ric(Σ) = −4k² (O1 audit, PP D1: computed from the metric). So X₇ = AdS₅×Σ is Einstein, with Ric = −6/L₇² ⇒ L₇² = 3/(2k²), while L₅² = 1/k². Hence (L₅/L₇)² = 2/3.
  - Also L₇ = 2r.
  - (−8)·(2/3) = −16/3, and the 5D BF bound is −4 (d = 4). In L₇ units the 5D bound is −6, which is stricter than the 7D bound −9.
- **K2 (CONDITIONAL, citation; PDF read).** DFGHM eq. (4.7) with p = 7, q = 4, ℓ = 2, minus branch, gives M²L₇² = (36/9)·2·(2−3) = −8.
  - Hypotheses as printed: the background (2.4)–(2.9) is AdS_p × Einstein M_q with Freund–Rubin flux on M_q.
  - The coupled-scalar system (3.31)–(3.33) → (4.1)–(4.2) uses only □ₓ, the internal harmonics and the Einstein constants. The text after (3.42) says the properties of M_q enter only through q and R.
  - AdS maximal symmetry is used only in the BF bound (3.1). That bound must now be the 5D one, because spacetime is AdS₅, not AdS₇.
- **K3 (CONDITIONAL, citation). Second route via 7D SO(5) gauged sugra (NL S1b; MR2 C3), with V = (g²/2)(2TrT² − (TrT)²) and kinetic −¼Tr(T⁻¹∂T)².**
  - PP re-did the expansion. At T = e^{φ}, Σφ = 0: V = −15g²/2 − (g²/2)Σφᵢ² + O(φ³).
  - Kinetic −¼(∂φ)². With φ = √2χ this gives M² = −2g².
  - For L = R − V in 7D, Ric = (V₀/5)g ⇒ L₇² = 4/g². Hence M²L₇² = −8 (PROVED given the Lagrangian).
  - The Lagrangian (PPvN) and the consistent truncation (NVvN) are citations, so K3 is CONDITIONAL. It does not use DFGHM or lemma L1, but it is not citation-free.
- **K4 (CONDITIONAL; independent PP 11D computation, numerical rank evidence; exact symbolic confirmation PENDING).** PP linearized the full 11D equations directly on the actual (D) geometry, without DFGHM or the 7D sugra:
  - Ansatz:
    - base metric perturbation (A ψ g + C ∇∇ψ)Y
    - S⁴ trace B ψ Y g_S⁴
    - flux δC₃ = β ψ ε·∇Y
  - Here Y = 5cos²θ − 1 is the ℓ = 2 harmonic (checked: □Y = −10Y/r²), and ψ = ψ(x⁰, y, v) depends on AdS₅ **and** H² coordinates, with □_{X₇}ψ = μψ. X₇ is not conformally flat, so Weyl terms are present.
  - All 11D Einstein and Maxwell components were sampled at 3 points, giving 51 linear conditions on (A, B, C, β).
  - A nontrivial solution exists only at μ = −16k²/3 and μ = +320k²/3: the smallest singular value is 5×10⁻¹⁶ and 2×10⁻¹⁶ there, against ≥ 0.6 at every other point of a 460-point grid on μ ∈ [−20, 133]k². These are exactly (2/3)×(−8, 160)/L₇²: the DFGHM ℓ = 2 minus and plus branches.
  - Because ψ carries Σ dependence through □_{X₇}, this also shows directly that the mode depends on X₇ only through □_{X₇}.
  - Not a gauge artefact: pure-gauge modes need h_μα ≠ 0 or traceless h_(αβ) ≠ 0, which the ansatz excludes. δ(F²) (gauge-invariant, since F̄² is constant) is ∝ (B, β)-linear and nonzero.
  - PENDING: exact nullspace (sympy radical simplification did not finish) and the closed-form mode vector.
- **K5 (PROVED, given K1 plus any one of K2/K3/K4). The Σ-constant copy.**
  - It exists on every compact or finite-area H²/Γ.
  - □₇ = □₅ on it, so m²L₅² = −16/3: 14 real modes, Δ = 2 ± 2i/√3. The value is independent of N (masses are k-ratios) and of g and Γ.
- **K6 (PROVED, normalization). Σ-harmonic copies.**
  - Physical Σ metric ρ²ĝ with K̂ = −1, ρ = 1/(2k). So λ_phys = λ̂/ρ² = 4k²λ̂, and λ_phys L₅² = 4λ̂.
  - Hence m²L₅² = −16/3 + 4λ̂. A copy violates BF iff λ̂ < 1/3, i.e. λ_phys < 4k²/3 = 8.10196×10⁻⁴ ℓ_p⁻² at N = 4880.
- **K7 (CONDITIONAL, citation).**
  - Bolza λ̂₁ ≈ 3.8388872588 (Strohmaier–Uski, curvature −1) gives m²L₅² ≈ +10.0222. The Kravchuk–Mazáč–Pal bound 3.8388976481 gives +10.0223.
  - So on Bolza and nearby surfaces exactly 14 modes (the Σ-constant ones) violate BF.
  - Role: Bolza only fixes the count of *extra* unstable copies. It cannot remove the constant-mode instability.
  - Near degeneration λ̂₁ → 0 (Schoen–Wolpert–Yau/Buser): more unstable copies. CONDITIONAL.
- **K8 (CONDITIONAL, citation).** BF violation implies linear instability (normalizable modes growing in global time): Breitenlohner–Freedman 1982, as used in DFGHM §3.1.

## 2. Lemma L1 (DFGHM with AdS₇ replaced by any Einstein space)
- **L1-scalar (CONDITIONAL on DFGHM text; numerically corroborated by K4).** For the coupled π/b/H sector, the linearized Ricci of pure-trace and Hessian base perturbations involves only □ₓ and Ric(X). Two identities hold on any Einstein X:
  - R⁽¹⁾(g f) contains no Riemann tensor;
  - Δ_L∇∇f = ∇∇□f.
  - So Weyl(X) does not enter. K4 confirms this on the actual non-conformally-flat X₇. MR2's "PROVED" for this sector: PP accepts it as CONDITIONAL (structural argument plus citation) pending the K4 exact nullspace; it is upgraded to PROVED once K4 is exact.
- **L1-S⁴-TT and forms (CONDITIONAL).** The S⁴-TT operator (3.40) uses only the S⁴ Riemann tensor plus □ₓ, and the form operators are Hodge/Maxwell on X, which split on the product. This is structurally correct per DFGHM's remark after (3.42). PP did not verify it component by component, so MR2's PROVED is downgraded to CONDITIONAL.
- **L1-vectors (CONDITIONAL).** Rests on NL's reconstruction of the garbled printed (5.2); not re-derived by PP.
- **L1-spin-2 (CONDITIONAL).** Arithmetic checked:
  - Δ_L(φ g_Σ) = −□φ g_Σ, because the Riemann and Ricci terms cancel when K_Σ = Λ_R.
  - Shift −2Λ_R = +8k² gives +8 in L₅ units; mixed harmonic-1-form shift −K − Λ_R = +8k² gives +8; AdS₅-TT and Σ-TT shifts are 0.
  - MR2's shifts (0, 0, +8, +8) are confirmed as arithmetic. The Fierz–Pauli constraint solution (a, c) was not re-derived.
- Not REFUTED in any sector. The headline does not depend on the vector or spin-2 sectors.

## 3. √6/2 nucleation channel (settles PP 4660b73e C4)
- **W1 (PROVED, arithmetic).** A probe M5 on ℝ^{1,3}×Σ at a point of S⁴ and fixed Poincaré y is a codimension-1 wall in AdS₅ wrapping Σ.
  - charge/tension = q₀/(4k) = √6/2 = (3/2)(L₅/L₇) = √(6/d) at d = 4.
  - The AdS₇×S⁴ calibration gives 1.
  - MR2's and NL's forms agree.
- **W2 (CONDITIONAL; probe limit, no backreaction, T₅ fixed by the AdS₇ BPS calibration).** Ratio > 1 means the wall energy is ∝ (1 − √6/2)e^{−4ky}·Area(Σ), which is unbounded below toward the boundary. That is a Seiberg–Witten / MMS brane-nucleation instability: non-perturbative and independent of the KK analysis.
- It is not a KK mode, and PP's C3 (48, 8) is not contradicted: the 14 lies outside the 2-modulus truncation. NL's and MR2's reproductions of 48 and 8 match PP C3 (re-run logs).

## 4. MR2 errata (3d943367) and other items
- **E1 (PROVED).** For λ̂ ≤ 1/4: m²L₅² = −16/3 + 4λ̂ ≤ −13/3. MR2 7824e789 §3's "≥ −13/3" is REFUTED (counterexample λ̂ → 0 gives −16/3). NL M2 is right, and MR2's corrected text is right. The Otal–Rosas input is CONDITIONAL (not fetched).
- **E2 (CONDITIONAL).** MR2 upgrades the Teichmüller modes (m² = 0, 6g−6 = 6) to PROVED. PP accepts the arithmetic: on TT, Δ_L^Σ = 2K cancels −2Λ_R. The rest of the spin-2 structure is CONDITIONAL as in §2, so PP grades this CONDITIONAL.
- **E3.** MR2's S11 moves from OPEN to CONDITIONAL. Agreed, except S⁴-TT and forms, which are CONDITIONAL, not PROVED (§2).
- **E4.** MR2's tally bookkeeping: noted; no mathematical content.
- **KR (14) factor 16 (PROVED).** With Ω₄ the unit-S⁴ form, 6R₀³Ω₄ is 16 = (R₀/r)⁴ times the value from KR's own (4)/(5) with m₀ = 1/R₀, which is (3/8)R₀³Ω₄. This agrees with PP's O1 audit D2 (2b0a4125). It is immaterial to every mass.
- **MR2 7824e789 S1 label.** "PROVED [MR2-calc]" should read: PROVED arithmetic, CONDITIONAL on the cited DFGHM (4.7) or the 7D Lagrangian. PP's K4 numerics corroborate it independently.
- Numbers: k, L₅ = 40.567128, L₇ = 49.684382, r, ρ and Area match PP across the MR2 and NL logs (PROVED, re-run).

## 5. Open / pending
- PENDING: K4 exact symbolic nullspace and mode vector (this would make K5 PROVED without citations).
- PENDING: the K4 check at an ℓ = 3 harmonic (lower branch should be 0).
- OPEN: fermions (irrelevant to BF); the number of genus-2 eigenvalues in (1/4, 1/3) over moduli space; the nonlinear endpoint of the 14 instability; backreacted nucleation.

## 6. Verdict for the Owner's stability decision
(D) as adopted (OW 7708ec5d, CONDITIONAL proposal) is **perturbatively unstable**. The 14 Σ-constant scalars at m²L₅² = −16/3 violate the AdS₅ BF bound −4, for every N, every g ≥ 2 and every Γ; no choice of N, genus or modulus removes them.
- Status: CONDITIONAL on DFGHM (4.7) or the 7D sugra Lagrangian (two independent citations, both read or re-derived). It is independently corroborated by PP's direct 11D linearization on the actual geometry (numerical rank, exact form PENDING).
- It is also non-perturbatively unstable at probe level (√6/2 > 1, CONDITIONAL).
- Options:
  1. Accept (D) as unstable.
  2. Replace it with a supersymmetric twisted solution (MN N = 2 / N = 1 / BBBW). That needs a new Owner adoption; PP 4660b73e decision 4.

Tip 7cddb188 untouched. No CERT. Nothing sent outside. No Gemini.
