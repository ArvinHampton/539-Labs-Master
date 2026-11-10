# NL RELAY — PR1 Rule-4 hybrid MC recompute FINDINGS (Rule 5) — 2026-10-26 ~16:42 CDT America/Chicago
Authority: Owner Standing Rules 4–5; Rule-4 OPEN OW `bc42067bf015fb321ac11e45c1b6a74019ed85a6294d21e80a4691442b09d1f8`; ASSIGN pack `3a6e41d9f9c7227cb1f0c61007c63eeaf2bfb8bddd33526790d078f30d9fefd3`; runnable-spec `27058bad386fc64dff071324e4f4d248a60113c68349917b42656c93025fe980`; PASS/READY YES `7070d2b1ceaedaa148b5a918fb7ab79b48dbbbe2b560a03e5cd3cba3b586cfda`.

## PR1 FINDINGS (verified live)
- Path: `/workspace/quantum-comp/reports/PR1-FINDINGS-RULE4_HYBRID_MC_RECOMPUTE_2026-10-26.md`
- sha256: `8e6d0b8affda74855e6dc4d8af7de85bdafb053cc97d49f9b015cfae9501e2c1`
- tip Soft SF LOCK: `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` tip_touched **NO** (re-verified at relay)

## NL review (Rule 5)
**ACCEPT — verdict INCONCLUSIVE stands.**

| Check | Result |
|---|---|
| Authority pack / runnable-spec / OW shas | MATCH on disk |
| tip Soft SF LOCK tip_touched NO | MATCH |
| χ²_recomputed vs Doc 0.79 | **ABSENT** — no Written data set / dof / full E_leak–F_friction coefficients; none invented |
| Doc-full §3.1 integration | **NOT RUN** (honest ABSENT inventory) |
| What ran | minus-PT 118 structural inventory; reduced-form `corrected_E_leak.py` samples only (CHI2_DOF hard-coded 0.79 in script — not a recompute) |
| Rank-20 | SAMPLE ONLY / NOT FORCED — unused in verdict |
| Zwegers/Path4 / Eigen/CRT | excluded as required |
| Invent of missing coeffs | **NONE** — compliant |

## Substance
Rule-4 open under PASS/READY YES was executed within Written bounds. Recompute cannot produce MATCH or TENSION against Doc χ²/dof = 0.79 until Owner supplies (or unlocks) a Written observational data set, dof, and the missing E_leak/F_friction coefficients (including numerical g_s X^M if required for Doc-full load). Reduced-form samples and structural 118-check do **not** flip READY / PASS on numerics. Lemma NL-JOIN-1 PASS / READY YES (structural) **stands unchanged** — this FINDINGS does not reopen the join.

## Next (recommend; not auto-opened)
- Owner Write (or corpus unlock) for missing Written coefficients / χ² data set+dof if Doc-full recompute is desired.
- Hybrid MC remains runnable-spec + INCONCLUSIVE recompute record; not a numerics pass.
- Path4/Zwegers C1–C3 still HARD GATED (Local asymptotic accept + D1-norm ID) — separate from this Rule-4 lane.

## Explicit
No tip fold. Soft SF CONFIRM Write-only / no tip Soft SF re-pin. No Card4 Path4 package numerics authorized by this relay.
