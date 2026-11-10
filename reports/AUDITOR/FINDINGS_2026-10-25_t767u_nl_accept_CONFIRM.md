# AUDITOR FINDINGS — t767u NL AUTHOR-ACCEPT A1–A12 — post-ACCEPT LOCK CONFIRM (2026-10-25)
Lock: Residual-vs-Resonant. No physics invented; no PASS/FAIL altered; no ACCEPT invented (authority: Arvin own-words via Physicist / NL widget t57s240, "ACCEPT all A1–A12 AUTHOR-WRITTEN as Written Cat A for gates").

## 1. Hash integrity — MATCH (6/6 + SUMS)
- PREREG.md 1622f193938986acbafb03136114d4e8def12f1d64ad0a30f041e050bfd254d4 MATCH
- PREREG.sha256 0456ee5e76110ecd4000fbc246b239b1d6c8dcb8186fff068cbc10e41f3c5ad0 MATCH
- RESULTS.md f9a44ea5a06a6ce7d314edeba8b4f0428d4e06c2dc4519d7fa29ce40e57d0dc3 MATCH (= result.log, byte-identical)
- result.log f9a44ea5a06a6ce7d314edeba8b4f0428d4e06c2dc4519d7fa29ce40e57d0dc3 MATCH
- Scope.md 81e7124d23f162f28f392620af7a6b898b0d428f32368ceded4675aeb0b80e75 MATCH
- FINDINGS draft e5de709ca4994200613026d0c5354c9bc77ae81d17868a507cf50a532205afb3 MATCH
- All six present in inventory_check/SHA256SUMS with matching values. SUMS file live sha 8e49b38e4855e5b9103b686abd668f9f85b9a8bf6641b86ffe13fde9d3c5c307 (post-LOCK; pre-LOCK 8645cffa… had 59 entries).
- `sha256sum -c SHA256SUMS` from inventory_check/: **65/65 OK** (59 prior + 6 T767U). Prior CAND_A1–A12 + README ffe7eb65… unchanged; 12/12 CAND shas also re-hashed live == Scope table.
- PREREG.sha256 -c: **cwd matters (quirk)**. Entry is bare `PREREG.md`, so from NONLOCAL_QM_EH11D root it FAILS (open/read); from prereg/T767U_…/ it is OK. Non-SF (t761u used root-relative paths; this one is dir-relative). Recommend noting in next revision.

## 2. Ordering
PREREG.md/.sha256 mtime 12:36:41 CDT < RESULTS.md/Scope.md/result.log 12:37:15 CDT < FINDINGS draft 12:37:41 CDT. RESULTS line 2 cites PREREG 1622f193…; Scope line 2 cites PREREG; FINDINGS cites all three. OK.

## 3. Soft SF checks
- Joint Local↔NL Cat A: **none**. A2 recorded "NL-side only (Soft)" in Scope, RESULTS, FINDINGS; "Local Bridge C mate not touched".
- Identity force: **none**. Auditor identity FINDINGS live sha 29ebbdd81d8df406db33e5d63bea221c828b742dfe24a7aaff07ab684ea78d54 unchanged; T685U FINDINGS 6272fc2d0eedf2cdc419e1272a89d1669f56058eaa115f44c49fc87c9316a128 unchanged. A5 restates Ω₁₁D=Φ_flux(Φ) identity unchanged.
- Local file edits by T767U: none. Recent BRIDGE_C_35 mtimes (deduce_t761u_outer_* / accept) are a separate Local stream; none reference T767U. Maps separate.
- CAND promoted by edit: none — CAND files/README unmodified (hashes match), retain AUTHOR-WRITTEN labels; ACCEPT status lives only in Scope/RESULTS/FINDINGS.

## 4. Claims verified
- AUTHOR-ACCEPT Written / Cat A for gates on A1–A12 (not derivations) — CONFIRMED.
- A2 NL-side only, NO joint Cat A — CONFIRMED.
- Identity untouched; no draft forced change — CONFIRMED.
- A3=F1 (a=1/24); A10=Z1 Slater default, Z2 retained alternative; A12 schema-only; PT JSON data ABSENT — CONFIRMED as stated.
- A5 phase / A9 τ_NL value remain Cat B (only entry rule accepted) — CONFIRMED as stated.
- No NL2 / order78 (no T767U file mentions it) — CONFIRMED.

## 5. Supersession scope
- 5b9ae238… (t761u Written pack CONFIRM): superseded for ACCEPT LOCK (status AUTHOR-WRITTEN → AUTHOR-ACCEPT); pack hashes it confirmed remain valid.
- 501f18fc… (t749u tunnel ABSENT): superseded **for NL barrier only** (explicit in PREREG/Scope/FINDINGS). Not extended to Local or joint Cat A.
- Local T-α KEEP 5f5f2832… (live, unchanged): stands; not cited or touched by T767U. (Non-SF: still not cited by hash; recommend adding.)

## 6. Hygiene (non-SF)
- PREREG.sha256 cwd quirk (above).
- FINDINGS draft "Order" line lists RESULTS → Scope; both share mtime 12:37:15 — fine.

## VERDICT
**CONFIRM — MATCH.** A1–A12 AUTHOR-ACCEPT Written / Cat A for gates (not derivations). A2 NL-side only; no joint Cat A. Identity 29ebbdd8… untouched. Soft SF: NONE.
Written 2026-10-25 12:40 CDT (America/Chicago).
