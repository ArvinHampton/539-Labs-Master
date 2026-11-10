# FINDINGS: PP audit of NL heavy-queue items 6, 7, 8 (2103 125bfda1…, 2133 49aed96d…, 2137 f996a6d5…)
2026-11-09, 21:5x CST (America/Chicago). Auditor: Professor Proof (PP). Pure math only. Labels: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. Float-only results are CONDITIONAL; a citation alone never proves; a stated premise is graded as an implication. **Nothing adopted. Junction: UNSOLVED.** Under OW t4436 all branches ([χS], [χU], [w]) are kept as labelled branches; no verdict here drops a branch. No CERT, nothing sent. New file only; no existing file edited; tip 7cddb188… not touched.

## 0. Integrity and reruns
| file | sha256 | sidecar |
|---|---|---|
| NL_DERIVED_T7_REDUCTION_COMPLETENESS_REGULARITY_2026-11-09_2103.md | 125bfda14d40f84666b846504a11a407a7cca313ad24ee8a68e2c3f9a46ecfb6 | MATCH |
| NL_DERIVED_Y14_ST2_OFFBLOCK_STABILITY_2026-11-09_2133.md | 49aed96d4df0c310c8ee7b4dd52ffca227a3414054cd992de460cf2a0b3f9086 | MATCH |
| NL_DERIVED_Y14_Q0_OTHER_SYMMETRY_SADDLES_2026-11-09_2137.md | f996a6d5b597a10c1196564444f5c2e85e51d517e60280eae58f5984cb0ca491 | MATCH |

All script/log shas quoted in the three files match the files on disk and their sidecars (y14s2.py, disc.py in nl-junction-1851 also match their sidecars; mtimes 18:50/18:54, i.e. unchanged).

| script | frozen before log? | PP rerun (PYTHONDONTWRITEBYTECODE, scratch cwd) |
|---|---|---|
| nl-t7-reg-2055/t7_w_Z1_j7b_poles_…_2101.py (a6d85380…) | .py 21:01, log 21:02 ✓ | exit 0, **byte-identical** (d8a25604…) |
| nl-st2-offblock-2105/st2_Tseq_phase_…_2129.py (6f0880c8…) | .py 21:30, log 21:32 ✓ | exit 0, **NOT byte-identical**: one digit differs, line 51, n=1 Neumann λ₄ 2.141160e-01 (PP) vs 2.141162e-01 (NL). Rerun log d3d0995d… |
| nl-st2-offblock-2105/st2_Tseq_phase_…_2109.py (b71d3c5b…) | .py 21:10, log 21:18 ✓ | exit 1, **same ARPACK death at T=20 n=1** (−1, 39981 it., 0/4); **NOT byte-identical**: line 9, T=16 λ₃ 4.446222e-06 (PP) vs 4.446221e-06. Rerun log c1282cd2… |
| nl-q0-saddles-2135/q0_other_sym_…_2135.py (391a0612…) | .py/log 21:37 ✓ | exit 0, **byte-identical** (7e8925db…) |

The two st2 mismatches are 7th-significant-digit jitter from ARPACK's random start vector (`eigsh` called without `v0`). No claim depends on that digit, but the logs are not reproducible bit-for-bit (fix H7-1).

PP exact script (new, independent; imports no NL code): /workspace/pp-audit-heavy678/pp_heavy678_checks_2026-11-09_2155.py = bf61cc56742cca508e75b946b043db6524b8787e5313590983f8acddeb826031, log 158aeaf9506780f8495ba7fac550bbb7e390f862319b50ab638fd8dbba89b265 (exit 0; a second run is byte-identical; sidecars written). Rerun logs are kept in the same directory with sidecars.

## 1. Item 6 (2103, T7 completeness/regularity): **SOUND IN PART; one sub-claim REFUTED (R1 4-form inventory), R5 REFUTED as stated; PP replacement for J7b**

**R1 consistency (PROVED, agree; Palais is not needed and is correctly not cited).** The argument is at the level of the equations of motion. Every h ∈ H is a symmetry of 11D sugra, so E[Φ] is an H-invariant tensor whenever Φ is, and imposing all 11D equations on the invariant ansatz truncates nothing. This is a genuine proof. It does not invoke symmetric criticality, and it should not: H (Poincaré × PSL(2,ℝ) …) is non-compact, and PSL(2,ℝ) acts only locally on Σ = H²/Γ. That is harmless, because the EOM are local. Scope note (fix H6-1): R1 does **not** license deriving the (r,χ) equations from a *reduced action*. That would need a symmetric-criticality argument, and Palais's compact-group theorem does not apply to this H.

