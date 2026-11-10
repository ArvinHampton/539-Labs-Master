# MR2: KK spectrum of (D) = AdS₅×S⁴×Σ₂ vs the BF bound; verdict on the "probe instability √6/2 > 1" claim. 2026-11-09, ~15:30 CST (America/Chicago)
Agent: MR2 (Math Research 2). Authority: Owner's own words, t4294u, 15:13 CST (Physicist transcript pos 17862; record OWNER_WRITE_MAINCHAT_t4294_SIDECAR_KK_OPS_VERIF_P5a_2026-11-09_1515.md, item 2). Context records: blueprint 5a6e7177…; vacuum FINDINGS_PP_DERIVE_ADS5S4SIGMA_PARAMETERS_2026-11-09_1357.md (4660b73edc32…); RECORD 5b4592d4….
Limits: this is a new additive file and nothing existing was edited. Tip 7cddb188… untouched (re-hashed this turn). No CERT, no Gemini, nothing sent outside, no agent messaged. Public arXiv PDFs and abstracts only. Invention hold: the computations below are MR2's assembly of cited formulas and are marked [MR2-calc]; PP audit is pending.
Script: MR2_KK_SPECTRUM_ADS5_S4_SIGMA2_BF_BOUND_2026-11-09.py. Its log (.log) is reproducible, and both have sidecars.
Companion: MR2_11D_ADS5_S4_SIGMA2_TO_PHI_V35_MAP_PROPOSAL_2026-11-09.md (fd191d28…). Its numbers are reused and agree: k, L, Φ, a_D.
NL cross-check: no `NL_DERIVED_O4_KK_SPECTRUM_*` file existed at writing time (ls 15:2x CST), so there was nothing to compare.

## Rollup
PROVED 9 · CONDITIONAL 7 · OPEN 6 · REFUTED 0. Headline: **(D) is perturbatively BF-unstable.** The instability comes from the 14 of SO(5) at S⁴ level k=2, in its Σ-constant mode: m²L² = −16/3 < −4. It does not depend on N or g, and no choice of N or genus removes it.

## 0. Which solution is (D)? (PROVED, by inspection plus script §1)
- (D) is the **untwisted direct product**: ds² = AdS₅(L=1/k) + round S⁴(r=√6/4k) + Σ_g = H²/Γ (ρ=1/2k), with G₄ = q₀vol(S⁴) only and no warping or fibration.
- Its ratios L/ρ = 2 and L/r = 2√6/3 match **Kehagias–Russo hep-th/0003281 §3.2, eqs. (13)–(14)**, which is solution (vi) of their §2. KR state that it is non-SUSY, and say (p.3–4) that "a definite statement for the stability … needs a case-by-case study of the spectrum … not studied yet".
- It is **NOT** MN N=2, MN N=1 or BBBW. Those are warped, with a squashed S⁴ fibred over Σ through the topological twist (hep-th/0007018 §4; 1203.0303; 2011.04775 intro).
- Every MN/GM/BBBW spectrum below **does not apply directly to (D) (comparison only)**.
- Structural fact, PROVED by script §1: M₇ = AdS₅×Σ is Einstein with Ric = −6/L₇²·g, L₇ = √6/(2k) = 2r. So (D) is exactly the Freund–Rubin form M₇×S⁴ of AdS₇×S⁴, with AdS₇ replaced by the Einstein space AdS₅×H²/Γ (KR p.4: "replacing Hr by any Einstein space"). Also (L₅/L₇)² = 2/3.
- Equivalently, it is the 7D maximal SO(5) gauged-sugra vacuum (scalars at the SO(5) point, A=0, S₃=0) on the 7D Einstein space AdS₅×Σ.

## 1. Literature pins
- [P1] DeWolfe–Freedman–Gubser–Horowitz–Mitra hep-th/0105047.
  - §3 eqs. (3.31)–(3.33), coupled scalars (π, b, H).
  - §4 eq. (4.3)/(4.7): m²₋L² = (p−1)²/(q−1)²·k(k−q+1) and m²₊L² = (p−1)²/(q−1)²·(k+2(q−1))(k+q−1).
  - §4 special cases: the minus branch starts at k=2 on S^q, and the plus branch extends to k=0.
  - §5 (5.2): vectors. §8: φ^I modes.
  - Their scalar equations involve the external space only through □ₓ and its Einstein constant. That is the basis of C1 below.
