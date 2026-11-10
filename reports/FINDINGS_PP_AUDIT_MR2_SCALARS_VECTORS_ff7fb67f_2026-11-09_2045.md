# PP audit: MR2 scalar/vector masses on MN2 under Group A (ff7fb67f)
Written 2026-11-09 2045 CST by Professor Proof (Soft SF audit). New additive file. No existing file was edited and nothing is adopted. Authority: OW d5eaeef3, b0b9ae7f, 8b26c786, 90cec14c. Labels: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. Naming: resonant algebra.

## Integrity
| file | sha256 (actual = sidecar) | mtime CST |
|---|---|---|
| MR2_MN2_KK_A_S4_SCALARS_VECTORS_COMPUTED_AUT48_2026-11-09.py | 88dadcf9cf76b845…8b5ee6e ✓ | 20:39:56.510 |
| …_2026-11-09.log (empty, 0 B) | e3b0c44298fc1c14…7852b855 ✓ | 20:39:56.518 |
| …_RUN2.log | 82a3d9478376a1a5…4902646 ✓ | 20:40:09.826 |
| .md | ff7fb67fb3bafc49…8311df50 ✓ | 20:41:35.485 |

- The .py was frozen before RUN2 (20:39:56 < 20:40:09). ✓
- **PP rerun** of the frozen .py (copy sha 88dadcf9…): exit 0, about 25 s. rerun.log sha 82a3d947…, **byte-identical to RUN2**. ✓
- **Empty log.** Disclosure D1 is honest. The file is 0 B with the empty-string sha e3b0c442…, and its mtime is 8 ms after the .py, which fits a command that never started (exit 127). It supports **no claim**, and the .md cites none from it. Keeping it rather than deleting it follows the never-overwrite rule. ✓
- The header says "~20:42" and the mtime is 20:41:35. This is within the stated approximation and is not a slip.

## PP independent exact recomputation (own transcription of CGR (3.7)/(3.8) from /workspace/pp-audit-kk/cgr.txt lines 357–380)
Files are in /workspace/pp_sv_2045/: pp_sv.py be7d451d… / pp_sv.log 1cab2f45…, and pp_sv2.py cbee6e65… / pp_sv2.log 8a8ff885….
- **Transcription.** PP compared MR2's Lpot term by term against (3.8): (l−ψ²)², the ε^{ab}ε^{cd} quartic, e^{−10φ}[2(l+ψ²)−e^{10λ}ψTψ−e^{−10λ}ψT⁻¹ψ], and ½e^{−4φ}[e^{8λ}(TrT)²−2e^{8λ}TrT²+4e^{−2λ}TrT]. All match. V = −Lpot is the right sign. The kinetic coefficients 30, 30, ¼tr(T⁻¹dT)² and e^{2λ−6φ}T⁻¹ match (3.7).
- **(φ,λ) block** (pp_sv2, own code): V₀ = −3·2^{2/3}g², g²L² = 2^{4/3}, gradient 0. The eigenvalues are **−4** (δφ:δλ = 1:3) and **12** (δφ:δλ = −3). ✓
- **T block** (by hand, with exact confirmation): for T = e^{tm}, the quadratic part of Lpot is ½e^{−4φ}(2e^{−2λ}−e^{8λ})·Tr tm². This vanishes exactly at e^{10λ} = 2, so all **5 are at 0**, independent of the kinetic normalisation. w = diag(w,w,−2w) lies in this 5-plet. ✓
- **ψ block** (by hand, with exact confirmation): V_ψψ = g²(2^{2/3}+2^{−4/3})ψ² = (5/4)·2^{2/3}g²ψ², and K = e^{2λ−6φ} = 1, so m²L² = **5** (×6). ✓
- **Block-diagonality** (by structure): there is no term linear in tm (Tr tm = 0), so φ,λ do not mix with T. ψ enters only quadratically, and ψ–T mixing first appears at cubic order. So the matrix is block-diagonal at quadratic order. ✓ This agrees with MR2's exact off-block = 0.
- **Vectors.** The N=2 data a = diag(2^{4/3}, 2^{−2/3}, 2^{−2/3}) and M = g²vvᵀ with v = (0,−1,1) give eig(a⁻¹M)L² = {0, 0, 8}. This equals CGR (6.3): 2^{5/3}g²L² = 8, with Δ = 2+√9 = 5. In N=4 the massless vectors are A(1) plus the 3 gauge fields F^{αβ} (D𝒯 ∝ [A,𝒯] = 0 at 𝒯 = 1, and ψ = 0). That gives **4 massless** plus the **χ triplet at 8**. ✓ (The χ decoupling uses CGR (B.7)/(B.12)/(6.3), which PP did not re-derive. That step is a stated premise.)
- **Exact Aut⁺** (pp_sv, exact closure in ℚ(ζ₈) of ⟨A,B,J⟩ on H^{1,0}): order **48**, with order statistics {1:1, 2:13, 3:8, 4:6, 6:8, 8:12} = GL(2,3). ✓ The float [G] row is now exact.

