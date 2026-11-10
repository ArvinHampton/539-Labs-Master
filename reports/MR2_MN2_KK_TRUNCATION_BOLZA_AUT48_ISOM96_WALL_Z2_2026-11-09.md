# MR2: KK truncation of MN N=2 (N=4880, g=2, Γ = Bolza) under (A) Aut⁺(Bolza), order 48, and (B) Isom(Bolza), order 96, each combined with the wall ℤ₂
Written 2026-11-09, ~18:50 CST (America/Chicago), by MR2 (executor). New additive file; no existing file edited. Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md re-hashed 7cddb188ca34… (unchanged). No CERT, no Gemini, nothing sent outside.

**Authority (all sha-verified this run):**
- OW 49b04146… (t4398, 18:28): restrict the KK analysis to Bolza × wall-ℤ₂ invariant modes. This is a scope choice, not a result.
- OW 91e69b38… (t4400, 18:32): "Pursue both for possible resolutions". Run (A) and (B) and report where they differ. Which group is adopted is not decided.
- Auditor ADDENDUM3 a7de4ea83b89… (reports/bridges/AUDITOR/, sidecar MATCH), §1a. It flagged that "Bolza symmetries" does not name the group.
- Vacuum OW 19a88b19… (MN N=2, CONDITIONAL). Wall OW f825dfff… and MR2 wall file bd47ff5e…. Citation scope OW 36683379….
- Inputs used: MR2 7824e789… and 7c407fa5… (the (D) KK rule, for comparison only); NL 418e4e50… (with its log 30b89fb5…, sha MATCH); MR2 V2 .py ad134752… (metric, sha MATCH); MR2 ERRATUM2 7b9ebdaf….

**Scope statement, applying at every step.** Everything below is the **invariant sector only**, under the group named on each line. The full KK spectrum, including Wilson lines and spin structure, **stays OPEN**. Modes excluded by a truncation are not claimed absent.

## Files (reports/)
| file | sha256 |
|---|---|
| MR2_MN2_KK_TRUNCATION_BOLZA_AUT48_ISOM96_WALL_Z2_2026-11-09.py | 88949658116586c63dc4785fc31c222eed6d9ef44afbefbc6e40a4946b20b26c (chmod a-w and sidecar written **before** the run) |
| MR2_MN2_KK_TRUNCATION_BOLZA_AUT48_ISOM96_WALL_Z2_2026-11-09.log | a2d105e69f723604238ff3eed30664b41bd6d4f9c1d6e717542849f4389c253f (exit 0, 44 s) |
| this .md | see .md.sha256 |

## 0. Correction carried (per MR2 ERRATUM2 7b9ebdaf)
- **Bolza λ₁ = 3.8388872588…, with multiplicity 3** (Strohmaier–Uski arXiv:1110.2150 §5.3; multiplicity 3 per Cook arXiv:2108.11825 Thm 1.27).
- **3.8388976481 is the Kravchuk–Mazáč–Pal upper bound** over all genus-2 surfaces (arXiv:2111.12716). It is not the Bolza value; the two differ by 1.04e-5 (log [M]).
- The job brief's "λ₁ ≈ 3.8388976" is therefore the KMP bound. This file uses the Bolza value.

## 1. The two groups (log [G]). PROVED in-repo, except one cited lemma
- **Construction.** I built the group acting on y² = x⁵ − x from four generators: x → ix, x → (x+1)/(1−x) (both with their y-lifts), the hyperelliptic involution J: y → −y, and complex conjugation K. I let it act on H¹(Σ,ℝ) ≅ H^{1,0}, realified to 4×4 matrices, and on the 6 branch points.
- **Order of the closure.** The closure has order **96**: 48 holomorphic elements and 48 antiholomorphic ones. The action on H¹ is faithful (96 distinct matrices).
- **(A) = Aut⁺, order 48.** Its element-order statistics, {1:1, 2:13, 3:8, 4:6, 6:8, 8:12}, are identical to those of GL(2,3), which I enumerated directly. There are 8 classes, irreducible dimensions 1,1,2,2,2,3,3,4, and orthogonality holds to 4e-15.
  - Label: **PROVED** that |Aut⁺| ≥ 48 with these statistics. That |Aut⁺| equals 48 is **CONDITIONAL**: it rests on the cited lemma in PP c74b5a2d B-M16 (uniqueness of the hyperelliptic involution). Identifying the group as GL(2,3) is consistent with the order statistics and the character table; I did not build an explicit isomorphism, so that part is CONDITIONAL (Cook 2108.11825 §3).
