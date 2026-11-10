# MR2 — Proposed map: 11D data on AdS₅×S⁴×Σ₂ → Φ and V₃₅ (with 61-puncture analysis and 35-dim literature anchors)
Date: 2026-11-09, ~15:20 CST (America/Chicago). Agent: Math Research 2 (MR2), citation/literature-only, invention HOLD (every proposal is labelled as a proposal).
Authority: OWNER_WRITE_MAINCHAT_BLUEPRINT_1509_CORRECTED_ADOPTED_2026-11-09_1511.md, sha256 5a6e717732c413a39c89d9b95c9b17455ecf4da8dd64e8bb9d879f427e6a845c (read in full; prefix 5a6e7177 MATCH). Non Local item O1: "NL and MR2 propose the 11D→Φ/V₃₅ map, evaluated on S⁴×Σ_g"; O3: standard (2πℓ_P)³N, N = 4880, g = 2 chosen (not forced), N ≫ 1.
Limits honoured: additive new files only; nothing edited; tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 untouched (re-hashed this turn); no CERT; nothing sent outside; no Gemini; no agent messaged. Public arXiv PDFs read only.
Check script: MR2_11D_ADS5_S4_SIGMA2_PHI_V35_CHECK_2026-11-09.py (sha256 62be2fa178c295064688aa9d4ddda040e737c8a4b0777b66175e1dcac3deb108; sympy + exact fractions; output reproduced in §5 and §6).
Labels: PROVED / CONDITIONAL / OPEN / REFUTED, exactly one per result. Standard: REFUTED only for a precise claim shown false.

Non Local Path cross-check: no NL_DERIVED_O1_* file existed in reports/ at 15:18 CST, so there was nothing to cross-check. This file cites NL's earlier results instead of re-deriving them. When NL's O1 files appear, §9 lists the points to compare.

---
## 1. Setup: which geometry (D) is
**Owner (D), verbatim** (OW 7708ec5d…, quoted in RECORD_PP_ADOPT_ADS5_S4_SIGMAg_CONDITIONAL_OW7708ec5d_2026-11-09_1353.md, sha 5b4592d4…, L5): "(D) Adopt AdS₅×S⁴×Σ_g as a CONDITIONAL proposal replacing the flux lock; flux normalization, N and genus stay OPEN." The 15:11 record then fixes the standard normalization, N = 4880 and g = 2 as chosen inputs.

**The (D) metric** (PP FINDINGS_PP_DERIVE_ADS5S4SIGMA_PARAMETERS_2026-11-09_1357.md, sha 4660b73e…, L16–18):
ds² = e^{−2ky}η + dy² + r²dΩ₄² + ρ²ds²(H²/Γ), with G = q₀ vol(S⁴_r), q₀ = 2√6k, r = √6/(4k), ρ = 1/(2k), L_AdS = 1/k, Λ₁₁ = 0.

- **S1 (PROVED). (D) is the Kehagias–Russo direct product, not Maldacena–Núñez.** Kehagias–Russo hep-th/0003281 §3.2, eqs. (13)–(14), give AdS₅×H²/Γ×S⁴ with L² = 2R₀²/3, ρ² = R₀²/6, r² = R₀²/4 and F̂₄ = 6R₀³Ω₄. This gives L/ρ = 2 and L/r = √(8/3), which are exactly PP's D2 ratios. KR state that the solution has no Killing spinors, i.e. it is non-supersymmetric, and they name the genus-2 quotient explicitly.
- **S2 (PROVED, from the literature). Maldacena–Núñez (MN) / Gaiotto–Maldacena (GM) is a different geometry.** In MN (hep-th/0007018 §4, eqs. (22), (28), (29)) and GM (0904.4466 §2.2, eq. (2.7)), S⁴ is *fibred* over Σ_g through the topological twist, which embeds the Σ_g spin connection in U(1) or SO(2) ⊂ SO(5)_R. The S⁴ is also squashed, with W = 1 + cos²θ, and the metric is warped by W^{1/3} and Δ^{1/3}. Eight (N = 2) or four (N = 1) supercharges are preserved. Those solutions are not a direct product, so **(D) ≠ MN**.
- **S3 (CONDITIONAL on the Owner switching (D) to MN). MN/GM central charges do not transfer to (D).** The class-S numbers in §6 are stated only as the MN/GM alternative. PP 4660b73e "Owner decisions" item 4 already notes that a twisted MN background would need a new Owner adoption.
- **S4 (PROVED, PP C4, cited). (D) is non-perturbatively unstable at probe level.** The probe-M5 charge/tension ratio is √6/2 > 1. Any holographic statement about (D) below is therefore CONDITIONAL on a dual CFT existing at all.

