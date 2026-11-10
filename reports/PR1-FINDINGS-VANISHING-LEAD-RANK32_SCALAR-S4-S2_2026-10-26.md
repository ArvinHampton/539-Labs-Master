# PR1 FINDINGS — Vanishing Lead Rank 32: scalar S₄(Γ₀(49)) dim 10; scalar S₂(Γ₀(49)) >0
Date 2026-10-26 ~11:10 CDT · Report-only · cite-only

## Locks
- tip Soft SF LOCK 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — **tip_touched=NO**; catalog not touched.
- Soft SF invent HOLD (tip fill else); Soft SF F3 CLOSED; invent-ban: no new numbers; dimcalc outputs READ only, nothing re-run.
- Bridge PARTIAL / READY NO / NOT Cat A. Decisions verbal on Owner voice.
- Assignments file now sha 9e9118b864bd98c4801b0453af0c49cf27f57b7072c5f33a312bd9f083f95fcc (L52 logs "PR1 Rank36 DONE 04f1748a… → Rank32 scalar baselines").

## Rank 32 claim table
| # | Claim | Where (corpus) | Status |
|---|---|---|---|
| C1 | dim S₄(Γ₀(49)) = 10 (g=1,c=8,ε₂=0,ε₃=2) | MR1-AUTHOR-PROVE-P5A §3 L21 | **Author-proposed (numeric)**; standard literature formula, no numbered reference quoted |
| C1a | script reproduction: "scalar G0(49) S4 check: (18.0, 10.0, 8, 8.9e-16)" (M=18, S=10, Eis=8) | MR1-P5A-reverse-dimcalc .out L16 | Author-proposed numeric, read-only |
| C1b | Sanity: trivial SL₂ℤ → 0; Perm → 10 = dim S₄(Γ₀(49)) | MR1 §4 L26; dimcalc.py L93 | Author-proposed (method calibration) |
| C1c | S₄(Γ₀(49)) = 10, old₇=2, new=8 | MR2 Rank9 L31; MR2 Rank11 L33–34 | MR2 restatement (proposed) |
| C1d | Inventory row 7 "nonzero dim 10 (not a vanishing)" | CORPUS_VANISHING_INVENTORY L33 | catalog restatement → MR1 §3 |
| C1e | Merged stub row 32 | MERGED_VANISHING_MAP_STUB L54 | stub restatement → MR1 §3 + MR2 V-SCALAR-S2 |
| C2 | scalar S₂(Γ₀(49)) **>0** (49a line), "NONZERO baseline" | MR2 CORPUS-VANISHING-MAP L30 (V-SCALAR-S2), "standard dim formula" | **MR2-proposed / literature-standard**; **exact dim ABSENT** in corpus |
| C2a | Γ₀(49) genus 1 (input to C1, C2) | OWNER_WRITE Farey R14 L11; PHYSICIST P2 §1n | **Owner Write (Cat B)** |
| C2b | 49a line in S₂(Γ₀(49)) "not claimed" to vanish under W₇ | tip L426, L443 (via Inventory row 20) | Written tip non-claim, cite-only |
Owner Write of either scalar dimension itself: **ABSENT**.

