# MR2 label fixes for the O1 map, per PP audit 2b0a4125: supersedes labels in fd191d28 where stated. 2026-11-09, ~15:40 CST (America/Chicago)
Agent: MR2 (Math Research 2). Citation/literature-only; invention HOLD. Authority: OW 5a6e717732c413a39c89d9b95c9b17455ecf4da8dd64e8bb9d879f427e6a845c.
Audit read in full: reports/FINDINGS_PP_AUDIT_MR2_ADS5S4SIGMA2_PHI_V35_MAP_2026-11-09_1530.md, sha256 2b0a41259414d006ac3c2c784cab6170cae1810c6dd4bd1dc5ba7b35b759392a (recomputed; MATCH with its sidecar; 105 lines).
Target (unchanged, not edited): MR2_11D_ADS5_S4_SIGMA2_TO_PHI_V35_MAP_PROPOSAL_2026-11-09.md, sha256 fd191d28fb1aa40f974bb2f6df5ff3150984f88803907d534668d7b771ff733f. Companion cross-check: MR2_CROSSCHECK_NL_F3_O1_W35_MAP_2026-11-09.md, sha256 9354fe2a1b30a9965eba529d94c8b9fcb1e4a77eae17e8c3bd5f86ad5b20580a.
Limits: new additive file only. Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 untouched (re-hashed). No CERT, no Gemini, nothing sent outside, no agent messaged.

## 0. Rules for reading fd191d28 from now on
- **Symbol.** Every occurrence of "V₃₅" in fd191d28 that means the geometric space Λ⁴T*M₇ (P-V35-a, M1–M3, §7 A1/A2, §8, §9, §10) is to be read as **W₃₅**. The Owner-locked **V₃₅** (OW e4ef0a81 / LOCK c290a274: the dim-14 Hilbert newspace over ℚ(√35)) is **untouched and not renamed**. fd191d28 §2 row "V₃₅ (number-theory sense)" and §7 A8 refer to the Owner's V₃₅, unchanged.
- **Labels.** The table in §3 below **supersedes** fd191d28 §8 and the inline labels of S1, S2, M3, A3 and A4. Everything else in fd191d28 stands, including every number (PP N1: all match to ≥ 7 digits; PP H2: the log is byte-identical on re-run).

## 1. PP's five fixes: each checked
1. **S1 split. AGREE.**
   - "(D) is the KR solution, as a solution" is **PROVED**. PP D1 computes the Ricci tensor from the metric and checks all 121 Einstein components, dG = 0 and d*G = 0. MR2's script had entered the Ricci eigenvalues by hand (PP caveat H1), so D1 closes that gap. MR2's cross-check 9354fe2a §3 independently matches KR (2), (4), (5) and (13) with m₀ = 1/R₀, R₀ = √6/(2k).
   - The attribution to KR's printed text is **CONDITIONAL** (citation).
   - The printed KR (14) is a separate item, S1c below.
2. **S2 → CONDITIONAL. AGREE.** "MN/GM ≠ (D)" depends on the MN/GM metrics as printed: MN eqs. (22), (28), (29); GM (2.7). It is a citation-based claim. MR2 did fetch and pin those equations, but by the shared rule a literature claim is CONDITIONAL. No mathematical change.
3. **M3. AGREE, with one extra argument.**
   - (a) Existence of a G₂-structure: **CONDITIONAL**. It rests on the cited theorem (Gray; Bryant ~L461) that an orientable spin 7-manifold admits a G₂-structure.
   - (b) **New: no torsion-free G₂-structure induces the (D) metric on M₇ — PROVED.** I checked it two ways:
     - PP's argument: the holonomy of the Riemannian product ℝ_y×S⁴_r×Σ₂ is {1}×SO(4)×SO(2). That has rank 0+2+1 = 3, while G₂ has rank 2. So Hol ⊄ G₂, and by the holonomy principle no parallel (torsion-free) φ compatible with the metric exists. This proof is self-contained, using only rank and the product-holonomy decomposition.
     - The check requested in the brief: torsion-free G₂ ⇒ Ricci-flat (Bonan, cited). The induced M₇ metric dy² + r²dΩ₄² + ρ²ds²_Σ has Ric = 0 on y, +8k² on S⁴ and −4k² on Σ, so it is not Ricci-flat. This gives the same conclusion, but it is CONDITIONAL on Bonan's theorem; the rank argument is what carries PROVED.
   - (c) **Frame-dependence of the 1+7+27 split — PROVED.** NL 965de066 §4, PP V4 (pp_g2.log) and MR2 9354fe2a A6 agree. ∗φ has 7 decomposable terms, so the singlet fraction ⟨α,∗φ⟩²/7 is 1/7 on 7 coordinate 4-planes and 0 on the other 28.
   - Net: the fd191d28 M3 wording "canonicity OPEN" is replaced by M3b/M3c, both PROVED.
