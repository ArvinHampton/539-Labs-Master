# NL ERRATUM 23 — accepting PP e9ac8a37 (confirmation of Erratum 22) and PP f530cbc0 (audit of D6 stage 2, 2216)
2026-11-09, 2241 CST (America/Chicago). **NL derived proposal.** Additive only: no target file, log, or prior script is edited (including `z2_bvp_continuation.log`). Authority: OW t4426 d5eaeef3 ("Pursue all open"); OW t4436 32881263 ("Let the math lead"; [χS], [χU] and [w] are kept as labelled branches unless a PROVED or REFUTED result drops one); the 90% usage stop is lifted per OW t4431 (record f700141d…). Nothing adopted. **Junction: UNSOLVED. Count gap: unchanged.**
Sources (sidecars OK):
- FINDINGS_PP_CONFIRM_NL_ERRATUM22_72a7f5b7_2026-11-09_2218.md (e9ac8a37b7914838d7423c393a105ccb5a7cb544c78b7485d9b77dca9e0272a8)
- FINDINGS_PP_AUDIT_NL_D6_STAGE2_f504d1b9_2026-11-09_2228.md (f530cbc00b253d50588165857d3ce4e2a19185c121b6ba5167ced8c6d8bcf9f8)

Targets (sidecars OK; none edited):
- NL_ERRATUM22_ACCEPT_PP_e2f5f582_aad209d2_2026-11-09_2211.md (72a7f5b77e642c2a54c5635631b9d8b0ea2ff1ac8974ad199ff6afb6909ca7b4)
- NL_DERIVED_BPS_D6_STAGE2_RCHI_PDE_2026-11-09_2216.md (f504d1b977d65e2ca2fe6868f752bafc7eee868e002c966e40a55ac68f7b4e1e)

Scripts, new dated directory `/workspace/nl-e23-2233/`. Each `.py` sidecar was frozen before its run; each `.log` sidecar was written after the run (disclosed). The 2203 and 2110 originals are not edited.
- e22_checks_exact_tests_2026-11-09_2233.py = 5428c77e225593270e4f215f8aa7e0bb11b3e843c4d3200b4b04f5ab4276a149, log 1ab9e2299fc67583915754065931f72add5adae40ce3ce32275e594060e1dda6
- e23_w3_symbolic_exact_2026-11-09_2233.py = 5108b775c59ab573f7c168446a3d3a0995de73d839f99fad699687f19d7c3000, log 07e1e9d3df55763e072daf53b47ef473c9b1e57c5159e69a7032b413af41c3a4
- e23_eta_part1_exact_2026-11-09_2233.py = bbd18221f1a9a62d62aaea150f03e4ef3410d1b2e956b2bc175c249f74265cf6, log c205872b6d68be7cf607fc8e05fe6689143e0cfd724874c1d40244ea5e5bb81b (first attempt; wrong ω₂ conversion; left unchanged)
- e23_eta_part1_exact_2026-11-09_2239.py = f9a5e1586324106e7cb6e3fe353481b64c01ee0ff0f06f79629ad4a83e56ddf5, log 43bda5858e90ff5cda01a650cabc3b564c3cff40cd76b0b5defddd5afef2ae13 (corrected CGR (2.6) frame conversion)
- e23_z2_real_print_2026-11-09_2233.py = 40800a3e86ca933355019b187d7956342027205a0e02870ee575373c72886820, log 237cd6a41e45cd347ea12f5f8d80397301ffb052189f071fc51e9575e03e59ac
- NOTE_z2_bvp_continuation_log_hand_annotation_2026-11-09_2233.md = 77ab006c86fde47d020d95ac31b579c4ce04948b5b1601e67eb2406afa10a9e6

Cited, not copied: PP `/workspace/audit-scratch/d6s2/pp_d6s2_exact_2026-11-09_2225.py` = f0dc79a2f578ca56…, log 440e7d1d…. The 2110 originals (eta 46b2918e…, w3_symbolic db57d70b…, z2_bvp_ir_regular c72e7162… / log 37e7f960…, z2_bvp_continuation 9353d5ed… / log b4036905…) and the 2203 e22_checks (1f2ef5ada08f098e…) are not edited.
Limits: no CERT, no Gemini, nothing sent, no agent messaged. Naming per OW f1d167d1: where the algebra is named it is "resonant algebra" (it is not named in this file). Tip 7cddb188… checked before and after. PP's math was re-checked independently; no item was disagreed with.

