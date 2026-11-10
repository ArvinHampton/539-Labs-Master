# NL DERIVED: junction on non-constant faces, localized vs smeared M5s, and an attempt to derive the O1 parity — MN2, MN1, BBBW, N = 4880, g = 2
Author: Non Local Path (NL). Everything below is an **NL derived proposal**.
Authority:
- OW 7b5a725b (17:03): GO. Item B: non-constant faces and localized M5s, O1 OPEN.
- OW 9a8ced02 (17:05): even parity is a candidate only; it can be locked only by a derivation.
- OW 48102805, OW f283cffd.
- HOLD aaadb280: no vacuum adopted.
Builds on:
- NL 1655 (3cd6c8d3), erratum 5 (59218e61).
- PP 5cbd050a, including the lemma K = −2k_x with k_fib = −2k_x pointwise.
- PP cb4d26b0.
- Templates file NL_DERIVED_FACE_SOURCE_TEMPLATES_FIBRE_SIGMA_G4LEGS_2026-11-09_1711.md (53096d43…).
Limits: new file only. No MR2 numbers. No CERT. Nothing sent outside. Tip 7cddb188 untouched. **Neither parity is declared.**
Scratch: /workspace/nl-junction-1705/
- parity_lprime.py (48f25c60…), with parity_lprime_full.log (9d408e5b…). parity_lprime.log (d8c83ccc…) came from the first half of the script; parity_interior.log (1d772126…) is a tail-5 excerpt of the full log. Use the full log.
- pointwise_p3b_dedup.py (9c7541ea…), with pointwise_p3b_dedup.log (09446574…).
- templates.py (abe4a288…).