4. **A4 → CONDITIONAL. AGREE.** The counts 14 / 10 / 5 come from the NVvN field content (hep-th/9905075, ~L191–200), which is a citation.
5. **A3. AGREE.** The argument is replaced.
   - fd191d28 said "11 = 5+6, not 4+7". PP is right that, as worded, this clashes with MR2's own M1 split x^μ(4) | M₇(7).
   - What was meant is that the *compact* internal space is 6D, because M₇ contains the non-compact y. That was never stated, so the stated argument is invalid as written and is withdrawn.
   - New argument (NL; checked in 9354fe2a A8): b₃(S⁴×Σ₂) = 0 by Künneth, from b(S⁴) = (1,0,0,0,1) and b(Σ₂) = (1,4,1). So **"35 massless C₃ moduli on (D)" is REFUTED.** The broader "E₇₍₇₎/SU(8) structure applies" is **OPEN**. The arithmetic 70 = 28+35+7 = 35+35 stays PROVED.

## 2. PP's additional results: noted and accepted
- **F4 (accepted; checked).** No scalar Φ makes EH (alg)+(EH-lock) hold on (D):
  - G_ext = −6k² is definition-free;
  - alg-1 forces Φ = 576k², while the lock forces Φ = 1728k²;
  - EH's own left side 6k² − 3K at K = 8k² gives −18k² ≠ −6k².
  - Recorded as the claim "some Φ makes the EH system hold on (D)": **REFUTED** (M6b). This strengthens fd191d28 M6, which was only under P-Φ-a, and agrees with MR2 9354fe2a Q1(b).
- **F5 (accepted).** fd191d28 "the external coefficient −1/96 does match" means only the relation G_ext = −Φ/96 under P-Φ-a. EH's formula G_ext = 6k² − 3K does not hold on (D).
- **V2 (accepted; checked).** The six blocks are the bidegree decomposition, not irreducibles:
  - (0,2,2) = Λ²ℝ⁴ = Λ²₊ ⊕ Λ²₋ = 3+3;
  - (1,2,1) = (3+3)⊗ℝ² = 6+6, each real-irreducible because ℝ² is real-irreducible for SO(2);
  - (1,3,0) = 4, (0,3,1) = 4⊗ℝ² = 8 and (1,1,2) = 4 are irreducible.
  - Real irreducible split: 1+4+8+3+3+6+6+4 = 35. fd191d28 "SO(4)×SO(2) splitting" should read "**bidegree split**".
- **V3 (accepted, OPEN).** ℝ_y comes from the Poincaré/RS slicing, and SO(2,4) mixes y with x^μ, so W₃₅ as defined depends on the slicing. Φ is an 11D scalar and does not.
- **KR (14) reading (accepted).** PP: (14) matches (D) only if Ω₄ := vol(unit S⁴)/16, i.e. 6m₀·vol(S⁴_{R₀/2}). The correct unit-sphere form is G = (3/8)R₀³·vol(unit S⁴). This is the same factor 16 = (R₀/r)⁴ found in MR2 9354fe2a Q2.
  - Label harmonization: as a precise claim, "(14) with Ω₄ = unit-S⁴ volume form satisfies KR (2)/(13)" is REFUTED (S1c).
  - Whether this is a misprint or an unstated convention is OPEN. PP calls it a convention, and MR2 does not dispute that reading.
  - It does not affect S1a.
- **N2 (accepted).** a = c ∝ k⁻⁹, so the value is very sensitive to normalization. Only the standard normalization is admissible (the EH normalization is refuted by Dirac pairing, PP 4660b73e A3), so 2.8115×10¹⁰ is the only value quoted.
- **§7 handoff (noted).** The KK file 7824e789 is audited separately. The derivations must not use maximal symmetry of AdS₇.

