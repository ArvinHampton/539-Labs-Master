# ERRATUM (Local-derived): PP audit fixes to the t4407 candidate-resolutions file, 2026-11-09 19:13 CST (America/Chicago)

- **Target (NOT edited):** FINDINGS_LOCAL_OWNER_ITEM_CANDIDATE_RESOLUTIONS_t4407_2026-11-09_1859.md, sha256 bfa5da3b0c7b1fd8107a6ad2579c915356f055acaad5f2664d244f004a852be6 ("bfa5da3b"). Line numbers below refer to that file.
- **Audit applied:** FINDINGS_PP_AUDIT_LOCAL_t4407_CANDIDATE_RESOLUTIONS_2026-11-09_1911.md, sha256 320c8c7ea4ae267cd55db3efaff84c3fd946165c68ea1101ed9f1cdb4fc5ce11 ("PP 320c8c7e"), fix list F1–F9.
- **Authority:** Owner t4407 (OW b0b9ae7f). Nothing is adopted; the Owner chooses.
- **Rules:** additive file. Nothing deleted, renamed, moved or overwritten. Tip 7cddb188… untouched (sha checked before and after). No CERT, no Gemini, nothing sent outside. Pure math only.
- **New Local evidence** (evidence_local_owner_candidates_2026-11-09/, each file with a .sha256 sidecar):
  - e1_erratum_pp_audit_checks.{py,log}: fixes 1 and 4. Its fix-5 block crashed (wrong unpacking order of sympy.gcdex) and is superseded; the file is kept on disk.
  - e1b_erratum_fix5_normalizer.{py,log}: fix 5.

## Fix 1 (F1): V-3, replace the R26 citation with PP's exact proof
- **L56, old:** "Tip R26 (cited, Auditor-confirmed) says no invertible intertwiner exists on V₄₂. This refutation rests on that cited premise."
- **L56, new:** "No invertible intertwiner between ρ and ρ^W exists on V₄₂, by PP's exact proof (PP 320c8c7e §1(a); script pp_v3_r26_structural.py, 1e26fc9d…). The proof runs as follows.
  - W₇TW₇⁻¹ = (1,0;−49,1) = ST⁴⁹S⁻¹ in SL₂(ℤ).
  - V₄₂ is S,T-stable, so an intertwiner would make ρ(T)|V₄₂ conjugate to ρ(T)⁴⁹|V₄₂.
  - ρ(T) is diagonalizable, with root-of-unity eigenvalues of order dividing 9800. So conjugacy forces equal eigenvalue multisets.
  - ζ ↦ ζ⁴⁹ strictly lowers the top 7-adic valuation of the eigenvalue orders.
  - V₄₂ contains exact T-eigenvectors with eigenvalues e(−1/140), e(−1/35), e(−9/140) and e(1/14), all of order divisible by 7.
  - These facts contradict each other.
  R26 as filed is float-only (SVD tol 1e−8) and is no longer used."
- **REFUTED stands,** now independent of R26.
- Local re-check (e1 log): W₇TW₇⁻¹ = ST⁴⁹S⁻¹ = [[1,0],[−49,1]] (exact). Local did not re-run PP's ℤ[x]/Φ₉₈₀₀ eigenvector certificate; it is cited.
- **L184, old:** "V-3 (from cited R26)". **New:** "V-3 (PP exact proof 320c8c7e §1(a))".
- **L44 / L47:** the context mention of R26 stays, read as "R26, float-only, qualitatively re-proved exactly by PP 320c8c7e".

## Fix 2 (F2): J-3, conductor versus minimal modular level
- **L77, old:** "[PROVED] cond(J) = 49·19600 = 960400. J is a quotient of J₀(19600) up to isogeny, and 19600 is the least such level."
- **L77, new:** "[PROVED] Conductor: cond(J) = 960400 = 140²·49 = d_K^{2·dim E}·N(f_{E_K}), with f_{E_K} = 𝔭₇² and N(f_{E_K}) = 49 (Milne 1972; PP 320c8c7e §1(b)). This equals cond(E₄₉)·cond(Ξ) = 49·19600. Minimal modular level, a different invariant: the least N such that J is a quotient of J₀(N) up to isogeny is lcm(49, 19600) = 19600. The level 19600 is NOT the conductor of J."
- No tag change.

