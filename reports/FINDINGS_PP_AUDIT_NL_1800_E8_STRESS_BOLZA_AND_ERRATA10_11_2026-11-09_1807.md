# FINDINGS: PP audit of NL 1800 (E₈ instanton stress on the odd HW wall; Γ = Bolza), NL erratum 10 (1736/erratum 7) and NL erratum 11 (1750); verification of OW 7ff8299d and OW 9bb1858c. 2026-11-09 (America/Chicago, CST)
Agent: Professor Proof (Soft SF). Additive new file; nothing edited. No CERT. No message sent. Nothing adopted. Only public arXiv API reads (citations CONDITIONAL). No Gemini. Lock 96f8d42e §4 not used. HOLD 587eca0c unchanged. b not fixed.
Tip: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, re-hashed: **MATCH (untouched)**.
Convention: K_ab = ∇_a n_b, k_t := −K(t̂,t̂), S_ab = −(2/κ²)(K_ab − h_abK) on the 10D Z₂ wall.

Targets (each equals its sidecar):
- (1) NL_DERIVED_E8_INSTANTON_STRESS_ODD_HW_WALL_BOLZA_2026-11-09_1800.md, sha 859328a2003242ca59109ffb699ba69995f4d5c9dec0055e49d16adc4e2d379d
- (2) NL_ERRATUM10_1736_E7_ACCEPT_PP_7f0ce656_2026-11-09_1801.md, sha 52424877cfb52b9dd0f8f5377ad611b6c7a5981007f9c150f2c677c4901c7ea4
- (3) NL_ERRATUM11_1750_ACCEPT_PP_bf4773a8_2026-11-09_1801.md, sha c2864c22f648196776045cb9de30223fdd29fa936f9d813001fb955e37ecd036
PP scratch: /workspace/audit-scratch/pp_1800_audit/ (sidecars written)
- e8stress_rerun.log 58438f89… and weight_rerun.log a90ef532… (byte-identical to NL logs)
- pp_1800_checks.py 82c0a358… / .log 020c5b7f… (Y3 with electric legs; excess recompute; Gauss–Bonnet; E₈ flat dims)
- arxiv_fbr.xml 9c5ebd95… (arXiv 1807.08367 metadata)

## Rollup
PROVED 44 · CONDITIONAL 11 · OPEN 3 · REFUTED 3 · PENDING 0 (61 graded items).
- **OW 7ff8299d is verified** (sha = sidecar, Owner words quoted below). It matches the relay: NL E₈ stress job, MR2 MN N=2 wall-boundary curvature job, Γ := Bolza adopted.
- **OW 9bb1858c is verified on disk** (sha = sidecar). It authorizes NL to pursue Y14, Y15 and the Y16 tr R² loophole. **It does NOT say "Y16 first"**: the items are numbered Y14, Y15, Y16, and Y16 is called "the only route that could change the junction verdict", with no ordering instruction. It records an Owner voice direction in paraphrase; it contains no verbatim Owner quote.
- **NL 1800:** the stress formula, sign, trace and Israel inversion are PROVED, and the NEC inequality K(ê,ê) ≤ k_t is PROVED for every field. **The equality K(ê,ê) − k_t = −(κ²/2λ²)|F(ê,·)|² holds only for magnetic fields** (F(t̂,·) = 0). "For any E₈ field" is REFUTED by counterexample, and the general form uses |F(k,·)|².
- The Y6 weight argument **survives the conformal-invariance check**. W is not a conformal factor of the fibre metric, so 4D conformal invariance cannot absorb it. It is PROVED for the stated weighted equation; its identification with the full HW wall equation is CONDITIONAL.
- **The excess (2489, 6510) is REFUTED as a rounding artifact.** The correct interval is (2492.1, 6506.7) M5 units for N_flux = 4880.
- Bolza: Γ1 and Γ5 are PROVED. Γ3's 496 is a real dimension. Γ2's genus-2 maximality is misattributed.
- **Erratum 10 applies all 13 fixes. Erratum 11 applies all 9.** NL's explanation of PP's 22 is right in substance but incomplete (§3).

