# NL DERIVED: resolution pass — O1 parity, mixed and x-dependent faces, radial-profile ODEs, nonlinear localized M5s — MN2, MN1, BBBW, N = 4880, g = 2
Author: Non Local Path (NL). Everything below is an **NL derived proposal**.
Authority:
- OW ff8a1670 (t4358, 17:30): "pursue all to resolution".
- OW 9a8ced02: a parity can be locked only by a derivation **audited by PP**, never by declaration.
- OW 7b5a725b, OW 48102805, OW f283cffd.
- HOLD aaadb280.
Builds on:
- NL 1655, erratum 5, 1711, 1713.
- Erratum 7 (NL_ERRATUM7_FACE_SOURCES_NONCONSTANT_ACCEPT_PP_f3c5d73f_2026-11-09_1735.md, 130e2796…). All 11 PP fixes are applied there.
- PP 5cbd050a, cb4d26b0, f3c5d73f.
Limits: no vacuum, source or b adopted. **No parity is locked**; the result in §A awaits PP audit, and both parities stay recorded for every dependent result. No MR2 numbers. No CERT. Nothing sent outside. Tip 7cddb188 untouched.
Scratch: /workspace/nl-junction-1730/
- resolve.py (f6da8509…), with resolve_1736.log (39566c5e…).
- face.py and flowlin.py are copies identical to the audited 1646 versions.

## A. O1: the Z₂ parity of G₄
Premises:
- (P-a) The face pairing is P3: a Z₂ orbifold whose matching uses [K] = 2K. This formula needs the face to be **fixed pointwise** by σ. If σ acted on the face by a non-trivial isometry τ, the jump at y would be K(y) + K(τy), not 2K(y). In that case the 1655–1713 Israel algebra would not apply, and σ would no longer have the face as its fixed set.
- (P-b) σ is a symmetry of 11D supergravity, including the CS term ∫C∧G∧G.

Derivation:
- **A1 (PROVED given P-a).** σ restricted to the face is the identity, and σ acts as −1 on the normal. So s_x = s_Σ = s₄ = +1, s_r = −1, and s₁₁ = −1 (σ reverses orientation).
- **A2 (PROVED given P-b; this is the M-theory parity rule).** The kinetic terms are even under orientation reversal and the CS term is odd. So an orientation-reversing σ is a symmetry only if C₃ → −σ*C₃. There is no internal symmetry C → −C at fixed orientation, because the cubic CS term forbids it. This is the same rule as the Hořava–Witten orbifold (citation CONDITIONAL; the algebra here is self-contained).
- **A3 (PROVED given P-a and P-b; via PD1).** Φ(r′) = s₁₁s₄Φ(r) = −Φ(r). **The S⁴ flux, and every G₄ component tangent to the face, is odd. Components with one dr leg are even.**
- **A4 (PROVED given A3 and Bianchi).** N_b = [Φ]/(2πℓ_P)³ = 2N_flux, so the stack is its own image and its charge does not cancel. This is consistent with the "charge must not cancel against its image" requirement. That requirement is therefore a consequence here, not an extra premise.
- **A5 (PROVED given standard Witten quantization).** On the S⁴ fibre, TM|_{S⁴} = TS⁴ ⊕ (a trivial normal bundle pulled back from the base), so λ = p₁/2 restricts to p₁(TS⁴)/2 = 0. There is no half-integer shift, Φ/(2πℓ_P)³ = N_flux ∈ ℤ, and N_b ∈ 2ℤ. (4880 = 2·2440 is allowed as N_b; as the bulk flux it gives N_b = 9760.)
- **A6 (CONDITIONAL on Hořava–Witten 1996).** A 10D fixed plane of an orientation-reversing Z₂ in M-theory has a gravitational anomaly that must be cancelled by an E₈ vector multiplet living on it.
  - So P3 implies the face is an HW-type wall carrying E₈. That is an extra source not in the Owner's definitions.
  - Wall Bianchi: 2N_flux = N_M5 + n_inst, where n_inst is the E₈ instanton number on the S⁴. ∫_{S⁴}tr R² = 0 because p₁(TS⁴) = 0.
  - Small-instanton/M5 exchange is allowed (Ganor–Hanany, CONDITIONAL).
  - A self-dual E₈ instanton on the S⁴ fibre has stress like a smeared M5: tension along (x, Σ) and none along the fibre. It is brane-like and NEC-obeying, so by erratum 7 fix 3 it cannot cure the fibre-NEC deficit.
