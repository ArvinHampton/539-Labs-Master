# AUDITOR FINDINGS — t1218u MR1 exact-c Cat B CONFIRM — 2026-10-25 (America/Chicago)

**Verdict: MATCH-with-SF** · Clear-for-fold: **YES** (no hard blocker) · Bridge PARTIAL · READY NO · Cat B (not Cat A)

## Hashes (verified)
| Artifact | expected | live | |
|---|---|---|---|
| OWNER_WRITE_MR1_EXACT_C_t1218u_2026-10-25.md | 7a86075e…b020f | 7a86075e96ae6647f51dfcdf21296310da6380a620f40b0ec2559fcf4edb020f | MATCH |
| MR1-AUTHOR-PURSUE-W7-GENS-K-EXACTC_2026-10-25.md | 0a7f773e…c569e | 0a7f773e05c139ea1b45bab3291a8740df823ddf16a7b3fe7f74c9b76cad569e | MATCH |
| heavy-daily/2026-10-18-V42-Structure/rel.pkl | f8dadf42… | f8dadf42d8bd1bb4f03e572b9c7616e5745e44dc21c4ae8fb5e4b56d2617e511 | MATCH |
| Prior V₄₂ Write (cited in Write inputs) | 9fe6172f… | cited consistently | MATCH |

## Independent re-check of rel.pkl c
Loaded pickle (dict, 2 keys); 159 (i,j,c) triples; 6 unique c (tol 1e-5). Nearest ζ₁₀^k and |err|:
- 1 → k=0, 0
- −1 → k=5, 1.2e-16
- 0.809017+0.587785i → k=1, 2.52e-7
- 0.309017+0.951057i → k=2, 4.84e-7
- −0.809017−0.587785i → k=6, 2.52e-7
- −0.309017−0.951057i → k=7, 4.84e-7
Set = {1,−1,ζ₁₀,ζ₁₀²,ζ₁₀⁶,ζ₁₀⁷} ⊂ μ₁₀ ⊂ ℚ(ζ₅). Max err 4.84e-7 (≤4.9e-7 claim). All |c|=1 to ≤4.7e-7. Closed forms in Write table consistent. Status correctly Cat B (numerical recognition, not proof).

## Exclusions
W₇ on V / Γ₀(49) gens / k=−2 reconciliation: stated ABSENT / NOT Written in both Write and source FINDINGS (§2–§4). MATCH.

## Tip
Write cites tip 70c47a4c… "not edited". Live tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` sha256 0677d02a10f298d0e84f41f6da876fe6ed4b886b92000ed70e9cec3be6173ca3 (sidecar agrees), mtime 20:47:47 CDT = MR2 P-fgeom §1k fold, predates this Write (~20:48). Live tip contains no ζ₁₀/μ₁₀ exact-c text → Write did not edit tip. Tip untouched: **Y**. No fold performed by Auditor.

## Soft SF
- SF-1: Write/brief cite tip 70c47a4c… as live; stale vs live 0677d02a… (MR2 fold, not this Write). Fold must be applied against 0677d02a….

No outbound messages sent.
