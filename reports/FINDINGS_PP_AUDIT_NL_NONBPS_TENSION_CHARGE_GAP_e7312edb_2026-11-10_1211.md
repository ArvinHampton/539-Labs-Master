# FINDINGS: PP audit of NL e7312edb (does any non-BPS configuration close the exact tension-minus-charge gap? D-B3 pursuit, OW 1130)
2026-11-10, written 12:11:36 CST (America/Chicago). Author: **Professor Proof (PP), Soft SF audit** (audit after lane self-prove, not first-prove). Additive new file; no existing file edited, renamed, deleted or chmod-ed. **Nothing adopted.** **Junction UNSOLVED.** No CERT. Wording: resonant algebra. No message sent (no SendToAgent, no SendToUser, no external send). No metric invented; no non-BPS closing configuration first-proved.

## 0. Authority (each sha re-hashed by PP = its sidecar)
- **OW 1130** OWNER_WRITE_CALL_83d7a0fa_PURSUE_OPEN_ITEMS_UNAUDITED_FILINGS_2026-11-10_1130.md, sha 945d81bb447a923fc68c79ea3ce4df1405aa6f5787e27a301898e98042a47b3c = sidecar. Pursuit only: find whether any non-BPS configuration closes the tension-minus-charge gap. Its framing clauses ("BPS instanton trades leave the gap unchanged", "the S-four curvature charge is zero") are not adopted. N = 4880 and charge 9760 unadopted. PP is told to prioritize auditing NL and MR2 filings.
- **OW 1117** OWNER_WRITE_CALL_83d7a0fa_REVERSE_ENGINEER_FROM_GEOMETRY_2026-11-10_1117.md, sha bff79185f361bf461194c8d8c9590a4dc7ad0e520ce2f985f41048453545a2f4 = sidecar (geometry first; method directive).
- **OW 1108** OWNER_WRITE_CALL_83d7a0fa_PURSUE_HW_ODD_G4_BRIDGE_C_CLOSING_IMPLICATIONS_2026-11-10_1108.md, sha c6375f853020e8e994125e1b42acffe830350db0b116b60f0f5f75abbb5f84ca = sidecar. E₈ wall sector CONDITIONAL, gated by backreaction (O5).
- **Standing t4436** OWNER_WRITE_MAINCHAT_t4436_LET_MATH_LEAD_ALL_OPEN_PATHS_2026-11-09_2127.md, sha 328812635d807f5cb7d1e5e6b5df7f89512060c36c090a2a191526ab7e90fd46 = sidecar.
- PP audits as filed; no first-prove; no regrade by fiat. Citation rule: a citation never makes a result PROVED by itself; Y14 stage-2 floats cannot support a general PROVED; 2808.6 and 19520/3 stay CONDITIONAL test targets.
- NL Erratum 26 (NL_ERRATUM26_ACCEPT_PP_5cf92795_E8_DELTA_1120_2026-11-10_1142.md, a44b18d945aaf2600cbafde50c6777a983c81899c47c5e545c9b5e4a0a538179 = sidecar, 11:42:04) is being confirmed separately by PP. It is **not** treated as confirmed here and is **not** used as an input. The restatements are checked against PP 5cf92795 directly (§3).

## 1. Integrity
| object | sha256 (PP re-hash) | = sidecar | mode | note |
|---|---|---|---|---|
| NL filing NL_DERIVED_NONBPS_TENSION_CHARGE_GAP_MAKEUP_2026-11-10_1142.md | e7312edb8e4b5ad3d104c779688d7842a9e7b5deb3aaafe6176de1bfe94fe4bd | yes | 644 | header "written 11:42:33 CST" = mtime 11:42:33.784 ✓; 24521 bytes. Mode 644 = NL convention (nit only) |
| /workspace/nl-e8-nonbps-1130/nonbps_gap.py | e483f4b183773da0e3791cacc0ba27d93f56e55cbba8fc4a4208d29af5dbbe12 | yes | 444 | mtime 11:39:35.528; sidecar 11:39:35.532 |
| /workspace/nl-e8-nonbps-1130/nonbps_gap_run.log | bf2484a6718be693dcca5802c8f8bf6791894b9f8213cf738f0adf4f3b7c6402 | yes | 444 | mtime 11:39:39.488; sidecar 11:39:39.568 |
| PP 5cf92795 FINDINGS_PP_AUDIT_NL_E8_INSTANTON_GEOMETRIC_DELTA_79ad0c64_2026-11-10_1137.md | 5cf927959babc94b1719c99b312cfbb9d6366237626c781e8d5c75f21ce15b03 | yes | 444 | restatement source |
| NL 1120 (79ad0c64) | 79ad0c6417e825d4fee8d412af62a767688b883a88c39c6a6affd716ce4ffa29 | yes | 644 | frozen; read only |
| NL Y14 stage 2 (1950) | 5e079f4aa6d5ea5a3a84f9f9f66abb249fd432b0af849e94e4cc3c6c494f2ebd | yes | 644 | literature (twisted blocks, T1, S2-2, S2-c, table §5) |
| PP 077e417d (Y14 stage-2 audit) | 077e417db7f24ece269d7dcde21bc89e260bbe1102d985c63ab60aa94813c23b | yes | 644 | S2-2 → CONDITIONAL (N10) |
| OW 1130 / 1117 / 1108 / t4436 | see §0 | yes | 644 | — |
| Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | yes | 644 | mtime 2026-11-06 14:38:54 CST; custody §9 |

