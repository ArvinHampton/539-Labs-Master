# FINDINGS — PR2 post-LOCK re-tag (t1055u) — CONFIRM
Auditor · 2026-10-25 ~19:30 CDT (America/Chicago) · CONFIRM-only · invent-ban ON · residual-C LOCKED (read-only)

## Verdict: MATCH-with-SF

## Inputs (sha256 verified by Auditor)
- Catalog `/workspace/obs-data-PR2-COSMO-BIO-NEURO.md` = `51135ff617dc510019f3fb01c28fb03e17a4113f1f9f76142fd7a69ca9747992` (v0.5.5) — MATCH claimed.
- Backup `.pre-lock-retag-fec25921.md` = `fec259215f573c7911fae0f82ab1e67ae670ccce5c2171f165adb851399e7216` (v0.5.4) — MATCH name/changelog.
- residual-C tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` = `492fb3ac95c20e9117594639eb5947c90785a09e93da8301d6e83980c490a6fa` — MATCH (untouched).
- LOCK_DIGEST `964294cc…4d` — matches HASH_INTEGRITY line T1055U LOCK hashes; catalog cites full value.
- Pointer `PR_CATALOG_POST_LOCK_RETAG_POINTER_t1055u` = `a6836958…0d3b` MATCH; inventory `INVENTORY_POST_LOCK_OPEN_ITEMS_t1055u` = `d299708f…b277` MATCH; ledger tip `2bce6278…c455` present in inventory + ADOPTED_PATH_GUIDANCE.

## Diff vs backup (fec25921 → 51135ff6)
Changes only: header version line; §1 post-LOCK pointer bullet; C14 and §2.7 "OPEN" → "OPEN post-LOCK"; §7 "No LOCK / untouched" superseded by LOCK cite + 8-token re-tag list; trio ACK status suffixes; 61ω ledger cite updated to LOCK-era tip; §9 changelog. No numeric/measured value changed; no new physics content.

## Claims
| Claim | Result |
|---|---|
| LOCK 964294cc…/492fb3ac… | MATCH |
| 8 tokens re-tagged | MATCH (SF-1) |
| No promotions | MATCH — all remain OPEN/NEED WRITE/SUPERSEDED |
| C photon→torsion NEED WRITE | MATCH |
| rates / W4.6 mechanism OPEN | MATCH |
| Measured rows unchanged | MATCH (C14 values identical; only tag text) |
| invent-ban ON | MATCH — no new coefficients/rates/Ω ratios |
| Not Cat A | MATCH |
| residual-C not edited | MATCH (tip sha unchanged) |

## Soft flags (clerical only)
- SF-1: "8 tokens" count includes duplicates (#4≈#1, #5/#6≈#2) and #8 is a status-line supersede, not a model token — 4 distinct model items + 1 status line. Counting hygiene only.
- SF-2: 61ω ledger cite swapped `2c90bbe3…` → `2bce6278…` (LOCK-era tip) — legit per inventory, but a cite change beyond pure retag; noted for traceability.
- SF-3: Truncated hash cites (a6836958…, d299708f…, 964294cc…) in body; full values present elsewhere in file.

## residual-C untouched: YES
