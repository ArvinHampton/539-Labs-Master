# FINDINGS — PP audit of NL_DERIVED_JSC_MN2_KK_OPERATOR_COUNTING_2026-11-09_1948.md (9a29b6da…) — 2026-11-09 (America/Chicago)
Auditor: Professor Proof (PP). Pure math. Labels PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. Float-only results are CONDITIONAL. A citation alone never makes a result PROVED (OW 3f160803 + 36683379). Under OW 90cec14c (GO, not adoption). **Nothing adopted. Junction: UNSOLVED.** No CERT, no sends, no Gemini. Tip 7cddb188 read-only. Lock 96f8d42e §4 stays purged. Nomenclature per OW 81b74a31 (the algebra is not named in this file).

## 0. Integrity
- Target 9a29b6dafa68bc54f86dda2ade0305069b326fdf64102dbefcdb2bd3db2c5699 = sidecar.
- /workspace/nl-jsc-1947/ — every file matches its sidecar:
  - cgr_level0_masses.py 7bf0412d…
  - cgr_level0_masses.log 5ac90deb…
  - selfdual_stress_check.py df221f28…
  - selfdual_stress_check.log b91d362c…
- PP reran cgr_level0_masses.py: the log is **byte-identical**.
- arXiv 1906.08900v2 fetched this run (/workspace/pp-audit-kk/cgr.txt).

## 1. Grades
| item | NL | PP | note |
|---|---|---|---|
| K1 level-0 masses | PROVED | **PROVED** | §2.1 |
| K2 IR codimension | PROVED | **PROVED** (linear, finite truncation, Δ ≠ 4); Δ = 4 sub-clause **CONDITIONAL** | §2.2 |
| K3 higher spectrum | OPEN | OPEN | not computed (correct) |
| K4 C4 face = smeared 5-brane, NEC | PROVED | **PROVED** (exact arithmetic) | §2.3; Y15 reconciliation §3 |
| K5 split drops out | CONDITIONAL | CONDITIONAL | extra hypotheses listed, §2.4 |
| K6 expected dimension −M − n_rel | CONDITIONAL | **OPEN** (the M-scaling of the count is not established); PP's weaker K6′ CONDITIONAL | §2.5 (priority) |
| K7 non-generic/BPS loophole | OPEN | OPEN | relation to C6, §2.6 |
| K8 Group-A scope | PROVED | PROVED | wording, §2.6 |

## 2. Checks
### 2.1 K1
- **Potential.** The script's potential is CGR (3.8) with ψ = 0, T = 1, l = −1: TrT = 3, Tr T² = 3, so the last bracket is 9e^{8λ} − 6e^{8λ} + 12e^{−2λ}. It matches (3.8) term by term.
- **Kinetic normalisation.** CGR (3.7) has −30∗dφ∧dφ − 30∗dλ∧dλ, so the equation of motion is 60□φ = ∂V and m² = V″/60. This is correct.
- **Radius.** In 5D with L = R − V, R_mn = (V/3)g_mn, so V₀ = −12/L². The script gets g²L² = 2·2^{1/3} = 2^{4/3}, matching CGR (6.2). ∇V = 0 at e^{30φ} = e^{10λ} = 2, matching CGR (6.1).
- **Eigenvalues.** m²L² = {12, −4} exactly. Δ(Δ − 4): 6·2 = 12 and 2·(−2) = −4.
  - Δ = 2 sits exactly at the BF bound (m²L² = −4), so the two roots coincide (Δ₊ = Δ₋ = 2).
- **Independent confirmation in the paper.** CGR §6.1 (p. 22) states that "the φ, λ equations … give rise to two scalars with m²L² = −4, 12 … dual to scalar operators with Δ = 2, 6". (This is a citation; the PROVED grade rests on the recomputation.)
- **H-invariance.** φ and λ are SO(2)×SO(3) singlets and constant on Σ, so they are PSL(2,ℝ)-invariant. Both lie in the T7 sector.
- The T scalars (Δ = 4) are a 5 of SO(3), not singlets, so they are correctly excluded. **PROVED.**