## 2. Project definitions found (paths and line pins)
| Object | Where | What the files say | Status |
|---|---|---|---|
| Φ (EH) | nonlocal/Einstein_Hampton_Equation_Rewrite_Appendix_2026-09-28.txt (sha 08b8541a…), §3 (alg) and (EH-lock), ~L33–38 | "6k²−3K = −Φ/96, 4k²+K = Φ/144" ⇒ "k² = Φ/1728, K = 8k²", for a single 6D Einstein fibre. Φ is not otherwise defined. | Φ **undefined as an object** (OPEN). NL's FINDINGS_NL_OWNER_DEFS_PREV_TEH_2026-11-09_1233.md (sha 76e63cc2…) L23 and L33 ("Φ is 'evaluated across V₃₅', which is undefined"). bridges/NONLOCAL_QM_EH11D/MILESTONE_2026-10-24b.md L3 asks the Owner for "Φ := G² (or its actual definition)". |
| V₃₅ (EH sense) | Owner DEF2 (Zenodo 18586411), as relayed in NL 76e63cc2 L33, and the question C5 in GEMINI_ROUND_QUESTIONS_2026-11-09_1238.md L23 | "a flux scalar Φ is 'evaluated' over V₃₅" | **OPEN (undefined)**. PP FINDINGS_PP_SOFTSF_AUDIT_PHYSICIST_GEMINI_CHECK_2026-11-09_1305.md (sha 90400213…) L101–103 lists the candidates SL(6,ℝ), Λ³/Λ⁴(ℝ⁷), Sym²₀(ℝ⁸); "Λ⁴(R⁷) is the one tied to F4". |
| V₃₅ (number-theory sense; **name collision**) | OWNER_WRITE_CAVEAT2_NARROW_ALL_FOUR_CLPLUS_V35_2026-11-03.md (sha e4ef0a81…) L16; parent LOCK c290a274… | "V₃₅ = full adelic LMFDB cuspidal newspace of parallel weight [2,2] and level (1) over ℚ(√35)" (dim 14 lock) | Owner-LOCKED object of **dimension 14**, not 35. It is unrelated to any 4-form space. FINDINGS_LOCAL_SOFTSF_CAT_A_FOOLPROOF_F4_F6…_2026-11-03.md (sha 0a1c4add…) L21 says separately that the RTA Part III "V_35 is defined nowhere on disk". |
| "61-puncture limit" | references/entanglement-publications/existing-corpus-CORPUS.md L397 and L405; theorems-18-40-v1.txt L169, L215, L248 | "ω-branches (punctures) are both 61" in the T₃ ternary map; "539 steps produce 61 punctures"; "Divergences capped by 61 punctures" | **OPEN.** On disk, the 61 is a count of branches in an integer map, not punctures of a Riemann surface. NL 76e63cc2 L29 and PP 90400213 L99 both record it as undefined. |
| N = 4880 | PP 4660b73e B5: ⌊e³·3⁵⌋ = 4880 | an input, not forced | PROVED arithmetic; the choice is the Owner's. |

**Conclusion (OPEN).** Φ, V₃₅ (in the EH sense) and the 61-puncture limit are **not defined** in the project files. Everything in §§3–4 is therefore a labelled **PROPOSAL**, not a definition.

