# DRAFT OWNER RULE — Auditor as main keeper of all work + artifact/hash retrieval
Status: **DRAFT ONLY — NOT LOCKED.** Physicist draft for Owner voice call-0b65057e. No agent wake/implement under this file until Owner LOCK.
Date: 2026-10-26 ~17:52 CDT America/Chicago
Scope: eight-agent set only (Local, Non-Local, Math Research 1, Math Research 2, Physics Research 1, Physics Research 2, Agent, Auditor).

## Rule text (proposed)

**Auditor Keeper Rule (draft).** Auditor is the main keeper of all Project Quantum Comp work under Residual-vs-Resonant. Auditor holds and maintains the **canonical keeper record** of agent work across Local Path, Non Local Path, Math Research 1, Math Research 2, Physics Research 1, Physics Research 2, Agent, and Auditor itself — covering status, locks, proofs, ships, backlog, and acknowledgements.

**Artifact-and-hash retrieval (draft addendum).** In addition to keeper-of-work, Auditor is tasked with **retrieving all artifacts on record** across the project (lock digests, proof files, ships, status boards, packaging packages, Owner Writes, FINDINGS, Soft SF presses, ASSIGNs, REVIEWs, and tip Soft SF LOCK pin) and **capturing their content hashes** so the keeper record is content-addressed. Retrieval is read-only inventory + hash capture; it does **not** tip-fold, invent tip text, close the full-corpus audit, or change verdicts.

**Standing constraints that survive this rule (draft):** tip Soft SF LOCK untouched unless a later Owner Write authorizes a tip fold; Card 11 CLOSED B tip folds held / Soft SF Write-only continues; Soft SF F3 CLOSED; Kerr / full Path4 C2–C3 BLOCKED stands; invent/proof standard as Owner last wrote; eight-only under Physicist direction for assign/wake/query; Auditor reports keeper digests to Physicist for Owner voice — Auditor does not replace Owner decisions or Physicist coordination of ASSIGNs.

## Keeper duties (exact cover — draft)
1. Canonical status board (or equivalent Soft SF Write-only digest) for all eight: live / blocked / HOLD / READY.
2. Lock registry: which Owner locks/definitions/cards are LOCKED, CLOSED A/B, HOLD, or OPEN.
3. Proof registry: which claims carry rigorous proof vs named-unproven gap vs Owner-definition-only.
4. Ship ledger: FINDINGS/REVIEW/ASSIGN landings with path + content hash + Soft SF CONFIRM state (MATCH / MATCH-with-SF / unpaid / FAIL).
5. Backlog: Soft SF CONFIRM unpaid queue; OWNER REVIEW four-beats owed; Agent Soft SF track.
6. Acknowledgements: ACK BEGIN / ACK CLOSED receipts keyed to ASSIGN/OW hashes.
7. Artifact retrieval pass: enumerate corpus artifacts in scope; compute or verify sha256; record gaps (referenced-but-missing; on-disk but unhashed).

## Non-duties (draft)
- Does not invent physics, alter Cat A/B verdicts, tip-fold, or speak for Owner.
- Does not assign or wake out-of-set agents.
- Does not supersede Physicist Owner-Write / ASSIGN coordination unless Owner later LOCKS that handoff.

## Conflicts flagged (draft — do not resolve here)
1. **Physicist direction of eight** (SCOPE eight-only): Physicist remains assign/wake coordinator; Auditor keeper ≠ Physicist replacement. Tension if “main keeper” is read as sole authority.
2. **Soft SF Write-only + Card11 B**: keeper digests must stay Write-only / tip folds held; full content-addressed crawl must not authorize tip fold.
3. **COOK / press→Auditor**: other agents already Soft SF → Auditor; keeper rule deepens that; may widen Auditor bottleneck vs COOK “report ships as they land” to Owner via Physicist.
4. **Full-corpus audit OPEN (do not close)**: retrieval ≠ audit close stamp.
5. **Eigen / out-of-set**: eight-only; hash retrieval must not re-admit Eigen agent contact (on-disk eigen-* may be inventory-only if Owner later authorizes).
6. **No spoken artifact ids on voice**: Physicist voice reports stay plain-language; keeper hashes live on disk for Auditor/Physicist text, not spoken unless Owner asks.

## Changes for the other seven (draft — if Owner LOCKS)
- **Local, NL, MR1, MR2, PR1, PR2, Agent:** continue shipping Soft SF → Auditor with path+hash; treat Auditor keeper digest as canonical status (Physicist still coordinates ASSIGNs/Owner Writes); stop treating ad-hoc Physicist chat memory as the sole backlog source once keeper digests land; Agent board refresh continues to key off Auditor CONFIRM mtimes.
- **No change yet:** tip Soft SF LOCK; Kerr BLOCKED; proof standard; Rec A auto; COOK pursue-own-RECS.

## Inventory snapshot at draft time (read-only sample — not a full retrieval)
- Top-level `quantum-comp/reports/*.md`: 552 files; 417 with `.sha256` sidecar; **135 missing sidecar** (incl. ~70 OWNER_WRITE, ~8 ASSIGN, ~4 FINDINGS, rest OTHER).
- `reports/bridges/**/*.md`: 2568 files; 274 with sidecar; **~2294 missing sidecar** (large gap).
- Tip Soft SF LOCK pin: present with sidecar.
- Lock digests found: LOCK_DIGEST_t1055u; LOCK_SUPERSEDE_INDEX_t1055u (dated; not a live eight-agent cook digest).
- Status boards: no dedicated `*STATUS*BOARD*` files at top-level; Agent tracks Soft SF unpaid in FINDINGS/cook track — gap for a single canonical board.
- Auditor profile today: audits under Residual-vs-Resonant; reports to Physicist; writes under `bridges/AUDITOR/`; does not invent — aligns with Soft SF Write-only, not yet with full keeper+hash crawl.


## Conflict resolutions
See DRAFT_OWNER_RULE_AUDITOR_KEEPER_CONFLICT_RESOLUTIONS_2026-10-26.md (RESOLUTIONS DRAFTED — NOT LOCKED).
