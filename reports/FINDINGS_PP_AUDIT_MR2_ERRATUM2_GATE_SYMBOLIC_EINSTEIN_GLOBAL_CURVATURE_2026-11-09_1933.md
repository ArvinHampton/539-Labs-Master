# FINDINGS — PP audit of MR2 ERRATUM2 (gate fixes per PP 384096a8) and the exact-Einstein / global-curvature package — 2026-11-09 19:33 CST (America/Chicago)
Auditor: PP. Pure math. Labels: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. I refute only by proof or counterexample.
Limits:
- New file only. Nothing edited. No CERT. No Gemini. Nothing sent. **Nothing adopted.**
- Citation scope per OW 36683379: any source is allowed, the math is checked where feasible, and a citation alone never makes a result PROVED.
- Outside reads: arXiv 2111.12716 (KMP), 1110.2150 (Strohmaier–Uski), 2108.11825 (Cook thesis), and the public Bolza-spectrum table.

Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91: MATCH at start (18:45) and at write time (19:33).

PP scratch: /workspace/pp_e2_1850 (sha256 prefixes)
- Scripts: pp_exact_fresh.py 0530bf92009d0c31, pp_cross.py 00c93bf125f86934, pp_slice.py 99f3b6a17f0d8094.
- Logs: exact_MN2z1.log bbeb5c52dbe8e1f4, exact_MN1z0.log aae2072ecd85ef1a, exact_BBBWz2.log 368166592d26c1be, exact_BBBWz3.log 3c08bf8b0aa63daa, cross.log dd79b3ee49bc915f, slice_MN2.log 01d51aaa387b49f8 (empty: killed by its 1500 s timeout, so no claim is made from it).

## 0. Owner record OW b0b9ae7f — PROVED (on disk, sidecar MATCH, wording quoted)
- File: OWNER_WRITE_MAINCHAT_t4407_PURSUE_ALL_OPEN_ITEMS_FOR_RESOLUTIONS_2026-11-09_1843.md, sha b0b9ae7fecd635e0735a66a7839bdf0148d65f8eba8adf032c68c0ad3c73494d, mtime 18:42:56 CST.
- Verbatim: "Pursue all for resolutions".
- Physicist's scope reading: every open decision item gets candidate resolutions with grades and a recommendation. "Nothing is adopted until the Owner chooses in own words."
- Lanes:
  - MR2: φ₂→−φ₂ vs HW gluing, DP-a/b, Layer2, R_c, KK tower (OW 91e69b38), §10 definitions.
  - PP: audits each candidate file.
- Tip untouched, no CERT, additive. The record is a pursuit order, not an adoption.
- Also read for item (1g): OW 49b04146 (sha 49b041469b7d…, 18:28:56; KK tower restricted to Bolza- and wall-ℤ₂-invariant modes, "scope choice, not a result") and OW 91e69b38 (sha 91e69b3888eb…, 18:32:08; run both Aut⁺ order 48 and full order 96). Both sidecars MATCH.

## 1. Files — PROVED (every sidecar MATCHes)
| file | sha256 | mtime (CST) |
|---|---|---|
| ERRATUM2 md | 7b9ebdaf… | 18:32:30 |
| symbolic/global md | 78cac4c4… | 18:43:57 |
| .py | d0191f02… | 18:00:15 |
| .log | 01d6e4cd… | 18:42:50 |
| _GLOBAL_CURVATURE.py | d9388162… | 18:07:32 |
| logs MN2z1 / MN1z0 / BBBWz2 / BBBWz3 | 4893f1d2… / aa28c625… / 1dae84ad… / 7d4d44d2… | 18:31:45–48 |
| _FRAME_EINSTEIN_AND_DG4_CONTROL.py / .log | dd952331… / 604aa979… | 18:07:07 / 18:17:07 |
| _MN2_SYMBOLIC_REDUCED.py | 3cfbe7da… | 18:17:29 |

- Each .py predates its log.
- **_MN2_SYMBOLIC_REDUCED: PENDING.** No log is filed. Both MN2 symbolic processes were still running at 19:15 (`ps`), and their scratch logs show only headers.

