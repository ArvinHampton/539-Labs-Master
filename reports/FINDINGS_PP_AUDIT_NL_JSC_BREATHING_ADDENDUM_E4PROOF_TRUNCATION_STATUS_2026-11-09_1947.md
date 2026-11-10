# FINDINGS (ADDENDUM) — PP audit of NL JS-C files 1942 (E4 symbolic proof) and 1943 (MN2 breathing-truncation status), folded into the JS-C breathing audit — 2026-11-09 (America/Chicago)
Auditor: Professor Proof (PP). **Additive addendum to FINDINGS_PP_AUDIT_NL_JSC_BREATHING_EQUATIONS_SHOOT_ERRATUM_2026-11-09_1944.md (sha 3982a4b8c878e3861cd3bd01cca9b339774069ebc95445ad53a2ba558fa6293c), which is not modified (never-overwrite rule); read the two together.** Under OW 90cec14c (GO, not adoption). Pure math; labels PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. **Nothing adopted. Junction: UNSOLVED.** No CERT, no sends, no Gemini. Tip 7cddb188 read-only. Lock 96f8d42e §4 stays purged. Citation scope OW 3f160803 + 36683379 applied (a citation alone never upgrades). Nomenclature per OW 81b74a31.

## 0. Integrity
- NL_DERIVED_JSC_E4_IDENTITY_SYMBOLIC_PROOF_2026-11-09_1942.md 59a4f05e72337ae35bd72e6f840d41a052399435f4c77d8d4be062df67cd000b = sidecar.
- NL_DERIVED_JSC_MN2_BREATHING_TRUNCATION_STATUS_2026-11-09_1943.md b103f08fc425c3a3f03aa20f9c3a8670ac50aae81bfe5b50b90fd9e5c2f5323c = sidecar.
- /workspace/nl-jsc-1939/: cgr_mn2_identification.py 635a0c55… / .log f5525346…, e4_symbolic_proof.py 53104aca… / .log 635938d0… — all MATCH. cgr_mn2_identification.py rerun by PP: byte-identical log. e4_symbolic_proof.py not rerun (PP used its own independent script, below).
- PP independent script: /workspace/pp-audit-jsc/pp_Rrchi_closed.py (62f0ac90…), log d1069926… (own metric build, own Christoffels, f, g, β arbitrary functions, γ, X_a, X_b symbolic).

## 1. File 1942 — E4 identity
- **P1 — PROVED (independently reproduced).** PP's own sympy gives R_{rχ} = 3(X_a−X_b) sin 2χ β′ / [(X_a+X_b) + (X_b−X_a)cos 2χ]. Since X_a+X_b+(X_b−X_a)cos 2χ = 2(X_b cos²χ + X_a sin²χ) = 2D̃, this is **exactly 3(X_a−X_b) sin 2χ β′/(2D̃) = (3/2)β′∂_χ ln D̃**, as NL states. It is independent of γ, f, g and β″. PP's run had a₁ = 1; NL's has a₁ symbolic. Both give the same result.
- **P2 — PROVED (T_{rχ} = 0 checked term by term).**
  - Einstein (trace-reversed): R_{MN} = (1/12)(G_{MPQR}G_N{}^{PQR} − (1/12)g_{MN}G²). The Chern–Simons term is metric-independent, so it never enters the Einstein equation.
  - g_{rχ} = 0, so the G² term drops. G₄ has no r-leg, so G_{rPQR} = 0. The inverse metric has g^{rM} = 0 for M ≠ r (the only off-diagonal entry is g_{φ₁u}, with no r index), so raising indices produces no metric mixing. Hence T_{rχ} = 0 identically.
  - The G₄ ansatz also satisfies its own equations for any β(r): dG₄ = 0 (r-independent, no dr leg); d⋆G₄ = 0 because ⋆G₄ is the MN2 7-form (which already contains dr) times a function of r only; and G₄∧G₄ = 0 because G₄ lives entirely on the 6 internal directions. So the CS term does not obstruct either. **The only failing equation is the rχ Einstein equation.**
  - **Zeros of sin 2χ:** χ = 0, π/2 are the degenerate-orbit endpoints, where R_{rχ} vanishes automatically. Because β′ depends on r only and sin 2χ ≠ 0 on the open interval (0, π/2), the equation still forces **β′ ≡ 0**.
  - **X_a = X_b:** R_{rχ} ≡ 0 for every β. This is consistent with the singlet class (E1). But X_a = X_b is not MN2, and the remaining equations are not checked there.