- **A7 (OPEN).** Full worldvolume anomaly inflow for an M5 stack *on* an HW wall, combining the FHMM inflow with the wall's E₈ sector. Not computed.
- **A8 (REFUTED, by A1–A3, within P3).** The claim tested is "within P3, with the face fixed pointwise, the S⁴ flux can be even". Given P-b it cannot.
- **A9 (PROVED, PD5).** Outside P3, i.e. in the two-sided gluings P1 and P2, σ does not exist and O1 is undefined.

O1 status:
- **Forced odd within P3**, given P-a and P-b (A3, PROVED given premises; A8 REFUTED for even).
- **The remaining Owner choice is whether the face is a Z₂ fixed plane at all.** If it is (P3), it is HW-type: O1 is odd, an E₈ sector is required (A6), and N_b = 2N_flux. If not, O1 has no meaning.
- Per OW 9a8ced02 nothing is locked until PP audits this. Every O1-dependent result elsewhere stays given for both parities.

## B. Faces that vary in more directions (pure smeared M5 source, Z₂)
Tools:
- **B0a (PROVED, algebra; extends the PP lemma to any face).** S = −σP^{wv} with Israel 2(K_ab − h_abK) = κ²σP_ab gives K_ab = −(K/2)P^{wv}_ab + K·P^{fib}_ab. The trace gives K = −2k_w with k_w := −K/2. So on every face, the wv block (x and the horizontal Σ lifts) is umbilic with eigenvalue k_w, and the fibre block is umbilic with eigenvalue −2k_w. No symmetry is needed.
- **B0b (PROVED; sympy check in resolve_1736.log, residual 0).** For any Killing field ξ tangent to the face, K(ξ,ξ) = ½n(|ξ|²).
- **B0c (PROVED).** At a critical point p of r_b (∂r_b = 0), K_ab(p) = K^{(0)}_ab(r_b(p)) − n_r Hess_ab(r_b), where K^{(0)} is the constant-face curvature (diagonal in the horizontal frame, PP F17) and n_r > 0.
- **B0d (PROVED given J1).** λ_i′ = 2f′ is impossible on the flow: for i=1 when z ≥ −1 (eq3 → −2e^{f+2λ₁} − (1+z)/8·e^{f−2g−2λ₁} < 0), and for i=2 when z ≤ 1 (eq4) (resolve_1736.log, sympy). The other λ′ is eliminated by eq1, so one circle alone suffices.
  - So 2f′ − λ_i′ has a fixed sign on the whole flow. It is **< 0**, since it equals −2/r at the IR end.
  - Numerical cross-check: max (2f′−λ₁′)/|f′| = −1.89 / −1.99 / −1.85 / −1.82.

Results:
- **B1 (PROVED given J1, every z).** Take any static face independent of μ and of φ_i, with i = 1 if z ≥ −1 and i = 2 if z ≤ 1. Its dependence on (x¹, x², x³, σ, φ_j) is arbitrary. No solution.
  - Both ∂_t and ∂_{φ_i} are tangent Killing fields. ∂_t is in the wv block and ∂_{φ_i} in the fibre block, since it is orthogonal to the horizontal lifts.
  - B0a + B0b give 0 = ½n(ln c_{φ_i}c_x²) = n^r(2f′ − λ_i′). Here ln(c_φc_x²) = 2ln μ_i − 2λ_i + 4f has no μ term because n^μ = 0.
  - n^r > 0 for graph faces, so this contradicts B0d.
  - This covers r_b(σ), r_b(x¹), r_b(σ, x), and **twisted-φ faces r_b(σ, x, φ_j)** for the circle j ≠ i.
