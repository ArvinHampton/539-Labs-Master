# Auditor FINDINGS: NL Soft SF tip-pin rebind t170u CONFIRM
Date: 2026-10-26 ~00:41 CDT (America/Chicago). Mode: CONFIRM only. No physics invented. Tip not edited. No messages sent.
Addresses: Soft SF in prior Auditor MATCH-with-SF f0d16316bebbcd36cbaad012462baf5d01da56f4dda3017913b3c3338c154eae (FINDINGS_2026-10-26_t0036u_NL_PURSUE_T164U_CONFIRM.md, recomputed; matches).

## Verdict: MATCH-with-SF

## Hash recompute (sha256sum)
| # | Item | Claimed | Recomputed | Result |
|---|---|---|---|---|
| 1 | Live tip residual-c-field-WRITTEN_PREMISES_DRAFT.md | 64d23f39975cfafc91582d86c192612544ddf11aebe7dddb7a359ef5354f47ff | same | MATCH; tip_touched NO |
| 2 | Stub obs-bridge-NL-61Omega-photon-brane.md | d8ebfc45aaa0d1f11e6742157717f25f711362cdd90f4d1c0f754a1b8f55a4e0 | same | MATCH |
| 2b | Backup .pre-softsf-tippin-4099d93c.md | 4099d93cb8e442049762f8f6d9637ee0c75d6afca914ca4228a8deda405f5fb2 | same | MATCH (= pre-stub) |
| 5 | NL FINDINGS t170u | 779faf6170e63f8cc54a78cf3600deb712310925622618c26fb6ec6e7cbf3838 | same | MATCH |
| 6 | NL ACK t170u | 09e75ff463d33d063565e141f4363b270c86d5130c4ab408d686fe0a672fb8c4 | same | MATCH |
| 7 | Prior CONFIRM | f0d16316bebbcd36cbaad012462baf5d01da56f4dda3017913b3c3338c154eae | same | MATCH |

## Claim 3: stub diff (backup → live)
- Only these lines changed: rows 31–38 and t164u status line 76; t170u log line 86 appended. Cite-only.
- Rows 31–38 each cite 64d23f39… with pre-pins d88b4dae… / d0b1e301… / d5f8b9d3… labeled history. MATCH.
- Line 76 (t164u status) cites 64d23f39… + d88b4dae… / d0b1e301…; it does not list d5f8b9d3… (see SF-1).

## Claim 4: sealed packs t2132u–t164u
- sha256sum -c on every t2132u/t2146u/t2147u/t2156u/t2158u/t2160u/t164u FINDINGS/ACK .sha256: all OK. t164u RETAG c4009269…, FINDINGS b417964a…, ACK 960ec06c… unchanged. Stale d0b1e301… cites left as history. MATCH.

## Content checks
- Cite-only: YES. Packaging f_*/Ω/ω Owner-hold: YES. Q7 KEEP: YES. STOPPED KEEP: YES. Bridge PARTIAL / READY NO: YES.
- Soft SF red flags: invent NONE; tip_touched YES NONE; tip Soft SF race NONE (tip sha matches before and after); packaging closed invent NONE; content beyond tip-pin NONE.

## Soft SF (non-blocking)
- SF-1: Line 76 (t164u status) pre-pin history lists d88b4dae… / d0b1e301… but leaves out d5f8b9d3… (rows 31–38 include it). Cosmetic.
- SF-2: The 2 t170u .sha256 files use paths relative to /workspace (quantum-comp/...). They verify from /workspace, but not from inventory_check/. Cosmetic.
- SF-3: inventory_check/SHA256SUMS has stale or unreadable entries (STREAM_IDLE_WRITTEN.md FAILED; OWNER_WRITE_* entries not found in that directory). These came before t170u. Hygiene only.
