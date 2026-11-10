# NL ERRATUM 22 — accepting PP e2f5f582 (audit of heavy-queue items 6, 7, 8) and PP aad209d2 (confirmation of Erratum 21)
2026-11-09, 2211 CST (America/Chicago). **NL derived proposal.** Additive only: no target file is edited. Authority: OW t4426 d5eaeef3 ("Pursue all open"); OW t4436 32881263 ("Let the math lead"; [χS], [χU] and [w] are kept as labelled branches unless a PROVED or REFUTED result drops one); the 90% usage stop is lifted per OW t4431 (record f700141d…). Nothing adopted. **Junction: UNSOLVED. Count gap: unchanged.**
Sources (sidecars OK):
- FINDINGS_PP_AUDIT_NL_HEAVY_6_7_8_2026-11-09_2155.md (e2f5f582482fb0b54f1ac62ed214bb8b3ccc32ee62b7e31cd185ad78e8d043b0)
- FINDINGS_PP_CONFIRM_NL_ERRATUM21_078b0b32_2026-11-09_2141.md (aad209d22aee391b6b4b3882d724dcb6362df4b6cd03528509c50c7270d73db3)

Targets (sidecars OK; none edited):
- NL_DERIVED_T7_REDUCTION_COMPLETENESS_REGULARITY_2026-11-09_2103.md (125bfda1…)
- NL_DERIVED_Y14_ST2_OFFBLOCK_STABILITY_2026-11-09_2133.md (49aed96d…)
- NL_DERIVED_Y14_Q0_OTHER_SYMMETRY_SADDLES_2026-11-09_2137.md (f996a6d5…)
- NL_ERRATUM21_ACCEPT_PP_3fa2e067_2252cafc_2026-11-09_2135.md (078b0b32…)

Scripts, new dated directory `/workspace/nl-e22-2203/`. Each `.py` sidecar was frozen before its run; each `.log` sidecar was written after the run (disclosed).
- e22_checks_2026-11-09_2203.py = 1f2ef5ada08f098e20ba00ec360aa762f4585f679cbef03313d4f373d10183fe, log b4c2325b6651648070baf12372ec9b32c68ba9a43ecd1f25fd196ed52f838610
- e22_st2_Tseq_phase_v0_2026-11-09_2203.py = fd277b44043f32ac108f28e4c81a318dcb1dae2bc70918dd321005e24cd4aef5, log 02f7bfe96d7019e17f7d2972fd83e68861510524bdc82894af3123fee6ac1f07
The 2109 and 2129 ST2 originals are not edited (6f0880c8…, b71d3c5b…). Cited, not copied: PP v2 `/workspace/pp-pushforward-2026-11-09/pp_pushforward_corrected_v2_2026-11-09_2144.py` = 87deaed2f5900e15c09d316a4c7dcf89027b7ef39c5b0b9faf3570d51e0c0a7e, log 3d26fbed24838cb4c092f0d5fe100af5fcbb646c83d60d983168124729fffcf1; PP `/workspace/pp-audit-heavy678/pp_heavy678_checks_2026-11-09_2155.py` = bf61cc56…, log 158aeaf9….
Limits: no CERT, no Gemini, nothing sent, no agent messaged. Naming per OW f1d167d1: where the algebra is named it is "resonant algebra" (it is not named in this file). Tip 7cddb188… checked before and after. PP's math was re-checked independently; no item was disagreed with.

**Tally: PROVED 2 · CONDITIONAL 0 · OPEN 0 · REFUTED 2 · total 4**
(E21-α, E21-β, the v2 citation, wording/scope fixes, the v0 rerun, and the J7a self-correction are hygiene and carry no label. Revised tallies of the target files are in §6 and are not re-counted as extra rows here, except J7b-PP, which is a new item, and the Weyl evaluation, which is the exact basis of the existing Q8-conf label and is not added to the 2137 roll-up.)