## Fix 3 (F3): J-3 certificates, Milne, and the c1 log label
- **L76, append:** "Reference: Milne, *On the arithmetic of abelian varieties*, Invent. Math. 17 (1972), for Res_{K/ℚ}E_K ~ E × E^{χ_K}. The 400-prime Euler-factor check (log c1) is exact but supporting only."
- **L78, old:** "(cited c2e9b6fe §4: L(49a1,1) = 0.96665…, L′(Ξ,1) = 4.43262…)".
- **L78, new:** "(certified by PP ball arithmetic, PP 320c8c7e §1(b), pp_j3_lvalues_arb.py 4747836f…:
  - L(49a1, 1) ∈ [0.96665585280840577337 ± 3.5e−21] ≠ 0;
  - L′(Ξ, 1) ∈ [4.4326227316864161623 ± 2.2e−20] ≠ 0;
  - L(Ξ, 1) = 0, since ε(Ξ) = −1 exactly.)"
- **L76 and L212, label note:** read the c1 log's "primes 3..400" as "**first 400 primes excluding 2, 5, 7**". The log itself is not touched.
- No tag change: J-3's PROVED tags stand on the certificates.

## Fix 4 (F4): Oc-2, add the condition a_p(f) ≠ 0
- **L34, append:** "The conclusion needs some prime p ∤ 2·5·7·cond(ψ) with χ₁₄₀(p) = −1 **and a_p(f) ≠ 0**. Otherwise a_p(f) = χ₁₄₀(p)a_p(f) = 0, and the eigenvalues coincide at p. Witness: p = 11, where a₁₁(49a1) = 4 and χ₁₄₀(11) = (140/11) = −1. There are infinitely many such p: they split in ℚ(√−7) and are inert in ℚ(√35), by Chebotarev. So one can always avoid cond(ψ)."
- Local check (e1 log): a₁₁ = 4 and (140/11) = −1. Among the first 200 primes there are 52 with χ₁₄₀(p) = −1 and a_p ≠ 0: 11, 37, 53, 71, 79, 113, ….
- **PROVED stands** with the condition stated.

## Fix 5 (F5): J-1, withdraw "no Fricke +1 law"
- **L66, old:** "[PROVED] (cited, PP counterexample) W₄₉ does not normalize Γ₀(980), since WTW⁻¹ = (1,0;−49,1) ∉ Γ₀(980). So J-1 carries no Fricke +1 law either."
- **L66, new:** "[PROVED] (narrowed) The **level-49 matrix** W₄₉ = (0,−1;49,0) does not normalize Γ₀(980), since W₄₉TW₄₉⁻¹ = (1,0;−49,1) ∉ Γ₀(980). This says nothing about involutions defined at level 980 itself:
  - the level-980 Fricke W₉₈₀ = (0,−1;980,0) and the Atkin–Lehner W₄₉^{(980)} = (49a, b; 980c, 49d) (det 49) do normalize Γ₀(980) (standard Atkin–Lehner theory);
  - so J-1 does carry Fricke / Atkin–Lehner involutions.
  The withdrawn sentence 'So J-1 carries no Fricke +1 law either' is **WITHDRAWN**. What J-1 lacks is Ξ itself (L65: f_Ξ ∉ S₂(Γ₀(980)))."
- Local illustration (e1b log, 156 sampled elements of Γ₀(980)): W₄₉ fails, while W₉₈₀ and W₄₉^{(980)} (a=1, b=22, c=1, d=9) map every sample into Γ₀(980). This is an illustration only; the theorem is standard.
- **Regrade:** the tag stays **PROVED**, with scope narrowed to the matrix fact. The overstated consequence was not separately tagged, so the count does not change.