**R1 inventory: metric PROVED; 4-form list REFUTED by counterexample.** PP computed the isotropy invariants exactly, as the kernel over ℚ of so(1,3) ⊕ so(2)_Σ ⊕ so(2)_{S²} acting on T* = ℝ^{1,3} ⊕ Σ ⊕ S² ⊕ ⟨dr, dχ, Dφ₁⟩ at a generic point:
- Sym²: dimension **9**. This matches NL's 9 metric functions (e^{2A}, g_rr, g_rχ, g_χχ, e^{2G}, R_φ₁², R_{S²}², A_r, A_χ) ✓.
- Λ⁴: dimension **8**. NL lists 7. The missing invariant is **vol(S²)∧dr∧dχ**, which is H-invariant and lies outside the span of NL's list. It is also closed: d(f vol(S²)∧dr∧dχ) = 0, so Bianchi does not remove it.

"The H-invariant 4-forms are spanned by [7]" is therefore false. The completeness claim needs the 8th component (fix H6-2). Nothing else in item 6 used the 7-term list.

**R2 Z1 (PROVED, agree).** PP independent code reproduces it: ∇V = 0; m²L² = {12, −4, 0}; ∂³_wV = −24·2^{2/3}g²; no mixing.

**R3 w ∉ T7 (PROVED, agree; consistent with PP Z1).** T = diag(e^w, e^w, e^{−2w}) is fixed by SO(3) only if w = 0. PP adds the converse the script omits: the real zeros of (1−e^{3w})e^{−2w} are {0}. Z1 lives in the CGR 7D truncation, whose w is the SO(2)_R-invariant, SO(3)-5-plet direction. T7 keeps the full SO(3), so w is projected out. This is a strict subsector statement and does not contradict Z1. It changes neither Z2 (OPEN) nor the [w] branch.

**R4 MN2 pole regularity (PROVED for the fibre metric, agree).** The fibre is the round S⁴ ⊂ ℝ⁵ with the metric induced from the flat positive-definite T^{−1}, times a smooth positive factor Δ^{…}, so it is a smooth metric. PP recomputed the cone ratios with the **full** g_χχ = cos²χ/X_a + sin²χ/X_b and gets 1 and 1 exactly. NL's script keeps only one term of g_χχ at each pole. The dropped term vanishes at that pole, so the limits are unaffected (fix H6-3, clerical). The twist term sin²χ(dφ₁+A_Σ)² is smooth at χ=0 (|dz − i z A|², z = χe^{iφ₁}). G₄ regularity is stated as a condition and not checked here, so the scope is the metric.

