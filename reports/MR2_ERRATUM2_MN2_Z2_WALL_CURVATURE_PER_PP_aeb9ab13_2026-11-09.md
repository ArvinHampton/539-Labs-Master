# MR2 ERRATUM2 to the MN2 Z₂-wall curvature check — fixes requested by PP audit aeb9ab13 — 2026-11-09, written 19:14 CST (America/Chicago; header time = time of writing, mtime follows within minutes)
Author: MR2 (executor). Additive file. No existing file edited. Labels: PROVED / CONDITIONAL / OPEN / REFUTED. No CERT, no Gemini, nothing sent outside. Nothing adopted on anyone's behalf; this records MR2's own corrections.

Inputs (sha256 re-verified against sidecars at 18:41 and 19:12 CST):
- MR2 main: MR2_MN2_Z2_WALL_BOUNDARY_CURVATURE_E8_BOLZA_2026-11-09.md bd47ff5e8f62a6226680a93107cacae8c8be573399e1f101a2dc57635f03fbfb (mtime 18:11:05); .py ce94face…; .log 7d0728e1… (mtime 18:09:53)
- MR2 erratum 1: MR2_ERRATUM_MN2_Z2_WALL_BOUNDARY_CURVATURE_SYSTOLE_LABEL_2026-11-09.md 2368ffbdc6cd6bbe9482e476a085f5d3193da21ef1ea5e2324d3a4a44bf6f295 (mtime 18:11:17)
- PP audit: FINDINGS_PP_AUDIT_MR2_MN2_Z2_WALL_CURVATURE_E8_2026-11-09_1840.md aeb9ab130c11ceeebe475b1b1da12e61c6dc294aaf23c4b4fb2166dda5cae128 (read in full)
- PP fe0c3d92: FINDINGS_PP_AUDIT_NL_1800_E8_STRESS_BOLZA_AND_ERRATA10_11_2026-11-09_1807.md fe0c3d92fdfac839653f9358f0a2c193c91a9e9dd42d46bbcbc6d58e1b794ae3 (sidecar MATCH)
- Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, untouched (checked at start and at write).

## Files (reports/)
| file | sha256 |
|---|---|
| MR2_ERRATUM2_MN2_Z2_WALL_CURVATURE_PER_PP_aeb9ab13_2026-11-09.py | 10d2ae9e31aeb6ae8df6e249ee4a6edb6127a378c5d72c1cdff593149f44e9fb (frozen chmod a-w 18:45:59, before the run) |
| MR2_ERRATUM2_MN2_Z2_WALL_CURVATURE_PER_PP_aeb9ab13_2026-11-09.log | 5f27219270f29ed500c37331e7742b5cf4f658776e7de34b0f47a0eaf570a323 (exit 0, 618 s, dps 60) |
| MR2_ERRATUM2_MN2_Z2_WALL_CURVATURE_PER_PP_aeb9ab13_POLE_DPS120_2026-11-09.py | 6a1498a7d19feb9ceedc95713356007b01f408f0c0807dc23dee655c7ba6b079 (frozen before its run) |
| MR2_ERRATUM2_MN2_Z2_WALL_CURVATURE_PER_PP_aeb9ab13_POLE_DPS120_2026-11-09.log | 508ac55a52d0b471ee43b5db56f4f077110cb3e7c007043c2f61677c252b683d (exit 0, 359 s) |
| this .md | see .md.sha256 |
Routines are exec'd from the frozen V2 .py (sha ad134752…, checked by assert); its stdout banner is suppressed. The wall metric is rebuilt with the same construction as ce94face. Nothing was tuned: grids, ε list, windows and GL orders were fixed in the frozen .py before the run.

