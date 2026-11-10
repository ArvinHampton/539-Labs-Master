# MR2 branch attempt: B1-c2′, candidate E-T — connection-preserving involutive E₈ lift through Pin(6) with a compensating Spin(10) reflection (cc21b272 row 12)
2026-11-10, written 10:16:19 CST (America/Chicago; this is the write time, matching the file's mtime). Author: MR2. Additive; nothing edited (cc21b272, its erratum 55941d82 and 51cd8bc8 untouched); **nothing adopted** (not E-T, not 1a, not B1-c2′); no CERT, no Gemini, nothing sent. Junction **UNSOLVED**. Group A stays the KK scope; c2′ conflicts with it on scope only. Wording: resonant algebra.

## Authority and inputs (sha = sidecar, checked 10:13 CST)
- OW 83d7a0fa e72a188bf2d2d73ab186242bd8d4e0f391bb0eebadb660d80c97be0f222b497b; OW t4436 328812635d807f5cb7d1e5e6b5df7f89512060c36c090a2a191526ab7e90fd46; OW t445u d64f6fd2ac51628251b8f39a658251fbc15935734b54aead2f0843569caf7def.
- Target: cc21b2728dd74fe6aae8d7da186a5bb40f9b5b4e8d8390226f2fa0e904f08f11 (row 12).
- PP 1007: 51198d6fd2056673a01d22aff38147ffe626dab29d26de471a4c90ca73978deb. PP addendum 1008 (supersedes 1007 on row 12 and the tally): 107dc13de4a9a8ea097908d639f5c6e951539c1972c7f64f5f0425bb9f18501d.
- MR2 erratum 55941d820946de7fd5aec8603cfb711c569a71a42b27fe32b77bd575a192f4fa, confirmed by PP f2e2e0a68230f578f9eabd04a1e240eced7e6ae7cb761c99125152c9eaf91f95. Nit note aca26c53878828fb213ab1433374dbd5297a17d7b501c33d26fc5bb68f04ca58 (not re-filed).
- E-S± filing 51cd8bc836926a68b55d8ce80933008baf5f94d3994321773dc11f31d0f2a882 (pending PP; not re-litigated).
- 8399be55265f2cb0a42a69db4f6ffcb0e2ecc711fc6cc83aef3c4c47c85f41a1: twist model, the 11D SUSY spin structure d₀, and the Weierstrass model.
- No external source fetched.

**PP's requirement (addendum, fix 7).** Specify the compensating reflection in Spin(10). Prove (i) that f preserves the spin structure on TY₆, and (ii) that the Pin lift squares to +1, not to the central −1, on the 128.

**Premises (stated; results are graded as implications):**
- **R-inv.** r is an involution with fixed points (a reflection). This holds for the class of complex conjugation c, as shown in 51cd8bc8.
- **Twist model** (8399be55). The twist line bundle L satisfies K ⊗ L ≅ O (L = TΣ), so the twisted spinor bundle K^{1/2}_s ⊗ L^{1/2}_{s_R} has degree 0. Spin structures on Σ are modelled by Weierstrass subsets (model M, COND).
- **d₀.** E-T uses the TY₆ spin structure induced by the 11D SUSY spin structure d₀ = s ⊕ s_R = 0. This is premise (1) of 8399be55 §A: COND.
- **Emb-T.** E₈ ⊃ Spin(16)/⟨ω⟩ with 248 = 120 ⊕ 128 (128 a chiral spinor). E-T is the standard embedding Spin(6) ⊂ Spin(6) × Spin(10) ⊂ Spin(16), with trivial Spin(10) connection. Standard Lie theory, stated as a premise.

## Script and log (frozen: chmod a-w and sidecar written before the run)
| file | sha256 | mtime |
|---|---|---|
| /workspace/mr2-c2e8-1010/c2p_ET_pin_lift_2026-11-10_1016.py (+ identical copy in reports/ with its own sidecar, cmp ✓) | a7eeb8f25eb3698946497c4b12e87db9928f7ef31f4ecd82ad87f2c4e46e72b2 | 10:14:46 |
| /workspace/mr2-c2e8-1010/c2p_ET_pin_lift_2026-11-10_1016.log (+ identical copy in reports/, cmp ✓) | 3232e6a49fcaf2ff921d07de46c36216c6390a1a1e875b28a03d91b5ae6422bc | 10:15:11; exit 0, ~25 s |

Nits:
- "1016" in the names is ~1–2 min ahead of the run.
- The Clifford checks use numpy np.allclose on matrices whose entries are 0, ±1, ±i. They are exact up to floating representation of these integers; PP has accepted this as effectively exact before (7f366e78), and the grading here relies on that.
- No dead code was found. No empty or superseded logs.

## 1. (i) f preserves the TY₆ spin structure (choice d₀)
- **Stabilising.** TY₆ = π*TΣ ⊕ V_vert and V_vert ⊕ ℝ = π*(L ⊕ ℝ³). So TY₆ ⊕ ℝ ≅ π*(TΣ ⊕ L ⊕ ℝ³), and H¹(Y₆; ℤ₂) ≅ H¹(Σ; ℤ₂) (the fibre S⁴ is simply connected).
- **Labelling.** Spin structures on TΣ ⊕ L (both summands spin) are labelled by the root s ⊗ s_R of K ⊗ L ≅ O, i.e. by d ∈ J[2], with d₀ = the trivial root. This is 8399be55's d.
  - w₂(TY₆) = π*(w₂Σ + w₂L) = 0, consistent with PP and with 51cd8bc8 §1.
- **The map.** f acts as dr ⊕ dr ⊕ P on TΣ ⊕ L ⊕ ℝ³: dr is antilinear on both line bundles, and P is a constant reflection.
  - It is orientation-reversing on TY₆ (det −1, PP addendum item 1).
  - We stabilise by the compensating direction ℝ_a and act there by −1. Then df ⊕ (−1) is orientation-preserving on TY₆ ⊕ ℝ_a, and spin structures can be compared.
  - Constant O(·) factors do not change the class. So f acts on d through r's linear action on J[2].
- **The trivial root is canonical.** f*O ≅ O, so **d₀ is fixed by every isometry**: δ(f; d₀) = 0.
- **Log [d]:** d₀ is fixed in all 5 orientation-reversing classes. The J[2] fixed counts are 8, 4, 2, 4, 1 (class sizes 3, 6, 6, 1, 8). For r = c the fixed elements are ∅, {0,∞}, {0,1}, {−1,0}, {1,∞}, {−1,∞}, {−1,1} and {−i,i}.

## 2. The compensating reflection, and (ii) the square on the 128
- **Specification.** Fix a unit vector a in the ℝ¹⁰ of SO(10). The compensator is the reflection R_a, with Pin(10) lift e_a.
- **The global lift.** df ⊕ R_a is an orientation-preserving automorphism of the rank-7 bundle TY₆ ⊕ ℝ_a ⊂ (TY₆ ⊕ ℝ¹⁰). It preserves the spin structure d₀ ⊕ (trivial) by §1, and it preserves the connection ∇^{LC} ⊕ d (f is an isometry, cc21b272 [M]; R_a is constant).
  - It therefore lifts to an automorphism of the Spin(7) principal bundle with its connection, unique up to ±1.
  - Through Spin(7) ⊂ Spin(16) → E₈ (Emb-T), it gives a connection-preserving automorphism of the E-T E₈ bundle covering f.
- **Local form at a fixed point.** One exists for r = c (a real point of Σ, μ₁ and μ₂ nonzero, φ₁ fixed, φ₂ ∈ {0, π}). There df = diag(−1, −1, −1, 1, 1, 1) on (x̂, φ̂₁, φ̂₂, …) and the lift is L = e_x e_{φ₁} e_{φ₂} e_a.
- **Log [L], Cl(16) on ℂ²⁵⁶:**
  - The anticommutators are exact, and the chiral projectors have rank 128 + 128.
  - L has degree 4, so it is even and lies in Spin(16). It commutes with ω, so it preserves each 128.
  - **L² = +1 on 128₊ and on 128₋**, and L² = +1 on all 256.
  - Ad_L = Ad(df) on so(6), Ad(R_a) on so(10), and df ⊗ R_a on the (6,10) part.
- **Contrasts:**
  - A three-vector compensator e_a e_b e_c squares to **−1 on both 128s**: the central element, which is nontrivial in E₈. So it would not give an involution.
  - No compensator (e_x e_{φ₁} e_{φ₂}) is odd: it does not lie in Spin(16) and does not commute with ω.
- **Global square.** The square of the global lift covers f² = id (R-inv) and preserves the connection. So it is a constant central element ±1 of Spin(7) on the connected Y₆. It equals L² = +1 at the fixed point, hence **+1 everywhere**, and so +1 on the 128.
- **The Spin(10) part.** R_a preserves the trivial Spin(10) connection of E-T. The E-T Spin(6) connection is preserved because Ad_L = Ad(df) and f is an isometry.

## 3. Verdict for E-T (row 12)
- **Restored, as an implication.** For r in the c-class (R-inv) and E-T built on the TY₆ spin structure d₀, E-T has a **connection-preserving involutive E₈ lift**: df ⊕ R_a, lifted through Spin(7) ⊂ Spin(16) → E₈, with L² = +1 on the 128. The premises are the twist model with model M, d₀ (COND), and Emb-T.
  - The same holds for each of the 8 c-fixed d ∈ J[2].
  - For a d not fixed by r, there is no lift for that choice.
- **Not claimed:** classes not shown to be involutions (only their δ counts are reported); r̃ alone; and whether E-T is the physical 1a datum, the pointwise Bianchi equation and J_M5 ≥ 0 (OPEN, as in cc21b272).
- The topological lift (n = 0 by D2, given D4) is unchanged.
- E-Λ± (row 13) is untouched. Its premise remains a fixed SO(3) ⊂ E₈ subgroup embedding (PP addendum fix 8).

## Labels (PP convention)
| # | item | grade |
|---|---|---|
| 1 | TY₆ ⊕ ℝ ≅ π*(TΣ ⊕ L ⊕ ℝ³); TY₆ spin structures ↔ d ∈ J[2]; d₀ is the trivial root of K ⊗ L | PROVED as implication of the twist model |
| 2 | δ(f; d₀) = 0 for every orientation-reversing r (canonical; log [d] in all 5 classes) | PROVED as implication of the twist model and M |
| 3 | J[2] fixed counts 8, 4, 2, 4, 1; r = c fixes 8 (listed) | PROVED as implication of M |
| 4 | Compensator specified (R_a, a fixed unit vector in ℝ¹⁰); df ⊕ R_a lifts to a connection-preserving Spin(7)-bundle automorphism | PROVED as implication of rows 1–2 and Emb-T |
| 5 | Ad_L = Ad(df) on so(6), Ad(R_a) on so(10), df ⊗ R_a on (6,10) | PROVED (exact Clifford) |
| 6 | L² = +1 on 128₊, 128₋ and all 256 | PROVED (exact Clifford) |
| 7 | the global square is +1 everywhere (constant central element, +1 at a fixed point of the c-class) | PROVED as implication of R-inv |
| 8 | contrasts: a three-vector compensator gives −1 on the 128; no compensator is not in Spin(16) | PROVED |
| 9 | R_a preserves the trivial Spin(10) connection; the Spin(6) connection is preserved | PROVED |
| 10 | **E-T connection-preserving involutive E₈ lift exists (r in the c-class; spin structure d₀ or any c-fixed d)** | **PROVED as implication of the twist model/M, R-inv, Emb-T** |
| 11 | E-T's TY₆ spin structure is the 11D SUSY structure d₀ | COND (8399be55 §A premise 1) |
| 12 | whether E-T is the physical 1a datum (pointwise Bianchi, J_M5 ≥ 0) | OPEN (nothing adopted) |

**Tally (graded rows 1–12):**
- PROVED 10: rows 1–10.
- COND 1: row 11.
- OPEN 1: row 12.
- REF 0.
- Total 10 + 1 + 1 + 0 = 12. Junction UNSOLVED.

## Branch status (pending PP)
- **cc21b272 row 12 (E-T):** proposed regrade from OPEN to **PROVED as an implication** (premises as in row 10; d₀ COND) for the connection-preserving involutive lift. The topological lift is unchanged. MR2 does not edit cc21b272; the parent handles errata.
- **B1-c2′:** COND overall, not adopted.
- **1a:** not adopted; pure form REF (fe0c3d92); rescues OPEN.
- **E-S± (51cd8bc8):** pending PP, untouched.

Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, MATCH at 10:13 CST and at write.
