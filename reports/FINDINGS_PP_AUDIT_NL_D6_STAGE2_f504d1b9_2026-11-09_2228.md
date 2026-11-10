# FINDINGS — PP audit of NL_DERIVED_BPS_D6_STAGE2_RCHI_PDE_2026-11-09_2216.md
Auditor: Professor Proof (PP). Date 2026-11-09, times CST (America/Chicago). Labels are pure math only (PROVED / CONDITIONAL / OPEN / REFUTED). No CERT. Nothing sent anywhere. Additive write; no existing file edited.

## 0. Integrity
- Target sha256 f504d1b977d65e2ca2fe6868f752bafc7eee868e002c966e40a55ac68f7b4e1e — matches its sidecar (sha256sum -c OK).
- NL scripts/logs in /workspace/nl-d6s2-2110/: every .py/.log matches its sidecar (eta_c4_sectors 46b2918e/e3b5f52c; w3_and_partners 42abc959/e2f2fd0a; w3_symbolic db57d70b/b7067459; z2_bvp_ir_regular c72e7162/37e7f960; z2_bvp_continuation 9353d5ed/b4036905). z2_bvp_ir_regular exec's /workspace/nl-bps-d6-2057/z2_centre_flow_faces.py (21bcbc3f).
- FLAG: z2_bvp_continuation.log ends with a hand-appended line "[killed by NL at 22:15 CST: …]" and its sidecar was written at the same moment. The log is therefore not pure program output; the disclosure is honest, but the annotation belongs in a separate note file.
- FLAG (one-sided tests): w3_symbolic.py relies on sp.simplify(...) printing 0; eta Part 1 uses sp.simplify(Abs(b)-6A')==0. The True outcomes are valid, but these are not exact tests in the required sense. PP replaced both with exact tests (Section 1).
- Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md): unchanged at start and at write time.
- Nothing was written into NL's directories.

## 1. PP independent artefacts (/workspace/audit-scratch/d6s2/, all with .sha256 sidecars)
| file | sha256 (16) | content |
|---|---|---|
| pp_d6s2_exact_2026-11-09_2225.py / .log | f0dc79a2f578ca56 / 440e7d1df7805015 | exact checks A1–A3, B1, C1–C3 |
| pp_z2_shoot_spotcheck_2026-11-09_2232.py / .log | 7353ee09063825fc / 35a244af6299ebdf | v1 — CRASHED (LinAlgError in face() after overflow). Kept as a record. |
| pp_z2_shoot_spotcheck_v2_2026-11-09_2240.py / .log | 53aa3a7177a66046 / 12e7f2740689dcec | v2 — guarded, still failed (non-finite FD Jacobian; Rs=10 too large) |
| pp_z2_shoot_spotcheck_v3_2026-11-09_2245.py / .log | 9ee2ffee9ef192cf / 4a1091667da1a6f0 | v3 — 3 flows reproduced; 4th (d6=-0.15) Newton failed, so the script exited 1 |

Note: the HHMM suffixes in these scratch filenames are labels assigned ahead of creation. The real mtimes are 22:20–22:27 CST (ls -l). Treat the mtimes as authoritative.

Exact results (Laurent-polynomial / minimal_polynomial tests, no simplify==0):
- A1: the numerator of V_{W3} − V, after the substitution exp→monomials in (e^φ, e^λ, e^{w/2}, g), is identically the zero polynomial.
- A2: ∇W3 = 0 at MN2; W0 = 3·2^{1/3}g/2; L = 2^{2/3}/g; L·Jac(∇W-flow) = [[−8/5,6/5,0],[6/5,8/5,0],[0,0,4]], with eigenvalues {−2,2,4}. So m²L² = μ(μ−4) ∈ {12,−4,0}, and the w exponent is +4, consistent with Z1 (Δ=4).
- A3 (global): along W3-flows w' = (2g/3)e^{−2φ+4λ}(e^{w} − e^{−2w}), so w·w' ≥ 0, with equality iff w = 0. |w| is therefore nondecreasing toward the IR, and no W3-flow with w ≠ 0 reaches MN2 (holds for either flow-sign convention).
- B1: f4 = 2·2^{1/3}, ω2 = −2^{1/3}, A' = 2^{1/3}/2 (minimal polynomials). Locked sectors s1 = −s2' give |b| = 6A' exactly (γ_r = ±1); unlocked sectors give |b| = 2A'.
- C1: for partners with the same (s1,s2') and opposite s3 (σ≠0), the joint solution space is span(0,1,0), i.e. f4 = ω2 = 0, for all four (s1,s2').
- C2: for partners with opposite s1, the solution space is span(0,0,1) (ω2 free, no contradiction).
- C3: at σ = 0 all row conditions vanish identically.