## 2. Fix-by-fix compliance with 384096a8 §14 — PROVED: 8/8 applied
| # | fix | ERRATUM2 | check |
|---|---|---|---|
| 1 | (D) wording | e^{2f} = F0 = 2/3, L² = 2/3; K = 90+144+384 = 618, Ric² = 828 | Re-derived: 40·(3/2)² = 90; 4·6² = 144; 2·4·3·16 = 384; Ric² = 180+72+576 = 828. ✓ |
| 2 | maximum location | μ₁ = 1 pole, β → 0; values 3408 / 3312 / 1939.2 / 40/3 | Log MN2z1: 3407.99999999999999999999999984 (Richardson limit). The α = π/2 profile decreases monotonically in β on the grid, from 3408.0 to 511.808. ✓ |
| 3 | warping claim, thresholds, Bolza | OPEN; 0.2784 / 0.2529 / 0.2163 / 0.1905 | Equals my 0.278 / 0.253 / 0.216 / 0.191 (384096a8 §10); the "0.19–0.28" range is mine. Bolza margins 11.0–16.0× agree. ✓ |
| 4 | z=2 PERPOINT rows | supplied in FRAME log (20 pts) | Present (read). ✓ |
| 5 | dG₄ control that can fail | λ=0 gives max\|dG₄\| ≈ max\|G₄\| (e.g. MN2 0.0886 / 0.0886); λ(1+1e-6) gives 1e-6·\|G₄\| | **Can now fail, and does (PROVED).** The response is linear in δλ, as expected since dG₄ ∝ (λ−λ*). The true-λ residual 1e-37 to 8e-37 is the FD noise floor (dps 60, h = 1e-25, so ~1e-60/1e-25 ≈ 1e-35). ✓ |
| 6 | frame residuals | ≤ 3e-60 generic, 1.4e-50 near poles, ~1.9e-26 corners; controls 5.9e-7 to 57.5 | Read every row in the FRAME log. Single-pole rows reach 1.5e-38 to 4.5e-38, and this is disclosed. ✓ |
| 7 | "all points" | kept CONDITIONAL; symbolic run PENDING | ✓ (see §3) |
| 8 | cosmetics | 14/16, β = 1e-6, 6.65e-11, header-vs-mtime rule | ✓. The ERRATUM2 header (18:28) is now *earlier* than its mtime (18:32:30), consistent with "header written at; mtime authoritative". |

Minor point: ERRATUM2 item 7 points to the symbolic md by name. That md was finalised at 18:43:57, after ERRATUM2's mtime. This forward reference is benign; the md cites ERRATUM2's sha back correctly.

## 3. Exact rational Einstein test
### 3a. Are the zeros at rational points truly exact? — PROVED (by reading the method and code d0191f02; no approximation enters the zero test)
1. **Coordinates.** In s = tan(θ/2), cos θ and sin θ are rational and dθ = 2ds/(1+s²). Every ĝ entry is therefore rational in (s_a, s_b, r, v, X₁, X₂).
2. **Warp factor.** Δ^{-2/3} never appears as a number. R(g) comes from R(ĝ) through the exact conformal formula, with ∂ω = −⅓∂Δ/Δ, which is rational.
3. **Flux.** G₄ = Δ√|ĝ| *′Ω enters only quadratically. Only |det ĝ| (rational) appears, together with Δ⁴ = e^{−12ω}.
4. **Algebraic parameters.**
   - X₁ is algebraic. I confirmed in sympy that each minimal polynomial is irreducible over Q: 8X⁵−1, 4X⁵−3, 16X¹⁰−1228X⁵+81, 3X¹⁰−122X⁵+6.
   - w = √(1+3z²) is eliminated through the BBBW identity. |x2map(X₁*) − X₂*| = 0 to 40 digits for all four candidates.
   - Numerator ≡ 0 mod minpoly ⇔ the value at X₁* is 0. The minpoly is irreducible, so zero at one root ⇔ divisible.
   - For z=2 and z=3 the minpoly has two positive real roots (0.5807 / 2.3820 and 0.5476 / 2.0977). Divisibility proves vanishing at all conjugates, so the branch question does not affect the zero test. The X₂ branch is fixed by x2map, which was checked numerically.
