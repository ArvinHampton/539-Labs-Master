# FINDINGS — Auditor CONFIRM — t1145u NL pursue resolutions (A/B/C) — 2026-10-25 ~20:55 CDT (America/Chicago)
Scoring: CONFIRM-only. No physics invented. Residual-C tip not edited. No outbound messages.

## Hashes (verified on box)
- A Write `reports/OWNER_WRITE_NL_BLOCK_PURSUE_OPEN_t1145u_2026-10-25.md` 2352a5a986c0abf400838a386237be54c5ca3a32c6a0cb86ed5b0007c6665c91 — MATCH (mtime 20:47:07 CDT)
- B ACK `inventory_check/ACK_OWNER_WRITE_NL_BLOCK_PURSUE_OPEN_t1145u_2026-10-25.md` 9bd4406a4716895d95c0cf3c61ee55cd6b6c6bbe11bac606e7b2720094bb3df2 — MATCH; sidecar OK
- C FINDINGS `inventory_check/FINDINGS_NL_OPEN_QUEUE_RETAG_t1145u_2026-10-25.md` 9046ce8e32d924ad9ee1f2c50c3c9d32c1bdf79ab7ad15f0c92a8d73318121e1 — MATCH; sidecar OK
- Search script 2e2c0bf9… and hits dbee2555… — match A's citations; sidecars OK
- Prior NL deepen CONFIRM bbd69312… cited in A — consistent with HASH_INTEGRITY L408
- Stub `/workspace/obs-bridge-NL-61Omega-photon-brane.md` 64e17d5f19e2acc2cdafe6c438b19a11435f24946b21edab6ea478b470d355e4 (mtime 15:07 CDT) — untouched: YES
- Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` live 0677d02a10f298d0e84f41f6da876fe6ed4b886b92000ed70e9cec3be6173ca3 (mtime 20:47:47 CDT) ≠ expected LOCK 70c47a4c…. The change came from the MR2 §1k P-fgeom fold (same attribution as PR2 CONFIRM f0ede6c0… and Local Wave-4 CONFIRM 3cde8519…). A was written 20:47:07, 40 s before that, and cites 70c47a4c as pre/post. **Tip touched by NL: NO.**

## Checks
| Expect | Result |
|---|---|
| Tip untouched by NL | MATCH (with SF-1: the cited LOCK is stale; MR2 changed the tip) |
| Stub untouched | MATCH |
| Bridge PARTIAL / READY NO / not Cat A | MATCH (A, B, C) |
| No new mechanisms | MATCH — every row is ABSENT/OPEN/KEEP; no mechanism or coefficient added |
| Q4 / Q8 ABSENT-hold KEEP | MATCH (6 / 0 hits, with reasons) |
| H OPEN KEEP | MATCH |
| ψ OPEN KEEP | MATCH |
| Soft SF-W5 KEEP (decay = coherence envelope) | MATCH — Author note says off-diagonal envelope, Trρ=1 kept |
| ER=EPR/Φ(y) residual: the Φ(y)→ρ₊₋U coeff is ABSENT | MATCH |
| Pursue-resolve posture | MATCH — A quotes "pursuing resolutions to any problem stopping them"; content is a per-problem pursuit, with no "block" instruction |

## Soft SF
- SF-1: Tip LOCK 70c47a4c cited in A/B/C and in the brief is stale. Live tip is 0677d02a via MR2 §1k. NL is not at fault.
- SF-2: The filenames still say `BLOCK_PURSUE_OPEN`. A's line 2 explains why; the content pursues resolutions. Clerical only.
- SF-3 (note): Tip §1k now folds f_warp ≡ f_curv ≡ 1 into Ω_11D ≡ 1. A's Q8 row covers only f_*, friction factor, and f(Ω), and still cites Ω_11D≡1. It does not cite §1k. f_* stays ABSENT; no conflict.
- SF-P (pasted Grok blocks) is inherited, as A says.

## Verdict
- A: MATCH-with-SF (SF-1, SF-2, SF-3)
- B: MATCH-with-SF (SF-1, SF-2)
- C: MATCH-with-SF (SF-1)
- **Overall: MATCH-with-SF.** Bridge PARTIAL / READY NO / not Cat A. Tip untouched by NL: Y. Stub untouched: Y.
