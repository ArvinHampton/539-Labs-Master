# NL DERIVED (F3, O1): proposed 11D → Φ map and a geometric 35-dim candidate W₃₅, evaluated on S⁴×Σ₂, with cross-check of MR2, 2026-11-09
Author: Non Local Path (NL). New dated file; nothing edited. Tip 7cddb188… untouched. No CERT. Nothing sent outside.
Authority: OW 5a6e717732c413a39c89d9b95c9b17455ecf4da8dd64e8bb9d879f427e6a845c (NL O1, joint with MR2). Vacuum (D): OW 7708ec5d / RECORD 5b4592d4; parameters PP 4660b73e, 4d07bd1b, 9dde377d.
MR2 file addressed: MR2_11D_ADS5_S4_SIGMA2_TO_PHI_V35_MAP_PROPOSAL_2026-11-09.md, sha256 fd191d28fb1aa40f974bb2f6df5ff3150984f88803907d534668d7b771ff733f; script …PHI_V35_CHECK_2026-11-09.py 62be2fa1…, log cf7b9833… (sidecars match).
NL scripts: /workspace/nl-1511/f3_phi_v35.py (8dbe5ba4…, log 2f70ab85…), f3_extra.py-inline (log f3_extra.log 656544ff…), and f1_teh_vacuum.py (F1).
Conventions: PP's (G_MN = T_std(G), standard field G quantized as (2πℓ_P)³N). The O5 form is related by T^(EH) = 2T_std (F1 §2).
Every candidate below is an **NL derived proposal**, CONDITIONAL on OW 5a6e7177 and on Owner adoption. C5 (non-SUSY stability, Ooguri–Vafa) stays OPEN.

## 0. Name collision (rule for this file)
The Owner-locked **V₃₅** is the full adelic level-1 parallel-weight [2,2] cuspidal Hilbert newspace over ℚ(√35), dimension 14, all four Cl⁺ components (OW e4ef0a810d1be98f9995c3120cc60954b6120632419a6f443cf451cef2c09f3e; parent LOCK c290a274…, which also says "35 names the field, not the dimension"). This file does **not** reuse that symbol. The geometric 35-dimensional candidate is called **W₃₅**.

## 1. Corpus definitions found (rg across /workspace)
| symbol | source | content | status |
|---|---|---|---|
| Φ (EH) | nonlocal/Einstein_Hampton_Equation_Rewrite_Appendix_2026-09-28.txt (08b8541a…) §3 | appears only in (alg): 6k²−3K = −Φ/96, 4k²+K = Φ/144 ⇒ k² = Φ/1728, K = 8k² | not defined there |
| Φ := 8πG₁₁·G² | grok_export/qc-chats/cd250095-2abb-4dee-b86a-e4481020d5ef.md L1524 (chat export, not Owner text) | flux-squared scalar with κ² = 8πG₁₁ | corpus reading; not adopted |
| Φ (homonyms) | Zenodo 18586411 / 17812645 (scalar field Φ(x^μ,x⁵) with g₁₁Φψ̄ψ); RTA Thms 11.6–11.7 (period function); 9dde377d Part A (tree map Φ: T₃ → Hⁿ) | different objects | not the EH Φ |
| V₃₅ (RTA) | RTA Def. 33.2 (rta-o3-read.txt f7d5ead2… L6388; also v12/v17 texts) | complex span of the 105 functions K₂μ, K₃μ, K₄μ (μ ∈ D, \|D\| = 35); Prop. 33.6: dim = 36 | corpus definition |
| V₃₅ (Owner lock) | OW e4ef0a81, LOCK c290a274 | Hilbert newspace over ℚ(√35), dim 14 | Owner-LOCKED |
| "Φ evaluated across V₃₅" | Owner DEF2 as relayed (NL 1232 item 20; NL 76e63cc2) | no definition of "across" | OPEN |

**L-dim (REFUTED by proof).** "W₃₅ ≅ V₃₅ as vector spaces", for either corpus V₃₅: dim W₃₅ = 35, while dim V₃₅ = 14 (Owner lock) and dim V₃₅ = 36 (RTA Def. 33.2). A linear isomorphism needs equal dimension. So any relation between W₃₅ and the locked V₃₅ can only be a non-isomorphic map (a projection, an embedding or a pairing), and whether such a map exists or means anything is **OPEN**.

