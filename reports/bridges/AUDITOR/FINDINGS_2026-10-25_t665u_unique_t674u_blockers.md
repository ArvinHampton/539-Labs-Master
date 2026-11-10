# FINDINGS — CONFIRM deduce_t665u_unique + deduce_t674u — 2026-10-25 00:32 CDT (America/Chicago)
Auditor: Residual-vs-Resonant. DEDUCED-only audit; no physics invented; PASS/FAIL unaltered; soft-SF only. Local only; NL untouched; order78 not started.

## Hash match (all MATCH)
| File | Claimed | Live |
|---|---|---|
| t665u_unique PREREG.md | 74ab81d0… | 74ab81d0bca7487ba331fd4d18b66749a9942d59f327f298b9bdcb10df9115d5 MATCH |
| t665u_unique RESULTS.md | 26220d2e… | 26220d2e9453bd688b235f1dead4d8d6031359dedc296d2db220c1f984e87db8 MATCH |
| t665u_unique SHA256SUMS | 5b7e7188… | 5b7e718849aa84c4dd64345eaa21e21788731d48681203c7dfc84b7bdc7ef873 MATCH |
| t674u PREREG.md | b824329c… | b824329c8dc3ac0da0ce1807451bd7b5695bf58f00daa21d460a1423da4f4d21 MATCH |
| t674u RESULTS.md | e67f2a0b… | e67f2a0bdf0e4fa5619c3a11f99f44a3c59781dfd82fa899d498d7fa4d4dada5 MATCH |
| t674u SHA256SUMS | 70d8f970… | 70d8f970c18b3e10c477ccee76caa53217e454e0b7328eaf85d815266b9f5109 MATCH |
| BRIDGE_C_35/STREAM_IDLE_LOCAL.md | bc405260… | bc405260b11f104082d29a86a700d220869ec871f491a67fb55778d4cf006aa2 MATCH |
| inventory_check/SHA256SUMS | bc39c86c… | bc39c86c8c2eede370f11703d5f87fe0f4c1f8c5e80efcb8923db8825c676f65 MATCH |

sha256sum -c: t665u_unique 3/3 OK; t674u 3/3 OK; inventory_check 26/26 OK.

## Checks
1. PREREG before RESULTS: t665u_unique PREREG mtime 00:29:18, RESULTS 00:30:06; t674u PREREG/RESULTS both 00:30:33 (sub-ms apart, RESULTS cites PREREG sha). PASS (t674u ordering by mtime weak — SF-T674-1).
2. Premise pins: 13eb50e6… live (3 copies identical). Text verified: L132 "That uniqueness is interpolation uniqueness"; L143–144 Identity B7 "Written data therefore exhibit non-uniqueness off-sample, not uniqueness"; L161–162 OB4 "Written data do not force uniqueness of residual_slash off the four samples"; L169 "does not make residual_slash unique as an abstract function". Remark85 bd271862… L12 matches. 7add2a9a L35 deg-3 "discrete data only" matches. a6a91a3b/7368b855/426ea3e0 prefixes match live files. 
3. PASS-NO-UNIQUE forced by Written: YES (B7/OB4 explicit). ≥2 competitors (deg-3 7add2a9a L35; Dual-split 13eb50e6 B7): CONFIRMED as Written-stated. Not free invent.
4. t674u B1 NOT FORCED, B2–B4 ABSENT-with-gap, B5 ABSENT (order72 RESULTS L12/L16 "T1–T4 ABSENT" verified). Bridge PARTIAL / READY NO / residual-C OPEN: not overclaimed.
5. order78 directory absent (not started). STREAM states CORE_FREEZE, no order78. SF-W7-3 fence declared.
6/7. Consistent with baseline 76cc1042… (uniqueness FAIL): PASS-NO-UNIQUE closes hunt as no-unique, NOT unique form found. "Unique form LOCKED: NO" stated.

## Soft SF (no PASS/FAIL change)
- SF-T665U-1: OB4 cited at L159; live text is L161–162 (L159 is a different statement). Citation off by 2–3 lines; content correct.
- SF-T665U-2: "31 files with Closure in path" not reproduced: Auditor counts 19 (residual_slash|residual_factor) or 88 (full RG pattern) by grep -rl. Fence count unverifiable; recommend recording exact command.
- SF-T665U-3: Note label "PASS-NO-UNIQUE" relabels prior ABSENT-with-gap; acceptable since OB4 explicit, but 13eb50e6 L167 scope (functions outside Pack+(S) not excluded) means no-unique holds w.r.t. Written corpus only.
- SF-T674-1: t674u PREREG/RESULTS same-second mtimes; prereg-first not independently demonstrable beyond sha citation.
- SF-T674-2: B2 supply item (iii) mentions W_7 images and g_7 pole — listed as supply need, not claim; fine, no invent.

## Open set
residual-C OPEN; B1 (Written off-sample functional constraint), B2 δ_W7≡0 ∀x, B3 sample-h table, B4 outer_*/X4 identity, B5 T1–T4 Written. Bridge PARTIAL; READY NO; order78 NOT started.

## Verdict
CONFIRM: PASS-NO-UNIQUE (t665u_unique) and all t674u blockers ABSENT-with-gap/NOT FORCED. Soft-SF 5. No blockers to confirmation.
