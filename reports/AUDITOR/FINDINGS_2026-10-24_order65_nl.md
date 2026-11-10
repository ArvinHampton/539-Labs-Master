# FINDINGS 2026-10-24 — order65 + NONLOCAL ledger pass (Auditor)
Window: 22:19–22:22 CDT (America/Chicago). Read-only on all sources. No PASS/FAIL altered. Source tags: PAPER = corpus pdf/tex/txt; CHAT = agent/coordinator notes.

## A) order65 (PDF sweep, quote-only): COMPLETE, hashes OK, 1 WARNING
- Hashes: PREREG.sha256 OK (b80ee00f…5b6); SHA256SUMS 3/3 OK. mtime PREREG 22:19:13 < RESULTS 22:19:25. No scripts/data (quote-only; RG47f-bis SKIP, consistent with PREREG). No PASS claimed; no invented formula.
- Quotes verified (PAPER): rev9.2 p1 "signature-(1, 1) Zwegers-type indefinite theta series", p7 "holomorphic part of a Zwegers indefinite theta function [13]", p13 "signature-(1, 1) indefinite theta", p31 "The modular completion of 12 q c0 ϑ is"; Clean_v2 p37 "…by citation (Zwegers [18], Cor. 2.9).", p67 Cor. 2.9 row. All exact. Item 2 "FOUND generic / not A(2)-tied / not READY" is consistent.
- **W-65-1 (WARNING) — path BRIDGE_C_35/order65/RESULTS.md, Item 1 & Item 3.** Claim: "0 hits in all 65 extracted PDFs" and "`rho_lab|ρ_lab|ρlab` → 0 hits anywhere". Evidence: pdftotext of heavy-daily/2026-10-19-Bridge-C-Clean-v2/Bridge_C_Clean_v2.pdf has 9 `ρlab` hits (e.g. text lines 4230 "ρlab : S 7→ Slab", 4233 "Theorem 18.2 (Weil realisation of the label representation). (i) ρlab ∼", 4309 Remark 18.4, 4355 "Corollary 18.6 (The residual law in K3 terms). ρlab ∼", 4535 "ρ = ρlab is the 140-label representation"); Bridge_C_Clean.pdf also 9 hits. (Item-1 terms: 0 hits, confirmed.) Not shown that any of these is a corner/EVEN ↔ ρ_lab pairing, so ABSENT-of-pairing may still hold, but the "0 hits anywhere" coverage claim is false. Fix: additive note in RESULTS listing the Clean/Clean_v2 ρlab hits (Thm 18.2, Rem 18.4, Cor 18.6, §19 s=7) with page numbers, and an explicit quote-only judgment whether any pairs corner/EVEN with ρlab; re-hash SUMS. Item 3 stays OPEN; RG47f-bis SKIP unaffected unless a written pairing formula is found there.
- **N-65-1 (note):** RESULTS says heavy-daily "21 extracted"; `find reports/heavy-daily -name '*.pdf'` gives 20 (incl. zwegers + 3 refs). Fix: correct count or name the 21st file.
- N-65-2 (note): prep file absence is disclosed. OK.

## B) GATE_DECISIONS header (N-H3): RESOLVED
order57/GATE_DECISIONS.md:2 now reads "from Physicist and Mathematician (coordinator)"; "Auditor" no longer appears in attribution. GATE_DECISIONS.sha256 OK (675fc9e7…1822), file and hash both 22:17:52.

## C) W-64 re-check: still OPEN (narrowed)
- order64/RESULTS.md:5 and :41 and GATE addendum now say "Physicist ruling", and :41 states explanation is not asserted by order64. Good.
- Remaining: headline tags still read "CLOSED-EXPLAINED (order7)" (order64/RESULTS.md:4; GATE_DECISIONS order64 addendum line 1), and RESULTS:6 "fails the w=1 pairing as order7 forces" — this still reads as order7 itself explaining RG47e, which order63/RESULTS.md:12 says it does not (law is on 105-dim M, not ρ_lab). Fix: retag as "CLOSED-EXPLAINED (Physicist ruling; basis order7 Cat A, M² = 35P)", additive line; re-hash. Close on landing. RG47e FAIL stands. order64 SUMS 4/4 + PREREG OK.

## D) W-C3 / C10: still OPEN
MAPS_CANDIDATES/RESULTS.md mtime 16:56:59; line 8 still "C3 … **OPEN**"; no C10 superseding row. Local additive rows not landed.

## E) NONLOCAL
### CONTRADICTION_LEDGER.md (6 entries): quotes VERIFIED, 1 note
- All 19 cited path:line quotes checked (N:96,98,99,100,102; G:125–126,129; L:20,21,33,109,116; C:33,96,100; T:18,46,53): exact. Count 6 (4 hard/2 soft) matches table. Self-label "Cat A documentation of written disagreement only" is accurate: it documents PAPER contradictions, unlocks nothing, Cat B (539.9 s, β_PBH) flagged per row. No invent.
- N-NL-CL1 (note): CL6 arithmetic is the ledger's own (539.9/n approximations) — labeled "approx only"; fine, but it's auditor-style analysis, not a quote. Tag as derived-by-agent.
- CL1 "h_c→Ω_GW conversion not done" disclosed. OK.
### CODEX_FTOTAL_STRUCTURE.md: OK, 1 note
- Formula source T:44–69 (PAPER); "61 punctures" (T:75,96) and "/10" present in source. No numerics, no PREREG, ABSENT items stated. "≥19 unvalued" is an agent count (structure). N-NL-FT1 (note): dimensional-homogeneity remark is agent analysis, not PAPER; tag it as such.
### STREAM_IDLE_WRITTEN: **ABSENT** on disk (find over /workspace/quantum-comp). Coordinator FYI claims it (CHAT). N-NL-SI (note): file not present; cannot audit.
### MILESTONE_2026-10-24d.md: consistent with standing rule — header "all WRITTEN-CHAT, not paper Cat A"; NL1 OPEN; k(N) OPEN. N-NL-d (note): the line "Status (auditor relabel …)" attributes the relabel to the Auditor; Auditor recommended it in findings but did not edit sources. Fix: "relabel per Auditor finding W-NL-1 (applied by Non Local Path)".
### MILESTONE_2026-10-24e.md: EH-JX1 PASS — prereg dir exists (prereg/EH_JX1_20261024/{PREREG.md,run.py,result.log}). "a=1/24 locked" labeled DECLARED-LOCK; fork OPEN. **W-NL-3 (WARNING):** milestone e lacks the CHAT tag that d carries; "PASS" here is a bookkeeping/lock-consistency test on WRITTEN-CHAT conventions (Φ/flux→k), not PAPER. Fix: add "(WRITTEN-CHAT; does not clear NL1)" line. Hash check of EH_JX1 not performed this pass (next slice).
- NL1: **stays OPEN**. Nothing here is PAPER evidence for Ω/Vol(S6)/k11(N).

## Counts this pass
Blockers 0 / Warnings 2 (W-65-1, W-NL-3) / Notes 6 (N-65-1, N-65-2, N-NL-CL1, N-NL-FT1, N-NL-SI, N-NL-d). Resolved: N-H3.
