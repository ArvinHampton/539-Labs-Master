# FINDINGS — Auditor CONFIRM t761u outer_* ACCEPT (O-α, outer_* defs/schema only) — 2026-10-25 CDT (America/Chicago)
Package: BRIDGE_C_35/deduce_t761u_outer_accept/  Lock: Residual-vs-Resonant; CORE_FREEZE; SF-W7-3. PASS/FAIL unaltered. Package NOT edited.
Supersedes for the ACCEPT LOCK: prior outer_written CONFIRM 46e4e3bdd29286140ec2222c506479d1dbc1f56ac2ac1922618d7c1ad250c020 (remains valid as Written-stage baseline).

## Verdict: MATCH — CONFIRM. Soft SF: NONE.

## 1. Hashes (recomputed)
- FINDINGS draft 6f1c16624a192b8185973e419eae8af1a2258d3caa8e7b4e3ab325ce21ad8f35 MATCH
- PREREG 4cf8cc18beec7a057f33fa8da47fc4ec86deaccb95927fa6bfa41f374a62b286 MATCH (= logs/PREREG.sha256; = draft; = RESULTS cite; = STREAM LOCK)
- RESULTS 467b6af23f908dc375d7b3ddef917e228abb6f844b2e719370dee898625218ab MATCH (= STREAM LOCK)
- SHA256SUMS 0f7271f5d2741d69f281f70ae7e1c7f413c006ebae6654c5fa85396b15d79979 MATCH (= STREAM LOCK); `sha256sum -c` 7/7 OK
- scope quote (author_candidates/O_ALPHA_ACCEPT_SCOPE_QUOTE_t761u.md) 7eef4763d20c266aeb9c5494e71d7388caf3622e1100963bfe8e05c3499965f9 MATCH
- INVENTORY 5161e63cc666e6a9342d0ac89670ddb0ddb7c7ddfe13a364a4a93da738cc5973; logs/PREREG.sha256 25d4028996344c6f8fc4a52d3c51e2e648ba0afbebad8c1c004613e4bec4087e; verify_basis 8f9b0af555ece04dbca0398089ca6e6ec1dcc7597f5ca9d5647bbb4c13141725; sums_check 60c4639ef426dc8adc0ea946d4e1444dc852a9198a78691cc00914b0f654da07 (excluded from SUMS per INVENTORY)
- Auditor independent live re-check of all 17 basis shas in verify_basis (AW-α CONFIRM aac04151…, menu 39c9a9a6…, outer RESULTS 910d8e31… / PREREG bdb2a87c… / SUMS 613a1f01… / draft 2743ba15…, AW-α PREREG a0dcc096… / RESULTS 3aae6f19… / scope 6880b1cd… / SUMS c9a2213f…, MASTER 544de792…, B3-α b96ff7bd…, T-α 5f5f2832…, HD e60cad9b… / 1bab65c4…, ledger 7dbd63af…, X4 ABSENT 2bb870b4…): 17/17 OK. outer_written SUMS -c 9/9 OK rc=0; t761u_accept SUMS -c 7/7 OK rc=0. Prior outer_written CONFIRM file live = 46e4e3bd… OK.

## 2. Ordering
PREREG mtime 12:40:17 CDT < RESULTS 12:40:56 CDT; RESULTS cites full PREREG sha. OK.

## 3–5. Claims / Soft SF
- outer_* defs/schema CLOSED under O-α as ACCEPT-sourced Cat A AUTHOR-ACCEPT Written, outer_* only: O-1a m=0 incl (outer_even(0)=0); O-2a ledger form only, NO ledger≡HD; O-3a schema-only EMPTY table; O-4a unit coeff — VERIFIED. Scope-quote INGESTED lines match PREREG "Scope (verbatim ACCEPT)" verbatim in content (only backtick formatting on O-3a schema string differs) and the menu 39c9a9a6… lines.
- Formulas in RESULTS M2 (outer_even=35m²+7m; outer_odd=35m²+42m+49/4) are quoted from menu 39c9a9a6… (HD e60cad9b… L16–22), not new; m=0 extension is the accepted O-1a choice. No table cells; no Ξ Fourier coeffs.
- NOT O-β/γ/δ; NOT O-X4 (G-2 unresolved) — stated in PREREG/RESULTS/scope/LOCK. OK.
- Soft SF scan: ledger≡HD explicitly NOT Cat A; Cat A strictly outer_* defs/schema; no invented cells/coeffs; G-A3 stays PAUSED (no auto-reopen); 4da09dec… not revived. Soft SF: none.
- F-A PASS; F-B CLOSED; F-C NO; F-D OPEN (residual-C); F-E NO — consistent with pre-stated criteria.
- M5: STREAM LOCK present in BRIDGE_C_35/STREAM_IDLE_LOCAL.md L44 (after outer_written LOCK L43). Note: an outer_written LOCK (L43) is now also present, resolving the prior hygiene note in 46e4e3bd…. No hygiene issue.
- Brief note: the task's claims list contained a garbled/duplicated Soft-SF line; audited against the complete version.

## 6. Posture
outer_* CLOSED Cat A under O-α (defs/schema only, table EMPTY); O-X4/ledger≡HD NOT Cat A; AW-α + B3-α KEEP + T-α KEEP stand; Bridge PARTIAL; READY NO; residual-C OPEN; X4 ABSENT (2bb870b4…); G-A3 PAUSED; R-C1 stands; CORE_FREEZE SF-W7-3; no order78.
