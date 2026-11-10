# NL DERIVED: odd-parity HW-wall face — μ-dependent and time-dependent faces, nonlinear localization, and the E₈ wall sector (MN2, MN1, BBBW z=2; N = 4880, g = 2)
Author: Non Local Path (NL). Everything below is an **NL derived proposal**.
Authority and scope:
- **OW f825dfff** (t4369, 17:45; sha verified): the face is a Z₂ fixed plane (an HW-type wall). O1 is odd per PP 544fc7b0, PROVED given P-b and therefore CONDITIONAL on P-b. The E₈ wall sector and n_inst are CONDITIONAL. f825dfff contains no NL assignment.
- **The instruction to work the odd case only and drop the even branch comes from Physicist's 17:46 relay, not from Owner text.**
- OW ff8a1670 (pursue to resolution). HOLD 587eca0c: no vacuum adopted. No source and no b adopted.
Builds on:
- NL 1655, errata 5, 7 and 8, 1711, 1713, 1736.
- 1736 §B–§D is still pending PP audit, so results that use 1736 B2 are marked CONDITIONAL on that audit.
Limits: no MR2 numbers. No CERT. No outside services; only arXiv metadata was read. Tip 7cddb188 untouched.
Weekly usage: 39.7% at the start and 40.2% at the halfway point, both below 90%.
Scratch: /workspace/nl-junction-1746/, each file with a sidecar:
- checks.py and checks_1750.log
- arxiv_titles_1747.txt, from the export.arxiv.org API at 17:48, with arxiv_raw.xml

Twisted circles per candidate:
- MN2, (p, q) = (2, 0): φ₁ is twisted, φ₂ is untwisted (F₂ = 0).
- MN1, (1, 1), and BBBW z=2, (3, −1): both are twisted.

Notation: Q = (1+z)e^{−2λ₁} + (1−z)e^{−2λ₂}, so g′ − f′ = ⅛e^{f−2g}Q.

## 1. μ-dependent static faces with no attained minimum
- **K1 (PROVED; sympy residual 0, checks_1750.log). Σ Killing lift.**
  - Take a face that is independent of σ and of every twisted φ_i. It may depend on x, μ and untwisted φ.
  - At any point p, the local H² isometries ξ lift to 11D Killing fields that preserve A_i. The field η = ξ − A_p(ξ)∂_φ is Killing, tangent to the face, and equal to the horizontal lift F at p.
  - So K(F̂,F̂) = ½n(ln c_Σ). This extends PP's r_b(μ) check to faces that also depend on x and μ.
- **K2a (PROVED given J1 for MN2 and MN1); K2b (CONDITIONAL for BBBW z=2, on the numerical min Q = 2.000). Σ-vs-x no-go without any minimum.**
  - Take any face independent of σ, of the twisted φ's, and of at least one x^α, which may be t.
  - Worldvolume umbilicity (B0a) requires K(F̂,F̂) = K(x̂_α,x̂_α).
  - By K1 and B0b, both sides are ½n(ln c). So the condition is n(ln(c_Σ/c_x)) = 2n^r(g′ − f′) = 0. Here c_Σ/c_x = e^{2(g−f)} has no μ dependence, and n^r > 0 for a graph.
  - That contradicts Q > 0.
  - **This closes item (1) for every μ-dependent static face that does not depend on σ or on a twisted φ, with or without a minimum.**
