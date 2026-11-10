# NL erratum 9: O1 wording fixes, accepting PP's audit 1bd92da7 of erratum 8 (additive)
Author: Non Local Path (NL). The derivations below are **NL derived proposals**.
Date: 2026-11-09, CST (America/Chicago). New file only. No conclusions change. No vacuum, source or b adopted. No CERT. Nothing sent outside. Tip 7cddb188 untouched.

- **Audit:** FINDINGS_PP_AUDIT_NL_ERRATUM8_O1_AND_OW_f825dfff_2026-11-09_1750.md (sha 1bd92da71029f93c2800cb2dc5c131a7b52010315308f0e7f9c8b175090427bc, equal to its sidecar). It passes erratum 8 and asks for wording fixes only.
- **Applies to:**
  - NL_ERRATUM8_O1_ACCEPT_PP_544fc7b0_2026-11-09_1745.md (96fb6069…)
  - 1736 §A
  - NL_DERIVED_ODD_HW_WALL_E8_MU_TIME_LOCALIZATION_2026-11-09_1750.md (4d9c9951…)

## Fixes
1. **A11 / fix 2(ii).** For the free antipodal τ, the net face charge is 2N_flux **on the covering space**. On the quotient face/τ the charge per fundamental domain is not stated (CONDITIONAL).
2. **Domain of the sign rule.** ε = −s_x s_Σ holds for τ that **preserve the S⁴ fibration**, where s₄ cancels identically (PP: all 8 sign patterns check).
   - τ that mix S⁴ with Σ or x are not covered (OPEN; moot under f825dfff).
   - Time-reversal caveat: if s_x = −1 is realized by t → −t, the classical rule C → s₁₁σ*C holds. The quantum, antiunitary treatment has not been checked (CONDITIONAL; not needed under f825dfff).
3. **Alignment with OW f825dfff (17:45).** The Owner has now **defined τ = id**: the face is a fixed plane, an HW-type wall.
   - So O1 = **odd**, CONDITIONAL on P-b. E₈ and n_inst are CONDITIONAL, and N_M5 + n_inst = 2N_flux.
   - Erratum 8's "O1 lock (OPEN) / remaining Owner choice τ" is superseded.
   - The P-nofix items (A9b, A10, A10e, A11, A11e) stay correct but are now off-premise and no longer apply.
   - Erratum 8 predates f825dfff, so this is an alignment, not an error.
4. **Attribution.** f825dfff contains no NL assignment. In every NL file, including the main 1750 file, the instruction "work the odd case only / drop the even branch" is attributed to **Physicist's 17:46 relay**, not to Owner text. The 1750 file already attributes it that way in its header.

## Tally (wording items)
| label | count | items |
|---|---|---|
| PROVED | 1 | fix 2: ε = −s_x s_Σ for fibration-preserving τ |
| CONDITIONAL | 3 | fix 1: quotient charge normalization; fix 2: time-reversal caveat; fix 3: O1 odd given P-b |
| OPEN | 1 | fix 2: τ mixing S⁴ with the base |
| REFUTED | 0 | — |

Check: 1 + 3 + 1 + 0 = 5. Fix 4 is an attribution note, not a claim.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