**Tally: PROVED 2 · CONDITIONAL 0 · OPEN 0 · REFUTED 0 · total 2**
(E22-α, E22-β, E22-γ, E22-δ, the hand-typed-log note, the exact-test replacements, the |b| record, and the S2-7 / S2-12 wording are hygiene and carry no label. Revised tallies of the target files are in §6 and are not re-counted as extra rows here. E23-1 is the S2-4 grade change already counted in the revised 2216 tally; E23-2 is additional exact content of the existing S2-10 PROVED row, not a new D6 S2 row.)

## 1. Erratum 22 bookkeeping (PP e9ac8a37): FAITHFUL, with E22-α, E22-β, E22-γ, E22-δ
Hygiene (no label). Erratum 22 remains FAITHFUL. Four bookkeeping fixes, no grade changes of E22-1…E22-4:
- **E22-α.** E22-1 through E22-4 are **PP's e2f5f582 results, independently re-derived by NL**. The E22 headings that said only "independently re-derived" are corrected to that attribution.
- **E22-β.** Each of the four E22 rows restates a result already graded in a target tally that E22 §6 itself revises (E22-1 = R1b; E22-2 = R5; E22-3 = J7b-PP; E22-4 = the exact basis of Q8-conf). The 2/0/0/2 figure is accepted as that erratum's row count. **For any roll-up, its distinct new claims are 0/0/0/0.**
- **E22-γ.** The three `simplify(...)==0` tests in e22_checks_2026-11-09_2203.py (former lines 185, 203, 210) are replaced, in a **new** script e22_checks_exact_tests_2026-11-09_2233.py, by minimal-polynomial or rational/log tests. The 2203 original is not edited. Independently:
  - minpoly(W_{χφχφ}(MN2 IR, χ=π/4) − 2^{3/5}/18) = X;
  - minpoly(e^{−s₀}) = 9X³−256, and minpoly(e^{−s₀}/(256/9)^{1/3}) = X−1, with e^{−s₀} = 4·2^{2/3}·3^{1/3}/3;
  - 36(sol[0]−bound) = 0·ln2 + 0·ln3, leftover 0, and exp(36(sol[0]−bound)) = 1.
- **E22-δ.** Along the wall curve with the correct sign B = C − ½ln6, write δ = C−C₀ and A′(δ) = (√6/3)e^{−4δ}. Then
  d²(δ) = (A′+1)² + 5A′² + (δ−ln2)² + δ²,
  and the exact second derivative is **d²''(δ) = 4(96 A′² + 8 A′ + 1)**. The quadratic 96z²+8z+1 has discriminant −320 < 0, so d²'' > 0 on all of ℝ and d² is **strictly convex**. The critical point is therefore the unique global minimizer. PP's 50-digit evaluation 1.244305691631… at δ*≈0.581915… is the numeric value of that unique min; the 4001-point grid of e22_checks gives 1.2443057045 at C−C₀ = 0.5820, consistent at grid resolution. **R6 stays CONDITIONAL** (the analytic bound |Y−FP|≥1 uses only A′>0 and is unaffected; the numeric minimum remains a float evaluation).

## 2. D6 stage 2 (2216 / f504d1b9): PP f530cbc0, revised tally 8/2/3/0
PP's tally is 8 PROVED / 2 CONDITIONAL / 3 OPEN / 0 REFUTED; nothing was refuted. As filed, without the twist-lock proof, NL's 7/3/3/0 was correct. This erratum upgrades S2-4 and records the remaining fixes. The as-filed 2216 file is not edited.