## 3. Literature pins (fetched this turn; arXiv PDF sha256 prefixes in brackets)
- [L1] Maldacena–Núñez, hep-th/0007018 [770d87d8]. §4 "Twists of the M5 brane theory": U(1)×U(1) ⊂ SO(5) truncation; ansatz eq. (22); IR AdS₅ values eq. (28); 11D uplift eq. (29). Footnote 5: G₁₁ = 16π⁷ℓ_p⁹ and R²_AdS₇ = 4(πN)^{2/3}ℓ_p².
- [L2] Gaiotto–Maldacena, 0904.4466 [21445168]. Eq. (2.1): c = (2n_v+n_h)/12, a = (5n_v+n_h)/24. Eq. (2.4): T_N gives n_v = 2N³/3 − 3N²/2 − N/6 + 1 and n_h = 2N³/3 − 2N/3. §2.1 gluing rule: a genus-g surface is built from 2(g−1) T_N blocks and 3(g−1) SU(N) groups. Eq. (2.5): n_v = (g−1)(4N³/3 − N/3 − 1), n_h = (g−1)(4N³/3 − 4N/3). Eq. (2.7): MN N = 2 metric with prefactor (πNℓ_p³)^{2/3}. Eq. (2.8): c = πR³/(8G₅) = (g−1)N³/3, with A_Σ = 4π(g−1).
- [L3] Bah–Beem–Bobev–Wecht, 1203.0303 [473bfa98]. Eqs. (2.12)–(2.13): p = (1+z)(g−1), q = (1−z)(g−1). Eq. (2.20): finite-N a, c. Eq. (2.22): large N, a = c = (1−g)N³[1 − 9z² + κ(1+3z²)^{3/2}]/(48z²), with κ = −1 for hyperbolic Σ (L418). |z| = 1 is N = 2 MN, z = 0 is N = 1 MN (L645–648). Eq. (E.6): a_{T_N}, c_{T_N}.
- [L4] Kehagias–Russo, hep-th/0003281 [a9640d13]. §3.2, eqs. (13)–(14): AdS₅×H²/Γ×S⁴, non-SUSY, finite-volume quotients including genus 2 and cusped F₂.
- [L5] Henningson–Skenderis, hep-th/9806087 [b2c963b9]. §3.2, eqs. (20)–(22): the holographic Weyl anomaly of an Einstein AdS₅ bulk, which gives a = c ∝ L³/G₅ (the formula GM use in (2.8)).
- [L6] Nastase–Vaman–van Nieuwenhuizen, hep-th/9905075 [c72f35c9]. Around L191–200: maximal 7D SO(5)_g gauged sugra from 11D on S⁴. Fields: graviton; 4 gravitini; SO(5)_g vectors B^{AB} (10); scalars Π_A^i ∈ SL(5,ℝ)/SO(5)_c (14); three-forms S_{αβγ A} (5); spin-½ λ_{Ii}.
- [L7] Bryant, "Some remarks on G₂-structures", math/0305124 [af0aff03]. Eq. (2.13): Λ³ = Λ³₂₇ ⊕ Λ³₇ ⊕ Λ³₁. Eq. (2.25): Λ⁴(V*) ≅ Λ⁴₁ ⊕ Λ⁴₇ ⊕ Λ⁴₂₇ ≅ V₀,₀ ⊕ V₁,₀ ⊕ V₀,₂. The text around L203–220 shows Λ³₂₇ = i_φ(S²₀). Around L461–478: M⁷ admits a G₂-structure iff it is orientable and spin.
- [L8] Flux quantization: Witten hep-th/9609122, as already verified by PP in 4660b73e A1, giving ∫_{S⁴}G = (2πℓ_p)³N with 2κ² = (2π)⁸ℓ_p⁹; B1 gives no half-integer shift on (D). **Not re-fetched.** GM [L2] use the same G₁₁ = 16π⁷ℓ_p⁹ (= (2π)⁸ℓ_p⁹/16π).
- [L9] **Not fetched this turn** (pre-arXiv; cited by standard reference only): Cremmer–Julia, Nucl. Phys. B159 (1979) 141; de Wit–Nicolai, Nucl. Phys. B208 (1982) 323. Only the representation arithmetic for these is checked here (§5).

## 4. Proposed map (PROPOSAL, step by step; all CONDITIONAL on (D) and on the Owner adopting each definition)
**Step M0 (input; CONDITIONAL on (D)).** The 11D data are (g₁₁, G₄) of (D) from §1, with g = 2, standard quantization, N = 4880 and N ≫ 1.

**Step M1 (PROPOSAL P-V35-a).** Let M₇ := ℝ_y × S⁴ × Σ₂. This is the 7D space transverse to the 4D x^μ. Its effective volume is PP's V₇eff (FINDINGS_PP_DERIVE_11D_MAP_2026-11-09_1328.md, sha 9dde377d…, B2). Define V₃₅|_p := Λ⁴T*_pM₇, with dim = C(7,4) = **35** (PROVED, arithmetic).
- This is the only candidate on PP's list (90400213 L102) that *contains* the 4-form G₄ of (D) by construction: G₄ = q₀ vol(S⁴) lies in Λ⁴T*M₇.
- The internal 6D space S⁴×Σ₂ alone gives Λ⁴(ℝ⁶) = 15, and Λ³(ℝ⁶) = 20 = 35 − 15. That reproduces PP's C5 count "35 − 15 = 20".

