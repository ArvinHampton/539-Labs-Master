# FINDINGS: PP confirmation of MR2 scalar/vector status and errata (bd32b4e2)
Auditor: PP (Professor Proof). Written 20:36 CST (America/Chicago). Scope: OW d5eaeef3 under OW 8b26c786. Additive; nothing edited or sent; no CERT; no Gemini; nothing adopted. Tip 7cddb188 unchanged.

**Provenance.** MR2_MN2_KK_A_SCALAR_VECTOR_STATUS_AND_ERRATA_2026-11-09.md has sha bd32b4e24e10c54cab1c22a7fb394522ae283ee05143990eff757bee8205da22, sidecar MATCH, mtime 20:31:32. It is text only. The cited PP file 7441335e is correct.

## Checks
| point | verdict |
|---|---|
| (a) undressed-lift qualifier | **FAITHFUL.** It applies to stage-1 RA-3 for the j ≠ 0 q = 0 rows: 12 (triplet), 32 (j = 2), 40 (j = 1), and by "likewise" also 58.157 and 60. It applies to **all** stage-2 charged rows as premise (CL), now the canonical *undressed* lift, and to the §1 selection rule. The j = 0 q = 0 rows (20, 56, and also 66.157) are correctly exempt: they carry no SO(3)_R or U(1) action, so dressing cannot reach them. The cited source is ecee2668 §3 ("Dressing the lifts by R-symmetry elements … OPEN"), verified. |
| (b) "supplements"; RA-5 counted once | **FAITHFUL.** "Replaces" becomes "supplements". The general holomorphic identity is counted only in b75f7e52 (1/0/0/0). Stage 2 stays 3/4/1/0, with row 3 being the original ladder identities. No double count. |
| Scalar/vector masses: OPEN | **CORRECT.** Nothing is computed, and no supermultiplet inference is made. The cited ecee2668 §7 Σ-constant scalars are verified as listed: −4 (Δ = 2), 0 (5-plet, Δ = 4, COND), 12 (Δ = 6). PP independently finds the SO(3)-breaking scalar w at m²L² = 0 exactly in the CGR 3-scalar sector (PP 1aa88a30 audit, Z1), which is consistent with the 5-plet at 0. |
| Group A selection rule: COND | **JUSTIFIED, not overgraded.** The grade rests on a citation and unproved steps, not on floats. (i) ⟨A,B,J⟩ = Aut⁺ rests on ecee2668 §1, "PROVED in-repo except one cited lemma". (ii) The HW premise. (iii) The canonical undressed lift, a stated scope premise. (iv) **One step is asserted, not shown:** "the Σ-side invariant content is the same as for spin-2". That holds for modes that are Σ-scalars of charge q. Scalar and vector fluctuations with Σ-tangent legs (e.g. h_{zz}, A_z, C₃ with a Σ leg) are sections of K^{q+n}-type bundles with shifted weight, and J acts on them with an extra sign; ecee2668 §3 shows J = −1 on harmonic 1-forms. For these modes the rule must use the shifted weight (fix S1). With (iv) unestablished for Σ-legged modes, COND is the right grade. PROVED would be an overgrade. |
| Tally 0/1/1/0 = 2 | **CONFIRMED.** Errata rows 3 and 4 are bookkeeping, not graded. Stage 1 2/4/1/0, stage 2 3/4/1/0 and b75f7e52 1/0/0/0 are unchanged. |

**Verdict: FAITHFUL.** Both b75f7e52 nits are applied correctly, and the grades are correct.

## Residual fixes (minor)
- **S1.** §1: qualify "the Σ-side invariant content is the same as for spin-2". It holds per total Σ-weight (U(1) charge q plus the Σ-tangent index weight n). Modes with Σ legs use K^{q+n}-type invariants with the corresponding J sign (cf. ecee2668 §3), not the spin-2 Σ-scalar list.
- **S2.** The header "Written 20:33 CST" is later than the file mtime of 20:31:32 (the same kind of slip as stage fix 1). Correct it in the next additive file.
