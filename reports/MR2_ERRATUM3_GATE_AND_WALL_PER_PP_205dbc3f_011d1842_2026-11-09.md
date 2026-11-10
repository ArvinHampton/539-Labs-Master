# MR2 ERRATUM3 — gate fixes per PP 205dbc3f, wall fixes per PP 011d1842, and the batch-1 follow-ups — 2026-11-09, written 19:57 CST (America/Chicago)
Author: MR2. Additive; no existing file edited. Tip 7cddb188 untouched. No CERT, no Gemini, nothing sent. Nothing adopted. Nomenclature: "resonant algebra" (OW 81b74a31); not otherwise used here.

Inputs (sha = sidecar, verified at 19:56 CST):
- PP gate audit FINDINGS_PP_AUDIT_MR2_ERRATUM2_GATE_SYMBOLIC_EINSTEIN_GLOBAL_CURVATURE_2026-11-09_1933.md, 205dbc3f067a31413e803d984010815dcf14c3a4d95835a5300b4dfe07f93eee.
- PP wall audit FINDINGS_PP_AUDIT_MR2_ERRATUM2_WALL_PER_aeb9ab13_2026-11-09_1946.md, 011d1842efb1a2b89846fe1e6b0c06863a0fe2161358dc50c440898d99f810a1.

## Files (reports/)
| file | sha256 |
|---|---|
| MR2_ERRATUM3_GATE_AND_WALL_PER_PP_205dbc3f_011d1842_2026-11-09.py | 511d7d7a10f37e4337e1655f6e861b1eb461bf6f5bd1143956b441e3271bc34b (frozen before run) |
| MR2_ERRATUM3_GATE_AND_WALL_PER_PP_205dbc3f_011d1842_2026-11-09.log | 7e38f85b5c05398ac704e65e65ecf672873696b7654d9b050d75eef810ac07d8 (exit 0, 20 s, dps 40) |
| MR2_TWISTED_VACUA_EINSTEIN_SYMBOLIC_AND_GLOBAL_CURVATURE_2026-11-09_MN2_SYMBOLIC_REDUCED_TIMEOUT_SCRATCHLOG.log | 0c2f7448104e291f8233ca42e62e0c3628360a999803ad94e9e7a6b402864c66 (verbatim copy of /workspace/scratch/mr2_1750/symred_MN2.log, mtime 19:07 preserved; produced by _MN2_SYMBOLIC_REDUCED.py 3cfbe7da…, sidecar MATCH) |
| this .md | see .md.sha256 |

## A. Gate audit 205dbc3f
- **G1. Disclosure — ACCEPTED.**
  - The 8 "random" exact Einstein test points were seed-fixed (random.seed(20261109); numerators and denominators in 1..97). They are the same 8 points for all four candidates.
  - Schwartz–Zippel was not invoked. Even with a stated sample set and degree bound it would give only a probability, not a proof.
  - PP's 8 fresh points (secrets RNG, 1..997) and its independent engine reproduce the exact zeros (PP §3c).
- **G2. All points — ACCEPTED, no degree bound given.**
  - "Einstein at all points" stays **CONDITIONAL**, and the full symbolic zero is **OPEN**.
  - Why not quick: the deterministic route (grid / combinatorial Nullstellensatz, or d_b+1 symbolic slices) needs explicit a priori bounds deg_{s_a}P and deg_{s_b}P. These have to be tracked through the inverse metric, the Christoffel symbols, the Riemann tensor and the flux terms, with denominators that are powers of (1+s²), Δ_num and the block determinants.
  - That bookkeeping is not quick, and both of PP's one-slice attempt and the reduced symbolic run exceeded their time caps.
  - Path: degree tracking plus slices, about 1–2 h of compute on an unloaded box.
- **PENDING → OPEN — the MN2 symbolic reduced run.**
  - The scratch log (filed above) shows the field set up (QQ(X1, s_a, s_b), minpoly 8X₁⁵ − 1) and then exit_code=124 (timeout). It never printed a "FULL SYMBOLIC ZERO" line.
  - Graded **OPEN (timeout, not a failure)**: it shows neither zero nor nonzero. Not rerun.