**Step M2 (PROVED, linear algebra). The natural splitting of V₃₅ on (D) is under SO(4)×SO(2), not G₂.** Write T*M₇ = ℝ_y ⊕ T*S⁴ ⊕ T*Σ (1+4+2) and sort Λ⁴ by degrees (y, S⁴, Σ):
(0,4,0) = 1, (1,3,0) = 4, (0,3,1) = 8, (0,2,2) = 6, (1,2,1) = 12, (1,1,2) = 4. Sum = 35 (script output).
- The (D) flux occupies only the 1-dimensional block (0,4,0).
- No other block is sourced on (D), by PP B3: H⁴(S⁴×Σ_g; ℤ) = ℤ[S⁴].

**Step M3 (CONDITIONAL on choosing a G₂-structure φ on M₇). The 1+7+27 split.** Bryant (2.25) gives Λ⁴ ≅ 1 ⊕ 7 ⊕ 27 pointwise (PROVED, cited; 27 = dim S²₀(ℝ⁷), also checked).
- **Existence: PROVED.** By Bryant ~L461, M₇ admits a G₂-structure because it is orientable and spin: ℝ, S⁴ and Σ₂ are all spin, and products of spin manifolds are spin.
- **Canonicity: OPEN.** The (D) metric has holonomy SO(4)×SO(2) on the internal part, which is not contained in G₂ as a torsion-free structure. So any G₂-structure is an extra choice, and the split of G₄ into its 1, 7 and 27 parts depends on φ.
- **Owner must choose φ** if the 1+7+27 reading is meant.

**Step M4 (PROPOSAL P-Φ-a). Φ := G_MNPQ G^MNPQ = 4!·|G|²_{V₃₅}.** This is the Λ⁴ norm on V₃₅ from M1, in the sugra normalization (1/2κ²)∫(R − ½|G|²). It is equivalent to Φ := 16πG₁₁·F_MNPQF^MNPQ in the Owner-adopted O5 normalization T^(EH) = (1/6)FF − (1/48)gF² with G_MN = 8πG₁₁T. "Φ evaluated across V₃₅" is then read as the quadratic form on V₃₅ evaluated on G₄. This matches the Owner's own wording "Φ := G²" in the NL MILESTONE L3, but the Owner never adopted it, so it is **a proposal**.

**Step M5 (PROVED given P-Φ-a, sympy). The Einstein blocks on (D):**
- G_AdS₅ = −Φ/96, G_S⁴ = +Φ/96, G_Σ = −Φ/96.
- On the vacuum, Φ = 24q₀² = **576k²**.
- Hence k² = Φ/576, Ric_S⁴ = 8k² = Φ/72, and the Gauss curvature of Σ is K_Σ = −4k² = −Φ/144.

**Step M6 (REFUTED, under P-Φ-a, for (D)). The EH pair (alg) and the lock (EH-lock) do not hold on (D).**
- The external coefficient −1/96 **does** match (PROVED).
- But G_S⁴ − G_ext = Φ/48, not Φ/144.
- And k² = Φ/576, not Φ/1728. The ratio is exactly 3.
- K_S⁴ = 8k² does agree with EH's "K = 8k²", as RECORD 5b4592d4 item 3 also notes.
- Cause: (alg) assumes a single 6D Einstein fibre, but S⁴×Σ₂ is not Einstein (Ric = 8k² vs −4k²).
- The coefficient 1/144 does appear on (D), but as |K_Σ|/Φ, not as the fibre-minus-external Einstein block. Reading that as the intended meaning would be an identification, which is OPEN and not proposed here.

**Step M7 (PROVED, sympy; normalization from [L8] and PP A1/A4).** q₀·Vol(S⁴_r) = (2π)³N gives k = √(3/8)(πN)^{−1/3} ℓ_p⁻¹, and hence
**Φ(N) = 216 (πN)^{−2/3} ℓ_p⁻²**.