5. **Denominators.** Nonzero is checked numerically at 60 digits. This is rigorous when |den| is far above 10⁻⁶⁰, and the logged values are O(1).

Floating point appears only in that denominator check and in the X₁×1.1 control. **Each logged point-check is an exact proof that E_MN = 0 at that point (PROVED pointwise).** This assumes the engine implements the formulas correctly, which is cross-validated by (i) the R·Δ^{−2/3} match to V2 numerics (25 digits), (ii) the failing controls, and (iii) my independent engine (§3c).

### 3b. MR2's 32 points (8 × 4 candidates) — PROVED pointwise (log read)
- MN2: 53 components identically 0 and 13/13 nontrivial reduce to 0, at all 8 points. MN1 / z=2 / z=3: 52 identically 0 and 14/14 reduce to 0. MN2 has one more identically-zero component because a₂ = 0.
- Disclosure needed: the "random" points come from `random.seed(20261109)`, with numerators and denominators in 1..97. They are the **same 8 points for every candidate**, because each candidate ran in its own process with the same seed.

### 3c. PP rerun at FRESH points (secrets RNG, numerators/denominators in 1..997, MR2 frozen engine) — PROVED pointwise
| candidate | fresh points (r, v, s_a, s_b) | result |
|---|---|---|
| MN2 | (75/602, 55/163, 5/176, 971/297), (277/46, 841/367, 523/846, 795/808), (5/6, 187/241, 581/94, 681/233), (455/417, 231/695, 229/478, 93/97) | **13/13 exact zero at each of 4** |
| BBBW z=2 | (134/777, 14/597, 164/95, 297/842), (559/855, 106/249, 389/215, 236/13) | **14/14 at each** |
| MN1 | (34/121, 787/976, 758/3, 507/419) | **14/14** |
| BBBW z=3 | (124/439, 179/317, 224/589, 911/155) | **14/14** |

- **Exact controls at a fresh MN2 point** (605/478, 81/37, 496/803, 871/162): λ = 1/8, λ = 0 and flux × 11/10 each leave **13/13 components nonzero**. The λ(1+1e-6) control was not reached; I stopped the run to free CPU.
- MR2's own z=2 exact controls are confirmed from its log: λ = 1/8 → 15 nonzero, λ = 0 → 15, flux × 11/10 → 15, X₁×1.1 → |E| = 8.18.
- **Independent cross-check (my own engine:** own Christoffels, CLP Ω, λ_CLP = 1/8; r = v = 1; α = 2 atan s_a, β = 2 atan s_b; dps 60) at the same 8 fresh points:
  - Frame rel |E|/|Ric| = 6.2e-61 to 4.0e-55.
  - The 1e-55 values sit at near-pole s_a (758/3, 5/176) or at mixed points. This matches MR2's pole-precision pattern.
  - Control λ(1+1e-6): 1.9e-7 to 4.1e-7, which **fails as it should**.
- Two codes agree, the exact test is reproduced at fresh points, and the controls discriminate.

### 3d. "All points" and Schwartz–Zippel — CONDITIONAL; a path to PROVED exists but is not yet taken
- At r = v = 1 (the homogeneity reduction holds because the metric and Ω are invariant under (t,x,r) → λ(t,x,r) and the H² affine maps, and E is covariant), each numerator is a polynomial P(s_a, s_b) over the number field Q(X₁*), of finite degree.
- **Schwartz–Zippel** bounds Pr[P(pt) = 0 | P ≢ 0] ≤ deg P/|S| for points drawn uniformly from a finite S². That is a probability statement, not a proof. MR2 also states neither S (in effect {a/b : 1 ≤ a, b ≤ 97}) nor a degree bound. **So the randomized test cannot be graded PROVED**, and MR2's CONDITIONAL is correct.
- **Deterministic upgrade (would be PROVED).** Combinatorial-Nullstellensatz / grid lemma: if deg_{s_a}P ≤ d_a and deg_{s_b}P ≤ d_b, then vanishing on S_a × S_b with |S_a| > d_a and |S_b| > d_b forces P ≡ 0. Two ways to use it:
  - (a) Derive explicit d_a and d_b by tracking degrees through the formulas. Metric entries are rational of low degree with denominators powers of (1+s²), Δ_num and the block determinants. Then exact-test a (d_a+1)×(d_b+1) grid.
  - (b) More economical: prove exact zero on d_b+1 full slices s_b = b_i, with s_a symbolic (univariate field Q(X₁,X₂)(s_a)). Then ∏(s_b − b_i) | P, and P ≡ 0 once deg_{s_b}P ≤ d_b.
  - Either route still needs an a priori degree bound. The completed symbolic run (PENDING) would make the bound unnecessary.
