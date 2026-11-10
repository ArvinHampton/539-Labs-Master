# PR1 FINDINGS — Vanishing lead Rank 10: S₄(SL₂ℤ, ρ̄) sub-witness ≠0 dim 11 (2026-10-26, America/Chicago)

Scope: Rank 10 ONLY. Cite-only. No new numbers or math introduced.

## Locks / standing
- tip Soft SF LOCK `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` sha256 `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91`. I verified it at start and at end. **tip_touched=NO**. I did not edit the Soft SF tip-pin catalog.
- Soft SF invent HOLD tip fill else. Soft SF F3 CLOSED (no Fricke Role A / ρ(W₇)). Not reopened, not tip-folded.
- Bridge PARTIAL / READY NO / NOT Cat A.
- Assignments `VANISHING_LEAD_ASSIGNMENTS_2026-10-26.md` sha `348bf88ef158a84f1a56c1c28937c06f2323071ccdc536474f1f5cbfaebde881`. The computed hash matches the brief (L17 = Rank 10 → PR1).
- Map stub `MERGED_VANISHING_MAP_STUB_2026-10-26.md` sha `b3e0d20ba9d428c0c0315fe27cfe8e5d4929fac2f762c442475b2aab07aa5627`, row 10 (L32): "S₄(SL₂ℤ, ρ̄) sub-witness | 4 | −2 | ≠0 dim 11 | proposed | MR1 P5A-VANISHING §4 | b829661e2a6b | Independent refutation of P5a".

## Rank 10 claim table
| Field | Value (cited) |
|---|---|
| Object | S₄(SL₂(ℤ), ρ̄), ρ̄ = dual of ρ = ρ_N₂\|V₄₂ (42-dim) |
| κ / k | 4 / −2 |
| Claim | dim = **11** (≠0); ρ-convention companion dim 9 |
| Author | MR1 (Author prove campaign). Not an Owner Write. |
| Status in source | **proposed** ("All new math below is proposed until Owner Writes"). Numeric: floating point, integers to 1e-12 |
| Method | Riemann–Roch on the modular orbifold, with local constants fitted on the six even characters χ_n (overdetermined 6 eqs/4 unknowns, resid 9e-16). Sanity checks: trivial → 0; Perm → 10 = dim S₄(Γ₀(49)). Source caveat: the formula is "fitted+sanity-checked, not quoted from a numbered reference" |
| Exact text | MR1 §4 table row "ρ̄ (dual, operative) \| **11** \| **592**"; L32: "already S₄(SL₂ℤ, ρ̄) ≠ 0 and those forms are cusp forms for (Γ₀(49), ρ̄)." |

## Source chain (full sha256)
1. **Primary:** `/workspace/grok-batches/MR1-AUTHOR-PROVE-P5A-VANISHING_2026-10-26.md` `b829661e2a6b1ae49e743f111336ca2c4893bd90dd7a292ad05d8e03cd1b7e8d`. The `.sha256` sidecar matches. §4 L24–32.
2. Script: `/workspace/grok-batches/MR1-P5A-dimcalc_2026-10-26.py` `0ecd4166edd333abb2bca0e6da9d9c9c5ab7dbd1a285bfc2d8bb503b8919861f`. I did not re-run it.
3. Reverse-dimcalc output: `/workspace/grok-batches/MR1-P5A-reverse-dimcalc_2026-10-26.out` `e2b260385fe0b4ce55e04ba364b74163cb3c66d1c4e42fa97696c774e59473e9` (script `.py` `bfd0141a873cbc2ea696e73ade614740f2483491e4fde48bdd0b4ea408256402`).
   - L24: "rhobar k 4 SL2Z M,S,Eis 12.0 11.0 1 | G0(49) M,S,Eis 603.0 592.0 11 | S new= 581.0".
   - L18 (ρ): "SL2Z … 10.0 9.0 1 | G0(49) … 584.0 573.0 11 | S new= 564.0".
   - These are a second output that agrees with MR1 on 11 / 592 / 9 / 573. It comes from the same author and the same method family, so it is not fully independent.
4. MR2 connection `MR2-FINDINGS-P5A-REVERSE-ENGINEER-CONNECTION_2026-10-26.md` `2b49ca25e96073e76dd64d8479f0d5b1985d41b74c3cdc4a11411b46677a9cec`.
   - L11: "11 of the dims already come from level 1 (S₄(SL₂ℤ, ρ̄) = 11, oldforms pulled up 56 ways only through Perm)".
   - L29 R4 new/old cut: removing the oldforms induced from S₄(SL₂ℤ, ρ̄) (11) "cannot reach 0 at κ=4". This is a restatement and cites MR1.
