# PP confirm: Local t4407 erratum 511c6ca5 (fixes F1–F9 of PP 320c8c7e)
Author: Professor Proof (PP). Audit only. Additive. No CERT. Nothing adopted. Nothing sent. Tip 7cddb188 MATCH before and after (read only).
PP scratch: /workspace/audit-scratch/pp_1915_t4407_erratum/ (pp_j1_exact.py/.log, e1b_rerun_copy.py, e1b_rerun.log; each with a .sha256 sidecar).

## Verdict: **CONFIRMED (MATCH, with 1 custody nit)**

## Integrity
- [PROVED] ERRATUM_LOCAL_t4407_CANDIDATES_PP_AUDIT_FIXES_2026-11-09_1913.md hashes to 511c6ca504547a67fcd33f86f444390f5c9dfe0a7cbf5caba541b02a49e42ad0, which equals its sidecar.
- [PROVED] The target is unchanged: its sha is still bfa5da3b0c7b1fd8107a6ad2579c915356f055acaad5f2664d244f004a852be6.
- [PROVED] The four new evidence sidecars all pass: e1 .py/.log and e1b .py/.log. Their hashes equal the erratum's F9 rows.
- e1 crashed in its fix-5 block, as disclosed. Its fix-1 and fix-4 lines ran and are correct:
  - WTW⁻¹ = ST⁴⁹S⁻¹ = (1,0;−49,1).
  - a₁₁ = 4 and (140/11) = −1.
  - There are 52 qualifying primes among the first 200.
- PP reran e1b on a scratch copy. Its output is byte-identical to the filed log.

## Line citations and fidelity (checked programmatically against bfa5da3b)
- Each quoted "old" text occurs verbatim on the cited line: L34, L38, L44, L47, L56, L65, L66, L76, L77, L78, L96, L147, L184 and L212.
- Each "new" text matches PP's F1–F8 in content.
- PP checked two details in the new text:
  - F7's example 1_d⊗iσ_yK has square −1, because iσ_y is real with (iσ_y)² = −1.
  - F5's W₄₉^{(980)} with a=1, b=22, c=1, d=9 gives 49·9 − 20·22 = 1, so det = 49.
- **Nit (custody only):** F9 says to add the row "after L208". The §E table actually ends at L206, and L208 is the "Custody notes" header. The row belongs after L206. This does not affect any content.

## J-1 (fix 5), verified exactly (pp_j1_exact)
- [PROVED] With W₄₉ = (0,−1;49,0): W₄₉TW₄₉⁻¹ = (1,0;−49,1). Since −49 ≡ 931 (mod 980), this is not in Γ₀(980). T ∈ Γ₀(980), so W₄₉ does not normalize Γ₀(980). This narrowed PROVED claim is correct.
- [PROVED] For g = (α,β;980γ,δ) ∈ Γ₀(980), symbolically:
  - W₉₈₀gW₉₈₀⁻¹ = (δ, −γ; −980β, α) ∈ Γ₀(980).
  - For W₄₉^{(980)} = (49a,b;980c,49d) with det 49, the conjugate has integer entries and lower-left entry 980(αcd − 20βc² − cdδ + 49d²γ) ∈ 980ℤ.
  So the withdrawal of "no Fricke +1 law" is justified exactly, not only by the e1b sample.

## Rollup and recommendations
- [PROVED] The corrected rollup is 41/5/7/7, equal to PP 320c8c7e.
- Only fix 6 changes a count: the Oc-3 records-consistency claim moves from PROVED to CONDITIONAL, so I1 goes from 4/2/3/0 to 3/3/3/0. Fix 5 narrows scope only, with no count change.
- The recommendations are unchanged. J-3 is still recommended, and this is logically consistent: J-1 now has involutions at level 980 but still does not carry Ξ (PROVED, f_Ξ ∉ S₂(Γ₀(980))).

## Residual fixes
1. (Custody nit, optional) Place the gen_findings, e1 and e1b rows after L206, the end of the §E table, rather than "after L208".
No math residuals.

Professor Proof (PP). Nothing adopted. No CERT. No Gemini. Nothing sent. Tip 7cddb188 untouched.
