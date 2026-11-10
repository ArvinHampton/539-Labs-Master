# MR2: twisted SUSY vacua replacing (D) — geometry + literature compare (MN N=2, MN N=1, BBBW) at N = 4880, g = 2 — 2026-11-09 17:05 CST (America/Chicago)
Agent: MR2 (Math Research 2). Authority: OW OWNER_WRITE_MAINCHAT_VACUUM_REPLACE_D_TWISTED_SUSY_COMPARE_2026-11-09_1609.md (sha 822cecb27e974268175d5d88d6b0ab032fc7be1d85ea5f10321d9c24da128ca0, verified). **Nothing is adopted; this is for the Owner to choose.**
Limits: new additive files only; no existing file edited; tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 checked (MATCH). No CERT, no Gemini, nothing sent outside, no agent messages. Literature = public arXiv PDFs in /workspace/scratch/mr2_1109/ (pdftotext + rendered pages).
t4327 (ed526f70) is withdrawn (OW 5f59e33e5b49ed7f7a89b06f0ceff0b7bc7dc034c83d5c65a72bea176aa3a234, file re-hashed, matches sidecar; as reported by NL/PP): brane and face are UNDEFINED, junction items OPEN, no stance on DP-a or Layer2.

## Files (scripts frozen)
| file | sha256 | status |
|---|---|---|
| …_COMPARE_2026-11-09_V2.py | d6e9b1f10f79b6aefa2c6c3f579f53ffd526db165c0f55149948ad1cdeccbd10 | **current** |
| …_COMPARE_2026-11-09_V2.log | c15fa0bde7cdad945610223605dbd7a8ee9c380b82a04c27ddfea3d9da38d5ed | current (exit 0) |
| …_COMPARE_2026-11-09.py | 4562c8a1936a460b23999a2e4b0f5942886c53c98fee58ae185ad839b5051d4c | SUPERSEDED by V2 (frozen) |
| …_COMPARE_2026-11-09.log | 986adf547589e17395781d3d288e863c59cf48c7a174655c7958fab4fd26baea | output of 4562c8a1, SUPERSEDED |
| drafts 6d069d09 (NL 16:20), aa16d54e (PP 16:33) | not on disk (overwritten in place before freezing) | SUPERSEDED |
Inputs: NL 418e4e50e4ce791bfb7c00fe4916dcee7082027c38ed7c55fea82659c98838e6 (re-hashed, MATCH); PP audit FINDINGS_PP_AUDIT_TWISTED_SUSY_VACUA_COMPARE_2026-11-09_1638.md df503cd99df53b222b27f5d6a2dfbb1fb09dd9c7237630d72a7fff36a75ed494.
Literature (sha of PDF): 1112.5487 (0762c8b0…), 1203.0303 BBBW (473bfa98…), 0904.4466 GM (21445168…), hep-th/0007018 MN (770d87d8…), hep-th/9903214 CLP (cited, as in NL).

## 0. Response to PP audit df503cd9 (M1–M4)
- **M1 done.** .py frozen (4562c8a1 + its .log, sidecars); the fix is in the new V2 files.
- **M2 (§6) — bug found and fixed; not tuned.** Residual max|R^t_t + R| (units 1/ℓ²):