- [P2] Kehagias–Russo hep-th/0003281, eqs. (10), (13), (14) and §6. The vacuum and the open stability question.
- [P3] Nastase–Vaman–van Nieuwenhuizen hep-th/9905075 and hep-th/9911238: consistent truncation of 11D on S⁴ to 7D maximal SO(5) gauged sugra. The 14 scalars have M²L₇² = −8 (Δ=4, the (2,0) stress-tensor multiplet). That agrees with [P1] (4.7) at k=2.
- [P4] Comparison only:
  - MN N=2 low-lying modes in the N=4 truncation: Cheung–Gauntlett–Rosen 1906.08900 §6.1. They are m²L² = −4, 12 (Δ=2,6); 5×0 (Δ=4); 6×5 (Δ=5); 2-forms Δ=3; vectors Δ=3,5. All satisfy BF, and −4 saturates it.
  - In the same paper, §6.2: the non-SUSY AdS₅ vacua of that truncation (S² case) violate BF (−6.92).
  - Universal (Σ-constant) KK sectors of MN1/BBBW: Bhattacharya–Katyal–Varela 2607.25952 and 2610.13938.
  - Trombone truncation on MN2: same authors, cited in 2607.25952.
  - Consistent truncations: Szepietowski 1209.3025; Cassani–Josza–Petrini–Waldram 2011.04775.
  - Spectrometry method: Malek–Samtleben 1911.12640.
  - No paper giving the full KK spectrum of MN1/MN2/BBBW (all Σ-harmonics) was found. Only universal or truncation sectors are published.
- [P5] Probe/nonperturbative: Seiberg–Witten hep-th/9903224; Maldacena–Michelson–Strominger hep-th/9812073 (fragmentation); Bena–Pilch–Warner 2003.02851 (brane-jets); Ooguri–Vafa 1610.01533 (conjecture); Martin–Reall 0810.2707 (non-SUSY AdS₅×KE₆, the analogous linear and 5-brane analysis).
- [P6] λ₁ on genus 2:
  - Kravchuk–Mazáč–Pal 2111.12716 abstract: λ₁ ≤ 3.8388976481 for all genus-2 surfaces.
  - Strohmaier–Uski 1110.2150: Bolza λ₁ ≈ 3.8388872588.
  - Fortier Bourque–Petri 2302.02540: LP bounds.
  - Otal–Rosas (Duke 2009): λ_{2g−2} > 1/4. For g=2 that means at most one nonzero eigenvalue ≤ 1/4. Cited from memory, not fetched this turn.
  - Small λ₁ under degeneration: Schoen–Wolpert–Yau / Buser. Cited, not fetched.
- [P7] Central charges, comparison: Gaiotto–Maldacena 0904.4466 eqs. (2.1) and (2.5); BBBW 1203.0303 eq. (2.21), with κ=−1.

## 2. Spectrum table (AdS₅ units, L = L₅ = 1/k)
Reduction rule [MR2-calc]: a 7D field with M²L₇² and Σ-harmonic eigenvalue λ_hyp (on the unit-curvature hyperbolic metric) has m²L₅² = (2/3)·M²L₇² + 4λ_hyp. So 5D BF (−4) corresponds to −6 in L₇ units, which is stricter than the 7D BF (−9).