## Per-fix verdicts
| # | PP fix | my check | verdict |
|---|---|---|---|
| 1 | ∫_{S⁴}G₄ = π², N = 4880 and wall charge 9760 exact | 60-digit GL 12×8 / 24×16 / 40×40 / 60×60: flux/π² − 1 = −1.05e-5 / −2.7e-11 / −9.6e-19 / −4.8e-28 (spectral convergence). N = 4879.99999999999999999999999765. | **ADOPTED. PROVED.** 4879.95 was quadrature error of the 12×8 rule (reproduced exactly: 9.869500571714688). |
| 2 | (iii) finite for every ε; EFT control needs ε_y ≳ ℓ_p | Agree; argument below. | **ADOPTED** (finite-for-every-ε PROVED; EFT control CONDITIONAL; thickness OPEN). |
| 3 | NEC also fails along t+Σ; no-go PROVED via fe0c3d92 | fe0c3d92 Y3-ineq checked line by line, hypotheses verified below. | **ADOPTED. PROVED** (given thin-wall Israel and E₈-YM + M5 source content). Scope limit made explicit. |
| 4 | C3 fixed set = AdS₅ × (S³ bundle over Σ twisted by φ₁); HW trF² = ½trR² OPEN; parity+C→−C PROVED | Agree, with one refinement. | **ADOPTED with a MODIFICATION**: the S³ bundle is metrically twisted (not a Riemannian product) but topologically trivial, ≅ Σ × S³. |
| 5 | sup Riem² = 3408 (eig 40/3) at β → 0; rerun edge refinement | Rerun on the correct edge at dps 60, plus a dps-120 global scan. | **ADOPTED.** Limit PROVED to 26 digits; global sup CONDITIONAL. New finding: dps-dependence near coordinate edges (below). |
| 6 | N_req omits x-block warp (factor 0.84–1.34) | Reproduced: horizontal [0.842008, 1.3366]; also fixed-φ [0.855988, 1.3588]. | **ADOPTED.** Measure CONDITIONAL; NL's gauge-dependence challenge noted. |
| 7 | Bianchi 9760/19520 are bookkeeping; δ-weights as KINK − NO_SOURCE with window | Rerun with two windows and two ε. | **ADOPTED, plus the reason PP's raw baseline differed from mine** (quadrature, below). |
| 8 | OW 36683379 regrades: Bolza value PROVED; normalisations PROVED; LOSW not needed | Independent Bolza enumeration; Dirac check by hand. | **ADOPTED.** |
| 9 | State tally rule (~12/3/3/1) | 12/3/3/1 reproduced in the old convention; new explicit per-claim rule given. | **ADOPTED.** |
| 10 | Header times; stale log banner | Fixed below and in the new .py. | **ADOPTED.** |
No fix is disputed.

## Details
### Fix 1 — flux and N (PROVED)
- Log §1: |∫G₄| (uplift, λ = 1/16) = 9.86960440108935861883449099512… vs π² = 9.86960440108935861883449099987…, at GL 60×60.
- Errors fall geometrically with order, as expected for an analytic integrand on S⁴. So N = 4880 and the wall charge [G₄] = 2G₄ ⇒ 2N = 9760 are exact. This also agrees with closure of G₄ (cohomology class) and with the AdS₇×S⁴ normalization (V2 log).
- E₈ identification of the wall source (tr F∧F − ½ tr R∧R): **CONDITIONAL** (HW hep-th/9603142; anomaly-inflow math not rechecked). Unchanged.

### Fix 2 — (iii) reworded
- **PROVED:** for every ε > 0 the smoothed metric (σ_ε = ε ln cosh(ρ/ε)) is real-analytic, so every invariant is finite. Only the thin-wall limit ε → 0 diverges (as 1/ε², coefficients unchanged from bd47ff5e).
- **CONDITIONAL (power counting):** with Riem ~ k/ε_y at the centre, any 11D higher-derivative term relative to the Einstein–Hilbert term is at least (kℓ_p)(ℓ_p/ε_y)^m with m ≥ 1. Examples: ℓ_p⁶R⁴/R ~ (kℓ_p)³(ℓ_p/ε_y)³; ℓ_p^{2n−2}∇^{2n−4}Riem²/R ~ (kℓ_p)(ℓ_p/ε_y)^{2n−3}. Terms linear in curvature are total derivatives or field-redefinable.
  - kℓ_p ∈ [0.0254, 0.0285]. So the derivative expansion, not ℓ_p²√Riem² < 1, is the binding criterion. It fails at ε_y ~ ℓ_p because m is unbounded.
  - "Two-derivative sugra controls the wall" therefore needs ε_y ≳ ℓ_p.
  - The old sentence "bounded only if ≥ ℓ_p thick / reaches 1 at 0.114 ℓ_p" is **withdrawn**. The arithmetic 4kℓ_p ∈ [0.1014, 0.1139] stays PROVED, but it is not an EFT bound.