| case | aa16d54e (PP) | 4562c8a1 (float grid, poles in mpmath) | **V2 (all mpmath dps 60, 48 pts)** |
|---|---|---|---|
| VALID (D) product AdS₅×H²×S⁴, exact R = 6 | — | — | 3.5e-25 (R = 6.0 at all pts) |
| VALID-NEG product F0=G0=1 (expected residual exactly 22) | — | — | 22.0 |
| MN1 z=0 | 530 | 3.4e-7 | **4.3e-25** |
| MN2 z=1 | 237 | 2.1e-6 | **4.8e-25** |
| BBBW z=2 | 79 | 3.0e-6 | **4.4e-25** |
| BBBW z=3 | 447 | 9.2e-7 | **1.7e-25** |
| NEG-CONTROL z=2, X₁×1.1 | 498 | 1.36 | **1.36** (FAIL, as it must) |
  - Diagnosis: the coded metric and the symbolic Ricci routine are **unchanged** from aa16d54e to V2. The fault was numerical: aa16d54e evaluated the lambdified symbolic Ricci (rational functions with sin^{-k}α, sin^{-k}β) in float64 on a grid offset only 10⁻³ from the coordinate poles α = 0, π and β = 0, π/2. Catastrophic cancellation gave O(R) garbage there, for the control too. With the same expressions evaluated at 60 digits (points down to 10⁻⁶ from every pole), every true candidate passes at ~10⁻²⁵. The X₁×1.1 control fails at 1.36, and the wrong-radius product fails at exactly 22. The routine was first validated on the (D) product, where R = 6 = 4k² exactly with k² = 3/2 in S⁴-radius-½ units. (PROVED, own computation, V2.log §6a/6b.)
  - Scope: R^t_t = R^r_r = −R is the AdS₅-block (trace) part of the 11D Einstein equation with an internal G₄. It is necessary, not sufficient, so the full solution property stays CONDITIONAL (citations below).
- **M3** applied: every literature formula is CONDITIONAL with its arXiv equation; only own arithmetic and symbolic checks are PROVED.
- **M4** done: SUSY and EFT columns are filled for every candidate (§2, §5, §8).

## 1. Conventions and normalization
- **K1 (CONDITIONAL; project F1 f2e5120d, standard sugra).** S = (1/2κ²)∫(R − ½|G|²), 2κ² = (2π)⁸ℓ_p⁹, G₁₁ = 16π⁷ℓ_p⁹, ∫_{S⁴}G = (2πℓ_p)³N, G_MN = ½T^(EH)_MN. With R_MN = (1/12)(G·G)_MN − (1/144)g_MN G², the trace gives R = G²/144, so **Φ := G·G = 144 R** for any solution (PROVED, algebra).
- **K2 (PROVED, arithmetic; input MN fn. 5 R²_AdS7 = 4(πN)^{2/3}ℓ_p², CONDITIONAL).** Uplift units set R_AdS7 = 1 and the S⁴ radius to ½. The physical metric is ℓ²·(uplift metric) with ℓ = 2(πN)^{1/3}ℓ_p, i.e. ℓ³ = 8πNℓ_p³. Freund–Rubin check: (6/ℓ)(ℓ/2)⁴(8π²/3) = (2π)³N ℓ_p³ exactly (log §0). At N = 4880: ℓ = 49.6843822 ℓ_p, ℓ² = 2468.5378 ℓ_p².
- **K3 (PROVED, symbolic).** det h₄ = Δ sin⁶α sin²β cos²β/(X₀X₁²X₂²), with X₀X₁²X₂² = 1. So Δ^{-1/2}√h₄ is X-independent and J = ∫Δ^{-1/2}√h₄ = 8π²/3 for every X. Then a = (g−1)N³e^{3f₀+2g₀}J/π² reproduces BBBW (4.6) to all digits for all candidates (log §5). **Flux quantization:** the same ℓ that gives N units on round S⁴ reproduces BBBW's a(N), consistent with BBBW App. D (D.47)–(D.51). Label: CONDITIONAL on (D.47) (topological flux through the twisted S⁴ fibre not re-integrated here), PROVED as a normalization consistency check.

