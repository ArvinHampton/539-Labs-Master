# PP audit: MR2 KK truncation of MN N=2 under (A) Aut⁺ (order 48) and (B) Isom (order 96), each with the wall ℤ₂
Author: Professor Proof (PP). Audit only. Additive new file. No CERT. Nothing adopted. Nothing sent. Refutations are made only by proof or counterexample.
Citations are graded under OW 36683379. The scope is OW 49b04146 together with OW 91e69b38: this is a scope choice, and the full KK spectrum stays OPEN. Tip 7cddb188 MATCH before and after.
PP scripts are in /workspace/audit-scratch/pp_1852_audit/, each with a sidecar:
- pp_kk_checks.py (a5d0918f…) and its log (1de37729…)
- pp_fem238.py (88f90fd5…) and its log (ccf7b3ef…)
- mr2kk_rerun.log (1d4dc7da…)

## 0. Records and integrity
- R1 [PROVED] The three MR2 files equal their sidecars:
  - .md ecee266893471955b9fa53eaaa7c87bbfae9efea16d7e194b4dc07409a61cfdd
  - .py 88949658116586c63dc4785fc31c222eed6d9ef44afbefbc6e40a4946b20b26c (mtime 18:46:26, before the .log at 18:47:15, consistent with "frozen before the run")
  - .log a2d105e69f723604238ff3eed30664b41bd6d4f9c1d6e717542849f4389c253f
- R2 [PROVED] PP reran the frozen .py. Its output is byte-identical to MR2's .log apart from the runtime line (107.6 s vs 43.7 s) and the wrapper's trailing "exit 0".
- R3 [PROVED] OW b0b9ae7f: OWNER_WRITE_MAINCHAT_t4407_PURSUE_ALL_OPEN_ITEMS_FOR_RESOLUTIONS_2026-11-09_1843.md = b0b9ae7fecd635e0735a66a7839bdf0148d65f8eba8adf032c68c0ad3c73494d = its sidecar.
  - Verbatim: "Pursue all for resolutions."
  - The lanes propose and recommend; nothing is adopted until the Owner chooses in his own words. The KK tower is an MR2 item, and PP audits.
- R4 [PROVED] OW b1893386 (t4410, about 18:51): OWNER_WRITE_MAINCHAT_t4410_KK_RUN_PINPLUS_CHECK_DRESSED_GROUP_B_BEFORE_CHOICE_2026-11-09_1851.md = b189338679afe075f120c60553707520c74e9e7de7540b9bb23a589b5280c40f = its sidecar.
  - Verbatim: "Run the Pin⁺ check on dressed Group B before I choose."
  - Direction:
    - MR2 runs the Pin⁺ (structure/anomaly) check on dressed B, with both 5D parity and time reversal, and PP audits it.
    - The group choice (A, B-dressed, or neither) is deferred to the Owner. **No group is adopted now.**
    - The junction stays UNSOLVED, the full KK spectrum stays OPEN, the count gap is unchanged, and MN2 stays CONDITIONAL.
  - This matches the relay.
- R5 [CONDITIONAL: not verifiable on disk] **The disclosed Δ correction.**
  - The .md on disk does not mention a corrected Δ. There is no earlier version on disk. The .md mtime is 18:49:02.611 and its sidecar's is 18:49:02.615.
  - PP recomputed every Δ in the .md from Δ = 2 + √(4 + m²L₅²). **All are correct.** The values are 9.082, 14.404, 17.401, 20.504, 24.746, 23.184, 30.16, 5.4173, and 2/4/6.
  - The only Δ not printed in the .log is **394.578 → m²L₅² 789.16 → Δ = 30.163**. It is therefore the likely corrected value, and as filed it is correct.
  - Which value was changed cannot be confirmed from disk.

## 1. The groups (PP's own construction, independent of MR2's code)
- G1 [PROVED] **Group closure.**
  - The generators are x → ix and x → (x+1)/(1−x), with their y-lifts, plus J and K.
  - The closure has order **96**, with **48** holomorphic elements.
  - The 96 realified H¹ matrices are distinct, so the action is faithful.
