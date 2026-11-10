# FINDINGS: PP audit of NL erratum 7 (1735) and NL 1736 §B–§D (no-gos for general faces, radial ODEs, localization). 2026-11-09 (America/Chicago, CST)
Agent: Professor Proof (Soft SF). Additive new file; nothing edited. No CERT. No message sent. No outside service (no arXiv read needed). No Gemini. Lock 96f8d42e §4 not used. No vacuum adopted (HOLD aaadb280). b not fixed. **§A (O1) of 1736 is NOT audited here** (covered by a separate audit); only its tally lines are counted.
Tip: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, re-hashed: **MATCH (untouched)**.
Convention throughout: K_ab = e_a^M e_b^N ∇_M n_N = −n_M(∂_a∂_bX^M + Γ^M_NP ∂_aX^N ∂_bX^P) (the NL0 / PP-lemma convention).

Targets:
- (1) NL_ERRATUM7_FACE_SOURCES_NONCONSTANT_ACCEPT_PP_f3c5d73f_2026-11-09_1735.md, sha 130e27969e0d5921029007475c185c9006d5e510abd7ec6b614e6a58d4974c71 (= sidecar).
- (2) NL_DERIVED_RESOLUTION_O1_MIXED_FACES_ODES_NONLINEAR_M5_2026-11-09_1736.md, sha 13ccd16251d055aa735dac4be75bc8e9f90d95d087ea0cff8b118efb80965f59 (= sidecar).
PP scratch: /workspace/audit-scratch/pp_1736_audit/ (each file has a .sha256 sidecar)
- resolve_rerun.log 39566c5e… (rerun of NL resolve.py)
- pp_geom_checks.py f8770b09… / .log cd0dbbb0… (8D twisted model: Killing identity, W⊥∂_φ, B0c, B2 identity, twisted-φ Lie-drag failure, D2 counterexample)
- pp_pole_check.py 58670aa5… / .log 42ca64c2… (isotropy of K⁽⁰⁾ at the loci where a φ-circle shrinks, on the real uplift metric via face.py)