- **E23-1 (PROVED, as an implication; S2-4 twist lock; credit PP §3).** In any Σ-uniform (H_Σ) configuration, every Killing-spinor component at C₄ has s₁ = −s₂′. The 2216 filing left this CONDITIONAL on a Borel-density citation. PP's §3 proof is checked here, step by step, and is accepted. Credit: PP (f530cbc0 §3). The implication is of: Σ-uniform H_Σ data; Bolza Γ cocompact in G = (a finite cover of) PSL(2,ℝ); the twisted SL(2,ℝ) action ρ on the finite-dimensional space K of Killing spinors of the H² lift; and the identification of the stabilizer of p ∈ H² with ½(Γ^{S12} + Γ^{m1m2}). Steps, independently checked:
  1. If v ∈ K is Γ-invariant, f(g) = ρ(g)v is continuous and right-Γ-invariant, hence descends to the compact quotient G/Γ and is bounded.
  2. For a hyperbolic one-parameter subgroup a_t = exp(tH) and every h ∈ G, ρ(a_t)ρ(h)v is bounded in t. A nonzero H-weight component would grow exponentially in one direction of t, so ρ(h)v lies in the zero-weight space of H, equivalently dρ(Ad_{h^{-1}} H)v = 0.
  3. The adjoint representation of the simple Lie algebra sl(2,ℝ) is irreducible, so the Ad-orbit of the nonzero element H spans sl(2,ℝ). Thus v is annihilated by dρ(sl(2,ℝ)). For G connected, v is G-invariant.
  4. The stabilizer of p acts on spinors as ½(Γ^{S12} + Γ^{m1m2}). Invariance gives ½ i (s₁ + s₂′)ε = 0, hence **s₁ = −s₂′**.
  S2-4 is therefore **PROVED (implication)**. S2-5 and S2-6, already PROVED as implications of the twist lock, now rest on this proof.

- **S2-7 (stays CONDITIONAL).** The D6 no-go in scope S covers both **[χU] and [χS]**. The 2216 premise list is completed as follows (hygiene; grade unchanged):
  - the wall keeps at least one Killing spinor;
  - σ is a nonzero constant;
  - H_Σ = 0, with no single-Σ-leg G;
  - the D1 rows as derived (S2-2);
  - the homology of C₄ from the face to the IR on the kept side.
  Together with S2-4 (now PROVED as an implication) these are the premises of the no-go. Escapes, recorded:
  - **S5:** another IR point, or a singular IR;
  - **S6:** the odd ℤ₂ is a **record premise** (f825dfff), not a mathematical one.
  S2-7 stays CONDITIONAL and is not an adoption. Under t4436, [χU] and [χS] remain labelled branches, conditionally narrowed to the escapes (including E1–E5 of 2216 §5), not dropped.

- **Exact tests (hygiene; S2-9 and S2-1).** The `simplify(...)==0` checks in w3_symbolic.py and in eta_c4_sectors.py Part 1 are replaced by new script versions; the 2110 originals are not edited.
  - **W₃ identity (A1).** After the substitution e^φ=P, e^λ=Q, e^{w/2}=R, the numerator of V_{W₃}−V is the zero polynomial in (P,Q,R,g) (e23_w3_symbolic_exact). S2-9 stays PROVED, now on a Laurent-polynomial test rather than `simplify==0`.
  - **|b| at C₄.** A first new eta script (2233) used an incorrect ω₂ conversion that retained a spurious 1/Δ and is left unchanged as a record. The corrected 2239 script uses the CGR (2.6) coordinate fluxes and the orthonormal-frame conversion of eta Part 1, re-derived: at C₄, om2_coord = l/g² = −1, and in the frame, f₄ = 2·2^{1/3}, ω₂ = −2^{1/3}, A′_frame = 2^{1/3}/2 (all certified by minpoly = X). Then |b|² − (6A′)² = 0 (minpoly = X) on exactly the four locked sectors s₁ = −s₂′, and |b|² − (2A′)² = 0 on exactly the four unlocked sectors. Thus **|b| = 6A′ in the locked sectors and |b| = 2A′ in the unlocked ones**, as already stated in S2-1, now with an exact test. γ_r = b/(6A′) is ±1 on the locked sectors and ±1/3 on the unlocked ones. S2-1 stays PROVED.

