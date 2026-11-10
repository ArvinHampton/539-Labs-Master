# PP audit: MR2 E-T Pin(6)/Spin(10) restoration of cc21b272 row 12 (0069b9ae…)
2026-11-10, written ≈10:24 CST (America/Chicago; the file mtime is authoritative). Author: PP (Soft SF audit rules). Additive. No existing file was edited, and nothing was written under /workspace/mr2-c2e8-1010/. Nothing adopted; no CERT, no Gemini, nothing sent externally. Junction **UNSOLVED**. Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, MATCH and untouched (mtime 2026-11-06 14:38 CST).

## 0. Integrity (sha = sidecar, recomputed 10:2x CST)
| file | sha256 | sidecar | mtime CST |
|---|---|---|---|
| reports/MR2_BRANCH_ATTEMPT_BATCH1_C2PRIME_E8_ET_PIN6_SPIN10_LIFT_2026-11-10.md | 0069b9ae53a1d9f2f4a863ff8e97f5aaad6de02497a62ed704e8c21a55506781 | ✓ | 10:16:19 (= header) |
| mr2-c2e8-1010/c2p_ET_pin_lift_2026-11-10_1016.py (+ reports/ copy) | a7eeb8f25eb3698946497c4b12e87db9928f7ef31f4ecd82ad87f2c4e46e72b2 | ✓ both | 10:14:46 (frozen before log) |
| mr2-c2e8-1010/c2p_ET_pin_lift_2026-11-10_1016.log (+ reports/ copy) | 3232e6a49fcaf2ff921d07de46c36216c6390a1a1e875b28a03d91b5ae6422bc | ✓ both | 10:15:11 |
Context re-read: PP addendum 107dc13d… (row 12 → OPEN, fix 7); MR2 erratum 55941d82… (row 12′ topological lift is a scoped sub-statement "included in 12", not an extra graded row).

PP evidence, new (frozen chmod a-w, sidecars):
- reports/PP_EXACT_ET_PIN_0069b9ae_2026-11-10_1024.py — 9b474b33a0739a61ba8181039c45f85d1a8a980047bbe3db6a761edccb8ceb14 (scratch original /workspace/pp-scratch/et-pin-0069/)
- reports/PP_EXACT_ET_PIN_0069b9ae_2026-11-10_1024.log — 5a35044ac2312f42f640f4d093c83179344330f07e52527367cafc11a6108a65 (exit 0, ≈111 s)

## 1. HARD POINT: np.allclose is not an exact test → PP exact re-run
MR2's [L] block (rows 5, 6, 8) rests only on np.allclose. On that evidence alone those rows would be **COND (float)**. The "7f366e78 precedent" does not license PROVED under the current rules. MR2's log line "anticommutators exact: True" is mislabelled; it is an allclose result.

