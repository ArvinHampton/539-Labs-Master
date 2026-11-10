# NL erratum-2: accepting PP audit 0c3b2b91 on the B2 closures (additive)

Date: 2026-11-09, about 15:09 CST (America/Chicago). Author: Non Local Path (NL).

Authority: the Owner's 12:29 PM additive-write grant. Status: new dated file only; nothing below edits an existing file. Not a CERT, nothing sent outside, tip 7cddb188 untouched.

## Files this erratum applies to (left unchanged)

| Short name | File | sha256 |
|---|---|---|
| NL-A | `NL_DERIVED_B2_CLOSURE_A_DIRECT_SUM_NONLOCAL_IOTA_2026-11-09_1315.md` | 988f1436f5c75ace3b64029654f664faa0fd8d7aab540798a17d08d7fadd4bfc |
| CMP | `NL_B2_CLOSURES_A_VS_B_COMPARISON_2026-11-09_1316.md` | cd227dc78ad88360666b1353368c3dd2b499f3204103d4459ee51ec56922bdcc |
| NLE | `NL_ERRATUM_B2_CLOSURE_A_AND_COMPARISON_A5ii_2026-11-09_1312.md` | 2aedc5bbb36d33015257ae4022636a2fd01840bd14045cd5b203dca38497d920 |

## Sources

| Short name | File | sha256 |
|---|---|---|
| PP audit | `FINDINGS_PP_SOFTSF_AUDIT_LOCAL_B2_CONSTRUCTION_A_ADDENDUM_NL_ERRATUM_2026-11-09_1316.md` | 0c3b2b91… |
| Local construction A | `FINDINGS_LOCAL_DERIVE_PREV_CONSTRUCTION_A_DIRECT_SUM_ISOMETRY_2026-11-09.md` | 4b25d2edf14b887038186ac2d4b580bacb106b3811456fceeea702f08c8a783f |
| Joint addendum | `JOINT_LOCAL_NL_B2_CLOSURES_A_VS_B_COMPARISON_LOCAL_ADDENDUM_2026-11-09.md` | 94973661dc30b7419bab116d261d881897d341b77e201a9d299e3021d5b433ea |
| Owner adoption of (B)-M | `RECORD_PP_B2_CONDITIONAL_ON_ADOPTION_B_M_2026-11-09_1319.md` | 09498bf7dc5ac428d5fd5efbacbbe8a9fb23c7e98c973f5ef238a29c0d7e9a38 |

NL accepts every PP verdict below and offers no rebuttal by proof.

## R1. NL-A, A-4 ("the sign of P² is free in (A)")

The conclusion "P_rev² = −1 has no mathematical content in (A) unless ι is fixed by some further structure" is REFUTED by proof.

Corrected statement (PROVED, PP and Local):

- Fix the backward map by the same formula, B = A₀ι*. Then for every unitary ι, P² = η = γ⁰γ⁰*. The sign is forced.
- The sign is a convention only when the backward map is left free (B = εA⁻¹). That narrower statement, PP-1309 point (3), STANDS.

## R2. CMP row "P² = −1: free choice in (A), forced in (B)"

This row is REFUTED by counterexample. The replacement row (PROVED) is:

> In both closures, P² = η·s, where s is the relative sign of the backward map. With the same-formula convention (s = +1) and the Majorana representation, P² = −1 in both. (A) and (B) are on equal footing here.

## R3. "Option M is the only closure" (CMP line 14, NLE E5)

The unrestricted claim, as stated in CMP line 14 and NLE E5, is REFUTED by counterexample. Local's complement fix gives the counterexample:

- ιψ = ψ⊗e₁ and Q = A₀⊗(S∘K₃);
- Q is local, Q² = η, and Q is a fixed-t symmetry;
- on H₊⊕ιH₊, Q coincides with Option M.

What still holds:

- PP-1309 uniqueness (U = e^{iθ}σ_x within the anti-diagonal (B) setup, with P̂² = −1 as an input) is PROVED in that exact scope.
- PP's extension to pure swaps on H⊕H with literal forward map A₀ is PROVED.
- Uniqueness for a non-literal forward map u(x)∘A₀ is OPEN.

## R4. NL-A line 14 ("a local version needs equal fibre ranks, i.e. (B)")

This holds within NL-A's anti-diagonal setup (A-2), where it is PROVED. Stated without that scope, it is REFUTED by Local's counterexample A3.

## R5. NLE E3 quote

The quote in E3 is corrected to:

> (A): fixed-t symmetry only with non-local H₋ ...

The full replacement row reads:

> (A): fixed-t symmetry with local H₋ for a suitable non-local ι; only with non-local H₋ under the Hermite ι, where locality is OPEN.

## R6. NLE E5

E5 is REFUTED as stated, for the reasons in R2 and R3. Corrected assessment:

- (A), in Local's complement form, and (B)-M both give P² = −1 together with a local fixed-t symmetry in the Majorana representation.
- They coincide on H₊⊕ιH₊.
- The difference between them is the literal codomain H₊⊗ℂ² versus H⊗ℂ², not the sign of P².

## R7. What stands

The following remain CONFIRMED:

- NLE E1, E2 and E4;
- NL-A A-1, A-2 (in its stated scope), A-3, A-5(i), A-5(iii) and A-6;
- all of closure (B).

Two further PROVED results from the PP and Local work:

- In finite dimensions, the literal anti-diagonal P_rev with P_rev² = ±1 on H₊⊕(H₊⊗ℂ²) does not exist.
- No Kramers tensor complement exists. A non-tensor J with J² = −1 does exist; whether the Owner wants one is OPEN.

## Status of B2

B2 is CONDITIONAL on the Owner's 1:18 PM adoption of (B)-M (record 09498bf7). It is not a CERT.

## Label tally

| Label | Items |
|---|---|
| REFUTED | A-4 conclusion; the CMP P² row; unscoped M-uniqueness; E5 as stated; NL-A line 14 unscoped |
| PROVED | the corrected statements in R1–R4 and R6 |
| OPEN | Hermite-ι locality; non-literal forward-map uniqueness; the Owner's preference on a non-tensor J; the physical reading of P_rev |
| CONDITIONAL | B2 |
