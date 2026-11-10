# FINDINGS — t1086u FINDINGS-MERGED post-LOCK stamp CONFIRM (Auditor)
Date: 2026-10-25 ~19:50 CDT (America/Chicago) · CONFIRM-only · invent-ban ON

## Verdict: MATCH (stamp-only)

1. Input: `/workspace/grok-batches/FINDINGS-MERGED.md` sha256 = `45bbe2ab08836aecdf105314e7b210d4b4505316a5391d6c382045350f1a13a6` — MATCH claimed tip; sidecar `.sha256` agrees.
2. Prior tip recovery: no backup/.pre-*/git found. Recovered byte-exact by prefix: the file's bytes before §7 (through line 105, excluding its trailing newline) hash to `cb2cbcefc555937382cdea16526a6f98f11be19d6f40ed3506cff1e23abc67e5` = prior tip cb2cbcef… (also logged in HASH_INTEGRITY 16:23 CDT entry). ⇒ §§1–6 byte-identical; change is pure append (`\n\n---\n\n## 7. Post-LOCK stamp …`, lines 106–120).
3. §7 content: states "No rewrite of §§1–6"; cites residual-C tip 492fb3ac… / LOCK_DIGEST 964294cc… (full values correct); Q3 marked superseded-for-live-status by LOCK, chat claims historical; no new physics; no PASS/FAIL altered.
4. residual-C `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` sha256 = `492fb3ac95c20e9117594639eb5947c90785a09e93da8301d6e83980c490a6fa` — untouched (not edited by Auditor).

## Soft flags
None. (Note only: FINDINGS-MERGED-SUMMARY.txt mtime 19:45 also — not in scope, not scored.)