## 3. Superseding status table (one label per row; replaces fd191d28 §8)
| ID | statement | label |
|---|---|---|
| S1a | (D) is the Kehagias–Russo solution: metric and flux solve the 11D equations exactly, and the radius ratios match (PP D1 from the metric; MR2 cross-check 9354fe2a §3) | PROVED |
| S1b | Attribution to KR's printed text (eqs. (1), (2), (4), (5), (13); non-SUSY statement p.3 and §3.2) | CONDITIONAL |
| S1c | KR (14) "F̂₄ = 6R₀³Ω₄" read with Ω₄ = unit-S⁴ volume form solves KR (2)/(13). It does not: the amplitude is 96/R₀ against the required 6/R₀. It is consistent iff Ω₄ := vol(unit S⁴)/16. Misprint vs convention: OPEN | REFUTED |
| S2 | MN/GM geometry ≠ (D): fibred, squashed, warped, SUSY (citation-based) | CONDITIONAL |
| S3 | MN/GM a, c apply to (D) | CONDITIONAL |
| S4 | (D) unstable: probe-M5 charge/tension √6/2 > 1 (PP C4, probe level). BF-instability is in MR2 KK 7824e789, pending PP audit | CONDITIONAL |
| M1a | dim W₃₅ = dim Λ⁴T*_pM₇ = 35, M₇ = ℝ_y×S⁴×Σ₂; G ∈ Γ(Λ⁴T*M₇) | PROVED |
| M1b | Owner adoption of W₃₅ as the EH "V₃₅" object | OPEN |
| M2a | Bidegree split (y,S⁴,Σ) = 1+4+8+6+12+4; G in the (0,4,0) block; exactly 1 of 35 frame components nonzero | PROVED |
| M2b | Real irreducible SO(4)×SO(2) refinement: 1+4+8+(3+3)+(6+6)+4 | PROVED |
| M2c | W₃₅ depends on the Poincaré/RS slicing (ℝ_y is not SO(2,4)-invariant); Φ itself is slicing-independent | OPEN |
| M3a | Existence of some G₂-structure on M₇ (orientable + spin ⇒ G₂-structure; Gray / Bryant ~L461) | CONDITIONAL |
| M3b | No torsion-free G₂-structure induces the (D) metric on M₇ | PROVED |
| M3c | The 1+7+27 split of G depends on the chosen φ / frame (singlet fraction 1/7 on 7 of 35 coordinate 4-planes, 0 on 28) | PROVED |
| M4 | Φ := G_MNPQG^MNPQ (P-Φ-a) adopted as the EH Φ | OPEN |
| M5 | On (D): G_AdS = G_Σ = −Φ/96, G_S⁴ = +Φ/96, Φ = 576k², k² = Φ/576, Ric_S⁴ = Φ/72, K_Σ = −Φ/144 (given P-Φ-a) | PROVED |
| M6a | Under P-Φ-a, EH "G_fib − G_ext = Φ/144" (fibre S⁴, Σ or averaged) and "k² = Φ/1728" hold on (D) | REFUTED |
| M6b | Some scalar Φ makes the EH system (alg)+(EH-lock) hold on (D) (PP F4: alg-1 forces 576k², the lock forces 1728k²; also 6k²−3K at K = 8k² gives −18k² ≠ −6k²) | REFUTED |
| M7 | Φ(N) = 216(πN)^{−2/3}; Φ(4880) = 0.350004763 ℓ_P⁻² (on P-Φ-a, (D), chosen N) | CONDITIONAL |
| M8a | G₅ = 9π²/(4(g−1)N²); πL³/(8G₅) = (8√6/81)(g−1)N³ = 3(g−1)/(1024π³k⁹) (algebra; PP N1 all digits) | PROVED |
| M8b | Holographic reading a = c (Henningson–Skenderis / GM (2.8) formula; dual CFT existence) | CONDITIONAL |
| M8c | 4D Newton constant G₄ (needs brane separation b) | OPEN |
| P1 | The project's "61" = punctures of Σ | OPEN |
| P2 | g = 2 puts no upper bound on n; at n = 61, 2g−2+n = 63 and 3g−3+n = 64 | PROVED |
| P3 | 61 maximal punctures (class S, MN-type geometry): a ≈ 1.220099×10¹², c ≈ 1.220129×10¹² | CONDITIONAL |
| P4 | 61 cusps on (D): Area 162857.95 ℓ_P², a_D ≈ 8.856×10¹¹. KK/continuum stability is OPEN (cross-check 9354fe2a §4) | CONDITIONAL |
| P5 | Meaning of "limit" | OPEN |
| A1 | Λ⁴(ℝ⁷) ≅ 1+7+27 under G₂ (Bryant §2.6, eqs. (2.13)/(2.25), proof given there; dims checked) | PROVED |
| A3a | "35 massless C₃ axion moduli on (D)": b₃(S⁴×Σ₂) = 0 by Künneth (Betti numbers 1,4,1,0,1,4,1) | REFUTED |
| A3b | A broader E₇₍₇₎/SU(8) structure applies to (D) | OPEN |
| A3c | Arithmetic: 70 = 28+35+7; Λ⁴ℝ⁸ = Λ⁴ℝ⁷ ⊕ Λ³ℝ⁷ = 35+35 | PROVED |
| A4 | No 35-dim multiplet in the 7D SO(5) gauged-sugra fields (14, 10, 5; NVvN field content cited) | CONDITIONAL |
| A5a | SO(5) irreps of dim 35 are (4,0) and (2,1) (Weyl formula) | PROVED |
| A5b | A 35 or 35′ occurs in the S⁴ KK spectrum of (D)/MN | OPEN |
| A6 | Relevance of SL(6), SU(6), Sym²₀(ℝ⁸) (dim 35) to AdS₅×S⁴×Σ_g | OPEN |
| A7 | A 35-dim object inside the MN/GM AdS₅ solutions | OPEN |
| A8 | W₃₅ ≅ V₃₅ (Owner lock, dim 14) as vector spaces | REFUTED |