- **K4 (CONDITIONAL on uniform C² bounds for x-translates and on PP's audit of 1736 B2). The remaining class.** These are faces depending on μ *and* on σ or a twisted φ, with no attained minimum.
  - Take a sequence of points whose radius tends to inf r_b, and translate each by an x-isometry.
  - If the translates converge in C² to a limit face, the limit solves the same Israel system (x-translations are symmetries) and attains its minimum. B2 then excludes it.
- **K5 (OPEN).** Two gaps remain.
  - The a-priori C² estimates. The Israel system for a spacelike-normal graph is of mean-curvature type, so Schauder or Ecker–Huisken-type bounds are the candidate route.
  - The degenerate case inf r_b = r*, where the face runs into the throat and there is no limit face.

## 2. Time-dependent faces r_b(t, …)
- **T1a (PROVED given J1 for MN2 and MN1); T1b (CONDITIONAL for BBBW z=2, on Q numerics).**
  - Take a face independent of σ, of the twisted φ's, and of one spatial x^α. It may depend on t, the other x's, μ and untwisted φ.
  - The K2 argument goes through with ∂_{x^α} as the Killing worldvolume direction. A timelike graph face has a spacelike normal with n^r > 0. **No solution.**
- **T2 (PROVED given J1, every z).**
  - Take a face independent of μ, of φ_i (φ₁ if z ≥ −1, φ₂ if z ≤ 1), and of one spatial x^α. It may depend on t and σ.
  - The Killing identity on ∂_{φ_i} and ∂_{x^α} gives n^r(2f′ − λ_i′) = 0. That contradicts 1736 B0d (λ_i′ = 2f′ is impossible on the flow). **No solution.**
- **T3 (OPEN).** Two classes remain: faces that depend on all four x^a, and faces that depend on t and on both μ and (σ or a twisted φ).
  - There is no tangent Killing field in the right block and no extremum principle in Lorentzian signature.

## 3. Nonlinear localization
- **L1 (PROVED, algebra).** On the Z₂ wall, any open region with zero face stress must have K_ab = 0, i.e. be totally geodesic. Here zero stress means no M5s and no E₈ field stress.
- **L2a (PROVED given J1 for MN2 and MN1); L2b (CONDITIONAL for z=2).** Flow faces are nowhere totally geodesic, because k_Σ − k_x ∝ g′ − f′ ≠ 0. So any localized configuration is an O(1) deformation of the geometry, and a perturbative bound does not exist.
- **L3 (PROVED, algebra).** All admissible wall sources obey the NEC: M5s in any orientation (erratum 7, fix 3) and E₈ Yang–Mills (§4 E2).
  - So any backreacted IR-kept configuration must satisfy k_x ≥ k_a pointwise on its own face.
  - The flow faces violate this in the fibre directions. Backreaction must therefore reverse the sign of k_x − k_fib, which is an O(1) change in the fibre extrinsic curvature.
- **L4 (CONDITIONAL on the BPS property of M5s and small instantons).** Tension per unit charge is 1 however the source is localized. Localization cannot change the charge side, 2N_flux. The required tension N_req belongs to the unknown backreacted geometry.
- **L5 (OPEN).** The bound on the change in N_req, and whether a factor of 2.5–3.3 is reachable.

## 4. E₈ wall sector (odd case)
Citations, with titles verified on arXiv at 17:48 CST (all CONDITIONAL):
- Hořava–Witten hep-th/9510209, "Heterotic and Type I String Dynamics from Eleven Dimensions"
- Hořava–Witten hep-th/9603142, "Eleven-Dimensional Supergravity on a Manifold with Boundary"
- Ganor–Hanany hep-th/9602120, "Small E₈ Instantons and Tensionless Non-critical Strings"
- Seiberg–Witten hep-th/9603003, "Comments on String Dynamics in Six Dimensions"
- Freed–Harvey–Minasian–Moore hep-th/9803205, "Gravitational Anomaly Cancellation for M-Theory Fivebranes"
- Ohmori–Shimizu–Tachikawa 1404.3887, "Anomaly polynomial of E-string theories"

Results:
- **E0 (CONDITIONAL, HW 9603142).** The wall carries an E₈ vector multiplet with action ∝ (1/λ²)∫√h tr F², where λ² ∝ κ^{4/3}. The wall Bianchi identity is sourced by δ(wall)(tr F∧F − ½tr R∧R). At leading order the wall has no bare tension.
- **E1 (CONDITIONAL on HW for the wall term; the p₁ step is PROVED).** Integrated over the fibre S⁴: 2N_flux = N_M5 + n_inst. The ∫_{S⁴}tr R² term vanishes because p₁(TS⁴) = 0.
- **E2 (PROVED, algebra; random check in checks_1750.log, min T(k,k) = 2.57 > 0).** The YM stress T_ab ∝ tr(F_acF_b^c − ¼h_abF²) obeys the NEC: T(k,k) = |F(k,·)|² ≥ 0, because a vector orthogonal to a null k is spacelike or null.
  - **E2-end (PROVED given J1).** So E₈ fields cannot cure the fibre-NEC deficit at the end faces.
  - **E2-int (CONDITIONAL on the interior numerics of 1711 E2).** The same holds on interior faces.
- **E3 (PROVED, algebra; numerical |T| < 2×10⁻¹⁵).** A self-dual E₈ field (instanton) on the 4D fibre has zero fibre-block stress, and its worldvolume block is −ρh. That is exactly smeared-M5-like tension.
- **E4 (CONDITIONAL on GH/SW and the HW normalization).** A BPS small instanton has tension per unit charge equal to T_M5. Trading M5s for instantons keeps N_M5 + n_inst = 2N_flux and the tension fixed. **So the count gap N_req/(2N_flux) ∈ [1.255, 1.667) is unchanged by n_inst.**
- **E5 (CONDITIONAL on the Bogomolny bound ∫|F|² ≥ |∫tr F∧F|).** Non-self-dual E₈ energy raises tension above charge. At fixed charge it could close the *count* gap, given 25.5%–66.7% excess energy over the BPS value. But that stress obeys the NEC (E2), so the fibre-NEC deficit remains. **E₈ can close at most the count gap, never the junction.**
- **E5x (OPEN).** Whether static non-self-dual E₈ configurations exist on the warped, squashed fibre with the required profile.
- **E6 (CONDITIONAL, FHMM and OST).** An M5 stack at the HW wall is the E-string theory, and its anomaly polynomial is known and matched by inflow. This adds no condition on N beyond integrality. The wall anomaly fixes λ²/κ^{4/3} (HW).
- **E7 (CONDITIONAL, HW).** At leading order the wall adds no w < −1 stress of its own.
- **Verdict (CONDITIONAL; it follows from E2, E4 and E5).** The E₈ sector can neither close the junction nor cure the NEC/WEC deficit on constant faces: it is PROVED at the end faces and CONDITIONAL in the interior. It does not change the BPS count gap. Only non-BPS E₈ energy could close the count gap, and whether that exists is OPEN (E5x).

## 5. Status, resolution path and ETA
| item | status | what resolves it | ETA |
|---|---|---|---|
| (1) μ-dependent faces, no minimum | Resolved for faces independent of σ and twisted φ (K2). The remainder is CONDITIONAL (K4) or OPEN (K5). | C² a-priori estimates plus the r* case; PP audit of 1736 B2 | 1–2 h, then a 20 min audit |
| (2) time-dependent faces | Resolved when one spatial x is free and the face is independent of μ+φ_i (T2) or of σ+twisted φ (T1). The rest is OPEN (T3). | A Lorentzian or causal argument, or an explicit counterexample search | 2–4 h |
| (3) nonlinear localization | No perturbative bound (L1–L3). The bound is OPEN (L5). | A backreacted cohomogeneity ≥ 2 solution (numerical relaxation) | days |
| (4) E₈ wall | Cannot close the junction (E2 at the end faces PROVED; interior CONDITIONAL). The BPS count gap is unchanged (E4). Non-BPS existence OPEN (E5x). | Existence analysis of static non-self-dual E₈ fields on the warped fibre | 2–3 h for an existence analysis |

## Tally (header checked against the item lists)
| label | count | items |
|---|---|---|
| PROVED | 10 | K1, K2a, T1a, T2, L1, L2a, L3, E2, E2-end, E3 |
| CONDITIONAL | 13 | K2b, K4, T1b, L2b, L4, E0, E1, E2-int, E4, E5, E6, E7, the §4 verdict |
| OPEN | 4 | K5, T3, L5, E5x |
| REFUTED | 0 | — |

Check: 10 + 13 + 4 + 0 = 27.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
