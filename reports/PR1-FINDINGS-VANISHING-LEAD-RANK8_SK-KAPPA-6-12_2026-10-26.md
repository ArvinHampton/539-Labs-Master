# PR1 FINDINGS — Vanishing Lead Rank 8 / Q4: S_κ(Γ₀(49), ρ̄), κ=6,8,10,12 (k=−2)
Date: 2026-10-26 ~11:10 CDT (America/Chicago). Worker: Physics Research 1 executor. Report-only.

## Locks
- Soft SF tip LOCK `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` — cite only; **tip_touched=NO**; catalog not touched.
- Soft SF invent HOLD; Soft SF F3 CLOSED. invent HOLD: no new numbers; dimcalc **not** re-run (existing `.out` read only).
- Bridge **PARTIAL / READY NO / NOT Cat A**.

## Sources (sha256 verified on-box this run)
| Source | Path | sha256 |
|---|---|---|
| reverse-dimcalc `.out` (34 lines, nonempty) | grok-batches/MR1-P5A-reverse-dimcalc_2026-10-26.out | `e2b260385fe0b4ce55e04ba364b74163cb3c66d1c4e42fa97696c774e59473e9` ✓ |
| AMEND-2 (MR1 reverse-engineer-all, §8) | grok-batches/MR1-AUTHOR-REVERSE-ENGINEER-ALL-VANISHINGS_2026-10-26.md | `8173e7b381ba858be90e5a46b453efaa369d63a40ff8bab24ca86f3681e17d9c` ✓ |
| P5a prove FAIL FINDINGS | grok-batches/MR1-AUTHOR-PROVE-P5A-VANISHING_2026-10-26.md | `b829661e2a6b1ae49e743f111336ca2c4893bd90dd7a292ad05d8e03cd1b7e8d` |
| MERGED_VANISHING_MAP_STUB | quantum-comp/reports/MERGED_VANISHING_MAP_STUB_2026-10-26.md | `b3e0d20ba9d428c0c0315fe27cfe8e5d4929fac2f762c442475b2aab07aa5627` |
| CORPUS_VANISHING_INVENTORY | quantum-comp/reports/CORPUS_VANISHING_INVENTORY_2026-10-26.md | `fb2983460ebadf7c8fe1d934d33ae05d57d725fcbf716933edb7780d273756c0` |
| Assignments (drifts) | quantum-comp/reports/VANISHING_LEAD_ASSIGNMENTS_2026-10-26.md | `6c6497287601fb3dd9fd6e9cf49afcfc91b3d6cd2a0d44ac6020a9c35e9558cb` (Q4 row line 28) |
Script cited by AMEND-2: `MR1-P5A-reverse-dimcalc_2026-10-26.py` sha `bfd0141a…` (not re-run).

## Claim table κ → dim S_κ(Γ₀(49), ρ̄) → source
| κ | `.out` line (rhobar, G0(49) M,S,Eis) | dim S | S_new | SL₂ℤ S | AMEND-2 / V11 | Proposed | Status |
|---|---|---|---|---|---|---|---|
| 4 (ref) | 603 / 592 / 11 | 592 | 581 | 11 | V3/V11: 592 | — | P5a **FAIL** (cite) |
| 6 | 995 / **984** / 11 | 984 | 966 | 18 | 984 (l.118, V11) | 984 | **VERIFIED-cite** (numeric proposed) |
| 8 | 1387 / **1376** / 11 | 1376 | 1351 | 25 | 1376 (l.119) | 1376 | **VERIFIED-cite** |
| 10 | 1779 / **1768** / 11 | 1768 | 1736 | 32 | 1768 (l.120) | 1768 | **VERIFIED-cite** |
| 12 | 2171 / **2160** / 11 | 2160 | 2121 | 39 | 2160 (l.121) | 2160 | **VERIFIED-cite** |
Residuals on all rows ≤ 1.4e-15. Arithmetic note (cite-only consistency, no new number): consecutive even-κ step = 392 in every row.

## Verify matrix
| κ | .out | AMEND-2 | MERGED stub (row 8) | CORPUS inv (row 12) | Result |
|---|---|---|---|---|---|
| 6 | 984 | 984 | 984 | 984 | MATCH |
| 8 | 1376 | 1376 | 1376 | 1376 | MATCH |
| 10 | 1768 | 1768 | "…" | "…" | MATCH (.out/AMEND-2) |
| 12 | 2160 | 2160 | "…" | "…" | MATCH (.out/AMEND-2) |
**Tuple (984, 1376, 1768, 2160) MATCHES.** No CONFLICT, none ABSENT.

## Backwards inference (corpus only)
- All four even weights give dim S_κ ≫ 0 with growing dims → raising even κ never frees vanishing (AMEND-2 V11 "Raising even κ alone never vanishes"; stub row 8).
- Consistent with P5a FAIL @ κ=4 (592 > 0, FAIL FINDINGS b829661e…): the obstruction is not weight-specific; κ=4 is the smallest member of the same nonvanishing even-κ ladder. Odd κ vacuous by ρ(−I)=I (V4/R1); no Γ₀(49)-invariants (`.out`: dim invariants = 0) so no scalar×fixed-vector kill (V1).
- Per AMEND-2 V13: uniqueness survives via M_{−2}(Γ₀(49),ρ)={0}; existence remains a finite linear-condition problem — not freed by κ.

## Gaps / recommendations (no invent)
1. **Stale GAP:** CORPUS_VANISHING_INVENTORY row 12 says `.out` is 0 bytes (e3b0c442…). On-box `.out` is now nonempty, sha e2b26038… — recommend inventory owner amend (not done here).
2. MERGED stub row 8 marks "C3 not reproduced" and lists script hash only; recommend adding `.out` sha e2b26038… + AMEND-2 sha 8173e7b3….
3. All dims remain **numeric proposed** (floating-point SVD, single script); no independent exact/second-method reproduction — status cannot exceed VERIFIED-cite.
4. Dims are total cusp dims; S_new column also present — downstream users should specify which.

## Status
Rank 8 / Q4: **VERIFIED-cite (numeric proposed), tuple MATCH, ≠0 at κ=6–12.** Bridge PARTIAL / READY NO / NOT Cat A. tip_touched=NO.
