# MR2 branch attempt: B1-c2′, candidate E-S± — δ(f) on the vertical spin structures, f = P∘r̃
2026-11-10, written ≈10:11–10:14 CST (America/Chicago, box clock; mtimes authoritative). Author: MR2. Additive; nothing edited (cc21b272 untouched; the cc21b272 erratum is the parent's, not written here); **nothing adopted** (not E-S±, not 1a, not B1-c2′); no CERT, no Gemini, nothing sent. Junction **UNSOLVED**. Group A stays the KK scope; c2′ conflicts with it on scope only. Wording: resonant algebra.

## Authority and inputs (sha = sidecar, checked 10:08 and 10:11 CST)
- OW 83d7a0fa e72a188bf2d2d73ab186242bd8d4e0f391bb0eebadb660d80c97be0f222b497b; OW t4436 328812635d807f5cb7d1e5e6b5df7f89512060c36c090a2a191526ab7e90fd46; OW t445u d64f6fd2ac51628251b8f39a658251fbc15935734b54aead2f0843569caf7def; keep/drop 0f6357745f045edb308ed37b45b9b4fdb1a5cada80b0a93dc4ef2fe5e4f9089f.
- Target item: MR2_BRANCH_ATTEMPT_BATCH1_C2PRIME_E8_BUNDLE_UNDER_1A_R_TILDE_INVARIANCE_2026-11-10.md, cc21b2728dd74fe6aae8d7da186a5bb40f9b5b4e8d8390226f2fa0e904f08f11, row 14.
- PP audit FINDINGS_PP_AUDIT_MR2_C2PRIME_E8_BUNDLE_cc21b272_2026-11-10_1007.md, 51198d6fd2056673a01d22aff38147ffe626dab29d26de471a4c90ca73978deb.
- PP addendum FINDINGS_PP_AUDIT_MR2_C2PRIME_E8_BUNDLE_cc21b272_ADDENDUM_ROW12_2026-11-10_1008.md, 107dc13de4a9a8ea097908d639f5c6e951539c1972c7f64f5f0425bb9f18501d. It supersedes 1007 on row 12 and the tally. PP tally 15/2/6/0 = 23. Row 14 is OPEN (undone computation); "a vertical spin structure exists (w₂ = 0)" is PROVED.
- MR2_MN2_KK_GROUP_B_DRESSED_PINPLUS_CHECK_2026-11-09.md, 8399be55265f2cb0a42a69db4f6ffcb0e2ecc711fc6cc83aef3c4c47c85f41a1, with its .py 2f0e12201717a508a6c3fc965c829ddf1e3e7677e50a8d725debe11beb4c03db and .log c920912746999f6237fd5757a46561e1d9e70484f0ae63abe3441c958f0e9183. It supplies the Weierstrass model, the generator permutations, and the K (= complex conjugation) row "8/16".
- No external source was fetched.

**Premises used (stated, so results are graded as implications):**
- **R-inv (PP 1007 fix 1).** r ∈ Isom(Bolza) \ Aut⁺ is chosen to be an involution with fixed points (a reflection). Verified here for the class of complex conjugation c: (x, y) ↦ (x̄, ȳ) on y² = x⁵ − x squares to the identity, and it has real points (x = 2, y² = 30). Jc squares to the identity too and has points with x ∈ (0, 1), y ∈ iℝ. Bolza also has orientation-reversing isometries of order > 2; for those, f² = id is **not** claimed.
- **M (model).** Spin structures on Σ (roots of K; roots of L = K or K⁻¹ have the same combinatorics) correspond to odd subsets of the six Weierstrass points modulo complement. An isometry acts through its permutation of W, and an antiholomorphic one acts by θ ↦ r*θ̄. This is the 8399be55 model, taken from the hyperelliptic theta-characteristic literature: cited, not rederived, so COND. The quadratic-form algebra behind it is re-checked exactly in [A].
- **Emb.** E-S± uses a fixed index-1 embedding SU(2) ⊂ E₈ with centraliser E₇, E₈ ⊃ (SU(2) × E₇)/ℤ₂, and 248 = (3,1) + (1,133) + (2,56). This is standard Lie theory, stated as a premise.

## Script and log (frozen: chmod a-w and sidecar written before the run)
| file | sha256 | mtime |
|---|---|---|
| /workspace/mr2-c2e8-1010/c2p_ESpm_vertical_spin_delta_2026-11-10_1015.py (+ identical copy in reports/ with its own sidecar, cmp ✓) | 5cdf6aaa2c0be5b17a37f3b3539b809b8627e4edbdfb2fc9d50b36f64df6b769 | 10:08:44 |
| /workspace/mr2-c2e8-1010/c2p_ESpm_vertical_spin_delta_2026-11-10_1015.log (+ identical copy in reports/, cmp ✓) | 7837d39c29a8a88d6c4cc9352cecbf43260f9935fe8cb8068d38a6b797b978d8 | 10:08:45; exit 0, < 1 s |

Nits:
- "1015" in the names is ~6 min ahead of the run.
- In the class loop, the first `cl = {...}` comprehension is dead code: it is immediately overwritten by the correct conjugation loop.
- The assertion `len(set(...)) >= 1` is vacuous.
- The run was completed **before** the parent's steering message (10:10). The script does not depend on it. R-inv is applied in the write-up, not in the code.
- No empty or superseded logs.

## 1. Re-verification of w₂(V_vert) = 0 (the claim in cc21b272). PROVED
- V_vert ⊕ ℝ = π*(L ⊕ ℝ³), so w₁ = 0 and w₂(V_vert) = π*(c₁(L) mod 2).
- In the audited metric the twist is Dφ₁ = dφ₁ + A, with A = dx/y and charge 1 on z₁ = μ₁e^{iφ₁}. This agrees with the 7D KSE run (k·a = 4·(1/4) = 1).
- Log [W2]: dA = y⁻² dx∧dy, which is exactly the area form of the curvature −1 metric.
- Area(Bolza) = (8 − 2)π − 8(π/4) = 4π, by Gauss–Bonnet for the regular octagon with angles π/4. So |deg L| = 4π/2π = 2, c₁(L) mod 2 = 0, and w₂(V_vert) = 0.
- The cc21b272 claim stands.

## 2. Vertical spin structures and the action of f. PROVED (given M for the identification)
- **(a) Counting.** H¹(Y₆; ℤ₂) ≅ H¹(Σ; ℤ₂), because the fibre S⁴ is simply connected. Spin structures on V_vert correspond to spin structures on π*(L ⊕ ℝ³), hence to spin structures on L ⊕ ℝ³ over Σ (π* is an iso on H¹), hence to spin structures on L, i.e. the 16 roots of L.
- **(b) Action of f.** f acts on L ⊕ ℝ³ as dr ⊕ P. dr is antilinear on L; P is a constant reflection of the trivial ℝ³. The total determinant is (−1)(−1) = +1, matching fibre degree +1 (cc21b272 [D]).
  - A constant O(3) factor does not change the class.
  - So f acts on vertical spin structures as r acts on roots of L, i.e. through r's permutation of W (model M).
  - δ(f; s) = f*s − s ∈ J[2], and f lifts to S± for the chosen s if and only if δ(f; s) = 0.

## 3. Results (log)
- **[A] Model algebra, exact.** q_T(S) = |S ∩ T| + |S|/2 mod 2 (T an odd subset, S an even subset).
  - It is well-defined modulo complements and is a quadratic refinement of the mod-2 intersection form.
  - The 16 forms are distinct, and exactly the 6 singleton T have Arf = 1 (the odd theta characteristics O(w_i)).
- **[G] Image groups on W.** The image of Aut⁺ has order 24 (= Aut⁺/⟨J⟩) and the image of Isom has order 48 (O_h on the octahedron vertices W). There are 24 orientation-reversing images; each has two preimages ±J in Isom \ Aut⁺, and J fixes all 16 structures.
- **[C] Fixed vertical spin structures** for each orientation-reversing conjugacy class:

  | class size | cycle type on W | representative (images of 0, ∞, 1, i, −1, −i) | fixed / 16 (odd, even) |
  |---|---|---|---|
  | 3 | (2,1,1,1,1) | 0, ∞, 1, −i, −1, i (complex conjugation c) | **8** (4, 4) |
  | 6 | (2,2,1,1) | 0, ∞, i, 1, −i, −1 | 4 (2, 2) |
  | 6 | (4,2) | ∞, 0, i, −1, −i, 1 | 2 (0, 2) |
  | 1 | (2,2,2) | ∞, 0, −1, −i, 1, i | 4 (0, 4) |
  | 8 | (6) | 1, −1, i, ∞, −i, 0 | 1 (0, 1) |

  Every orientation-reversing image fixes at least one structure (24 of 24; none fixes zero).
- **[K] r = c** (the reflection class, which satisfies R-inv): it fixes **8/16**, namely the subsets {0}, {∞}, {1}, {−1}, {0,1,∞}, {−1,0,∞}, {−1,0,1} and {−i,0,i}. This reproduces the 8399be55 "K: 8/16" row.
- **[S] The lift's square.** At a fixed point of f (one exists for r = c: over a real point of Σ, take φ₁ at a fixed value of φ₁ ↦ −φ₁ + λ and φ₂ ∈ {0, π}), f acts on T S⁴ with two −1 eigenvalues, the φ₁ and φ₂ directions.
  - Its lift is e₃e₄, a rotation by π. It squares to −1 on S₊ and on S₋, and it preserves each of them.
  - f̃² covers f² = id (R-inv) and commutes with the connection, so it is a constant central element of SU(2). It is therefore −1 on all of Y₆, since Y₆ is connected.
  - In E₈ (Emb), −1 ∈ SU(2) acts as −1 on (2,56) (112 dimensions) and +1 on 136, so it is a nontrivial element. It equals the central z ∈ E₇.
  - **Strict ℤ₂ lift:** choose a constant h ∈ E₇ with h² = z (one exists: z lies in a maximal torus of the connected group E₇). Then f̃′ = f̃·h⁻¹ satisfies f̃′² = 1. It still preserves the connection, because h commutes with SU(2) and with f̃.

## 4. Verdict for E-S± (the row 14 question)
- **Keep, as an implication:** for r = c and its class (premises R-inv and M), f preserves exactly 8 of the 16 vertical spin structures. For each of those 8, both S₊ and S₋ lift under f.
  - The lift preserves the vertical connection (as for E-Λ±).
  - After the constant E₇ dressing h, it is a strict ℤ₂ lift (premise Emb).
- **Obstruction:** for the other 8 structures, δ(f; s) ≠ 0 and no lift exists for that choice.
- **Other orientation-reversing classes:** the fixed counts 4, 2, 4, 1 are computed, but those classes are not shown to be involutions. So f² = id and the ℤ₂ statement are not claimed there; only δ is.
- **Not fixed by any filed source:** which vertical spin structure the physical datum uses. The 11D SUSY structure d₀ = s ⊕ s_R = 0 does not single one out. Nor which r is used. Both OPEN; nothing adopted.
- **Not touched:**
  - E-T and its Pin(6)/Spin(10) issue (PP addendum; left for a later pass).
  - E-Λ±: its premise is a fixed SO(3) ⊂ E₈ subgroup embedding (PP 1007); not recomputed here.
  - The pointwise Bianchi and J_M5 ≥ 0 questions (still OPEN in cc21b272).

## Labels (PP convention)
| # | item | grade |
|---|---|---|
| 1 | w₂(V_vert) = 0, w₁ = 0: deg L = ±2 re-verified (dA = y⁻²dx∧dy; Gauss–Bonnet area 4π) | PROVED |
| 2 | 16 vertical spin structures ↔ roots of L; H¹(Y₆; ℤ₂) ≅ H¹(Σ; ℤ₂) | PROVED |
| 3 | f acts on vertical spin structures through r's W-permutation (dr antilinear; the constant P contributes nothing) | PROVED as implication of M |
| 4 | model M itself (theta characteristics ↔ odd subsets, natural under Isom) | COND (citation, from 8399be55) |
| 5 | [A] q_T are the 16 quadratic refinements; Arf = 1 for exactly the 6 singletons | PROVED (exact) |
| 6 | [G] image orders 24 / 48; 24 orientation-reversing images | PROVED |
| 7 | [C] per-class fixed counts 8, 4, 2, 4, 1; no orientation-reversing class fixes 0 | PROVED as implication of M |
| 8 | R-inv holds for the c-class (c² = id, Jc² = id, real points exist) | PROVED |
| 9 | [K] r = c fixes 8/16 (listed) | PROVED as implication of M |
| 10 | [S] f̃² = −1 on S± for r = c (fixed point exists; constant on Y₆) | PROVED as implication of R-inv |
| 11 | strict ℤ₂ lift after the constant E₇ dressing h, h² = z | PROVED as implication of Emb and R-inv |
| 12 | **E-S± lift under f: exists for the 8 c-fixed vertical spin structures (both S₊ and S₋); fails for the other 8** | **PROVED as implication of M, R-inv, Emb** |
| 13 | which vertical spin structure / which r the physical 1a datum uses | OPEN (nothing adopted) |

**Tally (graded rows 1–13):**
- PROVED 11: rows 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12.
- COND 1: row 4.
- OPEN 1: row 13.
- REF 0.
- Total 11 + 1 + 1 + 0 = 13. Junction UNSOLVED.

## Branch status (pending PP)
- **cc21b272 row 14 (E-S±):** proposed regrade from OPEN to **PROVED as an implication of M (COND), R-inv and Emb, for r in the c-class and s_R one of its 8 fixed structures**. "w₂ = 0" stays PROVED. MR2 does not edit cc21b272 or write its erratum; the parent does.
- **B1-c2′:** COND overall, not adopted.
- **1a:** not adopted; pure form REF (fe0c3d92); rescues OPEN.
- **E-T row 12:** OPEN per the PP addendum; untouched.

Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, MATCH at 10:08 CST and at write.