## Verdicts by row (MR2 tally numbering)
| # | claim | MR2 | PP |
|---|---|---|---|
| 1 | vacuum, g²L² = 2^{4/3} | PROVED (given CGR) | **PROVED** as an implication of the CGR Lagrangian premise (reproduced) |
| 2 | 13-scalar matrix −4, 12, 0×5, 5×6, block-diagonal | PROVED (given CGR) | **PROVED** (implication; PP's own transcription agrees) |
| 3 | Z1: w marginal, {0,4}, ∂³_wV = −24·2^{2/3}g² | PROVED | **PROVED** (ratio exactly 1 to PP's Z1) |
| 4 | (−3:1) ↔ Δ=6, (1:3) ↔ Δ=2 | PROVED | **PROVED** |
| 5 | vectors: 4 massless, χ triplet at 8 (Δ 5) | PROVED (given CGR) | **PROVED** as an implication of CGR (3.7) and (6.3) |
| 6 | these are MN2 KK masses | COND | **COND** |
| 7 | all CGR modes Aut⁺-invariant under (P1)–(P2); J-sign table | PROVED (implication) | **PROVED only as an implication.** The J sign (−1)^{m−q} is a correct local fibre statement at Weierstrass points: K^{m}⊗V^{q} ≅ K^{m−q} with V ≅ TΣ ≅ K⁻¹, and dJ = −1. It is a necessary condition at fixed points, not a global invariance criterion. "All truncation modes survive" is not unconditional. |
| 8 | J = −I on H^{1,0}, so there are no invariant harmonic 1-forms | PROVED | **PROVED** (hyperelliptic J*: dx/y ↦ −dx/y) |
| 9 | \|Aut⁺\| = 48, GL(2,3) statistics; H⁰(K²) multiplicity 0 | COND (float) | **PROVED** on PP exact: order and statistics in this audit; H⁰(K²)^{Aut⁺} = 0 in eb979fda. MR2's float run on its own stays COND. |
| 10 | invariant 1-forms = df ⊕ *dg; lowest 23.0786 | decomposition PROVED; value COND | **Decomposition PROVED.** If α is invariant, averaging f and g keeps them invariant, and d, * commute with Aut⁺. The value 23.0786 is **COND** (FEM). The 5D masses of these Σ-vectors are **OPEN** (folded into row 14). |
| 11 | Δ₂ = 2j+4 | PROVED | **The arithmetic is PROVED**: 4+2j(j+3)+2j(j+1) = 4(j+1)². Calling it "CGU's universal family" rests on the Chen–Gutperle–Uhlemann 1903.07109 citation. Under the strict rule that identification is **COND**, so the row is PROVED only as identity plus citation, not as a multiplet fact. |
| 12 | A₂Ā₂ partners (j=1: scalar 0, vector 8; j=2: 12, 24) survive | COND | **COND.** The arithmetic is exact: Δ₀ = 2+2j; scalar Δ₀(Δ₀−4) gives 0 and 12; vector at Δ₀+1 with (Δ−1)(Δ−3) gives 8 and 24. The multiplet content and survival are cited, not derived. |
| 13 | full-spectrum lowest −4 / 0; no mode below BF | COND | **COND.** In the truncation, min = −4 = −d²/4 at d = 4 exactly, so the bound is saturated, not violated: **PROVED** (implication). The full spectrum rests on cited SUSY ⇒ unitarity. |
| 14 | Σ-dependent towers, non-universal levels, charged partners, K^a, fermions | OPEN | **OPEN** |
| 15 | dressed lift | OPEN | **OPEN** |

**Tally.**
- MR2's header says **8/5/2/0 = 15**. Its own row labels give **9/4/2/0 = 15**: PROVED rows 1, 2, 3, 4, 5, 7, 8, 10, 11; COND rows 6, 9, 12, 13; OPEN rows 14, 15. MR2's parenthetical, which counts row 10 as PROVED, also gives 9/4. **MR2's self-flag is correct, and the header is a slip.**
- **PP tally: 10 PROVED · 3 COND · 2 OPEN · 0 REFUTED = 15.** Row 9 is upgraded on PP's exact recomputation. Rows 7 and 11 are PROVED only as an implication or identity, with the caveats above.
- **Nothing is REFUTED.**

## Self-flags
- **D3 sentence is garbled** (confirmed). "{4−Δ, Δ}… in the convention φ ~ r^{−(4−Δ)}, r^{−Δ}" has a broken ellipsis and a mixed convention. The [N4] log label "{Delta-4? i.e. 4-Delta, -Delta}" is also garbled. The values that are used are correct: Δ = 6 gives 4−Δ = −2, and w gives {0, 4}.
- **D2** (wrong y-lift, giving 96 matrices including iI) is honest and consistent. Dropping the i adjoins a scalar, which doubles the group. The frozen .py rejects the bad lift exactly.

## Fixes for an MR2 erratum (additive, new file)
1. Tally header: 8/5/2/0 → **9/4/2/0 = 15** (MR2's own rows). Optionally adopt the PP grade 10/3/2/0 with row 9 PROVED via PP exact (this file plus eb979fda).
2. Rewrite D3: "Boundary falloffs z^{4−Δ} and z^{Δ} (z → 0). For the 12 mode, 4−Δ = −2. For w, the second-order exponents are {0, 4}." Mark the [N4] log label as cosmetic.
3. Row 7: say "PROVED as implication of (P1)–(P2)". The J-sign table is a necessary condition at J-fixed points, not a global criterion.
4. Row 11: split it. The arithmetic identity is PROVED. The identification with the CGU n=0 family is COND (citation 1903.07109).
5. Row 13 / RA-6: state that the truncation minimum −4 = −d²/4 (d = 4) is PROVED (implication, saturated). Only the full-spectrum statement is COND.
6. Row 10: note that the 5D masses of the df ⊕ *dg Σ-vectors are OPEN (row 14).
7. Row 5: list the χ decoupling (CGR (B.7)/(B.12)/(6.3)) as a stated premise.

**Verdict: confirmed, with clerical fixes.** Integrity is clean, with a byte-identical rerun. Every mass is independently reproduced exactly: −4, 12, 0×5 (including w), 5×6, block-diagonal; vectors 0×4 and 8×3. Group A projection checks pass with the stated grades. There are no refutations.