## 2. Φ candidates on (D)
On (D): G^M_M = −6k² (AdS₅ including y), +6k² (S⁴), −6k² (Σ₂); q₀ = 2√6k; G² = 24q₀² (F1, sympy).
- **Φ-1 := G_MNPQG^MNPQ (sugra normalization) = κ²G² in the κ-explicit EH form = 2κ²F² in the O5 form (F = G/(√2κ)).** On (D), Φ-1 = 576k² (PROVED). This is the same proposal as MR2 M4 (P-Φ-a); the O5 equivalence matches MR2's "16πG₁₁F²" since 2κ² = 16πG₁₁.
- **Φ-3 := −96·G_ext** (the Φ that makes L7's first equation hold on (D)) = 576k² = Φ-1 (PROVED). So L7a, G_ext = −Φ/96, holds on (D) exactly when Φ is the flux square. This is an internal-consistency pass.
- **Φ-2 := 1728k²** (relabel k so that the old lock holds). Then Φ-2 = 3·G², and L7a fails: G_ext + Φ-2/96 = 12k² ≠ 0 (PROVED). Φ-2 is a convention that is inconsistent with L7a, so NL does not propose it.
- **Numbers (CONDITIONAL on N = 4880, g = 2 inputs):** Φ-1(N) = 216(πN)^{−2/3} ℓ_P⁻² = 0.350005 ℓ_P⁻² (agrees with MR2 M7).

## 3. Old L7 relations on (D) with Φ = Φ-1
| relation | value on (D) | label |
|---|---|---|
| L7a G_ext = −Φ/96 | holds | PROVED |
| L7b G_fib − G_ext = Φ/144, fibre = S⁴ | Φ/48 | REFUTED by proof |
| L7b with fibre = Σ₂ | 0 | REFUTED by proof |
| L7b with fibre-averaged G (6D trace/6 = 2k²) | Φ/72 | REFUTED by proof |
| lock k² = Φ/1728 | k² = Φ/576 (ratio 3) | REFUTED by proof |
| lock K = 8k² | holds as the S⁴ Ricci eigenvalue | PROVED |
| Gauss curvature K_Σ = −Φ/144 | holds | PROVED |
- No Einstein-block difference on (D) equals Φ/144; the number 1/144 occurs only as K_Σ/Φ. Reading the old 1/144 as K_Σ would be a new identification, OPEN and not proposed.
- Reason (PROVED, 4d07bd1b): (alg) assumes one 6D Einstein fibre, and S⁴×Σ₂ is not Einstein (Ric 8k² vs −4k²).

## 4. Geometric 35-dimensional candidates (W₃₅)
- **W-a (NL proposal, same as MR2 M1):** W₃₅|_p := Λ⁴T*_pM₇ with M₇ = ℝ_y × S⁴ × Σ₂, the 7D space transverse to the brane worldvolume. dim = C(7,4) = 35 (PROVED). G ∈ Γ(Λ⁴T*M₇) by construction (G has no x^μ legs), so Φ-1 = 4!·|G|²_{W₃₅}: "Φ evaluated across W₃₅" = the pointwise Λ⁴ norm summed over the 35 frame components.
  - Of the 35 orthonormal-frame components, exactly one is nonzero on (D): the S⁴ volume component q₀ (PROVED).
  - SO(4)×SO(2) split by degrees (y, S⁴, Σ): (0,4,0)=1, (1,3,0)=4, (0,3,1)=8, (0,2,2)=6, (1,2,1)=12, (1,1,2)=4; sum 35 (PROVED; agrees with MR2 M2). G sits in the 1-dim block.
  - Evaluated on S⁴×Σ₂ with the y-integral, an integrated version ∫_{M₇}Φ-1·vol = 576k²·V₇eff needs b (OPEN; F1 §3).
- **W-b (alternative):** M₇' = S⁴ × Σ₂ × S¹_y (y compactified, orbifold or circle). Pointwise identical to W-a (PROVED); differs only in the y-integral, where 9dde377d's interval form must be replaced. Not preferred: the adopted junction set-up has faces at y = 0 and y = b, i.e. an interval.
- **W-c (rejected):** Λ⁴ of the 6D internal space only: dim C(6,4) = 15 ≠ 35 (PROVED). Λ³(ℝ⁶) = 20.
- **W-d (rejected for (D)):** 35 C₃ axions. Harmonic 3-forms on S⁴×Σ₂: b₃ = 0 (Künneth, b = 1,4,1,0,1,4,1) (PROVED). So no 35 massless 3-form moduli on (D); the T⁷ count 35 = Λ³ℝ⁷ does not apply (agrees with MR2 A3).
- **G₂ reading (PROVED: not canonical).** For a decomposable S⁴ 4-form, the Λ⁴₁ (G₂-singlet) fraction relative to the standard φ is 1/7 when the S⁴ legs sit on frame directions {1,2,3,4} and 0 when they sit on {0,1,2,3} (NL f3 log). So the 1+7+27 split of G depends on the G₂-structure chosen, consistent with MR2 M3 "canonicity OPEN". If the Owner wants a G₂ reading, φ must be supplied.

## 5. Answers to MR2 §9 (MR2 fd191d28…)
1. **Φ and its normalization.** Agree. NL Φ-1 = MR2 M4: Φ = G·G in sugra normalization = 2κ²F² = 16πG₁₁F² in the O5 form, and Φ = 576k², not 1728k². The O5 vs sugra relation is T^(EH) = 2T_std (NL F1 §2). Factor 576 vs 1728: the ratio 3 is exact; restoring 1728 needs Φ-2, which breaks L7a (§2).
2. **Where W₃₅ lives.** On M₇ = ℝ_y × S⁴ × Σ₂ (with y), as MR2 M1. On the 6D internal space it has dim 15 (W-c).
3. **Split.** The canonical SO(4)×SO(2) split (MR2 M2; NL count agrees). NL proves the G₂ split is frame-dependent (§4) and does not use it without an Owner φ.
4. **(D) as Kehagias–Russo.** Yes. NL treats (D) as the direct product, not MN. Independent check (sympy): MR2's quoted KR ratios L² = 2R₀²/3, ρ² = R₀²/6, r² = R₀²/4 give L/ρ = 2, L/r = 2√6/3 = √(8/3), r·k = √6/4, ρ·k = 1/2, exactly (D) (PROVED for the ratios). NL did not fetch hep-th/0003281, so the equation numbers (13)–(14) and the flux amplitude in KR's own convention are taken on MR2's citation, not independently checked.

## 6. MR2 claims verified independently
| MR2 claim | NL check | verdict |
|---|---|---|
| M5: G_AdS = G_Σ = −Φ/96, G_S⁴ = +Φ/96, Φ = 576k², k² = Φ/576 | sympy 11D tensor (F1) + f3 log | CONFIRMED (PROVED) |
| M6: fib − ext = Φ/48, not Φ/144; k² = Φ/576, not Φ/1728; old forms REFUTED | §3 (also Σ and averaged fibre fail) | CONFIRMED (REFUTED-by-proof stands) |
| "only K_Σ = −Φ/144 holds" (the only place 1/144 appears) | §3: no block difference equals Φ/144; K_Σ = −4k² = −Φ/144 | CONFIRMED |
| S1: (D) = KR non-SUSY product | ratios only (§5 item 4) | ratios CONFIRMED; citation details not independently checked |
| M8: G₅ = 9π²/(4(g−1)N²) | F1: G₅ = 9.32487×10⁻⁷ ℓ_P³ at N = 4880, g = 2 | CONFIRMED (numeric) |
| M8: a_D = c_D = πL³/(8G₅) = (8√6/81)(g−1)N³ | recomputed: 2.81151×10¹⁰ both ways | arithmetic CONFIRMED; holographic reading CONDITIONAL (MR2 S4, PP C4) |
| M2 block count 35 | recomputed | CONFIRMED |
| A3 (E₇/SU(8) 35+35 does not apply to (D)) | b₃(S⁴×Σ₂) = 0 and 11 = 5+6 | CONFIRMED |
NL did not check MR2 §6 (61 punctures) or the class-S numbers in §5/§6; they are outside this go.

## 7. For MR2 cross-check (questions)
1. Do you accept Φ-2 (1728k²) as REFUTED for L7a, or do you prefer to keep it as a pure convention labeled inconsistent with L7a?
2. Can you confirm from KR's text the flux amplitude F̂₄ = 6R₀³Ω₄ in their normalization against q₀ = 2√6k = 3/r here? (NL finds a convention-dependent factor and did not resolve it.)
3. For an integrated "Φ across W₃₅", do you prefer the pointwise norm (no b needed) or ∫_{M₇} (needs b)?
4. Do you know any literature map from Λ⁴T*M₇ data to a Hilbert modular space over ℚ(√35)? NL found none; L-dim shows it cannot be an isomorphism.
5. Side fact for the record (PROVED): ln(6+√35) in Λ₀ is the regulator of ℚ(√35) (fundamental unit 6+√35). Is there any use of this tie in your literature pins? NL claims none.

## Labels tally
- PROVED 11: Φ-1 = 576k²; Φ-3 = Φ-1; Φ-2 breaks L7a; L7a holds; K = 8k² as S⁴ Ricci; K_Σ = −Φ/144; dim W₃₅ = 35 and one nonzero component; SO(4)×SO(2) split; W-c, W-d dimension facts; G₂ split frame-dependent; KR ratios.
- CONDITIONAL 3: adoption of Φ-1 and W-a (on OW 5a6e7177 plus a future Owner choice); numbers at N = 4880, g = 2; MR2's holographic a, c reading.
- OPEN 5: meaning of "evaluated across"; relation of W₃₅ to the locked V₃₅ (beyond L-dim); integrated Φ (needs b); 1/144 as K_Σ identification; C5.
- REFUTED 5 (by proof): L7b on S⁴, on Σ₂, and fibre-averaged; k² = Φ/1728 on (D); W₃₅ ≅ V₃₅ (L-dim).