### 2.2 K2 (priority)
- **Setup.** Take a domain-wall flow whose **IR end** is the MN2 AdS₅ point, at the Poincaré interior z → ∞ (equivalently r → −∞ with metric dr² + e^{2r/L}dx²). The linear radial solutions are z^{4−Δ} and z^{Δ}.
- **Mode by mode:**
  - **Δ > 4 (irrelevant):** z^{4−Δ} decays and z^Δ grows. Regularity kills one coefficient: **codimension 1.**
  - **2 ≤ Δ < 4 (relevant, standard quantisation):** both branches grow, so both coefficients must vanish: **codimension 2.**
  - **BF bound Δ = 2:** the double root gives z², z² ln z. Both grow, so **codimension 2**, as NL says.
  - **Alternate quantisation (1 ≤ Δ₋ < 2):** the exponent pair {Δ₋, 4 − Δ₋} is the same pair of positive numbers. Both branches still grow in the IR, so it is still codimension 2. Quantisation choice is a condition at the conformal boundary, and here that end is replaced by the wall, so it **does not change the IR count.**
  - The rule "a source/vev pair per mode, with IR regularity fixing one" is the Δ > 4 case only. For relevant modes at an IR endpoint, regularity fixes **both**.
  - **Direction of flow:** counting 2 per relevant mode is correct for a flow *into* the point (IR end). For a flow *out of* the point (UV end, at z → 0) the count would be reversed: normalisability fixes one coefficient per mode, and relevant modes are the free deformations. NL's setup is the IR-end case, so 2 is right.
  - **BF-violating modes:** these have complex exponents with Re = 2, both growing. None occur at level 0, and higher-KK stability of MN2 is assumed via supersymmetry (part of K3).
- **Marginal Δ = 4.** The branches are a constant and z⁴. Only the constant survives, and it does not decay. It is allowed only if the mode is exactly marginal and the IR endpoint may move along the conformal manifold. If the endpoint is pinned to exactly MN2, it costs 2. Marginally (ir)relevant cases have log running and need a nonlinear analysis.
  - NL's "1 per Δ ≥ 4" is therefore **CONDITIONAL** for Δ = 4.
  - No H-invariant level-0 mode has Δ = 4, so K1 is unaffected. Higher levels (K3) might have such modes.
- **Nonlinear statement.** In a finite χ-truncation where the fixed point is hyperbolic (no Δ = 4 modes), the stable-manifold theorem upgrades the linear counts to codimensions of a smooth IR-regular set. For the untruncated PDE the "dimension" is formal.
- **Cross-check.** This agrees with the singlet toy. There, the two irrelevant modes give W^s of dimension 2 inside the 4D constraint surface (PP pp_stable_manifold.log: stable eigenvalues 2 − 2√3 and 2 − 2√13).
- **Grade:** PROVED (linear, Δ ≠ 4, finite truncation). The Δ = 4 clause is CONDITIONAL.

### 2.3 K4
- With S^a_b = −(2/κ²)(K^a_b − δ^a_b K) (aeb9ab13) and K = diag(k ×4 on x, k ×2 on Σ, −2k ×4 on the fibre), trK = −2k.
- That gives S on x and Σ = −6k/κ² and S on the fibre = −(2/κ²)(−2k + 2k) = 0. So ρ = −S^t_t = 6k/κ², P_x = P_Σ = −ρ, P_fib = 0 (exact).
- This is the stress of a pure-tension 6D brane on ℝ^{1,3} × Σ, smeared over S⁴ (an M5).
- NEC for null vectors along x, Σ and the fibre: ρ + P_x = ρ + P_Σ = 0 and ρ + P_fib = ρ, so the NEC holds iff k ≥ 0.
- This agrees with PP 1935 §1.2 (κ²ρ = 6k_x, S_fib = 0).
- **PROVED.** It is the face kinematics only. Two caveats:
  - The sign condition k_x > 0 is a requirement on the bulk solution at the face. No bulk solution exists yet.
  - "Tension = charge" is still OPEN on the twisted S⁴ (E16-F3).

### 2.4 K5
- Self-dual F on a Euclidean 4-plane has vanishing 4D YM stress. The script checks this on 3 random samples at ≤ 4.4e-16 (float). The standard identity F_acF_bc = ¼δ_ab F² for (anti-)self-dual F makes it exact.
- Along x and Σ (no F legs) T_μν = −¼g_μν F², i.e. ρ = −P = ¼F² ≥ 0, which is M5-like. Both statements are correct.
- **Hypotheses needed beyond NL's:**
  - (i) self-duality must hold with respect to the *squashed, fibred* S⁴ metric at the face (X_a ≠ X_b, twisted over Σ);
  - (ii) the existence of an H-invariant (up to gauge) self-dual E₈ connection there (cf. E16-A5a);
  - (iii) the orientation (instanton vs anti-instanton) must match the M5 charge sign;
  - (iv) the instanton density n_inst(χ) is fixed by the connection and is not freely smearable like n_M5(χ). So the split can still restrict which n(χ) are reachable, even if it drops out of the equations;
  - (v) this holds at leading order only: the HW −½ tr R² and the G₄ boundary condition are not included.
