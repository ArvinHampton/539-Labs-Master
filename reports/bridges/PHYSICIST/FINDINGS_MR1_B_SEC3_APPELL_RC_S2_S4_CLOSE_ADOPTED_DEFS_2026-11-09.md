# FINDINGS — MR1: closing S2–S4 of B§III (Appell→R_c) under the Owner-adopted definitions
Date: 2026-11-09 (America/Chicago). Author: Math Research 1. Audience: Local (hand-off), Professor Proof (audit), Physicist and Mathematician.
Authority: Owner write `OWNER_WRITE_MAINCHAT_BLUEPRINT_1509_CORRECTED_ADOPTED_2026-11-09_1511.md` sha 5a6e717732c413a39c89d9b95c9b17455ecf4da8dd64e8bb9d879f427e6a845c (item O6).
Reviewed argument: B `OWNER_DOCUMENT_FORMAL_RESOLUTIONS_STRUCTURAL_CORRECTIONS_COMPENDIUM_2026-11-05.md` sha 9c6f83da… §III.
Prior grading: MR1 `FINDINGS_MR1_SOFTSF_PP_PROOF_REVIEW_B_SEC3_APPELL_RC_2026-11-05.md` sha f4305f21ece052cc1cdeca55a33a0ca049a95bc698c63a0165c3fa6c31a499db (S1 PASS, S2–S4 GAP).
Citation reconciliation: "eea23f27" = Local's absorb of that review, `FINDINGS_LOCAL_SOFTSF_ABSORB_MR1_BSEC3_APPELL_RC_2026-11-05.md` sha eea23f274097c97ead742586746f177edc674703ac6b0f54d702a202a8dab294 (PRESS abea152b…). Same argument, same grading; no conflict.
Limits kept: tip 7cddb188… untouched (sha re-checked this run); no CERT; nothing sent outside; no Gemini; no invented Appell–Lerch object.

## Adopted definitions (Owner, DEFINITIONS not proofs)
- Λ₀ := ln(6+√35)/√10
- κ := √(2/Λ₀)
- R_c := κ·ℓ_P

## Computations (mpmath, 30 digits)
- Λ₀ = 0.783577217617423511236510881232
- κ = 1.597622240065248810609550354750
- κ − 1.59543 = +0.0021922 (B§III value)
- κ − √(2/0.7858) = +0.0022612 (old Tier E value 1.5953611)

## Results

R1 — PROVED. ε = 6+√35 is the fundamental unit of ℤ[√35] = O_K, K = ℚ(√35) (35 ≡ 3 mod 4; (6,1) is the least solution of x²−35y² = 1; norm +1). Hence ln(6+√35) = Reg(K) and Λ₀ = Reg(K)/√10.

R2 — PROVED (class number cited, numerically confirmed). For the real quadratic field of discriminant D = 140, Dirichlet's formula gives L(1,χ₁₄₀) = 2·h·Reg/√140 with h(140) = 2, so L(1,χ₁₄₀) = 2 ln(6+√35)/√35 = 0.837679281… — this is exactly the Prop. 41.5 residue. Check: the partial sum Σ_{n≤2·10⁶} χ₁₄₀(n)/n = 0.8376773, giving h ≈ 1.999995. Consequence (identity):
  Λ₀ = √(7/8)·L(1,χ₁₄₀) = (√35/(2√10))·L(1,χ₁₄₀), checked to 30 digits.
So the adopted Λ₀ is an arithmetic invariant of ℚ(√35) / the character of conductor 140, tying it to the Weil(140) side of Local's O1/O2.

S2 (derivation of R_c from normalized Appell–Lerch boundary sums matching tree growth)
- S2a — PROVED (definitional): under the adoption, R_c is DEFINED, so B§III no longer needs a derivation for R_c to be well-defined. The S2 gap is closed in the sense that nothing downstream depends on it.
- S2b — OPEN: no Appell–Lerch sum, normalization, boundary sum or operator is identified whose evaluation gives κ or Λ₀. R1–R2 give an L-value (Dirichlet class-number) route, not an Appell–Lerch one. Appell–Lerch/mock objects in the literature encode imaginary-quadratic class numbers (Hurwitz/Zagier), not real-quadratic regulators; that is an observation, not a disproof, so the link stays OPEN.
- S2c — OPEN: "spectral radius bound matching tree vertex growth." The 4-regular Bruhat–Tits tree has spectral radius 2√3 ≈ 3.4641 and growth rate 3; neither equals κ. B does not state which radius it means, so no precise false claim is shown.

S3 (the numerical evaluation)
- S3a — PROVED: κ = 1.5976222400652488… under the adopted definitions.
- S3b — REFUTED (CONDITIONAL on reading B's dimensionless "R_c = 1.59543…" as κ = R_c/ℓ_P): 1.59543 ≠ κ; difference 2.19×10⁻³, far beyond rounding.
- S3c — Note: the old Tier E value √(2/0.7858) = 1.5953611 used Λ₀ ≈ 0.7858; the adopted Λ₀ = 0.7835772. Any downstream number that was built on 1.5954 or 0.7858 must be recomputed with the adopted values. This is a flag, not a verdict on those numbers.
- S3d — PROVED: units. R_c = κℓ_P has length dimension (≈1.5976 ℓ_P); B's R_c was dimensionless. Only the ratio R_c/ℓ_P = κ is comparable.

S4 ("independent of empirical vacuum scaling coefficients")
- S4a — PROVED (CONDITIONAL on the Owner's definitions): κ is a closed-form function of ln(6+√35) and √10, containing no fitted or empirical input; R_c depends further only on ℓ_P.
- S4b — OPEN: the physical claim that this R_c is the correct coherence radius is not derived; it is adopted. "Parameter-free" holds for the definition, not as a theorem about nature.
- S4c — OPEN: why the divisor is √10 (and not another normalization such as √35 or √140) is not derived; R2 shows Λ₀ = √(7/8)·L(1,χ₁₄₀), so the factor √(7/8) is the unexplained piece if one wants Λ₀ from the L-value.

## Summary table
| Item | Label |
|---|---|
| S1 circularity | PASS (unchanged) |
| R1 Λ₀ = Reg(ℚ(√35))/√10 | PROVED |
| R2 Λ₀ = √(7/8)·L(1,χ₁₄₀) | PROVED (h=2 cited + numerically confirmed) |
| S2a R_c well-defined | PROVED (definitional) |
| S2b Appell–Lerch link | OPEN |
| S2c tree spectral-radius match | OPEN |
| S3a κ value | PROVED |
| S3b B's 1.59543 = κ | REFUTED (conditional on identification) |
| S3c old 0.7858/1.5954 inputs | FLAG: recompute downstream |
| S3d units | PROVED |
| S4a no empirical input | PROVED (conditional on adoption) |
| S4b physical derivation | OPEN |
| S4c √10 normalization | OPEN |

Hand-off: Local, for O1/O2 (character 140) and any R_c use. PP: please audit R1, R2, S3b. No CERT.