## 2. Per-candidate 11D data (uplift units; multiply the metric by ℓ², G₄ by ℓ³)
Common form — **CONDITIONAL: 1112.5487 eqs (8)–(9); 1203.0303 eqs (3.8), (4.1)–(4.4); CLP hep-th/9903214 §4 uplift**:
ds²₁₁ = Δ^{1/3}[e^{2f₀}(−dt² + dx⃗² + dr²)/r² + e^{2g₀}(dx² + dy²)/y²] + ¼Δ^{−2/3}[X₀^{−1}dμ₀² + Σᵢ Xᵢ^{−1}(dμᵢ² + μᵢ²(dφᵢ + aᵢ dx/y)²)],
with μ₀ = cos α, μ₁ = sin α cos β, μ₂ = sin α sin β, Δ = Σ X_a μ_a², X₀ = (X₁X₂)^{−2}, e^{f₀} = X₀^{−1}, e^{2g₀} = (X₁X₂/8)((1−z)X₁ + (1+z)X₂), a₁ = (1+z)/2, a₂ = (1−z)/2. The fixed point (κ = −1) is X₁⁵ = [1+7z+7z²+33z³ − (1+4z+19z²)√(1+3z²)]/(4z(1−z)²) and X₁/X₂ = (1+z)/(2z+√(1+3z²)).
G₄ — **CONDITIONAL, 1203.0303 eq (4.5)**: *₁₁F₄ = 4Σ_a(X_a²μ_a² − ΔX_a)ε₇ + 2ΔX₀ε₇ + ¼Σᵢ Xᵢ^{−2}d(μᵢ²)∧(dφᵢ + aᵢdx/y)∧*₇Fⁱ, with Fⁱ = aᵢ dx∧dy/y². The prefactor of the last term prints garbled in pdftotext; ¼ is MR2's **inference** from consistency with CLP (4.2) and the gauge-field rescaling, not a verified transcription (OPEN until checked on the rendered page). G₄ has no AdS₅ legs (CONDITIONAL). This is all §6 uses.

| quantity | MN1 (z=0) | MN2 (z=1) | BBBW z=2 | BBBW z=3 |
|---|---|---|---|---|
| X₁ | (3/4)^{1/5} = 0.9440875 | 2^{−3/5} = 0.6597540 | 0.5806736 | 0.5476001 |
| X₂ | = X₁ | 2^{2/5} = 1.3195079 | 1.4721143 | 1.5458070 |
| X₀ | 1.2587833 | 2^{2/5} (= X₂, SO(3)) | 1.3685252 | 1.3956047 |
| e^{f₀} | 0.7944179 | 2^{−2/5} = 0.7578583 | 0.7307136 | 0.7165353 |
| e^{2g₀} | 0.2103666 | 2^{1/5}/4 = 0.2871746 | 0.4098498 | 0.5383668 |
| (p,q) | (1,1) | (2,0) [mirror (0,2)] | (3,−1) [mirror z=−2: (−1,3)] | (4,−2) |
| literature form | MN (28)–(29) | MN (26); GM (2.7) | BBBW (3.8)/(4.1)–(4.5) | same |
- **G1 (PROVED, sympy).** z → 0 gives X₁⁵ = 3/4 exactly. This reproduces MN (28): e^{5φ} = 4/3 with X₁ = e^{−φ}, X₀ = e^{4φ}, and e^{−2g−3φ} = 4 with e^{2g} = e^{2g₀}, e^{−3φ} = X₁³ (= 4.000…, log §2).
- **G2 (PROVED, sympy).** z → 1 (BBBW form 0/0) gives X₁ = 2^{−3/5}, X₂ = X₀ = 2^{2/5}. Then Δ_BBBW = 2^{−3/5}(1 + cos²θ) and Δ^{1/3}e^{2f₀} = ½Δ_MN^{1/3}, which reproduces the ½ds²(AdS₅) prefactor and the Δ_MN = 1 + cos²θ of MN (26).
- **G3 (PROVED, numerical).** All X_a > 0 and all metric functions are real for z = 0, 1, 2, 3, −2 (mirror = swap 1↔2, identical invariants).