- **G3. KK — ACCEPTED, CONDITIONAL.**
  - Under the invariant-mode scope (OW 49b04146 / 91e69b38; Group A per 8b26c786), the lowest nonconstant invariant Σ eigenvalue is ≈ 23.0786 = λ₁([0;2,3,8]). It is the same for the order-48 and order-96 groups.
  - Unwarped MN2: m²L₅² = (F₀/G₀)·λ = 2 × 23.0786 = **46.16**. F₀/G₀ = 2 exactly is PROVED.
  - The eigenvalue and "no invariant vector at λ₁" (Cook Lemma 3.15, Faber–Krahn sketch) are CONDITIONAL: literature numerics plus a sketch-level check.
  - 7.68 = 2λ₁ is kept only as the untruncated full-tower estimate.
  - Wilson lines, spin structure and warping are not included, and the KK spectrum stays OPEN.
- **G4. Bolza values — the requested upgrade is ACCEPTED for the systole only.**
  - PP's fix 4 concerns the **systole** 2 arccosh(1+√2) = 3.0571418390, which is now PROVED: PP 384096a8 computer-assisted, plus MR2's independent enumeration in ERRATUM2 5511845e (15241 elements, minimum |tr| = 2+2√2).
  - **Bolza λ₁ ≈ 3.8388872588 stays CONDITIONAL.** PP's own §6 keeps it CONDITIONAL.
    - Strohmaier–Uski (arXiv:1110.2150 §5.3) report a rigorous error bar of about 1e-6 from their implementation. MR2 has not re-derived or rerun that enclosure.
    - KMP's bound λ₁ < 3.8388976481 for genus 2 is verified in exact rational arithmetic in their paper, but it is an upper bound, not the value.
    - So no in-repo, math-checked enclosure exists, and under OW 36683379 a citation alone is not PROVED.
  - "KMP bound > S–U value" is PROVED as arithmetic (difference 1.04e-5).
- **G5. Two-root branch — ACCEPTED.** For z=2 and z=3 the minimal polynomials (16X¹⁰ − 1228X⁵ + 81 and 3X¹⁰ − 122X⁵ + 6, irreducible) each have two positive real roots: 0.5807 / 2.3820 and 0.5476 / 2.0977. The x2map identity fixes the physical branch (checked numerically to 40 digits). The zero test, divisibility by an irreducible minpoly, covers every conjugate, so the branch does not affect it. PROVED (PP §3a).
- **G6. Precision rule — ACCEPTED as a heuristic (CONDITIONAL).**
  - Precision loss near the coordinate edges grows with 1/distance. The working rule is dps ≳ 8|log₁₀ d| + margin, where d is the distance to the nearest coordinate edge, mainly β → π/2 (see W4).
  - Corner residuals of about 1.9e-26 at dps 60 are consistent with this.
  - The rule is not sharp: dps 90 already sufficed at d = 1e-12, where the rule asks for 96.
  - Required practice: confirm any edge value by a dps-doubling comparison.

## B. Wall audit 011d1842
- **W1. Fix-7 baseline adjudication — REVERSED (ACCEPTED).** Verified in two parts:
  - **Exact baseline (PROVED).** NO_SOURCE is smooth MN2, which has the isometry (ρ, x) → (ρ + c, e^{c}x) with a ρ-independent internal block. So every mixed G^a_b is constant in ρ, and the raw baseline is exactly 2Wε√(wF₀)G^a_b/k, linear in W.
  - **MR2's quadrature (PROVED, log (A)).** The 48-node GL rule in u = tanh(ρ/ε) integrates a ρ-constant to 0.980833 × exact at W = 4 and **0.445879 × exact at W = 10**. That is, exact/quadrature = **1.019542** and **2.242760**, which are PP's 1.0195 and 2.243.
  - Hence **PP's ρ-space aeb9ab13 baseline was exact, and MR2's u-space raw baselines were low.** ERRATUM2's attribution ("PP's 96-node baseline differs because of quadrature") is withdrawn: **REFUTED**.
  - MR2's "1.14× from W = 4 to 10" was an artefact of MR2's own rule; the true ratio is 2.5.
  - KINK − NO_SOURCE is unaffected (same nodes, the bulk error cancels) and stays PROVED.
  - Future practice: integrate the bulk part analytically or in ρ, and use u only for the kink part.
- **W2. "Double coordinate degeneracy" qualifier — REFUTED (ACCEPTED).**
  - Verified from MR2's own POLE log 508ac55a: at (α, β) = (1e-3, π/2 − 1e-12), which is far from the α-pole, the value is 2.2e27 at dps 40 and 511.80792853607 at dps 60, against 511.807928712851 at dps 90/120 (off by 1.8e-7).
  - So the artefact follows the distance to β = π/2 (cancellation in cos β), not double degeneracy.
