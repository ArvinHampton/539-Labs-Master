# FINDINGS — order74 (BRIDGE_C_35 LOCAL)
Auditor, 2026-10-24 ~23:12 CDT America/Chicago. Residual-vs-Resonant lock. No invent; PASS/FAIL not altered (flag only).

## Hash (live)
- PREREG 42850e59… MATCH; RESULTS 68ff36f5… MATCH; GATE_DECISIONS_ADDENDUM 43b5db7f… MATCH; STREAM_IDLE_LOCAL bdaf4a6f… MATCH (data/ and root copy).
- order74/SHA256SUMS -c: 16/16 OK. order57 GATE_DECISIONS 640da80d… unchanged. Pins 6c66dbc0…, 003e74bf…, a6dfcec4…, b10193b4… OK.
- data: numeric_C.py b40c913c…, numeric_C_N40.json 036d1678…, numeric_C_N40_table.txt e837816c… OK.
- Re-scan for RESULTS_ADDENDUM / SUMS refresh: **ABSENT** (dir unchanged since 23:08).

## Claims
1. G1 **OPEN ≠ ACCEPT** — confirmed (addendum + RESULTS). order68 REJECT reasons uncured; REJECT 640da80d… binds until ACCEPT; Ξ HOLD; no numeric Ξ.
2. RG74c numeric C — reproduction: re-ran numeric_C.py → JSON byte-identical to hashed json; table identical; R=200≡R=400; 0 negative exponents. Script uses pinned M=[[2,s],[s,s]] (W-PO-1 003e74bf…), B=v^T M w, sgn(0)=0 (pin 6c66dbc0…), c1/c2, Q_s — no invented ingredients. **However N=40 is a PREREG choice; pin says only "Degree truncation" with no degree.**
   - Per coordinator/Physicist hygiene (~23:09): RG74c retag PASS → **SKIP** (exploratory) accepted. Auditor does not alter label; **W-74-1 (flag):** RESULTS 68ff36f5… still reads "PASS (computed, N=40)" while SKIP accepted; no hashed addendum on disk. RG74c final disposition **HELD** pending addendum. Numeric table reproducible as exploratory data only.
   - Minor: numeric_C.py requires argv[1] (crashes without it) — info only.
3. Residual law C **OPEN**; Bridge **PARTIAL**; READY **NO** — confirmed. T1–T4 ABSENT, T5/T7 CLOSED-LOCAL, T6 HOLD.
4. Maps separate; no residual_slash invented; RG47f-bis HOLD — confirmed.
5. **S-B-1: stays OPEN.** B and sgn(0) ingested; M resolved via W-PO-1 Gram cite (part of N-SB1-1 cured). Truncation degree not written by author (N=40 is local choice) → N-SB1-1 remains (trunc degree; B(c,v) map adequacy to be confirmed by author if required). Not closed.

## t604u note
FINDINGS_2026-10-24_t604u_confirmed.md exists → ledger 7dbd63af… confirmed (parallel audit); no soft-hold needed.

## Open after audit
W-NL-1/2, W-PO-2 (+N-PIN-CONF-1, N-T604U-2), W-PO-3, W-PIN-3 watch, S-B-1 (+N-SB1-1 narrowed: trunc degree), **W-74-1** (RESULTS PASS vs accepted SKIP; await hashed addendum). W-PO-1 CLOSED. 0 blockers.
