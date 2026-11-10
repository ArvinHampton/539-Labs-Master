# WRITE — Hybrid MC RUNNABLE-SPEC UPDATE post NL-JOIN-1 PASS — 2026-10-26 (CDT)
Author: Non Local Path

## Status
**RUNNABLE-SPEC UPDATE** — not a completed MC run; not a pass of numerics. DESIGN `6bbc198e9a73ef8d80b8d7c1127404b3226faf66f4893272ba0fdaadd465968b` (FINDINGS_NL_HYBRID_MC_PROJECT_MATH_2026-10-26.md) upgraded to a join-wired runnable-spec under PASS/READY YES `7070d2b1…`.

## Named gap (as ACK'd)
**GAP:** Hybrid Monte Carlo remains DESIGN-only while NL-JOIN-1 is PASS / READY YES — highest leverage is a **runnable hybrid-MC load wired through the passed residual↔NL join on RR-NL-SHEET-01**.
This Write is the FIRST concrete step under press-further OW `d3c2a26dd6ec4a08527e27f2738c2031bf83f1294c14619b0cf667ec5dcd3b92`.

## Runnable load (for PR1)
- Primary observable: **E_leak(t)** on RR-NL-SHEET-01 ("RPPT118 E_leak(t) load"); secondary: **F_friction**.
- Join wire: residual packaging / g_s ↔ NL E_leak through g_s X^M (PASSED NL-JOIN-1; PROOF `946a5910…`, sameness `e41ceac4…`).
- Frozen params (sheet `da91ad83ac35a2f3a897dbd1794b90d102b409284012b889d6b74849e3af5998`, CITED from Corrected 7D, not invented): ρ_DM = 0.31 GeV/cm³; β_PBH = 0.18; κ_dark = 0.45; element sum z = 1…118.
- Reference band: Doc-quoted χ²/dof = 0.79 — **reference only** until PR1 recomputes.
- Rank-20 δ_W₇ (`85c9c5cf…`): SAMPLE ONLY status flag / optional stratification hook. NOT a proof obligation; NOT FORCED; no ∀x requirement.
- MC structure: Corrected 7D §3.1 (`4758d180…`) 118-element reverse-parity integration of E_leak(t) (deepen `ce6520ce…`) — not lattice QCD.

## Non-goals
- No tip Soft SF invent; tip LOCK `7cddb188…` untouched.
- No Card4/Zwegers/Path4 package numerics (C1 named 0.10 per `586dbac0…` but gated on Local Written asymptotic).
- No Eigen/Q89/CRT.
- NL does not run numerics — Rule-4 → PR1.

## Success criteria for later PR1 Rule-4 FINDINGS
1. Recompute E_leak integration over z = 1…118 with frozen params.
2. Report recomputed χ²/dof vs Doc band 0.79.
3. State MATCH / TENSION / INCONCLUSIVE vs reference.
4. Ship FINDINGS path+sha to NL for Rule-5 relay (`a04b55ce…`).

## Invent authority
Lifts `c6e9aad7823f14b0bf134c34daaac0d4edf9cc971aa630ec7444da430555e353` (general) + `fe2ee91204797cff827acd78cf597707f763ca8a63ac51872b7602a7a7316356` (hybrid-MC-FIRST) cover this scope.

- Card4 gate: C1 tolerance NAMED = 0.10 (OW `586dbac0d703a10f547277a7e9a61792da0da89c72dac4af1624af7ca117baff`); Path4/Zwegers physical-load package numerics remain GATED until Local lands Written asymptotic; then C1–C3 use 0.10; C4 disclaimer; Path 8 exclusion stands.
