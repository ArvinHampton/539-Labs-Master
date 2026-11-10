# FINDINGS — Residual law C candidate (Fricke W7), t625u
Stamp: 2026-10-24 23:20 CDT (America/Chicago). Auditor: soft flags only; PASS/FAIL untouched; local/nonlocal maps separate.

## Live shas
- pins/RESIDUAL_LAW_C_CANDIDATE_W7_2026-10-24.md b9a214385ef8c550570a20327e5ef1f74f4608ddd355b8cba78ba6782e303f90 (MATCH)
- pins/SHA256SUMS ef3bd9229f9240674ebf81cabe10554b0e0a2235681dfee6dbd6405baf2d823f (MATCH ef3bd922…); sha256sum -c 10/10 OK
- Parents unchanged: trunc b77fe22b…, OMEGA_F c9c3b30d…, ledger ffc93ae4…, confirmed b10193b4…, t604u 7dbd63af…, G1_REOPEN 6c66dbc0…, W_PO1 003e74bf…, P_orth a6dfcec4…, PIN_LEDGER_UPDATE 6de428d8…

## Written (candidate) vs OPEN
- Written: cocycle definition δ_W7 h(x) = h(x) − residual_slash(x)·h(W7 x) as OPEN candidate.
- Written (stated, not evidenced): vanishing to machine precision at x = 1/7, 3/7, 5/7, 1 with residual_slash recovered from span of C_axis residual periods, completion of Θ_third, Eichler integral of Ξ shadow.
- OPEN: exact identity δ_W7 h ≡ 0 for all x — explicitly "not yet proved".
- Written: Zwegers completion → H_s, NOT C. Separation OK.
- Non-clearances: no Bridge YES / READY YES; no closed form for residual_slash; G1/Ξ HOLD/GATE 640da80d… unaffected.

## Invent-ban
- Pin carries invent-ban on proof / closing δ≡0. No Cat A elevation of the candidate identity; no close claim. OK.

## residual-C disposition: OPEN (no hashed exact-identity proof on disk).

## order76: ABSENT on disk (only order75). WATCH. No PREREG invented; no RESULTS audited.

## Soft flags
- SF-W7-1: Sample-point vanishing is chat/pin-text only — no hashed numeric artifact (values, precision, residual_slash recovery script). Not evidence-grade until hashed.
- SF-W7-2: Hygiene line "Category A discrete" in pin header could be misread as Cat A status for the candidate; body is clear it is OPEN. Wording watch only.
- SF-W7-3: Legacy files reports/heavy-daily/*Residual_Law_C_Closure* (2026-08-25, plus copies in _git_v8_unpushed_clone and self-audit/repo) title a "closure". Not cited, not in SUMS; must not be used to close residual-C. Watch for conflation.
- SF-W7-4: residual_slash only described by "recovery"; W7 action on x (incl. x=1 fixed/cusp behavior) not specified in pin. Definitional gap for any future proof.

## Open set (unchanged by this audit)
residual-C OPEN; RG75e OPEN; G1 OPEN≠ACCEPT; Bridge PARTIAL; READY NO; W-PO-2 OPEN (narrowed); W-PO-3 OPEN; W-NL-1/2 OPEN; W-PIN-3 watch; Ξ HOLD; GATE 640da80d… binds; soft N-SB1-2, N-T617U-1/2, SF-75-1..4 carried; order76 watch. Closed (untouched): S-B-1, W-74-1.
