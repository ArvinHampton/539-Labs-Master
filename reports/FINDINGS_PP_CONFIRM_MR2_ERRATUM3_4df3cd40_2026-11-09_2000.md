# FINDINGS — PP confirmation of MR2 ERRATUM3 (4df3cd40), covering the gate fixes per PP 205dbc3f, the wall fixes per PP 011d1842, and the batch-1 follow-ups
Auditor: PP (Professor Proof), Soft SF audit agent. Written 20:00 CST (America/Chicago).
- Method: pure math only. Labels are PROVED / CONDITIONAL / OPEN / REFUTED / PENDING, and refutation is only by proof or counterexample.
- Rules: this is an additive new file; no existing file was edited. No CERT. Nothing was sent and no agent was messaged. No Gemini. Nothing was adopted.
- Naming: "resonant algebra" (OW 81b74a31); no affected names appear below.
- Tip: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md has sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 at the start and at write time. It is unchanged.

## 1. Sidecars and provenance
| file | sha256 (recomputed) | sidecar | mtime CST |
|---|---|---|---|
| MR2_ERRATUM3_GATE_AND_WALL_PER_PP_205dbc3f_011d1842_2026-11-09.md | 4df3cd40c190cb0b8beb078fb0de7acf1757166f5898cb26dd6814342fe89d4b | MATCH | 19:57:43 |
| …ERRATUM3….py | 511d7d7a10f37e4337e1655f6e861b1eb461bf6f5bd1143956b441e3271bc34b | MATCH | 19:56:24 |
| …ERRATUM3….log | 7e38f85b5c05398ac704e65e65ecf672873696b7654d9b050d75eef810ac07d8 | MATCH | 19:56:57 |
| MR2_TWISTED_VACUA_EINSTEIN_SYMBOLIC_AND_GLOBAL_CURVATURE_2026-11-09_MN2_SYMBOLIC_REDUCED_TIMEOUT_SCRATCHLOG.log | 0c2f7448104e291f8233ca42e62e0c3628360a999803ad94e9e7a6b402864c66 | MATCH | 19:07:29 (its sidecar is dated 19:56:24) |

- **Frozen before run: confirmed.** The .py sidecar is dated 19:56:24 and the log 19:56:57. The 20 s runtime fits that gap.
- **Scratch log copy: confirmed.** It is byte-identical (same sha) to /workspace/scratch/mr2_1750/symred_MN2.log (mtime 19:07:29).
  - Its content: the field is set up as QQ(X1, s_a, s_b) with minpoly 8X₁⁵ − 1, and then `exit_code=124`. It never prints a "FULL SYMBOLIC ZERO" line.
  - The sidecar was written afterwards, at 19:56. That is fine for a disclosed verbatim copy.
- **Rerun on a copy: identical.** I ran /workspace/pp_e3_2000/e3.py (sha 511d7d7a…, the same file). It exited 0 in 20 s. Its output e3_rerun.log (9ef0460c…, which includes my appended EXIT line) is **byte-identical** to MR2's log once the EXIT line is removed. The script's own sha assert on V2 (ad134752…) passed.

## 2. Gate fixes (PP 205dbc3f)
| # | check | verdict |
|---|---|---|
| G1 | Seed disclosed, no Schwartz–Zippel used | **FAITHFUL.** `random.seed(20261109)` is at line 263 of MR2_TWISTED_VACUA_EINSTEIN_SYMBOLIC_AND_GLOBAL_CURVATURE_2026-11-09.py. ERRATUM3 explicitly does not invoke Schwartz–Zippel. |
| G2 | "All points" CONDITIONAL; full symbolic OPEN; no degree bound | **FAITHFUL.** The PENDING MN2 symbolic run → OPEN (timeout, not a failure). This matches the scratch log. The degree-bound route is honestly left undone. |
| G3 | KK m²L₅² = 46.16 | **FAITHFUL.** 2 × 23.0785584813816 = 46.15711696…, which rounds to 46.16. F₀/G₀ = 2 is PROVED. The eigenvalue and the "no invariant vector at λ₁" claim are CONDITIONAL, which agrees with PP. |
| G4 | Bolza: systole vs λ₁ | **FAITHFUL; see the ruling in §5.** |
| G5 | Two-root branch | **FAITHFUL.** I re-checked with sympy. 16X¹⁰ − 1228X⁵ + 81 is irreducible over ℚ, with positive real roots 0.580674 and 2.38200. 3X¹⁰ − 122X⁵ + 6 is irreducible, with positive real roots 0.547600 and 2.09770. 8X⁵ − 1 is irreducible, with root 0.659754. Divisibility by an irreducible minpoly covers every conjugate. PROVED. |
| G6 | dps rule stated as a heuristic | **FAITHFUL.** It is labelled CONDITIONAL, and dps-doubling confirmation is required. |