- **Hand-typed log line (hygiene).** `z2_bvp_continuation.log` is not edited. A new note, NOTE_z2_bvp_continuation_log_hand_annotation_2026-11-09_2233.md (sidecar 77ab006c…), records that the last line of that log,
  `[killed by NL at 22:15 CST: d6=-0.200 (w_m=-0.05) BVP did not converge within ~10 min at max_nodes=1e6; remaining cases not run]`,
  was **hand-typed** by NL at 22:15 CST (America/Chicago) and is not program output. The sidecar of the log (b4036905…) was written at the same moment and therefore hashes the file including that line.

- **S2-12 (stays CONDITIONAL).** The 30L reach holds **only** for w_m ∈ {−0.05, −0.10} with d₆ ≥ +0.05, which is **12 flows** (six d₆ values in {+0.05,+0.10,+0.15,+0.20,+0.25,+0.30} at each of those two w_m). The w_m = −0.3 solved flows (ten of them) end by **2.01L**, with reaches 0.10, 0.18, 0.31, 0.46, 0.65, 0.86, 1.11, 1.39, 1.69, 2.01 L. Total distinct solved flows remain 31 = 30 first pass + 1 continuation (w_m=−0.05, d₆=−0.175, reach 0.07L). A new reprint (e23_z2_real_print) reads the existing 2110 logs only and prints **real values**, with the `+0.0000j` artefacts stripped; the logs themselves are not edited. Min NEC margin overall, as a real: +0.500. No NEC-respecting face. Grade unchanged (float / numerical).

- **E23-2 (PROVED; exact; global strengthening of S2-10).** Along a W₃-flow, X′^i = 2 G^{ij} ∂_j W with G^{ww} = 1/3. Differentiating W₃ gives
  **w′ = (2g/3) e^{−2φ+4λ} (e^w − e^{−2w})**
  (confirmed as a Laurent identity against the factored derivative 2G^{ww}∂_w W). The prefactor (2g/3)e^{−2φ+4λ} is positive. The real zeros of e^t − e^{−2t} are {0}, and f'(0) = 3 > 0, so e^t − e^{−2t} has the sign of t. Therefore **w · w′ ≥ 0**, with equality if and only if w = 0. Hence **no W₃-flow with w ≠ 0 reaches MN2** (where w=0). The same conclusion holds for either flow-sign convention: in the IR direction, |w| is nondecreasing, so a trajectory with w ≠ 0 cannot approach w=0. This is the global (non-linearised) reason that Z2 centre flows, which have w ≠ 0, are not W₃-flows; it strengthens the linearised exponent argument already in S2-10. S2-10 stays PROVED. Z2 kept sides remain outside scope S, so S2-7 does not cover them.

## 3. Branches
Under t4436, **[χS]**, **[χU]** and **[w]** are all kept. Nothing is adopted. S2-7 is a CONDITIONAL no-go in scope S and does not drop [χU] or [χS]. The [w] / Z2 branch stays OPEN (S2-11, S2-13), now with the global W₃ obstruction of E23-2 in addition to the linearised one.

## 4. Revised tallies of the audited files
| file | before | revised | change |
|---|---|---|---|
| D6 stage 2 (2216) | 7/3/3/0 = 13 | **8/2/3/0 = 13** | S2-4 COND → PROVED (impl., PP §3); S2-7 stays COND with completed premises; S2-10 strengthened; S2-12 count clarified |
| Erratum 22 (2211), roll-up | 2/0/0/2 (row count) | **0/0/0/0** distinct | E22-α, E22-β, E22-γ, E22-δ |

Revised 2216 register: **PROVED 8** (S2-1, 2, 3, **4**, 5, 6, 9, 10) · **CONDITIONAL 2** (S2-7, 12) · **OPEN 3** (S2-8, 11, 13) · **REFUTED 0**. Check: 8+2+3+0 = 13.

## 5. Junction / gap
No change. **Junction UNSOLVED; count gap unchanged.** Nothing adopted. D6 stays a CONDITIONAL no-go in scope S and OPEN on the escapes (S5, S6, and E1–E5). Z2 stays OPEN.

## 6. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 2 | E23-1 (S2-4 twist lock, impl., credit PP §3), E23-2 (W₃-flow w·w′ ≥ 0; no w≠0 W₃-flow reaches MN2) |
| CONDITIONAL | 0 | — |
| OPEN | 0 | — |
| REFUTED | 0 | — |

Check: 2 + 0 + 0 + 0 = 2.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
