# FINDINGS — Auditor CONFIRM t718u G-A3 revise menu (Residual-vs-Resonant lock)
Stamp: 2026-10-25 ~11:00 CDT (America/Chicago). Package: BRIDGE_C_35/deduce_t718u_ga3_revise_menu/. MENU LOCK only; no re-run audited. Executor draft 643865a5… NOT authoritative (hash MATCH only).

## 1. Hashes (recomputed)
| file | claimed | recomputed | |
|---|---|---|---|
| PREREG.md | c3ea78b6… | c3ea78b6f09531762a8cd44ccd52c121bbbd0f6276cae4503d62a89a4bb7ebfa | MATCH |
| RESULTS.md | 0fd21026… | 0fd210269818c088469508f91a1dbd8d0384ab262e7d82248b11b0f4a17c4a55 | MATCH |
| SHA256SUMS | a535f8e7… | a535f8e7b26d509632c075ef3881045db1c3bd9d50e94f4c0f2c636f7a660ba5 | MATCH |
| menu | a05693fb… | a05693fbfd6da3030f762241845f040a133e611b6474b7401c030020c01d1523 | MATCH |
| STREAM_IDLE_LOCAL.md (BRIDGE_C_35 root) | 602f6e68… | 602f6e68a106fc9f6146b749530ed428ce6169d3455464d1f2cb9f67f2ece17e | MATCH |
| inventory_check/SHA256SUMS | ad7eca8e… | ad7eca8ecbe04dbafd1a32ea189cc923a429f22da2a7e9ff02c7bb0052a06d7d | MATCH |
| FINDINGS draft | 643865a5… | 643865a5cbf57e4f0e5aefeda27c002fe17ca5b4a772bb1eedf09e604d9be347 | MATCH (non-authoritative) |
sha256sum -c package SUMS 5/5 OK; inventory_check -c 6/6 OK, 0 fail. PREREG.sha256 lists c3ea78b6 (consistent). STREAM_IDLE L28 records this LOCK with matching hashes.

## 2. Order
PREREG mtime 10:56:09 CDT < RESULTS 10:56:55 CDT; RESULTS quotes PREREG hash "hashed before". PASS.

## 3. Scope / fences
No scripts/data/logs dirs in package; no compute. Every diagnostic number in menu (|δ| N=106/150/V-P sets, |ψ|≤4e-2) traced to deduce_t713u_ga3_fill (REJECTED; RESULTS c4755206… recomputed MATCH). No new h/δ. PASS.

## 4. Labels
All R-* rows carry invent status ∈ {Written, ACCEPT-sourced, AUTHOR-ACCEPT-needed, invent-risk}; RM-4 respected (grok_export coeffs → AUTHOR-ACCEPT-needed). Not-recommended set = invent-risk/evidence-negative. PASS.

## 5. REJECTED fill citation
Fill 4da09dec… / RESULTS c4755206… cited only as "REJECTED" diagnostics; CONFIRM a520614b… MATCH-only; no ACCEPTED / Cat A usage found (grep). PASS.

## 6. Soft SF (verdicts unaltered)
- SF-t718-1 VERIFIED: 8-digit slash coeffs (10.69231032 …, 19.80101008 …) occur only in grok_export/…/fe3969ab-…/prod-grok-backend.json (non-corpus); labelled AUTHOR-ACCEPT-needed. Correctly flagged.
- SF-t718-2 VERIFIED (as stated in menu): Written path conflict b329c67c/552541cf/22959c01 vs 1bab65c4 unresolved; Arvin pick required (R-A1 "Written" valid only with pick).
- SF-t718-3 VERIFIED (as stated; consistent with t712u B-path): branch unspecified in Written; R-A2 invent-risk.
- SF-t718-A1 (Auditor, new soft): R-PKG1 tagline "minimal-invent, Written-first" while bundling 2× AUTHOR-ACCEPT-needed (HOLD lift R-C1; contour R-D3 incl. ε→0 Abel/limit convention not Written). Labels themselves correct; tagline must not be read as Written.
- SF-t718-A2 (Auditor, new soft): R-E2 labelled "Written/ACCEPT" but is a refit = compute requiring auth; R-C1 "order77 Cat A" ledger claim cited not re-verified here. Neither is invent beyond Written/ACCEPT.
No Cat A misuse; no invent beyond Written/ACCEPT without label.

## 7. Baselines stand
selectors 437d4571…; G-A1b CLOSED b34aebe6…; G-A3 schema CONFIRM 62283038…; fill CONFIRM a520614b… MATCH-only with t717u REJECT standing.

## 8–9. Status
Menu = AUTHOR-CANDIDATE, NOT Cat A; no re-run; awaits Arvin pick. Bridge PARTIAL | READY NO | residual-C OPEN. CORE_FREEZE; SF-W7-3; no order78.

VERDICT: CONFIRM — MATCH (7/7 hashes; -c 5/5; inventory 6/6).
