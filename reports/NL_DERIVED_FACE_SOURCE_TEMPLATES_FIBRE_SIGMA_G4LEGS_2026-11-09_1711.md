# NL DERIVED: face stress-energy templates (fibre pressure, anisotropic Σ tension, G₄ legs) — MN2, MN1, BBBW, N = 4880, g = 2
Author: Non Local Path (NL). Everything below is an **NL derived proposal**. **No source is adopted. These are templates.**
Authority:
- OW 7b5a725b (t4350/t4352, 17:03): templates GO.
- OW 9a8ced02 (17:05): even parity is a candidate only; it can be locked only by a derivation.
- OW 48102805, OW f283cffd.
- HOLD aaadb280: no vacuum adopted; the candidates are shown side by side.
- O1 (the Z₂ parity of G₄) is **OPEN**. Every parity-dependent result below is given for both parities.
Builds on:
- NL 1655 (3cd6c8d3) plus erratum 5 (59218e61).
- PP audits 5cbd050a and cb4d26b0, including the PP lemma.
Limits: new file only. No MR2 numbers. No CERT. Nothing sent outside. Tip 7cddb188 untouched.
Scratch: /workspace/nl-junction-1705/
- templates.py (abe4a288…), with templates_full.log (67c7d2aa…). templates.log is identical to it.

## 0. Setup and conventions (inherited; PROVED given J1)
- Pairing: P3, the Z₂ orbifold with the IR side kept (the "IR-kept" case). Results for the UV-kept case are stated where they differ.
- Face: constant radius r = r_b. The face label is R_Σ(b)/R_Σ^IR, written R/R₀ below.
- Frame eigenvalues k_a are as in 1655 §3, with K = Σ k_a. The required total face stress is S^a_a = −(2/κ²)(k_a − K), with no sum.
- Required energy density: ρ = (2/κ²)(k_x − K) > 0.
  - Numerically, k_x − K > 0 on every sampled face (parity_lprime_full.log). At the two end faces it is analytic: 3|k_x| and 5|k_x|.
- Smeared M5 stack: ρ_M5 = σ_M5 = N_b T_M5 ρ(y), with P_x = P_Σ = −σ_M5 and P_fib = 0.
- Deficit (the required extra stress): Δ^a_a := S^a_a(required) − S^a_a(M5).
  - Δ_x = −(ρ − σ_M5)
  - Δ_Σ = −(2/κ²)(k_Σ − K) + σ_M5
  - Δ_{fib,a} = −(2/κ²)(k_a − K)
- Equation-of-state ratios of the required total stress: w_a := P_a/ρ = −(k_a − K)/(k_x − K).
- **T0 (PROVED given J1).** At the exact end faces:
  - IR end: w_Σ = w_fib = −4/3 (all four fibre directions).
  - UV end: w_Σ = −1, w_fib = −6/5.
  - Numbers on flow faces (averaged over the S⁴) are in the table below and templates_full.log.

| R/R₀ | MN2 w_Σ, w_fib(φ₁, φ₂, μ₋, μ₊) | MN1 w_Σ, w_fib | BBBW z=2 w_Σ, w_fib |
|---|---|---|---|
| 1.001 | −1.332, (−1.333, −1.333, −1.333, −1.333) | −1.332, (−1.333 ×4) | −1.332, (−1.333, −1.333, −1.333, −1.333) |
| 1.5 | −1.104, (−1.266, −1.223, −1.223, −1.250) | −1.122, (−1.252, −1.252, −1.240, −1.252) | −1.090, (−1.269, −1.208, −1.210, −1.248) |
| 10 | −1.002, (−1.202, −1.200, −1.200, −1.201) | −1.002, (−1.201, −1.201, −1.200, −1.201) | −1.001, (−1.202, −1.199, −1.200, −1.201) |

BBBW z=3 is similar; see the log. For general z the end values ±4/3, −1 and −6/5 are z-independent (T0), and only the interior interpolation depends on z.

## 1. Energy conditions of the required stress
For a face stress, NEC along a face null direction (t + a) reads ρ + P_a ≥ 0, which here is (2/κ²)(k_x − k_a) ≥ 0. WEC additionally needs ρ ≥ 0.
- **E1 (PROVED given J1, end faces).** In the IR-kept case:
  - Σ direction, IR end: ρ + P_Σ = (2/κ²)k_x < 0, so NEC is violated.
  - Fibre directions, both ends: ρ + P_fib = (2/κ²)k_x < 0 (k_x < 0 with the normal toward the IR), so NEC is violated.