**Step M8 (PROVED as 5D Einstein-frame coefficients; holographic reading CONDITIONAL on a dual CFT existing, see S4).**
- G₅ = G₁₁/V₆, with V₆ = (8π²/3)r⁴·4π(g−1)ρ² = 3π³(g−1)/(8k⁶).
- This gives **G₅ = 9π²/(4(g−1)N²) ℓ_p³**.
- The Henningson–Skenderis/GM coefficient is **a_D = c_D = πL³/(8G₅) = (8√6/81)(g−1)N³ ≈ 0.241925 (g−1)N³**.
- Calibration: the same method on AdS₅×S⁵ returns N²/4 (script).
- Compare MN: N = 2 gives (g−1)N³/3 [L2 (2.8)] and N = 1 gives 9(g−1)N³/32 [L3 (2.22)]. (D) gives a different coefficient, as it must, because the geometry is different (S1/S2).
- 4D Newton constant: G₄ = G₅·2k/(1 − e^{−2kb}), via PP 9dde377d B2. This is CONDITIONAL on the undefined brane separation b (OPEN).

## 5. Numbers at g = 2, N = 4880 (ℓ_p = 1; standard normalization; from the script)
| quantity | formula | value | label |
|---|---|---|---|
| k | √(3/8)(πN)^{−1/3} | 0.0246505002 | PROVED (= PP A4) |
| L_AdS | 1/k | 40.5671282 | PROVED |
| r (S⁴) | √6/(4k) | 24.8421911 | PROVED |
| ρ (Σ₂) | 1/(2k) | 20.2835641 | PROVED |
| Area(Σ₂) | 4π(g−1)ρ² | 5170.09355 | PROVED (= PP C1) |
| (ℓ_p/r)⁶ | | 4.2546×10⁻⁹ | PROVED; sugra validity CONDITIONAL on N ≫ 1 |
| Φ (P-Φ-a) | 216(πN)^{−2/3} | **0.350004763 ℓ_p⁻²** | CONDITIONAL on P-Φ-a and (D) |
| G₅ | 9π²/(4(g−1)N²) | 9.32487×10⁻⁷ ℓ_p³ | CONDITIONAL on (D) |
| a_D = c_D | (8√6/81)(g−1)N³ | **2.81151276×10¹⁰** | CONDITIONAL (S4: dual CFT existence) |
| MN N = 2 (alternative geometry) | GM (2.5) via (2.1), exact | a = 929714161355/24 ≈ 3.873809×10¹⁰; c = 232428539119/6 ≈ 3.873809×10¹⁰ | PROVED as arithmetic on [L2]; applies only if (D) → MN |
| MN N = 1 (alternative geometry) | 9(g−1)N³/32, large N | 3.26853×10¹⁰ | same as above |

## 6. "61-puncture limit" analysis
- **P1 (OPEN).** The project's 61 is a T₃-map branch count (§2). No project file identifies it with punctures on Σ_g. Any such identification is CONDITIONAL on an Owner definition.
- **P2 (PROVED, Euler characteristic). Class-S puncture constraint.** A genus-g surface with n punctures admits a pants decomposition iff 2g−2+n > 0. For g = 2 that holds for every n ≥ 0, so class S places **no upper bound** on n and nothing singles out n = 61.
  - At n = 61: −χ = 2g−2+n = **63** pairs of pants (T_N blocks), and 3g−3+n = **64** tubes, which is also the number of SU(N) gauge groups and dim_ℂ M_{2,61}.
- **P3 (CONDITIONAL: 61 *maximal* SU(N) punctures, in the GM/class-S N = 2 theory, i.e. the MN-type geometry, not (D)).**
  - Gluing 2g−2+n T_N blocks with 3g−3+n SU(N) vector multiplets [L2 §2.1, (2.4)] reproduces (2.5) at n = 0 (checked) and gives, per maximal puncture: δn_v = 2N³/3 − N²/2 − N/6 and δn_h = 2N³/3 − 2N/3.
  - At g = 2, N = 4880, n = 61: n_v = 4880273033559, n_h = 4880999219040, a = 9760788128945/8 ≈ 1.220099×10¹², c = 2440257547693/2 ≈ 1.220129×10¹². At large N, a/N³ → (2g−2+n)/6 = 10.5; the script gives 10.4987.
  - The gravity dual with punctures is GM's sourced, LLM-type class (GM §3 onward). It is not the uniform MN solution and not (D).
