# AUDITOR FINDINGS — t1135u MR1 Cat B V₄₂ basis FOLD re-CONFIRM — 2026-10-25 ~20:42 CDT (America/Chicago)

**Verdict: MATCH-with-SF** (fold is clean; one Soft SF is about sidecar housekeeping only)

## Shas (verified on disk)
| Artifact | sha256 |
|---|---|
| Live tip post-fold `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` (LOCK) | `70c47a4c40f4ff4fdf19a0c4488ba16b3e040680b482657f9e4c763b2cdd9ed3` |
| Pre-fold backup `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.pre-v42-basis-fold-c7121aa8.md` | `c7121aa8bf7d2e534f0ad55ce1b4a1a1a26db8289087979f3a263efe9565a5ef` |
| Fold stamp `OWNER_WRITE_MR1_V42_BASIS_FOLD_t1135u_2026-10-25.md` | `9c0752ff61c4563262a1c94369d8f4c8bdb463f9a159b60012c975654eec4442` |
| Write `OWNER_WRITE_MR1_V42_BASIS_t1135u_2026-10-25.md` | `9fe6172f7404e9ccbcf1bd4125675cf1319cc924a5f7dc8d1e0ca11273c32592` |
| Prior Write-CONFIRM `FINDINGS_2026-10-25_t1135u_MR1_V42_BASIS_CAT_B_CONFIRM.md` | `a0f7212d0e3098a41411b97d769d8886732c568ad0545b7e1b513b3846c428e9` |
| relations.py (as recorded in the tip) | `12730d9515b711e8c46aa1ae10f9fcabf53233d22dcaac4262a1d0d67b63efac` |

## Diff summary (backup → tip)
Three hunks. Every change is new §1j text or text inside §2 P1 (L161–184). §3 and later are unchanged.
1. **+§1j ledger** (new L152–160): lists the Write and CONFIRM shas, folds W-V42-1 into §2 P1 only, names the backup, and states READY NO / Bridge PARTIAL / NOT Cat A. Its "Not folded" list covers exact c, ρ matrices, W₇ rule, Γ₀(49) gens, k=−2 vs wt-0, and Z₇↔W₇.
2. **§2 P1 carrier bullet:** the text "42-basis … still ABSENT" is replaced by "No numeric 42×42 ρ matrices" plus a pointer to the Cat B basis. A new **V₄₂ monomial class basis** bullet is added: Cat B, float-complex c, 42 reps from 129 nonzero labels (3×1, 15×2, 24×4; 11 zero), "Not a ρ matrix Write", "No Z₇↔W₇". It records the full relations.py sha (**this clears Write-CONFIRM SF-1**), plus the shas for rel.pkl, V42-Structure, and deepen.
3. **§2 P1 Slots line `[[ ρ ]]`:** a wording update that adds "Cat B V₄₂ monomial class basis t1135u". G, V, k=−2 and multiplier are unchanged. k=−2 was already in the tip and is not new.

## Checks
- W-V42-1 folded into §2 P1 only, plus the §1j ledger: MATCH
- relations.py full sha recorded: MATCH (SF-1 cleared)
- Cat B and no Cat A promotion; Bridge PARTIAL / READY NO: MATCH
- N₂ carrier, Ω_11D≡1 and 55-Step content preserved (Ω_11D/55-Step grep count is 5 in both files; §1i untouched): MATCH
- No new Z₇↔W₇, W₇ rule, Γ₀(49) gens or k=−2: MATCH
- Float-c hygiene (no exact c, no ρ matrices claimed): MATCH
- Fold stamp table matches the on-disk shas: MATCH

## Soft SF
- **SF-1 (housekeeping):** the tip sidecar `residual-c-field-WRITTEN_PREMISES_DRAFT.md.sha256` still reads `c7121aa8…` (pre-fold) while the live tip is `70c47a4c…`. The Owner should refresh it. The Auditor did not edit it.
- **SF-2 (wording):** the §1j heading/status still says "pending Auditor re-CONFIRM". It can be updated to cite this FINDINGS on the next Owner touch. This does not block.
- Carry-forward: Write-CONFIRM SF-2 (source paths) and SF-3 (6-dp c) stay as Cat B caveats. SF-4 (re-CONFIRM on fold) is discharged by this document.

Tip not edited by Auditor. No outbound messages.