- G2 [PROVED] **Element orders and classes.**
  - Aut⁺ element orders are {1:1, 2:13, 3:8, 4:6, 6:8, 8:12}. These are GL(2,3)'s.
  - Aut⁺ has 8 classes. Isom has 13 classes, with orders {1:1, 2:31, 3:8, 4:8, 6:8, 8:24, 12:16}.
  - The abelianization gives **2 and 4** one-dimensional characters.
  - Σd² checks: 4·1 + 2·4 + 4·9 + 3·16 = 96, and 1+1+4+4+4+9+9+16 = 48.
  - The MR2 character tables (Dixon) agree with the class counts and the 1-dim counts. Nine non-linear irreps with Σd² = 92 match {2², 3⁴, 4³}. PP did not rederive the tables.
- G3 [CONDITIONAL, agree] |Aut⁺| = 48 and |Isom| = 96 exactly, and the isomorphism with GL(2,3). These rest on the B-M16 lemma (uniqueness of the hyperelliptic involution) and Cook.

## 2. Invariant-mode counting on the (2,3,8) triangle
- T1 [PROVED] **The boundary-condition logic.** Σ/Isom is the reflection triangle with angles π/8 at A, π/2 at B and π/3 at C.
  - A 1-dim character is a choice of ±1 on the three reflections.
  - At C the relation (r_AC r_BC)³ = 1 has odd order, which forces χ(r_AC) = χ(r_BC). The orders at A (8) and B (2) are even, so they impose nothing. That gives exactly 4 characters.
  - NNN is the trivial character. DDD (all reflections −1) is the orientation character.
  - On Aut⁺ (even words) DDD restricts to trivial, and the two mixed types both restrict to det.
  - For an Aut⁺-invariant eigenfunction f, every reflection acts by the same sign, because r_i r_j ∈ Aut⁺ and σ² = 1. So f is NNN or DDD, and the Aut⁺-invariant multiplicity equals #NN(λ) + #DD(λ).
  - Equivalently, it is the spectrum of the (2,3,8) double, the orbifold sphere Σ/Aut⁺, split by its reflection.
- T2 [PROVED numerically] **PP's own FEM.** It uses P1 elements on a different mesh (polar fan in the Poincaré disk), the area π/24 to 6e-8, and Richardson extrapolation over n = 80/160. It reproduces MR2 to ≤ 1e-4 in every BC type:
  - NN: 0, **23.0786**, 74.9267, 116.6025, 169.2045, 256.6929, 306.6803
  - DD: **222.3711**, **394.5778**, 583.473, …
  - DN: 32.6737, 120.4438, …
  - ND: 91.4649, 199.3263, …
  - The 23.0786 matches Strohmaier–Uski λ₈ = 23.0785584814 (MR2: 2.8e-9).
  - The flat-metric control fails, as required.
- T3 [PROVED numerically] **λ₁ eigenspace.** No 1-dim-character eigenvalue lies below 23.0786 in any of the four spectra. So the λ₁ eigenspace contains neither the trivial nor the orientation character.
  - Given its multiplicity 3 (SU/Cook, CONDITIONAL), it is a 3-dim irreducible: 1+1+1 and 2+1 would contain a 1-dim character. So λ₁ drops out of every invariant spectrum.
  - Spin-2 check: 2 × 3.8388872588 = **7.6777745** (Δ = 5.41728) ✓.
- T4 [PROVED as bookkeeping; REFUTED grade downgraded to CONDITIONAL] "3.8388976 is Bolza's λ₁."
  - MR2's own ERRATUM2 7b9ebdaf had already identified 3.8388976481 as the Kravchuk–Mazáč–Pal genus-2 upper bound. So the REFUTED row in §10 is a **self-correction** of the brief's wording, not a new result.
  - The Bolza value 3.8388872588 is cited from SU and was not recomputed by MR2 or PP. PP's triangle FEM cannot reach a 3-dim irreducible. A REFUTED grade needs a proof or a counterexample, so the grade is "**corrected, CONDITIONAL on SU**".

## 3. Truncation (A): Aut⁺ × wall ℤ₂
- A1 [PROVED numerically] The surviving levels are 0, 23.0786, 74.9267, 116.6025, 169.2045, **222.3711 (DD)**, 256.6929, 306.6803, 387.14, **394.578 (DD)**, …
  - Each level is simple within its BC type.
  - MR2's level-8 cell lists 387.14 (NN) and 394.58 (DD) but stops there. The next NN values are 442.85 and 500.66 (in the .log). These are not errors.