## Source chain (full sha256)
- MERGED_VANISHING_MAP_STUB_2026-10-26.md b3e0d20ba9d428c0c0315fe27cfe8e5d4929fac2f762c442475b2aab07aa5627
- grok-batches/MR1-AUTHOR-PROVE-P5A-VANISHING_2026-10-26.md b829661e2a6b1ae49e743f111336ca2c4893bd90dd7a292ad05d8e03cd1b7e8d
- grok-batches/MR1-P5A-dimcalc_2026-10-26.py 0ecd4166edd333abb2bca0e6da9d9c9c5ab7dbd1a285bfc2d8bb503b8919861f
- grok-batches/MR1-P5A-reverse-dimcalc_2026-10-26.py bfd0141a873cbc2ea696e73ade614740f2483491e4fde48bdd0b4ea408256402
- grok-batches/MR1-P5A-reverse-dimcalc_2026-10-26.out e2b260385fe0b4ce55e04ba364b74163cb3c66d1c4e42fa97696c774e59473e9
- grok-batches/MR1-AUTHOR-REVERSE-ENGINEER-ALL-VANISHINGS_2026-10-26.md 8173e7b381ba858be90e5a46b453efaa369d63a40ff8bab24ca86f3681e17d9c
- MR2-FINDINGS-CORPUS-VANISHING-MAP_2026-10-26.md b271f42ab1cf0a3407e82f47d793ac549f056226805e9e29fa942f8808f629b9
- MR2-FINDINGS-P5A-REVERSE-ENGINEER-CONNECTION_2026-10-26.md 2b49ca25e96073e76dd64d8479f0d5b1985d41b74c3cdc4a11411b46677a9cec
- MR2-FINDINGS-RANK9-NEWSPACE-W49-PERM_2026-10-26.md c0f9843556a16974005deb01c70705074b24ef9278211566cee26e068fa687ec
- MR2-FINDINGS-RANK11-TEITELBAUM-STEINBERG7_2026-10-26.md 570cc00584bfa735284b99cd3e391b5acff6a7afcca24043dbe8f572b9f0e756
- CORPUS_VANISHING_INVENTORY_2026-10-26.md fb2983460ebadf7c8fe1d934d33ae05d57d725fcbf716933edb7780d273756c0
- OWNER_WRITE_TC_ISOTYPIC_R3_NO_VANISH_2026-10-26.md f861f571727140aa01f42b7410371d815aee50da4850bca1cf3dad8782255d63
- OWNER_WRITE_MR1_GAMMA0_49_GENS_FAREY_R14_2026-10-25.md b0b17c0c1f8cbed85710c652ed0f41c84d5fe9bf3c9a94eb5f2e279d45976f76
- grok-batches/PHYSICIST-P2-CUSP-PATH-C-DRAFTS_2026-10-26.md 731f6ba0e1ad781c205899ad4e2ad33d45237c61bbe351485d673cfdb1d113ce
- VANISHING_LEAD_ASSIGNMENTS_2026-10-26.md 9e9118b864bd98c4801b0453af0c49cf27f57b7072c5f33a312bd9f083f95fcc

## Backwards (corpus-only wording)
1. **Calibration anchor for P5a FAIL.** MR1 §4 says the Shapiro/Perm₅₆ RR formula reproduces "Perm → 10 = dim S₄(Γ₀(49))" and "trivial SL₂ℤ → 0". The scalar 10 is therefore what checks the method behind the vector-valued **592** (ρ̄) / 573 (ρ) result (MR1 §4–5; .out L28). If the scalar anchor failed, the 592 would lose its sanity check. The anchor holds as proposed. It is not a Written check.
2. **Non-vanishing is generic, not an artefact.** The scalar space is already nonzero at κ=4. MR1 §5 gives a leading term of 588 = 42·3·56/12 for the 42-dim ρ̄, and MR1 says vanishing "cannot hold … without a cut". The scalar baseline is consistent with that wording. It does not prove it.
3. **R3 contrast (κ=2).** MR2 V-SCALAR-S2 marks the scalar S₂(Γ₀(49)) as NONZERO and says it "Contrasts R3 (needs isotypic cut of V₄₂)". T-C Owner Write (f861f571…) cites proposed S₂(Γ₀(49),ρ̄|N₃₆)=167 and S₂(…|N₆)=33, so neither piece is {0}, and R3 is status NO-VANISH. The positive scalar S₂ baseline is consistent with R3 failing as well.
4. **Newspace link.** MR2 Rank9/11 split 10 into old₇=2 and new=8. The scalar W₄₉ eigen-split is ABSENT and is "not to be imported as ρ̄ data".

Net: the Rank 32 rows are **baselines, not vanishing claims**. They support the P5a FAIL and R3 NO-VANISH readings only as calibration and consistency. They are not proof.

## Gaps / what would strengthen (recommendation only)
- G1: No Owner Write and no Auditor MATCH for dim S₄(Γ₀(49))=10. A numbered literature cite (e.g. the standard dimension formula, Diamond–Shurman Thm 3.5.1) or an Auditor MATCH would raise it above Author-proposed.
- G2: The **exact** dim S₂(Γ₀(49)) is not stated anywhere in the corpus. Only ">0 / 49a line" appears. Genus 1 is Owner-Written (Cat B), so the standard identity dim S₂ = g would fix it. That is a Write that Owner or Author should make. PR1 does not record a number here (invent-ban).
- G3: MR1 §6 says the RR local-term formula is fitted, not quoted. The scalar anchor is one check. An independent κ=2 scalar anchor through the same fitted k=2 formula is not in .out.
- No blocker for report-only.

Bridge PARTIAL · READY NO · NOT Cat A · tip_touched=NO
