# MR2 · MN2 · KK Group A: lowest scalar and vector masses (CGR truncation, exact) and Group A projection
Written 2026-11-09, ~20:42 CST (box clock), by MR2 (executor). New additive file; no existing file edited. Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md re-hashed 7cddb188 (untouched). No CERT, no Gemini, nothing external, no messages sent.

**Authority.** OW d5eaeef3 ("Pursue all open") under OW 8b26c786 (Group A = Aut⁺(Bolza), order 48, × wall ℤ₂: a scope choice, not a result). OW t4431 "Lift the 90% stop" (record f700141d, verified by MR2): no usage stop. Nothing adopted; c2 not pursued; junction UNSOLVED; full KK spectrum OPEN. Usage: 80.4% at start (20:32 CST), 82.0% at end (20:41 CST).

**Naming.** Resonant algebra (RA-n) as in stages 1/2.

## Files (reports/)
| file | sha256 |
|---|---|
| MR2_MN2_KK_A_S4_SCALARS_VECTORS_COMPUTED_AUT48_2026-11-09.py | 88dadcf9cf76b84545806d8b0cb96a1497e9ce7878bf19e2a9686ac0e8b5ee6e (chmod a-w, sidecar written **before** any run) |
| MR2_MN2_KK_A_S4_SCALARS_VECTORS_COMPUTED_AUT48_2026-11-09.log | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 = **empty file** (see disclosure D1) |
| MR2_MN2_KK_A_S4_SCALARS_VECTORS_COMPUTED_AUT48_2026-11-09_RUN2.log | 82a3d9478376a1a5a941990b4aff3fbd96f1b00efd4d126c8b3113eea4902646 (the real log: exit 0, 6 s, 20:40:03 CST; .py sidecar re-verified OK immediately before) |
| this .md | see .md.sha256 |

**Disclosures.**
- **D1.** The first run (20:39:56) was wrapped in `/usr/bin/time`, which is not installed. The shell returned exit 127, the script never ran, and an empty `.log` was frozen with its sidecar before I noticed. Under the never-edit rule I did not overwrite or delete it. The real output is `_RUN2.log`, produced by the same frozen `.py` (sha 88dadcf9…).
- **D2.** A pre-freeze dry run in scratch (/workspace/mr2sv, not filed) used the wrong y-lift for x → (x+1)/(1−x): 2√2·y/(1−x)³ instead of 2√2·i·y/(1−x)³. It generated 96 matrices, including iI. The frozen .py now checks both lifts exactly on the curve (log [G]: g1, g2 pass; the draft lift fails). With the correct lift the order is 48, with GL(2,3) order statistics, matching ecee2668 §1.
- **D3.** Cosmetic log labels. In [N4] the second "falloff exponent" printed (−Δ) has no meaning and is not used. The second-order exponents are {4−Δ, Δ}... in the convention φ ~ r^{−(4−Δ)}, r^{−Δ}; only the statement "the 12 mode has 4−Δ = −2" is used below. In [Z1] the exponent text is a template; the value (0, 4) is what is used.

## Inputs (sha or source)
- KK file ecee2668 (MR2_MN2_KK_TRUNCATION_BOLZA_AUT48_ISOM96_WALL_Z2_2026-11-09.md): §1 group, §3 H¹ and Wilson lines, §6 wall parity and canonical lift, §7 controls.
- Stage 1 8ca7b93a, stage 2 7491cdb8, status bd32b4e2, V2 .py ad134752 (sha MATCH).
- **CGR** = Cheung–Gauntlett–Rosen, arXiv:1906.08900v2. I read the LaTeX e-print (gunzipped tex sha256 c8dac9034e617ff6…) for the exact formulas: (gfans), (3fans), (ellkin), (ellpot) for the N=4 7D→5D reduction on Σ₂; (afredfnrwo) for the N=2 SO(2)_D truncation; §6.1 for the vacuum and spectrum. The local /workspace/pp-audit-kk/cgr.txt is the same paper; its §6.1 lines 1201–1256 agree.
- **CGU** = Chen–Gutperle–Uhlemann, arXiv:1903.07109 (JHEP06(2019)139), §4 eqs (1.3), (4.3), (4.4): universal spin-2 operators [2,2]^{(2ℓ;±2n)}_{Δ=4+2ℓ+n} are Q²Q̄² descendants of A₂Ā₂ (n=0) multiplets with scalar primary [0,0]^{(2ℓ;0)}_{Δ=2+2ℓ}. Read from the arXiv abstract/ar5iv text; the multiplet identification is **not** independently re-derived (COND).
- PP inputs folded in: Z1 (FINDINGS_PP_AUDIT_MR2_CROSSCHECK_NL_BPS_1aa88a30_2026-11-09_2034.md) and S1 (PP audit of bd32b4e2), as relayed.