- A2 [PROVED as an identity; CONDITIONAL on Bachas–Estes] Spin-2 m²L₅² = 2λ.
  - PP's rerun reproduces the sympy line "op − (F₀/G₀)(−Δ_H² f) simplifies to 0", with F₀/G₀ = 2 exactly.
  - 2 × 23.07856 = 46.157, Δ = 9.082 ✓.
- A3 [PROVED within the truncation, agree] **Σ-constant scalars.**
  - The masses are m²L² = −4 (Δ = 2), 0 (Δ = 4, the 5-plet; CONDITIONAL as MR2 says), and 12 (Δ = 6). All are wall-even.
  - −4 equals the AdS₅ BF bound −d²/4 = −4. It is saturated, not violated, and Δ₊ = Δ₋ = 2. This is consistent with PP's earlier BF audit of MR2 7824e789.
- A4 [PROVED for U(1), agree; with a scope gap] **Wilson lines.**
  - J = −1 on H¹ (PP-verified). Its fixed points in H¹(Σ, U(1)) = T⁴ are exactly the 2-torsion, the 16 points of H¹(Σ;ℤ₂).
  - The 15 nonzero 2-torsion classes are P_i − P_j. Under both groups their orbits have sizes **3 + 12** (PP-verified), so none is invariant. The 2-torsion is therefore handled.
  - The 16 linear modes are removed under the canonical lift.