## Rollup
PROVED 32 · CONDITIONAL 6 · OPEN 6 · REFUTED 2 · PENDING 0 (46 graded items).
- Headline 1: **Erratum 7 applies all 11 PP fixes and the C3 retraction faithfully.** Its tally 20/23/9/4 (56) is arithmetically consistent with its own lists; a strict recount from 1711+1713 including 1713's D4 gives 20/24/9/4 (57) (D4 was dropped as "folded into erratum 5"; disclosed, but a scoping choice).
- Headline 2: **B1 and B2 are PROVED given J1, for every real z** (B2 with explicit premises: static, C², embedded, compact in the internal directions, i.e. x-independent). The Killing identity is K(ξ,ξ) = +½ n(|ξ|²) in this convention (−½ in the K = −∇n convention); it applies. The Hessian sign in B2 is right. **B2 resolves the twisted-φ subclass that PP refuted in f3c5d73f (N2/N5) for static x-independent faces**, without Lie-dragging. PP supplies one missing step (minima on the loci where a φ-circle shrinks) and two strengthenings (the sign of 2f′−λ′ is not needed for compact faces; the result is independent of the tension sign and of the kept side).
- Headline 3: **C2 holds for static, coordinate-aligned one-variable profiles** (0 solutions, every N_b incl. 4880, both parities); r_b(t) is not covered (B6, OPEN).
- Headline 4: **D2 as stated ("no face point is totally geodesic") is REFUTED for general faces** by an explicit construction (a tilted static point with K_ab = 0). It is PROVED for constant-r faces for every z (via B0d, better than NL's g′−f′ route). The region version for general faces is OPEN; "O(1) change everywhere" is CONDITIONAL.
- 1736 header "PROVED 17" is a bookkeeping slip; the correct NL tally is 18/5/6/1 (30).

## 0. Integrity and authority
- **I1 [PROVED].** Both targets equal their sidecars. /workspace/nl-junction-1730/: face.py fd309c48…, flowlin.py b72d2296…, resolve.py f6da8509…, resolve_1736.log 39566c5e… all equal their sidecars. face.py and flowlin.py are byte-identical to the 1705 copies PP audited in f3c5d73f (I1 there). Upstream 1711 (53096d43…), 1713 (e2065e05…) and PP f3c5d73f… equal their sidecars.
- **I2 [PROVED].** resolve.py rerun from a scratch copy is **byte-identical** to resolve_1736.log (sha 39566c5e…).
- **I3 [PROVED].** Tip MATCH (header).
- **I4 [PROVED].** OW ff8a1670 is on disk: OWNER_WRITE_VOICE_9c8fa1db_t4358_PURSUE_ALL_OPEN_ITEMS_TO_RESOLUTION_ALL_BOTS_2026-11-09_1730.md, sha ff8a16701cd0832fc449c91fc9b2a2dc4ff84bf743a4fd757e07d21ddbacd441 = sidecar. 9a8ced02 was verified in f3c5d73f (A-2). Neither NL file adopts a vacuum, source, b or parity.

## 1. Erratum 7 (1735): fix-by-fix
- **E7-1 [PROVED, applied].** 1713 tally row 8 → 9; 9/9/4/0.
- **E7-2 [PROVED, applied].** Second form ρ(w_Σ+1) mis-signed; first form (2/κ²)(k_Σ − k_x) = −ρ(1+w_Σ) > 0 correct.
- **E7-3 [PROVED, applied].** "w_fib ≤ −1.2" withdrawn as REFUTED with PP's numbers (−1.1925; −1.1687/−1.1778). Brane mix redefined via NEC, T(k,k) = Σσ_i(1 − |P_ie|²) ≥ 0; conclusion PROVED at end faces, CONDITIONAL inside.
- **E7-4 [PROVED, applied].** Endpoint values only; interior z-dependent, non-monotone, pointwise w_fib ∈ [−1.342, −1.169] (= PP −1.3421/−1.1687).
- **E7-5 [PROVED, applied].** E3 PROVED at ends / CONDITIONAL inside (min 3.0017|k_x|). G3 made wholly CONDITIONAL, with the "ratio > 1" step CONDITIONAL on X2. This is more conservative than PP's wording and correct (the X2 dependence exists at the end faces too).
- **E7-6 [PROVED, applied; one forward clause to amend].** NC1 restricted to r_b(μ) plus φ_j with F_j = 0; Lie-drag bullet REFUTED; twisted-φ to NC4. The clause "treated, and resolved, in … 1736 §B" was an unaudited forward claim; per §2 below it is right for **static x-independent** twisted-φ faces (B2), while x-dependent twisted-φ faces without a minimum stay OPEN (B5). Fix 11 below.
- **E7-7 [PROVED, applied].** Sharp criterion; −0.549 = ½ln(1/3) and −0.347 = ½ln(1/2) check; z ∈ ℤ for g = 2 (CONDITIONAL citation); min Q = 2.0000 on all four flows is in resolve_1736.log (reproduced). Reporting it in a new log, not in templates.log, is the correct additive route. |z| ≥ 4 OPEN.
- **E7-8 [PROVED, applied].**
- **E7-9 [PROVED, applied].** ★F₄ stated; [[6,4],[4,6]], det 20.
- **E7-10 [PROVED, applied; minor].** 4 s.f. values 1.257e4/1.225e4/1.281e4/1.294e4 → 1.627e4 match 12568.6/12252.1/12812.2/12942.4 → 16266.7; bias +1.86; UV end open; monotonicity range cited. Minor: flow faces have R/R₀ > 1, so N_req^IR is also only a limit; the interval is open at both ends unless the exact fixed-point face is counted (fix 12).
- **E7-11 [PROVED, applied].** L1 interpretation CONDITIONAL, algebra PROVED. ε = R_stack/(L₇/2) = (N_b/N_flux)^{1/3} follows from R_stack³ = πN_bℓ_P³ and L₇ = 2(πN_flux)^{1/3}ℓ_P. ε = O(1) concession and L4 CONDITIONAL are right.
- **E7-12 [PROVED].** PP's C3 retraction is recorded correctly.
- **E7-T [CONDITIONAL, on scoping].** Recount from 1711 + 1713 + PP fixes:
  - 1711: PROVED 11 (T0-end, E1, E3-end, E4-bound, A1, A2 |z|≤1, B1 value, B3, AB1, G1, (β)⇔λ′=0), CONDITIONAL 14, OPEN 5 (X1–X4, |z|≥4). Matches.
  - 1713: PROVED 9, CONDITIONAL 9 as listed, OPEN 4. **1713's own tally had D4 (scan.log) CONDITIONAL, and PP N27 graded it CONDITIONAL.** Erratum 7 drops it ("folded into erratum 5"). Including it: CONDITIONAL 10.
  - REFUTED 4: correct (E4 sub-claim, B1 printed sign, NL0 twisted-φ Lie-drag, tally row "8").
  - So 20/23/9/4 (56) is right under NL's scoping; strict recount 20/24/9/4 (57). Notes: X3 ≡ O1 and X4 ≡ b appear in both files (unique OPEN items: 7); "E3-int" and "k_x − K > 0 interior" are the same numerical fact counted twice.

## 2. File (2), 1736 §B: general faces, pure smeared M5, Z₂
- **B0a [PROVED].** With 2(K_ab − h_abK) = κ²σP^{wv}_ab on the 10D face (dim W = 6, dim W⊥ = 4): trace gives c = −3K/2, so K_ab = −(K/2)P^{wv} + K·P^{fib}, i.e. wv eigenvalue k_w = −K/2 = κ²σ/6 and fibre eigenvalue −2k_w. Pure algebra, any face, no symmetry. (W = span of the face lifts of t, x, and the horizontal Σ directions.)
- **B0b [PROVED].** For a Killing field ξ tangent to the face: K(ξ,ξ) = g(∇_ξn, ξ) = −g(n, ∇_ξξ), and Killing's equation gives g(∇_ξξ, V) = −½V(|ξ|²). So **K(ξ,ξ) = +½ n(|ξ|²)** in this convention; in the K = −∇n convention it is −½ n·∇|ξ|². The sign matches the PP lemma and k_a = ½n(ln c_a) (f3c5d73f N1), so B1 is consistent. (B1 is homogeneous, and B2 flips K⁽⁰⁾ and the Hessian term together, so neither depends on the convention.) NL's sympy check is only a 3D diagonal toy. PP checked it on an 8D model with Σ = H², a μ-dependent warp D^{1/3}, and two twisted circles, on a face depending on (x, σ, μ, twisted φ₂): residuals 0 and −3×10⁻¹⁷; also K(∂_t, e_a) = 0 and g(∂_{φ₁}, W-lifts) = 0, so ∂_{φ₁} ∈ W⊥ (pp_geom_checks.log (1)).
- **B0c [PROVED].** At a critical point of r on the face, K_ab = K⁽⁰⁾_ab − n_r ∂_a∂_b r_b, with Hess tensorial there. Sign checked by the flat example z = ½y² (K_yy = −n_z h″). PP's 8D check with a generic Hessian, including mixed and twisted-φ₁ entries: max residual 3×10⁻¹⁶ (pp_geom_checks.log (3)).
- **B0d-1 [PROVED given J1].** The resolve.py eq1/eq3/eq4 equal face.py's rhs_r exactly (3λ₁′+2λ₂′ = R₁, etc.). With λ_i′ = 2f′ and eq1, the f′ terms cancel and eq3 → −2e^{f+2λ₁} − (1+z)/8·e^{f−2g−2λ₁} ≠ 0 for z ≥ −1, and eq4 likewise for z ≤ 1. Pointwise, so 2f′ − λ_i′ ≠ 0 on the whole flow.
- **B0d-2 [PROVED given J1].** The sign is < 0: the flow tends to the IR fixed point where λ′ = 0 and f′ = −1 (gauge h = f), and the quantity never vanishes. Numerics agree (−1.89/−1.99/−1.85/−1.82).
- **B0d-3 [CONDITIONAL, numerical; PP addition].** For z = 2, 3 the eq4 residual (z − 1 − 16e^{2g+4λ₂}) can vanish in principle; the log's max (2f′−λ₂′)/|f′| = −2.0000 shows it does not along these flows. So the i = 2 route is available there only numerically.
- **B1 [PROVED given J1, every real z].** Static graph faces independent of μ and of φ_i (i = 1 if z ≥ −1, i = 2 if z ≤ 1), arbitrary in (x, σ, φ_j). ∂_t ∈ W and ∂_{φ_i} ∈ W⊥ are tangent Killing fields; c_{φ_i}c_x² = X_i⁻¹μ_i²e^{4f} (Δ̃ cancels; PP checked ∂_μ ln(c₁c_x²) = 2/μ exactly); n^μ = 0. So 0 = n^r(2f′ − λ_i′), contradicting B0d-1. Covers r_b(σ), r_b(x), r_b(σ, x), and twisted-φ_j faces for j ≠ i. For z ∉ [−1, 1] a face depending on φ₁ (the only allowed i) is not covered by B1.
- **B2 [PROVED given J1, every real z, under explicit premises].** Premises: the face is static, C², embedded, inside the flow region, and **compact in the internal directions** (x-independent); then r|_face attains a global minimum p. At p the tangent plane is a constant-r tangent plane, so the face is locally a graph with ∂r_b = 0, and B0a + B0c in directions (φ̂_i, x̂ or t̂) give n_r[Hess(φ̂,φ̂) + 2Hess(x̂,x̂)] = n^r(2f′ − λ_i′). The left side is n_r·(≥ 0) and the right side is n^r·(< 0); since n_r and n^r have the same sign, this is a contradiction whichever way n points. A graph is not needed. Pointwise at p is enough: the Israel conditions must hold at every point, and B0d-1 is pointwise in r.
  - **Missing step, supplied by PP [PROVED].** If p lies where the φ_i circle shrinks (μ_i = 0), φ̂_i is undefined. Use any unit vector e in the transverse 2-plane, which is in W⊥. There K⁽⁰⁾ is isotropic in that plane with eigenvalue ½n^r∂_r ln(Δ̃^{-2/3}X_i⁻¹), the limit of the φ_i value, so the same identity holds with Hess(e,e) ≥ 0. Checked on the real uplift (face.py): the gap |k_μ − k_φ|/|k_x| → 0 quadratically (3×10⁻⁷, 3×10⁻⁹, 3×10⁻¹¹ at distance 10⁻², 10⁻³, 10⁻⁴; all four candidates, both circles; pp_pole_check.log).
  - **Strengthening [PROVED].** For compact faces the sign in B0d-2 is not needed: a global maximum also exists, and the same identity gives a contradiction there if 2f′ − λ_i′ > 0. Also, B1/B2 use only the eigenvalue ratio −2, so they hold for either kept side and any sign of σ.
  - **Non-compact directions:** t (handled by staticity, Hess(t,t) = 0) and x¹–x³. An x-dependent face need not attain a minimum; that is B5.
  - Consequence: **PP f3c5d73f N5 (twisted-φ faces, OPEN) is now PROVED for static x-independent faces**, every z. The refuted Lie-drag is not used, and the 8D model confirms that the Lie-drag value is indeed off by 0.0127 on such a face (pp_geom_checks.log (2)), which B2 does not need.
- **B3 (|z| ≤ 1) [PROVED given J1]; B3 (z = 2, 3) [CONDITIONAL, Q > 0 numerics].** At a global maximum, n_r Hess(F̂,F̂) = K⁽⁰⁾(F̂,F̂) − K⁽⁰⁾(x̂,x̂) = n^r(g′ − f′) > 0 vs Hess ≤ 0. Remark: x^α-independence is not needed; staticity with ∂_t in place of x̂ suffices.
- **B4 [PROVED].** The B1/B2 contradictions do not involve k_w, N_b or G₄ (G1/N8). So no solution at 4880, N_req or 2N_flux, either parity.
- **B5 [OPEN].** Agreed. It can be narrowed: for |z| ≤ 1, faces attaining a global maximum are excluded by B3 (with t̂). What remains is static x-dependent faces with no attained minimum (and, for |z| ≤ 1, no attained maximum) that depend on μ, or on φ_i for every admissible i.
- **B6 [OPEN].** Agreed.

## 3. File (2), §C: radial-profile ODEs
- **C1 [PROVED, structure].** For a static one-variable profile, eliminating k_w leaves at least five independent conditions (wv isotropy K(x̂) = K(Σ̂); three equalities among the four fibre eigenvalues; the ratio −2), plus off-diagonals, for one unknown function. Overdetermined. Wording: k_w = κ²σ/6 is constant only if σ is uniform on the face; σ = N_bT_M5ρ(y) varies with μ in general. Overdetermination holds either way.
- **C2 [PROVED given J1; scoped].** 0 solutions for static, coordinate-aligned profiles: ξ = x^α or σ (B1), ξ = μ or φ_i (B2), every z, every N_b incl. 4880, both parities. This upgrades r_b(μ) at z = 2, 3 from CONDITIONAL (f3c5d73f N4) to PROVED.
- **C2-t [OPEN].** "Every one-variable profile" includes r_b(t), which is B6. Profiles in a rotated variable mixing x with compact coordinates, e.g. r_b(x¹ + cμ), fall under B2 if they attain a minimum and under B5 if not.
- **C3 [CONDITIONAL].** Agreed. **C4 [OPEN].** Agreed (= B5).

## 4. File (2), §D: localization
- **D1 [PROVED].** S_ab = 0 ⇒ K_ab − h_abK = 0 ⇒ (trace, dim 10) K = 0 ⇒ K_ab = 0.
- **D2-const [PROVED given J1, every real z; PP route].** On constant-r faces, k_{φ_i} + 2k_x = n^r(2f′ − λ_i′) ≠ 0 (B0d-1, i chosen by z), so k_{φ_i} and k_x are not both 0. NL's g′ − f′ route needs Q > 0, which is numerical for z = 2, 3; the B0d route removes the z split.
- **D2-general [REFUTED, counterexample].** "No face point is totally geodesic" is false for general static faces. Construction: at a point where ∂_μ c_t ≠ 0 (true wherever Δ̃ is non-constant, i.e. λ ≠ 0, so in the flow interior), choose the tilt ∂_μ r_b so that n(c_t) = 0. Then K(t,t) = 0, K(t, e_a) = 0 automatically (static), and with n_r ≠ 0 the spatial second derivatives of r_b can be chosen to cancel the spatial block. Realized in the 8D model: tilt −16.62, max|K_ab| = 1.4×10⁻¹⁴ at the point (pp_geom_checks.log (4)).
- **D2-region-B1 [PROVED given J1].** No open region of a static face in the B1 class is totally geodesic (B1 identity with K = 0).
- **D2-region-general [OPEN].** Whether an open region of a general static face (as D1 needs) can be totally geodesic is not settled. Partial (PP): for a static x-independent face that is totally geodesic off the stack locus Σ × {y₀}, the global minimum of r must lie on that locus, by the B2 argument; for |z| ≤ 1 so must the global maximum, by B3.
- **D2-O(1) [CONDITIONAL].** "A localized pure-M5 Z₂ face needs an O(1) change of the geometry everywhere" is heuristic. It is supported by D2-const and the partial result, not proved. ε = 2^{1/3} = 1.26 is arithmetic-correct.
- **D3 [CONDITIONAL].** Agreed. 12.25k–16.27k / 4880 = 2.51–3.33 and /(2·4880) = 1.255–1.667 check.
- **D4 [OPEN].** Agreed. Wording: "a perturbative bound cannot exist" is not proved; say "no perturbative bound is available".

## 5. File (2) tally
- **T-1 [REFUTED as printed].** The header row "PROVED | 17" lists 17 names but omits D2 (|z| ≤ 1), which NL's own split note counts.
- **T-2 [PROVED, bookkeeping].** Recount: A 6/1/1/1 = 9, B 8/1/2/0 = 11, C 2/1/1/0 = 4, D 2/2/1/0 = 5, O1 lock 1 OPEN; total 18/5/6/1 = 30. PP's regrading above supersedes it for §B–§D.

## NL fixes (additive erratum only; none reverses a no-go)
1. 1736 tally header: PROVED 17 → **18** (18/5/6/1, 30).
2. B0b: state the convention (K_ab = ∇_a n_b ⇒ +½ n(|ξ|²); −½ in the opposite convention) and give the two-line Killing proof. The sympy toy is a 3D diagonal check only; cite PP's 8D twisted check.
3. B0d: state that the sign < 0 comes from the IR fixed point (λ′ = 0, f′ = −1) plus continuity. Note that the i = 2 route for z > 1 (and i = 1 for z < −1) is only numerically nonvanishing (CONDITIONAL).
4. B2: list the premises (static, C², embedded, inside the flow region, compact in the internal directions); a graph is not needed. Add the shrinking-circle step (transverse 2-plane vector; PP pole check). Note that for compact faces the sign of 2f′ − λ′ is not needed (minimum or maximum), and that B1/B2 hold for either kept side and any tension sign. Replace "every x-independent face" with "every static C² x-independent face in the flow region".
5. B3: replace "independent of one x^α" with "static" (use ∂_t; Hess(t,t) = 0).
6. B5: narrow the open class. For |z| ≤ 1, faces with a global maximum are excluded by B3; what remains is static x-dependent faces with no attained minimum (and, for |z| ≤ 1, no attained maximum).
7. C1: k_w = κ²σ/6 is constant only for uniform σ; state the count of independent conditions (≥ 5 vs 1 function).
8. C2: restrict to static, coordinate-aligned profiles. r_b(t) belongs to B6 (OPEN). Rotated profiles mixing x with compact coordinates go to B2/B5. Note that C2 upgrades r_b(μ) at z = 2, 3 to PROVED.
9. D2: withdraw "no face point is totally geodesic" for general faces (PP counterexample). Restrict to constant-r faces and prove it via k_{φ_i} + 2k_x = n^r(2f′ − λ_i′) ≠ 0, which holds for all z and removes the z split. State that the region version is PROVED for the B1 class and OPEN in general. Label "O(1) change everywhere" CONDITIONAL.
10. D4: "a perturbative bound cannot exist" → "no perturbative bound is available".
11. Erratum 7 fix 6: replace "treated, and resolved, in 1736 §B" with "static x-independent twisted-φ faces: no solution, by 1736 B2 (PP audit of this file); x-dependent ones without an attained minimum stay in B5 (OPEN)".
12. Erratum 7 fix 10: N_req^IR is also only a limit for flow faces (R/R₀ > 1), so the interval is open at both ends unless the exact fixed-point face is counted.
13. Erratum 7 tally: disclose that a strict recount including 1713 D4 gives 20/24/9/4 (57); that O1 ≡ X3 and b ≡ X4 appear in both files (7 unique OPEN items); and that E3-int and "k_x − K > 0 interior" are one fact counted twice.

Tip 7cddb188 untouched (MATCH). No CERT. No message sent. Nothing adopted. §A (O1) of 1736 not audited here.