## RA-1. Vacuum and normalisation (log [N4], [N2]). PROVED (given CGR Lagrangian as stated premise)
- With L = R − K_ij∂x^i∂x^j − V and V = −(CGR potential): at l = −1, e^{30φ} = 2, e^{10λ} = 2, 𝒯 = 1, ψ = 0 the full N=4 gradient (13 scalar directions) vanishes exactly.
- V₀ = −3·2^{2/3}g², so L² = −12/V₀ gives **g²L² = 2^{4/3}**, exactly CGR (6.2).
- The N=2 truncation (Σ = 2^{−1/3}, Ω = 1, φ̃ = 0, z = 0) gives the same V₀ with zero gradient.

## RA-2. Scalar masses of the N=4 truncation (log [N4], [N2]). PROVED given CGR (ellkin)/(ellpot); identification with MN2 KK modes COND
Full exact Hessian over all 13 physical scalars (φ, λ, 𝒯 (5), ψ^{aα} (6)), using exact kinetic metric at the vacuum. The mass matrix is **block-diagonal** (all off-block entries exactly 0).

| sector | SU(2)_R × U(1)_r | m²L₅² | Δ | multiplet (CGR §6.1) |
|---|---|---|---|---|
| (φ,λ), direction δφ:δλ = 1:3 | 1₀ | **−4** | 2 | stress tensor A₂Ā₂ [0;0]_{Δ=2} |
| (φ,λ), direction δφ:δλ = **−3:1** | 1₀ | **12** | 6 | B₁B̄₁ [0;0]^{(4;0)} |
| 𝒯 (incl. w) | 5₀ | **0** (×5) | 4 | B₁B̄₁ primary |
| ψ^{aα} | 3_{±1} | **5** (×6) | 5 | B₁B̄₁ |

- **Controls reproduced:** −4 and +12 (= NL B1, ecee2668 §7); the 5-plet at 0 is now computed for all five components (it was COND in ecee2668 §7 with only one component); ψ at 5 matches CGR. The N=2 truncation independently gives {−4, 12, 0, 5, 5}.
- **Z1 control (PP): reproduced.** w is marginal: ∂²_wV = ∂_w∂_φV = ∂_w∂_λV = 0 at MN2 (no Hessian mixing), m²L² = 0, Δ = 4, second-order exponents {0, 4}. **∂³_wV|_{MN2} = −24·2^{2/3}g²**, ratio to PP's value exactly 1 (same V = −L_pot convention). PROVED (exact).
- **(−3:1) check (PP): reproduced.** The Δ = 6 (m²L² = 12) eigendirection is δφ:δλ = −3:1, with 4−Δ = −2. The Δ = 2 mode is the 1:3 direction. PROVED (exact).
- DOF check: 13 physical + 3 Stueckelberg ξ^α = 16 = 1 + 3·5 (N=4 gravity + 3 vector multiplets). PROVED (counting).

## RA-3. Vector masses (log [VEC]). PROVED given CGR; identification COND
- N=2 truncation, exact: kinetic diag(Σ^{−4}, Σ²Ω², Σ²Ω^{−2}) on (A, A¹², B = 𝒜 − lA¹²); mass only from the Stueckelberg term ½e^{4φ̃}g²𝒜². Eigenvalues m²L₅² = **{0, 0, 8}**.
  - The massless directions are exactly A (U(1)_r, the twisted SO(2)) and A¹² with 𝒜 = 0 (the Cartan of SU(2)_R): **massless graviphoton control reproduced**, Δ = 3.
  - The massive one is χ³ with m² = 2^{5/3}g², i.e. **m²L₅² = 8, Δ = 5**, exactly CGR (6.3).
