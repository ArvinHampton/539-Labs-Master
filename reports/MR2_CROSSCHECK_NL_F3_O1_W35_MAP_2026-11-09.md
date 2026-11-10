# MR2 cross-check of NL F3 (O1): 11D → Φ and W₃₅ map, and answers to NL's five questions. 2026-11-09, ~15:35 CST (America/Chicago)
Agent: MR2 (Math Research 2). Citation/literature-only, invention HOLD. Authority: OW 5a6e717732c413a39c89d9b95c9b17455ecf4da8dd64e8bb9d879f427e6a845c (NL O1, joint with MR2).
Limits: new additive file only; nothing edited; tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 untouched (re-hashed); no CERT; no Gemini; nothing sent outside; no agent messaged.
Script: MR2_CROSSCHECK_NL_F3_O1_W35_CHECK_2026-11-09.py (sha256 9da0574e163f2df4d39c6243fd2a40da7861410219fa7fb3b199ac95699ac29c); log .log (sha256 2cd3a0fdb9011c77a62a3b15af8fbe695c3e3e9c1129a5aa2bd98ef2d03c7df0).

## 0. Files read, with hashes verified this turn
| file | claimed | computed | |
|---|---|---|---|
| NL_DERIVED_F3_O1_11D_TO_PHI_AND_W35_MAP_DRAFT_FOR_MR2_2026-11-09_1523.md (read in full, 84 lines) | 965de066…3302 | 965de066afd51ab52f1ea40fb29271c2e3501d4dc408233b03494709b8fb3302 | MATCH |
| NL_DERIVED_F1_TEH_ON_ADS5_S4_SIGMA2_STD_NORMALIZATION_O3_O5_2026-11-09_1520.md (read §1–§5) | f2e5120d… | f2e5120d975da057ca77ffee345cc9dcd66ebbd271f0528a8f8e8f20b7d4694e | MATCH |
| NL_DERIVED_F2_PREV_ON_MINUS_U_SECTOR_ONLY_O6_O9_O10_2026-11-09_1528.md | e9bdd871… | e9bdd871a04ddec2e56c99e58bad3f2d50d6172c0f4dd4b05c6a95ed13569ab7 | MATCH. Not needed for O1: P_rev does not enter the Φ/W₃₅ map. |
| MR2_11D_ADS5_S4_SIGMA2_TO_PHI_V35_MAP_PROPOSAL_2026-11-09.md (MR2 map) | fd191d28… | unchanged (sidecar OK) | |
| MR2_KK_SPECTRUM_ADS5_S4_SIGMA2_BF_BOUND_2026-11-09.md | 7824e789… | 7824e789316a169dc11eae4d684465e96b4b305cff02e568c43066fea106e8b8 | MATCH |
| Kehagias–Russo hep-th/0003281 (arXiv PDF) | — | a9640d134c60a6e4c1103f3a821038ddf225a64043179006846bcec5526ed6f8 | fetched. Pages 2 and 5 were rendered as images and read, because the text extraction of eqs. (1), (13) and (14) was unreliable. |

**Naming.** From here on I adopt NL's name **W₃₅ := Λ⁴T*M₇, with M₇ = ℝ_y×S⁴×Σ₂**. It is the same object as MR2's P-V35-a / M1. **V₃₅** is reserved for the Owner-locked Hilbert newspace (OW e4ef0a81, dim 14). MR2 map file §10 item 2 asked for exactly this rename, so this file treats that point as resolved by NL's naming. Owner adoption of the name is still pending (OPEN).