- **P4 (CONDITIONAL: 61 cusps on (D)). Geometric option.**
  - Σ_{2,61} = H²/Γ with Γ a finite-covolume Fuchsian group of signature (2; –; 61 cusps). Such Γ exist because 2g−2+n > 0 (uniformization / Poincaré polygon theorem; standard, not fetched). KR [L4] allow cusped finite-volume quotients explicitly, e.g. F₂.
  - Gauss–Bonnet gives Area = 2π(2g−2+n)ρ² = 162857.947 ℓ_p² at N = 4880.
  - a_D = c_D = (4√6/81)(2g−2+n)N³ ≈ **8.85627×10¹¹**, which is 63/2 times the n = 0 value.
  - **OPEN** for this option: the cusps make Σ non-compact, so the Laplacian has continuous spectrum and the KK reduction and stability need separate treatment. PP's PROVED compact-case statements B3 and C2 do not transfer automatically.
- **P5 (OPEN).** The word "limit" (n → 61? a cutoff "capped by 61"?) has no definition. No literature construction found here makes 61 a limit point.

## 7. Pinned anchors for 35-dimensional structures (priority deliverable)
| # | 35-dim structure | Pin | Applies to AdS₅×S⁴×Σ_g? | Label |
|---|---|---|---|---|
| A1 | Λ⁴(ℝ⁷) ≅ Λ³(ℝ⁷) (Hodge), dim 35 = 1+7+27 under G₂ | Bryant (2.13), (2.25); L203–220 | Pointwise on M₇ = ℝ_y×S⁴×Σ₂ (M1). The G₂ split needs a non-canonical φ (M3). | dim and decomposition PROVED; use on (D) CONDITIONAL on choosing φ |
| A2 | Λ⁴ on 1+4+2 under SO(4)×SO(2): 1+4+8+6+12+4 | this file M2 (script) | Yes, canonical for the (D) product metric | PROVED (CONDITIONAL on (D)) |
| A3 | 11D on T⁷ → 4D: 35 scalars from C_{ijk} (Λ³ℝ⁷); 70 = 28 (g_ij) + 35 (C_ijk) + 7 (dual C_μνi); E₇₍₇₎/SU(8): 70 = Λ⁴(8), and under SL(7) ⊂ SL(8) 70 = 35 + 35 | Cremmer–Julia 1979; de Wit–Nicolai 1982 [L9, not fetched]; counts checked by script | **No.** These belong to 7D internal tori or S⁷ with a 4D external space. (D) has a 6D internal space and a 5D external space. | arithmetic PROVED; applicability to (D) **REFUTED** (dimension count: 11 = 5+6, not 4+7). Physics content of the citation OPEN (not fetched). |
| A4 | SL(5)/SO(5): 14 scalars; 10 vectors; 5 three-forms (7D SO(5) gauged sugra on S⁴) | NVvN L191–200 [L6]; MN §4 uses the U(1)² truncation [L1] | Yes, it is the S⁴ reduction step used for MN. On (D), the round-S⁴ point is Π = 1. **No 35-dim multiplet here.** | PROVED (field content cited); "35 from this sector" REFUTED by count (14, 10, 5) |
| A5 | SO(5) irreps of dim 35: Dynkin (4,0) and (2,1), the 35 and 35′ | Weyl dimension formula (script) | S⁴ KK harmonics do carry SO(5) irreps. Whether a 35 or 35′ occurs in the (D) or MN spectrum was not checked or pinned. Scalar harmonics give 1, 5, 14, 30, 55, …, so no 35 there. | dims PROVED; occurrence OPEN |
| A6 | dim SL(6,ℝ) = dim SU(6) = 35; Sym²₀(ℝ⁸) = 35 | PP 90400213 L102; arithmetic | No AdS₅×S⁴×Σ_g pin found. SL(6)/SO(6) has dim 20 (Physicist 3ddf528d L20). | arithmetic PROVED; relevance OPEN |
| A7 | 35-dim objects inside the MN/GM AdS₅ solutions | MN [L1], GM [L2], BBBW [L3] searched | None found: the structures there are U(1)², SU(2)_R×U(1)_R, SU(N), and moduli 3g−3 (+n). | OPEN (not found ≠ absent) |
| A8 | Owner-locked V₃₅ = Hilbert newspace over ℚ(√35), dim 14 | OW e4ef0a81 L16 | No; it is number theory | name collision, flagged (OPEN until the Owner disambiguates) |