## 1. Erratum 21 bookkeeping (PP aad209d2): FAITHFUL, with E21-α and E21-β
Hygiene (no label). Erratum 21 remains FAITHFUL. Two bookkeeping fixes, no grade changes:
- **E21-α.** E21-4's flux derivation (the push-forward by t=cos²β and s=(1−x²)t, the v-substitution, the integrand −4v²(v²+3)/(v²+1)², the value −2, and k-independence) is **PP's exact derivation in 3fa2e067 §4 / pp_a2_flux_fix**, independently re-run by NL. The E21-4 heading "independently re-derived" is corrected to that attribution.
- **E21-β.** Each of the six E21 rows restates a result already graded in a target tally that E21 §8 itself revises (E21-1 = F9-b; E21-2 = R2-Y16; E21-3 = the exact sub-part of R2-UV; E21-4 = A2-flux; E21-5 = D6-2/3; E21-6 = D6-6). The 5/1/0/0 figure is accepted as that erratum's row count. **For any roll-up, its distinct new claims are 0/0/0/0.**
- **v2 citation (PP 87deaed2…).** The F=1/(1+s) line of pp_a2_flux_fix was a false negative of `simplify(lhs−rhs)==0`. The corrected v2 script uses the rigorous test **minimal_polynomial(R) = X−1** (independently confirmed: also minpoly(A_l/A₀)=minpoly(A_r/A₀)=X−1), and both sides equal **−2 + 2√2·log(1+√2)** exactly. The flux ∫_{S⁴}G₄(CGR)=−8π²/g³ is unaffected and stays PROVED on exact grounds.

## 2. Item 6 (2103): R1 split; R5 withdrawn; J7b-PP. Revised tally 4/2/2/2, plus J7b-PP
- **H6-1 (hygiene; R1a stays PROVED).** R1's consistency argument is at the **EOM level only**. Every h∈H is a symmetry of 11D supergravity, so E[Φ] is an H-invariant tensor whenever Φ is, and imposing the 11D equations on the invariant ansatz truncates nothing. Palais's compact-group theorem is not used and does not apply: H = Poincaré(1,3)×SO(3)×U(1)_{φ₁}×(PSL(2,ℝ) of H²) is non-compact, and PSL(2,ℝ) acts only locally on Σ=H²/Γ. The EOM are local, so that is harmless. R1 does **not** license deriving the (r,χ) equations from a reduced action (that would need symmetric criticality).
- **E22-1 (REFUTED, by counterexample; H6-2). ** The claim "the H-invariant 4-forms are spanned by [7]" is refuted. The isotropy-Lie-algebra kernel on T*=ℝ^{1,3}⊕Σ⊕S²⊕⟨dr,dχ,Dφ₁⟩, computed exactly over ℚ, has dimension **8**. The eight invariants are vol(ℝ^{1,3}), vol(Σ)∧vol(S²), vol(Σ)∧dr∧dχ, vol(Σ)∧dr∧Dφ₁, vol(Σ)∧dχ∧Dφ₁, **vol(S²)∧dr∧dχ**, vol(S²)∧dr∧Dφ₁, and vol(S²)∧dχ∧Dφ₁. The missing form **vol(S²)∧dr∧dχ** is H-invariant and lies outside NL's list. It is also closed: for any coefficient f(r,χ), df has only dr and dχ legs, so d(f vol(S²)∧dr∧dχ)=0; Bianchi does not remove it. The metric inventory is confirmed: dim Sym² = **9**. R1 is split: **R1a** (EOM-level consistency) stays PROVED; **R1b** (4-form list) is REFUTED. Nothing else in item 6 used the 7-term list.
- **H6-3 (hygiene; R4 stays PROVED, fibre metric).** With the full g_{χχ}=cos²χ/X_a+sin²χ/X_b, the cone ratios are **exactly 1** at both poles (independently re-derived). NL's script kept only one term of g_{χχ} at each pole; the dropped term vanishes there, so the limits are unaffected. The scope of R4 is the metric; G₄ regularity is a condition, not checked.
- **E22-2 (REFUTED, by counterexample; H6-4).** R5's claim that k_{x,E}=√6/3 "holds on the whole E8 wall family; not an obstruction; does not constrain C_w" is withdrawn. By the 1935 definition q:=Q e^{−4C}, and with Q fixed by the IR value q(C₀)²=24, one has **a(C_w)=(√6/3) e^{−4(C_w−C₀)}**, which equals √6/3 only at C_w=C₀. **Counterexample:** C_w=C₀−1 lies on the E8 family (e^{−2B_w}=6e^{−2C_w} holds for every C_w) and gives a=(√6/3)e⁴≈44.58>1, so the N4 inequality fails there. A second error: N4's monotone quantity is dA_E/dρ_E in Einstein-frame proper distance, dρ_E=e^s dy with s=(2B+4C)/3. Comparing y-derivatives and setting 1/L_{5,E}=1 is incorrect. In proper distance, **1/L_{5,E}=e^{−s₀}=(256/9)^{1/3}≈3.0526** (exact: 4·2^{2/3}·3^{1/3}/3; confirmed from B₀=−½ln4, C₀=−½ln(8/3)).
- **E22-3 (PROVED, as an implication of the N4 premise: NEC plus a 5D Einstein-scalar description; J7b-PP).** A singlet-toy wall solution requires
  a·e^{−s_w} ≤ e^{−s₀}  ⇔  **C_w − C₀ ≥ 7ln2/36 − ln3/12 ≈ +0.043228**
  (exact; independently re-derived). At C_w=C₀ it **fails**: 3.9565 > 3.0526. If one (incorrectly) compares y-derivatives, the condition is C_w−C₀ ≥ −ln(3/2)/8 ≈ −0.050683. Either way J7b **is** a constraint on C_w. It halves the scan line, and it is a necessary condition, not an existence result. E16-J7b is therefore not "discharged, not an obstruction". **PP self-correction, recorded:** PP's own J7a wording in 3982a4b8 ("A_E′=−a") is a y-derivative. Its sign is right, but the magnitude compared under N4 must carry e^{−s}.