## 3. Wall fixes (PP 011d1842)
| # | check | verdict |
|---|---|---|
| W1 | Baseline reversed; factors 1.019542 (W=4) and 2.242760 (W=10) | **FAITHFUL; numbers VERIFIED** (details below). |
| W2 | "Double degeneracy" REFUTED; the artefact tracks the distance to β = π/2 | **FAITHFUL.** POLE log 508ac55a line 7, at (α, β) = (0.001, 1.5707963): 2.22145870606767e+27 at dps 40 and 511.80792853607 at dps 60, against 511.807928712851 at dps 90 and 120. The difference is 1.77e-7. Far from the α-pole, the failure follows β alone. |
| W3 | L ≅ K dropped | **FAITHFUL.** deg L = a₁·Area/2π = 4π(g−1)/2π = 2 at g=2, so w₂ = 0 and the S³ bundle is trivial with no assumption. PROVED; this agrees with my own derivation in 011d1842. |
| W4 | Artefact text reworded | **FAITHFUL.** The text attributes the loss to cos β cancellation near β → π/2 and labels the rule a heuristic. |
| W5 | Fixed-φ convergence from 48×32 to 96×64 | **FAITHFUL** (reproduced). Horizontal ⟨(wF₀)²⟩ = 0.3341509085714847 and fixed-φ = 0.3396992600857756, identical at 48×32 and 96×64. 24×16 differs by about 3e-12 and 4e-13 relative. N_req/2N = 1.2876110196153 and 1.0315626941613. The label "PROVED (numeric limit)" is consistent with PP's usage in 205dbc3f §4. The measure choice stays CONDITIONAL. |
| W6 | Supremum skipped | **FAITHFUL.** sup Riem² = 3408 stays CONDITIONAL. |

**W1 details.**
- My independent float64 check uses numpy leggauss(48): ∫_{−U}^{U} du/(1−u²) with U = tanh W, divided by 2W.
- W=4: 0.98083254066, so exact/quadrature = **1.0195420304**.
- W=10: 0.44587923272, so exact/quadrature = **2.2427597578**.
- MR2's dps-40 values are 1.01954203041 and 2.24275975781. These agree.
- They confirm PP 011d1842's 1.0195 and 2.243. The exact baseline is linear in W by the ρ-isometry (PROVED). The true W=10 : W=4 ratio is 2.5. KINK − NO_SOURCE is unaffected.

## 4. Batch-1 follow-ups
- **Row #17: FAITHFUL.** ERRATUM3 §C restates row #17 as "thin limit kε → 0 valid: PROVED as an implication given existence; existence of the (2c) profile is OPEN". The OPEN premise stays visible.
- **Line-8 wording: FAITHFUL.** The superseded line is line 8 of MR2_ERRATUM_BATCH1_CANDIDATES_PER_PP_dee9410e_2026-11-09.md (sha b964cad18db9…). It reads "Grading convention (PP's): a row reading 'PROVED with a CONDITIONAL premise' counts as CONDITIONAL…".
  - ERRATUM3 replaces it with PP's ruling: a claim that states its premise is graded as an implication, and the strict rule applies only to premises that are used but not stated.
  - The alternative 14/12/8/5 is withdrawn, and the batch-1 tally stays 17/9/8/5 (39).
  - This also agrees with the R1 convention PP recommended in FINDINGS_PP_CONFIRM_MR2_ERRATUM_69a10b84_2026-11-09_1932.md (F8).
  - The b964cad1 file itself is not edited, which is correct under the additive rule.
- **985d404d provenance.**
  - 985d404d **is on disk**: it is FINDINGS_PP_CONFIRM_MR2_ERRATUM_69a10b84_2026-11-09_1932.md (sha 985d404d4135…a11d, sidecar MATCH, 19:32:39).
  - It does not and cannot reference b964cad1, which was written later at 19:50:34. That is expected, since the row-#17 and line-8 ruling was sent by message.
  - MR2's citation of the message is fine. Its phrase "not located on disk by MR2" is slightly inaccurate, because the 985d404d file exists; it just does not carry these follow-ups (residual fix R1).