- A4-gap [PROVED, counterexample; OPEN item missing from MR2's list] **Non-abelian SU(2)_R flat connections, up to gauge, are not covered.**
  - Take an abelian SU(2) flat connection, ρ(γ) = exp(iθ(γ)σ₃). Then ρ∘J_* = ρ⁻¹ = wρw⁻¹, where w is the Weyl element. So **every** such connection is J-invariant up to gauge, and the "J = −1 kills Wilson lines" argument does not extend to SU(2)_R moduli.
  - Full Aut⁺-invariance up to gauge, i.e. the Aut⁺-fixed points of the SU(2) character variety including torsion points with g·θ = det(g)·θ, is **not computed**.
  - MR2's PROVED claim holds as stated (canonical lift, no gauge dressing, U(1)/ℤ₂). The moduli-space statement is OPEN.
- A5 [PROVED counting, agree] **Spin structures.**
  - Because −1 ≡ +1 mod 2, J acts trivially on H¹(Σ;ℤ₂), so **J fixes all 16 theta characteristics**. The emptiness therefore comes entirely from the S₄ permutation action on the Weierstrass points.
  - The orbits are: odd 6 (one orbit); even 10 = 4 (face pairs of the octahedron) + 6. PP verified both.
  - **None of the 16 is invariant.** The theta/Weierstrass identification is CONDITIONAL (Mumford).
  - The unique SUSY spin structure on Y and its Aut⁺-invariance are CONDITIONAL, agree.

## 4. Truncation (B): Isom × wall ℤ₂
- B1 [PROVED; PP gives an independent proof of MR2's REFUTED] **(B) as an internal symmetry is REFUTED.**
  - Let σ be any orientation-reversing isometry of Σ (for example K: (x,y) → (x̄,ȳ)).
  - deg σ*L = −deg L = −2 ≠ 2, so every internal lift must include an orientation-reversing map of the twisted φ₁-plane.
  - Allow any O(3) part, with det ε. Then:
    - the 11D orientation sign is (−1)(−1)ε = ε;
    - the S⁴-flux component (N = 4880 ≠ 0) maps as G₄|_{S⁴} → (−1)·ε·G₄|_{S⁴}.
  - An M-theory symmetry needs f*G = (orientation sign)·G, i.e. −ε = ε. That is impossible for either ε. So **no internal lift is a symmetry.**
  - This uses only the S⁴-flux component, so it does not depend on MR2's full G₄ index list. It is CONDITIONAL only on the internal isometries being Σ-lifts × O(2) × O(3), which is MR2's caveat.
- B2 [PROVED, agree] **Dressing.**
  - Adding P or T (5D orientation −1) gives an orientation sign of −ε and G sign −ε, so the condition can be met.
  - Dressed (B) keeps the same species as (A), with 5D parity labels added: DD Σ-modes pair with P- or T-odd 5D fields.
  - A and B agree below 222.371. The levels 222.371 and 394.578 appear only in A-internal and dressed B.
- B3 [OPEN, agree] **The Pin⁺ check (OW b1893386).** Precisely, it must establish the following.
  - **Manifold.** Use the 11D double cover X = AdS₅ (Euclidean: H⁵) × Y₆, where Y₆ is the twisted S⁴ bundle over Bolza Σ. The group is the full Ĝ = (dressed Isom) × ℤ₂^wall.
    - Note that the wall ℤ₂ (ρ → −ρ, C → −C) is already an M-theory parity, so even (A) × wall involves an orientation-reversing element.
  - **(i) Bosonic invariance.** f*G₄ = (orientation sign of f)·G₄ for the generators. MR2's table and B1 give this.
  - **(ii) Structure.** X is spin, with spin structure s₀, and Pin⁺ structures on X form a torsor over H¹(X;ℤ₂) ≅ H¹(Σ;ℤ₂). (The S⁴ fibre has π₁ = 1 and AdS is contractible.)
    - For every g ∈ Ĝ, the class δ(g) = g*s₀ − s₀ ∈ H¹(Σ;ℤ₂) must vanish, with s₀ viewed as a Pin⁺ structure for orientation-reversing g.
    - Equivalently, each g maps Killing spinors to Killing spinors under the Pin⁺ Clifford action. Reflections act by Γ_n with Γ_n² = +1 in Euclidean signature. Then δ = 0 follows from the uniqueness of s₀ (CONDITIONAL).
  - **(iii) The lifted group.** Compute the extension class of 1 → ℤ₂^F → Ĝ̃ → Ĝ → 1 in H²(Ĝ;ℤ₂).
    - For a dressed P-reflection there are k = 3 reflected directions (u, φ₁, x³). In Pin⁺, (e₁e₂e₃)² = (−1)^{k(k−1)/2} = −1, so g̃² = (−1)^F. Its T-dressed analogue must be computed in Lorentzian signature.
    - Then check the triangle relations: (r̃_AB r̃_AC)⁸ and (r̃_AC r̃_BC)³ must equal +1 if MR2's claim that Aut⁺ lifts genuinely holds. At the π/8 vertex, the 2π Σ-rotation (−1 in Spin) must be cancelled by the φ₁ twist rotation.
  - **(iv) Obstruction class**, needed only if dressed B is gauged or used as an orbifold quotient.
    - The quotient must be **Pin⁺: w₂ = 0** (Kirby–Taylor convention, Pin⁺ ⇔ w₂ = 0). **w₂ + w₁² = 0 is the Pin⁻ condition, not the M-theory one.** M-theory requires Pin⁺ (Witten hep-th/9609122; Freed–Hopkins arXiv:1908.09916; cited, math-unchecked). The check must state its Clifford sign convention.
    - It must also check twisted flux quantization [G/2π] − λ/2 ∈ H⁴(·; ℤ̃_{w₁}). On the fibre λ|_{S⁴} = 0 because p₁(TS⁴) = 0, so the S⁴ flux is simply N ↦ −N under orientation-reversing g.
    - For gauging, the Pin⁺ anomaly must also be checked (Freed–Hopkins; CONDITIONAL).
  - For KK truncation alone, (i)–(iii) suffice.
  - Remark [PROVED from MR2's own table]: the "φ₂-flip & P" dressing is **orientation-preserving** in 11D, with G₄ invariant. It needs only a Spin lift (δ = 0 for spin structures), not Pin⁺. It is still CP-like from the 5D point of view.
- B4 [OPEN, agree] The Pin⁺ lift and R-symmetry-dressed lifts.

## 5. Junction and count gap
- J1 [PROVED, agree] **The junction is unchanged.** A truncation does not alter the background or the required S_ab. By 1800 Y3-ineq, no E₈ or NEC-obeying field supplies the fibre deficit.
- J2 [PROVED for Γ-independence, agree; with fixes] **The count gap is unchanged.**
  - MR2's "1.288 inside [1.255, 1.667)" uses the all-candidate interval.
  - For the adopted MN2, the interval is (1 + 2808.6/9760, 1.6667) = (**1.28777**, 1.6667). MR2's 1.28761 coincides with its open lower end to 1.6e-4; this is NL S13 and PP 1846.
  - MR2's 1.032 (fixed-φ) is **gauge-dependent**. PP 1846 gives the counterexample 0.9934 / 0.9046 / 0.7139 under pure-gauge shifts, so it should not be quoted as a gap comparison.

## 6. OPEN list and tallies
- O1 [PROVED with one omission] MR2's OPEN items are genuine: the irreducible labels, rigorous bounds above 28.08, R-dressed lifts, Pin⁺, the scalar/vector/form towers, the fibre spin-2 eigenvalues μ_F, the q ≠ 0 towers, and fermions. The list is honest except that it omits A4-gap (SU(2)_R moduli up to gauge).
- O2 [REFUTED, by count] MR2's §10 tally ("PROVED 9 · CONDITIONAL 4 · OPEN 3 · REFUTED 2 · mixed 4 · UNSOLVED 1", 23 entries) does not match its own table, which has **19 rows**.
  - PP's per-row reading of those 19 rows is: 4 pure PROVED, 7 mixed (PROVED plus a CONDITIONAL premise or OPEN bounds), 2 CONDITIONAL, 3 OPEN, 2 REFUTED and 1 UNSOLVED, which sums to 19.
  - MR2 should list the row assignment.

## A vs B as candidate resolutions (OW b0b9ae7f: graded for the Owner, nothing adopted)
- **(A) Aut⁺ × wall ℤ₂: the strongest candidate.**
  - It is an internal symmetry: the lift is canonical, and SUSY preservation and spin-structure invariance are CONDITIONAL.
  - The truncation is well-defined. Its spectrum is PROVED numerically (λ: 0, 23.08, 74.93, 116.60, 169.20, 222.37, …).
  - It kills all U(1)/ℤ₂ Wilson lines and all bare spin structures. SU(2)_R moduli are OPEN.
  - Remaining obligations: the wall ℤ₂ element is orientation-reversing, so the same Pin⁺ item (ii)–(iii) applies to (A) × wall for that one element.
- **(B) internal: REFUTED.** It is not a symmetry (B1 proof).
- **(B) dressed with P or T: a consistent candidate only as a CP/T-type symmetry, pending OW b1893386's Pin⁺ check (B3 (i)–(iii)).**
  - It removes **no species beyond (A)**. It only adds 5D parity selection rules, so its value over (A) is those selection rules alone.
  - The "φ₂ & P" variant needs only Spin.
- **Neither choice changes the junction (UNSOLVED) or the count gap.** This route offers no resolution of either. PP's audit-only reading: (A) is the minimal consistent choice, and dressed B adds only discrete parity data. The Owner decides.

## MR2 fixes (additive erratum)
1. Put the Δ-correction disclosure (which value, old → new) into an on-disk erratum. The filed values are all correct.
2. Add A4-gap to the OPEN list: SU(2)_R flat connections up to gauge, where the Weyl element makes every abelian SU(2) line J-invariant.
3. In §4, state that J fixes all 16 spin structures and that the emptiness comes from S₄ alone.
4. Regrade the λ₁ row from REFUTED to "corrected (self-correction, ERRATUM2), CONDITIONAL on SU".
5. §9: use the MN2 interval (1.28777, 1.6667), note that 1.2876 sits at its open end, and drop or flag 1.032 as gauge-dependent (PP 1846).
6. Make §10's tally match the rows.
7. For the Pin⁺ file:
   - cover Ĝ including the wall ℤ₂;
   - use w₂ = 0 (Pin⁺, stating the convention), not w₂ + w₁²;
   - compute δ(g) and the extension class in H²(Ĝ;ℤ₂);
   - treat the "φ₂ & P" Spin-only variant separately.

## Rollup (this file)
PROVED 25 · CONDITIONAL 3 · OPEN 2 · REFUTED 1 = 31
- **PROVED (25):**
  - R1–R4
  - G1, G2
  - T1, T2, T3
  - A1, A2, A3, A4, A4-gap, A5
  - B1, B2
  - J1, J2
  - O1
  - verifications: the Δ recomputation (all correct), the 2λ value, the spin-2 λ₁ value (7.6777745), the BF saturation, and the MR2 .py rerun
- **CONDITIONAL (3):** R5 (which Δ was corrected), G3, T4
- **OPEN (2):** B3 (Pin⁺, OW b1893386), B4
- **REFUTED (1):** O2 (tally against rows)

No CERT. No message sent. Nothing adopted. Tip 7cddb188 MATCH.
