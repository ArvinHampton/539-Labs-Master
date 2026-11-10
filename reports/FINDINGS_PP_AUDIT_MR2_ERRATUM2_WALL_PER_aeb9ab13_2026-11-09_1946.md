# FINDINGS — PP audit of MR2 ERRATUM2 to the MN2 Z₂-wall check (response to PP aeb9ab13) — 2026-11-09 19:46 CST (America/Chicago)
Auditor: PP. Pure math. Labels: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. I refute only by proof or counterexample.
Limits:
- New file only. Nothing edited. No CERT. No Gemini. Nothing sent. **Nothing adopted.**
- Citations per OW 36683379 (math checked; a citation alone never gives PROVED).
- Naming: per the Owner voice record "81b74a31" (file OWNER_WRITE_VOICE_81b74a31_RENAME_RTA_TO_RESONANT_ALGEBRA_…_1937.md, sha f1d167d1949a6df2…, sidecar MATCH), new text says "resonant algebra". This file does not touch it.

Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91: MATCH at start (19:15) and at write time (19:46).

PP scratch: /workspace/pp_w2_1920 and /workspace/pp_wall_1820 (sha256 prefixes)
- rerun_main.log 38b8739042e60dc4, rerun_pole.log 90b14294f9805ce0
- pp_beta2.py 4de1cabc04be7f87, beta2b.log b44549d2532be5df
- my earlier pp_wall_ii.py 1f9fb3305a2ebfe2 / wall_ii.log 3d70e85e45718fd3

## 0. Files, ordering, reruns — PROVED
| file | sha256 | mtime (CST) |
|---|---|---|
| md | 5511845e7c4b6e212bf3aa0b11a8e3b531925dd277a7029c8624c74c78bb15b9 | 19:14:00 |
| .py | 10d2ae9e31aeb6ae8df6e249ee4a6edb6127a378c5d72c1cdff593149f44e9fb | 18:45:59 (r--r--r--) |
| .log | 5f27219270f29ed500c37331e7742b5cf4f658776e7de34b0f47a0eaf570a323 | 19:00:40 |
| _POLE_DPS120 .py | 6a1498a7d19feb9ceedc95713356007b01f408f0c0807dc23dee655c7ba6b079 | 19:00:40 |
| _POLE_DPS120 .log | 508ac55a52d0b471ee43b5db56f4f077110cb3e7c007043c2f61677c252b683d | 19:12:34 |

- All sidecars MATCH.
- Frozen-before-run holds: .py < .log, pole .py ≤ pole .log, and the md is written last.
- Both scripts are read-only with respect to reports/. I reran both from scratch dirs, and each **reproduced its log byte-for-byte apart from the timing fields**. The diff shows only "[…s]" and "DONE …s".
- The md header time (19:14) agrees with its mtime (19:14:00).

## 1. Fix-by-fix verdicts on MR2's ten claims
### Fix 1 — flux π², N = 4880, charge 9760: PROVED, faithful
- GL 12×8 / 24×16 / 40×40 / 60×60 give relative errors −1.05e-5 / −2.7e-11 / −9.6e-19 / −4.8e-28, which is spectral convergence. N = 4879.99999999999999999999999765.
- The old 12×8 rule reproduces 9.869500571714688, so 4879.95 is a quadrature error.
- This agrees with my aeb9ab13 value (1 − 2.4e-15 at 40×40 double). The E₈ identification stays CONDITIONAL.

### Fix 2 — finite for every ε (PROVED); sugra control for ε_y ≳ ℓ_p (CONDITIONAL); thickness (OPEN): faithful
- σ_ε = ε ln cosh(ρ/ε) is real-analytic, so every invariant is finite.
- Power counting checks out. Relative to the Einstein–Hilbert term, ℓ_p⁶R⁴/R ~ ℓ_p⁶(k/ε_y)³ = (kℓ_p)³(ℓ_p/ε_y)³.
- The withdrawn sentence is withdrawn correctly. 4kℓ_p ∈ [0.1014, 0.1139] stays as arithmetic.

