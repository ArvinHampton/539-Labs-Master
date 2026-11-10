# FINDINGS — MR1 COOK free-pursue: on-mesh vars after N6+N36 ν=num/140 reclass (2026-10-26)
Executor: Math Research 1 · Soft-SF Write-only · OW COOK 08c8cdb9f851f85add943c18705a77c4de899464e29c9389e1663a42dcc05411 · proof OR named gap · Cat-A invent NONE · tip untouched · no Eigen contact (no eigen-* file opened/read; only sha256 of paths) · CF980 runner NOT run

## STATUS: PARTIAL — 0 new fills (nothing missed is fillable); inventory complete; named gaps below.

## Live hashes (verified 17:48 CDT)
| artifact | live sha256 | vs brief |
|---|---|---|
| tip residual-c-field-WRITTEN_PREMISES_DRAFT.md | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | MATCH (tip_pre=tip_end) |
| COOK OW | 08c8cdb9f851f85add943c18705a77c4de899464e29c9389e1663a42dcc05411 | MATCH |
| MODP CSV operative | 453d3c4fc1607465ec37d67c9c13a4963256eaa84fddacee7637508ad3e6ecfd | MATCH (not edited) |
| SCHEDULE TORD | f7ec76eff6b8888039e65cac8babaecd47285699fedca6577ca20df3ca2a6ea5 | MATCH (not edited) |
| prior FINDINGS PURSUE_MISSED_VARS | 67a1a1a3cf3c92c92cf7a242ffbc5d652df43494e802d6c3bde753a01664357f | MATCH |

## 1. Inventory (all rows on_mesh_N18=YES)
MODP CSV 14 data rows = schedule 14 rows, identical (family, exponent) key set:
- N36 ν ∈ {0,1,4,9,14,16,21,25}: 0 VACUOUS; others FILLED-MODP (p=7840981).
- N6 ν ∈ {1,9,29,81,109,121}: all FILLED-MODP (p=1027606441).
- OPEN / blank status / blank simpson_weight / blank coefficient: **NONE** in either operative CSV.
- ν/140 check: every N36 seed exponent equals ν/140 (c31 1/140, c9 4/140=1/35, c34 9/140, c20 14/140=1/10, c6 16/140=4/35, c28 21/140=3/20, c25 25/140=5/28); N6 a0..a5 e{1,9,29,81,109,121}/140. **No seed exponent /140 from the N6/N36 promote FINDINGS (27b1c5e8…, f57ea4b5…) is on-mesh-but-unfilled.**

## 2. Candidates examined → result
| # | candidate | result |
|---|---|---|
| C1 | further basis columns c*_e*/140 beyond the 7 N36 / 6 N6 seeds (true "missed vars") | **GAP-E (Eigen-only)**: sole on-disk basis copies are grok-batches/eigen-n36-503/n36_basis_q18_inf_modp.csv (e707cc96…) and grok-batches/eigen-q89-basis/rhos/q89_basis_q18_modp.csv (3fb6519f…). Non-eigen extracts exist only for N6 D1 (N6_D1_nu_columns_modp.csv) and N36 ν21/25 (56e9be7d…). No prior Soft-SF FINDINGS extracts other columns. Needs Owner authorize-read. Also no Written rule saying which further components are residual-C ν-cells (identification gap G3a of 67a1a1a3…). |
| C2 | N36 ν21,25 notes incomplete: N36 side CSV w1_sha/basis_sha = NA-HOLD | **GAP-N1**: provenance chain for 56e9be7d… to basis e707cc96… not stamped; verification requires eigen read (blocked). Filled value stands, HOLD CF980. |
| C3 | ext rows ν>18 (N36 21,25; N6 29,81,109,121) carry simpson_weight=4 / fill_tier=1-odd-w4 in operative CSV, but GA1 annotation CSV (mr1-n6-modp-q121-d1) has fill_tier=ext-write, simpson_weight BLANK | **GAP-GA1 (semantic inconsistency)**: Simpson weights/tiers are defined only on the N≤18 Simpson mesh (143080bc… GA1). Weight 4 for ν>18 is not proved by any Written rule; the reclass makes them on-mesh-by-Write but does not define a Simpson weight. Not edited (needs Owner Write). |
| C4 | N36 GA1 annotation still says OPEN for ν21,25 | stale annotation vs operative FILLED-MODP (post f57ea4b5…). Named stale-pointer only; no math gap. |
| C5 | N6 ν1,9 notes lack HOLD-CF980 stamp present on 29..121 | notes-only asymmetry; all mod-p fills HOLD for CF980 CERT anyway per brief. |
| C6 | N36 lane q^18 injectivity | **GAP G1** (unchanged): no CERT of q^18-truncation injectivity on 503-block; Lemma D1 determination applies over F_p only on N6 89-block. |

## 3. Proof notes
- Inventory completeness: by direct enumeration of both CSVs (14 rows each, key sets equal); a row is a fill candidate iff status∉{FILLED-MODP,VACUOUS} or a required field blank — none satisfy. QED.
- No char-0 asserted; no tip fold; no CSV mutated; all FILLED-MODP remain HOLD for CF980 CERT.

## Rec A
Owner Write authorizing a **read-only** column-header + named-column extraction from eigen-n36-503/n36_basis_q18_inf_modp.csv (e707cc96…) and eigen-q89-basis/rhos/q89_basis_q18_modp.csv (3fb6519f…), to (i) list all c*_e*/140 columns with e·140 ∈ on-mesh set and stamp w1/basis provenance for N36 ν21/25 (closes GAP-N1, scopes C1), plus a separate Owner Write fixing Simpson weight/tier semantics for ν>18 rows (GAP-GA1: either "ext-write, weight blank" or a proved weight rule).
