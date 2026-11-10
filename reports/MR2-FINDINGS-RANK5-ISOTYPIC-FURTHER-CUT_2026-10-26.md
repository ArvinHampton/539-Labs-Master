# MR2 FINDINGS — Rank 5 ONLY — S₂(Γ₀(49), W⊂V₄₂ isotypic) R3/T-C further-cut hunt (2026-10-26)
- **Status: FAIL-track — further cut ABSENT** (no Written/Cat-A cut in the corpus reaches 0)
- tip Soft SF LOCK sha (start = end): `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` (`/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md`)
- tip_touched Soft SF NO · Rank 5 only · Soft SF invent HOLD · Soft SF F3 CLOSED · Opt 1 Weil NOT selected · no tip fold · no invent · Bridge PARTIAL READY NO · No Fricke Role A / ρ(W₇)
- T-C Owner Write: `OWNER_WRITE_TC_ISOTYPIC_R3_NO_VANISH_2026-10-26.md` sha `f861f571727140aa01f42b7410371d815aee50da4850bca1cf3dad8782255d63` (verified)
- AMEND-2: `/workspace/grok-batches/MR1-AUTHOR-REVERSE-ENGINEER-ALL-VANISHINGS_2026-10-26.md` sha `8173e7b381ba858be90e5a46b453efaa369d63a40ff8bab24ca86f3681e17d9c` (verified)
- `.out`: `/workspace/grok-batches/MR1-P5A-reverse-dimcalc_2026-10-26.out` sha `e2b260385fe0b4ce55e04ba364b74163cb3c66d1c4e42fa97696c774e59473e9` (verified; numbers only)
- Connection: `2b49ca25e96073e76dd64d8479f0d5b1985d41b74c3cdc4a11411b46677a9cec` · Corpus map: `b271f42ab1cf0a3407e82f47d793ac549f056226805e9e29fa942f8808f629b9` (verified)

## 1. Baseline (cited)
- V₄₂ = N₃₆ ⊕ N₆; commutant dim 2 (`.out` l.30; AMEND-2 §R3).
- N₃₆: Γ₀(49) M₂=178, **S₂=167**, Eis 11; κ=4 S=503 (`.out` l.32).
- N₆: Γ₀(49) M₂=33, **S₂=33**, Eis 0; κ=4 S=89 (`.out` l.33). κ=4 total 592.
- Neither piece is 0. T-C "vanish after isotypic cut alone" **REJECTED** (Owner Write f861f571…, W-TC). That Write also says "No further cut proposed or invented."
- Leading-term check: at κ=2 the ambient leading term is 42·56·2/12 = 196, and per piece it is ∝ dim: 36/42·196 = 168 and 6/42·196 = 28. That fits 167 and 33. AMEND-2 l.156 adds that each Δκ=2 step is +392, so no even κ≥2 vanishes for ρ̄ or any isotypic piece. A further cut would have to remove essentially all of the mass.

## 2. Further-cut hunt (corpus only; no invent)
| # | Candidate | Source (sha) | Applies to N₃₆/N₆? | Resulting dim | Soft SF risk |
|---|---|---|---|---|---|
| 1 | Isotypic cut itself (commutant dim 2 ⇒ only 2 pieces; no finer Γ₀(49)-isotypic split) | `.out` e2b26038…; AMEND-2 8173e7b3… | Yes (it is the cut) | 167 / 33 | none; already REJECTED |
| 2 | Cusp/Eisenstein cut (S₂ ⊂ M₂) | `.out` l.32–33 | Already applied | 167 / 33 (N₆ has Eis 0) | none |
| 3 | Weight shift κ=4 | `.out`; AMEND-2 l.156 | Yes | 503 / 89 (grows) | none; wrong direction |
| 4 | V-INV0 Fix(Γ₀(49),ρ̄)=0 | Corpus map b271f42a… row V-INV0 | Rep-level invariants only. It is not a cut of S₂ on the pieces | n/a (it feeds R2) | applying it to R3 = invent → FORBIDDEN |
| 5 | Newspace / W₄₉ restriction (Rank 9 analogy) | `MR2-FINDINGS-RANK9-NEWSPACE-W49-PERM_2026-10-26.md` c0f98435… (Status FAIL / bounds only) | Not Written for the isotypic pieces. Restricting it to N₃₆/N₆ would need a new identification | unknown (Rank 9: cuts shrink the space but do not reach 0) | invent HOLD; Rank 9 not reopened |
| 6 | Hecke/eigen-cuts, Fricke, ρ(W₇) | none Written for N₃₆/N₆ (rg over reports/ + grok-batches/ .md) | — | — | Fricke Role A / ρ(W₇) excluded; would be invent → FORBIDDEN |
| 7 | Weil-rep / ρ_D dictionary | none (Opt 1 NOT selected) | — | — | FORBIDDEN |
| 8 | Inventory/merged stub rows (CI#10; Merged row 5) | `CORPUS_VANISHING_INVENTORY…` fb298346…; `MERGED_VANISHING_MAP_STUB…` | Only "vanish on cut — not computed". Now superseded by the `.out` dims | none | stale (they predate the `.out`) |
| 9 | Index of revised targets | `OWNER_WRITE_ALL_REVISED_VANISHING_TARGETS_INDEX…` 2a4be231… | T-C goes in as a status/REJECTED note only | — | none |
| 10 | PR1 Rank 32 scalar S₂ baseline | `PR1-FINDINGS-VANISHING-LEAD-RANK32…` | Calibration only (scalar S₂ is nonzero) | — | none |

**Result: further cut ABSENT.** No Owner-Written or Cat-A cut of N₃₆, N₆, or S₂ on them exists in the corpus. Every remaining route (rows 4–7) would need an invented operator, identification, or dictionary with tip ρ̄. Those routes are FORBIDDEN / invent HOLD.

## 3. Verdict
**FAIL-track.** No further cut in the corpus brings 167 or 33 to 0. The isotypic cut alone is not enough, and the Owner REJECT stands. Any new cut needs a new Owner Write. None is proposed here.

## 4. Soft SF risks (≤3)
1. Rows 4–6: applying V-INV0, the Rank-9 newspace/W₄₉ restriction, or a Hecke/Fricke cut to N₃₆/N₆ without an Owner Write would be an invent. Held.
2. The older inventory/stub rows still say "not computed" and could be misread as an open vanish. They are superseded by `.out` e2b26038… / AMEND-2.
3. The dims are numeric proposals (`.out`), not a theorem. T-C folds into the tip only through MR1 after Auditor Soft SF CONFIRM, as a REJECTED status note. There is no tip fold here.