- **P3 — PROVED in substance; one parenthetical is REFUTED by counterexample.**
  - NL writes: "at γ = −½ C4 has no solution at all". That is false. PP's exact face linsolve (FINDINGS_PP_AUDIT_NL_t4407_…_1935 §1.2; pp_israel_face_round.log) gives, at γ = −½, the family f′ = g′ = λ′ = 0 with β′ free, k_x = −β′/2, k_fib = −2k_x. For example β′ = −2 gives k_x = 1 > 0.
  - That branch also needs β′ ≠ 0, so P2 kills it too. **The conclusion (no uniform-ansatz realization on MN2, for every γ) stands.**
- **Effect on 1935:** E4 and E10 are PROVED. PP had already upgraded both in the 1944 file, and NL now concurs. E3 REFUTED is unchanged; P1 is its general form.
- **Tally 3/0/0/0:** PP **3/0/0/0**, with the P3 parenthetical corrected (fix A1).

## 2. File 1943 — MN2 breathing-truncation status
- **T1 — PROVED (verified against the paper's formulas, arXiv 1906.08900v2, fetched this run).**
  - CGR (2.5): ds² = Δ^{1/3}ds₇² + g^{−2}Δ^{−2/3}T⁻¹_{ij}Dμ^iDμ^j, with Δ = T_{ij}μ^iμ^j.
  - CGR (3.3): T^{ab} = e^{−6λ}δ^{ab} on the SO(2) plane and T^{αβ} = e^{4λ}𝒯^{αβ}.
  - CGR (3.2): A^{ab} = ω̄^{ab}/g, i.e. the twist sits on the SO(2) plane. In our language that is the φ₁ plane, a₁ = 1.
  - CGR (6.1)–(6.2): e^{10λ} = 2, e^{30φ} = 2, g²L² = 2^{4/3}, with 𝒯 = 1.
  - **PP's independent cross-checks against PP's own MN2 (mr2_core / pp_einstein, 384096a8 pipeline), with g = 2:**
    - (i) T^{ab} = 2^{−3/5} = X₁ and T^{αβ} = 2^{2/5} = X₀ = X₂. D̃ = X_a sin²χ + X_b cos²χ (NL script, rerun identical).
    - (ii) 7D AdS₅ radius²: e^{−4φ}L² = 2^{−2/15}·2^{4/3}/4 = **2^{−4/5}** = PP's ef² = X₀^{−2}. This matches L₅/L₇ = 2^{−2/5}.
    - (iii) 7D Σ radius²: e^{6φ}/g² = 2^{1/5}/4 = PP's e2g = X₁X₂²/4 at z = 1.
    - The metric identification is therefore exact.
  - G₄: CGR (2.6) with DT = 0, S₍₃₎ = 0 and F = the twist is the same uplift family PP's gate used (the Cvetič et al. formula of CGR ref. [14]). PP did not redo a component-by-component comparison of the 4-form here, so the flux part rests on the formula identity (fix A2: add a component check). Grade: PROVED (metric, scalars, radii); flux component match CONDITIONAL (formula identity, not recomputed).
- **T2 — REFUTED claim upheld (verified from arXiv 2011.04775, fetched this run).**
  - CJPW §4.1 "The MN1 solution" is the MN solution that is 5D N=2 / dual 4D N=1. Its symmetry is SU(2)_left × U(1)_right, and its metric (4.2) contains (3 + cos²ζ).
  - The paper says explicitly that the 5D N=4 MN solution (our MN2, 4D N=2) has a structure "embed[ded] in USp(4) ⊂ USp(6)" leading to **half-maximal** supergravity, citing [39, 14].
  - So the claim "CJPW is built on our MN2" is false.
  - **The 1935 E6 question is moot:** E6 OPEN should be closed as "premise REFUTED" and replaced by T6.
  - Naming note (no grade change): CJPW's "MN1" is the project's MN1 (X₁⁵ = 3/4 in mr2_core).
- **T3 — PROVED (given CGR's field content as published).**
  - det T = 1 forbids uniform rescaling of the S⁴ block (det(cT) = 1 ⇒ c = 1, NL script).
  - SO(2)×SO(3) singlets in CGR (3.2)–(3.4): only φ and λ. 𝒯 is a 5 of SO(3), ψ^{aα} is a (2,3), ξ^α/χ^α are (1,3); none is a singlet.
  - Of these, φ rescales Σ inside ds₇ and λ is the squashing.
  - So no CGR subtruncation with MN2's symmetry contains a uniform breathing mode.
- **T4 — PROVED (linear order).**
  - Around MN2, the fields f(r), g(r), λ(r) of the CLP sector form a consistent truncation, so their contribution to (R − T)_{rχ} vanishes identically.
  - A uniform δβ(r) therefore leaves δ(R − T)_{rχ} = (3/2)δβ′∂_χ ln D̃ ≠ 0 (P1, linear in β).
  - This must be balanced by fields outside CLP + β. In the SO(3)×U(1)×(lifted PSL(2,ℝ))-invariant sector those are the non-constant χ-harmonics, or G₄ components with dr∧dχ legs. So any breathing-type eigenmode has a nontrivial χ-profile and mixes with them, as NL states.
  - Wording fix A3: "χ-dependent" should be "non-constant χ-harmonic or dr∧dχ G₄ components".
- **T5 — PROVED** within the scope of 1859 C1 (PP 1935 §1.1: cohomogeneity-one, r-independent twist, M5 on x×Σ, twist-adapted frame).
- **T6 — OPEN.** Correct. CJPW's "believe" is not a proof (and the citation does not upgrade anything).
- **T7 — PROVED (EOM-level symmetry argument; NL's proof is valid).** Consistency is not merely asserted: the argument is the standard EOM-level one.
  - The group H is: Poincaré(1,3); SO(3) acting on μ^{3,4,5}; U(1) rotating φ₁; and PSL(2,ℝ) on H², lifted to the φ₁-circle bundle. The lift exists because the twist bundle is associated with the frame bundle of H², on which PSL(2,ℝ) acts.
  - Every element of H is a symmetry of 11D supergravity (isometries with G₄ invariant), so E[Φ] is H-invariant whenever Φ is.
  - Setting E[Φ] = 0 on invariant Φ is then exactly the reduced system, and every reduced solution is a full solution.
  - **Compactness / Palais is not needed** at the EOM level. Palais is needed only to derive the reduced equations from a reduced action. NL should not claim the action-level statement (fix A4).
  - Generic H-orbits on S⁴ are 3-dimensional (S² × S¹), so the invariant fields depend on (r, χ). Cohomogeneity two holds.
  - **Bolza:** PSL(2,ℝ)-invariant fields are invariant under every element of PSL(2,ℝ), so they are invariant under Γ (and descend to H²/Γ) and under Aut⁺(Bolza) ⊂ N(Γ)/Γ. Finiteness of the Bolza group is no issue. Caveat: the sector is *locally homogeneous*, so it is strictly smaller than the full Aut⁺(Bolza)-invariant sector of 49b04146 / 8b26c786. It is a consistent subsector of that scope, not all of it.
  - **Wall ℤ₂ (ρ → −ρ, C → −C):** this is a symmetry of the 11D action including the CS term (orientation reversal with C → −C), and it commutes with H. So the H × ℤ₂-invariant sector is also consistent in the bulk.
  - **HW compatibility — CONDITIONAL.** The HW boundary condition fixes the tangential (ℤ₂-odd) G₄ at the plane in terms of tr F² − ½ tr R². tr R∧R restricted to the face is built from the H-invariant metric, so it is H-invariant. Compatibility therefore requires the E₈ configuration and the M5/instanton source densities to be H-invariant (up to gauge), e.g. a spin-connection-type embedding. That is a hypothesis on the sources (the same as T8), not part of T7's bulk proof (fix A5).
- **T8 — CONDITIONAL** (correct). It rests on χ-dependent smearing of the wall sources being admissible. f825dfff fixes only ∫(n_M5 + n_inst) = 9760. Pointwise-in-χ Israel conditions (k_x(χ), k_Σ(χ), three fibre curvatures) are the right structure in the H-invariant sector. Localized M5s break H, so the smeared idealization is essential.
- **T9, T10 — OPEN** (correct).
- **T0 — PROVED** (trivial), with the T7 caveat: invariance holds, but the sector is a proper subsector of the KK scope.
- **Log-label slip:** the second "T^ab" line in cgr_mn2_identification.log is T^{αβ} = 2^{2/5}. The values are right and the label is wrong (NL already notes this). No grade impact.
- **Tally:** header 6/1/3/1 = 11 matches the table (T0, T1, T3, T4, T5, T7 / T8 / T6, T9, T10 / T2). **PP: PROVED 6 (T1's flux sub-part CONDITIONAL as noted), COND 1, OPEN 3, REFUTED 1**, i.e. it agrees, with fixes A2–A5.

## 3. How 1935/1936 grades change (PP rollup update)
| item | PP 1944 grade | PP grade after 1942/1943 |
|---|---|---|
| E3 | REFUTED | REFUTED (general form P1; forces β′ ≡ 0) |
| E4 | PROVED | PROVED (NL proof concurs; independent PP proof) |
| E6 | OPEN | **closed: premise REFUTED (T2); superseded by T6 (OPEN)** |
| E10 | PROVED | PROVED (P3; γ = −½ branch also excluded by β′ ≡ 0) |
| E5 | OPEN | OPEN, narrowed: finite-truncation route mostly blocked (T3, T4, T5); cohomogeneity-two setting exists (T7) |
| S3 / S6 | CONDITIONAL / OPEN | The singlet-toy codimension heuristic **does not carry over** to MN2 (T8: functional wall data). S6's "extra modulus" remark is superseded by T8/T9. |
| S5 | OPEN | OPEN |
- **Combined PP rollup across the five JS-C files (1935, 1936, 1942, 1943, erratum):** PROVED 19 · CONDITIONAL 3 · OPEN 6 · REFUTED 2 (E3, T2), plus the erratum record check and one REFUTED parenthetical in P3 (not counted as an item). Counting: 1935 = 8/0/2/1 with E6 moved from OPEN to closed (premise refuted, not re-counted) → 8/0/1/1; 1936 = 2/2/2/0; 1942 = 3/0/0/0; 1943 = 6/1/3/1. Total 19/3/6/2.

## 4. Against PP's §1.4 deliverables (update)
- Item 1 (truncation): **partly met.** T7 gives a proved-consistent arena (the cohomogeneity-two PDE sector, option (b) of §1.4). The PDEs themselves are not yet written, and no finite truncation exists (T3–T5).
- Items 2, 5, 6, 8: not met (T9, T10 OPEN). Item 3: met only in the singlet class (E7, E8). Item 4: partly met. Item 7: met with the T7 caveat (a proper subsector of the scope).
- **Junction: UNSOLVED.**

## 5. Fix list for NL (addendum)
1. A1 (1942 P3): delete "at γ = −½ C4 has no solution at all". Replace it with: "at γ = −½ the C4 branch is f′ = g′ = 0, β′ free (k_x = −β′/2); it also needs β′ ≠ 0 and is excluded by P2."
2. A2 (1943 T1): add an explicit component comparison of CGR (2.6) with the PP/CLP G₄ used in 384096a8, or state that the flux identification rests on the formula identity.
3. A3 (T4): replace "χ-dependent fields" with "non-constant χ-harmonics or G₄ components with dr∧dχ legs".
4. A4 (T7): state that the proof is at the level of the equations of motion (covariance), which needs no compactness. Do not claim an action-level (Palais) reduction.
5. A5 (T7/T8): state that HW compatibility requires H-invariant (up to gauge) E₈ data and source densities. State that the T7 sector is a locally homogeneous proper subsector of the 49b04146/8b26c786 scope.
6. A6 (1935 E6): record E6 as closed (premise refuted by T2), superseded by T6.
7. A7 (log): correct the T^{αβ} label in cgr_mn2_identification.log in a new additive log (do not edit the existing one).
8. A8 (next): for T10, deliver the H-invariant PDEs with exact residual checks, the MN2 linearized spectrum in the (r, χ) sector (IR conditions), and a relaxation solve with error control, as listed in PP 1935 §1.4.

Tip 7cddb188 untouched (read-only). No CERT. Nothing sent. Nothing adopted.
