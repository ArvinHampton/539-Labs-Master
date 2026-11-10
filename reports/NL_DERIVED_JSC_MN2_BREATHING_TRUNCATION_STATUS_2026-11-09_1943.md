# NL DERIVED: does a consistent MN2 truncation keep the S⁴ breathing mode? Construction, rule-outs, wall counting
2026-11-09, CST (America/Chicago). **NL derived proposal.** Nothing here is adopted. Junction status: **UNSOLVED** (19a88b19), unchanged.
Authority: OW 90cec14c (pursue), OW 36683379 (citations: the math was checked as stated, and no item is PROVED by citation alone), OW 8b26c786 / 49b04146 (scope).
Builds on: …EQUATIONS_MN2_2026-11-09_1935.md (ebdda4b6…), …SHOOT_MN2_2026-11-09_1936.md (358c4b09…), …E4_IDENTITY_SYMBOLIC_PROOF_2026-11-09_1942.md (59a4f05e…), and task-1 file …JUNCTION_SOURCES…_1859.md (9987bdcd…).
Scripts: /workspace/nl-jsc-1939/ (cgr_mn2_identification.py 635a0c55…, log f5525346…; e4_symbolic_proof.py 53104aca…). All have sidecars.

**Tally: PROVED 6 · CONDITIONAL 1 · OPEN 3 · REFUTED 1 · total 11**