- **Grade: CONDITIONAL**, as NL has it.

### 2.5 K6 (priority): the constraint count
- **(a) Momentum constraint as force balance.** At the ℤ₂ wall, Codazzi plus Israel give D_aS^a_χ = −[T_nχ].
  - For brane-type S^a_b = −σ(χ)P^a_b (P is the projector onto x × Σ), P^a_χ = 0, so D_aS^a_χ = σ(χ)·∂_χ ln√det h_{x×Σ}.
  - Force balance therefore reads **σ(χ)∂_χ ln(e^{4A}e^{2C})|_w = (bulk T_nχ term)**. It is *algebraic* in σ, not a differential equation for n(χ).
  - Where σ ≠ 0, it mainly constrains the χ-gradient of the worldvolume warp factors at the wall. It "fixes n(χ)" only if those gradients are given.
  - The count of M − 1 conditions is fine. NL's interpretation is imprecise (fix K3).
- **(b) Independence from the junction.** Given the Israel conditions, the bulk momentum constraint at r_w and the conservation of S are the **same** condition, so it must be counted once. NL does count it once.
  - Independence from the Hamiltonian constraint (the nn component, quadratic in K and σ) is generic but not shown.
  - Independence of both from the Ñ junction equations is an assumption (fix K4).
- **(c) The M-scaling — not established.** NL works in a *reduced* phase space of dimension 2N and then subtracts M Hamiltonian and (M − 1) momentum conditions at the wall.
  - In a reduced phase space those constraints are already solved. Re-imposing them at the wall is legitimate only for directions where the junction fixes a momentum that has **no value partner** in the reduced space.
  - In the toy that is A′: its value partner A is removed by the global dilatation. That is exactly why the toy wall curve is 1-dimensional and the toy count is −1. PP verified this directly: the 5D system (A′, B, B′, C, C′) has a 4D constraint surface, and the wall set is 1D.
  - For harmonics m ≥ 1, the warp-type values A_m(χ) are **not** removable by any global symmetry. Their momenta have value partners, and the constraints H_m and P_m are already solved.
  - Counted that way (wall values free, all momenta fixed by Israel, constraints imposed once, tangential χ-diffeos quotiented), PP obtains a wall image of dimension N − 1 + [(M − 1) source harmonics − (M − 1) force-balance conditions] = **N − 1**. That gives an expected dimension of **−1 − n_rel**, not −M − n_rel.
  - Both counts reproduce the toy at M = 1 (−1, with n_rel = 0). They differ for M ≥ 1 harmonics, and the single calibration point cannot decide between them.
  - **The claim "≤ −(M + 1)" is OPEN.**
- **(d) Theorem or heuristic?** "Expected dimension" is a **heuristic**. A theorem would need the following, none of which is provided:
  - a Fredholm set-up of the (elliptic in (r, χ)) wall-to-IR boundary-value problem;
  - its index;
  - transversality, i.e. Sard–Smale genericity over some parameter space.
- **(e) What a negative count proves.** A negative expected dimension does not prove non-existence. Non-generic solutions can exist: symmetric, BPS or calibrated ones (K7), or points where the constraint maps drop rank. There is also no generic family here, since the physical data are fixed numbers (N = 4880, 9760, Bolza), so "generic" has no parameter space to range over.
- **Grades:**
  - K6 as stated (≤ −(M + 1), so overdetermined by at least M + 1): **OPEN.**
  - **K6′ (PP, weaker): expected dimension ≤ −(1 + n_rel) ≤ −2**, using n_rel ≥ 1 from the H-invariant Δ = 2 mode (K1 + K2). This holds under either count. It is **CONDITIONAL** (heuristic; on χ-smearing; on independence (b)).
  - Non-existence: **not established** either way.

### 2.6 K7, K8, and NL §5
- **K7: OPEN.** PP's C6 (1935 §1.2) shows a BPS M5 wall (q² = 1) exists for **flat Σ only**; on H² it fails by the Σ curvature. So the simplest BPS loophole is already obstructed in the cohomogeneity-one class. χ-dependent BPS walls in the T7 sector are not excluded.
- **K8: PROVED.** Wording: G₄ components are ℤ₂-*odd* (with C → −C). "Even under the wall ℤ₂" should read "invariant under the wall ℤ₂ acting as (ρ, C) → (−ρ, −C)".
- **NL §5** says "the breathing-mode route … is generically closed … cannot reduce the deficit below M + 1". **This is an overclaim.** It rests on K6 (OPEN as stated) and on a heuristic that does not prove non-existence. The supportable statement is "heuristically overdetermined by ≥ 1 + n_rel ≥ 2 (CONDITIONAL); not closed."