## 1. Agreements and disagreements (NL F3 vs MR2 map fd191d28)
**Agreements** (each checked independently, not adopted on relay):
| # | point | NL F3 | MR2 | verdict |
|---|---|---|---|---|
| A1 | Φ-1 := G_MNPQG^MNPQ (sugra) = 2κ²F² = 16πG₁₁F² (O5 form); Φ = 576k² on (D) | §2 | M4, M5 | AGREE (PROVED). NL F1 §2 (T^(EH) = 2T_std, F = G_std/(√2κ)) is the same relation MR2 wrote as "16πG₁₁F², G_MN = 8πG₁₁T", because κ² = 8πG₁₁. |
| A2 | L7a G_ext = −Φ/96 holds; L7b = Φ/144 fails (actual Φ/48); lock k² = Φ/1728 fails (Φ/576); K = 8k² holds as the S⁴ Ricci eigenvalue; K_Σ = −Φ/144 | §3 | M5, M6 | AGREE. NL adds two more failing readings of L7b (fibre = Σ₂ gives 0; fibre-averaged gives Φ/72). MR2 accepts both (simple block arithmetic; REFUTED-by-proof). |
| A3 | Φ(4880) = 216(πN)^{−2/3} = 0.350005 ℓ_P⁻² | §2 | M7 | AGREE |
| A4 | W₃₅ on M₇ with y (dim 35); on the 6D internal space dim 15 | §4 W-a, W-c | M1 | AGREE |
| A5 | SO(4)×SO(2) split 1+4+8+6+12+4; G in the 1-dim block | §4 | M2 | AGREE (identical tables) |
| A6 | G₂ split not canonical | §4: the singlet fraction is 1/7 or 0 depending on frame placement | M3: "canonicity OPEN" | AGREE. NL's frame-dependence result **upgrades** MR2 M3 from "canonicity OPEN" to "**non-canonical: PROVED**", with the example as the proof. Plausibility check: for a decomposable unit 4-form α, the Λ⁴₁ component is ⟨α,∗φ⟩∗φ/7, and ⟨α,∗φ⟩ is ±1 when the four legs are a coassociative frame plane of ∗φ, and 0 otherwise. Both cases occur, so the split depends on the frame. MR2 did not rerun NL's f3 script (it is outside reports/), so the 1/7 value is CONDITIONAL on NL's log. |
| A7 | (D) = Kehagias–Russo product, not MN | §5.4 (ratios only) | S1 | AGREE. Upgraded in §3 below, from the KR text itself. |
| A8 | E₇/SU(8) 35+35 / T⁷ axions do not apply | W-d: b₃(S⁴×Σ₂) = 0 | A3: 11 = 5+6 | AGREE. NL's Betti argument is an independent second proof. Check (Künneth): b(S⁴) = (1,0,0,0,1), b(Σ₂) = (1,4,1), so b₃ = b₀(S⁴)b₃(Σ) + b₃(S⁴)b₀(Σ) + … = 0. PROVED. |
| A9 | G₅ = 9π²/(4(g−1)N²) = 9.32487×10⁻⁷ ℓ_P³; a_D = c_D = 2.81151×10¹⁰ | §6 | M8 | AGREE. NL F1 §3 matches. |
| A10 | name collision → W₃₅ vs V₃₅; any W₃₅ ≅ V₃₅ isomorphism is impossible (dims 35 vs 14, or 36 for RTA Def. 33.2) | §0, L-dim | §10.2 | AGREE (L-dim is PROVED as a dimension count). MR2 has not independently checked the RTA dim 36 (Prop. 33.6); it is taken on NL's citation. The 35-vs-14 case alone suffices for the Owner-locked V₃₅. |

**Disagreements and refinements** (none changes a PROVED/REFUTED label in either file):
- **D1 (labelling of Φ-2).** NL calls Φ-2 "a convention inconsistent with L7a". MR2's view: Φ-2 := 1728k² is a definition, and a definition cannot be REFUTED. What is REFUTED is the precise joint claim "on (D), Φ = c·G·G satisfies both L7a and the lock for some c": L7a needs c = 1 and the lock needs c = 3 (script). Substance is unchanged; only the label is sharper. See Q1.
- **D2 (stability label).** NL F1 §5 and F3 header keep "C5 stability OPEN". MR2's KK file (7824e789) finds (D) **perturbatively BF-unstable**: 14 scalars with m²L² = −16/3 < −4, for any N and g. That result is labelled PROVED [MR2-calc] and is **pending PP audit**. NL wrote before or without it. There is no contradiction, but once PP audits the KK file, NL's "C5 OPEN" is superseded for perturbative stability. Ooguri–Vafa itself remains a conjecture.
- **D3 (KR flux equation).** NL left a "convention-dependent factor" unresolved. §3 resolves it: KR's printed eq. (14) is off by a factor 16 from KR's own eqs. (2), (4) and (13). (D) itself agrees with KR's field equations exactly.
- **D4 (KR on cusped quotients, a new caveat for both files).** KR §3.2 claims that F₂ = H²/SL(2,ℤ) has no square-integrable Laplace eigenfunctions except the constant. That claim is **REFUTED**: SL(2,ℤ) has infinitely many Maass cusp forms. The first, LMFDB label 1.1, has spectral parameter R = 9.53369526, so λ = 1/4 + R² ≈ 91.14 (LMFDB Maass search, level 1, fetched this turn). There is also an Eisenstein continuum λ ∈ [1/4, ∞). Neither NL F3 nor MR2's map file relies on KR's claim. The consequence for the KK file is in §4.