- **H6-5 (hygiene; R6 stays CONDITIONAL).** The R6 script sign is fixed: **B=C−½ln6**, from e^{−2B}=6e^{−2C}, not B=C+½ln6. A new run (e22_checks) gives the numeric minimum **1.2443 at C−C₀≈0.582** (float, box-limited) with the correct sign, versus **1.966 at C−C₀≈0.348** with the old (wrong) sign. The analytic bound |Y−FP|≥1 uses only A′>0 and is unaffected. (The corrected number is 1.2443, not 1.966.)

R2, R3, R7, R8, R9: grades unchanged (R3's converse — real zeros of (1−e^{3w})e^{−2w} are {0} — is recorded under H8-2). The [w] branch is untouched: T7 keeps the full SO(3), so w is projected out; Z2 stays OPEN in the larger SO(2)_R sector.

## 3. Item 7 (2133): grades unchanged 3/1/2/0
- **H7-1.** The 2129 (and 2109) scripts called `eigsh` without `v0`, so ARPACK's random start made the logs not bit-for-bit reproducible (PP's reruns differed in the 7th digit; no claim depends on that digit). A new script, e22_st2_Tseq_phase_v0, passes a fixed `v0=RandomState(0).rand(n)` (normalized) to every `eigsh` call. The originals are not edited. The T-sequence agrees with 2129 to the printed digits; the n=1 Neumann λ₃,λ₄ differ in the 7th digit, as expected from a changed start vector. No claim is changed.
- **H7-2.** For n=2 and n=3 the Neumann phase spectrum has a near-kernel cluster ≲4×10⁻⁷ (n=3: −1.09e-8, 1.5e-11, 9.9e-10, 1.9e-8; confirmed in both 2129 and the v0 rerun). The phrase **"remaining eigenvalues are positive" is dropped** for n=2,3 Neumann. The S7-phase grade stays **PROVED**, resting on the identity E[h e^{iα}]−E[h]=∫A h²(α′)² with **A=sW/g_{tt}>0 exactly** on (0,∞): independently, g_{tt}=(X_a sinh²t+X_b)/(X_a cosh²t), g_{φφ}=X_b sinh²t/X_a, W=(X_a sinh²t+X_b)/cosh²t, each a ratio or sum of positive terms for t>0 and X_a,X_b>0, so A=W√(g_{φφ}/g_{tt})>0. The numbers remain a check only.
- **H7-3.** S7-a_t is reworded: a_t **"enters only via α′−a_t"**. The quadratic form depends only on that combination, so it is ≥0 with or without gauge fixing. Grade unchanged (PROVED).
- **H7-4.** Clerical: the 2109 and 2129 T=12/16, n=1 values **"agree to 6 digits"** (T=16 λ₁ is 1.068515e-06 in 2109 vs 1.068514e-06 in 2129; n=3 λ₃ is 2.427642e-04 vs 2.427643e-04). S7-T stays CONDITIONAL. S7-off and S7-w stay OPEN. S7-χ stays PROVED (scope): the fibre operator does not see the wall smearing; both [χS] and [χU] are kept.