- **W3. L ≅ K assumption dropped — ACCEPTED (PROVED).**
  - In the metric, the φ₁ circle (period 2π) is fibred by the connection a₁A with A = du/v and dA = du∧dv/v² the H² area form.
  - So deg L = (1/2π)·a₁·Area(Σ) = (1/2π)·1·4π(g−1) = **2** for g = 2 (up to orientation sign).
  - Since deg L is even, w₂(ℝ² ⊕ L) = 0 and the S³ bundle is trivial **unconditionally**. No identification of L is assumed.
- **W4. Precision-artefact text, reworded — ACCEPTED.**
  - Replacement: "Near the coordinate edge β → π/2, evaluating the polar-coordinate curvature loses about 8|log₁₀ d| digits to cancellation in cos β, where d is the distance to the edge. Values there must be confirmed by a dps-doubling comparison."
  - The rule is a heuristic (CONDITIONAL; see G6).
  - bd47ff5e's dps-40 values (edges at 1e-6) are unaffected; they were independently confirmed in aeb9ab13.
- **W5. Fixed-φ convergence — ACCEPTED (PROVED, log (B)).**
  - Horizontal ⟨(wF₀)²⟩: 0.3341509085724862 / 0.3341509085714847 / 0.3341509085714847 at GL 24×16 / 48×32 / 96×64.
  - Fixed-φ ⟨(wF₀)²⟩: 0.3396992600859116 / 0.3396992600857756 / 0.3396992600857756.
  - N_req/2N (no warp): 1.2876110196 and 1.0315626942, stable to 10 digits.
  - The 24×16 values carry a relative error of about 3e-12 (horizontal) and 4e-13 (fixed-φ); 48×32 and 96×64 agree to all 16 printed digits. All ERRATUM2 ranges stand. The measure stays CONDITIONAL.
- **W6. Analytic supremum — skipped** (optional, not trivial). "sup Riem² = 3408" stays CONDITIONAL.

## C. Batch-1 follow-ups (PP 985d404d, as relayed by the parent; not located on disk by MR2 at 19:56, applied as a grading clarification)
- **Row #17** is restated as "thin limit kε → 0 valid: PROVED **as an implication given existence; existence of the (2c) profile is OPEN**". The OPEN status stays visible.
- **Tally-convention line corrected.** The b964cad1 note wrongly presented the strict reading as PP's convention.
  - PP's ruling: a claim that **states** its premise is graded as an implication, PROVED if the implication is proved. "PROVED with a COND premise counts as COND" applies only to premises that are used but not stated.
  - So the alternative 14/12/8/5 is **withdrawn**. The batch-1 final tally stays **PROVED 17 / COND 9 / OPEN 8 / REF 5**.

## D. Tallies
- **Gate audit (PP 205dbc3f), updated:** 16 / 5 / 3 / 0 with 1 PENDING becomes **16 / 5 / 4 / 0** (PENDING → OPEN, timeout).
- **Wall audit (PP 011d1842): 17 / 5 / 4 / 2**, accepted as is. Both REFUTED items are MR2's: the baseline attribution and the double-degeneracy qualifier.
- **This erratum's own claims** (one label per atomic claim; stated premises graded as implications):
  - **PROVED 8:**
    1. exact baseline linear in W
    2. u-rule factors 1.019542 / 2.242760
    3. deg L = 2 from the metric, so w₂ = 0
    4. ⟨(wF₀)²⟩ convergence
    5. Bolza systole value
    6. two-root branch / all-conjugate zero test
    7. F₀/G₀ = 2, so m²L₅² = 2λ
    8. seed disclosure (bookkeeping)
  - **COND 4:**
    1. Einstein at all points
    2. Bolza λ₁ value
    3. lowest invariant eigenvalue 23.0786 → 46.16
    4. dps heuristic
  - **OPEN 2:** full symbolic zero (timeout); deterministic degree-bound certificate.
  - **REF 2:** MR2's baseline attribution; the double-degeneracy qualifier.
- Carried: junction **UNSOLVED**; KK spectrum OPEN; sup = 3408 CONDITIONAL; MN N=2 CONDITIONAL (19a88b19).

## E. Disagreements
- None on the math.
- One scope clarification: the request to "mark the Bolza λ₁ value PROVED" is not what PP's fix 4 says. PP upgrades the **systole**, which is accepted. **λ₁ stays CONDITIONAL**, because no rigorous enclosure has been rechecked in-repo, and PP's §6 agrees.