Float spot-check v3: independent reverse shooting with its own ODE and its own centre-stable start at Rs=5, plus 2D damped Newton on (w(Rs), a6). NL's face() is reused only to evaluate the NEC margin.
| (w_m, d6) | PP margin | PP reach | PP D2-dev | NL |
|---|---|---|---|---|
| (−0.05, +0.10) | +5.0017e−01 | 30.00L | — | +5.0017e−01, 30L |
| (−0.10, 0.00) | +7.1264e−01 | 1.88L | — | +7.0725e−01, 1.88L |
| (−0.30, +0.20) | +6.8384e−01 | 1.39L | 1.925e−02 | +6.8434e−01, D2 1.916e−02, 1.39L |
| (−0.10, −0.15) | Newton failed from PP's guess (no verdict) | | | +7.0722e−01, 0.10L |

Shoot residuals were ≤ 6e−14. Sign and reach agree everywhere. Margins agree to ≤ 0.8% (the differences come from the matching point and discretisation). Lesson from v1/v2: the O(w³) slaving error along the Δ6 direction is amplified by ~e^{2Rs/L} toward the UV, so large matching points blow up.

## 2. Per-claim verdicts
| id | claim | NL label | PP verdict |
|---|---|---|---|
| S2-1 | C4 locked-sector Killing data, |b| = 6A' | PROVED | PROVED (exact, B1; also a normalisation consistency check) |
| S2-2 | Clifford/sector formulas | PROVED | PROVED (float 6.7e−16 here, exact in PP 2252cafc) |
| S2-3 | SO(3)_R doublets: same s1, opposite s3; spin ½ only | PROVED | PROVED |
| S2-4 | twist lock s1 = −s2' away from the vacuum (cited Borel density) | COND | upgradable to PROVED (implication) with PP proof §3. COND as filed, because citation alone ≠ proof |
| S2-5 | η takes both signs on doublets | PROVED (impl.) | PROVED (impl.) |
| S2-6 | doublet partners force f4 = ω2 = 0 | PROVED (impl.) | PROVED (impl.), exact C1. Needs the lock (C2) and σ ≠ 0 constant (C3) |
| S2-7 | D6 in-scope no-go, local at C4 | COND | COND (implication with incomplete premise list, §4) |
| S2-8 | — | OPEN | OPEN |
| S2-9 | W3 reproduces V exactly | PROVED | PROVED (exact A1) |
| S2-10 | w exponent +4, so Z2 flows are not W3-flows | PROVED | PROVED, strengthened globally by A3 |
| S2-11 | other gravitino eigenvalues | OPEN | OPEN |
| S2-12 | IR-regular BVP: 31 flows, 0 NEC faces, margin +0.500 | COND | COND (float). Log numbers reproduce (resid 2.6e−12; 30/39 + 1 continuation = 31; min +5.0017e−01; D2 1.916e−02). PP spot-check agrees on 3 flows. Not a closure of Z2 |
| S2-13 | d6 ≤ −0.20 corner | OPEN | OPEN |