| # | mode | spin | m²L² (or Δ) | BF / unitarity | label | source |
|---|---|---|---|---|---|---|
| S1 | S⁴ level k=2, coupled trace/flux scalar, **14** of SO(5), Σ-constant | 0 | **−16/3 = −5.3333**; Δ = 2 ± 2i/√3 | **VIOLATES** (−4) | **PROVED** [MR2-calc from P1 (4.7) and P3; 14 real modes, any g, any N] | script §2–3 |
| S2 | same, Σ-harmonics with eigenvalue λ_hyp | 0 | −16/3 + 4λ_hyp | violates iff **λ_hyp < 1/3** | PROVED (formula); the count is moduli-dependent, see §3 | script §3 |
| S3 | S⁴ k≥3 minus branch, e.g. k=3 (30) | 0 | 0 + 4λ_hyp (k=3); 32/3+… (k=4) | OK | CONDITIONAL (P1 equations on an Einstein, non-maximally-symmetric M₇; standard, not re-derived) | script §2 |
| S4 | plus branch k=0 (S⁴ breathing) | 0 | 48 (Δ = 2+2√13) | OK | PROVED (matches PP C3) | script §2 |
| S5 | Σ breathing (7D Einstein–Λ reduction) | 0 | 8 (Δ = 2+2√3) | OK | PROVED (matches PP C3) | script §4 |
| S6 | Teichmüller TT modes, 6g−6 = 6 real | 0 | 0 (Δ=4) | OK (flat directions, classically) | CONDITIONAL (linear order; G has no Σ legs, so no flux mixing) | script §4 |
| S7 | 5D graviton plus Σ tower | 2 | 4λ_hyp (0 for constant: massless) | unitary | PROVED (Lichnerowicz splits on an Einstein product with equal Ricci constants) | §2 text |
| S8 | SO(5) gauge vectors (10), Σ-constant | 1 | 0 (Δ=3) | unitary | CONDITIONAL (7D gauge fields with A=0 background) | P3 |
| S9 | Wilson-line scalars: 10 × 2g = 40 harmonic-1-form modes | 0 | 0 at linear order | OK | CONDITIONAL | P3 + Hodge |
| S10 | k≥1 plus branch (112, 160, … in L₇ units) | 0 | ≥ 74.7 | OK | CONDITIONAL | script §2 |
| S11 | 7D massive vectors, 2-/3-forms, gravitini, and their Σ-components (incl. coexact 1-forms, vol_Σ legs); S⁴ TT (φ^I) | 0–2 | not computed | — | **OPEN** | — |
| S12 | fermions | ½, 3/2 | not computed (irrelevant to BF) | — | OPEN | — |

No 5D field equation outside S11/S12 was solved beyond the formulas cited. The "full" spectrum is therefore **not** claimed: S11 and S12 are OPEN. Filling them in cannot restore stability, because S1 alone is enough to make (D) unstable.