**Changed vs fd191d28:**
- S1 is split into S1a PROVED, S1b CONDITIONAL and S1c REFUTED; S1c comes from 9354fe2a and PP D2.
- S2: PROVED → CONDITIONAL.
- S4 is relabelled CONDITIONAL. It is a cited result at probe level.
- M1 is split into M1a (dimension, PROVED) and M1b (adoption, OPEN).
- M2b and M2c are new.
- M3 is split: M3a CONDITIONAL; M3b and M3c new, both PROVED.
- M6b is new (PP F4).
- M8 is split: M8a PROVED, M8b CONDITIONAL, M8c OPEN.
- A3 is replaced by A3a REFUTED (b₃ = 0), A3b OPEN and A3c PROVED.
- A4: PROVED/REFUTED-by-count → CONDITIONAL.
- A5 is split into A5a PROVED and A5b OPEN.
- A8: W₃₅ ≇ V₃₅ is REFUTED (dim 35 vs 14). This is the L-dim argument; RTA dim 36 is CONDITIONAL on the corpus and is not used.

## 4. Updated rollup (this table; 37 rows)
**PROVED 12 · CONDITIONAL 10 · OPEN 10 · REFUTED 5.**

PP's rollup (17/7/3/2) counts PP's own audit items, so it is not row-for-row comparable. PP found no numeric mismatch, and no disagreement remains between MR2, PP and NL on any label above.

## 5. Owner definitions still required (unchanged from fd191d28 §10, with symbols updated)
1. Φ: adopt P-Φ-a, or not. By M6b, no choice of Φ rescues the EH system on (D).
2. W₃₅: adopt the name and object Λ⁴T*M₇, and accept or replace its slicing-dependence (M2c). Also say whether "evaluated across" means the pointwise norm, which MR2 recommends, or the integrated version, which needs b.
3. A G₂-structure φ, only if the 1+7+27 reading is wanted. It cannot be torsion-free (M3b).
4. The meaning of the 61-puncture limit: maximal punctures, cusps, or the T₃ branch count.
5. Keep (D), or switch to MN/BBBW.
6. b, if G₄ is wanted.

Tip 7cddb188 untouched. No CERT. Nothing sent outside. No Gemini. No agent messaged. fd191d28 and the Owner's V₃₅ unchanged.
