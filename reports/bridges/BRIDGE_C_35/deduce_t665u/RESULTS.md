# RESULTS — deduce_t665u — 2026-10-25 (CDT)
PREREG.md sha256 9bcb0b44a474066c4b67b28e8af46c158c6c58240483feae484842cd9e7a05d8 (PREREG.sha256; unedited after hash).
Mode: DEDUCTION ONLY. No numeric invent. SF-W7-3 fence honored (Closure trees / Continue_Closure_* / PUSH_LOG_*Closure* noted, not read as law). CORE_FREEZE holds.
Short shas below refer to full shas in PREREG.

## RG-T665a residual_slash closed form — ABSENT-with-gap (uniqueness FAILS, DEDUCED)
- D-a1 DEDUCED [7368b855 L24–L28]: Written form is residual_slash(x)=|7x|^{-1/2}·residual_factor(x), residual_factor=a+bt+ct^2+d/(1+t^2), t=7x−3, a≈10.6923 b≈0.2160 c≈2.7618 d≈−7.5316, "recovered" from continuous span (fit, err ~1e−11).
- D-a2 DEDUCED (arithmetic re-check of Written coeffs only, no new numbers adopted): sample t=−2,0,2,4 give 19.8012, 3.1607, 20.6652, 55.3021 = Written ratios [7368b855 L33–36]. Four free coefficients vs four constraints ⇒ the ansatz is an exact interpolant; the data fix (a,b,c,d) only *given* the ansatz.
- D-a3 DEDUCED [7add2a9a L35]: a degree-3 polynomial P also interpolates the same four ratios exactly and is Written as "discrete data only… not a Fricke polynomial identity". P ≠ the rational ansatz off-sample (d/(1+t^2) is non-polynomial) ⇒ ≥2 distinct Written-compatible forms agree on all Written constraints.
- D-a4 DEDUCED [7add2a9a L12; 426ea3e0 L51]: no Written Fricke/modular identity selects the ansatz ("residual_slash is not Auto").
- Gap: no Written premise forcing the functional family of residual_factor off the 4 samples. Not uniquely forced ⇒ ABSENT-with-gap.

## RG-T665b δ_W7≡0 ∀x — ABSENT-with-gap (neither forced nor obstructed)
- D-b1 DEDUCED [a6a91a3b L25; b9a21438]: δ_W7 depends on residual_slash; by RG-T665a residual_slash is not uniquely determined off-sample ⇒ δ≡0 ∀x cannot be uniquely forced.
- D-b2 DEDUCED [7368b855 L50, L58; a6a91a3b L37]: h_residual^{high} values at samples/Fricke images not tabulated; law explicitly unclaimed. W7 pin's 4-point vanishing is a claim with exact ∀x "not yet proved" [b9a21438].
- D-b3 DEDUCED [426ea3e0 L153, L163, L195]: the Written obstruction concerns g_7^rad (not C) — does not prove an obstruction for C's δ_W7. No obstruction proof.
- Gap: exact identity for h under W_7 and a forced residual_slash. ABSENT-with-gap.

## RG-T665c sample-h / RG76d — ABSENT-with-gap
- D-c1 DEDUCED [d12dd01d L7, L13 (RESIDUAL_IDENTITY_HUNT ee4f4fc0 §6); e5a275a8 §B; 1e18a87d L149]: no Written h values; ledger Ξ (χ/ϑ) [7dbd63af] gives series structure but χ_even/χ_odd evaluations to h at x∈{1/7,3/7,5/7,1} require numeric evaluation not present in Written; computing them = new numeric, banned/not deduction. G1 [dfde6216 L13] forbids inventing from accept. ABSENT-with-gap.

## RG-T665d outer_* as Cat A — ABSENT-with-gap
- D-d1 DEDUCED [d12dd01d L20–29; dfde6216 L13–19]: ledger χ/ϑ form (k∈ℤ, q-prefactor, shift n+7k/2) vs HD outer_*·Θ_{3/2} (m≥0, a=7m/7m+7/2); G1 explicitly: ACCEPT ≠ form equivalence, X4 unshown, do not adopt outer_*. No Written re-indexing identity maps χ(k) to outer_*(m) ⇒ not forced. X4 equality unshown stays.

## RG-T665e Bridge/READY
a, b not PASS ⇒ Bridge PARTIAL; READY NO. residual-C OPEN. No unique closed form LOCKED. order78 NOT started.
