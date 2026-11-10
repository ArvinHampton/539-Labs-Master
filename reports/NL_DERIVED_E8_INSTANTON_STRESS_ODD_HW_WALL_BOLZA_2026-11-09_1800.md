# NL DERIVED: E₈ instanton stress-energy on the odd-G₄ Z₂ fixed plane (HW-type wall), with Γ = Bolza
Author: Non Local Path (NL). Everything below is an **NL derived proposal**.

Authority:
- **OW 7ff8299d** (t4377, 17:53; sha verified): queue job NL E₈ stress, and Γ := Bolza.
  - Not adopted there: DP-a stays neutral; there is no 5/3 gradient (the shortfall is (1.255, 1.667), CONDITIONAL); b stays OPEN; no minimal joint carrier; no Warden lock.
- **OW f825dfff:** the face is a Z₂ fixed plane, with O1 odd and CONDITIONAL on P-b.
- The "odd case only" instruction is from Physicist's 17:46 relay, not Owner text.

Builds on:
- NL 1750 (4d9c9951) and erratum 9 (76ec4e75).
- PP 7f0ce656, with rollup erratum 724325dd. B2 is now PROVED; D2-general is REFUTED.
- PP bf4773a8, whose points E3, E4, E5 and L3 are applied here.

Limits:
- HOLD 587eca0c: no vacuum adopted. No source and no b adopted.
- No MR2 curvature numbers. No CERT. No Gemini. No outside services: only public title checks.
- Tip 7cddb188 untouched.

Usage: 41.4% at the start and 41.7% at the halfway point.

Scripts, each with a sidecar, in /workspace/nl-junction-1754/:
- e8stress.py (a4ce6d04…) and e8stress_1758.log (58438f89…)
- weight.py (7c4f7008…) and weight_1801.log (a90ef532…)

Conventions (PP):
- K_ab = ∇_a n_b, and k_t := −K(t̂,t̂).
- Wall stress S_ab = −(2/κ²)(K_ab − h_ab K), so ρ = (2/κ²)(k_t − K).
- The 10D wall is R^{1,3} × Σ × fibre; Y₆ = Σ ⋉ S⁴ (twisted).

## 1. Wall stress and junction
- **Y0 (PROVED, algebra).** Inverting the Israel condition on the 10D Z₂ wall:
  - K = κ²S/18, and K_ab = −(κ²/2)(S_ab − h_ab S/9).
  - For a null k, S(k,k) = −(2/κ²)K(k,k).
- **Y1 (CONDITIONAL, HW hep-th/9603142; title checked).** The E₈ wall action is −(1/4λ²)∫_wall √h tr F_abF^ab. HW print λ² = 2π(4πκ²)^{2/3}; later factor revisions exist and are not cited here. It couples through S_ab δ(wall) in the Israel condition. The resulting stress is
  - **S^YM_ab = (1/λ²) tr(F_acF_b^c − ¼ h_ab F_cdF^cd)**, with tr positive-definite on the fields.
  - Its trace is h^{ab}S_ab = −(3/2λ²)|F|². YM is not conformal in 10D.
  - What is used below holds in any normalization: the stress formula, and the fact that one minimal E₈ instanton carries one M5 charge.
- **Y2 (PROVED; e8stress log residual 0).** For a static, x-translation-invariant field with legs only on Y₆:
  - The x-block is S_μν = −ρ η_μν, with ρ = |F|²/(4λ²) ≥ 0. That is pure tension, w_x = −1, whether BPS or not.
  - The Σ block is (1/λ²)|F(ê_Σ,·)|² − ρ, and the fibre block is (1/λ²)|F(ê_a,·)|² − ρ.
  - The trace is −6ρ.
- **Y3 (PROVED; numerics: min S(k,k) = |F_a·|² identity, residual 2×10⁻¹⁵; random null k gives min T(k,k) = 1.26 > 0).** For any static face and unit spatial ê:
  - **K(ê,ê) − k_t = −(κ²/2λ²)|F(ê,·)|² ≤ 0.**
  - So E₈ always pushes toward the NEC side, K(ê,ê) ≤ k_t. (k_t = k_x only for Poincaré-invariant faces.)
- **Y4 (PROVED given J1, end faces); Y4-int (CONDITIONAL, interior numerics of 1711 E2).** The constant-r flow faces need K(fib) > k_t (fibre-NEC deficit). By Y3, **no E₈ field, BPS or not, can supply this.**