## 3. Supersymmetry and R-symmetry
- **S1 MN2 (CONDITIONAL; MN hep-th/0007018 §4.1, text after (26): "SU(2)×U(1) isometries as required by N=2 superconformal invariance"; GM 0904.4466).** 4D N = 2 (8 Q), R-symmetry SU(2)_R × U(1)_r. Isometry SU(2) × U(1) (PROVED by inspection: X₀ = X₂ with a₂ = 0 gives SO(3) on (μ₀, μ₂ e^{iφ₂}), and U(1) on φ₁).
- **S2 MN1 (CONDITIONAL; MN §4.2; BBBW §2).** 4D N = 1 (4 Q), U(1)_R. Isometry U(2) = U(1)_R-mixing × SU(2)_F (PROVED by inspection: X₁ = X₂, a₁ = a₂ ⇒ U(2) on (μ₁e^{iφ₁}, μ₂e^{iφ₂}) ∈ ℂ²).
- **S3 BBBW |z| ≥ 2 (CONDITIONAL; BBBW (2.8), (2.17)).** 4D N = 1, U(1)_R = combination fixed by a-maximization, ε* = −0.434259 (z=2), −0.476834 (z=3). Isometry U(1)² (one R, one flavour). Field-theory duals for |z| > 1, g > 1 are **not known** (BBBW §7: "the biggest question we are left with is what to make of the CFT duals of the backgrounds with |z| > 1 and g > 1") — CONDITIONAL/OPEN on the CFT side.