5. `CORPUS_VANISHING_INVENTORY_2026-10-26.md` `fb2983460ebadf7c8fe1d934d33ae05d57d725fcbf716933edb7780d273756c0` L30 restates "S₄(SL₂ℤ,ρ̄)=11" from MR1.
6. Merged stub row 10 (above) restates MR1 §4.
7. Owner Writes checked: OWNER_WRITE_*_2026-10-26.md, including P5A_REWRITE `0e1c7cac9713089dd8aba4e6345db514a56311cf7fab3e2fa4221641db5ffde4` and TE_COEFF_CYCLE_592 `5048e04490f0a4b7d32f1ce2ae57227205679864a633d8f8fb603327fe1048dc`.
   - None of them writes S₄(SL₂ℤ, ρ̄) = 11. I grep'd for "SL₂ℤ" with no hits.
   - TE cites 592 as "proposed dim" only.
   - **Owner Write for dim 11: ABSENT.**
8. tip: no hit for "SL₂ℤ, ρ̄" / "11". **tip cite of dim 11: ABSENT.**
9. MR2 corpus vanishing map `b271f42ab1cf0a3407e82f47d793ac549f056226805e9e29fa942f8808f629b9` covers only V-P5a-FAIL (592). It has no separate dim-11 row.

## Backwards inference chain (corpus-cited only)
1. Operative P5a, tip L410 (W-P5a-OP): S₄(Γ₀(49), ρ̄) = {0}, κ=4, no cut. Tag: "to prove".
2. ρ is a genuine SL₂(ℤ)-rep on V₄₂ (MR1 §2: S_lab² = I, (S_lab⁻¹T_lab)³ = I). Its restriction to Γ₀(49) is the operative ρ̄ (MR1 §1).
3. Restriction step (MR1 §4 L32): every f ∈ S₄(SL₂ℤ, ρ̄) is automorphic under the subgroup Γ₀(49) ⊂ SL₂ℤ and stays cuspidal ("those forms are cusp forms for (Γ₀(49), ρ̄)"). MR2 L11 adds the induction view: Shapiro gives M_κ(Γ₀(49), Res ρ̄) ≅ M_κ(SL₂ℤ, ρ̄⊗Perm), and the trivial summand of Perm carries the level-1 forms.
4. So S₄(SL₂ℤ, ρ̄) ↪ S₄(Γ₀(49), ρ̄). If the dim-11 claim holds, dim S₄(Γ₀(49), ρ̄) ≥ 11 > 0 and P5a is false.
5. This lower bound is independent of the full 592 count. It needs only the level-1 count and the inclusion. It does not use the 56-coset Perm RR or the 588 leading term. It is still the same RR method and the same author as the 592 figure, so it supports the FAIL rather than independently verifying it.
6. The ρ convention gives 9 > 0, so the FAIL holds under either automorphy convention (MR1 L32).

## Status — Rank 10
**proposed / VERIFIED-cite** (the cite chain resolves with sha matches; the content is MR1-proposed numeric, not Owner-Written, not Auditor MATCH, not folded). There is no CONFLICT inside the corpus: every restatement agrees on 11. The only conflict upstream is C1 (tip OPEN-CLAIM vs proposed FAIL) on map row 3, and Rank 10 sides with FAIL.

## Gaps (recommendations only)
- G1: An Owner Write for "dim S₄(SL₂ℤ, ρ̄) = 11 (proposed→Written)", or an Auditor MATCH of MR1 §4. Neither exists today.
- G2: An explicit witness. MR1 §6 notes "No explicit q-expansion witness written". One explicit nonzero element of S₄(SL₂ℤ, ρ̄), from MR1 numeric (Eisenstein/theta construction per MR1 §6), would close Rank 10 without relying on the fitted RR.
- G3: A numbered-reference RR formula (MR1 §6: Skoruppa/Borcherds-type, "not quoted"). Owner/MR1 to supply the citation.
- G4: An independent re-run of `MR1-P5A-dimcalc_2026-10-26.py` by a non-MR1 lane. Not done here (cite-only brief).
- k/route choice after the FAIL returns to Arvin (MR1 §5).

Blocker: none for the cite chain. Promoting beyond proposed needs G1 or G2.

tip sha end = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91. **tip_touched=NO.** Bridge PARTIAL / READY NO / NOT Cat A.