## 3. K4 vs Y15 ("E₈ + smeared M5 gives the wrong signs")
- Y15's result file is **not on disk**. The AUDITOR addenda list Y15 as OPEN or NOT FOUND, and only the Y15 interval (2489, 6510) is recorded as REFUTED. PP cannot grade Y15 itself.
- **No tension, if Y15 refers to the exact-MN2 face.** Exact-MN2 faces require 6:8:8 with a nonzero fibre weight −8k and a null-energy deficit Σ|σ_neg| ≥ ρ_w/3 (aeb9ab13; MR2 batch1 L3, PP 1948). On those faces smeared M5/E₈ content *does* have the wrong signs. This is consistent with the on-record REFUTED "smeared-M5 Israel on exact end faces (P3a)".
- **K4 is about different face data.** K4 concerns the breathing C4 data (k_fib = −2k_x, λ′ = 0, g′ = f′), on which the required fibre stress is **zero** and the smeared M5 has the right sign iff k_x > 0.
- **Explicit tension, if Y15 claims wrong signs for the C4 data themselves.** K4 is exact arithmetic in the aeb9ab13 convention, so such a Y15 claim would have to be using:
  - (i) the opposite normal orientation, which flips ρ → −ρ; or
  - (ii) the bulk sign k_x < 0 at the face; or
  - (iii) extra stress (HW −½ tr R², G₄ boundary terms) not in K4.
- K4 does not establish k_x > 0 for any actual bulk solution. Y15 must state its face data and convention (fix K7).

## 4. Rollup
- **NL:** PROVED 4 · CONDITIONAL 2 · OPEN 2 · REFUTED 0 (= 8). The header matches the table.
- **PP:** **PROVED 4 (K1, K2, K4, K8) · CONDITIONAL 1 (K5) · OPEN 3 (K3, K6, K7) · REFUTED 0.**
- PP's new items: K6′ CONDITIONAL; the K2 Δ = 4 sub-clause CONDITIONAL.
- NL §5's "generically closed" is not supported.
- Junction **UNSOLVED**.

## 5. Fix list for NL
1. **K1:** state that Δ = 2 is a BF-saturating double root (z², z² ln z) and that alternate quantisation does not change the IR count.
2. **K2:** restrict "1 per Δ ≥ 4" to Δ > 4. Δ = 4 counts 1 only if exactly marginal with a movable endpoint; otherwise 2; log cases need nonlinear analysis. State the finite-truncation and hyperbolicity hypotheses for the nonlinear statement.
3. **K3 (wording of K6):** force balance is σ(χ)∂_χ ln√h_{x×Σ}|_w = bulk T_nχ term. It is algebraic in σ and constrains warp gradients. It is not a free equation "fixing n(χ)".
4. **K4:** state independence of the Hamiltonian constraint, the momentum constraint and the junction equations as an explicit hypothesis, or prove it, e.g. by a rank computation at M = 2.
5. **K5:** justify (or retract) subtracting H_m and P_m in the reduced phase space for harmonics m ≥ 1. PP's alternative count gives −1 − n_rel. Do the count explicitly at M = 2 with all metric functions, including the A_m values, and the wall-shape gauge.
6. **K6:** relabel "expected dimension" as a heuristic. Non-existence needs a Fredholm/transversality argument or an explicit obstruction. Retract "generically closed" in §5; replace it with "heuristically overdetermined (≥ 1 + n_rel), not closed".
7. **K7:** for the Y15 reconciliation, specify the face data (exact-MN2 vs C4) and the normal orientation used for any "wrong signs" claim. K4 holds for the C4 data in the aeb9ab13 convention.
8. **K8:** fix the parity wording (G₄ is odd; the sector is invariant under (ρ, C) → (−ρ, −C)). Add the K5 hypotheses (i)–(v).
9. **K9:** in K7, cite PP C6 (a BPS M5 wall needs flat Σ) as an obstruction to the simplest BPS loophole.

Tip 7cddb188 untouched (read-only). No CERT. Nothing sent. Nothing adopted.
