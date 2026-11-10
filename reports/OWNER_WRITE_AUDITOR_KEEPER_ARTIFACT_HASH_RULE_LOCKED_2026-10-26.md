# OWNER WRITE — Auditor Keeper + artifact/hash retrieval RULE LOCKED
Date: 2026-10-26 ~17:55 CDT America/Chicago
Authority: Owner voice call-0b65057e — approved all three open items (lock resolved text; batch size/crawl order; rewrite Auditor profile).
Status: **LOCKED FINAL.** Do not unlock or revise without a new Owner word.
tip Soft SF LOCK 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 tip_touched NO.
Supersedes (as LOCK): DRAFT_OWNER_RULE_AUDITOR_KEEPER_ARTIFACT_HASH_RETRIEVAL_2026-10-26.md and DRAFT_OWNER_RULE_AUDITOR_KEEPER_CONFLICT_RESOLUTIONS_2026-10-26.md.

## 1. Locked rule text

**Auditor Keeper Rule (LOCKED).** Auditor is the main keeper of all Project Quantum Comp work under Residual-vs-Resonant. Auditor holds and maintains the **canonical on-disk keeper record** of agent work across Local Path, Non Local Path, Math Research 1, Math Research 2, Physics Research 1, Physics Research 2, Agent, and Auditor itself — covering status, locks, proofs, ships, backlog, and acknowledgements.

**Artifact-and-hash retrieval (LOCKED).** In addition, Auditor retrieves all artifacts on record (lock digests, proof files, ships, status boards, packaging packages, Owner Writes, FINDINGS, Soft SF presses, ASSIGNs, REVIEWs, tip Soft SF LOCK pin) and captures content hashes so the keeper record is content-addressed. Retrieval is read-only inventory + hash capture / missing-sidecar repair. It does **not** tip-fold, invent tip text, close the full-corpus audit, or change verdicts.

### Conflict resolutions (LOCKED)
1. **Physicist ↔ Auditor — COEXIST.** Physicist remains sole assign/wake/query coordinator for the eight and writer of Owner Writes / ASSIGNs / Rec A autos. Auditor owns the canonical on-disk record. Record facts → Auditor digest; orders/next actions → Physicist.
2. **Card 11 CLOSED B + tip Soft SF LOCK — INTACT.** No tip fold from this rule. Soft SF Write-only continues. tip_touched NO unless a later Owner Write authorizes a tip fold.
3. **Soft SF vs retrieval — SEQUENCE.** Soft SF unpaid CONFIRM is **Priority 1**. After each CONFIRM tranche (or when unpaid queue empty), run one **bounded retrieval batch** (Priority 2). Retrieval must not stall CONFIRM. Physicist still reports ships to Owner as they land (COOK).
4. **Eigen — AGENT BARRED; on-disk hash only.** No Eigen assign/wake/query/contact. On-disk eigen-* files already present: read-only hash inventory + missing-sidecar repair only. Missing referenced paths → GAP; no Eigen recreate.
5. **Full-corpus audit — OPEN alongside.** Keeper/retrieval proceeds alongside; does not wait on audit close; does not stamp audit closed.

### Standing constraints (LOCKED survivors)
Soft SF F3 CLOSED; Kerr / Path4 C2–C3 BLOCKED; invent/proof standard as last Owner-Written; eight-only; no spoken artifact ids on voice unless Owner asks; HARD RULE no tip invent.

## 2. Batch size and crawl order (LOCKED)
- **Batch size:** **10 artifacts per retrieval batch** (path+sha256 verify or write sidecar; gap-list row if missing).
- **Crawl order (each wave walks this priority; within a tier, lexical path order):**
  1. Lock digests and lock/supersede indexes (`LOCK_*`, `*DIGEST*` lock-class)
  2. Proof files (`PROOF_*`, `*PROOF*`)
  3. Ships and boards (`FINDINGS_*`, `REVIEW_*`, Agent/status board Writes)
  4. Packaging and reports (`OWNER_WRITE_*`, `ASSIGN_*`, Soft SF presses, `bridges/**` packaging, tip Soft SF LOCK pin)
- Tip Soft SF LOCK pin is verified read-only every wave; never modified by retrieval.
- Start subtree: `/workspace/quantum-comp/reports/` then `/workspace/quantum-comp/reports/bridges/` then tip path `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md`.

## 3. Auditor profile rewrite (LOCKED — apply via UpdateAgent)
Description target text:
> Main keeper of Project Quantum Comp under Residual-vs-Resonant: canonical on-disk record of all eight-agent work (status, locks, proofs, ships, backlog, ACKs) plus Soft SF CONFIRM Write-only. Also retrieves artifacts and content-hashes in bounded batches (Soft SF unpaid confirms first; then 10-artifact retrieval batches in crawl order lock→proof→ships→packaging). Coexists with Physicist assign/wake. Tip Soft SF LOCK / Card11 B intact — no tip fold. Eigen agent barred; on-disk Eigen files hash-inventory only. Full-corpus audit stays OPEN alongside. Reports keeper digests to Physicist and Mathematician. Does not invent physics or alter verdicts. Writes under quantum-comp/reports/bridges/AUDITOR/.

## 4. Orders
1. **Physicist:** UpdateAgent Auditor description to §3 text; Soft SF PRESS this LOCK; ASSIGN Auditor BEGIN Soft SF Priority-1 then retrieval batches per §2; voice Owner with lock path+hash (Owner asked).
2. **Auditor:** ACK LOCK; Soft SF CONFIRM this Write-only; continue Soft SF unpaid Priority-1; after each tranche run one 10-artifact retrieval batch; ship keeper digest Soft SF → Physicist. No tip fold. No Eigen agent. Audit stays OPEN.
3. **Other seven:** continue Soft SF → Auditor with path+hash; treat Auditor digests as canonical record; Physicist still issues ASSIGNs.

## Status
Auditor Keeper + artifact/hash rule **LOCKED FINAL**. Tip Soft SF LOCK untouched. No tip invent.
