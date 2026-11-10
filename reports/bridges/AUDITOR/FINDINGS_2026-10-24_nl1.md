# FINDINGS 2026-10-24 — NL1_OMEGA_FTOTAL_20261024 (Auditor, ~22:57 CDT America/Chicago)
Read-only. No PASS/FAIL altered. No physics added.

## Hashes (live)
- PREREG.md 495c79449e5afde897b63ada51a5f83225584dee30afa0133781a3b0e15de52e — MATCH; PREREG.sha256 also pins run.py c64428d3… — 2/2 OK
- result.log 85bd2f63fd8eddc369a5f084898caf24312f9dc468f966fc99437f378950dabb — MATCH; RESULTS.sha256 content = this
- RESULTS.sha256 file 57028d0d4236bc7aba33d9e461be3bedf03d51832286d3cd0f197e547575712a — MATCH
- inventory_check/SHA256SUMS `-c` → 7/7 OK (incl. NL1 result.log, NL1_OPEN_SUPERSEDED_BY_T591U.md f8ec1dbd…); pins cited as comments only.
- STREAM_IDLE_WRITTEN.md 8dd745b4514f8d0b43890f4b3e50ee16037ecaed084916297746f42a42214dd8 (root = inventory_check copy; 22:56). Not in SUMS — note N-NL1-3.

## Checks
- PREREG↔result.log — PASS. run.py implements P1–P3, C1–C3 (C2 split a/b/c) as preregistered; log: P1–P3 HOLD, 5 controls FAIL, RESULT PASS. Rule satisfied.
- Forms vs pins — PASS. Ω₁₁D and F_total in PREREG/run.py match pin a6dfcec4… lines 17/22 (5 components, args k,K,b,Φ, "warped and flux channels feed Ω").
- Invent-ban — PASS. f_* , Ω₀ symbolic only; no numerics; Z-table ABSENT acknowledged.
- Cat tagging — PASS. Cat B continuum; explicitly not relabelled paper Cat A.
- Maps separate — PASS. Local P̂_orth/Ξ/G1 excluded; G1 REJECT stands; Map-C6 CLOSED.
- Supersession note — PASS. Additive; hashed FINDINGS_MAP_C6 (35ae4b64…) and MAP_C6 (c58bea17…) untouched, still OK.
- W-PO-2 INHERITED (structural PASS tests shape only; placeholder factors remain unsolved; N-PIN-CONF-1). W-PO-3 INHERITED (provenance "t591u — chat"). Neither resolved. W-PO-1 local-only, not touched.
- Note N-NL1-1: structural PASS is tautology-adjacent (locked form compared to itself; controls are hand-built mismatches). Valid as a prereg'd lock check; carries no empirical weight. Flag only.
- Note N-NL1-2: all files mtime 22:53 while PREREG header says ~22:54; hash-before-run asserted, not provable from mtimes.
- Note N-NL1-3: STREAM_IDLE_WRITTEN (8dd745b4…) unhashed in SUMS; posture consistent (NL1 structural ACCEPT, W-PO-2/3 apply).

## Disposition
0 blockers. HOLD from prior pass lifted (NL1 PREREG now present and audited). Open: W-NL-1, W-NL-2, W-PO-1 (held), W-PO-2 (+N-PIN-CONF-1), W-PO-3; watch W-PIN-3.