- My one-slice attempt (MN2, s_b = 3/7) did not finish within its 1500 s cap on this loaded box (load average 18–26). No claim is made from it.

## 4. Global maxima — values PROVED (numeric limit), global maximality CONDITIONAL
- MN2: K = 3408, Ric² = 3312, Weyl² = 1939.2 and max|eig Q| = 40/3 at α = π/2, β → 0. This matches my 384096a8 §8 and aeb9ab13.
- MN1: the α = π/2 profile is constant in β to all printed digits (K 910.372, RR 1061.54, W2 439.663, Q 6.62902062030). This is the μ₀ = 0 circle, consistent with the X₁ = X₂, a₁ = a₂ rotation symmetry of (μ₁, μ₂).
- z=2 / z=3: maxima at the μ₁ = 1 pole, 5755.40 and 7318.56.
- Richardson limits from ε = 1e-7 and 1e-8 at dps 110; the differences are 1e-10 to 1e-14, as expected for O(ε²).
- Maximality rests on a 13×13 seed grid plus golden-section refinement, so it is CONDITIONAL. MR2 correctly labels the monotonicity of the profiles as evidence.

## 5. Warping and thresholds — PROVED (arithmetic), the claim itself OPEN
- min X^{1/6} = 0.99046 / 0.93303 / 0.91347 / 0.90455.
- The thresholds 2π/(min X^{1/6}·ρ) are 0.2784 / 0.2529 / 0.2163 / 0.1905, equal to my 0.19–0.28.
- "Warping lengthens the systole" stays OPEN (withdrawn).
- Bolza value 2 arccosh(1+√2) = 3.05714183896: **PROVED** (PP computer-assisted, 384096a8; MR2's independent enumeration in its wall ERRATUM2 agrees). ERRATUM2's "CONDITIONAL as literature" should be upgraded under OW 36683379.

## 6. λ₁, the KMP bound, the KK estimate and the invariant-mode scope
- **Literature values, checked as citations:**
  - KMP arXiv:2111.12716 Thm 1.1(2): every genus-2 hyperbolic orbifold has **λ₁ < 3.8388976481**. The bound is strict; KMP verified it in exact rational arithmetic (their proof is not re-done here).
  - Bolza λ₁ ≈ 3.838887258, from Strohmaier–Uski (arXiv:1110.2150 §5.3): 3.8388872588421995…, with a rigorous error bar of 1e-6 in their implementation and multiplicity 3.
  - **MR2 attributes both numbers correctly, and the parent's "~3.83890" is the KMP bound rounded.**
  - The bound minus the value is 1.04e-5 > 0, so **the bound sits above the value (PROVED, arithmetic)**. The values themselves are CONDITIONAL (literature numerics; KMP's rigorous bound accepted, not re-proved).
- **KK normalization — PROVED (arithmetic):**
  - For a Σ-scalar mode, unwarped, m²L₅² = λ₁·F₀/G₀ (AdS₅ radius² ∝ F₀, Σ radius² ∝ G₀; the common Δ factor cancels).
  - MN2: F₀ = 2^{−4/5}, G₀ = 2^{−9/5}, so F₀/G₀ = **2 exactly** and m²L₅² = 2λ₁ = **7.6778**.
  - MN1: 4X₁⁵ = 3, giving 3λ₁ = 11.517. z=2: F₀/G₀ = 1.302776 = (√13−1)/2, giving 5.001. z=3: 0.953667, giving 3.661.
  - These match MR2's 11.5 / 7.68 / 5.00 / 3.66. As a KK mass the estimate is **CONDITIONAL**: it is unwarped, and Wilson lines and spin structure are not fixed.
- **Under the scope of OW 49b04146 / 91e69b38, the relevant eigenvalue is not λ₁:**
  - The constant mode (λ₀ = 0) is invariant, trivially.
  - **The λ₁ eigenspace has no Aut⁺-invariant and no full-group-invariant vector — CONDITIONAL (literature argument read and checked at sketch level):**
    - Cook (arXiv:2108.11825, Lemma 3.15) shows the trivial representation of the full isometry group (order 96; fundamental domain a (2,3,8) triangle, Neumann conditions) does not occur in E₁. The argument: a first Neumann eigenfunction has 2 nodal domains, so domain monotonicity and Faber–Krahn give λ > 6 > λ₁.
    - An Aut⁺-invariant f splits as f₊ + f₋ under a reflection. f₊ is excluded by Cook. f₋ is Dirichlet on a (2,3,8) triangle of area π/24, whose Faber–Krahn bound is ≫ λ₁.
    - So neither group-48 nor group-96 invariants occur at λ₁.
  - **Lowest nonconstant invariant eigenvalue ≈ 23.07856** — CONDITIONAL (literature numerics):
    - Aut⁺(Bolza)-invariant functions are functions on Bolza/Aut⁺ = the [0;2,3,8] orbifold. KMP give λ₁^{[0;2,3,8]} ≈ 23.07855 (their §4 theorem list).
    - This equals the multiplicity-1 Bolza eigenvalue 23.0785584813816 in the Strohmaier–Uski table.
    - It is reflection-even, because a reflection-odd eigenfunction would be Dirichlet on the triangle, as above. So the same value is lowest under the order-96 group.
    - **Both readings of 91e69b38 give the same lowest invariant Σ eigenvalue**, about 6.01 λ₁. Under that truncation the unwarped MN2 estimate becomes m²L₅² ≈ 2·23.0786 = **46.16**, not 7.68.
    - The wall ℤ₂ (radial; f825dfff) does not act on Σ, so it does not change this, though it does restrict the radial and fibre profiles.

## 7. MR2 fixes needed (future additive file)
1. Disclose that the 8 "random" exact points are seed-fixed and shared by all four candidates. State that Schwartz–Zippel is not invoked and would only be probabilistic.
2. To reach PROVED for all points: finish the symbolic run, or give an explicit degree bound plus a grid or slice certificate (§3d).
3. KK: under the OW 49b04146 / 91e69b38 scope, report the lowest invariant nonconstant Σ eigenvalue, ≈ 23.0786 = λ₁([0;2,3,8]), the same for groups 48 and 96. That gives an unwarped MN2 m²L₅² ≈ 46.2. Keep 7.68 only as the full-tower (non-truncated) estimate.
4. Bolza systole value: upgrade from CONDITIONAL (literature) to PROVED (PP 384096a8 and MR2 wall-ERRATUM2 enumeration), per OW 36683379.
5. For z=2 and z=3, state that the minpoly has two positive real roots and that x2map fixes the branch. The zero test covers all conjugates.
6. State the dps-versus-pole-distance rule for the corner residuals (~1e-26), consistent with MR2's own wall-ERRATUM2 precision finding.

## 8. Rollup (adopt nothing)
- **PROVED 16:**
  - OW b0b9ae7f; MR2 shas; tip; 8/8 fix compliance
  - exactness of the method; MR2's 32 exact points; PP's 8 fresh exact points; PP independent-engine cross-check
  - exact controls fail; frame residuals at samples; dG₄ control can fail
  - global-max values (numeric limit), with MN1 constant on its circle
  - (D) arithmetic; warp thresholds; KMP bound > Bolza value; KK normalization arithmetic (F₀/G₀ = 2)
- **CONDITIONAL 5:** Einstein at all points (randomized; Schwartz–Zippel not applicable as run); global maximality; λ₁ literature values; KK m²L₅² ≈ 7.68 as a physical estimate; the lowest invariant eigenvalue ≈ 23.0786 together with "no invariant vector at λ₁".
- **OPEN 3:** KK spectrum; warping vs systole; junction for MN N=2 (carried).
- **REFUTED 0.**
- **PENDING 1:** MN2 full symbolic zero (_MN2_SYMBOLIC_REDUCED, no log).
- **Total 25.**

No CERT. Nothing adopted. Nothing sent.
