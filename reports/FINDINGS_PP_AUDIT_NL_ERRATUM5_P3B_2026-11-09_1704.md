# FINDINGS: PP audit of NL erratum 5 (P3b upgrade; fixes F1, F2, F4–F6). 2026-11-09 17:04 CST (America/Chicago)
Agent: Professor Proof (Soft SF). Additive file; nothing edited. Tip 7cddb188 untouched (re-hashed). No CERT. Nothing sent outside (public arXiv source read only). Convention G = ½T^(EH). No MR2 numbers used.
Target: NL_ERRATUM5_JUNCTION_ACCEPT_PP_5cbd050a_2026-11-09_1701.md, sha 59218e611509a3ab4d6e5cc593c51d39d84fdb52cb84e8dd50914372ff8c8d11. It equals its sidecar.
Scratch: /workspace/audit-scratch/pp_p3b_1705/
- pp_p3b_check.py cc84ce8a…, .log 1895c7e2…
- arXiv 1203.0303 source B3W.tex

## Rollup
PROVED 7 · CONDITIONAL 2 · OPEN 0 · PENDING 0 · REFUTED 0. **P3b: PROVED given J1, upgrade ACCEPTED.** Cosmetic fixes: 3.

## Integrity
- **E0 (PROVED).** These match their sidecars:
  - pointwise_p3b.py 577c1946…
  - pointwise_p3b_1701.log 4ce80299…
  - scan_rerun_1700.log 4d4ded4c…
  - scan_rerun_1700.stderr e3b0c442… (empty)
- face.py fd309c48 and scan.py cf7b3354 are unchanged since 1655.

## P3b audit
- **B1 Identity (PROVED, independent).** I computed K^a_a = ½n^r∂_r ln c_a directly from the uplift metric coefficients (B3W eq. near L488: X_i = e^{2λ_i}, ds² = Δ^{1/3}ds₇² + ¼Δ^{−2/3}ds₄², gauge h = f). This gives k_{φ_i} + 2k_x = n^r(2f′ − λ_i′), with sympy residual 0. The Δ′/Δ terms and the μ-dependence cancel.
  - n^r = Δ^{−1/6}e^{−f} > 0 everywhere (Δ > 0 because X_i > 0), so n^r ≠ 0.
  - The lemma condition k_{φ_i} = −2k_x on the open dense set μ₁μ₂ ≠ 0 is therefore equivalent to λ_i′ = 2f′. That holds for both i, because the lemma needs every fibre eigenvalue.
- **B2 (A.15) transcription (PROVED by comparison).** NL's rhs_r matches B3W.tex L1040–1043 (eq. BPSeqns, m = 2 normalization, κ = −1) term by term, signs included.
  - The system is written in the gauge h = f. The condition λ′ = 2f′ is invariant under reparametrizing r, so the gauge choice and the direction of r do not matter.
  - The condition is homogeneous in K, so the orientation of the normal under Z₂ does not matter either.
- **B3 Substitution (PROVED).** With λ₁′ = λ₂′ = 2f′:
  - eq1 gives 5f′ + E = 0, so f′ = −E/5.
  - eq3 becomes −2e^{f+2λ₁} − (1+z)/8·e^{f−2g−2λ₁} = 0. The E-terms cancel exactly.
  - eq4 becomes −2e^{f+2λ₂} − (1−z)/8·e^{f−2g−2λ₂} = 0.
  - E ≠ 0 is **not needed** for the contradiction: the sign of E is never used, only the cancellation.
- **B4 Exhaustive z split (PROVED).**
  - eq3 is strictly negative for z ≥ −1 (closed, not just z > −1 as NL states), because −2e^{f+2λ₁} < 0 and the other term is ≤ 0.
  - eq4 is strictly negative for z ≤ 1.
  - The union is ℝ, with overlap [−1, 1]. So z = ±1 (MN N=2), z = 0 (MN N=1, where λ₁ = λ₂ is consistent with (A.15)) and z = 2, 3 (BBBW) are all covered, as is every truncated flow, since each one still satisfies (A.15).
- **B5 Robustness (PROVED).** Even under the opposite convention X_i = e^{−2λ_i} (condition λ′ = −2f′), eq3 and eq4 pick up an extra −(4/3)E term and stay strictly negative in the same z ranges. So the conclusion does not depend on the λ sign convention.
- **B6 Single radius vs. whole flow (PROVED).** The argument uses only (A.15) evaluated at the face radius r_b and the lemma condition at that same r_b. The flow satisfies (A.15) at every r, including the one-sided limit on the kept IR side. So the contradiction holds face by face, and the condition never has to hold along the flow.
  - This also covers the exact end geometries: at the AdS₅ fixed point λ′ = 0 ≠ 2f′, and at the AdS₇ end λ = 0 with f′ ≠ 0.
- **Verdict.** P3b goes from CONDITIONAL to **PROVED given J1** (CLP/BBBW BPS system, constant-radius faces, smeared pure-M5 source, Z₂). The numerical margins in pointwise_p3b_1701.log (≥ 1.82) are consistent and only supporting.

## Fix checks
- **F1 (CONDITIONAL; consistent).**
  - The last 4 lines of scan_rerun_1700.log are identical to scan.log (diff empty).
  - face.py L84 is a module-level print at column 0, after the `__main__` block at L54, so it runs on import.
  - Byte check: 451 − 400 = 51 bytes = "\n" plus the 50-byte "UV analytic…" line, which matches NL's explanation.
  - The original `tail -4` capture command cannot be re-verified from disk, hence CONDITIONAL.
- **F2, F4, F5, F6 (PROVED, wording matches the request).**
  - F2: the headline is scoped to constant-radius faces, smeared M5 tension, P1–P3; it is explicitly "not a no-go"; and the OPEN list includes P2′, J5, J6, J7.
  - F4: "PROVED given J1", with the exterior being the fixed point of the same CLP U(1)² truncation.
  - F5: P3a is restricted to the exact end geometries.
  - F6: P3e is CONDITIONAL on the Z₂ parity of G₄, which is OPEN.
- **NL tally 12/5/5/1 (CONDITIONAL).** Accepted as bookkeeping. "H PROVED" is right only together with its stated scope and with P2's given-J1 assumption about the exterior.

## Cosmetic fixes requested from NL
- C1. Change "impossible for z > −1" to **z ≥ −1**, and "z < 1" to **z ≤ 1**. The split is still exhaustive; the overlap is [−1, 1].
- C2. State that (A.15) is in the gauge h = f, and that λ′ = 2f′ is reparametrization-invariant. Note that E > 0 is not used.
- C3. pointwise_p3b.py's face list concatenates linspace with uv.t, so faces are double-counted. The "faces" counts overstate the number of distinct faces. This affects the numerical cross-check only.

Tip 7cddb188 untouched. No CERT. Nothing sent outside.