## 5. PP RULING on fix 4 (supersedes 205dbc3f fix 4)
- 205dbc3f fix 4 ("Bolza value → PROVED") referred to the **systole** (205dbc3f §4 line 107 and fix-list item 4). MR2 read it correctly, and **PP accepts MR2's split**:
  - **Bolza systole 2 arccosh(1+√2) = 3.0571418390: PROVED.** The proofs are PP 384096a8 (computer-assisted) and MR2's independent enumeration of 15241 elements with min |tr| = 2+2√2.
  - **Bolza λ₁ ≈ 3.8388872588: CONDITIONAL.** It becomes PROVED only if PP itself verifies a certified **two-sided** enclosure. A citation alone never makes a result PROVED (OW 36683379). FEM and KMP give only upper bounds; KMP's genus-2 bound is λ₁ < 3.8388976481. Strohmaier–Uski's ~1e-6 error bar is reported from their own implementation and has not been re-derived or rerun in-repo.
  - "KMP bound > S–U value" stays PROVED as arithmetic (difference 1.04e-5).
- This ruling supersedes 205dbc3f fix 4 as stated. It changes no tally, because the gate tally already counts λ₁ as CONDITIONAL.

## 6. Optional λ₁ lower bound: not attempted (not quick)
- **Temple / Lehmann–Goerisch route.** This needs a trial function u on Bolza with a rigorously bounded residual ‖Δu + λ̃u‖. It also needs a rigorous lower bound on λ₂ (≈ 5.3536), not a quoted value, and a certified separation of the triple λ₁ eigenspace (multiplicity 3, so the bound must be applied on a 3-dimensional trial space). Building and certifying those pieces with interval arithmetic would take hours.
- **Strohmaier–Uski enclosure route.** Their method of particular solutions with an a posteriori bound requires reimplementing the boundary-residual estimate on the octagon fundamental domain with controlled rounding. That is also not ≤ 20 minutes.
- So λ₁ is left **CONDITIONAL**, as stated.
- A path to PROVED: run an MPS implementation under interval or ball arithmetic (Arb), with a Moler–Payne-type residual bound for λ₁, plus a Lehmann–Goerisch lower bound for λ₂. About 3–5 h.

## 7. Tallies (re-counted)
- **Gate (205dbc3f updated): 16 / 5 / 4 / 0 (25). CONFIRMED.** The only change is the MN2 symbolic run, PENDING → OPEN on the timeout log. PENDING is now 0.
- **Wall (011d1842): 17 / 5 / 4 / 2 (28). CONFIRMED** as filed. The two REFUTED items are MR2's baseline attribution and the double-degeneracy qualifier.
- **ERRATUM3's own claims: 8 / 4 / 2 / 2 (16). CONFIRMED.** I checked every item against §§2–3.
  - P: baseline linear in W; u-rule factors; deg L = 2 / w₂ = 0; ⟨(wF₀)²⟩ convergence; systole; two-root branch / all-conjugate test; F₀/G₀ = 2; seed disclosure.
  - C: Einstein at all points; λ₁; 23.0786 → 46.16; dps heuristic.
  - O: full symbolic zero; degree-bound certificate.
  - R: MR2's baseline attribution; double degeneracy.
  - Arithmetic: 8 + 4 + 2 + 2 = 16.
- Carried statuses: junction UNSOLVED; KK spectrum OPEN; sup 3408 CONDITIONAL; MN N=2 CONDITIONAL.

## 8. Verdict
- **All gate fixes G1–G6, wall fixes W1–W6 and both batch-1 follow-ups are faithfully applied.**
- The rerun is byte-identical. The numbers 1.019542 and 2.242760 are independently verified. Nothing is refuted.
- The fix-4 dispute is resolved by the PP ruling in §5: the systole is PROVED and λ₁ stays CONDITIONAL.

## 9. Residual fixes for MR2 (cosmetic, no grade impact)
1. **R1.** In a future note, change "985d404d … not located on disk" to "985d404d (FINDINGS_PP_CONFIRM_MR2_ERRATUM_69a10b84_2026-11-09_1932.md) is on disk but predates b964cad1. The row-#17 and line-8 ruling came by message."
2. **R2.** Cite this file's §5 as the authority for the λ₁ CONDITIONAL / systole PROVED split, superseding 205dbc3f fix 4.

Scratch: /workspace/pp_e3_2000 (e3.py 511d7d7a…, e3_rerun.log 9ef0460c…).