## 3. Σ₂ harmonics vs BF, as a function of λ₁ (curvature −1 → (D) curvature K_Σ = −4k² = −Φ/144)
- **Check, PROVED:** −4k² = −0.00243058863 ℓ_p⁻² = −Φ/144 with Φ = 216(πN)^{−2/3} = 0.350004763 (the companion file's number).
- **Physical threshold, PROVED:** λ_phys < 4k²/3 = 8.1019621×10⁻⁴ ℓ_p⁻², equivalently λ_hyp < 1/3.
- **The λ=0 mode always violates the bound:** 14 modes for every g, every Γ (cocompact or finite-area cusped), and every N. **PROVED.**
- Unstable count = 14 × (1 + #{0 < λ_j,hyp < 1/3}).
- **Bolza and nearby surfaces: no extra modes. PROVED.** Here λ₁ ≈ 3.8389, so m²L² ≈ +10.022; the KMP upper bound gives +10.0223.
- **Surfaces near degeneration: CONDITIONAL on [P6] SWY/Buser.** There λ₁ → 0, so at least 14 more modes become unstable. By Otal–Rosas, at most one nonzero eigenvalue is ≤ 1/4 for g=2, which gives m²L² ≥ −13/3 for that one.
- **OPEN:** the number of genus-2 eigenvalues in (1/4, 1/3) as the moduli vary. The upper bound 3.8389 shows λ₁ is never large enough to matter for S1, which is the constant mode.

## 4. N- and g-dependence (standard (2πℓ_P)³N, N=4880, g=2; script §6)
- **PROVED:** all m²L² are pure numbers independent of N. g enters only through multiplicities (2g, 6g−6) and the moduli-dependent λ_j.
- **PROVED:** k = 0.0246505002 ℓ_p⁻¹, L₅ = 40.567128, L₇ = 49.684382, r = (πN)^{1/3} = 24.842191, ρ = 20.283564 (all in ℓ_p), Area(Σ₂) = 5170.09355 ℓ_p². These match PP 4660b73e and the companion file.
- **PROVED, as a formula:** a_D = c_D = πL³/8G₅ = (2/3)^{7/2}(g−1)N³ = (8√6/81)(g−1)N³ = 2.811512763×10¹⁰.
  - Calibrations: L₇⁵/G₇ = 16N³/3π² reproduced to 12 digits; this agrees with the companion file.
  - Physical meaning is **CONDITIONAL** on a dual CFT existing, which S1 undermines.
- Comparison only (not (D)):
  - MN N=2: exact GM a = 3.873809006×10¹⁰ and c = 3.873808985×10¹⁰.
  - MN N=1: large-N 9/32·N³ = 3.2685×10¹⁰.
- **CONDITIONAL:** sugra validity. (ℓ_p/r)⁶ = 4.3×10⁻⁹ and (ℓ_p/L)⁶ = 2.2×10⁻¹⁰. Higher-derivative and 1/N corrections are therefore O(10⁻⁹), and cannot close the gap −16/3 → −4 (ΔM²L² = 4/3). This requires the systole of Σ in ℓ_p ≫ 1; Bolza's systole is ≈3.06, giving ≈62 ℓ_p.
- **OPEN:** 1/N corrections to a and c for (D).

## 5. Verdict on PP's "probe instability √6/2 > 1"
- **Where it appears:** 4660b73e §(c) C4 (lines 66–70) and B6; summarised in bridges/AUDITOR/AUDITOR_ADVANCEMENTS_SINCE_RTA_V17_REPORT_2026-11-09.md L129; cited as S4 in the companion map file.
- **What it asserts:** a probe M5 on ℝ^{1,3}×Σ_g, at fixed Poincaré y and a point of S⁴, has WZ charge/tension = q₀/(4k) = √6/2. The potential ∝ (1−√6/2)e^{−4ky}·Area is unbounded below toward the boundary, so M5 nucleation makes (D) non-perturbatively unstable.
- **V1 (PROVED, reproduced):**
  - q₀/(4k) = √6/2 = 1.2247449. The AdS₇ calibration gives 1.
  - General closed form [MR2-calc]: for AdS_{d+1}×H^{6−d}×S⁴, charge/tension = √(6/d), which is > 1 for every d < 6.
  - The C₃∧G term vanishes (7 legs on S⁴) and the pull-back of G to the worldvolume is 0. So the computation is consistent.
- **V2 (CONDITIONAL; probe limit, no backreaction, T₅ normalised by the AdS₇ BPS calibration):** charge > tension for a codimension-1 brane in AdS is the Seiberg–Witten / MMS large-brane instability ([P5]). It is consistent with Ooguri–Vafa, which remains a conjecture.
  - Minor citation note: the mechanism here is the SW/MMS type. BPW's "brane-jet" pin is about warped uplifts, so it is a looser fit, though BPW say such instabilities "can arise in any non-SUSY AdS vacuum".
- **V3 (PROVED):** the claim is not refuted, and it is superseded in severity. (D) is already perturbatively unstable (S1). PP's own "perturbative stability OPEN beyond the 2-modulus truncation" is resolved: **UNSTABLE**.
  - This does not contradict PP C3: the BF-violating mode lives at S⁴ level k=2, outside the volume-moduli truncation.
  - The S⁴/Σ volume-mixing modes (48, 8) are confirmed positive.
- **B6 (CONDITIONAL):** "N drops by one per emitted M5". Standard, because the brane links S⁴; not recomputed.

## 6. Status table
| item | label |
|---|---|
| (D) = KR (vi) untwisted product, not MN/BBBW | PROVED |
| (D) is an Einstein-M₇ Freund–Rubin / 7D-sugra vacuum, L₇ = 2r | PROVED |
| 14 BF-violating scalars, m²L² = −16/3 (any N, g) | PROVED [MR2-calc; PP audit] |
| extra unstable modes iff λ_hyp < 1/3; none for Bolza | PROVED |
| extra modes near degeneration | CONDITIONAL (SWY/Buser pins) |
| count of eigenvalues in (1/4, 1/3) | OPEN |
| breathing 48, Σ-breathing 8 | PROVED |
| higher-k scalars, Teichmüller, vectors, Wilson lines | CONDITIONAL |
| other spins / form sectors / fermions | OPEN |
| √6/2 arithmetic | PROVED |
| √6/2 ⇒ nucleation instability | CONDITIONAL (probe) |
| a_D = (8√6/81)(g−1)N³ = 2.8115×10¹⁰ | PROVED (formula); CFT meaning CONDITIONAL |
| 1/N corrections; full MN KK spectra in literature | OPEN |
| MN/GM/BBBW numbers | comparison only; do not apply directly to (D) |

## 7. Still open / Owner decisions
1. Accept (D) as **perturbatively unstable**, or replace it with a SUSY twisted solution (MN N=2/N=1/BBBW), which is BF-stable by SUSY. Any replacement needs a new Owner adoption (PP 4660b73e, decision 4).
2. Is there a stabilising Γ or quotient? **No.** The constant mode exists on every finite-area Σ.
3. The S11/S12 sectors (forms, fermions, Σ-components of massive 7D fields) are OPEN. They can only add instabilities, not remove S1.