## Fix 6 (F6): Oc-3, the records-consistency claim becomes CONDITIONAL
- **L38, old tag:** [PROVED]. **New tag:** **[COND: completeness of Local's survey of the Owner records and of the Local PROVED results; a record-survey statement, not mathematics]**. The text is unchanged.

## Fix 7 (F7): H-3 odd d
- **L96, old:** "So P̂² = +1 ≠ −1, contradicting the adopted (B)-M square."
- **L96, new:** "So P̂² = VV̄ ⊗ 1 **≠ −1**, contradicting the adopted (B)-M square. **Scope:** this refutes only the Option-M form P̂ = (A ⊗ σ_x)K with A antiunitary on ℂ^d. ℂ^d ⊗ ℂ² is even-dimensional and does admit antiunitaries with square −1, e.g. 1_d ⊗ iσ_y K. So the refutation does not cover a general antiunitary on H₊ ⊗ ℂ²."
- **REFUTED stands** for the stated scope.

## Fix 8 (F8): α lemma
- **L147, old:** "Numerical identity check: residual 1.8e−15 (log c3)."
- **L147, new:** "The proof is the group-ring identity B(R_p e_g, R_q e_h) = [h ≡ −pq⁻¹g], hence B(Tx, Ty) = B(R_{tt*}x, y), with B nondegenerate (PP 320c8c7e §1(c) re-proves it algebraically). The 1.8e−15 residual in log c3 is an illustration only, not evidence."

## Fix 9 (F9): custody, add the generator to the §E evidence table
- **§E table (after L208), add the row:** | gen_findings_t4407.py | bba18ccf5d5c2183d252b789eea115a9d5972bb15c12a9edd539872bead4fc41 |
- New rows from this erratum:
  | e1_erratum_pp_audit_checks.py | fd733754f77d6cb65762634869fb9a8f3b5d388d1b301b61620b1dc6f417616d |
  | e1_erratum_pp_audit_checks.log | 8c5620e5bc445e77a387765e451da7e5719bce589464192f4d6e156d381c53be |
  | e1b_erratum_fix5_normalizer.py | 739a3fddbf69f6b3eb71c0a5ed752758856aeccdb375794314ca23353b5f04b9 |
  | e1b_erratum_fix5_normalizer.log | 0ee5405799cd92c0fbaaa207dbd9bc7da1d58944364207eb67dc49ce13274d0d |

## Corrected rollup and recommendations
- **Corrected rollup (60 graded claims): PROVED 41 · CONDITIONAL 5 · OPEN 7 · REFUTED 7. This matches PP 320c8c7e.**
  - Fix 6 moves one claim from PROVED to CONDITIONAL (42→41, 4→5).
  - The J-1 regrade (fix 5) narrows scope only. Its tag stays PROVED, so there is no count change.
  - Fixes 1, 2, 3, 4, 7 and 8 change wording, basis or scope only.
- **Corrected per-item counts:** only I1 changes, from 4/2/3/0 to **3/3/3/0**. The others are unchanged: I2 4/1/0/1, I3 10/0/2/0, I4 3/0/1/2, I5 6/1/0/0, I6 5/0/0/0, I7 2/0/0/1, I8 5/0/1/1, I9 3/0/0/2.
- **Recommendations: unchanged** (Oc-3, V-2, J-3 (+J-2 level), H-1, a-1, b-1, c-1, α-1, O5-1).
  - J-1 was not recommended. The fix-5 withdrawal makes J-1 more viable than bfa5da3b said, since it now has level-980 Fricke and Atkin–Lehner involutions. It still does not carry Ξ (PROVED), so the J-3 recommendation stands.
  - Fix 6 does not affect the Oc-3 recommendation, which was a naming choice.
- Bridge C stays **PARTIAL**. Nothing adopted.

Local-derived. For PP audit. Nothing adopted; the Owner chooses. Tip 7cddb188 untouched. No CERT. Nothing sent outside.