- **B2 (PROVED given J1, every z). Minimum principle.** Take any static face, depending on anything (σ, μ, φ₁, φ₂, x¹, x², x³), whose r_b attains a global minimum. No solution.
  - At the minimum p, B0a and B0c in the directions (φ̂_i, any spatial x̂) give n_r[Hess(φ̂,φ̂) + 2Hess(x̂,x̂)] = n^r(2f′ − λ_i′) < 0 (B0d).
  - At a minimum the left side is ≥ 0. Contradiction.
  - **This includes every x-independent face**, since the internal space Σ₂ × twisted S⁴ is compact and the minimum exists. In particular it covers PP's twisted-φ case, where K(F₁,F₁) and K(F₁,F₂) ≠ 0 (erratum 7 fix 6) and the Lie-drag fails. The minimum principle does not use Lie-dragging of Σ.
- **B3 (PROVED given J1 for |z| ≤ 1; CONDITIONAL on Q > 0 numerics for z = 2, 3). Maximum principle, a second route.** If r_b is independent of one spatial x^α and attains a global maximum, then n_r Hess(F̂,F̂) = n^r(g′ − f′) > 0. At a maximum Hess ≤ 0, so there is no solution.
- **B4 (PROVED; combines NC3 with B1 and B2).** B1 and B2 do not depend on N_b or on O1. So there is no solution at N_b = 4880, at N_req, or at 2N_flux, in either parity.
- **B5 (OPEN).** The only static faces left are those that depend on μ, or on both φ's, **and** whose r_b attains no global minimum. Such a face must use the non-compact x directions, for example r_b → its infimum only as |x| → ∞.
  - The system is the 10D Israel PDE B0a with K_ab = −n_M(∂_a∂_bX^M + Γ^M_NP∂_aX^N∂_bX^P).
  - What blocks a proof: there is no extremum to evaluate at, and no tangent Killing field in the fibre block.
  - Candidate tools: an asymptotic analysis as |x| → ∞, where the face must approach a constant face, which B2 excludes in the limit. The limit argument needs a uniform-convergence lemma.
- **B6 (OPEN).** Time-dependent faces r_b(t, …). There is no tangent ∂_t, and the Hessian along t has indefinite sign.

## C. Radial-profile ODEs
- **C1 (PROVED, structure).** For a one-variable profile r_b(ξ), B0a gives ten diagonal equations plus off-diagonal ones for a single unknown function and a constant k_w. The system is overdetermined.
- **C2 (PROVED given J1; from B1–B3). Solution count: 0** for every one-variable profile.
  - ξ = x¹: B1.
  - ξ = σ, μ, φ₁ or φ₂: compact, so B2 applies.
  - This holds for every N_b, including **4880**, in both parities and for every candidate.
  - Existence and uniqueness are moot.
  - So numerical integration of the pure-M5 profile ODE is not meaningful, because there is no solution to integrate. resolve_1736.log records the sign data that the proofs use.
- **C3 (CONDITIONAL; template sources, 1711).** With the templates' fibre pressure and Σ tension added, the profile ODEs become **under**determined: the sources are free functions. b is then not determined without an equation of state. This is the same as AB2.
- **C4 (OPEN).** Two-variable PDE profiles in the class B5, for example r_b(x¹, μ) with no minimum.

## D. Nonlinear localized-M5 effects
- **D1 (PROVED, algebra).** On a Z₂ face, any open region with zero face stress must satisfy K_ab − h_abK = 0, so K = 0 and K_ab = 0 there: it is totally geodesic. A localized stack (stress only at y₀ on the S⁴) therefore needs K_ab = 0 on the face away from y₀.
- **D2 (PROVED given J1 for |z| ≤ 1; CONDITIONAL for z = 2, 3).** On the flow geometry no face point is totally geodesic, because k_Σ − k_x = n^r(g′ − f′) ≠ 0.
  - So a localized pure-M5 Z₂ face needs an **O(1) change** of the geometry everywhere on the face, not a perturbation of the smeared configuration.
  - The expansion parameter ε = (N_b/N_flux)^{1/3} is O(1) anyway: 1.26 in the odd case, N_b = 2N_flux.
