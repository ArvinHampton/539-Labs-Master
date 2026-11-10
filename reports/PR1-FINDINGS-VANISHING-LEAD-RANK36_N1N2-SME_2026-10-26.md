# PR1 FINDINGS — Vanishing Lead Rank 36 (Q11): PR1-N1/N2 no-signalling; SME κ̃ bounds — 2026-10-26 ~11:05 CDT
Report-only. Owner voice via Physicist. invent-ban ON; no new numbers.

## Locks
- tip Soft SF LOCK `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` — cite only; **tip_touched=NO**. Catalog not edited.
- Soft SF invent HOLD (tip fill else). Soft SF F3 CLOSED.
- Bridge PARTIAL / READY NO / NOT Cat A.

## Sources (re-verified)
- Prior PR1 vanishing map `PR1-FINDINGS-CORPUS-VANISHING-MAP_2026-10-26.md` sha `d76991c3f3ae7c8621d5c27d9556c8bafd74a307930a8e137b8320da967f6d61` — MATCH (rows PR1-N1 L12, PR1-N2 L13).
- Catalog `/workspace/obs-data-PR1-HEPP-QM-GR.md` sha `6c680789ff64a7bb1a83276690e20a1748d8d2a31f19a97b869c13109b77f33d` — MATCH.
- Assignments `VANISHING_LEAD_ASSIGNMENTS_2026-10-26.md`: given sha `348bf88e…` **DRIFT** → now `df2523abad55689c1e6525354b16c32e229fa511254591aa17817aa7a456100f` (log-line appends; Q11 → Rank 36 → PR1 row L35 still present; L50 records PR1 Rank10 DONE → Q11 Rank36). Non-blocking.

## Rank 36 claim table
| ID | Claim (catalog, verbatim gist) | Line | Modular (κ,k) | Linked residual-C? | Status |
|---|---|---|---|---|---|
| PR1-N1 | Bell violations with no signalling, no Tsirelson violation; later exposed-field Write must not permit signalling | L224 — still matches | N/A | No (ties to Written (c)) | Non-modular null constraint |
| PR1-N2 | SME photon bounds incl. c_(I)00^(4)=√(4π)κ̃_tr ~10⁻¹⁹, (κ̃_e−)_XY ~10⁻²² (upper limits) | L233 — still matches | N/A — **SME κ̃ ≠ modular κ** (notation collision) | No | Non-modular upper limits |

## Re-grep since map (10:53 CDT)
Scope: catalog, `quantum-comp/reports/PR1_*` (all mtimes ≤ 10-26 00:34, pre-map), `PR1-FINDINGS-VANISHING-LEAD-RANK10_SL2Z-DIM11` (sha `1a2ab47b…` verified; only new PR1 file), `/workspace/author-written-identity-gaps-PR1-FINDINGS.md` (mtime 10-25 17:15, pre-map). Pattern: modular κ/k + vanish/residual-C. **Hits: 0.**
- **Modular κ/k vanishing linked to residual-C: ABSENT.**

## Status
- Rank 36: keep non-modular. **FLAG=NO.**
- Bridge PARTIAL / READY NO / NOT Cat A. tip_touched=NO.
