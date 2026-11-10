# FINDINGS — t665u Local residual-C deduce CONFIRM — 2026-10-25 00:27 CDT (America/Chicago)
Auditor: Residual-vs-Resonant. Scope: Local only (BRIDGE_C_35/deduce_t665u). NL W-PO-2 not taken (sibling auditor). No physics invented; no verdict altered.

## Live sha256 vs claimed — 5/5 MATCH
- deduce_t665u/PREREG.md 9bcb0b44a474066c4b67b28e8af46c158c6c58240483feae484842cd9e7a05d8 MATCH
- deduce_t665u/RESULTS.md 50b6b065f3b4c245238b85a6a2f13b74e4f3666c29e490ef1bcd7da2617b2783 MATCH
- deduce_t665u/SHA256SUMS 7dbebe09eeb4eba640d108716bbeb70dd8b2207b568fda9dc15c4eb4934c4136 MATCH
- STREAM_IDLE_LOCAL.md 37c31a39316ba241ab9d04077f2122724642775eae5d601762dafe424a937398 MATCH
- inventory_check/SHA256SUMS 6f3f42877399fc006ce47d35346b7ccbfe609048cf6d43889b8230f32fa4ca87 MATCH
sha256sum -c: deduce_t665u 3/3 OK; inventory_check 18/18 OK.
Order: PREREG mtime 00:24:19 CDT < RESULTS 00:24:45 CDT; PREREG.sha256 matches; RESULTS cites PREREG sha.

## Claims
1 Premise pins: CONFIRMED — all 14 full shas in PREREG recomputed live, all match (G1, INGEST, order77 x3, EXTRACT T658U/T635U, W7 pin, ledger 7dbd63af, t658u FINDINGS d17f83cf, 4 Extract-A sources).
2 DEDUCED cite Written shas: CONFIRMED (every D-* cites short sha+line); spot-check 7368b855 L24–36 and 7add2a9a L12/L35 text matches.
3 Uniqueness failure: CONFIRMED — 4-param ansatz = exact interpolant of 4 ratios; Written deg-3 polynomial also interpolates (7add2a9a L35). Auditor arithmetic re-check of Written coeffs reproduces 19.8012/3.1607/20.6652/55.3021 (no new numbers adopted). No closed form claimed.
4 No numeric invent: CONFIRMED — no outer_*, no h values, δ≡0 not presented as FOUND (RG-T665b ABSENT-with-gap).
5 SF-W7-3 fence: CONFIRMED — Closure trees noted not read as law; no Closure source among pins.
6 Bridge PARTIAL / READY NO / residual-C OPEN: CONFIRMED, no overclaim.
7 order78 not started: CONFIRMED (no order78* dir; text says NOT started).
8 CORE_FREEZE / Local only: CONFIRMED; no NL file mutation claims.
9 Free invent: none found in deduction chains.

## Soft flags (no verdict change)
- SF-T665-1: STREAM_IDLE_LOCAL entry stamped "~00:35 CDT" but file written ≤00:25 CDT (future-dated label).
- SF-T665-2: RESULTS cites short shas 1e18a87d, ee4f4fc0 that are NOT in PREREG pin list despite "short shas refer to full shas in PREREG"; they do appear in inventory_check files — pin fully next pass.
- SF-T665-3: Extract-A sources pinned from _git_v8_unpushed_clone path while inventory SHA256SUMS lists oct17-master path variants; both OK by sum but dual-path provenance should be noted.

## Open set
residual-C OPEN; Bridge PARTIAL; READY NO; order78 not started; RG-T665a–d ABSENT-with-gap; X4 equality unshown; W-PO (NL) untouched by this audit.
Blockers: none.
