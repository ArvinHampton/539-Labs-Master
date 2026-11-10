# Auditor Soft SF CONFIRM — NL t222u tip Soft SF pin → ea4eb298 (2026-10-26 t1032u America/Chicago)
Verdict: **MATCH-with-SF** (CONFIRM-only; no physics, no tip/stub edits, no Owner scoring)

## Recomputed hashes
- Live tip residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (mtime 10:31:22 CDT) — **≠ ea4eb298… FAIL (tip race)**
- tip backup .pre-p5a-rewrite-ea4eb298.md = ea4eb2988138eb5a4bf8559da7841c5219c50029baa2190b504c288a09e8483f PASS (Owner P5A rewrite, OWNER_WRITE_P5A_REWRITE_GAMMA0_49_2026-10-26.md, 10:27; tip rewritten 10:31)
- Stub obs-bridge-NL-61Omega-photon-brane.md = 9c5a947b8028a291a65c3f16f8257f5410e89db662882184d9148507fb600035 PASS (10:16:08)
- Stub backup .pre-softsf-tippin-e8c6fccb.md = e8c6fccb41184785d3be40b9be9fd9b0c7003b49c99fa7eeb79ed070f11137b9 PASS
- NL FINDINGS inventory_check/FINDINGS_NL_SOFTSF_TIPPIN_REBIND_t222u_2026-10-26.md = d8082e6afa1daf57a85fc33b3f33c859789cb6f05b129e829e7325ceb7a8bcb0 PASS
- ACK inventory_check/ACK_NL_SOFTSF_TIPPIN_REBIND_t222u_2026-10-26.md = f9694fb4f6eac368507ae9fe1f694abbb7ed7393c4c8f1daa950695f428af7b3 PASS
- Cited Auditor FINDINGS_2026-10-26_t1016u_SOFTSF_TIP_SF1_1V_LABEL_CONFIRM.md = 837fe34e6691518fe9db85c90cc94e874a6cf3b1f4ac1643cc4d53490f91386d PASS; actual verdict MATCH (HASH_INTEGRITY)

## Diff backup e8c6fccb → live 9c5a947b
Rows 31–38 + t164u status line: tip pin e84a3a81… → ea4eb298… (e84a3a81 moved to pre-pins history); one t222u log line appended. No other changes. tip_touched NO by NL (scope: stub-only pin). No invent, no new physics.

## Soft SF flags
- SF1 tip race: NL pin (10:16) was correct at pin time, but Owner P5A rewrite moved live tip ea4eb298 → 7cddb188 at 10:31. ea4eb298 is now history; a fresh NL tip pin to 7cddb188 (after Auditor CONFIRM of the P5A rewrite) is needed. Not an NL fault.
- SF2 omit Auditor MATCH cite: stub/FINDINGS/ACK contain 0 references to 837fe34e…; they cite Owner t1788s8775 + MR1 0324b774/4656e09d/345e2620 only. No wrong verdict label exists in artifacts (MATCH-with-SF label appears only in the NL message, not in files) — label hygiene: correct label is MATCH.
- SF3 Components cite lag: NL says "Components HOLD (Owner Park)"; tip-era docs say "[[ components — Arvin ]] remains open (B-HOLD)". Compatible (no change invented) but wording differs; harmonize on next pin.
- Out-of-scope edits: none.

## Standing constraints
tip_touched NO (NL); Soft SF invent HOLD tip fill else; F3 CLOSED (cited); Components open/HOLD unchanged; packaging Owner-hold; Bridge PARTIAL / READY NO; Q7 KEEP; STOPPED KEEP.