## 2. BPS (self-dual) case
- **Y5 (PROVED; weight.py).** Take a field that varies only along the fibre, has legs only on the fibre, and is self-dual with respect to the induced fibre metric.
  - Its fibre block is 0 and its mixed blocks are 0. The worldvolume (t, x, Σ) block is −ρh.
  - Y0 then gives K^wv = κ²ρ/6 and K^fib = −κ²ρ/3, ratio −2. That is exactly the smeared-M5 face (B0a).
  - Σ- or x-dependence would add worldvolume legs (PP).
- **Y6 (PROVED given J1, for vertical fields on constant faces; weight.py rank 3).**
  - The static wall equation is D(W ⋆₄F) = 0 on the fibre, with weight W = c_x²c_Σ = Δ̃e^{4f+2g}.
  - For self-dual F this reduces to d_fib Δ̃ ∧ F = 0.
  - A nonzero self-dual 2-form F in 4D cannot satisfy v∧F = 0 for v ≠ 0 (the linear system has rank 3).
  - So **a self-dual fibre field must vanish wherever d_fib Δ̃ ≠ 0.** Finite-size BPS instantons are not static solutions on flow faces where λ ≠ 0. They can only shrink to the critical loci of Δ̃.
- **Y7 (CONDITIONAL; Ganor–Hanany hep-th/9602120, Seiberg–Witten hep-th/9603003).** Zero-size E₈ instantons are M5s (the small-instanton transition). So the BPS sector reduces to the M5 template and adds nothing new.
- **Y8 (CONDITIONAL, HW).** Modified Bianchi identity: dG₄ = Σ δ⁵(M5) + δ¹(wall)∧(tr F∧F − ½tr R∧R)/(16π²), with tr normalized so that one minimal instanton gives 1.
  - Integrating over S⁴(r₊) − S⁴(r₋) in the odd case: **N_M5 + n_inst = 2N_flux**, where n_inst = (1/8π²)∫_{S⁴_fib} tr F∧F.
  - The tr R² term integrates to 0 because p₁(TS⁴) = 0 (PROVED in 1750 E1).
- **Y9 (PROVED, degree count).** Instantons on Σ-wrapped 4-cycles, e.g. the S²-subbundles over Σ, have F∧F with Σ legs, so ∫_{S⁴_fib} of it vanishes. They do not enter N_M5 + n_inst. They carry the G₄ component with Σ legs, like γ-leg M5s, and their stress is again NEC-obeying (Y3).
- **Y10 (CONDITIONAL; Y5 + Y7 + HW).** BPS instantons have tension per unit charge equal to that of an M5. **The count gap N_req/(2N_flux) ∈ (1.255, 1.667), open at both ends, is unchanged by n_inst.**

## 3. General (non-self-dual) case and existence
- **Y11 (PROVED).** Weighted Bogomolny bound: ∫W|F|² ≥ W_min ∫|F|² ≥ W_min · 8π²|k|.
  - A non-self-dual field has a nonzero, **traceless** fibre stress (e8stress: trace 9×10⁻¹⁶, max|T_fib|/ρ = 0.77). It therefore also enters the fibre Israel equations, not just the x equation (PP E5).
- **Y12 (CONDITIONAL, citations; titles checked via DOI/PMC/AMS).**
  - Sibner–Sibner–Uhlenbeck, "Solutions to Yang–Mills equations that are not self-dual", PNAS 86 (1989) 8610: infinitely many non-self-dual SU(2) solutions on round S⁴, charge 0.
  - Sadun–Segert, "Non-self-dual Yang-Mills connections with nonzero Chern number", Bull. AMS 24 (1991) 163: non-self-dual solutions on every SU(2) bundle over round S⁴ with C₂ ≠ ±1.
  - Via the SU(2) ⊂ E₈ embedding, non-BPS E₈ fields exist on the **round, unweighted** S⁴.
  - Taubes, "Self-dual Yang-Mills connections on non-self-dual 4-manifolds", JDG 17 (1982): self-dual solutions exist when b₂⁺ = 0, which holds for S⁴. That covers the squashed fibre for the unweighted problem only.
