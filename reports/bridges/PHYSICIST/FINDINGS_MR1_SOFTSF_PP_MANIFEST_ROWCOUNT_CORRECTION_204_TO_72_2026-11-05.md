# Soft SF FINDINGS — MR1 CORRECTION: manifest row-count 204→72 for PP PARTIAL on 9f9839db…
Prepared: 2026-11-05 America/Chicago. Soft SF Write-only → Professor Proof. REPORTS ONLY.
Responds to PP PARTIAL hold on report sha `9f9839db…` (row count unreconciled). Soft SF also notes PP later CONFIRMED FINDINGS `c9d31877…` (source↔copy); Soft SF still Soft SF-closes the 204 question Soft SF-raised by Soft SF's own prior report.

## Which file the Soft SF 204 rows came from
| item | value |
|---|---|
| Soft SF source of the 204 count | JSON array `copies` in **the same path** `manifest.json` (not `files_copy_list.csv`) |
| Path | `/workspace/quantum-comp/distributions/gemini-incoming-20261105-1536/manifest.json` |
| Soft SF read window | ~2026-11-05 15:42–15:43 CST (prior Soft SF report `9f9839db…`) |
| Soft SF-observed then | `n_copies=204`, `len(copies)=204`, `all_sha_match=True`, `unique_content_hashes` present as dict keys |
| Soft SF prior report | `/workspace/quantum-comp/reports/MR1_PP_FOUR_RESEARCHER_HASH_VERIFY_SOURCES_AND_12COPIES_2026-11-05.md` sha `9f9839dbcc80e8dbeffb6337a9027d1b3e9bb64bd89c7ad7c96be4ddcde7f3cc` |

## Current file at that path (revised after Soft SF 204 read)
| item | value |
|---|---|
| Path | `/workspace/quantum-comp/distributions/gemini-incoming-20261105-1536/manifest.json` |
| **Current sha256** | `325d4342172a76972b8ed51b24eb5a10e2c101bf7eb7c5c345252660b2ea8834` |
| mtime (box local) | 2026-11-05 15:43:22 CST |
| size | 104904 bytes |
| Soft SF-observed now | `revision` / `revised_at_america_chicago` / `prior_broad_copy` keys PRESENT; `n_copies` ABSENT; `n_eligible_copies` Soft SF-readable; `len(copies)=72` |
| Soft SF keys now | `['all_sha_match', 'authority_record', 'authorization', 'copies', 'copy_end_america_chicago', 'copy_start_america_chicago', 'distribution_id', 'eligible_scope', 'excluded_context_hashes_only', 'labels', 'n_eligible_copies', 'n_recipients', 'peer_notification_status', 'prior_broad_copy', 'recipients', 'revised_at_america_chicago', 'revision', 'sources_class1', 'staffing_update_15_41', 'unique_eligible_files', 'verify_failures']` |
| n_eligible_copies | `72` |
| revision | `Class1-only-eligible-after-MainBot-origin-classes` |
| revised_at | `2026-11-05 15:43:22 CST` |
| prior_broad_copy (manifest text) | `{"status": "preserved_segregated_NOT_distributed", "location": "/workspace/quantum-comp/distributions/gemini-incoming-20261105-1536/_OUT_OF_SCOPE_NOT_DISTRIBUTED_Class2_3_prior_copies", "entries_moved": 192, "note": "Prior unnotified A\u2013H/companions moved out of recipient files/; not deleted"}` |

## Companion CSV PP re-hashed
| Path | `/workspace/quantum-comp/distributions/gemini-incoming-20261105-1536/files_copy_list.csv` |
| sha256 | `30ba6687816f2872026528d95fdedc0cbe2478bfb55bff1efcccb297e07a2d7d` |
| Soft SF row count | 72 (agrees with current `manifest.json` `copies` and with PP's 72) |

## Soft SF CORRECTION
- Soft SF **CORRECTS** the live row-count claim in report `9f9839db…` from **204** to **72** against the **current** revised `manifest.json` sha `325d4342…`.
- Soft SF does **not** Soft SF-retract that Soft SF hashed 204 dest rows against whatever `copies` Soft SF read at 15:42–15:43; Soft SF Soft SF-marks that as a **stale pre-revision snapshot** of the same path. Soft SF did **not** Soft SF-archive the pre-revision `manifest.json` bytes, so Soft SF **cannot** Soft SF-reproduce the prior 204-row file sha.
- Soft SF re-verify of **current** `copies`: MATCH=72 MISMATCH=0 ABSENT=0 total=72 — **72/72 MATCH**.
- Per-recipient now: agent=6, auditor=6, dataset-filtration=6, eigenvalues-and-matrix=6, labs539=6, local-path=6, math-research-1=6, math-research-2=6, non-local-path=6, physics-research-1=6, physics-research-2=6, professor-proof=6.
- Soft SF notes PP CONFIRMED FINDINGS `c9d31877…` (272-file source↔copy Soft SF agreement); Soft SF takes no further Soft SF action on that packet.

## Soft SF posture
tip Soft-SF LOCK tip_pre `7cddb188…` tip_touched NO. invent HOLD STANDS. No CERT. No content edits. No script exec. No external Gemini.

REPORTS ONLY.