- **OPEN (physics premise):** the actual thickness of an HW/E₈ wall.

### Fix 3 — NEC no-go (PROVED, given hypotheses)
- Stress: S_ab = −(2/κ²)(K_ab − h_ab K) (one-sided K, Z₂). With one-sided K = −k h^{(x)} and K = −4k this gives S = −(6k/κ²)h on R^{1,3} and −(8k/κ²)h on all six internal directions. Trace S = −72k/κ² = (18/κ²)K, matching fe0c3d92 Y0.
- For null k = t̂ + ê:
  - ê internal (along Σ: 2 directions; along the fibre: 4): S(k,k) = 6k/κ² − 8k/κ² = **−2k/κ² < 0**. MR2 previously stated only the fibre.
  - ê along x: S(k,k) = 0 (saturated).
- fe0c3d92 Y3-ineq (line 47 of that file), checked:
  - Static face ⇒ K(t̂,ê) = 0. Here K is diagonal, so this **holds**.
  - Y0 gives S(k,k) = −(2/κ²)K(k,k). Here K(k,k) = K(t̂,t̂) + K(ê,ê) = k + 0 = +k > 0.
  - For E₈ YM, S(k,k) = (1/λ²) tr|F(k,·)|² ≥ 0. F(k,k) = 0, so F(k,·) ⊥ k is spacelike or null (positive-definite trace convention).
  - For M5s with tension ≥ 0 and worldvolume ∋ t̂: S(k,k) = ρ(1 − |ê_∥|²) ≥ 0.
  - Hence S_required(k,k) < 0 cannot be supplied. All hypotheses hold for this wall.
- **Scope (OPEN):** wall terms outside YM + M5 are not covered. In particular, an HW gravitational −½ tr R² contribution, or higher-derivative wall terms, could in principle carry NEC-violating stress. That is not excluded here.

### Fix 4 — C3 fixed set
- **PROVED (log §1):**
  - The metric depends on no φ (symbols: F0, G0, X1, X2, a1, a2, α, β, r, v).
  - g_{φ₂u} ∝ a₂ = 0 for MN2.
  - The G₄ index sets are {u,v,α,φ₂}, {u,v,β,φ₂}, {u,α,β,φ₂}, {α,β,φ₁,φ₂}. Each has exactly one φ₂ leg and no r leg.
  - So φ₂ → −φ₂ is an orientation-reversing isometry with φ*G₄ = −G₄, and together with C → −C it is a symmetry of the solution.
- **PROVED:** the fixed set in each S⁴ fibre is {μ₂ sin φ₂ = 0} = S³ ⊃ {μ₂ = 0}. The φ₁ circle inside it is fibred with connection a₁A_Σ (a₁ = 1), so the fixed set is AdS₅ × S(ℝ ⊕ L ⊕ ℝ) → Σ, with L the φ₁ line bundle. Its induced metric is **not** a Riemannian product (the connection has curvature). PP's correction is adopted.
- **Modification, PROVED:**
  - ℝ² ⊕ L is an oriented rank-4 bundle over a closed surface. These are classified by w₂ ∈ H²(Σ;ℤ₂), since π₁SO(4) = ℤ₂.
  - w₂ = c₁(L) mod 2 = (2 − 2g) mod 2 = 0 for the MN N=2 twist (L ≅ K_Σ^{±1}, degree ±2).
  - So the S³ bundle is topologically trivial: fixed set ≅ AdS₅ × Σ × S³ as a manifold, but not as a metric product.
  - This relies on the MN2 twist line bundle being K_Σ^{±1}, which is the standard MN N=2 twist (BBBW p = 2g−2, q = 0).
