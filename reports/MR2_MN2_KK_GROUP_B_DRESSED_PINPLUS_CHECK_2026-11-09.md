# MR2: Pin⁺ check for the KK truncation symmetry of MN N=2 (N=4880, g=2, Γ = Bolza): the adopted A × wall ℤ₂ first, then dressed B (moot)
Author: MR2. Additive new file. No CERT. No Gemini. Nothing sent. Nothing adopted by MR2.
- Authority: OW b1893386 (t4410, "Run the Pin⁺ check on dressed Group B before I choose.") and OW 8b26c786 (t4414, 19:05, Owner's words "Group A"; sha verified = sidecar). Under OW 8b26c786 the truncation symmetry is **Aut⁺(Bolza) (48) × wall ℤ₂**. That is a scope choice, not a result. B is not adopted, so §B below is **moot** and is filed because it was essentially finished.
- Folds in PP audit 1fe6c574 (FINDINGS_PP_AUDIT_MR2_KK_TRUNCATION_BOLZA_48_96_WALL_Z2_2026-11-09_1858.md), items B3 (a)–(g). Each item was verified independently. §3 lists the points of agreement and the one refinement.
- Builds on the KK file ecee2668 (.py 88949658, sha-checked and exec'd in the [0] line of the log). Tip 7cddb188 MATCH before and after.
- Full spectrum OPEN. Junction UNSOLVED. Count gap unchanged. Vacuum MN N=2 CONDITIONAL (19a88b19).

## Files (reports/)
| file | sha256 |
|---|---|
| MR2_MN2_KK_GROUP_B_DRESSED_PINPLUS_CHECK_2026-11-09.py (frozen: chmod a-w + sidecar at 19:04:58, before the run) | 2f0e12201717a508a6c3fc965c829ddf1e3e7677e50a8d725debe11beb4c03db |
| MR2_MN2_KK_GROUP_B_DRESSED_PINPLUS_CHECK_2026-11-09.log (19:05:00, runtime 0.5 s plus the exec of the KK group section) | c920912746999f6237fd5757a46561e1d9e70484f0ae63abe3441c958f0e9183 |
| this .md | see sidecar |

The file name keeps the planned "GROUP_B" stem from OW b1893386. Its content leads with A, per OW 8b26c786.

## 0. Conventions (PP item b)
- **Signature and Clifford algebra.** Lorentzian, mostly plus: η = diag(−1, +1, …, +1). The rep is a real 32×32 representation of Cl(10,1), with γ₀² = −1 and γᵢ² = +1. It is constructed explicitly in log [C] (Clifford error 0), with Γ⁰⋯Γ¹⁰ = +1 (the Hořava–Witten convention).
- **Euclidean.** Every Γₐ² = +1. A reflection across the hyperplane normal to n lifts to ±n·Γ, with square +1. This is Kirby–Taylor **Pin⁺**, and its obstruction class is **w₂ = 0**. **w₂ + w₁² = 0 is Pin⁻.** I agree with PP.
- **Why M-theory needs Pin⁺.** This is PROVED in-repo (log [C], second line), so it does not rest only on the citation.
  - The 11D gravitino is Majorana, so it needs a real 32-dimensional module.
  - Cl(10,1) has p − q = 9 ≡ 1 mod 8, so it is M₃₂(ℝ) ⊕ M₃₂(ℝ), and a real 32 exists.
  - In Cl(1,10) (the Pin⁻ convention, spatial γ² = −1), the volume element ω is central with ω² = (−1)^{55}·(−1)^{10} = −1. So ω is a commuting complex structure on any real module. Every real module then has dimension ≥ 64, and no real 32 exists.
  - Hence spatial reflections lift as R = γᵢ with R² = +1, and time reversal as T = γ₀ with T² = (−1)^F. This is Witten 1508.04715 (§2, verified) and Freed–Hopkins 1908.09916 (§2, verified).
  - For a real M, T² = M² on the field even though T is antiunitary.

## A. The adopted group: Aut⁺ × wall ℤ₂ (OW 8b26c786). PP items (a)–(d) and (g)
Generators of Ĝ_A: g1 (x → ix), g2 (x → (x+1)/(1−x)), J (y → −y), and W (ρ → −ρ with C → −C, per OW f825dfff).

**A1 (a). W is orientation-reversing, and its bosonic rule holds. PROVED (log [C] table, row W).**
- The 11D orientation sign is −1, the G₄ sign is −1, and f*G = (orientation sign)·G is satisfied.
- W reflects no wall-tangent direction, so the 10D wall orientation is preserved.
- Its lift is W̃ = Γ_ρ, with W̃² = +1 and [W̃, Γ_ρ] = 0. It preserves the HW projection Γ_ρε = ε, which is the 10D chirality (log: Γ_wall = +Γ_ρ).
- On S⁴ flux it maps N to −N on the image side. That is the standard 2N wall charge of the orbifold (bd47ff5e), not a violation.

**A2 (b). Pin⁺ (w₂ = 0) structures exist for every element. PROVED, given the premise that X is spin.**
- Take X = AdS₅ × Y₆. Here Y₆ is the twisted S⁴ bundle over Σ, X is oriented, and w₂(X) = 0 (it is spin, CONDITIONAL as in ecee2668 §4). Pin⁺ ⇔ w₂ = 0, so every spin structure is in particular a Pin⁺ structure.
- **W.** W acts only on the contractible AdS factor, as a hyperplane reflection. X/W is the manifold with boundary {ρ ≥ 0} × (rest). Its w₂ is restricted from X, so it is 0, and a Pin⁺ structure exists (in fact a Spin one, since X/W is orientable).
- **Aut⁺.** These elements preserve orientation, so they need only a Spin lift (A3, A4).
- **Truncation alone needs no quotient.** The Aut⁺ fixed-point orbifold is never formed (A6).

**A3 (c). δ(g) = g*s₀ − s₀ = 0 in H¹(Σ;ℤ₂) for every generator. PROVED as a computation, given the twisted-spin model (CONDITIONAL, ecee2668 §4).**
- The model: Pin⁺/Spin structures on X form a torsor over H¹(X;ℤ₂) ≅ H¹(Σ;ℤ₂) ≅ J[2], with 16 elements. This holds because π₁(S⁴) = 1 and AdS is contractible.
- A structure is labelled by d = s ⊕ s_R ∈ J[2], where s is the Σ theta characteristic and s_R is the R-bundle root. The SUSY structure is d₀ = 0 (s_R = s).
- In the Weierstrass model, J[2] is even subsets modulo complement and theta characteristics are odd subsets modulo complement. The log checks the torsor bijection (True) and computes δ for each generator and each of the 16 base choices s:

  | generator | Weierstrass permutation (0, ∞, 1, i, −1, −i) → | bare Σ spin structures fixed | δ(g) on s₀ |
  |---|---|---|---|
  | g1 | 0, ∞, i, −1, −i, 1 | 2/16 | 0 |
  | g2 | 1, −1, ∞, i, 0, −i | 2/16 | 0 |
  | J | identity | **16/16** | 0 |
  | W | identity on Σ | 16/16 | 0 |
  | (K, dressed B only) | 0, ∞, 1, −i, −1, i | 8/16 | 0 |

- Orbits of Ĝ_A on J[2] are {0}, 3 and 12, so d₀ is the unique fixed point.
- Bare Σ spin structures are moved by g1 and g2, so none is Aut⁺-invariant (16 → orbits 6, 4, 6). J fixes all 16, which confirms PP fix 3. The bare non-invariance comes only from the permutation action.

**A4 (d). The lifted group and its extension class. Values PROVED (log [E]); identification of the class CONDITIONAL on descent.**
- **Vertex rotations.** Σ/Aut⁺ is the (2,3,8) orbifold sphere. Its vertex rotations have orders 8, 2 and 3.
  - The Σ-only spin lift has m-th power **−1**: the 2π rotation, i.e. (−1)^F.
  - The twisted lift (Σ plane together with the φ₁-plane, for both L = TΣ and L = K) has m-th power **+1** for m = 8, 2 and 3. So the 2π rotation on Σ is cancelled by the twist rotation, exactly as PP's B3(iii) requires.
  - Each rotation lift commutes with W̃.
- **Relation to the reflection lifts.** The product of reflection lifts equals −1 times the connected lift (log). This sign is absorbed in the dressed-B analysis (§B).
- **Data for Ĝ_A.**
  - W̃² = +1.
  - (r̃_a r̃_b)^m = +1 for all three vertices. J, the central order-2 element, acts at each Weierstrass point as a rotation by π on Σ and on the φ₁-plane, and its twisted lift squares to +1 (the m = 2 line).
  - [W̃, Aut⁺ lifts] = +1.
- **Extension class.** The class of 1 → ℤ₂^F → Ĝ̃_A → Ĝ_A → 1 restricted to the orbifold group Δ⁺(2,3,8) × ℤ₂^W is **0**. So Ĝ̃_A ≅ Ĝ_A × ℤ₂^F, and the action on fermions is a genuine Aut⁺ × ℤ₂ action.
  - **Descent to the finite group Ĝ_A is CONDITIONAL.** Ĝ_A = (Δ⁺/π₁Σ) × ℤ₂, so π₁(Σ) must lift trivially. That holds if the twisted spinor bundle K^{1/2}_s ⊗ L_R^{1/2} is the trivial (integer-power) bundle of the SUSY structure, which is the ecee2668 §4 premise.
  - This upgrades the KK file's "genuine Aut⁺ action, no double cover" from an assertion to a computed statement on the generating relations.
- **Wall compatibility.** Every Aut⁺ lift commutes with Γ_ρ. Each one is an even product of tangent gammas, so it preserves the HW projection and the 10D wall chirality. PROVED (log [C] rows A, and [E]).

**A5. Anomaly and global issues for A × wall. CONDITIONAL.**
- W is the HW orbifold element, already gauged. Its consistency, meaning the E₈ wall theory, anomaly inflow and twisted flux quantization [G/2π] − λ/2 ∈ H⁴(·; ℤ̃_{w₁}), is the HW/f825dfff premise: CONDITIONAL, not rederived.
- On the S⁴ fibre, λ|_{S⁴} = 0 because p₁(TS⁴) = 0, so the flux statement is N ↦ −N under W. I agree with PP.
- Aut⁺ is used only as a truncation, not gauged, so it needs no new anomaly check (PP item g, agreed).
- The bulk parity anomaly of the Pin⁺ theory cancels by FH Theorem 2.2: CONDITIONAL on the citation and on an m_c structure.
- The setting of the quantum integrand (a ℤ/2 torsor) is OPEN.

**A6 (g). Scope. PROVED as bookkeeping.**
- For the truncation, items (i) bosonic invariance, (ii) δ = 0 and (iii) the extension class suffice. All three hold for Ĝ_A, with the CONDITIONAL premises above.
- Gauging Aut⁺ as an orbifold quotient is not part of OW 8b26c786. It would add fixed points with local groups ℤ₈, ℤ₂ and ℤ₃ acting on Σ and the φ₁-plane, plus twisted-sector and flux questions. That is OPEN and not pursued.

**A verdict: A × wall ℤ₂ passes the Pin⁺ check. CONDITIONAL on:** (1) X spin, with the unique SUSY structure d₀ (ecee2668 §4); (2) descent of the computed extension class from Δ⁺ to Aut⁺; (3) HW consistency of the wall orbifold (f825dfff); (4) FH Theorem 2.2 for the bulk anomaly. It is not PROVED, because the citations and premises are not rederived.

## B. Dressed Group B. Moot under OW 8b26c786 (filed for completeness; nearly done when the choice arrived)
Lifts are taken at a fixed point of a Σ-reflection r. The φ₁-plane uses local Cartesian gammas g8 and g9 at μ₁ = 0, and the coordinate-index table in log [C] uses the bd47ff5e G₄ sets.
- **Bosonic rule.** Log [C], rows (i), (ii), (i′), (ii′). PROVED, given the bd47ff5e index sets.
  - (i) {u, φ₁, x³} and (ii) {u, φ₁, t} are orientation-reversing with G → −G, so they are consistent.
  - (i′) and (ii′) add a φ₂ (O(3)_R det −1) reflection. They are orientation-preserving with G invariant, so they are consistent and need **only a Spin lift** (PP item f, agreed).
  - Bare s {u, φ₁} and s′ {u, φ₁, φ₂} fail the rule. This agrees with PP B1.
  - S⁴ flux N → +N in all dressed cases.
- **δ(g) = 0.** The same J[2] computation as A3, including K. PROVED, given the model.
- **Extension data.** Log [E]; PROVED values, identical for L = TΣ and L = K:

  | dressing | 11D orientation | r̃² | (r̃r̃)⁸ | (r̃r̃)² | (r̃r̃)³ | [W̃, r̃] | class on (Δ*(2,3,8) × ℤ₂^W), χ = orientation character of Isom, w = wall class |
  |---|---|---|---|---|---|---|---|
  | (i) + P | −1 | **−1** = (−1)^F | +1 | +1 | +1 after sign choice | **−1** | χ∪χ + χ∪w |
  | (ii) + T, Lorentzian (PP item e) | −1 | **+1** | +1 | +1 | +1 after sign choice | **−1** | χ∪w |
  | (i′) + φ₂ + P | +1 | +1 | +1 | +1 | +1 | +1 | 0 (split) |
  | (ii′) + φ₂ + T, Lorentzian | +1 | −1 | +1 | +1 | +1 | +1 | χ∪χ |

  - PP's (r̃)² = (−1)^F for P is confirmed.
  - The T case is done directly in Lorentzian signature with the real Majorana rep (T² = M²). It gives +1, which differs from P by the (−1)^F of Wick rotation, as Witten's CRT argument predicts.
  - The m = 3 relation is fixed to +1 by the relative sign of two reflection lifts. The m = 8 and m = 2 relations are sign-independent and equal +1.
- **Decisive point: refinement of PP item (g).** In cases (i) and (ii), **[W̃, r̃] = −1**: the lifts of the commuting elements W and r anticommute. This is a cocycle entry, item (iii), not a gauging-of-r issue. So r does not normalize the gauged subgroup ⟨W̃⟩. It maps the HW projection Γ_ρε = +ε to −ε, which is the opposite 10D wall chirality.
  - Equivalently, r reflects 3 wall-tangent directions, so it reverses the 10D wall orientation. A theory with net chiral content on the wall (E₈ Majorana–Weyl gauginos of one chirality) cannot have that as a symmetry.
  - 2D control (log): T and R each flip chirality, while CRT preserves it.
  - Pin⁻ would not help: the gamma count is the same, and Pin⁻ is in any case excluded in 11D (§0).
  - **(i) and (ii) with the wall ℤ₂: REFUTED**, PROVED in-repo given the HW orbifold premise (f825dfff). **Bulk only, without the wall: CONDITIONAL consistent** (δ = 0, relations lift, FH Theorem 2.2).
- **(i′) and (ii′) commute with W̃.** They are even in wall-tangent directions and preserve the wall chirality. Verdict: CONDITIONAL consistent.
  - OPEN: invariance of the E₈ bundle, preservation of the Killing spinor (that r̃ maps the MN Killing spinors to themselves), and descent of the class.
  - Species are the same as A, with parity labels.
- **Gauging remark (not needed; moot).**
  - The codimension-3 fixed loci of (i) and (ii) have RP² links, with w₂ = a² ≠ 0, so they are not Pin⁺. (They are Pin⁻ by w₂ + w₁² = 0, which is the wrong type.)
  - (i′) and (ii′) have codimension-4 fixed sets with RP³ links, which are spin. Log [Q].
- **Surviving modes.** No case changes the species relative to A. Only 5D parity labels would be added.

## 3. Response to PP 1fe6c574 items (each verified independently)
- (a) **Agree.** W is orientation-reversing. Its lift and relations are done in A1 and A4.
- (b) **Agree.** Pin⁺ ⇔ w₂ = 0 (Kirby–Taylor), and w₂ + w₁² = 0 is Pin⁻. The Majorana argument for Pin⁺ is now in-repo (§0). The earlier RP² remark (w₂ ≠ 0 means not Pin⁺) is consistent with this.
- (c) **Agree and done** (A3).
- (d) **Agree and done** (A4 and §B). One refinement: the extension class must include the W-cross term [W̃, r̃]. That term, not the square, is what decides dressed B.
- (e) **Done** in Lorentzian signature (§B).
- (f) **Agree.** These are the primed variants, Spin-only (§B).
- (g) **Agree for bulk truncation.** One dispute, limited in scope. PP's "(B) dressed: a consistent candidate pending (i)–(iii)" fails at (iii) once the gauged wall element is in Ĝ. No gauging of the dressed element is needed to see the failure. This is moot under OW 8b26c786.

## 4. Labels
| item | label |
|---|---|
| Pin⁺ forced by a real Majorana 32 (Cl(10,1) vs Cl(1,10)) | PROVED |
| A: bosonic rule for W and Aut⁺ | PROVED (given bd47ff5e index sets) |
| A: δ(g) = 0 for g1, g2, J, W | PROVED computation; twisted-spin model CONDITIONAL |
| J fixes all 16 theta characteristics | PROVED |
| A: vertex relations lift to +1; W̃² = +1; [W̃, Aut⁺] = +1; class 0 on Δ⁺ × ℤ₂ | PROVED values; descent CONDITIONAL |
| A: wall chirality preserved | PROVED |
| A × wall passes the Pin⁺ check | CONDITIONAL (premises 1–4 in A) |
| A: integrand setting; Aut⁺ gauging | OPEN; not pursued |
| B (i), (ii) with wall | REFUTED (given the HW premise); moot |
| B (i), (ii) bulk only | CONDITIONAL; moot |
| B (i′), (ii′) | CONDITIONAL; Killing spinor and E₈ bundle OPEN; moot |
| junction | UNSOLVED (unchanged) |
| full KK spectrum | OPEN |

Tally (13 rows, by table order): PROVED 4 (rows 1, 2, 4, 6) · PROVED with a CONDITIONAL premise 2 (rows 3, 5) · CONDITIONAL 3 (rows 7, 10, 11) · OPEN 2 (rows 8, 13) · REFUTED 1 (row 9) · UNSOLVED 1 (row 12).

Pre-distribution correction (disclosed): the first write of this file, at 19:07 CST and never distributed, had the tally "PROVED 4 · PROVED-with-premise 3 · CONDITIONAL 3 · OPEN 1 · REFUTED 1 · UNSOLVED 1", which did not match the rows, and an unfinished sentence about J in A4. Both were fixed before the sidecar was reported.

## 5. Remaining path
A's Pin⁺ obligations are discharged up to the CONDITIONAL premises. Closing those needs:
- a proof of descent (π₁Σ lifts trivially), about 1 h;
- the uniqueness of the SUSY structure (ecee2668 §4), which belongs to the analytic Killing-spinor computation, a few hours;
- the integrand setting, which is a research-level OPEN item.

The next A items are in the erratum and its follow-on (SU(2)_R flat connections). Tip 7cddb188 MATCH.