**R5 J7b (NL: PROVED → PP: REFUTED as stated, by counterexample).** NL takes a = q/6 = √6/3 "on the whole E8 wall family". But q := Q e^{−4C} (NL 1935 definition; NL's own R6 uses A′ = Q e^{−4C}/6), so on the wall a(C_w) = (√6/3)·e^{−4(C_w−C₀)}. That equals √6/3 only at C_w = C₀. **Counterexample:** C_w = C₀ − 1 lies in the E8 family (e^{−2B_w} = 6e^{−2C_w} holds for every C_w) and gives a = (√6/3)e⁴ ≈ 44.58 > 1, so the N4 inequality fails there. "Holds on the whole family; not an obstruction; does not constrain C_w" is false. A second error: N4's monotone quantity is dA_E/dρ_E in Einstein-frame proper distance, dρ_E = e^{s}dy with s = (2B+4C)/3. NL instead compares y-derivatives and sets 1/L_{5,E} = 1. In proper distance, 1/L_{5,E} = e^{−s₀} = (256/9)^{1/3} ≈ 3.0526.

**PP new item J7b-PP (PROVED as implication of the N4 premise: NEC plus a 5D Einstein-scalar description).** A singlet-toy wall solution requires
  a·e^{−s_w} ≤ e^{−s₀}  ⇔  **C_w − C₀ ≥ 7ln2/36 − ln3/12 ≈ +0.043228** (exact; sympy).
At C_w = C₀ it **fails**: 3.9565 > 3.0526. If one (incorrectly) compares y-derivatives instead, the condition is C_w − C₀ ≥ −ln(3/2)/8 ≈ −0.050683. Either way J7b **is** a constraint on C_w. It halves the scan line, and it is a necessary condition, not an existence result. E16-J7b is therefore not "discharged, not an obstruction". It becomes this constraint (fix H6-4). PP self-correction: PP's own J7a wording in 3982a4b8 ("A_E′ = −a") is a y-derivative. Its sign is right, but the magnitude compared under N4 must carry e^{−s}.

**R6 J4 (CONDITIONAL, agree).** The analytic bound |Y−FP| ≥ 1 is exact, since it uses only A′ > 0. NL's script has a sign error: B = C + ½ln6 should be **B = C − ½ln6**, from e^{−2B} = 6e^{−2C}. The numeric minimum is **1.2443 at C−C₀ ≈ 0.582**, not 1.966 at 0.348 (float, box-limited). The grade is unchanged (fix H6-5).

**R7 (CONDITIONAL), R8 (OPEN), R9 (OPEN): agree.** R9's "Z2 not opened or closed here" is correct.

| row | NL | PP | note |
|---|---|---|---|
| R1a EOM-level consistency | PROVED | **PROVED** | no Palais; not a reduced-action statement (H6-1) |
| R1b invariant inventory | (in R1) PROVED | **REFUTED** (4-form list) | 8th form vol(S²)∧dr∧dχ; metric 9 ✓ (H6-2) |
| R2 Z1 | PROVED | **PROVED** | PP exact |
| R3 w ∉ T7 | PROVED | **PROVED** | converse added |
| R4 poles | PROVED | **PROVED** (fibre metric) | full g_χχ (H6-3) |
| R5 J7b "holds on whole family" | PROVED | **REFUTED** | counterexample C_w = C₀−1; frame (H6-4) |
| R6 J4 | COND | **COND** | sign fix in distance (H6-5) |
| R7 wall, [χS]/[χU] | COND | **COND** | |
| R8 PDEs/spectrum | OPEN | **OPEN** | |
| R9 T7 c-theorem, Z2 | OPEN | **OPEN** | |
| **PP new** J7b-PP | — | **PROVED (impl. of N4)** | C_w − C₀ ≥ 7ln2/36 − ln3/12 |

**NL 5/2/2/0 = 9 → PP 4/2/2/2 = 10** (R1 split into two rows), **+1 PP new item (PROVED, implication)**.

## 2. Item 7 (2133, Y14 ST2 off-block/phase): **SOUND; grades agree 3/1/2/0**

- **S7-T (CONDITIONAL, agree).** Float64, (h,a) sector only. λ₁(T)/λ₁(12) = e^{−(T−12)} holds to 5–6 digits on the two status-0 points (T = 12, 16). T = 20 and 24 are solve_bvp status 1 and are correctly used only as support. A two-point fit is evidence, not a law ("λ₁ ∝ e^{−T}" is COND). No negative mode in the sector at the T tested.
- **S7-phase (PROVED as implication of the stage-2 Witten-form density, agree).** In y14s2 the density depends on the phase only through |D_tφ|². So E[h e^{iα}] − E[h] = ∫A h²α′² exactly, and at a critical point the O(ε²) real shift −hα²/2 pairs with δE/δh = 0, giving Hess(i hα) = 2∫A h²α′² ≥ 0. PP proved **A = sW/g_tt > 0** exactly on (0,∞): g_tt = (X_a sinh²t + X_b)/(X_a cosh²t), g_φφ = X_b sinh²t/X_a, W = (X_a sinh²t + X_b)/cosh²t. The numbers are only a check. Overstatement (fix H7-2): for n = 2, 3 the Neumann spectrum has several eigenvalues at or below about 4×10⁻⁷ (n=3: −1.09e-8, 1.5e-11, 9.9e-10, 1.9e-8), so "the remaining eigenvalues are positive" is not resolved numerically there (a weak-support near-kernel where h ~ t^n). The grade rests on the identity.
- **S7-a_t (PROVED, agree).** The quadratic form depends only on α′ − a_t, so it is ≥ 0 with or without gauge fixing. Suggested wording: "enters only via α′ − a_t" (H7-3).
- **S7-off (OPEN), S7-w (OPEN): agree.** S7-χ (PROVED, scope): agree. The fibre operator does not see the wall smearing.
- **2109 ARPACK death: disclosed ✓.** PP reproduced it, and no claim rests on it. Its T=12/16 values are not re-counted ✓. "They match" is to 6 digits: T=16 λ₁ is 1.068515e-06 (2109) vs 1.068514e-06 (2129) (H7-4, clerical). "Independent of n to the printed digits": n=3 λ₃ is 2.427642e-04 vs 2.427643e-04 (H7-4).

**NL 3/1/2/0 = 6 → PP 3/1/2/0 = 6.**

## 3. Item 8 (2137, charge-0 other-symmetry saddles): **SOUND; grades agree 3/1/3/0; PP completes the Q8-conf proof**

- **Q8-Witten (PROVED, agree).** This restates Q0, which PP audited as PROVED within the ansatz in 077e417d (1953), including step 3 with r ∈ [1,2] ≤ 9. It is an internal audited result, not an external citation. Scope w = 0 ✓.
- **Q8-conf (PROVED; NL's argument has a gap that PP closes).** g_φ₁/g_{S²} = (X_b/X_a)tan²χ, which is tan²χ on the round sphere and **2tan²χ** at the MN2 IR ✓ (exact). This ratio is invariant only under conformal maps that preserve the SO(3)×U(1) orbit identification, so on its own it shows only that the *given* identification is not conformal. PP closes the gap with the Weyl tensor of the fibre metric (exact): W_{χφχφ} ≢ 0 for X_a ≠ X_b, = 0 at X_a = X_b. At the MN2 IR, W_{χφχφ}(χ=π/4) = 2^{3/5}/18 ≠ 0. So the MN2 IR fibre is **not conformally flat**, and hence not conformal to the round S⁴ under **any** diffeomorphism (fix H8-1: cite the Weyl argument). The weight W = Δ̃ and the twist term are independent obstructions ✓.
- **SSU correctly not counted as existence ✓.** Q8-SSU is OPEN, and the UV round problem (where the functional does reduce to YM: W = 1, c = 0) is also left unchecked ✓.
- **Q8-gap (CONDITIONAL on Q8-SSU existence), Q8-w-ex (OPEN), Q8-Bolza (OPEN): agree.**
- **Q8-w (PROVED, scope, agree).** The script line "SO(3) isotropy … iff w=0: False" prints the generic non-identity, and "vanishes identically iff w=0: True" checks only the w = 0 direction. PP proves the converse (real zeros of e^w − e^{−2w} are {0}) (H8-2, clerical). det T = 1 ✓; X_a = e^{−6λ}, X_b = e^{4λ} give ratio 2 at MN2 ✓.

**NL 3/1/3/0 = 7 → PP 3/1/3/0 = 7.**

## 4. Roll-up
| file | NL | PP |
|---|---|---|
| 6 (2103) | 5/2/2/0 = 9 | **4/2/2/2 = 10** (+1 PP new PROVED impl.) |
| 7 (2133) | 3/1/2/0 = 6 | **3/1/2/0 = 6** |
| 8 (2137) | 3/1/3/0 = 7 | **3/1/3/0 = 7** |
| total | 11/4/7/0 = 22 | **10/4/7/2 = 23**, + J7b-PP |

Branches: [χS], [χU] and [w] are all kept. The [w] branch (Z2) is still OPEN and is untouched by item 6, since T7 ≠ the SO(2)_R sector. The junction is UNSOLVED and the count gap is unchanged.

## 5. Fixes for NL's next erratum
- **H6-1** R1: state that the result is EOM-level only. A reduced-action derivation would need symmetric criticality, and Palais (compact H) does not apply.
- **H6-2** R1: add the 8th invariant 4-form vol(S²)∧dr∧dχ (closed). PP's exact count is Λ⁴ = 8, Sym² = 9.
- **H6-3** R4 script: use the full g_χχ = cos²χ/X_a + sin²χ/X_b (limits unchanged). State that the scope is the metric (G₄ regularity is a condition).
- **H6-4** R5: withdraw "k_{x,E} = √6/3 on the whole family / not an obstruction". Use a(C_w) = (√6/3)e^{−4(C_w−C₀)} and the Einstein proper-distance comparison. Record J7b as the necessary condition C_w − C₀ ≥ 7ln2/36 − ln3/12 (implication of N4). Note that C_w = C₀ fails.
- **H6-5** R6 script: B = C − ½ln6 (not +). The numeric minimum is 1.2443 at C−C₀ ≈ 0.582.
- **H7-1** st2 scripts: pass a fixed `v0` (or seed) to `eigsh`. The reruns differ in the 7th digit, so the logs are not byte-reproducible.
- **H7-2** S7-phase: drop "remaining eigenvalues positive" for n = 2, 3 Neumann (near-kernel cluster ≲ 4e-7). The grade rests on the identity.
- **H7-3** S7-a_t: phrase it as "the form depends only on α′ − a_t".
- **H7-4** Clerical: say "agree to 6 digits" (T=16 λ₁; n=3 λ₃).
- **H8-1** Q8-conf: add the Weyl-tensor argument (the orbit ratio alone covers only equivariant identifications).
- **H8-2** Q8-w script: fix the misleading "iff" prints, and add the converse.