- **Y13 (CONDITIONAL).** Bourguignon–Lawson–Simons, "Stability and gap phenomena for Yang-Mills fields", PNAS 76 (1979) 1550: weakly stable SU(2) and SU(3) fields on round S⁴ are self-dual or anti-self-dual. So the non-BPS solutions of Y12 are unstable saddles. For general E₈ this is not covered.
- **Y14 (OPEN). Existence of static non-self-dual E₈ fields for the actual weighted problem** D(Δ̃ e^{4f+2g} ⋆F) = 0 on the squashed, twisted fibre.
  - Neither the conformal-invariance argument nor the equivariant ODE reduction of SSU and Sadun–Segert carries over, because the weight breaks conformal invariance.
  - The U(1)² fibre isometry still allows a cohomogeneity-2 reduction.
- **Y15 (OPEN). Can non-BPS energy close the count gap?**
  - At fixed charge 2N_flux = 9760 it needs an excess tension in (2489, 6510) M5 units, i.e. 25.5%–66.7% above BPS.
  - The same field must also satisfy the fibre Israel equations, which receive its traceless fibre stress.
  - Even if Y14 succeeds, the junction fails by Y4. **Non-BPS E₈ can at most close the count gap, never the fibre NEC.**
- **Y16 (CONDITIONAL; PP L3).** "Every wall source obeys the NEC" assumes the HW wall's −½tr R² term is dropped. That term is the same order in κ^{2/3} as tr F², and its stress is not NEC-guaranteed.
  - In the 1750 L3 terms, the NEC reads K(ê,ê) ≤ k_t. The "O(1) backreaction" claim stays CONDITIONAL, shown only near constant faces.
  - The 1736 D2 claim is restricted to constant faces (D2-general REFUTED by PP).

## 4. Γ = Bolza
- **Γ1 (PROVED).** The flow's Σ has constant curvature, so every junction quantity depends on Σ only through e^{2g}, the curvature normalization, and vol(Σ) = 4π(g−1) = 4π (Gauss–Bonnet at K = −1).
  - **Bolza changes none of the junction numbers** (N_req, the gap, the NEC margins) relative to any other hyperbolic genus-2 surface.
- **Γ2 (CONDITIONAL, citations).**
  - Systole 2 arccosh(1+√2) = 3.0571; the second length is 4.8969 (computed). Bolza is the systole maximizer in genus 2 (Fortier Bourque–Rafi, "Local maxima of the systole function"; title checked).
  - Curve y² = x⁵ − x, with Aut = GL(2,3) of order 48 (Wikipedia "Bolza surface", title checked; secondary source).
  - The systole enters only Wilson-line and KK gaps, not the junction.
- **Γ3 (PROVED, dimension count at irreducible points).** Flat E₈ connections on Σ: dim = 2g·248 − 248 − 248 = 496 for g = 2. Aut(Bolza) acts on this space.
- **Γ4 (CONDITIONAL, index formula).** For E₈ instantons on the fibre S⁴, the virtual dimension is 4h^∨n − 248 = 120n − 248. Irreducible ones need n ≥ 3; n = 1, 2 are reducible embeddings.
- **Γ5 (PROVED, Gysin).** Y₆ is an S⁴ bundle over Σ₂ (Euler class in H⁵(Σ) = 0).
  - Its Betti numbers are (1, 4, 1, 0, 1, 4, 1), χ = −4, and H₄(Y₆) = ℤ·[S⁴_fib].
- **Γ6 (OPEN).** Moduli of Σ-wrapped instantons on the ruled surfaces P(L_i ⊕ O) over Bolza, via stable holomorphic bundles. This is not cited, and it does not enter the fibre count (Y9).

## 5. OPEN items: resolution path and ETA
| item | what resolves it | ETA |
|---|---|---|
| Y14 | Cohomogeneity-2 reduction under U(1)²; a min-max (SSU-type) argument with the weight; numerical relaxation on the end-face weights | 3–5 h |
| Y15 | Given Y14, solve the fibre Israel equations jointly with the traceless stress. The answer is bounded by Y4 regardless: it can never fix the NEC. | +2 h after Y14 |
| Γ6 | A stable-bundle count on P(L_i ⊕ O) over Bolza (Aut 48 equivariant) | 2 h; not needed for the count gap |

## Tally (header checked against the item lists)
| label | count | items |
|---|---|---|
| PROVED | 11 | Y0, Y2, Y3, Y4, Y5, Y6, Y9, Y11, Γ1, Γ3, Γ5 |
| CONDITIONAL | 10 | Y1, Y4-int, Y7, Y8, Y10, Y12, Y13, Y16, Γ2, Γ4 |
| OPEN | 3 | Y14, Y15, Γ6 |
| REFUTED | 0 | — |

Check: 11 + 10 + 3 + 0 = 24.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
