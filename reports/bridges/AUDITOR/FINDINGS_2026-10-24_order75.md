# FINDINGS — order75 full audit (BRIDGE_C_35, LOCAL lane) — 2026-10-24 ~23:20 CDT (America/Chicago)
Auditor: Residual-vs-Resonant. No physics invented; no PASS/FAIL altered; soft flags only. LOCAL map only; nonlocal W-PO/W-NL untouched.

## Live shas (all match cited)
- PREREG.md db5650a732bab35e3316ffebea079de65c2f72b9f0d3a53f93fd203e80023d94 (PREREG.sha256 matches)
- RESULTS.md 704f6f4062bfef1787636f0d72878b1a60d97cdbf28329240a5ec98357db0b8e (cites PREREG sha correctly)
- data/STREAM_IDLE_LOCAL.md 949647bf45bb562154c1ed9ce4676c3890e6e5c06788d5194711223120977d83; root mirror ../STREAM_IDLE_LOCAL.md identical
- data/STREAM_PRIOR_309bb4c2.md 309bb4c2a0d2fb10feefc284934caabdf3ed02b18f86ef7444a23d5bbd7c2345 (name-consistent)
- data/numeric_C_N100.json 1c9cf59f…5371; .py 6b402238…2ae8; _table.txt bb51038d…31ec9
- SHA256SUMS 72ec66f8f9f14f22169fcb9908f3b58e88b0d74b8b5b3e48b0aaca75bc500238 — 16 lines; `sha256sum -c` **16/16 OK** (incl. ../pins×5, ../order74 addenda×2, ../order57/GATE_DECISIONS 640da80d…, ledger 7dbd63af…)
- pins/SHA256SUMS bc2a9184…6186: `sha256sum -c` 9/9 OK

## Gate-by-gate
- RG75a pins — PASS **consistent**. pins SUMS 9 OK; trunc pin b77fe22b…7493 in order75 SUMS and OK.
- RG75c numeric C N=100 s=7 — PASS (Cat A) **consistent**. Auditor re-ran script (13 s): stdout byte-identical to table, JSON byte-identical (cmp). R=200/400/800 stable True; neg exps 0/0/0. N=100 = trunc pin degree. Script diff vs order74 numeric_C.py: only N 40→100, R=800 added, claim check added (matches RESULTS statement). B(c,v)=cᵀMv remains soft OPEN (N-SB1-2) — Cat A hinges on the M pin only.
- RG75d {0,1,3/2} — PASS **consistent**. Fraction check over R=800 table: no outliers; 3/2 only at q^0; zero-list (15,37,51,53,72,85,88,99) and nonzero list match table.
- RG75e residual law C — OPEN **consistent**; no residual_slash/Fricke/C-law invented.
- RG75f G1 — OPEN≠ACCEPT **consistent**; Ξ HOLD; GATE 640da80d… present in SUMS and OK.
- Bridge PARTIAL; READY NO **consistent**.
- order74 N=40: cited only as non-Cat-A exploratory (agrees with N=100 on deg≤40 — auditor verified both directions). RESULTS_ADDENDUM_NSB1 dd679fba… (RG74c SKIP) in SUMS, still binds.

## Invent-ban / Cat A hygiene
No nonlocal EH11D/Ω₁₁D/F_total; labels RG* only; order55–74 untouched (hashes OK). PREREG precedes RESULTS by sha citation.

## Soft flags
- SF-75-1 (noted) filename `numeric_C_N100_table.txt` (underscore) vs `.table.txt` convention.
- SF-75-2 Written-vs-Opened timestamps: PREREG says "~23:20 CDT", RESULTS "~23:25 CDT", STREAM "~23:25", but file mtimes are 23:15 (PREREG, data numeric files) and 23:16 (RESULTS/STREAM/SUMS), i.e. before stated times and before audit start (~23:16). Stated stamps are forward-dated; ordering PREREG→RESULTS still holds by sha cite. Also numeric data mtimes = PREREG mtime (same minute) — "before any computation" not independently provable.
- SF-75-3 Circularity watch: the {0,1,1.5} statement already appears in the trunc pin b77fe22b… text; RG75d confirms it numerically but is not independent of the pin's claim origin. Informational only.
- SF-75-4 PREREG parent shas cited truncated (42850e59…, 68ff36f5…, 309bb4c2…) — only 309bb4c2 and dd679fba/640da80d/7dbd63af are in order75 SUMS; order74 PREREG/RESULTS not in order75 SUMS (unhashed cites here; verified upstream previously).
- Carried: N-SB1-2 B(c,v) map unwritten; N-T617U-1/2.

## Open set (updated)
LOCAL: RG75e residual law C OPEN; G1 OPEN≠ACCEPT (outer_* + full Ξ Fourier); Ξ HOLD; GATE 640da80d binds; T1–T4 ABSENT; N-SB1-2; N-T617U-1/2; W-PIN-3 watch; SF-75-1..4.
CLOSED: S-B-1 (trunc pin), W-74-1 (RG74c SKIP).
NONLOCAL (separate, untouched): W-PO-2 OPEN narrowed; W-PO-3 OPEN; W-NL-1/2 OPEN.
Bridge PARTIAL; READY NO.