## 4. Item 8 (2137): grades unchanged 3/1/3/0
- **E22-4 (PROVED; exact; H8-1).** The orbit-ratio g_{φ₁}/g_{S²}=(X_b/X_a)tan²χ is a conformal invariant only under maps that preserve the SO(3)×U(1) orbit identification, so on its own it shows only that the *given* identification is not conformal. The gap is closed by the Weyl tensor of the fibre metric (T^{−1} block, coordinates (χ,φ,θ,ψ), g_{χχ}=cos²χ/X_a+sin²χ/X_b): W_{χφχφ}≡0 at X_a=X_b, and W_{χφχφ}≢0 for X_a≠X_b. At the MN2 IR, **W_{χφχφ}(χ=π/4)=2^{3/5}/18 ≠ 0** (independently re-derived; also W=0 at X_a=X_b, χ=π/4). So the MN2 IR fibre is **not conformally flat**, and hence not conformal to the round S⁴ under **any** diffeomorphism. The weight W=Δ̃ and the twist term remain independent obstructions. This is the exact basis of the existing Q8-conf PROVED label, not a new 2137 row. Q8-Witten, Q8-gap, Q8-SSU, Q8-w-ex and Q8-Bolza are unchanged.
- **H8-2 (hygiene).** The Q8-w script line "SO(3) isotropy … iff w=0: False" printed the generic non-identity, and "vanishes identically iff w=0: True" checked only the w=0 direction. The converse is added: the real zeros of e^w−e^{−2w} and of (1−e^{3w})e^{−2w} are **{0}** (independently re-derived). The same converse is recorded for R3. det T=1 and X_b/X_a=2 at MN2 stand. Q8-w stays PROVED (scope).

## 5. Branches
Under t4436, **[χS]**, **[χU]** and **[w]** are all kept. The [w] branch (Z2) stays OPEN and is untouched by item 6, since T7 is not the SO(2)_R sector. No branch is dropped.

## 6. Revised tallies of the audited files
| file | before | revised | change |
|---|---|---|---|
| 6, T7 completeness (2103) | 5/2/2/0 = 9 | **4/2/2/2 = 10**, **+ J7b-PP (PROVED, impl. of N4)** | R1 split (R1b REFUTED); R5 REFUTED; J7b-PP new |
| 7, ST2 off-block (2133) | 3/1/2/0 = 6 | **3/1/2/0 = 6** | wording, v0, "agree to 6 digits"; grades unchanged |
| 8, charge-0 saddles (2137) | 3/1/3/0 = 7 | **3/1/3/0 = 7** | Weyl argument is the exact basis of Q8-conf; converse added |
| heavy-queue roll-up | 11/4/7/0 = 22 | **10/4/7/2 = 23, plus J7b-PP** | |
| Erratum 21 (2135), roll-up | 5/1/0/0 (row count) | **0/0/0/0** distinct | E21-α, E21-β |

## 7. Junction / gap
No change. **Junction UNSOLVED; count gap unchanged.** Nothing adopted. D6 and Z2 stay OPEN. No item of PP e2f5f582 or aad209d2 was disagreed with.

## 8. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 2 | E22-3 (J7b-PP), E22-4 (Weyl value / non-conformal-flatness) |
| CONDITIONAL | 0 | — |
| OPEN | 0 | — |
| REFUTED | 2 | E22-1 (R1b 4-form list), E22-2 (R5 as stated) |

Check: 2 + 0 + 0 + 2 = 4.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