## A. Non-constant faces r = r_b(ξ)
Setup (NL0, PROVED given J1):
- Write the face as a graph: Φ := r − r_b(ξ) = 0, where ξ ranges over fibre coordinates (μ, φ_i), Σ coordinates σ, or x.
- Unit normal: n_M ∝ ∂_MΦ = (1, −∂_ξ r_b). Because the face is a graph, n^r = g^{rr}/|dΦ| > 0 everywhere.
- Induced metric: h = h(r_b(ξ)) + Δ̃^{1/3}e^{2f}(∂_ξr_b)(∂_ξ'r_b) dξdξ′. The second term is the radial tilt, added to the ξ block.
- Extrinsic curvature: K_ab = −n_M(∂_a∂_bX^M + Γ^M_NP ∂_aX^N ∂_bX^P). This is a second-order PDE in r_b(ξ).
- Lie-dragged directions: for any frame 1-form e^a among dx, e_Σ, Dφ_i with i_n de^a = 0 on the relevant vector, the diagonal entry is k_a = ½ n(ln c_a). This holds because:
  - dDφ_i = gF_i, F_i has Σ legs only, and F_i(n, ∂_φ) = 0;
  - the c_a depend only on (r, μ).
- Israel with pure smeared M5 (Z₂, either kept side; the condition is homogeneous in K):
  - On the worldvolume (x, Σ): K_ab − h_abK ∝ h_ab.
  - On the fibre: K_ab − h_abK = 0.
  - So every off-diagonal fibre–Σ entry must vanish as well.

Results:
- **NC1 (PROVED given J1 for |z| ≤ 1; CONDITIONAL for z ≥ 2 on λ₂ ≥ λ₁ along the flow, numerical). Faces r_b(μ, φ) that depend only on fibre coordinates: no solution, for any profile and any N_b.**
  - x and Σ stay Lie-dragged, so the worldvolume isotropy needs n(ln c_Σ/c_x) = 0.
  - c_Σ/c_x = e^{2(g−f)} depends on r only, so this is 2n^r(g′ − f′) = 0.
  - But n^r > 0, and (A.15) gives g′ − f′ = ⅛e^{f−2g}[(1+z)e^{−2λ₁} + (1−z)e^{−2λ₂}] > 0. This is strict for |z| ≤ 1; for z ≥ 1 it holds if λ₂ ≥ λ₁ (min(λ₂ − λ₁) ≥ 0 on every flow, templates_full.log).
- **NC2 (PROVED given J1, every z). Faces r_b(σ) that depend only on Σ coordinates: no solution.**
  - φ_i and x stay Lie-dragged, and n has no μ component. So k_{φ_i} = ½n^r∂_r ln c_{φ_i} and k_x = ½n^r∂_r ln c_x.
  - The PP lemma still holds: the Σ block equals k_x·h (worldvolume isotropy) and every fibre entry equals K, so K = 6k_x + 4K and K = −2k_x.
  - Then k_{φ_i} + 2k_x = n^r(2f′ − λ_i′) = 0 forces λ₁′ = λ₂′ = 2f′. That contradicts (A.15) exactly as in P3b, for z ≥ −1 via eq3 and for z ≤ 1 via eq4.
  - There is also an independent obstruction: K_{φσ} = ½c_φ g F_i(n, E_σ) ≠ 0 whenever n^σ ≠ 0 and F_i ≠ 0, while pure M5 needs K_{φσ} = 0.
- **NC3 (PROVED). The no-go in NC1/NC2 does not depend on N_b or on O1.** The Israel stress does not involve G₄. So it holds at N_b = 4880, at N_b = N_req (about 12.3k–16.3k), and at 2N_flux, for both parities.
- **NC4 (OPEN). Mixed profiles and x-dependent faces.** This covers r_b depending on both σ and fibre coordinates, and faces that depend on x (which break 4D Poincaré).
  - The Σ block then carries the Hessian ∇_σ∇_σ′ r_b.
  - The system to solve is the PDE above with S = −N_bT_M5ρ P^{wv}, i.e. the ten diagonal and the off-diagonal Israel equations.
  - No solution and no no-go is claimed.

## B. Localized vs smeared M5s
- **L1 (PROVED, algebra; CONDITIONAL on the harmonic M5 solution, Güven 1992).** Near a localized stack of N_b M5s:
  - ds² = H^{−1/3}dx₆² + H^{2/3}(dρ² + ρ²dΩ₄²), with H ≈ R³/ρ³ and R³ = πN_bℓ_P³.
  - A tube ρ = const has k_wv = 1/(2R) = 1/L₇ and k_Ω = 0, so K = 6k_wv.
  - This is exactly the UV end-face structure. There the PP lemma fails (k_fib = 0 ≠ −2k_x; P3a, PROVED).
  - So localization near the stack reproduces the AdS₇ end, which does not admit a pure-M5 face.
- **L2 (CONDITIONAL on distributional GR for codimension > 1 sources, Geroch–Traschen 1987).** A localized stack is codimension 4 inside the face and codimension 5 in 11D. It is not a thin-shell source. Israel needs S_ab to be a regular tensor on the face. The smeared ρ(y) is the S⁴-monopole (ℓ = 0) part of the localized source.
- **L3 (PROVED, Gauss law plus Bianchi).** The charge does not depend on localization: N_b equals the flux jump.
  - Odd parity: N_b = 2N_flux.
  - Even parity: N_b = 0.
- **L4 (CONDITIONAL on linearized backreaction and the decoupling of S⁴ harmonics ℓ ≥ 1 in the CLP truncation).** Localization changes the source only by ℓ ≥ 1 harmonics. At linear order these integrate to zero against dvol₄, so ∫(k_x − K)dvol₄, and hence N_req, is unchanged.
  - **Change in the N_b requirement: 0 at linear order.**
  - Reaching 4880 would need a factor of 2.51–3.33 in N_req, or 1.255–1.667 against the charge in the odd case. That is an O(1) change, not a small correction.
- **L5 (CONDITIONAL on the BPS property of a localized stack).** Tension = charge for the stack, so the mismatch in the odd case (N_req/(2N_flux) ∈ [1.255, 1.667]) persists. In the even case no net-charge BPS stack exists.
- **L6 (CONDITIONAL on NL 1620 N1).** A localized stack homogeneous on Σ must sit at μ₀ = 1 (MN1, BBBW) or on the arc μ₁ = 0 (MN2).
- **L7 (OPEN).** Nonlinear localization effects and the full backreacted localized face.

## C. Attempt to derive the O1 parity
Ingredients:
- 11D sugra with the CS term ∫C∧G∧G.
- The face Z₂ σ.
- Bianchi dG₄ = 2κ²T_M5 ★J_M5.
- EOM d★G₄ = −½G∧G.
- The flow's G₄ (CLP (4.2)).
Steps:
- **PD1 (PROVED given that σ is a symmetry of 11D sugra).**
  - The CS term is odd under orientation reversal, so invariance needs C₃ → s₁₁σ*C₃, where s₁₁ is σ's 11D orientation sign.
  - The orbifold condition is G = s₁₁σ*G.
  - Then the flux through the S⁴ at mirror radii obeys Φ(r′) = s₁₁s₄Φ(r), with s₁₁ = s_r s_x s_Σ s₄ and s_r = −1.
  - **So Φ is odd if and only if s_x s_Σ = +1**, i.e. σ preserves the orientation of the M5 worldvolume (x, Σ).
  - A pure radial reflection gives odd parity. A Z₂ that also reverses the Σ or x orientation gives even parity.
  - The Owner records do not specify σ's action on the internal directions.
- **PD2 (PROVED given the P3 pairing and Bianchi).** Net M5 charge on the face = (1 − ε_Φ)Φ. That is 2N_flux if odd and 0 if even.
- **PD3 (CONDITIONAL).** Conditions: (i) the face is a Z₂ orbifold (P3), not a two-sided gluing; (ii) the Owner's brane carries net charge N_b ≠ 0 with no anti-branes.
  - Under (i)+(ii), PD2 forces ε_Φ = −1 (odd), and PD1 then forces s_x s_Σ = +1.
  - Neither condition is on record, and pure-M5 P3 has no solution anyway. **So this does not lock a parity.**
- **PD4 (CONDITIONAL on CLP (4.2), a static face, and Lorentzian sources only).**
  - In the even case the crossing legs (dr ∧ fib³, proportional to ★̄dX_α ∧ d(μ_α²)) are odd. Flipping them needs Euclidean M2 sources. A static face therefore needs λ₁′ = λ₂′ = 0 at r_b.
  - Numerically this holds at no finite face: min (|λ₁′| + |λ₂′|)/|f′| ≥ 2.5×10⁻⁵ on R/R₀ ∈ [1.001, 100], with no sign change; it → 0 only asymptotically at both ends (parity_lprime_full.log).
  - In the odd case the tangent Σ legs (∝ F_i) jump. That needs extra M5s wrapping ℝ^{1,3} × a fibre 2-cycle, which is Lorentzian and allowed.
- **PD5 (PROVED given standard Bianchi in the bulk).** Along the flow Φ = N(2πℓ_P)³ is constant in r. For the pairings P1 and P2 (no Z₂) the parity is undefined, so O1 only matters for P3.
- **O1 grade: OPEN.**
  - No derivation forces a parity without premises that are not on record (σ's internal action; net charge across a Z₂).
  - Under PD3's conditions the result would be odd (CONDITIONAL). PD4 disfavours even for static faces (CONDITIONAL).
  - Even parity is **not** REFUTED, and odd parity is **not** PROVED.
  - Until PP audits this, every O1-dependent result stays given for both parities.

## D. Erratum 5 cosmetic fixes (PP cb4d26b0)
1. **Ranges.** In erratum 5 F3, read "impossible for **z ≥ −1**" (eq3) and "**z ≤ 1**" (eq4). The union is ℝ, with overlap [−1, 1].
2. **Gauge.** (A.15) is written in the gauge h = f. The condition λ_i′ = 2f′ is invariant under reparametrizing r and under the orientation of the normal. **E > 0 is not used**: only the exact cancellation of the E terms matters.
3. **Double counting.** pointwise_p3b.py concatenated the linspace grid with uv.t.
   - The deduplicated rerun, pointwise_p3b_dedup.py (9c7541ea…) with its log (09446574…), finds **distinct faces 3536 / 3427 / 3560 / 3579**. Each original count was one higher, because only the shared start point r = 1 was duplicated.
   - **Corrected minima (unchanged):** min |2f′ − λ₁′|/|f′| = 1.8934 (MN2), 1.9873 (MN1), 1.8481 (z=2), 1.8248 (z=3). min |2f′ − λ₂′|/|f′| = 2.0000, 1.9873, 2.0000, 2.0000.
   - This affects only the numerical cross-check. P3b stays PROVED given J1 (accepted by PP cb4d26b0).
4. **scan.log explanation.** PP marks it CONDITIONAL, because the original `tail -4` capture cannot be re-checked from disk. NL agrees.

## E. Correction to the 1711 templates file (additive note)
In B1, the Σ tension of the extra source should read σ_Σ^ex = −ρ(1 + w_Σ) = (2/κ²)(k_Σ − k_x). The first form there was printed with the wrong sign. The value is positive (w_Σ < −1), and the conclusions B1–B3 are unchanged.

## Tally
| label | count | items |
|---|---|---|
| PROVED | 8 | NL0, NC1 for |z| ≤ 1, NC2, NC3, L1 (algebra), L3, PD1, PD2, PD5 |
| CONDITIONAL | 9 | NC1 for z ≥ 2, L2, L4, L5, L6, PD3, PD4, D3 (dedup numbers, supporting), D4 (scan.log explanation) |
| OPEN | 4 | NC4, L7, O1, b (J6; never fixed) |
| REFUTED | 0 | — |

Note on counting: L1 is counted as PROVED for its algebra; its input solution is cited. NC1 is split by z range and counted once in each row. The PROVED row lists 9 names because PD5 was added after the count; the correct PROVED count is **9**.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