## 1. Which published truncation contains our MN2
- **T1 (PROVED; checked against arXiv 1906.08900 eqs. 2.5, 3.1–3.3, 6.1).** Our MN2 (SO(3)×U(1) symmetric, X_a = 2^{−3/5}, X_b = 2^{2/5}, twist on the SO(2) plane) is the maximally supersymmetric AdS₅ vacuum of the Cheung–Gauntlett–Rosen (CGR) N=4 truncation. Their vacuum e^{10λ} = 2 gives T^{ab} = e^{−6λ} = X_a and T^{αβ} = e^{4λ} = X_b. Their Δ = T_ij μ^iμ^j equals our D̃ exactly (cgr_mn2_identification.log; the second "T^ab" label in that log should read T^{αβ}).
- **T2 (REFUTED, by the paper's own construction).** Claim, carried in the 1935 file (E6) and in task-1 notes: "the CJPW 4-vector + 1-hyper, SO(3)×U(1)×ℝ truncation (arXiv 2011.04775) is built on our MN2". It is not. CJPW §4.1 builds it on the 4D N=1 MN solution, which they call "MN1": SU(2)_left × U(1)_right symmetric, metric (4.2) with (3 + cos²ζ). For the 4D N=2 MN solution (ours), CJPW point to the half-maximal truncation instead (CGR and their refs. [39, 14]). So E6 of the 1935 file asked about the wrong truncation. E6 is superseded by T3 below; the 1935 file is not edited.

## 2. Finite truncations: rule-outs
- **T3 (PROVED).** The CGR truncation contains no uniform S⁴ breathing scalar.
  - CGR is 7D maximal SO(5) supergravity reduced on Σ. Its uplift is ds² = Δ^{1/3}ds₇² + g^{−2}Δ^{−2/3}T^{−1}_{ij}Dμ^iDμ^j, with det T = 1 and g a fixed constant.
  - Rescaling the S⁴ block uniformly at fixed squashing needs T → cT, and det(cT) = 1 forces c = 1 (script).
  - Of its 16 scalars, the SO(2)×SO(3)-invariant ones are only φ and λ. ψ^{aα} is a (2,3), ξ^α a (1,3) and 𝒯 a (1,5), so none of them is invariant. φ rescales Σ inside the 7D metric, and λ changes X_a : X_b. Neither is the uniform S⁴ mode.
  - So no subtruncation of CGR that keeps MN2's symmetry has a breathing mode.
- **T4 (PROVED, from P1/P2 of the 1942 file).** Around MN2, the uniform breathing profile is not a linear KK eigenmode. P1 is exact in β, hence also linear in it, so a uniform δβ(r) sources δR_rχ = (3/2)δβ′∂_χ ln D̃ ≠ 0. That term can only be balanced by χ-dependent fluctuations of other fields (squashing, metric, or G₄ with dr∧dχ legs). Any breathing-type mode on MN2 therefore has a nontrivial χ-profile and mixes with those fields.
- **T5 (PROVED; reference: task-1 lemma C1, 1859 file).** Varying squashing alone does not help. Within the 7D U(1)² CLP bulk, which contains the (φ, λ) sector of T3, no M5 or fibre-only E₈ source closes a constant-r face. So the "varying squashing" candidate without breathing is already excluded.
- **T6 (OPEN).** Whether some finite consistent truncation around MN2 contains a breathing-type (S⁴-volume) mode is open.
  - Against: CJPW state they "believe" their list (with the half-maximal one) is the most general set of truncations on these backgrounds. That is a belief, not a proof. T3 and T4 also count against.
  - For: massive truncations that keep breathing and squashing exist for unwarped Sasaki–Einstein / G-structure cases. MN2 is warped, which CJPW's footnote 1 places outside the conventional G-structure argument.
  - No finite candidate was found here.

## 3. The consistent setting that does contain the breathing mode
- **T7 (PROVED).** The sector invariant under H = Poincaré(1,3) × SO(3) × U(1), combined with the local PSL(2,ℝ) of H² compensated by the twist U(1) (descending to Bolza and wall ℤ₂), is a consistent truncation. It is a cohomogeneity-two truncation: all fields are functions of (r, χ).
  - Proof: the 11D equations are H-covariant. So E[Φ] is H-invariant whenever Φ is, and the H-invariant ansatz is the most general H-invariant configuration. The equations therefore close on the invariant components.
  - It contains MN2, β(r,χ), squashing X(r,χ), g_rχ, and G₄ components with dr∧dχ legs. It is infinite-dimensional, i.e. a PDE system rather than a finite truncation.
  - It lies inside the 49b04146 / 8b26c786 scope: everything is invariant under Aut⁺(Bolza) × wall ℤ₂.
- **T8 (CONDITIONAL, on χ-dependent smearing of wall sources being admissible; f825dfff fixes only the total).**
  - In T7 the Israel conditions hold pointwise in χ: k_x(χ), k_Σ(χ), and the three fibre extrinsic curvatures (χχ, S², φ₁).
  - The wall data are the field values at r_w, which are free functions of χ (this includes the "squashing modulus" X(r_w, χ)), plus the source densities n_M5(χ) and n_inst(χ). The only constraint on the densities is ∫(n_M5 + n_inst) = 9760.
  - Israel fixes the normal derivatives. The rr and rχ Einstein equations are constraints on the wall data.
  - So the n_inst/N_M5 split and the squashing modulus become functions of χ, not single numbers.
- **T9 (OPEN).** The count of free wall data against the IR codimension in T7 is open. Both sides are function spaces. A per-harmonic count needs the MN2 KK mass operator on H-invariant (r,χ) modes, which has not been computed. The singlet toy (1936 file, S2–S3) is overdetermined by one condition. Whether the source functions in T8 cure that, harmonic by harmonic, is the open question.
- **T10 (OPEN).** No shoot was done. It is a two-dimensional (r,χ) boundary-value problem with fibre endpoints at χ = 0, π/2 and the MN2 IR. It needs:
  - (i) the H-invariant field equations as PDEs;
  - (ii) the MN2 linearized spectrum in this sector, to fix the IR conditions;
  - (iii) a relaxation solver.
  Doing it reliably was not feasible in this run.

## 4. Junction impact
- No breathing-mode junction solution exists in any finite truncation derived or verified here:
  - the uniform ansatz is refuted (E3) and forbidden in closed form (P2);
  - CGR has no breathing scalar (T3);
  - squashing alone fails (T5).
- The only consistent arena that contains the breathing mode is the cohomogeneity-two PDE sector (T7). Its wall has functional freedom (T8), so the singlet-toy codimension argument does not carry over. Existence there is **OPEN** (T9, T10).
- Correction for the record: CJPW is not a truncation around our MN2 (T2).

## 5. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 6 | T1, T3, T4, T5, T7, plus T0 below |
| CONDITIONAL | 1 | T8 |
| OPEN | 3 | T6, T9, T10 |
| REFUTED | 1 | T2 |

- **T0 (PROVED).** Scope check: every field in T7 is constant along Σ up to the twist compensator. So it is Aut⁺(Bolza)-invariant, and it is kept ℤ₂-even at the wall by construction.
