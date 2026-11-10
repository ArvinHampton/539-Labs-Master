# FINDINGS — t1052u outer_* O-3b Write + residual-C §1d insert — Auditor CONFIRM
Date: 2026-10-25 ~19:05 CDT (America/Chicago). Lane: Auditor. invent-ban ON; CORE_FREEZE; no order78; Empty #7–#9 HOLD; 4da09dec not revived. No draft/Write edits made.

## Verified inputs (sha256)
| Input | Expected | Observed |
|---|---|---|
| OWNER_WRITE_OUTER_STAR_t1052u_2026-10-25.md | e52446ff1be74cd22c62fec84e6bc398d0602e124f47c907e7631f9b8b99bc26 | MATCH |
| residual-c-field-WRITTEN_PREMISES_DRAFT.md | fcb3f00ca4842a535b1583b1f9a219a2624b93c9db47ba3cfb68a3c7701614ac | MATCH (sidecar .sha256 also fcb3f00c…) |
| Prior draft 9adb84fa6540b518b18943a54459d1388d65bfa823d78d08ba750d3eb57be7ab | — | NO backup file found in /workspace (no pre-t1052u copy); diff not possible. Cited in §1d header + t1049u FINDINGS + HASH_INTEGRITY. |
Prior context cited: FINDINGS 46e4e3bd… (menu 39c9a9a6…, formulas verbatim at HD e60cad9b…); FINDINGS b467bb54… (O-α defs ACCEPT, table EMPTY); Identity-gaps b28c5ffe…; t1049u FINDINGS 8e2488b4… (outer_* OPEN).

## Verdict: MATCH-with-SF

## 1. Formula check — MATCH
Write W-O1: outer_even=35m²+7m, outer_odd=35m²+42m+49/4 (m≥0) = O-α / HD e60cad9b L16–22 as recorded by 46e4e3bd… and b467bb54…. No new formula.

## 2. Table check — MATCH (all 16 rows)
Independent Fraction recompute m=0..15: all even and odd cells equal Write table exactly (e.g. m=0: 0, 49/4; m=7: 1764, 8085/4; m=15: 7980, 34069/4). k columns 2m / 2m+1 consistent.
HD: re-ran deduce_t761u_outer_written/scripts/outer_check.py → ALL_MATCH True vs 1bab65c4 listed values (even m=1..8, odd m=0..6) and |ledger_exp| k=0..11. Rows beyond listed range (even m≥9, odd m≥7) are formula-only (Write says so: "for m in listed range").

## 3. NOT O-X4 — CONFIRMED
Write and §1d both state ledger form only (O-2a), NOT O-X4, no ledger≡HD Cat A; X4 ABSENT.

## 4. Insert fidelity (§1d) — faithful to Write, SF on provenance
§1d lines 70–80 restate Write content verbatim-equivalent; header row L18 updated to mention outer_* table. No new physics introduced. Prior-backup absent → full-diff fidelity unverifiable (SF-1).

## 5. invent-ban / open items
invent-ban ON (L16). LOCK None (L14); P5 tag blank; residual_B1 OPEN; X4 ABSENT; G-A3 PAUSED. Bridge PARTIAL (L17); no READY YES claim found. Unchanged.

## 6. GATING outer_* — CLEARED (audit ref this FINDINGS)
O-3b table is Owner Written (t1052u), formula-consistent all rows, HD-consistent on listed range.

## Soft SF
- SF-1: no backup of prior 9adb84fa… → insert diff unverifiable; recommend saving pre-insert copies (pattern `.pre-…-<sha8>.md`).
- SF-2 (minor): "ALL_MATCH vs HD" covers only HD-listed range; m≥9 even / m≥7 odd are arithmetic extension, not HD-attested. Wording acceptable as-is.
- G-O1 carried: HD even list omits m=0 (outer_even(0)=0 via O-1a).
- No invent; no Cat A without ACCEPT; no Empty KEEP / 4da09dec; no Local/NL mix; no Bridge YES / δ≡0 / LOCK claim; no algebraic-under-geometric relabel; no O-X4 claim.

## Remains OPEN
LOCK; P5 `[[ to prove / accepted ]]`; residual_B1 value; X4; G-A3 PAUSED; ρ generator matrices; cusp rules; P4 blanks. Bridge PARTIAL; READY NO.

## HASH_INTEGRITY
Record this file's sha256 out-of-band (not embedded).
