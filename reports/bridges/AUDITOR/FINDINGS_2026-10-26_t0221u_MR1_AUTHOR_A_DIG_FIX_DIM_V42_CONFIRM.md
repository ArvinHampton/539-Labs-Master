# Auditor FINDINGS — MR1 Author A-DIG dim Fix(S_lab⁻²) on V₄₂ — CONFIRM (2026-10-26 02:21 CDT America/Chicago)
Scope: CONFIRM-only. No tip edit, no fold, no invented physics. Auth: Owner t1728s8568 (A-DIG then B-HOLD), t1729s8579.

## Verdict: **MATCH-with-SF**
Proposed fill dim ker(S_lab⁻² − Id)|_{V₄₂} = **42** reproduced by independent re-run. Not 0 → no STOP / no A-WALL. Restriction to V₄₂ succeeded.

## Hashes (recomputed)
| item | path | sha256 | status |
|---|---|---|---|
| Author FINDINGS | /workspace/grok-batches/MR1-AUTHOR-A-DIG-FIX-DIM-SLAB-INV2_2026-10-26.md | 23360aa6b9b8e13b19108a098946c51dee5eb8c2bcf61cedce16b073faaf3713 | MATCH |
| WRITE | /workspace/grok-batches/MR1-AUTHOR-WRITE-A-DIG-FIX-DIM-SLAB-INV2_2026-10-26.md | 5b269ed51f399ce26aab37d135b8b5d3c7e1112bc74487b76ce5736d4f744e57 | MATCH (prefix 5b269ed5) |
| script | /workspace/quantum-comp/scripts/adig_fix_dim_slab_inv2_2026-10-26.py | a804c96c8f1abb44807fba0c2aafc716199aa1f5f966d8ee1bb5283c05117198 | MATCH |
| output | /workspace/quantum-comp/scripts/adig_fix_dim_slab_inv2_2026-10-26.out | 0afe5ea4222b6a3cbbac759f0dcccd01333c1e4aaaa0e994d062113cd584cd30 | MATCH |
| tip Soft SF LOCK | /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md | 5569b14f4b1bbeceba1a6c33ae4cd48bfdc6630484a6bd5b8a0caef3866dfa93 | MATCH; tip_touched NO |
| C5 Cross-Review | stage_rev4/.../Cross_Review_2026-10-18/2026-10-18-Cross-Review.md | 17f5733de060409f3424b45012abdf6027e244262e41c67626a9ca80bad0c4f0 | MATCH |
| V42-Structure | stage_rev4/.../V42_Structure_2026-10-18/2026-10-18-V42-Structure.md | 234c9128bca04fe584e79952a1d534d2762a9edbc760062778ac7aa6c7962ed0 | MATCH |
| OUTPUTS bundle | stage_rev4/.../V42_Structure_2026-10-18/OUTPUTS_BUNDLE_2026-10-18.txt | 1efca730ca983baae515c0cef6815ff7f979f1f57683a822b6fe74273dbb6543 | MATCH |
| v42.py | heavy-daily/2026-10-18-V42-Structure/v42.py | 184ff4b452affbee6660fa7a41428615e9f9212ffd668599b2bd200a22b2943d | MATCH |
| family.py | heavy-daily/2026-10-18-V42-Structure/family.py (identical across copies) | 07dabdaa1efbc52773f964547829925f4c7340a67cd0d2fc1bc92bb9ef686498 | MATCH |
| uvec.py | heavy-daily/2026-10-17-cusp-part/uvec.py | 8195a613f7472bbd480873bcab494770341669d9a36a3955c9d1c46a3a913817 | MATCH — **SF flag** |
| fitF.pkl | heavy-daily/2026-10-17-cusp-part/fitF.pkl | 38381938398edcf9cacb9e5dbc0b8715d29f45614e42653d8146555f42a1420f | MATCH (import chain only) |

## Checks
1. FINDINGS/WRITE/script/output hashes: PASS.
2. Tip 5569b14f live; tip_touched NO: PASS.
3. Re-run of script (2026-10-26 ~02:21 CDT): rc 0; non-sha lines identical to stored .out; `RESULT dim ker(S_lab^-2 - Id) on V42 = 42`; dim V=42, gap 0.655 vs 6.6e-16; (S_lab⁻²−Id)|_V max sv 8.13e-16; exact Pexact²=I; ambient Fix=72 (not pasted onto V₄₂). C5 relations reproduced. PASS.
4. Invent-ban: only 2026-10-18 Author S/P material + Owner-cleared code; no tip invent. **SF-1:** uvec.py 8195a613 (+ fitF.pkl via import) from 2026-10-17 cusp-part folder — dependency of v42.py, not in the 2026-10-18 authorization list as such; Owner to clear. Not an invent (Author code, unmodified hash), so not REJECT.
5. Cat B / no A-WALL consistent with Soft SF F3 CLOSED (ρ(−I)=S_lab⁻²): PASS. **SF-2:** containment V₄₂⊂Fix(P) is floating-rank (decisive gap) + structural (V42-Structure W=Fix(P)); correctly labeled Cat B, not Cat A. **SF-3:** carrier identification family.py A=[[2,7],[7,7]] ↔ tip N₂ Gram relies on prior Auditor t1131u/t1135u chain, not re-proved.
6. No tip fold; Components B-HOLD untouched; Bridge PARTIAL READY NO: PASS.

## Status
Proposed fill (Author §6) eligible for Owner Write consideration; nothing folded. Owner decision needed on SF-1.