- **E2 (CONDITIONAL, numerical; templates_full.log).** On every sampled flow face, every candidate, every μ and every fibre direction: (ρ + P_fib)/|ρ-scale| ∈ [−1.28, −0.78] < 0, so fibre NEC is violated. The Σ direction is also NEC-violating; its violation → 0⁻ toward the UV.
- **E3 (PROVED given J1).** In the UV-kept case all signs flip, so ρ < 0 and WEC is violated on every face. (This uses k_x − K > 0, which is analytic at the ends and numerical in between.)
- **E4 (PROVED, a bound on brane-like sources).** Take any superposition of positive-tension branes (M5, M2, or M5s wrapped in any directions, smeared or not).
  - Each brane i contributes ρ_i ≥ 0, P = −ρ_i along its worldvolume and 0 transverse.
  - So P_a ≥ −Σρ_i = −ρ, i.e. w_a ≥ −1, in every direction.
  - Required w_fib ≤ −1.2 < −1 (T0 at the end faces; E2 in between), so **no superposition of positive-tension branes can supply the required fibre stress** on an IR-kept Z₂ face.
  - Scope: exact at the end faces; CONDITIONAL on E2 for interior faces.

## 2. Templates
### (a) Fibre pressure: S^extra = diag(0_x, 0_Σ, p_{φ₁}, p_{φ₂}, p_{μ₋}, p_{μ₊})
- **A1 (PROVED given J1).** This absorbs exactly the fibre deficit, with p_a(r_b, μ) = −(2/κ²)(k_a − K) = w_a ρ. That is a fibre *tension*, since w_a ≈ −1.2 to −1.33.
- **A2 (PROVED given J1 for |z| ≤ 1; CONDITIONAL for z ≥ 2 on λ₂ ≥ λ₁ along the flow, which is numerical).** It leaves the Σ-vs-x mismatch unmatched.
  - The M5 needs k_Σ = k_x, i.e. g′ = f′.
  - But (A.15) gives g′ − f′ = ⅛e^{f−2g}[(1+z)e^{−2λ₁} + (1−z)e^{−2λ₂}].
  - This is > 0 for |z| ≤ 1, and for z ≥ 1 whenever λ₂ ≥ λ₁; numerically min(λ₂ − λ₁) ≥ 0 on every flow.
  - Fibre pressure plus M5 alone therefore has **no solution at any r_b**, and b is undefined for this source.
- **A3 (CONDITIONAL on E2).** NEC: ρ_ex = 0 and P_ex < 0, so NEC is violated for this source by itself.

### (b) Anisotropic Σ tension: S^extra = diag(0_x, −σ_Σ^ex h_Σ, 0_fib)
- **B1 (PROVED given J1).** It absorbs the Σ mismatch with σ_Σ^ex = (2/κ²)(k_Σ − k_x) evaluated at the face, i.e. ρ(w_Σ + 1), so the Σ tension exceeds the x tension.
- **B2 (PROVED at the end faces; CONDITIONAL in between, using 1655 res_fib ≥ 4).** It leaves the fibre components unmatched, because the M5 has zero fibre stress and k_fib ≠ K. So there is no solution by itself, and b is undefined.
- **B3 (PROVED).** NEC along Σ for this source: ρ_ex + P_ex,Σ = −σ_Σ^ex < 0, so NEC is violated.

### (a)+(b) combined, with M5 tension on x
- **AB1 (PROVED given J1).** Any diagonal, x-isotropic stress can be matched, so all components close at every r_b. The x equation is then the only one left involving the M5: N_b T_M5 ρ(y) = (2/κ²)(k_x − K) ⇒ **N_b = N_req(x)(r_b)**.
- **AB2 (CONDITIONAL, numerical monotonicity, 1655 P3c).** **b as a function of the source:** b = N_req(x)⁻¹(N_b), with exactly one solution when N_b ∈ [N_req^IR, 10N/3).
  - N_req^IR: 12568.6 (MN2), 12252.1 (MN1), 12812.2 (z=2), 12942.4 (z=3). The UV value 10N/3 = 16266.7.
  - Outside that range there is no solution. **N_b = 4880 has none.**
  - If the extra sources also carry x tension σ_x^ex, the relation becomes N_b T_M5 = (2/κ²)∫(k_x − K) − ∫σ_x^ex. In that case b is fixed only once the source's equation of state is given: w_source,a(r_b) = w_a(r_b) for each a.
- **AB3 (CONDITIONAL on E2).** The combined extra stress violates NEC (E4).

### (c) G₄ legs on or crossing the face (CLP (4.2), hep-th/9903214; legs CONDITIONAL on CLP)
- **G0 (CONDITIONAL on CLP (4.2)).** The 4-form has three kinds of legs:
  - (α) four fibre legs, tangent to the face, from the ε₇ terms;
  - (β) dr ∧ three fibre legs, crossing the face, from ★̄dX_α ∧ d(μ_α²), proportional to λ′;
  - (γ) Σ² ∧ two fibre legs, tangent, from d(μ_i²) ∧ Dφ_i ∧ ★̄F_i, proportional to the twist F_i.