- **OPEN:** the HW boundary condition on this plane needs tr F² = ½ tr R² (restricted), unless tr R∧R restricted to the plane vanishes. "No Israel stress" ≠ "no source". Not computed.
- C3 stays a proposal, not the Owner's face.

### Fix 5 — global maximum
- **PROVED (numerical, dps 60; log §5):** at α = π/2, β = 10^{−k} (k = 2…15), Riem² = 3408 − 12512·β² + … (residual −1.2512·10^{4−2k} at every k). At β = 1e-15, Riem² = 3407.99999999999999999999999999. max|eig Q| → 13.333333333333334 = 40/3; this eigenvalue step is double precision (numpy), so it is good to about 1e-15.
- Edge β = 1e-12, 181 α: maximum at α = π/2 (3408.0). Local 21×11 grid around (π/2, 0): maximum at (π/2, 1e-12).
- So the maximum sits at μ₁ = 1 (α = π/2, β → 0), and **the β = π/2 / α-pole edge refinement in bd47ff5e was the wrong edge (confirmed)**.
- ℓ_p²√3408/ℓ² = 0.02364884884; ℓ_p²·(40/3)/ℓ² = 0.005401308074. The bd47ff5e bounds (0.02365, 5.401e-3) stand.
- **New finding (precision, PROVED by dps comparison; POLE log):**
  - My dps-60 49×25 global scan returned Riem² = 1.01e10 at (α, β) = (1e-9, π/2 − 1e-12). That is a cancellation artefact.
  - At that point dps 40/60/90/120 gives 2.2e51 / 1.0e10 / 511.807928712851 / 511.807928712851. At (1e-6, π/2 − 1e-12): 2.2e39 / 512.05 / 511.8079… / 511.8079…
  - The same 1225 points at dps 120 give max 3407.980947366 at (π/2 + 1.234e-3, 1e-12) and min 511.807928713. Consistent with sup = 3408 at the exact point α = π/2, which is not on that grid.
  - Riem² is a smooth scalar on compact S⁴, so it is bounded. Within ~1e-6 of a double coordinate degeneracy, the polar-coordinate evaluation needs dps ≳ 8·|log₁₀ distance| + margin.
  - bd47ff5e's dps-40 run used edges at 1e-6 and agreed with 9ab8f0a6 and PP's independent values, so its reported numbers are not affected. Future scans must state dps against edge distance.
- **CONDITIONAL:** "3408 is the global supremum" (dense dps-120 scan plus edge and local refinement, not an analytic proof). The analytic route (invariants rational in cos²α, sin²β at fixed X) remains OPEN, ETA 30–45 min. Separate from any other executor's global scan.

### Fix 6 — N_req measure (CONDITIONAL)
- Log §6, 24×16 mp-GL. No-warp values reproduced: horizontal 1.28761101961, fixed-φ 1.03156269416.
- The x-block warp is √|g_x| = (wF₀)² ∈ [1/4, 2^{2/3}/4 = 0.396850…] (exact; min wF₀ = 1/2 exactly, PROVED, log §H).
- The k-weighted fibre averages are ⟨(wF₀)²⟩ = 0.334150908572 (horizontal) and 0.339699260086 (fixed-φ). Relative to the warp at the M5 location:
  - horizontal: factor ∈ [0.842008, 1.3366], so N_req/(2N) ∈ [1.08418, 1.72103];
  - fixed-φ: factor ∈ [0.855988, 1.3588], so N_req/(2N) ∈ [0.883006, 1.40168].
