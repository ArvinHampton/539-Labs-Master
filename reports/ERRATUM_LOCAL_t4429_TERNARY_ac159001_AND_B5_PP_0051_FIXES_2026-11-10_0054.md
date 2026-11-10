# ERRATUM (Local-derived) to FINDINGS_LOCAL_t4429_TERNARY_THETA_FALLBACK_i_2026-11-09_2242.md (ac159001…) and to the B5 status line, applying PP audit d9fc6cde. 2026-11-10, written 00:54 CST (America/Chicago)

- **Scope.** Additive. The three audited files (2159, 2207, 2242) are NOT edited; this file corrects 2242 and records the B5 D=28 sub-result by reference. No CERT. No Gemini. Nothing sent outside. Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, checked before and after writing.
- **Source audit:** FINDINGS_PP_AUDIT_LOCAL_THREE_FILES_2159_2207_2242_2026-11-10_0051.md, sha256 d9fc6cde8f3fb728360d5b00f9e2f5a4cd5dfec928ce8ddd76e951c1e7ed9de9 (verified on disk; matches the stated sha).
- **Rule:** OW 3f160803 as amended by 36683379 (a citation alone never makes a claim PROVED). "Resonant algebra" (RTA historical alias only).
- **No grade change.** PP 0051 made none. Bridge C stays 47/11/5/2/1 + V₈₄ (66 rows). t4436 stays 63/17/5/9/2. O-b stays OPEN. B5 stays PENDING.

## F1. TT-2 row of 2242: the d=343 control is PROVED via TT-1

2242 TT-2 (quoted): "Method control: the f = 49a1 packet is recovered as genus differences — d = 343 (D = 7, dim 2: θ_{x²+2y²+49z²−xy} − θ_{x²+7y²+14z²−7yz}), d = 686 (D = 14, dim 2), d = 1372 (D = 7 and 14, dim 8), stable from N = 12000 to 20000", graded "evidence (formal, truncated, mod p)".

Correction, per PP 0051 §3: the d=343, D=7 difference H = θ_{Q₁} − θ_{Q₂} with Q₁ = x² − xy + 2y² + 49z² and Q₂ = x² + 7y² − 7yz + 14z² is identically G₁, because Q₁ = L₁ ⊕ ⟨49⟩ and Q₂ = ⟨1⟩ ⊕ 7·L₁, so H = θ_{L₁}(τ)θ(49τ) − θ_{L₁}(7τ)θ(τ) = G₁. That control is therefore **PROVED via TT-1**. The rest of TT-2 (d = 686 and d = 1372) stays evidence (formal, truncated, mod p). TT-3 stays evidence.

## F2. 6272 D=28: joint kernel 0, exact (PROVED on the PARI base); B5 remains PENDING

Evidence: reports/evidence_local_t4407_computations_2026-11-09/ob_v3_6272_D28_D56.log, sha256 5cd47ca8215aff6b3651f60e29ab3193d643d7300751b75199b2fa72f09a1588 (matches its sidecar). The log records, exactly:

- N=6272, D=28: dim 388; joint kernel of T(p²) − χ₋₄(p)a_p(f) for p=3,5,11 shrinks 88 → 32 → 0 (3964 s).

mfheckemat and matker are exact over ℚ in PARI. **Sub-result: PROVED (PARI base)** — there is no form in S_{3/2}(Γ₀(6272), χ₂₈) with these T(p²)-eigenvalues. This is a settled sub-result inside the PENDING B5 row. **B5 stays PENDING** until ob_v4 closes D=56. No rollup change.

## F3. TT-4 caveat 1 of 2242 restated

2242 caveat 1 (quoted): "Linear algebra is mod one prime; truncation N ≤ 80000 is below the weight-3/2 Sturm bound of the θ-levels for large d (≈ 1.5·d·Π(1+1/p) at level 4d, e.g. ≈ 9400 for d = 10976, while independence of generators was measured only on n ≤ 3000 (v4) or N/9 (v4b/c)). A genuine form could be lost if two θ-series agree up to that range but differ beyond it."

That wording is self-contradictory (80000 > 9400). Replace caveat 1 by:

1. The linear algebra is mod one prime. Generator independence was measured only on n ≤ 3000 (v4) or n ≤ N/9 (v4b/c). A genuine form could be lost if two θ-series agree up to that range but differ beyond it. (Truncation N ≤ 80000 is not claimed to lie below the Sturm bound.)

Caveats 2 and 3 of 2242 stand. TT-4 and TT-5 remain evidence (negative); OPEN as mathematics.

## Status (no claims; jobs not disturbed)

- **ob_v4_6272_D56** (PID 1045534, wrapped by `timeout 14400` as PID 1045533): started 00:48:10 CST. Log at writing (00:54 CST): mfinit done, dim 388 [131s]; after p=3, joint kernel dim 88 [188s]. Still running; p=5 not yet reported.
- **chain_v2_ob_v3_then_D56_s2e_12544.sh** (PID 1015729, started 00:06:30 CST): alive, waiting on ob_v4. Log: "ob_v3 gone at Tue Nov 10 00:48:10 CST 2026"; "ob_v3 did not finish D=56; starting ob_v4_6272_D56 at Tue Nov 10 00:48:10 CST 2026". After ob_v4 it is to run s2e (J-2 at 9800) then ob_v4_12544. s1e (PID 932685) also still running; not touched.

Local-derived. Erratum only; nothing adopted is implied.
