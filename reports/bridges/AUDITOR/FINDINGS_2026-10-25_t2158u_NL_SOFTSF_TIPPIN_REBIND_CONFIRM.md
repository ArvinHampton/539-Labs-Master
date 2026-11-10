# Auditor FINDINGS — t2158u NL Soft SF tip-pin rebind CONFIRM (cite-only)
Date: 2026-10-25 ~21:58 CDT (America/Chicago). Mode: CONFIRM-only; no physics invented; tip not edited; no messages sent.

## Verdict: MATCH-with-SF

## Hash recompute (sha256sum)
| # | File | Claimed | Recomputed | Result |
|---|---|---|---|---|
| 1 | /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md (tip) | d0b1e3016182eab1522c5fa6b2743e7c8c48d5446d8b0e59b3acfdd61bb09851 | same | MATCH; tip_touched NO |
| 2 | /workspace/obs-bridge-NL-61Omega-photon-brane.md | 644c235cf4158d3c7392ead7cda51930e2adcd9da34422894993f8431d44873d | same | MATCH |
| 3 | claimed path `obs-bridge-NL-61Omega-photon-brane.md.pre-softsf-tippin-6f0f9a7a.md` | 6f0f9a7acb44a6ac7d0ff74241ecda2c7e9fe01e2c8aa7b464c45901208193db | path ABSENT; actual `/workspace/obs-bridge-NL-61Omega-photon-brane.pre-softsf-tippin-6f0f9a7a.md` = same hash | MATCH-with-SF (path label) |
| 4 | inventory_check/FINDINGS_NL_SOFTSF_TIPPIN_REBIND_t2156u_2026-10-25.md | 12def35f3f0e808c28259b63a002ded526d40f162d81db2885c5dbcb01b39337 | same | MATCH |
| 5 | inventory_check/ACK_NL_SOFTSF_TIPPIN_REBIND_t2156u_2026-10-25.md | d9332815f4c858269570411c4582d7a148a8976836b0a9e8a9edacc57636a3b7 | same | MATCH |

## Content checks
- Diff pre→live: changes only rows 31–38, line 40, and appended t2156u log (line 83). Cite-only. PASS.
- Rows 31–38 carry "tip Soft SF pin d0b1e301… (pre-pin d5f8b9d3…) untouched by NL". PASS.
- t2147u rows + line 40: "Auditor CONFIRM MATCH 77c6f643…"; no residual "pending" outside the log quote. PASS.
- Row 36: "ω ≠ Ω_11D per Write OP.3" label note. PASS.
- Sealed t2132u–t2153u NL packs: all recomputed hashes equal their .sha256 sidecars (t2139u/t2153u ACK sidecars use full-path labels, so `sha256sum -c` from dir warns; manual compare MATCH). t2153u ACK still cites d5f8b9d3… as history. PASS.
- No invent; Bridge PARTIAL / READY NO; Q7 KEEP. PASS.

## Soft SF
1. Claim 3 backup path wrong: `.md.pre-softsf-…` claimed; real file `obs-bridge-NL-61Omega-photon-brane.pre-softsf-tippin-6f0f9a7a.md` (hash matches).
2. (minor, pre-existing) t2139u/t2153u ACK .sha256 sidecars use repo-relative path labels, not basename.
- invent: NONE. tip_touched YES falsely: NONE. Tip Soft SF wrong pin: NONE (d0b1e301… correct).
