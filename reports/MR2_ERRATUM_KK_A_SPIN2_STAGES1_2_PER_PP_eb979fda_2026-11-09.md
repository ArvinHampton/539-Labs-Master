# MR2 ERRATUM — KK Group A spin-2 stages 1 (8ca7b93a) and 2 (7491cdb8), per PP audit eb979fda
Written 20:28 CST (box clock). Additive; the stage files are unchanged. Authority: OW d5eaeef3 under OW 8b26c786 (Group A = Aut⁺(48) × wall ℤ₂, a scope choice, not a result). Full spectrum OPEN; junction UNSOLVED; count gap unchanged. Tip 7cddb188 MATCH, untouched.

- **Audit:** FINDINGS_PP_AUDIT_MR2_KK_A_SPIN2_STAGES1_2_8ca7b93a_7491cdb8_2026-11-09_2018.md, sha256 eb979fdad83ebdf4f6540067c4160f996fdcc7f287a98427e4db0f7eab6b029a, **MATCHES** its sidecar.
- **Tiny check for fix 8 (frozen before run):** `MR2_ERRATUM_KK_A_SPIN2_STAGES1_2_PER_PP_eb979fda_2026-11-09.py`, sha256 e7f61bce212dad75c3f7c08141830e621460cf892888bd652866eee54875aae0; `….log`, sha256 2100e70f7bc54baeb5674200d1901ebbd1d61f68f379df3d64d9f7b9685be8f9.

All 10 fixes are ACCEPTED. No disagreements.

## Fix 1. Header times. ACCEPT
- The stage-1 md was written **20:04 CST**, not "~20:25"; its .py and log are from 20:03.
- The stage-2 md was written **20:09 CST**, not "~20:45"; its .py and log are from 20:08.
- The stated times were wrong; the mtimes are correct.

## Fix 2. Stage-1 RA-1 ran at a₁ = 7/10. ACCEPT
- The stage-1 11D-vs-reduced check used a₁ = 7/10, not the MN2 value a₁ = 1.
- This is harmless at q = 0. With ∂_{φ₁}ψ = 0, the twist enters only through g^{uu} = 1/g_uu(bare) from block inversion, which is independent of a₁, and through √g, whose (u, φ₁) block determinant is also independent of a₁.
- The MN2 value a₁ = 1 was used in all stage-2 RA-4 charged checks. Grade unchanged: COND.

## Fix 3. Running max. ACCEPT (cosmetic)
The stage-1 log's per-test "max rel diff over 3 random points" is a cumulative running maximum over the tests so far (`worst` is never reset). Every per-test value is therefore an upper bound on that test's own error. The overall maximum is 1.4e-15.

## Fix 4. RA-6 basis. ACCEPT
MR2's own RA-6 computation is **float**:
- a character average with np.linalg.eigvals on float matrices, rounded to an integer, with no error bound;
- a float η = dx³/y² det check.

On its own it is COND. RA-6 is graded **PROVED on PP's exact recomputation** in eb979fda (ℚ(ζ₈) fixed spaces of A, B, J; exact character average over 48 elements; exact orbifold integers), cited here with its math checked against MR2's values. The stage-2 wording "computer-assisted, exact group" is withdrawn.

## Fix 5. RA-6 scope. ACCEPT
The row 0,0,0,0,0,1,0,1 (m = 1…8) holds for the order-48 group ⟨A, B, J⟩ as constructed. Its identification with all of Aut⁺(Bolza) inherits the status of ecee2668 §1.

## Fix 6. Canonical-lift premise on every charged headline. ACCEPT
- Lifts of the Aut⁺ action to K^q are unique only up to a character of GL(2,3), and nontrivial characters exist (det). A det-twisted lift would change the invariant counts.
- Every charged statement in stage 2 therefore carries the explicit premise **(CL): canonical derivative lift (ecee2668 §6, 3rd bullet)**. This covers RA-6/RA-7 survival, the q = ±1 lowest mass 55.157, the q = ±6 Landau mass 84, and the table complete below 120.
- Stage-1 q = 0 statements need (CL) only in the trivial form: q = 0 functions carry no fibre action.

## Fix 7. Completeness wording. ACCEPT
Replace the stage-2 log's "|q| ≥ 7 … ≥ 105" with the md version:
- H ≥ |q| and ℓ ≥ |q| give m²L₅² ≥ q² + 8|q|;
- q = 7 is handled explicitly: ≥ 129 (Landau m = 6) and raised levels ≥ 235;
- q = 8 gives ≥ 128;
- q ≥ 9 gives ≥ 153.

So the table is complete below 120, given RA-5 completeness. PP's wider enumeration reproduces it, the next entries being 127.157 (×2), 128 and 129.

## Fix 8. RA-5 general holomorphic sections. ACCEPT. PROVED (exact sympy, this log)
For F = v^{k/2}·g(u+iv) with g holomorphic and arbitrary, the log gives Δ_k F − (k/2)(1−k/2)F = 0 and L_k F = 0.
- Control: for anti-holomorphic g(u−iv), both are nonzero (2i k g′ v^{k/2+1} and 2i g′ v^{k/2+1}).
- This replaces the stage-2 e4 check, which tested v^{k/2} only.
- Completeness of the Landau list stays COND (Maass theory, citation).

## Fix 9. "Exact" wording. ACCEPT
The neutral masses (12, 20, 32, 40) and their Δ are exact given the operator. The comparison "below the Σ-only 46.157" is **not exact**: it uses the float λ₁ᴵ = 23.07856. The ordering is not in doubt (margin ≥ 6), but the statement is COND.

## Fix 10. Self-disclosures 1–4. CONFIRMED by PP; folded in
1. The stage-1 log row 46.157119 (λ = 23.07856, μ = 0) is the Σ-only reference, not an S⁴-dependent mode. Its "above" tag is the strict `<` test failing on equality.
2. "ecee2668 §A" should read **§6 (3rd bullet)**.
3. The 4 "does not match" lines in the stage-2 log are the rejected s = −1 control.
4. The stage-2 log's completeness line omits q = 8. This is cosmetic, since H ≥ |q| gives ≥ 128.

## Tallies (unchanged, as PP confirms)
- Stage 1: **PROVED 2 · COND 4 · OPEN 1 · REF 0 = 7.**
- Stage 2: **PROVED 3 · COND 4 · OPEN 1 · REF 0 = 8.** RA-6 is PROVED on PP's exact recomputation.
- This erratum's new item (fix 8 identity): PROVED.

## Still OPEN
- Charged scalars and vectors (stage-2 row 8; not started — skipped under the budget rule, since they need the flux-mixing mass matrix).
- Rigorous Σ FEM bounds.
- Masses above 120.
- An exact symbolic version of RA-1/RA-4.

Rules: new dated files only; .py frozen before its log; no existing file edited; tip untouched; no CERT, no Gemini, nothing external; no messages sent. Naming: resonant algebra (RA-n).