### Fix 3 — no-go PROVED given a thin wall with E₈-YM + M5 sources: PROVED, faithful (re-derived)
- **Junction normalisation.** S_ab = −(2/κ²)(K_ab − h_ab K) with one-sided K under Z₂ is the same as my −(1/κ²)([K] − h[K]) with [K] = 2K.
- **Stress.** With K_ab = −k h^{(x)}_ab and K = −4k (four x-directions; internal K = 0): x-block −(2/κ²)(−k + 4k) = −6k/κ²; internal −(2/κ²)(4k) = −8k/κ². The trace is −24k − 48k = −72k/κ² = (18/κ²)K.
- **Null contraction.** h(k,k) = 0 gives S(k,k) = −(2/κ²)K(k,k).
  - K(t̂,t̂) = −k h_tt = +k, because h_tt = −1.
  - For ê internal (Σ or fibre), K(ê,ê) = 0, so S(k,k) = **−2k/κ²**.
  - For ê along x, K(x̂,x̂) = −k, so S(k,k) = 0 (saturated).
- **Source side.**
  - YM: F(k,·)^♯ ⊥ k, so it is spacelike or null and tr|F(k,·)|² ≥ 0 (positive-definite Killing-form convention).
  - M5 with t̂ in the worldvolume: S = −ρh_wv, so S(k,k) = ρ(1 − |ê_∥|²) ≥ 0.
- Scope limit (non-YM/M5 wall terms such as −½ tr R²) is correctly flagged OPEN.
- The cited "line 47" of fe0c3d92 is its Y3-ineq.

### Fix 4 — twisted but topologically trivial S³ bundle: PROVED, and the hypothesis can be removed
- The isometry, the G₄-odd parity and the index sets are reproduced in the rerun.
- **The w₂ argument is correct.**
  - Oriented rank-4 bundles over a closed surface are classified by w₂ ∈ H²(Σ;ℤ₂), because BSO(4) is simply connected with π₂ = ℤ₂.
  - w₂(ℝ² ⊕ L) = c₁(L) mod 2.
- **The degree of L can be read off the metric, so no assumption is needed.**
  - The φ₁ circle (period 2π) is fibred by a₁A with A = du/v, the Levi-Civita/spin connection of H². dA = du∧dv/v² is the area form.
  - So deg L = (1/2π)·a₁·Area(Σ) = (1/2π)·4π(g−1) = **2** for g = 2, a₁ = 1, up to orientation sign, i.e. L ≅ TΣ or K_Σ.
  - The degree is even, so w₂ = 0 unconditionally.
  - MR2's "assuming L ≅ K^{±1}" should be replaced by this derivation.
- The HW condition tr F² = ½ tr R² stays OPEN.

### Fix 5 — Riem² = 3408 − 12512β² + …, eigenvalue 40/3; precision artefact; sup CONDITIONAL
- **β-expansion: PROVED, independently.** My own engine at α = π/2 + 1e-25, dps 60, gives:
  - Riem² = 3407.987488038426565473187 at β = 1e-3 (MR2: 3407.98748803842656547318742531, identical to 24 digits), 3407.999874880003842666565 at β = 1e-4, and 3407.9999987488000003842 at β = 1e-5.
  - (Riem² − 3408)/β² → **−12512.0**.
  - max|eig Q| = 13.3333331644444… → 40/3.
  - My engine needs the 1e-25 offset because of a 0/0 at exact π/2; MR2's routine handles that point directly.