## 2. Answers to NL's five questions (NL F3 §7)
**Q1. Φ-2 (1728k²): REFUTED for L7a, or kept as a convention?**
- (a) "Φ-2 satisfies L7a on (D)" is **REFUTED**: G_ext + Φ-2/96 = −6k² + 18k² = 12k² ≠ 0 (script).
- (b) "Some single normalization Φ = c·G·G satisfies L7a and the lock k² = Φ/1728 together on (D)" is **REFUTED**: L7a forces c = 1 and the lock forces c = 3 (script).
- (c) Φ-2 *as a definition* is not refutable. MR2 recommends **not** proposing it, in agreement with NL, because the only gain is restoring the number 1728 while breaking the field-equation reading.
- Label for the record: Φ-2 = "admissible definition; REFUTED as compatible with L7a". Adoption is OPEN, and the recommendation is to reject it.

**Q2. KR's flux amplitude F̂₄ = 6R₀³Ω₄ vs q₀ = 2√6k = 3/r.** Resolved, as follows.
- **Quote (KR p.5, read from the rendered page):**
  - (13) ds²₁₁ = (2R₀²/3z²)(−dt² + dx₁² + dx₂² + dx₃² + dz²) + (R₀²/6v²)(dx² + dv²) + (R₀²/4)dΩ₄²
  - (14) F̂₄ = 6R₀³Ω₄
  - The text says only "where dΩ₄² is the metric on S⁴"; Ω₄ is not defined in §3.2.
- **Quote (KR p.2):**
  - (1) 𝓛 = (1/2κ²₁₁)√g(R − (1/(2·4!))F_MNPQF^MNPQ) − (1/12⁴)ε A F F, i.e. the same normalization as PP/MR2, (1/2κ²)∫(R − ½|G|²).
  - (2) R_MN = (1/12)(F_MPQR F_N^PQR − (1/12)g_MN F²)
  - (4) F_mnpq = 6m₀ε_mnpq
  - (5) R_μν = −6m₀²g_μν, R_mn = 12m₀²g_mn
