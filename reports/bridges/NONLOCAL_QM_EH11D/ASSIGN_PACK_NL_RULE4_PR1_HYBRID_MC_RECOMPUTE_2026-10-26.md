# ASSIGN PACK — Rule-4 PR1 Hybrid MC Recompute — 2026-10-26 (CDT)
From: Non Local Path → Target: **Physics Research 1** (agent id `f953b308-cfcd-4240-8277-77edda51f40e`)

## Authority
- Rule-4 OPEN OW `bc42067bf015fb321ac11e45c1b6a74019ed85a6294d21e80a4691442b09d1f8`
- ASSIGN pack task `c6e1fa269be0b794cb57064cc3e5367e87ac9db120ce20c4b50428a9106eb691`
- PASS/READY YES `7070d2b1ceaedaa148b5a918fb7ab79b48dbbbe2b560a03e5cd3cba3b586cfda`
- Runnable-spec Write B `WRITE_NL_HYBRID_MC_RUNNABLE_SPEC_POST_JOIN_PASS_2026-10-26.md` sha `27058bad386fc64dff071324e4f4d248a60113c68349917b42656c93025fe980`
- Standing Rules 4–5 `a04b55ce…`

## Task
Execute Rule-4 numerical recompute of the hybrid MC load defined in Write B / DESIGN `6bbc198e…` / deepen `ce6520ce…` / sheet `da91ad83…` under the PASSED join.

- Observables: E_leak(t) on RR-NL-SHEET-01 (primary); F_friction (secondary).
- Inputs (frozen, CITED): ρ_DM = 0.31 GeV/cm³; β_PBH = 0.18; κ_dark = 0.45; z = 1…118.
- Method: Corrected 7D §3.1 numerical integration (118-element reverse-parity; not lattice QCD). PR1 runs the compute.
- Success criteria: report recomputed χ²/dof; verdict MATCH / TENSION / INCONCLUSIVE vs Doc 0.79; no invent of new physics; Rank-20 δ_W₇ SAMPLE ONLY as optional flag (not FORCED, no ∀x).

## Hard excludes
- tip Soft SF LOCK `7cddb188…` untouched.
- Card4: C1 named 0.10 (`586dbac0…`) for reference only — **NO Zwegers/Path4 package numerics** (wait for Local Written asymptotic; then C1–C3 tolerance, C4 disclaimer, Path 8 exclusion).
- No Eigen/CRT/Q89; no tip invent.

## Delivery
PR1 ships FINDINGS path+sha to Non Local Path for Rule-5 review+relay before Owner/Physicist consume.

## NL Rule-5 watch: **OPEN** upon this pack.

- Card4 gate: C1 tolerance NAMED = 0.10 (OW `586dbac0d703a10f547277a7e9a61792da0da89c72dac4af1624af7ca117baff`); Path4/Zwegers physical-load package numerics remain GATED until Local lands Written asymptotic; then C1–C3 use 0.10; C4 disclaimer; Path 8 exclusion stands.
- This pack does NOT authorize Zwegers/Path4 package numerics (gated on Local Written asymptotic).