- **D3 (CONDITIONAL on BPS-ness of the localized stack and on 5D zero-mode dominance at the face).** The BPS bound is topological, so tension = charge exactly for any localization. The required effective tension comes from the 5D zero-mode junction. The mismatch it must overcome is a factor of 2.51–3.33 versus N, or 1.255–1.667 versus the charge in the odd case.
- **D4 (OPEN; no rigorous bound).** The change in N_req from fully nonlinear localization. Massive KK modes feed the zero-mode junction only at second order, but with ε = O(1) that is not small.
  - Known localized solutions (Fayyazuddin–Smith; Lunin; M5s near HW walls; CONDITIONAL citations) give no closed form for this geometry.
  - Whether a factor of 2.5–3.3 is reachable is **OPEN**. D1/D2 show the localized pure-M5 Z₂ face is not a small deformation, so a perturbative bound cannot exist.

## Resolution path and ETA per item
| item | status now | what would resolve it | realistic ETA |
|---|---|---|---|
| (a) O1 | Odd forced within P3 (A3, PROVED given P-a/P-b); even REFUTED within P3 (A8); undefined outside P3. Not locked. | (1) PP audit of A1–A5 and A8. (2) An Owner decision on whether the face is a Z₂ fixed plane (P3), which makes it an HW-type wall with E₈ (A6). (3) The anomaly inflow on the wall (A7). | (1) 15–20 min of PP audit. (2) One Owner answer. (3) 1–2 h of literature-backed derivation. |
| (b) mixed and x-dependent faces | B1 and B2 PROVED given J1 (including twisted-φ and all x-independent faces). B3 partly CONDITIONAL. B5 and B6 OPEN. | B5: an asymptotic/uniform-convergence lemma reducing faces without a minimum to B2 at infinity. B6: a causal or maximum-principle argument for time-dependent faces. | B5: 30–60 min. B6: 1–2 h. Then a PP audit. |
| (c) radial ODEs | Solution count 0 for every one-variable profile, every N_b including 4880, both parities (C2, PROVED given J1). | Done for pure M5. The two-variable class (C4) is the same as B5. With template sources (C3), resolution needs an equation of state, which is an Owner choice. | Pure M5: done, pending PP audit (about 15 min). C4: with B5. |
| (d) nonlinear localization | D1 PROVED; D2 PROVED for |z| ≤ 1. A bound on δN_req is OPEN (D4). | A fully backreacted localized-M5 + Z₂ solution. This is a cohomogeneity ≥ 2 nonlinear PDE in 11D sugra (numerical relaxation), or a proof that the 5D zero-mode tension is protected (a BPS/Gauss argument for the junction, not just for the stack). | Protection argument: 1–2 h, uncertain. Full numerics: days, outside the current caps. |

## Tally
| label | count | items |
|---|---|---|
| PROVED | 17 | A1, A2, A3, A4, A5, A9, B0a, B0b, B0c, B0d, B1, B2, B3 (|z| ≤ 1), B4, C1, C2, D1 |
| CONDITIONAL | 5 | A6, B3 (z = 2, 3), C3, D3, D2 (z = 2, 3) |
| OPEN | 6 | A7, B5, B6, C4, D4, O1 lock (awaiting PP audit and the Owner's P3 choice) |
| REFUTED | 1 | A8 (even parity within P3) |

Splits: B3 and D2 are each split by z range. D2 for |z| ≤ 1 is PROVED and is counted with D1 under the PROVED row, which then holds **18** items:
- PROVED 18: the 17 listed plus D2 (|z| ≤ 1).
- CONDITIONAL 5.
- OPEN 6.
- REFUTED 1.
- Total 30.

Count check: A gives 6 PROVED + 1 CONDITIONAL + 1 OPEN + 1 REFUTED = 9. B gives 8 PROVED + 1 CONDITIONAL + 2 OPEN = 11. C gives 2 PROVED + 1 CONDITIONAL + 1 OPEN = 4. D gives 2 PROVED + 2 CONDITIONAL + 1 OPEN = 5. The O1 lock adds 1 OPEN. Sum: 9 + 11 + 4 + 5 + 1 = 30.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
