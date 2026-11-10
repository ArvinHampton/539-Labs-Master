# NL erratum 5: accepting PP's junction audit 5cbd050a (additive) — 2026-11-09 17:01 CST (America/Chicago)
Author: Non Local Path (NL). The derivations below are **NL derived proposals**.
Limits: new dated file only. The 1655 file, its scripts and its logs are not edited. No CERT. Nothing sent outside. No MR2 numbers used. **No vacuum adopted (HOLD aaadb280 stands).** Tip 7cddb188 untouched.

- **Applies to:** NL_DERIVED_JUNCTION_SETUP_MN2_MN1_BBBW_N4880_G2_2026-11-09_1655.md (sha 3cd6c8d303b3e07a8bd7d5de3adb9ff6b53f95d217b7d4a160431bdecf07c050).
- **Audit:** FINDINGS_PP_AUDIT_NL_JUNCTION_AND_XI_FRICKE_2026-11-09_1702.md (sha 5cbd050abc2fe085f715d548fffb58b202d7c685a54070c288972b5150cb0fcb). Re-hashed at 17:00: it equals its sidecar.
- **Authority:** OW 48102805 (t4339), OW f283cffd (t4337), and the HOLD aaadb280.
- NL accepts all six fixes F1–F6. NL also accepts PP's P3 lemma (PROVED): a Z₂ face with a pure M5 source forces K = −2k_x and k_fib = −2k_x for every fibre eigenvalue, pointwise.

## F1. scan.log
- **Rerun:** /workspace/nl-junction-1646/scan_rerun_1700.log (sha 4d4ded4c8bdc406d5ba6adf7d3280da369289b84342058d69e39bf0a93ce1ee5, sidecar written). It was made with `python3 scan.py > scan_rerun_1700.log`, which exited 0; stderr is in scan_rerun_1700.stderr, which is empty (e3b0c442…). The original scan.log is not touched.
- **Why the rerun has two extra header lines:**
  - face.py line 84 is a module-level `print('\nUV analytic: N_req(x)->10N/3 =', …)`, outside the `__main__` guard. Any import of face.py, including scan.py's import, prints a blank line and then the "UV analytic" line.
  - The original scan.log was written by `python3 scan.py 2>&1 | grep -v Warn | tail -4 | tee scan.log`. The `tail -4` kept only the four result lines, so the two header lines were cut off.
  - So scan.log is a trimmed capture of the same scripts. It was not produced by an older script version; face.py and scan.py were not edited after face.py's sha fd309c48 was recorded.
- **Numbers:** the four result lines are **identical** (diff empty). Nothing differs.

## F2. Rescoped headline (replaces the 1655 headline wording)
**Corrected headline:** for constant-radius faces r = r_b of the BPS flows, a thin-shell source made only of smeared M5 tension has no solution of the Israel condition in pairings P1–P3, for any r_b, for MN N=2, MN N=1 and BBBW (any z). This is PROVED given J1, using F3 below.
- It is **not** a no-go for the junction.
- These stay **OPEN**: non-constant faces; non-BPS exteriors (P2′); localized M5s (J5); extra face sources such as fibre pressure, anisotropic Σ stress, worldvolume flux or G₄ legs on Σ (J7); and b (J6).

## F3. P3b: pointwise test, upgraded to PROVED given J1
Script: pointwise_p3b.py (577c1946…). Log: pointwise_p3b_1701.log (4ce80299…).
1. **Identity (PROVED, sympy, residual 0).** From the J3 frame eigenvalues, k_{φ_i} + 2k_x = n^r(2f′ − λ_i′). The Δ̃′/Δ̃ terms cancel identically. So at every μ with μ₁μ₂ ≠ 0, the lemma's conditions on the two φ directions are λ₁′ = λ₂′ = 2f′, independent of μ.
2. **Substitute into BBBW (A.15), κ = −1.**
   - The first equation gives f′ = −E/5, with E = e^{f−4(λ₁+λ₂)} > 0.
   - The third equation then reduces to −e^{f+2λ₁}[2 + (1+z)/8 · e^{−2g−4λ₁}] = 0. For z > −1 the left side is strictly negative, so this is impossible.
   - The fourth equation gives the mirror result, impossible for z < 1.
   - Every real z is covered, including z = 1, 0, 2 and 3.
3. **Conclusion.** On every face r_b of every candidate flow, at least one of k_{φ₁}, k_{φ₂} differs from −2k_x (at every μ with μ₁μ₂ ≠ 0). So the PP lemma fails and there is no pure-M5 Z₂ solution.
   - **P3b: CONDITIONAL → PROVED given J1.** It uses only (A.15), not the numerical flows.
4. **Numerical cross-check (supporting only).** Over about 3,400–3,600 faces per candidate:
   - min |2f′ − λ₁′|/|f′| = 1.893 (MN2), 1.987 (MN1), 1.848 (z=2), 1.825 (z=3);
   - min |2f′ − λ₂′|/|f′| ≥ 1.987.
   - Both φ conditions fail on every sampled face.

## F4. P2
P2 is relabeled **PROVED given J1** (the BPS system is CONDITIONAL on CLP/BBBW).
- Stated assumption: the exterior is the BPS AdS₅×Σ₂ fixed point of the **same** CLP U(1)² truncation.
- The proof uses only continuity of h_ab plus Picard–Lindelöf uniqueness for the autonomous (A.15) (PP's 3-step form).
- Non-BPS exteriors remain P2′ (OPEN).

## F5. P3a scope
P3a (REFUTED) covers only faces of the **exact** AdS₅×Σ₂ and AdS₇×S⁴ geometries. It does not cover faces of the flow, which only approach them asymptotically. Flow faces are covered by P3b (F3).

## F6. P3e
- The conclusions "N_b = 2N or 0", "charge ≠ tension" and "not BPS" stay **CONDITIONAL** on the Z₂ parity of G₄ (PP O1).
- That parity is **OPEN**: no Owner record settles it.
- The arithmetic is unchanged: 2κ²T_M5 = (2π)³, and tension/charge (odd case) is 1.288 / 1.255 / 1.313 / 1.326 at the IR face and 5/3 at the UV face.

## Revised tally for the 1655 file (with this erratum)
| label | count | items |
|---|---|---|
| PROVED | 12 | J0, J1a, J2 (given J1), J2a, J3, J3a, P1, P2 (given J1), P3-lemma (PP), P3b (given J1), P3d, H (rescoped headline, given J1) |
| CONDITIONAL | 5 | J1 (CLP/BBBW), J1b, J1c, P3c, P3e (on G₄ parity) |
| OPEN | 5 | P2′, J5, J6 (b), J7, Z₂ parity of G₄ |
| REFUTED | 1 | P3a (exact end geometries only) |

Change from 1655 (9/6/4/1):
- P3b goes from CONDITIONAL to PROVED.
- The P3 lemma and H are added as PROVED.
- The G₄ parity becomes a separate OPEN item.

## New files (all in /workspace/nl-junction-1646/, each with a .sha256 sidecar)
- scan_rerun_1700.log 4d4ded4c8bdc406d5ba6adf7d3280da369289b84342058d69e39bf0a93ce1ee5
- scan_rerun_1700.stderr e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 (empty)
- pointwise_p3b.py 577c1946f8393f8e44a804fb6d80e78e7dc7c4eddba91e6fe5939d4ab3810f0f
- pointwise_p3b_1701.log 4ce80299fb7bc081ba3cab04d4ddcafbd0365188b77d74ba8de8a9f0640f9f4e

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