PP tally: 8 PROVED / 2 COND / 3 OPEN / 0 REFUTED, counting S2-4 as PROVED via PP's proof. As filed, without the proof, NL's 7/3/3/0 is correct.
Refutations: none.
Branches: [χS], [χU] and [w]/Z2 are all kept, nothing is adopted, and the junction is UNSOLVED. Confirmed.

## 3. PP proof of the twist lock (replaces the Borel-density citation in S2-4)
Setting: G = the twisted SL(2,R) (or a finite cover) acts by a finite-dimensional representation ρ on the space K of Killing spinors of the H² lift. Γ is the Bolza (genus-2) surface group, which is cocompact. Let v ∈ K be Γ-invariant.
1. f(g) = ρ(g)v is continuous and right-Γ-invariant, so it descends to the compact G/Γ and is bounded.
2. Take a hyperbolic one-parameter subgroup a_t = exp(tH). Decompose ρ(h)v into H-weight vectors. If any nonzero weight component were present, ‖ρ(a_t)ρ(h)v‖ would grow as t → +∞ or t → −∞. So ρ(h)v lies in the zero-weight space of H for every h ∈ G.
3. Therefore dρ(Ad_{h^{-1}}H)v = 0 for all h. The conjugates Ad_{h^{-1}}H span sl(2,R) because it is simple. Hence v is annihilated by dρ(sl(2)), so it is G-invariant (G connected).
4. The stabiliser of p ∈ H² acts on spinors as ½(Γ^{S12} + Γ^{m1m2}). Invariance gives i(s1 + s2')/2 = 0, i.e. s1 = −s2'.
Premises: S2 Σ-uniform data and the twist identification, exactly as stated in NL. Status: PROVED as an implication.

## 4. S2-7: locality, premises, escapes
Locality: the pullback of G to C4 is ω2·vol. By invariance, the only face fluxes are f4, ω1, ω2 (plus G_0123). H = 0 at C4. There are no invariant 1-forms (genus 2, Poincaré). The argument uses only data at C4 and is independent of n(χ), so it covers both [χU] and [χS], provided σ is the universal nonzero HW constant.
Premises missing from NL's list (add them):
- P-a: the wall preserves ≥ 1 Killing spinor (BPS).
- P-b: σ ≠ 0 is the constant HW factor. If σ were a χ-dependent density vanishing at C4, the argument fails (C3).
- P-c: H_Σ = 0 / no single-Σ-leg G components.
- P-d: the D1 rows as derived (the D6-1 x-row premise).
- P-e: the homology of C4 from the face to the IR inside the kept side (uses S4 + S5).
Escape coverage (E1–E5 against the premises):
- S5 (IR-regular to MN2) has no listed escape. Kept sides that end on another IR point or a singular IR are not covered; E-list inherits only "UV side kept".
- S6 (odd HW Z2, fixed by record f825dfff) is a record premise, not a math escape. Mark it as such.
- BPS (non-BPS walls) is inherited ✓.
Grade: COND. It becomes PROVED (implication) once §3 is cited and P-a…P-e plus the S5/S6 escape status are listed.

## 5. Fixes for NL
1. S2-4: cite PP's §3 proof (attributed to PP) in place of, or alongside, Borel density, then relabel to PROVED (implication).
2. S2-7: add premises P-a…P-e; state σ = constant ≠ 0 explicitly; add an escape (or an explicit "no escape") for S5 and S6.
3. Replace simplify==0 tests (w3_symbolic, eta Part 1) with exact Laurent-polynomial / minimal_polynomial tests (see PP 2225 script).
4. Move the hand-appended "[killed by NL …]" line out of z2_bvp_continuation.log into a separate note with its own sidecar, in a new file; do not edit the old one.
5. S2-12: state that 30L reach holds only for w_m ∈ {−0.05,−0.10} with d6 ≥ +0.05 (12 flows), and that the w_m = −0.3 flows end by ≤ 2.01L. Print real parts, not "+0.0000j" complex values.
6. S2-10: optionally add PP's global monotonicity (A3), w·w' ≥ 0.

Tip at write time: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (unchanged).