## 8. Status table
| ID | Statement | Label |
|---|---|---|
| S1 | (D) = Kehagias–Russo AdS₅×H²/Γ×S⁴ (ratios match) | PROVED |
| S2 | MN/GM ≠ (D) (fibred, squashed, warped, SUSY) | PROVED |
| S3 | MN/GM a, c apply to (D) | CONDITIONAL on an Owner switch to MN |
| M1 | V₃₅ := Λ⁴T*M₇, M₇ = ℝ_y×S⁴×Σ₂, dim 35 | PROPOSAL; dim PROVED; adoption OPEN |
| M2 | SO(4)×SO(2) split 1+4+8+6+12+4; G₄ in the 1-dim block | PROVED (on (D)) |
| M3 | G₂ split 1+7+27 on M₇ | existence PROVED; canonical use OPEN; CONDITIONAL on φ |
| M4 | Φ := G·G = 4!·‖G‖²_{V₃₅} | PROPOSAL (OPEN until adopted) |
| M5 | G_AdS = G_Σ = −Φ/96, G_S⁴ = +Φ/96, Φ = 576k², k² = Φ/576, K_Σ = −Φ/144 | PROVED given M4 and (D) |
| M6 | EH (alg) "fib − ext = Φ/144" and lock "k² = Φ/1728" hold on (D) with M4 | REFUTED (actual Φ/48 and Φ/576) |
| M7 | Φ(N) = 216(πN)^{−2/3}; Φ(4880) = 0.350005 ℓ_p⁻² | CONDITIONAL (M4, (D)) |
| M8 | G₅ = 9π²/(4(g−1)N²); a = c = (8√6/81)(g−1)N³ = 2.8115×10¹⁰ | CONDITIONAL (dual CFT; S4 instability) |
| P1 | project 61 = Σ-punctures | OPEN |
| P2 | no upper bound on n for g = 2; n = 61 gives 63 pants and 64 tubes | PROVED |
| P3 | 61 maximal punctures: a ≈ 1.220099×10¹², c ≈ 1.220129×10¹² | CONDITIONAL (MN-type + maximal punctures) |
| P4 | 61 cusps on (D): Area 162857.9 ℓ_p², a_D ≈ 8.856×10¹¹ | CONDITIONAL; KK/stability OPEN |
| P5 | meaning of "limit" | OPEN |
| A3 | E₇/SU(8) 35+35 applies to (D) | REFUTED (5+6 vs 4+7) |

## 9. Points for NL's O1 files (when they appear)
1. Does NL's Φ agree with M4, including the normalization (O5 vs sugra) and the factor 576 vs 1728?
2. Does NL take V₃₅ on M₇ (with y) or on the 6D internal space? On 6D it has dim 15.
3. Does NL use the canonical SO(4)×SO(2) split or a G₂ choice?
4. Does NL treat (D) as the KR product (S1) rather than MN?

## 10. Definitions the Owner still must supply
1. **Φ**: adopt or reject P-Φ-a (Φ := G_MNPQG^MNPQ), and state its normalization: O5/EH, sugra, or a fixed multiple such as 3G·G to restore 1/1728. Choosing a multiple only to restore 1/1728 would make the coefficient a convention, not a derived result.
2. **V₃₅**:
   - adopt or reject P-V35-a (Λ⁴T*M₇ with M₇ = ℝ_y×S⁴×Σ₂);
   - **rename one of the two V₃₅'s**, because it collides with the Owner-locked dim-14 Hilbert newspace V₃₅ (e4ef0a81 / c290a274);
   - say what "evaluated across" means: a pointwise norm, an integral over M₇ (then V₇eff and b enter), or a projection onto the 1/7/27 parts.
3. **G₂-structure φ on M₇**, if the 1+7+27 reading is intended.
4. **"61-puncture limit"**:
   - which kind of puncture: class-S maximal punctures, cusps of H²/Γ, or the T₃ ω-branch count with no geometric meaning;
   - what "limit" means.
5. **(D) vs MN**: keep the non-SUSY, probe-unstable KR product, or switch to MN N = 2 / N = 1 (needs a new adoption; PP 4660b73e decision 4).
6. **b** (brane separation), if a 4D G₄ is wanted.

Tip 7cddb188 untouched. No CERT. Nothing sent outside. No Gemini.
