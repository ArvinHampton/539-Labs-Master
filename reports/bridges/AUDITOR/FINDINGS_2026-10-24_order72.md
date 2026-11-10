# FINDINGS 2026-10-24 — BRIDGE_C_35 order72 LOCKED (Auditor, ~22:57 CDT America/Chicago)
Read-only. No PASS/FAIL altered. No physics added.

## Hashes (live re-check)
- PREREG.md 331fc6d2dfae8d4937819099c86e5c9cbf1c382fb102425174e08de728a3f6ea — MATCH (PREREG.sha256 OK)
- RESULTS.md 2cc5b814324d847ebc498bedc61f9f15952b0c67812142b3e9a59bd4aaa19708 — MATCH
- Sources a6dfcec4… / 6de428d8… / ffc93ae4… / confirmed b10193b4… / ADDENDUM_CONFIRMED_LEDGER a7dd0812… — all OK
- data/P_orth_excerpt_verbatim.md d0cac6eb… OK; RESULTS_ADDENDUM_WPO1.md 263e547c… OK
- order72/SHA256SUMS `sha256sum -c` → **10/10 OK** (coordinator said 9: WPO1 addendum added ~22:55).
- **N-72-1 (cite drift, not a blocker):** STREAM_IDLE_LOCAL is now **f6557a4fc1c9a59e82522dd900814190b7e3b19d0e31e43ab89a64bd1d3e39d5** (root + order72/data/ identical; in SUMS). Coordinator cite a1a85b81… is the prior snapshot, explicitly "superseded for posture only" in the new file (W-PO-1 bind rewrite, 22:55). Coordinator should update its cite.
- G1 GATE order57/GATE_DECISIONS.md 640da80d… OK.

## Claims
1. Bridge PARTIAL — PASS. RESULTS: T5 FOUND/CLOSED-LOCAL; T1–T4 ABSENT; residual law for C OPEN; READY NO. Consistent with prereg rule (c).
2. G1 REJECT stands — PASS. RESULTS (d), both addenda, STREAM agree; confirmed ledger "still frozen" ≠ PASS; no numeric Ξ adopted.
3. Maps separate — PASS. Ω₁₁D/F_total Cat B nonlocal, not ingested (e); Map-C6 CLOSED-LOCAL not reopened.
4. Invent-ban / P̂_orth — PASS. Excerpt matches pin a6dfcec4… form verbatim; s, H_s, coefficients explicitly not supplied; C not treated numerically.
5. W-PO: **W-PO-1 INHERITED, OPEN** (bound by RESULTS_ADDENDUM_WPO1; +7k/2 vs −7k/2; H_s undefined) — held open pending Arvin. **W-PO-2 INHERITED** (local lane out of scope; N-PIN-CONF-1 per FINDINGS_2026-10-24_pin_confirmed.md b1dcfab0…). **W-PO-3 INHERITED** (confirmed ledger: Drive/attach copy not found; chat lock stands). None resolved by order72.
6. Parents/READY/STREAM — PASS. PREREG cites order71 PREREG 56b61ee5… / RESULTS 4c4848c0… / STREAM 3998a735… / W-PIN-1 addendum 5571b7bf…; RESULTS cites PREREG 331fc6d2…. READY NO. STREAM posture consistent (T5 closed, W-PO-1 binds, G1 REJECT, watch for order73).
- Note N-72-2: PREREG/RESULTS mtimes both 22:53 (same minute); hash-before-results order asserted, not provable from mtimes. Note only.

## Regression check
W-PIN-1, W-PIN-2 remain CLOSED (474f25a9… unchanged). order71 OK unchanged.

## Disposition
0 blockers. Notes N-72-1, N-72-2. Open: W-NL-1, W-NL-2, W-PO-1 (held), W-PO-2 (+N-PIN-CONF-1), W-PO-3; watch W-PIN-3.
