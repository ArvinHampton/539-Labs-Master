# NL DERIVED: D6 stage 3 (g), S2-8: the general Poincaré (r,χ) BPS system and the LLM / SU(∞)-Toda check
2026-11-10, 1022 CST (America/Chicago). **NL derived proposal.** Additive only. Authority: Owner call-83d7a0fa (e72a188b…), OW t4436 (32881263…), OW t4431. Inputs: 2100 D6-8, 2216 S2-8, today's E5 (0a7d8e56…), E2 (197c5bd1…), E4 (4c25565f…) and E1 (2f33b65d…) files. Nothing adopted. **Junction: UNSOLVED. Count gap: unchanged. No candidate wall.** No CERT, no Gemini, nothing sent, no agent messaged. Tip 7cddb188… checked before and after. No new script.

**Tally: PROVED 1 · CONDITIONAL 1 · OPEN 1 · REFUTED 0 · total 3.**

Honest status: the general (r,χ) BPS system **was not derived** in this checkpoint. This file records exactly where it is still needed, and why the suggested LLM/Toda reduction cannot be used on those branches.

- **P8-1 (PROVED, implication). Where the PDE is not needed.**
  - The flux-free obstructions E5-4 (H_Σ∩SO(3)_R, with or without U(1)_R) and E2-4 (SO(3)_R×U(1)_R, Σ-non-uniform) use only three things at C₄: pointwise Clifford algebra, representation theory, and line-bundle topology. Neither uses any bulk equation away from the face.
  - So **no solution or reduction of the (r,χ) BPS PDE is needed** to exclude HW-BPS walls on:
    - scope S;
    - E5∩H_Σ;
    - E2∩U(1)_R (with SO(3)_R);
    - the E4 sub-cases that keep (reg) or (reg-all), see E4-5.
  - The PDE is needed only on the remaining BPS branches: **E1** (E1-4), **E2∩E5** (E2-5, E5-6) and **E4 with a singular C₄** (E4-6).
- **P8-2 (CONDITIONAL). The LLM/Toda reduction is unavailable on exactly those branches.**
  - Lin–Lunin–Maldacena (hep-th/0409174) reduce ½-BPS M-theory solutions to the SU(∞) Toda equation under two assumptions:
    - (A) an AdS₅ factor, with the bilinears of the AdS₅ Killing spinors;
    - (B) SU(2)×U(1) R-symmetry realised as an S² isometry and a U(1) isometry.
  - On **E1**, SU(2)_R is broken (B fails). On **E2∩E5**, U(1)_R is broken (B fails).
  - Every HW wall is Poincaré, not AdS₅, so (A) fails on all wall branches. LLM's AdS₅ limit describes only the IR vacuum.
  - Where (B) does hold (SO(3)_R×U(1)_R), P8-1 shows that HW-BPS walls are already excluded without the PDE.
  - So **the LLM/Toda reduction cannot decide any branch that is still open**.
  - **Condition:** LLM's derivation and assumptions are cited, not re-derived here. P8-2 rests on reading their stated hypotheses (A) and (B), so it is CONDITIONAL.
- **P8-3 (OPEN). The general Poincaré BPS system on E1, E2∩E5 and singular-C₄ E4 is not derived.**
  - Required data:
    - the 11D KSE on R^{1,3}×(r, Σ, S⁴-fibre), with at most SO(2) or no R-symmetry, Σ-dependence allowed (E2∩E5), and possibly singular along C₄ (E4);
    - D1 and D2 at the face;
    - Y15 NEC or an NEC-violating source;
    - the tadpole N_M5 + n_inst = 9760.
  - A natural next step (not done here) is a G-structure / spinor-bilinear analysis for one Poincaré Killing spinor of fixed chirality. E1-1 says such a spinor has its S² weight tied to its chirality on E1∩H_Σ.

## Branch register (t4436; not counted)
- Kept: [χS], [χU], [w]/Z2.
- OPEN for the PDE: E1, E2∩E5, E4 (singular).
- Proposed drops (pending PP audit), which need no PDE: E5∩H_Σ (E5-4) and E2∩U(1)_R (E2-4).
- S6 is a record premise.

## Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 1 | P8-1 |
| CONDITIONAL | 1 | P8-2 |
| OPEN | 1 | P8-3 |
| REFUTED | 0 | — |

Check: 1 + 1 + 1 + 0 = 3.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