## 4. Twist parameters at g = 2
- **T1 (CONDITIONAL; BBBW (2.12)–(2.13)).** p = (1+z)(g−1), q = (1−z)(g−1), p + q = 2g − 2, z = n/(g−1), n ∈ ℤ.
- **T2 (PROVED, arithmetic).** At g = 2, z = n ∈ ℤ, (p,q) = (1+n, 1−n): n = 0 → MN1 (1,1); n = ±1 → MN2 (2,0)/(0,2); |n| ≥ 2 → BBBW, e.g. (3,−1), (4,−2). There are no 0 < |z| < 1 points (BBBW's count g − 2 = 0). z ↔ −z is a mirror.
- **T3 (CONDITIONAL; BBBW L645 / §3 and L2114).** For κ = −1 the solutions are real for all properly quantized z and have no conical singularities. Large |z|: a ~ c ~ z (BBBW (4.9)); numerically e^{g₀}/e^{f₀} grows (0.577, 0.707, 0.876, 1.024 for z = 0, 1, 2, 3), so Σ becomes large relative to L₅. Sugra regime: no upper bound on |z| is stated in the literature; MR2 only checked z ≤ 3 (beyond that, OPEN).

## 5. Central charges at N = 4880, g = 2 (compare a_D = c_D = (8√6/81)N³ = 2.81151276×10¹⁰)
Formulas are CONDITIONAL: BBBW (4.6)/(4.7)=(2.22) large N; BBBW (2.6), (2.16)–(2.20) a-maximization for A_{N−1} (r = N−1, d = N²−1, h = N); GM 0904.4466 (2.5). Arithmetic is PROVED (log §3–4).

| candidate | a/N³ (large N) | a (exact) | c (exact) | a/a_D | c/a_D |
|---|---|---|---|---|---|
| MN1 | 9/32 | 3.26852635423125×10¹⁰ = 522964216677/16 | 3.2685263237375×10¹⁰ = 261482105899/8 | 1.16255078 | 1.16255077 |
| MN2 | 1/3 | 3.87380900564583×10¹⁰ = 929714161355/24 | 3.87380898531667×10¹⁰ = 232428539119/6 | 1.37783796 | 1.37783795 |
| BBBW z=2 | 0.4264175343 | 4.95558023204×10¹⁰ | 4.95558022803×10¹⁰ | 1.76260279 | 1.76260279 |
| BBBW z=3 | 0.5281529477 | 6.13789088706×10¹⁰ | 6.13789090019×10¹⁰ | 2.18312752 | 2.18312753 |
- **A1 (PROVED, sympy).** a-maximization gives MN2: ε* = −1/3, a = (N−1)(8N²+8N+5)/24 = (8N³−3N−5)/24, c = (N−1)(2N²+2N+1)/6 = (2N³−N−1)/6. This is **identical to GM (2.5)**, which verifies the requested formula a = (g−1)(8N³−3N−5)/24. MN1: ε* = 0, a = 3(N−1)(3N²+3N+2)/32, c = (N−1)(9N²+9N+4)/32. BBBW (2.20) closed form = a-max output (difference 0). All candidates satisfy the BBBW bound (2.23) ½ ≤ a/c ≤ 3/2. MN1/MN2 large-N ratio = 27/32.
- Note: (D) is non-SUSY with a_D = c_D only from its own holographic formula; ratios above compare like with like (holographic, leading order).

## 6. Curvature / EFT validity (V2 log §6; PROVED numerically on a 48-point grid incl. pole neighbourhoods, own code)
| candidate | R range (1/ℓ²) | ℓ_p²R_max | ℓ_p²Φ range | ℓ_p²√(R_MN R^MN)_max | L₅ = ℓe^{f₀} | Σ radius ℓe^{g₀} | Area(Σ) | e^{g₀}/e^{f₀} |
|---|---|---|---|---|---|---|---|---|
| (D) ref | 4k² const | 2.43e-3 | 0.350 const | — | 40.567 ℓ_p | 20.28 ℓ_p (=1/2k) | 5170.1 ℓ_p² | 0.5 |
| MN1 | [4.4026, 6.9993] | 2.84e-3 | [0.257, 0.408] | 1.32e-2 | 39.470 ℓ_p | 22.79 ℓ_p | 6525.7 ℓ_p² | 0.577 |
| MN2 | [5.2913, 12.000] | 4.86e-3 | [0.309, 0.700] | 2.33e-2 | 37.654 ℓ_p | 26.63 ℓ_p | 8908.3 ℓ_p² | 0.707 |
| BBBW z=2 | [5.2059, 14.897] | 6.03e-3 | [0.304, 0.869] | 2.89e-2 | 36.305 ℓ_p | 31.81 ℓ_p | 12713.8 ℓ_p² | 0.876 |
| BBBW z=3 | [5.2356, 16.481] | 6.68e-3 | [0.305, 0.961] | 3.19e-2 | 35.601 ℓ_p | 36.46 ℓ_p | 16700.4 ℓ_p² | 1.024 |
- **E1 (PROVED, numerical).** At N = 4880 every candidate has ℓ_p²R ≤ 6.7×10⁻³ and ℓ_p²|Ric| ≤ 3.2×10⁻² everywhere sampled, including within 10⁻⁶ of the poles of the S⁴ fibre. All invariants are finite there and no singularity is seen. All curvatures scale as ℓ^{−2} ∝ N^{−2/3} (PROVED, scaling). So ℓ_p²R ≪ 1 holds, with higher-derivative (R⁴) corrections ~ (ℓ_p/ℓ)⁶ ~ 10⁻¹⁰ relative.
- **E2 (CONDITIONAL; MN "completely smooth"; BBBW L2114 no conical singularities).** Global smoothness. MR2's grid is consistent with this but is a sample.
- **E3 (OPEN).** The full Riemann/Kretschmann invariant was not computed (only R and R_MN R^MN). The systole of the chosen hyperbolic Σ₂ (a modulus not fixed by sugra) controls light wrapped-brane states, and ℓ·e^{g₀}·sys(Σ) ≫ ℓ_p is needed. It depends on the Owner's choice of Γ (OPEN).
- **E4 (PROVED).** No scale separation: Σ and S⁴ radii are O(L₅) for all candidates (ratio 0.58–1.02), as in (D).

## 7. What carries over from (D)
- **Φ (PROVED from K1 + §6).** Φ = G·G = 144R is now **position-dependent** on the S⁴ fibre (ranges in §6; (D) had the constant ℓ_p²Φ = 0.350). Φ is r- and Σ-independent (residual ≤ 10⁻⁵⁸), so Φ = Φ(α, β) only. For MN2, Φ_max = 144·12/ℓ² exactly (numerically 12.000000), at the SO(3)-fixed locus.
- **W₃₅ = Λ⁴T*M₇ (PROVED, linear algebra).** M₇ = ℝ_r × (S⁴ ↪ M₆ → Σ₂) is no longer a product but a twisted S⁴ bundle. The Ehresmann connection Aⁱ = aᵢdx/y splits TM₇ = ℝ ⊕ H(≅π*TΣ) ⊕ V (rank 1+2+4), so the bidegree split 35 = 1+4+8+6+12+4 survives as a **bundle** decomposition. The refinement 1+4+8+3+3+6+6+4 (Λ²V = Λ²₊ ⊕ Λ²₋) also survives, since V is oriented with a metric. The splitting now depends on the connection (twist), not just on the slicing. Slicing dependence stays OPEN (as before).
- **b₃ (PROVED, Leray–Serre).** For an oriented S⁴ bundle M₆ → Σ₂, E₂^{p,q} = H^p(Σ)⊗H^q(S⁴) with q ∈ {0, 4} has no total degree 3. So b₃(M₆) = 0, as for the product. The earlier no-torsion-free-G₂ rank argument used the product structure; for the twisted case it is OPEN.
- **EH relations (CONDITIONAL; F1 f2e5120d, OW 2d1e877e).** G = ½T^(EH) is the standard 11D Einstein equation, which these candidates solve (CONDITIONAL on S/T citations). P_rev = T1 has no bulk map (no conflict at the level of definitions; R-symmetry interplay OPEN, as in NL C5).
- **Junction, brane/face, V₇eff, G₅ downstream: OPEN** (on hold per OW 822cecb2; brane/face UNDEFINED per OW 5f59e33e as NL/PP-reported; no stance on DP-a/Layer2).

## 8. Cross-check against NL 418e4e50 (log §7)
- **X1 (PROVED).** NL's a_D = πL₅³/(8G₅) = 0.24192492 N³ equals MR2's (8/81)√6 = 0.24192491 N³ (difference from NL's 8-digit input rounding).
- **X2 (PROVED).** With a = πL₅³/(8G₅): G₅/G₅(D) = (L₅/L₅,D)³·(a_D/a). Using MR2's L₅ = ℓe^{f₀} and a:

| candidate | MR2 L₅ [ℓ_p] (NL) | MR2 G₅ [ℓ_p³] (NL) | MR2 G₅/G₅(D) (NL) | a_D/a | Area(Σ) MR2 (NL) |
|---|---|---|---|---|---|
| MN2 | 37.6537206 (37.653721) | 5.41185e-7 (5.4118e-7) | 0.58037 (0.5804) | 0.725775 | 8908.317 (8908.32) |
| MN1 | 39.4701616 (39.470162) | 7.38779e-7 (7.3878e-7) | 0.79227 (0.7923) | 0.860177 | 6525.690 (6525.69) |
| BBBW z=2 | 36.3050537 (36.305054) | 3.79199e-7 (3.7920e-7) | 0.40665 (0.4067) | 0.567343 | 12713.77 (12713.77) |
| BBBW z=3 | 35.6006119 (35.600612) | 2.88678e-7 (2.8868e-7) | 0.30958 (0.3096) | 0.458058 | 16700.44 (16700.44) |
- **X3 — discrepancy in the brief, not in NL.** The brief quoted "3.79e-7 / 2.89e-7" as BBBW G₅ *ratios*. These are NL's **G₅ values** in ℓ_p³. The ratios are 0.4067 / 0.3096 (NL §6 table, confirmed). No numerical disagreement with NL was found. G₅ and L₅ are 7D-frame quantities; only a is frame-invariant (agree with NL D1, PP A3). NL's remark that Area = 2 × BBBW e^{2g₀} is a unit convention. MR2's Area = ℓ²e^{2g₀}·4π(g−1) reproduces NL's numbers exactly.
- **X4 (agree).** The NL and PP fixed-point values, (X₁X₂)²(X₁+X₂) = 3/2 (MR2 X's give the same), and 27/32 all match.

## 9. arXiv ID checks (abstract pages fetched 2026-11-09 ~16:45 CST, arxiv.org/abs + citation meta)
| ID | title / authors | NL use | verdict |
|---|---|---|---|
| hep-th/0003286 | "Consistent Kaluza-Klein Sphere Reductions", M. Cvetič, H. Lü, C.N. Pope (PRD 62, 064028) | T2: U(1)² truncation consistent + 11D uplift | **Partial match.** A real paper on consistent sphere reductions; it lists the S⁴ reduction of D=11 among the consistent cases (citing Nastase–Vaman–van Nieuwenhuizen). Its explicit U(1)² ansatz is for S³ (§4.2), not S⁴. The 11D S⁴ U(1)² uplift is in hep-th/9903214 (Cvetič, Duff, Hoxha, Liu, Lü, Lu, Martinez-Acosta, Pope, Sati, Tran), which NL also cites. Suggest citing 9903214 (+ hep-th/9905075) as the primary source. |
| 1911.12640 | "Kaluza-Klein Spectrometry for Supergravity", E. Malek, H. Samtleben (PRL 124, 101601) | B6: ExFT KK spectrometry | **Match.** |
| 2009.12051 | "Adjoint Reidemeister torsions of two-bridge knots", S. Yoon (Proc. AMS) | B6: Malek–Samtleben long paper | **Mismatch — REFUTED** ("2009.12051 is Malek–Samtleben" is false). The intended paper is arXiv:**2009.03347**, "Kaluza-Klein Spectrometry from Exceptional Field Theory", E. Malek, H. Samtleben (PRD 102, 106016), verified on arxiv.org. |

## 10. Joint comparison table (MR2 columns; NL columns in the JOINT_ file)
| candidate | metric/G₄ | SUSY / R | twist g=2 | a ; c (N=4880) | /a_D | EFT (ℓ_p²R_max; Σ/L₅) | Φ / W₃₅ | junction |
|---|---|---|---|---|---|---|---|---|
| MN2 | MN (26), BBBW (4.5) — CONDITIONAL; §6 PASS 4.8e-25 PROVED | N=2, SU(2)_R×U(1)_r — CONDITIONAL | z=±1, (2,0) — PROVED | 3.87381e10 ; 3.87381e10 — PROVED (arith.) | 1.3778 — PROVED | 4.86e-3; 0.707 — PROVED | Φ∈[0.309,0.700]/ℓ_p²; W₃₅ bundle split — PROVED | OPEN |
| MN1 | MN (28)–(29) — CONDITIONAL; §6 PASS 4.3e-25 | N=1, U(1)_R (+SU(2)_F) — CONDITIONAL | z=0, (1,1) — PROVED | 3.26853e10 ; 3.26853e10 — PROVED | 1.1626 — PROVED | 2.84e-3; 0.577 — PROVED | Φ∈[0.257,0.408] — PROVED | OPEN |
| BBBW z=2 | 1203.0303 (3.8),(4.1)–(4.5) — CONDITIONAL; §6 PASS 4.4e-25 | N=1, U(1)_R (+U(1)_F) — CONDITIONAL; CFT dual unknown | (3,−1) — PROVED | 4.95558e10 ; 4.95558e10 — PROVED | 1.7626 — PROVED | 6.03e-3; 0.876 — PROVED | Φ∈[0.304,0.869] — PROVED | OPEN |
| BBBW z=3 | same — CONDITIONAL; §6 PASS 1.7e-25 | same — CONDITIONAL | (4,−2) — PROVED | 6.13789e10 ; 6.13789e10 — PROVED | 2.1831 — PROVED | 6.68e-3; 1.024 — PROVED | Φ∈[0.305,0.961] — PROVED | OPEN |

## Label tally (items K1–K3, G1–G3, S1–S3, T1–T3, A1, E1–E4, Φ, W₃₅, b₃, G₂, EH, junction, X1–X4, arXiv ×3, §6 fix, G₄-coefficient)
PROVED 17 (K2, K3-check, G1, G2, G3, T2, A1, E1, E4, Φ, W₃₅, b₃, X1, X2, X4, §6-fix, arXiv 1911.12640 match) · CONDITIONAL 11 (K1, K3-flux, S1, S2, S3, T1, T3, E2, EH, hep-th/0003286 partial, solution property) · OPEN 5 (E3, G₂-twisted, junction/brane/face, |z|>3 regime, G₄ ¼ coefficient) · REFUTED 1 (2009.12051 attribution).
Nothing adopted. Tip 7cddb188… untouched (checked 17:02 CST).