- **G1 (PROVED given standard 11D sugra).** A finite jump of G₄ adds no δ-function to T_MN, which is quadratic in G. So G₄ legs feed S_ab only through face-localized sources: branes whose charge produces the jump, worldvolume H₃, or Chern–Simons-induced M2 charge.
  - Bianchi across the face: [G₄] = 2κ²T_M5 × (M5 charge density), with 2κ²T_M5 = (2π)³ℓ_P³ (PP).
  - The EOM d★G₄ = −½G₄∧G₄ + (M2 source): a jump in ★G₄ needs M2 charge on the face.
- **G2-odd (CONDITIONAL on O1 = odd).**
  - (α) jumps by 2N(2πℓ_P)³, so N_b = 2N_flux (integer, even).
  - (γ) jumps by 2·(γ), which needs extra M5s on ℝ^{1,3} × (a 2-cycle in the fibre spanned by μ_i, φ_i), smeared on Σ. Their charge ∝ the twist degrees (p, q) = (2,0) MN2, (1,1) MN1, (3,−1) z=2. The normalization is OPEN.
  - (β) is even and continuous: no constraint.
  - Their stress: tension on x and 2 fibre directions. It is brane-like, so E4 says it cannot reach w_fib < −1.
  - Charge vs tension: N_req(x)/(2N_flux) ∈ [1.255, 1.667] at every face. This is independent of N, so it holds whichever of {bulk flux, stack} is set to 4880.
  - Flux quantization: N_flux ∈ ℤ on each side, so N_b ∈ 2ℤ (4880 = 2 × 2440 is allowed).
- **G2-even (CONDITIONAL on O1 = even, and on CLP).**
  - (α) and (γ) are continuous, so the net M5 charge on the face is 0. That contradicts the Owner's brane ("stack of N wrapped M5s", N ≠ 0) unless M5–anti-M5 pairs are allowed.
  - (β) is odd, so it must flip sign across the face. Its jump is invisible to Bianchi (dr∧dr = 0), but it requires a jump in ★G₄ with legs x⁴Σ²(fib¹). That needs M2 sources whose worldvolume is three *fibre* directions, i.e. Euclidean, not static.
  - So a static even face needs (β)(r_b) = 0, i.e. λ₁′ = λ₂′ = 0 at r_b. Numerically this never happens at a finite face: min (|λ₁′| + |λ₂′|)/|f′| > 2×10⁻⁵ for R/R₀ ∈ [1.001, 100], with no sign changes; it → 0 only asymptotically at both ends (parity_lprime_full.log). CONDITIONAL, numerical.
- **G3 (PROVED given G0).** In both parities the G₄-leg sources are brane-like (E4). They cannot cure the fibre NEC deficit on an IR-kept face. Per source, b is undefined in the even case (no static face) and N_req⁻¹-type in the odd case (AB2 with N_b = 2N_flux): no solution, since the ratio is > 1.

## 3. Per-candidate summary (templates only; nothing adopted)
| candidate | N_req(x) IR→UV | w_Σ IR→UV | w_fib IR→UV | fibre NEC (IR-kept) | odd: N_req/(2N_flux) | even: static face |
|---|---|---|---|---|---|---|
| MN2 (z=1) | 12568.6 → 16266.7 | −4/3 → −1 | −4/3 → −6/5 | violated | 1.288 → 1.667 | none (λ′ ≠ 0) |
| MN1 (z=0) | 12252.1 → 16266.7 | −4/3 → −1 | −4/3 → −6/5 | violated | 1.255 → 1.667 | none |
| BBBW z=2 | 12812.2 → 16266.7 | −4/3 → −1 | −4/3 → −6/5 | violated | 1.313 → 1.667 | none |

General z: T0, E1, E3, E4, A1, B1, B3, AB1 and G1 are z-independent. A2 is analytic for |z| ≤ 1.

## 4. Open
- **X1 (OPEN).** A non-brane source with w_fib < −1 (NEC-violating, e.g. an orientifold-like negative-tension object or a quantum/Casimir term), and whether any exists in M-theory on this face.
- **X2 (OPEN).** The normalization of the (γ)-leg M5 charge in G2-odd.
- **X3 (OPEN).** O1 itself; see the derivation attempt in the JOB 2 file.
- **X4 (OPEN).** b. Here it is given only as a function, b = N_req⁻¹(N_b), or through equation-of-state matching. It is never fixed.

## Tally
| label | count | items |
|---|---|---|
| PROVED | 11 | T0, E1, E3, E4, A1, B1, B3, AB1, G1, G3, A2 for |z| ≤ 1 |
| CONDITIONAL | 10 | E2, A2 for z ≥ 2, A3, B2, AB2, AB3, G0, G2-odd, G2-even, the §0 sign k_x − K > 0 on interior faces |
| OPEN | 4 | X1, X2, X3, X4 |
| REFUTED | 0 | — |

A2 is split by z range and counted once in each row.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