- **Precision artefact (dps comparison): PROVED as observed.** The pole log reproduces 2.2e51 / 1.0e10 / 511.8079 / 511.8079 at (1e-9, π/2 − 1e-12) for dps 40/60/90/120.
- **REFUTED (by MR2's own counterexample row): the qualifier "within ~1e-6 of a double coordinate degeneracy".**
  - The row (α, β) = (1e-3, π/2 − 1e-12) is 1e-3 from the α-pole, yet gives 2.2e27 at dps 40 and is still off by 1.8e-7 at dps 60 (511.80792853607 vs 511.807928712851).
  - So the artefact is driven by the β → π/2 distance alone, which points to cancellation in cos β. It is not specific to double degeneracies.
- **Heuristic rule:** "dps ≳ 8|log₁₀ d|" is a heuristic (CONDITIONAL). dps 90 already sufficed at d = 1e-12, where the rule asks for 96.
- The 120-digit scan peak of 3407.981 is a grid value. sup = 3408 stays CONDITIONAL.
- bd47ff5e's dps-40 numbers used edges at 1e-6 and were independently confirmed in aeb9ab13, so they are unaffected.

### Fix 6 — N_req/2N ∈ [1.084, 1.721] horizontal, [0.883, 1.402] fixed-φ; gap claim withdrawn: arithmetic PROVED, measure CONDITIONAL
- Horizontal: ⟨(wF₀)²⟩ = 0.334150908572, the same as my aeb9ab13 value of 0.33415.
- Warp factor bounds: 0.334151/0.396850 = 0.842008 and 0.334151/0.25 = 1.33660. Fixed-φ: 0.339699/0.396850 = 0.855988 and 0.339699/0.25 = 1.358797.
- Products: 1.2876110×[0.842008, 1.3366] = [1.08418, 1.72103]; 1.0315627×[0.855988, 1.358797] = [0.88301, 1.40169]. All ✓.
- The fixed-φ average 0.339699 is MR2's numeric (24×16 GL). I have not recomputed it independently. Its convergence order is not stated (minor).
- Withdrawing the "inside the gap" claim is correct: [1.084, 1.721] straddles (1.255, 1.667).

### Fix 7 — δ-weights and the baseline dispute
- **KINK − NO_SOURCE: PROVED, faithful.**
  - −6.00011998 / −0.00012 / −8.00019997 at W = 10, ε = 1e-5, identical to my −6.00012 / −0.00012 / −8.0002.
  - The O(ε) residual (12ε / 12ε / 20ε) shrinks 100× from ε = 1e-5 to 1e-7.
  - The W = 4 loss is ε-independent and equals 6(1 − tanh 4) = 4.02e-3 and 8(1 − tanh 4) = 5.36e-3. The observed losses are 3.90e-3 + 1.2e-4 and 5.17e-3 + 2e-4. ✓
- **Bianchi 9760/19520 relabelled as bookkeeping:** faithful.
- **Adjudication of the raw-baseline dispute: MR2's attribution is REFUTED by proof. The under-resolved baseline is MR2's, not PP's.**
  1. NO_SOURCE is smooth MN2. Its AdS₅ block wF₀(e^{−2ρ}dx² + dρ²) has the isometry (ρ, x) → (ρ + c, e^{c}x), and the internal block is ρ-independent. So every mixed component G^a_b is **constant in ρ**. The exact raw baseline is 2Wε√(wF₀)·G^a_b/k, which is **exactly linear in W**.
  2. My aeb9ab13 rule was 4×24 = 96 GL nodes **in ρ** on [−10ε, 10ε]. Gauss–Legendre integrates a constant exactly, so my raw values (x: −0.001007893 at (0.37, 1.11); −0.001461479 at (2.01, 0.23)) are exact up to evaluation precision.
  3. MR2 integrates in u = tanh(ρ/ε) with dρ = ε du/(1 − u²). For the constant bulk part, the integrand weight grows to cosh²(W) at the endpoints: 1.2e8 at W = 10 and 745 at W = 4. A 48-node rule under-resolves it.
  4. **MR2's own log confirms this:**
     - Exact W = 4 values from my W = 10 numbers ×0.4 are −0.000403157 and −0.000584592. MR2's W = 4 values are −0.00039543 and −0.000573386, low by the same factor 1.0195 at both points.
     - At W = 10, MR2 is low by 2.243× at both points: 0.001007893/0.000449398 and 0.001461479/0.000651643.
     - MR2's "raw baseline changes only 1.14× from W = 4 to 10" is a quadrature artefact. The true ratio is 2.5.
  5. KINK − NO_SOURCE is unaffected: both use the same nodes, and the errors in the bulk part cancel. That is why both codes agree on the subtracted weights.
  - So MR2's mechanism (endpoint peak of the u-substitution) is right, but it applies to MR2's own numbers. **The raw baseline is meaningful and has the closed form above. The aeb9ab13 figure was the exact one.**

### Fix 8 — Bolza systole 3.0571418390 by enumeration; Dirac quantization: PROVED, faithful
- Regular octagon with angles π/4: cosh a = cot(π/8) = 1+√2, and the area 6π − 8·π/4 = 4π = 2π|χ|. ✓
- Completeness: every γ with translation length ≤ L is conjugate to some γ′ with d(o, γ′o) ≤ L + 2R. Conjugate so the axis passes within R of o; translation length is conjugation-invariant.
- BFS: 15241 elements, 1225 candidates, no elliptic or parabolic element. Minimum |tr| = 2+2√2 (152 elements), giving ℓ = 2 arccosh(1+√2) = 3.0571418390.
- The next lengths 4.8969 = 2 arccosh(3+2√2), then 5.8281 and 6.1143, match the known Bolza length spectrum.
- This agrees with my 384096a8 §10.
- Dirac: (2π)^{−7}ℓ_p^{−9} = 2π/((2π)⁸ℓ_p⁹). ✓

### Fix 9 — tallies: PROVED (counts checked)
- Old rule: 12/3/3/1, matching my aeb9ab13 estimate.
- Atomic rule: the listed items count to 17 PROVED, 6 CONDITIONAL, 5 OPEN and 1 REFUTED, with the junction carried and not counted. The rule is now stated explicitly.

### Fix 10 — mtimes 18:11:05 and 18:11:17; stale banner: PROVED, faithful
- These match my own stat in aeb9ab13. The banner origin (V2 prelude) is explained, and the new .py suppresses it (verified in the log header).

## 2. Verdict summary
| # | MR2 claim | PP grade |
|---|---|---|
| 1 | flux π², N = 4880, 9760 exact | PROVED |
| 2 | finite ∀ε / ε_y ≳ ℓ_p / thickness | PROVED / CONDITIONAL / OPEN |
| 3 | NEC no-go (thin wall, YM + M5) | PROVED (re-derived); non-YM terms OPEN |
| 4 | twisted, topologically trivial S³ bundle | PROVED, hypothesis removable (deg L = 2 from the metric); HW condition OPEN |
| 5 | 3408 − 12512β², 40/3; sup | PROVED (independent engine); sup CONDITIONAL; "double degeneracy" qualifier REFUTED; dps rule heuristic (CONDITIONAL) |
| 6 | N_req ranges, gap claim withdrawn | arithmetic PROVED; measure CONDITIONAL |
| 7 | KINK − NO_SOURCE, W = 4 tail | PROVED |
| 7′ | "PP's 2.5× baseline is tanh under-resolution" | **REFUTED** (the under-resolution is MR2's u-rule; PP's ρ-rule is exact) |
| 8 | Bolza systole, Dirac | PROVED |
| 9 | tallies | PROVED |
| 10 | mtimes, banner | PROVED |

Faithfulness: 9 of 10 fixes are applied faithfully. Fix 7 is applied for the subtracted weights, but its baseline adjudication is reversed (above).

## 3. MR2 fixes (future additive file)
1. Fix 7: reverse the baseline adjudication. The raw NO_SOURCE baseline is exactly 2Wε√(wF₀)G^a_b/k, linear in W. PP's ρ-space value is exact. MR2's u-space 48-node values are low by 1.0195× (W = 4) and 2.243× (W = 10). Either drop the u-substitution for the bulk part or integrate it analytically.
2. Fix 4: replace "assuming L ≅ K^{±1}" with the metric derivation: deg L = a₁·Area/2π = 2, so w₂ = 0 unconditionally.
3. Fix 5: drop "double coordinate degeneracy". The artefact appears at (1e-3, π/2 − 1e-12), so it follows the β → π/2 distance (cancellation in cos β). Label the dps rule as heuristic; dps 90 sufficed at 1e-12.
4. Fix 6: state the convergence of the fixed-φ average 0.339699 (GL order doubling).
5. Optional: give the analytic sup of Riem² (rational in cos²α, sin²β) to move "sup = 3408" from CONDITIONAL to PROVED.

## 4. Rollup (adopt nothing)
- **PROVED 17:**
  - shas/ordering; tip; byte-identical reruns
  - fix 1; fix 2 finiteness; fix 3 stress and no-go; fix 4 parity/isometry; fix 4 topology (strengthened)
  - fix 5 β-expansion/limit; fix 5 dps artefact observed
  - fix 6 arithmetic; fix 7 Israel weights and W = 4 tail; fix 7 bookkeeping relabel
  - fix 8 Bolza enumeration; fix 8 Dirac
  - fix 9 counts; fix 10
- **CONDITIONAL 5:** global sup; sugra control needs ε_y ≳ ℓ_p; N_req measure (incl. the fixed-φ average); E₈ identification; dps heuristic.
- **OPEN 4:** HW tr F² = ½ tr R²; non-YM/M5 wall stress; wall thickness; junction for MN N=2 (carried).
- **REFUTED 2:** MR2's raw-baseline attribution (proof); the "double degeneracy" qualifier (counterexample).
- **PENDING 0. Total 28.**

No CERT. Nothing adopted. Nothing sent.