**Log count.** The frozen log has **23** lines beginning `[PASS]`, **0** `[FAIL]`. A naive `grep -c PASS` gives 25 (the "23/23 PASS" and "ALL PASS" summary lines). NL's "23/23 PASS, exit 0" is correct.

**Method claim, verified by reading nonbps_gap.py.** No `simplify()==0`, no `allclose`, no `nsimplify`, no numpy, no `evalf`, no float literal in any test. `Fr("2808.6")` is built from a string, so it is the exact rational 14043/5. Zero tests are `sp.expand(...)==0`, Gröbner remainders modulo {s²+c²−1, s_θ²+c_θ²−1} (a Gröbner basis: coprime leading terms), or exact Fraction comparisons. Nits:
- (M-1) K2 takes F_A and D_A a as unconstrained symbolic 2×2 matrices (not su(2)-valued). This is harmless: the t⁴ coefficient does not involve them. PP Q9 re-checks the t⁴ coefficient on a curved chart.
- (M-2) Z1, F2 and I1–I3 are bookkeeping comparisons of inputs (as PP said of 1120's C5/C6). They are not tests of the geometric chain.
- (M-3) C3's comment says "factor of X_b − X_a". The factor is actually **(X_b − X_a)²** (PP Q5b). The test passes either way.
- (M-4) The log has no wall-clock stamp. "Frozen before the run" is supported only by the mtime order: script 11:39:35.528 < sidecar 11:39:35.532 < log 11:39:39.488. The filing's "run started at 11:39:35.54" is not evidenced in the log itself (nit, no effect).

## 2. Evidence (PP)
Directory /workspace/quantum-comp/reports/evidence_pp_audit_nl_nonbps_gap_e7312edb_2026-11-10/. Every file is mode 444 and has a `.sha256` sidecar (444) that verifies with `sha256sum -c`.
| file | sha256 | content |
|---|---|---|
| nonbps_gap_copy.py | e483f4b183773da0e3791cacc0ba27d93f56e55cbba8fc4a4208d29af5dbbe12 | byte-identical copy of NL's frozen script (`cmp` clean); frozen original not touched |
| nonbps_gap_rerun.log | bf2484a6718be693dcca5802c8f8bf6791894b9f8213cf738f0adf4f3b7c6402 | PP re-run (sympy 1.14.0), exit 0, 23/23, **byte-identical** to NL's log (`cmp` clean; the log carries no wall-clock, so there is nothing to except) |
| pp_exact_checks_v1_draft.py | 8fb2663d7f14bf844dce2ef12f736a379ec117c907aee42e5741d4fffd168dda | PP's first draft, kept for disclosure (buggy; superseded) |
| pp_exact_checks_v1_draft_partial.log | 088679b1531ad5660d9f296b520300672ca9ae0581595d706c57249d1bb8b641 | v1 sections Q1–Q4 only: 2 FAIL from PP's own bug |
| pp_exact_checks_v2.py | 90f085ccca81e8126226ea7ba55de55decdf5b92ccaa81c2d8470b1516a2f3ff | **sealed final** independent checks Q1–Q10 |
| pp_exact_checks_v2.log | 62a3ece066f7048ff97f43cff144a94c5014d3af6dcc17d96ca723e6c4da9b48 | **32/32 PASS, exit 0**; a second run is byte-identical |

**Disclosure.** PP's v1 draft had two defects, both in PP's own code:
- (i) In Q2, PP defined the charge density as the Pfaffian instead of 2·Pfaffian. Q2a and Q2c failed for that reason, not because of anything in NL's work.
- (ii) PP's v1 Weyl computation, with both X's symbolic plus a full |Weyl|² factorization, did not finish in 10 minutes and was killed.

v2 fixes (i) and restructures (ii): it sets X_a = 1 by a constant rescaling, keeps r = X_b/X_a symbolic, and uses a Weierstrass rational parametrization. v2 is the final run. NL's files are untouched.

**What PP's checks establish.** These are independent implementations, not re-runs. Zero tests use `Poly(...).is_zero` after `cancel`, or `expand==0` on derivative polynomials, or exact Rational/Fraction comparisons. There are no floats and no trig identities.
- **Q1 (B1–B5):**
  - T − Q = 2N₋ + (u−1)n + ε_ex.
  - At u ≥ 1, T − Q has only nonnegative coefficients for both signs of n: 2N₋ + δ + v|n| + vδ (+2|n| for n < 0).
  - **u < 1 witness:** u = ½, n = Q, BPS, N± = 0 gives T − Q = −Q/2 < 0. So A1's u ≥ 1 scope is sharp.
  - A2's form (1−u)N₊ + (1+u)N₋ + u(e_u − n) holds.
  - **Closure is T − Q − Δ_N = u·e_u − n + 2N₋ − Δ_N** (Q1e). GB8's filed g = u·e_u − n − **2N₋** − Δ_N differs from it by −4N₋ (Q1f).
  - **A5 counterexample for n < 0:** u = 2, n = −1, Δ_N = 0 gives target 1, but the Bogomolny floor is 2u|n| = 4 (Q1g).
- **Q2 (P1):** with ⋆ built from the Levi-Civita symbol, ⋆² = 1, q = 2Pf(F), ρ ∓ q/2 = ⅛Σ_ordered(F ∓ ⋆F)² = ½Σ_{3 pairs}.
- **Q3 (W5):** for both SD and ASD ω, det(v ↦ v∧ω) = ±(a²+b²+c²)². So W5 does not depend on the orientation or trace convention.
- **Q4 (GB3's density step):** for W = X_b + (X_a − X_b)|y|² on S⁴ ⊂ ℝ³⊕ℝ², the tangential gradient is 2(X_a − X_b)(−|y|²x, (1−|y|²)y). Its zero set is {y = 0} ∪ {x = 0}, an S² and an S¹ with empty interior.
- **Q5 (GB6):**
  - At r = 1 all 21 Weyl components vanish identically.
  - For general r, **C_0303 = 4t²(r−1)²(1−t²)² / [3(1+t²)²(r(1−t²)² + 4t²)]** with t = tan(χ/2), and the denominator is positive.
  - At r = 2, sin χ = 3/5: C_0303 = 48/1025, which is NL's C2 value in the same R^a_bcd convention.
  - So on this family **the fibre is conformally flat iff r = 1**. This is stronger than C1–C3.
- **Q6 (W1, W2):** the virial identity holds in an independent matrix-su(2) implementation (D = d + [A,·]), and t_ab is traceless.
- **Q7 (W3, W4):** Hess cos α = −cos α·g on round S⁴, and |∇h|² = 1 − h², with no trig identity used.
- **Q8 (F1/F2), with a strengthening:**
  - For a **general** 45-component 10D field, including electric and x-legs: tr_fib S + 4ρ = 2P_ff + P_Σf + P_xf + 3E_f² + 4E_Σ² + 4E_x² ≥ 0. It is a diagonal form with no negative coefficient.
  - A positive-tension brane with k ≤ 4 fibre directions in its worldvolume has tr_fib T = −kT ≥ −4ρ.
  - With w < −1 and ρ > 0 the gap is −4ρ(1+w) > 0. The exact values 4w are −24/5 and −16/3.
- **Q9 (K):** on any positive-definite chart the t⁴ coefficient of |F|²_g along t·a is 2φ⁴det(g⁻¹) > 0.
- **Q10 (I1–I3, labelled CONDITIONAL test targets only):**
  - Δ_N(UV) = 19520/3 and Δ_N(IR) = 14043/5.
  - At [u=2] the UV-BPS endpoint gives g < 0 iff n ≤ 6506.
  - At n = 115 the UV sign needs only e_u(UV) < 19865/6.
  - IR excess Δ_N − n = 13468/5 > 0.
  - Z1 holds.

## 3. Use of PP 5cf92795 restatements (checked against 5cf92795 §3–§7, not against Erratum 26)
| restatement | in e7312edb | verdict |
|---|---|---|
| N-1: n_inst = (1/16π²)∫tr F∧F, n_R = −(1/32π²)∫tr R∧R, u := 8π²/(λ²T_M5) | header "Normalization N" | ✓ used; u-values carried as branches, not adopted |
| GA12 = implication of C ∧ I ∧ N | header | ✓ |
| GA13 REFUTED only as u = 2 ∧ C ∧ I | header | ✓ |
| D-B1 CONDITIONAL on u = 1, R5, S1, N, x-tension = energy density | header; A7 | ✓ |
| D-B2 requires u ≠ 1 ∧ ¬C, plus ¬GA7b under I | header | ✓ |
| D-B3 OPEN; V sense by sense | header; V′ | ✓ (D-B3 left unclosed, §6) |
| D-D given J1, constant unbackreacted end faces, IR-kept pairing, source set; tr R² leading 1/N; C∧X₈ OPEN | header; A13 | ✓ |
| R9 new OPEN item, x-equation only | GB8, §3 junction | ✓ |
| 3-pair excess sum (= ¼ over all 6) | header ε_ex | ✓ (PP Q2) |
| 23/23 (1120 log) | header | ✓ |
| struck D-A sentence "instanton energy does not cancel tr R²" | line 27: explicitly not reused | ✓ not reused anywhere (grep) |
| GA4 nit 8: "for every smooth connection on TM\|_{S⁴} (closed smooth fibre)" | GB0 still says "for every fibre metric" | **nit** (§8 N-6) |
| GA7a scope "constant face; fibre-only legs and dependence" (nit 9) | GB3 says "warped face … as in 1120 GA7a" without naming constant face / fibre-only | **required scope** (§4 GB3) |

## 4. Lead items (NL's audit-first list)
### 4.1 A1, sign [u ≥ 1]: PROVED (implication), stands
- B2 is reproduced independently (Q1b) for both signs of n, with e_u ≥ |n| from GB2.
- The u < 1 companion (A2, B4) is reproduced (Q1d). The **u ≥ 1 scope is sharp**: at u < 1 a negative gap is kinematically closable, with u = ½, n = Q, BPS giving T − Q = −Q/2 (Q1c). Only N_req ≥ uQ survives there.
- **Required scope:** A1 is an implication of the bookkeeping premises T = N₊ + N₋ + u·e_u and Q = N₊ − N₋ + n. These are the D-B1 premises (R5 HW charge equation, S1, N, x-tension = energy density) plus the source set {E₈ YM, positive-tension M5/anti-M5}. C∧X₈ (S4) is outside the source set and is OPEN.
- On-record Δ_N test targets: 14043/5 and 19520/3 are > 0 (Q10a), so A1 does not fire on them. These are labelled CONDITIONAL test targets, not adopted numbers.

### 4.2 A5, off-shell kinematic closure: PROVED **only in the n = 0 scope**; the literal [u ≠ 1] clause overclaims (priority)
- **What is proved** (A3 + Q9 + connectedness): fix any u > 0, any Δ_N ≥ 0, n = 0, N₋ = 0 and N₊ = Q. Then the trivial bundle carries smooth connections A_t = t·a (polynomial energy, quartic growth, value 0 at t = 0) with ε_ex = u·e_u(A_t) taking every value in [0, ∞), so ε_ex = Δ_N. With n = 0 the [u ≠ 1] target Δ_N − (u−1)n *is* Δ_N. So "charge 0 suffices" proves the statement for every u, **with n = 0**.
- **What is not proved:** the clause "every target Δ_N − (u−1)n ≥ 0 at [u ≠ 1]" read for n ≠ 0.
  - For **n > 0** a charge-n connection is needed, which is not charge 0. Reaching small targets needs A4 (infimum 0: Taubes / grafting). A4 is CONDITIONAL, a citation not re-checked. Only targets ≥ ε_ex(A₀) for an exhibited charge-n A₀ are proved. That part of A5 is **CONDITIONAL on A4**.
  - For **n < 0** it is **false as written**. GB2 gives ε_ex ≥ 2u|n|. Counterexample: u = 2, n = −1, Δ_N = 0 gives target 1 < 4 (Q1g). The condition must be target ≥ 2u|n|.
- **Ruling:** A5 stays **PROVED** (no class change) **with its statement restricted to n = 0** (equivalently "for every u and every Δ_N ≥ 0 there is an off-shell charge-0 configuration"). The n ≠ 0 extension is CONDITIONAL on A4 for n > 0 and needs the floor for n < 0. "Not a closure; off shell" ✓. The citation in A4 is not upgraded.

### 4.3 GB3: PROVED for the stated equation, **with required scope**; it does not cover the twisted blocks used in A9
- The argument checks out. ε_ex = 0 with n > 0 gives F⁻ ≡ 0. Then D(W⋆F) = dW∧⋆F + W D⋆F = dW∧F = 0 (Bianchi). W5 holds for SD and ASD (Q3), so F = 0 on {dW ≠ 0}. That set is dense for W = Δ̃ (Q4; analytic non-constant W in general), so F ≡ 0, a contradiction. For n < 0, ε_ex ≥ 2u|n| > 0 holds trivially.
- **Required scope (GA7a / PP fe0c3d92 Y6-math, as restated in 5cf92795 §3.4):**
  - the stated equation is the **source-free** D(W⋆₄F) = 0;
  - on a **constant** (unbackreacted) face, with W = c_x²c_Σ ∝ Δ̃ so that dW = dΔ̃;
  - for fields with **fibre-only legs and fibre-only dependence**;
  - W real-analytic and non-constant;
  - the full HW system is GA7b, CONDITIONAL.
  The row heading "warped face … every smooth static charged E₈ field" must not be read beyond that class.
- **Load-bearing consequence.** The Y14 stage-2 blocks used in A9 are **twisted**: F_tot = F_fib^hor + Φ·π*F_tw has a ΣΣ leg (Y14 T1). They solve D(W⋆F_fib) = (twist source) ≠ 0, not the stated equation. GB3 therefore does **not** apply to them. Their strict non-BPS character is Y14 S2-2, which PP 077e417d ruled **CONDITIONAL** (N10). GB3's grade is unchanged, but citing GB3 in A9 and V′ for twisted blocks must be corrected (§4.6, §4.8).
- The density step is illustrated exactly for W = Δ̃ (Q4). For W = Δ̃e^{4f+2g} on a constant face, the factor is constant, so the step is the same.

### 4.4 GB5 / GB6: both PROVED; "does not transport to MN2" verified and strengthened
- **GB5 [PROVED for its class].**
  - The virial identity is re-checked (Q6). On shell, for conformal Killing X, it gives ∫|F|²X(W) = 0. This uses tracelessness and needs the **source-free** equation and a closed smooth fibre.
  - For conformally round ĝ with W = w(h), w′ > 0 strictly (h the height in the round representative), X = ∇h gives X(W) = w′(1 − h²) (Q7). So F ≡ 0, and no static field exists.
  - Hypotheses to keep explicit: conformally round, strictly monotone w, source-free equation.
- **GB6 [PROVED].**
  - Weyl ≡ 0 at r = 1 (Q5a). For general r, C_0303 = 4t²(r−1)²(1−t²)²/[3(1+t²)²(r(1−t²)² + 4t²)] (Q5b), and it equals 48/1025 at r = 2, sin χ = 3/5 (Q5c).
  - So on the MN2-type family the fibre is **conformally flat iff X_a = X_b**. Every face with r ∈ (1, 2] (all interior faces and IR; Y14 §3 gives r ∈ [1, 2] on the flow) fails GB5's hypothesis.
- **"Does not transport" is correct and load-bearing.** A round-fibre obstruction (GB5) **may not be applied to MN2 faces**, and the filing does not apply it: A8 explicitly says GB5 does not apply. Scope: GB6 shows only that GB5 is inapplicable. It is not evidence that static non-BPS fields exist (A8 OPEN) and not a no-go. The UV face (round, constant W) is outside GB5 as well, since w′ > 0 fails; this is consistent with the BPS UV field used in A9.
- **GB6′ [CONDITIONAL, stands].** It cites Ferrand–Obata, not re-checked. The gap that conformal isometries need not fix W is disclosed. Add: for twisted blocks the virial identity acquires a source term, so neither GB4's on-shell form nor GB6′ applies to them as stated.

### 4.5 GB7: PROVED, stands; exact statement and hypotheses
- The statement is the first variation of E_W along a **C¹ family of critical points**, in a space where E_W is C¹ (smooth or W^{1,2} connections): dE_W/ds = DE_W(A_s)[∂_sA] = 0. Isometries of ĝ and gauge preserve the unweighted e_u.
- What is proved: on a fixed face, e_u can vary only along moduli of critical points, and E_W is constant there. "No tuning knob" means **no external continuous parameter**. It does not mean that e_u is constant on moduli (the row says so).
- "Exact closure is a selection condition" is a restatement of the definition.
- For twisted blocks, replace E_W by the full reduced functional including the twist term. The argument is identical for any C¹ functional whose critical points are the static solutions.
- Critical-value structure is A16 (OPEN) ✓.

### 4.6 A9 and its gates: CONDITIONAL, stands **gated**; additional gates required (priority)
- What is right:
  - 9760, N = 4880, 2808.6 and 19520/3 appear only as labelled CONDITIONAL test targets (I1–I3; Q10).
  - The IVT lemma (GB8) is trivially valid **for continuous g on a compact interval**.
  - N₋ = 0 in A9, so GB8's sign error (§5) does not affect A9.
- **IVT hypotheses are assumed, not proved:**
  - (vii) **branch continuity**: the charge-n twisted branch must exist and depend continuously on b across all interior faces. Y14 S2-c computed this only for n = 1–3. For n ≈ 115 it is assumed. This is gate (i) as filed ✓, but it must say "assumed".
  - (viii) **UV endpoint landing (new gate)**: g(UV) < 0 uses the round BPS field e_u = n. The IVT needs the **same** branch to reach, at the UV end, a field with 2e_u − n < 19520/3, i.e. e_u(UV) < 19865/6 at n = 115 (Q10c). Round S⁴ has non-SD equivariant critical points, so this is not automatic. Y14 says "stage 1's untwisted validation applies" at the UV, which was not computed for n = 115.
  - (ix) **The UV is a limit** (c → 0, R/R₀ → ∞). Either g must extend continuously to that limit, or a finite b₂ with g(b₂) < 0 must be exhibited.
  - (x) **Δ_N(b) continuity along the flow**: on record only as interior float prints (Y14 §5).
- **(xi) attribution fix (priority):** "the closing configuration is strictly non-BPS at b* (GB3)" is wrong for a twisted block (§4.3). Replace it with "(Y14 S2-2, CONDITIONAL per PP 077e417d)".
- Gates (ii)–(vi) as filed ✓. The Y14 table entry at u = 2, "(110, 115]", does not say whether it uses e or e_u. It is carried as filed (CONDITIONAL).
- The row stays **CONDITIONAL**, an implication of gates (i)–(xi). It does not close D-B3.
- **A9′ [u=1]: OPEN, stands.** No extrapolation past n = 160 is used ✓. Nit: "places this just beyond its computed range" repeats Y14's own wording. Better: "not reached within the computed range n ≤ 160 (e_u)". Note also that Y14's **e**-column (weighted) gives an in-range bracket (155, 160]. So A9′'s OPEN status depends on taking the x-tension to be e_u (unweighted), which the filing defines (header) but which belongs with the D-B1 premise "x-tension = energy density". NL should state the choice explicitly (nit).

### 4.7 A13(b): fibre-trace form verified; A13 REFUTED **only as scoped**
- F1 is reproduced, and PP Q8 **strengthens** it:
  - tr_fib S + 4ρ ≥ 0 holds for a **general** 10D E₈ field, including electric and x-legs: 2P_ff + P_Σf + P_xf + 3E_f² + 4E_Σ² + 4E_x².
  - It holds for any positive-tension brane with ≤ 4 fibre directions in its worldvolume.
  - So the restriction to "magnetic Y₆ fields" and the M5 orientation (t, x, Σ) is not needed for (b).
  - This remark does not raise any grade.
- F2: 4w_fib = −24/5 (UV) and −16/3 (IR), both < −4, exact. These are given J1 inputs (T0/F1 PROVED given J1; J1 CONDITIONAL).
- The contradiction needs ρ_req > 0 (IR-kept pairing): −4ρ_src − 4wρ_req = −4ρ(1+w) > 0 (Q8d).
- **Ruling:** A13 is REFUTED as an implication. Under J1 (CONDITIONAL, CLP/BBBW), constant unbackreacted **end** faces, IR-kept pairing (ρ_req > 0), source set {E₈ YM, positive-tension branes}, tr R² at leading 1/N only (CONDITIONAL at N = 4880), and C∧X₈ OPEN, the claim "a closing configuration is a full geometric solution at the end faces" is false.
- It is **not** a refutation of J1, of the geometry, or of the E₈ wall sector. It does **not** close D-B3, and it does **not** solve or refute the junction (Junction UNSOLVED).
- (a) = 1120 D-D/C3 as scoped in 5cf92795 §3.1 ✓.
- **A14 [CONDITIONAL] stands** (GA8-int, Y15-int float numerics).

### 4.8 V′: CONDITIONAL, sense by sense; two headline overreaches (priority)
- The sense-by-sense form is right, and the grade CONDITIONAL is right. Fixes needed:
  - (a) "kinematically yes, with continuous tuning and no quantization (A5)" must carry A5's **n = 0 scope** (§4.2).
  - (b) "**Any** smooth static closing field is strictly non-BPS (GB3, A7)" overclaims. GB3/A7 cover constant warped faces, fibre-only legs and dependence, and the source-free stated equation. Twisted blocks fall under Y14 S2-2 (CONDITIONAL). The round UV face (W constant) is outside GB3. Restate it as "on constant warped faces, for fibre-only fields obeying the stated equation (GB3); twisted blocks CONDITIONAL (S2-2)".
- The other senses are correctly labelled: A1 PROVED (u ≥ 1, source set); A6 OPEN; A9 CONDITIONAL / A9′ OPEN; A10–A12; A13 REFUTED as scoped; A14 CONDITIONAL; A15 OPEN. None of A1/A5/A9/A13 is overstated beyond (a) and (b).

## 5. Other rows (same standard)
| row | NL | PP | basis / required scope |
|---|---|---|---|
| GB0 | PROVED | PROVED (p₁ step) | stable triviality ⇒ p₁ = 0 ⇒ ∫tr R∧R = 0 for **every smooth connection on TM\|_{S⁴}** (closed smooth fibre), as in 5cf92795 §3.3; backreacted point sources = O5. "Charge equation with no curvature term" is the HW Bianchi identity, R5 **CONDITIONAL**; label "(p₁ step)". Not a relitigation of D-A ✓; struck sentence not reused ✓ |
| GB1 | COND | COND | standard topology, not re-derived |
| GB2 | PROVED | PROVED | P1 = Q2 (both orientations Q3). Nit: state the trace/orientation convention under which n_inst ≥ 0 ↔ SD |
| GB3 | PROVED (impl.) | PROVED (stated eq.) | §4.3 required scope; not applicable to twisted blocks |
| GB4 | PROVED | PROVED | W1/W2 = Q6. The flat-chart check transfers to curved g via normal coordinates (first-order tensor identity using Bianchi). On-shell virial needs the source-free equation and a closed smooth fibre |
| GB5 | PROVED (class) | PROVED (class) | §4.4 |
| GB6 | PROVED | PROVED | §4.4; strengthened to "conformally flat iff X_a = X_b" (Q5). C3 factor is squared (M-3) |
| GB6′ | COND | COND | §4.4 |
| GB7 | PROVED | PROVED | §4.5 |
| GB8 | PROVED (lemma) | PROVED after sign fix | **g must read u·e_u − n + 2N₋ − Δ_N** (Q1e/f). As filed, "g(b*) = 0 i.e. integrated closure" is false for N₋ > 0. It is correct at N₋ = 0, which is R9's form and A9's case. No class change (priority fix) |
| GB9 | PROVED (ratio) | PROVED (ratio algebra) | Z1 tautology; boundary-value statement GA2/P-b CONDITIONAL (named ✓) |
| A2 | PROVED | PROVED | Q1d. Add: at u < 1 negative Δ_N is not excluded; only N_req ≥ uQ (Q1c) |
| A3 | PROVED | PROVED | A3 rests on: the affine space of connections; the energy along segments being a polynomial in t (IVT); t⁴ coefficient > 0 on any metric (Q9); and the flat connection at n = 0 |
| A4 | COND | COND | Taubes / grafting, cited. (Given Taubes, the infimum is attained, giving [0, ∞); still a citation) |
| A6 | OPEN | OPEN | nit: "codimension-1 coincidence" is a heuristic, not proved |
| A7 | PROVED (impl.) | PROVED (impl.), rescoped | GB3 scope (constant warped face, fibre-only, stated equation), u = 1, N₋ = 0. "Can only be realized by zero-size (point) instantons" → "**is not realized by any smooth static fibre-only field; a realization would need zero-size objects, whose identification with M5s is I (CONDITIONAL)**" |
| A8 | OPEN | OPEN | ✓; add the twist-source remark (§4.4) |
| A10 | PROVED (impl.) | PROVED (impl.) | pointwise P1. Label must carry [u ≥ 1] and GA2/P-b (CONDITIONAL) set-up |
| A11 | PROVED | PROVED | GB3 local form, same scope as GB3. W non-constant on U follows from analyticity + connectedness |
| A12 | OPEN | OPEN | — |
| A15 | OPEN | OPEN | no backreacted metric on disk or constructed; none invented ✓. "What transfers" list fine; GB3 transfer stays "CONDITIONAL on the static equation holding there" |
| A16 | OPEN | OPEN | — |

## 6. D-B3
D-B3 is **correctly left unclosed**. What is PROVED is only the integrated sign at u ≥ 1 (A1) and the off-shell kinematics at n = 0 (A5, scoped). Fixed-face on-shell (A6), [u=1] flow (A9′), profile (A12) and backreacted (A15) closure are OPEN. [u=2] flow closure (A9) is CONDITIONAL on gates (i)–(xi). A closing configuration is not a full geometric solution at the end faces (A13, as scoped). **D-B3 is advanced, not closed; it stays OPEN in 1120's ledger.**

## 7. Tally
- **Ruled: PROVED 16 · CONDITIONAL 6 · OPEN 6 · REFUTED 1 = 29. NL's counts stand.** Lists = header = body, 29 distinct rows, no double count. **No row changes label class.**
- Mandatory scope relabels: A1 (bookkeeping premises + source set + [u ≥ 1]); A5 (n = 0; n > 0 CONDITIONAL on A4; n < 0 floor 2u|n|); GB3/A7/A11 (constant warped face, fibre-only, source-free stated equation); GB8 (+2N₋); GB0 ("p₁ step"; R5 CONDITIONAL); A9 (gates vii–xi); A10 ([u ≥ 1], GA2/P-b); A13 (as in §4.7); V′ (§4.8).
- **Other standing tallies: unchanged by this file.** That includes t4436 menus, Bridge C (PARTIAL), the parent E₈ ledger, 1120's ruled 22/16/5/2, 1800 (13/11/3/2 as revised), Y14 stage 2 (7/10/2/1 per 077e417d), and Y16. None is rewritten. **E₈ wall sector stays CONDITIONAL** (gated by O5).

## 8. Fixes for an additive NL erratum (do not edit e7312edb, nonbps_gap.py or nonbps_gap_run.log)
**Priority (NL should act):**
1. **A5:** restrict the statement to n = 0 (any u, any Δ_N ≥ 0). Mark the n > 0 extension CONDITIONAL on A4. Replace "target ≥ 0" by "target ≥ 2u|n|" for n < 0 (counterexample Q1g).
2. **GB8:** g(b) := u·e_u(n,b) − n **+ 2N₋** − Δ_N(b) (Q1e/f).
3. **GB3 scope:** constant (unbackreacted) face, fibre-only legs and dependence, source-free D(W⋆F) = 0 (GA7a / fe0c3d92 Y6-math). State that twisted (Σ-legged, sourced) blocks are **not** covered.
4. **A9:**
   - replace "strictly non-BPS at b* (GB3)" with "(Y14 S2-2, CONDITIONAL per 077e417d)";
   - add gates (vii) branch continuity **assumed** for n ≈ 115, (viii) UV landing e_u(UV) < 19865/6 at n = 115 on the same branch, (ix) the UV as a limit / continuity of g there, and (x) continuity of Δ_N(b).
5. **V′:** scope "kinematically yes" to A5's n = 0 statement. Scope "any smooth static closing field is strictly non-BPS" to GB3's class, with twisted blocks via S2-2 (CONDITIONAL).
6. **A7:** "only by zero-size (point) instantons" → "not by any smooth static fibre-only field (GB3 class); zero-size objects need I (CONDITIONAL)".
7. **A1:** name the bookkeeping premises (R5, S1, N, x-tension = energy density) in the label. State that the u < 1 companion leaves negative Δ_N kinematically closable (Q1c).

**Non-priority (nits):**
- N-1. A9′: "not reached within the computed range n ≤ 160 (e_u)". Also state the e vs e_u choice (Y14's e-column crossing is (155, 160]).
- N-2. A10: put [u ≥ 1] and GA2/P-b in the label.
- N-3. GB2: state the trace/orientation convention for n_inst ≥ 0 ↔ SD (W5 holds for both, Q3).
- N-4. C3 comment: the factor is (X_b − X_a)²; GB6 may say "conformally flat iff X_a = X_b on this family" (Q5b).
- N-5. A13(b): it may note that (b) holds for general fields and any positive-tension brane orientation (Q8). Optional.
- N-6. GB0: "for every smooth connection on TM|_{S⁴} (closed smooth fibre)", plus "(p₁ step); charge equation R5 CONDITIONAL".
- N-7. A6: mark "codimension-1 coincidence" as heuristic.
- N-8. K2: optional su(2)-valued background. Z1/F2/I1–I3 are bookkeeping comparisons.
- N-9. Log: a RUN_START wall-clock line would evidence "frozen before run" directly.
- N-10. Mode 644 on the filing (NL convention): optional.

## 9. Custody
- Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, mode 644, mtime 2026-11-06 14:38:54 CST. Hashes: at 11:47:44 CST (start), at 12:09:07 CST (before this write), and after this write (report-back). Never opened for writing; not chmod-ed.
- NL filing e7312edb and its sidecar, nonbps_gap.py, nonbps_gap_run.log and their sidecars: read and hashed only. The script was copied, not edited.
- Frozen 1120 files, e8delta.py, PP 5cf92795, Y14/077e417d, the OWs and Erratum 26: read and hashed only.
- Running Local jobs (s1e, chain_v2, s2e, wait_then_ob_v5) and other agents' directories: untouched. The parallel PP confirm of Erratum 26 and the audit of Local dff4b879 / MR2 9811de14 were neither waited on nor mixed in.
- New files: only this findings file, its sidecar, and the PP evidence directory (§2). PP's scratch copies in /tmp are not cited.

Nothing adopted. Tip 7cddb188 untouched. Junction UNSOLVED. No CERT. D-B3 is not closed. Resonant algebra.