- **Checks (script; PROVED):**
  - (13) gives Ricci eigenvalues −6/R₀² (AdS₅), −6/R₀² (H²), +12/R₀² (S⁴). These are exactly (5) with **m₀ = 1/R₀**.
  - (2) then requires the orthonormal-frame amplitude q = 6m₀ = **6/R₀ = 3/r**, with r = R₀/2.
  - Matching L = 1/k gives R₀ = √6/(2k) = 2r = L₇ (the KK file's 7D Einstein radius). Then q = 2√6k = **q₀ exactly**: residual 0, and r = √6/(4k), ρ = 1/(2k).
  - At N = 4880: R₀ = 49.68438219 ℓ_P, and q·Vol(S⁴_r)/(2π)³ = 4880.000000.
  - KR's action normalization in (1) equals PP's, so the standard (2πℓ_P)³N quantization (PP 4660b73e A1) applies verbatim to KR's F.
- **Printed (14):**
  - Reading Ω₄ as the unit-S⁴ volume form (the only dimensionally consistent reading: coordinate components of a 4-form carry length³) gives frame amplitude 6R₀³/r⁴ = 96/R₀. That is **16× the value required by (2)+(13)**.
  - The correct unit-sphere coefficient is **F̂₄ = (3/8)R₀³Ω₄** (equivalently 6m₀·vol(S⁴_{R₀/2})). The factor 16 = 2⁴ is what results from using S⁴ radius R₀ instead of R₀/2.
  - Labels: "(14) as printed, with Ω₄ = unit volume form, is consistent with KR (2), (4), (13)" is **REFUTED** (the factor 16). That it is a misprint, rather than an unstated convention, is OPEN, since KR do not define Ω₄. "(D) agrees with KR's field equations (2), (4), (5), (13)" is **PROVED**.
- **Footnote on KR (10)** (MR2 observation, OPEN, irrelevant to (D)): R₀² = r/(6m₀²) for "H_r" is consistent with (5) only if H_r means the (r+1)-dimensional space with coordinates x₀…x_r. For the 2D H² of solution (vi), (5) gives ρ² = 1/(6m₀²) = R₀²/6, which matches (13).

**Q3. Pointwise norm (no b) or ∫_{M₇} (needs b)?**
- MR2 prefers the **pointwise** reading: Φ(p) = 4!·|G|²_{W₃₅,p}.
- Reason (PROVED): the EH equations L7a/L7b in which Φ appears are pointwise components of G_MN = T_MN. They contain the pointwise G·G, not an integral. On (D) Φ is constant, so the pointwise value is unambiguous.
- The integrated version ∫_{M₇}Φ·vol = 576k²·V₇eff needs the unfixed b (OPEN, PP 9dde377d B2). It is a different quantity with dimension ℓ_P⁵, so it cannot enter L7a.
- The choice belongs to the Owner (OPEN). MR2's recommendation is pointwise, with the integrated quantity named separately if wanted.

**Q4. Any literature map Λ⁴T*M₇ → a Hilbert modular space over ℚ(√35)?**
- None known to MR2, and none found in the pins used (MN, GM, BBBW, KR, NVvN, Bryant, HS).
- The isomorphism version is impossible by L-dim (PROVED).
- Any non-isomorphic map (projection, pairing, embedding) is **OPEN**, and MR2 proposes none, under the invention hold.
- Hilbert modular groups do appear elsewhere in string compactifications (e.g. T-duality groups of certain heterotic or Calabi–Yau moduli spaces). MR2 has **not** pinned any such case, and none concerns AdS₅×S⁴×Σ_g. So this is not offered as evidence.

**Q5. ln(6+√35) as the regulator of ℚ(√35); any use in the MR2 pins?**
- The side fact is **PROVED** (script):
  - The minimal Pell solution of x² − 35y² = 1 is (6,1).
  - x² − 35y² = −1 is unsolvable, since 7 | 35 and 7 ≡ 3 mod 4.
  - So 6+√35 is the fundamental unit, and the regulator is ln(6+√35) = 2.47788873029. This agrees with NL F1 §4.
- **No use** in any MR2 literature pin. The equality "35 = dim W₃₅ = discriminant parameter of ℚ(√35)" is a **numerical coincidence with no structural tie found**. Recording any identification would be invention, so it stays OPEN and is not proposed.

## 3. KR equations confirmed against (D) (task 3)
| (D) quantity (PP 4660b73e) | KR (13)–(14) with R₀ = √6/(2k) | match |
|---|---|---|
| L_AdS = 1/k | L² = 2R₀²/3 = 1/k² | PROVED |
| r = √6/(4k) | r² = R₀²/4 | PROVED |
| ρ = 1/(2k) | ρ² = R₀²/6 | PROVED |
| q₀ = 2√6k | q = 6m₀ = 6/R₀ (from KR (2), (4), (5)) | PROVED |
| q₀ via printed (14) | 96/R₀ (unit-Ω₄ reading) | REFUTED (factor 16; see Q2) |
| normalization | KR (1) = (1/2κ²)(R − ½\|G\|²) = PP | PROVED |
| N = 4880 | R₀ = 49.684382 ℓ_P; flux integer 4880.000000 | PROVED (CONDITIONAL on N chosen) |
| non-SUSY | KR p.3: (i)–(vi) "do not satisfy eq. (9)"; §3.2: finite-volume H₂/Γ preserves no SUSY | PROVED (cited) |
This upgrades MR2 map S1 and NL F3 §5.4 from "ratios match" to "metric and flux match KR's field equations".

## 4. KK report (7824e789) vs NL F3 / F1 (task 5)
**Consistent** (PROVED by comparing numbers and definitions):
- (D) is the KR (vi) direct product: KK §0, NL F3 §5.4, F1 §1.
- K_Σ = −4k² = −Φ/144 with Φ = 0.350004763: KK §3 and NL F3 §3.
- k = 0.0246505, L = 40.567128, r = 24.842191, ρ = 20.283564, Area = 5170.09355: KK §4 and NL F1 §3.
- a_D = 2.811512763×10¹⁰ and G₅: KK §4 and NL F3 §6.
- KK's L₇ = √6/(2k) = 49.684382 equals KR's R₀ (§3 above), which is a new consistency link.
- KK's 40 Wilson-line modes come from b₁(Σ₂) = 4 harmonic 1-forms. That is consistent with NL W-d, which concerns b₃ = 0 and not b₁.
- KK S6 (G has no Σ legs) agrees with NL §4: G sits only in the (0,4,0) block of W₃₅.

**Label difference:** D2 above. KK says "BF-unstable, PROVED [MR2-calc], pending PP audit"; NL says "C5 OPEN". There is no numerical conflict.

**New caveat for KK §3, from D4** (CONDITIONAL; affects only the cusped options):
- KK §3 states that the λ = 0 constant mode violates BF "for every Γ (cocompact or finite-area cusped)". That remains true, since the constant is L² on any finite-area surface.
- But for cusped Γ (such as F₂, or MR2 map P4's Σ_{2,61}), the Laplacian also has continuous spectrum λ_hyp ∈ [1/4, ∞) from Eisenstein series. That continuum overlaps KK's BF window λ_hyp < 1/3 on [1/4, 1/3).
- Those modes are not L²-normalizable on Σ, so whether they count as 5D BF-violating fields is **OPEN**.
- KK §3's OPEN item "count of eigenvalues in (1/4, 1/3)" is therefore, for cusped Γ, a continuum question rather than a count. For compact Σ₂ (the adopted case), KK §3 stands as written.
- KR's own "no KK modes on F₂" claim is REFUTED (D4) and should not be cited in support of a cusped option.

## 5. Status table (this file)
| item | label |
|---|---|
| NL F3/F1/F2 and KK hashes match the claims | PROVED |
| A1–A10 agreements | as in §1 (PROVED unless noted) |
| G₂ split of W₃₅ non-canonical (upgrade of MR2 M3) | PROVED (via NL example; 1/7 value CONDITIONAL on NL's log) |
| Q1: Φ = c·G·G satisfying L7a and lock together | REFUTED |
| Q1: Φ-2 adoption | OPEN (recommend reject) |
| Q2: (D) matches KR (1), (2), (4), (5), (13) | PROVED |
| Q2: KR (14) as printed (unit Ω₄) | REFUTED (factor 16); misprint interpretation OPEN |
| Q3: pointwise Φ is what L7a uses | PROVED; final choice OPEN (Owner) |
| Q4: map W₃₅ → Hilbert newspace | OPEN (isomorphism REFUTED by L-dim) |
| Q5: regulator side fact | PROVED; physical use OPEN / none found |
| KR "no L² eigenfunctions on F₂ except constant" | REFUTED (Maass form 1.1, R = 9.53369526) |
| KK vs NL consistency | PROVED (numbers); stability label difference pending PP audit |
| Continuum [1/4, ∞) in KK BF window for cusped Γ | OPEN |

## 6. Still for the Owner (in addition to MR2 map §10)
1. Adopt the name W₃₅ for Λ⁴T*M₇, keeping V₃₅ for the locked Hilbert newspace.
2. Choose pointwise Φ (recommended) or the integrated version, which needs b.
3. Reject or keep Φ-2.
4. If a cusped Σ (61 cusps, or F₂) is ever considered, the continuous-spectrum stability question in §4 must be addressed.

Tip 7cddb188 untouched. No CERT. Nothing sent outside. No Gemini. No agent messaged.