- So the count ratio depends on (a) the Σ measure and (b) where the M5s sit on the fibre (or how they are smeared). The earlier statement "the count matches to O(1); the anisotropy is what fails" survives. The specific 1.2876 and 1.0316 are **not** physical numbers. In particular "horizontal value inside NL's count gap (1.255, 1.667)" is downgraded: the warped range [1.084, 1.721] straddles that gap.
- NL's separate challenge that 1.0316 is gauge-dependent is recorded as **NL's challenge, under PP audit**. I take no position beyond the measure dependence shown here.
- **CONDITIONAL:** measure and M5-location premise. Arithmetic PROVED.

### Fix 7 — δ-weights as KINK − NO_SOURCE; Bianchi residuals are bookkeeping
- Window: ρ ∈ [−Wε, Wε] (proper y = √(wF₀)·ρ), 48-node mp-GL in u = tanh(ρ/ε), at dps 60. KINK − NO_SOURCE, in units of k = 1/√(wF₀), identical at (0.37, 1.11) and (2.01, 0.23):

| ε | W | x-block | ρρ | internal (all 6) |
|---|---|---|---|---|
| 1e-5 | 10 | −6.00011998 | −0.00012 | −8.00019997 |
| 1e-7 | 10 | −6.00000118 | −1.2e-6 | −8.00000197 |
| 1e-5 | 4 | −5.99609572 | −0.00012 | −7.99483426 |
| 1e-7 | 4 | −5.995977 | −1.2e-6 | −7.9946364 |

