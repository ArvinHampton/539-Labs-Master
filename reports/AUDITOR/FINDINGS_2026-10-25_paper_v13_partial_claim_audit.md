# AUDITOR FINDINGS — Paper v13 PARTIAL claim audit (sec:partial13)
Timestamp: 2026-10-25 13:37 CDT
Lock: Residual-vs-Resonant. No physics invented; no PASS/FAIL altered; paper not edited.

## Verdict: MATCH-with-SF (soft only)

## PDF
RTA_FOUNDATION_BOUND_v13.pdf sha256 0c59814aabfe88c2c63f04fbcca0fe905422a36e5b4fa71f592251261c06bbe7 — VERIFIED (matches claim).
pdftotext: sec:partial13 heading "Author-ACCEPT inventory" present; abstract (front_v13.tex l.25) rendered.

## Inclusion
main_v13.tex:47 \input{partIII_partial_v13.tex}; front_v13.tex:25 abstract sentence cites Section~\ref{sec:partial13}.

## Claim map (partIII_partial_v13.tex)
- l.2 "status inventory, not a new set of proofs"; invent-ban, CORE_FREEZE, no order-78 — MATCH (no proofs/equations in section).
- l.6 AW-α Ξ aac04151 — MATCH Cat A.
- l.7 O-α outer_* b467bb54 — MATCH.
- l.8 PB-α c26b5f72 — MATCH.
- l.9 E-α ε→0/W7/mixed 0aaec40d — MATCH.
- l.10 NL A1–A12 723f02a0 — MATCH (NL-side; no joint Local↔NL claim made anywhere).
- l.11 G-A1c 7e20e84c, G-R2 2b959003, B3-α b96ff7bd, T-α 5f5f2832 — MATCH.
- l.11 G-A1b b34aebe6, T-γ (under 5f5f2832), S-B1' 437d4571 "PARTIAL", NL W-PO-2/3 29ebbdd8 — see SF-1.
- l.16 G-A3 595b85d5 catalogue-only, G-α KEEP PAUSED, empty h-table, 4da09dec rejected/not used — MATCH (not revived).
- l.17 h_res^high b6788ae1 catalogue-only, M2=0, H-α KEEP — MATCH.
- l.18 X4 ABSENT-with-gap 2bb870b4, not accepted — MATCH.
- l.21 "Bridge: PARTIAL. READY: NO. Residual question for C: OPEN ... G-A3 PAUSED" — MATCH.
- l.23–25 remark: does not force residual smallness / settle op:xi — MATCH (no δ≡0, no Abel theorem).
- front l.25: "Bridge link remains partial: no readiness claim ... residual question for C remains open ... catalogue-only entries, not theorems" — MATCH.
- PDF grep: no Bridge YES / READY YES / δ≡0 / order78 / joint Cat A wording. ("Abel step/summation" at Lemma 8.9 is pre-existing Part I analysis, not new to partial13.)

## Soft SF list
- SF-1 (soft, citation scope): l.11 "Only the following are Category A" enumerates items outside the LOCKED Cat A list supplied for this audit: "G-A1b dual-split OUT (b34aebe6…)", "tunnel T-α and T-γ (5f5f2832…)" (lock is T-α KEEP only), "revised S-B1′ ... PARTIAL (437d4571…)", "NL W-PO-2 CLOSED and W-PO-3 FINISHED (29ebbdd8…)". Hashes appear in prior Auditor records, but not confirmed Cat A under this audit's lock; S-B1′ "PARTIAL" inside a Cat A list is internally ambiguous. Suggest author either restrict l.11 to the LOCKED list or relabel these as "earlier records (see FINDINGS)". Not a FAIL; no overclaim of Bridge/READY/δ.
No other SF.

## What stands
Local Cat A: AW-α, O-α, PB-α, E-α; NL A1–A12 (NL-side only); G-A1c R-UQ0; G-R2 R-NV0; B3-α KEEP; T-α KEEP.
Bridge PARTIAL. READY NO. residual-C OPEN. G-A3 PAUSED. X4 ABSENT. H-α KEEP (M2=0). No order78. No joint Local↔NL Cat A.