- N=4: the A^{αβ} triplet gets mass only through D𝒯 and Dψ; at 𝒯 = 1, ψ = 0 the 𝒯 term is g(A^{αβ}+A^{βα}) = 0, so the **SU(2)_R triplet is massless** (exact by inspection; not printed beyond the [VEC] line). The χ^α triplet is massive at 8 by SO(3) covariance from χ³ (CGR (6.3)).
- Two-forms K^a (U(1)_r doublet, Δ = 3 per CGR) are not vectors; not recomputed (COND, citation).

## RA-4. Group A projection of the truncation modes, with the J sign (S1) (log [JS], [G]). PROVED as implication; COND overall
**Premises (stated):** (P1) the CGR ansatz (gfans)/(3fans) as written; (P2) canonical **undressed** lift (ecee2668 §6; status bd32b4e2 erratum (1)): γ ∈ Aut⁺ acts on Σ by isometry, on the twisted SO(2) ⊂ SO(5) index by the same frame rotation dγ, and trivially on SO(3)_R; (P3) HW wall ℤ₂ as in ecee2668 §6.

- **Mechanism.** Every CGR mode is built from ē^a ⊗ E_a, ε^{ab}ē^b ⊗ E_a, ω̄^{ab}, vol(Σ) and Σ-constants. ē^a ⊗ E_a is the identity section of T*Σ ⊗ V with V ≅ TΣ (twist); ε^{ab} is the complex structure. Orientation-preserving isometries commute with both, so under (P2) every CGR 5D field configuration is mapped to itself. **All CGR modes are Aut⁺-invariant.**
- **J sign, per PP S1 (not assuming the spin-2 rule).** At a Weierstrass point dJ = −1 on T_pΣ. A mode valued in K^m ⊗ V^q has fibre J-sign (−1)^{m−q}:

| mode (Σ legs) | weight m−q | J-sign | Group A |
|---|---|---|---|
| φ, λ, 𝒯, A, A^{αβ}, χ^α∧vol_Σ, h^α (no Σ legs, or vol_Σ) | 0 | + | kept |
| ψ^{aα} ē^a ⊗ E_a (Σ leg paired with twisted index) | 0 | + | kept (global section is the identity, invariant) |
| K^a ∧ ē^a (same pairing) | 0 | + | kept |
| SU(2)_R / U(1)_r Wilson lines, C₃ and g_{μm} along **harmonic** 1-forms (untwisted index) | 1 | − | **removed**: J = −I on H^{1,0} exactly (log [G]), so no invariant vector in H¹(Σ,ℝ) |
| (2,3) SO(5) Σ-leg modes, weight ±2 part (sections of K^{±2}) | 2 | + | lowest Landau level removed: H⁰(K²) = Sym² H⁰(K) has trivial multiplicity 0 (log [G], float average; PP's exact order-48 recomputation in eb979fda and ecee2668 §6 PROVED) |

- Labels: "all CGR modes invariant" **PROVED as implication of (P1)–(P2)**; J-sign table PROVED (local fibre computation); H¹ invariants = 0 **PROVED** (exact: J ∈ Aut⁺ acts as −I on H^{1,0}); Aut⁺ order 48 with GL(2,3) statistics reproduced (float closure, entries in ℚ(ζ₈); exact lifts checked). Physical identification COND (consistent truncation; vacuum COND per OW).
- **Verification of the brief's note.** The harmonic Σ-vector modes are removed because J acts as −1 on all of H¹. **Not all Σ-vector modes are removed:** Hodge decomposition on 1-forms is Aut⁺-equivariant (γ* commutes with d and *, orientation preserved), so invariant 1-forms are d f ⊕ *d g with f, g Aut⁺-invariant functions. The invariant non-harmonic 1-form spectrum of the Hodge Laplacian equals the invariant function spectrum: **lowest 23.0786** (then 74.93, 116.60, …; ecee2668 §2, FEM). Decomposition PROVED; eigenvalues COND (float); their 5D masses in the twisted background OPEN.
- **Wall ℤ₂.** It removes no species (ecee2668 §6). Metric-derived modes (φ, λ, 𝒯, ψ, the 7D gauge fields A, A^{αβ}) are wall-even; C₃-derived χ^α, h^α, K^a take the ecee2668 §6 parity. COND (HW).

## RA-5. Beyond the truncation: universal S⁴ towers via CGU (log [CGU]). Identity PROVED; multiplet assignment COND
- **Exact identity.** Stage-1 spin-2 masses at λ_Σ = 0, q = 0, ℓ = j, n = 0: 4 + m²L² = 4(j+1)², so **Δ₂ = 2j + 4** exactly. This is CGU's universal family Δ = 4 + 2ℓ + n at n = 0 with SU(2)_R spin ℓ = j. PROVED (arithmetic; independent consistency check of stage 1 against CGU).
- **Rule (stated, COND on CGU §4).** Such a spin-2 is the Q²Q̄² descendant of an A₂Ā₂ multiplet with scalar primary of SU(2)_R spin j, r = 0, Δ₀ = 2 + 2j, so m²L² = Δ₀(Δ₀−4) = 4(j²−1). The QQ̄ level contains a vector [1,1] at Δ₀ + 1, m²L² = Δ₀(Δ₀−2).
  - j = 0: scalar −4, vector 0 (= the stress-tensor multiplet: reproduces RA-2/RA-3 exactly).
  - **j = 1 (from the 12, Δ = 6 spin-2 triplet): scalar SU(2)_R triplet m²L² = 0 (Δ = 4); vector m²L² = 8 (Δ = 5).**
  - j = 2 (from 32): scalar 5-plet 12 (Δ = 6); vector 24 (Δ = 7). j = 3: scalar 32; vector 48.
- **Group A survival.** These multiplets have Σ-constant spin-2 members (stage 1 RA-3). Under (P2) the SUSY spin structure is Aut⁺-invariant (ecee2668 §4, COND), so Aut⁺ commutes with SU(2,2|2) and projects whole supermultiplets. Hence the partners survive. COND (undressed lift; SUSY spin-structure argument; CGU).
- **Non-universal levels** (e.g. the 20 singlet, Δ₂ = 2+2√6; Σ-dependent 46.157, …) have irrational Δ, so they are not of CGU form. Their multiplet position, and hence their scalar/vector partners, is **OPEN**.

## RA-6. Headline answers (Group A, canonical undressed lift)
| quantity | value | label |
|---|---|---|
| lowest invariant scalar | **m²L₅² = −4, Δ = 2** (SU(2)_R × U(1)_r singlet; stress-tensor multiplet bottom; wall-even) | PROVED within truncation (given CGR); lowest overall COND (see BF) |
| next invariant scalars | 0 (Δ 4, 5-plet, includes w), 5 (Δ 5, 3_{±1}), 12 (Δ 6, singlet) [truncation]; 0 (Δ 4, **triplet**) [CGU j=1, beyond truncation] | truncation PROVED (given CGR); CGU row COND |
| lowest invariant vector | **m²L₅² = 0, Δ = 3**: 4 massless graviphotons, SU(2)_R triplet + U(1)_r | PROVED within truncation (given CGR); lowest overall COND (unitarity Δ ≥ 3 ⇒ m² ≥ 0) |
| next invariant vectors | 8 (Δ 5, SU(2)_R triplet χ^α) [truncation]; 8 (Δ 5) in the j=1 A₂Ā₂ multiplet [CGU] | PROVED (given CGR) / COND |

**BF verdict: no invariant mode has m²L₅² < −4.**
- Within the CGR truncation: the minimum over all 13 scalars is exactly −4 (saturated, not violated). PROVED (exact), given CGR.
- Full Group A KK spectrum: for real Δ, m² = Δ(Δ−4) = (Δ−2)² − 4 ≥ −4. Modes of a supersymmetric AdS₅ vacuum fill unitary SU(2,2|2) representations (positive energy; Breitenlohner–Freedman / Gibbons–Hull–Warner), so Δ is real. The Group A projection only removes modes. COND (vacuum SUSY per OW; the standard SUSY ⇒ stability theorem cited, not re-derived).
- **Corollary.** Since −4 is attained by an invariant mode and is the bound, **−4 is the lowest invariant scalar mass in the full spectrum**, and **0 is the lowest invariant vector mass**. COND (as above).
- Wall: the Δ = 2 mode is BF-saturated. Its quantisation choice at the HW wall (Neumann-type, wall-even) is CONDITIONAL on HW and does not affect stability.

## Errata (other files; no edit made)
- **bd32b4e2** (status file): the header says "Written 20:33 CST", but the file mtime is 20:31:32 CST. Read the header time as **≈ 20:31**.
- **ecee2668 §7**: the 5-plet "0, CONDITIONAL (one component)" is now computed for all five 𝒯 components (RA-2), PROVED given CGR.

## Tally (PP convention: a stated premise counts as an implication; float or an unverified citation counts as COND)
| # | claim | label |
|---|---|---|
| 1 | RA-1 vacuum stationary; g²L² = 2^{4/3} | PROVED (given CGR as stated input) |
| 2 | RA-2 scalar masses −4, 12, 0×5, 5×6; block-diagonal | PROVED (given CGR) |
| 3 | Z1: w marginal, {0,4}, ∂³_wV = −24·2^{2/3}g² | PROVED (reproduced, exact) |
| 4 | (−3:1) ↔ Δ=6 (4−Δ = −2); (1:3) ↔ Δ=2 | PROVED |
| 5 | RA-3 vectors 0,0 (U(1)_r, SU(2)_R Cartan), 8 (Δ 5); SU(2)_R triplet massless | PROVED (given CGR) |
| 6 | these truncation masses are MN2 KK masses (consistent truncation; vacuum) | COND |
| 7 | RA-4 all CGR modes Aut⁺-invariant under (P1)–(P2); J-sign table | PROVED (implication) |
| 8 | J = −I on H^{1,0}; no invariant vector in H¹ | PROVED (exact) |
| 9 | Aut⁺ order 48, GL(2,3) statistics; H⁰(K²) trivial mult. 0 (this run) | COND (float closure/averages; exact versions in ecee2668/PP) |
| 10 | invariant 1-forms = d f ⊕ *d g, f,g invariant; lowest 23.0786 | decomposition PROVED; value COND (FEM) |
| 11 | RA-5 Δ₂ = 2j+4 identity (stage 1 ↔ CGU n=0) | PROVED |
| 12 | RA-5 A₂Ā₂ partners: triplet scalar 0 (Δ 4), vector 8 (Δ 5), j=2: 12/24 … survive Group A | COND (CGU; SUSY spin structure; undressed lift) |
| 13 | lowest invariant scalar −4, vector 0 in the full spectrum; BF: none below −4 | COND (SUSY ⇒ unitarity) |
| 14 | masses of Σ-dependent scalar/vector towers (non-harmonic invariant 1-forms, invariant functions, K^{±2} higher Landau levels), non-universal S⁴ levels (20, 56, …), charged-q towers' scalar/vector partners, two-forms K^a recomputation, fermions | OPEN |
| 15 | R-symmetry-dressed lift (would change j≠0 projection; status bd32b4e2 erratum 1) | OPEN (Owner/scope) |

**PROVED 8 · COND 5 · OPEN 2 · REF 0 = 15** (row 10 counted as PROVED for its decomposition; its FEM value is carried as COND from ecee2668).

## What remains OPEN and why
- **Σ-dependent scalar/vector towers.** They mix metric and C₃ in the twisted background; there is no CGR-type truncation for them. Exact masses need the coupled linearised 11D equations or ExFT spectroscopy (Malek–Samtleben 1911.12640), which is days of work, not 2–3 h. Unitarity still bounds them: none below −4 (COND).
- **Non-universal S⁴ multiplets** (20 singlet, etc.): their position in SU(2,2|2) multiplets is not fixed by CGU.
- **Charged (q ≠ 0) partners** of stage 2's Landau-level modes.
- **Dressed lift** (scope choice).
- **Rigorous Bolza eigenvalue bounds** above 28.08.

Rules: new dated files only; .py frozen before its logs; no existing file edited (the empty .log of D1 kept as is); tip untouched; no CERT, no Gemini, nothing external; no messages sent; c2 not pursued.