- **PROVED:** Israel −6k / 0 / −8k. The residual at W = 10 is O(ε) (12ε, 12ε, 20ε) and shrinks 100× from ε = 1e-5 to 1e-7. At W = 4 the residual is ε-independent and equals the truncated kink tail: 6(1 − tanh 4) = 4.03e-3 and 8(1 − tanh 4) = 5.37e-3, which match. So the window must be ≳ 10ε. The bd47ff5e window (10ε) was adequate.
- **Raw NO_SOURCE baseline — explanation of PP's 2.5× discrepancy:**
  - The bulk integrand is uniform in ρ, but the u = tanh substitution puts a 1/(1 − u²) endpoint peak into it, which a finite GL rule under-resolves. That is why the raw baseline does not scale with W (W = 4 → 10 changes it by only 1.14×, not 2.5×) and depends on the node count (my 32 or 48 vs PP's 96).
  - The kink part is smooth in u (sech² dρ = ε du) and is captured exactly, and the bulk part is the same function at the same nodes in both cases. So only KINK − NO_SOURCE is meaningful; the raw baseline is not.
- **Relabel:** the Bianchi residuals 9760 (no source), 19520 (wrong sign), ±9760 (misplaced) are **bookkeeping** (they follow by definition from [G] = 2G and the chosen J). They are not tests of the code. The discriminating controls are WRONG_SIGN (δ-weights flip to +6 / 0 / +8) and MISPLACED (baseline at ρ = 0), both PROVED in bd47ff5e and confirmed by PP.

### Fix 8 — regrades under OW 36683379
- **Bolza systole value 2 arccosh(1+√2) = 3.0571418389619963: PROVED (computer-assisted, independent of PP 384096a8; log §8).**
  - Regular octagon, angles π/4, opposite sides paired (Poincaré: one vertex cycle, angle sum 2π, area 4π = 2π|χ|). Apothem cosh a = cot(π/8) = 1+√2, so the generators have trace 2+2√2. Circumradius R = 2.44845.
  - Every γ with translation length ≤ L has a conjugate with d(o, γo) ≤ L + 2R. All such γ are reached by BFS over side-pairings with bound L + 3R (tile-chain argument).
  - With L = 3.6: 15241 elements in the BFS and 1225 candidates. No non-identity elliptic or parabolic element (torsion-free).
  - Smallest |tr| > 2 is 4.828427125 = 2+2√2 (152 elements). Next lengths are 4.8969, 5.8281, 6.1143.
  - Floating-point BFS (double); the margins between the length levels are > 1.8, so rounding cannot change the result.
- **Normalisations PROVED** (internal consistency): T_M2·T_M5 = (2π)^{−2}(2π)^{−5}ℓ_p^{−9} = (2π)^{−7}ℓ_p^{−9} = 2π/((2π)^8ℓ_p^9) = 2π/(2κ²). Dirac quantization holds.
- **LOSW:** V2 is a pure geometry check of the given (a, b, H); it is valid whether or not that is an LOSW solution. "LOSW solution form" stays CONDITIONAL but is **not used**.

### Fix 10 — cosmetics
- Real mtimes: main md 18:11:05, .py 18:05:28, .log 18:09:53, erratum 1 at 18:11:17. Its header "~18:15" and erratum-1 "~18:20" were wrong; the mtimes are authoritative.
- The bd47ff5e log line 1 "== MR2 adoption blockers: Riemann / systole / full EOM ==" is the V2 prelude's own banner, printed when the routines were exec'd. It is stale and cosmetic. The new .py suppresses it and prints its own banner.

## Fix 9 — tally and counting rule
- **Old convention (bd47ff5e §6 rows; compound rows counted once by headline label; V1 and V2 as two PROVED; proved-at-samples rows as PROVED):** erratum-1 9/6/3/1 plus the three OW 36683379 regrades (Bolza value, normalisations, NEC no-go: CONDITIONAL → PROVED) gives **12/3/3/1**. PP's estimate is reproduced.
- **New rule (used from now on):** one label per atomic claim. A compound row is split into its claims. Carried items (the junction) are listed but not counted. Premises are counted where they are stated as claims. Under this rule, for bd47ff5e + erratum 1 + this erratum:
  - **PROVED 17:**
    1. V1
    2. V2 geometry
    3. C2 gluing / [G₄] = 2G₄
    4. N = 4880 and charge 9760 exact
    5. (i) one-sided limits at samples
    6. (ii) Israel weights
    7. (ii) NEC no-go (given hypotheses)
    8. (iii) 1/ε² scaling and coefficients
    9. (iii) finite for every ε
    10. magnitudes arithmetic (k, ρ_w, N_req numbers, min wF₀ = 1/2)
    11. normalisations
    12. discriminating controls
    13. C3 symmetry (isometry, G₄ odd, + C → −C)
    14. C3 fixed set (twisted S³ bundle, topologically trivial)
    15. Bolza systole value
    16. systole bounds [75.95, 85.25] ℓ_p
    17. β → 0 edge limit 3408 / 40/3
  - **CONDITIONAL 6:**
    1. 3408 is the global sup
    2. exact-MN2-near-wall premise
    3. E₈ identification of the source
    4. sugra control needs ε_y ≳ ℓ_p
    5. N_req measure / M5 location
    6. LOSW solution form (unused)
  - **OPEN 5:**
    1. C3 HW condition tr F² = ½ tr R²
    2. localized backreaction / sub-ℓ_p micro-structure
    3. warping vs systole
    4. actual wall thickness
    5. non-YM/M5 wall stress (−½ tr R², higher-derivative) vs the 6:8:8 requirement
  - **REFUTED 1:** C1 (source-free smooth isometric fixed locus).
  - Carried, not counted: junction for MN N=2 **OPEN/UNSOLVED**. Nothing here solves it; it confirms the required S_ab.
- **Effect on the junction and count gap:** no change to the junction status. The count-gap comparison is now measure- and location-dependent (Fix 6).

## Open items, paths, ETA
| item | path | ETA |
|---|---|---|
| analytic global sup of Riem² (= 3408?) | maximise the rational function of (cos²α, sin²β) symbolically at the MN2 X | 30–45 min |
| C3 HW condition | compute tr R∧R restricted to the fixed set; then the E₈ bundle needed | 1–2 h, only after an Owner decision |
| non-YM wall stress | HW −½ tr R² wall term evaluated on the kink | ~1 h (literature normalization must be math-checked) |
| backreaction / micro-structure / thickness | jointly with NL Y14; beyond-sugra for < ℓ_p | days / no in-repo path |
