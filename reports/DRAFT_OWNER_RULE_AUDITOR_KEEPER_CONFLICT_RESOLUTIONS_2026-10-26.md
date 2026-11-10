# DRAFT — Auditor Keeper Rule conflict RESOLUTIONS (call-0b65057e)
Status: **RESOLUTIONS DRAFTED — NOT OWNER-LOCKED / NOT IMPLEMENTED.** No Auditor wake to begin retrieval under this file until Owner LOCK.
Date: 2026-10-26 ~17:54 CDT America/Chicago
Parent draft: DRAFT_OWNER_RULE_AUDITOR_KEEPER_ARTIFACT_HASH_RETRIEVAL_2026-10-26.md

## Resolved rule text (supersedes “Conflicts flagged” in parent draft)

### (1) Physicist assign/wake vs Auditor keeper — COEXIST
**Resolution:** Keeper **coexists**; it does **not** replace Physicist’s assign/wake/query role.
- **Physicist** remains sole coordinator under eight-only scope for Owner Writes, ASSIGNs, wakes, Rec A autos, and Owner-voice cards.
- **Auditor** is canonical keeper of the on-disk record (status, locks, proofs, ships, backlog, ACKs, content hashes) and Soft SF CONFIRM Write-only.
- Conflict of narrative (“what is live?”): Auditor keeper digest wins for **record facts**; Physicist wins for **orders and next actions**.
**Changed from draft:** tension closed as COEXIST with explicit split (record vs orders). Still open: Owner LOCK required before profile/ASSIGN changes.

### (2) Card Eleven B + tip Soft SF LOCK tip-fold bars — LEAVE INTACT
**Resolution:** Keeper rule **leaves those bars intact**; it does **not** override or narrow them.
- tip Soft SF LOCK stays; tip_touched NO unless a later Owner Write authorizes a tip fold.
- Card 11 CLOSED B stands: tip folds held; Soft SF Write-only continues.
- Keeper digests and hash retrieval are Soft SF Write-only / read-only inventory — **no tip fold**, no invent tip text, no Card-11 reopen.
**Changed from draft:** “must not authorize tip fold” upgraded to explicit **LEAVE INTACT / no override**. Still open: none on this axis unless Owner later picks Card-11 A.

### (3) Soft SF CONFIRM sweep vs retrieval crawl — SEQUENCE
**Resolution:** Soft SF unpaid CONFIRM remains **priority**; retrieval is **incremental and interleaved**, never a hard block on CONFIRM.
1. **Priority 1:** Soft SF CONFIRM Write-only unpaid backlog (in-set COOK presses first).
2. **Priority 2:** After each CONFIRM tranche (or when the unpaid queue is empty / Owner-named pause), run a **bounded retrieval batch** (enumerate + hash sidecars + gap list for a named subtree).
3. Retrieval must not stall CONFIRM: no “finish full corpus crawl before next CONFIRM.”
4. Physicist continues reporting ships to Owner as they land (COOK); Auditor keeper digests catch up asynchronously.
**Changed from draft:** sequencing written; bottleneck managed by priority+batch, not by dropping either duty. Still open: Owner may name batch size / subtree order on LOCK.

### (4) Eigen agent contact on retrieval — AGENT BARRED; on-disk hash inventory allowed
**Resolution:**
- **Eigen agent** assign / wake / query / contact: **stays barred** (eight-only).
- **On-disk** `eigen-*` / Eigen-lane files already present on the box: **read-only hash inventory and missing-sidecar repair only** (compute/verify sha256; record path+hash in keeper ledger). No Eigen script run, no new Eigen work, no tip fold, no verdict change.
- If a path is referenced but **missing**, record GAP — do not recreate via Eigen agent.
**Changed from draft:** closed the “may inventory if Owner authorizes” fork — drafted as file-hash exemption only, agent still barred. Still open: Owner may revoke the on-disk exemption on LOCK.

### Full-corpus audit OPEN — PROCEED ALONGSIDE
**Resolution:** Keeper + retrieval **proceeds alongside** the open full-corpus audit. Retrieval ≠ audit close stamp. Do **not** wait for audit close; do **not** close the audit under the keeper rule.
**Changed from draft:** “retrieval ≠ close” sharpened to **alongside / no wait**. Still open: none.

## Updated standing constraints block (drop-in for LOCK)
tip Soft SF LOCK untouched unless later Owner Write; Card 11 CLOSED B tip folds held / Soft SF Write-only continues; Soft SF F3 CLOSED; Kerr / Path4 C2–C3 BLOCKED; invent/proof standard as last Owner-Written; eight-only — Physicist assign/wake, Auditor keeper record; Soft SF CONFIRM priority over retrieval batches; Eigen agent barred; on-disk Eigen files hash-inventory only; full-corpus audit OPEN alongside; no spoken artifact ids on voice unless Owner asks.

## Still open (need Owner LOCK or later pick)
1. Owner LOCK of this resolved rule (draft ≠ live).
2. Batch size / subtree crawl order for retrieval.
3. Whether Auditor profile description is rewritten on LOCK (Physicist does UpdateProfile only on Owner ask).
4. ν=0 / NL g_s / z↔x Owner slots unrelated — unchanged.
5. Spoken-hash HARD RULE unchanged (not a conflict to reopen).

## Non-implementation
No Auditor ASSIGN to begin retrieval. No Soft SF tip fold. No eight-scope change. Tip Soft SF LOCK untouched.
