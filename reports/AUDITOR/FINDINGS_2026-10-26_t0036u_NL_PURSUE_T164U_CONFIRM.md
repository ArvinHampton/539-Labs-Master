# AUDITOR FINDINGS — NL t164u pursue (non-packaging) CONFIRM
Time: 2026-10-26 ~00:36 CDT (America/Chicago). Mode: CONFIRM-only. Tip not edited.

## Hash recompute (sha256sum) — base NONLOCAL_QM_EH11D/inventory_check/
| # | File | Claimed | Recomputed | Result |
|---|---|---|---|---|
| 1 | FINDINGS_NL_OPEN_QUEUE_RETAG_t164u_2026-10-26.md | c40092693a3f41c70bd8e932ef79795c89cf1c571414e41b84eddd733940d238 | same | MATCH (.sha256 agrees) |
| 2 | FINDINGS_NL_PURSUE_RESOLUTIONS_t164u_2026-10-26.md | b417964a23428204fc17fb7e1eef12324d28103ee4f156f307ba2aa2bce41044 | same | MATCH (.sha256 agrees) |
| 3 | ACK_OWNER_WRITE_NL_PURSUE_RESOLUTIONS_t164u_2026-10-26.md | 960ec06cc48c3ff3f57b2cc71de01ecc93b0e1f7caace7930c71261c351e8418 | same | MATCH (.sha256 agrees) |
| 4 | /workspace/obs-bridge-NL-61Omega-photon-brane.md | 4099d93cb8e442049762f8f6d9637ee0c75d6afca914ca4228a8deda405f5fb2 | same | MATCH |
| 4b | backup .pre-pursue-t164u-535ccef7.md | 535ccef7… | 535ccef722267033f333d0600c4303b8c5672655dd7b4e200d7e6c99908c3c3f | MATCH |
| 5 | Live tip residual-c-field-WRITTEN_PREMISES_DRAFT.md | d88b4dae527d2eec9f1112427160130fbc12fcd7044bae151a7359efcd4b21d6 | same | MATCH (post MR2 §1o) |

## Content checks
- Cite-only; no numbers invented (4 items kept ABSENT; re-search empty): PASS
- No new OWNER_WRITE (ACK: "No OWNER_WRITE issued this pass"): PASS
- Packaging f_*/Ω/ω OWNER-HOLD, not closed: PASS
- Q7 proof-gated KEEP; STOPPED Q9/Q14–16 KEEP: PASS
- Stub diff vs backup: only t164u status line replaced + one history line appended; cite-only: PASS
- NL tip_touched NO (tip moved externally by MR2 §1o, not by NL): PASS

## Soft SF
- invent: NONE
- tip_touched YES: NONE
- packaging invent: NONE
- tip stale pin: YES — RETAG, FINDINGS, ACK and stub all pin tip LOCK d0b1e301… while live tip is d88b4dae… (external §1o fold). Soft SF only; not a FAIL.

## Verdict: MATCH-with-SF