## 0. Integrity and authority
- **I1 [PROVED].** All three targets equal their sidecars. /workspace/nl-junction-1754/: e8stress.py a4ce6d04…, e8stress_1758.log 58438f89…, weight.py 7c4f7008…, weight_1801.log a90ef532… all equal their sidecars.
- **I2 [PROVED].** Both scripts, rerun from scratch copies, are byte-identical to the NL logs.
- **I3 [PROVED].** Tip MATCH.
- **I4 [PROVED] OW 7ff8299d.** OWNER_WRITE_MAINCHAT_t4377_QUEUE_JOBS_NL_E8_STRESS_MR2_WALL_CURVATURE_BOLZA_GAMMA_2026-11-09_1753.md, sha 7ff8299dbcaf3b526936b40a9e24d8b9e58edf13fd9a9a93e822a92ca82a16ac = sidecar. Owner own words (widget t4377s18163): "As mine: approve both queue jobs (NL E₈ instanton stress-energy, MR2 wall-boundary curvature for MN N=2) and adopt Bolza for Γ. Nothing else from the pasted text."
  - Adopted: (1) the NL job, E₈ instanton stress on the odd-G₄ fixed plane, including non-BPS existence (OPEN), with no source, b or vacuum adopted; (2) the MR2 job, MN N=2 wall-boundary curvature with localized E₈ energy, checking whether the 11D invariants stay bounded, with no vacuum adopted; (3) Γ := Bolza (genus 2), with the systole claim pending PP's audit of 9ab8f0a6.
  - Not adopted: DP-a rejection, minimal joint carrier, "5:02 PM baseline", "5/3 gradient", b solved dynamically, Warden lock, strategy map.
  - Unchanged: vacuum HOLD 587eca0c.
  - NL 1800's authority lines match this record.
- **I5 [PROVED] OW 9bb1858c on disk.** OWNER_WRITE_VOICE_11fd320e_PURSUE_NL_E8_OPEN_PATHS_Y14_Y15_TRR2_NEC_2026-11-09_1805.md, sha 9bb1858ce34ee985d18d5a1db3ca838f20e2fddab741d7732e970e1e354ff27c = sidecar. It is an Owner voice direction recorded in paraphrase: "pursue every open path in NL 1800 (859328a2…) to resolution".
  - 1. Y14: non-BPS existence on the squashed, twisted, weighted fibre, via U(1)² cohomogeneity-2 reduction, min-max with the weight, and end-face numerics.
  - 2. Y15: the fibre Israel equations with the traceless stress.
  - 3. Y16 loophole: the stress of the −½tr R² wall term, and whether it can violate K(ê,ê) ≤ k_t.
  - Also: track MR2's jobs and PP's gate audit of 9ab8f0a6. Unchanged: HOLD, Γ = Bolza, no CERT.
- **I6 [REFUTED, by quotation] "Y16 first".** The record has no priority instruction. It lists Y14, Y15, Y16 in that order and only notes that Y16 is the one route that could change the junction verdict. Any "Y16 first" ordering is an agent reading, not Owner text.
- Compliance note (not graded): NL says its Y12/Γ2 titles were checked via DOI/PMC/AMS and Wikipedia. Those are outside the arXiv-only read allowance. This is flagged for the Owner; the affected citations are treated as CONDITIONAL and unverified here.