- **(B) = Isom, order 96.** There are 13 classes. The irreducible dimensions are 1⁴, 2², 3⁴, 4³, and Σd² = 96. This matches SmallGroup(96,193) as quoted (Wikipedia "Bolza surface", GAP) and Cook's GL(2,3) ⋊ ℤ₂.
  - Character table: PROVED in-repo (Dixon's method, orthogonality to 3e-14). Equality |Isom| = 96: CONDITIONAL, as in B-M16.
- **J (hyperelliptic involution).** J is the unique element acting as −1 on H¹, and it is central in Isom. **PROVED.**
- **One-dimensional characters.**
  - Aut⁺ has 2: trivial and det.
  - Isom has 4: trivial, the orientation character (χ₃ in the log), and two lifts of det.
  - **PROVED** (character table).

## 2. Laplacian on Σ: invariant modes per level (log [T]). PROVED numerically (FEM + Richardson); identification PROVED
- **Method.**
  - Σ/Isom is the hyperbolic (2,3,8) triangle. Its area is π/24 = 4π/96 (FEM area 0.13089972 against exact 0.13089969). The triangle's angles and right angle were checked to 1e-12.
  - Each 1-dim character of Isom is a choice of Neumann (N) or Dirichlet (D) condition on the side through the π/8 and π/2 vertices (AB) and on the two sides at the π/3 vertex (AC = BC, forced by the order-3 relation).
  - So the **trivial-representation multiplicity** in an eigenspace is:
    - **(B) Isom:** the number of times λ occurs in the **NN** spectrum.
    - **(A) Aut⁺:** the number of times λ occurs in **NN ∪ DD**, because DD is the orientation character, which is trivial on Aut⁺.
  - The DN and ND spectra carry the det character of GL(2,3), so they are excluded in both scopes.
- **Validation.**
  - The first nonzero NN eigenvalue is 23.078559, against the Strohmaier–Uski value λ₈ = 23.0785584814 (multiplicity 1): relative difference **2.8e-9**.
  - None of the 1-dim spectra has an eigenvalue below 28.5 other than this one. That agrees with the SU list, where λ₁…λ₇ and λ₉ all have multiplicity ≥ 2. Cook identifies λ₁ as a 3-dim irreducible.
  - Control 1: the flat-metric NN control (102.4, 337.0, …) matches nothing, as required.
  - Control 2: λ₁ = 3.83889 is absent from all four 1-dim spectra, as required.
- **Invariant eigenvalues** (Richardson spread at most 1.6e-4 for the levels quoted):

| level | λ (hyperbolic, K = −1) | character | (A) Aut⁺ keeps | (B) Isom keeps |
|---|---|---|---|---|
| 0 | 0 | trivial | ✓ | ✓ |
| 1 | 23.078559 (= SU λ₈) | NN (Isom-trivial) | ✓ | ✓ |
| 2 | 74.92671 | NN | ✓ | ✓ |
| 3 | 116.60252 | NN | ✓ | ✓ |
| 4 | 169.20450 | NN | ✓ | ✓ |
| 5 | 222.37113 | **DD (orientation character)** | ✓ | ✗ |
| 6 | 256.69282 | NN | ✓ | ✓ |
| 7 | 306.68025 | NN | ✓ | ✓ |
| 8 | 387.14 / 394.58 | NN / **DD** | ✓ / ✓ | ✓ / ✗ |
- **Caveats on the table.**
  - The levels above 28.08 are FEM-only, not cross-checked against SU (I only had SU's first ten). They are **PROVED numerically** to the stated spread, with rigorous error bars **OPEN**.
  - For reference, the det-type levels excluded in both scopes are 32.674 (DN), 91.465 (ND), 120.44 (DN), ….
  - **Each invariant level is simple (multiplicity 1 in the invariant sector).** That is PROVED in the FEM sense: no near-degenerate pairs inside a BC type.
- **Literature identification of the action on the eigenspaces.**
  - λ₁ is a 3-dim irreducible and λ₂ is 4-dim (Cook 2108.11825 Thms 1.27–1.28; Cook flags a conjecture).
  - λ₈ = 23.0786 is the trivial representation: PROVED here by the NN match.
  - The full irreducible label of every higher-dim eigenspace is **OPEN**. It isn't needed for invariant counting, because the trivial multiplicity is fixed by the NN/DD spectra.

## 3. Harmonic 1-forms and Wilson lines (log [G], [W])
- **H¹(Σ,ℝ) contains no invariant vector. PROVED.**
  - As an Aut⁺ representation it splits into the two complex-conjugate 2-dim irreducibles (χ₃ ⊕ χ₄).
  - As an Isom representation it is the 4-dim irreducible χ₁₂.
  - The trivial multiplicity is 0 for both. J acts as −1 on H¹, so this holds for any subgroup containing J.
- **Continuous Wilson lines.**
  - MN N=2 has 4 twist-neutral 7D gauge fields: the 3 of SU(2)_R ⊂ SO(3) and U(1)_r, which is the fluctuation of the twisted SO(2).
  - With dim H¹ = 4 they give 16 real harmonic-1-form modes at linear order (CONDITIONAL, linear order).
  - **All 16 are removed in (A) and in (B). PROVED** under the canonical derivative lift with no gauge dressing. This holds because J lies in both groups and acts as −1, and no element of SO(3) × U(1) can act as −1 on all of these gauge directions (−1 ∉ Ad(SO(3)) on the 3).
  - The same applies to C₃ modes with one leg along a harmonic 1-form.
  - Dressing the lifts by R-symmetry elements would be a separate scope choice: **OPEN**, not done.
- **Discrete ℤ₂ Wilson lines (flat ℤ₂ classes in H¹(Σ,ℤ₂)).**
  - The 15 nonzero classes correspond to the pairs P_i − P_j of Weierstrass points. Under (A) and (B) they fall into orbits of sizes 3 and 12, and **0 are invariant**.
  - Label: the counting is PROVED. The identification with Weierstrass pairs is standard (Mumford, *Tata Lectures on Theta II*, ch. IIIa) and CONDITIONAL as a citation.
  - Corollary: the only invariant flat U(1) connection is the trivial one. J forces any fixed point onto the 2-torsion, and the 2-torsion has no nonzero invariant (PROVED given the above).

## 4. Spin structures (log [W])
- **Bare Σ spin structures: none of the 16 is invariant under (A), and so none under (B). PROVED (counting); identification CONDITIONAL (Atiyah 1971; Mumford IIIa).**
  - The 6 odd theta characteristics O(P_i) form one orbit of size 6.
  - The 10 even ones, the 3+3 splittings of the Weierstrass points, form orbits of sizes 4 and 6.
- **In the twisted theory the Σ spin structure is not a free choice. CONDITIONAL** (standard MN twist structure; argument below).
  - The 11D spinors on Y = S⁴-bundle over Σ are sections of K^{s/2} ⊗ L_R with L_R² = K^{∓1}. Only the product enters.
  - Since π₁(S⁴) = 1, the spin structures of Y form a torsor over H¹(Y;ℤ₂) ≅ H¹(Σ;ℤ₂) (16 of them).
  - Twisting by a nontrivial flat ℤ₂ bundle ε turns the constant Killing spinors into sections of ε, which have no global section. So **exactly one spin structure on Y is supersymmetric**: the one in which every fermion bundle is an integer power K^n.
  - Each K^n carries a canonical Aut⁺ action via dγ, and the SUSY spin structure is unique, so it is **Aut⁺-invariant and the action is a genuine Aut⁺ action** (no double cover).
  - The empty bare-Σ count above is consistent with this: invariance is only possible after the R-twist.
- **(B).** The orientation-reversing elements need an M-theory parity lift (§5), which needs a **Pin⁺ structure** (Witten hep-th/9609122, M-theory parity). That is **OPEN**, not checked.

## 5. How the elements of (B) act on the MN N=2 background (log [L]). The key A–B difference
- **Forced fibre flip. PROVED** (sympy, V2 metric). An orientation-reversing isometry of Σ, modelled locally as u → −u, maps the twist bundle (degree 2g−2) to its inverse. It therefore lifts only together with **φ₁ → −φ₁**, which is charge conjugation of the twisted U(1). The metric is invariant under (u, φ₁) → (−u, −φ₁) and **not** under u → −u alone.
- **Sign of G₄. PROVED** given the G₄ index sets of bd47ff5e C2.
  - Under this lift every G₄ component flips: {u,v,α,φ₂}, {u,v,β,φ₂}, {u,α,β,φ₂} and {α,β,φ₁,φ₂} → −G₄.
  - The map preserves 11D orientation (two reflections).
  - An M-theory symmetry needs (sign of G₄) = (orientation sign), because the C∧G∧G term is parity-odd.
- **Outcomes by dressing:**

| lift of a Bolza reflection | G₄ | orientation | symmetry? |
|---|---|---|---|
| (u, φ₁) alone | − | + | **No** |
| + φ₂ → −φ₂ (any O(3) det −1) | + | − | **No** |
| + wall ℤ₂ (ρ → −ρ, G₄ ∝ sgn ρ) | + | − | **No** |
| + x³ → −x³ (5D parity P) | − | − | **Yes** |
| + t → −t (time reversal T) | − | − | **Yes** |
| + φ₂ flip & P | + | + | **Yes** |

- **(B) read as an internal (KK) symmetry: REFUTED.** PROVED in-repo, given the bd47ff5e index sets. CONDITIONAL only on the internal isometries being Isom(Σ) lifts × O(2) × O(3).
  - A truncation to Isom-invariant modes by a purely internal action is not a truncation by a symmetry of MN N=2. It has no consistency guarantee beyond linear order.
- **(B) read consistently: the orientation-reversing elements must be dressed with an odd number of 5D spacetime reflections (P or T). PROVED** (same basis).
  - Then (B) acts as a **CP/T-type symmetry**, not an internal one. That matches complex conjugation of the class-S moduli (τ → −τ̄), with this interpretation CONDITIONAL.
  - Dressed (B) **does not remove KK species beyond (A)**. A DD-type Σ-mode f, with σ*f = −f, is kept, and its 5D field just has to be odd under P or T.
  - So the dressed-(B) species list equals (A)'s, with parity labels added. **PROVED** (follows from the table).
  - The dressed elements form a group isomorphic to Isom (P² = 1, and the dressing goes through the orientation character).
  - The dressings preserve the constant-ρ wall, so they commute with the wall ℤ₂.

## 6. S⁴ harmonics and the wall ℤ₂ parity
- **How the wall ℤ₂ acts.** It is ρ → −ρ on AdS₅ with C → −C (f825dfff; bd47ff5e C2). It acts on the 5D fields, not on Σ or S⁴.
  - It **does not remove 5D species**. It fixes their parity at the wall: even fields are Neumann-type, odd fields are Dirichlet-type.
  - Metric-derived fields are even: the X_i, h, the 5D graviton, and the 4D-tangent components of the 7D KK gauge fields.
  - C₃-derived fields with only 4D-tangent legs are odd; those with a ρ leg have the opposite parity.
  - Label: **PROVED** (the sign rule of an M-theory parity, with the background G odd). The orbifold boundary conditions themselves are CONDITIONAL on the HW premise.
- **SO(5) → SO(2)_twist × SO(3)_R content of the 14 (S⁴ level 2).** PROVED (representation counting).
  - q = 0: **1 + 5**, i.e. 6 modes.
  - q = ±1: 3 each, i.e. 6 modes.
  - q = ±2: 1 each, i.e. 2 modes.
- **Which are kept.**
  - The q = 0 modes are functions on Σ. Under both groups only their Σ-constant (and NN/DD) parts are kept.
  - The q ≠ 0 modes are sections of K^q. Their lowest Landau levels have no invariants under (A): H⁰(K) is the 2-dim irreducible χ₄ (trivial multiplicity 0), and H⁰(K²) = Sym² H⁰(K) is the 3-dim irreducible χ₆ (trivial multiplicity 0). This is **PROVED** for these holomorphic sections; log [G].
  - Their full twisted spectra and invariant counts are **OPEN**.

## 7. 5D masses of the surviving lowest levels (log [N], [S], [M])
**Σ-constant scalar sector.** Kept in A and in B, wall-even.

| mode | m²L₅² | Δ | label |
|---|---|---|---|
| SU(2)_R singlet (stress-tensor multiplet bottom) | −4 | 2 | PROVED within the U(1)² truncation (NL B1; its log line reproduced, sha MATCH). Consistent truncation CONDITIONAL (NL T2) |
| SU(2)_R **5-plet** | 0 | 4 | CONDITIONAL. NL computes one component (−3.4e-17 ≈ 0). The full 5 follows from SO(3)_R covariance and matches Cheung–Gauntlett–Rosen 1906.08900 §6.1 ("5×0"). The identification of the SO(3)-breaking direction is not re-derived |
| singlet (mixes with Σ breathing h) | 12 | 6 | PROVED within truncation (NL B1); CONDITIONAL as above |

**Spin-2 tower.** Wall-even.
- New in-repo result, **PROVED (exact sympy identity on the V2 metric, sha ad134752 MATCH):**
  - For any ψ = f(Σ), the Bachas–Estes spin-2 operator −e^{2A}(1/√g)∂_m(√g g^{mn}∂_n ψ) equals (F₀/G₀)·Δ_{H²} f exactly.
  - F₀/G₀ = e^{2f₀−2g₀} = **2** exactly at MN N=2.
  - The common warp D^{1/3} cancels, and the twist cross-terms drop out.
  - So **m²L₅² = 2λ_hyp**. That is CONDITIONAL only on the Bachas–Estes reduction (arXiv:1103.2800, form generalised to AdS₅; derivation in the .py comments).
  - For comparison, (D) gives (L₅/ρ)² = 4, i.e. 7824e789 S7's 4λ. The (D) rule does **not** carry over to MN N=2.
- This also sharpens the "≈ 7.68 unwarped estimate" in ERRATUM2. For λ₁ the spin-2 value is exactly 2 × 3.8388872588 = **7.677775** (Δ = 5.4173), with the warping included. That mode is **not invariant** under either group, because λ₁ is a 3-dim irreducible.

| scope | invariant spin-2 levels: λ → m²L₅² (Δ) |
|---|---|
| both (A) and (B) | 0 → 0 (Δ=4, massless 5D graviton); 23.07856 → 46.157 (9.082); 74.9267 → 149.853 (14.404); 116.6025 → 233.205 (17.401); 169.2045 → 338.409 (20.504); 256.6928 → 513.386 (24.746) |
| (A) only (DD levels) | 222.3711 → 444.742 (23.184); 394.578 → 789.16 (30.16) |
| (B) internal | the NN list only |
| (B) dressed | same list as (A); DD levels have P/T-odd 5D fields |

- Labels for these masses:
  - The levels and masses are PROVED numerically: Richardson spread ≤ 2e-4 on λ for the first six; 23.0786 is confirmed against SU to 3e-9.
  - The mass formula is CONDITIONAL on Bachas–Estes.
- What is **OPEN**:
  - Σ-harmonic towers of the scalar, vector and form sectors in the twisted background, which don't factorise like spin-2.
  - Spin-2 modes with S⁴ dependence: they separate as 2λ + μ_F, with the fibre eigenvalues μ_F not computed.
  - Fermions.
  - The q ≠ 0 towers.
  - B5's positive-energy bound (CONDITIONAL) keeps everything ≥ −4.

## 8. Where (A) and (B) differ
1. **Species lists.**
   - (A) keeps NN ∪ DD Σ-levels; (B) internal keeps NN only.
   - The first difference is at λ = 222.371 (spin-2 m²L₅² = 444.74). Below that the two invariant spectra are **identical**: 0, 23.08, 74.93, 116.60, 169.20.
   - PROVED numerically.
2. **Status as a symmetry.**
   - (A) is an internal symmetry of MN N=2 × wall (canonical derivative lift; SUSY preserved, CONDITIONAL).
   - (B) is **not** internal (REFUTED, §5). It exists only when dressed with P or T, and then it adds parity labels instead of removing species. In that case the dressed-(B) species list equals (A)'s.
3. **Spin structure.**
   - (A): the unique SUSY spin structure on Y is invariant (CONDITIONAL).
   - (B): needs a Pin⁺ lift (OPEN).
4. **No difference** in: Wilson lines (none survive in either), discrete ℤ₂ lines (none), the Σ-constant sector, or the wall parities.

## 9. Junction and count gap
- **Junction (UNSOLVED): unchanged by (A) and by (B). PROVED** for the truncation as such; CONDITIONAL for the NEC part.
  - The Israel data, the 6:8:8 anisotropic stress and the fibre-NEC deficit (bd47ff5e (ii); NL Y3/Y5) are local and Γ-independent.
  - A truncation only selects fluctuation modes; it does not change the background or the required S_ab.
  - The surviving modes are ordinary sugra fields obeying the NEC (CONDITIONAL), including the BF-saturated Δ=2 scalar, so none of them supplies the NEC-violating fibre stress.
  - The dressed-(B) P/T elements preserve the constant-ρ wall and do not change S_ab.
- **Count gap: unchanged by (A) and by (B).**
  - N_req/(2N_flux) is a ratio of two Σ-integrals of constant densities, so it is independent of Area(Σ) and of Γ (PROVED, bd47ff5e §3/§5).
  - Neither truncation changes the flux quantum N = 4880 or the wall charge 2N = 9760.
  - The only discrete data that could shift charges are ℤ₂ Wilson lines (none survive) and the spin structure (fixed to the unique SUSY one, CONDITIONAL). So the gap stays NL's [1.255, 1.667), against MR2's 1.288 (horizontal measure, inside the gap) and 1.032 (fixed-φ measure, below it). The measure choice is still CONDITIONAL.
- **Neither scope offers a resolution of the junction or the count gap.** The Owner's "possible resolutions" are not found along this route (OPEN for other routes).

## 10. Labels
| item | label |
|---|---|
| closure order 96 = 48 + 48; faithful on H¹; order statistics = GL(2,3); character tables (8 and 13 classes) | PROVED (in-repo) |
| equalities |Aut⁺| = 48, |Isom| = 96; GL(2,3) isomorphism | CONDITIONAL (B-M16 lemma; Cook) |
| Σ/Isom = (2,3,8) triangle; 1-dim characters ↔ N/D boundary conditions; NN ↔ trivial, DD ↔ orientation | PROVED |
| invariant Σ-levels (table §2), simple; 23.0786 = SU λ₈ | PROVED numerically (FEM; rigorous bounds OPEN above 28.08) |
| irreducible labels of the higher-dim eigenspaces | OPEN (λ₁ 3-dim and λ₂ 4-dim per Cook: CONDITIONAL) |
| no invariant harmonic 1-forms; all 16 continuous Wilson-line modes removed (A, B) | PROVED (lift without gauge dressing); linear-order masslessness CONDITIONAL |
| no invariant ℤ₂ Wilson lines or bare spin structures | PROVED counting; Weierstrass/theta identification CONDITIONAL |
| unique SUSY spin structure on Y, Aut⁺-invariant | CONDITIONAL |
| (B) as an internal symmetry | REFUTED |
| (B) dressed with P or T is a symmetry; same species as (A) | PROVED (given bd47ff5e index sets) |
| Pin⁺ lift for dressed (B); R-symmetry-dressed lifts | OPEN |
| wall-ℤ₂ parities (metric even, tangential C₃ odd) | PROVED; orbifold BCs CONDITIONAL (HW) |
| H⁰(K), H⁰(K²) have no Aut⁺ invariants | PROVED |
| Σ-constant masses −4, 0 (5-plet), 12 | PROVED within truncation (−4, 12); 5-plet CONDITIONAL; consistency CONDITIONAL |
| spin-2 operator = 2Δ_Σ exactly; m²L₅² = 2λ | identity PROVED; Bachas–Estes form CONDITIONAL |
| scalar/vector/form Σ-towers, fibre spin-2 μ_F, q ≠ 0 towers, fermions, full spectrum | OPEN |
| junction | UNSOLVED (unchanged by A or B) |
| count gap | unchanged by A or B (PROVED for Γ-independence; measure CONDITIONAL) |
| "λ₁ ≈ 3.8388976 is Bolza's" (job brief) | REFUTED. It is the KMP bound; Bolza is 3.8388872588 |

Tally (rows): PROVED 9 · CONDITIONAL 4 · OPEN 3 · REFUTED 2 · mixed 4 (the PROVED part with a CONDITIONAL premise is listed in the row) · UNSOLVED 1 (junction, carried).

## 11. Remaining path and ETA
| item | path | ETA |
|---|---|---|
| fibre spin-2 eigenvalues μ_F (S⁴-dependent spin-2, both groups) | 2D Sturm–Liouville in (α,β) on the V2 metric (the operator separates: 2λ + μ_F) | ~1 h |
| full irreducible labels of the Bolza eigenspaces | FEM on the full octagon + projection with all 96 elements (characters from §1) | 1–2 h |
| invariant counts of the q ≠ 0 towers (charged 12 of the 14) | weight-2q Maass/Landau spectrum on Bolza with the K^q-twisted triangle problem | 2–3 h |
| rigorous eigenvalue bounds beyond 28.08 | SU-type MPS or interval FEM | days |
| scalar/vector Σ-towers in the twisted background | ExFT spectrometry (Malek–Samtleben 1911.12640), restricted to the invariant sector | days |
| Pin⁺ lift for dressed (B) | Owner first decides whether dressed (B) is wanted | 1 h after a decision |
| Owner choice | (A), (B)-internal (REFUTED as a symmetry), or (B)-dressed (= A species + P/T labels) | Owner |