PP rebuilt the same Jordan–Wigner Cl(16) on ℂ²⁵⁶ over the Gaussian integers ℤ[i]: each matrix is an (Re, Im) pair of int64 arrays, products use integer matmul, and every equality is np.array_equal. Nothing is float. Results (log lines X1–X8):
- X1: {e_a, e_b} = 2δ_ab·I for all 256 pairs, exact.
- X2: ω = e₀…e₁₅, ω² = I, and tr ω = 0. So (I ± ω)/2 are idempotents of trace 128, hence of rank 128 each.
- X3: **L = e₀e₁e₂e₆ satisfies L² = I exactly** on all 256 (hence on 128₊ and 128₋), and Lω = ωL.
- X4 (stronger than MR2's bivector check): L e_i L⁻¹ = −e_i for i ∈ {x, φ₁, φ₂, a} and +e_i for the other 12, exact. So Ad_L on ℝ¹⁶ is df ⊕ R_a, which gives so(6), so(10) and the (6,10) block at once.
- X5: Ad_L on all 120 bivectors, exact.
- X6: the three-vector compensator e₀e₁e₂e₆e₇e₈ squares to −I exactly and commutes with ω.
- X7: the no-compensator element e₀e₁e₂ anticommutes with ω exactly. So it swaps 128₊ ↔ 128₋ and is odd, i.e. not in Spin(16).
- X8: (e_{i1}…e_{ik})² = (−1)^{k(k−1)/2}·I, checked exactly for k = 1…8.

**Independent algebraic proof, no computer.** For distinct indices, moving each factor past the others gives (e_{i1}…e_{ik})² = (−1)^{k(k−1)/2} ∏ e_{ij}². For even k this does not depend on the signature convention. So k = 4 gives +1, k = 6 gives −1, and the odd k = 3 element lies outside Spin. For the vectors: e_i anticommutes with the 3 other factors of L when i is in the set, and with all 4 when it is not. That gives the X4 signs.
Rows 5, 6 and 8 are therefore **PROVED**, on PP's exact and algebraic proofs, not on MR2's allclose.

## 2. The requested checks
**(1) Compensator.** Specified: R_a for a fixed unit vector a ∈ ℝ¹⁰, with Pin(10) lift e_a. Note that e_a ∉ Spin(10); only the product L lies in Spin(16).
- Why one reflection: df at a fixed point has exactly 3 eigenvalues equal to −1 (verified in (4) below). The compensator must be odd, so that the total is in SO(16), and the total degree k = 3 + m needs (−1)^{k(k−1)/2} = +1. So m ≡ 1 (mod 4).
- m = 1 is the minimal choice. m = 3 gives −1 (MR2's contrast). m = 5 would also give +1, so "single" means minimal, not unique (X8).
- −1 ∈ Spin(16) acts as −1 on both 128s. It is not the semispin kernel element ±ω, so it is nontrivial in E₈ = Spin(16)/⟨ω⟩·… . Hence the m = 3 lift has order 4 in E₈, as MR2 says. **PROVED.**

**(2) L ∈ Spin(16), degree 4, and the contrasts.** **PROVED** (exact, §1).
Nit: MR2's log prints "square on 128±" for the odd element. That line is meaningless, because the element does not preserve either 128.

**(3) f preserves d₀ and the 7 other c-fixed structures.**
- Combinatorics, re-run exactly by PP (D1–D4):
  - |J[2]| = 16; |Ap| = 24; |Fu| = 48; c ∉ Ap, c² = id.
  - g₁ is x ↦ ix, g₂ is x ↦ (x+1)/(1−x), and c is complex conjugation. All three were checked as exact Möbius maps on W over ℚ(i).
  - The class fixed counts 8, 4, 2, 4, 1 and the r = c fixed list match MR2.
  - Extra information: only the classes of size 3, 6 (first) and 1 consist of involutions on W.
- Conceptually, d₀ is f-fixed. PP checked the step MR2 states only as "f*O ≅ O".
  - With L = TΣ, TΣ ⊕ L = V ⊕ V = V ⊗ ℝ². Its canonical spin structure comes from the SO(2) reduction, through the homomorphic lift ĥ(θ) = exp(θ/2·(e₁e₂ + e₃e₄)).
  - It is natural under orientation-reversing isometries g ↦ g ⊕ g. With ŝ = e₂e₄ one has ŝ ĥ(θ) ŝ⁻¹ = ĥ(−θ), so the induced map on P_SO ×_{SO(2)} Spin(4) is well defined.
  - Constant reflections on trivial summands (P on ℝ³, −1 on ℝ_a) lift to constant Pin elements and do not change the class.
  - Since d₀ is a fixed base point, f acts on spin structures affinely through r* on H¹(Σ; ℤ₂) ≅ J[2]. So the fixed structures are exactly the 8 r*-fixed classes.
- **Premise MR2 must make explicit (Eq-L).** Under L ≅ TΣ, f acts on L by dr itself. The alternative is dr composed with a U(1) gauge function e^{iα}, whose winding class mod 2 in H¹(Σ; ℤ₂) would shift δ(f; d₀). This is part of the twist model, but it is used, so it must be stated.
- Grade: **PROVED as an implication** of the twist model plus M plus Eq-L.

**(4) Global square.**
- Let F be any lift of the SO(7)-automorphism df ⊕ R_a. (df ⊕ R_a)² = id on frames, so F² is a gauge transformation over the identity of SO(7). It therefore takes values in {±1} and is locally constant. Y₆ is connected (an S⁴ bundle over a connected Σ), so F² is constant.
  - Connection preservation is not even needed for this step.
- At a fixed point, F_p = ±L, so F² = L² = +1.
- Fixed points exist for r = c (D4: (x, y) = (1, 0) on y² = x(x⁴ − 1)).
- **Fixed-point structure, checked by PP.** f = dr ⊕ dr_L ⊕ P on TΣ ⊕ (L ⊕ ℝ³), with the radial direction +1. A fixed fibre point y lies in the 3-dimensional +1 eigenspace of dr_L ⊕ P on ℝ⁵, and T_yS⁴ = y^⊥ carries both −1 directions. So **every** fixed point has exactly 3 eigenvalues −1: the fixed locus Fix(r) × S² has codimension 3 everywhere, including where μ₁ = 0 or μ₂ = 0.
  - This makes the choice of fixed point irrelevant, and it is consistent with k = 4 at every point.
- **PROVED as an implication** of R-inv. The step "r = c is an involution with fixed points" is exact here. That the physical r is in the c-class stays a premise.
- Nit: the report's "φ₁ fixed" should read φ₁ ∈ {0, π} (or μ₁ = 0).

**(5) Premises stay premises.** These are all kept as premises: the twist model with the 8399be55 Weierstrass model M (COND), R-inv, d₀ = the 11D SUSY structure (COND, 8399be55 §A premise 1), Emb-T (E₈ ⊃ Spin(16)/⟨ω⟩, 248 = 120 ⊕ 128, cited Lie theory), [M] (f is an isometry, from cc21b272), and **Eq-L (new, PP)**.
- Row 10 holds for d₀ **and** for every c-fixed d. Its truth as an implication therefore does not depend on the COND identification in row 11. Row 11 only matters for which of the 8 is physical.

**(6) Parent tally.** See §4.

## 3. The 12 rows (PP grades)
| # | item | MR2 | PP |
|---|---|---|---|
| 1 | TY₆ ⊕ ℝ ≅ π*(TΣ ⊕ L ⊕ ℝ³); spin structures ↔ J[2] torsor with base d₀ | PROVED impl. | **PROVED** as implication (twist model) |
| 2 | δ(f; d₀) = 0 for every orientation-reversing r | PROVED impl. | **PROVED** as implication (twist model, M, **Eq-L**); naturality argument §2(3) |
| 3 | J[2] fixed counts 8, 4, 2, 4, 1; c fixes the 8 listed | PROVED impl. M | **PROVED** as implication of M (exact re-run D1–D3) |
| 4 | R_a specified; df ⊕ R_a lifts to a connection-preserving Spin(7) automorphism | PROVED impl. | **PROVED** as implication (rows 1–2, [M], Emb-T) |
| 5 | Ad_L = df ⊕ R_a on so(6), so(10), (6,10) | PROVED "exact" (allclose) | **PROVED** by PP exact ℤ[i] (X4, X5) + algebra; MR2 evidence alone = COND |
| 6 | L² = +1 on 128₊, 128₋, 256 | PROVED "exact" (allclose) | **PROVED** by PP exact ℤ[i] (X3) + algebra; MR2 evidence alone = COND |
| 7 | global square constant +1 | PROVED impl. R-inv | **PROVED** as implication of R-inv (Y₆ connected; codim-3 fixed locus checked) |
| 8 | contrasts: 3-vector → −1; none → odd, not in Spin(16) | PROVED (allclose) | **PROVED** by PP exact (X6–X8) + algebra |
| 9 | R_a preserves the trivial Spin(10) connection; Spin(6) connection preserved | PROVED | **PROVED** (as implication of [M] for the Spin(6) part) |
| 10 | E-T connection-preserving involutive E₈ lift exists (r in the c-class; d₀ or any c-fixed d) | PROVED impl. | **PROVED as implication** (twist model/M, Eq-L, R-inv, Emb-T, [M]) |
| 11 | E-T's spin structure is the 11D SUSY d₀ | COND | **COND** |
| 12 | E-T is the physical 1a datum (Bianchi, J_M5 ≥ 0) | OPEN | **OPEN** |
**Report tally: PROVED 10 · COND 1 · OPEN 1 · REF 0 = 12.** This agrees with MR2. The changes are in the grounds: rows 5, 6 and 8 are carried by PP's exact proof, and row 2 adds Eq-L.

## 4. Verdict on cc21b272 row 12, and the parent tally
- **Row 12 (E-T connection-preserving involutive E₈ lift): OPEN → PROVED as an implication.**
  - Premises: twist model + 8399be55 M (COND), Eq-L, R-inv (r in the c-class), Emb-T, [M].
  - Scope: d₀ or any of the 8 c-fixed d. For a non-fixed d, no lift exists.
  - The topological lift (12′, n = 0, D4) is unchanged.
  - Whether E-T is the physical 1a datum stays OPEN.
- **Parent E₈ tally:** 15/2/6/0 → **16/2/5/0 = 23**, plus 1 bookkeeping row.
  - 12′ was a scoped sub-statement "included in 12" (erratum 55941d82), not a separate graded row, so there is no double count.
  - This counts **row 12 only**. The row 14 E-S± audit (51cd8bc8) is separate and still pending; it is not pre-added here. E-Λ± and E-S± are untouched.
- B1-c2′ stays COND overall, not adopted. Literal c2 and c2″ are unchanged. 1a is not adopted. 8399be55 stays COND as a premise. Junction UNSOLVED.

## 5. Fixes for MR2 (next additive file; do not edit 0069b9ae)
1. **(priority)** Withdraw "np.allclose … effectively exact (7f366e78)" as a ground for PROVED. Cite PP's exact ℤ[i] re-run (PP_EXACT_ET_PIN_0069b9ae_…_1024, 9b474b33… / 5a35044a…) and the algebraic identity (e_{i1}…e_{ik})² = (−1)^{k(k−1)/2}. Relabel the log's "anticommutators exact" as allclose.
2. **(priority)** Add premise **Eq-L**: under L ≅ TΣ, f acts on L by dr (no U(1) gauge function of nontrivial mod-2 winding). Rows 2, 4 and 10 rest on it.
3. Give the naturality argument for d₀ in place of "f*O ≅ O". This is the canonical V ⊕ V spin structure, with ŝ ĥ(θ) ŝ⁻¹ = ĥ(−θ) (§2(3)).
4. State that every fixed point has exactly 3 eigenvalues −1 (fixed locus Fix(r) × S², codimension 3), including μ₁ = 0 or μ₂ = 0. Fix "φ₁ fixed" to "φ₁ ∈ {0, π}".
5. State that the compensator degree must be ≡ 1 mod 4. "Single reflection" is the minimal choice, not the unique one, since m = 5 also works. Also state e_a ∈ Pin(10) \ Spin(10).
6. The odd-element "square on 128±" printout is ill-posed, since that element swaps the 128s. Report its square on ℂ²⁵⁶ (−I) instead.
7. Note that the global square needs only (df ⊕ R_a)² = id and connectedness, not connection preservation.
8. Row 10 holds for any c-fixed d, so it does not depend on row 11's COND. Say so.