## 1. NL 1800
- **Y0 [PROVED].** Trace: S = (18/κ²)K ⇒ K = κ²S/18. K_ab = hK − (κ²/2)S_ab = −(κ²/2)(S_ab − hS/9). S(k,k) = −(2/κ²)K(k,k) for null k.
- **Y1-stress [PROVED].** For L = −(1/4λ²)√h tr F² with tr positive-definite, T_ab = −(2/√h)δS/δh^{ab} = (1/λ²)tr(F_acF_b^c − ¼h_abF²). Then T_tt ≥ 0 (correct sign), and the 10D trace is (1 − 10/4)|F|²/λ² = −(3/2λ²)|F|² (correct). The trace normalization only rescales λ².
- **Y1-HW [CONDITIONAL, HW 9603142].** λ² = 2π(4πκ²)^{2/3}, so λ⁶ ∝ κ⁴ (consistent with 1750's λ² ∝ κ^{4/3}). The coefficient and its later revisions are CONDITIONAL.
- **Y2 [PROVED].** x-block −ρη with ρ = |F|²/4λ²; Σ and fibre blocks (1/λ²)|F(ê,·)|² − ρ; trace −4ρ + 4ρ − 6ρ = −6ρ, consistent with Y1.
- **Y3-ineq [PROVED].** For a static face K(t̂,ê) = 0, so K(k,k) = K(ê,ê) − k_t for k = t̂ + ê. Then Y0 gives K(ê,ê) − k_t = −(κ²/2)S(k,k) = −(κ²/2λ²)tr|F(k,·)|² ≤ 0. F(k,·) ⊥ k, so it is spacelike or null. This holds for every E₈ field. With M5s present, add S_M5(k,k) ≥ 0.
- **Y3-mag [PROVED].** If F(t̂,·) = 0 (purely magnetic), |F(k,·)|² = |F(ê,·)|², giving NL's formula. Checked to residual 3.6×10⁻¹⁵.
- **Y3-general equality [REFUTED, counterexample].** "For any E₈ field" fails with electric legs. Take E = F_{t1} ≠ 0 with F_{e1} = F_{te} = 0. Then S(t̂,ê) = 0, which is compatible with a static face, but |F(k,·)|² = |F(ê,·)|² + E₁². Random fields give deviations up to 42.8 (pp_1800_checks.log (1)). The inequality is unaffected.
- **Y4-end [PROVED given J1]; Y4-int [CONDITIONAL].** The fibre-NEC deficit needs K(fib) > k_t, which Y3-ineq forbids for any E₈ field, BPS or not.
- **Y5 [PROVED].** S_wv = −ρh (6 directions), S_fib = 0, S = −6ρ ⇒ K^wv = κ²ρ/6, K^fib = −κ²ρ/3, ratio −2 = B0a (weight.py, reproduced).
- **Y6-math [PROVED, for the stated equation].** The 10D wall action, restricted to fields that live on the fibre (legs and dependence), is ∫ W tr F∧⋆₄F with W = √|h_{tx}|·√h_Σ = c_x²c_Σ = Δ̃e^{4f+2g}, giving D(W⋆₄F) = 0. For SD F, Bianchi gives dW∧F = 0, which on a constant face is dΔ̃∧F = 0. If v∧F = 0 with v ≠ 0, F is decomposable, so F∧F = 0; but F∧F = |F|²vol for SD F, so F = 0 (rank 3 reproduced).
  - **The conformal-invariance worry is resolved.** 4D YM and self-duality are invariant under rescaling g₄, which is why the fibre metric's own Δ̃^{-2/3} factor drops out. But W is not a rescaling of g₄: it is the volume density of the other six wall directions multiplying the 4D Lagrangian. Since ⋆₄ on 2-forms is conformally invariant, no choice of g₄ can absorb W. ∫W tr F∧F is not topological for non-constant W, so SD fields are not automatically critical, and the claim survives.
  - Strengthening: the critical set of Δ̃|_{S⁴} (points and circles; S³ at μ₀ = 0 for MN1) has empty interior. A smooth static SD field therefore vanishes **identically**, and BPS instantons appear only at zero size.
- **Y6-phys [CONDITIONAL].** That D(W⋆F) = 0 is the full wall equation needs: (i) a constant face (on non-constant faces dW picks up df and dg); (ii) the field living on the fibre; (iii) neglect of the HW wall couplings of C₃/G₄ to tr F∧F and of the tr R² term (cf. Y16). NL labels it PROVED given J1; it should be split this way.
- **Y7 [CONDITIONAL]. Y8 [CONDITIONAL]** (its p₁ step is PROVED, as in 1750 E1). **Y10 [CONDITIONAL].** Agreed.
- **Y9 [PROVED].** If F∧F has Σ legs, its restriction to S⁴_fib vanishes, so it does not enter N_M5 + n_inst. Its stress obeys the NEC (Y3-ineq). As defined, a Σ-wrapped field with pure-fibre F∧F components would count.
- **Y11 [PROVED].** W > 0, so ∫W|F|² ≥ W_min∫|F|² ≥ W_min·8π²|k| (normalization of Y8). The fibre stress is traceless (reproduced: 9×10⁻¹⁶, max|T_fib|/ρ = 0.77).
- **Y12 [CONDITIONAL].** SSU, PNAS 86 (1989) 8610; Sadun–Segert, Bull. AMS 24 (1991) 163; Taubes, JDG 17 (1982). The titles agree with PP's knowledge, but they are not arXiv-fetchable under the rule, so they remain unverified at title level here. Content as cited: non-SD SU(2) solutions on round S⁴ (charge 0 for SSU; C₂ ≠ ±1 for SS); Taubes' existence on manifolds with b₂⁺ = 0. **Y13 [CONDITIONAL]** BLS, PNAS 76 (1979) 1550, same note.
- **Y14 [OPEN]. Y15 [OPEN].** Agreed; now authorized by OW 9bb1858c.
- **Y15-arith [REFUTED, exact recomputation].** Excess = N_req − 2N_flux. With N_flux = 4880 (face.py's N), the lower ends are 2808.6 (MN2), 2492.1 (MN1), 3052.2 (z = 2) and 3182.4 (z = 3). The upper end is exact: 10N/3 − 2N = (2/3)·9760 = 6506.67. So the interval is **(2492.1, 6506.7)**, not (2489, 6510), which came from the rounded ratios 1.255 and 1.667. If instead N_b = 4880 is the stack (N_flux = 2440), everything halves: (1246.1, 3253.3). NL must say which.
- **Y16 [CONDITIONAL].** Agreed.
- **Γ1 [PROVED].** Every hyperbolic genus-2 metric is locally isometric to H², and the Israel data are local. N_b is a flux through S⁴, independent of area(Σ). Area = −2πχ = 4π (computed 12.566).
- **Γ2 [CONDITIONAL]** Systole 2 arccosh(1+√2) = 3.05714 (computed). Points to fix:
  - arXiv 1807.08367 (Fortier Bourque–Rafi, "Local maxima of the systole function", title verified) shows that Bolza is the unique L₁ ≈ 3.057 **local** maximum. Global maximality in genus 2 is Jenni (1984), which should be cited (CONDITIONAL).
  - The second length 4.8969 = 2 arccosh(3+2√2) is asserted, not derived.
  - GL(2,3), of order 48, is the orientation-preserving automorphism group; the full isometry group has order 96.
  - The curve is y² = x⁵ − x.
- **Γ3 [PROVED, dimension count].** Hom(π₁Σ₂, E₈)/E₈ at irreducible points has **real** dimension 2g·248 − 248 − 248 = (2g−2)·248 = 496. That equals complex dimension (g−1)·248 = 248 for semistable E₈^ℂ bundles (Narasimhan–Seshadri). These are the moduli of flat E₈ connections (Wilson lines) on Σ for the wall gauge field, not instanton moduli. 496 = 2·248 is correct.
- **Γ4 [CONDITIONAL].** 120n − 248: negative for n = 1, 2, and 112 for n = 3. Agreed.
- **Γ5 [PROVED].** Y₆ is the S⁴ bundle over Σ₂, the internal space of the wall (and of the flow at fixed r). Its structure group is connected, so it is orientable with trivial monodromy on H⁴(S⁴). The Euler class lies in H⁵(Σ) = 0, so the Leray–Serre/Gysin sequence degenerates with torsion-free ℤ coefficients. Betti numbers (1,4,1,0,1,4,1), χ = −4. **H₄(Y₆;ℤ) ≅ H²(Y₆;ℤ) ≅ ℤ** by Poincaré duality, generated by [S⁴_fib], the dual of the pulled-back point class of Σ. Correct.
- **Γ6 [OPEN].** Agreed.
- **T-1800 [PROVED].** 11/10/3/0 = 24 matches the item lists.

## 2. Erratum 10 (vs PP 7f0ce656 fixes 1–13)
- **X1–X13 [PROVED, each applied faithfully].**
  - Header 17 → 18. B0b convention and proof. B0d sign source and numerical-only routes. B2 premises, shrinking-circle step and strengthenings. B3 static. B5 narrowed.
  - C1 k_w. C2 scope (r_b(t) OPEN; r_b(μ) at z = 2, 3 upgraded). D2 general REFUTED, D2-const PROVED every z, region versions. D4 wording.
  - Erratum 7 fix 6 restated. N_req interval open at both ends. Erratum 7 disclosure 20/24/9/4 = 57, 7 unique OPEN items, double count.
- **X-T [PROVED].** The erratum's own 8/4/4/2 = 18 matches its list. 1736 corrected = 18/5/6/1 = 30. Erratum 7 strict = 20/24/9/4 = 57. The PP rollup is cited correctly as 33/6/6/2 after 724325dd.

## 3. Erratum 11 (vs PP bf4773a8 fixes 1–9)
- **Z1–Z9 [PROVED, each applied faithfully].** z = 3 (K2c, T1b); conjunction; K4 depends only on K5; L2-const/L2-inference with the wording fix; L3-alg/sources/conclusion; E3 caveat; E4 open interval; E5 traceless stress (pointing to 1800 Y15); header updated.
- **Z-T [PROVED].** Revised 1750 tally 11/16/4/0 = 31 is arithmetic-correct. Its CONDITIONAL (16) and OPEN (4) lists equal PP's item for item.
- **Z-22 [PROVED, confirmed with correction].** PP's PROVED 22 = 5 integrity (I1–I5) + 5 erratum-9 items (EF1–EF4, ET) + 1 tally item (T-1750) + 11 math items. NL omits the tally item. The 11 math items are not the same set as NL's 11: PP counts L2-const once (all z) plus E1-p₁ as a separate PROVED step, while NL splits L2a/L2b and folds the p₁ step into E1 (CONDITIONAL). The totals coincide by accident.

## NL fixes (additive erratum only)
1. Y3: state the identity as K(ê,ê) − k_t = −(κ²/2λ²)tr|F(k,·)|² with k = t̂ + ê, plus S_M5(k,k) if M5s are present. It reduces to |F(ê,·)|² only for magnetic fields (F(t̂,·) = 0). The inequality stays as is.
2. Y6: name the equation (the 10D wall YM equation for fibre-only fields, weight W = c_x²c_Σ). Note that W is not a conformal factor of g₄, so 4D conformal invariance does not remove it. Split Y6 into PROVED (math) and CONDITIONAL (constant face, fibre-only field, neglect of HW C₃–tr F∧F couplings and tr R²). Add that smooth static SD fields vanish identically.
3. Y15: replace (2489, 6510) with (2492.1, 6506.7) for N_flux = 4880. Give per-candidate lower ends (2808.6/2492.1/3052.2/3182.4) and the exact upper end (2/3)·9760. State whether 4880 is N_flux or N_b; if N_b, use (1246.1, 3253.3).
4. Γ2: cite Jenni (1984) for global systole maximality in genus 2; Fortier Bourque–Rafi gives the local-maximum statement. Derive or flag the second length 4.8969. Say "orientation-preserving Aut = GL(2,3), order 48 (full isometry group 96)".
5. Γ3: "real dimension 496 (complex 248), moduli of flat E₈ connections on Σ at irreducible points".
6. Γ5: write H₄(Y₆;ℤ) ≅ H²(Y₆;ℤ) ≅ ℤ·[S⁴_fib] (Poincaré duality; orientable since the structure group is connected).
7. Y1: record λ⁶ ∝ κ⁴, with coefficient and revisions CONDITIONAL.
8. Y12/Y13/Γ2: title checks via DOI/PMC/AMS/Wikipedia fall outside the arXiv-only allowance. Mark them as non-arXiv, unverified under the rule (CONDITIONAL), and flag this for the Owner.
9. Erratum 11 note: PP's 22 includes 11 non-math items (5 integrity, 5 erratum 9, 1 tally); the math item sets differ (E1-p₁; L2 split).
10. Any NL plan citing OW 9bb1858c: do not cite "Y16 first" as Owner text (I6).

Tip 7cddb188 untouched (MATCH). No CERT. No message sent. Nothing adopted. Y14–Y16 results not audited (not yet filed).
